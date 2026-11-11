"""Release regression: existing published HTML may only gain concrete links.

Baseline is the production commit verified before this service was added.
Run with Python 3.12+: python3 -m unittest test_concrete_preservation
"""
import json
import re
import subprocess
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

BASE = 'b4f86b02c1d0b42c2658f23451c3d42e09158e37'
ROOT = Path(__file__).resolve().parent
NEW_PATHS = ('/betoonitood/', '/ru/betonnye-raboty/', '/en/concrete-works/')


def original(path):
    return subprocess.check_output(['git', 'show', f'{BASE}:{path}'], cwd=ROOT)


class ConcretePreservation(unittest.TestCase):
    def test_all_existing_html_is_preserved(self):
        files = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASE], cwd=ROOT).decode().splitlines()
        for file in files:
            if not file.endswith('.html') or file.startswith('reference-kit/'):
                continue
            with self.subTest(file=file):
                current = (ROOT / file).read_text()
                # Remove only the new service's complete homepage card and links.
                for path in NEW_PATHS:
                    current = re.sub(r'<a class="step-ph" href="' + re.escape(path) + r'">.*?</a>', '', current, flags=re.S)
                    current = re.sub(r'<a\b[^>]*href="' + re.escape(path) + r'"[^>]*>[^<]*</a>', '', current)
                self.assertEqual(current.encode(), original(file))

    def test_existing_assets_are_identical(self):
        files = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASE, 'assets', 'img', 'fonts'], cwd=ROOT).decode().splitlines()
        for file in files:
            with self.subTest(file=file):
                self.assertEqual((ROOT / file).read_bytes(), original(file))

    def test_old_sitemap_entries_are_preserved(self):
        ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        def entries(raw):
            return {item.findtext('s:loc', namespaces=ns): item for item in ET.fromstring(raw).findall('s:url', ns)}
        before, after = entries(original('sitemap.xml')), entries((ROOT / 'sitemap.xml').read_bytes())
        self.assertEqual(set(after) - set(before), {'https://luxaed.ee' + p for p in NEW_PATHS})
        self.assertTrue(set(before) <= set(after))
        for url, item in before.items():
            if url in ('https://luxaed.ee/', 'https://luxaed.ee/ru/', 'https://luxaed.ee/en/'):
                continue
            with self.subTest(url=url):
                self.assertEqual(ET.tostring(after[url]), ET.tostring(item))


if __name__ == '__main__':
    unittest.main()
