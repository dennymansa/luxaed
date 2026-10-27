# LuxAed article rewrite: privacy_fence (ET / RU / EN).
# Paths: /kinnine-aed/, /ru/gluhoj-zabor/, /en/privacy-fence/
#
# Prices: only the LuxAed price table (FACTS_prices.md). The 20 m, 30 m, 80 m and 100 m totals are
# plain multiplications of those ranges (e.g. 30 m x 70-135 = 2 100-4 050; 20 m solid + 80 m roll
# mesh = 1 400-2 700 + 2 000-3 600 = 3 400-6 300).
# Legal facts: only FACTS.md (keys ehs, lisa1) and the municipal_rules table with the FACTS.md
# corrections (keys harku, saue, viimsi, kiili, rae, saku, keila, maardu, nomme, tallinn).
# Harku ban includes the exception "except as noise barriers or around industrial sites"; Saue covers
# opaque fences of any material; Rae covers only the checked northern plan area (incl. Peetri).
# No new official source was added, so NEW_SRC is empty.
# The wind-load figures are plain physics, not a legal or product claim: at 25-30 m/s gusts the
# dynamic pressure is about 0.4-0.56 kPa, i.e. roughly 1.8-2.5 kN on a 2.5 m x 1.8 m solid bay
# (a couple of hundred kilograms of force); the base moment grows with height squared, (1.8/1.5)^2 = 1.44.

NEW_SRC = {}

