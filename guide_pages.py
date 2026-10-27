#!/usr/bin/env python3
"""Generate LuxAed buyer-guide pages in ET, RU and EN."""

import json
import re

from build_pages import DOMAIN, PHONE, SCRIPTS, TEL, footer, head, nav, write
from problem_content import ARTICLES, GATE_GUIDE, PERMIT_GUIDE, GATE_WONT_OPEN, LEANING_FENCE, link_cards
from service_catalog import SERVICE_MATRIX

_SVC = {service.get("key"): service for service in SERVICE_MATRIX}
# price-table rows and comparison-table rows link to the matching service page
PRICE_ROW_LINKS = ["roll_mesh", "panel_mesh", "panel_mesh", "wood", "steel_picket", "profiled_sheet", "bar_metal",
                   "gates", "gates", "gates", "gates", "intercom", "repair"]
CHOOSE_ROW_LINKS = ["roll_mesh", "panel_mesh", "wood", "steel_picket", "profiled_sheet", "bar_metal"]


def _svc_link(key, lang, label):
    return f'<a href="{_SVC[key][lang]["path"]}">{label}</a>'


def _help_cards(tag, heading, cards):
    items = "".join(
        f'<a class="svc-card help-card" href="{href}"><div class="ic">→</div><h3>{title}</h3><p>{text}</p></a>'
        for href, title, text in cards)
    return (f'<section class="section help-links"><div class="wrap"><span class="tag">{tag}</span>'
            f'<h2 class="big">{heading}</h2><div class="svc-cards help-cards">{items}</div></div></section>')


PATHS = {
    "prices": {"et": "/hinnad/", "ru": "/ru/ceny/", "en": "/en/prices/"},
    "choose": {"et": "/kuidas-valida-aeda/", "ru": "/ru/kak-vybrat-zabor/", "en": "/en/how-to-choose-a-fence/"},
    "area": {"et": "/piirkonnad/harjumaa/", "ru": "/ru/rajony/harjumaa/", "en": "/en/areas/harju-county/"},
}

HOME = {"et": "/", "ru": "/ru/", "en": "/en/"}


def _ld(data):
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'


def faq_html(items):
    return '<div class="faq" id="faqList">' + "".join(
        f'<div class="faq-item"><button class="faq-q">{q}</button><div class="faq-a"><p>{a}</p></div></div>'
        for q, a in items
    ) + '</div>'


def schemas(lang, path, title, desc, faq=None, crumb=None, article=None):
    """crumb = (parent_name, parent_path, short_name) puts the page under a hub.
    article = {"headline", "published", "modified"} adds Article markup."""
    trail = [{"@type": "ListItem", "position": 1, "name": {"et": "Avaleht", "ru": "Главная", "en": "Home"}[lang], "item": DOMAIN + HOME[lang]}]
    if crumb:
        parent_name, parent_path, short_name = crumb
        trail.append({"@type": "ListItem", "position": 2, "name": parent_name, "item": DOMAIN + parent_path})
        trail.append({"@type": "ListItem", "position": 3, "name": short_name, "item": DOMAIN + path})
    else:
        # breadcrumb label without the " | LuxAed" / " — LuxAed" brand suffix
        name = re.sub(r"\s*[|\u2014\u2013-]\s*LuxAed\s*$", "", title)
        trail.append({"@type": "ListItem", "position": 2, "name": name, "item": DOMAIN + path})
    blocks = [
        _ld({"@context": "https://schema.org", "@type": "WebPage", "name": re.sub(r"\s*[|\u2014\u2013-]\s*LuxAed\s*$", "", title),
             "description": desc, "url": DOMAIN + path, "inLanguage": lang,
             "isPartOf": {"@id": DOMAIN + "/#website"},
             "about": {"@id": DOMAIN + "/#business"}}),
        _ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": trail}),
    ]
    if article:
        blocks.append(_ld({"@context": "https://schema.org", "@type": "Article",
                           "headline": article["headline"], "description": desc,
                           "inLanguage": lang, "mainEntityOfPage": DOMAIN + path,
                           "datePublished": article["published"], "dateModified": article["modified"],
                           "image": DOMAIN + article["image"],
                           "author": {"@type": "Organization", "@id": DOMAIN + "/#business", "name": "LuxAed", "url": DOMAIN + "/"},
                           "publisher": {"@type": "Organization", "@id": DOMAIN + "/#business", "name": "LuxAed", "url": DOMAIN + "/",
                                         "logo": {"@type": "ImageObject", "url": DOMAIN + "/apple-touch-icon.png"}}}))
    if faq:
        blocks.append(_ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq
        ]}))
    return blocks


def page(lang, path, title, desc, inner, faq=None, hero="luxaed-wide-wood", crumb=None, article=None):
    H = head(lang, path, title, desc, og_img=f"/img/{hero}.jpg",
             schema_blocks=schemas(lang, path, title, desc, faq, crumb, article),
             og_type="article" if article else "website")
    call = {"et": "Helista", "ru": "Позвонить", "en": "Call"}[lang]
    close = {"et": "Sulge", "ru": "Закрыть", "en": "Close"}[lang]
    body = f'''{nav(lang, path)}
<main id="main">{inner}</main>
<div class="lb" id="lb"><button class="lb-x" aria-label="{close}">&times;</button><img src="" alt="" id="lbImg"></div>
{footer(lang)}
<div class="mob-bar"><a class="btn btn-accent mob-call" href="tel:{TEL}">{call}</a></div>
{SCRIPTS}
</body></html>'''
    print("wrote", write(path, H + "\n" + body))


def hero(lang, kicker, h1, lead, image="luxaed-wide-wood", cta_href=None):
    quote = {"et": "Küsi täpset pakkumist", "ru": "Получить точный расчёт", "en": "Get an exact quote"}[lang]
    call = {"et": "Helista", "ru": "Позвонить", "en": "Call"}[lang]
    return f'''<section class="svc-hero guide-hero"><div class="hero-photo-bg" style="background:url('/img/{image}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap"><span class="tag">{kicker}</span><h1>{h1}</h1><p class="lead">{lead}</p>
  <div class="hero-btns"><a class="btn btn-accent" href="{cta_href or HOME[lang] + '#form'}">{quote} →</a><a class="btn btn-ghost" href="tel:{TEL}">{call} {PHONE}</a></div></div></section>'''


