"""Concrete article and additive links, using the existing guide-page shell."""
import html

from build_pages import DOMAIN, webp_sources
from concrete_guide_content import CARDS, CONTENT, DATE, PATHS, SERVICE_PATHS, SOURCES
from guide_pages import faq_html, hero, page
from problem_content import HUB_ROW

MARKER_START = '<!-- CONCRETE_GUIDE_LINK_START -->'
MARKER_END = '<!-- CONCRETE_GUIDE_LINK_END -->'

ARTICLE_CSS = '''<style id="concrete-guide-css">
.concrete-story .field-meta{font-size:14px;color:var(--body-text-dim);margin-bottom:22px}
.concrete-story .field-intro{font-size:21px;line-height:1.65;max-width:800px}
.concrete-story .field-scope{font-size:15px;line-height:1.7;color:var(--body-text-dim);margin-top:24px;padding-left:18px;border-left:3px solid var(--accent)}
.concrete-story .field-toc{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 28px;padding-left:26px;margin-top:26px}
.concrete-story .field-toc li{padding-left:5px;line-height:1.6}
.concrete-story .field-toc a{color:var(--accent-deep);text-decoration:underline;text-underline-offset:4px}
.concrete-story .field-step{scroll-margin-top:100px}
.concrete-story .field-number{display:block;color:var(--accent);font-size:18px;font-weight:800;letter-spacing:.12em;margin-bottom:12px}
.concrete-story .field-step h2{font-size:clamp(27px,3.2vw,42px);line-height:1.18;margin-bottom:26px;max-width:760px;text-wrap:balance}
.concrete-story .field-step p{font-size:18px;line-height:1.8;max-width:790px;margin:16px 0}
.concrete-story .field-check{padding:18px 22px;background:#fff;border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:0 12px 12px 0;margin-top:26px}
.concrete-story .field-check strong{display:block;color:var(--accent-deep);font-size:13px;letter-spacing:.04em;margin-bottom:6px}
.concrete-story .field-photo{margin:36px 0 0}
.concrete-story .field-photo a{display:block;border-radius:16px;overflow:hidden}
.concrete-story .field-photo img{display:block;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover}
.concrete-story .field-photo figcaption{font-size:14px;line-height:1.6;color:var(--body-text-dim);margin-top:12px;max-width:790px}
.concrete-story .field-source{font-size:13px!important;margin-top:18px!important;color:var(--body-text-dim)}
.concrete-story .field-source a,.concrete-story .field-sources a{color:var(--accent-deep);text-decoration:underline;text-underline-offset:3px}
.concrete-story .field-checklist{padding-left:23px;margin-top:24px}
.concrete-story .field-checklist li{font-size:18px;line-height:1.7;margin:14px 0;padding-left:7px}
.concrete-story .field-sources{padding-left:20px;columns:2;column-gap:35px}
.concrete-story .field-sources li{font-size:14px;line-height:1.6;margin:0 0 12px;break-inside:avoid}
@media(max-width:760px){.concrete-story .hero-photo-bg{background-image:url('/img/luxaed-concrete-posts-white-mobile.webp')!important}.concrete-story .field-toc{grid-template-columns:1fr}.concrete-story .field-step p{font-size:17px}.concrete-story .field-intro{font-size:19px}.concrete-story .field-sources{columns:1}.concrete-story .field-step h2{font-size:28px}.concrete-story .field-check{padding:16px}.concrete-story .field-step{scroll-margin-top:90px}}
</style>'''


def teaser(lang):
    title, description = CARDS[lang]
    tag, heading = {
        'et': ('LuxAedi praktika', 'Enne betoonivalu'),
        'ru': ('Практика LuxAed', 'Перед заливкой бетона'),
        'en': ('LuxAed on site', 'Before the concrete pour'),
    }[lang]
    return (MARKER_START + '<section class="section help-links"><div class="wrap">'
            f'<span class="tag">{tag}</span><h2 class="big">{heading}</h2>'
            f'<div class="svc-cards help-cards"><a class="svc-card help-card" href="{PATHS[lang]}">'
            f'<div class="ic">10</div><h3>{html.escape(title)}</h3><p>{html.escape(description)}</p>'
            '</a></div></div></section>' + MARKER_END)


def _photo(item):
    name, alt, caption = item
    return (f'<figure class="field-photo"><a href="/img/{name}.jpg" data-lb="1">'
            f'<picture>{webp_sources(name)}<img src="/img/{name}.jpg" alt="{html.escape(alt)}" '
            'width="1200" height="900" loading="lazy" decoding="async"></picture></a>'
            f'<figcaption>{html.escape(caption)}</figcaption></figure>')


def _source_links(keys, lang):
    return ' · '.join(f'<a href="{html.escape(SOURCES[key][1])}" target="_blank" rel="noopener">'
                      f'{html.escape(SOURCES[key][0])}</a>' for key in keys)