ARTICLE = {
    "et": {
        "title": "Kinnine aed: profiilplekk-, puit- või lippaed? | LuxAed",
        "desc": "Kinnine aed koos paigaldusega: profiilplekk 70–135 €/jm, metall-lippaed 85–155 €/jm, puit 90–160 €/jm. Võrdleme privaatsust, tuult, hooldust ja valla reegleid.",
        "short": "Kinnine aed",
        "image": "luxaed-svc-wood",
        "kicker": "Võrdlus · kinnised aiad",
        "h1": "Kinnine aed:<br><em>profiilplekk-, puit- või lippaed?</em>",
        "lead": "Kinnine aed varjab hoovi võõraste pilkude eest, kuid peab vastu pidama tuulele ja lumele ning mahtuma valla reeglitesse. Võrdleme kolme levinumat lahendust ja selgitame, kus kinnine aed on üldse lubatud.",
        "direct": ("Kõige soodsam kinnine aed on profiilplekk, kõige vähem hooldust vajab metall-lippaed ja kõige soojema ilmega on puitaed.",
                   'Meie hinnatabelis maksab koos paigaldusega profiilplekk-aed 70–135 €/jm, metall-lippaed 85–155 €/jm ja puitaed 90–160 €/jm. Enne materjali valikut kontrollige aga planeeringut: mitmes Harjumaa omavalitsuses ei ole läbipaistmatu plankaed eramu ümber lubatud või peab aed olema osaliselt läbipaistev. Kui privaatsust on vaja ainult ühel küljel, on ülejäänud piiril <a href="/paneelaed-voi-vorkaed/">võrk- või paneelaed</a> tunduvalt soodsam.'),
        "blocks": [
            {"type": "table", "tag": "Võrdlus", "h": "Kolm kinnist aeda kõrvuti",
             "headers": ("", "Profiilplekk", "Puit", "Metall-lippaed"),
             "rows": [("Hind koos paigaldusega", "70–135 €/jm", "90–160 €/jm", "85–155 €/jm"),
                      ("30 m aed", "2 100–4 050 €", "2 700–4 800 €", "2 550–4 650 €"),
                      ("Privaatsus", "Täielik", "Tiheda laudisega täielik, vahedega kõrge", "Keskmisest täielikuni, sõltub vahest ja paigutusest"),
                      ("Tuulekoormus", "Suur", "Tihedale laudisele mõjub suur koormus", "Väiksem, kui lamellide vahel on vahe"),
                      ("Hooldus", "Vähene: pesemine ja kriimude parandus", "Kaitsekihti tuleb korrapäraselt uuendada", "Vähene"),
                      ("Välimus", "Ühtlane ja sile, karkass jääb tagaküljele", "Soe ja looduslik", "Kaasaegne, ühe- või kahepoolne"),
                      ("Kui planeering nõuab läbipaistvust", "Ei sobi", "Sobib ainult vahedega laudisena", "Sobib hõreda vahega"),
                      ("Väravad", "Sama pleki ja tooniga", "Puittäitega teraskarkassil", "Samade lamellide ja tooniga")],
             "note": "Hinnad on meie hinnatabelist ja sisaldavad materjali ning tavapaigaldust. 30 m hinnad on arvutatud samadest vahemikest, täpse summa anname pärast tasuta mõõdistust."},
            {"type": "sections", "tag": "Reeglid", "h": "Kas kinnine aed on teie krundil lubatud",
             "intro": "Riik ei määra aiale ühtset kõrgust ega läbipaistvust. Ehitusseadustiku § 12 järgi peab aed vastama detailplaneeringule või selle puudumisel üldplaneeringule. Just planeeringud seavad kinnisele aiale kõige sagedamini tingimusi.",
             "items": [("Kus kinnine aed on keelatud või piiratud", [
                           "Harku vallas on läbipaistmatud plankaiad keelatud, välja arvatud müratõkkena või tööstusalade ümber, ning eramu võrkaed või osaliselt läbipaistev puitaed tohib olla kuni 1,5 m kõrge. Saue valla üldplaneering ei luba reeglina läbipaistmatut aeda üheski materjalis, välja arvatud tööstusala ümber või liiklusala ääres müra- või ohutustõkkena.",
                           "Viimsis on läbipaistmatu plankaed lubatud ainult tööstus- või liiklusala ümber müra- või ohutustõkkena. Kiili vallas peab tänavapoolne aed olema osaliselt läbipaistev puitaed ja läbipaistmatu plankaed on keelatud, välja arvatud tööstushoonete ümber. Rae valla põhjaosas, sealhulgas Peetris, on kinnine aed kuni 1,8 m lubatud ainult müratõkkena, kui müra ületab piirnorme."]),
                       ("Kus nõutakse läbipaistvust", [
                           "Saku, Keila ja Maardu planeeringute järgi peab aed olema vähemalt 25% ulatuses läbipaistev ning Keilas ei tohi tänava poole rajada üle 1,5 m kõrgust läbipaistmatut müüri. Sakus ei kehti läbipaistvuse nõue elamumaal hekile. Nõmmel on üldjuhul oodatud hõre läbipaistev puitlippaed või hekiga kombineeritud võrkaed.",
                           'Tallinna miljööaladel on tänavaäärse aia kõrgus üldjuhul 1,2–1,5 m ja plankaial 1,5–1,8 m. Kõigi kontrollitud omavalitsuste nõuded leiate <a href="/aia-korgus-harjumaal/">aia kõrguse ja läbipaistvuse juhendist</a>.']),
                       ("Mida teha enne tellimist", [
                           "Vaadake esmalt oma krundi detailplaneeringut, sest see on aia jaoks kõige täpsem dokument ja võib lubada või keelata rohkem kui üldplaneering. Kui sõnastus jääb ebaselgeks, küsige valla planeerimisspetsialistilt, kas teie valitud aed sobib, ja hoidke vastus alles. Naabri kinnine aed ei tõenda midagi, sest see võib olla ehitatud enne praegust planeeringut."])],
             "sources": ["ehs", "harku", "saue", "viimsi", "kiili", "rae", "saku", "keila", "maardu", "nomme", "tallinn"]},
            {"type": "sections", "tag": "Tuul", "h": "Tuul, postid ja vundament",
             "intro": "Tuule jaoks on kinnine aed sein: õhk, mis võrkaiast läbi lendaks, surub nüüd vastu plekki või laudist ja see jõud kandub postide kaudu vundamenti.",
             "items": [("Miks kinnine aed vajab tugevamaid poste", [
                           "Tugevates tormiiilides võib ühele 2,5 m laiusele ja 1,8 m kõrgusele kinnisele lõigule mõjuda jõud, mis on võrreldav paarisaja kilogrammi raskusega. See jõud püüab posti maapinna kohalt murda või vundamenti kallutada. Seepärast on kinnise aia postid jämedamad, need paigaldatakse tihedamalt ja sügavamale kui võrkaial ning karkass on jäigem.",
                           "Kõrgus suurendab koormust kiiremini, kui arvata võiks: 1,8 m kõrguse kinnise aia posti jalale mõjuv koormus on umbes 1,4 korda suurem kui 1,5 m aial. Mere ääres, lagedal põllul ja kõrgemate hoonete vahel, kus tuul tugevneb, valime postid ja alused just sellega arvestades."]),
                       ("Külm, savi ja paekivi", [
                           "Kinnise aia postid ei tohi külmakerke tõttu liikuda, sest pikal siledal pinnal on näha isegi paari sentimeetri kalle. Savises pinnases peab alus ulatuma piisavalt sügavale ega tohi ülaosas laieneda, muidu haarab külmunud maa sellest kinni ja tõstab selle üles. Paljudes Harjumaa kohtades on paekivi maapinna lähedal. Siis puuritakse auk kivisse või kinnitatakse post ankrutega, selle asemel et jätta see madalaks.",
                           "Kuna kinnise aia postid lähevad sügavale, kaasnevad aia ehitamisega tavaliselt kaevetööd sügavamal kui 30 cm. Ehitusseadustiku lisa 1 järgi on siis vaja ehitusteatist ja ehitusprojekti. LuxAed annab teatise jaoks aia tehnilised andmed. Kes koostab projekti ja esitab teatise, lepime kokku eraldi."]),
                       ("Kinnise täitega värav tuules", [
                           'Sama pleki, laudise või lamellidega sõiduvärav on tuules samuti puri. Tugev tuul võib tiibvärava tiiva lahti lüüa ning koormab hingi ja ajamit, liugvärav liigub aga rullikutel ja talub tuult üldjuhul paremini. Kui krunt on tuuline, arutage seda juba värava valikul. Abiks on juhend <a href="/liugvarav-voi-tiibvarav/">liugvärav või tiibvärav</a>.'])],
             "sources": ["lisa1"]},
            {"type": "sections", "tag": "Materjalid", "h": "Profiilplekk, puit ja metall-lippaed lähemalt",
             "items": [("Profiilplekk-aed: kõige soodsam täielik varje", [
                           'Profiilplekk-aed koosneb tsingitud ja polümeerkattega terasplekist, mis kinnitatakse metallroovidele ja postidele. See varjab täielikult, on kiire paigaldada ja vajab vähe hoolt: piisab pesemisest ja kattekihi kriimude õigeaegsest parandamisest. Pakume alati valmis <a href="/aiad/profiilplekk-aed/">profiilplekk-aeda koos karkassi ja postidega</a>, mitte ainult plekki.',
                           "Nõrgad kohad on tagakülg ja käitumine tuules. Karkass jääb tagaküljele ning kui kruvisid on vähe või roovid on nõrgad, hakkab plekk tuules kolksuma. Soodsam kate võib päikesepoolsel küljel aastatega tuhmuda."]),
                       ("Puitaed ja plankaed: kõige soojem välimus", [
                           'Puitaia ehitame teraskarkassile, mis hoiab selle sirgena ka siis, kui puit paisub ja kuivab. Tihe laudis ehk plankaed varjab täielikult, laudade vahega saab privaatsust ja tuult tasakaalustada. Lauad jäetakse maapinnast eemale, et need ei imeks niiskust. Lähemalt kirjutame sellest <a href="/aiad/puitaed/">puitaia lehel</a>.',
                           "Puit vajab hoolt. Ilma kaitsekihita läheb see päikese käes halliks ja hakkab pragunema, seega tuleb õli või värvi korrapäraselt uuendada, päikesepoolsel küljel sagedamini. Liiga tihedalt kokku pandud lauad kaarduvad niiskusega, nii et väike vahe laudade vahel on vajalik ka tihedas aias."]),
                       ("Metall-lippaed: reguleeritav privaatsus", [
                           'Metall-lippaed koosneb tsingitud ja pulbervärvitud lamellidest, mis paigaldatakse püsti või pikali. Vahe valite ise: hõre ühepoolne aed laseb läbi valgust ja tuult, tihe kahepoolne ehk malepaigutusega aed varjab peaaegu täielikult. Nurga alt vaadates paistab ka vahedega lippaed üsna kinnine, otse vaadates jääb see läbipaistvaks. Valikud leiate <a href="/aiad/lippaed/">metall-lippaia lehelt</a>.',
                           "Lippaed vajab vähe hoolt ja selle värv püsib, kuid tihedam täide tähendab ka suuremat tuulekoormust ja kõrgemat hinda. Kui planeering nõuab läbipaistvust, ärge eeldage, et kahepoolne lippaed sobib: otse vaadates võib see olla peaaegu kinnine. Küsige sel juhul enne tellimist valla arvamust."])]},
            {"type": "sections", "tag": "Igapäevaelu", "h": "Mida kinnine aed teie hoovis muudab",
             "items": [("Privaatsus ja kõrgus", [
                           "1,5 m kõrgune aed varjab terrassil istujat, kuid tänaval seisev täiskasvanu näeb sellest üle. Naabri teise korruse aknast ei varja hoovi ükski aed, seal aitavad puud, pergola või varjesein terrassi juures. Seega mõelge enne kõrguse ja materjali valikut läbi, keda ja kust soovite varjata."]),
                       ("Lumi ja vari", [
                           "Kinnise aia taha tekivad tuisuga lumehanged, tihti just sissesõidule või teerajale. Aia varjus sulab lumi kevadel hiljem ja aia põhjaküljel olev peenar jääb päikeseta. Tee ääres võtab kinnine aed vastu kogu lume, mille sahk sinna lükkab."]),
                       ("Müra", [
                           "Tavaline kinnine aed summutab tänavamüra vaid veidi, peamiselt seetõttu, et kaob otsene vaade teele. Müra vähendamiseks peab tõke olema raske, pragudeta ja piisavalt kõrge, seega vajab tõsine müraprobleem erilahendust."]),
                       ("Külalised ja ligipääs", [
                           'Kinnise aia tagant ei näe, kes jalgvärava taga seisab. Selle lahendavad <a href="/varavad/domofonid/">videodomofon ja jalgvärava elektrilukk</a>: näete külalist või kullerit ekraanil ja avate värava toast. Meie hinnatabelis maksab videodomofon koos jalgvärava elektriluku ja tavapaigaldusega 650–1 600 €.'])]},
            {"type": "sections", "tag": "Hind", "h": "Mis maksab kinnine aed",
             "items": [("Millest hind sõltub", [
                           'Hinda mõjutavad kõige rohkem kõrgus, postide tugevus ja samm vastavalt tuulele, pleki paksus ja kate, lamellide tihedus ning puidu liik ja viimistlus. Väravad, vana aia eemaldamine ja keerulisem pinnas lisanduvad eraldi. Täpse hinna anname kirjalikus pakkumises pärast tasuta mõõdistust, kõik hinnad leiate <a href="/hinnad/">hinnatabelist</a>.']),
                       ("Kinnine ainult seal, kus seda vaja on", [
                           "Kui kogu 100 m krundipiir tehakse profiilplekist, maksab see meie hinnatabeli järgi 7 000–13 500 €. Kui kinnine on ainult 20 m tänava pool ja ülejäänud 80 m on rullvõrk, maksab sama piir 3 400–6 300 €. Sageli piisab kinnisest lõigust tänava, terrassi või naabri akende poole."])]},
            {"type": "cards", "tag": "Meie soovitus", "h": "Mida me ise soovitame", "cols": 2,
             "items": [("Planeering enne materjali", "Kontrollige detailplaneeringut enne, kui valite plekki, puitu või lamelle. Kui kinnine aed ei ole lubatud, ei aita ka kõige ilusam materjal."),
                       ("Tuulisel krundil metall-lippaed", "Mere ääres ja lagedal krundil eelistame vahedega metall-lippaeda: nurga alt vaadates varjab see hästi, kuid tuul koormab seda vähem."),
                       ("Puit siis, kui olete valmis hooldama", "Puitaed on puitmaja juurde kõige soojem valik, kuid kaitsekihti tuleb uuendada. Kui te seda teha ei soovi, valige plekk või metall."),
                       ("Ilus külg: leppige naabriga kokku", "Profiilplekk- ja ühepoolsel lippaial on esi- ja tagakülg. Piiriaia puhul leppige naabriga kirjalikult kokku, kummale poole esikülg jääb.")]},
            {"type": "cards", "tag": "Levinud probleemid", "h": "Mis läheb sageli valesti", "cols": 3,
             "items": [("Aed kaldub tormiga", "Kinnise aia postid on liiga nõrgad, liiga harvad või liiga madala alusega."),
                       ("Plekk kolksub tuules", "Kruvisid on vähe või roovid on nõrgad, nii et plekk liigub iga iiliga."),
                       ("Puit läheb halliks ja kaardub", "Kaitsekihti ei uuendata, lauad puudutavad maad või on liiga tihedalt koos."),
                       ("Plankaed ei olnud lubatud", "Planeeringu keeld või läbipaistvuse nõue selgub alles pärast tellimist."),
                       ("Lumehang sissesõidul", "Kinnine aed on tuulepoolsel küljel ja tuisk kuhjab lume selle taha."),
                       ("Värav ei püsi tuules", "Tuul lööb kinnise täitega tiibvärava lahti ja koormab hingi ning ajamit.")]},
        ],
        "faq": [
            ("Milline kinnine aed on kõige odavam?", "Meie hinnatabelis on kõige soodsam profiilplekk-aed, 70–135 €/jm koos paigaldusega. Metall-lippaed maksab 85–155 €/jm ja puitaed 90–160 €/jm."),
            ("Mida teha, kui vald nõuab läbipaistvat aeda?", "Siis ei sobi kinnine profiilplekk- ega plankaed. Valige hõreda vahega metall-lippaed, vahedega puitaed või 3D paneelaed ja lisage privaatsust hekiga. Näiteks Sakus ei kehti läbipaistvuse nõue elamumaal hekile."),
            ("Kas kinnise aia võib teha ainult tänava poole?", "Jah, kui planeering lubab tänava poole kinnist aeda. Näiteks Kiili, Keila ja Maardu planeeringud nõuavad osalist läbipaistvust ka tänavapoolselt aialt, seega kontrollige enne tellimist oma krundi detailplaneeringut."),
            ("Kas plankaia keeld kehtib ka profiilplekk-aiale?", "Ärge eeldage, et see ei kehti. Saue valla üldplaneering ei luba reeglina läbipaistmatut aeda üheski materjalis ja seal, kus planeering nõuab läbipaistvust, ei sobi ka kinnine plekk-aed. Kui sõnastuses on juttu ainult plankaiast, küsige enne tellimist valla planeerimisspetsialistilt."),
            ("Kummale poole jääb kinnise aia ilus külg?", "Profiilplekk- ja ühepoolsel lippaial jäävad postid ja karkass tagaküljele. Kahepoolne lippaed ja mõlemalt poolt laudisega puitaed näevad mõlemalt poolt ühtemoodi välja. Piiriaia puhul leppige naabriga enne tööd kokku, kummale poole esikülg jääb."),
            ("Kas kinnist aeda saab hiljem kõrgemaks teha?", "Harva ilma poste vahetamata. Kõrgem kinnine aed koormab poste tuulega tunduvalt rohkem ja uus kõrgus peab mahtuma planeeringus lubatud kõrguse sisse. Kui plaanite kõrgemat aeda, valige postid ja alused kohe selle järgi."),
        ],
        "links_keys": ["neighbour", "permit_guide", "mistakes"],
        "links_extra": [("/aiad/lippaed/", "Metall-lippaed", "Valitav vahe, toon ja privaatsus.")],
        "cta": ("Aitame valida kinnise aia", "Tasuta mõõdistusel kontrollime tuult, pinnast ja planeeringut ning pakume teie krundile sobiva lahenduse.", "/#form", "Küsi pakkumist"),
    },
    "ru": {
        "title": "Глухой забор: профнастил, дерево или штакетник? | LuxAed",
        "desc": "Глухой забор с установкой: профнастил 70–135 €/м, металлический штакетник 85–155 €/м, дерево 90–160 €/м. Сравниваем приватность, ветер, уход и правила волостей.",
        "short": "Глухой забор",
        "image": "luxaed-svc-wood",
        "kicker": "Сравнение · глухие заборы",
        "h1": "Глухой забор:<br><em>профнастил, дерево или штакетник?</em>",
        "lead": "Глухой забор закрывает двор от чужих глаз, но должен выдержать ветер и снег и уложиться в правила волости. Сравниваем три самых распространённых варианта и объясняем, где глухой забор вообще разрешён.",
        "direct": ("Дешевле всего глухой забор из профнастила, меньше всего ухода требует металлический штакетник, а теплее всех выглядит дерево.",
                   'В нашем прайсе с установкой забор из профнастила стоит 70–135 €/м, металлический штакетник 85–155 €/м, деревянный забор 90–160 €/м. Но до выбора материала проверьте планировку: в нескольких волостях Харьюмаа глухой дощатый забор у частного дома не разрешён или забор должен быть частично прозрачным. Если закрыться нужно только с одной стороны, на остальной границе <a href="/ru/3d-zabor-ili-setka-rabitsa/">сетка или 3D-панели</a> обойдутся заметно дешевле.'),
        "blocks": [
            {"type": "table", "tag": "Сравнение", "h": "Три глухих забора рядом",
             "headers": ("", "Профнастил", "Дерево", "Металлический штакетник"),
             "rows": [("Цена с установкой", "70–135 €/м", "90–160 €/м", "85–155 €/м"),
                      ("Забор 30 м", "2 100–4 050 €", "2 700–4 800 €", "2 550–4 650 €"),
                      ("Приватность", "Полная", "Полная при сплошной обшивке, высокая с зазорами", "От средней до полной, зависит от зазора и схемы"),
                      ("Ветровая нагрузка", "Большая", "На плотную обшивку действует большая нагрузка", "Меньше, если между планками есть зазор"),
                      ("Уход", "Минимальный: мыть и закрашивать царапины", "Покрытие нужно регулярно обновлять", "Минимальный"),
                      ("Вид", "Ровный и гладкий, каркас с обратной стороны", "Тёплый, природный", "Современный, одно- или двусторонний"),
                      ("Если планировка требует прозрачности", "Не подходит", "Подходит только с зазорами между досками", "Подходит с редким шагом"),
                      ("Ворота", "Из того же листа и цвета", "С деревянным заполнением на стальном каркасе", "С тем же штакетником и цветом")],
             "note": "Цены из нашего прайса, с материалом и стандартным монтажом. Суммы для 30 м посчитаны по тем же диапазонам, точную сумму называем после бесплатного замера."},
            {"type": "sections", "tag": "Правила", "h": "Разрешён ли глухой забор на вашем участке",
             "intro": "Единой высоты или прозрачности забора государство не устанавливает. По § 12 строительного кодекса забор должен соответствовать детальной планировке, а если её нет, общей планировке. Именно планировки чаще всего ставят глухому забору условия.",
             "items": [("Где глухой забор запрещён или ограничен", [
                           "В волости Харку глухие дощатые заборы запрещены, кроме шумовых барьеров и заборов вокруг промышленных территорий, а сетчатый или частично прозрачный деревянный забор у частного дома может быть высотой до 1,5 м. Общая планировка волости Сауэ, как правило, не допускает глухой забор из любого материала, кроме как вокруг промышленной зоны или у транспортной зоны в качестве шумового или защитного барьера.",
                           "В Виймси глухой дощатый забор допускается только вокруг промышленной или транспортной зоны как шумовой или защитный барьер. В волости Кийли забор со стороны улицы должен быть частично прозрачным деревянным, а глухие дощатые заборы запрещены, кроме как вокруг промышленных зданий. В северной части волости Раэ, включая Пеэтри, глухой забор до 1,8 м разрешён только как шумовой барьер, если шум превышает нормы."]),
                       ("Где требуют прозрачности", [
                           "По планировкам Саку, Кейлы и Маарду забор должен быть прозрачным не менее чем на 25%, а в Кейле со стороны улицы нельзя ставить глухую стену выше 1,5 м. В Саку требование прозрачности на жилой земле не распространяется на живую изгородь. В Нымме, как правило, ожидают редкий прозрачный деревянный штакетник или сетку в сочетании с живой изгородью.",
                           'В районах miljööala в Таллинне высота уличного забора, как правило, составляет 1,2–1,5 м, а дощатого 1,5–1,8 м. Требования всех проверенных нами волостей и городов собраны в <a href="/ru/vysota-zabora-v-harjumaa/">статье о высоте и прозрачности забора</a>.']),
                       ("Что сделать до заказа", [
                           "Сначала посмотрите детальную планировку своего участка: для забора это самый точный документ, и она может разрешать или запрещать больше, чем общая планировка. Если формулировка неясна, спросите у специалиста по планировке в волости, подходит ли выбранный забор, и сохраните ответ. Глухой забор соседа ничего не доказывает: его могли поставить до нынешней планировки."])],
             "sources": ["ehs", "harku", "saue", "viimsi", "kiili", "rae", "saku", "keila", "maardu", "nomme", "tallinn"]},
            {"type": "sections", "tag": "Ветер", "h": "Ветер, столбы и основание",
             "intro": "Для ветра глухой забор представляет собой стену: воздух, который прошёл бы сквозь сетку, давит на лист или доски, и эта сила через столбы передаётся на основание.",
             "items": [("Почему глухому забору нужны мощные столбы", [
                           "В сильных порывах шторма на один пролёт шириной 2,5 м и высотой 1,8 м может действовать сила, сравнимая с весом в пару сотен килограммов. Она стремится переломить столб у земли или наклонить основание. Поэтому столбы глухого забора толще, их ставят чаще и глубже, чем у сетчатого, а каркас делают жёстче.",
                           "С высотой нагрузка растёт быстрее, чем кажется: нагрузка у основания столба при высоте глухого забора 1,8 м примерно в 1,4 раза больше, чем при 1,5 м. У моря, в открытом поле и между высокими домами, где ветер усиливается, мы подбираем столбы и основания именно с учётом этого."]),
                       ("Мороз, глина и известняк", [
                           "Столбы глухого забора не должны сдвигаться от морозного пучения: на длинном ровном полотне заметен даже наклон в пару сантиметров. В глинистом грунте основание должно уходить достаточно глубоко и не расширяться кверху, иначе замёрзшая земля захватит его и вытолкнет. Во многих местах Харьюмаа известняк залегает близко к поверхности, и тогда отверстие бурят в камне или крепят столб анкерами, а не ставят его неглубоко.",
                           "Так как столбы глухого забора уходят глубоко, при его установке обычно ведутся земляные работы глубже 30 см. По приложению 1 к строительному кодексу тогда нужны уведомление о строительстве (ehitusteatis) и проект. LuxAed предоставляет технические данные забора для уведомления, а кто готовит проект и подаёт уведомление, договариваемся отдельно."]),
                       ("Глухие ворота на ветру", [
                           'Въездные ворота с тем же профнастилом, доской или штакетником на ветру тоже работают как парус. Сильный ветер может распахнуть створку распашных ворот, нагружая петли и привод, а откатные ворота движутся на роликах и обычно переносят ветер лучше. Если участок ветреный, обсудите это уже при выборе ворот: в этом поможет статья <a href="/ru/otkatnye-ili-raspashnye-vorota/">откатные или распашные ворота</a>.'])],
             "sources": ["lisa1"]},
            {"type": "sections", "tag": "Материалы", "h": "Профнастил, дерево и металлический штакетник подробнее",
             "items": [("Профнастил: самая дешёвая полная защита от взглядов", [
                           'Забор из профнастила делают из оцинкованного стального листа с полимерным покрытием, который крепят к металлическим лагам и столбам. Он закрывает полностью, быстро монтируется и почти не требует ухода: достаточно мыть его и вовремя закрашивать царапины на покрытии. Мы всегда предлагаем <a href="/ru/zabory/profnastil/">готовый забор из профнастила с каркасом и столбами</a>, а не просто лист.',
                           "У профнастила два слабых места: обратная сторона и поведение на ветру. Каркас виден с обратной стороны, а если саморезов мало или лаги слабые, лист на ветру начинает хлопать. Недорогое покрытие с годами может выгореть на солнечной стороне."]),
                       ("Деревянный и дощатый забор: самый тёплый вид", [
                           'Деревянный забор мы ставим на стальной каркас, который держит его ровным, даже когда древесина разбухает и усыхает. Сплошная обшивка, то есть дощатый забор, закрывает полностью, а зазором между досками можно найти баланс между приватностью и ветром. Доски не должны касаться земли, чтобы не впитывать влагу. Подробнее читайте на странице о <a href="/ru/zabory/derevyannye/">деревянных заборах</a>.',
                           "Дерево требует ухода. Без защитного покрытия оно на солнце сереет и начинает трескаться, поэтому масло или краску нужно регулярно обновлять, а на солнечной стороне чаще. Слишком плотно подогнанные доски от влаги коробятся, так что небольшой зазор нужен даже в глухом заборе."]),
                       ("Металлический штакетник: регулируемая приватность", [
                           'Металлический штакетник собирают из оцинкованных и порошково окрашенных планок, которые ставят вертикально или горизонтально. Зазор выбираете вы: редкий односторонний штакетник пропускает свет и ветер, а плотный двусторонний в шахматном порядке закрывает почти полностью. Под углом даже штакетник с зазорами выглядит довольно закрытым, а при взгляде прямо остаётся прозрачным. Все варианты собраны на странице о <a href="/ru/zabory/metallicheskie-lameli/">металлическом штакетнике</a>.',
                           "Штакетник требует мало ухода и держит цвет, но более плотное заполнение означает и большую ветровую нагрузку, и более высокую цену. Если планировка требует прозрачности, не рассчитывайте, что двусторонний штакетник подойдёт: при взгляде прямо он может быть почти глухим. В таком случае до заказа спросите мнение волости."])]},
            {"type": "sections", "tag": "В быту", "h": "Что глухой забор меняет на вашем дворе",
             "items": [("Приватность и высота", [
                           "Забор высотой 1,5 м скрывает человека, сидящего на террасе, но взрослый на улице видит поверх него. От окна второго этажа соседа двор не закроет никакой забор, там помогают деревья, пергола или ширма у террасы. Поэтому сначала решите, от кого и откуда вы хотите закрыться, и уже потом выбирайте высоту и материал."]),
                       ("Снег и тень", [
                           "За глухим забором метель наметает сугробы, нередко прямо на въезд или дорожку. В тени забора снег весной тает позже, а грядка с северной стороны остаётся без солнца. У дороги глухой забор принимает на себя весь снег, который сталкивает снегоуборщик."]),
                       ("Шум", [
                           "Обычный глухой забор приглушает уличный шум лишь немного, в основном потому, что исчезает прямой вид на дорогу. Чтобы снизить шум, преграда должна быть тяжёлой, без щелей и достаточно высокой, поэтому при серьёзном шуме нужно специальное решение."]),
                       ("Гости и доступ", [
                           'За глухим забором не видно, кто стоит у калитки. Это решают <a href="/ru/domofony-videodomofony/">видеодомофон и электрозамок калитки</a>: вы видите гостя или курьера на экране и открываете калитку из дома. В нашем прайсе видеодомофон с электрозамком калитки и стандартным монтажом стоит 650–1 600 €.'])]},
            {"type": "sections", "tag": "Цена", "h": "Сколько стоит глухой забор",
             "items": [("От чего зависит цена", [
                           'Сильнее всего на цену влияют высота, мощность и шаг столбов с учётом ветра, толщина и покрытие листа, плотность штакетника, порода дерева и отделка. Ворота, демонтаж старого забора и сложный грунт считаются отдельно. Точную цену указываем в письменном предложении после бесплатного замера, а все цены собраны в <a href="/ru/ceny/">прайсе</a>.']),
                       ("Глухой только там, где нужно", [
                           "Если всю границу 100 м сделать из профнастила, по нашему прайсу это стоит 7 000–13 500 €. Если глухим сделать только 20 м со стороны улицы, а остальные 80 м из рулонной сетки, та же граница обойдётся в 3 400–6 300 €. Часто достаточно глухого участка со стороны улицы, террасы или окон соседа."])]},
            {"type": "cards", "tag": "Наш совет", "h": "Что мы советуем", "cols": 2,
             "items": [("Планировка до материала", "Проверьте детальную планировку до того, как выбирать профнастил, дерево или штакетник. Если глухой забор не разрешён, не поможет даже самый красивый материал."),
                       ("На ветреном участке штакетник", "У моря и на открытом месте мы предпочитаем металлический штакетник с зазорами: под углом он хорошо закрывает, а ветер нагружает его меньше."),
                       ("Дерево, если готовы ухаживать", "Деревянный забор лучше всего подходит к деревянному дому, но покрытие придётся обновлять. Если не хотите этим заниматься, выбирайте профнастил или металл."),
                       ("Лицевая сторона: договоритесь с соседом", "У профнастила и одностороннего штакетника есть лицевая и обратная сторона. Для забора на границе письменно договоритесь с соседом, куда смотрит лицевая сторона.")]},
            {"type": "cards", "tag": "Частые проблемы", "h": "Что часто идёт не так", "cols": 3,
             "items": [("Забор кренится в шторм", "Столбы глухого забора слишком слабые, стоят редко или у них слишком мелкое основание."),
                       ("Лист хлопает на ветру", "Мало саморезов или слабые лаги, и лист двигается при каждом порыве."),
                       ("Дерево сереет и коробится", "Покрытие не обновляют, доски касаются земли или подогнаны слишком плотно."),
                       ("Дощатый забор был запрещён", "Запрет в планировке или требование прозрачности выясняется уже после заказа."),
                       ("Сугроб на въезде", "Глухой забор поставили с наветренной стороны, и метель наметает снег за ним."),
                       ("Ворота не держатся на ветру", "Ветер распахивает распашные ворота с глухим заполнением, страдают петли и привод.")]},
        ],
        "faq": [
            ("Какой глухой забор самый дешёвый?", "В нашем прайсе дешевле всего забор из профнастила, 70–135 €/м с установкой. Металлический штакетник стоит 85–155 €/м, деревянный забор 90–160 €/м."),
            ("Что делать, если волость требует прозрачный забор?", "Тогда глухой забор из профнастила или досок не подойдёт. Выбирайте металлический штакетник с редким шагом, деревянный забор с зазорами или 3D-панели и добавьте приватность живой изгородью. Например, в Саку требование прозрачности на жилой земле на живую изгородь не распространяется."),
            ("Можно сделать глухим только уличную сторону?", "Да, если планировка разрешает глухой забор со стороны улицы. Например, планировки Кийли, Кейлы и Маарду требуют частичной прозрачности и от уличного забора, поэтому до заказа проверьте детальную планировку своего участка."),
            ("Запрет на дощатый забор касается и профнастила?", "Не рассчитывайте, что нет. Общая планировка Сауэ, как правило, не допускает глухой забор из любого материала, а там, где требуется прозрачность, глухой профнастил тоже не подходит. Если в тексте упомянут только дощатый забор, до заказа уточните у специалиста по планировке в волости."),
            ("Куда смотрит лицевая сторона глухого забора?", "У профнастила и одностороннего штакетника столбы и каркас остаются с обратной стороны. Двусторонний штакетник и деревянный забор, обшитый с обеих сторон, выглядят одинаково с любой стороны. Для забора на границе договоритесь с соседом до работ, куда будет смотреть лицевая сторона."),
            ("Можно ли потом сделать глухой забор выше?", "Редко без замены столбов. Более высокий глухой забор заметно сильнее нагружает столбы ветром, а новая высота должна уложиться в допустимую по планировке. Если планируете высокий забор, сразу подбирайте столбы и основания под него."),
        ],
        "links_keys": ["neighbour", "permit_guide", "mistakes"],
        "links_extra": [("/ru/zabory/metallicheskie-lameli/", "Металлический штакетник", "Зазор, цвет и приватность на выбор.")],
        "cta": ("Поможем выбрать глухой забор", "На бесплатном замере проверим ветер, грунт и планировку и предложим решение для вашего участка.", "/ru/#form", "Оставить заявку"),
    },
    "en": {
        "title": "Privacy fence: profiled sheet, timber or picket? | LuxAed",
        "desc": "Privacy fences installed: profiled sheet €70–135/m, steel picket €85–155/m, timber €90–160/m. We compare privacy, wind, upkeep and municipal rules.",
        "short": "Privacy fence",
        "image": "luxaed-svc-wood",
        "kicker": "Comparison · privacy fences",
        "h1": "Privacy fence:<br><em>profiled sheet, timber or steel picket?</em>",
        "lead": "A solid fence keeps your garden private, but it also has to stand up to wind and snow and fit the municipal rules. We compare the three most common options and explain where a solid fence is allowed at all.",
        "direct": ("Profiled sheet is the cheapest privacy fence, a steel picket fence needs the least upkeep, and timber looks the warmest.",
                   'In our price guide, installed: profiled sheet €70–135/m, steel picket €85–155/m and timber €90–160/m. Before choosing a material, check the plan: in several Harju County municipalities a solid plank fence around a house is not allowed, or the fence has to be partly see-through. If you only need privacy on one side, <a href="/en/mesh-panels-or-chain-link/">roll mesh or 3D mesh panels</a> cost far less on the rest of the boundary.'),
        "blocks": [
            {"type": "table", "tag": "Comparison", "h": "Three privacy fences side by side",
             "headers": ("", "Profiled sheet", "Timber", "Steel picket"),
             "rows": [("Price installed", "€70–135/m", "€90–160/m", "€85–155/m"),
                      ("30 m fence", "€2,100–4,050", "€2,700–4,800", "€2,550–4,650"),
                      ("Privacy", "Complete", "Complete when close-boarded, high with gaps", "Medium to complete, depends on gap and layout"),
                      ("Wind load", "High", "Close boarding takes a high load", "Lower when the pickets are spaced"),
                      ("Upkeep", "Minimal: wash it, touch up scratches", "The finish needs renewing regularly", "Minimal"),
                      ("Look", "Even and smooth, frame on the back", "Warm and natural", "Modern, single- or double-sided"),
                      ("Where the plan requires transparency", "Not suitable", "Only with gaps between boards", "Suitable with wide spacing"),
                      ("Gates", "Same sheet and colour", "Timber infill on a steel frame", "Same pickets and colour")],
             "note": "Prices are from our price guide and include materials and standard installation. The 30 m figures are calculated from the same ranges; we confirm the exact amount after a free site visit."},
            {"type": "sections", "tag": "Rules", "h": "Is a solid fence allowed on your plot?",
             "intro": "No national rule sets fence height or transparency. Under § 12 of the Building Code a fence must comply with the detailed plan, or the general plan if there is none, and that is where most limits on solid fences come from.",
             "items": [("Where solid fences are banned or restricted", [
                           "Harku Municipality bans solid close-boarded fences except as noise barriers or around industrial sites, and allows a mesh or partly transparent timber fence at a house up to 1.5 m tall. The Saue general plan generally allows no opaque fence of any material, except around industrial areas or as a noise or safety barrier by traffic areas.",
                           "Viimsi allows a solid plank fence only around industrial or traffic areas as a noise or safety barrier. Kiili requires a partly transparent timber fence on the street side and bans solid plank fences except around industrial buildings. In northern Rae, including Peetri, a solid fence up to 1.8 m is allowed only as a noise barrier where noise exceeds the limits."]),
                       ("Where transparency is required", [
                           "The Saku, Keila and Maardu plans require fences to be at least 25% transparent, and Keila allows no opaque wall over 1.5 m on the street side. In Saku the transparency rule on residential land does not apply to hedges. In Nõmme the plan generally expects a sparse, see-through timber picket fence or mesh combined with a hedge.",
                           'In the milieu-value areas (miljööala) of Tallinn, street fences are generally 1.2–1.5 m tall and close-boarded fences 1.5–1.8 m. Our <a href="/en/fence-height-rules-harju-county/">fence height and transparency guide</a> collects the rules of every municipality we checked.']),
                       ("What to do before you order", [
                           "Start with the detailed plan for your plot, the most precise document for a fence, which may allow or forbid more than the general plan. If the wording is unclear, ask the municipality's planning officer whether your chosen fence is acceptable and keep the reply. A neighbour's solid fence proves nothing: it may predate the current plan."])],
             "sources": ["ehs", "harku", "saue", "viimsi", "kiili", "rae", "saku", "keila", "maardu", "nomme", "tallinn"]},
            {"type": "sections", "tag": "Wind", "h": "Wind, posts and foundations",
             "intro": "To the wind, a solid fence is a wall: the air that would pass through mesh now pushes on the sheet or boards, and that force travels down the posts into the foundations.",
             "items": [("Why a solid fence needs heavier posts", [
                           "In strong storm gusts, a single solid bay 2.5 m wide and 1.8 m tall can take a force comparable to the weight of a couple of hundred kilograms, trying to snap the post at ground level or tip its foundation. That is why solid fences get thicker posts, set closer and deeper than for mesh, and a stiffer frame.",
                           "Height raises the load faster than you might expect: the load at the foot of a post on a 1.8 m solid fence is about 1.4 times that on a 1.5 m fence. By the sea, in open fields and between taller buildings where the wind picks up, we size posts and foundations with this in mind."]),
                       ("Frost, clay and limestone", [
                           "Frost heave must not move these posts, as even a couple of centimetres of lean shows on a long, smooth face. In clay the footing has to go deep enough and must not widen towards the top, or the frozen ground grips and lifts it. Where limestone lies close to the surface, as in many parts of Harju County, the hole is drilled into the rock or the post anchored to it rather than left shallow.",
                           "Because the posts go deep, building a solid fence usually involves digging deeper than 30 cm, and Annex 1 of the Building Code then requires a building notice and a design. LuxAed provides the technical data of the fence for the notice; who prepares the design and files the notice is agreed separately."]),
                       ("Solid gates in the wind", [
                           'A vehicle gate with the same sheet, boards or pickets is a sail too. Strong wind can blow a swing-gate leaf open, straining the hinges and motor, while a sliding gate runs on rollers and generally copes better. On a windy plot, raise this when choosing the gate; our guide to <a href="/en/sliding-or-swing-gate/">sliding or swing gates</a> helps.'])],
             "sources": ["lisa1"]},
            {"type": "sections", "tag": "Materials", "h": "Profiled sheet, timber and steel pickets in detail",
             "items": [("Profiled sheet: the cheapest complete screen", [
                           'A profiled-sheet fence is galvanised, polymer-coated steel sheet fixed to steel rails and posts. It screens completely, goes up quickly and needs little care beyond washing and prompt touching-up of scratches. We always supply a <a href="/en/fences/profiled-sheet/">finished profiled-sheet fence with frame and posts</a>, not just the sheet.',
                           "Its weak points are the back and the wind. The frame shows on the back, and too few screws or weak rails make the sheet rattle in the wind. A cheaper coating can fade on the sunny side over the years."]),
                       ("Timber and close-boarded fences: the warmest look", [
                           'We build timber fences on a steel frame that keeps them straight as the wood swells and dries. Close boarding screens completely, gaps between the boards balance privacy against wind, and the boards are kept off the ground so they do not soak up moisture. Read more about our <a href="/en/fences/wooden/">wooden fences</a>.',
                           "Timber needs care. Without a protective finish it turns grey in the sun and starts to crack, so the oil or paint must be renewed regularly, more often on the sunny side. Boards fitted too tightly warp as they take up moisture, so even a close-boarded fence needs small gaps."]),
                       ("Steel picket: adjustable privacy", [
                           'A steel picket fence is made of galvanised, powder-coated pickets fitted vertically or horizontally. You choose the gap: a sparse single-sided fence lets light and wind through, while a dense double-sided, staggered layout screens almost completely. Seen at an angle, even a spaced picket fence looks fairly closed, yet straight on it stays see-through. See the options on our <a href="/en/fences/steel-picket/">steel picket fence</a> page.',
                           "Steel pickets need little care and hold their colour, but denser infill means a higher wind load and a higher price. If the plan requires transparency, do not assume a double-sided layout will qualify, as straight on it may look almost solid; ask the municipality before you order."])]},
            {"type": "sections", "tag": "Everyday life", "h": "What a solid fence changes in your garden",
             "items": [("Privacy and height", [
                           "A 1.5 m fence hides someone sitting on the terrace, but an adult standing in the street can see over it. No fence hides your garden from a neighbour's upstairs window; trees, a pergola or a screen by the terrace help there. Decide who you want to screen, and from where, before choosing height and material."]),
                       ("Snow and shade", [
                           "Drifting snow piles up behind a solid fence, often right on the driveway or path. In its shade snow melts later in spring and a bed on the north side loses its sun, while by a road the fence takes all the snow the plough pushes at it."]),
                       ("Noise", [
                           "An ordinary solid fence softens road noise only slightly, mostly by hiding the road from view. Cutting noise takes a heavy, gap-free barrier of sufficient height, so serious noise needs a purpose-built solution."]),
                       ("Visitors and access", [
                           'Behind a solid fence you cannot see who is at the pedestrian gate. A <a href="/en/intercoms-video-intercoms/">video intercom with an electric lock</a> solves that: you see a guest or courier on screen and let them in from the house. In our price guide, a video intercom with a pedestrian-gate lock costs €650–1,600 with standard installation.'])]},
            {"type": "sections", "tag": "Price", "h": "What a privacy fence costs",
             "items": [("What drives the price", [
                           'Height, post strength and spacing for the wind, sheet thickness and coating, picket density, and the timber and its finish drive the price most. Gates, old-fence removal and difficult ground are priced separately. The exact price comes in a written quote after a free site visit, and all prices are in our <a href="/en/prices/">price guide</a>.']),
                       ("Solid only where you need it", [
                           "A 100 m boundary built entirely in profiled sheet costs €7,000–13,500 in our price guide. Make only the 20 m street side solid and the other 80 m roll mesh, and the same boundary costs €3,400–6,300. A solid run towards the street, the terrace or a neighbour's windows is often enough."])]},
            {"type": "cards", "tag": "Our advice", "h": "What we recommend", "cols": 2,
             "items": [("The plan before the material", "Check the detailed plan before choosing sheet, timber or pickets. If a solid fence is not allowed, even the best-looking material will not help."),
                       ("Steel pickets on a windy plot", "By the sea and on open land we prefer a spaced steel picket fence: it screens well at an angle, and the wind loads it less."),
                       ("Timber if you are ready to maintain it", "Timber is the warmest choice for a timber house, but the finish will need renewing. If you do not want to do that, choose sheet or steel."),
                       ("The good face: agree with your neighbour", "Profiled sheet and single-sided pickets have a front and a back. On a boundary fence, agree in writing with your neighbour which way the good face points.")]},
            {"type": "cards", "tag": "Common problems", "h": "What often goes wrong", "cols": 3,
             "items": [("The fence leans after a storm", "The posts of the solid fence are too weak, too far apart or on too shallow a footing."),
                       ("The sheet rattles in the wind", "Too few screws or weak rails let the sheet move with every gust."),
                       ("The timber greys and warps", "The finish is not renewed, and the boards touch the ground or are fitted too tightly."),
                       ("A plank fence was not allowed", "The ban or transparency rule in the plan only comes to light after the order."),
                       ("A snowdrift on the driveway", "The solid fence stands on the windward side and drifting snow piles up behind it."),
                       ("The gate will not stay put in the wind", "Wind blows open a solid swing-gate leaf, straining the hinges and motor.")]},
        ],
        "faq": [
            ("Which privacy fence is the cheapest?", "In our price guide, profiled sheet is the most affordable at €70–135/m installed. Steel picket is €85–155/m and timber €90–160/m."),
            ("What if the municipality requires a see-through fence?", "Then a solid profiled-sheet or plank fence will not do. Choose a spaced steel picket fence, a timber fence with gaps or 3D mesh panels, and add privacy with a hedge. In Saku, for example, the transparency rule on residential land does not apply to hedges."),
            ("Can only the street side be solid?", "Yes, where the plan allows a solid fence on the street side. The Kiili, Keila and Maardu plans, for example, require partial transparency on street fences too, so check the detailed plan for your plot before ordering."),
            ("Does a ban on plank fences also cover profiled sheet?", "Do not assume it does not. The Saue general plan generally allows no opaque fence in any material, and where a plan requires transparency, solid sheet does not qualify either. If the wording only mentions plank fences, check with the municipality's planning officer before you order."),
            ("Which side of a privacy fence faces out?", "On profiled sheet and single-sided pickets, the posts and frame stay on the back. Double-sided pickets and timber boarded on both sides look the same from either side. On a boundary fence, agree with your neighbour before work starts which way the good face points."),
            ("Can a solid fence be made taller later?", "Rarely without replacing the posts. A taller solid fence puts much more wind load on the posts, and the new height must still fit within the height the plan allows. If you may want a taller fence, have the posts and foundations sized for it from the start."),
        ],
        "links_keys": ["neighbour", "permit_guide", "mistakes"],
        "links_extra": [("/en/fences/steel-picket/", "Steel picket fences", "Choose the gap, colour and privacy.")],
        "cta": ("We help you choose a privacy fence", "At a free site visit we check the wind, ground and plan and suggest the right solution for your plot.", "/en/#form", "Get a quote"),
    },
}