PRICE_ROWS = {
    "et": [
        ("Rullvõrkaed", "25–45 €/jm", "Materjal, postid ja tavapaigaldus; sobib pikale piirile."),
        ("3D-paneelaed", "35–60 €/jm", "Keevispaneelid, postid, kinnitused ja tavapaigaldus."),
        ("2D-paneelaed", "50–85 €/jm", "Jäigem ja raskem keevispaneel; hind sõltub traadist ja kõrgusest."),
        ("Puitaed", "90–160 €/jm", "Puit, teraskarkass, postid ja paigaldus; viimistlus mõjutab hinda."),
        ("Metall-lippaed", "85–155 €/jm", "Ühepoolne või tihedam lahendus, valitud profiil ja RAL-toon."),
        ("Profiilplekk-aed", "70–135 €/jm", "Kinnine plekk, metallkarkass ja tuulekoormusele sobivad postid."),
        ("Keevitatud varbaed", "140–280 €/jm", "Mõõdu järgi valmistatud terassektsioonid ja pinnakaitse."),
        ("Jalgvärav", "550–950 €", "Raam, lukk, postid ja tavapaigaldus; täide sobitatakse aiaga."),
        ("Tiibvärav", "1 400–2 300 €", "Kahetiivaline komplekt tavalaiusega avale; automaatika võib lisanduda."),
        ("Liugvärav automaatikaga", "2 100–3 000 €", "Raam, vundament, ajam ja ohutusseadmed tavalahenduses."),
        ("Automaatika olemasolevale väravale", "500–1 250 €", "Kui värava konstruktsioon ja elektrivalmidus on sobivad."),
        ("Videodomofon ja jalgvärava elektrilukk", "650–1 600 €", "Üks välipaneel, juhtimine, elektrilukk ja tavapärane paigaldus; kaablitee ning mobiilifunktsioon mõjutavad hinda."),
        ("Remont ja diagnostika", "al 90 €", "Väljasõit ja esmane diagnostika; detailid ning töömaht lisanduvad."),
    ],
    "ru": [
        ("Рулонная сетка / рабица", "25–45 €/м", "Материал, столбы и стандартный монтаж; выгодно для длинной границы."),
        ("3D-панель", "35–60 €/м", "Сварные панели, столбы, крепления и стандартный монтаж."),
        ("2D-панель", "50–85 €/м", "Более жёсткая и тяжёлая панель; цена зависит от проволоки и высоты."),
        ("Деревянный забор", "90–160 €/м", "Дерево, стальной каркас, столбы и монтаж; отделка влияет на цену."),
        ("Металлический штакетник", "85–155 €/м", "Одностороннее или более закрытое заполнение, профиль и цвет RAL."),
        ("Забор из профнастила", "70–135 €/м", "Сплошной лист, металлокаркас и столбы с учётом ветровой нагрузки."),
        ("Сварной прутковый забор", "140–280 €/м", "Стальные секции по размеру, защитное покрытие и монтаж."),
        ("Калитка", "550–950 €", "Рама, замок, столбы и стандартный монтаж; заполнение в стиле забора."),
        ("Распашные ворота", "1 400–2 300 €", "Комплект на стандартный проём; автоматика может считаться отдельно."),
        ("Откатные ворота с автоматикой", "2 100–3 000 €", "Рама, фундамент, привод и устройства безопасности."),
        ("Автоматика на существующие ворота", "500–1 250 €", "Если конструкция ворот и электроподготовка подходят."),
        ("Видеодомофон и электрозамок калитки", "650–1 600 €", "Одна вызывная панель, управление, электрозамок и стандартный монтаж; кабель и мобильные функции влияют на цену."),
        ("Ремонт и диагностика", "от 90 €", "Выезд и первичная диагностика; детали и объём ремонта отдельно."),
    ],
    "en": [
        ("Roll mesh / chain-link", "€25–45/m", "Material, posts and standard installation; efficient for long boundaries."),
        ("3D welded panel", "€35–60/m", "Panels, posts, fixings and standard installation."),
        ("2D welded panel", "€50–85/m", "A heavier, more rigid panel; wire and height affect the price."),
        ("Wooden fence", "€90–160/m", "Timber, steel frame, posts and installation; finish affects the price."),
        ("Steel picket fence", "€85–155/m", "Single- or denser double-sided layout, profile and RAL colour."),
        ("Profiled-sheet fence", "€70–135/m", "Solid sheet, steel frame and posts sized for wind exposure."),
        ("Welded metal-bar fence", "€140–280/m", "Made-to-measure steel sections, protective finish and installation."),
        ("Pedestrian gate", "€550–950", "Frame, lock, posts and standard installation; infill matched to the fence."),
        ("Swing gate", "€1,400–2,300", "A standard two-leaf set; automation may be priced separately."),
        ("Automated sliding gate", "€2,100–3,000", "Frame, foundation, drive and standard safety devices."),
        ("Automation for an existing gate", "€500–1,250", "Where the gate structure and electrical preparation are suitable."),
        ("Video intercom and pedestrian-gate lock", "€650–1,600", "One outdoor panel, control, electric lock and standard installation; cabling and mobile features affect the price."),
        ("Repair and diagnostics", "from €90", "Call-out and initial diagnosis; parts and further work are additional."),
    ],
}


