#!/usr/bin/env python3
"""Problem-led repair pages (ET/RU/EN) and the link cards that point to them.

Each page reuses the service landing template (service_layout.render_service), so
it looks exactly like /aia-remont/: same hero, lead form, sections and footer.
Only the copy and photos differ. Facts stay within what the site already states
(repair and diagnostics from 90 EUR, written quotes, work on other installers'
gates). Legal and insurance statements link to their official source.
"""

REPAIR_HUB = {"et": "/aia-remont/", "ru": "/ru/remont-zaborov/", "en": "/en/fence-repair/"}
REPAIR_HUB_NAME = {"et": "Aia ja värava remont", "ru": "Ремонт заборов и ворот", "en": "Fence & gate repair"}
GATES_HUB = {"et": "/varavad/", "ru": "/ru/vorota-avtomatika/", "en": "/en/gates-automation/"}

PROBLEM_ROWS = [
    {"et": "/aia-remont/varav-ei-avane/", "ru": "/ru/remont-zaborov/vorota-ne-otkryvayutsya/", "en": "/en/fence-repair/gate-wont-open/"},
    {"et": "/aia-remont/liugvarava-remont/", "ru": "/ru/remont-zaborov/remont-otkatnyh-vorot/", "en": "/en/fence-repair/sliding-gate-repair/"},
    {"et": "/aia-remont/viltu-aed/", "ru": "/ru/remont-zaborov/pokosilsya-zabor/", "en": "/en/fence-repair/leaning-fence/"},
    {"et": "/aia-remont/kahjustatud-aed/", "ru": "/ru/remont-zaborov/povrezhdennyj-zabor/", "en": "/en/fence-repair/damaged-fence/"},
]
GATE_WONT_OPEN, SLIDING_GATE, LEANING_FENCE, DAMAGED_FENCE = PROBLEM_ROWS

# Guide pages built by guide_more.py; listed here so link cards can point to them.
GUIDE_ROWS = [
    {"et": "/aia-ehitusteatis/", "ru": "/ru/razreshenie-na-zabor/", "en": "/en/fence-permit/"},
    {"et": "/liugvarav-voi-tiibvarav/", "ru": "/ru/otkatnye-ili-raspashnye-vorota/", "en": "/en/sliding-or-swing-gate/"},
]
PERMIT_GUIDE, GATE_GUIDE = GUIDE_ROWS

# Guides hub and articles (built by articles.py). Paths live here so the footer,
# sitemap, validator and link cards all use one registry.
HUB_ROW = {"et": "/nouanded/", "ru": "/ru/sovety/", "en": "/en/guides/"}
ARTICLES = {
    "panel_vs_mesh": {"et": "/paneelaed-voi-vorkaed/", "ru": "/ru/3d-zabor-ili-setka-rabitsa/", "en": "/en/mesh-panels-or-chain-link/"},
    "privacy_fence": {"et": "/kinnine-aed/", "ru": "/ru/gluhoj-zabor/", "en": "/en/privacy-fence/"},
    "neighbour": {"et": "/aed-naabri-piiril/", "ru": "/ru/zabor-s-sosedom/", "en": "/en/boundary-fence-neighbour/"},
    "road_utilities": {"et": "/aed-tee-ja-trasside-lahedal/", "ru": "/ru/zabor-u-dorogi-i-kommunikacij/", "en": "/en/fence-near-road-and-utilities/"},
    "mistakes": {"et": "/aia-ehituse-vead/", "ru": "/ru/oshibki-pri-ustanovke-zabora/", "en": "/en/fence-building-mistakes/"},
    "contractor": {"et": "/kuidas-valida-aiafirmat/", "ru": "/ru/kak-vybrat-firmu-dlya-zabora/", "en": "/en/how-to-choose-a-fence-contractor/"},
    "municipal_rules": {"et": "/aia-korgus-harjumaal/", "ru": "/ru/vysota-zabora-v-harjumaa/", "en": "/en/fence-height-rules-harju-county/"},
    "gate_safety": {"et": "/automaatvarava-ohutus/", "ru": "/ru/bezopasnost-avtomaticheskih-vorot/", "en": "/en/automatic-gate-safety/"},
}
ARTICLE_ORDER = ["panel_vs_mesh", "privacy_fence", "mistakes", "contractor", "neighbour", "road_utilities", "municipal_rules", "gate_safety"]
GUIDE_ROWS = GUIDE_ROWS + [HUB_ROW] + [ARTICLES[key] for key in ARTICLE_ORDER]

LKF_URL = "https://www.lkf.ee/et/liiklus%C3%B5nnetus/lkf-i-h%C3%BCvitatav-kahju"
CHECKED = {"et": "Kontrollitud 27.09.2026.", "ru": "Проверено 27.09.2026.", "en": "Checked 27 September 2026."}

TAGS = {
    "et": {"answer": "Lühivastus", "we_do": "LuxAed teeb", "before": "Enne väljakutset", "causes": "Levinud põhjused"},
    "ru": {"answer": "Короткий ответ", "we_do": "Что делаем", "before": "До вызова мастера", "causes": "Частые причины"},
    "en": {"answer": "Short answer", "we_do": "What we do", "before": "Before you call", "causes": "Common causes"},
}

REPAIR_PRICE = {
    "et": "Remondi ja diagnostika hind algab 90 eurost: see katab väljasõidu ja esmase diagnostika. Detailid ja töömaht lisanduvad. Täpse hinna ütleme pärast diagnostikat, enne remondi alustamist.",
    "ru": "Ремонт и диагностика от 90 €: это выезд и первичная диагностика. Детали и объём работ оплачиваются отдельно. Точную цену называем после диагностики, до начала ремонта.",
    "en": "Repair and diagnostics start from €90, which covers the call-out and initial diagnosis. Parts and further work are additional. We give the exact price after diagnosis, before any repair starts.",
}


def _base(lang, row, key):
    t = TAGS[lang]
    return {
        "path": row[lang], "form_service": "remont", "form_material": "", "price_key": "repair",
        "crumb_parent": (REPAIR_HUB_NAME[lang], REPAIR_HUB[lang]),
        "answer_tag": t["answer"], "intro_tag": t["we_do"], "checks_tag": t["before"], "variants_tag": t["causes"],
        "price_lead": REPAIR_PRICE[lang],
    }


PROBLEMS = {}

