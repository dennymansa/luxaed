#!/usr/bin/env python3
# RU support pages: o-nas, faq, kontakty, privaatsus, tingimused
import json, html
from build_pages import head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN, about_page_schema, person_artur_schema, webpage_schema
from gen_ru import form_html, faq_html

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
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><span class="ht-label">34 отзыва в Facebook · рекомендуют</span></div>
    <h1>Кто мы</h1>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:16px;max-width:720px">Мы специализируемся на изготовлении и установке заборов, ворот и калиток в Таллинне и Харьюмаа <b>уже более 15 лет</b>. Работаем с деревом, профнастилом и сварной 3D-сеткой, ставим автоматику ворот и домофоны и ремонтируем существующие конструкции. Наш мастер видел все типы заборов, грунтов и водоотвода.</p>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:12px;max-width:720px">Берём весь процесс на себя: приезжаем на бесплатный замер, закупаем материалы, устанавливаем и передаём готовый объект. Стоимость называем заранее. Без скрытых доплат и сюрпризов.</p>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:12px;max-width:720px">Новый забор вокруг дачи, откатные ворота с автоматикой или ограждение всей территории. Поможем с любой задачей.</p>
  </div></div>
  <div class="hero-stats"><div class="hstat"><b>100%</b><span>Рекомендуют в Facebook</span></div><div class="hstat"><b>34</b><span>Отзыва</span></div><div class="hstat"><b>15</b><span>Лет опыта мастеров</span></div></div></div>
</section>
<section class="section"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Мастер</span><h2 class="big">Артур Мустафин. Более 15 лет опыта в строительстве заборов и ворот.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-artur.webp"><img src="/img/luxaed-artur.jpg" width="750" height="1000" alt="Артур Мустафин, мастер LuxAed" loading="lazy"></picture></div>
  <div class="equip-body"><p class="lead" style="margin-bottom:14px">За 15 лет работы Артур построил тысячи заборов и ворот в Таллинне и Харьюмаа. Благодаря большому опыту он заранее знает, какое решение лучше подойдёт именно для вашего участка, какие материалы выбрать и как избежать лишних затрат.</p><ul class="svc-bens">
    <li>Более 15 лет опыта в строительстве заборов и ворот</li>
    <li>Тысячи выполненных объектов в Таллинне и Харьюмаа</li>
    <li>Работа с любыми типами заборов, ворот и автоматики</li>
    <li>Опыт на участках с любыми грунтами и рельефом</li>
    <li>Помощь с выбором материалов и оптимального решения</li>
    <li>Контроль качества на каждом этапе работ</li>
  </ul><p style="margin-top:16px"><b>Мы не просто устанавливаем заборы.</b> Мы строим надёжные решения, которые прослужат долгие годы.</p></div>
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
    <li>Более <b>15 лет</b> опыта в Таллинне и Харьюмаа</li>
    <li>Заборы из дерева, профнастила и сварной 3D-сетки</li>
    <li>Откатные и распашные ворота, автоматика и домофоны</li>
    <li>Закупку материалов и весь процесс берём на себя</li>
    <li>Бесплатный замер, цена заранее, гарантия на работы</li>
    <li>Работаем круглый год, включая зиму</li>
  </ul>
