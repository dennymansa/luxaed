#!/usr/bin/env python3
"""Hard build gate for LuxAed's translated static site."""
from collections import Counter
import json
import os
import re
import xml.etree.ElementTree as ET

from build_pages import DOMAIN, LANGS, PAGES, SOCIAL_IMAGE
from service_catalog import SERVICE_MATRIX, service_paths

ROOT = os.path.dirname(os.path.abspath(__file__))
OLD_CANONICALS = ("/ru/zabory/3d-paneli/", "/en/fences/metal/")


def fail(message):
    raise RuntimeError(message)


def page_file(path):
    return os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")


def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def one(pattern, text, label):
    matches = re.findall(pattern, text, flags=re.DOTALL | re.IGNORECASE)
    if len(matches) != 1:
        fail(f"{label}: expected exactly one match, got {len(matches)}")
    return matches[0]


def json_ld(html, path):
    blocks = re.findall(
        r'<script\s+type="application/ld\+json"[^>]*>(.*?)</script>', html,
        flags=re.DOTALL | re.IGNORECASE,
    )
    parsed = []
    for index, block in enumerate(blocks, 1):
        try:
            parsed.append(json.loads(block))
        except json.JSONDecodeError as exc:
            fail(f"{path}: invalid JSON-LD block {index}: {exc}")
    return parsed


def jpeg_dimensions(path):
    """Read JPEG dimensions without adding an image-library build dependency."""
    sof_markers = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                   0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}
    with open(path, "rb") as handle:
        if handle.read(2) != b"\xff\xd8":
            fail(f"{path}: social image is not a JPEG")
        while True:
            byte = handle.read(1)
            if not byte:
                fail(f"{path}: JPEG dimensions were not found")
            if byte != b"\xff":
                continue
            marker = handle.read(1)
            while marker == b"\xff":
                marker = handle.read(1)
            if not marker:
                fail(f"{path}: truncated JPEG marker")
            marker_value = marker[0]
            if marker_value in (0xD8, 0xD9):
                continue
            length_bytes = handle.read(2)
            if len(length_bytes) != 2:
                fail(f"{path}: truncated JPEG segment")
            length = int.from_bytes(length_bytes, "big")
            if length < 2:
                fail(f"{path}: invalid JPEG segment length")
            if marker_value in sof_markers:
                frame = handle.read(length - 2)
                if len(frame) < 5:
                    fail(f"{path}: truncated JPEG frame")
                return int.from_bytes(frame[3:5], "big"), int.from_bytes(frame[1:3], "big")
            handle.seek(length - 2, os.SEEK_CUR)


def schema_by_type(blocks, schema_type):
    return [block for block in blocks if block.get("@type") == schema_type]


def validate_catalog():
    if len(SERVICE_MATRIX) != 8:
        fail(f"Expected 8 services, got {len(SERVICE_MATRIX)}")
    if len(PAGES) != 13 or any(set(row) != set(LANGS) for row in PAGES):
        fail("Page matrix must contain 13 complete ET/RU/EN rows")
    all_paths = [row[lang] for row in PAGES for lang in LANGS]
    if len(all_paths) != 39 or len(set(all_paths)) != 39:
        fail("Page matrix must contain 39 unique URLs")


def validate_social_asset():
    asset = os.path.join(ROOT, SOCIAL_IMAGE.lstrip("/"))
    if not os.path.isfile(asset):
        fail(f"Missing social image: {SOCIAL_IMAGE}")
    if jpeg_dimensions(asset) != (1200, 630):
        fail(f"{SOCIAL_IMAGE}: expected 1200x630 JPEG")


