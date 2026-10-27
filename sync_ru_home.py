#!/usr/bin/env python3
# Keep the hand-built RU home (ru/index.html) in sync with the build_pages-derived chunks.
#
# WHY THIS EXISTS: ru/index.html is the ONLY page not produced by a gen_*.py — it is hand-built.
# Every other page pulls SCRIPTS / video_block() / partners_marquee() straight from build_pages,
# so a change there propagates everywhere EXCEPT the RU home. That gap caused real desyncs
# (RU videos not playing, stale sunset, old carousel arrows). Run this after every build so the
# RU home can never drift again:  python3 build_pages... gens ...; python3 sync_ru_home.py
import io, re, importlib
import build_pages
from lead_form import render_lead_form
importlib.reload(build_pages)

P = 'ru/index.html'
s = io.open(P, encoding='utf-8').read()
orig = s
changed = []

# One Russian FAQ list for the homepage and /ru/faq/. It lives in
# gen_ru_support.py; importing it writes nothing (that script builds its pages
# only when run directly).
from gen_ru_support import RU_HOME_FAQ

def sub_once(pattern, repl_str, label):
    global s
    new, n = re.subn(pattern, lambda m: repl_str, s, count=1, flags=re.DOTALL)
    if n != 1:
        raise SystemExit(f"sync_ru_home: anchor for '{label}' not found (matches={n}) — RU home structure changed, fix the pattern")
    if new != s:
        changed.append(label)
    s = new

# Keep the hand-built RU head/body on the same single-container tracking
# architecture as every generated page. Remove both our managed block and the
# obsolete direct Ads gtag before inserting the current shared snippets.
before_tracking = s
s = re.sub(r'\s*<!-- LUX_TRACKING_START -->.*?<!-- LUX_TRACKING_END -->\s*', '\n', s, flags=re.DOTALL)
s = re.sub(
    r'\s*<script>(?=(?:(?!</script>).)*(?:AW-960623543|googletagmanager\.com/gtag/js))(?:(?!</script>).)*</script>\s*',
    '\n', s, flags=re.DOTALL,
)
s = re.sub(r'\s*<!-- LUX_GTM_NOSCRIPT_START -->.*?<!-- LUX_GTM_NOSCRIPT_END -->\s*', '\n', s, flags=re.DOTALL)
tracking_head = build_pages.tracking_head()
if tracking_head:
    s, tracking_head_count = re.subn(
        r'(<meta name="viewport"[^>]*>\s*)',
        lambda m: m.group(1) + tracking_head + '\n',
        s, count=1,
    )
    if tracking_head_count != 1:
        raise SystemExit("sync_ru_home: viewport anchor for tracking not found")
tracking_body = build_pages.tracking_body()
if tracking_body:
    s, tracking_body_count = re.subn(
        r'(<body[^>]*>\s*)',
        lambda m: m.group(1) + tracking_body + '\n',
        s, count=1,
    )
    if tracking_body_count != 1:
        raise SystemExit("sync_ru_home: body anchor for GTM noscript not found")
if s != before_tracking:
    changed.append('tracking')

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
         f'<link rel="icon" href="{build_pages.FAVICON}">', 'favicon')
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
  <div><span class="tag">Что мы предлагаем</span><h2 class="info-title">Строительство и установка заборов</h2></div>
  <div><p>LuxAed устанавливает заборы под ключ в Таллинне и Харьюмаа, от замера до готового ограждения. Работаем с деревом, профнастилом, металлическим штакетником, рулонной и 2D/3D-сеткой. Закажите у нас <a href="/ru/vorota-avtomatika/">установку автоматических ворот</a> и <a href="/ru/domofony-videodomofony/">видеодомофон с открыванием калитки</a>, чтобы весь въезд работал как одна система.</p></div>
</div></div></section>'''
sub_once(r'<section class="info-strip">.*?</section>', info, 'service_scope')

# The homepage keeps its visible FAQ without FAQPage markup (/ru/faq/ carries
# the FAQPage schema). Remove any FAQPage block left from earlier builds.
s, removed_faq_schema = re.subn(
    r'<script type="application/ld\+json">\s*\{\s*"@context"\s*:\s*"https://schema\.org"\s*,\s*"@type"\s*:\s*"FAQPage".*?</script>\n?',
    '', s, flags=re.DOTALL)
if removed_faq_schema:
    changed.append('faq_schema_removed')
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
    (r'<span class="ht-score">\d+% рекомендуют</span>', f'<span class="ht-score">{build_pages.RECOMMEND_PERCENT}% рекомендуют</span>'),
    (r'<div class="hstat"><b>\d+%</b><span>рекомендуют в Facebook</span></div>', f'<div class="hstat"><b>{build_pages.RECOMMEND_PERCENT}%</b><span>рекомендуют в Facebook</span></div>'),
    (r'<div class="hstat"><b>\d+</b><span>отзыва в Facebook</span></div>', f'<div class="hstat"><b>{build_pages.REVIEW_COUNT}</b><span>отзыва в Facebook</span></div>'),
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
sub_once(r'<script>\s*\n(?:window\.__t0[^\n]*\n)?function closeMob\(\).*?</script>(?:\s*<script src="/assets/lead-form\.js\?v=[^"]+" defer></script>)*(?:\s*<script>window\.va = [^\n]*</script>)?(?:\s*<script defer src="/_vercel/insights/script\.js"></script>)?', build_pages.SCRIPTS, 'SCRIPTS')
# 2) the same lead form as every generated RU landing page.
ru_lead_form = render_lead_form('ru')
sub_once(r'(?:<!-- LEAD_FORM_START -->\s*)?<div class="form-slot">\s*<div class="form-card[^\"]*" id="form">.*?</form>\s*</div>\s*</div>\s*(?:<!-- LEAD_FORM_END -->)?', ru_lead_form, 'lead_form')
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
