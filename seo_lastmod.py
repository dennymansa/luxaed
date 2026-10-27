"""Persist sitemap dates for meaningful page changes, not every deployment."""
import hashlib
import json
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
STATE = ROOT / "seo_page_state.json"


class ContentFingerprint(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.main = False
        self.title = False
        self.skip = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag in ("script", "style"):
            self.skip = True
        if tag == "main":
            self.main = True
        if tag == "title":
            self.title = True
        if tag == "meta" and values.get("name") in ("description", "robots"):
            self.parts.append(str(sorted(attrs)))
        if tag == "link" and values.get("rel") in ("canonical", "alternate"):
            self.parts.append(str(sorted(attrs)))
        if self.main and not self.skip:
            meaningful = {k: v for k, v in attrs if k in (
                "href", "src", "srcset", "alt", "action", "type", "name", "value")}
            self.parts.append(tag + str(sorted(meaningful.items())))

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = False
        if tag == "main":
            self.main = False
        if tag == "title":
            self.title = False

    def handle_data(self, data):
        if (self.main or self.title) and not self.skip:
            text = " ".join(data.split())
            if text:
                self.parts.append(text)


def fingerprint(source):
    parser = ContentFingerprint()
    parser.feed(source)
    if not parser.parts:
        raise ValueError("Cannot fingerprint an empty page")
    return hashlib.sha256("\n".join(parser.parts).encode()).hexdigest()


def update_dates(paths, today=None):
    today = today or date.today().isoformat()
    previous = json.loads(STATE.read_text()) if STATE.exists() else {}
    # Preserve the published dates on first migration. New URLs use today's date.
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    published = {}
    sitemap = ROOT / "sitemap.xml"
    if sitemap.exists():
        for node in ET.parse(sitemap).getroot().findall("s:url", ns):
            url = node.findtext("s:loc", namespaces=ns)
            lastmod = node.findtext("s:lastmod", namespaces=ns)
            if url and lastmod:
                from urllib.parse import urlsplit
                published[urlsplit(url).path] = lastmod
    current = {}
    for path in paths:
        digest = fingerprint((ROOT / path.strip("/") / "index.html").read_text())
        old = previous.get(path)
        if old and old["digest"] == digest:
            lastmod = old["lastmod"]
        elif old:
            lastmod = today
        else:
            lastmod = published.get(path, today)
        current[path] = {"digest": digest, "lastmod": lastmod}
    STATE.write_text(json.dumps(current, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    return {path: item["lastmod"] for path, item in current.items()}
