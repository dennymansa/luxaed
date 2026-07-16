#!/usr/bin/env python3
# RU support pages: o-nas, faq, kontakty, privaatsus, tingimused
import json, html
from build_pages import head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN, about_page_schema, person_artur_schema, webpage_schema, REVIEW_COUNT, EXPERIENCE_YEARS, RECOMMEND_PERCENT


def faq_html(items):
    return '<div class="faq" id="faqList">' + ''.join(
        f'<div class="faq-item"><button class="faq-q">{q}</button><div class="faq-a"><p>{a}</p></div></div>'
        for q, a in items
    ) + '</div>'

def hero(kicker, h1, lead, img="luxaed-wide-wood", crumb=None):
    cr=''  # visible breadcrumbs removed per request (JSON-LD kept for SEO)
    return f'''<section class="svc-hero">
  <div class="hero-photo-bg" style="background:url('/img/{img}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap">{cr}
    <span class="tag">{kicker}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="hero-btns"><a class="btn btn-accent" href="/ru/#form">Оставить заявку →</a><a class="btn btn-ghost" href="tel:{TEL}">Позвонить {PHONE}</a></div>
  </div>
</section>'''

def page(path, title, desc, inner, og="/img/luxaed-hero.jpg", schema=None):
    H=head("ru", path, title, desc, og_img=og, schema_blocks=schema)
    body=f'''{nav("ru", path)}
<main id="main">
{inner}
</main>
<div class="lb" id="lb"><button class="lb-x" aria-label="Закрыть">&times;</button><img src="" alt="" id="lbImg"></div>
{footer("ru")}
<div class="mob-bar"><a class="btn btn-accent mob-call" href="tel:{TEL}"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="vertical-align:-3px;margin-right:6px"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>Позвонить</a></div>
{SCRIPTS}
</body></html>'''
    print("wrote", write(path, H+"\n"+body))