def validate_page(row, lang):
    path = row[lang]
    file_path = page_file(path)
    if not os.path.isfile(file_path):
        fail(f"Missing generated page: {path}")
    html = read(file_path)
    canonical = one(r'<link\s+rel="canonical"\s+href="([^"]+)"', html, f"{path} canonical")
    if canonical != DOMAIN + path:
        fail(f"{path}: canonical is {canonical}")
    alternates = dict(re.findall(
        r'<link\s+rel="alternate"\s+hreflang="([^"]+)"\s+href="([^"]+)"', html,
        flags=re.IGNORECASE,
    ))
    expected_alts = {code: DOMAIN + row[code] for code in LANGS}
    expected_alts["x-default"] = DOMAIN + row["et"]
    if alternates != expected_alts:
        fail(f"{path}: hreflang mismatch {alternates} != {expected_alts}")
    if not re.search(r'<title>\S.*?</title>', html, flags=re.DOTALL):
        fail(f"{path}: missing title")
    if not re.search(r'<meta\s+name="description"\s+content="\S', html):
        fail(f"{path}: missing meta description")
    expected_social = DOMAIN + SOCIAL_IMAGE
    social_values = {
        "og:image": one(r'<meta\s+property="og:image"\s+content="([^"]+)"', html, f"{path} og:image"),
        "og:image:secure_url": one(r'<meta\s+property="og:image:secure_url"\s+content="([^"]+)"', html, f"{path} og:image:secure_url"),
        "twitter:image": one(r'<meta\s+name="twitter:image"\s+content="([^"]+)"', html, f"{path} twitter:image"),
    }
    if any(value != expected_social for value in social_values.values()):
        fail(f"{path}: social image mismatch {social_values}")
    if one(r'<meta\s+property="og:image:type"\s+content="([^"]+)"', html, f"{path} og:image:type") != "image/jpeg":
        fail(f"{path}: wrong social image type")
    if one(r'<meta\s+property="og:image:width"\s+content="([^"]+)"', html, f"{path} og:image:width") != "1200":
        fail(f"{path}: wrong social image width")
    if one(r'<meta\s+property="og:image:height"\s+content="([^"]+)"', html, f"{path} og:image:height") != "630":
        fail(f"{path}: wrong social image height")
    if one(r'<meta\s+name="twitter:card"\s+content="([^"]+)"', html, f"{path} twitter:card") != "summary_large_image":
        fail(f"{path}: wrong Twitter card type")
    one(r'<meta\s+property="og:image:alt"\s+content="(\S[^"]*)"', html, f"{path} og:image:alt")
    one(r'<meta\s+name="twitter:image:alt"\s+content="(\S[^"]*)"', html, f"{path} twitter:image:alt")
    if not re.search(r'<h1(?:\s[^>]*)?>.*?</h1>', html, flags=re.DOTALL):
        fail(f"{path}: missing H1")
    json_ld(html, path)

    dropdown = one(r'<div class="dd">(.*?)</div>', html, f"{path} service dropdown")
    menu_links = re.findall(r'href="([^"]+)"', dropdown)
    if menu_links != service_paths(lang):
        fail(f"{path}: service dropdown is not the catalog order")
    footer = one(r'<footer\b.*?</footer>', html, f"{path} footer")
    missing_footer = [service for service in service_paths(lang) if f'href="{service}"' not in footer]
    if missing_footer:
        fail(f"{path}: footer is missing {missing_footer}")

    for asset in re.findall(r'(?:src|href)="/img/([^"?#]+)', html):
        if not os.path.isfile(os.path.join(ROOT, "img", asset)):
            fail(f"{path}: missing image/video asset /img/{asset}")
    return html


def validate_services():
    catalog_paths = {path for lang in LANGS for path in service_paths(lang)}
    for row in PAGES:
        for lang in LANGS:
            path = row[lang]
            if path not in catalog_paths:
                continue
            html = read(page_file(path))
            blocks = json_ld(html, path)
            for schema_type in ("Service", "BreadcrumbList", "FAQPage"):
                if len(schema_by_type(blocks, schema_type)) != 1:
                    fail(f"{path}: expected one {schema_type} schema")
            service = schema_by_type(blocks, "Service")[0]
            if service.get("url") != DOMAIN + path or service.get("inLanguage") != lang:
                fail(f"{path}: Service URL/inLanguage mismatch")
            crumbs = schema_by_type(blocks, "BreadcrumbList")[0]["itemListElement"]
            if crumbs[-1].get("item") != DOMAIN + path:
                fail(f"{path}: final breadcrumb is not canonical")
            questions = re.findall(r'<button class="faq-q">(.*?)</button>', html, flags=re.DOTALL)
            schema_questions = [item["name"] for item in schema_by_type(blocks, "FAQPage")[0]["mainEntity"]]
            if questions != schema_questions:
                fail(f"{path}: visible FAQ and FAQ schema differ")


