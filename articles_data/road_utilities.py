# -*- coding: utf-8 -*-
"""LuxAed article rewrite: road_utilities (/aed-tee-ja-trasside-lahedal/, /ru/zabor-u-dorogi-i-kommunikacij/,
/en/fence-near-road-and-utilities/).

Legal facts come from FACTS.md. Everything beyond FACTS.md was verified on 27.09.2026 in the primary
sources quoted below. New source keys are defined in NEW_SRC.

ehs = Riigi Teataja API akt 111072026032 (redaction 01.08.2026-30.09.2026). §§ 70-78 are word for word
identical in the redaction in force from 01.10.2026 (RT I, 11.07.2026, 33).
  § 70(2) "Kaitsevööndis on keelatud: ... 3) takistada ehitisele juurdepääsu; 4) takistada ehitise hooldamist, ..."
  § 70(3) "Nõusoleku andmise eest ei või kaitsevööndiga ehitise omanik võtta tasu ... Ehitise omanik ei või nõusoleku andmisest põhjendamatult keelduda. Kaitsevööndiga ehitise omanikul on õigus nõuda, et kaitsevööndis tegutsev isik on kaitsevööndiga ehitise omaniku vahetu järelevalve all."
  § 70(4) "Kaitsevööndiga ehitise omanik annab tasuta andmeid ehitise asukoha kohta kinnisasja omanikule ja selle õiguspärasele kasutajale."
  § 71(1) "Teel on kaitsevöönd, kui tee on avalikult kasutatav."
  § 71(4) "Käesoleva paragrahvi lõigetes 2 ja 3 nimetatud kaitsevööndi laiust võib tee omanik põhjendatud juhul vähendada."
  § 72(1)1 "paigaldada liiklejat häirivat valgustusseadet või teabe- ja reklaamivahendit;"
  § 72(2) "Tee kaitsevööndi maa kinnisasja omanik on kohustatud lubama kõrvaldada nähtavust piirava ja liiklusele ohtliku taimestiku, objekti või ehitise. Kinnisasja omanik peab võimaldama paigaldada tee kaitsevööndisse tee korrashoiuks ajutisi lumetõkkeid, rajada lumevalle ja kraave tuisklume tõkestamiseks ning paisata lund väljapoole teed, kui nimetatud tegevus ei takista juurdepääsu kinnisasjale."
  § 74(2)1 "ladustada materjale ning teha lõhkamis-, puurimis-, kaevandamis-, vaia-, kaeve-, täite-, üleujutus- või kuivendustöid ..."
  § 77(2)4 "ehitada traattarasid ja metallaedu, ... – kõrgepingepaigaldise õhuliinide kaitsevööndis;"
  § 77(2)5 "töötada löökmehhanismidega, tasandada pinnast, teha mullatöid sügavamal kui 0,3 meetrit, ... – õhu- ja maakaabelliinide kaitsevööndites."
  § 78(2)5 "töötada löökmehhanismidega, tihendada või tasandada pinnast, rajada transpordivahenditele ja mehhanismidele läbisõidukohti ning teha mullatöid sügavamal kui 0,3 meetrit ... – pinnases paikneva sideehitise kaitsevööndis."

kvoond = Riigi Teataja API akt 103022022020 (in force, RT I, 03.02.2022, 20)
  § 3 A-kategooria kuni 0,1 baari; B-kategooria "töörõhuga üle 0,1 baari kuni 5 baari (kaasa arvatud)"
  § 4(4) "Maakaabelliinide ja gaasitorustiku pinnasesse paigaldamisel pannakse pinnasesse kaabli või torustiku kohale kollane hoiatuslint. Hoiatuslinti ei pea paigaldama, kui kaabli või torustiku paigaldamise tehnoloogia seda ei võimalda."
  § 5(5) "... võib kaitsevööndiga ehitise omanik nõuda, et kaitsevööndis tegutsev isik on kaitsevööndiga ehitise omaniku vahetu järelevalve all. Samuti võib maakaabelliinide puhul nõuda maakaabli täpse asukoha väljaselgitamiseks pinnase käsitsi lahtikaevamist."
  § 6(1) "Kui kaitsevööndis tegutsemiseks on vajalik kaitsevööndiga ehitise omaniku nõusolek ja kui kaitsevööndiga ehitise omanik peab lisaks nõusoleku andmisele tegema ka täiendavaid toiminguid, võib ta nõuda nendega seonduva kulu hüvitamist."
  § 7(1) "1) peatab viivitamata oma tegevuse, ... 2) teavitab viivitamata ... kaitsevööndiga ehitise omanikku; 3) võtab tarvitusele abinõud edasise kahjustuse ärahoidmiseks; 4) kolmandatele isikutele tekkiva ohu korral teavitab neid ..."
  § 8(1)-(2) "... avastab tundmatu kaitsevööndiga ehitise ..., tuleb tööd peatada." "Tundmatust kaitsevööndiga ehitisest tuleb teatada kinnisasja omanikule ja tõenäolisele võrguettevõtjale, ..."
  § 10(1) "kuni 1 kV nimipingega (kaasa arvatud) liinide korral 2 meetrit;" "1 kV kuni 35 kV nimipingega liinidel õhukaabli kasutamise korral 3 meetrit;" "1 kV kuni 35 kV nimipingega liinide korral 10 meetrit;"
  § 10(3) "Maakaabelliini kaitsevöönd on piki kaablit kulgev ala, mida mõlemalt poolt piiravad liini äärmistest kaablitest 1 meetri kaugusel paiknevad mõttelised vertikaaltasandid."
  § 13(1)1 "A- ja B-kategooria gaasipaigaldiste korral torustiku välimisest mõõtmest 1 meetrit;"
  § 14 1) "maismaal – 1 meeter sideehitisest ..."

uvvkvoond (NEW) = Riigi Teataja API akt 114092023002, "Ühisveevärgi ja -kanalisatsiooni kaitsevööndi ulatus" (RT I, 14.09.2023, 2, in force)
  § 2(1)1 survetorustik "alla 250 mm siseläbimõõduga torustikul 2 m;"
  § 2(2)1 vabavoolne "torustikul, mille siseläbimõõt on alla 250 mm ja mis on paigaldatud kuni 2 m sügavusele, – 2 m;"
  § 2(2)2 "torustikul, mille siseläbimõõt on alla 250 mm ja mis on paigaldatud sügavamale kui 2 m, – 2,5 m;"

topo (NEW) = Riigi Teataja API akt 119042016003, "Topo-geodeetilisele uuringule ja teostusmõõdistamisele esitatavad nõuded" (RT I, 19.04.2016, 3, in force)
  § 2 p 1 "maa-ala topograafiline plaan (edaspidi maa-ala plaan või plaan) – ... millel esitatakse situatsioon, reljeef, tehnovõrgud ja piirid ..."
  § 28(1) "Maa-alune tehnovõrk kantakse maa-ala plaanile, ..."
  § 28(13) "Kui puudulike lähteandmete tõttu ei ole tagatud maa-aluse võrgurajatise asendi nõutav täpsus, tähistatakse see võrgurajatis maa-ala plaanil kirjega „ORIENT”."
  § 8(3)3 "nõuetekohase teostusjoonise puudumisel maa-aluse tehnovõrgu tasapinnalise asendi puhul 1 meeter."

memo743 (NEW, key requested in FACTS.md) = https://api.riigikogu.ee/api/files/1f9d6ed0-9752-4316-b110-6db182b450ba/download
  (downloaded 27.09.2026, 97-page PDF). NOTE: the passage is on printed page 41, not 40:
  "Muudatus on vajalik, sest esinenud on olukordi, kus tee kaitsevööndisse on püstitud ehitusloa ja ehitusteatise kohustuseta ehitisi, näiteks kasvuhoone, puukuur, piirdeaed, mis piiravad teel liiklemisel nähtavust või takistavad tee korrashoiutöid. Tee korrashoiutööde ja seire käigus tuvastatud nähtavust piirav ja liiklust ohustav taimestik, objekt või kaitsevööndisse ehitatud kasvuhoone, puukuur, aed või mõni muu planeeringule mittevastav või teeomaniku nõusolekuta püstitatud ehitis palutakse kinnisasja omanikul eemaldada. Kui kinnisasja omanik sellest keeldub ..., on tee omanikul õigus nähtavust piirav ja liiklusele ohtlik taimestik, objekt või ehitis kõrvaldada."

transpordiamet (NEW) = https://www.transpordiamet.ee/mahasoidud (fetched 27.09.2026)
  "Kinnistule juurdepääsu (ristumiskoha, mahasõidu) ehitamiseks riigiteelt peab maaomanik taotlema selleks Transpordiameti kooskõlastuse."
  "Kui teie kinnistu asub kohaliku tee ääres, siis annab juurdepääsu ehitamise kooskõlastuse kohalik omavalitsus (KOV)."
  "Kui teie kinnistu asub eratee ääres, siis tuleb kooskõlastus taotleda eratee omanikult."
  "Taotluse menetlemine võtab aega kuni 30 kalendripäeva."
  "Jälgida tuleb, et tee lähedal olevad ehitised, sh piirdeaiad ja -hekid ei varjaks nähtavust, sealhulgas näiteks hoovist väljasõitmisel."
  "Transpordiametil on õigus liiklusele ohtlik ehitis paluda kõrvaldada. Selle vältimiseks soovitame saata enne ehitamist asendiplaani joonise kooskõlastamiseks ..."
  "Riigitee kaitsevöönd ei tähenda ehituskeeluvööndit."
  "... teele liiga lähedale ehitatud ehitisi võivad kahjustada teelt sõidukite rataste alt lenduvad kivid, samuti talihooldel teelt tõrjutav lumi ning libedusetõrjel kasutatavad soolad."

elektrilevi (NEW) = https://elektrilevi.ee/et/teenused/kaitsevoondi-kooskolastused (fetched 27.09.2026; RU and EN pages also exist)
  "Elektriliini kaitsevööndis tegutsemine vajab alati liini omaniku nõusolekut."
  "Esita taotlus vähemalt 10 tööpäeva enne tööde algust."
  Price list item "Elektrivõrgu- ja alajaama kaitsevööndis toimuvate tegevuste järelevalve kohapeal" (a paid service).

harku = https://www.harku.ee/ehitus-planeerimine-ja-taristu/ehitamine-ja-muud-seonduvad-tegevused/rajatised (fetched 27.09.2026)
  "Kui kinnistu piir jääb lähemale kui 2 meetrit teekatte servast, tuleb tagada lume koristamise võimalus – piirdeaed peab asuma vähemalt 2 meetri kaugusel teekatte servast."
saue = Saue valla üldplaneering 2021, ch. 4.5 Arhitektuursed nõuded (PDF fetched 27.09.2026)
  "piirdeaedade rajamisel arvestada teekaitsevööndi nõuetega, piirdeaedu võib reeglina rajada teekatte servast minimaalselt 2 m kaugusele;"
  "piirdeaedu ei tohi rajada väljapoole krundi piire;"
rae = Rae valla põhjapiirkonna üldplaneering 2024, seletuskiri (PDF fetched 27.09.2026)
  "Väravate avanemist transpordimaa poole ei ole lubatud planeerida." (also: "Väravad ei tohi avaneda teemaale.")
maaamet = Maaomaniku meelespea (fetched 27.09.2026)
  "Tutvu ka võimalike seadustest tulenevate kitsendustega kitsenduste kaardil."
Terms page (FACTS.md): LuxAed is not liable for hidden utilities the customer did not disclose.
"""