</div></section>
<section class="section section--dark" style="position:relative;overflow:hidden"><div style="position:absolute;inset:0;background:url('/img/luxaed-sunset.webp') center 40%/cover no-repeat;pointer-events:none"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(8,10,16,.92) 0%, rgba(10,12,20,.74) 40%, rgba(12,10,16,.86) 100%);pointer-events:none"></div>
  <div class="wrap" style="position:relative"><span class="tag">Нам доверяют</span><h2 class="big big--xl">Отзывы говорят за нас</h2>
  <p class="lead lead--lg">Клиенты рекомендуют LuxAed за скорость, качество и профессиональный подход.<br>Смотрите отзывы на нашей странице в <a href="{FB}" target="_blank" rel="noopener" style="color:var(--accent)">Facebook</a>.</p>
  <div class="nums">
    <div class="num"><b>100<small>%</small></b><div class="t">Рекомендуют</div><p>По отзывам в Facebook</p></div>
    <div class="num"><b>34</b><div class="t">Отзыва</div><p>Реальные отзывы клиентов</p></div>
    <div class="num"><b>15</b><div class="t">Лет опыта</div><p>Опыт наших мастеров в заборах и воротах</p></div>
    <div class="num"><b>2000<small>+</small></b><div class="t">Заборов</div><p>Установлено за 15 лет</p></div>
  </div></div>
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
<section class="cta-final"><div class="wrap"><h2>Обсудим <em>ваш забор или ворота</em>?</h2>
  <p>Оставьте заявку или позвоните. Приедем на бесплатный замер и назовём точную стоимость.</p>
  <div class="hero-btns"><a class="btn btn-accent" href="/ru/#form">Оставить заявку →</a><a class="btn btn-ghost" href="tel:{TEL}">Позвонить {PHONE}</a></div></div></section>'''
page("/ru/o-nas/","О компании LuxAed. Заборы и ворота в Таллинне","LuxAed. Заборы и ворота в Таллинне и Харьюмаа. Дерево, профнастил, 3D-сетка, автоматика. 100% рекомендуют в Facebook.", about_inner, schema=[about_page_schema("/ru/o-nas/","ru","О компании LuxAed","Мастер по заборам и воротам Артур Мустафин и история LuxAed в Таллинне и Харьюмаа."),person_artur_schema("ru")])

# ---------- FAQ ----------
FAQ=[("Сколько стоит забор или ворота?","Точную стоимость назвать заранее нельзя. Она зависит от материала, длины и высоты забора, рельефа участка и наличия ворот с автоматикой. После бесплатного замера мы называем конкретную цену без скрытых доплат."),
("Из каких материалов вы делаете заборы?","Дерево (на стальном каркасе), профнастил и сварную 3D-сетку. Поможем выбрать материал под ваш бюджет, участок и внешний вид."),
("Вы ставите автоматику на ворота?","Да, устанавливаем автоматику откатных и распашных ворот, пульты, фотоэлементы и домофоны. Можем поставить автоматику и на уже существующие ворота."),
("Какие районы вы обслуживаете?","Работаем в Таллинне и по всей Харьюмаа. Если объект дальше, напишите, обсудим возможность выезда."),
("Вы делаете ремонт заборов?","Да, ремонтируем заборы и ворота: замена секций и столбов, регулировка створок, ремонт автоматики и фурнитуры."),
("Сколько времени занимает установка?","Зависит от объёма работ и материала. Ориентировочный срок назовём после замера и согласования проекта."),
("Нужно ли готовить участок заранее?","Желательно обеспечить свободный доступ к линии будущего забора. Остальное обсудим индивидуально."),
("Как оставить заявку?","Позвоните по телефону "+PHONE+", напишите на "+EMAIL+" или заполните форму на сайте. Мы всегда на связи.")]
faq_schema=['<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]},ensure_ascii=False)+'</script>']
faq_inner=f'''{hero("Вопросы и ответы","Частые вопросы о заборах и воротах","Собрали ответы на вопросы, которые чаще всего задают перед заказом забора или ворот.", crumb="Вопросы")}
<section class="section"><div class="wrap"><span class="tag">FAQ</span><h2 class="big">Что спрашивают перед заказом</h2>{faq_html(FAQ)}</div></section>
<section class="cta-final"><div class="wrap"><h2>Не нашли ответ?</h2><p>Позвоните или напишите. Подскажем и приедем на бесплатный замер.</p>
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
 ("Кто обрабатывает данные","LuxAed (заборы и ворота, Таллинн, Эстония) обрабатывает персональные данные, которые вы предоставляете при обращении через сайт, телефон, email или Facebook."),
 ("Какие данные мы собираем","Имя, телефон, email, адрес участка и описание задачи, а также фотографии, которые вы прикрепляете к заявке. Эти данные нужны, чтобы подготовить расчёт и связаться с вами."),
 ("Цель и правовое основание","Данные используются только для ответа на заявку, подготовки предложения и оказания услуг. Правовое основание: ваше согласие и подготовка к заключению договора."),
 ("Хранение данных","Мы храним данные столько, сколько необходимо для обработки заявки и исполнения услуги, после чего удаляем их, если нет иных законных оснований для хранения."),
 ("Передача третьим лицам","Мы не продаём и не передаём ваши данные третьим лицам, кроме случаев, предусмотренных законом."),
 ("Ваши права","Вы вправе запросить доступ к своим данным, их исправление или удаление, а также отозвать согласие. Для этого свяжитесь с нами по email."),
 ("Cookie","Сайт может использовать технические cookie для корректной работы. Аналитические и рекламные скрипты подключаются только при наличии соответствующего согласия."),
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
