#!/usr/bin/env python3
# LuxAed static page generator. Shared shared site chrome + per-page content.
# Run:  python3 build_pages.py
import os, html, hashlib
from service_catalog import LANGS, service_rows, service_nav, service_tiles

SITE = os.path.dirname(os.path.abspath(__file__))
PHONE = "+372 5695 8285"; TEL = "+37256958285"; EMAIL = "luxaed9@gmail.com"
FB = "https://www.facebook.com/LuxxAed"; DOMAIN = "https://luxaed.ee"
SOCIAL_IMAGE = "/img/luxaed-og-v2.jpg"
GA_ID = ""   # set to "G-XXXXXXXXXX" for direct GA4 (usually leave empty and use GTM instead)
GTM_ID = ""  # set to "GTM-XXXXXXX" to switch on Google Tag Manager (manages GA/Pixel/etc.)
AW_ID = "AW-960623543"                  # Google Ads conversion account id
AW_LEAD_LABEL = "AW-960623543/dU7wCMWR9swcELfnh8oD"  # conversion action: lead form submitted
REVIEW_COUNT = 34
EXPERIENCE_YEARS = 15
RECOMMEND_PERCENT = 100
COPYRIGHT_YEAR = 2026

# Language path map for hreflang + language switch. Service rows are generated
# from one mandatory ET/RU/EN matrix; a service cannot exist in only one language.
LANG_HOME = {"ru":"/ru/", "et":"/", "en":"/en/"}
PAGES = [{"ru":"/ru/","et":"/","en":"/en/"}] + service_rows() + [
 {"ru":"/ru/o-nas/","et":"/meist/","en":"/en/about/"},
 {"ru":"/ru/faq/","et":"/kkk/","en":"/en/faq/"},
 {"ru":"/ru/privaatsus/","et":"/privaatsus/","en":"/en/privacy/"},
 {"ru":"/ru/tingimused/","et":"/tingimused/","en":"/en/terms/"},
]
def _row(path):
    for r in PAGES:
        if path in r.values(): return r
    return None
def alt(path, lang):
    row = _row(path)
    return row.get(lang, LANG_HOME[lang]) if row else LANG_HOME[lang]

def webp_sources(image_name):
    """Responsive WebP <source> tags for an image basename under /img/."""
    mobile = os.path.join(SITE, "img", image_name + "-mobile.webp")
    mobile_source = (f'<source media="(max-width:760px)" type="image/webp" '
                     f'srcset="/img/{image_name}-mobile.webp">') if os.path.exists(mobile) else ""
    return mobile_source + f'<source type="image/webp" srcset="/img/{image_name}.webp">'

def service_tiles_html(lang):
    """Homepage service cards from the same translated service matrix as nav/sitemap."""
    return "".join(
        f'''<a class="step-ph" href="{path}"><div class="img-wrap"><picture>{webp_sources(image)}<img src="/img/{image}.jpg" alt="{html.escape(title)}" width="600" height="400" loading="lazy"></picture></div>
<div class="sp-top-label"><span>{html.escape(badge)}</span></div><div class="sp-body"><h3>{html.escape(title)}</h3><p>{html.escape(desc)}</p></div></a>'''
        for path, image, badge, title, desc in service_tiles(lang)
    )

SVC = {lang: service_nav(lang) for lang in LANGS}  # nav + footer, one source
NAVLBL = {"ru":{"about":"О нас","faq":"Вопросы","contact":"Контакты","services":"Услуги ▾",
               "cta":"Оставить заявку","cta_mini":"Заявка","home":"Главная"},
          "et":{"about":"Meist","faq":"KKK","contact":"Kontakt","services":"Teenused ▾",
               "cta":"Küsi pakkumist","cta_mini":"Päring","home":"Avaleht"},
          "en":{"about":"About","faq":"FAQ","contact":"Contact","services":"Services ▾",
               "cta":"Get a quote","cta_mini":"Quote","home":"Home"}}

def logo_svg():
    """Vehicle-derived LuxAed lockup: geometric wordmark, descriptor and fence mark."""
    return ('<svg class="brand-lockup" viewBox="-6 -4 248 68" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            '<g stroke="currentColor" stroke-width="3.4" stroke-linecap="butt" stroke-linejoin="miter">'
            '<path d="M2 3V35H22"/>'
            '<path d="M29 3V24.5C29 31.5 33 35 39.5 35S50 31.5 50 24.5V3"/>'
            '<path d="M57 3L79 35M79 3L57 35"/>'
            '<path d="M84 35L96.5 3L109 35"/>'
            '<path d="M115 3H138M115 3V35H138M115 19H135"/>'
            '<path d="M145 3V35H155C166 35 172 29.3 172 19S166 3 155 3H145"/></g>'
            '<text x="86" y="54" fill="currentColor" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="10.5" font-weight="400" letter-spacing="1">AIAD JA VÄRAVAD</text>'
            '<g stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M187 18H232M187 36H232M187 46H232"/>'
            '<path d="M188.5 46V15.5M230.5 46V15.5"/>'
            '<path d="M193 46V13L196 8L199 13V46M201 46V13L204 8L207 13V46M209 46V13L212 8L215 13V46M217 46V13L220 8L223 13V46"/>'
            '</g></svg>')

