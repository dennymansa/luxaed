#!/usr/bin/env python3
"""Buyer articles and the guides hub in ET, RU and EN, built on the same guide
template as /kuidas-valida-aeda/ and /aia-ehitusteatis/. Copy lives in
article_content.py; this file only renders it.
"""

import re

from article_content import ARTICLE_CONTENT, DATE, HUB_CONTENT, HUB_NAME, _src
from guide_pages import faq_html, hero, page
from problem_content import ARTICLES, ARTICLE_ORDER, HUB_ROW, _CARD_COPY, _CARD_PATHS, link_cards

DIRECT_TAG = {"et": "Lühivastus", "ru": "Короткий ответ", "en": "Short answer"}
FAQ_LABELS = {"et": ("KKK", "Korduma kippuvad küsimused"),
              "ru": ("Вопросы", "Частые вопросы"),
              "en": ("FAQ", "Frequently asked questions")}
SOURCES_LABEL = {"et": "Allikad", "ru": "Источники", "en": "Sources"}
CHECKED = {
    "et": "Kontrollitud 27.09.2026. See juhend ei ole õigusnõu: enne tööd kontrollige kehtivaid nõudeid.",
    "ru": "Проверено 27.09.2026. Это не юридическая консультация: перед работами уточните действующие требования.",
    "en": "Checked on 27 September 2026. This guide is not legal advice: check the current requirements before work starts.",
}
UPDATED = {"et": "Uuendatud 27.09.2026.", "ru": "Обновлено 27.09.2026.", "en": "Updated on 27 September 2026."}
HUB_LEAD_TAG = {"et": "Juhendid", "ru": "Статьи", "en": "Guides"}


def _cards(items, cols):
    cls = {2: "answer-grid answer-grid--2", 3: "answer-grid answer-grid--3"}.get(cols, "answer-grid")
    return f'<div class="{cls}">' + "".join(
        f'<article class="answer-card"><h3>{title}</h3><p>{text}</p></article>' for title, text in items) + "</div>"


def _table(block):
    headers = block["headers"]
    head = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = "".join("<tr>" + "".join(
        f'<th scope="row">{cell}</th>' if i == 0 else f'<td data-label="{headers[i]}">{cell}</td>'
        for i, cell in enumerate(row)) + "</tr>" for row in block["rows"])
    cls = " ".join(filter(None, ["price-table article-table", block.get("cls")]))
    return (f'<div class="price-table-wrap"><table class="{cls}"><thead><tr>{head}</tr></thead>'
            f'<tbody>{body}</tbody></table></div>')


def _sources(keys, lang):
    if not keys:
        return ""
    return f'<p class="source-note">{SOURCES_LABEL[lang]}: {", ".join(_src(k, lang) for k in keys)}.</p>'


def _block(block, lang, alt):
    section = "section section--alt" if alt else "section"
    head = f'<span class="tag">{block["tag"]}</span><h2 class="big">{block["h"]}</h2>'
    if block["type"] == "text":
        paras = "".join(f'<p class="lead">{p}</p>' for p in block["paras"])
        return (f'<section class="{section}"><div class="wrap guide-narrow">{head}{paras}'
                f'{_sources(block.get("sources"), lang)}</div></section>')
    if block["type"] == "table":
        note = f'<p class="source-note">{block["note"]}</p>' if block.get("note") else ""
        return f'<section class="{section}"><div class="wrap">{head}{_table(block)}{note}</div></section>'
    if block["type"] == "cards":
        return f'<section class="{section}"><div class="wrap">{head}{_cards(block["items"], block.get("cols"))}</div></section>'
    if block["type"] == "sections":
        intro = f'<p class="lead">{block["intro"]}</p>' if block.get("intro") else ""
        items = "".join(
            f'<div class="guide-sub"><h3>{title}</h3>' + "".join(f"<p>{p}</p>" for p in paras) + "</div>"
            for title, paras in block["items"])
        return (f'<section class="{section}"><div class="wrap guide-narrow">{head}{intro}{items}'
                f'{_sources(block.get("sources"), lang)}</div></section>')
    raise ValueError(f"unknown block type {block['type']}")