# ---------------------------------------------------------------- gate won't open
PROBLEMS["gate_wont_open"] = {
    "et": {
        "name": "Väravaautomaatika remont", "hero": "luxaed-auto-2", "og": "/img/luxaed-auto-2.jpg",
        "title": "Värav ei avane? Väravaautomaatika remont Tallinnas — LuxAed",
        "desc": "Automaatvärav ei avane, ei sulgu või peatub poolel teel? Levinud põhjused, mida saate ise ohutult kontrollida, ja väravaautomaatika remont Tallinnas ja Harjumaal.",
        "kicker": "Remont · väravaautomaatika", "h1": "Värav ei avane<br><em>või ei sulgu?</em>",
        "hero_prompt": "Hei! Värav jäi seisma?",
        "lead": "Sageli on põhjus lihtne: vool, pult, fotoelemendid, lumi või avariivabastus. Kontrollige need ise üle. Kui värav ikka ei liigu, tuleme kohale, teeme diagnostika ja ütleme hinna enne tööd.",
        "answer": ("Kõige sagedamini on põhjus toites, puldis, fotoelementides, jääs või avariivabastuses.",
                   "Kontrollige esmalt kaitsmeid, puldi patareid, fotoelementide puhtust ja seda, et avariivabastus on lukus. Talvel takistab liikumist sageli jää või lumi. Kui need on korras, vajab diagnostikat ajam, juhtplokk või värava mehaanika."),
        "checks_h": "Mida saate ise kontrollida",
        "checks_lead": "Need sammud on ohutud ja võtavad paar minutit. Ärge avage elektrikilpi ega ajami kaant, kui te pole elektrik.",
        "checks": [
            ("Vool ja kaitsmed", "Vaadake, kas elektrikilbis on kaitse või rikkevoolukaitse välja löönud. See juhtub sageli pärast vihma või äikest."),
            ("Pult", "Proovige teist pulti või koodiklaviatuuri. Kui teine töötab, on põhjus patareis või puldi sidumises."),
            ("Fotoelemendid", "Pühkige fotoelementide klaasid puhtaks ja vaadake, et kiire ees pole lund, oksi ega prügikasti. Määrdunud fotoelement ei lase väraval sulguda."),
            ("Avariivabastus", "Kui ajam undab, aga värav ei liigu, võib avariivabastus olla lahti. Keerake see võtmega tagasi lukku."),
            ("Lumi ja jää", "Talvel puhastage värava alune ja kandurite ümbrus. Jää värava teel paneb ajami jõupiirangu tööle ja värav peatub."),
            ("Takistus teel", "Kivi, oks või lehed liugvärava teel takistavad liikumist. Eemaldage need ja proovige uuesti."),
        ],
        "intro_h": "Mida teeme, kui automaatika ei tööta",
        "intro_p": "Leiame rikke põhjuse ja parandame selle. Töötame BFT, Nice, CAME ja teiste levinud ajamitega, ka nende väravatega, mille on paigaldanud teised meistrid.",
        "bens": ["Rikke diagnostika kohapeal", "Fotoelementide puhastus ja seadistus", "Pultide ja vastuvõtja sidumine", "Lõpuasendite ja jõu seadistus", "Ajami, juhtploki või detailide vahetus", "Töö ja ohutuse kontroll pärast remonti"],
        "variants_h": "Miks automaatvärav ei avane",
        "variants": [
            ("⚡", "Toide või juhtplokk", "Välja löönud kaitse, niiskus ühenduskarbis või äikesest kahjustatud juhtplokk."),
            ("◎", "Fotoelemendid", "Must, niiske või nihkunud fotoelement. Värav keeldub sulgumast või pöörab tagasi."),
            ("⌁", "Pult ja vastuvõtja", "Tühi patarei, kadunud sidumine või vastuvõtja rike."),
            ("⚙", "Ajam ja hammaslatt", "Kulunud hammasratas, nihkunud hammaslatt või ajami mootori rike."),
            ("⇄", "Mehaanika", "Kulunud rullikud, vajunud tiib või kinni jooksnud hinged koormavad ajamit üle."),
            ("❄", "Talv", "Jää värava teel, külmunud hinged või lumi tiibade ees."),
        ],
        "cta_band": "Värav ei liigu? Teeme diagnostika",
        "local_h": "Väravaautomaatika remont Tallinnas ja Harjumaal",
        "local_p": "Töötame Tallinnas ja kogu Harjumaal. Enne väljasõitu saatke foto väravast ja ajami andmesildist, nii saame rikke kohta parema ülevaate juba ette.",
        "incl": ["Rikke diagnostika", "Hinna kooskõlastamine enne tööd", "Kokkulepitud remont või detailide vahetus", "Lõpuasendite ja ohutuse kontroll"],
        "factors": ["Rikke põhjus", "Ajami mudel ja varuosade saadavus", "Vajalike detailide hulk", "Värava mehaanika seisukord", "Ligipääs ja töömaht"],
        "process_h": "Nii remondime väravaautomaatikat",
        "process": [
            ("Saatke kirjeldus ja fotod", "Kirjeldage, mida värav teeb või ei tee, ning lisage foto ajamist ja selle andmesildist."),
            ("Diagnostika kohapeal", "Kontrollime üle toite, juhtploki, fotoelemendid, puldid, ajami ja värava mehaanika."),
            ("Hind enne tööd", "Ütleme, mida on vaja parandada või vahetada ja mis see maksab. Alles siis alustame."),
            ("Remont ja kontroll", "Parandame rikke, seadistame lõpuasendid ja jõu ning kontrollime ohutusfunktsioone."),
        ],
        "gallery_h": "Automaatväravad ja ajamid meie töödest",
        "gallery": [("luxaed-auto-2", "BFT ajam puidust liugväraval"), ("luxaed-w-gates-auto", "Liugvärava BFT ajam"), ("luxaed-post-install-2", "Liugvärava ajam betoonalusel"), ("luxaed-w-gates-winter", "Liugvärav talvel")],
        "video": ("luxaed-video-puitvarav", "Puidust liugvärav automaatikaga"), "video_h": "Vaata, kuidas korras automaatvärav liigub",
        "faq": [
            ("Kuidas avada automaatvärav käsitsi voolukatkestuse ajal?", "Enamikul ajamitel on avariivabastus. Avage see võtmega, siis saab värava käsitsi lahti lükata. Kui vool taastub, keerake vabastus tagasi lukku, muidu ajam väravat ei liiguta."),
            ("Miks värav avaneb, aga ei sulgu?", "Kõige sagedamini on põhjus fotoelementides: need on määrdunud, niisked, nihkes või midagi on kiire ees. Süsteem arvab, et teel on takistus, ja jätab värava lahti."),
            ("Miks värav peatub poolel teel ja pöörab tagasi?", "Ajami jõupiirang tunneb takistust. Põhjus võib olla jää või prügi värava teel, kulunud rullikud, vajunud tiib või valesti seadistatud jõud."),
            ("Mida saan enne meistri kutsumist ise kontrollida?", "Kontrollige kaitsmeid, puldi patareid, fotoelementide puhtust ja seda, et avariivabastus on lukus; talvel eemaldage värava teelt jää ja lumi. Ärge avage elektrikilpi ega ajami kaant, kui te pole elektrik."),
            ("Kui palju maksab väravaautomaatika remont?", "Remondi ja diagnostika hind algab 90 eurost: väljasõit ja esmane diagnostika. Detailid ja töö lisanduvad. Täpse hinna ütleme enne remondi alustamist."),
        ],
        "final_cta": "Paneme teie värava <em>taas liikuma</em>",
        "final_cta_text": "Jätke päring või helistage.<br>Diagnostika järel ütleme hinna enne remondi alustamist.",
    },
    "ru": {
        "name": "Ремонт автоматики ворот", "hero": "luxaed-auto-2", "og": "/img/luxaed-auto-2.jpg",
        "title": "Не открываются ворота? Ремонт автоматики в Таллинне — LuxAed",
        "desc": "Автоматические ворота не открываются, не закрываются или встают на полпути? Частые причины, что проверить самому, и ремонт автоматики в Таллинне и Харьюмаа.",
        "kicker": "Ремонт · автоматика ворот", "h1": "Ворота не открываются<br><em>или не закрываются?</em>",
        "hero_prompt": "Привет! Ворота встали?",
        "lead": "Часто причина простая: питание, пульт, фотоэлементы, снег или ручная разблокировка. Проверьте это сами. Если ворота всё равно не двигаются, приедем, проведём диагностику и назовём цену до начала работ.",
        "answer": ("Чаще всего дело в питании, пульте, фотоэлементах, наледи или ручной разблокировке.",
                   "Сначала проверьте автоматы в щитке, батарейку пульта, чистоту фотоэлементов и то, что разблокировка закрыта. Зимой движение часто блокирует лёд или снег. Если всё в порядке, нужна диагностика привода, блока управления или механики ворот."),
        "checks_h": "Что можно проверить самому",
        "checks_lead": "Эти шаги безопасны и займут пару минут. Не вскрывайте электрощит и крышку привода, если вы не электрик.",
        "checks": [
            ("Питание и автоматы", "Посмотрите, не выбило ли автомат или УЗО в щитке. Такое часто бывает после дождя или грозы."),
            ("Пульт", "Попробуйте другой пульт или кодовую панель. Если другой работает, дело в батарейке или привязке пульта."),
            ("Фотоэлементы", "Протрите стёкла фотоэлементов и проверьте, что луч ничего не перекрывает: снег, ветки, мусорный бак. Грязный фотоэлемент не даёт воротам закрыться."),
            ("Разблокировка", "Если привод гудит, а ворота стоят, возможно, открыта ручная разблокировка. Закройте её ключом."),
            ("Снег и лёд", "Зимой очистите зону под воротами и у кареток. Лёд на пути ворот включает защиту по усилию, и ворота останавливаются."),
            ("Препятствие", "Камень, ветка или листья на пути откатных ворот мешают движению. Уберите их и попробуйте снова."),
        ],
        "intro_h": "Что делаем, если автоматика не работает",
        "intro_p": "Находим причину неисправности и устраняем её. Работаем с приводами BFT, Nice, CAME и другими распространёнными марками, в том числе на воротах, которые ставили другие мастера.",
        "bens": ["Диагностика на месте", "Чистка и настройка фотоэлементов", "Привязка пультов и приёмника", "Настройка крайних положений и усилия", "Замена привода, блока управления или деталей", "Проверка работы и безопасности после ремонта"],
        "variants_h": "Почему не открываются автоматические ворота",
        "variants": [
            ("⚡", "Питание или блок управления", "Выбитый автомат, влага в распределительной коробке или повреждённый грозой блок управления."),
            ("◎", "Фотоэлементы", "Грязный, влажный или сбитый фотоэлемент. Ворота не закрываются или едут обратно."),
            ("⌁", "Пульт и приёмник", "Разряженная батарейка, сбитая привязка или неисправный приёмник."),
            ("⚙", "Привод и зубчатая рейка", "Изношенная шестерня, сместившаяся рейка или неисправность мотора."),
            ("⇄", "Механика", "Изношенные ролики, просевшая створка или заклинившие петли перегружают привод."),
            ("❄", "Зима", "Лёд на пути ворот, замёрзшие петли или снег перед створками."),
        ],
        "cta_band": "Ворота не двигаются? Проведём диагностику",
        "local_h": "Ремонт автоматики ворот в Таллинне и Харьюмаа",
        "local_p": "Работаем в Таллинне и по всему Харьюмаа. Перед выездом пришлите фото ворот и шильдика привода: так мы заранее получим представление о неисправности.",
        "incl": ["Диагностика неисправности", "Согласование цены до работ", "Согласованный ремонт или замена деталей", "Проверка крайних положений и безопасности"],
        "factors": ["Причина неисправности", "Модель привода и наличие запчастей", "Количество деталей", "Состояние механики ворот", "Доступ и объём работ"],
        "process_h": "Как мы ремонтируем автоматику ворот",
        "process": [
            ("Пришлите описание и фото", "Опишите, что ворота делают или не делают, и приложите фото привода и его шильдика."),
            ("Диагностика на месте", "Проверяем питание, блок управления, фотоэлементы, пульты, привод и механику ворот."),
            ("Цена до работ", "Говорим, что нужно починить или заменить и сколько это стоит. Только потом начинаем."),
            ("Ремонт и проверка", "Устраняем неисправность, настраиваем крайние положения и усилие, проверяем защитные функции."),
        ],
        "gallery_h": "Автоматические ворота и приводы с наших объектов",
        "gallery": [("luxaed-auto-2", "Привод BFT на деревянных откатных воротах"), ("luxaed-w-gates-auto", "Привод BFT откатных ворот"), ("luxaed-post-install-2", "Привод откатных ворот на бетонном основании"), ("luxaed-w-gates-winter", "Откатные ворота зимой")],
        "video": ("luxaed-video-puitvarav", "Деревянные откатные ворота с автоматикой"), "video_h": "Посмотрите, как ездят исправные автоматические ворота",
        "faq": [
            ("Как открыть автоматические ворота вручную, если нет света?", "У большинства приводов есть ручная разблокировка. Откройте её ключом, и ворота можно сдвинуть рукой. Когда питание вернётся, закройте разблокировку, иначе привод не будет двигать ворота."),
            ("Почему ворота открываются, но не закрываются?", "Чаще всего виноваты фотоэлементы: они грязные, влажные, сбиты или что-то перекрывает луч. Система считает, что на пути препятствие, и оставляет ворота открытыми."),
            ("Почему ворота останавливаются на полпути и едут обратно?", "Срабатывает защита привода по усилию. Причиной бывают лёд или мусор на пути, изношенные ролики, просевшая створка или неверно настроенное усилие."),
            ("Что можно проверить самому до вызова мастера?", "Проверьте автоматы, батарейку пульта, чистоту фотоэлементов и то, что ручная разблокировка закрыта; зимой уберите лёд и снег с пути ворот. Не открывайте щиток и крышку привода, если вы не электрик."),
            ("Сколько стоит ремонт автоматики ворот?", "Ремонт и диагностика от 90 €: выезд и первичная диагностика. Детали и работа оплачиваются отдельно. Точную цену называем до начала ремонта."),
        ],
        "final_cta": "Починим автоматику <em>ваших ворот</em>",
        "final_cta_text": "Оставьте заявку или позвоните.<br>После диагностики назовём цену до начала ремонта.",
    },
    "en": {
        "name": "Gate automation repair", "hero": "luxaed-auto-2", "og": "/img/luxaed-auto-2.jpg",
        "title": "Gate won't open? Automatic gate repair in Tallinn — LuxAed",
        "desc": "Automatic gate won't open, won't close or stops halfway? Common causes, what you can safely check yourself, and gate automation repair in Tallinn and Harju County.",
        "kicker": "Repair · gate automation", "h1": "Gate won't open<br><em>or close?</em>",
        "hero_prompt": "Hey! Gate stuck?",
        "lead": "The cause is often simple: power, the remote, the photocells, snow or the manual release. Check these first. If the gate still won't move, we come out, diagnose the fault and give you the price before any work.",
        "answer": ("Most often the cause is the power supply, the remote, the photocells, ice or the manual release.",
                   "First check the breakers, the remote battery, whether the photocells are clean and whether the manual release is locked. In winter, ice or snow often blocks the gate. If all of that is fine, the drive, the control board or the gate mechanics need a diagnosis."),
        "checks_h": "What you can safely check yourself",
        "checks_lead": "These steps are safe and take a couple of minutes. Do not open the electrical panel or the drive cover unless you are an electrician.",
        "checks": [
            ("Power and breakers", "Check whether a breaker or RCD has tripped in the consumer unit. This often happens after rain or a thunderstorm."),
            ("Remote", "Try another remote or the keypad. If that works, the battery or the remote pairing is the problem."),
            ("Photocells", "Wipe the photocell lenses and make sure nothing blocks the beam, such as snow, branches or a wheelie bin. A dirty photocell stops the gate closing."),
            ("Manual release", "If the drive hums but the gate does not move, the manual release may be open. Lock it again with the key."),
            ("Snow and ice", "In winter, clear the area under the gate and around the carriages. Ice in the gate's path triggers the force limit and the gate stops."),
            ("Obstacles", "A stone, branch or leaves in the path of a sliding gate stop it moving. Remove them and try again."),
        ],
        "intro_h": "What we do when gate automation fails",
        "intro_p": "We find the cause of the fault and fix it. We work with BFT, Nice, CAME and other common drives, including gates installed by other companies.",
        "bens": ["On-site fault diagnosis", "Photocell cleaning and alignment", "Remote and receiver pairing", "Limit position and force setup", "Drive, control board or part replacement", "Function and safety check after repair"],
        "variants_h": "Why an automatic gate won't open",
        "variants": [
            ("⚡", "Power or control board", "A tripped breaker, moisture in a junction box or a control board damaged by lightning."),
            ("◎", "Photocells", "A dirty, wet or misaligned photocell. The gate refuses to close or reverses."),
            ("⌁", "Remote and receiver", "A flat battery, lost pairing or a faulty receiver."),
            ("⚙", "Drive and gear rack", "A worn gear, a shifted gear rack or a motor fault."),
            ("⇄", "Mechanics", "Worn rollers, a sagging leaf or seized hinges overload the drive."),
            ("❄", "Winter", "Ice in the gate's path, frozen hinges or snow in front of the leaves."),
        ],
        "cta_band": "Gate not moving? Book a diagnosis",
        "local_h": "Gate automation repair in Tallinn and Harju County",
        "local_p": "We work across Tallinn and Harju County. Send a photo of the gate and the drive's rating label before the visit so we can get an idea of the fault in advance.",
        "incl": ["Fault diagnosis", "Price agreed before work", "Agreed repair or part replacement", "Limit position and safety check"],
        "factors": ["Cause of the fault", "Drive model and parts availability", "Number of parts needed", "Condition of the gate mechanics", "Access and scope of work"],
        "process_h": "How we repair gate automation",
        "process": [
            ("Send a description and photos", "Tell us what the gate does or does not do, and add a photo of the drive and its rating label."),
            ("On-site diagnosis", "We check the power supply, control board, photocells, remotes, drive and gate mechanics."),
            ("Price before work", "We explain what needs repairing or replacing and what it costs. Only then do we start."),
            ("Repair and check", "We fix the fault, set the limit positions and force, and test the safety functions."),
        ],
        "gallery_h": "Automatic gates and drives from our projects",
        "gallery": [("luxaed-auto-2", "BFT drive on a wooden sliding gate"), ("luxaed-w-gates-auto", "BFT sliding gate drive"), ("luxaed-post-install-2", "Sliding gate drive on a concrete base"), ("luxaed-w-gates-winter", "Sliding gate in winter")],
        "video": ("luxaed-video-puitvarav", "Wooden sliding gate with automation"), "video_h": "See how a working automatic gate moves",
        "faq": [
            ("How do I open an automatic gate by hand during a power cut?", "Most drives have a manual release. Unlock it with the key and push the gate open by hand. Lock the release again when the power returns, otherwise the drive will not move the gate."),
            ("Why does my gate open but not close?", "The photocells are the most common cause: they are dirty, wet or misaligned, or something blocks the beam. The system thinks there is an obstacle and leaves the gate open."),
            ("Why does the gate stop halfway and reverse?", "The drive's force limit detects resistance. Ice or debris in the path, worn rollers, a sagging leaf or an incorrect force setting can cause it."),
            ("What can I check myself before calling a technician?", "Check the breakers, the remote's battery, that the photocells are clean and that the manual release is locked; in winter, clear ice and snow from the gate's path. Don't open the electrical panel or the drive cover unless you are an electrician."),
            ("How much does gate automation repair cost?", "Repair and diagnostics start from €90 for the call-out and initial diagnosis. Parts and labour are additional. We confirm the exact price before the repair starts."),
        ],
        "final_cta": "Let's get your gate <em>moving again</em>",
        "final_cta_text": "Send an enquiry or call us.<br>After diagnosis we give the price before any repair.",
    },
}

