# -*- coding: utf-8 -*-
"""LuxAed article rewrite: neighbour (/aed-naabri-piiril/, /ru/zabor-s-sosedom/, /en/boundary-fence-neighbour/).

Legal facts come from FACTS.md. Facts beyond FACTS.md were verified on 27.09.2026 in the primary
sources below. All of them use EXISTING source keys (aos, maaamet, harku), so NEW_SRC is empty.

aos = Riigi Teataja API akt 128012026007 (redaction 07.02.2026-30.09.2026). The cited paragraphs
(128, 129, 141, 145, 147-151) are word for word identical in the redaction in force from 01.10.2026
(RT I, 30.06.2026, 5), so the page stays correct after 1 October.
  § 128(1) "Piir külgnevate maatükkide vahel määratakse maakatastri andmete ja piirimärkidega seaduses sätestatud korras."
  § 128(2) "Kinnisasja omanik peab tagama piirimärgistuse säilimise. Ta ei või piirimärke muuta ega ümber paigutada."
  § 129(4) "Piiri kindlakstegemise kulud kannavad naabrid võrdselt, kui seadusest, kohtulahendist või tehingust ei tulene teisiti."
  § 141(1) "Seadusjärgne kitsendus kehtib kinnistusraamatusse kandmata."
  § 141(3) "Kohtulahendi või tehinguga seatud kitsendus, samuti selle kitsenduse muutmine või lõpetamine kehtib kolmandate isikute suhtes, kui see on kinnistusraamatusse kantud."
  § 145(1) "Ehitist tuleb hoida sellises korras, et selle varisemisel või osade eraldumisel oleks välistatud naaberkinnisasja kahjustamine."
  § 145(2) "Omanik, kelle kinnisasja ohustavad käesoleva paragrahvi 1. lõikes nimetatud asjaolud, võib nõuda kahjuliku toime eest vastutavalt isikult ohu kõrvaldamist."
  § 147 "... peab naaberkinnisasja omanik seda lubama, kui see on hädavajalik, tingimusel, et temale tagatakse kahju hüvitamine."
  § 148(3) "Naaberkinnisasja omanik võib nõuda ehitajalt oma kinnisasja piiridesse ulatuva ehitise osa kõrvaldamist, kui ehitaja on pahauskne või kui kinnisasja omanik enne ehitamise algust või hiljemalt ajal, mil selle osa kõrvaldamine ei olnud seotud ülemääraste kulutustega, sellele vastu vaidles."
  § 148(4) "Kokkulepe hüvitise suuruse või hüvitisest loobumise kohta kehtib, kui see on kantud märkusena kinnistusraamatusse."
  § 149(1) "Kinnisasja omanikul on õigus ära lõigata ja endale võtta naaberkinnisasjalt tema kinnisasjale ulatuvad puude ja põõsaste juured, oksad ja viljad, kui need kahjustavad kinnisasja kasutamist ja naaber ei ole neid hoiatusele vaatamata selleks vajaliku aja jooksul kõrvaldanud."
  § 150 "Piiril kasvavad puud ja põõsad on naabrite kaasomandis."
  § 151(2) "Käesoleva paragrahvi 1. lõikes nimetatud asja kasutamine ei tohi olla vastuolus asja otstarbega ega tekitada kahju naabrile."

maaamet = https://geoportaal.maaamet.ee/est/ruumiandmed/maakatastri-andmed/maaomaniku-meelespea-p549.html (fetched 27.09.2026)
  "Õigus paigaldada ja taastada piirimärke ning teostada katastrimõõdistamisi on ainult maakorraldustööde tegevuslitsentsi omaval maamõõtjal."
  "Piirimärgi võib paigaldada maa alla."
  "Maamõõtja on kohustatud piiride kättenäitamisele kutsuma kõikide kinnisasjade omanikud, kelle kinnisasjal on mõõdistatava piiriga ühine piiripunkt."
  "Maamõõtja koostab piiride kulgemise ja kättenäitamise kohta piiriprotokolli, ..."
  "Kui kinnisasja omanik, kes on kutsutud piiride kättenäitamisele, ei ilmu kohale , loetakse kutse saatmisega piirimärkide asukohad ja nende alalhoiu kohustus kinnisasja omanikule teatavaks tehtuks ja omanik piiride asukohaga nõustunuks."
  "Kui puudutatud katastriüksuste omanikel on erinev teadmine ühisest piirist või ei saavutata omavahel kokkulepet, on piiri kindlakstegemisel määravaks maamõõtja seisukoht."
  "piirimärkide taastamise kulud kannavad naaberkatastriüksuste omanikud võrdsetes osades, kui asjaosalised ei ole kokku leppinud teisiti;"
  "maaomanikul on õigus pöörduda nõudega piirimärkide taastamise kulude hüvitamiseks kahju tekitaja poole."
  "Piirimärgi taastamise ja kulude hüvitamise osas kokkuleppe saavutamiseks pöördu esmalt naaberkinnisasja omaniku poole. Kui kokkulepet ei saavutata, alles siis kaalu nõuete esitamist ja kohtu poole pöördumist."
  "Esmalt tee kindlaks katastriüksuse piiri täpne asukoht maastikul: tutvu maakatastris registreeritud katastriüksuse plaani ja piiriprotokolliga, täiendavaid materjale võid küsida katastripidajalt."
  "Käsi-GPS ja mobiiltelefon võivad olla abiks piirimärgi otsimisel maastikul, kuid nad ei taga katastrimõõdistamisel nõutavat täpsust, ..."
  "Maa- ja Ruumiameti Geoportaali kaardirakendustest nähtuva alusel ei saa otsustada, kas ehitis paikneb üle katastriüksuse piiri või ei."
  "Katastriüksuse piiri asukoht katastrikaardil võib olla ebatäpne."
  "Ehitise planeerimisel tuleb arvestada ka asjaõigusseaduses toodud naabrusõiguse sätetega. Seega tutvusta eelnevalt oma plaane naabritele."
  "Piirirajatiseks oleva aia ehitamiseks, muutmiseks või kõrvaldamiseks on vaja konsulteerida kohaliku omavalitsusega."
  Solutions for a structure over the boundary, incl. "saavuta piirinaabriga kokkulepe piiriülest ehitamist lubava asjaõiguse kandmises kinnistusraamatusse;"
  and "ehitise omanik lammutab või teisaldab ehitise või selle üle piiri ulatuva osa;"

harku = https://www.harku.ee/ehitus-planeerimine-ja-taristu/ehitamine-ja-muud-seonduvad-tegevused/rajatised (fetched 27.09.2026)
  "Naabritega koostöö on kohustuslik, kui piirdeaed eraldab kahte kinnistut – see on ühiskasutuses rajatis."

Prices: FACTS_prices.md only (roll mesh 25–45 €/jm, 3D panels 35–60 €/jm, worked example 40 m of 3D panels
1 400–2 400 €; the "half each" figure 700–1 200 € is that range divided by two).
"""