PRICE_COPY = {
    "et": {
        "title": "Aia ja värava hinnad Tallinnas ja Harjumaal | LuxAed", "kicker": "Hinnad 2026",
        "h1": "Kui palju maksab <em>aed või värav?</em>",
        "lead": "Siia oleme koondanud aedade ja väravate ligikaudsed hinnad Tallinnas ja Harjumaal. Pärast tasuta mõõdistust koostame teie krundi jaoks täpse pakkumise.",
        "direct": "Lühidalt", "direct_h": "Rullvõrk- ja 3D-paneelaed maksavad koos paigaldusega tavaliselt 25–60 €/jm, jäigem 2D-paneelaed 50–85 €/jm. Kinnine puitaed, metall-lippaed või profiilplekk-aed maksab enamasti 70–160 €/jm.",
        "note": "Tabelis on materjali ja tavapaigalduse ligikaudne hind. Kirjalikus pakkumises näitame eraldi käibemaksu, transpordi, vana aia eemaldamise, keerulise pinnase lisatööd, väravad ja elektritööd.",
        "table_h": "Ligikaudsed hinnad", "service": "Lahendus", "range": "Hind", "includes": "Mida arvestada",
        "example_h": "Näidisarvutus: 50 m eramukrundi piir", "example": [
            ("3D-paneelaed 50 m", "1 750–3 000 €"), ("Puitaed 50 m", "4 500–8 000 €"),
            ("Profiilplekk-aed 50 m", "3 500–6 750 €"), ("+ jalgvärav", "550–950 €"),
        ],
        "why_h": "Mis muudab hinna kallimaks või odavamaks?", "why": [
            ("Pinnas ja reljeef", "Kivi, täitepinnas, suured kõrguste vahed ja piiratud ligipääs suurendavad töömahtu."),
            ("Kõrgus ja tuulekoormus", "Kõrgem või kinnine aed vajab tugevamaid poste, väiksemat sammu ja suuremaid aluseid."),
            ("Väravad ja elekter", "Liugvärava vundament, kaabeldus, automaatika ja läbipääsuseadmed arvutatakse eraldi."),
            ("Vana aia lammutus", "Lammutuse maht, betoonpostide eemaldamine, jäätmete laadimine ja äravedu sõltuvad olemasolevast konstruktsioonist."),
        ],
    },
    "ru": {
        "title": "Цены на заборы и ворота в Таллинне и Харьюмаа | LuxAed", "kicker": "Примерные цены 2026",
        "h1": "Сколько стоит <em>забор или ворота?</em>",
        "lead": "Здесь собраны примерные цены на заборы и ворота в Таллинне и Харьюмаа. После бесплатного замера подготовим точный расчёт для вашего участка.",
        "direct": "Если коротко", "direct_h": "Забор из рулонной сетки или 3D-панелей с материалом и монтажом обычно стоит 25–60 €/м, а из более жёстких 2D-панелей обойдётся в 50–85 €/м. Глухой забор из дерева, металлического штакетника или профнастила обычно стоит 70–160 €/м.",
        "note": "В таблице указана примерная стоимость материала и обычного монтажа. В письменном предложении отдельно укажем НДС, доставку, демонтаж, работу со сложным грунтом, ворота и электрику.",
        "table_h": "Примерные цены", "service": "Решение", "range": "Цена", "includes": "Что входит и влияет на цену",
        "example_h": "Пример бюджета: 50 м вокруг частного участка", "example": [
            ("3D-панель, 50 м", "1 750–3 000 €"), ("Деревянный, 50 м", "4 500–8 000 €"),
            ("Профнастил, 50 м", "3 500–6 750 €"), ("+ калитка", "550–950 €"),
        ],
        "why_h": "Что делает проект дороже или дешевле?", "why": [
            ("Грунт и рельеф", "Камни, насыпной грунт, большие перепады и сложный доступ увеличивают объём работ."),
            ("Высота и ветер", "Высокому или сплошному забору нужны более мощные столбы, меньший шаг и усиленные основания."),
            ("Ворота и электрика", "Фундамент откатных ворот, кабель, привод и контроль доступа считаются отдельно."),
            ("Демонтаж", "Удаление старых секций и бетонных столбов, погрузка и вывоз зависят от конструкции."),
        ],
    },
    "en": {
        "title": "Fence and gate prices in Tallinn and Harju County | LuxAed", "kicker": "2026 prices",
        "h1": "How much does a <em>fence or gate cost?</em>",
        "lead": "Here are typical fence and gate prices for Tallinn and Harju County. After a free site measurement, we prepare an exact quote for your property.",
        "direct": "In short", "direct_h": "Roll mesh and 3D panel fences usually cost €25–60/m installed, and stiffer 2D panels €50–85/m. Solid timber, steel-picket and profiled-sheet fences are more often in the €70–160/m range.",
        "note": "The table shows an approximate cost for materials and standard installation. The written quote lists VAT, transport, removal, difficult ground, gates and electrical work separately.",
        "table_h": "Typical prices", "service": "Solution", "range": "Price", "includes": "What is included and what affects the price",
        "example_h": "Example budget: a 50 m residential boundary", "example": [
            ("3D panel fence, 50 m", "€1,750–3,000"), ("Wooden fence, 50 m", "€4,500–8,000"),
            ("Profiled-sheet fence, 50 m", "€3,500–6,750"), ("+ pedestrian gate", "€550–950"),
        ],
        "why_h": "What makes the price higher or lower?", "why": [
            ("Ground and levels", "Rock, made ground, large level changes and restricted access increase the workload."),
            ("Height and wind", "A taller or solid fence needs stronger posts, closer spacing and larger foundations."),
            ("Gates and power", "Sliding-gate foundations, cabling, drives and access control are priced separately."),
            ("Old-fence removal", "Removing concrete posts, loading and disposal depend on the existing structure."),
        ],
    },
}


PRICE_FAQ = {
    "et": [("Kas mõõdistus on tasuta?", "Jah. Tallinnas ja Harjumaal teeme pakkumise jaoks mõõdistuse tasuta."), ("Kas hind sisaldab materjali ja paigaldust?", "Jah, tabelis on materjali ja tavapaigalduse ligikaudne hind. Transport, vana aia eemaldus, keeruline pinnas, väravad, elektritööd ja käibemaks on kirjalikus pakkumises eraldi real."), ("Kas vana aia eemaldus kuulub hinda?", "Vana aia lammutus ja äravedu arvestatakse eraldi, sest betoonpostide, vundamendi ja jäätmete maht on igal objektil erinev."), ("Millal saan lõpliku hinna?", "Pärast mõõdistust ja lahenduse valikut saadame pakkumise. Näete lõplikku hinda enne tööde alustamist."), ("Kui palju maksab 50 m aed?", "Meie hinnatabeli järgi maksab 50 m 3D paneelaeda 1 750–3 000 €, profiilplekk-aeda 3 500–6 750 € ja puitaeda 4 500–8 000 €. Jalgvärav lisab 550–950 €.")],
    "ru": [("Замер бесплатный?", "Да. В Таллинне и Харьюмаа выезжаем на замер бесплатно."), ("В цену входят материал и монтаж?", "Да, в таблице указана примерная стоимость материала и стандартного монтажа. Доставка, демонтаж старого забора, сложный грунт, ворота, электрика и НДС идут в письменном предложении отдельными строками."), ("Демонтаж старого забора входит?", "Демонтаж и вывоз считаем отдельно. Стоимость зависит от бетонных столбов, фундамента и количества отходов."), ("Когда будет окончательная цена?", "После замера и выбора конструкции отправим предложение. Окончательная цена будет известна до начала работ."), ("Сколько стоит забор длиной 50 м?", "По нашему прайсу 50 м забора из 3D-панелей стоят 1 750–3 000 €, из профнастила 3 500–6 750 €, деревянного 4 500–8 000 €. Калитка добавляет 550–950 €.")],
    "en": [("Is the site measurement free?", "Yes. Site measurement is free in Tallinn and Harju County."), ("Does the price include materials and installation?", "Yes, the table shows an approximate cost for materials and standard installation. Transport, old-fence removal, difficult ground, gates, electrical work and VAT are listed separately in the written quote."), ("Is old-fence removal included?", "Removal and disposal are priced separately. The cost depends on concrete posts, foundations and the amount of waste."), ("When do I receive the final price?", "We send the quote after the measurement, once you have chosen a solution. You will know the final price before work begins."), ("How much does a 50 m fence cost?", "In our price guide, 50 m of 3D mesh panel fence costs €1,750–3,000, profiled sheet €3,500–6,750 and timber €4,500–8,000. A pedestrian gate adds €550–950.")],
}