def _help_cards(tag, heading, cards, section="section help-links"):
    items = "".join(
        f'<a class="svc-card help-card" href="{href}"><div class="ic">→</div><h3>{title}</h3><p>{text}</p></a>'
        for href, title, text in cards)
    return (f'<section class="{section}"><div class="wrap"><span class="tag">{tag}</span>'
            f'<h2 class="big">{heading}</h2><div class="svc-cards help-cards">{items}</div></div></section>')


def _cta(h2, text, href, button):
    return (f'<section class="cta-final"><div class="wrap"><h2>{h2}</h2><p>{text}</p>'
            f'<div class="hero-btns"><a class="btn btn-accent" href="{href}">{button} →</a></div></div></section>')


def _plain(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def article_page(key, lang):
    c = ARTICLE_CONTENT[key][lang]
    path = ARTICLES[key][lang]
    cta_h2, cta_text, cta_href, cta_button = c["cta"]
    direct_h, direct_p = c["direct"]
    parts = [hero(lang, c["kicker"], c["h1"], c["lead"], c["image"], cta_href=cta_href),
             f'<section class="section direct-answer"><div class="wrap"><span class="tag">{DIRECT_TAG[lang]}</span>'
             f'<h2 class="big">{direct_h}</h2><p class="lead">{direct_p}</p></div></section>']
    for i, block in enumerate(c["blocks"]):
        parts.append(_block(block, lang, alt=(i % 2 == 0)))
    legal = any(block.get("sources") or block.get("cls") == "rules-table" for block in c["blocks"])
    faq_alt = "section section--alt" if len(c["blocks"]) % 2 == 0 else "section"
    tag, heading = FAQ_LABELS[lang]
    parts.append(f'<section class="{faq_alt}"><div class="wrap"><span class="tag">{tag}</span><h2 class="big">{heading}</h2>'
                 f'{faq_html(c["faq"])}<p class="source-note">{CHECKED[lang] if legal else UPDATED[lang]}</p></div></section>')
    tag, heading, cards = link_cards("guides", lang, c.get("links_keys", []))
    cards = list(c.get("links", [])) + cards + list(c.get("links_extra", []))
    parts.append(_help_cards(tag, heading, cards))
    parts.append(_cta(cta_h2, cta_text, cta_href, cta_button))
    article = {"headline": _plain(c["h1"]), "published": DATE, "modified": DATE, "image": f"/img/{c['image']}.jpg"}
    page(lang, path, c["title"], c["desc"], "\n".join(parts), c["faq"], c["image"],
         crumb=(HUB_NAME[lang], HUB_ROW[lang], c["short"]), article=article)


def hub_page(lang):
    c = HUB_CONTENT[lang]
    cta_h2, cta_text, cta_href, cta_button = c["cta"]
    parts = [hero(lang, c["kicker"], c["h1"], c["lead"], c["image"], cta_href=cta_href)]
    for i, (group, items) in enumerate(c["groups"]):
        cards = []
        for target, title, text in items:
            if title is None:
                cards.append((_CARD_PATHS[target][lang],) + _CARD_COPY[lang][target])
            else:
                cards.append((target, title, text))
        section = "section help-links section--alt" if i % 2 == 0 else "section help-links"
        parts.append(_help_cards(HUB_LEAD_TAG[lang], group, cards, section))
    parts.append(_cta(cta_h2, cta_text, cta_href, cta_button))
    page(lang, HUB_ROW[lang], c["title"], c["desc"], "\n".join(parts), None, c["image"])


if __name__ == "__main__":
    count = 0
    for language in ("et", "ru", "en"):
        hub_page(language)
        count += 1
        for article_key in ARTICLE_ORDER:
            article_page(article_key, language)
            count += 1
    print(f"Guides hub and articles done: {count}")
