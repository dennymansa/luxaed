#!/usr/bin/env python3
"""Shared ET/RU/EN service-page renderer.

Language files contain only translated content. Structure, schema, sections,
stats and conditional modules live here so a layout change reaches all service
pages in all languages in one build.
"""
import html
import json

from build_pages import (
    DOMAIN, EMAIL, EXPERIENCE_YEARS, FB, PHONE, RECOMMEND_PERCENT,
    REVIEW_COUNT, SCRIPTS, SVC, TEL, footer, head, nav, reel_strip,
    webp_sources, write,
)
from lead_form import render_lead_form


UI = {
    "et": {
        "home": "Avaleht", "services": "Teenused", "services_anchor": "/#teenused",
        "prompt": "Hei! Vajad uut aeda?", "trust": "arvustust Facebookis · soovitavad",
        "recommend": "soovitavad Facebookis", "reviews": "arvustust", "experience": "aastat kogemust",
        "quote": "Küsi pakkumist", "call": "Helista", "close": "Sulge",
        "get_tag": "Mida saate", "options": "Valikud", "local": "Tallinn ja Harjumaa",
        "price_tag": "Ausalt hinnast", "price_h": "Millest sõltub hind",
        "price_p": "Fikseeritud hinnakirja ei ole. Täpse hinna ütleme pärast tasuta mõõdistust.",
        "included": "Alati hinna sees", "affects": "Mõjutab hinda",
        "year_round": "Töötame aastaringselt, ka talvel", "warranty": "Garantii tehtud töödele",
        "process_tag": "Kuidas töötame", "process_h": "Neli lihtsat sammu",
        "gallery": "Galerii", "gallery_h": "Tehtud tööde näited", "more_photos": "Vaata rohkem fotosid Facebookis →",
        "video": "Videod", "video_h": "Vaata paigaldust ja valmis lahendusi",
        "faq": "KKK", "faq_h": "Korduma kippuvad küsimused",
        "other": "Teised teenused", "other_h": "Vaata ka", "more": "Loe lähemalt →",
        "default_final": "Arvutame teie krundile <em>sobiva lahenduse</em>",
        "default_final_text": "Jätke päring või helistage.<br>Tuleme tasuta mõõdistusele ja ütleme täpse hinna.",
        "process": [
            ("Jätke päring", "Üks kõne või sõnum, ja võtame kogu töö enda peale. Tuleme tasuta mõõdistusele teile sobival ajal."),
            ("Leiame sobiva lahenduse", "Pakume materjali ja lahenduse teie krundi ja eelarve järgi ning ütleme täpse hinna."),
            ("Paigaldame korralikult", "Paigaldame aia või värava ning seadistame vajaduse korral automaatika. Hoiame teid kursis."),
            ("Anname töö üle", "Vaatame tulemuse koos teiega üle ja anname valmis objekti üle koos hooldussoovitustega."),
        ],
    },
    "ru": {
        "home": "Главная", "services": "Услуги", "services_anchor": "/ru/#uslugi",
        "prompt": "Привет! Нужен новый забор?", "trust": "отзыва в Facebook · рекомендуют",
        "recommend": "рекомендуют на Facebook", "reviews": "отзыва", "experience": "лет опыта",
        "quote": "Оставить заявку", "call": "Позвонить", "close": "Закрыть",
        "get_tag": "Что вы получаете", "options": "Варианты", "local": "Таллинн и Харьюмаа",
        "price_tag": "Честно о цене", "price_h": "От чего зависит стоимость",
        "price_p": "Фиксированного прайса нет. Точную стоимость называем после бесплатного замера.",
        "included": "Всегда входит в процесс", "affects": "Влияет на стоимость",
        "year_round": "Работаем круглый год, включая зиму", "warranty": "Гарантия на выполненные работы",
        "process_tag": "Как мы работаем", "process_h": "Четыре шага до готового результата",
        "gallery": "Галерея", "gallery_h": "Примеры выполненных работ", "more_photos": "Больше фото в нашем Facebook →",
        "video": "Видео", "video_h": "Посмотрите монтаж и готовые решения",
        "faq": "Вопросы", "faq_h": "Частые вопросы",
        "other": "Другие услуги", "other_h": "Смотрите также", "more": "Подробнее об услуге →",
        "default_final": "Рассчитаем <em>подходящее решение</em> для вашего участка",
        "default_final_text": "Оставьте заявку или позвоните.<br>Приедем на бесплатный замер и подготовим точный расчёт.",
        "process": [
            ("Вы оставляете заявку", "Один звонок или сообщение — и мы берём организацию работ на себя. Приедем на бесплатный замер."),
            ("Подбираем и считаем", "Предложим материал и конструкцию под участок и бюджет и заранее назовём стоимость."),
            ("Аккуратно устанавливаем", "Установим забор или ворота и при необходимости подключим автоматику. Будем держать вас в курсе."),
            ("Сдаём готовый объект", "Вместе проверим результат и передадим готовую конструкцию с рекомендациями по эксплуатации."),
        ],
    },
    "en": {
        "home": "Home", "services": "Services", "services_anchor": "/en/#teenused",
        "prompt": "Hey! Need a new fence?", "trust": "Facebook reviews · recommend",
        "recommend": "recommend on Facebook", "reviews": "reviews", "experience": "years of experience",
        "quote": "Get a quote", "call": "Call", "close": "Close",
        "get_tag": "What you get", "options": "Options", "local": "Tallinn and Harjumaa",
        "price_tag": "Clear pricing", "price_h": "What affects the price",
        "price_p": "There is no one-size-fits-all price list. We give an exact quote after the free site measurement.",
        "included": "Always included", "affects": "Affects the price",
        "year_round": "Year-round installation, including winter", "warranty": "Warranty on completed work",
        "process_tag": "How we work", "process_h": "Four steps to a finished result",
        "gallery": "Gallery", "gallery_h": "Examples of completed work", "more_photos": "More photos on Facebook →",
        "video": "Videos", "video_h": "See the installation and finished solutions",
        "faq": "FAQ", "faq_h": "Frequently asked questions",
        "other": "Other services", "other_h": "You may also need", "more": "Learn more →",
        "default_final": "We'll specify the <em>right solution</em> for your property",
        "default_final_text": "Send an enquiry or call us.<br>We'll measure the site free of charge and provide an exact quote.",
        "process": [
            ("You send an enquiry", "One call or message and we take care of the process. We arrange a free site measurement."),
            ("We advise and quote", "We recommend a material and construction for the plot and budget, with the price agreed up front."),
            ("We install with care", "We install the fence or gate and connect automation where required, keeping you informed."),
            ("We hand over the result", "We inspect the completed work with you and provide operating and care guidance."),
        ],
    },
}


