#!/usr/bin/env python3
"""build_zip.py - the ONLY way to produce moving24-staging.zip.

Runs validate.py first (hard invariants), then builds the zip
deterministically, then verifies the zip contents. Refuses to ship
a broken tree.

Usage:  python3 build_zip.py
"""
import subprocess, sys, zipfile, pathlib, os

HERE = pathlib.Path(__file__).parent
STAGING = HERE / 'staging'
OUT = HERE / 'moving24-staging.zip'
EXCLUDE_NAMES = {'.DS_Store', 'config.php', 'build.txt', '.nojekyll'}
EXCLUDE_DIRS = {'_incoming', '_logotest', '.claude', '_ai', '.git'}

# 1. validate
print('=== 1/3 validate ===')
r = subprocess.run([sys.executable, str(HERE / 'validate.py')])
if r.returncode != 0:
    print('\nBUILD ABORTED: validate.py failed. Fix the failures above, then rerun.')
    sys.exit(1)

# 2. build
print('\n=== 2/3 zip ===')
if OUT.exists():
    OUT.unlink()
count = 0
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for path in sorted(STAGING.rglob('*')):
        if path.is_dir():
            continue
        relparts = path.relative_to(STAGING).parts
        if path.name in EXCLUDE_NAMES or (relparts and relparts[0] in EXCLUDE_DIRS):
            continue
        z.write(path, str(path.relative_to(STAGING)))
        count += 1
size_mb = OUT.stat().st_size / 1024 / 1024
print(f'{OUT.name}: {count} files, {size_mb:.1f} MB')

# 3. verify zip contents
print('\n=== 3/3 verify zip ===')
problems = []
with zipfile.ZipFile(OUT) as z:
    names = z.namelist()
    if any('config.php' in n for n in names):
        problems.append('config.php leaked into the zip')
    lead = [n for n in names if n.endswith('lead.php')]
    if lead != ['lead.php']:
        problems.append(f'lead.php entries unexpected: {lead}')
    if 'index.html' not in names or 'sitemap.xml' not in names:
        problems.append('missing root index.html or sitemap.xml')
    for required in ('ru/index.html', 'en/index.html', 'fi/index.html', '.htaccess'):
        if required not in names:
            problems.append(f'missing {required}')

if problems:
    for p in problems: print('  FAIL:', p)
    OUT.unlink()
    print('\nBUILD ABORTED: zip verification failed, artifact deleted.')
    sys.exit(1)

print('zip verified: no secrets, lead.php x1, all languages present.')
print(f'\nREADY TO UPLOAD: {OUT}')