# ---------------------------------------------------------------- sliding gate repair
PROBLEMS["sliding_gate"] = {
    "et": {
        "name": "Liugvärava remont", "hero": "luxaed-w-gates-winter", "og": "/img/luxaed-w-gates-winter.jpg",
        "title": "Liugvärava remont: jookseb kinni, vajub või kolksub — LuxAed",
        "desc": "Liugvärav käib raskelt, jookseb kinni, vajub otsast või kolksub? Vahetame rullikud ja kandurid, reguleerime juhikud ja parandame aluse. Tallinn ja Harjumaa.",
        "kicker": "Remont · liugväravad", "h1": "Liugvärava<br><em>remont</em>",
        "hero_prompt": "Hei! Liugvärav käib raskelt?",
        "lead": "Kinni jooksmine, kolksumine ja otsast vajumine tulevad enamasti kulunud rullikutest, lahtistest kanduritest või vajunud alusest. Leiame põhjuse ja parandame värava ilma kogu väravat vahetamata.",
        "answer": ("Liugvärav jookseb kinni või vajub, kui kanduri rullikud on kulunud, kandurid on lahti või alus on vajunud.",
                   "Ka nihkes ülemine juhik või vastuvõtja paneb värava hõõruma. Rullikud ja juhikud saab enamasti vahetada ja reguleerida kohapeal. Vajunud alus või löögist kõverdunud raam vajab suuremat tööd."),
        "checks_h": "Mida saate ise vaadata",
        "checks_lead": "Vaadake väravat küljelt ja alt. Kui värav on tugevalt viltu või rullikutelt maas, ärge seda jõuga liigutage.",
        "checks": [
            ("Kandurid ja rullikud", "Puhastage kandurite ümbrus liivast, lehtedest ja jääst. Prügi rullikute ees on sage kinni jooksmise põhjus."),
            ("Värava vaba ots", "Vaadake, kas värava vaba ots on madalamal kui varem või lohiseb vastuvõtjasse. See viitab lahtistele kanduritele või vajunud alusele."),
            ("Heli", "Kolksumine ja kriuksumine liikumisel tulevad sageli kulunud rullikutest või lahtistest poltidest."),
            ("Pärast lööki", "Kui väravat on autoga puudutatud, vaadake, kas raam on kõver. Kõverdunud väravat ei tasu ajamiga edasi liigutada."),
        ],
        "intro_h": "Mida liugväraval parandame",
        "intro_p": "Konsoolne liugvärav liigub alusele kinnitatud kandurite rullikutel. Kui üks osa kulub või nihkub, koormab see kogu süsteemi ja ajamit. Remondime nii automaatikaga kui ka käsitsi liigutatavaid liugväravaid.",
        "bens": ["Rullikute ja kandurite vahetus", "Kandurite ja kõrguse reguleerimine", "Ülemise juhiku ja vastuvõtja seadistus", "Raami sirgendamine ja tugevdamine", "Aluse ja kinnituste kontroll", "Ajami ja hammaslati seadistus"],
        "variants_h": "Miks liugvärav jookseb kinni",
        "variants": [
            ("⚙", "Kulunud rullikud", "Rullikute laagrid kuluvad ning rullikud hakkavad kinni jooksma, kriuksuma või kolksuma."),
            ("▭", "Lahtised kandurid", "Kandurite poldid lõdvenevad ja värav vajub otsast allapoole."),
            ("⇥", "Nihkes juhikud", "Ülemine juhik või vastuvõtja on nihkes. Värav hõõrub või ei sulgu lõpuni."),
            ("▦", "Vajunud alus", "Betoonalus on vajunud või pragunenud ning värav ei püsi enam loodis."),
            ("✕", "Löögikahjustus", "Auto või tugev lükkamine on raami kõverdanud."),
            ("❄", "Jää ja lumi", "Talvel koguneb kandurite juurde jää või lumi."),
        ],
        "cta_band": "Liugvärav jookseb kinni? Vaatame üle",
        "local_h": "Liugväravate remont Tallinnas ja Harjumaal",
        "local_p": "Remondime liugväravaid Tallinnas ja kogu Harjumaal. Enne väljasõitu saatke fotod kanduritest, värava vabast otsast ja ajamist, nii saame töö ulatusest parema ülevaate.",
        "incl": ["Värava ja kandurite ülevaatus", "Hinna kooskõlastamine enne tööd", "Rullikute, kandurite või juhikute vahetus kokkuleppel", "Värava liikumise ja automaatika kontroll"],
        "factors": ["Värava kaal ja pikkus", "Kandurite ja rullikute mudel", "Aluse seisukord", "Raami kahjustused", "Automaatika seadistus"],
        "process_h": "Nii remondime liugväravat",
        "process": [
            ("Saatke fotod", "Pildistage kandureid, värava vaba otsa, vastuvõtjat ja ajamit ning kirjeldage, millal probleem algas."),
            ("Ülevaatus", "Kontrollime rullikuid, kandureid, juhikuid, alust, raami ja automaatika seadistust."),
            ("Hind enne tööd", "Ütleme, mida vahetada või reguleerida ja mis see maksab."),
            ("Remont ja lõppkontroll", "Vahetame või reguleerime osad ning kontrollime, et värav liigub kergelt ja sulgub täpselt."),
        ],
        "gallery_h": "Liugväravad ja nende detailid",
        "gallery": [("luxaed-gate-hardware-1", "Liugvärava rullikud ja kandurid"), ("luxaed-wood-sliding-gate-1", "Puidust liugvärav ja kandurid alusel"), ("luxaed-w-gates-winter", "Liugvärav talvel"), ("luxaed-post-install-1", "Liugvärava karkass enne paigaldust")],
        "video": ("luxaed-reel-varav-oht", "Liugväravad õhtuvalguses"), "video_h": "Vaata, kuidas korras liugvärav töötab",
        "faq": [
            ("Kas liugvärava rullikuid saab vahetada ilma väravat maha võtmata?", "Sageli jah. Värav toestatakse ja kandur või rullikud vahetatakse kohapeal. See sõltub kanduri mudelist ja värava seisukorrast."),
            ("Miks liugvärav vajub otsast allapoole?", "Kõige sagedamini on kandurite kinnitused lõdvenenud või alus vajunud. Mõnikord on põhjus kulunud rullikutes või löögist kõverdunud raamis."),
            ("Kas raskelt liikuv värav võib ajamit kahjustada?", "Jah. Raskelt liikuv värav koormab ajamit ja hammaslatti üle. Mehaaniline põhjus tasub kõrvaldada enne, kui ajam rikki läheb."),
            ("Kui palju maksab liugvärava remont?", "Remondi ja diagnostika hind algab 90 eurost: väljasõit ja esmane diagnostika. Rullikud, kandurid, muud detailid ja töömaht lisanduvad. Hinna ütleme enne tööd."),
        ],
        "final_cta": "Paneme liugvärava <em>taas kergelt liikuma</em>",
        "final_cta_text": "Jätke päring või helistage.<br>Vaatame värava üle ja ütleme hinna enne remondi alustamist.",
    },
    "ru": {
        "name": "Ремонт откатных ворот", "hero": "luxaed-w-gates-winter", "og": "/img/luxaed-w-gates-winter.jpg",
        "title": "Ремонт откатных ворот в Таллинне: заедают, просели — LuxAed",
        "desc": "Откатные (раздвижные) ворота заедают, тяжело ходят, просели или стучат? Меняем ролики и каретки, регулируем направляющие, чиним основание. Таллинн и Харьюмаа.",
        "kicker": "Ремонт · откатные ворота", "h1": "Ремонт<br><em>откатных ворот</em>",
        "hero_prompt": "Привет! Ворота тяжело ходят?",
        "lead": "Заедание, стук и провисание края чаще всего связаны с изношенными роликами, ослабшими каретками или просевшим основанием. Найдём причину и починим ворота без замены всей конструкции.",
        "answer": ("Откатные ворота заедают или проседают, когда изнашиваются ролики, ослабевают каретки или проседает основание.",
                   "Сбитая верхняя направляющая или уловитель тоже заставляют ворота тереться. Ролики и направляющие обычно меняют и регулируют на месте. Просевшее основание или погнутая после удара рама требуют более серьёзной работы."),
        "checks_h": "Что можно посмотреть самому",
        "checks_lead": "Осмотрите ворота сбоку и снизу. Если ворота сильно перекосило или они сошли с роликов, не двигайте их силой.",
        "checks": [
            ("Каретки и ролики", "Очистите зону кареток от песка, листьев и льда. Мусор перед роликами часто вызывает заедание."),
            ("Высота края", "Посмотрите, не опустился ли свободный край ворот и не въезжает ли он в уловитель с усилием. Это признак ослабших кареток или просевшего основания."),
            ("Звук", "Стук и скрип при движении часто дают изношенные ролики или ослабшие болты."),
            ("После удара", "Если в ворота въехала машина, проверьте, не погнута ли рама. Погнутые ворота не стоит дальше гонять приводом."),
        ],
        "intro_h": "Что чиним в откатных воротах",
        "intro_p": "Консольные откатные ворота едут на роликах кареток, закреплённых на основании. Если одна деталь износилась или сместилась, нагрузка ложится на всю систему и на привод. Ремонтируем ворота и с автоматикой, и с ручным открыванием.",
        "bens": ["Замена роликов и кареток", "Регулировка кареток и высоты", "Настройка верхней направляющей и уловителя", "Правка и усиление рамы", "Проверка основания и креплений", "Настройка привода и зубчатой рейки"],
        "variants_h": "Почему заедают откатные ворота",
        "variants": [
            ("⚙", "Износ роликов", "Подшипники роликов изнашиваются, и ролики начинают заедать, скрипеть или стучать."),
            ("▭", "Ослабшие каретки", "Болты кареток ослабевают, и край ворот опускается."),
            ("⇥", "Сбитые направляющие", "Верхняя направляющая или уловитель сместились. Ворота трутся или не закрываются до конца."),
            ("▦", "Просевшее основание", "Бетонное основание просело или треснуло, и ворота больше не стоят ровно."),
            ("✕", "Удар", "Машина или сильный толчок погнули раму."),
            ("❄", "Лёд и снег", "Зимой у кареток намерзает лёд или набивается снег."),
        ],
        "cta_band": "Ворота заедают? Приедем и посмотрим",
        "local_h": "Ремонт откатных ворот в Таллинне и Харьюмаа",
        "local_p": "Чиним откатные ворота в Таллинне и по всему Харьюмаа. Перед выездом пришлите фото кареток, свободного края ворот и привода: так мы заранее лучше поймём объём работ.",
        "incl": ["Осмотр ворот и кареток", "Согласование цены до работ", "Замена роликов, кареток или направляющих по договорённости", "Проверка хода ворот и автоматики"],
        "factors": ["Вес и длина ворот", "Модель кареток и роликов", "Состояние основания", "Повреждения рамы", "Настройка автоматики"],
        "process_h": "Как мы ремонтируем откатные ворота",
        "process": [
            ("Пришлите фото", "Сфотографируйте каретки, свободный край ворот, уловитель и привод и опишите, когда началась проблема."),
            ("Осмотр", "Проверяем ролики, каретки, направляющие, основание, раму и настройку автоматики."),
            ("Цена до работ", "Говорим, что заменить или отрегулировать и сколько это стоит."),
            ("Ремонт и проверка хода", "Меняем или регулируем детали и проверяем, что ворота идут легко и точно закрываются."),
        ],
        "gallery_h": "Откатные ворота и их детали",
        "gallery": [("luxaed-gate-hardware-1", "Ролики и каретки откатных ворот"), ("luxaed-wood-sliding-gate-1", "Деревянные откатные ворота и каретки на основании"), ("luxaed-w-gates-winter", "Откатные ворота зимой"), ("luxaed-post-install-1", "Каркас откатных ворот перед монтажом")],
        "video": ("luxaed-reel-varav-oht", "Откатные ворота вечером"), "video_h": "Посмотрите исправные откатные ворота в работе",
        "faq": [
            ("Можно ли поменять ролики, не снимая ворота?", "Часто да. Ворота подпирают, и каретку или ролики меняют на месте. Это зависит от модели кареток и состояния ворот."),
            ("Почему откатные ворота провисают на конце?", "Чаще всего ослабли крепления кареток или просело основание. Иногда причина в изношенных роликах или погнутой после удара раме."),
            ("Могут ли тугие ворота испортить привод?", "Да. Тяжело идущие ворота перегружают привод и зубчатую рейку. Механическую причину лучше устранить до того, как сломается привод."),
            ("Сколько стоит ремонт откатных ворот?", "Ремонт и диагностика от 90 €: выезд и первичная диагностика. Ролики, каретки, другие детали и объём работ оплачиваются отдельно. Цену называем до начала работ."),
        ],
        "final_cta": "Вернём воротам <em>лёгкий ход</em>",
        "final_cta_text": "Оставьте заявку или позвоните.<br>Осмотрим ворота и назовём цену до начала ремонта.",
    },
    "en": {
        "name": "Sliding gate repair", "hero": "luxaed-w-gates-winter", "og": "/img/luxaed-w-gates-winter.jpg",
        "title": "Sliding gate repair: sticking, sagging or noisy — LuxAed",
        "desc": "Sliding gate sticking, hard to move, sagging at the end or clunking? We replace rollers and carriages, adjust the guides and fix the base. Tallinn and Harju County.",
        "kicker": "Repair · sliding gates", "h1": "Sliding gate<br><em>repair</em>",
        "hero_prompt": "Hey! Gate hard to slide?",
        "lead": "Sticking, clunking and a dropping end are usually caused by worn rollers, loose carriages or a settled base. We find the cause and repair the gate without replacing the whole structure.",
        "answer": ("A sliding gate sticks or sags when the rollers wear, the carriages work loose or the base settles.",
                   "A shifted top guide or catcher also makes the gate rub. Rollers and guides can usually be replaced and adjusted on site. A settled base or a frame bent by an impact needs more work."),
        "checks_h": "What you can check yourself",
        "checks_lead": "Look at the gate from the side and from below. If the gate is badly skewed or off its rollers, do not force it.",
        "checks": [
            ("Carriages and rollers", "Clear sand, leaves and ice from around the carriages. Debris in front of the rollers is a common cause of sticking."),
            ("Height at the end", "Check whether the free end of the gate sits lower than before or drags into the catcher. This points to loose carriages or a settled base."),
            ("Noise", "Clunking and squeaking while moving usually come from worn rollers or loose bolts."),
            ("After an impact", "If a car has hit the gate, check whether the frame is bent. Do not keep running a bent gate with the drive."),
        ],
        "intro_h": "What we repair on sliding gates",
        "intro_p": "A cantilever sliding gate runs on carriage rollers fixed to its base. When one part wears or shifts, it loads the whole system and the drive. We repair both automated and manual sliding gates.",
        "bens": ["Roller and carriage replacement", "Carriage and height adjustment", "Top guide and catcher alignment", "Frame straightening and reinforcement", "Base and fixing inspection", "Drive and gear rack adjustment"],
        "variants_h": "Why a sliding gate sticks",
        "variants": [
            ("⚙", "Worn rollers", "Roller bearings wear out, and the rollers start to stick, squeak or clunk."),
            ("▭", "Loose carriages", "Carriage bolts work loose and the end of the gate drops."),
            ("⇥", "Misaligned guides", "The top guide or catcher has shifted. The gate rubs or does not close fully."),
            ("▦", "Settled base", "The concrete base has settled or cracked, so the gate no longer sits level."),
            ("✕", "Impact damage", "A car or a hard push has bent the frame."),
            ("❄", "Ice and snow", "In winter, ice or snow builds up around the carriages."),
        ],
        "cta_band": "Gate sticking? Let us take a look",
        "local_h": "Sliding gate repair in Tallinn and Harju County",
        "local_p": "We repair sliding gates across Tallinn and Harju County. Send photos of the carriages, the free end of the gate and the drive before the visit so we can judge the scope of work.",
        "incl": ["Gate and carriage inspection", "Price agreed before work", "Roller, carriage or guide replacement as agreed", "Gate travel and automation check"],
        "factors": ["Gate weight and length", "Carriage and roller model", "Condition of the base", "Frame damage", "Automation setup"],
        "process_h": "How we repair a sliding gate",
        "process": [
            ("Send photos", "Photograph the carriages, the free end of the gate, the catcher and the drive, and tell us when the problem started."),
            ("Inspection", "We check the rollers, carriages, guides, base, frame and automation settings."),
            ("Price before work", "We explain what to replace or adjust and what it costs."),
            ("Repair and test run", "We replace or adjust the parts and check that the gate moves easily and closes accurately."),
        ],
        "gallery_h": "Sliding gates and their hardware",
        "gallery": [("luxaed-gate-hardware-1", "Sliding gate rollers and carriages"), ("luxaed-wood-sliding-gate-1", "Wooden sliding gate with carriages on its base"), ("luxaed-w-gates-winter", "Sliding gate in winter"), ("luxaed-post-install-1", "Sliding gate frame before installation")],
        "video": ("luxaed-reel-varav-oht", "Sliding gates at dusk"), "video_h": "See a working sliding gate in action",
        "faq": [
            ("Can the rollers be replaced without taking the gate down?", "Often, yes. The gate is supported and the carriage or rollers are replaced on site. It depends on the carriage model and the condition of the gate."),
            ("Why does my sliding gate sag at the end?", "The carriage fixings have usually worked loose or the base has settled. Sometimes worn rollers or a frame bent by an impact are the cause."),
            ("Can a stiff gate damage the drive?", "Yes. A gate that is hard to move overloads the drive and the gear rack. Fix the mechanical cause before the drive fails."),
            ("How much does sliding gate repair cost?", "Repair and diagnostics start from €90 for the call-out and initial diagnosis. Rollers, carriages, other parts and labour are additional. We confirm the price before work."),
        ],
        "final_cta": "Let's make your gate <em>glide again</em>",
        "final_cta_text": "Send an enquiry or call us.<br>We inspect the gate and give the price before the repair.",
    },
}

