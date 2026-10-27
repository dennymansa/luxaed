#!/usr/bin/env python3
# Deploy transform for GitHub Pages project site (served at /<BASE>/).
# Prefixes internal absolute paths (/img, /assets, /uslugi, /et ...) with BASE.
# Idempotent (won't double-prefix). SEO URLs (https://luxaed.ee) are left intact.
# For a real root domain (luxaed.ee) deploy: set BASE="" (this becomes a no-op).
import html, re, glob, os

BASE = ""   # root-domain deploy (luxaed.ee via Vercel); was "/luxaed" for github.io project path

def fix_html(s):
    if not BASE: return s
    b = BASE
    # href/src="/..."  (skip protocol-relative //, and already-prefixed)
    s = re.sub(r'(href|src)="/(?!'+re.escape(b[1:])+r'/)(?!/)', r'\1="'+b+'/', s)
    # srcset="/..."
    s = re.sub(r'srcset="/(?!'+re.escape(b[1:])+r'/)(?!/)', r'srcset="'+b+'/', s)
    # inline url('/...')
    s = re.sub(r"url\((['\"]?)/(?!"+re.escape(b[1:])+r"/)(?!/)", r"url(\1"+b+"/", s)
    return s

def fix_css(s):
    if not BASE: return s
    b = BASE
    return re.sub(r"url\((['\"]?)/(?!"+re.escape(b[1:])+r"/)(?!/)", r"url(\1"+b+"/", s)

# ---- Title Case for <title>/og:title/twitter:title (per language, connectors stay lowercase) ----
_STOP = {
 'ru': {'и','в','из','на','о','с','со','для','по','к','у','от','до'},
 'et': {'ja','ning','või'},
 'en': {'and','in','of','the','a','an','for','to','or','on','with','&','by','at','from','into','per','via','vs','vs.','as','near','across','over','under','between','within','without','onto'},
}
def _cap_first(w):
    for i,ch in enumerate(w):
        if ch.isalpha():
            return w[:i]+ch.upper()+w[i+1:]  # capitalise first letter, keep the rest (LuxAed, 3D, väravate stay intact)
        if ch.isdigit():
            return w  # 3D-, 15- etc: leave as-is
    return w
def _tc_part(s, lang):
    stop=_STOP.get(lang,set()); out=[]
    for i,w in enumerate(s.split(' ')):
        if not w or w == '&': out.append(w); continue
        low=w.lower().strip('.,()')
        # hyphenated compounds are capitalised on both sides: Fence-Building, Chain-Link
        out.append(w.lower() if (i>0 and low in stop) else '-'.join(_cap_first(part) for part in w.split('-')))
    return ' '.join(out)
def title_case(title, lang):
    # keep the "| LuxAed" brand suffix untouched; work on unescaped text so
    # words like won&#x27;t are cased as words, then escape again
    text = html.unescape(title)
    for sep in (' | ', ' — '):
        if sep in text:
            main, brand = text.rsplit(sep, 1)
            return html.escape(_tc_part(main, lang) + sep + brand)
    return html.escape(_tc_part(text, lang))
def brand_suffix(html_text):
    # one brand separator site-wide: "Page title | LuxAed" (no em dash in titles)
    def fix(mm):
        return mm.group(1) + re.sub(r'\s+(?:—|–|-)\s+LuxAed$', ' | LuxAed', mm.group(2)) + mm.group(3)
    html_text = re.sub(r'(<title>)(.*?)(</title>)', fix, html_text, count=1, flags=re.DOTALL)
    for prop in ('og:title', 'twitter:title', 'og:image:alt', 'twitter:image:alt'):
        html_text = re.sub(r'(<meta (?:property|name)="' + prop + r'" content=")([^"]*)(")', fix, html_text, count=1)
    return html_text
def apply_titlecase(html):
    m=re.search(r'<html lang="([a-z]{2})"', html)
    lang=m.group(1) if m else 'et'
    # English marketing titles conventionally use title case. Estonian and
    # Russian titles use sentence case, so preserve the wording supplied by
    # their generators instead of applying English capitalisation rules.
    if lang != 'en':
        return html
    def sub_title(mm): return '<title>'+title_case(mm.group(1), lang)+'</title>'
    html=re.sub(r'<title>(.*?)</title>', sub_title, html, count=1, flags=re.DOTALL)
    for prop in ('og:title','twitter:title'):
        def sub_meta(mm, prop=prop): return mm.group(1)+title_case(mm.group(2), lang)+mm.group(3)
        html=re.sub(r'(<meta (?:property|name)="'+prop+r'" content=")([^"]*)(">)', sub_meta, html, count=1)
    return html

def main():
    import hashlib
    # content hash of CSS -> cache-busting version so browsers always fetch fresh CSS
    ver=""
    if os.path.exists("assets/luxaed.css"):
        ver=hashlib.md5(open("assets/luxaed.css","rb").read()).hexdigest()[:8]
    css_inline=""
    if os.path.exists("assets/luxaed.css"):
        css_inline='<style id="lux-css">'+open("assets/luxaed.css",encoding="utf-8").read()+'</style>'
    n=0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith("reference-kit"): continue
        s=open(f,encoding="utf-8").read(); t=fix_html(s)
        t=brand_suffix(t)
        t=t.replace(' — LuxAed"', ' | LuxAed"')
        if not re.search(r'class="[^"]*\bhand\b', t):
            # the Caveat preload only helps pages that show the handwritten kicker
            t=re.sub(r'<link rel="preload" as="font" type="font/woff2" href="/fonts/caveat-var-[a-z]+\.woff2" crossorigin>\n?', '', t)
        t=apply_titlecase(t)
        if css_inline:
            # inline the full stylesheet (removes the render-blocking request);
            # idempotent: replaces the <link> on fresh builds or refreshes a previous inline copy
            t=re.sub(r'<link rel="stylesheet" href="/assets/luxaed\.css[^"]*">', lambda m: css_inline, t, count=1)
            t=re.sub(r'<style id="lux-css">.*?</style>', lambda m: css_inline, t, count=1, flags=re.DOTALL)
        if t!=s: open(f,"w",encoding="utf-8").write(t); n+=1
    for f in ["assets/luxaed.css"]:
        if os.path.exists(f):
            s=open(f,encoding="utf-8").read(); t=fix_css(s)
            if t!=s: open(f,"w",encoding="utf-8").write(t); n+=1
    print(f"BASE={BASE!r} applied to {n} files | css v={ver}")

if __name__=="__main__":
    main()
