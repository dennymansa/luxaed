#!/usr/bin/env python3
"""Publish the three concrete guides and additive teasers without a full rebuild."""
import re
from pathlib import Path

from apply_base import apply_titlecase, brand_suffix
from concrete_guide_content import CARDS, PATHS, SERVICE_PATHS
from concrete_guide_page import MARKER_END, MARKER_START, article_page, llms_block, teaser
from problem_content import HUB_ROW

ROOT = Path(__file__).resolve().parent


def main():
    css = '<style id="lux-css">' + (ROOT / 'assets/luxaed.css').read_text() + '</style>'
    for lang, path in PATHS.items():
        article_page(lang)
        target = ROOT / path.strip('/') / 'index.html'
        source = apply_titlecase(brand_suffix(target.read_text()))
        source = re.sub(r'<link rel="stylesheet" href="/assets/luxaed\.css[^"]*">', lambda _: css, source, count=1)
        target.write_text(source)
        for parent in (HUB_ROW[lang], SERVICE_PATHS[lang]):
            target = ROOT / parent.strip('/') / 'index.html'
            source = target.read_text()
            block = teaser(lang)
            if MARKER_START in source:
                updated, count = re.subn(re.escape(MARKER_START) + r'.*?' + re.escape(MARKER_END), lambda _: block, source, flags=re.S)
                if count != 1:
                    raise ValueError('Duplicate concrete-guide teaser: ' + parent)
            else:
                anchor = '<section class="cta-final">'
                if source.count(anchor) != 1:
                    raise ValueError('Missing or ambiguous final CTA: ' + parent)
                updated = source.replace(anchor, block + anchor, 1)
            if updated != source:
                target.write_text(updated)
    target = ROOT / 'llms.txt'
    source = target.read_text()
    line = '- ' + ' / '.join(CARDS[lang][0] for lang in ('en', 'et', 'ru')) + ': ' + ' · '.join(
        f'[{lang.upper()}](https://luxaed.ee{PATHS[lang]})' for lang in ('et', 'ru', 'en')) + '\n'
    if 'https://luxaed.ee' + PATHS['et'] not in source.split('## Service finder')[0]:
        anchor = '\n## Service finder by customer need'
        if source.count(anchor) != 1:
            raise ValueError('Missing llms guide anchor')
        source = source.replace(anchor, line + anchor, 1)
    block = llms_block() + '\n'
    if '## Concrete work and fence foundations\n' in source:
        source = re.sub(r'## Concrete work and fence foundations\n.*?(?=\n## |\Z)', lambda _: block, source, flags=re.S)
    else:
        if source.count('## Contact\n') != 1:
            raise ValueError('Missing llms contact anchor')
        source = source.replace('## Contact\n', block + '\n## Contact\n', 1)
    target.write_text(source)
    print('Concrete guides, six additive teasers and llms.txt updated')


if __name__ == '__main__':
    main()
