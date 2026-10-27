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
    REVIEW_COUNT, SCRIPTS, SVC, TEL, footer, head, image_fallback, nav, reel_strip,
    webp_sources, write,
)
from lead_form import render_lead_form
from service_catalog import SERVICE_MATRIX
from intercom_service import INTERCOM_USE_CASES
from problem_content import HUB_LINKS


PATH_TO_KEY = {
    item[lang]["path"]: item["key"]
    for item in SERVICE_MATRIX for lang in ("et", "ru", "en")
}

USE_CASES = {
    "et": {
        "wood": ("Kas puitaed sobib teie vajadusele?", "Puitaed on hea valik, kui soovite privaatsust ja sooja välimust ning olete valmis pinda perioodiliselt hooldama.", [("Parim", "Eramu tänavapoolne külg, terrassi või hoovi varjamine ja aiaga sobivad väravad."), ("Privaatsus", "Tihe laudis annab kõrge vaatevarje; laudade vahega saab tuult ja avatust reguleerida."), ("Tuul ja müra", "Tihedale puitaiale mõjub suur tuulekoormus. See võib tänavamüra veidi summutada, kuid müratõke see ei ole."), ("Arvestage", "Puit vajab värvi või õli uuendamist ning konstruktsioon peab hoidma lauad maapinnast eemal.")]),
        "roll_mesh": ("Millal valida rullvõrkaed?", "Rullvõrk on kõige praktilisem pika piiri, nõlva ja piiratud eelarve korral, kui privaatsus ei ole peamine eesmärk.", [("Parim", "Pikk perimeeter, suvilad, aiamaa, tagumine piir ja sujuva kaldega krunt."), ("Privaatsus", "Madal. Vaatevarjeks sobib paremini hekk või eraldi kinnine aiaosa."), ("Tuul ja müra", "Väga väike tuulekoormus, kuid võrk ei vähenda müra."), ("Arvestage", "Õige postisamm, nurgapostid ja pingutus määravad, kas võrk püsib sirge.")]),
        "panel_mesh": ("Millal valida 2D/3D-paneelaed?", "Paneelaed sobib, kui vajate vähese hooldusega jäika ja turvalist piiret, kuid mitte vaate- ega müravarjet.", [("Parim", "Eramu, koeraaedik, korteriühistu, ettevõtte territoorium ja väravatega tervik."), ("Privaatsus", "Madal; vajadusel saab mõne lõigu lahendada eraldi kinnise materjaliga."), ("Tuul ja müra", "Laseb tuule läbi ja sobib avatud krundile. Müra vastu ei aita."), ("Arvestage", "Kõrgus, traadi läbimõõt, postid, kinnitused ja alumine vahe valitakse kasutuse järgi.")]),
        "steel_picket": ("Millal valida metall-lippaed?", "Metall-lippaed sobib, kui soovite vähe hooldust, ühtset väravat ja reguleeritavat tasakaalu privaatsuse ning õhulisuse vahel.", [("Parim", "Kaasaegne tänavafront, eramud ning aed ja väravad ühes toonis."), ("Privaatsus", "Keskmisest kõrgeni; sõltub lippide vahest ning ühe- või kahepoolsest paigutusest."), ("Tuul ja müra", "Õhulisem lahendus koormab vähem kui kinnine aed. Müra vastu mõju on väike."), ("Arvestage", "Horisontaalne ja vertikaalne lahendus vajavad erinevat karkassi; profiil ja vahed tuleb ette valida.")]),
        "bar_metal": ("Millal valida varbaed?", "Keevitatud varbaed sobib esinduslikuks, tugevaks ja avatud piiriks, kus privaatsus ei ole peamine.", [("Parim", "Esifassaad, esinduslik eramu, ettevõte ja aiaga sama kujundusega väravad."), ("Privaatsus", "Madal; varbade vahe säilitab vaate ja valguse."), ("Tuul ja müra", "Väike tuulekoormus, kuid müra ja tolmu see ei blokeeri."), ("Arvestage", "Hinda mõjutavad terasprofiil, keevitustöö, detailid, tsinkimine, värv ja väravate disain.")]),
        "profiled_sheet": ("Kas vajate profiilplekki või valmis aeda koos paigaldusega?", "LuxAed teeb valmis profiilplekk-aia koos mõõdistuse, metallkarkassi, postide, paigalduse ja soovi korral samas stiilis väravatega.", [("Parim", "Tänavapoolne piir, hoovi varjamine, ühtne kinnine aed ja sobiva täitega väravad."), ("Privaatsus", "Väga kõrge. Alumisse serva ja väravate ümber jäävad vajalikud tehnilised vahed."), ("Tuul ja müra", "Kinnisele pinnale mõjub suur tuulekoormus. Tajutavat müra võib see mõnevõrra vähendada, kuid müratõke see ei ole."), ("Arvestage", "Postide profiil, samm, alus ja karkass valitakse kõrguse, pinnase ning avatud asukoha järgi.")]),
        "gates": ("Milline automaatvärav sobib teie aiale?", "Valmistame ja paigaldame automaatväravaid terviklahendusena. Liugvärav säästab ruumi sissesõidu ees; tiibvärav on sageli lihtsam, kui tiibade avanemiseks on piisavalt ruumi.", [("Liugvärav", "Sobib kitsale või kaldega sissesõidule, kui aia kõrval on piisav külgruum."), ("Tiibvärav", "Sobib tasasele ja avarale sissesõidule. Tiibade liikumisala tuleb hoida vaba, talvel ka lumest."), ("Automaatika", "Ajam valitakse värava kaalu, laiuse, kasutussageduse ja tuulekoormuse järgi."), ("Ohutus", "Fotoelemendid, õige jõuseadistus, avariivabastus ja regulaarne hooldus on osa toimivast süsteemist.")]),
        "repair": ("Kas remontida või vahetada?", "Remont on mõistlik, kui kandvad postid ja põhikonstruktsioon on terved; ulatusliku korrosiooni, viltuse aluse või korduvate rikete korral võib vahetus olla odavam.", [("Sageli remonditav", "Üksikud sektsioonid, postid, hinged, rullikud, lukk, juhtimine ja fotoelemendid."), ("Vajab ülevaatust", "Viltune liugvärav, pragunenud vundament, läbiv rooste ja mitme posti vajumine."), ("Esmane hinnang", "Saatke üldfoto ja lähivõtted kahjustusest, väravast või automaatika märgisest."), ("Enne tööd", "Diagnoosime põhjuse ja lepime kokku, millised osad säilitada ning millised vahetada.")]),
    },
    "ru": {
        "wood": ("Подойдёт ли вам деревянный забор?", "Дерево подходит, если нужна приватность и тёплый внешний вид и вы готовы периодически обновлять защитное покрытие.", [("Лучше всего", "Фасад частного дома, закрытый двор или терраса и ворота в одном стиле."), ("Приватность", "Плотная доска хорошо закрывает участок; зазор регулирует продуваемость."), ("Ветер и шум", "На плотный забор действует большая ветровая нагрузка. Он может немного снизить воспринимаемый шум, но не является шумовым экраном."), ("Учтите", "Покрытие нужно обновлять, а доски не должны постоянно контактировать с грунтом.")]),
        "roll_mesh": ("Когда выбирать рулонную сетку?", "Сетка практична для длинной границы, склона и ограниченного бюджета, если приватность не является главной задачей.", [("Лучше всего", "Большой периметр, дача, сад, задняя граница и плавный склон."), ("Приватность", "Низкая. Для закрытия участка лучше добавить живую изгородь или сплошной участок."), ("Ветер и шум", "Почти не создаёт ветровой нагрузки, но не снижает шум."), ("Учтите", "Ровность зависит от шага столбов, усиления углов и правильного натяжения.")]),
        "panel_mesh": ("Когда выбирать 2D/3D-панели?", "Панель подходит для жёсткого, безопасного и малообслуживаемого ограждения, когда не требуется защита от взглядов и шума.", [("Лучше всего", "Частный дом, собака, товарищество, предприятие и ворота с тем же заполнением."), ("Приватность", "Низкая; отдельные участки можно закрыть другим материалом."), ("Ветер и шум", "Хорошо продувается и подходит открытому участку. Шум не снижает."), ("Учтите", "Высоту, проволоку, столбы, крепления и нижний зазор выбирают по задаче.")]),
        "steel_picket": ("Когда выбирать металлический штакетник?", "Штакетник даёт мало ухода и позволяет настроить баланс между приватностью и продуваемостью.", [("Лучше всего", "Современный фасад участка и ворота в одном цвете с ограждением."), ("Приватность", "От средней до высокой: зависит от зазора и одно- или двухсторонней раскладки."), ("Ветер и шум", "Открытая раскладка нагружает меньше сплошного забора. Эффект от шума небольшой."), ("Учтите", "Горизонтальная и вертикальная раскладка требуют разного каркаса; профиль и шаг выбирают заранее.")]),
        "bar_metal": ("Когда выбирать прутковый забор?", "Сварные стальные секции подходят для прочной и представительной открытой границы, где приватность не главное.", [("Лучше всего", "Фасад, представительский частный дом, предприятие и ворота с тем же рисунком."), ("Приватность", "Низкая: зазоры сохраняют обзор и свет."), ("Ветер и шум", "Небольшая ветровая нагрузка, но пыль и шум почти не блокирует."), ("Учтите", "На цену влияют профиль, сварка, декор, цинкование, окраска и дизайн ворот.")]),
        "profiled_sheet": ("Нужен профлист или готовый забор с установкой?", "LuxAed делает именно готовый забор из профнастила под ключ: замер, металлический каркас, столбы, монтаж профлиста и, при необходимости, калитка и ворота.", [("Лучше всего", "Сторона улицы, закрытый двор, сплошная линия и ворота с тем же заполнением."), ("Приватность", "Очень высокая; остаются необходимые зазоры у земли и вокруг ворот."), ("Ветер и шум", "Сплошная поверхность сильно нагружается ветром. Может немного снизить воспринимаемый шум, но не является сертифицированным экраном."), ("Учтите", "Профиль столбов, шаг, основание и рама зависят от высоты, грунта и открытости участка.")]),
        "gates": ("Какие автоматические ворота подойдут для вашего забора?", "Изготавливаем и устанавливаем автоматические ворота для забора под ключ. Откатные экономят место перед въездом; распашные часто проще, если для створок достаточно свободного пространства.", [("Откатные", "Для узкого или наклонного въезда при наличии места вдоль забора."), ("Распашные", "Для ровного просторного въезда; зону движения створок нужно очищать от снега."), ("Автоматика", "Привод выбирают по весу, ширине, частоте использования и ветровой нагрузке."), ("Безопасность", "Фотоэлементы, настройка усилия, аварийное открывание и обслуживание обязательны для надёжной системы.")]),
        "repair": ("Ремонтировать или менять?", "Ремонт разумен, если основные столбы и каркас целы; при сквозной коррозии, плохом основании и повторных поломках замена может быть выгоднее.", [("Часто ремонтируется", "Отдельная секция, столб, петли, ролики, замок, блок управления или фотоэлементы."), ("Нужен осмотр", "Перекошенные откатные ворота, треснувший фундамент, сильная коррозия и просадка нескольких столбов."), ("Для оценки", "Пришлите общий план и крупные фото повреждения, ворот или шильдика автоматики."), ("До работы", "Находим причину и согласуем, что сохранить, а что заменить.")]),
    },
    "en": {
        "wood": ("Is a timber fence right for you?", "Choose timber for privacy and a warm appearance if you are prepared to renew its protective finish periodically.", [("Best for", "Residential frontages, screening a yard or terrace, and matching gates."), ("Privacy", "Close boarding gives high screening; board gaps can balance airflow and openness."), ("Wind and noise", "Close boarding takes high wind loads. It may slightly reduce perceived road noise but is not an acoustic barrier."), ("Consider", "Paint or oil needs renewal, and boards should be kept clear of constant ground contact.")]),
        "roll_mesh": ("When should you choose roll mesh?", "Roll mesh is practical for a long boundary, a slope and a limited budget when privacy is not the priority.", [("Best for", "Long perimeters, gardens, rear boundaries and gently sloping plots."), ("Privacy", "Low. Use a hedge or a separate solid section where screening is needed."), ("Wind and noise", "Very low wind loading, but mesh does not reduce noise."), ("Consider", "Post spacing, strengthened corners and correct tension determine whether it stays straight.")]),
        "panel_mesh": ("When should you choose 2D/3D panels?", "Choose welded panels for a rigid, secure, low-maintenance boundary where visual and noise screening are not required.", [("Best for", "Homes, dogs, apartment properties, commercial sites and matching gates."), ("Privacy", "Low; selected areas can use a separate solid material."), ("Wind and noise", "Lets wind through and suits exposed sites. It does not reduce noise."), ("Consider", "Height, wire size, posts, clips and the bottom gap must suit the use case.")]),
        "steel_picket": ("When should you choose steel pickets?", "Steel pickets offer low maintenance and an adjustable balance between privacy and airflow.", [("Best for", "Contemporary frontages and fences with matching gates in one colour."), ("Privacy", "Medium to high depending on spacing and single- or double-sided layout."), ("Wind and noise", "An open layout loads less than a solid fence. Noise reduction is limited."), ("Consider", "Horizontal and vertical layouts need different frames; choose the profile and spacing up front.")]),
        "bar_metal": ("When should you choose a metal-bar fence?", "Welded steel sections suit a strong, architectural open boundary where privacy is not the main goal.", [("Best for", "Frontages, premium homes, commercial sites and matching gates."), ("Privacy", "Low; bar spacing preserves views and daylight."), ("Wind and noise", "Low wind loading, but little screening from dust or noise."), ("Consider", "Steel profile, welding, details, galvanising, coating and gate design affect the price.")]),
        "profiled_sheet": ("Do you need sheet material or a finished installed fence?", "LuxAed provides the complete profiled-sheet fence: site measurement, steel frame, posts, sheet installation and matching pedestrian or vehicle gates where required.", [("Best for", "Street boundaries, screening a yard and gates with matching infill."), ("Privacy", "Very high, with necessary clearances at ground level and around gates."), ("Wind and noise", "A solid surface takes high wind loads. It may slightly reduce perceived noise but is not a certified acoustic screen."), ("Consider", "Post section, spacing, foundations and rails depend on height, ground and site exposure.")]),
        "gates": ("Which automatic gate suits your fence and entrance?", "We manufacture and install complete automatic gate systems. A sliding gate saves space in front of the entrance; a swing gate is often simpler where there is enough room for the leaves.", [("Sliding gate", "Good for a tight or sloping entrance where enough side run-back exists."), ("Swing gate", "Good for a level, open entrance; keep the leaf movement area clear of snow."), ("Automation", "The drive is selected for gate weight, width, usage frequency and wind loading."), ("Safety", "Photocells, force settings, emergency release and maintenance are part of a reliable system.")]),
        "repair": ("Repair or replace?", "Repair is sensible where the main posts and frame remain sound; severe corrosion, failed foundations or repeated faults can make replacement better value.", [("Often repairable", "Individual sections, posts, hinges, rollers, locks, controls and photocells."), ("Needs inspection", "A leaning sliding gate, cracked foundation, deep corrosion or several sinking posts."), ("For an estimate", "Send an overview plus close-ups of the damage, gate or automation label."), ("Before work", "We diagnose the cause and agree what can be retained and what should be replaced.")]),
    },
}