# Worked examples for whole projects, added at the bottom of the price page.
# Every figure is the sum of published PRICE_ROWS ranges (no new prices).
PRICE_EXAMPLES = {
    "et": ("Näidised", "Näidisarvutused tervikprojektidele", "Kokku",
           "Arvutatud meie hinnatabeli vahemikest. Täpse summa annab kirjalik pakkumine pärast mõõdistust.", [
        ("3D-paneelaed ja automaatväravad", [("40 m 3D-paneelaeda", "1 400–2 400 €"), ("Liugvärav automaatikaga", "2 100–3 000 €"), ("Jalgvärav", "550–950 €")], "4 050–6 350 €"),
        ("Puitaed ja tiibväravad", [("30 m puitaeda", "2 700–4 800 €"), ("Tiibvärav", "1 400–2 300 €"), ("Jalgvärav", "550–950 €")], "4 650–8 050 €"),
        ("Automaatika ja videodomofon olemasolevale väravale", [("Automaatika olemasolevale väravale", "500–1 250 €"), ("Videodomofon ja jalgvärava elektrilukk", "650–1 600 €")], "1 150–2 850 €"),
    ]),
    "ru": ("Примеры", "Примеры расчёта для целого проекта", "Итого",
           "Посчитано по диапазонам из нашего прайса. Точную сумму даёт письменное предложение после замера.", [
        ("3D-забор и автоматические ворота", [("40 м забора из 3D-панелей", "1 400–2 400 €"), ("Откатные ворота с автоматикой", "2 100–3 000 €"), ("Калитка", "550–950 €")], "4 050–6 350 €"),
        ("Деревянный забор и распашные ворота", [("30 м деревянного забора", "2 700–4 800 €"), ("Распашные ворота", "1 400–2 300 €"), ("Калитка", "550–950 €")], "4 650–8 050 €"),
        ("Автоматика и видеодомофон для существующих ворот", [("Автоматика на существующие ворота", "500–1 250 €"), ("Видеодомофон и электрозамок калитки", "650–1 600 €")], "1 150–2 850 €"),
    ]),
    "en": ("Examples", "Worked examples for a whole project", "Total",
           "Calculated from the ranges in our price guide. The written quote after the site visit gives the exact amount.", [
        ("3D panel fence and automated gates", [("40 m of 3D panel fence", "€1,400–2,400"), ("Automated sliding gate", "€2,100–3,000"), ("Pedestrian gate", "€550–950")], "€4,050–6,350"),
        ("Timber fence and swing gates", [("30 m of timber fence", "€2,700–4,800"), ("Swing gate", "€1,400–2,300"), ("Pedestrian gate", "€550–950")], "€4,650–8,050"),
        ("Automation and video intercom for an existing gate", [("Automation for an existing gate", "€500–1,250"), ("Video intercom and pedestrian-gate lock", "€650–1,600")], "€1,150–2,850"),
    ]),
}


def price_examples(lang):
    tag, heading, total_label, note, projects = PRICE_EXAMPLES[lang]
    cards = "".join(
        '<div class="estimate-card estimate-card--example"><h3>' + title + '</h3>'
        + "".join(f'<div class="estimate-line"><span>{name}</span><strong>{price}</strong></div>' for name, price in lines)
        + f'<div class="estimate-line estimate-line--total"><span>{total_label}</span><strong>{total}</strong></div></div>'
        for title, lines, total in projects)
    return (f'<section class="section price-examples"><div class="wrap"><span class="tag">{tag}</span><h2 class="big">{heading}</h2>'
            f'<div class="estimate-grid">{cards}</div><p class="price-note">{note}</p></div></section>')


GUIDE_LINKS = {
    "et": ("Loe edasi", "Kasulikud juhendid", [
        (PERMIT_GUIDE["et"], "Kas aia ehitamiseks on vaja luba?", "Ehitusteatis, vald ja naaber."),
        (GATE_GUIDE["et"], "Liugvärav või tiibvärav?", "Ruum, talv, automaatika ja hind."),
        (LEANING_FENCE["et"], "Aed on viltu või post logiseb?", "Põhjused ja remont."),
    ]),
    "ru": ("Читайте также", "Полезные статьи", [
        (PERMIT_GUIDE["ru"], "Нужно ли разрешение на забор?", "Ehitusteatis, волость и сосед."),
        (GATE_GUIDE["ru"], "Откатные или распашные ворота?", "Место, зима, автоматика и цена."),
        (LEANING_FENCE["ru"], "Покосился забор или шатается столб?", "Причины и ремонт."),
    ]),
    "en": ("Read next", "Useful guides", [
        (PERMIT_GUIDE["en"], "Do you need a permit for a fence?", "Building notice, municipality and neighbours."),
        (GATE_GUIDE["en"], "Sliding or swing gate?", "Space, winter, automation and price."),
        (LEANING_FENCE["en"], "Leaning fence or loose post?", "Causes and repair."),
    ]),
}


def guide_links(lang):
    tag, heading, cards = GUIDE_LINKS[lang]
    items = "".join(
        f'<a class="svc-card help-card" href="{href}"><div class="ic">→</div><h3>{title}</h3><p>{text}</p></a>'
        for href, title, text in cards)
    return (f'<section class="section help-links"><div class="wrap"><span class="tag">{tag}</span>'
            f'<h2 class="big">{heading}</h2><div class="svc-cards help-cards">{items}</div></div></section>')


def price_page(lang):
    c = PRICE_COPY[lang]
    assert len(PRICE_ROWS[lang]) == len(PRICE_ROW_LINKS)
    rows = "".join(f'<tr><th scope="row">{_svc_link(key, lang, name)}</th><td><strong>{price}</strong></td><td>{note}</td></tr>'
                   for key, (name, price, note) in zip(PRICE_ROW_LINKS, PRICE_ROWS[lang]))
    examples = "".join(f'<div class="estimate-line"><span>{name}</span><strong>{price}</strong></div>' for name, price in c["example"])
    factors = "".join(f'<article class="answer-card"><h3>{title}</h3><p>{text}</p></article>' for title, text in c["why"])
    inner = hero(lang, c["kicker"], c["h1"], c["lead"], "luxaed-wide-wood") + f'''
<section class="section direct-answer"><div class="wrap"><span class="tag">{c["direct"]}</span><h2 class="big">{c["direct_h"]}</h2><p class="price-note">{c["note"]}</p></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">{c["kicker"]}</span><h2 class="big">{c["table_h"]}</h2>
<div class="price-table-wrap"><table class="price-table"><thead><tr><th>{c["service"]}</th><th>{c["range"]}</th><th>{c["includes"]}</th></tr></thead><tbody>{rows}</tbody></table></div></div></section>
<section class="section"><div class="wrap guide-split"><div><span class="tag">{ {'et':'50 m','ru':'50 м','en':'50 m'}[lang] }</span><h2 class="big">{c["example_h"]}</h2><div class="estimate-card">{examples}</div></div><div><span class="tag">LuxAed</span><h2 class="big">{c["why_h"]}</h2><div class="answer-grid answer-grid--2">{factors}</div></div></div></section>
{price_examples(lang)}
<section class="section section--alt"><div class="wrap"><span class="tag">{ {'et':'KKK','ru':'Вопросы','en':'FAQ'}[lang] }</span><h2 class="big">{ {'et':'Korduma kippuvad küsimused','ru':'Частые вопросы','en':'Frequently asked questions'}[lang] }</h2>{faq_html(PRICE_FAQ[lang])}</div></section>
<section class="cta-final"><div class="wrap"><h2>{ {'et':'Arvutame teie aia täpse hinna','ru':'Рассчитаем точную цену для вашего участка','en':'Let us price your actual site'}[lang] }</h2><p>{ {'et':'Saatke päring. Mõõdame tasuta ja esitame kirjaliku pakkumise.','ru':'Оставьте заявку. Бесплатно измерим и подготовим письменное предложение.','en':'Send an enquiry. We measure free of charge and provide a written quote.'}[lang] }</p><div class="hero-btns"><a class="btn btn-accent" href="{HOME[lang]}#form">{ {'et':'Küsi pakkumist','ru':'Получить расчёт','en':'Get a quote'}[lang] } →</a></div></div></section>'''
    page(lang, PATHS["prices"][lang], c["title"], c["lead"], inner, PRICE_FAQ[lang])