# ---------------------------------------------------------------- leaning fence
PROBLEMS["leaning_fence"] = {
    "et": {
        "name": "Viltu aia ja postide remont", "hero": "luxaed-repair-real-v1", "og": "/img/luxaed-repair-real-v1.jpg",
        "title": "Aed on viltu või post logiseb? Aiapostide remont — LuxAed",
        "desc": "Viltu vajunud aed, logisev post või kõver sektsioon? Leiame põhjuse ning seame postid sirgeks, betoneerime uuesti või vahetame. Aia remont Tallinnas ja Harjumaal.",
        "kicker": "Remont · postid ja sektsioonid", "h1": "Aed on viltu<br><em>või post logiseb?</em>",
        "hero_prompt": "Hei! Aed hakkas kalduma?",
        "lead": "Viltu aed ei tähenda alati uut aeda. Sageli piisab mõne posti sirgeks seadmisest, uuesti betoneerimisest või vahetusest. Kui kaldu on pikk lõik, selgitame välja põhjuse, et probleem ei korduks.",
        "answer": ("Aed vajub viltu peamiselt külmakerge, tuulekoormuse või mädanenud ja roostes postide tõttu.",
                   "Külmakerge tõstab poste, mille alus või sügavus ei sobi pinnasega. Tuul koormab kinnist aeda. Üksikuid poste saab sirgeks seada ja uuesti kinnitada. Kui kaldu on paljud postid, tuleb lahendada põhjus: sügavus, alus või postide samm."),
        "checks_h": "Mida saate ise vaadata",
        "checks_lead": "Need tähelepanekud aitavad meil juba fotode põhjal aru saada, kas piisab väikesest remondist.",
        "checks": [
            ("Üks post või mitu", "Vaadake aiajoont küljelt. Kui kaldu on üks post, on remont väike. Kui kaldu on pikk lõik, on põhjus tavaliselt aluses või sügavuses."),
            ("Millal see juhtus", "Kevadel pärast külmi viitab kalle sageli külmakergele. Pärast tormi on põhjus tavaliselt tuul, pärast lumekoristust või auto kokkupõrget aga löök."),
            ("Posti jalam", "Vaadake posti kohast, kus see maasse läheb: kas puitpost on pehme, metallpost roostes või betoonalus lahti ja liigub koos postiga."),
            ("Sektsioon või värav", "Kas sektsioon on kõver või on ainult post kaldu? Kas jalgvärav hakkas hõõruma? Pildistage mõlemat."),
        ],
        "intro_h": "Mida viltu aiaga teeme",
        "intro_p": "Kontrollime, kas probleem on ühes postis, aluses, sektsioonis või kogu aiajoonel. Seejärel pakume kõige mõistlikuma lahenduse: sirgeks seadmine, uus betoneerimine, posti vahetus või lõigu ümberehitus.",
        "bens": ["Postide sirgeks seadmine ja loodimine", "Postide uuesti betoneerimine", "Mädanenud või roostes postide vahetus", "Sektsioonide ja kinnituste vahetus", "Tugevdus tuulisel krundil", "Vana posti ja betooni eemaldus"],
        "variants_h": "Miks aed vajub viltu",
        "variants": [
            ("❄", "Külmakerge", "Märg savine pinnas paisub külmaga ja tõstab poste, mille alus või sügavus pinnasega ei sobi."),
            ("≋", "Tuulekoormus", "Kinnisele puit- või profiilplekk-aiale mõjub suur tuulekoormus. Nõrgad postid hakkavad kalduma."),
            ("▥", "Mädanemine ja rooste", "Puitpost mädaneb maapinna kohalt, metallpost roostetab jalamist."),
            ("✕", "Löök või lumi", "Auto, lumesahk või vastu aeda lükatud lumi painutab poste ja sektsioone."),
        ],
        "cta_band": "Aed on viltu? Saatke fotod",
        "local_h": "Aia remont Tallinnas ja Harjumaal",
        "local_p": "Remondime viltu vajunud aedu Tallinnas ja kogu Harjumaal. Saatke foto aiajoonest küljelt ja lähivõte posti jalamist, siis näeme kahjustuse ulatust juba enne väljasõitu.",
        "incl": ["Aiajoone ja postide ülevaatus", "Hinna kooskõlastamine enne tööd", "Postide sirgeks seadmine, betoneerimine või vahetus kokkuleppel", "Sektsioonide ja väravate kontroll pärast remonti"],
        "factors": ["Viltu postide arv", "Posti ja aluse tüüp", "Pinnas ja ligipääs", "Sektsioonide seisukord", "Vana betooni eemaldus"],
        "process_h": "Nii parandame viltu aia",
        "process": [
            ("Saatke fotod", "Pildistage aiajoont küljelt ja posti jalamit lähedalt. Kirjutage, millal kalle tekkis."),
            ("Ülevaatus", "Kontrollime poste, aluseid, sektsioone ja pinnast ning leiame kalde põhjuse."),
            ("Hind enne tööd", "Pakume lahenduse ja ütleme hinna enne remondi algust."),
            ("Remont", "Seame postid sirgeks, betoneerime või vahetame need ning kinnitame sektsioonid ja väravad."),
        ],
        "gallery_h": "Postide ja aia remonditööd",
        "gallery": [("luxaed-repair-real-v1", "Vana betoonposti eemaldamine"), ("luxaed-reel-postid-poster", "Postiaukude puurimine"), ("luxaed-w-mesh-detail", "Kinnituste kontroll"), ("luxaed-w-crew", "Meister objektil")],
        "video": ("luxaed-reel-remont", "Vana betoonposti eemaldamine"), "video_h": "Vaata vana posti eemaldamist",
        "faq": [
            ("Kas viltu posti saab lihtsalt sirgeks lükata?", "Mõnikord saab posti sirgeks seada ja uuesti kinnitada. Kui alus on lahti või post mädanenud või roostes, tuleb see uuesti betoneerida või vahetada. Muidu vajub post järgmisel talvel tagasi."),
            ("Miks aed vajub kevadel viltu?", "Talvel paisub märg pinnas külmaga ja tõstab poste, mille alus või sügavus pinnasega ei sobi. Kevadel ei vaju post enam sirgelt tagasi. Seda nimetatakse külmakergeks."),
            ("Kas pean kogu aia välja vahetama?", "Tavaliselt mitte. Kui sektsioonid on terved ja kaldu on üksikud postid, on remont palju soodsam. Kui kaldu on enamik poste või sektsioonid on läbi roostetanud, võib uus aed olla mõistlikum."),
            ("Kui palju maksab aiaposti vahetus?", "Remondi ja diagnostika hind algab 90 eurost: väljasõit ja esmane diagnostika. Uued postid, betoon ja töö lisanduvad ning sõltuvad postide arvust, pinnasest ja ligipääsust. Hinna ütleme enne tööd."),
        ],
        "final_cta": "Seame teie aia <em>taas sirgeks</em>",
        "final_cta_text": "Saatke fotod või helistage.<br>Ütleme, kas remondist piisab, ja anname hinna enne tööd.",
    },
    "ru": {
        "name": "Ремонт покосившегося забора", "hero": "luxaed-repair-real-v1", "og": "/img/luxaed-repair-real-v1.jpg",
        "title": "Покосился забор, шатается столб? Ремонт в Таллинне — LuxAed",
        "desc": "Забор завалился, столб шатается или секция погнулась? Найдём причину, выпрямим, заново забетонируем или заменим столбы. Ремонт заборов в Таллинне и Харьюмаа.",
        "kicker": "Ремонт · столбы и секции", "h1": "Покосился забор<br><em>или шатается столб?</em>",
        "hero_prompt": "Привет! Забор повело?",
        "lead": "Если забор покосился, это ещё не значит, что нужен новый. Часто достаточно выпрямить, заново забетонировать или заменить несколько столбов. Если завалился длинный участок, ищем причину, чтобы проблема не повторилась.",
        "answer": ("Забор кренится в основном из-за морозного пучения, ветра или сгнивших и проржавевших столбов.",
                   "Пучение выталкивает столбы, основание или глубина которых не подходят грунту. Ветер нагружает сплошной забор. Отдельные столбы можно выпрямить и закрепить заново. Если наклонились многие столбы, нужно устранять причину: глубину, основание или шаг столбов."),
        "checks_h": "Что можно посмотреть самому",
        "checks_lead": "Эти наблюдения помогут нам уже по фото понять, хватит ли небольшого ремонта.",
        "checks": [
            ("Один столб или несколько", "Посмотрите на линию забора сбоку. Если наклонился один столб, ремонт небольшой. Если завалился длинный участок, причина обычно в основании или глубине."),
            ("Когда это случилось", "Наклон весной после морозов часто говорит о пучении. Если забор накренился после бури, виноват ветер, а если после уборки снега или наезда машины, то удар."),
            ("Низ столба", "Посмотрите у земли: не мягкий ли деревянный столб, не проржавел ли металлический, не болтается ли бетонное основание вместе со столбом."),
            ("Секция или калитка", "Погнута ли секция или наклонён только столб? Не начала ли тереть калитка? Сфотографируйте и то, и другое."),
        ],
        "intro_h": "Что делаем с покосившимся забором",
        "intro_p": "Проверяем, в чём проблема: в одном столбе, в основании, в секции или во всей линии забора. Затем предлагаем самый разумный вариант: выпрямить, заново забетонировать, заменить столб или переделать участок.",
        "bens": ["Выравнивание столбов", "Повторное бетонирование", "Замена сгнивших или ржавых столбов", "Замена секций и креплений", "Усиление на ветреном участке", "Демонтаж старого столба и бетона"],
        "variants_h": "Почему заваливается забор",
        "variants": [
            ("❄", "Морозное пучение", "Влажный глинистый грунт расширяется на морозе и выталкивает столбы, основание или глубина которых не подходят грунту."),
            ("≋", "Ветровая нагрузка", "Сплошной деревянный забор или профнастил сильно нагружается ветром. Слабые столбы начинают крениться."),
            ("▥", "Гниль и ржавчина", "Деревянный столб гниёт у земли, металлический ржавеет у основания."),
            ("✕", "Удар или снег", "Машина, снегоуборщик или сдвинутый к забору снег гнут столбы и секции."),
        ],
        "cta_band": "Забор покосился? Пришлите фото",
        "local_h": "Ремонт заборов в Таллинне и Харьюмаа",
        "local_p": "Ремонтируем покосившиеся заборы в Таллинне и по всему Харьюмаа. Пришлите фото линии забора сбоку и крупный план низа столба: так мы заранее увидим объём повреждений.",
        "incl": ["Осмотр линии забора и столбов", "Согласование цены до работ", "Выравнивание, бетонирование или замена столбов по договорённости", "Проверка секций и калитки после ремонта"],
        "factors": ["Количество наклонённых столбов", "Тип столба и основания", "Грунт и доступ", "Состояние секций", "Демонтаж старого бетона"],
        "process_h": "Как мы чиним покосившийся забор",
        "process": [
            ("Пришлите фото", "Сфотографируйте линию забора сбоку и низ столба крупным планом. Напишите, когда появился наклон."),
            ("Осмотр", "Проверяем столбы, основания, секции и грунт и находим причину наклона."),
            ("Цена до работ", "Предлагаем решение и называем цену до начала ремонта."),
            ("Ремонт", "Выпрямляем, бетонируем или меняем столбы и закрепляем секции и калитку."),
        ],
        "gallery_h": "Ремонт столбов и заборов",
        "gallery": [("luxaed-repair-real-v1", "Демонтаж старого бетонного столба"), ("luxaed-reel-postid-poster", "Бурение ям под столбы"), ("luxaed-w-mesh-detail", "Проверка креплений"), ("luxaed-w-crew", "Мастер на объекте")],
        "video": ("luxaed-reel-remont", "Демонтаж старого бетонного столба"), "video_h": "Посмотрите демонтаж старого столба",
        "faq": [
            ("Можно ли просто выпрямить наклонённый столб?", "Иногда столб можно выпрямить и закрепить заново. Если основание болтается или столб сгнил или проржавел, его нужно заново забетонировать или заменить. Иначе следующей зимой он снова наклонится."),
            ("Почему забор кренится весной?", "Зимой влажный грунт расширяется на морозе и выталкивает столбы, основание или глубина которых не подходят грунту. Весной столб уже не встаёт на место. Это морозное пучение."),
            ("Нужно ли менять весь забор?", "Обычно нет. Если секции целы и наклонились отдельные столбы, ремонт намного дешевле. Если завалилось большинство столбов или секции проржавели насквозь, новый забор может оказаться разумнее."),
            ("Сколько стоит замена столба забора?", "Ремонт и диагностика от 90 €: выезд и первичная диагностика. Новые столбы, бетон и работа оплачиваются отдельно и зависят от количества столбов, грунта и доступа. Цену называем до начала работ."),
        ],
        "final_cta": "Выпрямим ваш <em>забор</em>",
        "final_cta_text": "Пришлите фото или позвоните.<br>Скажем, хватит ли ремонта, и назовём цену до начала работ.",
    },
    "en": {
        "name": "Leaning fence repair", "hero": "luxaed-repair-real-v1", "og": "/img/luxaed-repair-real-v1.jpg",
        "title": "Leaning fence or loose post? Fence post repair — LuxAed",
        "desc": "Fence leaning, a post wobbling or a section bent? We find the cause and straighten, re-concrete or replace the posts. Fence repair in Tallinn and Harju County.",
        "kicker": "Repair · posts and sections", "h1": "Leaning fence<br><em>or loose post?</em>",
        "hero_prompt": "Hey! Fence leaning?",
        "lead": "A leaning fence does not always mean a new fence. Often a few posts can be straightened, re-concreted or replaced. If a long run is leaning, we find the cause so the problem does not come back.",
        "answer": ("Fences lean mainly because of frost heave, wind load or posts that have rotted or rusted.",
                   "Frost heave lifts posts whose base or depth does not suit the ground. Wind loads a solid fence. Single posts can be straightened and refixed. If many posts lean, the cause needs fixing: depth, base or post spacing."),
        "checks_h": "What you can check yourself",
        "checks_lead": "These observations help us judge from photos whether a small repair will do.",
        "checks": [
            ("One post or several", "Look along the fence line from the side. If one post leans, the repair is small. If a long run leans, the cause is usually the base or the depth."),
            ("When it happened", "Leaning in spring after frost often points to frost heave. After a storm the cause is wind; after snow clearing or a car, an impact."),
            ("Base of the post", "Look at ground level: is a timber post soft, a metal post rusted, or is the concrete base loose and moving with the post?"),
            ("Section or gate", "Is the section bent or is only the post leaning? Has the pedestrian gate started to rub? Photograph both."),
        ],
        "intro_h": "What we do with a leaning fence",
        "intro_p": "We check whether the problem is in one post, the base, a section or the whole fence line. Then we propose the most sensible fix: straightening, re-concreting, replacing a post or rebuilding a run.",
        "bens": ["Straightening and levelling posts", "Re-concreting posts", "Replacing rotten or rusted posts", "Replacing sections and fixings", "Reinforcement on windy sites", "Removing old posts and concrete"],
        "variants_h": "Why fences lean",
        "variants": [
            ("❄", "Frost heave", "Wet clay soil expands in frost and lifts posts whose base or depth does not suit the ground."),
            ("≋", "Wind load", "A solid timber or profiled-sheet fence takes a heavy wind load. Weak posts start to lean."),
            ("▥", "Rot and rust", "Timber posts rot at ground level; metal posts rust at the base."),
            ("✕", "Impact or snow", "A car, a snow plough or snow pushed against the fence bends posts and sections."),
        ],
        "cta_band": "Fence leaning? Send us photos",
        "local_h": "Fence repair in Tallinn and Harju County",
        "local_p": "We repair leaning fences across Tallinn and Harju County. Send a photo of the fence line from the side and a close-up of the post base, so we can see the extent of the damage before the visit.",
        "incl": ["Fence line and post inspection", "Price agreed before work", "Straightening, re-concreting or replacing posts as agreed", "Section and gate check after repair"],
        "factors": ["Number of leaning posts", "Post and base type", "Ground and access", "Condition of the sections", "Removing old concrete"],
        "process_h": "How we fix a leaning fence",
        "process": [
            ("Send photos", "Photograph the fence line from the side and the post base up close. Tell us when the lean appeared."),
            ("Inspection", "We check the posts, bases, sections and ground and find the cause of the lean."),
            ("Price before work", "We propose a solution and confirm the price before the repair starts."),
            ("Repair", "We straighten, re-concrete or replace the posts and refix the sections and gates."),
        ],
        "gallery_h": "Post and fence repair work",
        "gallery": [("luxaed-repair-real-v1", "Removing an old concrete post"), ("luxaed-reel-postid-poster", "Drilling post holes"), ("luxaed-w-mesh-detail", "Checking the fixings"), ("luxaed-w-crew", "Our craftsman on site")],
        "video": ("luxaed-reel-remont", "Removing an old concrete post"), "video_h": "Watch an old post being removed",
        "faq": [
            ("Can a leaning post simply be pushed straight?", "Sometimes a post can be straightened and refixed. If the base is loose or the post has rotted or rusted, it must be re-concreted or replaced, otherwise it will lean again next winter."),
            ("Why does my fence lean in spring?", "In winter, wet ground expands in frost and lifts posts whose base or depth does not suit the ground. In spring the post does not settle back straight. This is called frost heave."),
            ("Do I need to replace the whole fence?", "Usually not. If the sections are sound and only a few posts lean, a repair costs far less. If most posts lean or the sections have rusted through, a new fence may be the better option."),
            ("How much does replacing a fence post cost?", "Repair and diagnostics start from €90 for the call-out and initial diagnosis. New posts, concrete and labour are additional and depend on the number of posts, the ground and access. We confirm the price before work."),
        ],
        "final_cta": "Let's get your fence <em>straight again</em>",
        "final_cta_text": "Send photos or call us.<br>We tell you whether a repair is enough and give the price before work.",
    },
}

