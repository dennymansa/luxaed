#!/usr/bin/env python3
# LuxAed static page generator. Shared blue moving24 chrome + per-page content.
# Run:  python3 build_pages.py
import os, html

SITE = os.path.dirname(os.path.abspath(__file__))
PHONE = "+372 5695 8285"; TEL = "+37256958285"; EMAIL = "luxaed9@gmail.com"
FB = "https://www.facebook.com/LuxxAed"; DOMAIN = "https://luxaed.ee"

# 3-language path map (page key -> {ru, et, en}) for hreflang + language switch
PAGES = [
 {"ru":"/","et":"/et/","en":"/en/"},
 {"ru":"/uslugi/setka-3d/","et":"/et/aiad/vorkaed/","en":"/en/services/mesh-fence/"},
 {"ru":"/uslugi/derevyannye-zabory/","et":"/et/aiad/puitaed/","en":"/en/services/wooden-fence/"},
 {"ru":"/uslugi/profnastil/","et":"/et/aiad/metallaed/","en":"/en/services/metal-fence/"},
 {"ru":"/uslugi/vorota-kalitki/","et":"/et/varavad/","en":"/en/services/gates-automation/"},
 {"ru":"/uslugi/remont-zaborov/","et":"/et/aia-remont/","en":"/en/services/fence-repair/"},
 {"ru":"/o-nas/","et":"/et/meist/","en":"/en/about/"},
 {"ru":"/faq/","et":"/et/kkk/","en":"/en/faq/"},
 {"ru":"/kontakty/","et":"/et/kontakt/","en":"/en/contact/"},
 {"ru":"/privaatsus/","et":"/et/privaatsus/","en":"/en/privacy/"},
 {"ru":"/tingimused/","et":"/et/tingimused/","en":"/en/terms/"},
]
def _row(path):
    for r in PAGES:
        if path in r.values(): return r
    return PAGES[0]
def alt(path, lang):
    return _row(path).get(lang, "/")

SVC = {  # per-language service dropdown / footer list
 "ru": [("/uslugi/derevyannye-zabory/","Деревянные заборы"),
        ("/uslugi/profnastil/","Заборы из профнастила"),
        ("/uslugi/setka-3d/","Сетчатые/3D-заборы"),
        ("/uslugi/vorota-kalitki/","Ворота, калитки и автоматика"),
        ("/uslugi/remont-zaborov/","Ремонт заборов")],
 "et": [("/et/aiad/puitaed/","Puitaiad"),
        ("/et/aiad/metallaed/","Metallaed"),
        ("/et/aiad/vorkaed/","Võrkaed / paneelaed"),
        ("/et/varavad/","Väravad ja automaatika"),
        ("/et/aia-remont/","Aia remont")],
 "en": [("/en/services/wooden-fence/","Wooden fences"),
        ("/en/services/metal-fence/","Corrugated (metal) fences"),
        ("/en/services/mesh-fence/","Mesh / 3D fences"),
        ("/en/services/gates-automation/","Gates & automation"),
        ("/en/services/fence-repair/","Fence repair")],
}
NAVLBL = {"ru":{"about":"О нас","faq":"Вопросы","contact":"Контакты","services":"Услуги ▾",
               "cta":"Оставить заявку","cta_mini":"Заявка","home":"Главная"},
          "et":{"about":"Meist","faq":"KKK","contact":"Kontakt","services":"Teenused ▾",
               "cta":"Küsi pakkumist","cta_mini":"Päring","home":"Avaleht"},
          "en":{"about":"About","faq":"FAQ","contact":"Contact","services":"Services ▾",
               "cta":"Get a quote","cta_mini":"Quote","home":"Home"}}

def logo_svg():
    return ('<svg width="26" height="26" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            '<rect x="2" y="9" width="3" height="14" fill="#b5542e"/><rect x="8" y="6" width="3" height="17" fill="#b5542e"/>'
            '<rect x="14" y="9" width="3" height="14" fill="#b5542e"/><rect x="20" y="6" width="3" height="17" fill="#b5542e"/>'
            '<rect x="1" y="9" width="23" height="2.4" fill="#ecccb9"/></svg>')

