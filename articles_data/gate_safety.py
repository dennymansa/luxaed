# gate_safety: /automaatvarava-ohutus/, /ru/bezopasnost-avtomaticheskih-vorot/, /en/automatic-gate-safety/
#
# Verification notes (primary texts checked on 27.09.2026; quotes are exact):
#
# NEW SOURCE mreg_corr, Corrigendum to Regulation (EU) 2023/1230 (OJ, 4.7.2023),
# https://eur-lex.europa.eu/eli/reg/2023/1230/corrigendum/2023-07-04/oj :
#   "5. On page 38, Article 51, paragraph 2, first subparagraph: for: '14 January 2027', read: '20 January 2027'."
#   "10. On page 39, Article 54, second paragraph: for: '14 January 2027', read: '20 January 2027'."
#   (The consolidated OJ text of Art. 54 still reads "It shall apply from 14 January 2027.")
# ttja_masinad: "Alates 20.01.2027 kohaldatakse masinatele Euroopa Parlamendi ja nõukogu määrust nr 2023/1230/EL.
#   Seoses sellega muutub 20.01.2027 kehtetuks masinadirektiiv 2006/42/EÜ."
#
# New details taken from sources already registered (no new key needed):
#   mreg Art. 10(7): "The instructions may be provided in a digital format." ... "However, at the request of the
#     user at the time of the purchase, the manufacturer shall provide the instructions for use in paper format
#     free of charge within one month."
#   mreg Art. 18: "A natural or legal person that carries out a substantial modification of machinery or a related
#     product shall be considered to be a manufacturer for the purposes of this Regulation" ... "A non-professional
#     user who carries out a substantial modification to his or her machinery or related product, for his or her
#     own use, shall not be considered to be a manufacturer".
#   md Annex I 1.7.3: "All machinery must be marked visibly, legibly and indelibly with the following minimum
#     particulars: the business name and full address of the manufacturer ..., designation of the machinery, the CE
#     Marking ..., designation of series or type, serial number, if any, the year of construction".
#   md Annex I 1.7.4: "All machinery must be accompanied by instructions in the official Community language or
#     languages of the Member State in which it is placed on the market and/or put into service."
#   md Annex I 1.7.4.2 (q): "the operating method to be followed in the event of accident or breakdown; if a blockage
#     is likely to occur, the operating method to be followed so as to enable the equipment to be safely unblocked";
#     (r): "the description of the adjustment and maintenance operations that should be carried out by the user and
#     the preventive maintenance measures that should be observed".
#   std (Commission Implementing Decision (EU) 2023/1586, consolidated 15.11.2025), item 343: "EN 12635:2002+A1:2008
#     Industrial, commercial and garage doors and gates - Installation and use".
#   seos § 5 lg 1 p 1: "Seadme võib kasutusele võtta, kui: 1) see vastab nõuetele, on tehniliselt korras ning
#     ettenähtud otstarbel ja viisil kasutamiseks ohutu, sealhulgas on varustatud kasutamiseks vajalike töökindlate
#     ja -korras juhtimis-, kontroll- ja kaitseseadistega".
#   seos § 6 lg 2: "1) seadme nõuetekohaseks kasutamiseks ja korrashoiuks on loodud vajalikud tingimused, sealhulgas on
#     olemas asjakohane teave, mis on seadmega kokku puutuvatele isikutele teatavaks tehtud ja kättesaadav;
#     2) seadme kasutamine peatatakse, kui ilmneb vahetu oht; ... 4) seadme kasutamise ja korrashoiu (käidu) nõudeid
#     täidetakse".
#   seos § 13 lg 1: "Majandustegevusteate esitab majandustegevusena seadmetööd tegev ettevõtja."
#   ttja_uks (tõstuksed): "Hooldusintervallid annab ukse tootja kas ajaliselt (nt 3-6 kuud) või sõltuvalt
#     kasutusintensiivsusest (nt. 1000-5000 töötsüklit). Hoolduste tegemine on kohustuslik"; "Unustamise vältimiseks
#     on mõistlik sõlmida hooldusleping usaldusväärse firmaga."; "Paigaldaja peab tellijale üle andma ukse kasutus- ja
#     hooldusjuhendi ning vastavusdeklaratsiooni."; "kui olemasolevale käsitsi liigutatavale tõstuksele lisada ajam koos
#     juhtsüsteemiga, siis loetakse isik kes täiendused teostas automatiseeritud tõstukse tootjaks koos kõikide
#     kohustustega, mis on masina tootjal."
#   elektritoo § 4 (layperson list) and kompetents § 7 lg 1 p 2 (proven competence for the person responsible for
#     electrical work), as in the current article.
#
# Cables in a protective duct are presented as LuxAed's recommendation only, not as a legal duty.

NEW_SRC = {
    "mreg_corr": {
        "et": ("Masinamääruse (EL) 2023/1230 parandus", "https://eur-lex.europa.eu/eli/reg/2023/1230/corrigendum/2023-07-04/oj"),
        "ru": ("Исправление к регламенту (ЕС) 2023/1230", "https://eur-lex.europa.eu/eli/reg/2023/1230/corrigendum/2023-07-04/oj"),
        "en": ("Corrigendum to Regulation (EU) 2023/1230", "https://eur-lex.europa.eu/eli/reg/2023/1230/corrigendum/2023-07-04/oj"),
    },
}

