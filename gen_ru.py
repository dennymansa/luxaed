#!/usr/bin/env python3
# Generates RU service pages + support pages, using build_pages lib.
import json, html
from build_pages import (head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN, SVC)

def form_html(lang="ru"):
    chips=[("zabor","Забор"),("vorota","Ворота/калитка"),("avtomatika","Автоматика"),("remont","Ремонт")]
    ov='<svg class="chip-oval" viewBox="0 0 220 64" preserveAspectRatio="none" aria-hidden="true"><path d="M40 16C92 5 158 6 196 18 215 24 210 49 172 56 110 66 48 64 20 50 7 43 12 17 50 11 78 7 104 9 126 13"/></svg>'
    ch="".join(f'<button type="button" class="chip" data-svc="{s}">{ov}{t}<span class="chip-tick" aria-hidden="true">✓</span></button>' for s,t in chips)
    return f'''<div class="form-slot"><div class="form-card" id="form">
  <span class="form-tag">Оформить заявку</span>
  <h2>Что нужно сделать? <span class="pick-hint">(выберите)</span></h2>
  <form id="leadForm">
    <input type="hidden" name="service" id="serviceField">
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:0;top:0;width:1px;height:1px;opacity:0;overflow:hidden">
    <div class="chips" id="svcChips" role="radiogroup">{ch}</div>
    <div class="ff" data-svc="zabor"><select name="material" class="form-select" aria-label="Материал забора"><option value="">Материал забора</option><option>Дерево</option><option>Профнастил</option><option>3D-сетка (сварная)</option><option>Не знаю — подскажите</option></select></div>
    <div class="ff form-grid2" data-svc="zabor"><input type="text" name="length" inputmode="numeric" placeholder="Длина, м"><select name="height" class="form-select" aria-label="Высота"><option value="">Высота</option><option>до 1,5 м</option><option>1,5–2 м</option><option>выше 2 м</option></select></div>
    <div class="ff" data-svc="vorota,avtomatika"><select name="gate_type" class="form-select" aria-label="Тип ворот"><option value="">Тип ворот</option><option>Откатные</option><option>Распашные</option><option>Не знаю</option></select></div>
    <div class="ff" data-svc="vorota"><select name="automation" class="form-select" aria-label="Автоматика ворот?"><option value="">Автоматика ворот?</option><option>Да, с автоматикой</option><option>Без автоматики</option><option>Не знаю</option></select></div>
    <div class="ff form-grid2"><select name="plot" class="form-select" aria-label="Участок"><option value="">Участок</option><option>Ровный</option><option>Со склоном</option><option>Есть старый забор (демонтаж)</option><option>Не знаю</option></select><select name="timeline" class="form-select" aria-label="Когда?"><option value="">Когда?</option><option>Как можно скорее</option><option>В течение 1–3 мес.</option><option>Просто узнать цену</option></select></div>
    <div class="ff-base"><input type="text" name="address" placeholder="Адрес участка (город / район)"></div>
    <div class="form-grid">
      <input type="text" name="name" placeholder="Ваше имя *" required style="grid-column:1/-1">
      <input type="tel" name="phone" placeholder="Телефон *" required>
      <input type="email" name="email" placeholder="Email *" required>
    </div>
    <div class="ff"><textarea name="msg" placeholder="Комментарий: детали, пожелания, что отремонтировать..."></textarea></div>
    <label class="photo-upload ff" id="photoLabel"><input type="file" name="photos" accept="image/*" multiple id="photoInput" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);border:0"><svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg><span id="photoLabel-txt">Прикрепить фото (необязательно)</span></label>
    <button class="btn btn-accent" type="submit" style="width:100%;padding:13px;font-size:15px">Отправить заявку →</button>
    <p class="form-consent">Отправляя форму, вы соглашаетесь с <a href="/ru/privaatsus/">политикой конфиденциальности</a> и <a href="/ru/tingimused/">условиями</a></p>
    <div class="form-ok" id="formOk" role="status"><b>Спасибо, заявка принята.</b><br>Мы свяжемся с вами в ближайшее время.</div>
  </form>
</div></div>'''

