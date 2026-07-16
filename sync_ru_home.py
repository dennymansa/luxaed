#!/usr/bin/env python3
# Keep the hand-built RU home (ru/index.html) in sync with the build_pages-derived chunks.
#
# WHY THIS EXISTS: ru/index.html is the ONLY page not produced by a gen_*.py — it is hand-built.
# Every other page pulls SCRIPTS / video_block() / partners_marquee() straight from build_pages,
# so a change there propagates everywhere EXCEPT the RU home. That gap caused real desyncs
# (RU videos not playing, stale sunset, old carousel arrows). Run this after every build so the
# RU home can never drift again:  python3 build_pages... gens ...; python3 sync_ru_home.py
import io, re, json, importlib
import build_pages
from lead_form import render_lead_form
importlib.reload(build_pages)

P = 'ru/index.html'
s = io.open(P, encoding='utf-8').read()
orig = s
changed = []

RU_HOME_FAQ = [
    ("Сколько стоит забор или ворота?", "Стоимость зависит от материала, длины и высоты ограждения, грунта, рельефа и ворот. После бесплатного замера называем конкретную цену до начала работ."),
    ("Какие заборы вы делаете?", "Делаем деревянные заборы, ограждения из рулонной сетки и рабицы, сварной 2D/3D-сетки, металлического штакетника, прутковых металлических секций и профнастила. Если нужен другой вариант, пришлите фотографию или пример."),
    ("Делаете ли вы ворота вместе с автоматикой?", "Да. Изготавливаем откатные, распашные и пешеходные ворота и подбираем автоматику для въездных ворот. Существующие ворота можно автоматизировать после проверки конструкции."),
    ("Какие районы вы обслуживаете?", "Работаем в Таллинне и по всей Харьюмаа. Выезд дальше обсуждаем отдельно."),
    ("Вы ремонтируете заборы и ворота?", "Да. Меняем повреждённые секции и столбы, регулируем ворота, ремонтируем фурнитуру и автоматику."),
    ("Сколько времени занимает установка?", "Срок зависит от объёма работ, материала и условий участка. Ориентировочный график называем после замера и согласования решения."),
    ("Нужно ли готовить участок заранее?", "Желательно обеспечить свободный доступ к будущей линии забора. Остальную подготовку согласуем по состоянию участка."),
    ("Как оставить заявку?", f"Позвоните по телефону {build_pages.PHONE} или заполните форму на сайте. Можно приложить фотографии участка, линии забора, въезда и грунта."),
]

def sub_once(pattern, repl_str, label):
    global s
    new, n = re.subn(pattern, lambda m: repl_str, s, count=1, flags=re.DOTALL)
    if n != 1:
        raise SystemExit(f"sync_ru_home: anchor for '{label}' not found (matches={n}) — RU home structure changed, fix the pattern")
    if new != s:
        changed.append(label)
    s = new

# 0) shared navigation and the complete eight-service homepage module
sub_once(r'<header class="nav-wrap">.*?<main id="main">', build_pages.nav('ru', '/ru/') + '\n\n<main id="main">', 'nav')
services = f'''<!-- SERVICES -->
<section class="section svc-hide" id="uslugi"><div class="wrap">
  <span class="tag">Наши услуги</span><h2 class="big big--xl">Заборы и ворота для любого участка</h2>
  <p class="lead lead--lg">Выберите тип забора или ворот. Поможем подобрать решение, приедем на бесплатный замер и рассчитаем стоимость.</p>
  <div class="steps-ph">{build_pages.service_tiles_html('ru')}</div>
</div></section>'''
sub_once(r'<!-- SERVICES -->\s*<section class="section svc-hide" id="uslugi">.*?</section>', services, 'service_tiles')

# Keep the service scope, trust facts and FAQ identical to the translated site model.
sub_once(r'<link rel="icon" href="[^"]+">',
         '<link rel="icon" href="/img/luxaed-mark.svg">', 'favicon')
meta_desc = ("Производство и установка заборов, ворот и калиток в Таллинне и Харьюмаа. "
             "Дерево, рабица, сварная 2D/3D-сетка, штакетник, прутковые секции, профнастил и автоматика.")
sub_once(r'<meta name="description" content="[^"]*">',
         f'<meta name="description" content="{meta_desc}">', 'meta_description')
social_url = build_pages.DOMAIN + build_pages.SOCIAL_IMAGE
social_alt = re.search(r'<title>(.*?)</title>', s, flags=re.DOTALL).group(1)
social_og = (f'<meta property="og:image" content="{social_url}">'
             f'<meta property="og:image:secure_url" content="{social_url}">'
             '<meta property="og:image:type" content="image/jpeg">'
             '<meta property="og:image:width" content="1200">'
             '<meta property="og:image:height" content="630">'
             f'<meta property="og:image:alt" content="{social_alt}">\n')
sub_once(r'(?:<meta property="og:image(?::(?:secure_url|type|width|height|alt))?"[^>]*>\s*)+',
         social_og, 'social_og_image')
social_twitter = (f'<meta name="twitter:image" content="{social_url}">'
                  f'<meta name="twitter:image:alt" content="{social_alt}">\n')
sub_once(r'(?:<meta name="twitter:image(?::alt)?"[^>]*>\s*)+',
         social_twitter, 'social_twitter_image')
sub_once(r'<script type="application/ld\+json">(?:(?!</script>).)*?"@type"\s*:\s*"HomeAndConstructionBusiness"(?:(?!</script>).)*?</script>',
         build_pages.business_schema(), 'business_schema')
