#!/usr/bin/env python3
# Deploy transform for GitHub Pages project site (served at /<BASE>/).
# Prefixes internal absolute paths (/img, /assets, /uslugi, /et ...) with BASE.
# Idempotent (won't double-prefix). SEO URLs (https://luxaed.ee) are left intact.
# For a real root domain (luxaed.ee) deploy: set BASE="" (this becomes a no-op).
import re, glob, os

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