for _lang, _content in INTERCOM_USE_CASES.items():
    USE_CASES[_lang]["intercom"] = _content


# Outcome-led first-screen copy. The detailed service data below the fold still
# explains materials and construction, while the hero answers the homeowner's
# real question in plain language. Keeping this layer beside the shared layout
# also prevents one language from drifting back to catalogue-like copy.
OUTCOME_COPY = {
    "ru": {
        "wood": {
            "hero_prompt": "Хотите закрыть двор и сохранить тёплый вид?",
            "lead": "Закройте двор от улицы, добавьте уюта террасе и оформите ворота в одном стиле с домом. Сделаем деревянный забор на прочном стальном каркасе и подберём нужный просвет между досками.",
            "intro_h": "Деревянный забор для приватного и уютного двора",
            "intro_p": "Плотная доска скрывает участок от взглядов, а более открытая раскладка сохраняет свет и продуваемость. На замере согласуем направление досок, высоту, цвет, уход и ворота, чтобы весь фасад выглядел единым.",
        },
        "roll_mesh": {
            "hero_prompt": "Нужно оградить длинную границу без лишних затрат?",
            "lead": "Рулонная сетка помогает доступно оградить сад, дачу, заднюю границу или большой периметр. Она пропускает свет и ветер, хорошо повторяет плавный уклон и подходит для калиток и ворот.",
            "intro_h": "Практичное ограждение для длинной линии и неровного участка",
            "intro_p": "Подберём рабицу или сварную рулонную сетку, высоту, покрытие и шаг столбов. Усилим углы, аккуратно натянем полотно и продумаем нижний зазор, если во дворе есть собака.",
        },
        "panel_mesh": {
            "hero_prompt": "Нужен прочный забор для дома, собаки или территории?",
            "lead": "Жёсткие 2D- и 3D-панели обозначают границу, не закрывают свет и выдерживают повседневную нагрузку. Подходят частному дому, вольеру, квартирному товариществу и территории предприятия.",
            "intro_h": "Надёжный сетчатый забор без сложного ухода",
            "intro_p": "Выберем 2D- или 3D-секцию по требуемой жёсткости, высоте и размеру ячейки. Установим столбы, при необходимости добавим бетонную цокольную плиту, калитку и ворота с тем же заполнением.",
        },
        "steel_picket": {
            "hero_prompt": "Хотите современный забор без постоянной покраски?",
            "lead": "Металлический штакетник и горизонтальные ламели дают аккуратный фасад, сохраняют свет и позволяют выбрать уровень приватности. Забор, калитку и ворота сделаем в одном цвете.",
            "intro_h": "Настройте внешний вид и приватность под свой участок",
            "intro_p": "Вертикальная раскладка выглядит спокойнее и классичнее, горизонтальная подчёркивает современную архитектуру. Зазор можно оставить более открытым или сделать плотнее, в том числе двухсторонним.",
        },
        "bar_metal": {
            "hero_prompt": "Нужен прочный забор с индивидуальным рисунком?",
            "lead": "Сделаем сварные металлические секции под размеры и архитектуру участка. От строгих вертикальных прутков до декоративного рисунка, с калиткой и воротами в том же стиле.",
            "intro_h": "Представительный металлический забор на долгие годы",
            "intro_p": "Согласуем высоту, шаг элементов, рисунок, цвет и защиту металла. Конструкцию изготовим по размеру, а ворота и калитку сразу заложим в общий ритм ограждения.",
        },
        "profiled_sheet": {
            "name": "Изготовление и установка заборов из профнастила",
            "title": "Установка забора из профнастила под ключ в Таллинне — LuxAed",
            "desc": "Монтаж забора из профнастила под ключ в Таллинне и Харьюмаа: замер, профлист, металлический каркас, столбы, калитка и ворота. Точный расчёт после бесплатного замера.",
            "kicker": "Профнастил · профлист · изготовление и монтаж",
            "h1": "Забор из профнастила<br><em>с установкой под ключ</em>",
            "hero_prompt": "Хотите закрыть двор от посторонних взглядов?",
            "lead": "Не просто продадим профлист, а сделаем готовый забор. Бесплатно измерим участок, подберём материал и цвет, установим столбы и каркас, смонтируем профнастил, калитку и ворота.",
            "intro_h": "Больше приватности без сложного обслуживания",
            "intro_p": "Заказывая установку забора из профнастила, вы получаете весь комплект от замера до готовой линии ограждения. Чтобы большая сплошная поверхность оставалась устойчивой, рассчитываем столбы, шаг, основание и металлические лаги под высоту, грунт и ветер.",
            "cta_band": "Рассчитаем забор из профнастила с материалом и монтажом",
            "local_h": "Изготовление и монтаж заборов из профнастила в Таллинне и Харьюмаа",
            "local_p": "Работаем по Таллинну и Харьюмаа. На бесплатном замере проверяем длину, перепады, грунт, ветровую нагрузку и въезд, после чего рассчитываем профлист, каркас, столбы, крепёж, калитку и ворота.",
            "price_lead": "Готовый забор из профнастила с материалом и стандартным монтажом обычно стоит 70–135 €/м. Точная цена зависит от высоты, профлиста, каркаса, грунта, демонтажа, калитки и ворот и фиксируется после замера.",
            "final_cta": "Рассчитаем забор из профнастила <em>с установкой</em>",
            "final_cta_text": "Оставьте заявку или позвоните.<br>Бесплатно измерим участок и посчитаем материал, каркас, монтаж и ворота.",
        },
        "gates": {
            "name": "Изготовление и установка автоматических ворот",
            "title": "Установка автоматических ворот в Таллинне | LuxAed",
            "desc": "Изготовим и установим автоматические откатные или распашные ворота в Таллинне и Харьюмаа. Монтаж, привод и настройка безопасности. Бесплатный замер.",
            "kicker": "Автоматические ворота · изготовление · установка",
            "h1": "Установка<br><em>автоматических ворот</em>",
            "hero_prompt": "Хотите открывать въезд, не выходя из машины?",
            "lead": "Открывайте въезд с пульта, не выходя из машины. LuxAed изготовит и установит откатные или распашные ворота для вашего забора в Таллинне и Харьюмаа. Подключим привод и фотоэлементы, а при необходимости добавим управление с телефона.",
            "intro_h": "Ворота, которыми удобно пользоваться каждый день",
            "intro_p": "Установка автоматических ворот начинается с замера въезда. Подберём тип ворот под ширину, уклон и свободное место, рассчитаем привод по весу и частоте использования, затем настроим фотоэлементы, аварийную разблокировку и выбранный способ управления.",
            "local_h": "Изготовление и установка автоматических ворот в Таллинне и Харьюмаа",
            "local_p": "Работаем по Таллинну и Харьюмаа. На бесплатном замере проверяем проём, боковое пространство, уклон, электроподготовку и ежедневную нагрузку, после чего рассчитываем ворота, фундамент, привод, управление и устройства безопасности.",
            "price_lead": "Откатные ворота с автоматикой и стандартной установкой обычно стоят 2 100–3 000 €. Автоматика на подходящие существующие ворота стоит 500–1 250 €. Точную цену фиксируем после замера и проверки конструкции.",
            "final_cta": "Рассчитаем автоматические ворота <em>с установкой</em>",
            "final_cta_text": "Оставьте заявку или позвоните.<br>Бесплатно измерим въезд и посчитаем ворота, привод, монтаж и управление.",
        },
        "repair": {
            "hero_prompt": "Забор перекосился или ворота перестали закрываться?",
            "lead": "Вернём забору ровную линию, воротам лёгкий ход, а автоматике нормальную работу. Заменим только повреждённые детали, если всю конструкцию менять не нужно.",
            "intro_h": "Сначала найдём причину, потом предложим ремонт",
            "intro_p": "Просевший столб, сломанная секция, перекошенная створка или неисправный привод могут выглядеть похоже, но требуют разного ремонта. Пришлите фотографии, и мы подскажем, что можно восстановить и когда выгоднее замена.",
        },
    },
    "et": {
        "wood": {
            "hero_prompt": "Soovite privaatsemat hoovi ja sooja ilmet?",
            "lead": "Varjake hoovi tänava eest, looge terrassile rohkem privaatsust ja sobitage väravad maja stiiliga. Ehitame puitaia tugevale teraskarkassile ning valime sobiva laudade vahe.",
            "intro_h": "Puitaed privaatse ja hubase hoovi jaoks",
            "intro_p": "Tihe laudis varjab vaadet, õhulisem paigutus jätab rohkem valgust ja laseb tuulel liikuda. Mõõdistusel lepime kokku suuna, kõrguse, tooni, hoolduse ja väravate lahenduse.",
        },
        "roll_mesh": {
            "hero_prompt": "Vaja piirata pikk krundipiir mõistliku eelarvega?",
            "lead": "Rullvõrk on praktiline valik aiale, suvilale, tagumisele piirile ja suurele perimeetrile. See laseb läbi valguse ja tuule, järgib laugjat nõlva ning sobib koos jalg- ja sõiduväravaga.",
            "intro_h": "Praktiline piire pikale joonele ja ebatasasele krundile",
            "intro_p": "Valime punutud või keevitatud rullvõrgu, kõrguse, pinnakatte ja postide sammu. Tugevdame nurgad, pingutame võrgu ning arvestame alumise vahega, kui hoovis on koer.",
        },
        "panel_mesh": {
            "hero_prompt": "Vaja tugevat 3D paneelaeda kodu, koera või territooriumi ümber?",
            "lead": "3D paneelaed on jäik keevisvõrgust aiapaneel: see tähistab piiri, jätab valguse alles ja talub igapäevast koormust. Paigaldame 2D- ja 3D-paneelaedu Tallinnas ja Harjumaal: eramule, koeraaedikule, korteriühistule ja ettevõtte territooriumile.",
            "intro_h": "Tugev 3D paneelaed, mis ei vaja keerukat hooldust",
            "intro_p": "Valime 2D- või 3D-paneeli vajaliku jäikuse, kõrguse ja silma järgi. Paigaldame postid ning lisame vajaduse korral aluslaua, jalgvärava ja sama täitega sõiduvärava.",
        },
        "steel_picket": {
            "hero_prompt": "Soovite moodsat aeda ilma pideva värvimiseta?",
            "lead": "Vertikaalsed või horisontaalsed metall-lipid annavad korrastatud fassaadi, jätavad valgust ning võimaldavad valida privaatsuse taseme. Aia ja väravad teeme ühes toonis.",
            "intro_h": "Valige oma krundile sobiv ilme ja privaatsus",
            "intro_p": "Vertikaalne paigutus mõjub rahulikumalt ja klassikalisemalt, horisontaalne rõhutab moodsat arhitektuuri. Vahed võivad jääda õhulisemad või olla tihedamad, sealhulgas kahepoolse lahendusena.",
        },
        "bar_metal": {
            "hero_prompt": "Vaja tugevat aeda omanäolise kujundusega?",
            "lead": "Valmistame keevitatud metallsektsioonid krundi mõõtude ja arhitektuuri järgi. Sirgetest vertikaalvarbadest dekoratiivse kujunduseni, koos samas stiilis jalg- ja sõiduväravaga.",
            "intro_h": "Esinduslik metallaed aastateks",
            "intro_p": "Lepime kokku kõrguse, elementide sammu, kujunduse, värvi ja pinnakaitse. Valmistame sektsioonid mõõdu järgi ning kavandame jalg- ja sõiduväravad kohe aia üldise rütmi sisse.",
        },
        "profiled_sheet": {
            "name": "Profiilplekk-aia valmistamine ja paigaldus",
            "title": "Profiilplekk-aia paigaldus võtmed kätte Tallinnas — LuxAed",
            "desc": "Profiilplekk-aia valmistamine ja paigaldus Tallinnas ja Harjumaal: mõõdistus, metallkarkass, postid, profiilplekk, jalgvärav ja sõiduvärav.",
            "kicker": "Profiilplekk · aia valmistamine ja paigaldus",
            "h1": "Profiilplekk-aed<br><em>koos paigaldusega</em>",
            "hero_prompt": "Soovite hoovi võõraste pilkude eest varjata?",
            "lead": "Te ei saa ainult plekki, vaid valmis aia. Mõõdame krundi, valime materjali ja tooni, paigaldame postid ning karkassi ja teeme soovi korral ka jalg- ja sõiduvärava.",
            "intro_h": "Rohkem privaatsust vähese hooldusega",
            "intro_p": "Profiilplekk-aia paigaldus sisaldab terviklahendust mõõdistusest valmis piirdesse. Et suur kinnine pind püsiks stabiilne, valime postid, sammu, alused ja metallroovid kõrguse, pinnase ning tuule järgi.",
            "cta_band": "Arvutame profiilplekk-aia hinna koos materjali ja paigaldusega",
            "local_h": "Profiilplekk-aia valmistamine ja paigaldus Tallinnas ning Harjumaal",
            "local_p": "Töötame Tallinnas ja Harjumaal. Tasuta mõõdistusel kontrollime aiajoont, kõrgusi, pinnast, tuulekoormust ja sissesõitu ning arvutame profiilpleki, karkassi, postid, kinnitused ja väravad.",
            "price_lead": "Valmis profiilplekk-aed maksab koos materjali ja tavapaigaldusega tavaliselt 70–135 €/jm. Täpne hind sõltub kõrgusest, plekist, karkassist, pinnasest, lammutusest ja väravatest ning selgub pärast mõõdistust.",
            "final_cta": "Arvutame profiilplekk-aia hinna <em>koos paigaldusega</em>",
            "final_cta_text": "Jätke päring või helistage.<br>Mõõdame tasuta ja arvutame materjali, karkassi, paigalduse ning väravate hinna.",
        },
        "gates": {
            "name": "Automaatväravate valmistamine ja paigaldus",
            "title": "Automaatväravate ja aiaväravate paigaldus Tallinnas — LuxAed",
            "desc": "Automaatväravate ja aiaväravate valmistamine ja paigaldus Tallinnas ning Harjumaal: liug- ja tiibväravad, jalgväravad, ajam, fotoelemendid ja juhtimine. Tasuta mõõdistus.",
            "kicker": "Automaatväravad · valmistamine · paigaldus",
            "h1": "Automaatväravate<br><em>paigaldus</em>",
            "hero_prompt": "Soovite avada värava autost väljumata?",
            "lead": "Avage värav puldist, autost väljumata. LuxAed valmistab ja paigaldab liug- ning tiibväravaid Tallinnas ja Harjumaal. Ühendame ajami ja fotoelemendid ning lisame vajadusel telefonist juhtimise.",
            "intro_h": "Väravad, mida on mugav iga päev kasutada",
            "intro_p": "Automaatvärava paigaldus algab sissesõidu mõõdistusest. Valime väravatüübi laiuse, kalde ja vaba ruumi järgi, sobitame ajami värava kaalu ning kasutussagedusega ja seadistame ohutuse, avariivabastuse ning juhtimise.",
            "local_h": "Automaatväravate valmistamine ja paigaldus Tallinnas ning Harjumaal",
            "local_p": "Töötame Tallinnas ja Harjumaal. Tasuta mõõdistusel kontrollime ava, külgruumi, kallet, elektrivalmidust ja kasutuskoormust ning arvutame värava, vundamendi, ajami, juhtimise ja turvaseadmed.",
            "price_lead": "Automaatikaga liugvärav maksab koos tavapaigaldusega tavaliselt 2 100–3 000 €. Sobivale olemasolevale väravale maksab automaatika 500–1 250 €. Täpne hind selgub pärast mõõdistust ja konstruktsiooni kontrolli.",
            "final_cta": "Arvutame automaatvärava hinna <em>koos paigaldusega</em>",
            "final_cta_text": "Jätke päring või helistage.<br>Mõõdame tasuta ja arvutame värava, ajami, paigalduse ning juhtimise hinna.",
        },
        "repair": {
            "hero_prompt": "Aed on viltu või värav ei sulgu enam korralikult?",
            "lead": "Taastame aia sirge joone, värava sujuva liikumise ja automaatika töö. Kui kogu konstruktsiooni pole vaja vahetada, parandame ainult kahjustatud osad.",
            "intro_h": "Kõigepealt leiame põhjuse, siis pakume remondi",
            "intro_p": "Vajunud post, katkine sektsioon, viltune väravaleht ja rikkis ajam võivad tunduda sarnased, kuid vajavad erinevat lahendust. Saatke fotod ning ütleme, mida saab taastada ja millal on vahetus mõistlikum.",
        },
    },
    "en": {
        "wood": {
            "hero_prompt": "Want more privacy without losing a warm, natural look?",
            "lead": "Screen the garden from the street, make the terrace more private and match the gates to the house. We build timber fencing on a strong steel frame with board spacing chosen for your needs.",
            "intro_h": "A timber fence for a private, welcoming garden",
            "intro_p": "Close boarding screens the property, while a more open layout keeps daylight and airflow. During measurement we agree the board direction, height, colour, maintenance and matching gate design.",
        },
        "roll_mesh": {
            "hero_prompt": "Need to fence a long boundary on a sensible budget?",
            "lead": "Roll mesh is a practical way to enclose a garden, summer home, rear boundary or large perimeter. It lets light and wind through, follows a gentle slope and works with pedestrian and vehicle gates.",
            "intro_h": "A practical fence for long lines and uneven ground",
            "intro_p": "We select chain-link or welded roll mesh, height, coating and post spacing. Corners are strengthened, the mesh is tensioned correctly and the bottom gap is planned if a dog uses the garden.",
        },
        "panel_mesh": {
            "hero_prompt": "Need a strong fence for a home, dog or site?",
            "lead": "Rigid 2D and 3D panels define the boundary, preserve daylight and handle everyday use. They suit private homes, dog enclosures, apartment properties and commercial sites.",
            "intro_h": "A strong mesh fence with little maintenance",
            "intro_p": "We choose a 2D or 3D panel for the required rigidity, height and mesh size. We install the posts and can add a base board, pedestrian gate and vehicle gate with matching infill.",
        },
        "steel_picket": {
            "hero_prompt": "Want a contemporary fence without regular repainting?",
            "lead": "Steel pickets and horizontal metal slats give the frontage a clean look, retain daylight and let you choose the level of privacy. Fence, pedestrian gate and vehicle gate can all share one colour.",
            "intro_h": "Set the appearance and privacy to suit your property",
            "intro_p": "A vertical layout feels calm and traditional, while horizontal slats emphasise modern architecture. Spacing can be open or tighter, including a double-sided arrangement for more screening.",
        },
        "bar_metal": {
            "hero_prompt": "Need a strong fence with a design of its own?",
            "lead": "We make welded metal sections to suit the property's dimensions and architecture. Choose simple vertical bars or a decorative pattern, with pedestrian and vehicle gates in the same design.",
            "intro_h": "An architectural metal fence made to last",
            "intro_p": "We agree the height, element spacing, pattern, colour and metal protection. Sections are made to measure and the gates are designed as part of the same visual rhythm.",
        },
        "profiled_sheet": {
            "name": "Profiled-sheet fence supply and installation",
            "title": "Corrugated & Profiled-Sheet Fences in Tallinn | LuxAed",
            "desc": "Complete corrugated or profiled-sheet fence installation in Tallinn and Harju County: measurement, steel frame, posts, coated sheets and matching gates.",
            "kicker": "Profiled sheet · fence supply and installation",
            "h1": "Profiled-sheet fence<br><em>supplied and installed</em>",
            "hero_prompt": "Want to screen the garden from unwanted views?",
            "lead": "We provide the finished fence, not just the sheets. We measure the property, select the material and colour, install the posts and frame, and add matching pedestrian and vehicle gates if required.",
            "intro_h": "More privacy with straightforward maintenance",
            "intro_p": "Profiled-sheet fence installation covers the whole job from measurement to a finished boundary. Because a large solid surface takes higher loads, we specify posts, spacing, foundations and steel rails for the height, ground and wind exposure.",
            "cta_band": "Price a profiled-sheet fence with material and installation",
            "local_h": "Profiled-sheet fence supply and installation in Tallinn and Harjumaa",
            "local_p": "We work throughout Tallinn and Harjumaa. The free measurement covers boundary length, levels, ground, wind exposure and the entrance before we price the sheets, frame, posts, fixings and gates.",
            "price_lead": "A profiled-sheet fence with materials and standard installation usually costs €70–135/m. Height, sheet specification, frame, ground, removal and gates determine the final written quotation.",
            "final_cta": "Price your profiled-sheet fence <em>with installation</em>",
            "final_cta_text": "Send an enquiry or call us.<br>We measure free of charge and price the material, frame, installation and gates.",
        },
        "gates": {
            "name": "Automatic gate manufacture and installation",
            "title": "Automatic Gate Installation in Tallinn — LuxAed",
            "desc": "Automatic sliding and swing gates installed in Tallinn and Harju County: manufacture, drive, photocells and controls. Free site measurement and quote.",
            "kicker": "Automatic gates · manufacture · installation",
            "h1": "Automatic gate<br><em>installation</em>",
            "hero_prompt": "Want to open the entrance without leaving the car?",
            "lead": "Open the entrance by remote without leaving your car. LuxAed builds and installs sliding and swing gates in Tallinn and Harju County. We fit the drive and photocells, with optional phone controls to suit your system.",
            "intro_h": "Gates that are easy to use every day",
            "intro_p": "Automatic gate installation starts with measuring the entrance. We choose the gate type for its width, slope and available space, size the drive for gate weight and usage, then configure safety, emergency release and your preferred controls.",
            "local_h": "Automatic gate manufacture and installation across Tallinn and Harju County",
            "local_p": "During the free survey we check the opening, side run-back, slope, electrical preparation and usage, then price the gate, foundation, drive, controls and safety devices.",
            "price_lead": "An installed sliding gate with automation usually costs €2,100–3,000. Automation fitted to a suitable existing gate costs €500–1,250. We confirm the exact price after measurement and a structural check.",
            "final_cta": "Price your automatic gate <em>with installation</em>",
            "final_cta_text": "Send an enquiry or call us.<br>We measure free of charge and price the gate, drive, installation and controls.",
        },
        "repair": {
            "hero_prompt": "Has the fence moved or has the gate stopped closing?",
            "lead": "We restore a straight fence line, smooth gate movement and reliable automation. Where the whole structure does not need replacement, we repair only the damaged parts.",
            "intro_h": "We find the cause before recommending the repair",
            "intro_p": "A sinking post, damaged section, misaligned gate leaf and faulty drive can look similar but need different fixes. Send photographs and we will explain what can be repaired and when replacement offers better value.",
        },
    },
}


