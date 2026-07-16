#!/usr/bin/env python3
"""Build every LuxAed language and stop immediately on any parity/SEO failure."""
import subprocess
import sys


STEPS = (
    "gen_et_home.py",
    "gen_ru.py",
    "gen_ru_support.py",
    "gen_en_home.py",
    "sync_ru_home.py",
    "gen_sitemap.py",
    "gen_llms.py",
    "apply_base.py",
    "validate_site.py",
)


for script in STEPS:
    print(f"\n== {script} ==", flush=True)
    subprocess.run([sys.executable, script], check=True)

print("\nBUILD READY: all languages, sitemap, schema and internal links validated")