# ---------- О НАС ----------
about_inner=f'''<section class="hero hero--compact">
  <div class="hero-photo-bg" style="background:url('/img/luxaed-hero.webp') center 45%/cover no-repeat"></div>
  <div class="wrap"><div class="hero-grid" style="grid-template-columns:1fr;gap:0"><div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">{RECOMMEND_PERCENT}%</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">{REVIEW_COUNT} отзыва в Facebook · рекомендуют</a></div>
    <h1>Кто мы</h1>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:16px;max-width:720px">Мы специализируемся на изготовлении и установке заборов, ворот и калиток в Таллинне и Харьюмаа <b>уже более {EXPERIENCE_YEARS} лет</b>. Работаем с деревом, рулонной сеткой и рабицей, сварной 2D/3D-сеткой, металлическим штакетником, прутковыми секциями и профнастилом, ставим автоматику ворот и домофоны и ремонтируем существующие конструкции. Опыт помогает учитывать тип грунта, рельеф и водоотвод.</p>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:12px;max-width:720px">Берём весь процесс на себя: приезжаем на бесплатный замер, закупаем материалы, устанавливаем и передаём готовый объект. Стоимость называем заранее. Без скрытых доплат и сюрпризов.</p>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:12px;max-width:720px">Новый забор вокруг дачи, откатные ворота с автоматикой или ограждение всей территории. Поможем с любой задачей.</p>
  </div></div>
  <div class="hero-stats"><div class="hstat"><b>{RECOMMEND_PERCENT}%</b><span>Рекомендуют в Facebook</span></div><div class="hstat"><b>{REVIEW_COUNT}</b><span>Отзыва</span></div><div class="hstat"><b>{EXPERIENCE_YEARS}+</b><span>Лет опыта мастеров</span></div></div></div>
</section>
<section class="section"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Мастер</span><h2 class="big">Артур Мустафин.<br>Более {EXPERIENCE_YEARS} лет опыта в строительстве заборов и ворот.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-w-crew.webp"><img src="/img/luxaed-w-crew.jpg" width="1000" height="1333" alt="Мастер LuxAed монтирует забор" loading="lazy"></picture></div>
  <div class="equip-body"><p class="lead" style="margin-bottom:14px">Артур строит заборы и ворота в Таллинне и Харьюмаа более {EXPERIENCE_YEARS} лет. Он помогает выбрать подходящее участку решение и избежать лишних затрат.</p><ul class="svc-bens">
    <li>Более {EXPERIENCE_YEARS} лет опыта в строительстве заборов и ворот</li>
    <li>Выполненные объекты в Таллинне и Харьюмаа</li>
    <li>Контроль качества на каждом этапе работ</li>
  </ul></div>
</div></div></section>
<section class="section section--alt"><div class="wrap">
  <span class="tag">Принципы</span><h2 class="big">Что для нас важно</h2>
  <div class="svc-cards">
    <div class="svc-card"><div class="ic">1</div><h3>Всё одним звонком</h3><p>Замер, материалы, монтаж и ремонт. Из одних рук. Один звонок, и всё организовано.</p></div>
    <div class="svc-card"><div class="ic">2</div><h3>Работаем круглый год</h3><p>Ставим заборы и зимой. Мёрзлый грунт не проблема. Не переносим на весну.</p></div>
    <div class="svc-card"><div class="ic">3</div><h3>Аккуратные руки</h3><p>Работаем чисто, бережём участок и убираем за собой. Сдаём объект в порядке.</p></div>
    <div class="svc-card"><div class="ic">4</div><h3>Точная цена заранее</h3><p>Называем стоимость до начала и держим слово. Без скрытых доплат и сюрпризов в счёте.</p></div>
  </div>
</div></section>
<section class="section"><div class="wrap">
  <span class="tag">Почему мы</span><h2 class="big">Почему LuxAed</h2>
  <ul class="svc-bens">
    <li>Более <b>{EXPERIENCE_YEARS} лет</b> опыта в Таллинне и Харьюмаа</li>
    <li>Дерево, рулонная и сварная 2D/3D-сетка, штакетник, прутковые секции и профнастил</li>
    <li>Откатные и распашные ворота, автоматика и домофоны</li>
    <li>Закупку материалов и весь процесс берём на себя</li>
    <li>Бесплатный замер, цена заранее, гарантия на работы</li>
    <li>Работаем круглый год, включая зиму</li>
  </ul>
</div></section>
<section class="section section--dark" style="position:relative;overflow:hidden"><div style="position:absolute;inset:0;background:url('/img/luxaed-sunset.webp') center 40%/cover no-repeat;pointer-events:none"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(8,10,16,.95) 0%, rgba(10,12,20,.82) 40%, rgba(12,10,16,.9) 100%);pointer-events:none"></div>
  <div class="wrap" style="position:relative"><span class="tag">Нам доверяют</span><h2 class="big big--xl">Отзывы говорят за нас</h2>
  <p class="lead lead--lg">Клиенты рекомендуют LuxAed за скорость, качество и профессиональный подход.<br>Смотрите отзывы на нашей странице в <a href="{FB}" target="_blank" rel="noopener" style="color:var(--accent)">Facebook</a>.</p>
  </div>
</section>
<section class="section section--alt"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Оснащение</span><h2 class="big">Правильная техника, опытная бригада, аккуратный результат.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-w-van.webp"><img src="/img/luxaed-w-van.jpg" width="750" height="563" alt="Бригада LuxAed и фирменный бус на объекте" loading="lazy"></picture></div>
  <div class="equip-body"><ul class="spec">
    <li><b>Бур для столбов и трамбовка</b>: столбы встают прочно и по уровню</li>
    <li><b>Сварка и резка на месте</b>: стальные каркасы и рамы ворот</li>
    <li><b>Нивелир и замер</b>: секции в одну линию, даже на склоне</li>
    <li><b>Автоматика и домофоны</b>: настраиваем и подключаем под ключ</li>
    <li><b>Чистый объект</b>: убираем за собой и сдаём участок в порядке</li>
  </ul></div>
</div></div></section>
<section class="cta-final"><div class="wrap"><h2>Обсудим <em>ваш забор и ворота</em>?</h2>
  <p>Оставьте заявку или позвоните. Приедем на бесплатный замер и назовём точную стоимость.</p>
  <div class="hero-btns"><a class="btn btn-accent" href="/ru/#form">Оставить заявку →</a><a class="btn btn-ghost" href="tel:{TEL}">Позвонить {PHONE}</a></div></div></section>'''
