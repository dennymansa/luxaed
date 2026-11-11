#!/usr/bin/env python3
"""Add concrete work without regenerating existing published page content.

Run with Python 3.12+: python3 gen_concrete.py && python3 gen_sitemap.py
The full legacy build currently drifts from the published HTML. This focused
build only renders the new pages and inserts their navigation/homepage links.
"""
import re
from pathlib import Path

from apply_base import apply_titlecase, brand_suffix
from build_pages import PAGES, service_tiles_html
from concrete_service import CONCRETE_SERVICES
from service_catalog import SERVICE_MATRIX
from service_layout import render_service

ROOT = Path(__file__).resolve().parent
ENTRY = next(item for item in SERVICE_MATRIX if item['key'] == 'concrete')
REPAIR = next(item for item in SERVICE_MATRIX if item['key'] == 'repair')


def homepage_card(lang):
    cards = service_tiles_html(lang)
    return cards[cards.rfind('<a class="step-ph"'):]


def insert_links(source, lang):
    old = REPAIR[lang]
    new = ENTRY[lang]
    plain = f'<a href="{new["path"]}">{new["label"]}</a>'
    anchor = f'<a href="{old["path"]}">{old["label"]}</a>'
    # Restrict insertions to navigation/footer, preserving all page content.
    for region in (r'<div class="dd">.*?</div>', r'<footer\b.*?</footer>'):
        def add(match):
            block = match.group()
            if new['path'] in block:
                return block
            if block.count(anchor) != 1:
                raise ValueError(f'Missing or ambiguous {lang} navigation anchor')
            return block.replace(anchor, anchor + plain)
        source = re.sub(region, add, source, flags=re.S)
    mobile = f'<a class="nm-sub" href="{new["path"]}" onclick="closeMob()">{new["label"]}</a>'
    old_mobile = f'<a class="nm-sub" href="{old["path"]}" onclick="closeMob()">{old["label"]}</a>'
    if mobile not in source and old_mobile in source:
        source = source.replace(old_mobile, old_mobile + mobile)
    return source


def main():
    css = '<style id="lux-css">' + (ROOT / 'assets/luxaed.css').read_text() + '</style>'
    for lang, content in CONCRETE_SERVICES.items():
        target = ROOT / content['path'].strip('/') / 'index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        source = apply_titlecase(brand_suffix(render_service(lang, content)))
        source = re.sub(r'<link rel="stylesheet" href="/assets/luxaed\.css[^"]*">', lambda _: css, source, count=1)
        target.write_text(source)
    for row in PAGES:
        for lang, path in row.items():
            target = ROOT / path.strip('/') / 'index.html'
            source = target.read_text()
            updated = insert_links(source, lang)
            if path in ('/', '/ru/', '/en/') and 'class="step-ph" href="' + ENTRY[lang]['path'] + '"' not in updated:
                repair_card = re.search(r'<a class="step-ph" href="' + re.escape(REPAIR[lang]['path']) + r'">.*?</a>', updated, re.S)
                if not repair_card:
                    raise ValueError(f'Missing {lang} homepage repair card')
                end = repair_card.end()
                updated = updated[:end] + homepage_card(lang) + updated[end:]
            if updated != source:
                target.write_text(updated)
    target = ROOT / '404.html'
    source = target.read_text()
    lang = re.search(r'<html lang="([a-z]+)"', source).group(1)
    target.write_text(insert_links(source, lang))
    target = ROOT / 'llms.txt'
    source = target.read_text()
    if 'https://luxaed.ee/betoonitood/' not in source:
        line = '- Betoonitööd ja aiavundamendid / Бетонные работы и фундаменты / Concrete work and foundations: [ET](https://luxaed.ee/betoonitood/) · [RU](https://luxaed.ee/ru/betonnye-raboty/) · [EN](https://luxaed.ee/en/concrete-works/)\n'
        source = source.replace('\n## Repair problems', line + '\n## Repair problems')
        target.write_text(source)
    print('Concrete service pages and additive links generated in ET/RU/EN')


if __name__ == '__main__':
    main()