def lang_switch(cur_path, lang):
    out=['<div class="lang-switch" role="navigation" aria-label="Keel / Language / Язык">']
    for L,lbl in (("ru","RU"),("et","ET"),("en","EN")):
        p=alt(cur_path, L)
        a=' is-active' if L==lang else ''
        cur=' aria-current="page"' if L==lang else ''
        out.append(f'<a href="{p}" class="lang-link{a}" hreflang="{L}" lang="{L}"{cur}>{lbl}</a>')
    out.append('</div>')
    return "".join(out)

def nav(lang, cur_path):
    L = NAVLBL[lang]
    home = alt("/", lang); about = alt("/o-nas/", lang); faq = alt("/faq/", lang); contact = alt("/kontakty/", lang)
    dd = "".join(f'<a href="{u}">{t}</a>' for u,t in SVC[lang])
    ddm = "".join(f'<a class="nm-sub" href="{u}" onclick="closeMob()">{t}</a>' for u,t in SVC[lang])
    return f'''<header class="nav-wrap">
  <nav class="nav-pill">
    <a class="nav-logo" href="{home}" aria-label="LuxAed">{logo_svg()}<span>Lux<b>Aed</b></span></a>
    <div class="nav-links">
      <div><button>{L["services"]}</button><div class="dd">{dd}</div></div>
      <a href="{about}">{L["about"]}</a>
      <a href="{faq}">{L["faq"]}</a>
      <a href="{contact}">{L["contact"]}</a>
    </div>
    <div class="nav-cta">
      {lang_switch(cur_path, lang)}
      <a class="nav-tel" href="tel:{TEL}">{PHONE}</a>
      <a class="btn btn-accent navcta" href="{contact}#form"><span class="cta-full">{L["cta"]}</span><span class="cta-mini">{L["cta_mini"]}</span> →</a>
      <button class="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="navMobile" onclick="var n=document.querySelector('.nav-mobile');var o=n.classList.toggle('on');this.setAttribute('aria-expanded',o);">☰</button>
    </div>
  </nav>
</header>
<div class="nav-mobile" id="navMobile">
  <a href="{home}" onclick="closeMob()">{L["home"]}</a>
  {ddm}
  <a href="{about}" onclick="closeMob()">{L["about"]}</a>
  <a href="{faq}" onclick="closeMob()">{L["faq"]}</a>
  <a href="{contact}" onclick="closeMob()">{L["contact"]}</a>
  <a href="{contact}#form" onclick="closeMob()">{L["cta"]} →</a>
  <div class="lang-phones"><a href="tel:{TEL}"><span class="lp-fl">📞</span> {PHONE}</a></div>
</div>'''

