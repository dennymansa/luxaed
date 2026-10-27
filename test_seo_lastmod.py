"""Regression checks for truthful sitemap dates. Run: python3 -m unittest test_seo_lastmod."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import seo_lastmod


class SitemapDatesTest(unittest.TestCase):
    def test_css_and_tracking_do_not_change_content_date(self):
        a = '<title>Gates</title><style>a{color:red}</style><main><h1>Installation</h1></main><script>old()</script>'
        b = a.replace('red', 'blue').replace('old()', 'new()')
        self.assertEqual(seo_lastmod.fingerprint(a), seo_lastmod.fingerprint(b))

    def test_text_links_and_metadata_are_meaningful(self):
        source = '<meta name="description" content="Gates"><main><h1>Installation</h1><a href="/old/">More</a><img src="/gate.webp" alt="Gate"></main>'
        for old, new in [('Installation', 'Gate installation'), ('/old/', '/new/'), ('content="Gates"', 'content="Install gates"'), ('alt="Gate"', 'alt="Sliding gate"')]:
            with self.subTest(change=old):
                self.assertNotEqual(seo_lastmod.fingerprint(source), seo_lastmod.fingerprint(source.replace(old, new)))

    def test_date_changes_only_when_content_changes(self):
        with tempfile.TemporaryDirectory(prefix='luxaed-lastmod-test-') as tmp:
            root = Path(tmp)
            page = root / 'index.html'
            page.write_text('<main><h1>Gates</h1></main>')
            (root / 'sitemap.xml').write_text('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://luxaed.ee/</loc><lastmod>2026-09-27</lastmod></url></urlset>')
            with patch.object(seo_lastmod, 'ROOT', root), patch.object(seo_lastmod, 'STATE', root / 'state.json'):
                self.assertEqual(seo_lastmod.update_dates(['/'], '2026-09-28')['/'], '2026-09-27')
                self.assertEqual(seo_lastmod.update_dates(['/'], '2026-09-29')['/'], '2026-09-27')
                page.write_text('<main><h1>Gate installation</h1></main>')
                self.assertEqual(seo_lastmod.update_dates(['/'], '2026-09-29')['/'], '2026-09-29')
                self.assertEqual(seo_lastmod.update_dates(['/'], '2026-09-30')['/'], '2026-09-29')
                (root / 'new').mkdir()
                (root / 'new/index.html').write_text('<main><h1>New service</h1></main>')
                self.assertEqual(seo_lastmod.update_dates(['/', '/new/'], '2026-09-30')['/new/'], '2026-09-30')


if __name__ == '__main__':
    unittest.main()