# ---------------------------------------------------------------- storm or vehicle damage
PROBLEMS["damaged_fence"] = {
    "et": {
        "name": "Kahjustatud aia remont", "hero": "luxaed-w-van", "og": "/img/luxaed-w-van.jpg",
        "title": "Aed sai tormis või auto löögist kahjustada? Mida teha — LuxAed",
        "desc": "Torm, mahakukkunud puu või auto lõhkus aia või värava? Mida teha kohe, kuidas kahju dokumenteerida ja kes selle hüvitab. Remont Tallinnas ja Harjumaal.",
        "kicker": "Remont · kahjustused", "h1": "Aed sai tormis<br><em>või auto löögist kahjustada?</em>",
        "hero_prompt": "Aed sai kannatada?",
        "lead": "Kõigepealt ohutus ja fotod, siis remont. Selgitame, mida teha kohe pärast kahjustust ja kuidas saada kirjalik remondipakkumine, mille saate edastada kindlustusele.",
        "answer": ("Tagage ohutus, pildistage kahjustus ja teavitage kindlustust. Siis küsige remondipakkumine.",
                   "Lülitage automaatvärava toide välja ja ärge liigutage kõverdunud väravat. Kui kahju tekitas teadaolev sõiduk, hüvitab selle üldjuhul sõiduki liikluskindlustus. Kui sõiduk jäi tuvastamata, saab pöörduda Liikluskindlustuse Fondi poole. Tormikahju puhul vaadake oma kodukindlustuse tingimusi."),
        "checks_tag": "Esimesed sammud",
        "checks_h": "Mida teha kohe pärast kahjustust",
        "checks_lead": "Need sammud hoiavad teid ohutuna ja lihtsustavad hüvitise taotlemist.",
        "checks": [
            ("Ohutus", "Lülitage automaatvärava toide kilbist välja. Ärge liigutage kõverdunud väravat ega katsuge katkiste võrkude teravaid servi."),
            ("Fotod", "Pildistage kahjustus kaugelt ja lähedalt, ka sõiduki jäljed, mahakukkunud puu või muu põhjus. Pange kirja kuupäev ja kellaaeg."),
            ("Sõiduk", "Kui juht on teada, vahetage kontaktid ja kindlustuse andmed. Kui juht lahkus, teavitage politseid ja pöörduge Liikluskindlustuse Fondi poole."),
            ("Kindlustus", "Teavitage kindlustusandjat. Küsige meilt kirjalik remondipakkumine, mille saate kahjukäsitlusele edastada."),
        ],
        "intro_h": "Mida kahjustatud aiaga teeme",
        "intro_p": "Vaatame kahjustuse üle, selgitame, mida saab parandada ja mida tuleb vahetada, ning koostame kirjaliku pakkumise. Seejärel teeme remondi: vahetame sektsioonid ja postid ning seadistame värava ja automaatika uuesti.",
        "bens": ["Kahjustuse ülevaatus ja fotod", "Kirjalik remondipakkumine", "Sektsioonide ja postide vahetus", "Värava sirgendamine või vahetus", "Automaatika kontroll pärast lööki", "Vana materjali äravedu kokkuleppel"],
        "variants_tag": "Tüüpilised kahjustused",
        "variants_h": "Mis kõige sagedamini katki läheb",
        "variants": [
            ("▥", "Postid", "Löögist või tormist kõverdunud või alusest lahti tulnud postid."),
            ("▤", "Sektsioonid", "Paindunud paneelid, rebenenud võrk, murdunud lauad või plekid."),
            ("⇄", "Värav", "Kõverdunud raam, vigastatud rullikud, hinged või lukk."),
            ("⚙", "Automaatika", "Löögi saanud ajam, fotoelemendid või juhtplokk."),
        ],
        "cta_band": "Aed sai kannatada? Saatke fotod",
        "local_h": "Kahjustatud aedade remont Tallinnas ja Harjumaal",
        "local_p": "Tuleme kohale Tallinnas ja kogu Harjumaal. Fotode põhjal anname esmase hinnangu, ülevaatuse järel kirjaliku pakkumise.",
        "incl": ["Kahjustuse ülevaatus", "Kirjalik pakkumine tööde ja materjalidega", "Kokkulepitud remont või vahetus", "Värava ja automaatika kontroll pärast remonti"],
        "factors": ["Kahjustuse ulatus", "Aia ja värava tüüp", "Sektsioonide ja postide vahetuse vajadus", "Automaatika kahjustused", "Ligipääs ja äravedu"],
        "process_h": "Nii taastame kahjustatud aia",
        "process": [
            ("Saatke fotod", "Lisage päringule fotod kahjustusest ja kirjeldage, mis juhtus."),
            ("Ülevaatus", "Vaatame kahjustuse üle ja selgitame, mida saab parandada ja mida tuleb vahetada."),
            ("Kirjalik pakkumine", "Koostame pakkumise, kus on kirjas tööd ja materjalid. Selle saate edastada kindlustusele."),
            ("Remont", "Vahetame kahjustatud osad ning kontrollime aeda, väravat ja automaatikat."),
        ],
        "gallery_h": "Remonditööd ja valmis aiad",
        "gallery": [("luxaed-w-van", "LuxAed objektil"), ("luxaed-repair-real-v1", "Vana betoonposti eemaldamine"), ("luxaed-w-mesh-2", "Roheline 3D-võrkaed"), ("luxaed-w-crew", "Meister objektil")],
        "video": ("luxaed-reel-remont", "Vana betoonposti eemaldamine"), "video_h": "Vaata remonditööd objektil",
        "faq": [
            ("Kes maksab, kui auto sõitis vastu aeda?", "Kui sõiduk on teada, hüvitab kahju üldjuhul selle sõiduki liikluskindlustus. Kui sõiduk jäi tuvastamata, saab pöörduda Liikluskindlustuse Fondi poole, kes võib rakendada kuni 150 € omavastutust. Kui aia omanik sõitis oma aeda ise, liikluskindlustus seda kahju ei hüvita."),
            ("Kas kodukindlustus katab tormis kahjustatud aia?", "See sõltub teie kindlustuslepingust ja sellest, kas krundil olevad rajatised on kindlustatud. Küsige oma kindlustusandjalt ning lisage taotlusele fotod ja remondipakkumine."),
            ("Kas koostate pakkumise kindlustuse jaoks?", "Jah. Pärast ülevaatust koostame kirjaliku pakkumise, kus on kirjas tööd ja materjalid. Selle saate edastada kindlustusandjale."),
            ("Kas kõverdunud värava saab sirgeks teha?", "Mõnikord. Kergelt paindunud raami saab sirgendada ja tugevdada. Kui raam on murdunud või keevisõmblused lahti, on uus tiib või värav sageli kindlam lahendus."),
            ("Kui palju maksab kahjustatud aia remont?", "Remondi ja diagnostika hind algab 90 eurost: väljasõit ja esmane diagnostika. Detailid ja töö lisanduvad vastavalt kahjustusele. Kirjaliku pakkumise saate enne tööd."),
        ],
        "sources": [("Liikluskindlustuse Fond: LKF-i hüvitatav kahju", LKF_URL)],
        "final_cta": "Taastame aia pärast <em>tormi või lööki</em>",
        "final_cta_text": "Saatke fotod või helistage.<br>Vaatame kahjustuse üle ja koostame kirjaliku pakkumise.",
    },
    "ru": {
        "name": "Ремонт повреждённого забора", "hero": "luxaed-w-van", "og": "/img/luxaed-w-van.jpg",
        "title": "Забор повредило бурей или машиной: что делать — LuxAed",
        "desc": "Буря, упавшее дерево или машина сломали забор или ворота? Что сделать сразу, как задокументировать ущерб и кто его возмещает. Ремонт в Таллинне и Харьюмаа.",
        "kicker": "Ремонт · повреждения", "h1": "Забор повредило<br><em>бурей или машиной?</em>",
        "hero_prompt": "Привет! Забор пострадал?",
        "lead": "Сначала безопасность и фото, потом ремонт. Рассказываем, что сделать сразу после повреждения и как получить письменное предложение на ремонт, которое можно передать страховщику.",
        "answer": ("Обеспечьте безопасность, сфотографируйте повреждения и сообщите страховщику. Затем запросите предложение на ремонт.",
                   "Отключите питание автоматических ворот и не двигайте погнутые ворота. Если известно, какая машина причинила ущерб, его обычно возмещает обязательная автостраховка этой машины (liikluskindlustus). Если машину не установили, можно обратиться в Liikluskindlustuse Fond. При ущербе от бури проверьте условия своей страховки дома."),
        "checks_tag": "Первые шаги",
        "checks_h": "Что сделать сразу после повреждения",
        "checks_lead": "Эти шаги важны и для безопасности, и для получения возмещения.",
        "checks": [
            ("Безопасность", "Отключите питание автоматических ворот в щитке. Не двигайте погнутые ворота и не трогайте острые края порванной сетки."),
            ("Фото", "Сфотографируйте повреждения издалека и вблизи, следы машины, упавшее дерево или другую причину. Запишите дату и время."),
            ("Автомобиль", "Если водитель известен, обменяйтесь контактами и данными страховки. Если водитель уехал, сообщите в полицию и обратитесь в Liikluskindlustuse Fond."),
            ("Страховка", "Сообщите страховщику. Попросите у нас письменное предложение на ремонт, чтобы приложить его к заявлению о возмещении."),
        ],
        "intro_h": "Что делаем с повреждённым забором",
        "intro_p": "Осматриваем повреждения, объясняем, что можно починить, а что придётся заменить, и готовим письменное предложение. Затем ремонтируем: меняем секции и столбы, заново настраиваем ворота и автоматику.",
        "bens": ["Осмотр и фото повреждений", "Письменное предложение на ремонт", "Замена секций и столбов", "Правка или замена ворот", "Проверка автоматики после удара", "Вывоз старого материала по договорённости"],
        "variants_tag": "Типичные повреждения",
        "variants_h": "Что ломается чаще всего",
        "variants": [
            ("▥", "Столбы", "Погнутые ударом или бурей, вырванные из основания столбы."),
            ("▤", "Секции", "Погнутые панели, порванная сетка, сломанные доски или листы."),
            ("⇄", "Ворота", "Погнутая рама, повреждённые ролики, петли или замок."),
            ("⚙", "Автоматика", "Привод, фотоэлементы или блок управления после удара."),
        ],
        "cta_band": "Забор пострадал? Пришлите фото",
        "local_h": "Ремонт повреждённых заборов в Таллинне и Харьюмаа",
        "local_p": "Выезжаем по Таллинну и всему Харьюмаа. По фото даём первичную оценку, после осмотра готовим письменное предложение.",
        "incl": ["Осмотр повреждений", "Письменное предложение с работами и материалами", "Согласованный ремонт или замена", "Проверка ворот и автоматики после ремонта"],
        "factors": ["Объём повреждений", "Тип забора и ворот", "Нужна ли замена секций и столбов", "Повреждения автоматики", "Доступ и вывоз"],
        "process_h": "Как мы восстанавливаем повреждённый забор",
        "process": [
            ("Пришлите фото", "Приложите к заявке фото повреждений и опишите, что произошло."),
            ("Осмотр", "Осматриваем повреждения и объясняем, что можно починить, а что нужно заменить."),
            ("Письменное предложение", "Готовим предложение с работами и материалами. Его можно передать страховщику."),
            ("Ремонт", "Меняем повреждённые детали и проверяем забор, ворота и автоматику."),
        ],
        "gallery_h": "Ремонтные работы и готовые заборы",
        "gallery": [("luxaed-w-van", "LuxAed на объекте"), ("luxaed-repair-real-v1", "Демонтаж старого бетонного столба"), ("luxaed-w-mesh-2", "Зелёный 3D-забор"), ("luxaed-w-crew", "Мастер на объекте")],
        "video": ("luxaed-reel-remont", "Демонтаж старого бетонного столба"), "video_h": "Посмотрите ремонтные работы на объекте",
        "faq": [
            ("Кто платит, если в забор въехала машина?", "Если виновник установлен, ущерб обычно возмещает обязательная автостраховка его автомобиля. Если машину не установили, можно обратиться в Liikluskindlustuse Fond, который может применить франшизу до 150 €. Если владелец забора сам въехал в свой забор, автостраховка этот ущерб не возмещает."),
            ("Покрывает ли страховка дома забор, повреждённый бурей?", "Это зависит от вашего договора и от того, застрахованы ли сооружения на участке. Уточните у своего страховщика и приложите к заявлению фото и предложение на ремонт."),
            ("Вы готовите предложение для страховой?", "Да. После осмотра готовим письменное предложение с перечнем работ и материалов. Его можно передать страховщику."),
            ("Можно ли выправить погнутые ворота?", "Иногда. Слегка погнутую раму можно выправить и усилить. Если рама сломана или разошлись сварные швы, новая створка или ворота часто надёжнее."),
            ("Сколько стоит ремонт повреждённого забора?", "Ремонт и диагностика от 90 €: выезд и первичная диагностика. Детали и работа добавляются в зависимости от повреждений. Письменное предложение вы получите до начала работ."),
        ],
        "sources": [("Liikluskindlustuse Fond: какой ущерб возмещает LKF (на эстонском)", LKF_URL)],
        "final_cta": "Восстановим забор после <em>бури или удара</em>",
        "final_cta_text": "Пришлите фото или позвоните.<br>Осмотрим повреждения и подготовим письменное предложение.",
    },
    "en": {
        "name": "Damaged fence repair", "hero": "luxaed-w-van", "og": "/img/luxaed-w-van.jpg",
        "title": "Fence damaged by a storm or car? What to do — LuxAed",
        "desc": "A storm, fallen tree or car damaged your fence or gate? What to do straight away, how to record the damage and who pays for it. Repairs in Tallinn and Harju County.",
        "kicker": "Repair · damage", "h1": "Fence damaged by<br><em>a storm or car?</em>",
        "hero_prompt": "Hey! Fence damaged?",
        "lead": "Safety and photos first, then the repair. Here is what to do right after the damage and how to get a written repair quote you can pass on to your insurer.",
        "answer": ("Make it safe, photograph the damage and notify your insurer. Then ask for a repair quote.",
                   "Switch off the power to an automatic gate and do not move a bent gate. If a known vehicle caused the damage, that vehicle's compulsory motor insurance (liikluskindlustus) normally covers it. If the vehicle was not identified, you can turn to the Estonian Traffic Insurance Fund (Liikluskindlustuse Fond). For storm damage, check the terms of your home insurance."),
        "checks_tag": "First steps",
        "checks_h": "What to do right after the damage",
        "checks_lead": "These steps matter both for safety and for claiming compensation.",
        "checks": [
            ("Safety", "Switch off the power to an automatic gate at the panel. Do not move a bent gate or touch the sharp edges of torn mesh."),
            ("Photos", "Photograph the damage from a distance and close up, including vehicle marks, a fallen tree or any other cause. Note the date and time."),
            ("Vehicle", "If the driver is known, exchange contact and insurance details. If the driver left, report it to the police and contact the Traffic Insurance Fund."),
            ("Insurance", "Notify your insurer. Ask us for a written repair quote that you can pass on with your claim."),
        ],
        "intro_h": "What we do with a damaged fence",
        "intro_p": "We inspect the damage, explain what can be repaired and what must be replaced, and prepare a written quote. Then we carry out the repair: replacing sections and posts and resetting the gate and automation.",
        "bens": ["Damage inspection and photos", "Written repair quote", "Section and post replacement", "Gate straightening or replacement", "Automation check after an impact", "Removal of old materials if agreed"],
        "variants_tag": "Typical damage",
        "variants_h": "What breaks most often",
        "variants": [
            ("▥", "Posts", "Posts bent by an impact or storm, or pulled loose from their base."),
            ("▤", "Sections", "Bent panels, torn mesh, broken boards or sheets."),
            ("⇄", "Gate", "A bent frame or damaged rollers, hinges or lock."),
            ("⚙", "Automation", "A drive, photocells or control board hit in the impact."),
        ],
        "cta_band": "Fence damaged? Send us photos",
        "local_h": "Damaged fence repair in Tallinn and Harju County",
        "local_p": "We come out across Tallinn and Harju County. We give an initial estimate from photos and a written quote after the inspection.",
        "incl": ["Damage inspection", "Written quote listing work and materials", "Agreed repair or replacement", "Gate and automation check after repair"],
        "factors": ["Extent of the damage", "Fence and gate type", "Whether sections and posts need replacing", "Damage to the automation", "Access and removal"],
        "process_h": "How we restore a damaged fence",
        "process": [
            ("Send photos", "Add photos of the damage to your enquiry and tell us what happened."),
            ("Inspection", "We inspect the damage and explain what can be repaired and what must be replaced."),
            ("Written quote", "We prepare a quote listing the work and materials. You can pass it on to your insurer."),
            ("Repair", "We replace the damaged parts and check the fence, gate and automation."),
        ],
        "gallery_h": "Repair work and finished fences",
        "gallery": [("luxaed-w-van", "LuxAed on site"), ("luxaed-repair-real-v1", "Removing an old concrete post"), ("luxaed-w-mesh-2", "Green 3D mesh fence"), ("luxaed-w-crew", "Our craftsman on site")],
        "video": ("luxaed-reel-remont", "Removing an old concrete post"), "video_h": "Watch repair work on site",
        "faq": [
            ("Who pays if a car hit my fence?", "If the vehicle is known, its compulsory motor insurance normally covers the damage. If it was not identified, you can turn to the Traffic Insurance Fund (LKF), which may apply a deductible of up to €150. If you drove into your own fence, motor insurance does not cover it."),
            ("Does home insurance cover a fence damaged in a storm?", "It depends on your policy and whether structures on the plot are insured. Ask your insurer and include photos and the repair quote with your claim."),
            ("Do you prepare a quote for the insurer?", "Yes. After the inspection we prepare a written quote listing the work and materials. You can pass it on to your insurer."),
            ("Can a bent gate be straightened?", "Sometimes. A slightly bent frame can be straightened and reinforced. If the frame is broken or the welds have split, a new leaf or gate is often the safer option."),
            ("How much does damaged fence repair cost?", "Repair and diagnostics start from €90 for the call-out and initial diagnosis. Parts and labour are added according to the damage. You receive a written quote before work."),
        ],
        "sources": [("Estonian Traffic Insurance Fund (LKF): damage it compensates, in Estonian", LKF_URL)],
        "final_cta": "Let's restore your fence after <em>a storm or impact</em>",
        "final_cta_text": "Send photos or call us.<br>We inspect the damage and prepare a written quote.",
    },
}

