#!/usr/bin/env python3
# Generate sitemap.xml from the PAGES map in build_pages, WITH hreflang alternates
# (xhtml:link) so Google pairs the et/ru/en versions of every page. Run in the build.
import io
from build_pages import PAGES, DOMAIN

LASTMOD = "2026-07-10"  # bump on meaningful content changes

# priority by page role (index in PAGES): 0=home, 1..6=services, 7=about, 8=faq, 9..10=legal
def prio(i):
    if i == 0: return "1.0"
    if 1 <= i <= 6: return "0.8"
    if i in (7, 8): return "0.6"
    return "0.4"

def alts_xml(row):
    L = [("et", row["et"]), ("ru", row["ru"]), ("en", row["en"]), ("x-default", row["et"])]
    return "".join(f'<xhtml:link rel="alternate" hreflang="{lang}" href="{DOMAIN}{p}"/>' for lang, p in L)

out = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for i, row in enumerate(PAGES):
    p = prio(i)
    alts = alts_xml(row)
    for lang in ("et", "ru", "en"):
        loc = DOMAIN + row[lang]
        out.append(f'  <url><loc>{loc}</loc><lastmod>{LASTMOD}</lastmod><priority>{p}</priority>{alts}</url>')
out.append('</urlset>')
io.open("sitemap.xml", "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"sitemap.xml: {len(PAGES)*3} urls, lastmod {LASTMOD}, hreflang alternates added")