def partners_marquee(lang):
    # Real fence/gate-industry brands whose equipment & materials LuxAed installs (honest,
    # referential use — not a client claim). Wordmark pills, two scrolling rows.
    ROW1 = ["BFT","Nice","CAME","Locinox","Hörmann","Hikvision"]
    ROW2 = ["Makita","DoorHan","Stihl","RAL","Bosch","DEA System"]
    T={"ru":("Партнёры","Работаем с оборудованием и материалами ведущих брендов"),
       "et":("Partnerid","Töötame juhtivate brändide seadmete ja materjalidega"),
       "en":("Partners","We work with equipment and materials from leading brands")}
    tag,h2=T.get(lang,T["et"])
    from brand_logos import BRAND_LOGOS
    def pills(names):
        return "".join(f'<span class="pm-pill pm-brand" title="{n}">{BRAND_LOGOS.get(n, n)}</span>' for n in names)
    r1,r2=pills(ROW1),pills(ROW2)
    return (f'<section class="partners-marquee" aria-label="{tag}">'
            f'<div class="wrap"><span class="tag">{tag}</span><h2 class="big">{h2}</h2></div>'
            f'<div class="pm-row" tabindex="0" role="group" aria-label="{tag}"><div class="pm-track">'
            f'<div class="pm-set">{r1}</div><div class="pm-set" aria-hidden="true">{r1}</div></div></div>'
            f'<div class="pm-row pm-rev" aria-hidden="true"><div class="pm-track">'
            f'<div class="pm-set">{r2}</div><div class="pm-set">{r2}</div></div></div>'
            f'</section>')

# ---- work videos (self-hosted, downloaded from LuxAed FB) ----
VIDEO_CAPS = {
  "luxaed-reel-montaaz":  {"et":"Aia paigaldus objektil","ru":"Монтаж забора на объекте","en":"Fence installation on site"},
  "luxaed-reel-postid":   {"et":"Postiaukude puurimine","ru":"Бурение ям под столбы","en":"Drilling the post holes"},
  "luxaed-video-puitvarav":{"et":"Puidust lükandvärav automaatikaga","ru":"Деревянные откатные ворота с автоматикой","en":"Wooden sliding gate with automation"},
  "luxaed-reel-puitvarav2":{"et":"Puitvärav ja jalgvärav","ru":"Деревянные ворота и калитка","en":"Wooden gate and pedestrian gate"},
  "luxaed-reel-puitaed":  {"et":"Puitaed ja värav","ru":"Деревянный забор и ворота","en":"Wooden fence and gate"},
  "luxaed-reel-valmis":   {"et":"Valmis puit-metallaed","ru":"Готовый забор дерево-металл","en":"Finished wood-and-metal fence"},
  "luxaed-reel-vorkaed":  {"et":"3D-keevisvõrkaed","ru":"3D-сетчатый забор","en":"3D welded-mesh fence"},
  "luxaed-reel-vorkaed2": {"et":"3D-võrkaed heki ääres","ru":"3D-забор вдоль живой изгороди","en":"3D mesh fence by a hedge"},
  "luxaed-reel-metallaed":{"et":"3D-võrkaia paigaldus","ru":"Монтаж забора из 3D-сетки","en":"3D mesh fence installation"},
  "luxaed-reel-domofon":  {"et":"Domofoni paigaldus","ru":"Установка домофона","en":"Intercom installation"},
  "luxaed-reel-varav-oht":{"et":"Lükandväravad õhtuvalguses","ru":"Откатные ворота вечером","en":"Sliding gates at dusk"},
  "luxaed-reel-remont":   {"et":"Vana posti eemaldamine","ru":"Демонтаж старого столба","en":"Removing an old post"},
}
VIDEO_ORDER = ["luxaed-reel-valmis","luxaed-reel-montaaz","luxaed-reel-varav-oht","luxaed-reel-postid","luxaed-video-puitvarav",
               "luxaed-reel-puitvarav2","luxaed-reel-puitaed","luxaed-reel-vorkaed","luxaed-reel-vorkaed2",
               "luxaed-reel-metallaed","luxaed-reel-domofon","luxaed-reel-remont"]
VIDEO_DUR = {"luxaed-reel-domofon":15,"luxaed-reel-metallaed":31,"luxaed-reel-montaaz":64,"luxaed-reel-postid":36,
             "luxaed-reel-puitaed":29,"luxaed-reel-puitvarav2":63,"luxaed-reel-remont":57,"luxaed-reel-valmis":19,
             "luxaed-reel-varav-oht":50,"luxaed-reel-vorkaed":36,"luxaed-reel-vorkaed2":70,"luxaed-video-puitvarav":59}
# Use an explicit UTC designator. Google accepts ISO 8601 offsets, but `Z` avoids
# stale Search Console parsers treating the timezone as missing.
VIDEO_UPLOADED = "2025-08-01T06:00:00Z"

def _reelcard(v, lang):
    import json as _j
    c = VIDEO_CAPS[v].get(lang, VIDEO_CAPS[v]["et"])
    return (f'<figure class="reelcard" data-src="/img/{v}.mp4" onclick="playReel(this)" '
            f'tabindex="0" role="button" aria-label="{c}" onkeydown="if(event.key===\'Enter\'||event.key===\' \'){{event.preventDefault();playReel(this)}}">'
            f'<picture><source type="image/webp" srcset="/img/{v}-poster.webp"><img class="vid-poster" loading="lazy" decoding="async" src="/img/{v}-poster.jpg" alt="{c}" width="480" height="854"></picture>'
            f'<button class="vid-play" aria-hidden="true" tabindex="-1">▶</button>'
            f'<figcaption>{c}</figcaption></figure>')

def video_schema(items, lang):
    # VideoObject JSON-LD (name, description, thumbnailUrl, uploadDate required; +contentUrl, duration)
    import json as _j
    out = []
    for v, c in items:
        d = VIDEO_DUR.get(v, 30)
        obj = {"@context":"https://schema.org","@type":"VideoObject","name":c,
               "description":c+{"ru":". LuxAed, заборы и ворота в Таллинне и Харьюмаа.","en":". LuxAed, fences and gates in Tallinn and Harjumaa."}.get(lang,". LuxAed, aiad ja väravad Tallinnas ja Harjumaal."),
               "thumbnailUrl":[DOMAIN+f"/img/{v}-poster.jpg"],"uploadDate":VIDEO_UPLOADED,
               "duration":f"PT{d}S","contentUrl":DOMAIN+f"/img/{v}.mp4",
               "publisher":{"@type":"Organization","name":"LuxAed",
                            "logo":{"@type":"ImageObject","url":DOMAIN+"/img/luxaed-logo.png"}}}
        out.append('<script type="application/ld+json">'+_j.dumps(obj,ensure_ascii=False)+'</script>')
    return out