PROBLEM_ORDER = [("gate_wont_open", GATE_WONT_OPEN), ("sliding_gate", SLIDING_GATE),
                 ("leaning_fence", LEANING_FENCE), ("damaged_fence", DAMAGED_FENCE)]


# Topic-related links for the "Vaata ka" block on each problem page.
_SERVICE_LINKS = {
    "gates": {"et": ("/varavad/", "Väravad ja automaatika"), "ru": ("/ru/vorota-avtomatika/", "Ворота, калитки и автоматика"), "en": ("/en/gates-automation/", "Gates & automation")},
    "intercom": {"et": ("/varavad/domofonid/", "Domofonid ja videodomofonid"), "ru": ("/ru/domofony-videodomofony/", "Домофоны и видеодомофоны"), "en": ("/en/intercoms-video-intercoms/", "Intercoms & video intercoms")},
    "panel_mesh": {"et": ("/aiad/paneelaed/", "3D paneelaed"), "ru": ("/ru/zabory/2d-3d-setka/", "Сварные 2D/3D-сетки"), "en": ("/en/fences/mesh/", "Welded 2D/3D mesh")},
    "wood": {"et": ("/aiad/puitaed/", "Puitaed"), "ru": ("/ru/zabory/derevyannye/", "Деревянные заборы"), "en": ("/en/fences/wooden/", "Wooden fences")},
    "repair": {"et": ("/aia-remont/", "Aia ja värava remont"), "ru": ("/ru/remont-zaborov/", "Ремонт заборов и ворот"), "en": ("/en/fence-repair/", "Fence & gate repair")},
}
_RELATED = {
    "gate_wont_open": [("problem", "sliding_gate"), ("guide", "gate_safety"), ("service", "gates"), ("service", "intercom")],
    "sliding_gate": [("problem", "gate_wont_open"), ("guide", "gate_safety"), ("service", "gates"), ("guide", "gate_guide")],
    "leaning_fence": [("problem", "damaged_fence"), ("service", "panel_mesh"), ("service", "wood")],
    "damaged_fence": [("problem", "leaning_fence"), ("service", "repair"), ("service", "panel_mesh")],
}