def validate_home_cards():
    homes = {"et": "/", "ru": "/ru/", "en": "/en/"}
    for lang, path in homes.items():
        html = read(page_file(path))
        cards = re.findall(r'<a class="step-ph" href="([^"]+)"', html)
        if cards != service_paths(lang):
            fail(f"{path}: homepage service cards are not the complete catalog")
        blocks = json_ld(html, path)
        businesses = schema_by_type(blocks, "HomeAndConstructionBusiness")
        websites = schema_by_type(blocks, "WebSite")
        if len(businesses) != 1 or businesses[0].get("@id") != DOMAIN + "/#business":
            fail(f"{path}: canonical business schema is missing")
        if len(websites) != 1 or websites[0].get("@id") != DOMAIN + "/#website":
            fail(f"{path}: shared WebSite schema is missing")
        if websites[0].get("inLanguage") != list(LANGS):
            fail(f"{path}: WebSite language list is incomplete")


def validate_forms():
    """Keep the PPC form identical in structure across all three languages."""
    home_by_lang = {"et": "/", "ru": "/ru/", "en": "/en/"}
    expected_paths = set(home_by_lang.values()) | {path for lang in LANGS for path in service_paths(lang)}
    if len(expected_paths) != 27:
        fail(f"Expected 27 form pages, got {len(expected_paths)}")
    expected_services = ["aed", "varav", "automaatika"]
    contact_labels = {
        "et": ["Nimi *", "Telefon *", "E-post *", "Objekti aadress *"],
        "ru": ["Имя *", "Телефон *", "Email *", "Адрес объекта *"],
        "en": ["Name *", "Phone *", "Email *", "Site address *"],
    }
    length_options = {
        "et": [("unknown", "Ei tea veel"), ("up_to_50", "Kuni 50 m"), ("over_50", "Üle 50 m")],
        "ru": [("unknown", "Пока не знаю"), ("up_to_50", "До 50 м"), ("over_50", "Более 50 м")],
        "en": [("unknown", "Not sure yet"), ("up_to_50", "Up to 50 m"), ("over_50", "Over 50 m")],
    }
    for lang in LANGS:
        lang_paths = {home_by_lang[lang], *service_paths(lang)}
        for path in sorted(lang_paths):
            html = read(page_file(path))
            form = one(r'<form\s+id="leadFormV2"[^>]*>.*?</form>', html, f"{path} lead form")
            choices = re.findall(r'<button\s+class="project-choice[^>]*data-service="([^"]+)"', form)
            if choices != expected_services:
                fail(f"{path}: form choices are {choices}, expected {expected_services}")
            labels = [re.sub(r'<[^>]+>', '', label).strip() for label in re.findall(r'<span class="form-field-label">(.*?)</span>', form)]
            if labels[:4] != contact_labels[lang]:
                fail(f"{path}: contact labels are not the short {lang.upper()} set")
            length_select = one(r'<select\s+id="lengthSelect"[^>]*>(.*?)</select>', form, f"{path} length select")
            lengths = re.findall(r'<option\s+value="([^"]+)"[^>]*>([^<]+)</option>', length_select)
            if lengths != length_options[lang]:
                fail(f"{path}: length options are {lengths}, expected {length_options[lang]}")
            for field in ("name", "phone", "email", "address"):
                tag = one(rf'<input\b[^>]*name="{field}"[^>]*>', form, f"{path} {field} field")
                if " required" not in tag:
                    fail(f"{path}: {field} is not required")
            if not re.search(r'<input\b[^>]*name="photos"', form):
                fail(f"{path}: photo upload is missing")
            if not re.search(r'<textarea\b[^>]*name="msg"', form):
                fail(f"{path}: comment field is missing")
            if len(re.findall(r'<button\b[^>]*type="submit"', form)) != 1:
                fail(f"{path}: expected one submit button")
            stale = ("form-progress", "data-form-step", "formNext", "formBack")
            if any(marker in form for marker in stale):
                fail(f"{path}: two-step form controls are still present")