CHOOSE = {
    "et": {
        "title": "Kuidas valida aeda: aiatüübid, tuul, hooldus ja hind | LuxAed", "kicker": "Valik kasutuse järgi", "h1": "Milline aed sobib <em>teie krundile?</em>",
        "lead": "Ärge valige aeda ainult välimuse järgi. Privaatsus, tuulekoormus, hooldus, eelarve ja maapinna reljeef määravad, milline aed teie krundile tegelikult sobib.",
        "direct": "Kui vajate maksimaalset privaatsust, valige puit- või profiilplekk-aed. Tugeva tuulega avatud krundile on turvalisem õhuline võrk- või varbaed. Kõige soodsam pika piiri lahendus on rullvõrk.",
        "headers": ("Aiatüüp", "Parim kasutus", "Privaatsus", "Tuulekoormus", "Hooldus"),
        "rows": [("Rullvõrk", "Pikk piir, eelarve, nõlv", "Madal", "Väike", "Vähene"), ("2D/3D-paneel", "Tugevus, koer, territoorium", "Madal", "Väike", "Vähene"), ("Puitaed", "Privaatsus ja soe välimus", "Kõrge", "Keskmine", "Regulaarne"), ("Metall-lippaed", "Disain ja reguleeritav avatus", "Keskmisest kõrgeni", "Keskmine", "Vähene"), ("Profiilplekk", "Maksimaalne vaatevarje", "Väga kõrge", "Suur", "Vähene"), ("Varbaed", "Esinduslik ja tugev avatud piire", "Madal", "Väike", "Vähene")],
        "cards": [("Tuul", "Kinnine aed ei lase tuult läbi ja sellele mõjub suur tuulekoormus. Tuulisel krundil tuleb profiilpleki või tiheda puitaia postid ja alused eraldi arvutada."), ("Müra", "Tavaline kinnine aed varjab vaate ja võib tänavamüra veidi summutada, kuid see ei ole sertifitseeritud müratõke. Tõsise müraprobleemi jaoks on vaja erilahendust."), ("Privaatsus", "Kõige rohkem varjavad profiilplekk, tihe puitaed ja kahepoolne metall-lippaed. Võrk- ja varbaed jätavad krundi avatuks."), ("Koer ja lapsed", "Jäik 2D/3D-paneel väikese silma ja sobiva kõrgusega on praktiline. Väravate vahed, lukustus ja aia alumine serv tuleb samuti läbi mõelda.")],
    },
    "ru": {
        "title": "Как выбрать забор: типы, ветер, уход и цена | LuxAed", "kicker": "Выбор по задаче", "h1": "Какой забор подходит <em>вашему участку?</em>",
        "lead": "Выбирайте не только по внешнему виду. Приватность, ветровая нагрузка, уход, бюджет и рельеф определяют, какой забор действительно подойдёт.",
        "direct": "Для максимальной приватности выбирайте дерево или профнастил. На открытом ветреном участке безопаснее продуваемая сетка или прутковый забор. Для длинной границы экономичнее всего рулонная сетка.",
        "headers": ("Тип", "Лучше всего", "Приватность", "Ветер", "Уход"),
        "rows": [("Рулонная сетка", "Длинная граница, бюджет, склон", "Низкая", "Очень хорошо", "Низкий"), ("2D/3D-панель", "Прочность, собака, территория", "Низкая", "Очень хорошо", "Низкий"), ("Дерево", "Приватность и тёплый вид", "Высокая", "Средне", "Регулярный"), ("Металлический штакетник", "Дизайн и регулируемая открытость", "От средней до высокой", "Средне", "Низкий"), ("Профнастил", "Максимальная защита от взглядов", "Очень высокая", "Большая нагрузка", "Низкий"), ("Прутковый металл", "Прочное открытое ограждение", "Низкая", "Очень хорошо", "Низкий")],
        "cards": [("Ветер", "Сплошной забор не пропускает воздух и получает большую нагрузку. Для профнастила или плотного дерева на ветреном участке отдельно рассчитывают столбы и основания."), ("Шум", "Обычный сплошной забор может убрать прямую видимость дороги и немного снизить воспринимаемый шум, но это не сертифицированный шумозащитный экран."), ("Приватность", "Лучше всего закрывают участок профнастил, плотное дерево и двухсторонний штакетник. Сетка и прутковые секции оставляют участок открытым."), ("Собака и дети", "Жёсткая 2D/3D-панель с подходящей ячейкой и высотой практична. Важно также продумать низ забора, зазоры ворот и замки.")],
    },
    "en": {
        "title": "How to choose a fence: types, wind, upkeep and price | LuxAed", "kicker": "Choose by use case", "h1": "Which fence suits <em>your property?</em>",
        "lead": "Choose for more than appearance. Privacy, wind loading, maintenance, budget and ground levels determine which fence will actually suit you.",
        "direct": "For maximum privacy, choose timber or profiled sheet. On an exposed windy site, open mesh or metal-bar fencing is usually safer. Roll mesh is normally the most economical option for a long boundary.",
        "headers": ("Fence type", "Best for", "Privacy", "Wind", "Maintenance"),
        "rows": [("Roll mesh", "Long boundary, budget, slope", "Low", "Very good", "Low"), ("2D/3D panel", "Strength, dogs, business premises", "Low", "Very good", "Low"), ("Timber", "Privacy and a warm appearance", "High", "Medium", "Regular"), ("Steel picket", "Design and adjustable openness", "Medium to high", "Medium", "Low"), ("Profiled sheet", "Maximum visual screening", "Very high", "High loading", "Low"), ("Metal bar", "Strong, open architectural boundary", "Low", "Very good", "Low")],
        "cards": [("Wind", "A solid fence blocks airflow and takes higher loads. Posts and foundations for profiled sheet or close-boarded timber must be sized for an exposed site."), ("Noise", "A normal solid fence may remove the direct line of sight and slightly reduce perceived road noise, but it is not a certified acoustic barrier."), ("Privacy", "Profiled sheet, close-boarded timber and double-sided steel pickets give the most screening. Mesh and metal-bar fencing remain open."), ("Dogs and children", "A rigid 2D/3D panel with suitable mesh and height is practical. The bottom edge, gate gaps and locks also need attention.")],
    },
}


