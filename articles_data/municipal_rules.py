# municipal_rules: /aia-korgus-harjumaal/, /ru/vysota-zabora-v-harjumaa/, /en/fence-height-rules-harju-county/
#
# Verification notes (primary texts checked on 27.09.2026; quotes are exact):
#
# NEW SOURCE harku_tp, Harku valla ehitustingimusi ... tapsustav teemaplaneering (2018), ch. 3.14, p. 78,
# https://www.harku.ee/sites/default/files/documents/2025-08/Teemaplaneeringu%20seletuskiri.pdf (HTTP 200,
# 10 034 546 bytes, same file as the saved copy factcheck/harku_tp.pdf):
#   "Keelatud on läbipaistmatute plankpiirete rajamine v.a piirded, mis on vajalikud müratõkke eesmärgil
#    või vajalikud tööstusterritooriumi piiramiseks."
#   "Käesoleva teemaplaneeringuga on keelatud üle 1,5 m kõrguste aedade rajamine välja arvatud juhul, kui
#    piirdeaedade püsitamine on lubatud kehteststatud detailplaneeringu või ehitulsoaprojektiga."
#   "Kõik piirdeaiad peavad asuma teekatte servast minimaalselt 2 m kaugusel, et tagada lume koristamise
#    võimalused."
#
# New details taken from sources already registered (no new key needed):
#   viimsi (teemaplaneering 4.5): "Elamute (v.a korterelamud) piirdeaiad võib rajada: ... teedekatte servast
#     minimaalselt 2 m kaugusele."
#   saue (üldplaneering 4.4.1, keskuse maa): "Piirdeaedade rajamine üldjuhul ei ole lubatud."
#   saku (üldplaneering 4.1 and 4.2): "piirete lubatud kõrgus on kuni 1,5 m maapinnast, läbipaistvusega
#     vähemalt 25% (ei kehti haljaspiiretele)"; korterelamu maa-ala: "üldjuhul piirdeaedu mitte ette näha".
#   nomme (üldplaneering, footnote 8): "Piirdeaed ei tohi mõjuda suletud planguna, seetõttu on soovitatav
#     arvestada lippide vaheks 1/3 kuni 1/2 lipi laiusest."
#   nomme: "Suure liikluskoormusega tänavate ääres on erilahendusena lubatud tihedamad, vaheliti paigutatud
#     lippidega kahekihilised piirdeaiad, mille lippide vahe on traditsiooniline."
#   nomme: "Heki suurim lubatud kõrgus on üldjuhul 1,5 m."
#   keila (maakasutus): "Haljaspiire võib eelpool toodud näitajatest olla kõrgem."
#   kiili (üldplaneering): "Teedepoolsed piirdeaiad on osaliselt läbipaistvad puitaiad ja ei tohi olla
#     kõrgemad, kui 1,4 meetrit."
#   tallinn (Piirdeaiad, hoovialad ja haljastus, 11.04.2024): "Vaata kaardilt, millisel miljööalal Sinu hoone
#     asub"; "soovitame lähtuda algse projekti piirdeaia lahendusest, mis on üldjuhul leitav Tallinna
#     Linnaplaneerimise Ameti arhiivist"; "Piirdeaed ja väravad peavad olema ajaloolisesse asumisse sobiva
#     paigutuse, kõrguse, materjali ja kujundusega."; "Võrkpiirde kasutamine ja selle võimalik ulatus
#     otsustatakse igal üksikjuhul eraldi." (the page navigation also links "Tallinna planeeringute register").
#   tehn (§ 30 lg 1): "Ehitise kõrgus on ehitise suurim vertikaalmõõde ehitist vahetult ümbritsevast
#     maapinnast või katendist ehitise kõrgeima tarindi kõrgeima punktini, võtmata arvesse kohalikke
#     väiksemaid süvendeid ja kõrgendusi."
#   rae (scope): "lõunapiiriks on Kurna oja ja Kurna ojast alates kuni Tallinna ringteeni sellega külgneva
#     ala piir"; "Materjalikäsitluselt arvestada hoone ning naaberpiirete lahendusega."
#   muks § 52 lg 1 (permit on a monument and in a heritage conservation area) and §§ 58-59 (protection zone,
#     notice at least ten days ahead), as in FACTS.md.
#
# Editorial note for the source registry: SRC["tallinn"]["en"] is labelled "Tallinn, fences in heritage areas";
# the table cell below uses "Tallinn, fences in milieu-value areas" to match the milieu-value terminology.

NEW_SRC = {
    "harku_tp": {
        "et": ("Harku valla teemaplaneering", "https://www.harku.ee/sites/default/files/documents/2025-08/Teemaplaneeringu%20seletuskiri.pdf"),
        "ru": ("Харку, тематическая планировка", "https://www.harku.ee/sites/default/files/documents/2025-08/Teemaplaneeringu%20seletuskiri.pdf"),
        "en": ("Harku thematic plan", "https://www.harku.ee/sites/default/files/documents/2025-08/Teemaplaneeringu%20seletuskiri.pdf"),
    },
}