def home_video_items(lang):
    return [(v, VIDEO_CAPS[v].get(lang, VIDEO_CAPS[v]["et"])) for v in VIDEO_ORDER]

def _ld(obj):
    import json as _j
    return '<script type="application/ld+json">'+_j.dumps(obj, ensure_ascii=False)+'</script>'

def business_schema():
    """One canonical business entity reused on every language homepage."""
    return _ld({"@context":"https://schema.org","@type":"HomeAndConstructionBusiness",
        "@id":DOMAIN+"/#business","name":"LuxAed","image":DOMAIN+"/img/luxaed-hero.jpg",
        "logo":DOMAIN+"/img/luxaed-logo.png","url":DOMAIN+"/","telephone":PHONE,
        "email":EMAIL,"priceRange":"€€",
        "address":{"@type":"PostalAddress","addressLocality":"Tallinn",
                   "addressRegion":"Harjumaa","addressCountry":"EE"},
        "areaServed":["Tallinn","Harjumaa","Estonia"],"sameAs":[FB],
        "geo":{"@type":"GeoCoordinates","latitude":59.437,"longitude":24.7536},
        "openingHoursSpecification":[{"@type":"OpeningHoursSpecification",
            "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],
            "opens":"09:00","closes":"18:00"}],
        "aggregateRating":{"@type":"AggregateRating","ratingValue":5,
                           "bestRating":5,"reviewCount":REVIEW_COUNT}})

def website_schema():
    """Shared multilingual WebSite entity; identical on ET, RU and EN homes."""
    return _ld({"@context":"https://schema.org","@type":"WebSite",
                "@id":DOMAIN+"/#website","name":"LuxAed","url":DOMAIN+"/",
                "inLanguage":["et","ru","en"],
                "publisher":{"@id":DOMAIN+"/#business"}})

def person_artur_schema(lang):
    # Person schema for the master craftsman — E-E-A-T signal (real expert behind the business)
    jt = {"et":"Aedade ja väravate meister","ru":"Мастер по заборам и воротам",
          "en":"Fence and gate master craftsman"}.get(lang,"Meister")
    knows = {"et":["Aiad","Väravad","Väravaautomaatika","Piirdeaiad","Aia remont"],
             "ru":["Заборы","Ворота","Автоматика ворот","Ограждения","Ремонт заборов"],
             "en":["Fences","Gates","Gate automation","Fencing","Fence repair"]}.get(lang)
    return _ld({"@context":"https://schema.org","@type":"Person","name":"Artur Mustafin",
        "jobTitle":jt,"image":DOMAIN+"/img/luxaed-w-crew.jpg",
        "worksFor":{"@type":"Organization","name":"LuxAed","url":DOMAIN+"/"},
        "knowsAbout":knows})

def about_page_schema(path, lang, name, desc):
    return _ld({"@context":"https://schema.org","@type":"AboutPage","name":name,"description":desc,
        "url":DOMAIN+path,"inLanguage":lang,
        "mainEntity":{"@type":"HomeAndConstructionBusiness","name":"LuxAed","url":DOMAIN+"/",
            "image":DOMAIN+"/img/luxaed-hero.jpg","telephone":PHONE,"email":EMAIL,"priceRange":"€€",
            "address":{"@type":"PostalAddress","addressLocality":"Tallinn","addressRegion":"Harjumaa","addressCountry":"EE"},
            "areaServed":["Tallinn","Harjumaa","Estonia"],"sameAs":[FB],
            "employee":{"@type":"Person","name":"Artur Mustafin"}}})

def webpage_schema(path, lang, name, desc):
    return _ld({"@context":"https://schema.org","@type":"WebPage","name":name,"description":desc,
        "url":DOMAIN+path,"inLanguage":lang,
        "isPartOf":{"@type":"WebSite","name":"LuxAed","url":DOMAIN+"/"},
        "publisher":{"@type":"Organization","name":"LuxAed","url":DOMAIN+"/"}})

def video_block(lang):
    T = {"et": ("Videod", "Tahate näha, kuidas meistrid töötavad?",
                "Päris kaadrid meie objektidelt: paigaldus, automaatika ja valmis tööd.",
                "Rohkem videoid meie Facebookis →", "Keri kõrvale →",
                "Soovite unistuste aeda?", "Helistage kohe", f"Helista {PHONE}", "Küsi pakkumist →"),
         "ru": ("Видео", "Хотите посмотреть, как работают профессионалы?",
                "Живые кадры с наших объектов: монтаж, автоматика и готовые работы.",
                "Больше видео в нашем Facebook →", "Листайте вбок →",
                "Хотите забор мечты?", "Звоните прямо сейчас", f"Позвонить {PHONE}", "Оставить заявку →"),
         "en": ("Videos", "Want to see our team at work?",
                "Real footage from our sites: installation, automation and finished work.",
                "More videos on our Facebook →", "Swipe sideways →",
                "Want your dream fence?", "Call us right away", f"Call {PHONE}", "Get a quote →")}
    tag, h2, lead, fb, hint, cta_h, cta_sub, cta_call, cta_quote = T.get(lang, T["et"])
    cards = "".join(_reelcard(v, lang) for v in VIDEO_ORDER)
    _arr = {"ru":("Предыдущее","Следующее"),"en":("Previous","Next")}.get(lang,("Eelmine","Järgmine"))
    nav = (f'<div class="reel-nav-top">'
           f'<button class="reel-arrow reel-prev" aria-label="{_arr[0]}" onclick="reelScroll(this,-1)">‹</button>'
           f'<button class="reel-arrow reel-next" aria-label="{_arr[1]}" onclick="reelScroll(this,1)">›</button>'
           f'</div>')
    return (f'<section class="section section--dark vidsec" style="position:relative;overflow:hidden">'
            f'<div style="position:absolute;inset:0;background:url(\'/img/luxaed-sunset.webp\') center 42%/cover no-repeat;pointer-events:none"></div>'
            f'<div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(8,10,16,.95) 0%, rgba(10,12,20,.86) 45%, rgba(8,10,16,.93) 100%);pointer-events:none"></div>'
            f'<div class="wrap" style="position:relative"><div class="vidsec-head">'
            f'<div class="vidsec-intro"><span class="tag">{tag}</span><h2 class="big">{h2}</h2><p class="lead">{lead}</p></div>'
            f'{nav}</div></div>'
            f'<div class="wrap" style="position:relative"><div class="reelwrap"><div class="reelrow">{cards}</div></div>'
            f'<div class="reel-hint">{hint}</div>'
            f'<div style="text-align:center;margin-top:14px"><a class="gal-fb" href="{FB}/reels" '
            f'target="_blank" rel="noopener">{fb}</a></div></div></section>')

