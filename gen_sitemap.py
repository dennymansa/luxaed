#!/usr/bin/env python3
# Generate sitemap.xml from the PAGES map in build_pages, WITH hreflang alternates
# (xhtml:link) so Google pairs the et/ru/en versions of every page. Run in the build.
import io
from build_pages import PAGES, DOMAIN
from problem_content import PROBLEM_ROWS, GUIDE_ROWS
from seo_lastmod import update_dates

# Priority by page role, independent of how many ET-only service rows exist.
def prio(row):
    et = row.get("et", "")
    if et == "/": return "1.0"
    if et.startswith("/aiad/") or et.startswith("/varavad/") or et in ("/varavad/", "/aia-remont/"): return "0.8"
    if et in ("/hinnad/", "/kuidas-valida-aeda/", "/piirkonnad/harjumaa/"): return "0.7"
    if et.startswith("/aia-remont/") or any(et == row["et"] for row in GUIDE_ROWS): return "0.7"
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
EXPECTED_GROUPS = 17 + len(PROBLEM_ROWS) + len(GUIDE_ROWS)
if len(PAGES) != EXPECTED_GROUPS:
    raise RuntimeError(f"Expected {EXPECTED_GROUPS} translated page groups, got {len(PAGES)}")

dates = update_dates([path for row in PAGES for path in row.values()])
for row in PAGES:
    p = prio(row)
    alts = alts_xml(row)
    for lang in ("et", "ru", "en"):
        loc = DOMAIN + row[lang]
        out.append(f'  <url><loc>{loc}</loc><lastmod>{dates[row[lang]]}</lastmod><priority>{p}</priority>{alts}</url>')
out.append('</urlset>')
io.open("sitemap.xml", "w", encoding="utf-8").write("\n".join(out) + "\n")
url_count = sum(len(row) for row in PAGES)
if url_count != EXPECTED_GROUPS * 3:
    raise RuntimeError(f"Expected {EXPECTED_GROUPS * 3} sitemap URLs, got {url_count}")
print(f"sitemap.xml: {url_count} urls, per-page lastmod, complete hreflang alternates added")