def _json(data):
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'


def schema_blocks(lang, c):
    u = UI[lang]
    home_path = {"et": "/", "ru": "/ru/", "en": "/en/"}[lang]
    provider = {
        "@type": "HomeAndConstructionBusiness", "name": "LuxAed", "telephone": PHONE,
        "email": EMAIL, "url": DOMAIN + "/", "@id": DOMAIN + "/#business",
        "areaServed": ["Tallinn", "Harjumaa", "Estonia"],
    }
    blocks = [
        _json({"@context": "https://schema.org", "@type": "Service", "serviceType": c["name"],
               "name": c["name"], "description": c["desc"], "url": DOMAIN + c["path"],
               "inLanguage": lang, "provider": provider, "areaServed": ["Tallinn", "Harjumaa"]}),
        _json({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u["home"], "item": DOMAIN + home_path},
            {"@type": "ListItem", "position": 2, "name": u["services"], "item": DOMAIN + u["services_anchor"]},
            {"@type": "ListItem", "position": 3, "name": c["name"], "item": DOMAIN + c["path"]},
        ]}),
        _json({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in c["faq"]
        ]}),
    ]
    items = (c.get("types") or []) + (c.get("autotypes") or [])
    if items:
        blocks.append(_json({"@context": "https://schema.org", "@type": "ItemList",
                             "name": c.get("types_h", c["name"]), "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": item[4], "description": item[5],
             "image": DOMAIN + "/img/" + item[0] + ".jpg"} for i, item in enumerate(items)
        ]}))
    return blocks


def _benefits(items):
    return '<ul class="svc-bens">' + "".join(f'<li>{x}</li>' for x in items) + '</ul>'


def _cards(items):
    return '<div class="svc-cards">' + "".join(
        f'<div class="svc-card"><div class="ic">{icon}</div><h3>{title}</h3><p>{desc}</p></div>'
        for icon, title, desc in items
    ) + '</div>'


