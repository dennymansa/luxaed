#!/usr/bin/env python3
"""Two buyer guides in ET, RU and EN, built on the same template as /kuidas-valida-aeda/:
fence permits and neighbours, and sliding versus swing gates.

Legal statements quote official sources (Riigi Teataja, Harku vald, Tallinn),
checked on 27.09.2026. Prices repeat the published /hinnad/ ranges.
"""

from guide_pages import HOME, PATHS, faq_html, hero, page
from problem_content import GATE_GUIDE, GATES_HUB, PERMIT_GUIDE, SLIDING_GATE, GATE_WONT_OPEN, ARTICLES, link_cards
from service_layout import _types
from article_content import DATE, HUB_NAME
from problem_content import HUB_ROW

SHORT = {"permit": {"et": "Aia ehitusteatis", "ru": "Разрешение на забор", "en": "Fence permits"},
         "gates": {"et": "Liugvärav või tiibvärav", "ru": "Откатные или распашные ворота", "en": "Sliding or swing gate"}}


def _article(h1, image):
    import re
    headline = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h1)).strip()
    return {"headline": headline, "published": DATE, "modified": DATE, "image": f"/img/{image}.jpg"}

EHS_LISA1 = "https://www.riigiteataja.ee/aktilisa/1110/7202/6032/EhS_17062026_lisa1.pdf"
AOS = "https://www.riigiteataja.ee/akt/128012026007?leiaKehtiv"
MUKS = "https://www.riigiteataja.ee/akt/112072025020?leiaKehtiv"
HARKU = "https://www.harku.ee/ehitus-planeerimine-ja-taristu/ehitamine-ja-muud-seonduvad-tegevused/rajatised"
TALLINN = "https://www.tallinn.ee/et/ehitus/piirdeaiad-hoovialad-ja-haljastus"
EHR = "https://www.ehr.ee"


def _a(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


def _cards(items, cls="answer-grid answer-grid--2"):
    return f'<div class="{cls}">' + "".join(
        f'<article class="answer-card"><h3>{title}</h3><p>{text}</p></article>' for title, text in items) + '</div>'


def _link_cards(tag, heading, cards):
    items = "".join(
        f'<a class="svc-card help-card" href="{href}"><div class="ic">→</div><h3>{title}</h3><p>{text}</p></a>'
        for href, title, text in cards)
    return (f'<section class="section help-links"><div class="wrap"><span class="tag">{tag}</span>'
            f'<h2 class="big">{heading}</h2><div class="svc-cards help-cards">{items}</div></div></section>')


def _table(headers, rows):
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(
        (f'<th scope="row">{x}</th>' if i == 0 else f"<td>{x}</td>") for i, x in enumerate(row)) + "</tr>" for row in rows)
    return (f'<div class="price-table-wrap"><table class="price-table comparison-table"><thead><tr>{head}</tr></thead>'
            f'<tbody>{body}</tbody></table></div>')


def _cta(h2, text, href, button):
    return (f'<section class="cta-final"><div class="wrap"><h2>{h2}</h2><p>{text}</p>'
            f'<div class="hero-btns"><a class="btn btn-accent" href="{href}">{button} →</a></div></div></section>')