CHOOSE_FAQ = {
    "et": [("Milline aed sobib kõige paremini tuulisele krundile?", "Õhuline rullvõrk, paneelaed või varbaed laseb tuule läbi. Kinnise aia puhul tuleb konstruktsioon dimensioneerida asukoha tuulekoormuse järgi."), ("Milline aed aitab müra vastu?", "Täiesti kinnine ja piisava massiga erilahendus töötab paremini kui avatud aed, kuid tavaline puit- või profiilplekk-aed summutab müra vaid veidi ega ole müratõke."), ("Milline aed vajab kõige vähem hooldust?", "Tsingitud ja värvkattega võrkpaneel, metall-lippaed, varbaed ja profiilplekk-aed vajavad üldjuhul vähem regulaarset hooldust kui puit."), ("Kas eri krundikülgedel võib kasutada eri aedu?", "Jah. Sageli tehakse tänavapoolne külg privaatsest materjalist ja naabrite või tagumise piiri poole kasutatakse soodsamat võrkaeda.")],
    "ru": [("Какой забор лучше для ветреного участка?", "Рулонная сетка, панель или прутковый забор пропускают воздух. Для сплошного забора конструкцию нужно рассчитывать по ветровой нагрузке участка."), ("Какой забор помогает от шума?", "Закрытая конструкция достаточной массы работает лучше открытой, но обычный деревянный забор или профнастил снижает шум лишь немного и шумовым экраном не является."), ("Какой забор требует меньше ухода?", "Оцинкованная сетчатая панель, металлический штакетник, прутковые секции и профнастил обычно требуют меньше регулярного ухода, чем дерево."), ("Можно комбинировать разные типы?", "Да. Со стороны улицы часто ставят более закрытый забор, а по бокам и сзади используют экономичную сетку.")],
    "en": [("Which fence is best for a windy site?", "Roll mesh, welded panels and metal-bar fencing let air pass through. A solid fence must be structurally specified for the site's wind exposure."), ("Which fence helps with noise?", "A solid purpose-designed barrier with sufficient mass works better than an open fence, but an ordinary timber or profiled-sheet fence reduces noise only slightly and is not a noise barrier."), ("Which fence needs the least maintenance?", "Galvanised, powder-coated mesh, steel pickets, metal bars and profiled sheet generally need less regular maintenance than timber."), ("Can different fence types be combined?", "Yes. A common solution is a more private street frontage with economical mesh on side and rear boundaries.")],
}


# Additional problem-led answers mirror the way customers actually describe a
# fence project. These broaden useful query coverage without repeating keyword
# lists or creating thin one-question pages.
CHOOSE_MORE_CARDS = {
    "et": [
        ("Kaldega krunt", "Laugel nõlval järgib rullvõrk maapinda. Jäigad paneelid, puit- ja metallaiad paigaldatakse pärast kõrguste mõõtmist kalde järgi või astmetena."),
        ("Pikk piir ja kindel eelarve", "Rullvõrk on tavaliselt kõige soodsam pika perimeetri jaoks. 3D-paneel maksab rohkem, kuid annab jäigema ja korrastatuma tulemuse."),
        ("Erinevad krundiküljed", "Tänava poole võib teha privaatse puit-, plekk- või lippaia ning külg- ja tagapiirile kasutada õhulisemat võrku."),
        ("Väravad ja ligipääs", "Aia valikul arvestage kohe jalgvärava, sõiduvärava, automaatika, domofoni, laste, koera ja igapäevase liikumisega."),
    ],
    "ru": [
        ("Участок с уклоном", "На плавном склоне рулонная сетка повторяет рельеф. Жёсткие панели, дерево и металл ведём по уклону или ступенями после измерения высот."),
        ("Длинная граница и ограниченный бюджет", "Рулонная сетка обычно дешевле на большом периметре. 3D-панель стоит дороже, но даёт более жёсткую и аккуратную линию."),
        ("Разные стороны участка", "Со стороны улицы можно поставить глухой забор из дерева, профнастила или металлического штакетника, а по бокам и сзади использовать более открытую сетку."),
        ("Ворота и доступ", "Сразу учитывайте калитку, въездные ворота, автоматику, домофон, детей, собаку и ежедневные маршруты семьи по участку."),
    ],
    "en": [
        ("A sloping property", "Roll mesh can follow a gentle slope. Rigid panels, timber and metal are installed to the fall or stepped after the levels have been measured."),
        ("A long boundary and limited budget", "Roll mesh is usually the lowest-cost choice for a large perimeter. 3D panels cost more but give a more rigid, ordered line."),
        ("Different sides of the property", "Use private timber, profiled sheet or closely spaced steel pickets towards the street and more open mesh along side and rear boundaries."),
        ("Gates and access", "Plan the pedestrian gate, vehicle gate, automation, intercom, children, dog and everyday routes at the same time as the fence."),
    ],
}

CHOOSE_MORE_FAQ = {
    "et": [
        ("Milline aed sobib koerale?", "Jäik 2D/3D-paneel on sageli praktiline, kuid tähtsad on ka kõrgus, silma suurus, alumine vahe ja värava lukk. Väiksemale rahulikule koerale võib sobida õigesti pingutatud rullvõrk."),
        ("Milline aed on kõige soodsam?", "Pika ja lihtsa aiajoone puhul on rullvõrk tavaliselt kõige soodsam. Lõpphinda mõjutavad postid, nurgad, pinnas, kõrgus, väravad ja vana aia eemaldus."),
        ("Kuidas lahendada aed ebatasasel maal?", "Laugelt langev aed võib jälgida reljeefi; järsemad kõrguste vahed tehakse sageli astmetena. Mõõdistus näitab, milline lahendus jääb sirge ja praktiline."),
        ("Kas aeda saab paigaldada talvel?", "Paljusid töid teeme aastaringselt. Tegelik ajakava sõltub pinnasest, külmast, lumest, betoonitöödest ja valitud konstruktsioonist."),
    ],
    "ru": [
        ("Какой забор лучше для собаки?", "Часто подходит жёсткая 2D/3D-панель, но важны также высота, размер ячейки, нижний зазор и замок калитки. Для спокойной небольшой собаки может подойти правильно натянутая рулонная сетка."),
        ("Какой забор самый недорогой?", "Для длинной простой границы обычно выгоднее рулонная сетка. Итоговую цену меняют столбы, углы, грунт, высота, ворота и демонтаж старого ограждения."),
        ("Как поставить забор на неровном участке?", "Плавную линию можно вести по рельефу, а заметные перепады часто оформляют ступенями. После замера выбираем вариант, который останется ровным и удобным."),
        ("Можно устанавливать забор зимой?", "Многие работы выполняем круглый год. Конкретный срок зависит от грунта, мороза, снега, бетонных работ и выбранной конструкции."),
    ],
    "en": [
        ("Which fence is best for a dog?", "A rigid 2D/3D panel is often practical, but height, mesh size, bottom clearance and the pedestrian-gate lock matter too. Correctly tensioned roll mesh can suit a calm smaller dog."),
        ("Which fence is the least expensive?", "Roll mesh is normally the lowest-cost option for a long, simple boundary. Posts, corners, ground, height, gates and old-fence removal affect the final price."),
        ("How is a fence installed on uneven ground?", "A gentle line can follow the levels, while larger changes are often stepped. Measurement shows which method will stay straight and work well."),
        ("Can a fence be installed in winter?", "We do much of our work year-round. The actual schedule depends on ground conditions, frost, snow, concrete work and the selected construction."),
    ],
}

for _lang in ("et", "ru", "en"):
    CHOOSE[_lang]["cards"].extend(CHOOSE_MORE_CARDS[_lang])
    CHOOSE_FAQ[_lang].extend(CHOOSE_MORE_FAQ[_lang])