NEW_SRC = {}

ARTICLE = {
    "et": {
        "title": "Aed naabri piiril: seadus, piirimärgid ja kulud | LuxAed",
        "desc": "Aed naabri piiril samm-sammult: kuidas leida piirimärgid, mida naabriga kirja panna, kuidas kulud jagada ning mida teha vana aia ja vaidluse korral.",
        "short": "Aed naabri piiril",
        "image": "luxaed-mesh-2",
        "kicker": "Juhend · naaber ja piir",
        "h1": "Aed<br><em>naabri piiril</em>",
        "lead": "Piiriaed puudutab alati kahte peret ja just seal tekivad kõige sagedamini vaidlused. Selgitame, mida ütleb seadus, kuidas piir enne tööd kindlaks teha ning mida naabriga kirjalikult kokku leppida.",
        "direct": ("Enne piiriaeda leidke piirimärgid, leppige naabriga kirjalikult kokku asukoht, aia tüüp ja kulud ning alles siis alustage töid.",
                   "Nii ei jää aed mõne sentimeetri võrra valesse kohta ega jää kulud ühe pere kanda. Allpool käime läbi kõik sammud alates piirimärkidest kuni võimaliku vaidluseni."),
        "blocks": [
            {"type": "sections", "tag": "1. Piir", "h": "Kõigepealt tehke kindlaks, kus piir täpselt on",
             "intro": "Aia joon tuleb võtta piirimärkide järgi, mitte vana aia, heki ega kaardirakenduse järgi.",
             "items": [
                 ("Leidke piirimärgid maastikul", [
                     "Asjaõigusseaduse § 128 järgi määratakse piir maakatastri andmete ja piirimärkidega. Maa- ja Ruumiamet soovitab otsida märgid maastikul üles katastriüksuse plaani ja piiriprotokolli abil. Märk võib olla ka maa all või rohu sees, nii et otsige hoolega krundi nurkadest ja kohtadest, kus piir suunda muudab.",
                     "Maa- ja Ruumiameti sõnul ei saa kaardirakenduse põhjal otsustada, kas ehitis jääb üle piiri, ja katastrikaardil võib piir olla ebatäpne. Telefoni GPS aitab märki otsida, kuid piisavalt täpne see ei ole."]),
                 ("Kui märke ei leia, kutsuge litsentsiga maamõõtja", [
                     "Piirimärke tohib paigaldada ja taastada ainult litsentsiga maamõõtja. Ta kutsub kohale kõik omanikud, kelle kinnistul on selle piiriga ühine piiripunkt, ja koostab piiriprotokolli. Kutset ei tasu eirata: kui kutsutud omanik kohale ei tule, loetakse ta piiri asukohaga nõustunuks.",
                     "Kui naabrid saavad piirist erinevalt aru, on piiri kindlakstegemisel määrav maamõõtja seisukoht. Piirimärkide taastamise ja piiri kindlakstegemise kulud jagavad naabrid võrdselt, kui ei ole kokku lepitud teisiti."]),
                 ("Märkige joon ja kaitske märke", [
                     "Tõmmake märkide vahele nöör ja pildistage märgid. Omanik peab piirimärgid säilitama ega tohi neid ümber paigutada. Kui märk tööde käigus hävib, võib naaber nõuda taastamise kulude hüvitamist sellelt, kelle tegevuse tõttu see juhtus. Paluge ehitajal postid märkida nii, et puur märke ei riivaks."]),
             ],
             "sources": ["aos", "maaamet"]},
            {"type": "sections", "tag": "2. Naaber", "h": "Rääkige naabriga enne, kui tellite pakkumise",
             "items": [
                 ("Miks naabriga peab rääkima", [
                     "Asjaõigusseaduse § 151 järgi on kahte krunti eraldav müür, hekk, kraav või muu selline asi naabrite ühiskasutuses, sõltumata sellest, kellele see kuulub. Seda ei tohi kasutada vastuolus otstarbega ega nii, et see kahjustab naabrit. Harku vald ütleb otse, et kui piirdeaed eraldab kahte kinnistut, on koostöö naabritega kohustuslik.",
                     "Maa- ja Ruumiamet soovitab oma plaane naabritele varakult tutvustada ning piirirajatiseks oleva aia ehitamise, muutmise või eemaldamise puhul omavalitsusega nõu pidada. Ehitusteatise menetluses võib vald ehitusseadustiku § 36 järgi kaasata ka naaberkinnistu omaniku."]),
                 ("Mida kokku leppida ja kirja panna", [
                     "Leppige kokku ja pange kirja aia asukoht (täpselt piirile või tervikuna ühe krundi maale), tüüp, kõrgus ja ilus külg, ehituse ja hoolduse kulude jagamine, jalgvärav piiril, tööde aeg, ligipääs naabri poolelt ning see, mis saab vanast aiast ja hekist. Lisage skeem või pakkumine, millel aia joon on näha, ja kirjutage mõlemad kokkuleppele alla; enamasti piisab allkirjastatud lehest või selgest e-kirjade vahetusest.",
                     "Kontrollige enne ka planeeringut, sest see võib määrata aia <a href=\"/aia-korgus-harjumaal/\">lubatud kõrguse ja läbipaistvuse</a>. Kahe naabri soovitud kinnine aed ei pruugi seal lubatud olla."]),
                 ("Millal on vaja kinnistusraamatut", [
                     "Seadusest tulenevad naabrusõiguse kitsendused kehtivad kinnistusraamatusse kandmata, kuid tehinguga seatud kitsendus kehtib kolmandate isikute, näiteks uue omaniku, suhtes alles siis, kui see on kinnistusraamatusse kantud. Kui aed jääb osaliselt naabri maale ja soovite kindlust ka pärast müüki, soovitab Maa- ja Ruumiamet leppida kokku piiriülest ehitamist lubava asjaõiguse kandmises kinnistusraamatusse."]),
             ],
             "sources": ["aos", "harku", "maaamet", "ehs"]},
            {"type": "table", "tag": "Asukoht", "h": "Täpselt piirile või ühe krundi maale?",
             "headers": ("", "Aed täpselt piiril", "Aed ühe krundi maal"),
             "rows": [
                 ("Kelle maal aed seisab", "Postid on piirijoonel, aed jääb mõlema krundi peale.", "Aed on tervikuna ühe omaniku maal, piirist veidi eemal."),
                 ("Ehituskulud", "Jagatakse kokkuleppe järgi, näiteks pooleks.", "Üldjuhul maksab aia omanik, tema otsustab ka tüübi."),
                 ("Hooldus", "Aeda kasutavad mõlemad, pange hoolduse jagamine kirja.", "Omanik vajab ligipääsu ka välisküljele, näiteks värvimiseks."),
                 ("Sobib, kui", "Naabrid saavad hästi läbi ja soovivad sama aeda.", "Kokkuleppele ei jõuta või soovite ise otsustada."),
             ],
             "note": "Praktiline võrdlus, mitte õiguslik hinnang."},
            {"type": "sections", "tag": "3. Kulud", "h": "Kuidas kulud õiglaselt jagada",
             "items": [
                 ("Mida jagab seadus ja mida kokkulepe", [
                     "Seaduse järgi kannavad naabrid võrdselt piirimärkide paigaldamise kulud ja, kui ei ole kokku lepitud teisiti, ka piiri kindlakstegemise kulud. Piirirajatise korrashoiukulud jagatakse võrdselt siis, kui mõlemad seda kasutavad. Uue aia ehitushinna jagamine tuleb aga ise kokku leppida. Just see tekitab hiljem kõige rohkem tüli, kui midagi kirja ei pandud."]),
                 ("Kolm levinud viisi", [
                     "Kõige lihtsam on jagada arve pooleks. Kui üks naaber soovib kallimat aeda, on õiglane, et ta maksab vahe ise, näiteks kui üks soovib kinnist aeda, kuigi teisele piisaks <a href=\"/aiad/vorkaed/\">rullvõrkaiast</a>. Võib ka jagada piiri kaheks lõiguks, mille kumbki ehitab ja hooldab ise, kuid ühise tüübi ja kõrgusega.",
                     "Hinnatasemest annab aimu meie <a href=\"/hinnad/\">hinnatabel</a>: rullvõrkaed maksab paigaldatuna 25–45 €/jm ja <a href=\"/aiad/paneelaed/\">3D paneelaed</a> 35–60 €/jm. Näiteks 40 m 3D paneelaeda maksab 1 400–2 400 €, pooleks jagades 700–1 200 € kummalegi. Täpse summa annab kirjalik pakkumine pärast tasuta mõõdistust."]),
                 ("Pakkumine, mida on lihtne jagada", [
                     "Küsige pakkumist, kus aed, väravad, vana aia eemaldamine ja äravedu on eraldi ridadel. Siis on selge, kes mille eest maksab. Leppige ka kokku, kelle nimele tehakse leping ja arve."]),
             ],
             "sources": ["aos"]},
            {"type": "sections", "tag": "4. Tööd", "h": "Ligipääs, hekk ja tööd naabri poolel",
             "items": [
                 ("Kui tööks on vaja naabri maad", [
                     "Piiriaeda on lihtsam ehitada, kui meeskond saab töötada mõlemal pool piiri. Asjaõigusseaduse § 147 järgi peab naaber lubama üle oma maa materjali vedada, seal käia või sõita, kui ehitada saab ainult nii, see on hädavajalik ja talle tagatakse kahju hüvitamine. Veel parem on lihtsalt kokku leppida, millal tullakse, kust käiakse ja kuidas muru pärast korda tehakse."]),
                 ("Hekk, puud ja põõsad piiril", [
                     "Piiril kasvavad puud ja põõsad on naabrite kaasomandis, nii et piirihekki või piiril kasvavat puud ei tasu aia jaoks ühepoolselt maha võtta: leppige see naabriga kokku. Üle piiri ulatuvaid oksi ja juuri võib ära lõigata siis, kui need kahjustavad krundi kasutamist ja naaber ei ole neid hoiatusele vaatamata selleks vajaliku aja jooksul eemaldanud."]),
                 ("Kaablid ja torud piiri ääres", [
                     "Piiri ääres võivad kulgeda ka naabri või võrguettevõtja kaablid ja torud. Selgitage nende asukoht välja enne puurimist; kellelt küsida ja kui lähedale tohib kaevata, selgitame juhendis <a href=\"/aed-tee-ja-trasside-lahedal/\">aed tee ja trasside lähedal</a>."]),
             ],
             "sources": ["aos"]},
            {"type": "sections", "tag": "5. Vana aed", "h": "Vana piiriaed: eemaldada, parandada või jätta?",
             "items": [
                 ("Küsige enne lammutamist", [
                     "Kui vana aed on vajalik ka naabri huvides, näiteks tema koera või laste pärast, ei tohi seda asjaõigusseaduse § 151 järgi tema nõusolekuta kõrvaldada ega muuta. Leppige kokku, millal vana aed maha võetakse ja kui kiiresti uus asemele tuleb, et naabri hoov ei jääks vahepeal lahtiseks."]),
                 ("Kui vana aed kaldub või laguneb", [
                     "Ehitist tuleb hoida nii, et selle kokkuvarisemine või osade eraldumine ei kahjustaks naaberkinnistut, ja ohustatud naaber võib nõuda ohu kõrvaldamist. Alati ei pea kogu aeda välja vahetama: <a href=\"/aia-remont/viltu-aed/\">viltu vajunud postid</a> saab sageli remontida ja katkised väljad asendada."]),
                 ("Lammutamine, äravedu ja paberid", [
                     "Kui aia ehitamisega kaasnevad kaevetööd sügavamal kui 30 cm, vajab ehitusseadustiku lisa 1 järgi uue aia rajamine ehitusteatist ja ehitusprojekti ning vana aia lammutamine ehitusteatist. Üksiku osa asendamine samaväärsega teatist ei vaja; täpsemalt selgitame seda <a href=\"/aia-ehitusteatis/\">ehitusteatise juhendis</a>. Pange kirja ka see, kes vana aia eemaldab ja kuhu materjal viiakse."]),
             ],
             "sources": ["aos", "lisa1"]},
            {"type": "sections", "tag": "6. Vaidlus", "h": "Kui naaber ei ole nõus või aed jäi valesse kohta",
             "items": [
                 ("Kui kokkulepet ei tule", [
                     "Ärge alustage tööd vaidluse ajal. Kui naaber ei soovi ühist aeda, saate aia ehitada tervikuna oma maale ning otsustada tüübi ja aja ise, arvestades planeeringu nõuetega. Kui vaidlus on piiri asukoha üle, tellige maamõõtjalt piiri kindlakstegemine: siis on määrav maamõõtja seisukoht, mitte naabrite mälestused."]),
                 ("Kui aed on juba üle piiri", [
                     "Kui aed ehitati heauskselt üle piiri, peab naaber seda asjaõigusseaduse § 148 järgi taluma, kuid võib nõuda aia alla jääva maatüki omandamist või perioodilist hüvitist. Üle piiri ulatuva osa eemaldamist võib naaber nõuda siis, kui ehitaja oli pahauskne või kui naaber vaidles vastu enne ehitamise algust või hiljem, kuid hiljemalt ajal, mil eemaldamine ei olnud veel seotud ülemääraste kuludega.",
                     "Maa- ja Ruumiamet loetleb lahendused: mõõdistusvea korral tellige piiri kindlakstegemine, muidu leppige naabriga kokku piiri muutmises, piiriülest ehitamist lubavas asjaõiguses või hüvitises või tõstke aed ümber. Hüvitise suuruse kokkulepe kehtib, kui see on kantud märkusena kinnistusraamatusse."]),
                 ("Kõigepealt naaber, siis amet või kohus", [
                     "Piirimärgi ja selle kulude küsimuses soovitab Maa- ja Ruumiamet pöörduda kõigepealt naabri poole ning nõuete esitamist ja kohut kaaluda alles siis, kui kokkulepet ei saavutata. Aia enda üle vaidluses küsige nõu valla ehitusspetsialistilt ja keerulisemal juhul juristilt."]),
             ],
             "sources": ["aos", "maaamet"]},
            {"type": "cards", "tag": "Meie soovitus", "h": "Mida me ise soovitame", "cols": 2,
             "items": [
                 ("Kirjalik kokkulepe on odav kindlustus", "Üks lehekülg asukoha, tüübi ja kulude kohta hoiab ära vaidluse ka aastate pärast."),
                 ("Leidke piirimärgid enne mõõdistust", "Siis saame aia joone ja postide kohad kohe õigesti planeerida ning pakkumine on täpsem."),
                 ("Ühise raha eest parem aed", "Kui kulud jagatakse, saab sama eelarvega valida jäigema aia või parema värava."),
                 ("Kahtluse korral oma maale", "Kui naaber kõhkleb või piir on ebakindel, pange aed veidi oma krundi poole. See on turvalisem kui vaidlus postide üle."),
             ]},
            {"type": "cards", "tag": "Levinud probleemid", "h": "Mis läheb sageli valesti", "cols": 3,
             "items": [
                 ("Joon võeti vana aia järgi", "Vana aed ei olnud piiril ja uus aed jäi osaliselt naabri maale."),
                 ("Kokkulepe oli suuline", "Aastate pärast mäletavad naabrid kulude jagamist erinevalt."),
                 ("Piirimärk jäi posti alla", "Märk hävis puurimisel ja maamõõtjale tuli maksta."),
                 ("Vana aed lammutati küsimata", "Naaber vajas seda koera jaoks ja tema hoov jäi päevadeks lahtiseks."),
                 ("Piirihekk võeti maha", "Hekk oli mõlema naabri oma ja tüli algas enne, kui aed valmis sai."),
                 ("Karkass jäi naabri poole", "Ilusa külje suunas ei lepitud kokku ja naaber vaatab aastaid poste."),
             ]},
        ],
        "faq": [
            ("Kas aed peab olema täpselt piiril?", "Ei pea. Aia võib ehitada täpselt piirile või tervikuna ühe krundi maale. Leppige valik naabriga kirjalikult kokku, sest sellest sõltub, kuidas ehitus ja hooldus jagatakse."),
            ("Kes maksab naabritevahelise aia eest?", "Kui aeda kasutavad mõlemad naabrid, kannavad nad seaduse järgi korrashoiukulud võrdselt. Uue aia ehituskulude jagamine leppige enne tööd kirjalikult kokku, näiteks pooleks või nii, et kallima aia soovija maksab vahe."),
            ("Kas võin vana piiriaia ise eemaldada?", "Kui aed on vajalik ka naabri huvides, ei tohi seda asjaõigusseaduse § 151 järgi tema nõusolekuta kõrvaldada ega muuta. Leppige enne lammutamist kokku, millal see toimub ja kes materjali ära veab."),
            ("Mida teha, kui piirimärke ei leia?", "Tellige piiri taastamine litsentsiga maamõõtjalt, sest telefoni GPS ega kaardirakendus ei anna piisavat täpsust. Maamõõtja kutsub naabrid kohale ja taastamise kulud jagatakse võrdselt, kui ei ole kokku lepitud teisiti."),
            ("Mis saab, kui aed jäi naabri maale?", "Kui aed ehitati heauskselt, peab naaber seda taluma, kuid võib nõuda maa omandamist või perioodilist hüvitist. Eemaldamist võib ta nõuda, kui ehitaja oli pahauskne või kui naaber vaidles vastu enne ehitamist või hiljem, ajal, mil eemaldamine ei olnud veel ülemäära kulukas (asjaõigusseadus § 148)."),
            ("Kas naaber peab lubama tööd tema maalt teha?", "Ainult siis, kui ehitada saab üksnes naabri maad kasutades, see on hädavajalik ja naabrile tagatakse kahju hüvitamine (asjaõigusseadus § 147). Kui aeda saab ehitada ka oma poolelt, leppige ligipääs naabriga lihtsalt kokku."),
        ],
        "links_keys": ["permit_guide", "municipal_rules", "mistakes"],
        "links_extra": [("/aiad/vorkaed/", "Rullvõrkaed", "Soodne ja õhuline aed pikale piirile.")],
        "cta": ("Planeerime piiriaia koos teie ja naabriga", "Tasuta mõõdistusel vaatame piiri, pinnast ja ligipääsu ning koostame kirjaliku pakkumise, mida saate naabriga arutada.", "/#form", "Küsi pakkumist"),
    },
    "ru": {
        "title": "Забор между соседями: закон, межевые знаки, расходы | LuxAed",
        "desc": "Забор между соседями по шагам: как найти межевые знаки, о чём договориться письменно, как делить расходы, что делать со старым забором и при споре.",
        "short": "Забор между соседями",
        "image": "luxaed-mesh-2",
        "kicker": "Руководство · сосед и граница",
        "h1": "Забор<br><em>между соседями</em>",
        "lead": "Забор на границе всегда касается двух семей, и именно из-за него чаще всего возникают споры. Объясняем, что говорит закон, как до работ точно определить границу и о чём договориться с соседом письменно.",
        "direct": ("Сначала найдите межевые знаки, затем письменно договоритесь с соседом о месте, типе забора и расходах и только потом начинайте работы.",
                   "Так забор не сместится на несколько сантиметров на чужую землю, а расходы не лягут на одну семью. Ниже разбираем все шаги: от межевых знаков до возможного спора."),
        "blocks": [
            {"type": "sections", "tag": "1. Граница", "h": "Сначала точно определите, где проходит граница",
             "intro": "Линию забора берут по межевым знакам, а не по старому забору, живой изгороди или карте в приложении.",
             "items": [
                 ("Найдите межевые знаки на местности", [
                     "По § 128 Asjaõigusseadus граница определяется данными земельного кадастра и межевыми знаками. Maa- ja Ruumiamet советует искать знаки на местности по плану кадастровой единицы и пограничному протоколу. Знак может быть под землёй или в траве, поэтому внимательно проверьте углы участка и места, где граница меняет направление.",
                     "По словам Maa- ja Ruumiamet, по картографическому приложению нельзя решить, заходит ли постройка за границу участка, а граница на кадастровой карте может быть неточной. GPS в телефоне помогает в поиске, но недостаточно точен."]),
                 ("Если знаков нет, вызовите землемера с лицензией", [
                     "Устанавливать и восстанавливать межевые знаки может только землемер с лицензией. Он приглашает всех владельцев, у чьих участков есть общая точка с этой границей, и составляет пограничный протокол. Приглашение лучше не игнорировать: если приглашённый владелец не пришёл, считается, что он согласен с местом границы.",
                     "Если соседи понимают границу по-разному, при её определении решающим является мнение землемера. Расходы на восстановление знаков и определение границы соседи делят поровну, если не договорились иначе."]),
                 ("Отметьте линию и берегите знаки", [
                     "Натяните между знаками шнур и сфотографируйте их. Владелец обязан сохранять межевые знаки и не вправе их переносить, а если знак уничтожат во время работ, сосед может потребовать возмещения расходов на восстановление от того, по чьей вине это случилось. Попросите монтажников разметить столбы так, чтобы бур не задел знаки."]),
             ],
             "sources": ["aos", "maaamet"]},
            {"type": "sections", "tag": "2. Сосед", "h": "Поговорите с соседом до того, как заказывать предложение",
             "items": [
                 ("Почему без соседа не обойтись", [
                     "По § 151 Asjaõigusseadus стена, живая изгородь, канава или другая подобная вещь, разделяющая два участка, находится в совместном пользовании соседей независимо от того, кому она принадлежит. Пользоваться ею нельзя вопреки её назначению или во вред соседу. Волость Харку прямо пишет, что если забор разделяет два участка, сотрудничество с соседями обязательно.",
                     "Maa- ja Ruumiamet советует заранее рассказать соседям о своих планах, а перед строительством, изменением или сносом забора на границе проконсультироваться с самоуправлением. При рассмотрении уведомления о строительстве волость по § 36 строительного кодекса может привлечь и владельца соседнего участка."]),
                 ("О чём договориться и что записать", [
                     "Договоритесь и запишите место забора (ровно по границе или целиком на одном участке), тип, высоту и лицевую сторону, раздел расходов на строительство и уход, калитку на границе, сроки работ, доступ со стороны соседа и судьбу старого забора и живой изгороди. Приложите схему или предложение с линией забора и подпишите договорённость вдвоём; обычно достаточно подписанного листа или ясной переписки по e-mail.",
                     "Заранее проверьте и планировку: она может определять <a href=\"/ru/vysota-zabora-v-harjumaa/\">допустимую высоту и прозрачность забора</a>. Глухой забор, о котором договорились соседи, там может быть не разрешён."]),
                 ("Когда нужна поземельная книга", [
                     "Ограничения соседского права, установленные законом, действуют без записи в поземельную книгу, а ограничение, установленное сделкой, действует для третьих лиц, например нового владельца, только после внесения в поземельную книгу. Если забор частично стоит на земле соседа и вы хотите уверенности и после продажи, Maa- ja Ruumiamet советует договориться о внесении в поземельную книгу вещного права, разрешающего строить через границу."]),
             ],
             "sources": ["aos", "harku", "maaamet", "ehs"]},
            {"type": "table", "tag": "Место", "h": "Ровно по границе или на одном участке?",
             "headers": ("", "Забор по границе", "Забор на одном участке"),
             "rows": [
                 ("Чья земля", "Столбы на линии границы, забор на обоих участках.", "Забор целиком на земле одного владельца, чуть отступив от границы."),
                 ("Строительство", "Делится по договорённости, например пополам.", "Обычно платит владелец забора, он же выбирает тип."),
                 ("Уход", "Забором пользуются оба, раздел ухода запишите.", "Владельцу нужен доступ и к внешней стороне, например для покраски."),
                 ("Подходит, если", "Соседи ладят и хотят одинаковый забор.", "Договориться не удаётся или вы хотите решать сами."),
             ],
             "note": "Это практическое сравнение, а не юридическая оценка."},
            {"type": "sections", "tag": "3. Расходы", "h": "Как честно поделить расходы",
             "items": [
                 ("Что делит закон, а что договорённость", [
                     "По закону соседи поровну несут расходы на установку межевых знаков и, если не договорились иначе, на определение границы. Расходы на содержание пограничного сооружения делятся поровну, если им пользуются оба. Раздел стоимости строительства нового забора нужно согласовать самим, и именно он потом вызывает больше всего ссор, если ничего не записали."]),
                 ("Три обычных варианта", [
                     "Проще всего разделить счёт пополам. Если один сосед хочет забор дороже, справедливо, чтобы разницу оплатил он, например если один хочет глухой забор, а второму хватило бы <a href=\"/ru/zabory/setka-rabitsa/\">сетки-рабицы</a>. Можно и поделить границу на два отрезка, каждый строит и обслуживает свой, но с одинаковым типом и высотой забора.",
                     "Уровень цен показывает наш <a href=\"/ru/ceny/\">прайс</a>: сетка-рабица с монтажом стоит 25–45 €/м, а <a href=\"/ru/zabory/2d-3d-setka/\">забор из 3D-панелей</a> стоит 35–60 €/м. Например, 40 м забора из 3D-панелей стоят 1 400–2 400 €, то есть 700–1 200 € на каждого при разделе пополам. Точную сумму даёт письменное предложение после бесплатного замера."]),
                 ("Предложение, которое легко поделить", [
                     "Попросите предложение, где забор, ворота, демонтаж старого забора и вывоз указаны отдельными строками, тогда ясно, кто за что платит. Договоритесь и о том, на чьё имя оформляются договор и счёт."]),
             ],
             "sources": ["aos"]},
            {"type": "sections", "tag": "4. Работы", "h": "Доступ, живая изгородь и работы со стороны соседа",
             "items": [
                 ("Если для работ нужна земля соседа", [
                     "Забор на границе проще ставить, когда бригада может работать с обеих сторон. По § 147 Asjaõigusseadus сосед обязан позволить провезти через свой участок материал, пройти или проехать по нему, если строить можно только так, это крайне необходимо и ему гарантировано возмещение ущерба. Ещё лучше просто договориться, когда придут, где будут ходить и как потом приведут в порядок газон."]),
                 ("Живая изгородь, деревья и кусты на границе", [
                     "Деревья и кусты, растущие на границе, находятся в совместной собственности соседей, поэтому живую изгородь или дерево на границе не стоит убирать ради забора в одностороннем порядке: договоритесь с соседом. Ветки и корни, заходящие на ваш участок, можно срезать, если они мешают пользоваться участком, а сосед после предупреждения не убрал их за необходимое для этого время."]),
                 ("Кабели и трубы вдоль границы", [
                     "Вдоль границы могут проходить кабели и трубы соседа или сетевой компании. Выясните, где они, до бурения; у кого спрашивать и насколько близко можно копать, объясняем в статье <a href=\"/ru/zabor-u-dorogi-i-kommunikacij/\">забор у дороги и коммуникаций</a>."]),
             ],
             "sources": ["aos"]},
            {"type": "sections", "tag": "5. Старый забор", "h": "Старый забор на границе: снести, отремонтировать или оставить?",
             "items": [
                 ("Спросите перед демонтажем", [
                     "Если старый забор нужен и в интересах соседа, например из-за его собаки или детей, по § 151 Asjaõigusseadus его нельзя убрать или изменить без согласия соседа. Договоритесь, когда снимут старый забор и как быстро поставят новый, чтобы двор соседа не остался открытым."]),
                 ("Если старый забор кренится или разваливается", [
                     "Постройку нужно содержать так, чтобы её обрушение или отрыв частей не повредили соседний участок, а сосед, которому это угрожает, может потребовать устранить опасность. Менять весь забор нужно не всегда: <a href=\"/ru/remont-zaborov/pokosilsya-zabor/\">покосившиеся столбы</a> часто можно отремонтировать, а сломанные пролёты заменить."]),
                 ("Демонтаж, вывоз и документы", [
                     "Если при строительстве забора ведутся земляные работы глубже 30 см, то по приложению 1 к строительному кодексу для нового забора нужны уведомление о строительстве и проект, а для сноса старого нужно уведомление о строительстве. Замена отдельной части на равноценную уведомления не требует; подробнее в статье <a href=\"/ru/razreshenie-na-zabor/\">нужно ли разрешение на забор</a>. Запишите и то, кто демонтирует старый забор и куда вывозят материал."]),
             ],
             "sources": ["aos", "lisa1"]},
            {"type": "sections", "tag": "6. Спор", "h": "Если сосед против или забор оказался не на месте",
             "items": [
                 ("Если договориться не удаётся", [
                     "Не начинайте работы во время спора. Если сосед не хочет общий забор, вы можете поставить забор целиком на своей земле и сами решить тип и сроки, соблюдая требования планировки. Если спор идёт о месте границы, закажите у землемера определение границы: тогда решающим будет мнение землемера, а не то, как это помнят соседи."]),
                 ("Если забор уже заходит на участок соседа", [
                     "Если забор добросовестно поставили с заходом на участок соседа, сосед по § 148 Asjaõigusseadus должен это терпеть, но может потребовать выкупить землю под забором или платить периодическую компенсацию. Убрать часть, заходящую на его участок, сосед может потребовать, если строитель действовал недобросовестно или если сосед возражал до начала строительства или позже, но не позднее момента, когда снос этой части ещё не требовал чрезмерных расходов.",
                     "Maa- ja Ruumiamet перечисляет решения: при ошибке измерения закажите определение границы, в остальных случаях договоритесь с соседом об изменении границы, о вещном праве на строительство через границу или о компенсации либо перенесите забор. Договорённость о размере компенсации действует, если она внесена отметкой в поземельную книгу."]),
                 ("Сначала сосед, потом ведомство или суд", [
                     "По вопросу межевого знака и расходов Maa- ja Ruumiamet советует сначала обратиться к соседу, а о требованиях и суде думать, только если договориться не удалось. В споре о самом заборе посоветуйтесь со строительным специалистом волости, а в сложном случае с юристом."]),
             ],
             "sources": ["aos", "maaamet"]},
            {"type": "cards", "tag": "Наш совет", "h": "Что советуем мы", "cols": 2,
             "items": [
                 ("Письменная договорённость как дешёвая страховка", "Одна страница о месте, типе и расходах избавит от спора и через годы."),
                 ("Найдите межевые знаки до замера", "Тогда мы сразу правильно спланируем линию забора и места столбов, а предложение будет точнее."),
                 ("Общие деньги, забор лучше", "Если расходы делятся, за тот же бюджет можно выбрать более жёсткий забор или лучшие ворота."),
                 ("При сомнениях ставьте на своей земле", "Если сосед колеблется или граница неясна, поставьте забор чуть внутри своего участка. Это надёжнее, чем спор из-за столбов."),
             ]},
            {"type": "cards", "tag": "Частые проблемы", "h": "Что часто идёт не так", "cols": 3,
             "items": [
                 ("Линию взяли по старому забору", "Старый забор стоял не по границе, и новый частично оказался на земле соседа."),
                 ("Договорились на словах", "Через годы соседи по-разному помнят, как делили расходы."),
                 ("Межевой знак под столбом", "Знак уничтожили при бурении, и пришлось платить землемеру."),
                 ("Старый забор снесли без спроса", "Он был нужен соседу для собаки, и его двор несколько дней стоял открытым."),
                 ("Срубили живую изгородь", "Изгородь принадлежала обоим соседям, и ссора началась раньше, чем забор был готов."),
                 ("Каркас достался соседу", "О лицевой стороне не договорились, и сосед годами смотрит на столбы и лаги."),
             ]},
        ],
        "faq": [
            ("Должен ли забор стоять ровно по границе?", "Не обязательно. Забор можно поставить ровно по границе или целиком на земле одного участка. Письменно договоритесь с соседом о варианте, потому что от него зависит, как делить строительство и уход."),
            ("Кто платит за забор между соседями?", "Если забором пользуются оба соседа, по закону расходы на его содержание они несут поровну. Раздел расходов на строительство нового забора запишите до работ, например пополам или так, что разницу оплачивает тот, кто хочет забор дороже."),
            ("Можно ли самому убрать старый забор на границе?", "Если забор нужен и в интересах соседа, по § 151 Asjaõigusseadus его нельзя убрать или изменить без его согласия. До демонтажа договоритесь, когда он пройдёт и кто вывезет материал."),
            ("Что делать, если не найти межевые знаки?", "Закажите восстановление границы у землемера с лицензией, потому что GPS в телефоне и картографическое приложение не дают нужной точности. Землемер приглашает соседей, а расходы на восстановление делятся поровну, если не договорились иначе."),
            ("Что будет, если забор оказался на участке соседа?", "Если забор поставили добросовестно, сосед должен это терпеть, но может потребовать выкупить землю или платить компенсацию. Убрать его он может потребовать, если строитель действовал недобросовестно или если сосед возражал до строительства или позже, пока снос ещё не требовал чрезмерных расходов (§ 148 Asjaõigusseadus)."),
            ("Обязан ли сосед пустить рабочих на свой участок?", "Только если строить можно лишь с использованием его земли, это крайне необходимо и ему гарантировано возмещение ущерба (§ 147 Asjaõigusseadus). Если забор можно поставить со своей стороны, просто договоритесь с соседом о доступе."),
        ],
        "links_keys": ["permit_guide", "municipal_rules", "mistakes"],
        "links_extra": [("/ru/zabory/setka-rabitsa/", "Сетка-рабица", "Недорогой и лёгкий забор для длинной границы.")],
        "cta": ("Спланируем забор вместе с вами и соседом", "На бесплатном замере посмотрим границу, грунт и доступ и подготовим письменное предложение, которое можно обсудить с соседом.", "/ru/#form", "Оставить заявку"),
    },
    "en": {
        "title": "Boundary Fence with Neighbours: Law, Markers, Costs | LuxAed",
        "desc": "A boundary fence with your neighbour, step by step: finding the markers, what to agree in writing, sharing the costs, the old fence and handling a dispute.",
        "short": "Boundary fence with a neighbour",
        "image": "luxaed-mesh-2",
        "kicker": "Guide · neighbours and boundaries",
        "h1": "A boundary fence<br><em>with your neighbour</em>",
        "lead": "A boundary fence always involves two households, and it is where garden disputes most often start. We explain what the law says, how to pin down the boundary before work starts and what to agree with your neighbour in writing.",
        "direct": ("Before building a boundary fence, find the markers, agree its position, type and costs with your neighbour in writing, then start work.",
                   "That way the fence does not end up a few centimetres in the wrong place and the costs do not fall on one household. Below we go through every step, from the markers to a possible dispute."),
        "blocks": [
            {"type": "sections", "tag": "1. The boundary", "h": "First, establish exactly where the boundary runs",
             "intro": "Take the fence line from the boundary markers, not from the old fence, a hedge or a map app.",
             "items": [
                 ("Find the markers on the ground", [
                     "Under § 128 of the Law of Property Act, the boundary is determined by the land cadastre data and the boundary markers. The Land and Spatial Development Board advises finding the markers on site with the help of the cadastral unit plan and the boundary protocol. A marker may be underground or hidden in grass, so search the plot corners and the points where the boundary turns.",
                     "According to the Board, a map app cannot show whether a structure crosses the boundary, and the cadastral map may be inaccurate. Phone GPS helps you search but is not accurate enough."]),
                 ("If you cannot find them, call a licensed land surveyor", [
                     "Only a licensed land surveyor may install and restore boundary markers. The surveyor invites every owner whose plot shares a point with that boundary and draws up a boundary protocol. Do not ignore the invitation: an owner who is invited but does not attend is deemed to agree with the boundary's location.",
                     "If the neighbours understand the boundary differently, the surveyor's view is decisive when it is determined. The costs of restoring markers and determining the boundary are shared equally unless agreed otherwise."]),
                 ("Mark the line and protect the markers", [
                     "Run a string line between the markers and photograph them. Owners must keep markers intact and may not move them, and if one is destroyed during the work, the neighbour can claim the restoration costs from whoever caused it. Ask your installer to set out the posts so the auger keeps clear of the markers."]),
             ],
             "sources": ["aos", "maaamet"]},
            {"type": "sections", "tag": "2. Your neighbour", "h": "Talk to your neighbour before you ask for quotes",
             "items": [
                 ("Why your neighbour has a say", [
                     "Under § 151 of the Law of Property Act, a wall, hedge, ditch or similar thing separating two plots is in the neighbours' joint use, whoever owns it, and may not be used against its purpose or to the neighbour's harm. Harku Municipality states plainly that where a fence separates two properties, cooperating with the neighbours is mandatory.",
                     "The Land and Spatial Development Board advises telling your neighbours about your plans early and consulting the municipality before building, altering or removing a fence on the boundary. When processing a building notice, the municipality may also involve the neighbouring owner under § 36 of the Building Code."]),
                 ("What to agree and put in writing", [
                     "Agree and write down the fence's position (exactly on the boundary or entirely on one plot), its type, height and good face, how building and upkeep costs are shared, any pedestrian gate on the line, the timing, access from the neighbour's side and what happens to the old fence and any hedge. Attach a sketch or the quote showing the fence line and both sign it; a signed page or a clear email exchange is usually enough.",
                     "Check the plan first, as it may set the <a href=\"/en/fence-height-rules-harju-county/\">permitted height and transparency</a> of the fence. A solid fence that you both want may not be allowed there."]),
                 ("When the land register matters", [
                     "Restrictions set by neighbour law apply without any land register entry, but a restriction created by agreement binds third parties, such as a future owner, only once it is registered. If the fence stands partly on your neighbour's land and you want certainty even after a sale, the Board suggests registering a real right that permits building across the boundary."]),
             ],
             "sources": ["aos", "harku", "maaamet", "ehs"]},
            {"type": "table", "tag": "Position", "h": "Exactly on the boundary or on one plot?",
             "headers": ("", "Fence on the boundary", "Fence on one plot"),
             "rows": [
                 ("Whose land", "The posts stand on the line, so the fence is on both plots.", "Entirely on one owner's land, set slightly back from the line."),
                 ("Building costs", "Shared by agreement, for example half each.", "Usually paid by the fence owner, who also picks the type."),
                 ("Upkeep", "Both use the fence, so write down how upkeep is shared.", "The owner needs access to the outer face too, for example for painting."),
                 ("Best when", "The neighbours get on and want the same fence.", "You cannot agree or want to decide on your own."),
             ],
             "note": "A practical comparison, not a legal assessment."},
            {"type": "sections", "tag": "3. Costs", "h": "How to share the costs fairly",
             "items": [
                 ("What the law splits and what you agree", [
                     "By law, neighbours share equally the cost of installing boundary markers and, unless agreed otherwise, of determining the boundary. The upkeep costs of a boundary structure are shared equally if both use it. How to split the price of a new fence is up to you, and it causes the most arguments later if nothing was written down."]),
                 ("Three common ways to split", [
                     "The simplest is half each. If one neighbour wants a pricier fence, it is fair that they pay the difference, for example for a solid fence where <a href=\"/en/fences/roll-mesh/\">roll mesh</a> would do for the other. Or split the boundary into two sections that each of you builds and maintains, with one agreed type and height.",
                     "Our <a href=\"/en/prices/\">price guide</a> shows the level: installed roll mesh costs €25–45/m and <a href=\"/en/fences/mesh/\">3D mesh panels</a> €35–60/m. For example, 40 m of 3D panel fence costs €1,400–2,400, or €700–1,200 each if split in half. The written quote after the free site visit gives the exact amount."]),
                 ("A quote that is easy to split", [
                     "Ask for a quote with the fence, gates, removal of the old fence and disposal on separate lines, so it is clear who pays for what. Also agree whose name goes on the contract and invoice."]),
             ],
             "sources": ["aos"]},
            {"type": "sections", "tag": "4. The work", "h": "Access, hedges and working from the neighbour's side",
             "items": [
                 ("If the work needs your neighbour's land", [
                     "A boundary fence is easier to build when the crew can work from both sides. Under § 147 of the Law of Property Act, the neighbour must allow materials to be carried across their land, or people to walk or drive over it, if building is only possible that way, it is strictly necessary and any damage is compensated. Better still, simply agree when the crew comes, where they walk and how the lawn is put right afterwards."]),
                 ("Hedges, trees and shrubs on the line", [
                     "Trees and shrubs growing on the boundary are co-owned by the neighbours, so do not remove a boundary hedge or tree for the fence on your own: agree it with your neighbour. You may cut back branches and roots reaching onto your plot if they interfere with its use and the neighbour has not removed them within the time needed after a warning."]),
                 ("Cables and pipes along the boundary", [
                     "Your neighbour's or a utility company's cables and pipes may also run along the boundary. Find them before drilling; our guide to <a href=\"/en/fence-near-road-and-utilities/\">fences near roads and utilities</a> explains who to ask and how close you may dig."]),
             ],
             "sources": ["aos"]},
            {"type": "sections", "tag": "5. The old fence", "h": "The old boundary fence: remove, repair or keep?",
             "items": [
                 ("Ask before you take it down", [
                     "If the old fence is also needed in your neighbour's interest, for example for their dog or children, § 151 of the Law of Property Act says it may not be removed or altered without their consent. Agree when it comes down and how soon the new one goes up, so your neighbour's garden is not left open."]),
                 ("If the old fence leans or is falling apart", [
                     "Structures must be kept so that their collapse or falling parts cannot damage the neighbouring property, and a neighbour at risk may demand that the danger be removed. You do not always need a whole new fence: <a href=\"/en/fence-repair/leaning-fence/\">leaning posts</a> can often be repaired and broken panels replaced."]),
                 ("Removal, disposal and paperwork", [
                     "Where building the fence involves digging deeper than 30 cm, Annex 1 of the Building Code requires a building notice and a design for a new fence, and a building notice for demolishing the old one. Replacing a single part with an equivalent one needs no notice; our <a href=\"/en/fence-permit/\">fence permit guide</a> has the details. Also write down who removes the old fence and where the material goes."]),
             ],
             "sources": ["aos", "lisa1"]},
            {"type": "sections", "tag": "6. Disputes", "h": "If your neighbour disagrees or the fence is in the wrong place",
             "items": [
                 ("If you cannot agree", [
                     "Do not start work during a dispute. If your neighbour does not want a shared fence, you can build it entirely on your own land and decide the type and timing yourself, within the plan's requirements. If the dispute is about where the boundary runs, have a land surveyor determine it: the surveyor's view is then decisive, not what the neighbours remember."]),
                 ("If the fence already crosses the boundary", [
                     "If a fence was built over the boundary in good faith, the neighbour must tolerate it under § 148 of the Law of Property Act but may demand that the land under it be acquired or that periodic compensation be paid. The neighbour may demand removal of the part on their land if the builder acted in bad faith, or if the neighbour objected before building started or later, at the latest while removing that part was still possible without excessive cost.",
                     "The Board lists the ways out: order a boundary determination if a survey error is to blame; otherwise agree with your neighbour to change the boundary, register a right to build across it or pay compensation, or move the fence. An agreement on the amount of compensation is valid once it is noted in the land register."]),
                 ("Your neighbour first, then an authority or court", [
                     "For a boundary marker and its costs, the Board advises going to your neighbour first and thinking about claims or court only if you cannot agree. For a dispute about the fence itself, ask the municipality's building officer and, in harder cases, a lawyer."]),
             ],
             "sources": ["aos", "maaamet"]},
            {"type": "cards", "tag": "Our advice", "h": "What we recommend", "cols": 2,
             "items": [
                 ("A written note is cheap insurance", "One page on position, type and costs prevents an argument even years later."),
                 ("Find the markers before the site visit", "Then we can plan the fence line and post positions correctly straight away, and the quote is more accurate."),
                 ("Shared money, better fence", "When costs are shared, the same budget can buy a stiffer fence or a better gate."),
                 ("When in doubt, build on your side", "If your neighbour hesitates or the boundary is unclear, set the fence slightly inside your plot. That is safer than a dispute over posts."),
             ]},
            {"type": "cards", "tag": "Common problems", "h": "What often goes wrong", "cols": 3,
             "items": [
                 ("The line followed the old fence", "The old fence was off the boundary, so the new one ended up partly on the neighbour's land."),
                 ("The deal was verbal", "Years later the neighbours remember the cost split differently."),
                 ("A marker ended up under a post", "It was destroyed during drilling, and a surveyor had to be paid."),
                 ("The old fence came down unasked", "The neighbour needed it for a dog and was left with an open garden for days."),
                 ("The hedge was cut down", "It belonged to both neighbours, and the row started before the fence was finished."),
                 ("The frame faces the neighbour", "Nobody agreed on the good face, so the neighbour looks at posts and rails for years."),
             ]},
        ],
        "faq": [
            ("Does the fence have to be exactly on the boundary?", "No. It can go exactly on the boundary or entirely on one plot. Agree the choice with your neighbour in writing, because it decides how building and upkeep are shared."),
            ("Who pays for a fence between neighbours?", "If both neighbours use the fence, the law says they share its upkeep costs equally. Agree in writing before work starts how the building cost is split, for example half each or with the neighbour who wants the pricier fence paying the difference."),
            ("Can I remove the old boundary fence myself?", "If the fence is also needed in your neighbour's interest, it may not be removed or altered without their consent under § 151 of the Law of Property Act. Before taking it down, agree when it happens and who takes the material away."),
            ("What if I cannot find the boundary markers?", "Have a licensed land surveyor restore them, because phone GPS and map apps are not accurate enough. The surveyor invites the neighbours, and the restoration costs are shared equally unless agreed otherwise."),
            ("What if the fence ends up on my neighbour's land?", "If it was built in good faith, the neighbour must tolerate it but may demand that the land be acquired or compensation paid. They may demand removal if the builder acted in bad faith, or if they objected before building or later while removal was still possible without excessive cost (Law of Property Act § 148)."),
            ("Must my neighbour let the crew work from their side?", "Only if building is possible solely by using their land, it is strictly necessary and any damage is compensated (Law of Property Act § 147). If the fence can be built from your side, simply agree access with your neighbour."),
        ],
        "links_keys": ["permit_guide", "municipal_rules", "mistakes"],
        "links_extra": [("/en/fences/roll-mesh/", "Roll mesh fence", "Affordable and light for long boundaries.")],
        "cta": ("Let's plan the fence with you and your neighbour", "At the free site visit we check the boundary, ground and access and prepare a written quote you can discuss with your neighbour.", "/en/#form", "Get a quote"),
    },
}