sub_once(r'<script type="application/ld\+json">(?:(?!</script>).)*?"@type"\s*:\s*"WebSite"(?:(?!</script>).)*?</script>',
         build_pages.website_schema(), 'website_schema')

info = '''<section class="info-strip"><div class="wrap"><div class="info-inner">
  <div><span class="tag">Что мы предлагаем</span><h2 class="info-title">Заборы и ворота<br>под ключ.</h2></div>
  <div><p>Изготавливаем и устанавливаем <b>деревянные, сетчатые, сварные 2D/3D, штакетные, прутковые и профнастильные заборы</b>. Делаем калитки, откатные и распашные ворота, подбираем <b>автоматику</b> и ремонтируем существующие конструкции.</p></div>
</div></div></section>'''
sub_once(r'<section class="info-strip">.*?</section>', info, 'service_scope')

faq_schema = '<script type="application/ld+json">' + json.dumps({
    "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in RU_HOME_FAQ
    ]
}, ensure_ascii=False) + '</script>'
sub_once(r'<script type="application/ld\+json">\s*\{\s*"@context"\s*:\s*"https://schema\.org"\s*,\s*"@type"\s*:\s*"FAQPage".*?</script>',
         faq_schema, 'faq_schema')
faq_items = ''.join(
    f'<div class="faq-item"><button class="faq-q">{q}</button><div class="faq-a"><p>{a}</p></div></div>'
    for q, a in RU_HOME_FAQ
)
faq_visible = f'''<!-- FAQ -->
<section class="section" id="kkk"><div class="wrap"><span class="tag">Часто задаваемые вопросы</span>
  <h2 class="big">Что спрашивают перед заказом забора</h2><div class="faq" id="faqList">{faq_items}</div>
</div></section>'''
sub_once(r'<!-- FAQ -->\s*<section class="section" id="kkk">.*?</section>', faq_visible, 'faq_visible')

fact_replacements = [
    (r'<span class="ht-score">\d+%</span>', f'<span class="ht-score">{build_pages.RECOMMEND_PERCENT}%</span>'),
    (r'<div class="hstat"><b>\d+%</b><span>рекомендуют на Facebook</span></div>', f'<div class="hstat"><b>{build_pages.RECOMMEND_PERCENT}%</b><span>рекомендуют на Facebook</span></div>'),
    (r'<div class="hstat"><b>\d+</b><span>отзыва на странице</span></div>', f'<div class="hstat"><b>{build_pages.REVIEW_COUNT}</b><span>отзыва на странице</span></div>'),
    (r'<div class="hstat"><b>\d+\+?</b><span>лет опыта мастеров</span></div>', f'<div class="hstat"><b>{build_pages.EXPERIENCE_YEARS}+</b><span>лет опыта мастеров</span></div>'),
    (r'>\d+ отзыва в Facebook</a>', f'>{build_pages.REVIEW_COUNT} отзыва в Facebook</a>'),
    (r'<span class="gbp-rev-score">\d+</span>', f'<span class="gbp-rev-score">{build_pages.REVIEW_COUNT}</span>'),
    (r'<div><b>\d+</b><span>отзыва</span></div>', f'<div><b>{build_pages.REVIEW_COUNT}</b><span>отзыва</span></div>'),
    (r'<b style="color:#188038">\d+% рекомендуют</b>', f'<b style="color:#188038">{build_pages.RECOMMEND_PERCENT}% рекомендуют</b>'),
    (r'<div><b>\d+%</b><span>рекомендуют</span></div>', f'<div><b>{build_pages.RECOMMEND_PERCENT}%</b><span>рекомендуют</span></div>'),
    (r'"reviewCount"\s*:\s*"\d+"', f'"reviewCount":"{build_pages.REVIEW_COUNT}"'),
]
for pattern, replacement in fact_replacements:
    new = re.sub(pattern, replacement, s)
    if new != s:
        changed.append('shared_facts')
        s = new

shared_tail = build_pages.footer('ru') + f'''\n<div class="mob-bar"><a class="btn btn-accent mob-call" href="tel:{build_pages.TEL}"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="vertical-align:-3px;margin-right:6px"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>Позвонить</a></div>
<div class="lb" id="lb"><button class="lb-x" type="button" aria-label="Закрыть">&times;</button><img src="" alt="" id="lbImg"></div>\n'''
sub_once(r'(?:<!-- FOOTER -->|<footer class="foot">).*?(?=<script>\s*\n(?:window\.__t0[^\n]*\n)?function closeMob)', shared_tail, 'footer')

# 1) shared <script> block (anchored on the unique 'function closeMob')
sub_once(r'<script>\s*\n(?:window\.__t0[^\n]*\n)?function closeMob\(\).*?</script>(?:\s*<script src="/assets/lead-form\.js\?v=[^"]+" defer></script>)*', build_pages.SCRIPTS, 'SCRIPTS')
# 2) the same lead form as every generated RU landing page
sub_once(r'(?:<!-- LEAD_FORM_START -->\s*)?<div class="form-slot">\s*<div class="form-card[^\"]*" id="form">.*?</form>\s*</div>\s*</div>\s*(?:<!-- LEAD_FORM_END -->)?', render_lead_form('ru'), 'lead_form')
# 3) video section (dark sunset + looping carousel)
sub_once(r'<section class="section section--dark vidsec".*?</section>', build_pages.video_block('ru'), 'video_block')

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