NEW_SRC = {
    "memo743": {
        "et": ("Eelnõu 743 SE seletuskiri", "https://api.riigikogu.ee/api/files/1f9d6ed0-9752-4316-b110-6db182b450ba/download"),
        "ru": ("Пояснительная записка к законопроекту 743 SE", "https://api.riigikogu.ee/api/files/1f9d6ed0-9752-4316-b110-6db182b450ba/download"),
        "en": ("Explanatory memorandum to bill 743 SE", "https://api.riigikogu.ee/api/files/1f9d6ed0-9752-4316-b110-6db182b450ba/download"),
    },
    "transpordiamet": {
        "et": ("Transpordiamet, mahasõidud ja ehitamine kaitsevööndis", "https://www.transpordiamet.ee/mahasoidud"),
        "ru": ("Transpordiamet, съезды и строительство в охранной зоне", "https://www.transpordiamet.ee/mahasoidud"),
        "en": ("Transport Administration, access roads and building in the protection zone", "https://www.transpordiamet.ee/mahasoidud"),
    },
    "elektrilevi": {
        "et": ("Elektrilevi, kaitsevööndis tegutsemise luba", "https://elektrilevi.ee/et/teenused/kaitsevoondi-kooskolastused"),
        "ru": ("Elektrilevi, разрешение на работы в охранной зоне", "https://elektrilevi.ee/ru/teenused/kaitsevoondi-kooskolastused"),
        "en": ("Elektrilevi, permit to work in a protection zone", "https://elektrilevi.ee/en/teenused/kaitsevoondi-kooskolastused"),
    },
    "uvvkvoond": {
        "et": ("Ühisveevärgi ja -kanalisatsiooni kaitsevööndi ulatus", "https://www.riigiteataja.ee/akt/114092023002?leiaKehtiv"),
        "ru": ("Постановление об охранной зоне водопровода и канализации", "https://www.riigiteataja.ee/akt/114092023002?leiaKehtiv"),
        "en": ("Regulation on water and sewer protection zones", "https://www.riigiteataja.ee/akt/114092023002?leiaKehtiv"),
    },
    "topo": {
        "et": ("Topo-geodeetilise uuringu nõuded", "https://www.riigiteataja.ee/akt/119042016003?leiaKehtiv"),
        "ru": ("Требования к топогеодезическим изысканиям", "https://www.riigiteataja.ee/akt/119042016003?leiaKehtiv"),
        "en": ("Requirements for topographic surveys", "https://www.riigiteataja.ee/akt/119042016003?leiaKehtiv"),
    },
}