def choose_page(lang):
    c = CHOOSE[lang]
    headers = "".join(f"<th>{h}</th>" for h in c["headers"])
    rows = "".join("<tr>" + "".join(f"<{ 'th scope=\"row\"' if i == 0 else 'td' }>{_svc_link(key, lang, x) if i == 0 else x}</{ 'th' if i == 0 else 'td' }>" for i, x in enumerate(row)) + "</tr>" for key, row in zip(CHOOSE_ROW_LINKS, c["rows"]))
    cards = "".join(f'<article class="answer-card"><h3>{title}</h3><p>{text}</p></article>' for title, text in c["cards"])
    inner = hero(lang, c["kicker"], c["h1"], c["lead"], "luxaed-hero") + f'''
<section class="section direct-answer"><div class="wrap"><span class="tag">{ {'et':'Lühivastus','ru':'Короткий ответ','en':'Short answer'}[lang] }</span><h2 class="big">{c["direct"]}</h2></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">{c["kicker"]}</span><h2 class="big">{ {'et':'Aiatüüpide kiire võrdlus','ru':'Быстрое сравнение типов','en':'Quick fence comparison'}[lang] }</h2><div class="price-table-wrap"><table class="price-table comparison-table"><thead><tr>{headers}</tr></thead><tbody>{rows}</tbody></table></div></div></section>
<section class="section"><div class="wrap"><span class="tag">{ {'et':'Olukorrad','ru':'Ситуации','en':'Situations'}[lang] }</span><h2 class="big">{ {'et':'Lahendused levinud olukordadele','ru':'Ответы под реальные задачи','en':'Answers for real use cases'}[lang] }</h2><div class="answer-grid">{cards}</div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">{ {'et':'KKK','ru':'Вопросы','en':'FAQ'}[lang] }</span><h2 class="big">{ {'et':'Korduma kippuvad küsimused','ru':'Частые вопросы','en':'Frequently asked questions'}[lang] }</h2>{faq_html(CHOOSE_FAQ[lang])}</div></section>
{_help_cards(*link_cards("guides", lang, ["panel_vs_mesh", "privacy_fence", "municipal_rules"]))}
<section class="cta-final"><div class="wrap"><h2>{ {'et':'Ei pea ise lõplikku valikut tegema','ru':'Не обязательно выбирать в одиночку','en':'You do not have to decide alone'}[lang] }</h2><p>{ {'et':'Kirjeldage soovitud privaatsust, eelarvet ja krunti. Pakume 2–3 sobivat varianti.','ru':'Опишите приватность, бюджет и участок. Предложим 2–3 подходящих варианта.','en':'Tell us about privacy, budget and the site. We will suggest 2–3 suitable options.'}[lang] }</p><div class="hero-btns"><a class="btn btn-accent" href="{HOME[lang]}#form">{ {'et':'Küsi soovitust','ru':'Получить рекомендацию','en':'Ask for advice'}[lang] } →</a></div></div></section>'''
    page(lang, PATHS["choose"][lang], c["title"], c["lead"], inner, CHOOSE_FAQ[lang], "luxaed-hero")


AREA = {
    "et": {"title": "Aedade ja väravate paigaldus Harjumaal | LuxAed", "desc": "Paigaldame aedu ja väravaid Tallinnas ja kogu Harjumaal: Viimsi, Harku, Rae, Saue, Saku, Kiili, Keila, Maardu ja teised vallad. Tasuta mõõdistus.", "kicker": "Teeninduspiirkond", "h1": "Aiad ja väravad <em>kogu Harjumaal</em>", "lead": "Tuleme tasuta mõõdistusele Tallinnas ja Harjumaa valdades. Tartu, Pärnu ja ülejäänud Eesti ei ole meie põhiteeninduspiirkond.", "direct": "Teenindame Tallinna, Viimsi, Harku (sh Tiskre ja Tabasalu), Rae (sh Peetri ja Jüri), Saue (sh Laagri), Saku, Kiili, Jõelähtme, Kuusalu, Lääne-Harju, Anija, Kose ja Raasiku piirkonda ning Maardu, Keila ja Loksa linna.", "permit_h": "Valla nõuded enne aia ehitust", "permit": "Nõuded sõltuvad omavalitsusest, detailplaneeringust ja sellest, kas aia ehitamisel kaevatakse sügavamale kui 30 cm. Enamasti tuleb esitada ehitusteatis ja ehitusprojekt ning kontrollida valla lisatingimusi, näiteks aia kõrgust ja kaugust teest.", "cards": [("Tasuta mõõdistus", "Kontrollime aiajoont, kõrgusi, pinnast, ligipääsu ja värava ava."), ("Üks meeskond", "Aed, jalgvärav, sõiduvärav, automaatika ja remont ühest kohast."), ("Kohalik lahendus", "Arvestame Harjumaa pinnase, tuule, detailplaneeringu ja naabritega piirneva aiaga."), ("Kirjalik pakkumine", "Materjalid, töö, lisad ja eeldused on enne alustamist kirjas.")]},
    "ru": {"title": "Установка заборов и ворот по Харьюмаа | LuxAed", "desc": "Устанавливаем заборы и ворота в Таллинне и по всему Харьюмаа: Виймси, Харку, Раэ, Сауэ, Саку, Кийли, Кейла, Маарду и другие волости. Бесплатный замер.", "kicker": "Зона обслуживания", "h1": "Заборы и ворота <em>по всему Харьюмаа</em>", "lead": "Выезжаем на бесплатный замер в Таллинне и по уезду Харьюмаа. Тарту, Пярну и остальная Эстония не являются нашей основной зоной.", "direct": "Работаем в Таллинне, Виймси, Харку (в том числе Тискре и Табасалу), Раэ (в том числе Пеэтри и Юри), Сауэ (в том числе Лаагри), Саку, Кийли, Йыэляхтме, Куусалу, Ляэне-Харью, Ания, Козе и Раазику, а также в Маарду, Кейле и Локсе.", "permit_h": "Требования волости перед установкой забора", "permit": "Требования зависят от волости или города, детальной планировки и того, копают ли при установке глубже 30 см. Чаще всего нужно подать уведомление (ehitusteatis) и проект и проверить дополнительные условия волости, например высоту забора и расстояние до дороги.", "cards": [("Бесплатный замер", "Проверяем линию, высоты, грунт, доступ и проём ворот."), ("Одна команда", "Забор, калитка, ворота, автоматика и ремонт в одном проекте."), ("Местные условия", "Учитываем грунт, ветер, детальную планировку и границу с соседом."), ("Письменное предложение", "Материалы, работы, дополнения и условия фиксируем до начала.")]},
    "en": {"title": "Fence and gate installation across Harju County | LuxAed", "desc": "Fence and gate installation in Tallinn and across Harju County: Viimsi, Harku, Rae, Saue, Saku, Kiili, Keila, Maardu and more. Free site measurement.", "kicker": "Service area", "h1": "Fences and gates across <em>Harju County</em>", "lead": "We provide free site measurement in Tallinn and across Harju County. Tartu, Pärnu and the rest of Estonia are not our core service area.", "direct": "We cover Tallinn, Viimsi, Harku (including Tiskre and Tabasalu), Rae (including Peetri and Jüri), Saue (including Laagri), Saku, Kiili, Jõelähtme, Kuusalu, Lääne-Harju, Anija, Kose and Raasiku, as well as Maardu, Keila and Loksa.", "permit_h": "Check your municipality's rules first", "permit": "Requirements depend on the municipality, the detailed plan and whether building the fence involves digging deeper than 30 cm. Usually you file a building notice and a design and check the municipality's extra conditions, such as fence height and distance from the road.", "cards": [("Free measurement", "We check the boundary, levels, ground, access and gate opening."), ("One team", "Fence, pedestrian gate, vehicle gate, automation and repairs in one project."), ("Local conditions", "We account for Harju ground, wind, detailed plans and shared boundaries."), ("Written quote", "Materials, work, extras and assumptions are listed before work starts.")]},
}


