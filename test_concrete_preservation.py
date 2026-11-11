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

from concrete_guide_content import PATHS as GUIDE_PATHS, SERVICE_PATHS
from concrete_guide_page import MARKER_END, MARKER_START, teaser
from problem_content import HUB_ROW

BASE = 'b4f86b02c1d0b42c2658f23451c3d42e09158e37'
ROOT = Path(__file__).resolve().parent
NEW_PATHS = ('/betoonitood/', '/ru/betonnye-raboty/', '/en/concrete-works/')
GUIDE_BASE = '14d332d9f62a9a8fe01561046c0a4974753ec2b8'


def without_guide_teaser(source):
    return re.sub(re.escape(MARKER_START) + r'.*?' + re.escape(MARKER_END), '', source, flags=re.S)


def original(path):
    return subprocess.check_output(['git', 'show', f'{BASE}:{path}'], cwd=ROOT)


class ConcretePreservation(unittest.TestCase):
    def test_all_existing_html_is_preserved(self):
        files = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASE], cwd=ROOT).decode().splitlines()
        for file in files:
            if not file.endswith('.html') or file.startswith('reference-kit/'):
                continue
            with self.subTest(file=file):
                current = without_guide_teaser((ROOT / file).read_text())
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
        self.assertEqual(set(after) - set(before), {'https://luxaed.ee' + p for p in (*NEW_PATHS, *GUIDE_PATHS.values())})
        self.assertTrue(set(before) <= set(after))
        for url, item in before.items():
            item.tail = None
            after[url].tail = None
            if url in {'https://luxaed.ee' + p for p in ('/', '/ru/', '/en/', *HUB_ROW.values())}:
                # These pages gained a service card or article teaser. Only the date may change.
                after[url].find('s:lastmod', ns).text = item.findtext('s:lastmod', namespaces=ns)
            with self.subTest(url=url):
                self.assertEqual(ET.tostring(after[url]), ET.tostring(item))

    def test_guide_only_adds_six_teasers_to_current_release(self):
        files = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', GUIDE_BASE], cwd=ROOT).decode().splitlines()
        expected = {p.strip('/') + '/index.html': lang for row in (HUB_ROW, SERVICE_PATHS) for lang, p in row.items()}
        changed = set()
        for file in files:
            if not file.endswith('.html') or file.startswith('reference-kit/'):
                continue
            with self.subTest(file=file):
                before = subprocess.check_output(['git', 'show', f'{GUIDE_BASE}:{file}'], cwd=ROOT).decode()
                current = (ROOT / file).read_text()
                if current != before:
                    changed.add(file)
                    self.assertIn(file, expected)
                    block = teaser(expected[file])
                    self.assertEqual(current.count(block), 1)
                    self.assertEqual(current.replace(block, '', 1), before)
                else:
                    self.assertNotIn(file, expected)
        self.assertEqual(changed, set(expected))

    def test_guide_preserves_all_existing_media(self):
        files = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', GUIDE_BASE, 'assets', 'img', 'fonts'], cwd=ROOT).decode().splitlines()
        for file in files:
            with self.subTest(file=file):
                before = subprocess.check_output(['git', 'show', f'{GUIDE_BASE}:{file}'], cwd=ROOT)
                self.assertEqual((ROOT / file).read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