# ------------------------------------------------------------------ permit guide
PERMIT = {
    "et": {
        "title": "Kas aia ehitamiseks on vaja luba? Ehitusteatis 2026 — LuxAed",
        "desc": "Aed või värav, mille ehitamisel kaevatakse sügavamale kui 30 cm, vajab ehitusteatist ja ehitusprojekti. Mida nõuab seadus, mida vald ja mida leppida kokku naabriga.",
        "advice_tag": "Meie soovitus", "advice_h": "Mis on tegelikult oluline",
        "advice": [("Esmalt teatis, siis materjal", "Esitage ehitusteatis enne materjali tellimist. Kui vald küsib täiendusi, ei jää tellitud paneelid ootele."), ("Piir enne poste", "Kõige kallim viga on aed, mis jääb paar sentimeetrit naabri maale. Kui piirimärke pole näha, laske maamõõtjal piir taastada."), ("Planeering enne aiatüüpi", "Detailplaneering võib keelata kinnise plankaia või piirata kõrgust. Kontrollige see üle enne, kui aiatüübi valite."), ("Naabriga kirjalikult", "Lühike kiri asukoha, kõrguse ja kulude jagamise kohta hoiab ära hilisema vaidluse.")],
        "neighbour_more": f"Kulude jagamisest, piirimärkidest ja kirjalikust kokkuleppest loe lähemalt: <a href=\"{ARTICLES['neighbour']['et']}\">aed naabri piiril</a>.",
        "kicker": "Juhend · luba ja naaber", "h1": "Kas aia ehitamiseks<br><em>on vaja luba?</em>",
        "lead": "Lühidalt: enamasti on vaja ehitusteatist. Allpool selgitame, mida ütleb ehitusseadustik, milliseid lisatingimusi võib seada vald ja mida teha, kui aed tuleb naabriga ühisele piirile.",
        "direct_tag": "Lühivastus",
        "direct_h": "Kui uue aia või värava ehitamisel kaevatakse sügavamale kui 30 cm, on vaja ehitusteatist ja ehitusprojekti.",
        "direct_p": "Nii ütleb ehitusseadustiku lisa 1, mis kehtib alates 01.08.2026. Tavaline aed, mille postid betoneeritakse maasse, tähendab praktikas sügavamaid kaevetöid, seega arvestage ehitusteatisega. Aia ümberehitamine ja üksiku osa asendamine samaväärsega teatist ei vaja, laiendamine ja lammutamine vajavad. Kui vana aed lammutatakse ja asemele tuleb olemuslikult uus aed, on see lammutamine ja uue aia püstitamine.",
        "law_tag": "Ehitusseadustik", "law_h": "Mida seadus nõuab",
        "law_headers": ("Tegevus", "Mida on vaja"),
        "law_rows": [
            ("Uue aia või värava püstitamine, kui kaevetööd on sügavamal kui 30 cm", "Ehitusteatis ja ehitusprojekt"),
            ("Aia laiendamine", "Ehitusteatis"),
            ("Aia ümberehitamine (rekonstrueerimine)", "Ei ole vaja"),
            ("Üksiku osa asendamine samaväärsega", "Ei ole vaja"),
            ("Aia lammutamine", "Ehitusteatis"),
        ],
        "law_note": f"Allikas: {_a(EHS_LISA1, 'ehitusseadustiku lisa 1')} (kehtib alates 01.08.2026), rida „Piirdeaed või värav, mille ehitamisega kaasnevad kaevetööd sügavamal kui 30 cm”; kõik read kehtivad just sellise aia või värava kohta. Vald võib põhjendatud juhul nõuda ehitusteatist ka ehitise kohta, mida lisas 1 ei ole (ehitusseadustik § 35 lg 4). Kui aeda paigaldatakse ilma kaevetöödeta, küsige oma vallast.",
        "more_tag": "Vald ja planeering", "more_h": "Millega veel arvestada",
        "more_cards": [
            ("Planeering võib seada kõrguse ja materjali", "Detailplaneering või valla planeering võib määrata aia kõrguse, materjali ja läbipaistvuse. Harku valla teemaplaneeringu järgi ei tohi üksik-, kaksik- või ridaelamu võrkaed ega osaliselt läbipaistev puitaed olla kõrgem kui 1,5 meetrit ning läbipaistmatud plankaiad on keelatud, v.a müratõkkena või tööstusala ümber."),
            ("Kaugus tee servast", "Harku vallas peab aed asuma vähemalt 2 meetri kaugusel teekatte servast, kui krundi piir jääb teele lähemale. Nii jääb ruumi lumekoristuseks."),
            ("Tallinna miljööalad", "Tallinna miljööväärtuslikel aladel soovitab linn tänavaäärse aia kõrguseks üldjuhul 1,2–1,5 m, plankaiale 1,5–1,8 m. Võrk- ja keevispaneelaed ei ole seal linna hinnangul sobiv. Erandina võib seda kaaluda kinnistute vahel, mitte tänava poolel, kui võrk jääb tiheda heki või ronitaimede taha. Linn otsustab iga juhtumi puhul eraldi."),
            ("Maa-alused trassid", "Enne postiaukude puurimist selgitage välja kaablite ja torude asukoht. Nii ei jää aed trassi peale ega kahjusta tehnovõrke."),
            ("Mälestise kaitsevöönd", "Kinnismälestise või muinsuskaitseala kaitsevööndis kooskõlastab vald ehitusteatise Muinsuskaitseametiga. Kui teatist pole vaja, tuleb ametit teavitada vähemalt 10 päeva enne tööde algust. Mälestisel endal ja muinsuskaitsealal on ehitamiseks vaja ameti luba."),
        ],
        "more_note": f"Allikad: {_a(HARKU, 'Harku vald, rajatised')} (uuendatud 30.03.2026), {_a(TALLINN, 'Tallinn, piirdeaiad miljööaladel')} (uuendatud 11.04.2024) ja {_a(MUKS, 'muinsuskaitseseadus')} §§ 52, 58–59. Teiste Harjumaa valdade nõuded on koondatud juhendisse <a href=\"{ARTICLES['municipal_rules']['et']}\">aia kõrgus Harjumaa valdades</a>.",
        "neighbour_tag": "Naaber", "neighbour_h": "Aed naabriga ühisel piiril",
        "neighbour_p": "Asjaõigusseaduse § 151 järgi on kahte kinnisasja eraldav müür, hekk, kraav või muu selline asi naabrite ühiskasutuses, sõltumata sellest, kellele see kuulub. Kui seda kasutavad mõlemad naabrid, kannavad nad korrashoiukulud võrdselt. Kui asi on vajalik ühe naabri huvides, ei tohi seda tema nõusolekuta kõrvaldada ega muuta.",
        "neighbour_p2": "Praktikas: leppige asukoht, aia tüüp, kõrgus ja kulude jagamine naabriga enne tööd kirjalikult kokku. Kui piirimärgid pole kindlad, laske litsentsiga maamõõtjal piir enne postide paigaldamist taastada. Harku vald rõhutab, et kahte kinnistut eraldava aia puhul on naabritega koostöö kohustuslik.",
        "neighbour_note": f"Allikas: {_a(AOS, 'asjaõigusseadus § 151')}.",
        "how_tag": "Ehitisregister", "how_h": "Kuidas ehitusteatis esitada",
        "how_p": f"Ehitusteatis esitatakse kohalikule omavalitsusele {_a(EHR, 'ehitisregistri')} kaudu vähemalt 10 päeva enne tööde algust. Kui vald 10 päeva jooksul lisakontrolli vajadusest ei teata, võib ehitamist alustada, ja ehitusteatise alusel võib ehitada nelja aasta jooksul. Teatises märgitakse kinnistu andmed ja katastritunnus, aia kirjeldus ja asukoht krundil, koos teatisega esitatakse ehitusprojekt. Vald võib kaasata ka naaberkinnistu omaniku. Harku valla andmetel ehitusteatisel riigilõivu ei ole ja projekti asendiplaan tehakse geodeetilisele alusplaanile või mahamärkimisplaanile.",
        "how_p2": "LuxAed annab aia tehnilised andmed ja selgitab töö ulatust. Kas ametlikku projekti või teatist on vaja ja kes selle esitab, lepime kokku eraldi.",
        "faq": [
            ("Kas võrkaed vajab ehitusteatist?", "Jah, kui postide jaoks kaevatakse sügavamale kui 30 cm, näiteks puuritakse augud ja betoneeritakse. Siis on vaja ehitusteatist ja ehitusprojekti nagu igal piirdeaial. Kahtluse korral küsige oma vallast."),
            ("Kas vana aia asendamine uuega vajab teatist?", "Oleneb tööst. Üksiku osa samaväärne asendamine ja aia ümberehitamine teatist ei vaja. Kui vana aed lammutatakse ja asemele tuleb olemuslikult uus aed, on see lammutamine ja uue aia püstitamine (ehitusseadustik § 4 lg 4), mis vajab ehitusteatist ning kaevetööde korral sügavamal kui 30 cm ka ehitusprojekti."),
            ("Kas ilma kaevetöödeta paigaldatud aed vajab teatist?", "Mitte alati, sest lisa 1 nõue on seotud kaevetöödega sügavamal kui 30 cm. Vald võib siiski põhjendatud juhul teatist nõuda (ehitusseadustik § 35 lg 4), seega küsige enne tööd oma vallast."),
            ("Kui kiiresti võib pärast teatise esitamist alustada?", "Ehitusseadustiku järgi tuleb teatis esitada vähemalt 10 päeva enne tööde algust. Kui vald selle aja jooksul lisakontrolli vajadusest ei teata, võib alustada. Ehitusteatise alusel võib ehitada nelja aasta jooksul."),
            ("Kas mälestise lähedal kehtivad eraldi reeglid?", "Jah. Kinnismälestise või muinsuskaitseala kaitsevööndis kooskõlastab vald ehitusteatise Muinsuskaitseametiga. Kui teatist pole vaja, tuleb ametit teavitada vähemalt 10 päeva enne tööde algust."),
            ("Kes esitab ehitusteatise?", "Tavaliselt esitab teatise kinnistu omanik või tema esindaja ehitisregistris. LuxAed annab aia tehnilised andmed. Kes projekti ja teatise esitab, lepime kokku eraldi."),
        ],
        "disclaimer": "Kontrollitud 27.09.2026. See juhend ei ole õigusnõu: enne tööd kontrollige oma valla või linna kehtivaid nõudeid.",
        "links": ("Loe edasi", "Kasulikud juhendid", [
            (PATHS["area"]["et"], "Teenindame kogu Harjumaad", "Vallad, asulad ja tasuta mõõdistus."),
            (PATHS["choose"]["et"], "Kuidas valida aeda", "Privaatsus, tuul, hooldus ja hind."),
            (GATE_GUIDE["et"], "Liugvärav või tiibvärav?", "Ruum, talv, automaatika ja hind."),
        ]),
        "cta": ("Planeerime teie aia koos", "Mõõdistame tasuta ja anname aia tehnilised andmed teatise jaoks.", "Küsi tasuta mõõdistust"),
    },
    "ru": {
        "title": "Нужно ли разрешение на забор в Эстонии в 2026 году? — LuxAed",
        "desc": "Для забора или ворот, при установке которых копают глубже 30 см, нужны ehitusteatis и проект. Что требует закон, что добавляет волость и что согласовать с соседом.",
        "advice_tag": "Наш совет", "advice_h": "Что на самом деле важно",
        "advice": [("Сначала уведомление, потом материал", "Подайте ehitusteatis до заказа материала. Если волость попросит дополнений, вам не придётся ждать с уже купленными панелями."), ("Граница до столбов", "Дороже всего обходится забор, вставший на пару сантиметров на участок соседа. Если межевых знаков не видно, пусть землемер восстановит границу."), ("Планировка до выбора забора", "Детальная планировка может запретить глухой дощатый забор или ограничить высоту. Проверьте это до выбора типа забора."), ("С соседом письменно", "Короткое письмо о месте, высоте и разделе расходов избавит от споров потом.")],
        "neighbour_more": f"О разделе расходов, межевых знаках и письменной договорённости читайте подробнее: <a href=\"{ARTICLES['neighbour']['ru']}\">забор на границе с соседом</a>.",
        "kicker": "Руководство · разрешение и сосед", "h1": "Нужно ли разрешение<br><em>на забор?</em>",
        "lead": "Коротко: чаще всего нужно уведомление о строительстве (ehitusteatis). Здесь собрано, что говорит строительный кодекс, какие условия может добавить волость и что делать, если забор стоит на границе с соседом.",
        "direct_tag": "Короткий ответ",
        "direct_h": "Для нового забора или ворот, если при установке копают глубже 30 см, нужны уведомление о строительстве и проект.",
        "direct_p": "Так сказано в приложении 1 к строительному кодексу Эстонии (Ehitusseadustik), которое действует с 01.08.2026. Обычный забор, столбы которого бетонируют в грунт, на практике означает более глубокие земляные работы, поэтому рассчитывайте на ehitusteatis. Реконструкция и замена отдельной части равноценной уведомления не требуют, а для расширения и сноса оно нужно. Если старый забор сносят и ставят принципиально новый, это снос и строительство нового забора.",
        "law_tag": "Ehitusseadustik", "law_h": "Что требует закон",
        "law_headers": ("Действие", "Что нужно"),
        "law_rows": [
            ("Установка нового забора или ворот, если копают глубже 30 см", "Ehitusteatis и строительный проект"),
            ("Расширение забора", "Ehitusteatis"),
            ("Реконструкция (изменение) забора", "Не требуется"),
            ("Замена отдельной части на равноценную", "Не требуется"),
            ("Снос забора", "Ehitusteatis"),
        ],
        "law_note": f"Источник: {_a(EHS_LISA1, 'приложение 1 к Ehitusseadustik')} (действует с 01.08.2026), строка «Piirdeaed või värav, mille ehitamisega kaasnevad kaevetööd sügavamal kui 30 cm»; все строки относятся именно к такому забору или воротам. В обоснованном случае волость может потребовать уведомление и для сооружения, которого нет в приложении 1 (§ 35 ч. 4 Ehitusseadustik). Если забор ставят без земляных работ, уточните в своей волости.",
        "more_tag": "Волость и планировка", "more_h": "Что ещё учесть",
        "more_cards": [
            ("Планировка может задать высоту и материал", "Детальная планировка или планировка волости может задавать высоту, материал и прозрачность забора. По тематической планировке волости Харку сетчатый или частично прозрачный деревянный забор у частного, двухквартирного или рядного дома не должен быть выше 1,5 метра, а глухие дощатые заборы запрещены, кроме шумозащитных и промышленных."),
            ("Расстояние от дороги", "В волости Харку забор должен стоять не ближе 2 метров от края дорожного покрытия, если граница участка проходит ближе к дороге. Так остаётся место для уборки снега."),
            ("Исторические районы Таллинна", "В районах с ценной исторической средой (miljööala) город рекомендует уличный забор обычно высотой 1,2–1,5 м, а для дощатого 1,5–1,8 м. Сетчатые и сварные панельные заборы там, по оценке города, не подходят. В виде исключения их рассматривают между участками, но не со стороны улицы, если сетку полностью закрывает плотная живая изгородь или вьющиеся растения. Город решает в каждом случае отдельно."),
            ("Подземные коммуникации", "Перед бурением ям под столбы выясните, где проходят кабели и трубы. Так забор не окажется на трассе и не повредит сети."),
            ("Охранная зона памятника", "В охранной зоне памятника или зоны охраны старины (muinsuskaitseala) волость согласует уведомление с Департаментом охраны памятников. Если уведомление не нужно, департамент извещают не позже чем за 10 дней до работ. На самом памятнике и внутри muinsuskaitseala для строительства нужно разрешение департамента."),
        ],
        "more_note": f"Источники: {_a(HARKU, 'волость Харку, сооружения')} (обновлено 30.03.2026), {_a(TALLINN, 'Таллинн, заборы в miljööala')} (обновлено 11.04.2024) и {_a(MUKS, 'Muinsuskaitseseadus')} §§ 52, 58–59, на эстонском. Требования других волостей Харьюмаа собраны в статье <a href=\"{ARTICLES['municipal_rules']['ru']}\">высота забора в волостях Харьюмаа</a>.",
        "neighbour_tag": "Сосед", "neighbour_h": "Забор на границе с соседом",
        "neighbour_p": "По § 151 закона о вещном праве (Asjaõigusseadus) стена, живая изгородь, канава или другая подобная вещь, разделяющая два участка, находится в совместном пользовании соседей независимо от того, кому она принадлежит. Если ею пользуются оба соседа, расходы на содержание они несут поровну. Если вещь нужна в интересах одного соседа, её нельзя убрать или изменить без его согласия.",
        "neighbour_p2": "На практике: до начала работ письменно договоритесь с соседом о месте, типе, высоте забора и разделе расходов. Если межевые знаки не на месте, пусть землемер с лицензией восстановит границу до установки столбов. Волость Харку прямо указывает, что при заборе между двумя участками сотрудничество с соседями обязательно.",
        "neighbour_note": f"Источник: {_a(AOS, 'Asjaõigusseadus § 151')}, на эстонском.",
        "how_tag": "Регистр строений", "how_h": "Как подать ehitusteatis",
        "how_p": f"Уведомление подают в волость или город через {_a(EHR, 'строительный регистр (ehr.ee)')} не позже чем за 10 дней до начала работ. Если волость за 10 дней не сообщила о дополнительной проверке, можно начинать, а строить по уведомлению можно в течение четырёх лет. В уведомлении указывают данные участка и кадастровый номер, описание забора и его место на участке, вместе с уведомлением подают проект. Волость может привлечь и владельца соседнего участка. По данным волости Харку, госпошлины за ehitusteatis нет, а ситуационный план составляют на геодезической подоснове или плане разбивки.",
        "how_p2": "LuxAed даёт технические данные забора и описывает объём работ. Нужен ли официальный проект или уведомление и кто их подаёт, договариваемся отдельно.",
        "faq": [
            ("Нужен ли ehitusteatis для сетчатого забора?", "Да, если при установке столбов копают глубже 30 см, например бурят ямы и бетонируют. Тогда нужны ehitusteatis и проект, как для любого забора. Если сомневаетесь, уточните в своей волости."),
            ("Нужно ли уведомление, если меняю старый забор на новый?", "Зависит от работ. Замена отдельной части равноценной и реконструкция забора уведомления не требуют. Если старый забор сносят и ставят принципиально новый, это снос и строительство нового забора (§ 4 ч. 4 Ehitusseadustik): нужен ehitusteatis, а если копают глубже 30 см, то и проект."),
            ("Нужно ли уведомление, если забор ставят без земляных работ?", "Не всегда, потому что требование приложения 1 связано с земляными работами глубже 30 см. Но волость в обоснованном случае может потребовать уведомление (§ 35 ч. 4 Ehitusseadustik), поэтому уточните это до начала работ."),
            ("Когда можно начинать работы после подачи уведомления?", "По строительному кодексу уведомление подают не позже чем за 10 дней до начала работ. Если за это время волость не сообщила о дополнительной проверке, можно начинать. Строить по уведомлению можно в течение четырёх лет."),
            ("Есть ли особые правила рядом с памятником?", "Да. В охранной зоне памятника или muinsuskaitseala волость согласует уведомление с Департаментом охраны памятников. Если уведомление не нужно, департамент извещают не позже чем за 10 дней до начала работ."),
            ("Кто подаёт ehitusteatis?", "Обычно уведомление подаёт владелец участка или его представитель в строительном регистре. LuxAed предоставляет технические данные забора, а кто готовит проект и подаёт уведомление, договариваемся отдельно."),
        ],
        "disclaimer": "Проверено 27.09.2026. Это не юридическая консультация: перед работами уточните действующие требования в своей волости или городе.",
        "links": ("Читайте также", "Полезные статьи", [
            (PATHS["area"]["ru"], "Работаем по всему Харьюмаа", "Волости, посёлки и бесплатный замер."),
            (PATHS["choose"]["ru"], "Как выбрать забор", "Приватность, ветер, уход и цена."),
            (GATE_GUIDE["ru"], "Откатные или распашные ворота?", "Место, зима, автоматика и цена."),
        ]),
        "cta": ("Спланируем ваш забор вместе", "Бесплатно измерим участок и дадим технические данные забора для уведомления.", "Заказать бесплатный замер"),
    },
    "en": {
        "title": "Do you need a permit for a fence in Estonia? — LuxAed",
        "desc": "Digging deeper than 30 cm for a fence or gate means a building notice and a design. What the law requires, what municipalities add and what to agree with neighbours.",
        "advice_tag": "Our advice", "advice_h": "What really matters",
        "advice": [("Notice first, materials second", "File the building notice before ordering materials. If the municipality asks for more information, you are not left waiting with panels already bought."), ("Boundary before posts", "The costliest mistake is a fence that ends up a few centimetres on your neighbour's land. If you cannot see the boundary markers, have a surveyor restore them."), ("Check the plan before choosing", "A detailed plan may ban solid plank fences or limit the height. Check it before you choose the fence type."), ("Agree in writing", "A short note on position, height and cost sharing saves arguments later.")],
        "neighbour_more": f"For cost sharing, boundary markers and a written agreement, read more: <a href=\"{ARTICLES['neighbour']['en']}\">a boundary fence with your neighbour</a>.",
        "kicker": "Guide · permits and neighbours", "h1": "Do you need a permit<br><em>for a fence?</em>",
        "lead": "In short: usually you need a building notice (ehitusteatis). Here is what the Building Code says, which extra conditions your municipality may set, and what to do when the fence sits on a boundary with a neighbour.",
        "direct_tag": "Short answer",
        "direct_h": "Building a new fence or gate that involves digging deeper than 30 cm requires a building notice and a building design.",
        "direct_p": "That is what Annex 1 of the Estonian Building Code (Ehitusseadustik) says, in force since 1 August 2026. An ordinary fence with posts concreted into the ground involves deeper digging in practice, so expect to file a building notice. Reconstructing (altering) a fence or replacing a single part with an equivalent one needs no notice; extending or demolishing it does. Replacing a whole fence with a substantively new one counts as demolition plus new construction.",
        "law_tag": "Building Code", "law_h": "What the law requires",
        "law_headers": ("Work", "What you need"),
        "law_rows": [
            ("Building a new fence or gate with digging deeper than 30 cm", "Building notice and building design"),
            ("Extending a fence", "Building notice"),
            ("Reconstructing (altering) a fence", "Not required"),
            ("Replacing a single part with an equivalent one", "Not required"),
            ("Demolishing a fence", "Building notice"),
        ],
        "law_note": f"Source: {_a(EHS_LISA1, 'Building Code, Annex 1')} (in Estonian, in force since 1 August 2026), row “Piirdeaed või värav, mille ehitamisega kaasnevad kaevetööd sügavamal kui 30 cm”; every row applies to such a fence or gate. In justified cases the municipality may require a notice for a structure not listed in Annex 1 (Building Code § 35(4)). If the fence is installed without digging, ask your municipality.",
        "more_tag": "Municipality and plans", "more_h": "What else to consider",
        "more_cards": [
            ("Plans can set height and material", "A detailed plan or a municipal plan can set the height, material and transparency of a fence. Under Harku Municipality's thematic plan, a mesh or partly transparent timber fence at a detached, semi-detached or terraced house may not exceed 1.5 metres, and solid close-boarded fences are not allowed except as noise barriers or around industrial sites."),
            ("Distance from the road", "In Harku Municipality the fence must stand at least 2 metres from the edge of the road surface where the boundary is closer to the road, leaving room for snow clearing."),
            ("Tallinn milieu-value areas", "In Tallinn's milieu-value areas (miljööala) the city recommends street fences of generally 1.2–1.5 m, or 1.5–1.8 m for close-boarded fences. The city does not consider mesh and welded panel fences suitable there. As an exception they may be considered between plots, not on the street side, if a dense hedge or climbing plants fully hide the mesh. The city decides case by case."),
            ("Underground utilities", "Before drilling post holes, find out where cables and pipes run, so the fence does not sit on a utility line or damage it."),
            ("Near a listed monument", "In the protection zone of a listed monument or heritage conservation area, the municipality agrees the building notice with the National Heritage Board. If no notice is needed, the Board must be told at least 10 days before work starts. On the monument itself and inside a heritage conservation area, building needs the Board's permit."),
        ],
        "more_note": f"Sources: {_a(HARKU, 'Harku Municipality, structures')} (updated 30.03.2026), {_a(TALLINN, 'Tallinn, fences in milieu-value areas')} (updated 11.04.2024) and the {_a(MUKS, 'Heritage Conservation Act')} §§ 52, 58–59, in Estonian. The rules of other Harju County municipalities are collected in our guide to <a href=\"{ARTICLES['municipal_rules']['en']}\">fence height rules in Harju County</a>.",
        "neighbour_tag": "Neighbours", "neighbour_h": "A fence on a boundary with a neighbour",
        "neighbour_p": "Under § 151 of the Law of Property Act (Asjaõigusseadus), a wall, hedge, ditch or similar thing separating two properties is in the joint use of the neighbours, regardless of who owns it. If both neighbours use it, they share the maintenance costs equally. If it is needed in one neighbour's interest, it may not be removed or altered without that neighbour's consent.",
        "neighbour_p2": "In practice, agree the position, fence type, height and cost split with your neighbour in writing before work starts. If the boundary markers are uncertain, have a licensed land surveyor restore the boundary before the posts go in. Harku Municipality states that cooperation with neighbours is mandatory when a fence separates two plots.",
        "neighbour_note": f"Source: {_a(AOS, 'Law of Property Act § 151')}, in Estonian.",
        "how_tag": "Building Register", "how_h": "How to file a building notice",
        "how_p": f"The building notice goes to the municipality through the {_a(EHR, 'Building Register (ehr.ee)')} at least 10 days before work starts. If the municipality does not report a need for further checks within 10 days, work may begin, and you may build under the notice for four years. The notice gives the property details and cadastral number, a description of the fence and its position on the plot, and the design is filed with it. The municipality may also involve the neighbouring owner. According to Harku Municipality there is no state fee, and the site plan is drawn on a geodetic base plan or a setting-out plan.",
        "how_p2": "LuxAed provides the fence's technical data and describes the scope of work. Whether a formal design or notice is needed, and who files it, is agreed separately.",
        "faq": [
            ("Does a mesh fence need a building notice?", "Yes, if installing the posts involves digging deeper than 30 cm, for example drilling and concreting. Then you need a building notice and a design, as for any fence. If in doubt, ask your municipality."),
            ("Do I need a notice to replace an old fence with a new one?", "It depends on the work. Replacing a single part like-for-like or reconstructing the fence needs no notice. If the old fence is torn down and a substantively new one goes up, that is demolition plus new construction (Building Code § 4(4)), which needs a building notice and, with digging deeper than 30 cm, a design."),
            ("Does a fence installed without digging need a notice?", "Not always, because the Annex 1 requirement is tied to digging deeper than 30 cm. The municipality may still require a notice in justified cases (Building Code § 35(4)), so ask before work starts."),
            ("How soon can work start after filing the notice?", "Under the Building Code the notice must be filed at least 10 days before work starts. If the municipality does not report a need for further checks in that time, you may begin. You may build under the notice for four years."),
            ("Are there extra rules near a listed monument?", "Yes. In the protection zone of a listed monument or heritage conservation area, the municipality agrees the building notice with the National Heritage Board. If no notice is needed, the Board must be told at least 10 days before work starts."),
            ("Who files the building notice?", "Usually the property owner or their representative files it in the Building Register. LuxAed provides the fence's technical data; who prepares the design and files the notice is agreed separately."),
        ],
        "disclaimer": "Checked 27 September 2026. This guide is not legal advice: check the current requirements of your municipality before work starts.",
        "links": ("Read next", "Useful guides", [
            (PATHS["area"]["en"], "We cover all of Harju County", "Municipalities, villages and free measurement."),
            (PATHS["choose"]["en"], "How to choose a fence", "Privacy, wind, maintenance and price."),
            (GATE_GUIDE["en"], "Sliding or swing gate?", "Space, winter, automation and price."),
        ]),
        "cta": ("Let's plan your fence together", "We measure the site free of charge and provide the fence's technical data for the notice.", "Book a free measurement"),
    },
}