AREA_FAQ = {
    "et": [("Kas töötate ainult Tallinnas?", "Ei. Põhiteeninduspiirkond on Tallinn ja kogu Harjumaa."), ("Kas Harjumaa vallad nõuavad aia jaoks ehitusteatist?", "Enamasti jah: kui aia ehitamisel kaevatakse sügavamale kui 30 cm, on vaja ehitusteatist ja ehitusprojekti. Lisaks võib vald seada nõudeid aia kõrgusele ja kaugusele teest."), ("Kas mõõdistus on tasuta ka Keilas, Loksal ja Kuusalus?", "Jah. Tavapärane mõõdistus on tasuta kogu Harjumaa teeninduspiirkonnas, ka Keila ja Loksa linnas ning Kuusalu vallas."), ("Kas remondite aedu ka väljaspool Tallinna?", "Jah. Remondime aedu, väravaid ja automaatikat kogu Harjumaal. Remondi ja diagnostika hind algab 90 eurost.")],
    "ru": [("Вы работаете только в Таллинне?", "Нет, мы работаем в Таллинне и по всему уезду Харьюмаа."), ("Нужно ли в волостях Харьюмаа уведомление о строительстве забора?", "Чаще всего да: если при установке копают глубже 30 см, нужны ehitusteatis и проект. Кроме того, волость может ставить требования к высоте забора и расстоянию до дороги."), ("Замер бесплатный и в Кейле, Локсе и Куусалу?", "Да. Обычный замер бесплатный по всей нашей зоне в Харьюмаа, в том числе в городах Кейла и Локса и в волости Куусалу."), ("Ремонтируете заборы за пределами Таллинна?", "Да. Ремонтируем заборы, ворота и автоматику по всему Харьюмаа. Ремонт и диагностика от 90 €.")],
    "en": [("Do you work only in Tallinn?", "No. Our core service area is Tallinn and all of Harju County."), ("Do Harju County municipalities require a building notice for a fence?", "Usually yes: if building the fence involves digging deeper than 30 cm, you need a building notice and a design. Municipalities may also set rules on fence height and distance from the road."), ("Is measurement free in Keila, Loksa and Kuusalu too?", "Yes. A normal measurement is free across our Harju County service area, including the towns of Keila and Loksa and Kuusalu Municipality."), ("Do you repair fences outside Tallinn?", "Yes. We repair fences, gates and automation across Harju County. Repair and diagnostics start from €90.")],
}


def area_page(lang):
    c = AREA[lang]
    cards = "".join(f'<article class="answer-card"><h3>{title}</h3><p>{text}</p></article>' for title, text in c["cards"])
    places = ["Tallinn", "Viimsi", "Tiskre", "Harku", "Tabasalu", "Rae", "Peetri", "Jüri", "Saue", "Laagri", "Keila", "Saku", "Kiili", "Jõelähtme", "Maardu", "Kuusalu", "Lääne-Harju", "Anija", "Kose", "Raasiku", "Loksa"]
    if lang == "ru":
        places = ["Таллинн", "Виймси", "Тискре", "Харку", "Табасалу", "Раэ", "Пеэтри", "Юри", "Сауэ", "Лаагри", "Кейла", "Саку", "Кийли", "Йыэляхтме", "Маарду", "Куусалу", "Ляэне-Харью", "Ания", "Козе", "Раазику", "Локса"]
    chips = "".join(f'<span class="area-pill">{x}</span>' for x in places)
    inner = hero(lang, c["kicker"], c["h1"], c["lead"], "luxaed-sunset") + f'''
<section class="section direct-answer"><div class="wrap"><span class="tag">{ {'et':'Lühivastus','ru':'Короткий ответ','en':'Short answer'}[lang] }</span><h2 class="big">{c["direct"]}</h2><div class="areas">{chips}</div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">LuxAed</span><h2 class="big">{ {'et':'Mida Harjumaal pakume','ru':'Что вы получаете в Харьюмаа','en':'What you get in Harju County'}[lang] }</h2><div class="answer-grid">{cards}</div></div></section>
<section class="section"><div class="wrap guide-narrow"><span class="tag">{ {'et':'Ehitisregister','ru':'Регистр строений','en':'Building Register'}[lang] }</span><h2 class="big">{c["permit_h"]}</h2><p class="lead">{c["permit"]}</p><p class="source-note">{ {'et':'Kontrollige alati oma valla või linna kehtivaid nõudeid enne töö tellimist.','ru':'Перед заказом всегда проверьте актуальные требования своего города или волости.','en':'Always check the current requirements of your municipality before commissioning work.'}[lang] } <a href="{PERMIT_GUIDE[lang]}">{ {'et':'Loe täpsemalt ehitusteatise ja naabri kohta →','ru':'Подробнее об уведомлении о строительстве и соседях →','en':'More about the building notice and neighbours →'}[lang] }</a> · <a href="{ARTICLES['municipal_rules'][lang]}">{ {'et':'Aia kõrgus Harjumaa valdades →','ru':'Высота забора в волостях Харьюмаа →','en':'Fence height rules in Harju County →'}[lang] }</a> · <a href="{ARTICLES['road_utilities'][lang]}">{ {'et':'Aed tee ääres ja trasside lähedal →','ru':'Забор у дороги и коммуникаций →','en':'Fences near roads and utilities →'}[lang] }</a></p></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">{ {'et':'KKK','ru':'Вопросы','en':'FAQ'}[lang] }</span><h2 class="big">{ {'et':'Korduma kippuvad küsimused','ru':'Частые вопросы','en':'Frequently asked questions'}[lang] }</h2>{faq_html(AREA_FAQ[lang])}</div></section>
<section class="cta-final"><div class="wrap"><h2>{ {'et':'Mõõdame teie objekti Harjumaal','ru':'Измерим ваш объект в Харьюмаа','en':'We will measure your Harju site'}[lang] }</h2><p>{ {'et':'Jätke aadress ja telefon ning lepime sobiva aja kokku.','ru':'Оставьте адрес и телефон, и мы договоримся об удобном времени.','en':'Leave the address and phone number and we will arrange a suitable time.'}[lang] }</p><div class="hero-btns"><a class="btn btn-accent" href="{HOME[lang]}#form">{ {'et':'Küsi tasuta mõõdistust','ru':'Заказать бесплатный замер','en':'Book a free measurement'}[lang] } →</a></div></div></section>'''
    page(lang, PATHS["area"][lang], c["title"], c.get("desc", c["lead"]), inner, AREA_FAQ[lang], "luxaed-sunset")


if __name__ == "__main__":
    for language in ("et", "ru", "en"):
        price_page(language)
        choose_page(language)
        area_page(language)
    print("Guide pages done: 9")