def schema_service(name, desc, path, faq):
    svc={"@context":"https://schema.org","@type":"Service","serviceType":name,
         "provider":{"@type":"HomeAndConstructionBusiness","name":"LuxAed","telephone":PHONE,"email":EMAIL,
                     "areaServed":["Tallinn","Harjumaa","Estonia"],"url":DOMAIN+"/ru/"},
         "areaServed":["Tallinn","Harjumaa"],"description":desc,"url":DOMAIN+path}
    crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Главная","item":DOMAIN+"/ru/"},
        {"@type":"ListItem","position":2,"name":"Услуги","item":DOMAIN+"/ru/#uslugi"},
        {"@type":"ListItem","position":3,"name":name,"item":DOMAIN+path}]}
    faqs={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
    j=lambda o: '<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False)+'</script>'
    return [j(svc), j(crumb), j(faqs)]

def bens_html(items): return '<ul class="svc-bens">'+"".join(f"<li>{x}</li>" for x in items)+'</ul>'
def cards_html(cards): return '<div class="svc-cards">'+"".join(f'<div class="svc-card"><div class="ic">{ic}</div><h4>{n}</h4><p>{d}</p></div>' for ic,n,d in cards)+'</div>'
def gal_html(imgs): return '<div class="gal" id="gal">'+"".join(f'<a href="/img/{i}.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/{i}.webp"><img src="/img/{i}.jpg" alt="{html.escape(a)}" loading="lazy"></picture></a>' for i,a in imgs)+'</div>'
def faq_html(faq): return '<div class="faq" id="faqList">'+"".join(f'<div class="faq-item"><button class="faq-q">{q}</button><div class="faq-a"><p>{a}</p></div></div>' for q,a in faq)+'</div>'

PROCESS='''<div class="hsteps">
  <div class="hstep"><div class="hstep-num">1</div><h3>Вы оставляете заявку</h3><p>Один звонок или сообщение — и мы берём забор на себя. Приедем на бесплатный замер в удобное вам время.</p></div>
  <div class="hstep"><div class="hstep-num">2</div><h3>Подбираем и считаем</h3><p>Предложим материал и решение под ваш участок и бюджет и назовём точную стоимость — без сюрпризов в счёте.</p></div>
  <div class="hstep"><div class="hstep-num">3</div><h3>Аккуратно ставим</h3><p>Устанавливаем столбы, секции, ворота и автоматику. Держим вас в курсе на каждом этапе.</p></div>
  <div class="hstep"><div class="hstep-num">4</div><h3>Сдаём под ключ</h3><p>После завершения работ проверяем результат вместе с вами и передаём готовый объект — с рекомендациями по эксплуатации.</p></div>
</div>'''

def related_html(cur):
    cards=[(p,t) for p,t in SVC["ru"] if p!=cur][:3]
    return '<div class="svc-cards">'+"".join(f'<a class="svc-card" href="{p}" style="text-decoration:none"><div class="ic">→</div><h4>{t}</h4><p>Подробнее об услуге →</p></a>' for p,t in cards)+'</div>'

def service_page(c):
    sb=schema_service(c["name"], c["desc"], c["path"], c["faq"])
    H=head("ru", c["path"], c["title"], c["desc"], og_img=c.get("og",f'/img/{c["hero"]}.jpg'), schema_blocks=sb)
    body=f'''{nav("ru", c["path"])}
<main id="main">
<section class="svc-hero">
  <div class="hero-photo-bg" style="background:url('/img/{c["hero"]}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <span class="tag">{c["kicker"]}</span>
        <h1>{c["h1"]}</h1>
        <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><span class="ht-label">34 отзыва в Facebook · рекомендуют</span></div>
        <div class="hero-btns"><a class="btn btn-accent" href="#form">Оставить заявку →</a><a class="btn btn-ghost" href="tel:{TEL}">Позвонить {PHONE}</a></div>
      </div>
      {form_html()}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap"><span class="tag">Что вы получаете</span><h2 class="big">{c["intro_h"]}</h2><p class="lead">{c["intro_p"]}</p>{bens_html(c["bens"])}</div>
</section>

<section class="section section--alt">
  <div class="wrap"><span class="tag">Варианты</span><h2 class="big">{c["variants_h"]}</h2>{cards_html(c["variants"])}
    <div class="svc-cta"><b>{c["cta_band"]}</b><a class="btn" href="#form">Оставить заявку →</a></div></div>
</section>

<section class="section">
  <div class="wrap"><span class="tag">Честно о цене</span><h2 class="big">От чего зависит стоимость</h2>
    <p class="lead">Фиксированного прайса нет — точную цену называем после бесплатного замера. Вот что входит в работу и что влияет на итог.</p>
    <div class="honest">
      <div class="hon good"><h3>Всегда входит в процесс</h3><ul>{"".join(f"<li>{x}</li>" for x in c["incl"])}<li>Работаем круглый год, включая зиму</li><li>Гарантия на выполненные работы</li></ul></div>
      <div class="hon bad"><h3>Влияет на стоимость</h3><ul>{"".join(f"<li>{x}</li>" for x in c["factors"])}</ul></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap"><span class="tag">Как мы работаем</span><h2 class="big">Четыре шага до готового результата</h2>{PROCESS}</div>
</section>

<section class="section">
  <div class="wrap"><span class="tag">Галерея</span><h2 class="big">Примеры работ</h2><p class="lead">Реальные фотографии выполненных конструкций.</p>{gal_html(c["gallery"])}</div>
</section>

<section class="section section--alt">
  <div class="wrap"><span class="tag">Вопросы</span><h2 class="big">Частые вопросы</h2>{faq_html(c["faq"])}</div>
</section>

<section class="section">
  <div class="wrap"><span class="tag">Другие услуги</span><h2 class="big">Смотрите также</h2>{related_html(c["path"])}</div>
</section>

<section class="cta-final">
  <div class="wrap"><h2>Готовы обсудить <em>{c["name"].lower()}</em> для вашего участка?</h2>
    <p>Оставьте заявку или позвоните — приедем на бесплатный замер и назовём точную цену.</p>
    <div class="hero-btns"><a class="btn btn-accent" href="#form">Оставить заявку →</a><a class="btn btn-ghost" href="tel:{TEL}">Позвонить {PHONE}</a></div></div>
</section>
</main>
<div class="lb" id="lb"><button class="lb-x" aria-label="Закрыть">&times;</button><img src="" alt="" id="lbImg"></div>
{footer("ru")}
<div class="mob-bar"><a class="btn btn-accent mob-call" href="tel:{TEL}"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="vertical-align:-3px;margin-right:6px"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>Позвонить</a></div>
{SCRIPTS}
</body></html>'''
    fp=write(c["path"], H+"\n"+body)
    print("wrote", fp)

# ---------------- RU SERVICE CONTENT ----------------
SERVICES=[
{
 "path":"/ru/uslugi/setka-3d/","name":"Сетчатые и 3D-заборы","hero":"luxaed-svc-mesh","og":"/img/luxaed-svc-mesh.jpg",
 "title":"Сетчатые и 3D-заборы (сварные панели) в Таллинне — LuxAed",
 "desc":"Установка сетчатых и 3D-заборов из сварных панелей в Таллинне и Харьюмаа. Оцинковка + порошковая окраска, антрацит RAL 7016, столбы и монтаж под ключ. Бесплатный замер.",
 "kicker":"3D-сетка · сварные панели","h1":"Сетчатые<br><em>и 3D-заборы</em><br>в Таллинне",
 "lead":"Современные сварные 3D-панели с рёбрами жёсткости: прочно, аккуратно и с хорошей просматриваемостью участка. Оцинковка плюс порошковая окраска — служит десятилетиями.",
 "intro_h":"Почему выбирают 3D-заборы","intro_p":"Сварная панель с изгибами (3D) держит форму без парусности, не провисает и выглядит современно. Отличное решение для частных домов, таунхаусов и территорий.",
 "bens":["Прочные сварные панели с рёбрами жёсткости","Оцинковка + порошковая окраска — не ржавеет","Антрацит RAL 7016 и другие цвета","Хорошая просматриваемость и минимум парусности","Быстрый монтаж на столбы","Подходит для домов, таунхаусов и территорий"],
 "variants_h":"Какие бывают сетчатые заборы",
 "variants":[("3D","3D-панели","Сварная панель с V-образными рёбрами жёсткости — самый популярный и прочный вариант."),
             ("2D","2D двойной пруток","Двойной горизонтальный пруток — усиленная плоская панель для больших пролётов."),
             ("◧","Цвета RAL","Антрацит RAL 7016, зелёный RAL 6005, чёрный и другие цвета покрытия."),
             ("▤","Столбы и крепёж","Оцинкованные столбы с заглушками, планки и крепёж под панель.")],
 "cta_band":"Рассчитаем 3D-забор под ваш участок",
 "incl":["Выезд на замер участка","Установка оцинкованных столбов","Монтаж сварных панелей и крепежа","Выравнивание по уровню и рельефу","Проверка конструкции после монтажа"],
 "factors":["Длина забора и высота панелей (1.23–2.03 м)","Цвет и тип панели (2D/3D)","Рельеф участка и подготовка основания","Количество ворот и калиток","Демонтаж старого забора"],
 "gallery":[("luxaed-svc-mesh","Сварной 3D-сетчатый забор"),("luxaed-mesh-2","3D-сетчатый забор вдоль участка"),("luxaed-mesh-3","Сетчатый забор с зелёными столбами"),("luxaed-mesh-gate","Сетчатые ворота LuxAed")],
 "faq":[("Сколько служит 3D-забор?","При оцинковке и порошковой окраске сварные панели служат десятилетиями и не ржавеют. Точный срок зависит от условий эксплуатации."),
        ("Какая высота панелей бывает?","Стандартно от 1.23 до 2.03 м. Подберём высоту под задачу — приватность или обозначение границ."),
        ("Какой цвет выбрать?","Самые популярные — антрацит RAL 7016 и зелёный RAL 6005. Доступны и другие цвета покрытия."),
        ("Можно ли поставить ворота в тон забору?","Да, делаем откатные и распашные ворота с заполнением сварной панелью в тот же цвет.")],
},
{
 "path":"/ru/uslugi/derevyannye-zabory/","name":"Деревянные заборы","hero":"luxaed-svc-wood","og":"/img/luxaed-svc-wood.jpg",
 "title":"Деревянные заборы и ворота в Таллинне — LuxAed",
 "desc":"Производство и установка деревянных заборов и ворот в Таллинне и Харьюмаа. Горизонтальный забор, штакетник, жалюзи, стальной каркас, обработка дерева. Бесплатный замер и расчёт.",
 "kicker":"Дерево · стальной каркас","h1":"Деревянные<br><em>заборы</em><br>в Таллинне",
 "lead":"Тёплый, аккуратный вид участка. Делаем заборы и ворота из обработанного дерева на прочном стальном каркасе — сочетание природного дерева и надёжного металла.",
 "intro_h":"Почему деревянный забор","intro_p":"Дерево выглядит дорого и естественно, вписывается в любой участок. На стальном каркасе конструкция не провисает и служит долго.",
 "bens":["Обработанная древесина под погоду Эстонии","Прочный стальной каркас — не провисает","Горизонтальные, вертикальные и жалюзи","Заборы и ворота в едином стиле","Возможна автоматика ворот","Индивидуальный дизайн под участок"],
 "variants_h":"Виды деревянных заборов",
 "variants":[("▤","Горизонтальный","Горизонтальные доски на стальном каркасе — современный популярный вид."),
             ("▥","Штакетник","Классический вертикальный штакетник с зазором или без."),
             ("◫","Жалюзи (ранчо)","Наклонные ламели — приватность с продуваемостью."),
             ("⛩","Ворота из дерева","Откатные и распашные ворота с деревянным заполнением и автоматикой.")],
 "cta_band":"Подберём деревянный забор под ваш дом",
 "incl":["Выезд на замер участка","Изготовление секций и стального каркаса","Установка столбов и монтаж секций","Обработка и покрытие дерева","Проверка конструкции после монтажа"],
 "factors":["Длина и высота забора","Тип (горизонтальный, штакетник, жалюзи)","Порода и обработка древесины","Ворота и автоматика","Рельеф и подготовка основания"],
 "gallery":[("luxaed-svc-wood","Деревянный забор со стальным каркасом"),("luxaed-g1","Деревянный забор и откатные ворота"),("luxaed-wood-2","Деревянный забор на участке"),("luxaed-wood-3","Деревянный забор и ворота")],
 "faq":[("Дерево не сгниёт?","Используем обработанную древесину и покрытие, а каркас делаем стальным. При правильном уходе забор служит долгие годы."),
        ("Можно горизонтальные доски?","Да, горизонтальный забор на стальном каркасе — один из самых популярных вариантов."),
        ("Сделаете ворота в том же стиле?","Да, изготавливаем откатные и распашные ворота с деревянным заполнением под общий дизайн."),
        ("Нужен ли уход за забором?","Периодически рекомендуется обновлять защитное покрытие дерева — расскажем, как ухаживать.")],
},
{
 "path":"/ru/uslugi/profnastil/","name":"Заборы из профнастила","hero":"luxaed-svc-profnastil","og":"/img/luxaed-svc-profnastil.jpg",
 "title":"Заборы из профнастила в Таллинне — LuxAed",
 "desc":"Установка заборов из профнастила в Таллинне и Харьюмаа. Оцинкованный профлист, разные цвета, глухой забор для приватности. Практично и доступно. Бесплатный замер.",
 "kicker":"Профнастил · профлист","h1":"Заборы<br><em>из профнастила</em><br>в Таллинне",
 "lead":"Практичное и доступное решение: глухой забор из оцинкованного профлиста. Полная приватность, защита от ветра и пыли, разные цвета покрытия.",
 "intro_h":"Почему профнастил","intro_p":"Профлист — недорогой и быстрый в монтаже материал. Глухой забор закрывает участок от посторонних глаз и служит долго за счёт оцинковки и полимерного покрытия.",
 "bens":["Полная приватность — глухой забор","Оцинкованный лист с полимерным покрытием","Разные цвета (в т.ч. под дерево)","Защита от ветра, пыли и шума","Экономичное и быстрое решение","Столбы и лаги из металла"],
 "variants_h":"Варианты заборов из профнастила",
 "variants":[("▦","Стандартный профлист","Глухой забор из оцинкованного профлиста нужной высоты."),
             ("◧","Цветное покрытие","Полимерное покрытие разных цветов, в том числе под дерево."),
             ("▣","С кирпичными столбами","Комбинация профлиста с кирпичными или блочными столбами."),
             ("⛩","Ворота из профнастила","Откатные и распашные ворота с заполнением профлистом.")],
 "cta_band":"Рассчитаем забор из профнастила",
 "incl":["Выезд на замер участка","Установка металлических столбов и лаг","Монтаж профлиста","Выравнивание по уровню","Проверка конструкции после монтажа"],
 "factors":["Длина и высота забора","Марка и цвет профлиста","Тип столбов (металл, кирпич)","Ворота и калитки","Рельеф и подготовка основания"],
 "gallery":[("luxaed-svc-profnastil","Ворота из профнастила"),("luxaed-metal","Металлический забор с воротами"),("luxaed-profnastil-2","Забор из профнастила (пример типа)")],
 "faq":[("Профнастил не выгорает?","Качественный профлист с полимерным покрытием долго сохраняет цвет. Подбираем проверенные материалы."),
        ("Какая высота забора возможна?","Обычно 1.5–2.0 м и выше — подберём под задачу приватности и ветровую нагрузку."),
        ("Можно комбинировать со столбами из кирпича?","Да, делаем комбинированные заборы: профлист между кирпичными или блочными столбами."),
        ("Профнастил дешевле дерева и 3D-сетки?","Как правило да — это одно из самых доступных решений. Точную цену назовём после замера.")],
},
{
 "path":"/ru/uslugi/vorota-kalitki/","name":"Ворота, калитки и автоматика","hero":"luxaed-svc-gates","og":"/img/luxaed-svc-gates.jpg",
 "title":"Ворота, калитки и автоматика в Таллинне — LuxAed",
 "desc":"Откатные и распашные ворота, калитки, автоматика ворот и домофоны в Таллинне и Харьюмаа. Установка приводов, пультов и домофонов под ключ. Бесплатный замер.",
 "kicker":"Ворота · автоматика · домофоны","h1":"Ворота, калитки<br><em>и автоматика</em><br>в Таллинне",
 "lead":"Откатные и распашные ворота под ключ с автоматикой и домофонами. Изготавливаем, устанавливаем и подключаем — заезжаете во двор одним нажатием кнопки.",
 "intro_h":"Ворота с автоматикой под ключ","intro_p":"Подбираем тип ворот и привод под ваш въезд, ширину и рельеф. Устанавливаем автоматику, пульты, фотоэлементы и домофоны, а также обслуживаем существующие системы.",
 "bens":["Откатные (сдвижные) ворота","Распашные ворота","Автоматика: приводы, пульты, фотоэлементы","Домофоны и вызывные панели","Калитки в едином стиле с забором","Обслуживание и ремонт существующих ворот"],
 "variants_h":"Типы ворот и автоматики",
 "variants":[("⇄","Откатные ворота","Сдвижные ворота без нижней направляющей — удобно, не занимают место при открытии."),
             ("⛩","Распашные ворота","Классические двустворчатые ворота с приводами на каждую створку."),
             ("⚙","Автоматика","Приводы, пульты ДУ, фотоэлементы безопасности, сигнальная лампа."),
             ("🔔","Домофоны","Вызывные панели и домофоны с открытием калитки и ворот.")],
 "cta_band":"Подберём ворота и автоматику под ваш въезд",
 "incl":["Выезд на замер въезда","Изготовление ворот и калитки","Установка и выравнивание конструкции","Монтаж и настройка автоматики","Подключение домофона, проверка работы"],
 "factors":["Тип ворот (откатные / распашные)","Ширина и вес створки","Марка привода автоматики","Домофон и дополнительные опции","Заполнение (дерево, профнастил, 3D-сетка)"],
 "gallery":[("luxaed-svc-gates","Откатные деревянные ворота с автоматикой"),("luxaed-profnastil-gate","Распашные ворота из профнастила"),("luxaed-mesh-gate","Сетчатые ворота"),("luxaed-auto-2","Привод откатных ворот")],
 "faq":[("Откатные или распашные — что выбрать?","Откатные удобны, когда мало места перед въездом. Распашные проще и дешевле. Поможем выбрать на замере."),
        ("Можно поставить автоматику на существующие ворота?","В большинстве случаев да — оценим состояние конструкции и подберём подходящий привод."),
        ("Ставите домофоны?","Да, устанавливаем и подключаем домофоны и вызывные панели с открытием ворот и калитки."),
        ("Что с безопасностью автоматики?","Ставим фотоэлементы и сигнальную лампу, чтобы ворота не закрывались на автомобиль или человека.")],
},
{
 "path":"/ru/uslugi/remont-zaborov/","name":"Ремонт заборов и ворот","hero":"luxaed-g6","og":"/img/luxaed-g6.jpg",
 "title":"Ремонт заборов и ворот в Таллинне — LuxAed",
 "desc":"Ремонт заборов и ворот в Таллинне и Харьюмаа: замена секций и столбов, ремонт откатных и распашных ворот, автоматики и фурнитуры. Диагностика и расчёт. Звоните LuxAed.",
 "kicker":"Ремонт · обслуживание","h1":"Ремонт заборов<br><em>и ворот</em><br>в Таллинне",
 "lead":"Восстанавливаем заборы, ворота и автоматику: замена секций и столбов, регулировка створок, ремонт приводов и фурнитуры. Проведём диагностику и назовём стоимость.",
 "intro_h":"Что ремонтируем","intro_p":"Не обязательно менять весь забор — часто достаточно заменить повреждённые секции или столбы, отрегулировать ворота или восстановить автоматику.",
 "bens":["Замена повреждённых секций забора","Замена и выравнивание столбов","Ремонт откатных и распашных ворот","Ремонт и настройка автоматики","Замена роликов, направляющих, фурнитуры","Диагностика и расчёт до начала работ"],
 "variants_h":"Виды ремонтных работ",
 "variants":[("▤","Секции забора","Замена повреждённых панелей, досок или профлиста."),
             ("▥","Столбы","Замена, выравнивание и укрепление покосившихся столбов."),
             ("⇄","Ворота","Регулировка створок, замена роликов и направляющих."),
             ("⚙","Автоматика","Диагностика и ремонт приводов, пультов, фотоэлементов.")],
 "cta_band":"Проведём диагностику и починим забор",
 "incl":["Выезд и диагностика конструкции","Расчёт стоимости до начала работ","Замена секций, столбов или фурнитуры","Регулировка ворот и автоматики","Проверка работы после ремонта"],
 "factors":["Объём и вид повреждений","Тип забора и ворот","Необходимость замены материалов","Ремонт автоматики","Доступ к участку"],
 "gallery":[("luxaed-g8","Автоматика откатных ворот"),("luxaed-g9","Привод ворот на основании"),("luxaed-auto-2","Ремонт привода ворот"),("luxaed-g6","Столб и привод ворот")],
 "faq":[("Можно отремонтировать, а не менять весь забор?","Часто да — заменяем только повреждённые секции или столбы. На диагностике оценим, что выгоднее."),
        ("Чините автоматику ворот?","Да, диагностируем и ремонтируем приводы, пульты и фотоэлементы, при необходимости заменяем."),
        ("Ремонтируете ворота не своей установки?","Да, работаем и с конструкциями других мастеров — оценим на месте."),
        ("Сколько стоит ремонт?","Зависит от объёма работ. После диагностики называем конкретную стоимость без скрытых доплат.")],
},
]

if __name__=="__main__":
    for c in SERVICES:
        service_page(c)
    print("RU services done:", len(SERVICES))
