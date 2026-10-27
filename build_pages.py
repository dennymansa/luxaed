#!/usr/bin/env python3
# LuxAed static page generator. Shared shared site chrome + per-page content.
# Run:  python3 build_pages.py
import os, html, hashlib
from service_catalog import LANGS, service_rows, service_nav, service_tiles
from problem_content import PROBLEM_ROWS, GUIDE_ROWS

SITE = os.path.dirname(os.path.abspath(__file__))
PHONE = "+372 5695 8285"; TEL = "+37256958285"; EMAIL = "luxaed9@gmail.com"
FB = "https://www.facebook.com/LuxxAed"; DOMAIN = "https://luxaed.ee"
SOCIAL_IMAGE = "/img/luxaed-og-v2.jpg"
GA_ID = ""   # set to "G-XXXXXXXXXX" for direct GA4 (usually leave empty and use GTM instead)
GTM_ID = "GTM-KFX8R68S"  # LuxAed web container owned by iamdenisg@gmail.com
ADS_ID = ""  # Google Ads tag is loaded by GTM-KFX8R68S (AW-18353611074); a page-level
             # loader used to point at AW-18309429658, which is a different account.
ADS_PHONE_CONVERSION = ""  # phone conversions fire from GTM on the phone_click dataLayer event
REVIEW_COUNT = 34
EXPERIENCE_YEARS = 15
RECOMMEND_PERCENT = 100
COPYRIGHT_YEAR = 2026

# Language path map for hreflang + language switch. Service rows are generated
# from one mandatory ET/RU/EN matrix; a service cannot exist in only one language.
LANG_HOME = {"ru":"/ru/", "et":"/", "en":"/en/"}
PAGES = [{"ru":"/ru/","et":"/","en":"/en/"}] + service_rows() + [
 {"ru":"/ru/ceny/","et":"/hinnad/","en":"/en/prices/"},
 {"ru":"/ru/kak-vybrat-zabor/","et":"/kuidas-valida-aeda/","en":"/en/how-to-choose-a-fence/"},
 {"ru":"/ru/rajony/harjumaa/","et":"/piirkonnad/harjumaa/","en":"/en/areas/harju-county/"},
 {"ru":"/ru/o-nas/","et":"/meist/","en":"/en/about/"},
 {"ru":"/ru/faq/","et":"/kkk/","en":"/en/faq/"},
 {"ru":"/ru/privaatsus/","et":"/privaatsus/","en":"/en/privacy/"},
 {"ru":"/ru/tingimused/","et":"/tingimused/","en":"/en/terms/"},
] + [dict(row) for row in PROBLEM_ROWS] + [dict(row) for row in GUIDE_ROWS]
# Problem pages reuse the service template, so they carry the lead form.
FORM_PAGE_PATHS = {path for row in PROBLEM_ROWS for path in row.values()}
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


def image_fallback(image_name):
    """Return a real fallback asset; a few commissioned visuals are WebP-only."""
    ext = ".jpg" if os.path.exists(os.path.join(SITE, "img", image_name + ".jpg")) else ".webp"
    return f"/img/{image_name}{ext}"

def service_tiles_html(lang):
    """Homepage service cards from the same translated service matrix as nav/sitemap."""
    return "".join(
        f'''<a class="step-ph" href="{path}"><div class="img-wrap"><picture>{webp_sources(image)}<img src="{image_fallback(image)}" alt="{html.escape(title)}" width="600" height="400" loading="lazy"></picture></div>
<div class="sp-top-label"><span>{html.escape(badge)}</span></div><div class="sp-body"><h3>{html.escape(title)}</h3><p>{html.escape(desc)}</p></div></a>'''
        for path, image, badge, title, desc in service_tiles(lang)
    )

SVC = {lang: service_nav(lang) for lang in LANGS}  # nav + footer, one source
NAVLBL = {"ru":{"about":"О нас","faq":"Вопросы","guides":"Советы","prices":"Цены","contact":"Контакты","services":"Услуги ▾",
               "cta":"Оставить заявку","cta_mini":"Заявка","home":"Главная"},
          "et":{"about":"Meist","faq":"KKK","guides":"Nõuanded","prices":"Hinnad","contact":"Kontakt","services":"Teenused ▾",
               "cta":"Küsi pakkumist","cta_mini":"Päring","home":"Avaleht"},
          "en":{"about":"About","faq":"FAQ","guides":"Guides","prices":"Prices","contact":"Contact","services":"Services ▾",
               "cta":"Get a quote","cta_mini":"Quote","home":"Home"}}