def permit_page(lang):
    c = PERMIT[lang]
    tag, heading, cards = link_cards("guides", lang, ["municipal_rules", "neighbour", "road_utilities"])
    inner = hero(lang, c["kicker"], c["h1"], c["lead"], "luxaed-w-mesh-1") + f'''
<section class="section direct-answer"><div class="wrap"><span class="tag">{c["direct_tag"]}</span><h2 class="big">{c["direct_h"]}</h2><p class="lead">{c["direct_p"]}</p></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">{c["law_tag"]}</span><h2 class="big">{c["law_h"]}</h2>{_table(c["law_headers"], c["law_rows"])}<p class="source-note">{c["law_note"]}</p></div></section>
<section class="section"><div class="wrap"><span class="tag">{c["more_tag"]}</span><h2 class="big">{c["more_h"]}</h2>{_cards(c["more_cards"])}<p class="source-note">{c["more_note"]}</p></div></section>
<section class="section section--alt"><div class="wrap guide-narrow"><span class="tag">{c["neighbour_tag"]}</span><h2 class="big">{c["neighbour_h"]}</h2><p class="lead">{c["neighbour_p"]}</p><p class="lead">{c["neighbour_more"]}</p><p class="source-note">{c["neighbour_note"]}</p></div></section>
<section class="section"><div class="wrap guide-narrow"><span class="tag">{c["how_tag"]}</span><h2 class="big">{c["how_h"]}</h2><p class="lead">{c["how_p"]}</p><p class="lead">{c["how_p2"]}</p></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">{c["advice_tag"]}</span><h2 class="big">{c["advice_h"]}</h2>{_cards(c["advice"])}</div></section>
<section class="section"><div class="wrap"><span class="tag">{ {'et':'KKK','ru':'Вопросы','en':'FAQ'}[lang] }</span><h2 class="big">{ {'et':'Korduma kippuvad küsimused','ru':'Частые вопросы','en':'Frequently asked questions'}[lang] }</h2>{faq_html(c["faq"])}<p class="source-note">{c["disclaimer"]}</p></div></section>
{_link_cards(tag, heading, cards)}
{_cta(c["cta"][0], c["cta"][1], HOME[lang] + "#form", c["cta"][2])}'''
    page(lang, PERMIT_GUIDE[lang], c["title"], c["desc"], inner, c["faq"], "luxaed-w-mesh-1",
         crumb=(HUB_NAME[lang], HUB_ROW[lang], SHORT["permit"][lang]), article=_article(c["h1"], "luxaed-w-mesh-1"))