def reel_strip(items, tag, h2, lang="et"):
    # compact reels carousel for a service page (no CTA); items: list of (video, caption)
    def card(v, c):
        return (f'<figure class="reelcard" data-src="/img/{v}.mp4" onclick="playReel(this)" '
                f'tabindex="0" role="button" aria-label="{c}" onkeydown="if(event.key===\'Enter\'||event.key===\' \'){{event.preventDefault();playReel(this)}}">'
                f'<picture><source type="image/webp" srcset="/img/{v}-poster.webp"><img class="vid-poster" loading="lazy" decoding="async" src="/img/{v}-poster.jpg" alt="{c}" width="480" height="854"></picture>'
                f'<button class="vid-play" aria-hidden="true" tabindex="-1">▶</button>'
                f'<figcaption>{c}</figcaption></figure>')
    cards = "".join(card(v, c) for v, c in items)
    prev_label, next_label = {
        "ru": ("Предыдущее", "Следующее"),
        "en": ("Previous", "Next"),
    }.get(lang, ("Eelmine", "Järgmine"))
    nav = ('<div class="reel-nav-top">'
           f'<button class="reel-arrow reel-prev" aria-label="{prev_label}" onclick="reelScroll(this,-1)">‹</button>'
           f'<button class="reel-arrow reel-next" aria-label="{next_label}" onclick="reelScroll(this,1)">›</button>'
           '</div>')
    return (f'<section class="section vidsec"><div class="wrap"><div class="vidsec-head">'
            f'<div class="vidsec-intro"><span class="tag">{tag}</span><h2 class="big">{h2}</h2></div>{nav}</div></div>'
            f'<div class="wrap"><div class="reelwrap"><div class="reelrow">{cards}</div></div></div></section>')

def lang_switch(cur_path, lang):
    out=['<div class="lang-switch" role="navigation" aria-label="Keel / Language / Язык">']
    for L,lbl in (("et","ET"),("ru","RU"),("en","EN")):  # ET first (primary language)
        p=alt(cur_path, L)
        a=' is-active' if L==lang else ''
        cur=' aria-current="page"' if L==lang else ''
        out.append(f'<a href="{p}" class="lang-link{a}" hreflang="{L}" lang="{L}"{cur}>{lbl}</a>')
    out.append('</div>')
    return "".join(out)

def nav(lang, cur_path):
    L = NAVLBL[lang]
    home = alt("/", lang); about = alt("/meist/", lang); faq = alt("/kkk/", lang)
    # Service landing pages already contain a preconfigured quote form. Keep the
    # visitor (and the ad query/UTM parameters) on that landing page instead of
    # bouncing them to the language homepage.
    quote_href = "#form" if cur_path == home or any(path == cur_path for path, _ in SVC[lang]) else home + "#form"
    dd = "".join(f'<a href="{u}">{t}</a>' for u,t in SVC[lang])
    ddm = "".join(f'<a class="nm-sub" href="{u}" onclick="closeMob()">{t}</a>' for u,t in SVC[lang])
    mlang = '<div class="nav-mobile-lang">'+"".join(
        f'<a href="{alt(cur_path,L)}" lang="{L}" hreflang="{L}"'+(' aria-current="page" class="is-active"' if L==lang else '')+f'>{lbl}</a>'
        for L,lbl in (("et","ET"),("ru","RU"),("en","EN")))+'</div>'
    return f'''<header class="nav-wrap">
  <nav class="nav-pill">
    <a class="nav-logo" href="{home}" aria-label="LuxAed">{logo_svg()}</a>
    <div class="nav-links">
      <div><button>{L["services"]}</button><div class="dd">{dd}</div></div>
      <a href="{about}">{L["about"]}</a>
      <a href="{faq}">{L["faq"]}</a>
    </div>
    <div class="nav-cta">
      {lang_switch(cur_path, lang)}
      <a class="nav-tel" href="tel:{TEL}">{PHONE}</a>
      <a class="btn btn-accent navcta" href="{quote_href}"><span class="cta-full">{L["cta"]}</span><span class="cta-mini">{L["cta_mini"]}</span> →</a>
      <button class="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="navMobile" onclick="var n=document.querySelector('.nav-mobile');var o=n.classList.toggle('on');this.setAttribute('aria-expanded',o);">☰</button>
    </div>
  </nav>
</header>
<div class="nav-mobile" id="navMobile">
  {mlang}
  <a href="{home}" onclick="closeMob()">{L["home"]}</a>
  {ddm}
  <a href="{about}" onclick="closeMob()">{L["about"]}</a>
  <a href="{faq}" onclick="closeMob()">{L["faq"]}</a>
  <a href="{quote_href}" onclick="closeMob()">{L["cta"]} →</a>
  <div class="lang-phones"><a href="tel:{TEL}"><span class="lp-fl">📞</span> {PHONE}</a></div>
</div>'''