def logo_svg():
    # Original LuxAed mark: a subtle fence flanking the central orange arched gate.
    return ('<svg width="46" height="40" viewBox="0 0 30 26" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" '
            'stroke-linecap="round" stroke-linejoin="round">'
            '<g stroke="currentColor" stroke-width="1.4" opacity=".8">'
            '<path d="M2 22 H28"/>'
            '<path d="M4 22 V11 M6.5 22 V11 M23.5 22 V11 M26 22 V11"/>'
            '<path d="M3 11 H7.5 M22.5 11 H27"/></g>'
            '<g stroke="#b5542e" stroke-width="1.6">'
            '<path d="M10 22 V8 M20 22 V8"/>'
            '<path d="M10 8 Q15 4 20 8"/>'
            '<path d="M13 22 V10 M17 22 V10 M15 22 V9"/></g></svg>')

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
  "luxaed-video-puitvarav":{"et":"Puidust liugvärav automaatikaga","ru":"Деревянные откатные ворота с автоматикой","en":"Wooden sliding gate with automation"},
  "luxaed-reel-puitvarav2":{"et":"Puitvärav ja jalgvärav","ru":"Деревянные ворота и калитка","en":"Wooden gate and pedestrian gate"},
  "luxaed-reel-puitaed":  {"et":"Puitaed ja värav","ru":"Деревянный забор и ворота","en":"Wooden fence and gate"},
  "luxaed-reel-valmis":   {"et":"Valmis puit-metallaed","ru":"Готовый забор дерево-металл","en":"Finished wood-and-metal fence"},
  "luxaed-reel-vorkaed":  {"et":"3D paneelaed","ru":"Забор из 3D-сетки","en":"3D mesh panel fence"},
  "luxaed-reel-vorkaed2": {"et":"3D paneelaed heki ääres","ru":"3D-забор вдоль живой изгороди","en":"3D mesh fence by a hedge"},
  "luxaed-reel-metallaed":{"et":"3D paneelaia paigaldus","ru":"Монтаж забора из 3D-сетки","en":"3D mesh fence installation"},
  "luxaed-reel-domofon":  {"et":"Domofoni paigaldus","ru":"Установка домофона","en":"Intercom installation"},
  "luxaed-reel-varav-oht":{"et":"Liugväravad õhtuvalguses","ru":"Откатные ворота вечером","en":"Sliding gates at dusk"},
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
        "areaServed":["Tallinn","Harjumaa"],"sameAs":[FB],
        "geo":{"@type":"GeoCoordinates","latitude":59.437,"longitude":24.7536},
        "openingHoursSpecification":[{"@type":"OpeningHoursSpecification",
            "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],
            "opens":"09:00","closes":"18:00"}]})
# No aggregateRating in the markup: the 34 recommendations live on Facebook, and
# Google's review-snippet rules forbid marking up ratings gathered on other sites.

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
            "areaServed":["Tallinn","Harjumaa"],"sameAs":[FB],
            "employee":{"@type":"Person","name":"Artur Mustafin"}}})

def webpage_schema(path, lang, name, desc):
    return _ld({"@context":"https://schema.org","@type":"WebPage","name":name,"description":desc,
        "url":DOMAIN+path,"inLanguage":lang,
        "isPartOf":{"@type":"WebSite","name":"LuxAed","url":DOMAIN+"/"},
        "publisher":{"@type":"Organization","name":"LuxAed","url":DOMAIN+"/"}})