ARTICLE = {
    # =====================================================================
    # ET
    # =====================================================================
    "et": {
        "title": "Lubatud aia kõrgus Harjumaal ja Tallinnas | LuxAed",
        "desc": "Lubatud aia kõrgus ja läbipaistvus Viimsis, Harkus, Rae valla põhjaosas, Sauel, Sakus, Kiilis, Keilas, Maardus ja Tallinnas. Nõuded koos allikatega.",
        "short": "Aia kõrgus Harjumaal",
        "image": "luxaed-picket",
        "kicker": "Juhend · valdade nõuded",
        "h1": "Lubatud aia kõrgus<br><em>Harjumaal ja Tallinnas</em>",
        "lead": "Aia kõrgust ei määra seadus, vaid valla või linna planeering, ja sageli on sama oluline, kui läbipaistev aed peab olema. Kogusime Harjumaa valdade ja Tallinna nõuded ühte tabelisse ning selgitame, kuidas neid oma krundi puhul lugeda.",
        "direct": ("Enamikus Harjumaa planeeringutes on eramu aia lubatud kõrgus 1,5 m, kuid sageli peab aed olema ka osaliselt läbipaistev.",
                   "Kiilis on tänavapoolse aia lubatud kõrgus 1,4 m ning Loo alevikus, Liivamäel ja Saha küla põhjaosas 1,2 m. Sakus, Keilas ja Maardus peab aed olema vähemalt 25% ulatuses läbipaistev ning Sauel ei tehta läbipaistmatut aeda reeglina üldse. Kui krundil on kehtiv detailplaneering, lähtutakse eelkõige sellest."),
        "blocks": [
            {"type": "sections", "tag": "Seadus", "h": "Kust aia kõrguse nõuded tulenevad",
             "items": [
                 ("Planeering määrab, mitte seadus", [
                     "Ehitusseadustiku § 12 järgi peab ehitis olema kooskõlas planeeringuga: kui krundil on detailplaneering, lähtutakse sellest, ja kui seda ei ole, siis üldplaneeringust. Seadus ei määra aiale ühtset kõrgust, seega tulenevad kõrgus, läbipaistvus ja sageli ka materjal valla või linna planeeringust.",
                     "Harku ja Viimsi on aia nõuded koondanud teemaplaneeringusse ning Tallinna miljööaladel annab linn lisaks oma juhised."]),
                 ("Kuidas kõrgust mõõdetakse", [
                     "Kui planeering ei ütle teisiti, on ehitise kõrgus selle suurim vertikaalmõõde vahetult ümbritsevast maapinnast kõrgeima osa kõrgeima punktini. Aia puhul lähevad arvesse ka postide otsad ja postimütsid, mitte ainult paneel või laudis. Väikseid lohke ja kühme maapinnas ei arvestata. Kaldega krundi reeglit selgitame allpool."]),
                 ("Millal on vaja ehitusteatist", [
                     'Kui aia või värava ehitamisel kaevatakse sügavamale kui 30 cm, on vaja ehitusteatist ja ehitusprojekti. Teatis esitatakse ehitisregistris vähemalt 10 päeva enne tööde algust. Täpsemalt kirjutame sellest <a href="/aia-ehitusteatis/">ehitusteatise juhendis</a>.']),
             ],
             "sources": ["ehs", "tehn", "lisa1", "harku_tp", "viimsi", "tallinn"]},
            {"type": "table", "cls": "rules-table", "tag": "Vallad", "h": "Nõuded valdade ja Tallinna kaupa",
             "headers": ("Piirkond", "Kõrgus", "Läbipaistvus ja materjal", "Muud nõuded"),
             "rows": [
                 ('Harku vald<span class="cell-src"><a href="https://www.harku.ee/sites/default/files/documents/2025-08/Teemaplaneeringu%20seletuskiri.pdf" target="_blank" rel="noopener">Harku valla teemaplaneering</a>, <a href="https://www.harku.ee/ehitus-planeerimine-ja-taristu/ehitamine-ja-muud-seonduvad-tegevused/rajatised" target="_blank" rel="noopener">Harku vald, rajatised</a>, 30.03.2026</span>',
                  "Üksik-, kaksik- ja ridaelamu võrkaed või osaliselt läbipaistev puitaed kuni 1,5 m. Kõrgem aed ainult detailplaneeringu või ehitusloaprojekti alusel.",
                  "Läbipaistmatud plankaiad on keelatud, v.a müratõkkena või tööstusala piiramiseks. Puitmajale eelistatakse puitaeda.",
                  "Aed peab jääma teekatte servast vähemalt 2 m kaugusele, et lund saaks koristada."),
                 ('Viimsi vald<span class="cell-src"><a href="https://viimsi.ee/sites/default/files/documents/2025-09/Teemaplaneeringu%20seletuskiri.pdf" target="_blank" rel="noopener">Viimsi valla teemaplaneering</a>, <a href="https://viimsi.ee/ehitamine" target="_blank" rel="noopener">Viimsi vald, ehitamine</a></span>',
                  "Elamu ümber kuni 1,5 m. Korterelamu ümber ainult detailplaneeringuga ja kuni 1,0 m.",
                  "Läbipaistmatu plankaed ainult tööstus- või liiklusala ümber müra- või ohutustõkkena. Puitmajale soovitatakse puitaeda.",
                  "Vundamendiga, massiivne või üle 1,5 m aed vajab ehitusprojekti. Teekatte servast vähemalt 2 m. Aeda ei rajata väljapoole krundi piiri ega kallasrajale. Valla veebilehe järgi ei ole topeltaiad lubatud."),
                 ('Rae vald, põhjaosa (sh Peetri)<span class="cell-src"><a href="https://www.rae.ee/sites/default/files/documents/2025-06/Lisa%201_Seletuskiri.pdf" target="_blank" rel="noopener">Rae valla põhjapiirkonna üldplaneering</a></span>',
                  "Elamumaal kuni 1,5 m. Kaksik- ja ridaelamu bokside vahel hekk või kuni 1,0 m.",
                  "Kinnine aed kuni 1,8 m ainult müratõkkena, kui müra ületab piirnorme. Materjali valikul arvestatakse hoone ja naabrite aedadega.",
                  "Korterelamute krunte ei piirata. Väravad ei tohi avaneda teemaale. Mahasõit 3,5–5 m."),
                 ('Saue vald<span class="cell-src"><a href="https://www.sauevald.ee/sites/default/files/documents/2024-02/2021.06.28%20Saue%20valla%20u%CC%88ldplaneeringu%20seletuskiri_kehtestatud.pdf" target="_blank" rel="noopener">Saue valla üldplaneering</a></span>',
                  "Tiheasustusalal reeglina kuni 1,5 m, hajaasustuses kuni 2 m.",
                  "Läbipaistmatut aeda, olenemata materjalist, reeglina ei tehta. Erand on tööstusala ümbrus ning müra- või ohutustõke liiklusala ääres.",
                  "Teekatte servast reeglina vähemalt 2 m. Aeda ei rajata väljapoole krundi piiri. Keskuse maal piirdeaedu üldjuhul ei rajata."),
                 ('Saku vald<span class="cell-src"><a href="https://sakuvald.ee/wp-content/uploads/2025/10/Saku_YP_Seletuskiri.pdf" target="_blank" rel="noopener">Saku valla üldplaneering</a></span>',
                  "Pere- ja ridaelamumaal kuni 1,5 m maapinnast. Hajaasustuses kuni 2 m.",
                  "Läbipaistvus vähemalt 25%, pere- ja ridaelamumaal ei kehti see hekile. Kinnine aed ainult põhjendatud juhul müra või tolmu tõkkeks.",
                  "Korterelamu maal aeda üldjuhul ette ei nähta. Ulukiläbipääsude piiranguvööndis ei tohi aed takistada loomade liikumist."),
                 ('Kiili vald<span class="cell-src"><a href="https://www.kiilivald.ee/sites/default/files/documents/2026-06/Kiili_YP_seletuskiri_16_05_13.pdf" target="_blank" rel="noopener">Kiili valla üldplaneering</a></span>',
                  "Tänava pool kuni 1,4 m. Kruntidevaheline võrkaed kuni 1,6 m.",
                  "Tänava poole osaliselt läbipaistev puitaed. Läbipaistmatu plankaed on keelatud, v.a tööstushoonete ümber müra- ja turvatõkkena.",
                  "Suurel maaüksusel võib aia rajada vahetult hoonestatud ala ümber."),
                 ('Jõelähtme vald: Loo, Liivamäe, Saha põhjaosa ja Nehatu<span class="cell-src"><a href="https://joelahtme.ee/sites/default/files/documents/2026-06/Loo%20aleviku%2C%20Liivam%C3%A4e%20k%C3%BCla%2C%20Saha%20k%C3%BCla%20ja%20Nehatu%20k%C3%BCla%20%C3%BCldpaleneeringu%20seletuskiri.pdf" target="_blank" rel="noopener">Loo, Liivamäe, Saha ja Nehatu üldplaneering</a></span>',
                  "Loo alevikus, Liivamäel ja Saha põhjaosas pere- ja paariselamu maal kuni 1,2 m.",
                  "Läbipaistvus vähemalt 10%.",
                  "Ridaelamu maal lahendatakse aed detailplaneeringuga. Nehatu küla pereelamumaal piirdeaedu ei püstitata. Need on üldplaneeringu tingimused detailplaneeringute koostamiseks."),
                 ('Maardu linn<span class="cell-src"><a href="https://maardu.ee/sites/default/files/documents/2026-03/Maardu_linna_YP_Seletuskiri.pdf" target="_blank" rel="noopener">Maardu linna üldplaneering</a></span>',
                  "Väikeelamualadel tänavapoolne aed kuni 1,5 m.",
                  "Läbipaistvus vähemalt 25%. Kruntidevaheline aed peab olema läbinähtav.",
                  "Kruntidevahelise aia kõrgus ja materjal lepitakse kokku naabritega."),
                 ('Keila linn<span class="cell-src"><a href="https://planeering.keila.ee/maakasutus" target="_blank" rel="noopener">Keila linna üldplaneering</a></span>',
                  "Elamumaal üldjuhul kuni 1,5 m. Kesklinna miljööalal umbes 1,4 m.",
                  "Läbipaistvus vähemalt 25% jooksva meetri kohta. Tänava poole ei tohi rajada üle 1,5 m kõrgust läbipaistmatut müüri. Hekk võib olla kõrgem.",
                  "Kruntidevahelised aiad rajatakse naabrite kokkuleppel, üle 1,5 m kõrgune ainult naabrite kokkuleppel. Aeda ei rajata väljapoole krundi piiri ega korterelamu ümber, v.a detailplaneeringuga. Mälestisel ja selle kaitsevööndis kooskõlastatakse aed Muinsuskaitseametiga."),
                 ('Tallinn, Nõmme<span class="cell-src"><a href="https://www.tallinn.ee/et/media/311168" target="_blank" rel="noopener">Nõmme linnaosa üldplaneering</a></span>',
                  "Kuni 1,5 m, lähtudes naabrite aedadest.",
                  "Üldjuhul hõre läbipaistev puitlippaed või hekiga kombineeritud võrkaed. Kruntidevaheline aed võib olla ka võrkaed. Heki lubatud kõrgus on üldjuhul 1,5 m.",
                  "Krundisiseseid aedu ei rajata. Erilahendus vajab Linnaplaneerimise Ameti või linnaosa arhitekti ja piirinaabri kirjalikku nõusolekut. Nurgakrundil tuleb kaaluda tagasiastet või läbipaistvamat aeda."),
                 ('Tallinn, miljööalad<span class="cell-src"><a href="https://www.tallinn.ee/et/ehitus/piirdeaiad-hoovialad-ja-haljastus" target="_blank" rel="noopener">Tallinn, piirdeaiad miljööaladel</a>, 11.04.2024</span>',
                  "Tänavaäärne aed üldjuhul 1,2–1,5 m, plankaed 1,5–1,8 m, lähtudes naaberkruntide aedadest.",
                  "Võrk- ja keevispaneelaed ei ole miljööalale sobiv. Erandina võib kaaluda võrkaeda kruntide vahel, mitte tänava poole, kui tihe hekk või ronitaimed varjavad selle täielikult.",
                  "Võrkaia kasutamine ja ulatus otsustatakse iga juhtumi puhul eraldi. Aed ja väravad peavad sobima ajaloolise asumi ilmega."),
             ],
             "note": "Kontrollitud 27.09.2026 planeeringute ja valdade veebilehtede põhjal. Tabelis on üldised nõuded: kui krundil on kehtiv detailplaneering, lähtutakse sellest. Rae vallast kontrollisime ainult põhjapiirkonna üldplaneeringut (Tallinna piirist Kurna oja ja Tallinna ringteeni, sh Peetri). Teiste valdade ja Tallinna linnaosade nõuded leiate nende planeeringutest."},
            {"type": "sections", "tag": "Samm-sammult", "h": "Kuidas leida ja lugeda oma krundi nõudeid",
             "intro": "Tabel annab üldpildi, lõpliku vastuse annab teie krundi planeering.",
             "items": [
                 ("1. Leidke õige dokument", [
                     "Selgitage välja, kas krundil on kehtiv detailplaneering: selle leiate valla või linna planeeringute registrist või kaardirakendusest, Tallinnas Tallinna planeeringute registrist. Kui seda ei ole, kehtivad üldplaneering ja seda täpsustav teemaplaneering.",
                     "Tallinnas vaadake linna kodulehe kaardilt, kas krunt jääb miljööalale. Miljööalal soovitab linn lähtuda maja algse projekti aia lahendusest, mis on üldjuhul Linnaplaneerimise Ameti arhiivis."]),
                 ("2. Otsige õigetest kohtadest", [
                     "Aia nõuded on tavaliselt seletuskirja osas, mis käsitleb arhitektuuri, piirdeid või haljastust. Otsige sõnu „piirdeaed“, „piire“, „läbipaistvus“ ja „kõrgus“. Joonisel võivad olla ka ehitusjoon ja tagasiaste tänavast."]),
                 ("3. Eristage tänava- ja naabripoolset aeda", [
                     'Paljudes planeeringutes on tänava poole ja kruntide vahele eri nõuded. Kiilis tohib tänava poole teha kuni 1,4 m kõrguse osaliselt läbipaistva puitaia, kruntide vahele aga kuni 1,6 m võrkaia. Keilas ja Maardus sõltub kruntidevaheline aed naabrite kokkuleppest. Kuidas kokkulepe kirja panna, lugege <a href="/aed-naabri-piiril/">naabripiiril oleva aia juhendist</a>.']),
                 ("4. Kui midagi jääb ebaselgeks, küsige kirjalikult", [
                     "Saatke valla planeerimis- või ehitusspetsialistile lühike küsimus koos krundi aadressi, kavandatud kõrguse, materjali ja pildiga ning hoidke vastus alles. Nõmmes vajab erilahendus Linnaplaneerimise Ameti või linnaosa arhitekti ja piirinaabri kirjalikku nõusolekut.",
                     "Mälestisel ja muinsuskaitsealal vajab ehitamine Muinsuskaitseameti luba. Nende kaitsevööndis kooskõlastab vald ehitusteatise ametiga ja kui teatist vaja ei ole, tuleb ametit teavitada vähemalt 10 päeva ette."]),
             ],
             "sources": ["ehs", "tallinn", "kiili", "keila", "maardu", "nomme", "muks"]},
            {"type": "sections", "tag": "Läbipaistvus", "h": "Kuidas läbipaistvust hinnatakse",
             "items": [
                 ("Mida protsent tähendab", [
                     "Läbipaistvus näitab, kui suur osa aia vaatepinnast on avatud. Sakus, Keilas ja Maardus peab see olema vähemalt 25%, Loo alevikus, Liivamäel ja Saha küla põhjaosas vähemalt 10%. Keila planeering arvestab läbipaistvust jooksva meetri kohta."]),
                 ("Kuidas seda lippaial arvutada", [
                     "Jagage lippide vahe lipi laiuse ja vahe summaga. Kui lipi laius on 8 cm ja vahe 4 cm, on läbipaistvus 4 / 12 ehk umbes 33%. Kui vahe on 2 cm, jääb see 20% peale ega täida 25% nõuet. Postid ja põikpuud vähendavad avatud pinda veidi, seega jätke varu.",
                     "Nõmme üldplaneering soovitab lippide vaheks 1/3 kuni 1/2 lipi laiusest, et aed ei mõjuks suletud planguna. Kolmandik lipi laiusest annabki umbes 25% läbipaistvuse."]),
                 ("Kahepoolne lippaed", [
                     "Kahepoolne malepaigutusega lippaed laseb tuult läbi, kuid otse vaadates on see peaaegu kinnine. Nõmmes lubatakse sellist kahekihilist aeda erilahendusena suure liiklusega tänavate ääres. Kus planeering nõuab läbipaistvust, küsige enne tellimist vallalt, kas see sobib."]),
                 ("Hekk annab privaatsuse", [
                     "Kus aed peab olema läbipaistev, annab privaatsuse hekk. Saku pere- ja ridaelamumaal läbipaistvuse nõue hekile ei kehti ja Keilas võib hekk olla aiale seatud näitajatest kõrgem. Nõmmes on heki lubatud kõrgus siiski üldjuhul 1,5 m."]),
             ],
             "sources": ["saku", "keila", "maardu", "loo", "nomme"]},
            {"type": "sections", "tag": "Kalle", "h": "Aia kõrgus kaldega krundil",
             "items": [
                 ("Mida määrus ütleb", [
                     "Kaldega maapinnal arvestatakse kõrgust aeda vahetult ümbritseva madalaima ja kõrgeima maapinna aritmeetilisest keskmisest. Kui maapind on sektsiooni ühes otsas 40 cm kõrgemal kui teises, mõõdetakse kõrgust nende keskmiselt tasemelt ehk 20 cm kõrguselt madalama otsa maapinnast."]),
                 ("Astmeline või kalde järgi", [
                     "Jäigad paneelid paigaldatakse kaldel tavaliselt astmetena. Siis jääb iga astme allamäe otsas paneeli alla kolmnurkne vahe ja aed on seal kõrgem. Rullvõrgu, puitaia ja lippaia saab ehitada ka kalde järgi, nii et ülemine serv järgib maapinda ja kõrgus püsib ühtlane.",
                     "Soovitame hoida iga sektsiooni lubatud kõrguse piires, mõõdetuna selle kõrval olevast maapinnast. Nii ei teki vaidlust ka siis, kui keegi mõõdab aeda kõige ebasoodsamast kohast."]),
                 ("Postid, sokkel ja väravad", [
                     "Kõrgusesse lähevad ka postide otsad, postimütsid ja sokkel, kui see on aia osa. Värav ja väravapostid kuuluvad sama aia juurde, seega hoidke ka need lubatud kõrguse sees, kui planeering ei ütle teisiti.",
                     "Kui maapind on teie ja naabri pool eri kõrgusel, mõõtke aeda mõlemalt poolt. Tugimüüri peale tulev aed tasub vallaga enne läbi rääkida, sest naabri poolt vaadates võib kogukõrgus olla lubatust suurem."]),
             ],
             "sources": ["tehn"]},
            {"type": "sections", "tag": "Aiatüübid", "h": "Milline aed sobib nõuetega",
             "intro": 'Kiilis peab tänavapoolne aed olema osaliselt läbipaistev puitaed ja Nõmmes on see üldjuhul hõre puitlippaed või hekiga võrkaed, nii et metall- ja paneelaiad sobivad seal pigem kruntide vahele. Hinnad on meie <a href="/hinnad/">hinnatabelist</a> ning sisaldavad materjali ja tavapaigaldust.',
             "items": [
                 ("3D ja 2D paneelaed", [
                     'Paneelaed on läbipaistev ja sobib enamiku tabelis toodud planeeringutega; valige paneel, millega aed koos vahe ja postiotstega jääb lubatud kõrguse sisse. Tallinna miljööaladel keevispaneelaeda sobivaks ei peeta. <a href="/aiad/paneelaed/">3D paneelaed</a> maksab 35–60 €/jm, jäigem 2D paneelaed 50–85 €/jm.']),
                 ("Rullvõrkaed", [
                     "Võrkaed on läbipaistev ja kõige soodsam, 25–45 €/jm. See sobib hästi külg- ja tagapiirile, sest mitu planeeringut, näiteks Kiili ja Nõmme oma, lubab kruntide vahel võrkaeda. Tänava poole kombineerige see hekiga, kui planeering seda eeldab."]),
                 ("Metall-lippaed", [
                     '<a href="/aiad/lippaed/">Metall-lippaia</a> läbipaistvus sõltub lippide vahest, mille valite ise. Ühepoolne paigutus ja piisav vahe täidavad 25% nõude tavaliselt kergesti, kahepoolne malepaigutus mitte alati. Hind on 85–155 €/jm.']),
                 ("Varbaed", [
                     'Keevitatud <a href="/aiad/metallaed/">varbaed</a> on läbipaistev ka tänava poole ja sobib sinna, kus planeering nõuab õhulist aeda, kuid soovite esinduslikku ja vastupidavat lahendust. Hind on 140–280 €/jm. Miljööalal peab ka metallaia kujundus sobima ajaloolise asumi ilmega.']),
                 ("Puitaed", [
                     "Osaliselt läbipaistev puitaed on mitmes planeeringus eelistatud: Harku ja Kiili nimetavad seda otse ning Viimsi soovitab puitmajale puitaeda. Läbipaistmatu plankaed on Harkus, Viimsis ja Kiilis lubatud vaid erandina, näiteks müratõkkena. Puitaed maksab 90–160 €/jm."]),
                 ("Profiilplekk-aed", [
                     'Profiilplekk on läbipaistmatu, seega ei sobi see sinna, kus planeering nõuab läbipaistvust. Sauel ei tehta läbipaistmatut aeda reeglina üldse ning Rae valla põhjaosas lubatakse kinnist aeda kuni 1,8 m ainult müratõkkena. Enne <a href="/kinnine-aed/">kinnise aia</a> tellimist küsige vallalt kinnitust. Hind on 70–135 €/jm.']),
             ],
             "sources": ["kiili", "nomme", "harku_tp", "viimsi", "saue", "rae", "tallinn"]},
            {"type": "cards", "tag": "Meie soovitus", "h": "Mida me ise soovitame", "cols": 2,
             "items": [
                 ("Planeering enne materjali", "Valige aed alles siis, kui teate lubatud kõrgust ja läbipaistvuse nõuet. Nii ei maksa te aia eest, mis tuleb hiljem ümber teha."),
                 ("Jätke kõrgusele varu", "Soovitame jääda lubatud kõrgusest paar sentimeetrit allapoole. Maapind liigub külmaga, postimütsid lisavad kõrgust ja väike varu hoiab ära vaidluse."),
                 ("Privaatsus hekist", "Kus planeering nõuab läbipaistvust, sobib hästi läbipaistev aed ja selle taha istutatud hekk. Aed vastab reeglitele ja hekk annab aastatega privaatsuse."),
                 ("Tee äär ja lumi", 'Kui krunt piirneb teega, kontrollige tabelist kaugust teekatte servast ja lugege ka <a href="/aed-tee-ja-trasside-lahedal/">juhendit aia kohta tee ääres</a>. Liiga tee lähedal olev aed segab lumekoristust.'),
             ]},
            {"type": "cards", "tag": "Levinud probleemid", "h": "Mis läheb sageli valesti", "cols": 2,
             "items": [
                 ("Naabri aed võetakse eeskujuks", "Vana aed võib olla ehitatud enne praegust planeeringut või erikokkuleppega. Uus aed peab vastama kehtivatele nõuetele."),
                 ("Kinnine aed läbipaistvuse alal", "Profiilplekk- või plankaed pannakse alale, kus planeering nõuab läbipaistvust, ja selle võib tulla ümber teha."),
                 ("Kõrgus mõõdetakse paneelist", "Postimütsid, sokkel ja vahe maapinnaga jäetakse arvestamata ning valmis aed on lubatust kõrgem."),
                 ("Värav avaneb tänavale", "Tänava poole avanev tiib segab liiklust ja lumekoristust. Kontrollige planeeringust, kas see on üldse lubatud."),
             ]},
        ],
        "faq": [
            ("Kui kõrge tohib eramu aed Harjumaal olla?", "Enamikus meie kontrollitud planeeringutes kuni 1,5 m. Kiilis on tänavapoolse aia lubatud kõrgus 1,4 m ning Loo alevikus, Liivamäel ja Saha küla põhjaosas 1,2 m. Hajaasustuses lubavad Saue ja Saku kuni 2 m."),
            ("Mida tähendab 25% läbipaistvus?", "Vähemalt veerand aia vaatepinnast peab olema läbi nähtav, Keilas arvestatakse seda jooksva meetri kohta. Lippaias annab sellise tulemuse vahe, mis on umbes kolmandik lipi laiusest. 3D paneelaed ja varbaed on läbipaistvad, kinnine profiilplekk- või plankaed mitte."),
            ("Kas eramu ümber tohib ehitada kinnise aia?", "Üldjuhul mitte. Viimsis, Harkus ja Kiilis on läbipaistmatu plankaed lubatud vaid erandina, näiteks müratõkkena või tööstusala ümber, ning Sauel kehtib sama piirang igasugusele läbipaistmatule aiale. Rae valla põhjaosas lubatakse kinnist aeda kuni 1,8 m müratõkkena, kui müra ületab piirnorme."),
            ("Kuidas mõõdetakse aia kõrgust kaldega krundil?", "Kui planeering ei ütle teisiti, mõõdetakse kõrgust aeda vahetult ümbritsevast maapinnast aia kõrgeima punktini, ka postiotsteni. Kaldel võetakse aluseks madalaima ja kõrgeima maapinna keskmine. Soovitame hoida iga sektsiooni lubatud kõrguse piires, mõõdetuna selle kõrvalt."),
            ("Naabril on kõrgem aed. Kas võin ka sama kõrge teha?", "Mitte tingimata. Naabri aed võib olla ehitatud enne praegust planeeringut või erikokkuleppe alusel, uus aed peab aga vastama kehtivatele nõuetele. Kontrollige oma krundi planeeringut või küsige vallalt."),
            ("Mis siis, kui minu valda tabelis ei ole?", "Vaadake oma krundi detailplaneeringut ja valla üldplaneeringut või küsige valla planeerimisspetsialistilt kirjalikku vastust. Mõõdistusel aitame nõuded aia valikul arvesse võtta."),
        ],
        "links_keys": ["permit_guide", "privacy_fence", "neighbour"],
        "links_extra": [("/aiad/metallaed/", "Metallaed ja varbaed", "Läbipaistev aed tänava äärde.")],
        "cta": ("Valime aia, mis sobib planeeringuga", "Mõõdistusel arvestame lubatud kõrguse, läbipaistvuse ja tee äärega ning pakume sobiva lahenduse.", "/#form", "Küsi pakkumist"),
    },
    # =====================================================================
    # RU
    # =====================================================================
    "ru": {
        "title": "Высота забора в Харьюмаа и Таллинне | LuxAed",
        "desc": "Какой высоты и насколько прозрачным может быть забор в Виймси, Харку, Сауэ, Саку, Кийли, Кейле, Маарду, Таллинне и в северной части Раэ. Правила с источниками.",
        "short": "Высота забора в Харьюмаа",
        "image": "luxaed-picket",
        "kicker": "Руководство · требования волостей",
        "h1": "Высота забора<br><em>в Харьюмаа и Таллинне</em>",
        "lead": "Высоту забора задаёт не закон, а планировка волости или города, и часто не менее важно, насколько прозрачным должен быть забор. Мы собрали требования волостей Харьюмаа и Таллинна в одну таблицу и объясняем, как применить их к своему участку.",
        "direct": ("В большинстве планировок Харьюмаа забор частного дома может быть высотой до 1,5 м, но часто он должен быть и частично прозрачным.",
                   "В Кийли забор со стороны улицы может быть до 1,4 м, а в Лоо, Лийвамяэ и северной части Саха до 1,2 м. В Саку, Кейле и Маарду забор должен быть прозрачным не менее чем на 25%, а в Сауэ глухой забор, как правило, не ставят вообще. Если у участка есть действующая детальная планировка, исходят прежде всего из неё."),
        "blocks": [
            {"type": "sections", "tag": "Закон", "h": "Откуда берутся требования к высоте забора",
             "items": [
                 ("Высоту задаёт планировка, а не закон", [
                     "По § 12 строительного кодекса сооружение должно соответствовать планировке: если у участка есть детальная планировка, исходят из неё, а если её нет, из общей планировки. Закон не задаёт забору единую высоту, поэтому высота, прозрачность и часто материал берутся из планировки волости или города.",
                     "Харку и Виймси собрали требования к заборам в тематической планировке, а в районах miljööala Таллинна город даёт свои указания."]),
                 ("Как измеряют высоту", [
                     "Если планировка не говорит иначе, высота сооружения равна его наибольшему вертикальному размеру от земли непосредственно вокруг него до самой высокой точки самой высокой части. Для забора это значит, что в высоту входят верх столбов и колпаки, а не только панель или доски. Мелкие ямки и бугорки на земле не учитывают. Правило для склона объясняем ниже."]),
                 ("Когда нужно уведомление о строительстве", [
                     'Если при установке забора или ворот копают глубже 30 см, нужны уведомление о строительстве (ehitusteatis) и проект. Уведомление подают через строительный регистр не позднее чем за 10 дней до начала работ. Подробнее в <a href="/ru/razreshenie-na-zabor/">статье о разрешении на забор</a>.']),
             ],
             "sources": ["ehs", "tehn", "lisa1", "harku_tp", "viimsi", "tallinn"]},
            {"type": "table", "cls": "rules-table", "tag": "Волости", "h": "Требования по волостям и в Таллинне",
             "headers": ("Где", "Высота", "Прозрачность и материал", "Другие требования"),
             "rows": [
                 ('Волость Харку<span class="cell-src"><a href="https://www.harku.ee/sites/default/files/documents/2025-08/Teemaplaneeringu%20seletuskiri.pdf" target="_blank" rel="noopener">Харку, тематическая планировка</a>, <a href="https://www.harku.ee/ehitus-planeerimine-ja-taristu/ehitamine-ja-muud-seonduvad-tegevused/rajatised" target="_blank" rel="noopener">Волость Харку, сооружения</a>, 30.03.2026</span>',
                  "Сетка или частично прозрачный деревянный забор у частного, двухквартирного или рядного дома до 1,5 м. Выше только по детальной планировке или проекту со строительным разрешением.",
                  "Глухие дощатые заборы запрещены, кроме шумовых барьеров и ограждения промышленных территорий. Деревянному дому предпочтителен деревянный забор.",
                  "Забор должен стоять не ближе 2 м от края покрытия дороги, чтобы можно было убирать снег."),
                 ('Волость Виймси<span class="cell-src"><a href="https://viimsi.ee/sites/default/files/documents/2025-09/Teemaplaneeringu%20seletuskiri.pdf" target="_blank" rel="noopener">Виймси, тематическая планировка</a>, <a href="https://viimsi.ee/ehitamine" target="_blank" rel="noopener">Виймси, строительство</a></span>',
                  "У жилого дома до 1,5 м. У многоквартирного дома только по детальной планировке и до 1,0 м.",
                  "Глухой дощатый забор только вокруг промышленной или транспортной зоны как шумовой или защитный барьер. Деревянному дому рекомендуют деревянный забор.",
                  "Забор на фундаменте, массивный или выше 1,5 м строят по проекту. Не ближе 2 м от края покрытия дороги. Забор не ставят за пределами участка и на береговой тропе. По сайту волости двойные заборы не допускаются."),
                 ('Волость Раэ, северная часть (в т.ч. Пеэтри)<span class="cell-src"><a href="https://www.rae.ee/sites/default/files/documents/2025-06/Lisa%201_Seletuskiri.pdf" target="_blank" rel="noopener">Раэ, общая планировка северной части</a></span>',
                  "На жилой земле до 1,5 м. Между блоками двухквартирных и рядных домов живая изгородь или забор до 1,0 м.",
                  "Глухой забор до 1,8 м только как шумовой барьер, если шум превышает нормы. Материал подбирают с учётом дома и соседних заборов.",
                  "Участки многоквартирных домов не огораживают. Ворота не должны открываться на дорогу. Въезд шириной 3,5–5 м."),
                 ('Волость Сауэ<span class="cell-src"><a href="https://www.sauevald.ee/sites/default/files/documents/2024-02/2021.06.28%20Saue%20valla%20u%CC%88ldplaneeringu%20seletuskiri_kehtestatud.pdf" target="_blank" rel="noopener">Сауэ, общая планировка</a></span>',
                  "В плотной застройке, как правило, до 1,5 м, в рассеянной до 2 м.",
                  "Глухой забор из любого материала, как правило, не ставят. Исключения: вокруг промышленных зон и у транспортных зон как шумовой или защитный барьер.",
                  "Как правило, не ближе 2 м от края покрытия дороги. Забор не ставят за пределами участка. На земле центра заборы, как правило, не ставят."),
                 ('Волость Саку<span class="cell-src"><a href="https://sakuvald.ee/wp-content/uploads/2025/10/Saku_YP_Seletuskiri.pdf" target="_blank" rel="noopener">Саку, общая планировка</a></span>',
                  "На земле частных и рядных домов до 1,5 м от земли. В рассеянной застройке до 2 м.",
                  "Прозрачность не менее 25%, на земле частных и рядных домов это не касается живой изгороди. Глухой забор только в обоснованном случае для защиты от шума или пыли.",
                  "На земле многоквартирных домов заборы, как правило, не предусматривают. В зоне ограничений у переходов для диких животных забор не должен мешать их движению."),
                 ('Волость Кийли<span class="cell-src"><a href="https://www.kiilivald.ee/sites/default/files/documents/2026-06/Kiili_YP_seletuskiri_16_05_13.pdf" target="_blank" rel="noopener">Кийли, общая планировка</a></span>',
                  "Со стороны улицы до 1,4 м. Сетка между участками до 1,6 м.",
                  "Со стороны улицы частично прозрачный деревянный забор. Глухие дощатые заборы запрещены, кроме как вокруг промышленных зданий для защиты от шума и для безопасности.",
                  "На большом участке забор можно поставить непосредственно вокруг застроенной части."),
                 ('Йыэляхтме: Лоо, Лийвамяэ, север Саха и Нехату<span class="cell-src"><a href="https://joelahtme.ee/sites/default/files/documents/2026-06/Loo%20aleviku%2C%20Liivam%C3%A4e%20k%C3%BCla%2C%20Saha%20k%C3%BCla%20ja%20Nehatu%20k%C3%BCla%20%C3%BCldpaleneeringu%20seletuskiri.pdf" target="_blank" rel="noopener">Лоо, Лийвамяэ, Саха и Нехату, общая планировка</a></span>',
                  "В Лоо, Лийвамяэ и северной части Саха на земле частных и двухквартирных домов до 1,2 м.",
                  "Прозрачность не менее 10%.",
                  "Для рядных домов забор решают в детальной планировке. На земле частных домов в деревне Нехату заборы не ставят. Это условия общей планировки для составления детальных планировок."),
                 ('Город Маарду<span class="cell-src"><a href="https://maardu.ee/sites/default/files/documents/2026-03/Maardu_linna_YP_Seletuskiri.pdf" target="_blank" rel="noopener">Маарду, общая планировка</a></span>',
                  "В районах частных домов уличный забор до 1,5 м.",
                  "Прозрачность не менее 25%. Забор между участками должен быть просматриваемым.",
                  "Высоту и материал забора между участками согласуют соседи."),
                 ('Город Кейла<span class="cell-src"><a href="https://planeering.keila.ee/maakasutus" target="_blank" rel="noopener">Кейла, общая планировка</a></span>',
                  "На жилой земле, как правило, до 1,5 м. В исторической части центра около 1,4 м.",
                  "Прозрачность не менее 25% на погонный метр. Со стороны улицы нельзя ставить глухую стену выше 1,5 м. Живая изгородь может быть выше.",
                  "Заборы между участками ставят по договорённости соседей, выше 1,5 м только так. Забор не ставят за пределами участка и вокруг многоквартирного дома, кроме как по детальной планировке. На памятнике и в его охранной зоне забор согласуют с Департаментом охраны памятников."),
                 ('Таллинн, Нымме<span class="cell-src"><a href="https://www.tallinn.ee/et/media/311168" target="_blank" rel="noopener">Нымме, общая планировка</a></span>',
                  "До 1,5 м, с учётом заборов соседей.",
                  "Как правило, редкий прозрачный деревянный штакетник или сетка в сочетании с живой изгородью. Между участками может быть сетка. Живая изгородь, как правило, не выше 1,5 м.",
                  "Заборы внутри участка не ставят. Особое решение требует письменного согласия Департамента городского планирования или архитектора района и соседа. На угловом участке нужно рассмотреть отступ или более прозрачный забор."),
                 ('Таллинн, районы miljööala<span class="cell-src"><a href="https://www.tallinn.ee/et/ehitus/piirdeaiad-hoovialad-ja-haljastus" target="_blank" rel="noopener">Таллинн, заборы в miljööala</a>, 11.04.2024</span>',
                  "Уличный забор обычно 1,2–1,5 м, дощатый 1,5–1,8 м, с оглядкой на заборы соседних участков.",
                  "Сетчатые и сварные панельные заборы для miljööala не подходят. В виде исключения можно рассмотреть сетку между участками, но не со стороны улицы, если её полностью скрывает густая живая изгородь или вьющиеся растения.",
                  "Применение и объём сетки решают в каждом случае отдельно. Забор и ворота должны подходить к облику исторического района."),
             ],
             "note": "Проверено 27.09.2026 по планировкам и сайтам волостей. В таблице общие требования: если у участка есть действующая детальная планировка, исходят из неё. В волости Раэ мы проверили только общую планировку северной части (от границы Таллинна до ручья Курна и Таллиннской кольцевой дороги, включая Пеэтри). Требования других волостей и районов Таллинна ищите в их планировках."},
            {"type": "sections", "tag": "Шаг за шагом", "h": "Как найти и прочитать требования для своего участка",
             "intro": "Таблица даёт общую картину, а окончательный ответ даёт планировка вашего участка.",
             "items": [
                 ("1. Найдите нужный документ", [
                     "Выясните, есть ли у участка действующая детальная планировка: её можно найти в регистре планировок или на карте волости или города, в Таллинне в регистре планировок Таллинна. Если её нет, действуют общая планировка и уточняющая её тематическая планировка.",
                     "В Таллинне проверьте по карте на сайте города, не находится ли участок в районе miljööala. В таких районах город советует исходить из забора по первоначальному проекту дома, который обычно хранится в архиве Департамента городского планирования."]),
                 ("2. Ищите в правильных разделах", [
                     "Требования к забору обычно находятся в разделе пояснительной записки об архитектуре, ограждениях или озеленении. Планировки написаны по-эстонски, поэтому ищите слова «piirdeaed» (забор), «piire» (ограждение), «läbipaistvus» (прозрачность) и «kõrgus» (высота). На чертеже могут быть и строительная линия, и отступ от улицы."]),
                 ("3. Различайте уличный забор и забор с соседом", [
                     'Многие планировки задают разные требования для уличной стороны и для границы между участками. В Кийли со стороны улицы можно поставить частично прозрачный деревянный забор до 1,4 м, а между участками сетку до 1,6 м. В Кейле и Маарду забор между участками зависит от договорённости соседей. Как её оформить, читайте в <a href="/ru/zabor-s-sosedom/">статье о заборе между соседями</a>.']),
                 ("4. Если что-то неясно, спросите письменно", [
                     "Отправьте специалисту волости по планировке или строительству короткий вопрос с адресом участка, планируемой высотой, материалом и фото и сохраните ответ. В Нымме особое решение требует письменного согласия Департамента городского планирования или архитектора района и соседа.",
                     "На памятнике и на территории muinsuskaitseala для строительства нужно разрешение Департамента охраны памятников. В их охранной зоне волость согласует уведомление с департаментом, а если уведомление не нужно, департамент извещают не позднее чем за 10 дней до начала работ."]),
             ],
             "sources": ["ehs", "tallinn", "kiili", "keila", "maardu", "nomme", "muks"]},
            {"type": "sections", "tag": "Прозрачность", "h": "Как оценивают прозрачность",
             "items": [
                 ("Что означает процент", [
                     "Прозрачность показывает, какая доля видимой поверхности забора открыта. В Саку, Кейле и Маарду она должна составлять не менее 25%, в Лоо, Лийвамяэ и северной части Саха не менее 10%. Планировка Кейлы считает прозрачность на погонный метр."]),
                 ("Как посчитать для штакетника", [
                     "Разделите просвет между планками на сумму ширины планки и просвета. Если планка шириной 8 см, а просвет 4 см, прозрачность составляет 4 / 12, то есть около 33%. При просвете 2 см она падает до 20% и требованию 25% уже не соответствует. Столбы и поперечины немного уменьшают открытую площадь, поэтому оставьте запас.",
                     "Общая планировка Нымме советует делать просвет от 1/3 до 1/2 ширины планки, чтобы забор не выглядел сплошной стеной. Просвет в треть ширины планки как раз даёт около 25% прозрачности."]),
                 ("Двусторонний штакетник", [
                     "Двусторонний штакетник в шахматном порядке пропускает ветер, но если смотреть прямо, он почти глухой. В Нымме его допускают как особое решение вдоль оживлённых улиц. Если ваша планировка требует прозрачности, до заказа спросите в волости, подойдёт ли он."]),
                 ("Приватность даёт живая изгородь", [
                     "Где забор должен быть прозрачным, приватность даёт живая изгородь. В Саку на земле частных и рядных домов требование прозрачности на живую изгородь не распространяется, а в Кейле она может быть выше значений, установленных для забора. В Нымме её высота, однако, как правило, ограничена 1,5 м."]),
             ],
             "sources": ["saku", "keila", "maardu", "loo", "nomme"]},
            {"type": "sections", "tag": "Склон", "h": "Высота забора на участке со склоном",
             "items": [
                 ("Что говорит постановление", [
                     "На склоне высоту считают от среднего арифметического между самой низкой и самой высокой отметкой земли непосредственно вокруг забора. Если на одном конце секции земля на 40 см выше, чем на другом, высоту измеряют от среднего уровня, то есть от отметки на 20 см выше земли у нижнего конца."]),
                 ("Ступенями или по уклону", [
                     "Жёсткие панели на склоне обычно ставят ступенями, и у нижнего конца каждой ступени под панелью остаётся треугольный зазор, где забор выше над землёй. Сетку, деревянный забор и штакетник можно вести и по уклону, тогда верхний край повторяет рельеф, а высота остаётся ровной.",
                     "Мы советуем держать каждую секцию в пределах допустимой высоты, измеряя от земли рядом с ней. Тогда споров не будет, даже если кто-то измерит забор в самом невыгодном месте."]),
                 ("Столбы, цоколь и ворота", [
                     "В высоту входят верх столбов, колпаки и цоколь, если он является частью забора. Ворота и воротные столбы относятся к тому же забору, поэтому держите и их в пределах допустимой высоты, если планировка не говорит иначе.",
                     "Если земля у вас и у соседа на разном уровне, измерьте забор с обеих сторон. Забор на подпорной стенке лучше заранее обсудить с волостью: со стороны соседа общая высота может оказаться больше допустимой."]),
             ],
             "sources": ["tehn"]},
            {"type": "sections", "tag": "Типы заборов", "h": "Какой забор подходит под требования",
             "intro": 'В Кийли уличный забор должен быть частично прозрачным деревянным, а в Нымме это обычно редкий деревянный штакетник или сетка с живой изгородью, поэтому металлические и панельные заборы там лучше ставить между участками. Цены взяты из нашего <a href="/ru/ceny/">прайса</a> и включают материал и стандартный монтаж.',
             "items": [
                 ("3D- и 2D-панели", [
                     'Забор из сварных панелей прозрачный и подходит под большинство планировок из таблицы; выбирайте панель так, чтобы весь забор с зазором и столбами уложился в допустимую высоту. В районах miljööala Таллинна сварные панели считаются неподходящими. <a href="/ru/zabory/2d-3d-setka/">Забор из 3D-панелей</a> стоит 35–60 €/м, более жёсткий 2D 50–85 €/м.']),
                 ("Сетка-рабица", [
                     "Сетка прозрачна и дешевле всего, 25–45 €/м. Она хорошо подходит для боковых и задней границ, потому что многие планировки, например в Кийли и Нымме, допускают сетку между участками. Со стороны улицы сочетайте её с живой изгородью, если этого ждёт планировка."]),
                 ("Металлический штакетник", [
                     'Прозрачность <a href="/ru/zabory/metallicheskie-lameli/">металлического штакетника</a> зависит от просвета, который вы выбираете сами. Односторонняя схема с достаточным просветом обычно легко даёт 25%, двусторонняя в шахматном порядке не всегда. Цена составляет 85–155 €/м.']),
                 ("Сварной прутковый забор", [
                     '<a href="/ru/zabory/prutkovye/">Прутковый забор</a> прозрачен и со стороны улицы, поэтому подходит там, где планировка требует лёгкого забора, а вам нужен представительный и прочный вариант. Цена составляет 140–280 €/м. В районе miljööala его дизайн тоже должен соответствовать облику исторического района.']),
                 ("Деревянный забор", [
                     "Частично прозрачный деревянный забор в нескольких планировках считается предпочтительным: Харку и Кийли называют его прямо, а Виймси рекомендует деревянный забор для деревянного дома. Глухой дощатый забор в Харку, Виймси и Кийли допускается только как исключение, например как шумовой барьер. Деревянный забор стоит 90–160 €/м."]),
                 ("Профнастил", [
                     'Профнастил непрозрачен, поэтому не подходит там, где планировка требует прозрачности. В Сауэ глухие заборы, как правило, не ставят вообще, а в северной части Раэ глухой забор до 1,8 м допускается только как шумовой барьер. Прежде чем заказывать <a href="/ru/gluhoj-zabor/">глухой забор</a>, получите подтверждение волости. Цена составляет 70–135 €/м.']),
             ],
             "sources": ["kiili", "nomme", "harku_tp", "viimsi", "saue", "rae", "tallinn"]},
            {"type": "cards", "tag": "Наш совет", "h": "Что мы советуем", "cols": 2,
             "items": [
                 ("Сначала планировка, потом материал", "Выбирайте забор, когда уже знаете допустимую высоту и требования к прозрачности. Так вы не заплатите за забор, который потом придётся переделывать."),
                 ("Оставьте запас по высоте", "Советуем держаться на пару сантиметров ниже допустимой высоты. Земля зимой поднимается и оседает, колпаки добавляют высоту, а небольшой запас избавит от споров."),
                 ("Приватность за счёт живой изгороди", "Где планировка требует прозрачности, хорошо работает прозрачный забор с живой изгородью за ним. Забор соответствует правилам, а изгородь с годами даёт приватность."),
                 ("Край дороги и снег", 'Если участок граничит с дорогой, проверьте в таблице расстояние от края покрытия и прочитайте статью о <a href="/ru/zabor-u-dorogi-i-kommunikacij/">заборе у дороги и охранных зонах</a>. Забор у самой дороги мешает уборке снега.'),
             ]},
            {"type": "cards", "tag": "Частые проблемы", "h": "Что часто идёт не так", "cols": 2,
             "items": [
                 ("Ориентир на забор соседа", "Старый забор могли поставить до нынешней планировки или по особой договорённости. Новый забор должен соответствовать действующим требованиям."),
                 ("Глухой забор там, где нужна прозрачность", "Профнастил или доски ставят там, где планировка требует прозрачности, и забор могут потребовать переделать."),
                 ("Высоту меряют только по панели", "Колпаки, цоколь и зазор снизу не учитывают, и готовый забор оказывается выше допустимого."),
                 ("Ворота открываются на улицу", "Створка, открывающаяся на улицу, мешает движению и уборке снега. Проверьте в планировке, допускается ли это вообще."),
             ]},
        ],
        "faq": [
            ("Какой высоты может быть забор частного дома в Харьюмаа?", "В большинстве проверенных нами планировок до 1,5 м. В Кийли забор со стороны улицы может быть до 1,4 м, а в Лоо, Лийвамяэ и северной части Саха до 1,2 м. В рассеянной застройке Сауэ и Саку допускают до 2 м."),
            ("Что значит прозрачность 25%?", "Не меньше четверти видимой поверхности забора должно просматриваться, в Кейле это считают на погонный метр. У штакетника такой результат даёт просвет примерно в треть ширины планки. 3D-панели и прутковый забор прозрачны, а глухой забор из профнастила или досок нет."),
            ("Можно ли поставить глухой забор у частного дома?", "Как правило, нет. В Виймси, Харку и Кийли глухой дощатый забор допускается только как исключение, например как шумовой барьер или вокруг промышленной территории, а в Сауэ такое ограничение касается любого глухого забора. В северной части Раэ глухой забор до 1,8 м допускается как шумовой барьер, если шум превышает нормы."),
            ("Как измеряют высоту забора на склоне?", "Если планировка не говорит иначе, высоту измеряют от земли непосредственно у забора до его самой высокой точки, включая верх столбов. На склоне берут среднее между самой низкой и самой высокой отметкой земли. Мы советуем держать каждую секцию в пределах допустимой высоты, измеряя рядом с ней."),
            ("У соседа забор выше. Можно ли мне такой же?", "Не обязательно. Забор соседа могли поставить до действующей планировки или по особой договорённости, а новый забор должен соответствовать нынешним требованиям. Проверьте планировку своего участка или спросите в волости."),
            ("Что делать, если моей волости нет в таблице?", "Посмотрите детальную планировку участка и общую планировку волости или попросите письменный ответ у специалиста по планировке. На замере поможем учесть требования при выборе забора."),
        ],
        "links_keys": ["permit_guide", "privacy_fence", "neighbour"],
        "links_extra": [("/ru/zabory/prutkovye/", "Сварной прутковый забор", "Прозрачный забор со стороны улицы.")],
        "cta": ("Подберём забор по планировке", "На замере учтём допустимую высоту, прозрачность и край дороги и предложим подходящее решение.", "/ru/#form", "Оставить заявку"),
    },
    # =====================================================================
    # EN
    # =====================================================================
    "en": {
        "title": "Fence Height Rules in Harju County and Tallinn | LuxAed",
        "desc": "How tall and how see-through a fence may be in Viimsi, Harku, northern Rae, Saue, Saku, Kiili, Keila, Maardu and Tallinn: the planning rules, with sources.",
        "short": "Fence height rules in Harju County",
        "image": "luxaed-picket",
        "kicker": "Guide · municipal rules",
        "h1": "Fence height rules<br><em>in Harju County and Tallinn</em>",
        "lead": "Fence height is set by the municipal or city plan, not by national law, and how see-through the fence must be often matters just as much. We have gathered the rules of Harju County municipalities and Tallinn in one table and explain how to apply them to your own plot.",
        "direct": ("In most Harju County plans a house fence may be up to 1.5 m tall, but it often has to be partly see-through as well.",
                   "Kiili allows 1.4 m on the street side, and Loo, Liivamäe and northern Saha 1.2 m. Saku, Keila and Maardu require at least 25% transparency, and Saue generally allows no opaque fence at all. If your plot has a valid detailed plan, that plan comes first."),
        "blocks": [
            {"type": "sections", "tag": "The law", "h": "Where fence height rules come from",
             "items": [
                 ("The plan decides, not the law", [
                     "Under § 12 of the Building Code, a structure must comply with the plan: if your plot has a detailed plan, that plan applies, and if not, the general plan does. The law sets no single fence height, so height, transparency and often the material come from the municipal or city plan.",
                     "Harku and Viimsi have put their fence rules in a thematic plan, and in Tallinn's milieu-value areas (miljööala) the city adds its own guidance."]),
                 ("How height is measured", [
                     "Unless the plan says otherwise, a structure's height is its greatest vertical dimension from the ground immediately around it to the highest point of its highest part. For a fence this means post tops and caps count too, not just the panel or boards. Minor local dips and bumps in the ground are ignored. We explain the rule for slopes below."]),
                 ("When you need a building notice", [
                     'If building the fence or gate involves digging deeper than 30 cm, you need a building notice and a design. The notice is filed in the Building Register at least 10 days before work starts. There is more in our <a href="/en/fence-permit/">fence permit guide</a>.']),
             ],
             "sources": ["ehs", "tehn", "lisa1", "harku_tp", "viimsi", "tallinn"]},
            {"type": "table", "cls": "rules-table", "tag": "Municipalities", "h": "Rules by municipality and in Tallinn",
             "headers": ("Area", "Height", "Transparency and material", "Other rules"),
             "rows": [
                 ('Harku Municipality<span class="cell-src"><a href="https://www.harku.ee/sites/default/files/documents/2025-08/Teemaplaneeringu%20seletuskiri.pdf" target="_blank" rel="noopener">Harku thematic plan</a>, <a href="https://www.harku.ee/ehitus-planeerimine-ja-taristu/ehitamine-ja-muud-seonduvad-tegevused/rajatised" target="_blank" rel="noopener">Harku Municipality, structures</a>, 30.03.2026</span>',
                  "Mesh or partly transparent timber fence at a detached, semi-detached or terraced house up to 1.5 m. Taller only under a detailed plan or a building-permit design.",
                  "Solid close-boarded fences are banned, except as noise barriers or around industrial sites. Timber fences are preferred for timber houses.",
                  "The fence must stand at least 2 m from the road surface edge so snow can be cleared."),
                 ('Viimsi Municipality<span class="cell-src"><a href="https://viimsi.ee/sites/default/files/documents/2025-09/Teemaplaneeringu%20seletuskiri.pdf" target="_blank" rel="noopener">Viimsi thematic plan</a>, <a href="https://viimsi.ee/ehitamine" target="_blank" rel="noopener">Viimsi, building</a></span>',
                  "Up to 1.5 m around a house. Around an apartment block only if a detailed plan allows, up to 1.0 m.",
                  "Solid plank fences only around industrial or traffic areas as a noise or safety barrier. Timber fences are recommended for timber houses.",
                  "Fences on foundations, solid masonry fences or fences over 1.5 m need a design. At least 2 m from the road surface edge. No fences outside the plot or on the shore path. The municipality's website says double fences are not allowed."),
                 ('Rae Municipality, northern part (incl. Peetri)<span class="cell-src"><a href="https://www.rae.ee/sites/default/files/documents/2025-06/Lisa%201_Seletuskiri.pdf" target="_blank" rel="noopener">Rae northern area general plan</a></span>',
                  "Up to 1.5 m on residential land. Between semi-detached or terraced units, a hedge or up to 1.0 m.",
                  "A solid fence up to 1.8 m only as a noise barrier where noise exceeds the limits. Materials should match the house and neighbouring fences.",
                  "Apartment plots may not be fenced. Gates must not open onto the road. Driveways 3.5–5 m wide."),
                 ('Saue Municipality<span class="cell-src"><a href="https://www.sauevald.ee/sites/default/files/documents/2024-02/2021.06.28%20Saue%20valla%20u%CC%88ldplaneeringu%20seletuskiri_kehtestatud.pdf" target="_blank" rel="noopener">Saue general plan</a></span>',
                  "Generally up to 1.5 m in built-up areas, up to 2 m in sparsely populated areas.",
                  "Opaque fences of any material are generally not allowed. The exceptions are fences around industrial areas and noise or safety barriers by traffic areas.",
                  "Generally at least 2 m from the road surface edge. No fences outside the plot. Generally no fences on town-centre land."),
                 ('Saku Municipality<span class="cell-src"><a href="https://sakuvald.ee/wp-content/uploads/2025/10/Saku_YP_Seletuskiri.pdf" target="_blank" rel="noopener">Saku general plan</a></span>',
                  "Up to 1.5 m above ground on family and terraced-house land. Up to 2 m in sparsely populated areas.",
                  "At least 25% transparent; on family and terraced-house land this does not apply to hedges. Solid fences only where justified against noise or dust.",
                  "Fences are generally not planned on apartment-block land. In wildlife-crossing restriction zones a fence must not block animal movement."),
                 ('Kiili Municipality<span class="cell-src"><a href="https://www.kiilivald.ee/sites/default/files/documents/2026-06/Kiili_YP_seletuskiri_16_05_13.pdf" target="_blank" rel="noopener">Kiili general plan</a></span>',
                  "Up to 1.4 m on the street side. Mesh up to 1.6 m between plots.",
                  "A partly transparent timber fence on the street side. Solid plank fences are banned except around industrial buildings for noise and security.",
                  "On a large plot the fence may enclose just the built-up area."),
                 ('Jõelähtme: Loo, Liivamäe, northern Saha and Nehatu<span class="cell-src"><a href="https://joelahtme.ee/sites/default/files/documents/2026-06/Loo%20aleviku%2C%20Liivam%C3%A4e%20k%C3%BCla%2C%20Saha%20k%C3%BCla%20ja%20Nehatu%20k%C3%BCla%20%C3%BCldpaleneeringu%20seletuskiri.pdf" target="_blank" rel="noopener">Loo, Liivamäe, Saha and Nehatu general plan</a></span>',
                  "In Loo, Liivamäe and northern Saha, up to 1.2 m on detached and semi-detached house land.",
                  "At least 10% transparent.",
                  "For terraced houses the fence is set in the detailed plan. No fences on family-house land in Nehatu village. These are general-plan conditions for preparing detailed plans."),
                 ('Maardu<span class="cell-src"><a href="https://maardu.ee/sites/default/files/documents/2026-03/Maardu_linna_YP_Seletuskiri.pdf" target="_blank" rel="noopener">Maardu general plan</a></span>',
                  "Street fence up to 1.5 m in low-rise housing areas.",
                  "At least 25% transparent. Fences between plots must be see-through.",
                  "Neighbours agree the height and material of the fence between their plots."),
                 ('Keila<span class="cell-src"><a href="https://planeering.keila.ee/maakasutus" target="_blank" rel="noopener">Keila general plan</a></span>',
                  "Generally up to 1.5 m on residential land. About 1.4 m in the historic centre.",
                  "At least 25% transparent per running metre. No opaque wall over 1.5 m on the street side. A hedge may be taller.",
                  "Fences between plots by neighbours' agreement, and over 1.5 m only with that agreement. No fences outside the plot or around apartment blocks unless a detailed plan allows. On a listed monument and in its protection zone, agree the fence with the National Heritage Board."),
                 ('Tallinn, Nõmme<span class="cell-src"><a href="https://www.tallinn.ee/et/media/311168" target="_blank" rel="noopener">Nõmme district general plan</a></span>',
                  "Up to 1.5 m, following neighbouring fences.",
                  "Generally a sparse, see-through timber picket fence or mesh combined with a hedge. Mesh is fine between plots. Hedges generally up to 1.5 m.",
                  "No fences inside a plot. Special designs need written consent from the Urban Planning Department or the district architect and the neighbour. On a corner plot, consider a setback or a more transparent fence."),
                 ('Tallinn, milieu-value areas<span class="cell-src"><a href="https://www.tallinn.ee/et/ehitus/piirdeaiad-hoovialad-ja-haljastus" target="_blank" rel="noopener">Tallinn, fences in milieu-value areas</a>, 11.04.2024</span>',
                  "Street fences generally 1.2–1.5 m, close-boarded fences 1.5–1.8 m, following neighbouring plots.",
                  "Mesh and welded-panel fences are not considered suitable. As an exception, mesh may be considered between plots, never on the street side, if a dense hedge or climbers hide it completely.",
                  "Whether mesh can be used, and how much, is decided case by case. The fence and gates must suit the historic character of the area."),
             ],
             "note": "Checked on 27 September 2026 against the plans and municipal websites. The table shows general rules: if your plot has a valid detailed plan, that plan applies. In Rae we checked only the northern area general plan (from the Tallinn border to the Kurna stream and the Tallinn ring road, including Peetri). For other municipalities and Tallinn districts, see their plans."},
            {"type": "sections", "tag": "Step by step", "h": "How to find and read the rules for your plot",
             "intro": "The table gives the overall picture; your plot's plan gives the final answer.",
             "items": [
                 ("1. Find the right document", [
                     "Find out whether your plot has a valid detailed plan: it will be in the municipality's or city's planning register or map application, and in Tallinn in the Tallinn planning register. If there is none, the general plan applies, with any thematic plan that refines it.",
                     "In Tallinn, check on the city's map whether the plot lies in a milieu-value area. In these areas the city recommends starting from the fence in the house's original design, usually kept in the Urban Planning Department's archive."]),
                 ("2. Look in the right places", [
                     "Fence rules usually sit in the part of the explanatory report on architecture, boundaries or landscaping. Plans are in Estonian, so look for “piirdeaed” (fence), “piire” (boundary structure), “läbipaistvus” (transparency) and “kõrgus” (height). The drawing may also show the building line and a setback from the street."]),
                 ("3. Tell the street fence from the boundary fence", [
                     'Many plans set different rules for the street side and for the boundary between plots. Kiili allows a partly transparent timber fence up to 1.4 m on the street side but mesh up to 1.6 m between plots, and in Keila and Maardu the fence between plots depends on the neighbours\' agreement. Our guide to a <a href="/en/boundary-fence-neighbour/">boundary fence with a neighbour</a> explains how to put that in writing.']),
                 ("4. If something is unclear, ask in writing", [
                     "Send the municipality's planning or building officer a short question with the address, planned height, material and a photo, and keep the reply. In Nõmme a special design needs written consent from the Urban Planning Department or the district architect and from the neighbour.",
                     "On a listed monument or in a heritage conservation area, building needs a National Heritage Board permit. In their protection zones the municipality agrees the notice with the Board, and if no notice is needed, the Board must be told at least 10 days ahead."]),
             ],
             "sources": ["ehs", "tallinn", "kiili", "keila", "maardu", "nomme", "muks"]},
            {"type": "sections", "tag": "Transparency", "h": "How transparency is judged",
             "items": [
                 ("What the percentage means", [
                     "Transparency is the share of the fence's visible surface that is open. In Saku, Keila and Maardu it must be at least 25%, and in Loo, Liivamäe and northern Saha at least 10%. Keila's plan measures it per running metre."]),
                 ("How to work it out for a picket fence", [
                     "Divide the gap between pickets by the picket width plus the gap. With 8 cm pickets and a 4 cm gap, transparency is 4 / 12, about 33%. With a 2 cm gap it drops to 20% and no longer meets a 25% rule. Posts and rails reduce the open area slightly, so leave some margin.",
                     "Nõmme's general plan recommends a gap of 1/3 to 1/2 of the picket width so the fence does not read as a solid wall. A gap of one third of the picket width gives about 25%."]),
                 ("Double-sided picket fences", [
                     "A double-sided, staggered picket fence lets wind through but looks almost solid from straight on. Nõmme allows it as a special solution along busy streets. Where your plan requires transparency, ask the municipality before ordering one."]),
                 ("Privacy from a hedge", [
                     "Where the fence must be see-through, a hedge gives privacy. Saku's transparency rule on family and terraced-house land does not apply to hedges, and in Keila a hedge may exceed the fence figures. Nõmme, however, generally limits hedges to 1.5 m."]),
             ],
             "sources": ["saku", "keila", "maardu", "loo", "nomme"]},
            {"type": "sections", "tag": "Slopes", "h": "Fence height on a sloping plot",
             "items": [
                 ("What the regulation says", [
                     "On sloping ground, height is measured from the arithmetic mean of the lowest and highest ground level immediately around the fence. If the ground at one end of a section is 40 cm higher than at the other, height is measured from the average level, 20 cm above the ground at the lower end."]),
                 ("Stepped or raked", [
                     "Rigid panels are usually stepped on a slope, which leaves a triangular gap under the downhill end of each step, where the fence stands taller. Roll mesh, timber and picket fences can also be raked, so the top follows the ground and the height stays even.",
                     "We recommend keeping every section within the permitted height, measured from the ground beside it. That way there is no argument even if someone measures the fence at its least favourable point."]),
                 ("Posts, plinths and gates", [
                     "Post tops, caps and a plinth, where it is part of the fence, all count towards the height. The gate and gate posts belong to the same fence, so keep them within the permitted height too, unless the plan says otherwise.",
                     "If the ground level differs on your side and your neighbour's, measure from both sides. Discuss a fence on top of a retaining wall with the municipality first, as the total height seen from the neighbour's side may exceed the limit."]),
             ],
             "sources": ["tehn"]},
            {"type": "sections", "tag": "Fence types", "h": "Which fence fits the rules",
             "intro": 'In Kiili the street side must be a partly transparent timber fence, and in Nõmme it is generally sparse timber pickets or mesh with a hedge, so metal and panel fences suit those places better between plots. Prices are from our <a href="/en/prices/">price guide</a> and include materials and standard installation.',
             "items": [
                 ("3D and 2D mesh panels", [
                     'A mesh panel fence is see-through and fits most plans in the table; choose a panel height that keeps the whole fence, gap and post tops included, within the limit. Welded panels are not considered suitable in Tallinn\'s milieu-value areas. A <a href="/en/fences/mesh/">3D mesh panel fence</a> costs €35–60/m and the stiffer 2D panel €50–85/m.']),
                 ("Roll mesh / chain-link", [
                     "Mesh is see-through and the least expensive option at €25–45/m. It works well on side and rear boundaries, because several plans, such as Kiili's and Nõmme's, allow mesh between plots. On the street side, combine it with a hedge where the plan expects one."]),
                 ("Steel picket fence", [
                     'How see-through a <a href="/en/fences/steel-picket/">steel picket fence</a> is depends on the gap, which you choose. A single-sided layout with a sensible gap usually meets 25% easily; a double-sided staggered layout does not always. It costs €85–155/m.']),
                 ("Welded metal-bar fence", [
                     'A welded <a href="/en/fences/metal-bar/">metal-bar fence</a> stays see-through on the street side, so it suits plans that require an open fence when you want a sturdy, representative look. It costs €140–280/m; in a milieu-value area its design must also suit the historic surroundings.']),
                 ("Timber fence", [
                     "A partly transparent timber fence is the preferred option in several plans: Harku and Kiili name it directly, and Viimsi recommends timber fences for timber houses. A solid close-boarded fence is allowed in Harku, Viimsi and Kiili only as an exception, such as a noise barrier. A timber fence costs €90–160/m."]),
                 ("Profiled-sheet fence", [
                     'Profiled sheet is opaque, so it does not work where the plan requires transparency. Saue generally allows no opaque fences, and northern Rae allows a solid fence up to 1.8 m only as a noise barrier. Before ordering a <a href="/en/privacy-fence/">privacy fence</a>, get the municipality\'s confirmation. It costs €70–135/m.']),
             ],
             "sources": ["kiili", "nomme", "harku_tp", "viimsi", "saue", "rae", "tallinn"]},
            {"type": "cards", "tag": "Our advice", "h": "What we recommend", "cols": 2,
             "items": [
                 ("Check the plan before the material", "Choose the fence once you know the permitted height and the transparency rule. That way you do not pay for a fence that has to be rebuilt."),
                 ("Leave some height in reserve", "We recommend staying a few centimetres below the permitted height. Ground moves with frost, caps add height, and a small margin avoids arguments."),
                 ("Privacy from a hedge", "Where the plan requires transparency, a see-through fence with a hedge planted behind it works well. The fence stays within the rules and the hedge gives privacy as it grows."),
                 ("Road edge and snow", 'If your plot borders a road, check the distance from the road surface in the table and read our guide to <a href="/en/fence-near-road-and-utilities/">fences near roads and utilities</a>. A fence right at the road edge gets in the way of snow clearing.'),
             ]},
            {"type": "cards", "tag": "Common problems", "h": "What often goes wrong", "cols": 2,
             "items": [
                 ("Copying the neighbour's fence", "An old fence may predate the current plan or rest on a special agreement. A new fence must meet today's rules."),
                 ("A solid fence where transparency is required", "A profiled-sheet or plank fence goes up where the plan requires transparency, and it may have to be rebuilt."),
                 ("Measuring only the panel", "Caps, a plinth and the gap underneath are left out, and the finished fence ends up taller than allowed."),
                 ("The gate opens onto the street", "A leaf opening towards the street gets in the way of traffic and snow clearing. Check whether your plan allows it at all."),
             ]},
        ],
        "faq": [
            ("How tall can a house fence be in Harju County?", "Up to 1.5 m in most of the plans we checked. Kiili allows 1.4 m on the street side, and Loo, Liivamäe and northern Saha 1.2 m. Saue and Saku allow up to 2 m in sparsely populated areas."),
            ("What does 25% transparency mean?", "At least a quarter of the fence's visible surface must be see-through, and Keila measures this per running metre. On a picket fence, a gap of about one third of the picket width achieves it. 3D mesh panels and metal-bar fences are see-through; a solid profiled-sheet or plank fence is not."),
            ("Can I build a solid fence around a house?", "Generally not. In Viimsi, Harku and Kiili a solid plank fence is allowed only as an exception, for example as a noise barrier or around an industrial site, and in Saue the same restriction covers any opaque fence. In northern Rae a solid fence up to 1.8 m is allowed as a noise barrier where noise exceeds the limits."),
            ("How is fence height measured on a slope?", "Unless the plan says otherwise, height is measured from the ground immediately around the fence to its highest point, post tops included. On a slope, the mean of the lowest and highest ground level is used. We recommend keeping each section within the limit, measured beside it."),
            ("My neighbour's fence is taller. Can mine be the same height?", "Not necessarily. Your neighbour's fence may predate the current plan or rest on a special agreement, while a new fence must meet today's rules. Check your plot's plan or ask the municipality."),
            ("What if my municipality is not in the table?", "Check your plot's detailed plan and the municipality's general plan, or ask the planning officer for a written answer. At the site visit we help you take the rules into account when choosing the fence."),
        ],
        "links_keys": ["permit_guide", "privacy_fence", "neighbour"],
        "links_extra": [("/en/fences/metal-bar/", "Welded metal-bar fences", "A see-through street-side fence.")],
        "cta": ("We choose a fence that fits the plan", "At the site visit we account for the permitted height, transparency and the road edge, and suggest a suitable solution.", "/en/#form", "Get a quote"),
    },
}