# ------------------------------------------------------------------ gate guide
GATES = {
    "et": {
        "title": "Liugvärav või tiibvärav: kumb sobib teie sissesõidule? — LuxAed",
        "desc": "Liugvärav säästab ruumi sissesõidu ees, tiibvärav on lihtsam, kui tiibadel on ruumi. Võrdlus: külgruum, kalle, talv, automaatika ja hinnad Tallinnas.",
        "kicker": "Juhend · väravad", "h1": "Liugvärav või<br><em>tiibvärav?</em>",
        "lead": "Valik sõltub eelkõige ruumist: kas aia kõrval on ruumi liugvärava jaoks või värava ees ruumi tiibade avanemiseks. See võrdlus aitab otsustada juba enne mõõdistust.",
        "direct_tag": "Lühivastus",
        "direct_h": "Liugvärav sobib, kui värava ees on vähe ruumi või sissesõit on kaldu. Tiibvärav sobib tasasele sissesõidule, kus tiivad saavad vabalt avaneda.",
        "direct_p": "Liugvärav vajab aia kõrval külgruumi ja on talvel mugavam, sest lumi värava ees ei sega, kuid kandurite ümbrus tuleb lumest ja jääst puhtana hoida. Tiibvärav on lihtsama konstruktsiooniga ja sageli soodsam, kuid tiibade ette kogunev lumi tuleb enne avamist ära koristada.",
        "types_tag": "Kaks lahendust", "types_h": "Kuidas need erinevad",
        "types": [
            ("luxaed-wood-sliding-gate-1", "Puidust liugvärav teraskarkassil", "⇄", "Liugvärav", "Liugvärav", "Värav liigub avamisel aia kõrvale. Konsoolne liugvärav liigub alusele kinnitatud kanduritel ja selle tiib on avast pikem, sest sellel on vastukaaluosa.", ["Säästab ruumi värava ees", "Sobib kaldega sissesõidule", "Vajab külgruumi"]),
            ("luxaed-wood-swing-gate-1", "Puidust tiibväravad teraskarkassil", "⛩", "Tiibvärav", "Tiibvärav", "Kaks tiiba avanevad hingedel sisse- või väljapoole. Konstruktsioon on lihtne, kuid tiibade liikumisala peab olema vaba nii suvel kui ka talvel.", ["Lihtne konstruktsioon", "Vajab ruumi tiibadele", "Sobib tasasele sissesõidule"]),
        ],
        "table_tag": "Võrdlus", "table_h": "Liugvärav ja tiibvärav kõrvuti",
        "table_headers": ("", "Liugvärav", "Tiibvärav"),
        "table_rows": [
            ("Ruum värava ees", "Ei vaja", "Vajab tiibade avanemiseks"),
            ("Ruum aia kõrval", "Vajab külgruumi", "Ei vaja"),
            ("Kaldega sissesõit", "Sobib hästi", "Keerulisem, tiib võib maad riivata"),
            ("Talv ja lumi", "Lumi värava ees ei sega", "Tiibade ette kogunev lumi tuleb koristada"),
            ("Automaatika", "Üks ajam", "Ajam mõlemale tiivale"),
            ("Hind meie hinnatabelis", "Automaatikaga 2 100–3 000 €", "1 400–2 300 €, automaatika võib lisanduda"),
        ],
        "table_note": "Hinnad on meie hinnatabelist ja kehtivad standardlahendusele. Täpse hinna anname pärast mõõdistust.",
        "measure_tag": "Mõõdistus", "measure_h": "Mida mõõdistusel vaatame",
        "measure": [
            ("Ava laius", "Mõõdame sissesõidu ja valime värava pikkuse ning konstruktsiooni."),
            ("Külgruum ja kalle", "Kontrollime, kas aia kõrval on ruumi liugväravale ja kas sissesõit on kaldu."),
            ("Pinnas ja alus", "Hindame, milline vundament või alus sobib väravale ja postidele."),
            ("Elekter ja juhtimine", "Arvestame kaabli, ajami, fotoelementide ja juhtimise vajadusega."),
        ],
        "faq": [
            ("Kumb on odavam, liugvärav või tiibvärav?", "Tiibvärav on sageli soodsam. Meie hinnatabelis on tiibvärav 1 400–2 300 € ja automaatikaga liugvärav 2 100–3 000 €. Tiibvärava automaatika võib lisanduda."),
            ("Kui palju ruumi liugvärav vajab?", "Liugvärav liigub avamisel aia kõrvale, seega peab seal olema vaba külgruum. Konsoolse liugvärava tiib on avast pikem, sest sellel on vastukaaluosa. Täpse vajaduse mõõdame kohapeal."),
            ("Kas tiibväravale saab hiljem automaatika panna?", "Enamasti jah, kui värav ja postid on piisavalt tugevad ning elekter on olemas. Olemasolevale väravale maksab automaatika paigaldus orienteeruvalt 500–1 250 €."),
            ("Kumb töötab talvel paremini?", "Tavaliselt liugvärav, sest lumi värava ees seda ei sega, kuid kandurite ümbrus tuleb lumest ja jääst puhtana hoida. Tiibvärava ette kogunev lumi tuleb enne avamist ära koristada."),
            ("Kas kaldega sissesõidule sobib tiibvärav?", "Kaldel võib tiib avanedes maad riivata, seega on liugvärav sageli lihtsam lahendus. Mõnikord aitab tiibade kõrguse või avanemissuuna muutmine."),
            ("Kas liugvärav vajab vundamenti?", "Jah. Konsoolne liugvärav liigub alusele kinnitatud kanduritel ning meie automaatikaga liugvärava tavalahenduse hinnas (2 100–3 000 €) on vundament sees."),
        ],
        "links": ("Loe edasi", "Kasulik lugeda", [
            (ARTICLES["gate_safety"]["et"], "Automaatvärava ohutus", "CE-märgis, elektritööd ja hooldus."),
            (SLIDING_GATE["et"], "Liugvärav jookseb kinni?", "Rullikud, kandurid ja vajunud alus."),
            (GATE_WONT_OPEN["et"], "Värav ei avane või ei sulgu?", "Toide, pult, fotoelemendid ja talv."),
            (PATHS["prices"]["et"], "Aia ja värava hinnad", "Hinnatabel ja näidisarvutused."),
        ]),
        "cta": ("Mõõdame teie sissesõidu", "Tuleme tasuta mõõdistusele ja ütleme, kumb värav teie krundile sobib.", "Küsi väravate pakkumist"),
    },
    "ru": {
        "title": "Откатные или распашные ворота: что выбрать для въезда — LuxAed",
        "desc": "Откатные ворота экономят место перед въездом, распашные проще, если створкам есть куда открываться. Сравнение: место сбоку, уклон, зима, автоматика и цены.",
        "kicker": "Руководство · ворота", "h1": "Откатные или<br><em>распашные ворота?</em>",
        "lead": "Выбор зависит прежде всего от места: есть ли сбоку место для откатных ворот или перед воротами место, чтобы открывались створки. Это сравнение поможет решить ещё до замера.",
        "direct_tag": "Короткий ответ",
        "direct_h": "Откатные ворота подходят, если перед въездом мало места или въезд с уклоном. Распашные подходят для ровного въезда, где створки свободно открываются.",
        "direct_p": "Откатным воротам нужно место вдоль забора, зато зимой они удобнее: снег перед воротами не мешает, но зону кареток нужно очищать от снега и льда. Распашные проще по конструкции и часто дешевле, но снег перед створками приходится убирать перед открыванием.",
        "types_tag": "Два решения", "types_h": "Чем они отличаются",
        "types": [
            ("luxaed-wood-sliding-gate-1", "Деревянные откатные ворота на стальном каркасе", "⇄", "Откатные", "Откатные ворота", "При открывании ворота уходят вдоль забора. Консольные откатные ворота едут на каретках, закреплённых на основании, и их полотно длиннее проёма из-за противовеса.", ["Экономят место перед въездом", "Подходят для въезда с уклоном", "Нужно место сбоку"]),
            ("luxaed-wood-swing-gate-1", "Деревянные распашные ворота на стальном каркасе", "⛩", "Распашные", "Распашные ворота", "Две створки открываются на петлях внутрь или наружу. Конструкция простая, но зона движения створок должна быть свободна и летом, и зимой.", ["Простая конструкция", "Нужно место для створок", "Подходят для ровного въезда"]),
        ],
        "table_tag": "Сравнение", "table_h": "Откатные и распашные ворота рядом",
        "table_headers": ("", "Откатные", "Распашные"),
        "table_rows": [
            ("Место перед воротами", "Не нужно", "Нужно для открывания створок"),
            ("Место вдоль забора", "Нужно", "Не нужно"),
            ("Въезд с уклоном", "Подходят хорошо", "Сложнее, створка может задевать землю"),
            ("Зима и снег", "Снег перед воротами не мешает", "Снег перед створками нужно убирать"),
            ("Автоматика", "Один привод", "Привод на каждую створку"),
            ("Цена в нашем прайсе", "С автоматикой 2 100–3 000 €", "1 400–2 300 €, автоматика может считаться отдельно"),
        ],
        "table_note": "Цены из нашего прайса для стандартного решения. Точную цену называем после замера.",
        "measure_tag": "Замер", "measure_h": "Что смотрим на замере",
        "measure": [
            ("Ширина проёма", "Измеряем въезд и подбираем длину ворот и конструкцию."),
            ("Место сбоку и уклон", "Проверяем, хватает ли места вдоль забора для откатных ворот и есть ли уклон."),
            ("Грунт и основание", "Оцениваем, какой фундамент или основание подойдёт для ворот и столбов."),
            ("Электрика и управление", "Учитываем кабель, привод, фотоэлементы и способ управления."),
        ],
        "faq": [
            ("Что дешевле, откатные или распашные ворота?", "Распашные часто дешевле. В нашем прайсе распашные ворота стоят 1 400–2 300 €, а откатные с автоматикой 2 100–3 000 €. Автоматика для распашных может считаться отдельно."),
            ("Сколько места нужно откатным воротам?", "При открывании откатные ворота уходят вдоль забора, поэтому там должно быть свободное место. Полотно консольных откатных ворот длиннее проёма, потому что у него есть противовес. Точную длину измеряем на месте."),
            ("Можно ли потом поставить автоматику на распашные ворота?", "Чаще всего да, если ворота и столбы достаточно прочные и есть электричество. Автоматика на существующие ворота обойдётся примерно в 500–1 250 €."),
            ("Какие ворота лучше зимой?", "Обычно откатные: снег перед въездом им не мешает, но зону кареток нужно очищать от снега и льда. Перед распашными снег у створок нужно убирать перед открыванием."),
            ("Подойдут ли распашные ворота для въезда с уклоном?", "На уклоне створка может задевать землю при открывании, поэтому откатные ворота часто проще. Иногда помогает изменить высоту створок или направление открывания."),
            ("Нужен ли откатным воротам фундамент?", "Да. Консольные откатные ворота едут на каретках, закреплённых на основании, и в цене нашего стандартного решения с автоматикой (2 100–3 000 €) фундамент уже учтён."),
        ],
        "links": ("Читайте также", "Полезно знать", [
            (ARTICLES["gate_safety"]["ru"], "Безопасность автоматических ворот", "CE, электромонтаж и обслуживание."),
            (SLIDING_GATE["ru"], "Заедают откатные ворота?", "Ролики, каретки и просевшее основание."),
            (GATE_WONT_OPEN["ru"], "Не открываются ворота?", "Питание, пульт, фотоэлементы и зима."),
            (PATHS["prices"]["ru"], "Цены на заборы и ворота", "Прайс и примеры расчёта."),
        ]),
        "cta": ("Измерим ваш въезд", "Приедем на бесплатный замер и скажем, какие ворота подойдут вашему участку.", "Рассчитать ворота"),
    },
    "en": {
        "title": "Sliding or swing gate: which suits your driveway? — LuxAed",
        "desc": "Sliding gates save space in front of the entrance; swing gates are simpler where the leaves have room. Compare side space, slopes, winter use, automation and prices.",
        "kicker": "Guide · gates", "h1": "Sliding or<br><em>swing gate?</em>",
        "lead": "The choice depends mainly on space: is there room beside the fence for a sliding gate, or room in front of the entrance for the leaves to swing? This comparison helps you decide before the site visit.",
        "direct_tag": "Short answer",
        "direct_h": "Choose a sliding gate when there is little space in front of the entrance or the drive slopes. Choose a swing gate for a level entrance where the leaves can open freely.",
        "direct_p": "A sliding gate needs side space along the fence and is easier in winter, because snow in front of the gate does not block it, but the carriage area must be kept clear of snow and ice. A swing gate is simpler to build and often cheaper, but snow in front of the leaves has to be cleared before opening.",
        "types_tag": "Two options", "types_h": "How they differ",
        "types": [
            ("luxaed-wood-sliding-gate-1", "Wooden sliding gate on a steel frame", "⇄", "Sliding", "Sliding gate", "The gate slides along the fence when it opens. A cantilever sliding gate runs on carriages fixed to its base, and its leaf is longer than the opening because of the counterweight section.", ["Saves space in front", "Suits a sloping drive", "Needs side space"]),
            ("luxaed-wood-swing-gate-1", "Wooden swing gates on a steel frame", "⛩", "Swing", "Swing gate", "Two leaves open on hinges inwards or outwards. The construction is simple, but the leaves' swing area has to stay clear in summer and winter.", ["Simple construction", "Needs room for the leaves", "Suits a level entrance"]),
        ],
        "table_tag": "Comparison", "table_h": "Sliding and swing gates side by side",
        "table_headers": ("", "Sliding gate", "Swing gate"),
        "table_rows": [
            ("Space in front of the gate", "Not needed", "Needed for the leaves"),
            ("Space along the fence", "Needed", "Not needed"),
            ("Sloping drive", "Works well", "Harder, a leaf may scrape the ground"),
            ("Winter and snow", "Snow in front does not block it", "Snow in front of the leaves must be cleared"),
            ("Automation", "One drive", "A drive for each leaf"),
            ("Price in our price guide", "€2,100–3,000 with automation", "€1,400–2,300, automation may be extra"),
        ],
        "table_note": "Prices are from our price guide and apply to a standard solution. We give the exact price after the site visit.",
        "measure_tag": "Site visit", "measure_h": "What we check on site",
        "measure": [
            ("Opening width", "We measure the entrance and choose the gate length and construction."),
            ("Side space and slope", "We check whether there is room along the fence for a sliding gate and whether the drive slopes."),
            ("Ground and base", "We assess which foundation or base suits the gate and posts."),
            ("Power and control", "We plan the cable, drive, photocells and control method."),
        ],
        "faq": [
            ("Which is cheaper, a sliding or a swing gate?", "A swing gate is often cheaper. Our price guide lists swing gates at €1,400–2,300 and sliding gates with automation at €2,100–3,000. Automation for a swing gate may be extra."),
            ("How much space does a sliding gate need?", "A sliding gate moves along the fence when it opens, so that space has to be clear. The leaf of a cantilever sliding gate is longer than the opening because of its counterweight section. We measure the exact requirement on site."),
            ("Can automation be added to a swing gate later?", "Usually yes, if the gate and posts are strong enough and power is available. Automation for an existing gate is typically €500–1,250."),
            ("Which works better in winter?", "Usually a sliding gate, because snow in front of the entrance does not block it, though the carriage area must be kept clear of snow and ice. Snow in front of swing gate leaves has to be cleared before opening."),
            ("Does a swing gate suit a sloping drive?", "On a slope a leaf may scrape the ground as it opens, so a sliding gate is often simpler. Sometimes changing the leaf height or the opening direction helps."),
            ("Does a sliding gate need a foundation?", "Yes. A cantilever sliding gate runs on carriages fixed to its base, and the foundation is included in our standard price for a sliding gate with automation (€2,100–3,000)."),
        ],
        "links": ("Read next", "Useful reading", [
            (ARTICLES["gate_safety"]["en"], "Automatic gate safety", "CE marking, wiring and maintenance."),
            (SLIDING_GATE["en"], "Sliding gate sticking?", "Rollers, carriages and a settled base."),
            (GATE_WONT_OPEN["en"], "Gate won't open or close?", "Power, remote, photocells and winter."),
            (PATHS["prices"]["en"], "Fence and gate prices", "Price guide and worked examples."),
        ]),
        "cta": ("Let us measure your entrance", "We visit free of charge and tell you which gate suits your property.", "Get a gate quote"),
    },
}


