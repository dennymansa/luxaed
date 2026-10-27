# LuxAed article rewrite: panel_vs_mesh (ET / RU / EN).
# Paths: /paneelaed-voi-vorkaed/, /ru/3d-zabor-ili-setka-rabitsa/, /en/mesh-panels-or-chain-link/
#
# Prices: only the LuxAed price table (FACTS_prices.md). The 20 m, 50 m, 100 m and 120 m totals are
# plain multiplications of those ranges (e.g. 50 m x 25-45 = 1 250-2 250).
# Legal facts: only FACTS.md (keys tehn, ehs, lisa1) and the municipal_rules table (keys saku, keila,
# maardu, harku, tallinn, nomme). No new official source was added, so NEW_SRC is empty.
# Product details (panel width about 2.5 m, heights 1.23-2.03 m, RAL 7016 / 6005, PVC-coated roll
# mesh, braced corner posts, line wires, gravel boards, 2D panel is stiffer) match the LuxAed
# service pages /aiad/paneelaed/ and /aiad/vorkaed/.

NEW_SRC = {}

ARTICLE = {
    "et": {
        "title": "Võrkaed või 3D paneelaed: mis vahe ja kumb valida? | LuxAed",
        "desc": "Rullvõrkaed maksab koos paigaldusega 25–45 €/jm, 3D paneelaed 35–60 €/jm. Võrdleme jäikust, välimust, sobivust kaldele ja koerale ning väravaid.",
        "short": "Võrkaed või 3D paneelaed",
        "image": "luxaed-3d-mesh-fence-1",
        "kicker": "Võrdlus · võrkaiad",
        "h1": "Võrkaed<br><em>või 3D paneelaed?</em>",
        "lead": "Mõlemad aiad lasevad läbi valgust ja tuult, kuid aastate jooksul käituvad nad erinevalt. Rullvõrk on soodsam ja järgib maapinda, paneelaed on jäigem, püsib kauem sirge ja näeb korrastatum välja.",
        "direct": ("Pika, kaldega või tagumise piiri jaoks valige rullvõrk, tänava poole ja koeraga hoovi 3D paneelaed.",
                   'Meie hinnatabelis maksab rullvõrkaed koos paigaldusega 25–45 €/jm ja 3D paneelaed 35–60 €/jm, nii et 50 m piiril on vahe tavaliselt 500–750 eurot. Rullvõrk püsib sirge ainult toestatud nurgapostide ja õige pingutusega, jäik paneel hoiab kuju ise. Kui te pole veel kindel, kas vajate üldse läbipaistvat aeda, alustage <a href="/kuidas-valida-aeda/">aia valiku juhendist</a>.'),
        "blocks": [
            {"type": "table", "tag": "Võrdlus", "h": "Rullvõrk ja 3D paneelid kõrvuti",
             "headers": ("", "Rullvõrkaed", "3D paneelaed"),
             "rows": [("Hind koos paigaldusega", "25–45 €/jm", "35–60 €/jm"),
                      ("50 m aed", "1 250–2 250 €", "1 750–3 000 €"),
                      ("Ehitus", "Võrk pingutatakse postide vahele, üla- ja alaservas pingutustraat", "Jäigad keevitatud paneelid, post iga paneeli otsas"),
                      ("Kuju aastate pärast", "Püsib sirge, kui nurgad on toestatud ja pingutus õige", "Ei vaju, kuid näitab kohe iga kerkinud posti"),
                      ("Kaldega krunt", "Järgib laugjat kallet ja ebatasast maad", "Paigaldatakse astmetena või kalde järgi"),
                      ("Tuul", "Väike, kuni võrku ei kaeta kanga või hekiga", "Väike, kuni paneele ei kaeta kanga või ribadega"),
                      ("Üleronimine", "Rombikujuline silm annab jalale toe", "Kitsas silm ja jäikus teevad selle raskemaks"),
                      ("Parandus pärast lööki", "Mõlk pingutatakse välja, punutud võrku saab punuda uue tüki", "Vahetatakse kahjustatud paneel"),
                      ("Välimus", "Lihtne ja maalähedane", "Korrastatud ja kaasaegne"),
                      ("Väravad", "Võrk- või paneeltäitega raamis", "Sama paneeli ja tooniga")],
             "note": "Hinnad on meie hinnatabelist ja sisaldavad materjali ning tavapaigaldust. 50 m hinnad on arvutatud samadest vahemikest, täpse summa anname pärast tasuta mõõdistust."},
            {"type": "sections", "tag": "Ehitus", "h": "Mille poolest need aiad erinevad",
             "intro": "Kui kaalute, kas valida võrkaed või paneelaed, alustage ehitusest. Mõlemad on tsingitud terastraadist, kuid üks on painduv võrk ja teine jäik sektsioon, ning sellest tulenevad peaaegu kõik erinevused hinnas, paigalduses ja vastupidavuses.",
             "items": [("Rullvõrk: aed, mida hoiab pingutus", [
                           "Rullvõrk on kas punutud rombikujulise silmaga või keevitatud ristkülikukujulise silmaga. See tuuakse objektile rullides, pingutatakse postide vahele ning üla- ja alaserva tõmmatakse pingutustraat. Traat on tsingitud või tsingitud ja PVC-kattega, mis võimaldab valida näiteks rohelise tooni.",
                           "Rullvõrgu tugevus ei ole võrgus, vaid nurga- ja lõpp-postides. Need kannavad kogu pingutusjõudu, seetõttu toestatakse need kaldtugedega ja rajatakse kindla alusega. Vahepostid on kergemad ja paigaldatakse tavaliselt 2,5–3 m vahedega. Kui nurgapost vähegi järele annab, lõtvub kogu lõik."]),
                       ("3D paneelid: jäik sektsioon igas postivahes", [
                           "3D paneel on keevitatud terastraadist sektsioon, millele annavad jäikuse V-kujulised painutused. Paneeli laius on tavaliselt umbes 2,5 m ja levinumad kõrgused on 1,23–2,03 m. Iga paneeli otsas on post, mille külge paneel kinnitatakse klambritega. Tsingitud ja pulbervärvitud pind ei vaja värvimist. Populaarseimad toonid on antratsiit RAL 7016 ja roheline RAL 6005.",
                           "Paneel hoiab kuju ise, seega pole aias midagi pingutada. Selle eest peavad postid olema sentimeetri täpsusega õigel kaugusel ja kõrgusel, muidu paneel ei mahu vahele või aia ülaserv jääb laineliseks. Kui vajate veel jäigemat aeda näiteks ettevõtte territooriumile, on järgmine valik topeltvarrastega 2D paneelaed, mis maksab meie hinnatabelis 50–85 €/jm."]),
                       ("Mida see igapäevaselt tähendab", [
                           "Rullvõrku saab käega sisse suruda ja punutud võrgu silmas leiab jalg toe, nii et sellest on lihtsam üle ronida. 3D paneeli kitsas püstine silm ja jäikus teevad ronimise raskemaks. Paneeli ühes servas on lühikesed traadiotsad: ülaservas raskendavad need üleronimist, alaservas on aed lastele ohutum.",
                           'Rullvõrk jääb maastikus vähem silma ja sobib suvila, aiamaa või metsaäärse krundi ilmega. Paneelaed mõjub korrastatult ja sobib moodsa maja tänavafrondile. Paigaldame nii <a href="/aiad/vorkaed/">rullvõrkaedu</a> kui ka <a href="/aiad/paneelaed/">3D paneelaedu</a> koos samas stiilis väravatega.'])]},
            {"type": "sections", "tag": "Ilm", "h": "Tuul, lumi ja külm Eesti oludes",
             "items": [("Tuul", [
                           "Kumbki aed ei jää tuulele ette, sest õhk liigub võrgust peaaegu takistuseta läbi. Seepärast sobivad mõlemad ka mere äärde ja lagedale põllule. Probleem tekib siis, kui võrgule lisatakse varjekangas või varjeribad või kui hekk ja ronitaimed kasvavad sellest tihedalt läbi. Siis muutub aed tuule jaoks peaaegu kinniseks ja postid, mis valiti läbipaistvale aiale, hakkavad tormis kalduma.",
                           'Kui teate juba ette, et soovite osa aiast varjata, öelge seda mõõdistusel. Siis valime selle lõigu postid ja alused suurema koormuse järgi või teeme sinna kohe <a href="/kinnine-aed/">kinnise aia</a>.']),
                       ("Lumi ja lumesahk", [
                           "Tänava ääres lükkab sahk lume koos liiva ja kividega otse vastu aeda. Rullvõrgu alumine osa surutakse sellest välja ja võrk jääb kõveraks. 3D paneel peab paremini vastu, kuid tugev löök painutab selle jäädavalt. Mõlemal juhul aitab, kui aed jääb teest veidi eemale.",
                           "Erinevalt kinnisest aiast ei kuhja tuisk võrgu taha hangesid, sest tuul liigub võrgust läbi."]),
                       ("Külmakerge ja paekivi", [
                           "Mõlema aia suurim oht on külmakerge. Savises ja niiskes pinnases tõstab külmunud maa talvel ebasobiva alusega posti üles ja kevadel ei vaju see enam täpselt tagasi. Eriti kergesti tõuseb post, mille betoon on pealt laiem kui alt ja moodustab maas seene.",
                           'Rullvõrgu puhul ei paista väike liikumine kohe välja, kuid kui nurgapost kaldub, lõtvub kogu lõik. Paneelaias on kerkinud post kohe näha astmena aia ülaservas. Paljudes Harjumaa kohtades on paekivi maapinna lähedal. Siis puuritakse auk kivisse või ankurdatakse post kivi külge, selle asemel et jätta see madalaks. Kui aed juba kaldub, lugege, kuidas <a href="/aia-remont/viltu-aed/">viltu vajunud aeda ja poste remontida</a>.'])]},
            {"type": "sections", "tag": "Paigaldus", "h": "Kalle, postid ja väravad",
             "items": [("Kaldega krunt", [
                           "Rullvõrk on painduv ning järgib laugjat kallet ja ebatasast maad. 3D paneelid on ristkülikud: laugel kaldel saab neid iga posti juures veidi allapoole nihutada, järsemal kaldel paigaldatakse need astmetena. Iga astme alla jääb siis kolmnurkne vahe, mis suletakse betoonist aluslaua või pinnasega.",
                           'Astmed teevad aia iga paneeli madalama otsa juures kõrgemaks. Kui planeering ei ütle teisiti, mõõdetakse ehitise tehniliste andmete määruse järgi kõrgust aeda vahetult ümbritsevast maapinnast, kaldel madalaima ja kõrgeima maapinna keskmisest. Kui lubatud kõrgus on näiteks 1,5 m, valige paneel nii, et aed mahuks selle sisse ka astmete kohal. Valdade nõuded on koos <a href="/aia-korgus-harjumaal/">aia kõrguse juhendis</a>.']),
                       ("Postid ja alus", [
                           "Rullvõrgu aias kannavad koormust nurga-, lõpp- ja väravapostid, paneelaias jaotub see ühtlasemalt iga paneeli vahel olevatele postidele. Postide sügavus ja alus valitakse pinnase järgi. Enne puurimist selgitage välja maa-aluste kaablite asukoht, sest elektri- ja sidekaabli kaitsevööndis ei tohi ilma omaniku nõusolekuta kaevata sügavamale kui 0,3 m ega kasutada löökmehhanisme, näiteks postirammi.",
                           'Ka kerge võrkaed võib vajada ehitusteatist. Kui aia ehitamisega kaasnevad kaevetööd sügavamal kui 30 cm, on ehitusseadustiku lisa 1 järgi vaja ehitusteatist ja ehitusprojekti, olgu täiteks võrk või paneel. Kuidas teatis esitada, selgitab <a href="/aia-ehitusteatis/">ehitusteatise juhend</a>.']),
                       ("Väravad", [
                           "Väravad tasub planeerida koos aiaga. Paneelaia jalg- ja sõiduvärav tehakse tavaliselt sama paneeli ja tooniga, rullvõrkaia väravad aga võrk- või paneeltäitega raamis. Väravapost on alati tugevam ja sügavama alusega kui aiapost, sest värava raskus ja liikumine koormavad seda pidevalt.",
                           "Lühikesel tänavafrondil maksab värav rohkem kui aed ise. Meie hinnatabeli järgi maksab 20 m 3D paneelaeda 700–1 200 €, automaatikaga liugvärav aga 2 100–3 000 €. Kui automaatika tuleb alles hiljem, laske kaablile kaitsetoru maasse panna juba aia ehitamisel."])],
             "sources": ["tehn", "ehs", "lisa1"]},
            {"type": "text", "tag": "Planeering", "h": "Kus võrk- ja paneelaed on lubatud",
             "paras": ["Kuna mõlemad aiad on läbipaistvad, vastavad need tavaliselt ka planeeringutele, mis nõuavad aialt läbipaistvust. Näiteks Saku, Keila ja Maardu planeeringute järgi peab aed olema vähemalt 25% ulatuses läbipaistev ja Harku vallas tohib eramu võrkaed olla kuni 1,5 m kõrge.",
                       "Erand on Tallinna miljööalad, kus võrk- ja keevispaneelaeda ei peeta sobivaks. Erandina võib see olla kruntide vahel, kui tihe hekk või ronitaimed katavad selle täielikult, kuid tänava poole mitte, ja linn otsustab iga juhtumi puhul eraldi. Nõmmel on üldjuhul oodatud hõre läbipaistev puitlippaed või hekiga kombineeritud võrkaed ning kruntide vahel võib olla võrkaed."],
             "sources": ["saku", "keila", "maardu", "harku", "tallinn", "nomme"]},
            {"type": "sections", "tag": "Hind", "h": "Mis maksab ja millest hind sõltub",
             "items": [("Pikema piiri hind", [
                           '100 m piiril maksab rullvõrkaed koos materjali ja tavapaigaldusega 2 500–4 500 € ja 3D paneelaed 3 500–6 000 €. Kõik hinnad ja näidisarvutused leiate <a href="/hinnad/">hinnatabelist</a>.']),
                       ("Mis muudab lõpphinda", [
                           "Rullvõrgu hinda tõstavad nurgad, sest iga nurk ja lõpp vajab tugevat toestatud posti. Paneelaia hinda tõstavad kõrgus, aluslauad ja kalle, sest astmetega paigaldus nõuab rohkem tööd. Mõlemal juhul lisanduvad väravad, vana aia eemaldamine ja äravedu ning pinnase eripärad, näiteks paekivi või vesine savi.",
                           "Täpse hinna anname kirjalikus pakkumises pärast tasuta mõõdistust. Soovi korral arvutame mõlemad variandid ja ka kombinatsiooni, et näeksite vahet kogu aia, mitte ühe meetri kaupa."]),
                       ("Hooldus", [
                           "Kumbki aed ei vaja värvimist. Kord aastas tasub üle vaadata postid, klambrid ja pingutus ning trimmeri või niiduki tekitatud kriimud üle värvida, et rooste ei hakkaks katte alt levima. Rullvõrku saab vajadusel järele pingutada, paneelaias vaadake kevadel üle, kas mõni post on kerkinud."])]},
            {"type": "cards", "tag": "Meie soovitus", "h": "Mida me ise soovitame", "cols": 2,
             "items": [("Tänava poole paneel, tagapiirile rullvõrk", "120 m krundipiiri puhul, millest 25 m jääb tänava poole, maksab see kombinatsioon meie hinnatabeli järgi 3 250–5 775 €. Ainult rullvõrk maksaks 3 000–5 400 € ja ainult paneelaed 4 200–7 200 €, nii et korrastatud tänavafront lisab vaid paarsada eurot."),
                       ("Nurgapostide pealt ei tasu kokku hoida", "Rullvõrgu eluea määravad nurga- ja lõpp-postid ning nende toestus. Pakkumine, kus nurgad on toestamata, tähendab sageli järelpingutamist juba paari talve pärast."),
                       ("Kaldel otsustab mõõdistus", "Kas paneelid tulevad astmetena või kalde järgi, selgub kõrguste mõõtmisel. Näitame enne tööd, kui suured vahed astmete alla jäävad ja kuidas me need sulgeme."),
                       ("Mõelge väravatele kohe", "Sama täitega väravad teevad aiast terviku ja väravapostid saab kohe tugevama alusega õigesse kohta. Hiljem lisatud värav tähendab sageli aia osalist lahtivõtmist.")]},
            {"type": "cards", "tag": "Levinud probleemid", "h": "Mis läheb sageli valesti", "cols": 3,
             "items": [("Rullvõrk vajub", "Nurga- ja lõpp-postid on toestamata või pingutustraat puudub, nii et võrk lõtvub paari talvega."),
                       ("Paneelide joon on laineline", "Postid on seatud eri kõrgusele või on mõni neist külmaga kerkinud."),
                       ("Astmete alla jääb auk", "Kaldel paigaldatud paneelide alla jääb kolmnurkne vahe, millega ei arvestatud."),
                       ("Varjekangas kallutas postid", "Võrgule lisati kangas või ribad, kuid postid olid valitud läbipaistvale aiale."),
                       ("Sahk surus võrgu välja", "Aed on teele liiga lähedal ja lumi lükatakse otse vastu võrku."),
                       ("Koer pääseb alt läbi", "Alumine vahe jäi liiga suureks ja aluslauda ei paigaldatud.")]},
        ],
        "faq": [
            ("Kas 3D paneelaed on rullvõrgust palju kallim?", "Meie hinnatabelis on rullvõrkaed 25–45 €/jm ja 3D paneelaed 35–60 €/jm koos paigaldusega. 50 m piiril on vahe tavaliselt 500–750 eurot, kuid väravad ja nurgad mõjutavad lõpphinda sageli rohkem kui aia tüüp."),
            ("Kumb püsib kauem sirge?", "Õigesti paigaldatud paneelaed, sest jäik paneel ei veni ega vaju. Rullvõrk püsib sirge siis, kui nurga- ja lõpp-postid on toestatud ja pingutustraadid korralikult pingul. Pinnase liikumise järel võib rullvõrk vajada järelpingutamist, paneelaias tuleb kerkinud post uuesti loodida."),
            ("Kuidas vältida vahet paneeli all?", "Tasandage aiajoon enne paigaldust ja seadke postid nii, et paneeli alaserv jääks maapinna lähedale. Kaldel jäävad astmete alla kolmnurksed vahed, mis suletakse betoonist aluslaua või pinnasega. Koeraga hoovis tasub aluslaud lisada kogu aia ulatuses."),
            ("Kas vanad rullvõrgu postid sobivad 3D paneelidele?", "Tavaliselt mitte. Paneel vajab posti iga paneeli otsas ja sobivaid kinnitusi, vanad postid on aga sageli teise vahega, maapinna juurest roostes või viltu. Mõõdistusel vaatame, kas mõnda neist saab kasutada."),
            ("Kumba on lihtsam parandada, kui aed saab löögi?", "Paneelaias vahetatakse tavaliselt ainult kahjustatud paneel ja vajadusel post, kui sama kõrguse ja tooniga paneel on saadaval. Rullvõrgus saab väiksema mõlgi sageli välja pingutada ja punutud võrgu katkise koha asemele punuda uue tüki. Suurema kahju korral vahetatakse võrk kahe pingutuspunkti vahel."),
            ("Kas paneelaiale võib panna varjeriba või varjekanga?", "Võib, kuid siis koormab tuul aeda peaaegu nagu kinnist seina. Tavalise paneelaia postid on valitud läbipaistvale aiale ja tormis võivad varjatud lõigud kalduma hakata. Kui plaanite varjamist, valime selle lõigu postid ja alused kohe suurema koormuse järgi."),
        ],
        "links_keys": ["neighbour", "road_utilities", "gate_guide"],
        "links_extra": [("/aiad/paneelaed/", "3D paneelaed", "Paigaldus koos postide ja väravatega.")],
        "cta": ("Mõõdame ja arvutame mõlemad variandid", "Tasuta mõõdistusel vaatame piiri, kalde ja pinnase üle ning anname kirjaliku pakkumise nii rullvõrgule kui ka 3D paneelaiale.", "/#form", "Küsi pakkumist"),
    },
    "ru": {
        "title": "Сетка-рабица или 3D-панели: что выбрать для участка | LuxAed",
        "desc": "Сетка-рабица с установкой стоит 25–45 €/м, 3D-забор 35–60 €/м. Сравниваем жёсткость, внешний вид, работу на склоне, защиту от собаки и ворота.",
        "short": "Сетка-рабица или 3D-панели",
        "image": "luxaed-3d-mesh-fence-1",
        "kicker": "Сравнение · сетчатые заборы",
        "h1": "Сетка-рабица<br><em>или 3D-панели?</em>",
        "lead": "Оба забора пропускают свет и ветер, но с годами ведут себя по-разному. Сетка дешевле и повторяет рельеф, а забор из 3D-панелей жёстче, дольше остаётся ровным и выглядит аккуратнее.",
        "direct": ("Для длинной границы, склона или задней стороны участка выбирайте сетку-рабицу, а для фасада и двора с собакой 3D-панели.",
                   'В нашем прайсе забор из рулонной сетки с установкой стоит 25–45 €/м, а из 3D-панелей 35–60 €/м, поэтому на границе 50 м разница обычно составляет 500–750 евро. Сетка остаётся ровной только при укреплённых угловых столбах и правильном натяжении, а жёсткая панель держит форму сама. Если вы ещё не решили, нужен ли вам вообще прозрачный забор, начните с <a href="/ru/kak-vybrat-zabor/">руководства по выбору забора</a>.'),
        "blocks": [
            {"type": "table", "tag": "Сравнение", "h": "Рулонная сетка и 3D-панели рядом",
             "headers": ("", "Рулонная сетка", "3D-панели"),
             "rows": [("Цена с установкой", "25–45 €/м", "35–60 €/м"),
                      ("Забор 50 м", "1 250–2 250 €", "1 750–3 000 €"),
                      ("Конструкция", "Сетка натянута между столбами, по верху и низу натяжная проволока", "Жёсткие сварные панели, столб на каждом стыке"),
                      ("Форма через годы", "Ровная, если углы укреплены и натяжение правильное", "Не провисает, но сразу выдаёт каждый поднявшийся столб"),
                      ("Участок со склоном", "Повторяет плавный склон и неровности", "Ставится ступенями или по уклону"),
                      ("Ветер", "Малая нагрузка, пока сетку не закрыли тканью или живой изгородью", "Малая нагрузка, пока панели не закрыли тканью или лентами"),
                      ("Перелезть", "Ромбическая ячейка даёт опору ноге", "Узкая ячейка и жёсткость мешают"),
                      ("Ремонт после удара", "Вмятину вытягивают, в плетёную сетку вплетают новый кусок", "Меняют повреждённую панель"),
                      ("Внешний вид", "Простой, дачный", "Аккуратный и современный"),
                      ("Ворота", "С сеткой или панелью в раме", "С той же панелью и в том же цвете")],
             "note": "Цены из нашего прайса, с материалом и стандартным монтажом. Суммы для 50 м посчитаны по тем же диапазонам, точную сумму называем после бесплатного замера."},
            {"type": "sections", "tag": "Устройство", "h": "Чем эти заборы отличаются на самом деле",
             "intro": "Если вы выбираете между сеткой-рабицей и 3D-забором, начните с устройства. Оба забора делают из оцинкованной стальной проволоки, но один представляет собой гибкую сетку, а другой жёсткую секцию, и отсюда почти все различия в цене, монтаже и долговечности.",
             "items": [("Сетка-рабица: забор, который держится на натяжении", [
                           "Рулонная сетка бывает плетёной, с ромбической ячейкой (это классическая рабица), или сварной, с прямоугольной ячейкой. Её привозят в рулонах, натягивают между столбами, а по верхнему и нижнему краю протягивают натяжную проволоку. Проволока оцинкованная или оцинкованная с ПВХ-покрытием, которое позволяет выбрать цвет, например зелёный.",
                           "Прочность сетчатого забора зависит не от сетки, а от угловых и концевых столбов. Они принимают на себя всё натяжение, поэтому их укрепляют подкосами и ставят на надёжное основание. Промежуточные столбы легче и стоят обычно через 2,5–3 м. Если угловой столб хоть немного поддаётся, провисает весь пролёт."]),
                       ("3D-панели: жёсткая секция в каждом пролёте", [
                           "3D-панель представляет собой сварную секцию из стальной проволоки, жёсткость которой придают V-образные изгибы. Ширина панели обычно составляет около 2,5 м, а самые распространённые высоты 1,23–2,03 м. На каждом стыке стоит столб, к которому панель крепят хомутами. Оцинкованная и порошково окрашенная поверхность не требует покраски. Чаще всего выбирают антрацит RAL 7016 и зелёный RAL 6005.",
                           "Панель держит форму сама, натягивать ничего не нужно. Зато столбы должны стоять с точностью до сантиметра по расстоянию и высоте, иначе панель не встанет на место или верх забора пойдёт волной. Если нужен ещё более жёсткий забор, например для территории предприятия, посмотрите на забор из 2D-панелей с двойными горизонтальными прутками: в нашем прайсе он стоит 50–85 €/м."]),
                       ("Что это значит в быту", [
                           "Сетку можно продавить рукой, а в ромбической ячейке рабицы нога находит опору, поэтому через неё проще перелезть. Узкая вертикальная ячейка 3D-панели и её жёсткость мешают залезть наверх. На одном краю панели есть короткие выступающие концы проволоки: вверху они мешают перелезть, а внизу делают забор безопаснее для детей.",
                           'Сетка меньше бросается в глаза и подходит к облику дачи, огорода или участка у леса. Забор из 3D-панелей смотрится аккуратно и подходит к фасаду современного дома. Мы ставим и <a href="/ru/zabory/setka-rabitsa/">заборы из сетки-рабицы</a>, и <a href="/ru/zabory/2d-3d-setka/">заборы из 3D-панелей</a> с воротами в том же стиле.'])]},
            {"type": "sections", "tag": "Погода", "h": "Ветер, снег и мороз в эстонских условиях",
             "items": [("Ветер", [
                           "Оба забора почти не задерживают ветер: воздух проходит сквозь сетку практически свободно. Поэтому оба подходят и для участка у моря, и для открытого поля. Проблема появляется, когда на сетку вешают затеняющую ткань или вставляют ленты для приватности или когда сквозь неё густо прорастают живая изгородь и вьющиеся растения. Тогда для ветра забор становится почти глухим, и столбы, подобранные под прозрачный забор, в шторм начинают крениться.",
                           'Если вы заранее знаете, что захотите закрыть часть забора, скажите об этом на замере. Тогда мы подберём столбы и основания для этого участка под большую нагрузку или сразу сделаем там <a href="/ru/gluhoj-zabor/">глухой забор</a>.']),
                       ("Снег и снегоуборщик", [
                           "У дороги снегоуборщик сталкивает снег вместе с песком и камнями прямо на забор. Нижнюю часть сетки выдавливает наружу, и она остаётся выгнутой. 3D-панель держится лучше, но сильный удар гнёт её навсегда. В обоих случаях помогает, если забор стоит немного дальше от дороги.",
                           "В отличие от глухого забора, за сеткой метель не наметает сугробов, потому что ветер проходит насквозь."]),
                       ("Морозное пучение и известняк", [
                           "Главная угроза для обоих заборов заключается в морозном пучении. В глинистом и влажном грунте замёрзшая земля зимой выталкивает столб с неподходящим основанием, а весной он уже не опускается точно на место. Особенно легко поднимается столб, у которого бетон сверху шире, чем снизу, и образует в земле «гриб».",
                           'У сетки небольшое смещение сразу не заметно, но если кренится угловой столб, провисает весь пролёт. На заборе из 3D-панелей поднявшийся столб сразу виден ступенькой по верхнему краю. Во многих местах Харьюмаа известняк залегает близко к поверхности, и тогда отверстие бурят в камне или крепят столб анкерами, а не ставят его неглубоко. Если забор уже покосился, прочитайте, как <a href="/ru/remont-zaborov/pokosilsya-zabor/">отремонтировать покосившийся забор и столбы</a>.'])]},
            {"type": "sections", "tag": "Монтаж", "h": "Склон, столбы и ворота",
             "items": [("Участок со склоном", [
                           "Сетка гибкая и повторяет плавный склон и неровности земли. 3D-панели прямоугольные: на пологом склоне каждую можно немного опустить у столба, а на крутом их ставят ступенями. Тогда под каждой ступенью остаётся треугольный зазор, который закрывают бетонной цокольной плитой или грунтом.",
                           'Ступени делают забор выше у нижнего края каждой панели. Если планировка не говорит иначе, по постановлению о технических данных сооружений высоту измеряют от земли непосредственно вокруг забора, а на склоне берут среднее между самой низкой и самой высокой отметкой земли. Если допустимая высота составляет, например, 1,5 м, подберите панель так, чтобы забор уложился в неё и на ступенях. Требования волостей собраны в <a href="/ru/vysota-zabora-v-harjumaa/">статье о высоте забора</a>.']),
                       ("Столбы и основание", [
                           "В сетчатом заборе нагрузку несут угловые, концевые и воротные столбы, а в заборе из панелей она распределяется равномернее по столбам на каждом стыке. Глубину и основание столбов подбирают по грунту. До бурения выясните, где проходят подземные кабели: в охранной зоне электрического кабеля и кабеля связи без согласия владельца нельзя ни копать глубже 0,3 м, ни пользоваться ударными механизмами, например для забивки столбов.",
                           'Даже лёгкому сетчатому забору может понадобиться уведомление. Если при установке забора ведутся земляные работы глубже 30 см, по приложению 1 к строительному кодексу нужны уведомление о строительстве (ehitusteatis) и проект, будь то сетка или панели. Как подать уведомление, объясняем в <a href="/ru/razreshenie-na-zabor/">статье о разрешении на забор</a>.']),
                       ("Ворота", [
                           "Ворота лучше планировать вместе с забором. Калитку и въездные ворота для забора из 3D-панелей обычно делают с той же панелью и в том же цвете, а для сетки с сетчатым или панельным заполнением в раме. Воротный столб всегда мощнее обычного и стоит на более глубоком основании, потому что вес и движение ворот постоянно его нагружают.",
                           "На коротком фасаде ворота обходятся дороже самого забора. По нашему прайсу 20 м забора из 3D-панелей стоят 700–1 200 €, а откатные ворота с автоматикой 2 100–3 000 €. Если автоматику поставите позже, попросите заложить защитную трубу для кабеля уже при строительстве забора."])],
             "sources": ["tehn", "ehs", "lisa1"]},
            {"type": "text", "tag": "Планировка", "h": "Где разрешены сетчатые и панельные заборы",
             "paras": ["Оба забора прозрачные, поэтому обычно подходят и там, где планировка требует прозрачности. Например, по планировкам Саку, Кейлы и Маарду забор должен быть прозрачным не менее чем на 25%, а в волости Харку сетчатый забор у частного дома может быть высотой до 1,5 м.",
                       "Исключение составляют районы miljööala в Таллинне, где сетчатые и сварные панельные заборы не считаются подходящими. Между участками такой забор допускается в виде исключения, если его полностью скрывает густая живая изгородь или вьющиеся растения, но не со стороны улицы, и город решает каждый случай отдельно. В Нымме, как правило, ожидают редкий прозрачный деревянный штакетник или сетку в сочетании с живой изгородью, а между участками может быть сетка."],
             "sources": ["saku", "keila", "maardu", "harku", "tallinn", "nomme"]},
            {"type": "sections", "tag": "Цена", "h": "Сколько стоит и от чего зависит цена",
             "items": [("Цена длинной границы", [
                           'Для границы 100 м забор из рулонной сетки с материалом и стандартным монтажом стоит 2 500–4 500 €, а из 3D-панелей 3 500–6 000 €. Все цены и примеры расчёта собраны в <a href="/ru/ceny/">прайсе</a>.']),
                       ("Что меняет итоговую цену", [
                           "Цену сетчатого забора повышают углы, потому что каждому углу и концу нужен мощный столб с подкосами. Цену забора из панелей повышают высота, цокольные плиты и склон, потому что монтаж ступенями требует больше работы. В обоих случаях добавляются ворота, демонтаж и вывоз старого забора и особенности грунта, например известняк или мокрая глина.",
                           "Точную цену указываем в письменном предложении после бесплатного замера. По желанию считаем оба варианта и комбинацию, чтобы вы видели разницу для всего забора, а не за один метр."]),
                       ("Уход", [
                           "Ни один из этих заборов не нужно красить. Раз в год стоит осмотреть столбы, хомуты и натяжение, а царапины от триммера или газонокосилки закрасить, чтобы ржавчина не пошла под покрытие. Сетку при необходимости можно подтянуть, а на заборе из панелей весной проверьте, не поднялся ли какой-нибудь столб."])]},
            {"type": "cards", "tag": "Наш совет", "h": "Что мы советуем", "cols": 2,
             "items": [("Панели к улице, сетка сзади", "Если периметр участка 120 м, из них 25 м со стороны улицы, такая комбинация по нашему прайсу стоит 3 250–5 775 €. Только сетка обошлась бы в 3 000–5 400 €, только 3D-панели в 4 200–7 200 €, так что аккуратный фасад добавляет всего пару сотен евро."),
                       ("Не экономьте на угловых столбах", "Срок службы сетчатого забора определяют угловые и концевые столбы с подкосами. Предложение без подкосов на углах часто означает подтяжку сетки уже через пару зим."),
                       ("На склоне решает замер", "Ставить панели ступенями или по уклону, становится ясно после замера высот. До работ покажем, какие зазоры останутся под ступенями и как мы их закроем."),
                       ("Думайте о воротах сразу", "Ворота с тем же заполнением делают забор цельным, а воротные столбы сразу встают на место с усиленным основанием. Ворота, добавленные позже, часто означают частичную разборку забора.")]},
            {"type": "cards", "tag": "Частые проблемы", "h": "Что часто идёт не так", "cols": 3,
             "items": [("Сетка провисает", "Угловые и концевые столбы без подкосов или нет натяжной проволоки, и за пару зим сетка ослабевает."),
                       ("Верх панелей идёт волной", "Столбы выставлены на разную высоту или какой-то из них вытолкнуло морозом."),
                       ("Дыра под ступенями", "Под панелями на склоне остаётся треугольный зазор, который не учли заранее."),
                       ("Ткань наклонила столбы", "На забор повесили затеняющую ткань или ленты, а столбы подбирали под прозрачный забор."),
                       ("Снегоуборщик выдавил сетку", "Забор стоит слишком близко к дороге, и снег сталкивают прямо на сетку."),
                       ("Собака пролезает снизу", "Нижний зазор оставили слишком большим и не поставили цокольную плиту.")]},
        ],
        "faq": [
            ("3D-забор намного дороже сетки-рабицы?", "В нашем прайсе рулонная сетка стоит 25–45 €/м, а 3D-панели 35–60 €/м с установкой. На границе 50 м разница обычно составляет 500–750 евро, но ворота и углы часто влияют на итог сильнее, чем тип забора."),
            ("Что дольше остаётся ровным?", "Правильно установленный забор из 3D-панелей, потому что жёсткая панель не растягивается и не провисает. Сетка остаётся ровной, если угловые и концевые столбы укреплены подкосами, а натяжная проволока хорошо натянута. После подвижек грунта сетку может понадобиться подтянуть, а поднявшийся столб панельного забора заново выставить."),
            ("Как избежать зазора под панелью?", "Выровняйте линию забора до монтажа и выставьте столбы так, чтобы низ панели был близко к земле. На склоне под ступенями остаются треугольные зазоры, их закрывают бетонной цокольной плитой или грунтом. Если во дворе собака, цокольную плиту стоит поставить по всей длине."),
            ("Подойдут ли старые столбы от сетки для 3D-панелей?", "Обычно нет. Панели нужен столб на каждом стыке и подходящие крепления, а старые столбы часто стоят с другим шагом, проржавели у земли или покосились. На замере посмотрим, можно ли использовать какие-то из них."),
            ("Что проще отремонтировать после удара?", "В заборе из 3D-панелей обычно меняют только повреждённую панель и при необходимости столб, если панель той же высоты и цвета ещё можно купить. Небольшую вмятину на сетке часто можно вытянуть, а в плетёную рабицу вплести новый кусок вместо порванного. При серьёзном повреждении меняют сетку между двумя точками натяжения."),
            ("Можно ли повесить на панельный забор затеняющую ткань или ленты?", "Можно, но тогда ветер нагружает забор почти как глухую стену. Столбы обычного панельного забора подобраны под прозрачный забор, и в шторм закрытые участки могут накрениться. Если планируете закрывать забор, подберём столбы и основания этого участка сразу под большую нагрузку."),
        ],
        "links_keys": ["neighbour", "road_utilities", "gate_guide"],
        "links_extra": [("/ru/zabory/2d-3d-setka/", "Забор из 3D-панелей", "Монтаж со столбами и воротами.")],
        "cta": ("Измерим и посчитаем оба варианта", "На бесплатном замере посмотрим границу, склон и грунт и дадим письменное предложение и на сетку, и на 3D-панели.", "/ru/#form", "Узнать цену"),
    },
    "en": {
        "title": "Chain-link vs 3D mesh panel fence: which to choose? | LuxAed",
        "desc": "Roll mesh costs €25–45/m installed and 3D mesh panels €35–60/m. We compare stiffness, looks, slopes, dogs, wind and gates so you can choose the right fence.",
        "short": "Chain-link or 3D mesh panels",
        "image": "luxaed-3d-mesh-fence-1",
        "kicker": "Comparison · mesh fences",
        "h1": "Chain-link<br><em>or 3D mesh panels?</em>",
        "lead": "Both fences let light and wind through, but they age very differently. Roll mesh costs less and follows the ground, while 3D mesh panels are stiffer, stay straight for longer and look tidier.",
        "direct": ("Choose roll mesh for a long, sloping or rear boundary, and 3D mesh panels for the street side or a garden with a dog.",
                   'In our price guide, a roll-mesh fence costs €25–45/m installed and a 3D panel fence €35–60/m, so on a 50 m boundary the difference is usually €500–750. Roll mesh only stays straight with braced corner posts and correct tension, while a rigid panel holds its own shape. If you are not yet sure you want a see-through fence at all, start with our <a href="/en/how-to-choose-a-fence/">guide to choosing a fence</a>.'),
        "blocks": [
            {"type": "table", "tag": "Comparison", "h": "Chain-link and 3D mesh panels side by side",
             "headers": ("", "Chain-link / roll mesh", "3D mesh panels"),
             "rows": [("Price installed", "€25–45/m", "€35–60/m"),
                      ("50 m fence", "€1,250–2,250", "€1,750–3,000"),
                      ("Construction", "Mesh tensioned between posts, line wires top and bottom", "Rigid welded panels, a post at every joint"),
                      ("Shape after years", "Straight if the corners are braced and the tension is right", "Does not sag, but shows every lifted post at once"),
                      ("Sloping plot", "Follows a gentle slope and uneven ground", "Stepped or raked"),
                      ("Wind", "Low, unless the mesh is covered with fabric or a hedge", "Low, unless the panels are covered with fabric or strips"),
                      ("Climbing", "The diamond mesh gives a foothold", "Narrow mesh and stiffness make it harder"),
                      ("Repair after an impact", "Dents are pulled out, a new piece is woven into chain-link", "The damaged panel is replaced"),
                      ("Look", "Simple and rural", "Tidy and modern"),
                      ("Gates", "Mesh or panel infill in a frame", "Same panel and colour")],
             "note": "Prices are from our price guide and include materials and standard installation. The 50 m figures are calculated from the same ranges; we confirm the exact amount after a free site visit."},
            {"type": "sections", "tag": "Construction", "h": "What really separates the two",
             "intro": "Weighing up chain-link against a mesh panel fence? Start with how each is built. Both use galvanised steel wire, but one is a flexible mesh and the other a rigid section, which explains almost every difference in price, installation and durability.",
             "items": [("Chain-link and roll mesh: a fence held up by tension", [
                           "Roll mesh is either woven chain-link with a diamond pattern or welded mesh with rectangular openings. It comes in rolls, is tensioned between the posts and held by line wires along the top and bottom. The wire is galvanised, or galvanised and PVC-coated in a colour such as green.",
                           "Its strength lies in the corner and end posts, not the mesh. They carry all the tension, so they are braced with struts and set on a solid base, while the lighter intermediate posts are usually 2.5–3 m apart. If a corner post gives even slightly, the whole run goes slack."]),
                       ("3D mesh panels: a rigid section in every bay", [
                           "A 3D panel is a welded steel-wire section stiffened by V-shaped bends, usually about 2.5 m wide and most often 1.23–2.03 m tall. Each panel is clamped to a post at every joint. The galvanised, powder-coated finish never needs painting; anthracite RAL 7016 and green RAL 6005 are the most popular colours.",
                           "With nothing to tension, the posts must instead be set to the centimetre, or the panels will not fit and the top line will wave. For a business site, or anywhere you need even more stiffness, the next step up is a 2D panel fence with double horizontal wires, at €50–85/m in our price guide."]),
                       ("What that means day to day", [
                           "Roll mesh gives when pushed, and a foot finds a hold in the diamond mesh of chain-link, so it is easier to climb. The narrow vertical openings and stiffness of a 3D panel make climbing harder. One edge of each panel has short wire ends: at the top they deter climbers, at the bottom they keep the fence safer for children.",
                           'Roll mesh blends into the landscape around a summer house, garden plot or woodland edge, while a 3D panel fence looks ordered in front of a modern house. We install both <a href="/en/fences/roll-mesh/">chain-link and roll-mesh fences</a> and <a href="/en/fences/mesh/">3D mesh panel fences</a>, with gates to match.'])]},
            {"type": "sections", "tag": "Weather", "h": "Wind, snow and frost in Estonian conditions",
             "items": [("Wind", [
                           "Neither fence stands in the way of the wind, so both suit a seaside plot or open fields. The trouble starts when windbreak fabric or privacy strips are added, or a hedge grows densely through the mesh: the fence then acts almost like a solid wall, and posts chosen for an open fence start to lean in storms.",
                           'If you plan to screen part of the fence, tell us at the site visit. We will size the posts and foundations of that stretch for the extra load, or build a <a href="/en/privacy-fence/">solid privacy fence</a> there from the start.']),
                       ("Snow and the plough", [
                           "Along a road, the plough throws snow, sand and stones straight at the fence. Roll mesh gets pushed out at the bottom and stays bowed; a 3D panel copes better, but a hard hit bends it for good. Keeping the fence a little back from the road helps both.",
                           "Unlike a solid fence, mesh does not collect snowdrifts, because the wind blows straight through."]),
                       ("Frost heave and limestone", [
                           "The biggest threat to both fences is frost heave. In wet clay, frozen ground lifts a post with an unsuitable footing, and in spring it does not settle back where it was. A post whose concrete is wider at the top than the bottom, like a mushroom, is lifted most easily.",
                           'On roll mesh a small movement goes unnoticed until a corner post tilts and the whole run slackens; on a panel fence a lifted post shows at once as a step in the top line. In many parts of Harju County limestone lies close to the surface, so the hole is drilled into the rock or the post anchored to it rather than left shallow. If your fence already leans, see how we <a href="/en/fence-repair/leaning-fence/">repair a leaning fence and loose posts</a>.'])]},
            {"type": "sections", "tag": "Installation", "h": "Slopes, posts and gates",
             "items": [("A sloping plot", [
                           "Roll mesh bends to follow a gentle slope and uneven ground. 3D panels are rectangles: on a gentle slope each can be dropped slightly at every post, while steeper ground calls for steps, each leaving a triangular gap underneath that is closed with a concrete gravel board or soil.",
                           'Steps make the fence taller at the lower end of each panel. Unless the plan says otherwise, the regulation on technical data of structures measures height from the ground immediately around the fence, and on a slope from the average of the lowest and highest ground level. With a permitted height of 1.5 m, for example, choose a panel that stays within it at the steps too. The municipal rules are in our <a href="/en/fence-height-rules-harju-county/">fence height guide</a>.']),
                       ("Posts and foundations", [
                           "On roll mesh the load sits on the corner, end and gate posts; on panels it is spread across a post at every joint. Post depth and footing are chosen for the ground. Before drilling, find out where underground cables run: in the protection zone of an electricity or telecom cable you may not dig deeper than 0.3 m or use impact tools such as a post driver without the owner's consent.",
                           'Even a light mesh fence may need a building notice. If building it involves digging deeper than 30 cm, Annex 1 of the Building Code requires a building notice and a design, whether the infill is mesh or panels. Our <a href="/en/fence-permit/">fence permit guide</a> explains how to file one.']),
                       ("Gates", [
                           "Plan the gates with the fence. A 3D panel fence usually gets pedestrian and vehicle gates in the same panel and colour, and roll mesh gets mesh or panel infill in a frame. Gate posts are always heavier and set deeper than fence posts, because the weight and movement of the gate load them constantly.",
                           "On a short frontage the gate costs more than the fence: in our price guide, 20 m of 3D panel fence costs €700–1,200 and an automated sliding gate €2,100–3,000. If automation comes later, have a cable duct laid while the fence is built."])],
             "sources": ["tehn", "ehs", "lisa1"]},
            {"type": "text", "tag": "Planning", "h": "Where mesh and panel fences are allowed",
             "paras": ["Both fences are see-through, so they usually satisfy plans that require transparency: the Saku, Keila and Maardu plans ask for at least 25%, and in Harku Municipality a mesh fence at a house may be up to 1.5 m tall.",
                       "The exception is the milieu-value areas (miljööala) of Tallinn, where mesh and welded-panel fences are not considered suitable. Between plots they may be allowed as an exception if a dense hedge or climbers hide them completely, but never on the street side, and the city decides case by case. In Nõmme the plan generally expects a sparse, see-through timber picket fence or mesh combined with a hedge, with mesh allowed between plots."],
             "sources": ["saku", "keila", "maardu", "harku", "tallinn", "nomme"]},
            {"type": "sections", "tag": "Price", "h": "What it costs and what drives the price",
             "items": [("Prices for a longer boundary", [
                           'On a 100 m boundary, roll mesh comes to €2,500–4,500 and 3D mesh panels to €3,500–6,000, including materials and standard installation. All prices and worked examples are in our <a href="/en/prices/">price guide</a>.']),
                       ("What changes the final price", [
                           "Corners add to the cost of roll mesh, since every corner and end needs a heavy braced post. Height, gravel boards and slope add to the cost of panels, since stepped installation takes more work. Both depend on gates, removal and disposal of the old fence, and ground conditions such as limestone or waterlogged clay.",
                           "The exact price comes in a written quote after a free site visit, and on request we price both options and a combination so you can compare whole fences rather than metres."]),
                       ("Maintenance", [
                           "Neither fence needs painting. Once a year, check the posts, clamps and tension, and touch up strimmer or mower scratches before rust spreads under the coating. Roll mesh can be re-tensioned; on a panel fence, check each spring that no post has lifted."])]},
            {"type": "cards", "tag": "Our advice", "h": "What we recommend", "cols": 2,
             "items": [("Panels at the front, roll mesh at the back", "On a 120 m boundary with 25 m facing the street, this mix costs €3,250–5,775 in our price guide, against €3,000–5,400 for roll mesh all round and €4,200–7,200 for panels all round. A tidy frontage adds only a couple of hundred euros."),
                       ("Don't save on corner posts", "Braced corner and end posts decide how long roll mesh lasts. A quote without bracing often means re-tensioning within a couple of winters."),
                       ("On a slope, the site visit decides", "Whether panels are stepped or raked becomes clear once the levels are measured, and we show you in advance how big the gaps under the steps will be and how we will close them."),
                       ("Plan the gates now", "Gates with the same infill make the fence look like one piece, and their posts go in the right place on stronger footings. Adding a gate later often means taking part of the fence apart.")]},
            {"type": "cards", "tag": "Common problems", "h": "What often goes wrong", "cols": 3,
             "items": [("Roll mesh sags", "Corner and end posts are not braced or line wires are missing, so the mesh slackens within a couple of winters."),
                       ("The panel line waves", "Posts were set at different heights or one of them has been lifted by frost."),
                       ("Gaps under the steps", "Stepped panels on a slope leave triangular gaps that nobody planned for."),
                       ("Fabric tilted the posts", "Windbreak fabric or strips were added, but the posts were chosen for an open fence."),
                       ("The plough pushed the mesh out", "The fence stands too close to the road and snow is pushed straight into it."),
                       ("The dog gets out underneath", "The bottom gap was left too large and no gravel board was fitted.")]},
        ],
        "faq": [
            ("Are 3D panels much more expensive than roll mesh?", "In our price guide, roll mesh is €25–45/m and 3D panels €35–60/m installed. On a 50 m boundary the difference is usually €500–750, but gates and corners often affect the total more than the fence type."),
            ("Which stays straight for longer?", "A correctly installed 3D panel fence, because a rigid panel does not stretch or sag. Roll mesh stays straight when the corner and end posts are braced and the line wires are properly tensioned. After ground movement roll mesh may need re-tensioning, while a lifted post on a panel fence has to be re-levelled."),
            ("How do I avoid a gap under the panels?", "Level the fence line before installation and set the posts so the bottom of each panel sits close to the ground. On a slope, the steps leave triangular gaps that are closed with a concrete gravel board or soil. With a dog in the garden, it is worth fitting gravel boards along the whole fence."),
            ("Can old chain-link posts be reused for 3D panels?", "Usually not. Panels need a post at every joint and matching fixings, while old posts are often at a different spacing, rusted at ground level or leaning. At the site visit we check whether any of them can be reused."),
            ("Which is easier to repair after an impact?", "On a 3D panel fence usually only the damaged panel and, if needed, the post are replaced, provided a panel of the same height and colour is still available. A small dent in roll mesh can often be pulled out, and a new piece can be woven into chain-link in place of a torn one. With more serious damage, the mesh is replaced between two tensioning points."),
            ("Can I add privacy strips or windbreak fabric to a panel fence?", "You can, but the wind then loads the fence almost like a solid wall. The posts of an ordinary panel fence are chosen for an open fence, and screened stretches may start to lean in a storm. If you plan to screen it, we size the posts and foundations for that stretch for the higher load from the start."),
        ],
        "links_keys": ["neighbour", "road_utilities", "gate_guide"],
        "links_extra": [("/en/fences/mesh/", "3D mesh panel fences", "Installed with posts and matching gates.")],
        "cta": ("We measure and price both options", "At a free site visit we check the boundary, slope and ground and give you a written quote for both roll mesh and 3D panels.", "/en/#form", "Get a quote"),
    },
}