def article_page(lang):
    c = CONTENT[lang]
    service = SERVICE_PATHS[lang]
    label = {'et': 'Allikad', 'ru': 'Источники', 'en': 'Sources'}[lang]
    faq_tag, faq_h = {'et': ('KKK', 'Korduma kippuvad küsimused'), 'ru': ('Вопросы', 'Частые вопросы'),
                      'en': ('FAQ', 'Frequently asked questions')}[lang]
    hub_name = {'et': 'Nõuanded', 'ru': 'Советы', 'en': 'Guides'}[lang]
    parts = [ARTICLE_CSS, '<article class="concrete-story" id="gal">',
             hero(lang, c['kicker'], c['h1'], c['lead'], 'luxaed-concrete-posts-white', cta_href=service + '#form'),
             '<section class="section"><div class="wrap guide-narrow">'
             f'<p class="field-meta"><time datetime="{DATE}">{c["meta"]}</time></p>'
             f'<p class="field-intro">{c["intro"]}</p><p class="field-scope">{c["scope"]}</p>'
             f'<nav aria-label="{c["toc"]}" style="margin-top:36px"><h2>{c["toc"]}</h2><ol class="field-toc">' +
             ''.join(f'<li><a href="#tip-{n}">{p["h"]}</a></li>' for n, p in enumerate(c['points'], 1)) +
             '</ol></nav></div></section>']
    for n, point in enumerate(c['points'], 1):
        cls = 'section section--alt' if n % 2 else 'section'
        source = f'<p class="field-source">{label}: {_source_links(point["sources"], lang)}.</p>' if point.get('sources') else ''
        parts.append(f'<section class="{cls} field-step" id="tip-{n}"><div class="wrap guide-narrow">'
                     f'<span class="field-number" aria-hidden="true">{n:02d} / 10</span><h2>{point["h"]}</h2>' +
                     ''.join(f'<p>{p}</p>' for p in point['paras']) +
                     f'<aside class="field-check"><strong>{c["check_label"]}</strong>{point["check"]}</aside>{source}' +
                     (_photo(c['photos'][n]) if n in c['photos'] else '') + '</div></section>')
    parts.append('<section class="section section--alt"><div class="wrap guide-narrow">'
                 f'<h2 class="big">{c["checklist_h"]}</h2><ul class="field-checklist">' +
                 ''.join(f'<li>{item}</li>' for item in c['checklist']) + '</ul></div></section>')
    parts.append(f'<section class="section"><div class="wrap"><span class="tag">{faq_tag}</span>'
                 f'<h2 class="big">{faq_h}</h2>{faq_html(c["faq"])}</div></section>')
    parts.append('<section class="section section--alt"><div class="wrap guide-narrow">'
                 f'<h2 class="big">{c["sources_h"]}</h2><p class="source-note">{c["sources_p"]}</p><ul class="field-sources">' +
                 ''.join(f'<li><a href="{html.escape(url)}" target="_blank" rel="noopener">'
                         f'{html.escape(name)} — {c["source_labels"][key]}</a></li>'
                         for key, (name, url) in SOURCES.items()) + '</ul></div></section>')
    parts.append(f'<section class="section"><div class="wrap"><h2 class="big">{c["related_h"]}</h2><div class="svc-cards help-cards">' +
                 ''.join(f'<a class="svc-card help-card" href="{href}"><h3>{title} →</h3></a>' for href, title in [
                     (service, c['service_link']), (service + '#video', c['video_link']), (HUB_ROW[lang], c['hub_link'])]) +
                 '</div></div></section>')
    parts.append(f'<section class="cta-final"><div class="wrap"><h2>{c["cta_h"]}</h2><p>{c["cta_p"]}</p>'
                 f'<a class="btn btn-accent" href="{service}#form">{c["cta_button"]} →</a></div></section></article>')
    article = {'headline': c['h1'].replace('<br>', ' ').replace('<em>', '').replace('</em>', ''),
               'published': DATE, 'modified': DATE, 'image': '/img/luxaed-concrete-posts-white.jpg'}
    page(lang, PATHS[lang], c['title'], c['desc'], '\n'.join(parts), c['faq'],
         'luxaed-concrete-posts-white', crumb=(hub_name, HUB_ROW[lang], c['short']), article=article)


def llms_block():
    return '\n'.join([
        '## Concrete work and fence foundations',
        '- Scope: separate concrete work or work combined with fence and gate installation in Tallinn and Harju County. Strip foundations, concrete plinths, cast-in-place posts, and pillars using the specified Columbia or Fibo blocks.',
        '- ET: Betoonitööd, aia lintvundamendid, monoliitsed betoonpostid ning Columbia- ja Fibo-plokkidest postid. Ka eraldi teenusena Tallinnas ja Harjumaal.',
        '- RU: Бетонные работы, ленточные фундаменты под заборы, монолитные столбы и столбы из блоков Columbia и Fibo. Можно заказать отдельно в Таллинне и Харьюмаа.',
        '- Quotation: site-specific after inspection and agreement on scope. No universal foundation depth, reinforcement schedule, concrete class or gate-installation waiting period is specified on this site.',
        '- Design depends on soil, water, frost, fence and gate loads, finished levels, fixings and drainage. Structures retaining soil require a retaining-wall design. Loading follows the required concrete strength and mounting-system requirements.',
        '- Photos show real LuxAed projects; finished surfaces do not prove a hidden material or reinforcement detail. The service page also includes a 1:41 gate-roller installation video, with a 5x work sequence and the final 22 seconds at normal speed with Russian audio.',
        '- Service pages: ' + ' · '.join(f'[{lang.upper()}]({DOMAIN}{SERVICE_PATHS[lang]})' for lang in ('et', 'ru', 'en')),
        '- Ten practical concrete-work tips, published 2026-11-11: ' + ' · '.join(f'[{lang.upper()}]({DOMAIN}{PATHS[lang]})' for lang in ('et', 'ru', 'en')),
    ])