def footer(lang):
    if lang=="et":
        tagline="Aiad ja väravad Tallinnas ja Harjumaal. Tootmine, paigaldus, automaatika ja remont."
        h_s,h_c,h_k,h_hours="Teenused","Ettevõte","Kontakt","Lahtiolekuajad"
        comp=[("/et/meist/","Meist"),("/et/kkk/","KKK"),("/et/kontakt/","Kontakt"),("/et/privaatsus/","Privaatsus"),("/et/tingimused/","Tingimused")]
        hours=[("E–R","09–18"),("L","kokkuleppel"),("P","—")]
        rights="Kõik õigused kaitstud."; legal=[("/et/privaatsus/","Privaatsuspoliitika"),("/et/tingimused/","Kasutustingimused")]
        addr="Kesklinn, Tallinn,<br>Harjumaa, Eesti"
    elif lang=="en":
        tagline="Fences and gates in Tallinn and Harjumaa. Manufacturing, installation, automation and repair."
        h_s,h_c,h_k,h_hours="Services","Company","Contact","Opening hours"
        comp=[("/en/about/","About"),("/en/faq/","FAQ"),("/en/contact/","Contact"),("/en/privacy/","Privacy"),("/en/terms/","Terms")]
        hours=[("Mon–Fri","09–18"),("Sat","by appointment"),("Sun","—")]
        rights="All rights reserved."; legal=[("/en/privacy/","Privacy policy"),("/en/terms/","Terms of service")]
        addr="Kesklinn, Tallinn,<br>Harjumaa, Estonia"
    else:
        tagline="Заборы и ворота в Таллинне и Харьюмаа. Производство, установка, автоматика и ремонт."
        h_s,h_c,h_k,h_hours="Услуги","Компания","Контакты","Время работы"
        comp=[("/o-nas/","О нас"),("/faq/","Вопросы и ответы"),("/kontakty/","Контакты"),("/privaatsus/","Конфиденциальность"),("/tingimused/","Условия")]
        hours=[("Пн–Пт","09–18"),("Сб","по записи"),("Вс","—")]
        rights="Все права защищены."; legal=[("/privaatsus/","Политика конфиденциальности"),("/tingimused/","Условия обслуживания")]
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
        <a class="nav-logo" href="{home}" aria-label="LuxAed">{logo_svg()}<span>Lux<b>Aed</b></span></a>
        <p>{tagline}</p>
        <div class="foot-stats"><div><b>100%</b><span>{ {"et":"soovitab","en":"recommend"}.get(lang,"рекомендуют") }</span></div><div><b>34</b><span>{ {"et":"arvustust","en":"reviews"}.get(lang,"отзыва") }</span></div></div>
      </div>
      <div><h3>{h_s}</h3>{svc}</div>
      <div><h3>{h_c}</h3>{company}</div>
      <div><h3>{h_k}</h3><a href="tel:{TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{FB}" target="_blank" rel="noopener">Facebook</a><address style="font-style:normal;margin-top:8px;color:var(--hero-text-dim);font-size:13px;line-height:1.7">{addr}</address></div>
      <div><h3>{h_hours}</h3><div class="foot-hours">{hrs}</div></div>
    </div>
    <div class="foot-bottom"><span>&copy; 2026 LuxAed. {rights}</span><div class="foot-legal">{leg}<a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
    <div class="foot-wordmark">LUX<span>AED</span></div>
  </div>