ARTICLE = {
    "et": {
        "title": "Aed tee kaitsevööndis ja trasside lähedal | LuxAed",
        "desc": "Aed tee kaitsevööndis ja kaablite lähedal: kui lai on kaitsevöönd, kellelt küsida trasside asukohta, kuhu jätta lumele ruumi ja kuidas paigutada värav.",
        "short": "Aed tee ja trasside lähedal",
        "image": "luxaed-profnastil-2",
        "kicker": "Juhend · tee ja trassid",
        "h1": "Aed tee kaitsevööndis<br><em>ja trasside lähedal</em>",
        "lead": "Tänavaäärne aed peab arvestama lumesaha, nähtavuse ja maa-aluste kaablitega, mida krundil sageli näha ei ole. Selgitame, mida seadus kaitsevööndis lubab, kellelt trasside asukohta küsida ning kuidas aed ja värav paigutada nii, et hiljem ei peaks midagi ümber tegema.",
        "direct": ("Enne postiaukude puurimist küsige trasside asukohad nende omanikelt ja kontrollige, kui kaugele ulatub teie krundile tee kaitsevöönd.",
                   "Seadus aeda tee kaitsevööndis otse ei keela, kuid omanik peab lubama nähtavust piirava ja liiklusele ohtliku ehitise eemaldamise. Kaabli ja toru lähedal on kaevetööd piiratud. Allpool leiate kaitsevööndite laiused, selle, kellelt andmeid ja nõusolekut küsida, ning meie soovitused lume, värava ja kaablitorude kohta."),
        "blocks": [
            {"type": "sections", "tag": "Tee kaitsevöönd", "h": "Kui lai on tee kaitsevöönd ja mida see aiale tähendab",
             "items": [
                 ("Kaitsevööndi laius", [
                     "Ehitusseadustiku § 71 järgi on tänava kaitsevööndi laius äärmise sõiduraja välisservast 10 meetrit ja üld- või detailplaneering võib seda laiendada kuni 50 meetrini. Maanteel on kaitsevöönd mõlemal pool teed 30 meetrit, üleeuroopalisse teedevõrku kuuluval maanteel 50 meetrit. Kaitsevöönd on ainult avalikult kasutataval teel ja tee omanik võib seda põhjendatud juhul vähendada."]),
                 ("Mida kaitsevööndis ei tohi ja mida peab lubama", [
                     "Sama seaduse § 72 keelab kaitsevööndis näiteks paigaldada liiklejat häirivaid valgusteid ja reklaami. Aeda see paragrahv otse ei keela, kuid kinnistu omanik peab lubama kõrvaldada nähtavust piirava ja liiklusele ohtliku taimestiku, objekti või ehitise.",
                     "Tee korrashoiuks peab omanik võimaldama ka paigaldada ajutisi lumetõkkeid, rajada lumevalle ja kraave tuisklume tõkestamiseks ning paisata lund teelt välja, kui see ei takista juurdepääsu kinnistule."]),
                 ("Seletuskiri nimetab piirdeaia otse", [
                     "Seaduse muudatuse seletuskiri toob näiteks tee kaitsevööndisse püstitatud kasvuhoone, puukuuri ja piirdeaia, mis piiravad nähtavust või takistavad tee korrashoiutöid. Sellise ehitise eemaldamist palutakse kõigepealt kinnistu omanikult ja kui ta keeldub, võib tee omanik nähtavust piirava ja liiklusele ohtliku ehitise ise kõrvaldada."]),
             ],
             "sources": ["ehs", "memo743"]},
            {"type": "sections", "tag": "Riigitee ja vald", "h": "Mida lisaks nõuavad Transpordiamet ja vallad",
             "items": [
                 ("Riigitee ääres", [
                     "Transpordiameti sõnul ei tähenda riigitee kaitsevöönd ehituskeeluvööndit. Tee lähedal olevad ehitised, sealhulgas piirdeaiad ja hekid, ei tohi aga varjata nähtavust, ka siis, kui sõidate hoovist välja. Amet võib paluda liiklusele ohtliku ehitise eemaldada ja soovitab seepärast saata asendiplaani joonise enne ehitamist kooskõlastamiseks."]),
                 ("Lumi, sool ja kivid", [
                     "Transpordiameti hinnangul võivad teele liiga lähedale ehitatud ehitisi kahjustada rataste alt lenduvad kivid, talihooldel teelt lükatud lumi ja libedusetõrjeks kasutatav sool. Kõige rohkem saavad tavaliselt kannatada postid ja aia alumine osa, nii et valige tänava äärde tsingitud ja värvitud metallosad ning jätke aia ja teekatte vahele lumele ruumi."]),
                 ("Harku ja Saue: vähemalt 2 m teekatte servast", [
                     "Harku vallas peab aed asuma teekatte servast vähemalt 2 meetri kaugusel, kui krundi piir jääb teele lähemale, et lund saaks koristada. Saue valla üldplaneeringu järgi võib aia reeglina rajada teekatte servast vähemalt 2 m kaugusele ja mitte väljapoole krundi piire. Teiste omavalitsuste aianõuded on koondatud juhendisse <a href=\"/aia-korgus-harjumaal/\">aia kõrgus Harjumaal</a>. Oma krundi kohta vaadake ka detailplaneeringut."]),
             ],
             "sources": ["transpordiamet", "harku", "saue"]},
            {"type": "sections", "tag": "Värav", "h": "Värav tee ääres: avanemine, ooteruum ja kaablitoru",
             "items": [
                 ("Tiibvärav ei tohiks avaneda tänavale", [
                     "Rae valla põhjapiirkonna üldplaneering ütleb, et väravate avanemist transpordimaa poole ei ole lubatud planeerida. Ka mujal soovitame, et tiibvärav avaneks hoovi poole, sest tänavale avanev tiib jääb ette jalakäijale, autole ja lumesahale. Kui hoovis tiibadele ruumi ei ole, sobib paremini liugvärav; nende erinevusi selgitame juhendis <a href=\"/liugvarav-voi-tiibvarav/\">liugvärav või tiibvärav</a>."]),
                 ("Jätke autole ruumi värava ette", [
                     "Kui sõiduvärav on otse tänava serval, ootab auto värava avanemist sõiduteel. Soovitame paigutada värava nii, et auto mahub värava ja sõidutee vahele ning sealt on hea nähtavus mõlemale poole. <a href=\"/varavad/\">Automaatvärava</a> saab avada puldiga juba lähenedes, nii et ootamine jääb lühemaks."]),
                 ("Uus sissesõit vajab kooskõlastust", [
                     "Kui väravale tuleb uus sissesõit, vajab juurdepääs teelt kooskõlastust: riigiteelt annab selle Transpordiamet, kohalikult teelt omavalitsus ja eratee puhul tee omanik. Transpordiameti menetlus võtab kuni 30 kalendripäeva, nii et küsige kooskõlastust enne värava tellimist."]),
                 ("Pange kaablitoru maasse koos aiaga", [
                     "Kui plaanite kunagi automaatväravat, <a href=\"/varavad/domofonid/\">videodomofoni</a> või valgustust värava juures, pange kaitsetorud maasse juba aia ehitusel, muidu tuleb hiljem kaevata läbi valmis sillutise. Tooge toru hoonest või kilbist värava postini, hoidke see teiste võrkude kaitsevööndist eemale või küsige ristumiseks võrgu omaniku nõusolekut ning pildistage torud enne tagasitäitmist. See on meie soovitus, mitte seaduse nõue."]),
             ],
             "sources": ["rae", "transpordiamet", "ehs"]},
            {"type": "sections", "tag": "Trassid", "h": "Kaablid ja torud: kellelt asukohta küsida",
             "intro": "Puur ei tee vahet kaablil ja kivil, seega selgitage trassid välja enne, kui aia joon on paigas.",
             "items": [
                 ("Võrgu omanik annab andmed tasuta", [
                     "Ehitusseadustiku § 70 järgi annab kaitsevööndiga ehitise omanik asukoha andmed kinnisasja omanikule tasuta ja kaitsevööndite andmed kantakse maakatastrisse. Maa- ja Ruumiamet soovitab vaadata ka kitsenduste kaarti. Küsige andmeid kõigilt, kelle võrk võib krundi piiril olla: elektri, side, vee ja kanalisatsiooni, gaasi ning kaugkütte võrgu omanikult.",
                     "Alustage varakult. Näiteks Elektrilevi rõhutab, et elektriliini kaitsevööndis tegutsemine vajab alati liini omaniku nõusolekut, ja palub taotluse esitada vähemalt 10 tööpäeva enne tööde algust."]),
                 ("Vaadake üle geodeetiline alusplaan", [
                     "Kui majale või aiale on tehtud geodeetiline alusplaan, on maa-alused tehnovõrgud üldjuhul sellele kantud. Kui trassi asukoha täpsus ei ole tagatud, on see plaanil märgitud kirjega „ORIENT”. Nõuetekohase teostusjoonise puudumisel lubab määrus trassi asukohas kuni 1 meetri suurust viga. Sellisel juhul selgitage täpne koht välja kohapeal."]),
                 ("Oma kaablitest ei pruugi võrgu omanik teada", [
                     "Võrgu omaniku andmetes ei ole tavaliselt kaableid ja torusid, mille olete ise rajanud, näiteks maja toitekaablit liitumiskilbist majani, aiavalgustust, drenaaži või vana väravaajami kaablit. Märkige need enne mõõdistust skeemile või näidake kohapeal. LuxAed ei vastuta <a href=\"/tingimused/\">kasutustingimuste</a> järgi varjatud trasside eest, millest tellija ei teatanud, nii et see on ka teie huvides."]),
             ],
             "sources": ["ehs", "maaamet", "elektrilevi", "topo"]},
            {"type": "sections", "tag": "Kaitsevööndid", "h": "Kui lähedale kaablile ja torule tohib kaevata",
             "items": [
                 ("Kaitsevööndite laius", [
                     "Elektri maakaabli kaitsevöönd ulatub äärmisest kaablist 1 meetri kaugusele kummalegi poole, maa-alusel sidekaablil samuti 1 meeter ning A- ja B-kategooria gaasitorul (töörõhk kuni 5 baari) 1 meeter. Ühisveevärgi ja -kanalisatsiooni alla 250 mm läbimõõduga torul on kaitsevöönd toru teljest 2 meetrit kummalegi poole, sügavamal kui 2 m asuval vabavoolsel torul 2,5 meetrit. Õhuliini kaitsevöönd on liini teljest kuni 1 kV liinil 2 meetrit ja 1–35 kV liinil 10 meetrit, õhukaabli korral 3 meetrit."]),
                 ("Mida kaitsevööndis ei tohi", [
                     "Elektrikaabli ja pinnases oleva sidekaabli kaitsevööndis on keelatud töötada löökmehhanismidega, näiteks poste sisse lüüa, ja teha mullatöid sügavamal kui 0,3 meetrit. Sidekaabli kaitsevööndis on keelatud ka rajada sõidukitele läbisõidukohti, mis puudutab uut sissesõitu. Ühisveevärgi ja -kanalisatsiooni kaitsevööndis on keelatud puurimis-, vaia- ja kaevetööd.",
                     "Kõrgepinge õhuliini kaitsevööndis on keelatud ehitada traattarasid ja metallaedu, nii et seal tuleb aia materjal ja asukoht võrgu omanikuga kokku leppida. Igas kaitsevööndis on keelatud ka takistada juurdepääsu võrgu rajatisele ja selle hooldust. Piirangutest võib kõrvale kalduda võrgu omaniku nõusolekul, kui see ei vähenda ohutust."]),
                 ("Nõusolek on tasuta, lisatööd ei pruugi olla", [
                     "Võrgu omanik ei tohi nõusoleku andmisest põhjendamatult keelduda ega selle eest tasu võtta. Ta võib aga nõuda, et töö toimuks tema vahetu järelevalve all, ja maakaabli puhul, et täpne asukoht selgitataks välja käsitsi kaevates. Kui ta peab lisaks nõusolekule tegema muid toiminguid, võib ta nõuda nende kulude hüvitamist; näiteks on Elektrilevil kohapealne järelevalve tasuline teenus."]),
             ],
             "sources": ["ehs", "kvoond", "uvvkvoond", "elektrilevi"]},
            {"type": "sections", "tag": "Kui midagi leiate", "h": "Kui mullast tuleb hoiatuslint või puur tabab kaablit",
             "items": [
                 ("Kollane lint tähendab stopp", [
                     "Maakaabli ja gaasitoru kohale pannakse pinnasesse üldjuhul kollane hoiatuslint. Kui see tuleb postiaugust välja, lõpetage kaevamine ja selgitage enne jätkamist välja, mis selle all on. Lindi puudumine ei tähenda, et kaablit ei ole: kui paigaldustehnoloogia linti ei võimalda, seda ei panda."]),
                 ("Kui kaabel või toru saab kahjustada", [
                     "Kaitsevööndis tegutseja peab kahjustuse või selle ohu korral töö viivitamata peatama, teatama võrgu omanikule, võtma tarvitusele abinõud edasise kahju vältimiseks ja hoiatama teisi. Kui leiate tundmatu kaabli või toru, tuleb töö peatada ja teatada kinnisasja omanikule ning tõenäolisele võrguettevõtjale."]),
             ],
             "sources": ["kvoond"]},
            {"type": "cards", "tag": "Meie soovitus", "h": "Mida me ise soovitame", "cols": 2,
             "items": [
                 ("Trassid enne pakkumist", "Kui trassid on enne mõõdistust teada, saame postide kohad ja aia joone kohe õigesti planeerida ning võtame need pakkumises arvesse."),
                 ("Jätke lumele ruumi", "Ka seal, kus vald vahemaad ette ei kirjuta, jätke aia ja teekatte vahele riba, kuhu sahk saab lume lükata."),
                 ("Nurgakrundil hoidke vaade vaba", "Ristmiku lähedal ei tohiks aed ega hekk juhi vaadet varjata. Madalam või läbipaistev <a href=\"/aiad/paneelaed/\">3D paneelaed</a> on seal ohutum kui kinnine aed."),
                 ("Posti ei panda kaabli peale", "Kui trass jääb aia joonele, nihutage posti või muutke välja pikkust. See on odavam kui kaabli remont."),
             ]},
            {"type": "cards", "tag": "Levinud probleemid", "h": "Mis läheb sageli valesti", "cols": 3,
             "items": [
                 ("Puur tabas kaablit", "Trasside asukohta ei küsitud enne puurimist või unustati omaniku enda kaabel."),
                 ("Sahk lõhkus aia", "Aed on teele liiga lähedal ja lumi lükatakse otse selle vastu."),
                 ("Aed varjab ristmikul vaate", "Kõrge kinnine aed või hekk nurgakrundil takistab hoovist väljasõitjal teed nägemast."),
                 ("Värav avaneb tänavale", "Tiib jääb ette jalakäijatele ja talvel ei saa lumevalli tõttu väravat lahti."),
                 ("Auto ootab sõiduteel", "Sõiduvärav on teeserval ja iga kord seisab auto avanemist oodates tänaval."),
                 ("Kaablitoru jäi panemata", "Automaatika lisamiseks tuleb valmis sillutis uuesti üles võtta."),
             ]},
        ],
        "faq": [
            ("Kui lai on tänava kaitsevöönd?", "Ehitusseadustiku järgi 10 meetrit äärmise sõiduraja välisservast. Üld- või detailplaneering võib seda laiendada kuni 50 meetrini, maanteel on kaitsevöönd 30 meetrit."),
            ("Kas tee kaitsevööndisse tohib aeda ehitada?", "Ehitusseadustik aeda tee kaitsevööndis otse ei keela, kuid omanik peab lubama kõrvaldada nähtavust piirava ja liiklusele ohtliku ehitise. Aia asukohale võivad lisanõudeid seada detailplaneering ja vald, riigitee ääres ka Transpordiamet."),
            ("Kui lähedal maakaablile tohib kaevata?", "Maakaabli kaitsevöönd ulatub 1 meetri kaugusele kummalegi poole kaablit. Selles vööndis ei tohi ilma võrgu omaniku nõusolekuta kaevata sügavamale kui 0,3 meetrit ega töötada löökmehhanismidega."),
            ("Kuidas saan teada, kas krundil on kaableid?", "Küsige andmeid võrkude omanikelt, kes annavad asukoha andmed tasuta, ja vaadake Maa- ja Ruumiameti kitsenduste kaarti. Enda rajatud kaablid, näiteks aiavalgustus ja maja toitekaabel, tuleb aga ise üles märkida."),
            ("Kas võrgu omaniku nõusolek maksab?", "Ei, nõusolek on tasuta ja võrgu omanik ei tohi sellest põhjendamatult keelduda. Kui ta peab lisaks tegema muid toiminguid, näiteks saatma kohale järelevalve, võib ta nõuda nende kulude hüvitamist."),
            ("Kas värav tohib avaneda tänava poole?", "Mõni planeering keelab selle: näiteks Rae valla põhjapiirkonna üldplaneeringu järgi ei tohi väravate avanemist transpordimaa poole planeerida. Soovitame igal juhul, et tiibvärav avaneks hoovi poole või et valitaks liugvärav."),
        ],
        "links_keys": ["permit_guide", "neighbour", "gate_safety"],
        "links_extra": [("/aiad/paneelaed/", "3D paneelaed", "Läbipaistev ja jäik aed tänava äärde.")],
        "cta": ("Planeerime tänavaäärse aia õigesti", "Tasuta mõõdistusel vaatame tee äärt, väravakohta ja trasside märgistust ning võtame need pakkumises arvesse.", "/#form", "Küsi pakkumist"),
    },
    "ru": {
        "title": "Забор у дороги и коммуникаций: охранная зона | LuxAed",
        "desc": "Забор у дороги и рядом с кабелями: ширина охранной зоны, у кого узнать, где проходят сети, где оставить место для снега и как поставить ворота.",
        "short": "Забор у дороги и коммуникаций",
        "image": "luxaed-profnastil-2",
        "kicker": "Руководство · дорога и сети",
        "h1": "Забор у дороги<br><em>и коммуникаций</em>",
        "lead": "Забор вдоль улицы должен учитывать снегоуборщик, обзор и подземные кабели, которых на участке обычно не видно. Объясняем, что закон разрешает в охранной зоне, у кого узнавать, где проходят сети, и как расположить забор и ворота, чтобы потом ничего не переделывать.",
        "direct": ("До бурения ям под столбы узнайте у владельцев сетей, где идут коммуникации, и проверьте, заходит ли на участок охранная зона дороги.",
                   "Закон прямо не запрещает забор в охранной зоне дороги, но владелец обязан позволить убрать постройку, которая ограничивает обзор и опасна для движения, а рядом с кабелем и трубой земляные работы ограничены. Ниже разбираем расстояния, к кому обращаться за данными и согласием, и даём советы по снегу, воротам и кабельным трубам."),
        "blocks": [
            {"type": "sections", "tag": "Охранная зона дороги", "h": "Какой ширины охранная зона дороги и что она значит для забора",
             "items": [
                 ("Ширина охранной зоны", [
                     "По § 71 строительного кодекса ширина охранной зоны улицы составляет 10 метров от внешнего края крайней полосы, и общая или детальная планировка может расширить её до 50 метров. У шоссе охранная зона составляет 30 метров с каждой стороны, а у шоссе трансъевропейской сети она равна 50 метрам. Охранная зона есть только у дороги общего пользования, и владелец дороги может в обоснованном случае её уменьшить."]),
                 ("Что запрещено и что нужно допускать", [
                     "Тот же закон в § 72 запрещает в охранной зоне, например, устанавливать мешающее водителям освещение и рекламу. Забор этот параграф прямо не запрещает, но владелец участка обязан позволить убрать растения, объекты или постройки, которые ограничивают обзор и опасны для движения.",
                     "Для содержания дороги владелец также должен допускать временные снегозадерживающие щиты, снежные валы и канавы против заносов и сброс снега с дороги, если это не мешает подъезду к участку."]),
                 ("Пояснительная записка прямо называет забор", [
                     "Пояснительная записка к изменению закона приводит в пример поставленные в охранной зоне дороги теплицу, дровяник и забор, которые ограничивают обзор или мешают работам по содержанию дороги. Владельца участка сначала просят убрать такую постройку, а если он отказывается, владелец дороги может сам убрать постройку, которая ограничивает обзор и опасна для движения."]),
             ],
             "sources": ["ehs", "memo743"]},
            {"type": "sections", "tag": "Госдорога и волость", "h": "Что дополнительно требуют Transpordiamet и волости",
             "items": [
                 ("У государственной дороги", [
                     "По словам Transpordiamet (Транспортного департамента), охранная зона государственной дороги не означает запрета на строительство. Но постройки у дороги, включая заборы и живые изгороди, не должны закрывать обзор, в том числе при выезде со двора. Департамент может попросить убрать опасную для движения постройку и поэтому советует до строительства отправить на согласование чертёж ситуационного плана."]),
                 ("Снег, соль и камни", [
                     "По оценке Transpordiamet, камни из-под колёс, снег, который при зимнем содержании сталкивают с дороги, и соль против гололёда могут повредить постройки, стоящие слишком близко к дороге. Сильнее всего обычно страдают столбы и нижняя часть забора, поэтому у улицы выбирайте оцинкованные и окрашенные металлические детали и оставьте между забором и покрытием место для снега."]),
                 ("Харку и Сауэ: не ближе 2 м от края покрытия", [
                     "В волости Харку забор должен стоять не ближе 2 метров от края дорожного покрытия, если граница участка проходит ближе к дороге, чтобы можно было убирать снег. По общей планировке волости Сауэ забор, как правило, можно ставить не ближе 2 м от края покрытия и не за пределами участка. Требования к заборам в других самоуправлениях собраны в статье <a href=\"/ru/vysota-zabora-v-harjumaa/\">высота забора в Харьюмаа</a>, а для вашего участка смотрите и детальную планировку."]),
             ],
             "sources": ["transpordiamet", "harku", "saue"]},
            {"type": "sections", "tag": "Ворота", "h": "Ворота у дороги: открывание, место для машины и кабельная труба",
             "items": [
                 ("Распашные ворота лучше не открывать на улицу", [
                     "Общая планировка северной части волости Раэ говорит, что планировать открывание ворот в сторону транспортной земли не разрешается. И в других местах мы советуем, чтобы распашные ворота открывались во двор: створка на улице мешает пешеходам, машинам и снегоуборщику. Если во дворе нет места для створок, лучше подойдут откатные ворота; разницу объясняем в статье <a href=\"/ru/otkatnye-ili-raspashnye-vorota/\">откатные или распашные ворота</a>."]),
                 ("Оставьте место для машины перед воротами", [
                     "Если въездные ворота стоят прямо у края улицы, машина ждёт их открытия на проезжей части. Советуем расположить ворота так, чтобы машина помещалась между воротами и проезжей частью и оттуда был хороший обзор в обе стороны. <a href=\"/ru/vorota-avtomatika/\">Автоматические ворота</a> можно открыть пультом ещё на подъезде, и ждать придётся меньше."]),
                 ("Новый въезд нужно согласовать", [
                     "Если к воротам вы делаете новый въезд, съезд с дороги нужно согласовать. Согласование съезда с государственной дороги даёт Transpordiamet; если дорога местная, то самоуправление, а если частная, то её владелец. Рассмотрение в Transpordiamet занимает до 30 календарных дней, поэтому запросите согласование до заказа ворот."]),
                 ("Заложите кабельную трубу вместе с забором", [
                     "Если вы когда-нибудь планируете автоматику, <a href=\"/ru/domofony-videodomofony/\">видеодомофон</a> или свет у ворот, заложите защитные трубы уже при строительстве забора, иначе потом придётся копать через готовое мощение. Ведите трубу от дома или щита до столба ворот, обходите охранные зоны других сетей или получите согласие их владельца на пересечение и сфотографируйте трубы до засыпки. Это наша рекомендация, а не требование закона."]),
             ],
             "sources": ["rae", "transpordiamet", "ehs"]},
            {"type": "sections", "tag": "Сети", "h": "Кабели и трубы: у кого узнать, где они проходят",
             "intro": "Бур не отличает кабель от камня, поэтому выясните, где проходят сети, до того как линия забора окончательно намечена.",
             "items": [
                 ("Владелец сети даёт данные бесплатно", [
                     "По § 70 строительного кодекса владелец сооружения с охранной зоной бесплатно даёт владельцу участка данные о его расположении, а сведения об охранных зонах вносятся в земельный кадастр. Maa- ja Ruumiamet советует посмотреть и карту ограничений. Запросите данные у всех, чья сеть может проходить по границе участка: у владельцев электрических сетей, сетей связи, водопровода и канализации, газа и центрального отопления.",
                     "Начинайте заранее. Например, Elektrilevi подчёркивает, что работы в охранной зоне электролинии всегда требуют согласия её владельца, и просит подавать заявку минимум за 10 рабочих дней до начала работ."]),
                 ("Посмотрите геодезическую подоснову", [
                     "Если для дома или забора делали геодезическую подоснову, подземные сети на ней, как правило, показаны. Если точность положения трассы не гарантирована, на плане она помечена надписью «ORIENT», а без надлежащего исполнительного чертежа постановление допускает ошибку положения трассы до 1 метра. В таком случае точное место выясняйте на месте."]),
                 ("О ваших собственных кабелях владелец сети может не знать", [
                     "В данных владельца сети обычно нет кабелей и труб, которые вы проложили сами: питающего кабеля от щита подключения до дома, садового освещения, дренажа или старого кабеля привода ворот. Отметьте их на схеме до замера или покажите на месте. По нашим <a href=\"/ru/tingimused/\">условиям обслуживания</a> LuxAed не отвечает за скрытые коммуникации, о которых заказчик не сообщил, так что это и в ваших интересах."]),
             ],
             "sources": ["ehs", "maaamet", "elektrilevi", "topo"]},
            {"type": "sections", "tag": "Охранные зоны", "h": "Насколько близко к кабелю и трубе можно копать",
             "items": [
                 ("Ширина охранных зон", [
                     "Охранная зона подземного электрокабеля проходит в 1 метре от крайнего кабеля с каждой стороны, у подземного кабеля связи она тоже составляет 1 метр, а у газопровода категорий A и B (рабочее давление до 5 бар) также равна 1 метру. У трубы общественного водопровода и канализации диаметром меньше 250 мм зона составляет 2 метра от оси трубы в каждую сторону, а у самотечной трубы глубже 2 м она составляет 2,5 метра. Охранная зона воздушной линии от её оси составляет 2 метра для линий до 1 кВ и 10 метров для линий 1–35 кВ, а при самонесущем изолированном кабеле составляет 3 метра."]),
                 ("Что запрещено в охранной зоне", [
                     "В охранной зоне электрокабеля и подземного кабеля связи запрещено работать ударными механизмами, например забивать столбы, и вести земляные работы глубже 0,3 метра. В охранной зоне кабеля связи также запрещено устраивать проезды для транспорта, что касается нового въезда. В охранной зоне водопровода и канализации запрещены буровые, свайные и земляные работы.",
                     "В охранной зоне высоковольтной воздушной линии запрещено ставить проволочные и металлические заборы, поэтому материал и место забора там нужно согласовать с владельцем сети. В любой охранной зоне нельзя и мешать доступу к сооружению сети и его обслуживанию. От этих ограничений можно отступить с согласия владельца сети, если это не снижает безопасность."]),
                 ("Согласие бесплатное, а дополнительные работы могут быть платными", [
                     "Владелец сети не вправе без оснований отказать в согласии или брать за него плату. Но он может потребовать, чтобы работы шли под его непосредственным надзором, а в случае подземного кабеля также потребовать, чтобы точное место выяснили ручной раскопкой. Если кроме согласия ему нужно выполнить другие действия, он может потребовать возместить связанные с ними расходы: например, надзор на месте у Elektrilevi является платной услугой."]),
             ],
             "sources": ["ehs", "kvoond", "uvvkvoond", "elektrilevi"]},
            {"type": "sections", "tag": "Если что-то нашли", "h": "Если в яме показалась лента или бур задел кабель",
             "items": [
                 ("Жёлтая лента значит стоп", [
                     "Над подземным кабелем и газопроводом в грунт, как правило, укладывают жёлтую сигнальную ленту. Если она показалась в яме под столб, прекратите копать и до продолжения выясните, что под ней. Отсутствие ленты не значит, что кабеля нет: если технология прокладки её не позволяет, ленту не кладут."]),
                 ("Если кабель или трубу повредили", [
                     "При повреждении или угрозе повреждения тот, кто работает в охранной зоне, должен немедленно остановить работы, сообщить владельцу сети, принять меры против дальнейшего ущерба и предупредить других. Если нашли неизвестный кабель или трубу, работу нужно остановить и сообщить владельцу участка и вероятному сетевому предприятию."]),
             ],
             "sources": ["kvoond"]},
            {"type": "cards", "tag": "Наш совет", "h": "Что советуем мы", "cols": 2,
             "items": [
                 ("Сети до предложения", "Если трассы известны до замера, мы сразу правильно спланируем места столбов и линию забора и учтём их в предложении."),
                 ("Оставьте место для снега", "Даже там, где волость не задаёт расстояние, оставьте между забором и покрытием полосу, куда снегоуборщик сможет сдвинуть снег."),
                 ("На угловом участке лучше не закрывать обзор", "Рядом с перекрёстком забор и живую изгородь лучше делать такими, чтобы они не закрывали водителю обзор. Низкий или прозрачный <a href=\"/ru/zabory/2d-3d-setka/\">забор из 3D-панелей</a> там безопаснее глухого."),
                 ("Столб не ставят на кабель", "Если трасса попадает на линию забора, сдвиньте столб или измените длину пролёта. Это дешевле ремонта кабеля."),
             ]},
            {"type": "cards", "tag": "Частые проблемы", "h": "Что часто идёт не так", "cols": 3,
             "items": [
                 ("Бур задел кабель", "О трассах не спросили до бурения или забыли собственный кабель владельца."),
                 ("Снегоуборщик сломал забор", "Забор слишком близко к дороге, и снег сталкивают прямо на него."),
                 ("Забор закрывает обзор на перекрёстке", "Высокий глухой забор или изгородь на угловом участке мешает выезжающему со двора видеть дорогу."),
                 ("Ворота открываются на улицу", "Створка мешает пешеходам и упирается в снежный вал, а зимой ворота не открыть."),
                 ("Машина ждёт на дороге", "Въездные ворота стоят у края проезжей части, и машина каждый раз ждёт на улице."),
                 ("Не заложили кабельную трубу", "Чтобы добавить автоматику, приходится снова разбирать готовое мощение."),
             ]},
        ],
        "faq": [
            ("Какой ширины охранная зона улицы?", "По строительному кодексу она составляет 10 метров от внешнего края крайней полосы. Общая или детальная планировка может расширить её до 50 метров, а у шоссе охранная зона составляет 30 метров."),
            ("Можно ли ставить забор в охранной зоне дороги?", "Строительный кодекс прямо не запрещает забор в охранной зоне дороги, но владелец обязан позволить убрать постройку, которая ограничивает обзор и опасна для движения. Дополнительные требования к месту забора могут ставить детальная планировка и волость, а у государственной дороги также Transpordiamet."),
            ("Насколько близко к подземному кабелю можно копать?", "Охранная зона подземного кабеля проходит в 1 метре от него с каждой стороны. В этой зоне без согласия владельца сети нельзя копать глубже 0,3 метра и работать ударными механизмами."),
            ("Как узнать, есть ли на участке кабели?", "Запросите данные у владельцев сетей, которые дают сведения о расположении бесплатно, и посмотрите карту ограничений Maa- ja Ruumiamet. Кабели, которые вы проложили сами, например для садового освещения или питания дома, нужно отметить самим."),
            ("Согласие владельца сети платное?", "Нет, согласие бесплатное, и владелец сети не может без оснований в нём отказать. Если ему нужно выполнить дополнительные действия, например прислать надзор на место, он может потребовать возместить эти расходы."),
            ("Можно ли, чтобы ворота открывались на улицу?", "Некоторые планировки это запрещают: например, по общей планировке северной части волости Раэ открывание ворот в сторону транспортной земли планировать нельзя. Мы в любом случае советуем делать распашные ворота с открыванием во двор или выбрать откатные."),
        ],
        "links_keys": ["permit_guide", "neighbour", "gate_safety"],
        "links_extra": [("/ru/zabory/2d-3d-setka/", "Забор из 3D-панелей", "Прозрачный и жёсткий забор вдоль улицы.")],
        "cta": ("Правильно спланируем забор у улицы", "На бесплатном замере посмотрим край дороги, место ворот и отметки сетей и учтём их в предложении.", "/ru/#form", "Оставить заявку"),
    },
    "en": {
        "title": "Fences near Roads and Utilities: Protection Zones | LuxAed",
        "desc": "A fence near a road or buried cables: how wide the protection zones are, who to ask about utilities, where to leave room for snow and where to put the gate.",
        "short": "Fences near roads and utilities",
        "image": "luxaed-profnastil-2",
        "kicker": "Guide · roads and utilities",
        "h1": "Fences near roads<br><em>and utilities</em>",
        "lead": "A street-side fence has to cope with snowploughs, sight lines and buried cables you usually cannot see. We explain what the law allows in protection zones, who to ask where the utilities run and how to place the fence and gate so nothing has to be redone later.",
        "direct": ("Before drilling post holes, ask the network owners where their utilities run and check how far the road protection zone reaches your plot.",
                   "The law does not ban fences in a road protection zone as such, but the owner must allow the removal of a structure that restricts visibility and endangers traffic, and digging near cables and pipes is restricted. Below we cover the distances, who to ask for data and consent, and our advice on snow, gates and cable ducts."),
        "blocks": [
            {"type": "sections", "tag": "Road protection zone", "h": "How wide the road protection zone is and what it means for a fence",
             "items": [
                 ("Zone width", [
                     "Under § 71 of the Building Code, a street's protection zone extends 10 metres from the outer edge of the outermost lane, and a general or detailed plan may widen it to 50 metres. A highway's zone is 30 metres on each side, or 50 metres on the trans-European road network. Only publicly used roads have a protection zone, and the road owner may reduce it in justified cases."]),
                 ("What is banned and what you must allow", [
                     "Section 72 of the same Act bans, for example, lights that distract road users and advertising in the zone. It does not ban fences directly, but the landowner must allow the removal of vegetation, objects or structures that restrict visibility and endanger traffic.",
                     "For road maintenance, the owner must also allow temporary snow fences, snow banks and ditches against drifting snow, and snow to be thrown off the road, as long as this does not block access to the property."]),
                 ("The explanatory memorandum names fences", [
                     "The explanatory memorandum to the amendment gives a greenhouse, a woodshed and a fence built in the road protection zone as examples of structures that restrict visibility or hinder road maintenance. The landowner is first asked to remove such a structure, and if they refuse, the road owner may itself remove a structure that restricts visibility and endangers traffic."]),
             ],
             "sources": ["ehs", "memo743"]},
            {"type": "sections", "tag": "State roads and municipalities", "h": "Extra rules from the Transport Administration and municipalities",
             "items": [
                 ("Next to a state road", [
                     "The Transport Administration says a state road's protection zone is not a no-build zone. Structures near the road, such as fences and hedges, must not block visibility, for example when you drive out of your yard. The Administration may ask for a structure that endangers traffic to be removed, so it recommends sending a site plan drawing for approval before you build."]),
                 ("Snow, salt and stones", [
                     "According to the Transport Administration, structures built too close to the road can be damaged by stones thrown up by tyres, snow pushed off the road in winter maintenance and de-icing salt. Posts and the lower part of the fence usually suffer most, so use galvanised, coated metal parts by the street and leave room for snow between the fence and the road surface."]),
                 ("Harku and Saue: at least 2 m from the road surface", [
                     "In Harku Municipality the fence must stand at least 2 metres from the edge of the road surface where the plot boundary is closer to the road, so that snow can be cleared. Under the Saue general plan, a fence may as a rule be built at least 2 m from the edge of the road surface and not outside the plot. Fence rules for other municipalities are collected in our guide to <a href=\"/en/fence-height-rules-harju-county/\">fence height rules in Harju County</a>, and check your plot's detailed plan too."]),
             ],
             "sources": ["transpordiamet", "harku", "saue"]},
            {"type": "sections", "tag": "The gate", "h": "A gate by the road: opening, waiting space and a cable duct",
             "items": [
                 ("A swing gate should not open onto the street", [
                     "The general plan for Rae's northern area says gates may not be planned to open towards road land. Elsewhere too we recommend that a swing gate opens into the yard, because a leaf swinging over the street gets in the way of pedestrians, cars and the snowplough. If there is no room for the leaves inside, a sliding gate fits better; we compare the two in <a href=\"/en/sliding-or-swing-gate/\">sliding or swing gate</a>."]),
                 ("Leave room for the car in front of the gate", [
                     "If the driveway gate sits right at the edge of the street, the car waits on the carriageway while it opens. We recommend placing the gate so the car fits between the gate and the carriageway, with a clear view both ways. An <a href=\"/en/gates-automation/\">automatic gate</a> can be opened with the remote as you approach, which shortens the wait."]),
                 ("A new driveway needs approval", [
                     "If the gate comes with a new driveway, the access from the road needs approval: the Transport Administration gives it for a state road, the municipality for a local road and the owner for a private road. The Transport Administration takes up to 30 calendar days, so ask before you order the gate."]),
                 ("Lay the cable duct with the fence", [
                     "If you might ever want automation, a <a href=\"/en/intercoms-video-intercoms/\">video intercom</a> or lighting at the gate, lay protective ducts while the fence is being built, otherwise you will later have to dig through finished paving. Run the duct from the house or distribution board to the gate post, keep out of other utilities' protection zones or get the network owner's consent to cross, and photograph the ducts before backfilling. This is our recommendation, not a legal requirement."]),
             ],
             "sources": ["rae", "transpordiamet", "ehs"]},
            {"type": "sections", "tag": "Utilities", "h": "Cables and pipes: who to ask where they run",
             "intro": "An auger cannot tell a cable from a stone, so find the utilities before the fence line is fixed.",
             "items": [
                 ("Network owners provide data free of charge", [
                     "Under § 70 of the Building Code, the owner of a structure with a protection zone gives the landowner its location data free of charge, and protection zones are entered in the land cadastre. The Land and Spatial Development Board also suggests checking its restrictions map. Ask everyone whose network may run along your boundary: the electricity, telecom, water and sewer, gas and district heating network owners.",
                     "Start early. Elektrilevi, for example, stresses that any work in a power line's protection zone always needs the line owner's consent and asks for the application at least 10 working days before work starts."]),
                 ("Check the geodetic base plan", [
                     "If a geodetic base plan (topographic survey) was made for your house or fence, underground utilities are normally shown on it. Where the accuracy of a line's position is not guaranteed, it is marked ‘ORIENT’ on the plan, and without a proper as-built drawing the regulation allows the line's position to be out by up to 1 metre. In that case, find the exact location on site."]),
                 ("Network owners may not know about your own cables", [
                     "Network owners' data usually does not include cables and pipes you laid yourself: the supply cable from the meter cabinet to the house, garden lighting, drainage or an old gate-motor cable. Mark them on a sketch before the site visit or show them on site. Under our <a href=\"/en/terms/\">terms of service</a>, LuxAed is not liable for hidden utilities the customer did not disclose, so it is in your interest too."]),
             ],
             "sources": ["ehs", "maaamet", "elektrilevi", "topo"]},
            {"type": "sections", "tag": "Protection zones", "h": "How close to a cable or pipe you may dig",
             "items": [
                 ("Zone widths", [
                     "An underground power cable's protection zone runs 1 metre from the outermost cable on each side, an underground telecom cable's is also 1 metre and a category A or B gas pipe's (working pressure up to 5 bar) is 1 metre too. A public water or sewer pipe under 250 mm has a zone of 2 metres on each side of its axis, or 2.5 metres for a gravity pipe deeper than 2 m. An overhead line's zone, measured from its axis, is 2 metres for lines up to 1 kV and 10 metres for 1–35 kV lines, or 3 metres where aerial cable is used."]),
                 ("What is banned in the zone", [
                     "In the protection zone of a power cable or an underground telecom cable, impact tools such as a post driver are banned, as is soil work deeper than 0.3 metres. In a telecom cable's zone, building vehicle crossings is also banned, which matters for a new driveway. In a water and sewer zone, drilling, piling and excavation are banned.",
                     "In the protection zone of a high-voltage overhead line, wire and metal fences are not allowed, so agree the fence material and position with the network owner there. In any protection zone you must also not block access to the network structure or its maintenance. You may depart from these restrictions with the network owner's consent if safety is not reduced."]),
                 ("Consent is free, extra work may not be", [
                     "The network owner may not unreasonably refuse consent or charge for it. They may, however, require the work to be done under their direct supervision and, for an underground cable, the exact location to be found by hand digging. If they have to do more than give consent, they may ask you to cover those costs: Elektrilevi, for example, charges for on-site supervision."]),
             ],
             "sources": ["ehs", "kvoond", "uvvkvoond", "elektrilevi"]},
            {"type": "sections", "tag": "If you find something", "h": "If warning tape turns up or the auger hits a cable",
             "items": [
                 ("Yellow tape means stop", [
                     "Yellow warning tape is normally laid in the ground above an underground cable or gas pipe. If it turns up in a post hole, stop digging and find out what is underneath before you continue. No tape does not mean no cable: where the laying method does not allow tape, none is used."]),
                 ("If a cable or pipe is damaged", [
                     "Anyone working in a protection zone who damages a structure, or risks doing so, must stop immediately, inform the network owner, take steps to prevent further damage and warn others. If you find an unknown cable or pipe, stop work and inform the landowner and the likely network operator."]),
             ],
             "sources": ["kvoond"]},
            {"type": "cards", "tag": "Our advice", "h": "What we recommend", "cols": 2,
             "items": [
                 ("Utilities before the quote", "If the utilities are known before the site visit, we can plan post positions and the fence line correctly straight away and allow for them in the quote."),
                 ("Leave room for snow", "Even where the municipality sets no distance, leave a strip between the fence and the road surface where the plough can push snow."),
                 ("Keep sight lines clear on a corner plot", "Near a junction, a fence or hedge should not block a driver's view. A lower or see-through fence, such as <a href=\"/en/fences/mesh/\">3D mesh panels</a>, is safer there than a solid one."),
                 ("No post on top of a cable", "If a utility line crosses the fence line, move the post or change the panel length. That is cheaper than a cable repair."),
             ]},
            {"type": "cards", "tag": "Common problems", "h": "What often goes wrong", "cols": 3,
             "items": [
                 ("The auger hit a cable", "Nobody asked about utilities before drilling, or the owner's own cable was forgotten."),
                 ("The plough damaged the fence", "The fence is too close to the road and snow is pushed straight against it."),
                 ("The fence blocks the view at a junction", "A tall solid fence or hedge on a corner plot stops drivers leaving the yard from seeing the road."),
                 ("The gate opens onto the street", "The leaf blocks pedestrians and hits the snow bank, and in winter the gate will not open."),
                 ("The car waits on the road", "The driveway gate is at the road edge, so the car waits in the street every time."),
                 ("No cable duct was laid", "Adding automation means lifting finished paving again."),
             ]},
        ],
        "faq": [
            ("How wide is a street's protection zone?", "Under the Building Code, 10 metres from the outer edge of the outermost lane. A general or detailed plan may widen it to 50 metres, and a highway's zone is 30 metres."),
            ("Can I build a fence in a road protection zone?", "The Building Code does not ban fences in the zone directly, but the owner must allow the removal of a structure that restricts visibility and endangers traffic. The detailed plan and the municipality, and next to a state road the Transport Administration, may set extra requirements for the fence position."),
            ("How close to an underground cable can I dig?", "An underground cable's protection zone runs 1 metre on each side of it. Within that zone you may not dig deeper than 0.3 metres or use impact tools without the network owner's consent."),
            ("How do I find out if there are cables on my plot?", "Ask the network owners, who provide location data free of charge, and check the Land and Spatial Development Board's restrictions map. Cables you laid yourself, such as for garden lighting or the house supply, you have to mark yourself."),
            ("Does the network owner charge for consent?", "No, consent is free and may not be refused without good reason. If the owner has to do more, such as send someone to supervise on site, they may ask you to cover those costs."),
            ("Can the gate open towards the street?", "Some plans forbid it: the general plan for Rae's northern area, for example, says gates may not be planned to open towards road land. We recommend in any case that a swing gate opens into the yard, or choosing a sliding gate."),
        ],
        "links_keys": ["permit_guide", "neighbour", "gate_safety"],
        "links_extra": [("/en/fences/mesh/", "3D mesh panel fence", "See-through and rigid for street boundaries.")],
        "cta": ("Let's plan your street-side fence properly", "At the free site visit we look at the road edge, the gate position and utility markings and allow for them in the quote.", "/en/#form", "Get a quote"),
    },
}