def _related_links(key, lang):
    out = []
    for kind, target in _RELATED[key]:
        if kind == "service":
            out.append(_SERVICE_LINKS[target][lang])
        else:
            out.append((_CARD_PATHS[target][lang], _CARD_COPY[lang][target][0]))
    return out


def problem_page(key, lang):
    row = dict(PROBLEM_ORDER)[key]
    page = _base(lang, row, key)
    page.update(PROBLEMS[key][lang])
    page["related"] = _related_links(key, lang)
    return page


# ------------------------------------------------------------ link cards on existing pages
_CARD_COPY = {
    "et": {
        "gate_wont_open": ("Värav ei avane või ei sulgu", "Toide, pult, fotoelemendid ja talv."),
        "sliding_gate": ("Liugvärav jookseb kinni", "Rullikud, kandurid ja vajunud alus."),
        "leaning_fence": ("Aed on viltu või post logiseb", "Külmakerge, tuul ja mädanenud postid."),
        "damaged_fence": ("Aed sai tormis või auto löögist kahjustada", "Ohutus, fotod ja kindlustus."),
        "gate_guide": ("Liugvärav või tiibvärav?", "Ruum, talv, automaatika ja hind."),
        "permit_guide": ("Kas aia ehitamiseks on vaja luba?", "Ehitusteatis, vald ja naaber."),
    },
    "ru": {
        "gate_wont_open": ("Не открываются или не закрываются ворота", "Питание, пульт, фотоэлементы и зима."),
        "sliding_gate": ("Заедают откатные ворота", "Ролики, каретки и просевшее основание."),
        "leaning_fence": ("Покосился забор или шатается столб", "Пучение, ветер и сгнившие столбы."),
        "damaged_fence": ("Забор повредило бурей или машиной", "Безопасность, фото и страховка."),
        "gate_guide": ("Откатные или распашные ворота?", "Место, зима, автоматика и цена."),
        "permit_guide": ("Нужно ли разрешение на забор?", "Уведомление (ehitusteatis), волость и сосед."),
    },
    "en": {
        "gate_wont_open": ("Gate won't open or close", "Power, remote, photocells and winter."),
        "sliding_gate": ("Sliding gate sticking", "Rollers, carriages and a settled base."),
        "leaning_fence": ("Leaning fence or loose post", "Frost heave, wind and rotten posts."),
        "damaged_fence": ("Fence damaged by a storm or car", "Safety, photos and insurance."),
        "gate_guide": ("Sliding or swing gate?", "Space, winter, automation and price."),
        "permit_guide": ("Do you need a permit for a fence?", "Building notice, municipality and neighbours."),
    },
}