def cookie_banner(lang):
    T={"et":("Kasutame küpsiseid veebisaidi toimimiseks ning teie nõusolekul reklaami tulemuslikkuse mõõtmiseks.","Loe lähemalt","Nõustun","Ainult vajalikud","/privaatsus/"),
       "ru":("Мы используем файлы cookie для работы сайта, аналитики и рекламы.","Подробнее","Принять","Только необходимые","/ru/privaatsus/"),
       "en":("We use cookies to run the site and for analytics and ads.","Learn more","Accept","Only necessary","/en/privacy/")}
    txt,more,acc,dec,priv=T.get(lang,T["et"])
    return (f'<div class="cc-banner" id="ccBanner" role="dialog" aria-label="Cookies">'
            f'<div class="cc-text">{txt} <a href="{priv}">{more}</a></div>'
            f'<div class="cc-actions"><button type="button" class="cc-dec" onclick="ccChoose(0)">{dec}</button>'
            f'<button type="button" class="cc-acc" onclick="ccChoose(1)">{acc}</button></div></div>')

def footer(lang):
    if lang=="et":
        tagline="Aiad ja väravad Tallinnas ja Harjumaal. Tootmine, paigaldus, automaatika ja remont."
        h_s,h_c,h_k,h_hours="Teenused","Ettevõte","Kontakt","Lahtiolekuajad"
        comp=[("/meist/","Meist"),("/kkk/","KKK"),("/privaatsus/","Privaatsus"),("/tingimused/","Tingimused")]
        hours=[("E–R","09–18"),("L","kokkuleppel"),("P","—")]
        rights="Kõik õigused kaitstud."; legal=[("/privaatsus/","Privaatsuspoliitika"),("/tingimused/","Kasutustingimused")]
        addr="Kesklinn, Tallinn,<br>Harjumaa, Eesti"
    elif lang=="en":
        tagline="Fences and gates in Tallinn and Harjumaa. Manufacturing, installation, automation and repair."
        h_s,h_c,h_k,h_hours="Services","Company","Contact","Opening hours"
        comp=[("/en/about/","About"),("/en/faq/","FAQ"),("/en/privacy/","Privacy"),("/en/terms/","Terms")]
        hours=[("Mon–Fri","09–18"),("Sat","by appointment"),("Sun","—")]
        rights="All rights reserved."; legal=[("/en/privacy/","Privacy policy"),("/en/terms/","Terms of service")]
        addr="Kesklinn, Tallinn,<br>Harjumaa, Estonia"
    else:
        tagline="Заборы и ворота в Таллинне и Харьюмаа. Производство, установка, автоматика и ремонт."
        h_s,h_c,h_k,h_hours="Услуги","Компания","Контакты","Время работы"
        comp=[("/ru/o-nas/","О нас"),("/ru/faq/","Вопросы и ответы"),("/ru/privaatsus/","Конфиденциальность"),("/ru/tingimused/","Условия")]
        hours=[("Пн–Пт","09–18"),("Сб","по записи"),("Вс","—")]
        rights="Все права защищены."; legal=[("/ru/privaatsus/","Политика конфиденциальности"),("/ru/tingimused/","Условия обслуживания")]
        addr="Kesklinn, Tallinn,<br>Harjumaa, Estonia"
    svc="".join(f'<a href="{u}">{t}</a>' for u,t in SVC[lang])
    company="".join(f'<a href="{u}">{t}</a>' for u,t in comp)
    hrs="".join(f'<div><span>{a}</span><span>{b}</span></div>' for a,b in hours)
    leg="".join(f'<a href="{u}">{t}</a>' for u,t in legal)
    home=alt("/", lang)
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a class="nav-logo" href="{home}" aria-label="LuxAed">{logo_svg()}</a>
        <p>{tagline}</p>
        <div class="foot-stats"><div><b>{RECOMMEND_PERCENT}%</b><span>{ {"et":"soovitab","en":"recommend"}.get(lang,"рекомендуют") }</span></div><div><b>{REVIEW_COUNT}</b><span>{ {"et":"arvustust","en":"reviews"}.get(lang,"отзыва") }</span></div></div>
      </div>
      <div><h3>{h_s}</h3>{svc}</div>
      <div><h3>{h_c}</h3>{company}</div>
      <div><h3>{h_k}</h3><a href="tel:{TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{FB}" target="_blank" rel="noopener">Facebook</a><address style="font-style:normal;margin-top:8px;color:var(--hero-text-dim);font-size:13px;line-height:1.7">{addr}</address></div>
      <div><h3>{h_hours}</h3><div class="foot-hours">{hrs}</div></div>
    </div>
    <div class="foot-bottom"><span>&copy; {COPYRIGHT_YEAR} LuxAed. {rights}</span><div class="foot-legal">{leg}<a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
    <div class="foot-wordmark" aria-hidden="true">{logo_svg()}</div>
  </div>