EXTRA_FAQ = {
    "ru": {
        "wood": [
            ("Подойдёт ли деревянный забор для семьи с детьми или собакой?", "Да. Высоту, просвет между досками, нижний зазор и замок калитки выбираем так, чтобы ограждение подходило вашему двору и питомцу."),
            ("Можно поставить деревянный забор на участке с уклоном?", "Да. На плавном рельефе линию ведём по уклону, а при заметных перепадах делим забор на аккуратные ступени. Способ выбираем после замера."),
        ],
        "roll_mesh": [
            ("Подходит ли сетка-рабица для собаки?", "Подходит, если правильно выбрать высоту, размер ячейки, натяжение и нижний зазор. Для сильной или активной собаки иногда разумнее жёсткая 2D/3D-панель."),
            ("Можно сделать часть сетчатого забора закрытой от взглядов?", "Да. Со стороны улицы можно использовать дерево, профнастил или плотный металлический штакетник, а длинные боковые и задние границы оставить сетчатыми."),
        ],
        "panel_mesh": [
            ("Как подобрать 2D/3D-забор для собаки и детей?", "Смотрим на высоту, размер ячейки, диаметр проволоки, нижний зазор, ворота и замок. Для вольера и внешней границы могут потребоваться разные секции."),
            ("Можно добавить приватность только со стороны улицы?", "Да. Сетчатую границу можно комбинировать со сплошным участком из дерева, профлиста или металлического штакетника там, где нужен экран от взглядов."),
        ],
        "steel_picket": [
            ("Подходит ли металлический штакетник для участка с собакой?", "Да, если выбрать подходящий зазор между ламелями, расстояние от земли, высоту и надёжную калитку. Эти параметры согласуем до изготовления."),
            ("Сколько стоит металлический штакетник с установкой?", "Обычно 85–155 €/м с материалом и стандартным монтажом. На цену влияют высота, направление и шаг ламелей, одно- или двусторонняя раскладка, цвет RAL и ворота."),
        ],
        "bar_metal": [
            ("Можно сделать прутковый забор безопасным для детей и животных?", "Да. Подбираем высоту, шаг вертикальных элементов, нижний зазор и замок калитки. Горизонтальные детали, по которым легко забраться, обсуждаем отдельно."),
            ("Подходит ли сварной металлический забор для предприятия?", "Да. Он сохраняет обзор территории, выглядит представительно и может сочетаться с автоматическими воротами, калиткой, домофоном и контролем доступа."),
        ],
        "profiled_sheet": [
            ("Что входит в установку забора из профнастила под ключ?", "Осматриваем и измеряем участок, рассчитываем конструкцию, устанавливаем столбы и металлические лаги, монтируем профлист и отделочные планки, затем проверяем готовый забор. Калитка, ворота, автоматика и демонтаж включаются в расчёт по задаче."),
            ("Сколько стоит забор из профнастила с установкой?", "С материалом и стандартным монтажом забор из профнастила обычно стоит 70–135 €/м. Высота, толщина и покрытие профлиста, каркас, грунт, демонтаж, калитка и ворота меняют итоговую цену."),
            ("Профнастил полностью защищает от ветра и шума?", "Он закрывает прямой поток воздуха и может немного уменьшить воспринимаемый шум, но не является сертифицированной шумозащитой. Сплошную конструкцию обязательно рассчитываем по ветровой нагрузке."),
            ("Можно комбинировать профнастил с другим забором?", "Да. Закрытый участок ставят со стороны улицы или соседей, а боковые и задние границы делают из сетки, ламелей или прутковых секций."),
        ],
        "gates": [
            ("Сколько стоят автоматические ворота с установкой?", "Откатные ворота с автоматикой и стандартным монтажом обычно стоят 2 100–3 000 €, распашные 1 400–2 300 €, и к ним может добавиться автоматика. Автоматика на подходящие существующие ворота стоит 500–1 250 €."),
            ("Что входит в установку автоматических ворот под ключ?", "Замеряем въезд, изготавливаем ворота, готовим основание, устанавливаем и выравниваем конструкцию, подключаем привод, фотоэлементы и управление, затем проверяем безопасность и аварийное открывание."),
            ("Можно дать отдельный доступ семье, гостям или курьеру?", "Да. В зависимости от системы используют отдельные пульты, приложение, временный код, RFID-метку или домофон. Возможности уточняем по выбранному оборудованию."),
            ("Можно связать ворота, калитку и домофон в одну систему?", "Да. Планируем автоматику ворот, электрозамок калитки, домофон и способы управления как единый комплект, чтобы ими было удобно пользоваться."),
        ],
        "repair": [
            ("Что прислать для предварительной оценки ремонта?", "Нужны общий вид, крупные фотографии повреждения, место крепления и шильдик автоматики, если проблема с приводом. Добавьте адрес и коротко опишите, что изменилось."),
            ("Чините последствия ветра, удара или просадки грунта?", "Да. Сначала проверяем, что стало причиной деформации, затем согласуем замену секций, столбов, фундамента, фурнитуры или настройку ворот."),
        ],
    },
    "et": {
        "wood": [("Kas puitaed sobib laste või koeraga perele?", "Jah. Valime kõrguse, laudade vahe, alumise vahe ja jalgvärava luku vastavalt hoovile ning lemmikloomale."), ("Kas puitaeda saab paigaldada kaldega krundile?", "Jah. Laugel reljeefil järgib aed kallet, suuremate kõrguste vahede korral paigaldame sektsioonid astmeliselt. Lahendus selgub mõõdistusel.")],
        "roll_mesh": [("Kas rullvõrkaed sobib koerale?", "Sobib, kui kõrgus, silm, pingutus ja alumine vahe on õigesti valitud. Tugeva või väga aktiivse koera puhul võib jäik 2D/3D-paneel olla parem."), ("Kas osa võrkaeda saab pilkude eest sulgeda?", "Jah. Tänava poole võib kasutada puitu, profiilplekki või tihedat metall-lippaeda ning pikad külg- ja tagapiirid jätta võrkaiana.")],
        "panel_mesh": [("Kuidas valida 2D/3D-aed koerale ja lastele?", "Arvestame kõrguse, silma suuruse, traadi, alumise vahe, väravate ja lukuga. Koeraaedik ja krundi välispiir võivad vajada erinevat paneeli."), ("Kas privaatsust saab lisada ainult tänava poole?", "Jah. Võrkaeda saab vajalikes lõikudes kombineerida kinnise puit-, profiilplekk- või lippaiaga.")],
        "steel_picket": [("Kas metall-lippaed sobib koeraga krundile?", "Jah, kui lippide vahe, kaugus maast, kõrgus ja jalgvärava lukk on õigesti valitud. Lepime need enne valmistamist kokku."), ("Kui palju maksab metall-lippaed koos paigaldusega?", "Tavaliselt 85–155 €/jm koos materjali ja tavapaigaldusega. Hinda mõjutavad kõrgus, lippide suund ja vahe, ühe- või kahepoolne paigutus, RAL-toon ja väravad.")],
        "bar_metal": [("Kas varbaed on lastele ja loomadele ohutu?", "Jah. Valime kõrguse, püstiste elementide vahe, alumise vahe ja jalgvärava luku. Ronimist lihtsustavad horisontaaldetailid arutame eraldi."), ("Kas keevitatud metallaed sobib ettevõttele?", "Jah. See säilitab territooriumi nähtavuse ning sobib automaatvärava, jalgvärava, domofoni ja läbipääsusüsteemiga.")],
        "profiled_sheet": [("Mida sisaldab profiilplekk-aia paigaldus võtmed kätte?", "Mõõdame objekti, arvutame konstruktsiooni, paigaldame postid ja metallroovid, kinnitame profiilpleki ning viimistlusliistud ja kontrollime valmis aeda. Jalgvärav, sõiduvärav, automaatika ja lammutus lisatakse pakkumisse vastavalt vajadusele."), ("Kui palju maksab profiilplekk-aed koos paigaldusega?", "Koos materjali ja tavapaigaldusega maksab profiilplekk-aed tavaliselt 70–135 €/jm. Lõpphinda mõjutavad kõrgus, pleki paksus ja kate, karkass, pinnas, lammutus ning väravad."), ("Kas profiilpleki saab paigaldada olemasolevatele postidele või karkassile?", "Mõnikord saab. Kontrollime esmalt tugevust, geomeetriat, postide sammu, keevisliiteid ja konstruktsiooni sobivust tuulekoormusele."), ("Kas profiilplekki saab teiste aedadega kombineerida?", "Jah. Tänava või naabri poole võib teha kinnise lõigu ning külg- ja tagapiirile kasutada võrku, metall-lippe või varbaeda.")],
        "gates": [("Kui palju maksavad automaatväravad koos paigaldusega?", "Automaatikaga liugvärav maksab koos tavapaigaldusega tavaliselt 2 100–3 000 € ja tiibvärav 1 400–2 300 €, millele automaatika võib lisanduda. Sobivale olemasolevale väravale maksab automaatika 500–1 250 €."), ("Mida sisaldab automaatvärava paigaldus võtmed kätte?", "Mõõdame sissesõidu, valmistame värava, rajame vajaliku aluse, paigaldame ja joondame konstruktsiooni, ühendame ajami, fotoelemendid ning juhtimise ja kontrollime ohutust ning avariivabastust."), ("Kas perele, külalisele või kullerile saab anda eraldi ligipääsu?", "Jah. Sõltuvalt süsteemist saab kasutada eraldi pulte, rakendust, ajutist koodi, RFID-võtit või domofoni."), ("Kas värav, jalgvärav ja domofon saavad töötada ühe süsteemina?", "Jah. Kavandame väravaautomaatika, jalgvärava elektriluku, domofoni ja juhtimise ühe tervikuna.")],
        "repair": [("Mida saata remondi esmaseks hindamiseks?", "Saatke üldvaade, lähifotod kahjustusest, kinnituskoht ja automaatika andmesilt, kui probleem on ajamiga. Lisage aadress ning lühike kirjeldus."), ("Kas parandate tuule, löögi või pinnase vajumise kahjustusi?", "Jah. Leiame esmalt deformatsiooni põhjuse ning lepime kokku sektsioonide, postide, aluse, furnituuri või värava seadistuse remondi.")],
    },
    "en": {
        "wood": [("Is timber fencing suitable for a family with children or a dog?", "Yes. We select height, board spacing, bottom clearance and the pedestrian-gate lock for the garden and the pet."), ("Can a timber fence be installed on sloping ground?", "Yes. A gentle line can follow the slope, while larger level changes are handled in neat steps. The method is agreed after measurement.")],
        "roll_mesh": [("Is chain-link suitable for a dog?", "It can be when height, mesh size, tension and bottom clearance are correctly selected. A rigid 2D/3D panel may be better for a strong or very active dog."), ("Can only part of a mesh fence be screened for privacy?", "Yes. Timber, profiled sheet or close steel pickets can screen the street frontage while long side and rear boundaries remain mesh.")],
        "panel_mesh": [("How do I choose 2D/3D fencing for dogs and children?", "We consider height, mesh size, wire, bottom clearance, gates and locks. A dog enclosure and the outer boundary may need different panels."), ("Can I add privacy only on the street side?", "Yes. Mesh boundaries can be combined with solid timber, profiled sheet or metal slats only where screening is needed.")],
        "steel_picket": [("Is steel-picket fencing suitable for a property with a dog?", "Yes, when picket spacing, ground clearance, height and the pedestrian-gate lock are selected correctly."), ("How much does a steel picket fence cost with installation?", "A steel picket fence usually costs €85–155/m with materials and standard installation. Height, picket direction and spacing, single- or double-sided layout, RAL colour and gates affect the price.")],
        "bar_metal": [("Can a metal-bar fence be safe for children and pets?", "Yes. We select height, vertical-bar spacing, ground clearance and the pedestrian-gate lock, and discuss any horizontal elements that could be climbed."), ("Does welded metal fencing suit commercial sites?", "Yes. It preserves visibility and can integrate automated gates, pedestrian access, an intercom and access control.")],
        "profiled_sheet": [("What is included in a complete profiled-sheet fence installation?", "We measure the site, specify the structure, install posts and steel rails, fix the sheets and finishing trims, and check the completed fence. Pedestrian gates, vehicle gates, automation and removal are added to the quotation where required."), ("How much does an installed profiled-sheet fence cost?", "With materials and standard installation, a profiled-sheet fence usually costs €70–135/m. Height, sheet thickness and coating, frame, ground, removal and gates affect the final price."), ("Can profiled sheet be fitted to existing posts or a frame?", "Sometimes. We first check strength, alignment, post spacing, welds and whether the structure is suitable for the site's wind loading."), ("Does profiled sheet completely block wind and noise?", "It blocks direct airflow and may slightly reduce perceived noise, but it is not a certified acoustic barrier. A solid fence must be sized for wind loading."), ("Can profiled sheet be combined with another fence?", "Yes. Use solid sections towards the street or neighbour and mesh, pickets or metal bars on side and rear boundaries.")],
        "gates": [("How much do installed automatic gates cost?", "A sliding gate with automation usually costs €2,100–3,000 with standard installation, and a swing gate €1,400–2,300, to which automation can be added. Automation for a suitable existing gate costs €500–1,250."), ("What is included in turnkey automatic gate installation?", "We measure the entrance, manufacture the gate, prepare the required base, install and align the structure, connect the drive, photocells and controls, then test safety and emergency release."), ("Can family members, guests or couriers have separate access?", "Yes. Depending on the system, access can use separate remotes, an app, a temporary code, an RFID token or an intercom."), ("Can the vehicle gate, pedestrian gate and intercom work as one system?", "Yes. We plan gate automation, the pedestrian-gate electric lock, intercom and controls as one convenient setup.")],
        "repair": [("What should I send for an initial repair estimate?", "Send an overview, close-ups of the damage, the fixing point and the automation label if the drive is involved. Add the address and a short description."), ("Do you repair damage caused by wind, impact or ground movement?", "Yes. We first identify the cause and then agree repairs to sections, posts, foundations, hardware or gate settings.")],
    },
}