def validate_brand():
    """The vehicle-derived lockup must be the one shared by every indexed page."""
    for path in sorted(row[lang] for row in PAGES for lang in LANGS):
        html = read(page_file(path))
        if html.count('class="nav-logo"') != 2:
            fail(f"{path}: expected the shared header and footer logo")
        if html.count('class="brand-lockup"') != 3:
            fail(f"{path}: vehicle-derived logo is not used in header, footer and footer wordmark")
        if 'Lux<b>Aed</b>' in html or '<div class="foot-wordmark">LUX' in html:
            fail(f"{path}: stale hand-built LuxAed wordmark remains")
        if '<link rel="icon" href="/img/luxaed-mark.svg">' not in html:
            fail(f"{path}: shared fence-mark favicon is missing")


def validate_sitemap():
    tree = ET.parse(os.path.join(ROOT, "sitemap.xml"))
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9",
          "x": "http://www.w3.org/1999/xhtml"}
    urls = tree.findall("s:url", ns)
    if len(urls) != 39:
        fail(f"Sitemap contains {len(urls)} URLs, expected 39")
    locs = [node.findtext("s:loc", namespaces=ns) for node in urls]
    expected = [DOMAIN + row[lang] for row in PAGES for lang in LANGS]
    if Counter(locs) != Counter(expected):
        fail("Sitemap URL set differs from page matrix")
    row_by_url = {DOMAIN + row[lang]: row for row in PAGES for lang in LANGS}
    for node, loc in zip(urls, locs):
        alternates = {link.attrib["hreflang"]: link.attrib["href"] for link in node.findall("x:link", ns)}
        row = row_by_url[loc]
        expected_alts = {lang: DOMAIN + row[lang] for lang in LANGS}
        expected_alts["x-default"] = DOMAIN + row["et"]
        if alternates != expected_alts:
            fail(f"{loc}: sitemap hreflang mismatch")


def validate_redirects_and_links():
    redirects = json.load(open(os.path.join(ROOT, "vercel.json"), encoding="utf-8"))["redirects"]
    redirect_map = {item["source"].rstrip("/") or "/": item["destination"] for item in redirects}
    expected_redirects = {
        "/ru/zabory/3d-paneli": "/ru/zabory/2d-3d-setka/",
        "/en/fences/metal": "/en/fences/profiled-sheet/",
    }
    for source, destination in expected_redirects.items():
        if redirect_map.get(source) != destination:
            fail(f"Missing permanent redirect {source} -> {destination}")
    for old in OLD_CANONICALS:
        if os.path.isfile(page_file(old)):
            fail(f"Stale generated canonical still exists: {old}")
    for row in PAGES:
        for lang in LANGS:
            path = row[lang]
            html = read(page_file(path))
            for old in OLD_CANONICALS:
                if old in html:
                    fail(f"{path}: still links to obsolete URL {old}")
            for href in re.findall(r'href="(/[^"]*)"', html):
                target = href.split("#", 1)[0].split("?", 1)[0]
                if not target or target.startswith(("/img/", "/assets/", "/fonts/", "/api/")):
                    continue
                normalized = target.rstrip("/") or "/"
                if os.path.isfile(page_file(target)) or normalized in redirect_map:
                    continue
                if os.path.isfile(os.path.join(ROOT, target.lstrip("/"))):
                    continue
                fail(f"{path}: broken internal link {href}")


def main():
    validate_catalog()
    validate_social_asset()
    for row in PAGES:
        for lang in LANGS:
            validate_page(row, lang)
    validate_services()
    validate_home_cards()
    validate_forms()
    validate_brand()
    validate_sitemap()
    validate_redirects_and_links()
    print("VALID: 39 URLs · 13 complete hreflang groups · 8 services in ET/RU/EN")


if __name__ == "__main__":
    main()