def gate_page(lang):
    c = GATES[lang]
    tag, heading, cards = c["links"]
    inner = hero(lang, c["kicker"], c["h1"], c["lead"], "luxaed-wood-sliding-gate-1", cta_href=GATES_HUB[lang] + "#form") + f'''
<section class="section direct-answer"><div class="wrap"><span class="tag">{c["direct_tag"]}</span><h2 class="big">{c["direct_h"]}</h2><p class="lead">{c["direct_p"]}</p></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">{c["types_tag"]}</span><h2 class="big">{c["types_h"]}</h2>{_types(c["types"])}</div></section>
<section class="section"><div class="wrap"><span class="tag">{c["table_tag"]}</span><h2 class="big">{c["table_h"]}</h2>{_table(c["table_headers"], c["table_rows"])}<p class="price-note">{c["table_note"]}</p></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">{c["measure_tag"]}</span><h2 class="big">{c["measure_h"]}</h2>{_cards(c["measure"], "answer-grid")}</div></section>
<section class="section"><div class="wrap"><span class="tag">{ {'et':'KKK','ru':'Вопросы','en':'FAQ'}[lang] }</span><h2 class="big">{ {'et':'Korduma kippuvad küsimused','ru':'Частые вопросы','en':'Frequently asked questions'}[lang] }</h2>{faq_html(c["faq"])}</div></section>
{_link_cards(tag, heading, cards)}
{_cta(c["cta"][0], c["cta"][1], GATES_HUB[lang] + "#form", c["cta"][2])}'''
    page(lang, GATE_GUIDE[lang], c["title"], c["desc"], inner, c["faq"], "luxaed-wood-sliding-gate-1",
         crumb=(HUB_NAME[lang], HUB_ROW[lang], SHORT["gates"][lang]), article=_article(c["h1"], "luxaed-wood-sliding-gate-1"))


if __name__ == "__main__":
    for language in ("et", "ru", "en"):
        permit_page(language)
        gate_page(language)
    print("Extra guide pages done: 6")
