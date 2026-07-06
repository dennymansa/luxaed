#!/usr/bin/env python3
"""validate.py - hard invariants for the Moving24 staging tree.

Run before EVERY zip/deploy:  python3 validate.py
Exit code 0 = safe to ship. Non-zero = a hard invariant is broken.

Hard failures (block the build):
  1. broken internal link/asset reference (href/src/srcset/poster/CSS url())
  2. invalid JSON-LD on any page
  3. em-dash (U+2014) anywhere in any HTML
  4. GTM container marker missing on a tracked page (all pages except /turg/)
  5. page missing <title> or meta description
  6. hreflang set incomplete where present (must be et+en+ru+fi+x-default)
  7. canonical pointing at a non-moving24.ee host
  8. sitemap.xml invalid or referencing a non-existent page
  9. leftover __PLACEHOLDER__ tokens
 10. config.php present inside staging/ (secrets must stay server-side only)

Warnings (printed, do not block):
  - TODO comments in HTML
  - duplicate <title> across pages
  - temporary #gal-numbers overlay still present (must be removed before prod cutover)
"""
import re, sys, json, pathlib
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).parent / 'staging'
GTM_MARKER = 'GTM-TSG2CVLC'
UNTRACKED_OK = {'turg/index.html'}          # internal dossier, intentionally untracked
HREFLANG_REQUIRED = {'et', 'en', 'ru', 'fi', 'x-default'}

ATTR_RE = re.compile(r'(?:href|src|poster)="([^"]+)"')
SRCSET_RE = re.compile(r'srcset="([^"]+)"')
CSSURL_RE = re.compile(r'url\(([^)]+)\)')
PATHLIKE = re.compile(
    r'^(?:/|\./|\.\./)[^\s"\']*$|'
    r'\.(?:html?|jpg|jpeg|png|gif|svg|webp|ico|css|js|woff2?|xml|txt|mp4|json|php)(?:\?[^\s"\']*)?$')

failures, warnings = [], []


def rel(p): return str(p.relative_to(ROOT))


def resolve(base_page, ref):
    ref = ref.strip().strip("'").strip('"')
    if (not ref or ref.startswith(('#', 'mailto:', 'tel:', 'data:', 'javascript:',
                                   'http://', 'https://', '//'))):
        return None
    if ' ' in ref or not PATHLIKE.search(ref):
        return None
    ref_path = ref.split('?')[0].split('#')[0]
    if ref_path.startswith('/'):
        return ROOT / ref_path.lstrip('/')
    return (base_page.parent / ref_path).resolve()


pages = sorted(ROOT.rglob('index.html')) + [ROOT / '404.html']
titles = {}

for page in pages:
    s = page.read_text(encoding='utf-8')
    r = rel(page)

    # 1. broken refs
    refs = set(ATTR_RE.findall(s))
    for m in SRCSET_RE.findall(s):
        for part in m.split(','):
            u = part.strip().split(' ')[0]
            if u: refs.add(u)
    for m in CSSURL_RE.findall(s):
        u = m.strip().strip("'").strip('"')
        if u: refs.add(u)
    for ref in refs:
        target = resolve(page, ref)
        if target is not None and not target.exists():
            failures.append(f'{r}: broken ref "{ref}"')

    # 2. JSON-LD
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            json.loads(m.group(1))
        except Exception as e:
            failures.append(f'{r}: invalid JSON-LD ({e})')

    # 3. em-dash / en-dash / other long dashes (Denis's rule: hyphen only)
    for _d, _name in [('—','em-dash U+2014'), ('–','en-dash U+2013'),
                      ('‒','figure-dash U+2012'), ('―','horizontal-bar U+2015'),
                      ('−','minus U+2212')]:
        if _d in s:
            failures.append(f'{r}: contains {_name}')

    # 4. tracking
    if r not in UNTRACKED_OK and GTM_MARKER not in s:
        failures.append(f'{r}: GTM marker {GTM_MARKER} missing')

    # 5. title + description
    tm = re.search(r'<title>([^<]*)</title>', s)
    if not tm or not tm.group(1).strip():
        failures.append(f'{r}: missing <title>')
    else:
        titles.setdefault(tm.group(1).strip(), []).append(r)
    if not re.search(r'<meta name="description" content="[^"]+"\s*/?>', s):
        failures.append(f'{r}: missing/unclosed meta description')

    # 6. hreflang completeness
    langs = set(re.findall(r'<link rel="alternate" hreflang="([^"]+)"', s))
    if langs and langs != HREFLANG_REQUIRED:
        failures.append(f'{r}: hreflang set {sorted(langs)} != required {sorted(HREFLANG_REQUIRED)}')

    # 7. canonical host
    for cm in re.finditer(r'<link rel="canonical" href="([^"]+)"', s):
        if not cm.group(1).startswith('https://moving24.ee/'):
            failures.append(f'{r}: canonical points off-site: {cm.group(1)}')

    # 9. placeholders
    for ph in re.findall(r'__[A-Z][A-Z0-9_]{2,}__', s):
        failures.append(f'{r}: leftover placeholder {ph}')

    # warnings
    if '<!-- TODO' in s or '<!--TODO' in s:
        warnings.append(f'{r}: TODO comment in HTML')
    if 'id="gal-numbers"' in s:
        warnings.append(f'{r}: temporary #gal-numbers photo-numbering overlay is ACTIVE '
                        '(remove before production cutover)')

# duplicate titles
for t, files in titles.items():
    if len(files) > 1:
        warnings.append(f'duplicate <title> "{t[:60]}" on: {", ".join(files)}')

# 8. sitemap
try:
    tree = ET.parse(ROOT / 'sitemap.xml')
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    locs = [e.text for e in tree.getroot().findall('.//sm:loc', ns)]
    if not locs:
        locs = [e.text for e in tree.getroot().iter() if e.tag.endswith('loc')]
    for loc in locs:
        path = loc.replace('https://moving24.ee/', '').replace('https://staging.moving24.ee/', '')
        target = ROOT / path / 'index.html' if path else ROOT / 'index.html'
        if not target.exists():
            failures.append(f'sitemap.xml: {loc} -> no page on disk ({target.relative_to(ROOT)})')
except Exception as e:
    failures.append(f'sitemap.xml: parse error ({e})')

# 10. secrets
if (ROOT / 'config.php').exists():
    failures.append('staging/config.php EXISTS - secrets must never be in the shipped tree')

print(f'validate: {len(pages)} pages checked')
if warnings:
    print(f'\n--- {len(warnings)} warning(s) (non-blocking) ---')
    for w in warnings: print('  WARN:', w)
if failures:
    print(f'\n--- {len(failures)} FAILURE(s) ---')
    for f in failures: print('  FAIL:', f)
    sys.exit(1)
print('\nOK: all hard invariants hold.')
