#!/usr/bin/env python3
# Generate sitemap.xml from the PAGES map in build_pages, WITH hreflang alternates
# (xhtml:link) so Google pairs the et/ru/en versions of every page. Run in the build.
import io
from build_pages import PAGES, DOMAIN

LASTMOD = "2026-07-16"  # bump on meaningful content or URL changes

# Priority by page role, independent of how many ET-only service rows exist.
def prio(row):
    et = row.get("et", "")
    if et == "/": return "1.0"
    if et.startswith("/aiad/") or et in ("/varavad/", "/aia-remont/"): return "0.8"
    if et in ("/meist/", "/kkk/"): return "0.6"
    return "0.4"

def alts_xml(row):
    required = {"et", "ru", "en"}
    if set(row) != required:
        raise RuntimeError(f"Incomplete hreflang row: {row}")
    L = [(lang, row[lang]) for lang in ("et", "ru", "en")]
    L.append(("x-default", row["et"]))
    return "".join(f'<xhtml:link rel="alternate" hreflang="{lang}" href="{DOMAIN}{p}"/>' for lang, p in L)

out = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
if len(PAGES) != 13:
    raise RuntimeError(f"Expected 13 translated page groups, got {len(PAGES)}")

for row in PAGES:
    p = prio(row)
    alts = alts_xml(row)
    for lang in ("et", "ru", "en"):
        loc = DOMAIN + row[lang]
        out.append(f'  <url><loc>{loc}</loc><lastmod>{LASTMOD}</lastmod><priority>{p}</priority>{alts}</url>')
out.append('</urlset>')
io.open("sitemap.xml", "w", encoding="utf-8").write("\n".join(out) + "\n")
url_count = sum(len(row) for row in PAGES)
if url_count != 39:
    raise RuntimeError(f"Expected 39 sitemap URLs, got {url_count}")
print(f"sitemap.xml: {url_count} urls, lastmod {LASTMOD}, complete hreflang alternates added")
