#!/usr/bin/env python3
# Keep the hand-built RU home (ru/index.html) in sync with the build_pages-derived chunks.
#
# WHY THIS EXISTS: ru/index.html is the ONLY page not produced by a gen_*.py — it is hand-built.
# Every other page pulls SCRIPTS / video_block() / partners_marquee() straight from build_pages,
# so a change there propagates everywhere EXCEPT the RU home. That gap caused real desyncs
# (RU videos not playing, stale sunset, old carousel arrows). Run this after every build so the
# RU home can never drift again:  python3 build_pages... gens ...; python3 sync_ru_home.py
import io, re, importlib
import build_pages
importlib.reload(build_pages)

P = 'ru/index.html'
s = io.open(P, encoding='utf-8').read()
orig = s
changed = []

def sub_once(pattern, repl_str, label):
    global s
    new, n = re.subn(pattern, lambda m: repl_str, s, count=1, flags=re.DOTALL)
    if n != 1:
        raise SystemExit(f"sync_ru_home: anchor for '{label}' not found (matches={n}) — RU home structure changed, fix the pattern")
    if new != s:
        changed.append(label)
    s = new

# 1) shared <script> block (anchored on the unique 'function closeMob')
sub_once(r'<script>\s*\n(?:window\.__t0[^\n]*\n)?function closeMob\(\).*?</script>', build_pages.SCRIPTS, 'SCRIPTS')
# 2) video section (dark sunset + looping carousel)
sub_once(r'<section class="section section--dark vidsec".*?</section>', build_pages.video_block('ru'), 'video_block')
# 3) partners marquee (real brand logos, two rows)
sub_once(r'<section class="partners-marquee".*?</section>', build_pages.partners_marquee('ru'), 'partners_marquee')

# 4) VideoObject schema blocks in <head> (order must match the rendered carousel)
vs = "\n".join(build_pages.video_schema(build_pages.home_video_items('ru'), 'ru'))
new2, n2 = re.subn(r'(<script type="application/ld\+json">\{"@context": "https://schema\.org", "@type": "VideoObject".*?</script>\n?)+', vs + "\n", s, count=1, flags=re.DOTALL)
if n2 == 1 and new2 != s:
    changed.append('video_schema'); s = new2
elif n2 != 1:
    raise SystemExit("sync_ru_home: VideoObject schema anchor not found")

if s != orig:
    io.open(P, 'w', encoding='utf-8').write(s)
print("sync_ru_home:", ("updated " + ", ".join(changed)) if changed else "already in sync")