</footer>'''

SCRIPTS = '''<script>
function closeMob(){var n=document.querySelector('.nav-mobile');if(n)n.classList.remove('on');var b=document.querySelector('.burger');if(b)b.setAttribute('aria-expanded','false');}
(function(){var form=document.getElementById('leadForm');if(!form)return;var chips=document.querySelectorAll('#svcChips .chip');var f=document.getElementById('serviceField');function apply(svc){form.querySelectorAll('[data-svc]').forEach(function(el){if(el.classList.contains('chip'))return;var ok=svc&&el.getAttribute('data-svc').split(',').indexOf(svc)>=0;el.style.display=ok?'':'none';});}chips.forEach(function(c){c.addEventListener('click',function(){chips.forEach(function(x){x.classList.remove('on')});c.classList.add('on');var svc=c.getAttribute('data-svc');if(f)f.value=svc;apply(svc);});});apply('');})();
(function(){var i=document.getElementById('photoInput'),t=document.getElementById('photoLabel-txt');if(!i||!t)return;i.addEventListener('change',function(){if(i.files&&i.files.length)t.textContent=i.files.length===1?i.files[0].name:('Файлов: '+i.files.length);});})();
(function(){var form=document.getElementById('leadForm'),ok=document.getElementById('formOk');if(!form)return;form.addEventListener('submit',function(e){e.preventDefault();if(form._gotcha&&form._gotcha.value)return;ok.style.display='block';form.querySelector('button[type=submit]').disabled=true;});})();
(function(){var items=document.querySelectorAll('.faq-item');items.forEach(function(item){var q=item.querySelector('.faq-q'),a=item.querySelector('.faq-a');q.addEventListener('click',function(){var o=item.classList.contains('open');items.forEach(function(i){i.classList.remove('open');i.querySelector('.faq-a').style.maxHeight=null;});if(!o){item.classList.add('open');a.style.maxHeight=a.scrollHeight+'px';}});});})();
(function(){var lb=document.getElementById('lb');if(!lb)return;var im=document.getElementById('lbImg');document.querySelectorAll('#gal a[data-lb]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();im.src=a.getAttribute('href');var g=a.querySelector('img');im.alt=g?g.alt:'';lb.classList.add('on');});});lb.querySelector('.lb-x').addEventListener('click',function(){lb.classList.remove('on')});lb.addEventListener('click',function(e){if(e.target===lb)lb.classList.remove('on')});document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.classList.remove('on')});})();
(function(){if(matchMedia("(prefers-reduced-motion: reduce)").matches)return;var els=document.querySelectorAll(".__no_anim__");var it=[];els.forEach(function(el){var n=el.firstChild;if(!n||n.nodeType!==3)return;var m=n.nodeValue.match(/^(\\d+)(.*)$/);if(!m)return;var t=parseInt(m[1],10);if(t<10)return;it.push({el:el,node:n,t:t,s:m[2]||"",d:false});});if(!it.length)return;function run(x){if(x.d)return;x.d=true;var t0=null;function st(ts){if(t0===null)t0=ts;var p=Math.min((ts-t0)/1400,1),e=1-Math.pow(1-p,3);x.node.nodeValue=Math.round(x.t*e)+x.s;if(p<1)requestAnimationFrame(st);}requestAnimationFrame(st);}var io=new IntersectionObserver(function(en){en.forEach(function(e){if(!e.isIntersecting)return;it.forEach(function(x){if(x.el===e.target)run(x);});io.unobserve(e.target);});},{threshold:.4});it.forEach(function(x){io.observe(x.el)});})();
(function(){var bar=document.querySelector(".mob-bar");if(!bar)return;var vv=window.visualViewport,typing=false;function pin(){if(!vv)return;var o=window.innerHeight-vv.height-vv.offsetTop;bar.style.bottom=(o>0?o:0)+"px";}function fld(el){return el&&/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName)&&el.type!=="hidden";}function refresh(){var kb=vv&&(window.innerHeight-vv.height)>140;if(typing||kb){bar.style.display="none";}else{bar.style.display="";pin();}}document.addEventListener("focusin",function(e){if(fld(e.target)){typing=true;refresh();}});document.addEventListener("focusout",function(e){if(fld(e.target)){setTimeout(function(){if(!fld(document.activeElement)){typing=false;refresh();}},120);}});if(vv){vv.addEventListener("resize",refresh);vv.addEventListener("scroll",refresh);}refresh();})();
</script>'''

def head(lang, path, title, desc, og_img="/img/luxaed-hero.jpg", schema_blocks=None):
    ru = alt(path,"ru"); et = alt(path,"et"); en = alt(path,"en")
    canon = DOMAIN + path
    alts = (f'<link rel="alternate" hreflang="ru" href="{DOMAIN}{ru}">'
            f'<link rel="alternate" hreflang="et" href="{DOMAIN}{et}">'
            f'<link rel="alternate" hreflang="en" href="{DOMAIN}{en}">'
            f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}{ru}">')
    sb = "\n".join(schema_blocks or [])
    fav = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 26 26'%3E"
           "%3Crect x='2' y='9' width='3' height='14' fill='%23b5542e'/%3E%3Crect x='8' y='6' width='3' height='17' fill='%23b5542e'/%3E"
           "%3Crect x='14' y='9' width='3' height='14' fill='%23b5542e'/%3E%3Crect x='20' y='6' width='3' height='17' fill='%23b5542e'/%3E"
           "%3Crect x='1' y='9' width='23' height='2.4' fill='%23ecccb9'/%3E%3C/svg%3E")
    locale = {"et":"et_EE","en":"en_US"}.get(lang,"ru_RU")
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
{alts}
<meta property="og:url" content="{canon}"><meta property="og:type" content="website"><meta property="og:site_name" content="LuxAed">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{DOMAIN}{og_img}"><meta property="og:locale" content="{locale}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(title)}"><meta name="twitter:image" content="{DOMAIN}{og_img}">
{sb}
<link rel="icon" href="{fav}">
<link rel="preload" as="image" href="{og_img.replace('.jpg','.webp')}" fetchpriority="high">
<link rel="stylesheet" href="/assets/luxaed.css">
</head>
<body>
<a href="#main" class="skip-link">{ {"et":"Sisu juurde","en":"Skip to content"}.get(lang,"Перейти к содержимому") }</a>'''

def write(path, content):
    fp = os.path.join(SITE, path.strip("/"), "index.html") if path!="/" else os.path.join(SITE,"index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp,"w",encoding="utf-8").write(content)
    return fp