def video_block(lang):
    T = {"et": ("Videod", "Tahate näha, kuidas meistrid töötavad?",
                "Päris kaadrid meie objektidelt: paigaldus, automaatika ja valmis tööd.",
                "Rohkem videoid meie Facebookis →", "Kerige kõrvale →",
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
    home = alt("/", lang); about = alt("/meist/", lang); faq = alt("/kkk/", lang); prices = alt("/hinnad/", lang); guides = alt("/nouanded/", lang)
    # Service landing pages already contain a preconfigured quote form. Keep the
    # visitor (and the ad query/UTM parameters) on that landing page instead of
    # bouncing them to the language homepage.
    quote_href = "#form" if cur_path == home or cur_path in FORM_PAGE_PATHS or any(path == cur_path for path, _ in SVC[lang]) else home + "#form"
    dd = "".join(f'<a href="{u}">{t}</a>' for u,t in SVC[lang])
    ddm = "".join(f'<a class="nm-sub" href="{u}" onclick="closeMob()">{t}</a>' for u,t in SVC[lang])
    mlang = '<div class="nav-mobile-lang">'+"".join(
        f'<a href="{alt(cur_path,L)}" lang="{L}" hreflang="{L}"'+(' aria-current="page" class="is-active"' if L==lang else '')+f'>{lbl}</a>'
        for L,lbl in (("et","ET"),("ru","RU"),("en","EN")))+'</div>'
    return f'''<header class="nav-wrap">
  <nav class="nav-pill">
    <a class="nav-logo" href="{home}" aria-label="LuxAed">{logo_svg()}<span>Lux<b>Aed</b></span></a>
    <div class="nav-links">
      <div><button>{L["services"]}</button><div class="dd">{dd}</div></div>
      <a href="{prices}">{L["prices"]}</a>
      <a href="{guides}">{L["guides"]}</a>
      <a href="{about}">{L["about"]}</a>
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
  <a href="{prices}" onclick="closeMob()">{L["prices"]}</a>
  <a href="{guides}" onclick="closeMob()">{L["guides"]}</a>
  <a href="{about}" onclick="closeMob()">{L["about"]}</a>
  <a href="{faq}" onclick="closeMob()">{L["faq"]}</a>
  <a href="{quote_href}" onclick="closeMob()">{L["cta"]} →</a>
  <div class="lang-phones"><a href="tel:{TEL}"><span class="lp-fl">📞</span> {PHONE}</a></div>
</div>'''

def cookie_banner(lang):
    T = {
        "et": {
            "aria": "Küpsiste nõusolek", "title": "Küpsised",
            "text": "Kasutame küpsiseid analüütika ja reklaami mõõtmiseks.",
            "more": "Loe lähemalt", "privacy": "/privaatsus/",
            "necessary": "Vajalikud", "necessary_desc": "Vormi, turvalisuse ja nõusolekuvaliku jaoks. Alati aktiivne.",
            "analytics": "Analüütika", "analytics_desc": "Aitab Google Analyticsi kaudu mõista veebisaidi kasutamist.",
            "ads": "Reklaami mõõtmine", "ads_desc": "Google Adsi kampaaniate ja konversioonide mõõtmiseks. Isikupärastatud reklaami ei lubata.",
            "reject": "Ainult vajalikud", "settings": "Seaded", "accept": "Nõustun kõigega", "save": "Salvesta valik",
        },
        "ru": {
            "aria": "Согласие на cookie", "title": "Cookie",
            "text": "Мы используем cookie для аналитики и измерения рекламы.",
            "more": "Подробнее", "privacy": "/ru/privaatsus/",
            "necessary": "Необходимые", "necessary_desc": "Для формы, безопасности и сохранения выбора. Всегда активны.",
            "analytics": "Аналитика", "analytics_desc": "Помогает понять использование сайта через Google Analytics.",
            "ads": "Измерение рекламы", "ads_desc": "Для измерения кампаний и конверсий Google Ads. Персонализация рекламы не включается.",
            "reject": "Только необходимые", "settings": "Настройки", "accept": "Принять все", "save": "Сохранить выбор",
        },
        "en": {
            "aria": "Cookie consent", "title": "Cookies",
            "text": "We use cookies for analytics and advertising measurement.",
            "more": "Learn more", "privacy": "/en/privacy/",
            "necessary": "Necessary", "necessary_desc": "For the form, security and saving your choice. Always active.",
            "analytics": "Analytics", "analytics_desc": "Helps us understand website use through Google Analytics.",
            "ads": "Advertising measurement", "ads_desc": "For measuring Google Ads campaigns and conversions. Ad personalisation is not enabled.",
            "reject": "Necessary only", "settings": "Settings", "accept": "Accept all", "save": "Save selection",
        },
    }
    c = T.get(lang, T["et"])
    return f'''<div class="cc" id="cc" role="dialog" aria-label="{c["aria"]}" aria-live="polite" aria-hidden="true">
  <div class="cc-head"><div class="cc-ico" aria-hidden="true">🍪</div><div><div class="cc-title">{c["title"]}</div><div class="cc-txt">{c["text"]} <a href="{c["privacy"]}">{c["more"]}</a></div></div></div>
  <div class="cc-cats">
    <div class="cc-cat"><span><b>{c["necessary"]}</b><i>{c["necessary_desc"]}</i></span><span class="cc-sw cc-sw--lock" aria-hidden="true"></span></div>
    <div class="cc-cat"><span><b>{c["analytics"]}</b><i>{c["analytics_desc"]}</i></span><span class="cc-sw" data-for="analytics" role="switch" tabindex="0" aria-checked="false" aria-label="{c["analytics"]}"></span></div>
    <div class="cc-cat"><span><b>{c["ads"]}</b><i>{c["ads_desc"]}</i></span><span class="cc-sw" data-for="ads" role="switch" tabindex="0" aria-checked="false" aria-label="{c["ads"]}"></span></div>
  </div>
  <div class="cc-row"><button class="cc-btn cc-dec" type="button">{c["reject"]}</button><button class="cc-btn cc-cust" type="button">{c["settings"]}</button><button class="cc-btn cc-acc" type="button">{c["accept"]}</button></div>
  <div class="cc-row cc-saverow"><button class="cc-btn cc-save" type="button">{c["save"]}</button></div>
</div>'''

FOOT = {
    "et": {"tagline": "Piirdeaedade ja väravate ehitus Tallinnas ja Harjumaal: mõõdistus, paigaldus, automaatika ja remont.",
           "cta": "Küsi pakkumist →", "fences": "Aiad", "gates": "Väravad ja remont", "before": "Enne tellimist",
           "company": "Ettevõte", "contact": "Kontakt", "recommend": "soovitab", "reviews": "arvustust",
           "before_links": [("/hinnad/", "Hinnad 2026"), ("/kuidas-valida-aeda/", "Kuidas valida aeda"), ("panel_vs_mesh", "Võrkaed või 3D paneelaed"),
                            ("gate_guide", "Liugvärav või tiibvärav"), ("permit_guide", "Aia ehitamise luba"), ("municipal_rules", "Aia kõrgus Harjumaal"), ("/kkk/", "KKK"), ("hub", "Kõik nõuanded →")],
           "company_links": [("/meist/", "Meist"), ("/piirkonnad/harjumaa/", "Teeninduspiirkond")],
           "problems": [("gate_wont_open", "Värav ei avane"), ("sliding_gate", "Liugvärava remont"), ("leaning_fence", "Viltu aed, logisev post"), ("damaged_fence", "Tormi- või autokahju")],
           "hours": [("E–R", "09–18"), ("L", "kokkuleppel"), ("P", "suletud")],
           "rights": "Kõik õigused kaitstud.", "legal": [("/privaatsus/", "Privaatsuspoliitika"), ("/tingimused/", "Kasutustingimused")],
           "cookie": "Küpsiste seaded", "addr": "Kesklinn, Tallinn,<br>Harjumaa, Eesti"},
    "ru": {"tagline": "Установка заборов и ворот в Таллинне и Харьюмаа: замер, монтаж, автоматика и ремонт.",
           "cta": "Оставить заявку →", "fences": "Заборы", "gates": "Ворота и ремонт", "before": "Перед заказом",
           "company": "Компания", "contact": "Контакты", "recommend": "рекомендуют", "reviews": "отзыва",
           "before_links": [("/ru/ceny/", "Цены 2026"), ("/ru/kak-vybrat-zabor/", "Как выбрать забор"), ("panel_vs_mesh", "Сетка-рабица или 3D-панели"),
                            ("gate_guide", "Откатные или распашные ворота"), ("permit_guide", "Разрешение на забор"), ("municipal_rules", "Высота забора в Харьюмаа"), ("/ru/faq/", "Вопросы и ответы"), ("hub", "Все советы →")],
           "company_links": [("/ru/o-nas/", "О нас"), ("/ru/rajony/harjumaa/", "Где мы работаем")],
           "problems": [("gate_wont_open", "Не открываются ворота"), ("sliding_gate", "Ремонт откатных ворот"), ("leaning_fence", "Покосился забор"), ("damaged_fence", "Повреждение бурей или машиной")],
           "hours": [("Пн–Пт", "09–18"), ("Сб", "по записи"), ("Вс", "выходной")],
           "rights": "Все права защищены.", "legal": [("/ru/privaatsus/", "Политика конфиденциальности"), ("/ru/tingimused/", "Условия обслуживания")],
           "cookie": "Настройки cookie", "addr": "Кесклинн, Таллинн,<br>Харьюмаа, Эстония"},
    "en": {"tagline": "Fence and gate installation in Tallinn and Harju County: measuring, installation, automation and repair.",
           "cta": "Get a quote →", "fences": "Fences", "gates": "Gates & repair", "before": "Before you order",
           "company": "Company", "contact": "Contact", "recommend": "recommend", "reviews": "reviews",
           "before_links": [("/en/prices/", "Prices 2026"), ("/en/how-to-choose-a-fence/", "How to choose a fence"), ("panel_vs_mesh", "Chain-link or 3D panels"),
                            ("gate_guide", "Sliding or swing gate"), ("permit_guide", "Fence permits"), ("municipal_rules", "Fence height rules"), ("/en/faq/", "FAQ"), ("hub", "All guides →")],
           "company_links": [("/en/about/", "About us"), ("/en/areas/harju-county/", "Service area")],
           "problems": [("gate_wont_open", "Gate won't open"), ("sliding_gate", "Sliding gate repair"), ("leaning_fence", "Leaning fence or loose post"), ("damaged_fence", "Storm or car damage")],
           "hours": [("Mon–Fri", "09–18"), ("Sat", "by appointment"), ("Sun", "closed")],
           "rights": "All rights reserved.", "legal": [("/en/privacy/", "Privacy policy"), ("/en/terms/", "Terms of service")],
           "cookie": "Cookie settings", "addr": "Kesklinn, Tallinn,<br>Harju County, Estonia"},
}


def _foot_path(key, lang):
    from problem_content import (GATE_WONT_OPEN, SLIDING_GATE, LEANING_FENCE, DAMAGED_FENCE,
                                 GATE_GUIDE, PERMIT_GUIDE, HUB_ROW, ARTICLES)
    if key.startswith("/"):
        return key
    rows = {"gate_wont_open": GATE_WONT_OPEN, "sliding_gate": SLIDING_GATE, "leaning_fence": LEANING_FENCE,
            "damaged_fence": DAMAGED_FENCE, "gate_guide": GATE_GUIDE, "permit_guide": PERMIT_GUIDE, "hub": HUB_ROW}
    rows.update(ARTICLES)
    return rows[key][lang]


def _foot_col(title, links):
    items = "".join(f'<a href="{href}">{label}</a>' for href, label in links)
    return (f'<details class="foot-acc" open><summary><h3>{title}</h3></summary>'
            f'<div class="foot-links">{items}</div></details>')


def footer(lang):
    f = FOOT[lang]
    home = alt("/", lang)
    services = SVC[lang]
    fences = services[:6]
    gates = services[6:9] + [(_foot_path(key, lang), label) for key, label in f["problems"]]
    before = [(_foot_path(key, lang), label) for key, label in f["before_links"]]
    company = [(_foot_path(key, lang), label) for key, label in f["company_links"]]
    hrs = "".join(f'<div><span>{a}</span><span>{b}</span></div>' for a, b in f["hours"])
    leg = "".join(f'<a href="{u}">{t}</a>' for u, t in f["legal"])
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a class="nav-logo" href="{home}" aria-label="LuxAed">{logo_svg()}<span>Lux<b>Aed</b></span></a>
        <p>{f["tagline"]}</p>
        <div class="foot-stats"><div><b>{RECOMMEND_PERCENT}%</b><span>{f["recommend"]}</span></div><div><b>{REVIEW_COUNT}</b><span>{f["reviews"]}</span></div></div>
        <a class="btn btn-accent foot-cta" href="{home}#form">{f["cta"]}</a>
      </div>
      <nav class="foot-col" aria-label="{f["fences"]}">{_foot_col(f["fences"], fences)}</nav>
      <nav class="foot-col" aria-label="{f["gates"]}">{_foot_col(f["gates"], gates)}</nav>
      <nav class="foot-col" aria-label="{f["before"]}">{_foot_col(f["before"], before)}</nav>
      <nav class="foot-col" aria-label="{f["company"]}">{_foot_col(f["company"], company)}</nav>
      <div class="foot-contact"><h3>{f["contact"]}</h3><a href="tel:{TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{FB}" target="_blank" rel="noopener">Facebook</a><address style="font-style:normal;margin-top:8px;color:var(--hero-text-dim);font-size:13px;line-height:1.7">{f["addr"]}</address><div class="foot-hours">{hrs}</div></div>
    </div>
    <div class="foot-bottom"><span>&copy; {COPYRIGHT_YEAR} LuxAed. {f["rights"]}</span><div class="foot-legal">{leg}<a href="#cc" data-cookie-settings>{f["cookie"]}</a></div></div>
    <div class="foot-wordmark">LUX<span>AED</span></div>
  </div>
</footer>
{cookie_banner(lang)}'''

SCRIPTS = '''<script>
window.__t0=Date.now();
function closeMob(){var n=document.querySelector('.nav-mobile');if(n)n.classList.remove('on');var b=document.querySelector('.burger');if(b)b.setAttribute('aria-expanded','false');}
(function(){if(!window.matchMedia||!matchMedia('(max-width:760px)').matches)return;document.querySelectorAll('.foot-acc[open]').forEach(function(d){d.removeAttribute('open');});})();
(function(){var form=document.getElementById('leadForm');if(!form)return;var chips=document.querySelectorAll('#svcChips .chip');var f=document.getElementById('serviceField');function apply(svc){form.querySelectorAll('[data-svc]').forEach(function(el){if(el.classList.contains('chip'))return;var ok=svc&&el.getAttribute('data-svc').split(',').indexOf(svc)>=0;el.style.display=ok?'':'none';});}chips.forEach(function(c){c.addEventListener('click',function(){chips.forEach(function(x){x.classList.remove('on')});c.classList.add('on');var svc=c.getAttribute('data-svc');if(f)f.value=svc;apply(svc);});});var initial=form.getAttribute('data-default-service')||(f&&f.value)||'';if(initial){chips.forEach(function(c){c.classList.toggle('on',c.getAttribute('data-svc')===initial);});if(f)f.value=initial;}apply(initial);})();
(function(){var i=document.getElementById('photoInput'),t=document.getElementById('photoLabel-txt');if(!i||!t)return;i.addEventListener('change',function(){if(i.files&&i.files.length)t.textContent=i.files.length===1?i.files[0].name:((({et:'Faile: ',en:'Files: '})[document.documentElement.lang]||'Файлов: ')+i.files.length);});})();
(function(){document.addEventListener('click',function(e){var a=e.target&&e.target.closest?e.target.closest('a[href^="tel:"],a[href^="mailto:"]'):null;if(!a)return;var href=a.getAttribute('href')||'',isPhone=href.indexOf('tel:')===0,p={event:isPhone?'phone_click':'email_link_click',link_text:(a.textContent||'').trim().replace(/\\s+/g,' ').slice(0,80),page_path:location.pathname};if(isPhone)p.phone_number=href.replace(/^tel:/,'');(window.dataLayer=window.dataLayer||[]).push(p);});})();
(function(){var form=document.getElementById('leadForm'),ok=document.getElementById('formOk');if(!form)return;form.addEventListener('submit',function(e){e.preventDefault();if(form._gotcha&&form._gotcha.value)return;var btn=form.querySelector('button[type=submit]');btn.disabled=true;var data={};new FormData(form).forEach(function(v,k){if(k!=='photos')data[k]=v;});data.page=location.href;data.t=Math.round((Date.now()-(window.__t0||Date.now()))/1000);
var _fi=document.getElementById('photoInput');var _files=(_fi&&_fi.files)?[].slice.call(_fi.files,0,4):[];
Promise.all(_files.map(function(fl){return new Promise(function(res){var img=new Image();var u=URL.createObjectURL(fl);img.onload=function(){try{var sc=Math.min(1,1600/Math.max(img.width,img.height));var c=document.createElement('canvas');c.width=Math.round(img.width*sc);c.height=Math.round(img.height*sc);c.getContext('2d').drawImage(img,0,0,c.width,c.height);URL.revokeObjectURL(u);res({name:fl.name||'photo.jpg',data:c.toDataURL('image/jpeg',.8).split(',')[1]});}catch(_){res(null);}};img.onerror=function(){URL.revokeObjectURL(u);res(null);};img.src=u;});})).then(function(ph){data.photos_b64=ph.filter(Boolean);
return fetch('/api/lead/',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});}).then(function(r){if(!r.ok)throw 0;ok.style.display='block';(window.dataLayer=window.dataLayer||[]).push({event:'generate_lead',form_id:'leadForm',form_service:data.service||'',value:1,currency:'EUR',page_path:location.pathname});}).catch(function(){btn.disabled=false;var l=document.documentElement.lang;alert(l==='et'?'Saatmine ebaõnnestus. Palun proovige uuesti või helistage.':l==='en'?'Sending failed. Please try again or call us.':'Не удалось отправить. Попробуйте ещё раз или позвоните.');});});})();
(function(){var items=document.querySelectorAll('.faq-item');items.forEach(function(item){var q=item.querySelector('.faq-q'),a=item.querySelector('.faq-a');q.setAttribute('aria-expanded','false');q.addEventListener('click',function(){var o=item.classList.contains('open');items.forEach(function(i){i.classList.remove('open');i.querySelector('.faq-a').style.maxHeight=null;});if(!o){item.classList.add('open');a.style.maxHeight=a.scrollHeight+'px';}items.forEach(function(i){i.querySelector('.faq-q').setAttribute('aria-expanded',i.classList.contains('open')?'true':'false');});});});})();
(function(){var lb=document.getElementById('lb');if(!lb)return;var im=document.getElementById('lbImg');document.querySelectorAll('#gal a[data-lb]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();im.src=a.getAttribute('href');var g=a.querySelector('img');im.alt=g?g.alt:'';lb.classList.add('on');});});lb.querySelector('.lb-x').addEventListener('click',function(){lb.classList.remove('on')});lb.addEventListener('click',function(e){if(e.target===lb)lb.classList.remove('on')});document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.classList.remove('on')});})();
(function(){if(matchMedia("(prefers-reduced-motion: reduce)").matches)return;var els=document.querySelectorAll(".__no_anim__");var it=[];els.forEach(function(el){var n=el.firstChild;if(!n||n.nodeType!==3)return;var m=n.nodeValue.match(/^(\\d+)(.*)$/);if(!m)return;var t=parseInt(m[1],10);if(t<10)return;it.push({el:el,node:n,t:t,s:m[2]||"",d:false});});if(!it.length)return;function run(x){if(x.d)return;x.d=true;var t0=null;function st(ts){if(t0===null)t0=ts;var p=Math.min((ts-t0)/1400,1),e=1-Math.pow(1-p,3);x.node.nodeValue=Math.round(x.t*e)+x.s;if(p<1)requestAnimationFrame(st);}requestAnimationFrame(st);}var io=new IntersectionObserver(function(en){en.forEach(function(e){if(!e.isIntersecting)return;it.forEach(function(x){if(x.el===e.target)run(x);});io.unobserve(e.target);});},{threshold:.4});it.forEach(function(x){io.observe(x.el)});})();
(function(){var bar=document.querySelector(".mob-bar");if(!bar)return;var vv=window.visualViewport,typing=false;
function pin(){if(!vv)return;var o=window.innerHeight-vv.height-vv.offsetTop;bar.style.bottom=(o>0?o:0)+"px";}
function fld(el){return el&&/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName)&&el.type!=="hidden";}
function refresh(){var kb=vv&&(window.innerHeight-vv.height)>140;if(typing||kb){bar.style.display="none";}else{bar.style.display="";pin();}}
document.addEventListener("focusin",function(e){if(fld(e.target)){typing=true;refresh();}});
document.addEventListener("focusout",function(e){if(fld(e.target)){setTimeout(function(){if(!fld(document.activeElement)){typing=false;refresh();}},120);}});
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
(function(){var KEY="luxaed_consent_v3",VERSION=3,MAX_AGE=15552000000,cc=document.getElementById("cc");if(!cc)return;
function read(){try{var v=JSON.parse(localStorage.getItem(KEY)||"null");if(v&&v.v===VERSION&&typeof v.a==="boolean"&&typeof v.d==="boolean"&&Date.now()-Number(v.t||0)<MAX_AGE)return v;var old=localStorage.getItem("cc");if(old==="all"||old==="necessary"){v={v:VERSION,a:old==="all",d:old==="all",t:Date.now()};localStorage.setItem(KEY,JSON.stringify(v));localStorage.removeItem("cc");return v;}}catch(e){}return null;}
function apply(a,d){if(window.gtag)gtag("consent","update",{analytics_storage:a?"granted":"denied",ad_storage:d?"granted":"denied",ad_user_data:d?"granted":"denied",ad_personalization:"denied"});try{dataLayer.push({event:"consent_update",consent_analytics:!!a,consent_ads:!!d,consent_ad_personalization:false});}catch(e){}}
function clearOptional(kind){try{document.cookie.split(";").forEach(function(part){var n=part.split("=")[0].trim(),ok=kind==="analytics"?(/^_ga(?:_|$)/.test(n)||n==="_gid"||n==="_gat"):/^_(?:gcl|gac)(?:_|$)/.test(n);if(!ok)return;var root=location.hostname.replace(/^www\\./,"");["","; domain="+location.hostname,"; domain=."+root].forEach(function(dom){document.cookie=n+"=; Max-Age=0; path=/; SameSite=Lax"+dom;});});}catch(e){}}
function setSwitch(n,on){var sw=cc.querySelector('.cc-sw[data-for="'+n+'"]');if(!sw)return;sw.classList.toggle("cc-sw--on",!!on);sw.setAttribute("aria-checked",on?"true":"false");}
function sync(){var v=read()||{a:false,d:false};setSwitch("analytics",v.a);setSwitch("ads",v.d);}
function show(open){sync();cc.classList.add("show");cc.classList.toggle("cc-open",!!open);cc.setAttribute("aria-hidden","false");}
function hide(){cc.classList.remove("show","cc-open");cc.setAttribute("aria-hidden","true");}
function save(a,d){var v={v:VERSION,a:!!a,d:!!d,t:Date.now()};try{localStorage.setItem(KEY,JSON.stringify(v));localStorage.removeItem("cc");}catch(e){}apply(v.a,v.d);if(!v.a)clearOptional("analytics");if(!v.d)clearOptional("ads");hide();}
function state(n){var sw=cc.querySelector('.cc-sw[data-for="'+n+'"]');return!!(sw&&sw.classList.contains("cc-sw--on"));}
function flip(sw){var on=!sw.classList.contains("cc-sw--on");sw.classList.toggle("cc-sw--on",on);sw.setAttribute("aria-checked",on?"true":"false");}
window.luxaedOpenCookieSettings=function(){show(true);};
document.querySelectorAll("[data-cookie-settings]").forEach(function(a){a.addEventListener("click",function(e){e.preventDefault();show(true);});});
cc.querySelectorAll(".cc-sw[data-for]").forEach(function(sw){sw.addEventListener("click",function(){flip(sw);});sw.addEventListener("keydown",function(e){if(e.key===" "||e.key==="Enter"){e.preventDefault();flip(sw);}});});
cc.querySelector(".cc-cust").addEventListener("click",function(){show(true);});
cc.querySelector(".cc-dec").addEventListener("click",function(){save(false,false);});
cc.querySelector(".cc-acc").addEventListener("click",function(){save(true,true);});
cc.querySelector(".cc-save").addEventListener("click",function(){save(state("analytics"),state("ads"));});
var stored=read();if(stored){apply(stored.a,stored.d);if(!stored.a)clearOptional("analytics");if(!stored.d)clearOptional("ads");}else{var reveal=function(){show(false);};if(document.fonts&&document.fonts.ready){var shown=false,once=function(){if(shown)return;shown=true;reveal();};document.fonts.ready.then(once);setTimeout(once,2500);}else{reveal();}}
})();
(function(){var car=document.querySelector(".rev-carousel");if(!car)return;var vp=car.querySelector(".rev-viewport"),track=car.querySelector(".rev-track");var cards=[].slice.call(track.children);if(cards.length<2)return;var i=0,n=cards.length,auto=null;function step(){return (cards[1].offsetLeft-cards[0].offsetLeft)||cards[0].offsetWidth;}function perView(){return Math.max(1,Math.round(vp.offsetWidth/step()));}function maxI(){return Math.max(0,n-perView());}function setX(px){track.style.transform="translateX("+px+"px)";}function go(k){var m=maxI();i=k<0?m:(k>m?0:k);setX(-i*step());}function next(){go(i+1);}function prev(){go(i-1);}function start(){stop();auto=setInterval(next,4500);}function stop(){if(auto){clearInterval(auto);auto=null;}}car.querySelector(".rev-next").addEventListener("click",function(){next();start();});car.querySelector(".rev-prev").addEventListener("click",function(){prev();start();});var down=false,moved=false,sx=0,dx=0;function dS(x){down=true;moved=false;sx=x;dx=0;track.classList.add("is-drag");stop();}function dM(x){if(!down)return;dx=x-sx;if(Math.abs(dx)>5)moved=true;setX(-i*step()+dx);}function dE(){if(!down)return;down=false;track.classList.remove("is-drag");var th=Math.min(80,step()*0.2);if(dx<-th)next();else if(dx>th)prev();else go(i);dx=0;start();}track.addEventListener("mousedown",function(e){dS(e.clientX);});window.addEventListener("mousemove",function(e){dM(e.clientX);});window.addEventListener("mouseup",dE);track.addEventListener("touchstart",function(e){dS(e.touches[0].clientX);},{passive:true});track.addEventListener("touchmove",function(e){dM(e.touches[0].clientX);},{passive:true});track.addEventListener("touchend",dE);track.addEventListener("click",function(e){if(moved){e.preventDefault();e.stopPropagation();}},true);track.addEventListener("dragstart",function(e){e.preventDefault();});car.addEventListener("mouseenter",stop);car.addEventListener("mouseleave",start);window.addEventListener("resize",function(){go(i);});go(0);start();})();
</script>'''
SCRIPTS = SCRIPTS.replace("__ADS_PHONE_CONVERSION__", ADS_PHONE_CONVERSION)
LEAD_FORM_VERSION = hashlib.sha256(open(os.path.join(SITE, "assets", "lead-form.js"), "rb").read()).hexdigest()[:8]
SCRIPTS += f'\n<script src="/assets/lead-form.js?v={LEAD_FORM_VERSION}" defer></script>'
# Vercel Web Analytics: cookieless, no personal data, so it does not wait for the cookie banner.
# Enable it in Vercel -> Project -> Analytics. The 'lead' custom event is sent from lead-form.js.
VERCEL_ANALYTICS = ('<script>window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };</script>'
                    '\n<script defer src="/_vercel/insights/script.js"></script>')
SCRIPTS += '\n' + VERCEL_ANALYTICS

FAVICON = ("data:image/svg+xml,%3Csvg%20xmlns%3D%27http://www.w3.org/2000/svg%27%20viewBox%3D%270%200%2026%2026%27%20fill%3D%27none%27%20stroke%3D%27%23b5542e%27%20stroke-width%3D%272%27%20stroke-linecap%3D%27round%27%20stroke-linejoin%3D%27round%27%3E%3Cpath%20d%3D%27M4%2022%20H22%27/%3E%3Cpath%20d%3D%27M8%2022%20V9%20M18%2022%20V9%27/%3E%3Cpath%20d%3D%27M8%209%20Q13%204.5%2018%209%27/%3E%3Cpath%20d%3D%27M11%2022%20V11%20M15%2022%20V11%20M13%2022%20V10%27/%3E%3C/svg%3E")


def tracking_head():
    """Render Consent Mode, the LuxAed Ads destination, and the GTM container."""
    consent = '''<script>
window.dataLayer=window.dataLayer||[];
function gtag(){dataLayer.push(arguments);}
gtag("consent","default",{ad_storage:"denied",analytics_storage:"denied",ad_user_data:"denied",ad_personalization:"denied",wait_for_update:500});
gtag("set","ads_data_redaction",true);
gtag("set","url_passthrough",true);
(function(){try{var k="luxaed_consent_v3",max=15552000000,v=JSON.parse(localStorage.getItem(k)||"null");if(!(v&&v.v===3&&typeof v.a==="boolean"&&typeof v.d==="boolean"&&Date.now()-Number(v.t||0)<max)){var old=localStorage.getItem("cc");if(old==="all"||old==="necessary"){v={v:3,a:old==="all",d:old==="all",t:Date.now()};localStorage.setItem(k,JSON.stringify(v));localStorage.removeItem("cc");}else{v=null;}}if(v){gtag("consent","update",{analytics_storage:v.a?"granted":"denied",ad_storage:v.d?"granted":"denied",ad_user_data:v.d?"granted":"denied",ad_personalization:"denied"});}}catch(e){}})();
</script>'''
    ads_loader = '''<script async src="https://www.googletagmanager.com/gtag/js?id=__ADS_ID__"></script>
<script>gtag("js",new Date());gtag("config","__ADS_ID__");</script>'''.replace("__ADS_ID__", ADS_ID) if ADS_ID else ""
    if GTM_ID:
        loader = '''<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({"gtm.start":new Date().getTime(),event:"gtm.js"});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!="dataLayer"?"&l="+l:"";j.async=true;j.src="https://www.googletagmanager.com/gtm.js?id="+i+dl;f.parentNode.insertBefore(j,f);})(window,document,"script","dataLayer","__GTM_ID__");</script>'''
        return "<!-- LUX_TRACKING_START -->\n" + consent + ads_loader + "\n" + loader.replace("__GTM_ID__", GTM_ID) + "\n<!-- LUX_TRACKING_END -->"
    if GA_ID:
        direct = '''<script>
gtag("js",new Date());
gtag("config","__GA_ID__");
(function(){function load(){if(window.__luxGaLoaded)return;window.__luxGaLoaded=1;var s=document.createElement("script");s.async=true;s.src="https://www.googletagmanager.com/gtag/js?id=__GA_ID__";document.head.appendChild(s);}["scroll","click","touchstart","keydown"].forEach(function(ev){addEventListener(ev,load,{passive:true,once:true});});setTimeout(load,3500);})();
</script>'''
        return "<!-- LUX_TRACKING_START -->\n" + consent + direct.replace("__GA_ID__", GA_ID) + "\n<!-- LUX_TRACKING_END -->"
    return ""


def tracking_body():
    if not GTM_ID:
        return ""
    return ('<!-- LUX_GTM_NOSCRIPT_START -->'
            '<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=' + GTM_ID + '" '
            'height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>'
            '<!-- LUX_GTM_NOSCRIPT_END -->')


def head(lang, path, title, desc, og_img="/img/luxaed-hero.jpg", schema_blocks=None, og_type="website"):
    row = _row(path) or {lang:path}
    # preload the handwritten Caveat weight the hero kicker uses (per-language script) so it
    # doesn't flash a fallback font on load (kills the FOUT swap on the above-the-fold kicker)
    caveat = "caveat-var-cyrillic.woff2" if lang=="ru" else "caveat-var-latin.woff2"
    canon = DOMAIN + path
    alts = "".join(f'<link rel="alternate" hreflang="{L}" href="{DOMAIN}{row[L]}">' for L in ("ru","et","en") if L in row)
    xdefault = row.get("et", row.get(lang, path))
    alts += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}{xdefault}">'
    sb = "\n".join(schema_blocks or [])
    if path not in ("/", "/ru/", "/en/") and '"BreadcrumbList"' not in sb and "404" not in path:
        # pages without their own trail (about, FAQ, legal) get Home > page
        import json, re
        home = {"et": "/", "ru": "/ru/", "en": "/en/"}[lang]
        crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": {"et": "Avaleht", "ru": "Главная", "en": "Home"}[lang], "item": DOMAIN + home},
            {"@type": "ListItem", "position": 2, "name": re.sub(r"\s*[|\u2014\u2013-]\s*LuxAed\s*$", "", title), "item": DOMAIN + path}]}
        sb += "\n" + '<script type="application/ld+json">' + json.dumps(crumb, ensure_ascii=False) + "</script>"
    locales = {"et": "et_EE", "ru": "ru_RU", "en": "en_GB"}
    locale = locales[lang]
    locale_alts = "".join(f'<meta property="og:locale:alternate" content="{locales[L]}">' for L in ("et", "ru", "en") if L in row and L != lang)
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
{tracking_head()}
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
{alts}
<meta property="og:url" content="{canon}"><meta property="og:type" content="{og_type}"><meta property="og:site_name" content="LuxAed">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{_og_url}"><meta property="og:image:secure_url" content="{_og_url}"><meta property="og:image:type" content="image/jpeg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{_og_alt}"><meta property="og:locale" content="{locale}">{locale_alts}
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(title)}"><meta name="twitter:description" content="{html.escape(desc)}"><meta name="twitter:image" content="{_og_url}"><meta name="twitter:image:alt" content="{_og_alt}">
{sb}
<link rel="icon" href="{FAVICON}">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
{pre_img}
<link rel="preload" as="font" type="font/woff2" href="/fonts/{caveat}" crossorigin>
<link rel="stylesheet" href="/assets/luxaed.css">
{mob_css}
</head>
<body>
{tracking_body()}
<a href="#main" class="skip-link">{ {"et":"Sisu juurde","en":"Skip to content"}.get(lang,"Перейти к содержимому") }</a>'''

def write(path, content):
    fp = os.path.join(SITE, path.strip("/"), "index.html") if path!="/" else os.path.join(SITE,"index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp,"w",encoding="utf-8").write(content)
    return fp