def _types(items):
    cards = []
    for item in items:
        image, alt, icon, eyebrow, title, desc, specs = item[:7]
        position = item[7] if len(item) > 7 else ""
        style = f' style="object-position:{position}"' if position else ""
        chips = "".join(f'<li>{spec}</li>' for spec in specs)
        cards.append(
            f'<article class="gtype"><div class="gtype-img"><span class="gtype-badge"><span class="gt-ic">{icon}</span>{eyebrow}</span>'
            f'<picture>{webp_sources(image)}<img src="/img/{image}.jpg" alt="{html.escape(alt)}" width="640" height="480" loading="lazy" decoding="async"{style}></picture></div>'
            f'<div class="gtype-txt"><h3>{title}</h3><p>{desc}</p><ul class="gtype-specs">{chips}</ul></div></article>'
        )
    return f'<div class="gtypes gtypes--n{min(len(items), 4)}">' + "".join(cards) + '</div>'


def _gallery(items):
    return '<div class="gal" id="gal">' + "".join(
        f'<a href="/img/{image}.jpg" data-lb="1"><picture>{webp_sources(image)}<img src="/img/{image}.jpg" alt="{html.escape(alt)}" width="600" height="400" loading="lazy"></picture></a>'
        for image, alt in items
    ) + '</div>'


def _faq(items):
    return '<div class="faq" id="faqList">' + "".join(
        f'<div class="faq-item"><button class="faq-q">{q}</button><div class="faq-a"><p>{a}</p></div></div>'
        for q, a in items
    ) + '</div>'


def _process(items):
    return '<div class="hsteps">' + "".join(
        f'<div class="hstep"><div class="hstep-num">{i}</div><h3>{title}</h3><p>{desc}</p></div>'
        for i, (title, desc) in enumerate(items, 1)
    ) + '</div>'


def _related(lang, current):
    services = SVC[lang]
    index = next((i for i, (path, _) in enumerate(services) if path == current), 0)
    picks = [services[(index + offset) % len(services)] for offset in (1, 2, -1)]
    more = UI[lang]["more"]
    return '<div class="svc-cards">' + "".join(
        f'<a class="svc-card" href="{path}" style="text-decoration:none"><div class="ic">→</div><h3>{title}</h3><p>{more}</p></a>'
        for path, title in picks
    ) + '</div>'