_CARD_PATHS = {"gate_wont_open": GATE_WONT_OPEN, "sliding_gate": SLIDING_GATE,
               "leaning_fence": LEANING_FENCE, "damaged_fence": DAMAGED_FENCE,
               "gate_guide": GATE_GUIDE, "permit_guide": PERMIT_GUIDE, "hub": HUB_ROW}
_CARD_PATHS.update(ARTICLES)
_ARTICLE_CARDS = {
    "et": {"panel_vs_mesh": ("Võrkaed või 3D paneelaed?", "Hind, jäikus, koer ja kalle."),
           "privacy_fence": ("Kinnine aed: plekk-, puit- või lippaed?", "Hind, tuul, hooldus ja reeglid."),
           "neighbour": ("Aed naabri piiril", "Seadus, piirimärgid ja kulud."),
           "road_utilities": ("Aed tee kaitsevööndis ja trasside lähedal", "Kaitsevööndid ja trassid enne puurimist."),
           "mistakes": ("Levinud vead aia ehitamisel", "Mida teised hiljem kahetsevad."),
           "contractor": ("Kuidas valida aiafirmat", "Küsimused enne lepingut."),
           "municipal_rules": ("Lubatud aia kõrgus Harjumaal", "Kõrgus ja läbipaistvus valdade kaupa."),
           "gate_safety": ("Automaatvärava ohutus", "CE-märgis, elektritööd ja hooldus."),
           "hub": ("Kõik nõuanded", "Juhendid enne aia ja värava tellimist.")},
    "ru": {"panel_vs_mesh": ("Сетка-рабица или 3D-панели?", "Цена, жёсткость, собака и склон."),
           "privacy_fence": ("Глухой забор: профнастил, дерево или штакетник?", "Цена, ветер, уход и правила."),
           "neighbour": ("Забор между соседями", "Закон, межевые знаки и расходы."),
           "road_utilities": ("Забор у дороги и коммуникаций", "Охранные зоны и поиск сетей до бурения."),
           "mistakes": ("Частые ошибки при установке забора", "О чём потом жалеют."),
           "contractor": ("Как выбрать фирму для забора", "Вопросы до договора."),
           "municipal_rules": ("Высота забора в Харьюмаа", "Высота и прозрачность по волостям."),
           "gate_safety": ("Безопасность автоматических ворот", "CE, электромонтаж и обслуживание."),
           "hub": ("Все советы", "Статьи перед заказом забора и ворот.")},
    "en": {"panel_vs_mesh": ("Chain-link or 3D mesh panels?", "Price, stiffness, dogs and slopes."),
           "privacy_fence": ("Privacy fence: sheet, timber or picket?", "Price, wind, upkeep and rules."),
           "neighbour": ("A boundary fence with your neighbour", "The law, markers and costs."),
           "road_utilities": ("Fences near roads and utilities", "Protection zones and finding utilities before drilling."),
           "mistakes": ("Common fence-building mistakes", "What people regret later."),
           "contractor": ("How to choose a fence contractor", "Questions before you sign."),
           "municipal_rules": ("Fence height rules in Harju County", "Height and transparency by municipality."),
           "gate_safety": ("Automatic gate safety", "CE marking, wiring and maintenance."),
           "hub": ("All guides", "Reading before you order a fence or gate.")},
}
for _lang in ("et", "ru", "en"):
    _CARD_COPY[_lang].update(_ARTICLE_CARDS[_lang])

_HEADINGS = {
    "repair": {"et": ("Levinud mured", "Mis teie aia või väravaga juhtus?"),
               "ru": ("Частые проблемы", "Что случилось с вашим забором или воротами?"),
               "en": ("Common problems", "What happened to your fence or gate?")},
    "gates": {"et": ("Enne tellimist", "Kasulik lugeda väravate kohta"),
              "ru": ("Перед заказом", "Полезно знать о воротах"),
              "en": ("Before you order", "Useful reading about gates")},
    "fences": {"et": ("Enne tellimist", "Kasulik lugeda enne aia tellimist"),
               "ru": ("Перед заказом", "Полезно прочитать перед заказом забора"),
               "en": ("Before you order", "Useful reading before you order a fence")},
    "guides": {"et": ("Loe edasi", "Kasulikud juhendid"),
               "ru": ("Читайте также", "Полезные статьи"),
               "en": ("Read next", "Useful guides")},
}


def link_cards(kind, lang, keys):
    tag, heading = _HEADINGS[kind][lang]
    cards = [(_CARD_PATHS[k][lang],) + _CARD_COPY[lang][k] for k in keys]
    return tag, heading, cards


# Existing pages that get a small link section near the bottom.
HUB_LINKS = {}
for _lang in ("et", "ru", "en"):
    HUB_LINKS[REPAIR_HUB[_lang]] = link_cards("repair", _lang, ["gate_wont_open", "sliding_gate", "leaning_fence", "damaged_fence"])
    HUB_LINKS[GATES_HUB[_lang]] = link_cards("gates", _lang, ["gate_guide", "gate_safety", "gate_wont_open", "sliding_gate"])

# Fence service pages: three buyer articles each, picked by what that fence buyer asks next.
_FENCE_READING = {
    "wood": ["privacy_fence", "municipal_rules", "permit_guide"],
    "roll_mesh": ["panel_vs_mesh", "neighbour", "road_utilities"],
    "panel_mesh": ["panel_vs_mesh", "municipal_rules", "road_utilities"],
    "steel_picket": ["privacy_fence", "municipal_rules", "mistakes"],
    "bar_metal": ["municipal_rules", "permit_guide", "contractor"],
    "profiled_sheet": ["privacy_fence", "municipal_rules", "mistakes"],
}


def _fence_links():
    from service_catalog import SERVICE_MATRIX
    for service in SERVICE_MATRIX:
        keys = _FENCE_READING.get(service.get("key"))
        if keys:
            for lang in ("et", "ru", "en"):
                HUB_LINKS[service[lang]["path"]] = link_cards("fences", lang, keys)


_fence_links()