UI = {
    "et": {
        "home": "Avaleht", "services": "Teenused", "services_anchor": "/#teenused",
        "prompt": "Hei! Vajate uut aeda?", "trust": "arvustust Facebookis", "trust_verb": "soovitab",
        "recommend": "soovitab Facebookis", "reviews": "arvustust", "experience": "aastat kogemust",
        "quote": "Küsi pakkumist", "call": "Helista", "close": "Sulge",
        "get_tag": "Mida saate", "options": "Valikud", "local": "Tallinn ja Harjumaa",
        "price_tag": "Ausalt hinnast", "price_h": "Millest sõltub hind",
        "price_p": "Orienteeruvad hinnad leiate hinnalehelt. Täpse hinna ütleme pärast tasuta mõõdistust.",
        "included": "Alati hinna sees", "affects": "Mõjutab hinda",
        "year_round": "Töötame aastaringselt, kui ilm ja pinnas lubavad", "warranty": "24-kuuline garantii tehtud töödele",
        "process_tag": "Kuidas töötame", "process_h": "Neli lihtsat sammu",
        "gallery": "Galerii", "gallery_h": "Tehtud tööde näited", "more_photos": "Vaata rohkem fotosid Facebookis →",
        "video": "Videod", "video_h": "Vaata paigaldust ja valmis lahendusi",
        "faq": "KKK", "faq_h": "Korduma kippuvad küsimused",
        "other": "Teised teenused", "other_h": "Vaata ka", "more": "Loe lähemalt →",
        "default_final": "Leiame teie krundile <em>sobiva lahenduse</em>",
        "default_final_text": "Jätke päring või helistage.<br>Tuleme tasuta mõõdistusele ja ütleme täpse hinna.",
        "process": [
            ("Jätke päring", "Üks kõne või sõnum ja võtame kogu töö enda peale. Tuleme tasuta mõõdistusele teile sobival ajal."),
            ("Leiame sobiva lahenduse", "Pakume materjali ja lahenduse teie krundi ja eelarve järgi ning ütleme täpse hinna."),
            ("Paigaldame korralikult", "Paigaldame aia või värava ning seadistame vajaduse korral automaatika. Hoiame teid kursis."),
            ("Anname töö üle", "Vaatame tulemuse koos teiega üle ja anname valmis objekti üle koos hooldussoovitustega."),
        ],
    },
    "ru": {
        "home": "Главная", "services": "Услуги", "services_anchor": "/ru/#uslugi",
        "prompt": "Привет! Нужен новый забор?", "trust": "отзыва в Facebook", "trust_verb": "рекомендуют",
        "recommend": "рекомендуют в Facebook", "reviews": "отзыва", "experience": "лет опыта",
        "quote": "Оставить заявку", "call": "Позвонить", "close": "Закрыть",
        "get_tag": "Что вы получаете", "options": "Варианты", "local": "Таллинн и Харьюмаа",
        "price_tag": "Честно о цене", "price_h": "От чего зависит стоимость",
        "price_p": "Ориентировочные цены есть на странице цен. Точную стоимость называем после бесплатного замера.",
        "included": "Всегда входит в процесс", "affects": "Влияет на стоимость",
        "year_round": "Работаем круглый год, если позволяют погода и грунт", "warranty": "Гарантия 24 месяца на выполненные работы",
        "process_tag": "Как мы работаем", "process_h": "Четыре шага до готового результата",
        "gallery": "Галерея", "gallery_h": "Примеры выполненных работ", "more_photos": "Больше фото в нашем Facebook →",
        "video": "Видео", "video_h": "Посмотрите монтаж и готовые решения",
        "faq": "Вопросы", "faq_h": "Частые вопросы",
        "other": "Другие услуги", "other_h": "Смотрите также", "more": "Подробнее об услуге →",
        "default_final": "Рассчитаем <em>подходящее решение</em> для вашего участка",
        "default_final_text": "Оставьте заявку или позвоните.<br>Приедем на бесплатный замер и подготовим точный расчёт.",
        "process": [
            ("Вы оставляете заявку", "Один звонок или сообщение, и мы берём организацию работ на себя. Приедем на бесплатный замер."),
            ("Подбираем и считаем", "Предложим материал и конструкцию под участок и бюджет и заранее назовём стоимость."),
            ("Аккуратно устанавливаем", "Установим забор или ворота и при необходимости подключим автоматику. Будем держать вас в курсе."),
            ("Сдаём готовый объект", "Вместе проверим результат и передадим готовую конструкцию с рекомендациями по эксплуатации."),
        ],
    },
    "en": {
        "home": "Home", "services": "Services", "services_anchor": "/en/#teenused",
        "prompt": "Hey! Need a new fence?", "trust": "Facebook reviews", "trust_verb": "recommend",
        "recommend": "recommend on Facebook", "reviews": "reviews", "experience": "years of experience",
        "quote": "Get a quote", "call": "Call", "close": "Close",
        "get_tag": "What you get", "options": "Options", "local": "Tallinn and Harjumaa",
        "price_tag": "Clear pricing", "price_h": "What affects the price",
        "price_p": "Typical price ranges are in our price guide. We give an exact quote after the free site measurement.",
        "included": "Always included", "affects": "Affects the price",
        "year_round": "Year-round installation when weather and ground allow", "warranty": "24-month warranty on completed work",
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


PRICE_FROM = {
    "wood": {"et": ("Puitaed alates <b>90 €/jm</b> koos paigaldusega", "Puitaed maksab koos materjali ja tavapaigaldusega tavaliselt 90–160 €/jm."),
             "ru": ("Деревянный забор от <b>90 €/м</b> с установкой", "Деревянный забор с материалом и стандартным монтажом обычно стоит 90–160 €/м."),
             "en": ("Timber fence from <b>€90/m</b> installed", "A timber fence usually costs €90–160/m with materials and standard installation.")},
    "roll_mesh": {"et": ("Rullvõrkaed alates <b>25 €/jm</b> koos paigaldusega", "Rullvõrkaed maksab koos materjali ja tavapaigaldusega tavaliselt 25–45 €/jm."),
                  "ru": ("Забор из сетки от <b>25 €/м</b> с установкой", "Забор из рулонной сетки с материалом и стандартным монтажом обычно стоит 25–45 €/м."),
                  "en": ("Roll-mesh fence from <b>€25/m</b> installed", "A roll-mesh fence usually costs €25–45/m with materials and standard installation.")},
    "panel_mesh": {"et": ("3D paneelaed alates <b>35 €/jm</b> koos paigaldusega", "3D-paneelaed maksab koos materjali ja tavapaigaldusega tavaliselt 35–60 €/jm, 2D-paneelaed 50–85 €/jm. Näiteks 50 m 3D-paneelaeda maksab 1 750–3 000 €."),
                   "ru": ("3D-панели от <b>35 €/м</b> с установкой", "Забор из 3D-панелей с материалом и стандартным монтажом обычно стоит 35–60 €/м, из 2D-панелей 50–85 €/м. Например, 50 м забора из 3D-панелей стоят 1 750–3 000 €."),
                   "en": ("3D panel fence from <b>€35/m</b> installed", "A 3D panel fence usually costs €35–60/m with materials and standard installation, a 2D panel fence €50–85/m. For example, 50 m of 3D panel fencing costs €1,750–3,000.")},
    "steel_picket": {"et": ("Metall-lippaed alates <b>85 €/jm</b> koos paigaldusega", "Metall-lippaed maksab koos materjali ja tavapaigaldusega tavaliselt 85–155 €/jm."),
                     "ru": ("Металлический штакетник от <b>85 €/м</b> с установкой", "Забор из металлического штакетника с материалом и стандартным монтажом обычно стоит 85–155 €/м."),
                     "en": ("Steel picket fence from <b>€85/m</b> installed", "A steel picket fence usually costs €85–155/m with materials and standard installation.")},
    "bar_metal": {"et": ("Varbaed alates <b>140 €/jm</b> koos paigaldusega", "Keevitatud varbaed maksab koos materjali ja tavapaigaldusega tavaliselt 140–280 €/jm."),
                  "ru": ("Прутковый забор от <b>140 €/м</b> с установкой", "Сварной прутковый забор с материалом и стандартным монтажом обычно стоит 140–280 €/м."),
                  "en": ("Welded bar fence from <b>€140/m</b> installed", "A welded metal-bar fence usually costs €140–280/m with materials and standard installation.")},
    "profiled_sheet": {"et": ("Profiilplekk-aed alates <b>70 €/jm</b> koos paigaldusega", ""),
                       "ru": ("Забор из профнастила от <b>70 €/м</b> с установкой", ""),
                       "en": ("Profiled-sheet fence from <b>€70/m</b> installed", "")},
    "gates": {"et": ("Automaatne liugvärav alates <b>2 100 €</b>", ""),
              "ru": ("Откатные ворота с автоматикой от <b>2 100 €</b>", ""),
              "en": ("Automated sliding gate from <b>€2,100</b>", "")},
    "repair": {"et": ("Remont alates <b>90 €</b>", ""),
               "ru": ("Ремонт от <b>90 €</b>", ""),
               "en": ("Repairs from <b>€90</b>", "")},
}

PRICE_PAGE = {"et": ("/hinnad/", "Kõik hinnad"), "ru": ("/ru/ceny/", "Все цены"), "en": ("/en/prices/", "Price guide")}

AREA_LINE = {
    "et": ("Töötame kogu Harjumaal: Tallinn, Viimsi, Tiskre, Harku, Rae, Peetri, Jüri, Saue, Laagri, Keila.", "/piirkonnad/harjumaa/", "Teeninduspiirkond"),
    "ru": ("Работаем по всему Харьюмаа: Таллинн, Виймси, Тискре, Харку, Раэ, Пеэтри, Юри, Сауэ, Лаагри, Кейла.", "/ru/rajony/harjumaa/", "Зона обслуживания"),
    "en": ("We work across Harju County: Tallinn, Viimsi, Tiskre, Harku, Rae, Peetri, Jüri, Saue, Laagri, Keila.", "/en/areas/harju-county/", "Service area"),
}


def _json(data):
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'


def _trail(lang, c, home_path):
    """Home > parent hub > page for problem pages; Home > page for services.
    A #fragment level would point back at the homepage URL, so it is left out."""
    trail = [{"@type": "ListItem", "position": 1, "name": UI[lang]["home"], "item": DOMAIN + home_path}]
    if c.get("crumb_parent"):
        trail.append({"@type": "ListItem", "position": 2, "name": c["crumb_parent"][0], "item": DOMAIN + c["crumb_parent"][1]})
    trail.append({"@type": "ListItem", "position": len(trail) + 1, "name": c["name"], "item": DOMAIN + c["path"]})
    return trail


def schema_blocks(lang, c):
    u = UI[lang]
    home_path = {"et": "/", "ru": "/ru/", "en": "/en/"}[lang]
    provider = {
        "@type": "HomeAndConstructionBusiness", "name": "LuxAed", "telephone": PHONE,
        "email": EMAIL, "url": DOMAIN + "/", "@id": DOMAIN + "/#business",
        "areaServed": ["Tallinn", "Harjumaa"],
    }
    blocks = [
        _json({"@context": "https://schema.org", "@type": "Service", "serviceType": c["name"],
               "name": c["name"], "description": c["desc"], "url": DOMAIN + c["path"],
               "inLanguage": lang, "provider": provider, "areaServed": ["Tallinn", "Harjumaa"]}),
        _json({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": _trail(lang, c, home_path)}),
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
             "image": DOMAIN + image_fallback(item[0])} for i, item in enumerate(items)
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
            f'<picture>{webp_sources(image)}<img src="{image_fallback(image)}" alt="{html.escape(alt)}" width="640" height="480" loading="lazy" decoding="async"{style}></picture></div>'
            f'<div class="gtype-txt"><h3>{title}</h3><p>{desc}</p><ul class="gtype-specs">{chips}</ul></div></article>'
        )
    return f'<div class="gtypes gtypes--n{min(len(items), 4)}">' + "".join(cards) + '</div>'


def _gallery(items):
    return '<div class="gal" id="gal">' + "".join(
        f'<a href="{image_fallback(image)}" data-lb="1"><picture>{webp_sources(image)}<img src="{image_fallback(image)}" alt="{html.escape(alt)}" width="600" height="400" loading="lazy"></picture></a>'
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


def _use_cases(lang, path):
    key = PATH_TO_KEY.get(path)
    data = USE_CASES.get(lang, {}).get(key)
    if not data:
        return ""
    heading, direct, items = data
    tag = {"et": "Sobivus", "ru": "Кому подходит", "en": "Suitability"}[lang]
    cards = "".join(
        f'<article class="answer-card"><h3>{title}</h3><p>{text}</p></article>'
        for title, text in items
    )
    return (f'<section class="section section--alt svc-use-cases"><div class="wrap">'
            f'<span class="tag">{tag}</span><h2 class="big">{heading}</h2>'
            f'<p class="lead">{direct}</p><div class="answer-grid">{cards}</div></div></section>')


# "Vaata ka" links: related by topic, not by position in the service list.
RELATED_BY_KEY = {
    "wood": ["steel_picket", "profiled_sheet", "gates"],
    "roll_mesh": ["panel_mesh", "gates", "repair"],
    "panel_mesh": ["roll_mesh", "gates", "steel_picket"],
    "steel_picket": ["wood", "profiled_sheet", "gates"],
    "bar_metal": ["steel_picket", "gates", "panel_mesh"],
    "profiled_sheet": ["wood", "steel_picket", "gates"],
    "gates": ["intercom", "repair", "panel_mesh"],
    "intercom": ["gates", "repair", "panel_mesh"],
    "repair": ["gates", "panel_mesh", "wood"],
}


def _related(lang, current, explicit=None):
    services = SVC[lang]
    if explicit:
        picks = explicit
    else:
        by_key = {item["key"]: (item[lang]["path"], item[lang]["title"]) for item in SERVICE_MATRIX}
        keys = RELATED_BY_KEY.get(PATH_TO_KEY.get(current))
        if keys:
            picks = [by_key[k] for k in keys]
        else:
            index = next((i for i, (path, _) in enumerate(services) if path == current), 0)
            picks = [services[(index + offset) % len(services)] for offset in (1, 2, -1)]
    more = UI[lang]["more"]
    return '<div class="svc-cards">' + "".join(
        f'<a class="svc-card" href="{path}" style="text-decoration:none"><div class="ic">→</div><h3>{title}</h3><p>{more}</p></a>'
        for path, title in picks
    ) + '</div>'


def _answer_section(c):
    """Short direct answer under the hero (problem pages only)."""
    if not c.get("answer"):
        return ""
    heading, text = c["answer"]
    return (f'<section class="section direct-answer"><div class="wrap"><span class="tag">{c.get("answer_tag", "")}</span>'
            f'<h2 class="big">{heading}</h2><p class="lead">{text}</p></div></section>')


def _checks_section(c):
    """Self-checks or first steps as answer cards (problem pages only)."""
    items = c.get("checks") or []
    if not items:
        return ""
    cards = "".join(f'<article class="answer-card"><h3>{title}</h3><p>{text}</p></article>' for title, text in items)
    grid = "answer-grid answer-grid--3" if len(items) % 3 == 0 else "answer-grid answer-grid--2x"
    return (f'<section class="section section--alt"><div class="wrap"><span class="tag">{c.get("checks_tag", "")}</span>'
            f'<h2 class="big">{c.get("checks_h", "")}</h2><p class="lead">{c.get("checks_lead", "")}</p>'
            f'<div class="{grid}">{cards}</div></div></section>')


def _link_cards_section(path):
    """Small section of links to problem pages and guides on an existing page."""
    data = HUB_LINKS.get(path)
    if not data:
        return ""
    tag, heading, cards = data
    items = "".join(
        f'<a class="svc-card help-card" href="{href}"><div class="ic">→</div><h3>{title}</h3><p>{text}</p></a>'
        for href, title, text in cards
    )
    return (f'<section class="section help-links"><div class="wrap"><span class="tag">{tag}</span>'
            f'<h2 class="big">{heading}</h2><div class="svc-cards help-cards">{items}</div></div></section>')


def _sources(c, lang):
    items = c.get("sources") or []
    if not items:
        return ""
    label = {"et": "Allikas", "ru": "Источник", "en": "Source"}[lang]
    checked = {"et": "Kontrollitud 27.09.2026.", "ru": "Проверено 27.09.2026.", "en": "Checked 27 September 2026."}[lang]
    links = " · ".join(f'<a href="{url}" target="_blank" rel="noopener">{html.escape(name)}</a>' for name, url in items)
    return f'<p class="source-note">{label}: {links}. {checked}</p>'


def render_service(lang, c):
    c = dict(c)
    service_key = PATH_TO_KEY.get(c["path"])
    c.update(OUTCOME_COPY.get(lang, {}).get(service_key, {}))
    extra_faq = EXTRA_FAQ.get(lang, {}).get(service_key, [])
    if extra_faq:
        existing_questions = {question for question, _ in c["faq"]}
        c["faq"] = list(c["faq"]) + [item for item in extra_faq if item[0] not in existing_questions]
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
        note = f'<p class="visual-note">{c["variants_note"]}</p>' if c.get("variants_note") else ""
        variants_sec = f'<section class="section section--alt"><div class="wrap"><span class="tag">{c.get("variants_tag", u["options"])}</span><h2 class="big">{c["variants_h"]}</h2>{_cards(variants)}{note}{cta_band}</div></section>'
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
    use_cases = _use_cases(lang, c["path"])
    price_badge, price_range = PRICE_FROM.get(c.get("price_key") or service_key, {}).get(lang, ("", ""))
    price_lead = c.get("price_lead", u["price_p"])
    if price_range and "€" not in price_lead:
        if price_lead == u["price_p"]:
            price_lead = u["price_p"].split(". ", 1)[1]
        price_lead = f"{price_range} {price_lead}"
    price_url, price_label = PRICE_PAGE[lang]
    hero_price = f'<a class="hero-price" href="{price_url}">{price_badge} <span>· {price_label} →</span></a>' if price_badge else ""
    area_text, area_url, area_label = AREA_LINE[lang]
    area_line = f'<p class="svc-area">{area_text} <a href="{area_url}">{area_label} →</a></p>'
    body = f'''{nav(lang, c["path"])}
<main id="main">
<section class="hero"><div class="hero-photo-bg" style="background:url('/img/{c["hero"]}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap"><div class="hero-grid"><div>
    <div class="hero-kicker hand">{c.get("hero_prompt", u["prompt"])}</div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">{RECOMMEND_PERCENT}% {u["trust_verb"]}</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">{REVIEW_COUNT} {u["trust"]}</a></div>
    <div class="hero-service-kicker">{c.get("kicker", "")}</div><h1>{c["h1"]}</h1><p class="hero-service-lead">{c.get("lead", "")}</p>{hero_price}
    <div class="hero-btns"><a class="btn btn-accent" href="#form">{u["quote"]} →</a><a class="btn btn-ghost" href="tel:{TEL}">{u["call"]} {PHONE}</a></div>
  </div>{form}</div>
  <div class="hero-stats"><div class="hstat"><b>{RECOMMEND_PERCENT}%</b><span>{u["recommend"]}</span></div><div class="hstat"><b>{REVIEW_COUNT}</b><span>{u["reviews"]}</span></div><div class="hstat"><b>{EXPERIENCE_YEARS}+</b><span>{u["experience"]}</span></div></div></div>
</section>
{_answer_section(c)}{_checks_section(c)}<section class="section"><div class="wrap"><span class="tag">{c.get("intro_tag", u["get_tag"])}</span><h2 class="big">{c["intro_h"]}</h2><p class="lead">{c["intro_p"]}</p>{_benefits(c["bens"])}</div></section>
{use_cases}{types_sec}{auto_sec}{variants_sec}{local_sec}
<section class="section"><div class="wrap"><span class="tag">{u["price_tag"]}</span><h2 class="big">{u["price_h"]}</h2><p class="lead">{price_lead}</p>
  <div class="honest"><div class="hon good"><h3>{u["included"]}</h3><ul>{"".join(f"<li>{item}</li>" for item in c["incl"])}<li>{u["warranty"]}</li></ul></div>
  <div class="hon bad"><h3>{u["affects"]}</h3><ul>{"".join(f"<li>{item}</li>" for item in c["factors"])}</ul></div></div>{area_line}</div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">{u["process_tag"]}</span><h2 class="big">{process_h}</h2>{_process(process)}</div></section>
{gallery_sec}{video_sec}
<section class="section section--alt"><div class="wrap"><span class="tag">{u["faq"]}</span><h2 class="big">{u["faq_h"]}</h2>{_faq(c["faq"])}{_sources(c, lang)}</div></section>{_link_cards_section(c["path"])}
<section class="section"><div class="wrap"><span class="tag">{u["other"]}</span><h2 class="big">{u["other_h"]}</h2>{_related(lang, c["path"], c.get("related"))}</div></section>
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