def render_service(lang, c):
    u = UI[lang]
    blocks = schema_blocks(lang, c)
    H = head(lang, c["path"], c["title"], c["desc"],
             og_img=c.get("og", f'/img/{c["hero"]}.jpg'), schema_blocks=blocks)
    form = render_lead_form(lang, c.get("form_service", ""), c.get("form_material", ""))
    cta_band = f'<div class="svc-cta"><b>{c["cta_band"]}</b><a class="btn" href="#form">{u["quote"]} →</a></div>'
    types = c.get("types") or []
    autotypes = c.get("autotypes") or []
    variants = c.get("variants") or []
    types_cta = cta_band if types and not autotypes and not variants else ""
    types_sec = ""
    if types:
        note = f'<p class="visual-note">{c["visual_note"]}</p>' if c.get("visual_note") else ""
        types_sec = f'<section class="section"><div class="wrap"><span class="tag">{c["types_tag"]}</span><h2 class="big">{c["types_h"]}</h2>{_types(types)}{note}{types_cta}</div></section>'
    auto_sec = ""
    if autotypes:
        note = f'<p class="visual-note">{c["autotypes_note"]}</p>' if c.get("autotypes_note") else ""
        auto_sec = f'<section class="section section--alt"><div class="wrap"><span class="tag">{c.get("autotypes_tag", "")}</span><h2 class="big">{c.get("autotypes_h", "")}</h2>{_types(autotypes)}{note}{cta_band}</div></section>'
    variants_sec = ""
    if variants:
        variants_sec = f'<section class="section section--alt"><div class="wrap"><span class="tag">{u["options"]}</span><h2 class="big">{c["variants_h"]}</h2>{_cards(variants)}{cta_band}</div></section>'
    local_sec = ""
    if c.get("local_h") and c.get("local_p"):
        local_sec = f'<section class="section svc-local"><div class="wrap"><span class="tag">{u["local"]}</span><h2 class="big">{c["local_h"]}</h2><p class="lead">{c["local_p"]}</p></div></section>'
    gallery_sec = ""
    if c.get("gallery"):
        gallery_sec = f'<section class="section"><div class="wrap"><span class="tag">{u["gallery"]}</span><h2 class="big">{c.get("gallery_h", u["gallery_h"])}</h2>{_gallery(c["gallery"])}<div style="text-align:center;margin-top:30px"><a class="gal-fb" href="{FB}/photos_by" target="_blank" rel="noopener">{u["more_photos"]}</a></div></div></section>'
    videos = c.get("videos") or ([c["video"]] if c.get("video") else [])
    video_sec = reel_strip(videos, u["video"], c.get("video_h", u["video_h"]), lang=lang) if videos else ""
    final_h = c.get("final_cta", u["default_final"])
    final_p = c.get("final_cta_text", u["default_final_text"])
    process = c.get("process") or u["process"]
    process_h = c.get("process_h", u["process_h"])
    body = f'''{nav(lang, c["path"])}
<main id="main">
<section class="hero"><div class="hero-photo-bg" style="background:url('/img/{c["hero"]}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap"><div class="hero-grid"><div>
    <div class="hero-kicker hand">{c.get("hero_prompt", u["prompt"])}</div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">{RECOMMEND_PERCENT}%</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">{REVIEW_COUNT} {u["trust"]}</a></div>
    <div class="hero-service-kicker">{c.get("kicker", "")}</div><h1>{c["h1"]}</h1><p class="hero-service-lead">{c.get("lead", "")}</p>
    <div class="hero-btns"><a class="btn btn-accent" href="#form">{u["quote"]} →</a><a class="btn btn-ghost" href="tel:{TEL}">{u["call"]} {PHONE}</a></div>
  </div>{form}</div>
  <div class="hero-stats"><div class="hstat"><b>{RECOMMEND_PERCENT}%</b><span>{u["recommend"]}</span></div><div class="hstat"><b>{REVIEW_COUNT}</b><span>{u["reviews"]}</span></div><div class="hstat"><b>{EXPERIENCE_YEARS}+</b><span>{u["experience"]}</span></div></div></div>
</section>
<section class="section"><div class="wrap"><span class="tag">{u["get_tag"]}</span><h2 class="big">{c["intro_h"]}</h2><p class="lead">{c["intro_p"]}</p>{_benefits(c["bens"])}</div></section>
{types_sec}{auto_sec}{variants_sec}{local_sec}
<section class="section"><div class="wrap"><span class="tag">{u["price_tag"]}</span><h2 class="big">{u["price_h"]}</h2><p class="lead">{c.get("price_lead", u["price_p"])}</p>
  <div class="honest"><div class="hon good"><h3>{u["included"]}</h3><ul>{"".join(f"<li>{item}</li>" for item in c["incl"])}<li>{u["year_round"]}</li><li>{u["warranty"]}</li></ul></div>
  <div class="hon bad"><h3>{u["affects"]}</h3><ul>{"".join(f"<li>{item}</li>" for item in c["factors"])}</ul></div></div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">{u["process_tag"]}</span><h2 class="big">{process_h}</h2>{_process(process)}</div></section>
{gallery_sec}{video_sec}
<section class="section section--alt"><div class="wrap"><span class="tag">{u["faq"]}</span><h2 class="big">{u["faq_h"]}</h2>{_faq(c["faq"])}</div></section>
<section class="section"><div class="wrap"><span class="tag">{u["other"]}</span><h2 class="big">{u["other_h"]}</h2>{_related(lang, c["path"])}</div></section>
<section class="cta-final"><div class="wrap"><h2>{final_h}</h2><p>{final_p}</p><div class="hero-btns"><a class="btn btn-accent" href="#form">{u["quote"]} →</a><a class="btn btn-ghost" href="tel:{TEL}">{u["call"]} {PHONE}</a></div></div></section>
</main>
<div class="lb" id="lb"><button class="lb-x" aria-label="{u["close"]}">&times;</button><img src="" alt="" id="lbImg"></div>
{footer(lang)}
<div class="mob-bar"><a class="btn btn-accent mob-call" href="tel:{TEL}">{u["call"]}</a></div>
{SCRIPTS}
</body></html>'''
    return H + "\n" + body


def write_service(lang, c):
    path = write(c["path"], render_service(lang, c))
    print("wrote", path)
    return path