ARTICLE = {
    # =====================================================================
    # ET
    # =====================================================================
    "et": {
        "title": "Automaatvärava ohutus: CE, fotoelemendid ja hooldus | LuxAed",
        "desc": "Ajamiga värav on seaduse järgi masin. Mida üleandmisel saada, kuidas töötavad fotoelemendid ja turvaserv, kes tohib ajami ühendada ja kuidas väravat hooldada.",
        "short": "Automaatvärava ohutus",
        "image": "luxaed-w-gates-picket",
        "kicker": "Juhend · automaatväravad",
        "h1": "Automaatvärava ohutus<br><em>paigaldusest hoolduseni</em>",
        "lead": "Automaatvärav on mugav, kuid see on raske liikuv masin, mis peab iga takistuse ees peatuma. Selgitame, mida nõuab seadus, mida üleandmisel kontrollida ja kuidas hoida värav ohutuna ka talvel ja aastate pärast.",
        "direct": ("Automaatvärav on seaduse järgi masin: selle ohutuse eest vastutab tootja, sageli paigaldaja, ja omanik peab seda hooldama.",
                   'Üleandmisel peaksite saama EÜ vastavusdeklaratsiooni ja eestikeelse kasutusjuhendi ning nägema, et värav peatub takistuse ees ja avaneb käsitsi. Ajami ühendamine elektrivõrku on pädeva elektriku töö. Kui alles plaanite <a href="/varavad/">automaatväravat</a>, laske need punktid pakkumisse kirja panna.'),
        "blocks": [
            {"type": "sections", "tag": "Seadus", "h": "Miks automaatvärav on masin ja kes vastutab",
             "items": [
                 ("Ajamiga värav on masin", [
                     "Seadme ohutuse seaduse järgi on masin koost, millel on vähemalt üks liikuv osa ja muu kui inim- või loomjõul töötav ajam, ning ajamiga värav vastab sellele. Euroopa Komisjoni masinadirektiivi juhend nimetab ajamiga väravaid masinateks, millele kehtib lisaks ehitustoodete määrus."]),
                 ("Tootja on sageli paigaldaja", [
                     "Masinadirektiivi järgi peab tootja enne masina kasutusele võtmist tagama vastavuse olulistele ohutusnõuetele, koostama tehnilise toimiku, tegema vastavushindamise, koostama EÜ vastavusdeklaratsiooni ja kinnitama CE-märgise. Kui tootjat ei ole, loetakse tootjaks see, kes masina turule laseb või kasutusele võtab.",
                     "Tarbijakaitse ja Tehnilise Järelevalve Amet (TTJA) selgitab tõstuste kohta, et see, kes lisab käsitsi liigutatavale uksele ajami koos juhtsüsteemiga, loetakse automaatukse tootjaks koos kõigi tootja kohustustega. Väravaga on loogika sama: kui värav ja ajam pannakse kokku kohapeal, on tootja rollis üldjuhul paigaldaja."]),
                 ("Omaniku kohustused", [
                     "Seadme ohutuse seaduse järgi tuleb seadet kasutades tagada, et kasutamise ja korrashoiu nõudeid täidetaks, vajalik teave oleks seadmega kokku puutuvatele inimestele teada ja vahetu ohu korral kasutamine peatataks. Praktikas tähendab see, et kõik pereliikmed teavad, kuidas väravat käsitsi avada, ning takistuse ees mitte peatuv värav jääb seisma kuni remondini."]),
                 ("Mis muutub 20.01.2027", [
                     "Sellest päevast kohaldatakse masinatele ELi masinamäärust 2023/1230 ja masinadirektiiv 2006/42/EÜ muutub kehtetuks. Euroopa Liidu Teatajas avaldatud tekstis oli kuupäev 14. jaanuar, parandusega muudeti see 20. jaanuariks.",
                     "Kasutusjuhendi võib siis anda digitaalsena, kuid kui küsite seda ostu ajal, peab tootja andma selle kuu jooksul tasuta ka paberil. Kes teeb masinas olulise, ohutust mõjutava muudatuse, loetakse tootjaks, välja arvatud tavakasutaja, kes muudab oma masinat enda tarbeks."]),
             ],
             "sources": ["seos", "md", "mdguide", "ttja_uks", "mreg", "mreg_corr", "ttja_masinad"]},
            {"type": "sections", "tag": "Ohutusseadised", "h": "Kuidas värav inimest ja autot kaitseb",
             "intro": "Ohutus on kihiline, sest ükski seade üksi ei kata kõiki olukordi.",
             "items": [
                 ("Jõu piiramine", [
                     "Ajam tunneb liikumisel takistust, näiteks mootori koormuse järgi, ning peatub või liigub tagasi, kui värav millegi vastu läheb. See kaitse reageerib alles pärast kokkupuudet. Jõud seadistatakse värava kaalu ja liikumise järgi ning see tuleb üle kontrollida pärast iga remonti ja rullikute või ajami vahetust."]),
                 ("Fotoelemendid", [
                     "Fotoelementide paar saadab üle ava nähtamatu kiire ja kui kiir sulgemise ajal katkeb, värav peatub või avaneb uuesti. Fotoelement näeb ainult oma kiire kõrgusel, seega ei pruugi see märgata sellest madalamal olevat väikest last või looma ega õhukest jalgrattaraami."]),
                 ("Turvaserv", [
                     "Turvaserv on sulgemisservale kinnitatud kummiprofiil, mis tunneb survet ning peatab või pöörab värava kohe tagasi. See vähendab muljumisohtu seal, kus värav sulgub posti või teise tiiva vastu, ja soovitame seda eriti siis, kui krundil on lapsed või värav sulgub automaatselt."]),
                 ("Ohtlikud kohad", [
                     "Liugväraval on ohtlikud sulgemisserv posti juures, vahe värava ja posti või aia vahel ning rullikud ja hammaslatt. Tiibväraval on ohtlikud hingede pool, kuhu võivad jääda sõrmed, tiibade kokkupuutekoht ja ala, mida tiib avanedes pühib. Hea paigaldus hoiab vahed väikesed või katab liikuvad osad."]),
                 ("Standardid ja seadus", [
                     "Kasutusohutust käsitleb harmoneeritud standard EN 12453:2017+A1:2021, tootestandard on EN 13241:2003+A2:2016 ning paigaldust ja kasutamist käsitleb EN 12635:2002+A1:2008. Seadme ohutuse seaduse järgi eeldatakse, et standardis soovitatud ohutusabinõu vastab heale inseneritavale, ja seadme võib kasutusele võtta alles siis, kui sellel on vajalikud töökorras kaitseseadised."]),
             ],
             "sources": ["std", "seos"]},
            {"type": "sections", "tag": "Üleandmine", "h": "Üleandmise kontrollnimekiri",
             "intro": "Kontrollige kõike, kuni paigaldaja on veel kohal, ja varuge selleks pool tundi.",
             "items": [
                 ("1. EÜ vastavusdeklaratsioon", [
                     "Deklaratsioonist näete, kes on masina tootja ja millistele nõuetele värav vastab. Ajami tootja dokument katab ainult ajamit. Kohapeal kokku pandud tervikvärava deklaratsiooni koostab tervikvärava tootja, üldjuhul paigaldaja."]),
                 ("2. Eestikeelne kasutusjuhend", [
                     "Juhend peab olema selle riigi ametlikus keeles, kus masin kasutusele võetakse. Masinadirektiivi järgi kirjeldab see ka kasutaja seadistus- ja hooldustoiminguid, ennetavat hooldust ning seda, kuidas rikke või kinnijäämise korral toimida."]),
                 ("3. Märgistus", [
                     "Masinal, tavaliselt väraval või ajamil, peab olema loetav ja kustumatu märgistus tootja nime ja aadressi, masina nimetuse, CE-märgise, seeria või tüübi, olemasolu korral seerianumbri ning valmistamisaastaga."]),
                 ("4. Proovige kohe", [
                     "Laske näidata, kuidas värav voolukatkestuse ajal käsitsi avada ja pärast lukku tagasi panna. Katkestage sulgemise ajal fotoelemendi kiir esemega, mitte oma kehaga, ja vaadake, et värav peatub või avaneb uuesti. Küsige, kuidas jõu piiramist kontrolliti ja kas tulemus on kirjas."]),
                 ("5. Kirjalik ülevaade", [
                     "Laske kirja panna paigaldatud ohutusseadised, pultide arv, hooldusintervall ja hoolduse tegija. TTJA märgib tõstuste kohta, et paigaldaja peab tellijale üle andma kasutus- ja hooldusjuhendi ning vastavusdeklaratsiooni."]),
             ],
             "sources": ["md", "ttja_uks"]},
            {"type": "sections", "tag": "Elekter", "h": "Elektriühendus ja kaablid",
             "items": [
                 ("Kes tohib ajami ühendada", [
                     "Tavaisik tohib teha ainult määruses loetletud lihtsaid elektritöid, näiteks vahetada kaitsmeid ja valgusallikaid või lülitada kaitselüliteid. 230-voldise väravaajami ühendamist selles loetelus ei ole, seega tuleb see töö lasta teha pädeval elektrikul.",
                     "Elektritöö eest vastutava isiku kompetentsus peab olema tõendatud ja ettevõte, kes teeb elektritöid majandustegevusena, peab olema esitanud majandustegevusteate. Küsige paigaldajalt, kes elektritöö teeb."]),
                 ("Kaabel kaitsetorusse", [
                     'Meie soovitus on panna toite- ja juhtkaablid maasse kaitsetorusse ning jätta ruumi fotoelementide, signaallambi ja hilisema domofoni jaoks. Torus olevat kaablit on lihtne vahetada ja see saab kaevamisel harvem kahjustada. Kui aed alles ehitatakse, pange toru maasse enne postide betoneerimist, nagu kirjeldame ka <a href="/aia-ehituse-vead/">aia ehitamise vigade</a> juures.']),
             ],
             "sources": ["elektritoo", "kompetents", "seos"]},
            {"type": "sections", "tag": "Hooldus", "h": "Hoolduse loogika ja talv",
             "items": [
                 ("Kui tihti hooldada", [
                     "Hooldusintervalli annab tootja juhendis. TTJA toob tõstuste kohta näite, et intervall võib olla antud aja järgi (3–6 kuud) või töötsüklite järgi (1 000–5 000 tsüklit). Amet rõhutab, et hooldus on kohustuslik, ja soovitab hoolduslepingut, et see ei ununeks.",
                     "Mida rohkem värav liigub, seda sagedamini vajab see hooldust: ühe pere värav avaneb mõni kord päevas, ühistu või ettevõtte värav kümneid kordi."]),
                 ("Mida hooldus hõlmab", [
                     'Hooldus hõlmab kandureid, rullikuid või hingi, hammaslati ja ajami vahet, kinnitusi, piirlüliteid, jõu seadistust, fotoelemente, turvaservi ja käsitsi avamist. Hea hooldaja paneb kirja, mida kontrolliti ja vahetati. Kui liugvärav liigub raskelt, vajub või kolksub, on põhjus sageli mehaaniline. Sellest lähemalt <a href="/aia-remont/liugvarava-remont/">liugvärava remondi</a> lehel.']),
                 ("Talv", [
                     "Lumi ja jää katavad fotoelemente ning kogunevad tiibade ette või liugvärava liikumisalale. Jää tõttu võib ajam arvata, et ees on takistus, ja värav peatub poolel teel. Koristage lumi ja puhastage fotoelemendid, aga ärge suurendage ajami jõudu.",
                     'Hoidke avariivabastuse võti toas ja kontrollige enne külmi, et vabastuse lukk ei ole kinni külmunud. Kui värav talvel ei sulgu, vaadake meie <a href="/aia-remont/varav-ei-avane/">juhendit värava tõrgete kohta</a>. Liug- ja tiibvärava erinevust talvel võrdleme <a href="/liugvarav-voi-tiibvarav/">eraldi artiklis</a>.']),
             ],
             "sources": ["seos", "ttja_uks"]},
            {"type": "table", "tag": "Ajakava", "h": "Kes teeb mida ja millal",
             "headers": ("", "Kes", "Mida teha"),
             "rows": [
                 ("Iga kuu", "Omanik", "Fotoelementide test esemega, liikumisala puhastamine, uute häälte kuulamine"),
                 ("Enne talve", "Hooldaja või omanik", "Fotoelementide puhastus, avariivabastuse ja jõu seadistuse kontroll"),
                 ("Vähemalt kord aastas", "Hooldaja", "Hooldus tootja juhendi järgi ja kirjalik kokkuvõte"),
                 ("Pärast lööki, remonti või osade vahetust", "Paigaldaja või hooldaja", "Joonduse, jõu seadistuse ja kõigi ohutusseadiste kontroll"),
                 ("Kui värav ei peatu takistuse ees", "Omanik", "Automaatse kasutamise lõpetamine ja hooldaja kutsumine"),
             ],
             "note": "See on meie soovitatud rütm. Kui tootja juhend nõuab tihedamat hooldust, järgige juhendit."},
            {"type": "cards", "tag": "Küsimused", "h": "Mida paigaldajalt enne lepingut küsida", "cols": 2,
             "items": [
                 ("Kes on tootja ja milliseid dokumente saan?", "Kes koostab vastavusdeklaratsiooni ja kinnitab CE-märgise, kui värav ja ajam pannakse kokku kohapeal? Hea vastus nimetab ka eestikeelse kasutusjuhendi ja hooldusjuhise."),
                 ("Millised ohutusseadised on hinnas?", 'Fotoelemendid, turvaserv, signaallamp, nende arv ja see, kuidas jõudu kontrollitakse. Meie <a href="/hinnad/">hinnatabelis</a> sisaldab automaatikaga liugvärava hind raami, vundamenti, ajamit ja ohutusseadmeid tavalahenduses.'),
                 ("Kes teeb elektritöö?", "Küsige, kas ajami ühendab pädev elektrik ja kas ettevõte on esitanud majandustegevusteate."),
                 ("Kes hooldab ja kui tihti?", 'Küsige hooldusintervalli ja seda, kas firma teeb ka hooldust. Rohkem küsimusi leiate <a href="/kuidas-valida-aiafirmat/">aiafirma valimise juhendist</a>.'),
             ]},
            {"type": "cards", "tag": "Meie soovitus", "h": "Mida me ise soovitame", "cols": 2,
             "items": [
                 ("Kõigepealt korras värav", "Raskelt liikuv või vajunud värav koormab ajamit ja segab takistuse tuvastamist. Laske enne automaatika lisamist värav joondada ja kulunud osad vahetada."),
                 ("Turvaserv, kui on lapsed", "Fotoelemendid kaitsevad ainult kiire joonel. Kui krundil on lapsed või värav sulgub automaatselt, lisage sulgemisservale turvaserv."),
                 ("Automaatne sulgemine läbimõeldult", "Automaatne sulgemine on mugav, kuid siis peavad ohutusseadised olema laitmatus korras. Kui lapsed mängivad värava lähedal, kaaluge sulgemist ainult pultiga."),
                 ("Pult ei ole mänguasi", "Hoidke pultid lastele kättesaamatus kohas ja leppige kodus kokku, et värav liigub ainult siis, kui ava on vaba ja näha."),
             ]},
            {"type": "cards", "tag": "Levinud probleemid", "h": "Mis läheb sageli valesti", "cols": 2,
             "items": [
                 ("Fotoelemendid on kaetud", "Lumi, jää, mustus või kasvav põõsas katab fotoelemendi ja värav ei sulgu."),
                 ("Jõud on liiga suur", "Talvel või pärast remonti tõstetakse jõudu, et värav liiguks, ja siis tunneb ajam takistust liiga hilja."),
                 ("Keegi ei tea, kuidas käsitsi avada", "Voolukatkestuse ajal jääb auto õue või tänavale, sest vabastusvõtit ei leita."),
                 ("Juhuslik ümberehitus", "Keegi vahetas ajami või tiiva, kuid ohutusseadiseid üle ei kontrollinud ega dokumente uuendanud, ja värav muutus ohtlikuks."),
             ]},
        ],
        "faq": [
            ("Kas automaatväraval peab olema CE-märgis?", "Jah. Ajamiga värav on masin ja CE-märgise kinnitab tootja pärast vastavushindamist, kohapeal kokku pandud värava puhul üldjuhul paigaldaja. Küsige üleandmisel EÜ vastavusdeklaratsiooni."),
            ("Milliseid dokumente peab üleandmisel saama?", "EÜ vastavusdeklaratsiooni ja eestikeelse kasutusjuhendi, mis kirjeldab ka kasutaja hooldustoiminguid. Masinal peab olema märgistus tootja nime ja aadressi, CE-märgise ja valmistamisaastaga. LuxAed annab need koos värava üleandmisega ning kirjutab üles ka paigaldatud ohutusseadised ja hooldusintervalli."),
            ("Kas võin väravaajami ise elektrivõrku ühendada?", "Kui te ei ole pädev elektrik, siis mitte. Tavaisikule lubatud elektritööde loetelus 230-voldise ajami ühendamist ei ole."),
            ("Kui tihti tuleb automaatväravat hooldada?", "Tootja juhendis toodud intervalliga, mis võib olla antud aja või töötsüklite järgi. Seadme ohutuse seaduse järgi tuleb kasutamise ja korrashoiu nõudeid täita. Meie soovitus on hooldus vähemalt kord aastas ja kontroll enne talve."),
            ("Kas vanale väravale automaatika lisamine on ohutu?", "On, kui värav on konstruktsioonilt terve ning paigaldaja lisab vajalikud ohutusseadised ja võtab tootja kohustused. Enne tuleb hinnata raami, hingi või kandureid, poste ja alust, sest mootor ei tee nõrgast väravast ohutut. Meie hinnatabelis maksab automaatika sobivale olemasolevale väravale 500–1 250 €."),
            ("Mis muutub 2027. aastal?", "Alates 20.01.2027 kohaldatakse masinatele ELi masinamäärust 2023/1230, mis asendab masinadirektiivi 2006/42/EÜ. Kasutusjuhendi võib siis anda digitaalsena, kuid ostu ajal küsides peab tootja andma selle tasuta ka paberil."),
        ],
        "links_keys": ["gate_guide", "gate_wont_open", "sliding_gate"],
        "links_extra": [("/varavad/", "Automaatväravad", "Paigaldus koos ohutusseadmetega.")],
        "cta": ("Paigaldame automaatika ohutult", "Mõõdistusel hindame väravat, alust ja elektrit ning pakume ajami koos ohutusseadmetega.", "/varavad/#form", "Küsi väravate pakkumist"),
    },
    # =====================================================================
    # RU
    # =====================================================================
    "ru": {
        "title": "Безопасность автоматических ворот и их обслуживание | LuxAed",
        "desc": "Ворота с приводом считаются машиной. Что получить при сдаче, как работают фотоэлементы и защитная кромка, кто подключает привод и как обслуживать ворота.",
        "short": "Безопасность автоматических ворот",
        "image": "luxaed-w-gates-picket",
        "kicker": "Руководство · автоматические ворота",
        "h1": "Безопасность автоматических ворот<br><em>от монтажа до обслуживания</em>",
        "lead": "Автоматические ворота удобны, но это тяжёлая движущаяся машина, которая должна останавливаться перед любым препятствием. Объясняем, что требует закон, что проверить при сдаче работ и как сохранить ворота безопасными зимой и через годы.",
        "direct": ("Ворота с приводом по закону считаются машиной: за их безопасность отвечает производитель, часто монтажник, а владелец обязан их обслуживать.",
                   'При сдаче работ вы должны получить декларацию соответствия ЕС и инструкцию на эстонском языке и увидеть, что ворота останавливаются перед препятствием и открываются вручную. Подключение привода к сети выполняет компетентный электрик. Если вы только планируете <a href="/ru/vorota-avtomatika/">автоматические ворота</a>, попросите записать эти пункты в предложение.'),
        "blocks": [
            {"type": "sections", "tag": "Закон", "h": "Почему автоматические ворота считаются машиной и кто отвечает",
             "items": [
                 ("Ворота с приводом считаются машиной", [
                     "По закону о безопасности оборудования (Seadme ohutuse seadus) машиной считается узел, у которого есть хотя бы одна движущаяся часть и привод, работающий не от силы человека или животного, поэтому ворота с приводом считаются машиной. Руководство Еврокомиссии по директиве о машинах относит их к машинам, на которые распространяется и регламент о строительной продукции."]),
                 ("Производителем часто оказывается монтажник", [
                     "По директиве о машинах производитель до ввода машины в эксплуатацию обязан обеспечить соответствие основным требованиям безопасности, составить техническое досье, провести оценку соответствия, оформить декларацию соответствия ЕС и нанести маркировку CE. Если производителя нет, производителем считается тот, кто выпускает машину на рынок или вводит её в эксплуатацию.",
                     "Департамент защиты прав потребителей и технического надзора (TTJA) поясняет для подъёмных ворот, что тот, кто добавляет к ручным воротам привод и систему управления, становится производителем автоматических ворот. С въездными воротами логика та же: если ворота и привод собирают на месте, в роли производителя, как правило, выступает монтажник."]),
                 ("Обязанности владельца", [
                     "Закон о безопасности оборудования обязывает соблюдать требования к эксплуатации и содержанию, доводить нужную информацию до всех, кто соприкасается с оборудованием, и прекращать использование при непосредственной опасности. На практике все в семье должны знать, как открыть ворота вручную, а ворота, которые не останавливаются перед препятствием, не используют до ремонта."]),
                 ("Что изменится 20.01.2027", [
                     "С этого дня применяется регламент ЕС о машинах 2023/1230, а директива 2006/42/EC утрачивает силу; в Официальном журнале ЕС сначала стояло 14 января, исправление перенесло дату на 20 января. Инструкцию тогда можно выдавать в цифровом виде, но по просьбе при покупке производитель обязан в течение месяца бесплатно дать и бумажную. Тот, кто вносит в машину существенное изменение, влияющее на безопасность, считается производителем, кроме обычного пользователя, меняющего свою машину для себя."]),
             ],
             "sources": ["seos", "md", "mdguide", "ttja_uks", "mreg", "mreg_corr", "ttja_masinad"]},
            {"type": "sections", "tag": "Защита", "h": "Как ворота защищают людей и машину",
             "intro": "Безопасность строится из нескольких уровней, потому что ни одно устройство в одиночку не закрывает все ситуации.",
             "items": [
                 ("Ограничение усилия", [
                     "Привод чувствует сопротивление, например по нагрузке на мотор, и останавливается или отъезжает назад, если ворота во что-то упираются, но срабатывает только после контакта. Усилие настраивают по весу и ходу ворот и проверяют заново после каждого ремонта или замены роликов и привода."]),
                 ("Фотоэлементы", [
                     "Пара фотоэлементов создаёт поперёк проёма невидимый луч, и если он прерывается во время закрывания, ворота останавливаются или снова открываются. Фотоэлемент видит только на высоте своего луча, поэтому может не заметить маленького ребёнка или животное ниже луча, а также тонкую раму велосипеда."]),
                 ("Защитная кромка", [
                     "Защитная кромка представляет собой резиновый профиль на закрывающем краю ворот, который чувствует давление и сразу останавливает или разворачивает ворота. Она снижает риск защемления там, где ворота закрываются к столбу или ко второй створке, и мы советуем её особенно тогда, когда на участке есть дети или ворота закрываются автоматически."]),
                 ("Опасные места", [
                     "У откатных ворот опасны закрывающий край у столба, зазор между воротами и столбом или забором, ролики и зубчатая рейка. У распашных опасны сторона петель, где можно прищемить пальцы, место смыкания створок и зона открывания. Хороший монтаж оставляет зазоры маленькими или закрывает движущиеся части."]),
                 ("Стандарты и закон", [
                     "Безопасность эксплуатации описывает гармонизированный стандарт EN 12453:2017+A1:2021, требования к изделию задаёт EN 13241:2003+A2:2016, а монтаж и эксплуатацию описывает EN 12635:2002+A1:2008. По закону о безопасности оборудования мера, рекомендованная стандартом, считается хорошей инженерной практикой, а вводить оборудование в эксплуатацию можно только с исправными необходимыми защитными устройствами."]),
             ],
             "sources": ["std", "seos"]},
            {"type": "sections", "tag": "Сдача работ", "h": "Чек-лист при сдаче ворот",
             "intro": "Проверьте всё, пока монтажник ещё на месте, и выделите на это полчаса.",
             "items": [
                 ("1. Декларация соответствия ЕС", [
                     "Из неё видно, кто производитель машины и каким требованиям соответствуют ворота. Документ производителя привода касается только привода, а декларацию на ворота, собранные на месте, составляет производитель ворот в целом, как правило, монтажник."]),
                 ("2. Инструкция на эстонском языке", [
                     "Инструкция должна быть на официальном языке страны, где машину вводят в эксплуатацию. По директиве о машинах в ней описаны также регулировка и обслуживание со стороны пользователя, профилактика и порядок действий при поломке или заклинивании."]),
                 ("3. Маркировка", [
                     "На машине, обычно на воротах или приводе, должна быть разборчивая и несмываемая маркировка с названием и адресом производителя, наименованием машины, знаком CE, серией или типом, серийным номером, если он есть, и годом изготовления."]),
                 ("4. Проверьте на месте", [
                     "Попросите показать ручную разблокировку и возврат блокировки. Во время закрывания перекройте луч фотоэлементов предметом, а не своим телом, и убедитесь, что ворота останавливаются или открываются снова. Спросите, как проверяли усилие и записан ли результат."]),
                 ("5. Письменная сводка", [
                     "Попросите записать установленные устройства безопасности, количество пультов, интервал обслуживания и того, кто его выполняет. TTJA отмечает для подъёмных ворот, что монтажник обязан передать заказчику инструкцию по эксплуатации и обслуживанию и декларацию соответствия."]),
             ],
             "sources": ["md", "ttja_uks"]},
            {"type": "sections", "tag": "Электрика", "h": "Подключение и кабели",
             "items": [
                 ("Кто может подключать привод", [
                     "Обычный человек может выполнять только перечисленные в постановлении простые электроработы, например менять предохранители и лампы или переключать автоматы. Подключения привода ворот на 230 вольт в этом списке нет, поэтому эту работу должен выполнять компетентный электрик.",
                     "Компетентность лица, ответственного за электроработы, должна быть подтверждена, а фирма, которая выполняет электроработы как предпринимательскую деятельность, должна подать уведомление в регистр экономической деятельности (MTR). Спросите монтажника, кто будет делать электрику."]),
                 ("Кабель в защитной трубе", [
                     'Мы советуем прокладывать силовой и управляющие кабели в земле в защитной трубе и оставлять запас для фотоэлементов, сигнальной лампы и будущего домофона. Кабель в трубе легко заменить, и при земляных работах его реже повреждают. Если забор ещё строится, уложите трубу до бетонирования столбов, о чём мы пишем и в статье об <a href="/ru/oshibki-pri-ustanovke-zabora/">ошибках при установке забора</a>.']),
             ],
             "sources": ["elektritoo", "kompetents", "seos"]},
            {"type": "sections", "tag": "Обслуживание", "h": "Логика обслуживания и зима",
             "items": [
                 ("Как часто обслуживать", [
                     "Интервал указывает производитель в инструкции. TTJA на примере подъёмных ворот приводит интервалы по времени (3–6 месяцев) или по числу циклов (1 000–5 000). Департамент подчёркивает, что обслуживание обязательно, и советует заключить договор на обслуживание, чтобы о нём не забыть.",
                     "Чем чаще ворота работают, тем чаще им нужно обслуживание: ворота одной семьи открываются несколько раз в день, ворота товарищества или фирмы десятки раз."]),
                 ("Что входит в обслуживание", [
                     'Обслуживание охватывает каретки, ролики или петли, зазор между зубчатой рейкой и приводом, крепления, концевые выключатели, настройку усилия, фотоэлементы, защитные кромки и ручное открывание. Хороший мастер записывает, что проверено и что заменено. Если откатные ворота идут туго, просели или стучат, причина часто механическая. Подробнее на странице о <a href="/ru/remont-zaborov/remont-otkatnyh-vorot/">ремонте откатных ворот</a>.']),
                 ("Зима", [
                     "Снег и лёд закрывают фотоэлементы и скапливаются перед створками или в зоне хода откатных ворот. Из-за льда привод может решить, что впереди препятствие, и ворота остановятся на полпути. Уберите снег и очистите фотоэлементы, но не увеличивайте усилие привода.",
                     'Храните ключ аварийной разблокировки в доме и перед морозами проверьте, что замок разблокировки не примёрз. Если зимой ворота не закрываются, посмотрите наше <a href="/ru/remont-zaborov/vorota-ne-otkryvayutsya/">руководство по неисправностям ворот</a>. Как откатные и распашные ворота ведут себя зимой, мы сравниваем в <a href="/ru/otkatnye-ili-raspashnye-vorota/">отдельной статье</a>.']),
             ],
             "sources": ["seos", "ttja_uks"]},
            {"type": "table", "tag": "График", "h": "Кто, что и когда делает",
             "headers": ("", "Кто", "Что делать"),
             "rows": [
                 ("Каждый месяц", "Владелец", "Проверка фотоэлементов предметом, очистка зоны движения, внимание к новым звукам"),
                 ("Перед зимой", "Мастер или владелец", "Очистка фотоэлементов, проверка аварийной разблокировки и настройки усилия"),
                 ("Не реже раза в год", "Мастер", "Обслуживание по инструкции производителя и письменный отчёт"),
                 ("После удара, ремонта или замены деталей", "Монтажник или мастер", "Проверка выравнивания, настройки усилия и всех устройств безопасности"),
                 ("Если ворота не останавливаются перед препятствием", "Владелец", "Прекратить автоматическую работу и вызвать мастера"),
             ],
             "note": "Это рекомендуемый нами ритм. Если инструкция производителя требует более частого обслуживания, действуйте по инструкции."},
            {"type": "cards", "tag": "Вопросы", "h": "Что спросить у монтажника до договора", "cols": 2,
             "items": [
                 ("Кто производитель и какие документы я получу?", "Кто составит декларацию соответствия и нанесёт маркировку CE, если ворота и привод собирают на месте? Хороший ответ называет и инструкцию на эстонском языке, и указания по обслуживанию."),
                 ("Какие устройства безопасности входят в цену?", 'Фотоэлементы, защитная кромка, сигнальная лампа, их количество и способ проверки усилия. В нашем <a href="/ru/ceny/">прайсе</a> цена откатных ворот с автоматикой включает раму, фундамент, привод и устройства безопасности в стандартном решении.'),
                 ("Кто делает электрику?", "Спросите, подключает ли привод компетентный электрик и подала ли фирма уведомление об экономической деятельности."),
                 ("Кто обслуживает и как часто?", 'Спросите интервал обслуживания и то, обслуживает ли фирма ворота сама. Другие вопросы собраны в статье <a href="/ru/kak-vybrat-firmu-dlya-zabora/">о выборе фирмы для забора</a>.'),
             ]},
            {"type": "cards", "tag": "Наш совет", "h": "Что мы советуем", "cols": 2,
             "items": [
                 ("Сначала исправные ворота", "Ворота, которые идут туго или просели, перегружают привод и мешают распознать препятствие. Перед установкой автоматики выровняйте ворота и замените изношенные детали."),
                 ("Защитная кромка, если есть дети", "Фотоэлементы защищают только линию луча. Если на участке есть дети или ворота закрываются автоматически, поставьте защитную кромку на закрывающий край."),
                 ("Автозакрывание с умом", "Автоматическое закрывание удобно, но тогда устройства безопасности должны быть в безупречном состоянии. Если дети играют рядом с воротами, подумайте о закрывании только с пульта."),
                 ("Пульт не игрушка", "Храните пульты вне досягаемости детей и договоритесь дома, что ворота двигаются только тогда, когда проём свободен и хорошо виден."),
             ]},
            {"type": "cards", "tag": "Частые проблемы", "h": "Что часто идёт не так", "cols": 2,
             "items": [
                 ("Закрыты фотоэлементы", "Снег, лёд, грязь или разросшийся куст закрывают фотоэлемент, и ворота не закрываются."),
                 ("Слишком большое усилие", "Зимой или после ремонта усилие поднимают, чтобы ворота ехали, и привод распознаёт препятствие слишком поздно."),
                 ("Никто не знает, как открыть вручную", "При отключении электричества машина остаётся во дворе или на улице, потому что не могут найти ключ разблокировки."),
                 ("Случайная переделка", "Кто-то заменил привод или створку, не проверив устройства безопасности и не обновив документы, и ворота стали опасными."),
             ]},
        ],
        "faq": [
            ("Нужна ли автоматическим воротам маркировка CE?", "Да. Ворота с приводом считаются машиной, и маркировку CE наносит производитель после оценки соответствия, а у ворот, собранных на месте, это, как правило, монтажник. При сдаче попросите декларацию соответствия ЕС."),
            ("Какие документы нужно получить при сдаче ворот?", "Декларацию соответствия ЕС и инструкцию на эстонском языке, где описано и обслуживание со стороны пользователя. На машине должна быть маркировка с названием и адресом производителя, знаком CE и годом изготовления. LuxAed передаёт всё это при сдаче ворот вместе с перечнем установленных устройств безопасности и интервалом обслуживания."),
            ("Можно ли самому подключить привод ворот к сети?", "Если вы не компетентный электрик, нет. В списке электроработ, разрешённых обычному человеку, подключения привода на 230 вольт нет."),
            ("Как часто нужно обслуживать автоматические ворота?", "С интервалом из инструкции производителя, который может быть задан по времени или по числу циклов. Закон о безопасности оборудования требует выполнять требования к эксплуатации и содержанию. Мы советуем обслуживание не реже раза в год и проверку перед зимой."),
            ("Безопасно ли ставить автоматику на старые ворота?", "Да, если ворота конструктивно исправны, а монтажник добавляет нужные устройства безопасности и берёт на себя обязанности производителя. Сначала нужно оценить раму, петли или каретки, столбы и основание, потому что мотор не сделает слабые ворота безопасными. В нашем прайсе автоматика на подходящие существующие ворота стоит 500–1 250 €."),
            ("Что изменится в 2027 году?", "С 20.01.2027 к машинам применяется регламент ЕС о машинах 2023/1230, который заменяет директиву 2006/42/EC. Инструкцию тогда можно выдавать в цифровом виде, но по просьбе при покупке производитель обязан бесплатно дать и бумажную."),
        ],
        "links_keys": ["gate_guide", "gate_wont_open", "sliding_gate"],
        "links_extra": [("/ru/vorota-avtomatika/", "Автоматические ворота", "Установка с устройствами безопасности.")],
        "cta": ("Установим автоматику безопасно", "На замере оценим ворота, основание и электрику и предложим привод с устройствами безопасности.", "/ru/vorota-avtomatika/#form", "Рассчитать ворота"),
    },
    # =====================================================================
    # EN
    # =====================================================================
    "en": {
        "title": "Automatic Gate Safety: CE, Photocells and Servicing | LuxAed",
        "desc": "A powered gate is legally a machine. What to get at handover, how photocells, safety edges and force limits work, who may wire the drive and how to service it.",
        "short": "Automatic gate safety",
        "image": "luxaed-w-gates-picket",
        "kicker": "Guide · automatic gates",
        "h1": "Automatic gate safety<br><em>from installation to servicing</em>",
        "lead": "An automatic gate is convenient, but it is a heavy moving machine that must stop for anything in its way. We explain what the law requires, what to check at handover and how to keep the gate safe in winter and for years to come.",
        "direct": ("A powered gate is legally a machine: the manufacturer, often the installer, answers for its safety, and the owner must keep it maintained.",
                   'At handover you should receive the EC declaration of conformity and instructions in Estonian, and see the gate stop for an obstacle and open by hand. The mains connection is a job for a competent electrician, and if you are planning <a href="/en/gates-automation/">automatic gates</a>, have these points written into the quote.'),
        "blocks": [
            {"type": "sections", "tag": "The law", "h": "Why a powered gate is a machine, and who is responsible",
             "items": [
                 ("A gate with a drive is a machine", [
                     "Under the Equipment Safety Act, a machine is an assembly with at least one moving part and a drive powered by something other than human or animal effort, so a powered gate is a machine. The European Commission's Machinery Directive guide names powered gates as machinery also subject to the Construction Products Regulation."]),
                 ("The manufacturer is often the installer", [
                     "Under the Machinery Directive, before a machine is put into service the manufacturer must ensure it meets the essential safety requirements, compile a technical file, carry out a conformity assessment, issue an EC declaration of conformity and affix the CE marking. Where there is no manufacturer, whoever places the machine on the market or puts it into service is treated as one.",
                     "The Consumer Protection and Technical Regulatory Authority (TTJA) explains for overhead doors that whoever adds a drive and controls to a manual door becomes the manufacturer of the automated door. Gates follow the same logic: when gate and drive are assembled on site, the installer generally takes on the manufacturer's role."]),
                 ("What the owner must do", [
                     "The Equipment Safety Act requires users to meet the use and maintenance requirements, make the necessary information known to everyone who comes into contact with the equipment and stop using it in case of immediate danger. In practice, everyone at home should know how to open the gate by hand, and a gate that does not stop for an obstacle stays out of use until repaired."]),
                 ("What changes on 20 January 2027", [
                     "From that date the EU Machinery Regulation 2023/1230 applies and the Machinery Directive 2006/42/EC is repealed; the original Official Journal text said 14 January, but a corrigendum moved it to 20 January. Instructions may then be digital, but if you ask when buying, the manufacturer must provide a free paper copy within a month. Anyone making a substantial, safety-relevant change to a machine is treated as its manufacturer, except a non-professional user changing their own machine."]),
             ],
             "sources": ["seos", "md", "mdguide", "ttja_uks", "mreg", "mreg_corr", "ttja_masinad"]},
            {"type": "sections", "tag": "Safety devices", "h": "How the gate protects people and cars",
             "intro": "Safety works in layers, because no single device covers every situation.",
             "items": [
                 ("Force limitation", [
                     "The drive senses resistance, for example through the motor load, and stops or reverses if the gate runs into something, but only after contact. The force is set for the gate's weight and travel and must be rechecked after every repair or replacement of rollers or the drive."]),
                 ("Photocells", [
                     "A pair of photocells sends an invisible beam across the opening; if it is broken while the gate closes, the gate stops or reopens. A photocell only sees at beam height, so it may miss a small child or animal below it, or a thin bicycle frame."]),
                 ("Safety edge", [
                     "A safety edge is a rubber strip on the closing edge that senses pressure and stops or reverses the gate at once. It reduces the risk of crushing where the gate closes against a post or the other leaf, and we recommend one especially with children around or automatic closing."]),
                 ("Danger points", [
                     "On a sliding gate, watch the closing edge at the post, the gap beside the post or fence, and the rollers and rack. On a swing gate, watch the hinge side, where fingers get caught, and the point where the leaves meet. Good installation keeps gaps small or covers moving parts."]),
                 ("Standards and the law", [
                     "Safety in use is covered by the harmonised standard EN 12453:2017+A1:2021, the product by EN 13241:2003+A2:2016, and installation and use by EN 12635:2002+A1:2008. Under the Equipment Safety Act, a measure a standard recommends is presumed to be good engineering practice, and equipment may only be put into service with the necessary protective devices working."]),
             ],
             "sources": ["std", "seos"]},
            {"type": "sections", "tag": "Handover", "h": "Handover checklist",
             "intro": "Check everything while the installer is still there, and allow half an hour.",
             "items": [
                 ("1. EC declaration of conformity", [
                     "It names the manufacturer and the requirements the gate meets. The drive maker's document covers only the drive; for a gate assembled on site, the declaration for the whole gate comes from its manufacturer, generally the installer."]),
                 ("2. Instructions in Estonian", [
                     "They must be in the official language of the country where the machine is put into service, and under the Machinery Directive they describe the user's adjustment and maintenance tasks, preventive maintenance and what to do after a breakdown or blockage."]),
                 ("3. Marking", [
                     "The machine, usually the gate or its drive, must carry legible and indelible marking with the manufacturer's name and address, the designation, the CE marking, the series or type, any serial number and the year of construction."]),
                 ("4. Try it on the spot", [
                     "Have the installer show you the manual release and how to lock it again. While the gate closes, break the photocell beam with an object, never your body, and check that it stops or reopens. Ask how the force was checked and whether the result is recorded."]),
                 ("5. A written summary", [
                     "Ask for a written note of the safety devices fitted, the number of remotes, the service interval and who services the gate. TTJA notes for overhead doors that the installer must hand over the user and maintenance instructions and the declaration of conformity."]),
             ],
             "sources": ["md", "ttja_uks"]},
            {"type": "sections", "tag": "Electrical work", "h": "Wiring and cables",
             "items": [
                 ("Who may connect the drive", [
                     "A layperson may only do the simple electrical tasks listed in the regulation, such as replacing fuses and bulbs or switching circuit breakers. Connecting a 230-volt gate drive is not on that list, so it must be done by a competent electrician.",
                     "The competence of the person responsible for electrical work must be certified, and a business doing electrical work commercially must file a notice in the Register of Economic Activities (MTR). Ask the installer who will do the wiring."]),
                 ("Cables in a duct", [
                     'We recommend running power and control cables underground in a protective duct, with spare room for photocells, a warning light and a future intercom. A cable in a duct is easy to replace and less likely to be cut when someone digs. If the fence is still being built, lay the duct before the posts are concreted, as our article on <a href="/en/fence-building-mistakes/">fence-building mistakes</a> explains.']),
             ],
             "sources": ["elektritoo", "kompetents", "seos"]},
            {"type": "sections", "tag": "Servicing", "h": "How servicing works, and winter",
             "items": [
                 ("How often", [
                     "The manufacturer sets the interval in the instructions. TTJA's example for overhead doors is every 3–6 months or every 1,000–5,000 operating cycles; it stresses that servicing is mandatory and suggests a service contract so it is not forgotten. A family gate opens a few times a day, a housing association or business gate dozens of times, so the busier the gate, the sooner it is due."]),
                 ("What servicing covers", [
                     'Servicing covers the carriages, rollers or hinges, the gap between rack and drive, fixings, limit switches, the force setting, photocells, safety edges and the manual release, with a written record of what was checked and replaced. A sliding gate that runs stiffly, sags or knocks usually has a mechanical cause; see our <a href="/en/fence-repair/sliding-gate-repair/">sliding gate repair</a> page.']),
                 ("Winter", [
                     "Snow and ice cover photocells and build up in front of swing leaves or along a sliding gate's path, and ice can make the gate stop halfway as if there were an obstacle. Clear the snow and clean the photocells rather than turning up the force.",
                     'Keep the release key indoors and check before the frosts that the release lock has not frozen. If the gate will not close in winter, see our <a href="/en/fence-repair/gate-wont-open/">guide to gate faults</a>. We compare how sliding and swing gates cope with snow in <a href="/en/sliding-or-swing-gate/">a separate article</a>.']),
             ],
             "sources": ["seos", "ttja_uks"]},
            {"type": "table", "tag": "Schedule", "h": "Who does what, and when",
             "headers": ("", "Who", "What to do"),
             "rows": [
                 ("Every month", "Owner", "Photocell test with an object, clearing the gate's path, listening for new noises"),
                 ("Before winter", "Technician or owner", "Cleaning the photocells, checking the manual release and the force setting"),
                 ("At least once a year", "Technician", "Servicing to the manufacturer's instructions and a written summary"),
                 ("After an impact, repair or parts replacement", "Installer or technician", "Checking alignment, the force setting and every safety device"),
                 ("If the gate does not stop for an obstacle", "Owner", "Stopping automatic use and calling a technician"),
             ],
             "note": "This is the rhythm we recommend. If the manufacturer's instructions call for more frequent servicing, follow the instructions."},
            {"type": "cards", "tag": "Questions", "h": "What to ask an installer before you sign", "cols": 2,
             "items": [
                 ("Who is the manufacturer, and which documents will I get?", "Who issues the declaration of conformity and affixes the CE marking if gate and drive are assembled on site? A good answer also names the Estonian instructions and maintenance guidance."),
                 ("Which safety devices are included?", 'Photocells, a safety edge, a warning light, how many of each and how the force is checked. In our <a href="/en/prices/">price guide</a>, an automated sliding gate includes the frame, foundation, drive and standard safety devices.'),
                 ("Who does the electrical work?", "Ask whether a competent electrician connects the drive and whether the company has filed its notice of economic activity."),
                 ("Who services it, and how often?", 'Ask for the interval and whether the company services gates itself. More questions are in our guide on <a href="/en/how-to-choose-a-fence-contractor/">how to choose a fence contractor</a>.'),
             ]},
            {"type": "cards", "tag": "Our advice", "h": "What we recommend", "cols": 2,
             "items": [
                 ("Fix the gate before automating it", "A stiff or sagging gate overloads the drive and makes obstacles harder to detect. Have it aligned and worn parts replaced before adding automation."),
                 ("A safety edge if there are children", "Photocells only protect the line of their beam. With children around or automatic closing, fit a safety edge to the closing edge."),
                 ("Auto-close only with confidence", "Automatic closing is convenient, but then the safety devices must be in perfect order. If children play near the gate, consider closing by remote only."),
                 ("Remotes are not toys", "Keep remotes out of children's reach and agree at home that the gate only moves when the opening is clear and in view."),
             ]},
            {"type": "cards", "tag": "Common problems", "h": "What often goes wrong", "cols": 2,
             "items": [
                 ("Covered photocells", "Snow, ice, dirt or an overgrown shrub covers a photocell and the gate will not close."),
                 ("Force set too high", "The force is turned up in winter or after a repair to get the gate moving, so the drive detects obstacles too late."),
                 ("Nobody knows the manual release", "During a power cut the car is stuck inside or outside because nobody can find the release key."),
                 ("Casual modifications", "Someone replaced the drive or a leaf without rechecking the safety devices or updating the documents, and the gate became dangerous."),
             ]},
        ],
        "faq": [
            ("Does an automatic gate need CE marking?", "Yes. A powered gate is a machine, and the manufacturer affixes the CE marking after the conformity assessment; for a gate assembled on site, that is generally the installer. Ask for the EC declaration of conformity at handover."),
            ("Which documents should I receive at handover?", "The EC declaration of conformity and instructions in Estonian that also describe the maintenance the user should carry out. The machine must be marked with the manufacturer's name and address, the CE marking and the year of construction. LuxAed hands all of this over with the gate, together with a list of the safety devices fitted and the service interval."),
            ("Can I connect the gate drive to the mains myself?", "Not unless you are a competent electrician. Connecting a 230-volt drive is not on the list of electrical work a layperson may do."),
            ("How often should an automatic gate be serviced?", "At the interval in the manufacturer's instructions, which may be set by time or by operating cycles. The Equipment Safety Act requires the use and maintenance requirements to be met. We recommend a service at least once a year and a check before winter."),
            ("Is it safe to add automation to an old gate?", "Yes, if the gate is structurally sound and the installer adds the necessary safety devices and takes on the manufacturer's obligations. The frame, hinges or carriages, posts and base must be assessed first, because a motor does not make a weak gate safe. In our price guide, automation for a suitable existing gate costs €500–1,250."),
            ("What changes in 2027?", "From 20 January 2027, machinery falls under the EU Machinery Regulation 2023/1230, which replaces the Machinery Directive 2006/42/EC. Instructions may then be supplied digitally, but if you ask at the time of purchase the manufacturer must provide a free paper copy."),
        ],
        "links_keys": ["gate_guide", "gate_wont_open", "sliding_gate"],
        "links_extra": [("/en/gates-automation/", "Automatic gates", "Installed with safety devices.")],
        "cta": ("We install automation safely", "At the site visit we assess the gate, base and power supply and suggest a drive with safety devices.", "/en/gates-automation/#form", "Get a gate quote"),
    },
}