</footer>
{cookie_banner(lang)}'''

SCRIPTS = '''<script>
window.__t0=Date.now();
function closeMob(){var n=document.querySelector('.nav-mobile');if(n)n.classList.remove('on');var b=document.querySelector('.burger');if(b)b.setAttribute('aria-expanded','false');}
(function(){var form=document.getElementById('leadForm');if(!form)return;var chips=document.querySelectorAll('#svcChips .chip');var f=document.getElementById('serviceField');function apply(svc){form.querySelectorAll('[data-svc]').forEach(function(el){if(el.classList.contains('chip'))return;var ok=svc&&el.getAttribute('data-svc').split(',').indexOf(svc)>=0;el.style.display=ok?'':'none';});}chips.forEach(function(c){c.addEventListener('click',function(){chips.forEach(function(x){x.classList.remove('on')});c.classList.add('on');var svc=c.getAttribute('data-svc');if(f)f.value=svc;apply(svc);});});var initial=form.getAttribute('data-default-service')||(f&&f.value)||'';if(initial){chips.forEach(function(c){c.classList.toggle('on',c.getAttribute('data-svc')===initial);});if(f)f.value=initial;}apply(initial);})();
(function(){var i=document.getElementById('photoInput'),t=document.getElementById('photoLabel-txt');if(!i||!t)return;i.addEventListener('change',function(){if(i.files&&i.files.length)t.textContent=i.files.length===1?i.files[0].name:((({et:'Faile: ',en:'Files: '})[document.documentElement.lang]||'Файлов: ')+i.files.length);});})();
(function(){document.addEventListener('click',function(e){var a=e.target&&e.target.closest?e.target.closest('a[href^="tel:"]'):null;if(!a)return;var p={event:'phone_click',phone_number:(a.getAttribute('href')||'').replace(/^tel:/,''),link_text:(a.textContent||'').trim().replace(/\\s+/g,' ').slice(0,80),page_path:location.pathname};(window.dataLayer=window.dataLayer||[]).push(p);if(window.gtag)gtag('event','phone_click',{phone_number:p.phone_number,link_text:p.link_text,page_path:p.page_path});});})();
(function(){var form=document.getElementById('leadForm'),ok=document.getElementById('formOk');if(!form)return;form.addEventListener('submit',function(e){e.preventDefault();if(form._gotcha&&form._gotcha.value)return;var btn=form.querySelector('button[type=submit]');btn.disabled=true;var data={};new FormData(form).forEach(function(v,k){if(k!=='photos')data[k]=v;});data.page=location.href;data.t=Math.round((Date.now()-(window.__t0||Date.now()))/1000);
var _fi=document.getElementById('photoInput');var _files=(_fi&&_fi.files)?[].slice.call(_fi.files,0,4):[];
Promise.all(_files.map(function(fl){return new Promise(function(res){var img=new Image();var u=URL.createObjectURL(fl);img.onload=function(){try{var sc=Math.min(1,1600/Math.max(img.width,img.height));var c=document.createElement('canvas');c.width=Math.round(img.width*sc);c.height=Math.round(img.height*sc);c.getContext('2d').drawImage(img,0,0,c.width,c.height);URL.revokeObjectURL(u);res({name:fl.name||'photo.jpg',data:c.toDataURL('image/jpeg',.8).split(',')[1]});}catch(_){res(null);}};img.onerror=function(){URL.revokeObjectURL(u);res(null);};img.src=u;});})).then(function(ph){data.photos_b64=ph.filter(Boolean);
return fetch('/api/lead/',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});}).then(function(r){if(!r.ok)throw 0;ok.style.display='block';(window.dataLayer=window.dataLayer||[]).push({event:'generate_lead',form_service:data.service||''});if(window.gtag){gtag('event','generate_lead',{form_service:data.service||''});gtag('event','conversion',{send_to:'__AW_LEAD_LABEL__',value:1.0,currency:'EUR'});}}).catch(function(){btn.disabled=false;var l=document.documentElement.lang;alert(l==='et'?'Saatmine ebaõnnestus. Palun proovige uuesti või helistage.':l==='en'?'Sending failed. Please try again or call us.':'Не удалось отправить. Попробуйте ещё раз или позвоните.');});});})();
(function(){var items=document.querySelectorAll('.faq-item');items.forEach(function(item){var q=item.querySelector('.faq-q'),a=item.querySelector('.faq-a');q.setAttribute('aria-expanded','false');q.addEventListener('click',function(){var o=item.classList.contains('open');items.forEach(function(i){i.classList.remove('open');i.querySelector('.faq-a').style.maxHeight=null;});if(!o){item.classList.add('open');a.style.maxHeight=a.scrollHeight+'px';}items.forEach(function(i){i.querySelector('.faq-q').setAttribute('aria-expanded',i.classList.contains('open')?'true':'false');});});});})();
(function(){var lb=document.getElementById('lb');if(!lb)return;var im=document.getElementById('lbImg');document.querySelectorAll('#gal a[data-lb]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();im.src=a.getAttribute('href');var g=a.querySelector('img');im.alt=g?g.alt:'';lb.classList.add('on');});});lb.querySelector('.lb-x').addEventListener('click',function(){lb.classList.remove('on')});lb.addEventListener('click',function(e){if(e.target===lb)lb.classList.remove('on')});document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.classList.remove('on')});})();
(function(){if(matchMedia("(prefers-reduced-motion: reduce)").matches)return;var els=document.querySelectorAll(".__no_anim__");var it=[];els.forEach(function(el){var n=el.firstChild;if(!n||n.nodeType!==3)return;var m=n.nodeValue.match(/^(\\d+)(.*)$/);if(!m)return;var t=parseInt(m[1],10);if(t<10)return;it.push({el:el,node:n,t:t,s:m[2]||"",d:false});});if(!it.length)return;function run(x){if(x.d)return;x.d=true;var t0=null;function st(ts){if(t0===null)t0=ts;var p=Math.min((ts-t0)/1400,1),e=1-Math.pow(1-p,3);x.node.nodeValue=Math.round(x.t*e)+x.s;if(p<1)requestAnimationFrame(st);}requestAnimationFrame(st);}var io=new IntersectionObserver(function(en){en.forEach(function(e){if(!e.isIntersecting)return;it.forEach(function(x){if(x.el===e.target)run(x);});io.unobserve(e.target);});},{threshold:.4});it.forEach(function(x){io.observe(x.el)});})();
(function(){var bar=document.querySelector(".mob-bar");if(!bar)return;var vv=window.visualViewport,typing=false,form=document.getElementById("form"),formVisible=false;
function inView(){if(!form)return false;var r=form.getBoundingClientRect();return r.bottom>0&&r.top<window.innerHeight;}
function pin(){if(!vv)return;var o=window.innerHeight-vv.height-vv.offsetTop;bar.style.bottom=(o>0?o:0)+"px";}
function fld(el){return el&&/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName)&&el.type!=="hidden";}
function refresh(){var kb=vv&&(window.innerHeight-vv.height)>140;if(typing||kb||formVisible){bar.style.display="none";}else{bar.style.display="";pin();}}
formVisible=inView();
document.addEventListener("focusin",function(e){if(fld(e.target)){typing=true;refresh();}});
document.addEventListener("focusout",function(e){if(fld(e.target)){setTimeout(function(){if(!fld(document.activeElement)){typing=false;refresh();}},120);}});
if(form&&"IntersectionObserver" in window){new IntersectionObserver(function(entries){formVisible=entries[0].isIntersecting;refresh();},{threshold:.01}).observe(form);}
if(vv){vv.addEventListener("resize",refresh);vv.addEventListener("scroll",refresh);}refresh();})();
(function(){var mob=matchMedia('(max-width:760px)'),rm=matchMedia('(prefers-reduced-motion: reduce)');document.querySelectorAll('.partners-marquee .pm-row').forEach(function(row){
function setRate(r){row.querySelectorAll('.pm-set').forEach(function(set){set.getAnimations().forEach(function(a){a.playbackRate=r;});});}
row.addEventListener('mouseenter',function(){if(!mob.matches)setRate(.3);});row.addEventListener('mouseleave',function(){setRate(1);});
row.addEventListener('touchstart',function(){setRate(0);},{passive:true});row.addEventListener('touchend',function(){setRate(1);},{passive:true});row.addEventListener('touchcancel',function(){setRate(1);},{passive:true});});})();
function fsReq(v){try{if(v.requestFullscreen){v.requestFullscreen();}else if(v.webkitEnterFullscreen){v.webkitEnterFullscreen();}else if(v.webkitRequestFullscreen){v.webkitRequestFullscreen();}else if(v.msRequestFullscreen){v.msRequestFullscreen();}}catch(e){}}
function closeVlb(){var lb=document.getElementById('vlb');if(lb){var v=lb.querySelector('video');try{v.pause();}catch(e){}try{v.currentTime=0;}catch(e){}v.removeAttribute('src');try{v.load();}catch(e){}lb.classList.remove('on');}}
function openVlb(src,poster){var lb=document.getElementById('vlb');if(!lb){lb=document.createElement('div');lb.id='vlb';lb.className='vlb';lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');lb.innerHTML='<button class="vlb-x" aria-label="Close">&times;</button><video class="vlb-video" controls playsinline webkit-playsinline preload="auto"></video>';document.body.appendChild(lb);var vv=lb.querySelector('video');lb.querySelector('.vlb-x').addEventListener('click',closeVlb);lb.addEventListener('click',function(e){if(e.target===lb)closeVlb();});vv.addEventListener('click',function(e){e.stopPropagation();});document.addEventListener('keydown',function(e){if(e.key==='Escape')closeVlb();});}var v=lb.querySelector('video');v.src=src;if(poster)v.poster=poster;lb.classList.add('on');var p=v.play();if(p&&p.catch)p.catch(function(){});}
function resetReel(fig){var v=fig._v;if(v){try{v.pause();}catch(e){}v.remove();fig._v=null;}var b=fig.querySelector('.vid-fs');if(b)b.remove();fig.classList.remove('playing');}
function playReel(fig){var im=fig.querySelector('.vid-poster');openVlb(fig.dataset.src,im?(im.currentSrc||im.src):'');}
document.addEventListener('play',function(e){var t=e.target;if(t&&t.tagName==='VIDEO'){var all=document.getElementsByTagName('video');for(var i=0;i<all.length;i++){if(all[i]!==t){try{all[i].pause();}catch(_){}}}}},true);
// carousel arrows loop around (endless feel)
function reelScroll(btn,dir){var wrap=btn.closest('.vidsec');var row=wrap.querySelector('.reelrow');var step=Math.min(400,row.clientWidth*0.85);if(dir>0){if(row.scrollLeft+row.clientWidth>=row.scrollWidth-8){row.scrollTo({left:0,behavior:'smooth'});return;}}else{if(row.scrollLeft<=8){row.scrollTo({left:row.scrollWidth,behavior:'smooth'});return;}}row.scrollBy({left:dir*step,behavior:'smooth'});}
function ccChoose(all){try{localStorage.setItem('cc',all?'all':'necessary');}catch(e){}if(all&&window.gtag){gtag('consent','update',{ad_storage:'granted',analytics_storage:'granted',ad_user_data:'granted',ad_personalization:'granted'});}var b=document.getElementById('ccBanner');if(b)b.classList.remove('on');}
(function(){var b=document.getElementById('ccBanner');if(!b)return;var c=null;try{c=localStorage.getItem('cc');}catch(e){}if(!c)setTimeout(function(){b.classList.add('on');},600);})();
(function(){var car=document.querySelector(".rev-carousel");if(!car)return;var vp=car.querySelector(".rev-viewport"),track=car.querySelector(".rev-track");var cards=[].slice.call(track.children);if(cards.length<2)return;var i=0,n=cards.length,auto=null;function step(){return (cards[1].offsetLeft-cards[0].offsetLeft)||cards[0].offsetWidth;}function perView(){return Math.max(1,Math.round(vp.offsetWidth/step()));}function maxI(){return Math.max(0,n-perView());}function setX(px){track.style.transform="translateX("+px+"px)";}function go(k){var m=maxI();i=k<0?m:(k>m?0:k);setX(-i*step());}function next(){go(i+1);}function prev(){go(i-1);}function start(){stop();auto=setInterval(next,4500);}function stop(){if(auto){clearInterval(auto);auto=null;}}car.querySelector(".rev-next").addEventListener("click",function(){next();start();});car.querySelector(".rev-prev").addEventListener("click",function(){prev();start();});var down=false,moved=false,sx=0,dx=0;function dS(x){down=true;moved=false;sx=x;dx=0;track.classList.add("is-drag");stop();}function dM(x){if(!down)return;dx=x-sx;if(Math.abs(dx)>5)moved=true;setX(-i*step()+dx);}function dE(){if(!down)return;down=false;track.classList.remove("is-drag");var th=Math.min(80,step()*0.2);if(dx<-th)next();else if(dx>th)prev();else go(i);dx=0;start();}track.addEventListener("mousedown",function(e){dS(e.clientX);});window.addEventListener("mousemove",function(e){dM(e.clientX);});window.addEventListener("mouseup",dE);track.addEventListener("touchstart",function(e){dS(e.touches[0].clientX);},{passive:true});track.addEventListener("touchmove",function(e){dM(e.touches[0].clientX);},{passive:true});track.addEventListener("touchend",dE);track.addEventListener("click",function(e){if(moved){e.preventDefault();e.stopPropagation();}},true);track.addEventListener("dragstart",function(e){e.preventDefault();});car.addEventListener("mouseenter",stop);car.addEventListener("mouseleave",start);window.addEventListener("resize",function(){go(i);});go(0);start();})();
</script>'''
LEAD_FORM_VERSION = hashlib.sha256(open(os.path.join(SITE, "assets", "lead-form.js"), "rb").read()).hexdigest()[:8]
SCRIPTS = SCRIPTS.replace('__AW_LEAD_LABEL__', AW_LEAD_LABEL) + f'\n<script src="/assets/lead-form.js?v={LEAD_FORM_VERSION}" defer></script>'

def head(lang, path, title, desc, og_img="/img/luxaed-hero.jpg", schema_blocks=None):
    row = _row(path) or {lang:path}
    # preload the handwritten Caveat weight the hero kicker uses (per-language script) so it
    # doesn't flash a fallback font on load (kills the FOUT swap on the above-the-fold kicker)
    caveat = "caveat-var-cyrillic.woff2" if lang=="ru" else "caveat-var-latin.woff2"
    canon = DOMAIN + path
    alts = "".join(f'<link rel="alternate" hreflang="{L}" href="{DOMAIN}{row[L]}">' for L in ("ru","et","en") if L in row)
    xdefault = row.get("et", row.get(lang, path))
    alts += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}{xdefault}">'
    sb = "\n".join(schema_blocks or [])
    fav = "/img/luxaed-mark.svg"
    locale = {"et":"et_EE","en":"en_US"}.get(lang,"ru_RU")
    # `og_img` is the page hero and stays page-specific for responsive preloading.
    # Social previews use one versioned 1200x630 image so immutable CDN caches
    # cannot keep an older creative after a release.
    _base = og_img.replace('.jpg','.webp'); _mob = _base.replace('.webp','-mobile.webp')
    _og_url = DOMAIN + SOCIAL_IMAGE
    _og_alt = html.escape(title)
    if os.path.exists(os.path.join(SITE, _mob.lstrip('/'))):
        pre_img = (f'<link rel="preload" as="image" href="{_mob}" media="(max-width:760px)" fetchpriority="high">'
                   f'<link rel="preload" as="image" href="{_base}" media="(min-width:761px)" fetchpriority="high">')
        mob_css = "<style>@media(max-width:760px){.hero-photo-bg{background-image:url('"+_mob+"')!important}}</style>"
    else:
        pre_img = f'<link rel="preload" as="image" href="{_base}" fetchpriority="high">'
        mob_css = ""
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{ ('<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{"gtm.start":new Date().getTime(),event:"gtm.js"}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!="dataLayer"?"&l="+l:"";j.async=true;j.src="https://www.googletagmanager.com/gtm.js?id="+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,"script","dataLayer","'+GTM_ID+'");</script>') if GTM_ID else '' }
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
{alts}
<meta property="og:url" content="{canon}"><meta property="og:type" content="website"><meta property="og:site_name" content="LuxAed">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{_og_url}"><meta property="og:image:secure_url" content="{_og_url}"><meta property="og:image:type" content="image/jpeg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{_og_alt}"><meta property="og:locale" content="{locale}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(title)}"><meta name="twitter:description" content="{html.escape(desc)}"><meta name="twitter:image" content="{_og_url}"><meta name="twitter:image:alt" content="{_og_alt}">
{sb}
<link rel="icon" href="{fav}">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
{pre_img}
<link rel="preload" as="font" type="font/woff2" href="/fonts/{caveat}" crossorigin>
<link rel="stylesheet" href="/assets/luxaed.css">
{mob_css}
{ (lambda _ids=[i for i in (GA_ID, AW_ID) if i]: (
    '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
    'gtag("consent","default",{ad_storage:"denied",analytics_storage:"denied",ad_user_data:"denied",ad_personalization:"denied",wait_for_update:500});'
    'try{if(localStorage.getItem("cc")==="all"){gtag("consent","update",{ad_storage:"granted",analytics_storage:"granted",ad_user_data:"granted",ad_personalization:"granted"});}}catch(e){}'
    'gtag("js",new Date());'
    + "".join(f'gtag("config","{i}");' for i in _ids)
    + 'function __lg(){if(window.__lgd)return;window.__lgd=1;var s=document.createElement("script");s.async=1;s.src="https://www.googletagmanager.com/gtag/js?id=' + _ids[0] + '";document.head.appendChild(s);}'
    + '["scroll","click","touchstart","keydown"].forEach(function(ev){addEventListener(ev,__lg,{passive:true,once:true})});setTimeout(__lg,3500);</script>'
  ) if _ids else '')() }
</head>
<body>
{ ('<noscript><iframe src="https://www.googletagmanager.com/ns.html?id='+GTM_ID+'" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>') if GTM_ID else '' }
<a href="#main" class="skip-link">{ {"et":"Sisu juurde","en":"Skip to content"}.get(lang,"Перейти к содержимому") }</a>'''

def write(path, content):
    fp = os.path.join(SITE, path.strip("/"), "index.html") if path!="/" else os.path.join(SITE,"index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp,"w",encoding="utf-8").write(content)
    return fp