page("/ru/o-nas/","О компании LuxAed. Заборы и ворота в Таллинне",f"LuxAed. Все основные типы заборов, ворота и автоматика в Таллинне и Харьюмаа. Более {EXPERIENCE_YEARS} лет опыта. {RECOMMEND_PERCENT}% рекомендуют в Facebook.", about_inner, schema=[about_page_schema("/ru/o-nas/","ru","О компании LuxAed","Мастер по заборам и воротам Артур Мустафин и история LuxAed в Таллинне и Харьюмаа."),person_artur_schema("ru")])

# ---------- FAQ ----------
FAQ=[("Сколько стоит забор или ворота?","Точную стоимость назвать заранее нельзя. Она зависит от материала, длины и высоты забора, рельефа участка и наличия ворот с автоматикой. После бесплатного замера мы называем конкретную цену без скрытых доплат."),
("Из каких материалов вы делаете заборы?","Делаем деревянные заборы, ограждения из рулонной сетки и рабицы, сварной 2D/3D-сетки, металлического штакетника, прутковых металлических секций и профнастила. Если нужен другой вариант, пришлите фотографию или пример."),
("Вы ставите автоматику на ворота?","Да, устанавливаем автоматику откатных и распашных ворот, пульты, фотоэлементы и домофоны. Можем поставить автоматику и на уже существующие ворота."),
("Какие районы вы обслуживаете?","Работаем в Таллинне и по всей Харьюмаа. Если объект дальше, напишите, обсудим возможность выезда."),
("Вы делаете ремонт заборов?","Да, ремонтируем заборы и ворота: замена секций и столбов, регулировка створок, ремонт автоматики и фурнитуры."),
("Сколько времени занимает установка?","Зависит от объёма работ и материала. Ориентировочный срок назовём после замера и согласования проекта."),
("Нужно ли готовить участок заранее?","Желательно обеспечить свободный доступ к линии будущего забора. Остальное обсудим индивидуально."),
("Как оставить заявку?","Позвоните по телефону "+PHONE+", напишите на "+EMAIL+" или заполните форму на сайте. Мы всегда на связи.")]
faq_schema=['<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]},ensure_ascii=False)+'</script>']
faq_inner=f'''{hero("Вопросы и ответы","Частые вопросы о заборах и воротах","Собрали ответы на вопросы, которые чаще всего задают перед заказом забора или ворот.", crumb="Вопросы")}
<section class="section"><div class="wrap"><span class="tag">FAQ</span><h2 class="big">Что спрашивают перед заказом</h2>{faq_html(FAQ)}</div></section>
<section class="cta-final"><div class="wrap"><h2>Не нашли ответ?</h2><p>Позвоните или напишите.<br>Подскажем и приедем на бесплатный замер.</p>
<div class="hero-btns"><a class="btn btn-accent" href="/ru/#form">Оставить заявку →</a><a class="btn btn-ghost" href="tel:{TEL}">Позвонить {PHONE}</a></div></div></section>'''
page("/ru/faq/","Вопросы и ответы о заборах и воротах — LuxAed","Частые вопросы о заборах, воротах и автоматике в Таллинне: цена, материалы, сроки, автоматика, ремонт. Ответы от LuxAed.", faq_inner, schema=faq_schema)

# ---------- КОНТАКТЫ ----------

# ---------- LEGAL ----------
def legal_page(path, title, h1, kicker, blocks):
    inner=f'''{hero(kicker,h1,"", img="luxaed-g3", crumb=h1)}
<section class="section"><div class="wrap" style="max-width:820px">
{"".join(f"<h2 class='big' style='font-size:24px;margin-top:28px'>{t}</h2><p class='lead' style='margin-top:10px'>{b}</p>" for t,b in blocks)}
<p class="lead" style="margin-top:26px">По вопросам, связанным с этим документом, пишите на <a href="mailto:{EMAIL}" style="color:var(--accent)">{EMAIL}</a>.</p>
</div></section>'''
    page(path,title,h1+" — LuxAed, заборы и ворота в Таллинне.",inner,schema=[webpage_schema(path,"ru",title,h1)])

legal_page("/ru/privaatsus/","Политика конфиденциальности — LuxAed","Политика конфиденциальности","Конфиденциальность",[
 ("Ответственный за обработку данных","Ответственным за обработку персональных данных является LuxAed, Таллинн, Эстония. По вопросам защиты данных свяжитесь с нами по электронной почте "+EMAIL+" или по телефону "+PHONE+"."),
 ("Какие данные мы собираем","Если вы отправляете запрос через веб-форму, по телефону, электронной почте или через Facebook, мы можем обрабатывать ваше имя, номер телефона, адрес электронной почты, адрес или район объекта, выбранную услугу, сообщение и приложенные фотографии. К заявке из формы также могут добавляться первая посещённая страница, источник перехода и параметры рекламной кампании, чтобы мы понимали, из какого канала пришёл запрос. Для обеспечения безопасности и надёжности веб-сервер также может обрабатывать технические данные, например IP-адрес, время запроса, тип браузера и журнальные записи."),
 ("Цели и правовые основания обработки","Мы используем контактные данные и данные об объекте, чтобы ответить на запрос, организовать замер, подготовить предложение и оказать услугу. Правовым основанием является принятие мер до заключения договора или исполнение договора. Для обеспечения безопасности, предотвращения злоупотреблений и ведения делопроизводства мы можем основываться на законном интересе. Измерение с помощью Google Ads мы используем только с вашего согласия."),
 ("Поставщики услуг и передача данных","Мы не продаём ваши персональные данные. В необходимом объёме данные от нашего имени обрабатывают поставщики услуг: Vercel — для размещения сайта и технической обработки веб-формы, а Google Gmail — для пересылки запросов и их хранения в электронной почте. При наличии согласия мы используем Google Ads для измерения конверсий. Поставщики услуг могут привлекать субобработчиков и обрабатывать данные за пределами Европейской экономической зоны; в таком случае применяются предусмотренные условиями поставщика меры защиты данных, например стандартные договорные положения Европейской комиссии."),
 ("Файлы cookie и Google Ads","Сайт сохраняет ваш выбор в отношении файлов cookie в локальном хранилище браузера. По умолчанию код измерения Google Ads работает в режиме Consent Mode со статусом согласия «отказано». Хранение рекламных и аналитических данных разрешается только после того, как вы выберете «Согласен». Вы можете изменить свой выбор, удалив данные сайта luxaed.ee в браузере и выбрав вариант заново."),
 ("Хранение и безопасность","Мы храним данные запроса столько, сколько необходимо для его обработки, подготовки предложения и исполнения возможного договора, урегулирования претензий либо выполнения установленной законом обязанности. Когда данные больше не требуются, они удаляются или анонимизируются. Мы ограничиваем доступ к данным и применяем разумные технические и организационные меры безопасности."),
 ("Ваши права","Вы вправе запросить доступ к своим персональным данным, потребовать их исправления или удаления, ограничить обработку, возразить против обработки на основании законного интереса и в любое время отозвать согласие. Если обработка основана на согласии или договоре и выполнены применимые условия, вы можете запросить переносимость данных. Для подачи запроса напишите на "+EMAIL+". Вы также вправе подать жалобу в Инспекцию по защите данных Эстонии (Andmekaitse Inspektsioon)."),
 ("Обновление политики","Мы можем изменять политику конфиденциальности при изменении услуг или правовых требований. Актуальная версия публикуется на этой странице. Последнее обновление: 16.07.2026."),
])

legal_page("/ru/tingimused/","Условия обслуживания — LuxAed","Условия обслуживания","Условия",[
 ("Общие положения","Настоящие условия описывают порядок оказания услуг LuxAed по изготовлению, установке и ремонту заборов, ворот и автоматики в Таллинне и Харьюмаа."),
 ("Заявка и расчёт","Заявку можно оставить по телефону, email или через форму на сайте. Стоимость определяется после бесплатного замера и согласовывается до начала работ."),
 ("Замер и договорённости","Точная цена, материалы и сроки фиксируются после выезда на объект. Все существенные условия согласовываются с заказчиком заранее."),
 ("Оплата","Порядок и способ оплаты согласовываются индивидуально до начала работ. Мы не берём скрытых доплат сверх согласованной сметы без вашего согласия."),
 ("Гарантия и качество","Мы отвечаем за качество выполненных работ. Условия гарантии зависят от вида работ и материалов и оговариваются при заключении договора."),
 ("Ответственность","LuxAed не несёт ответственности за повреждения, вызванные скрытыми коммуникациями на участке, о которых заказчик не предупредил, а также за форс-мажор."),
 ("Контакты","По всем вопросам, связанным с услугами и условиями, свяжитесь с нами по телефону "+PHONE+" или email "+EMAIL+"."),
])

print("RU support pages done")
