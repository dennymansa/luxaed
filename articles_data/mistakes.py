# Article: mistakes (/aia-ehituse-vead/, /ru/oshibki-pri-ustanovke-zabora/, /en/fence-building-mistakes/)
#
# All legal facts come from FACTS.md (keys aos, maaamet, lisa1, ehs, kvoond, harku, saku).
# Extra wording checked in the primary sources on 27.09.2026 (existing source keys, so no NEW_SRC):
#
# ehs, § 77(2) p 5 (RT API 111072026032): "töötada löökmehhanismidega, tasandada pinnast, teha mullatöid
#   sügavamal kui 0,3 meetrit, küntaval maal sügavamal kui 0,45 meetrit, ning ladustada ja teisaldada
#   raskusi" in "õhu- ja maakaabelliinide kaitsevööndites".
# ehs, § 78(2) p 5: "töötada löökmehhanismidega, tihendada või tasandada pinnast, rajada transpordivahenditele
#   ja mehhanismidele läbisõidukohti ning teha mullatöid sügavamal kui 0,3 meetrit" in "pinnases paikneva
#   sideehitise kaitsevööndis".
# ehs, § 72(2): "Kinnisasja omanik peab võimaldama paigaldada tee kaitsevööndisse tee korrashoiuks ajutisi
#   lumetõkkeid, rajada lumevalle ja kraave tuisklume tõkestamiseks ning paisata lund väljapoole teed, kui
#   nimetatud tegevus ei takista juurdepääsu kinnisasjale."
# aos, § 148(3) (RT API 128012026007): "Naaberkinnisasja omanik võib nõuda ehitajalt oma kinnisasja piiridesse
#   ulatuva ehitise osa kõrvaldamist, kui ehitaja on pahauskne või kui kinnisasja omanik enne ehitamise algust
#   või hiljemalt ajal, mil selle osa kõrvaldamine ei olnud seotud ülemääraste kulutustega, sellele vastu vaidles."
# harku (Harku vald, rajatised): "Kui kinnistu piir jääb lähemale kui 2 meetrit teekatte servast, tuleb tagada
#   lume koristamise võimalus" and "piirdeaed peab asuma vähemalt 2 meetri kaugusel teekatte servast."
# harku: "Ehitusteatisel puudub riigilõiv."
#
# Note for the build: the consolidated EhS (111072026032) and AOS (128012026007) texts are valid until
# 30.09.2026 and a new wording starts 01.10.2026. The ?leiaKehtiv links follow it automatically, but the
# cited paragraphs should be re-checked once the new wording is published.

NEW_SRC = {}

ARTICLE = {
    "et": {
        "title": "Aia ehitamise vead: 10 viga ja kuidas neid vältida | LuxAed",
        "desc": "Aed naabri maal, esitamata ehitusteatis, nõrgad postid ja unustatud automaatikakaabel. Kümme levinud viga aia ehitamisel ja kuidas neid enne tööd vältida.",
        "short": "Aia ehitamise vead",
        "image": "luxaed-g7",
        "kicker": "Juhend · enne tellimist",
        "h1": "Aia ehitamise vead<br><em>ja kuidas neid vältida</em>",
        "lead": "Enamik aia probleeme saab alguse enne esimest posti: planeerimisel, piiri määramisel ja postide valikul. Allpool on kümme levinud viga koos selgitusega, mis juhtub, miks ja kuidas seda vältida.",
        "direct": ("Kõige kallimad vead on vale piir, esitamata ehitusteatis ja nõrgad postid: nende parandamiseks tuleb aed osaliselt uuesti ehitada.",
                   "Kontrollige enne tellimist piirimärke, planeeringu nõudeid ja trasse ning laske postid valida pinnase ja tuule järgi. Väravad ja automaatikakaabel planeerige koos aiajoonega, mitte pärast seda."),
        "blocks": [
            {"type": "sections", "tag": "Enne tööd", "h": "Viis viga enne esimest posti",
             "intro": "Need vead tekivad planeerimisel ja neid on hiljem kõige raskem parandada.",
             "items": [
                 ("1. Aed jääb naabri maale", [
                     "Piirimärgid on kadunud või rohtu kasvanud ning aiajoon pannakse paika vana aia või silma järgi. Mõnesentimeetrine viga jääb märkamata, kuni maja müüakse, naaber hakkab ehitama või tekib vaidlus.",
                     "Asjaõigusseaduse järgi peab naaber heauskselt üle piiri ehitatud aeda taluma, kuid võib nõuda selle alla jääva maa omandamist või perioodilist hüvitist. Kui ehitaja oli pahauskne või naaber vaidles vastu enne ehitamist või hiljemalt ajal, mil eemaldamine ei olnud veel seotud ülemääraste kuludega, võib ta nõuda aia eemaldamist oma maalt. See tähendab postide väljakaevamist ja uuesti paigaldamist.",
                     "Otsige piirimärgid üles ja pildistage need enne tööd. Kadunud märke tohib taastada ainult litsentsiga maamõõtja; naabrid kutsutakse kohale ja kulud jagatakse võrdselt, kui ei lepita kokku teisiti. Lähemalt juhendis <a href=\"/aed-naabri-piiril/\">aed naabri piiril</a>.",
                 ]),
                 ("2. Ehitusteatis jääb esitamata", [
                     "Alates 01.08.2026 kehtiva ehitusseadustiku lisa 1 järgi vajab aed või värav, mille ehitamisel kaevatakse sügavamale kui 30 cm, ehitusteatist ja ehitusprojekti. Betoneeritud postide puhul kaevatakse tavaliselt sügavamale, seega arvestage teatisega.",
                     "Teatis esitatakse ehitisregistris vähemalt 10 päeva enne tööde algust; kui vald selle aja jooksul lisakontrolli vajadusest ei teata, võib alustada. Esitage see enne materjali tellimist. Kui tööd on juba ilma teatiseta alanud, rääkige enne jätkamist valla ehitusspetsialistiga.",
                     "LuxAed annab aia tehnilised andmed; kes koostab projekti ja esitab teatise, lepitakse kokku eraldi. Täpsemalt <a href=\"/aia-ehitusteatis/\">ehitusteatise juhendis</a>.",
                 ]),
                 ("3. Planeeringu nõue selgub liiga hilja", [
                     "Aed peab vastama detailplaneeringule, selle puudumisel üldplaneeringule, ja planeering võib määrata aia lubatud kõrguse, läbipaistvuse ja materjali. Harku vallas ei tohi eramu võrkaed ega osaliselt läbipaistev puitaed olla kõrgem kui 1,5 m ja läbipaistmatud plankaiad on keelatud, välja arvatud müratõkkena või tööstusala ümber. Saku vallas peab pere- ja ridaelamumaa aed olema vähemalt 25% läbipaistev.",
                     "Kinnise profiilplekk-aia võib alal, kus nõutakse läbipaistvust, tulla ümber teha, ja siis maksate kaks korda. Vaadake detailplaneering üle enne aiatüübi valimist; omavalitsuste nõuded on koondatud juhendisse <a href=\"/aia-korgus-harjumaal/\">aia kõrgus Harjumaal</a>.",
                 ]),
                 ("4. Puur tabab kaablit", [
                     "Puur või postirammija ei tee vahet kivil ja kaablil ning katkenud elektri- või sidekaabel tähendab ohtu, tööde peatumist ja remondiarvet.",
                     "Ehitusseadustiku järgi on elektri- ja sidekaablite kaitsevööndis keelatud teha mullatöid sügavamal kui 0,3 m ja töötada löökmehhanismidega, näiteks postirammijaga, kui kaabli omanik pole selleks nõusolekut andnud. Maakaabli kaitsevöönd on üldjuhul 1 m kummalegi poole kaablit ja võrgu omanik annab asukoha andmed tasuta.",
                     "Küsige trasside asukohad enne puurimist ja märkige need krundil ära, ka kaablid, mille olete ise valgustuse või väravaautomaatika jaoks maasse pannud. LuxAedi tingimuste järgi ei vastuta me varjatud tehnovõrkude kahjustuste eest, millest klient ei teavitanud. Lähemalt juhendis <a href=\"/aed-tee-ja-trasside-lahedal/\">aed tee ääres ja trasside lähedal</a>.",
                 ]),
                 ("5. Tee äär jääb arvestamata", [
                     "Tee kaitsevööndis peab kinnistu omanik võimaldama tee korrashoiuks lume paiskamist teelt välja, seega saab tänavaäärne aed lumesahalt lund, jääd ja kruusa.",
                     "Harku vallas peab aed asuma teekatte servast vähemalt 2 m kaugusel, kui krundi piir jääb teele lähemale. Ka mujal hoiab tagasiaste aia terve ning nurgakrundil ei tohiks kõrge kinnine aed varjata autojuhi vaadet ristmikule. Kõverdunud postid ja sektsioonid tuleb sirgeks seada või välja vahetada.",
                 ]),
             ],
             "sources": ["aos", "maaamet", "lisa1", "ehs", "kvoond", "harku", "saku"]},
            {"type": "sections", "tag": "Konstruktsioon", "h": "Viis viga postides, väravates ja hinnas",
             "items": [
                 ("6. Kinnisel aial on nõrgad postid", [
                     "Kinnine profiilplekk-aed, tihe puitaed või tihe metall-lippaed on tuulele nagu puri. Kui postid on valitud nagu võrkaiale, hakkavad need tormi järel kalduma ja kinnitused lõdvenevad.",
                     "Postid, nende vahe ja alus valitakse aia kõrguse, pinnase ja tuule järgi; lagedal põllul või mere ääres on tuul tugevam kui majade vahel. Küsige pakkumises posti mõõtu ja postide vahet ning võrrelge. Tugevam post maksab alguses vähe võrreldes sellega, mida maksab hiljem kaldu postide vahetus.",
                 ]),
                 ("7. Külmakergega ei arvestata", [
                     "Märg savine pinnas paisub külmaga ja tõstab poste, mille alus või sügavus pinnasega ei sobi. Kevadel ei vaju post enam tagasi ja kalle ilmneb tavaliselt pärast esimest talve.",
                     "Sügavus ja alus valitakse pinnase järgi, sest savi, liiv, täitepinnas ja kõrge põhjavesi käituvad erinevalt, ning hea paigaldaja põhjendab oma valikut. Mõne posti sirgeks seadmine või uuesti betoneerimine on palju soodsam kui uus aed: remont ja diagnostika alates 90 € (väljasõit ja esmane diagnostika), postid ja töö lisanduvad. Lugege, <a href=\"/aia-remont/viltu-aed/\">kuidas viltu aeda remontida</a>.",
                 ]),
                 ("8. Väravale pole ruumi", [
                     "Aiajoon pannakse paika enne, kui keegi väravale mõtleb. Konsoolse liugvärava tiib on avast pikem, sest sellel on vastukaaluosa, ja vajab aia kõrval vaba külgruumi; tiibvärava tiivad vajavad vaba liikumisala aasta läbi ja kaldega sissesõidul võivad need maad riivata.",
                     "Mõõtke avause laius, külgruum ja kalle enne postide paigaldamist, sest hiljem tähendab ruumi tegemine sageli sektsioonide ja postide ümbertõstmist. Valida aitab võrdlus <a href=\"/liugvarav-voi-tiibvarav/\">liugvärav või tiibvärav</a>.",
                 ]),
                 ("9. Automaatikakaabel jääb panemata", [
                     "Paljud plaanivad automaatväravat hilisemaks. Kui ajami ja fotoelementide kaablite jaoks ei pandud kaitsetoru maasse, tuleb hiljem kaevata läbi sissesõidu, muru või sillutise.",
                     "Pange kaitsetoru maasse aia- ja väravapostide paigaldamisel, jätke otsad kättesaadavaks ja mõelge läbi, kust tuleb toide. Meie hinnatabelis maksab automaatika olemasolevale väravale 500–1 250 €, kui värava konstruktsioon ja elektrivalmidus on sobivad; ilma toru ja toiteta lisanduvad kaevamine ja kaablitööd. Lähemalt lehel <a href=\"/varavad/\">automaatväravate paigaldus</a>.",
                 ]),
                 ("10. Võrreldakse ainult jooksva meetri hinda", [
                     "Jooksva meetri hind sobib esimeseks võrdluseks, kuid lõpphinna määravad väravad, nurgad, kalle, pinnas, vana aia eemaldus ja äravedu. Pakkumine, kus neid ridu pole, tundub odavam.",
                     "Meie hinnatabeli järgi maksab 40 m 3D paneelaeda 1 400–2 400 €, kuid koos automaatikaga liugvärava ja jalgväravaga maksab kogu projekt 4 050–6 350 € ja üle poole sellest moodustavad väravad. Küsige kirjalikku pakkumist, kus iga töö on eraldi real, ja võrrelge rida-realt; hinnavahemikud leiate lehelt <a href=\"/hinnad/\">aia ja värava hinnad</a>.",
                 ]),
             ]},
            {"type": "text", "tag": "Seadus", "h": "Mida veel seadusest teada",
             "paras": [
                 "Vana aia asendamine ei ole alati remont. Aia puhul, mille ehitamisel kaevatakse sügavamale kui 30 cm, ei vaja teatist ümberehitamine ega üksiku osa vahetamine samaväärse vastu, kuid lammutamine vajab. Kui vana aed lammutatakse, et ehitada asemele sisuliselt uus aed, on tegemist lammutamise ja uue aia ehitamisega; sisuliselt sarnase aia taastamist võib käsitleda ümberehitamisena. Vald võib põhjendatud juhul nõuda teatist ka ehitise kohta, mida lisas 1 ei ole.",
                 "Ehitusteatise alusel võib ehitada neli aastat, vald võib menetlusse kaasata naaberkinnistu omaniku ja Harku valla andmetel teatisel riigilõivu ei ole. Kaitsevööndiga ehitise omanik ei tohi nõusolekust põhjendamatult keelduda ega selle eest tasu võtta, kõrgepinge õhuliini kaitsevööndis on traattarad ja metallaiad keelatud ning tänava kaitsevöönd ulatub äärmise sõiduraja välisservast 10 meetrini.",
             ],
             "sources": ["lisa1", "ehs", "harku"]},
            {"type": "table", "tag": "Kontroll-leht", "h": "Millal mida kontrollida",
             "headers": ("Etapp", "Mida kontrollida", "Kes aitab"),
             "rows": [
                 ("Enne pakkumist", "Piirimärgid, detailplaneering, trassid, väravate asukoht", "Teie, vald, võrkude omanikud"),
                 ("Mõõdistusel", "Aiajoon, kalle, pinnas, tee äär, värava külgruum, kaabli teekond", "Paigaldaja"),
                 ("Pakkumises", "Postid ja nende vahe, alused, väravad, kaitsetoru, vana aia eemaldus, maksegraafik", "Teie ja paigaldaja"),
                 ("Enne kaevamist", "Teatis esitatud, trassid märgitud, naabriga kokku lepitud", "Teie või kokkulepitud esitaja"),
                 ("Üleandmisel", "Aiajoon piirimärkide suhtes, postid loodis, väravad liiguvad vabalt", "Teie ja paigaldaja"),
                 ("Pärast esimest talve", "Postide asend, väravate liikumine, kinnitused", "Teie, vajadusel remont"),
             ],
             "note": "See on meie praktiline kontroll-leht; õigusnõuded ja allikad on ülal."},
            {"type": "cards", "tag": "Meie soovitus", "h": "Mis on tegelikult oluline", "cols": 2,
             "items": [
                 ("Piir ja postid enne kõike", "Materjali saab hiljem vahetada, valet aiajoont ja nõrku aluseid mitte. Kui eelarve on piiratud, valige pigem lihtsam aiatüüp kui nõrgemad postid."),
                 ("Üks mõõdistus hoiab ära mitu viga", "Kontrollime korraga piiri, kallet, pinnast, väravate ruumi ja tee äärt."),
                 ("Väravad ja kaabel koos aiaga", "Otsustage värava tüüp, külgruum ja kaitsetoru enne, kui aiajoon paika pannakse."),
                 ("Paberid enne materjali", "Esitage teatis ja leppige naabriga kokku enne tellimist, et paneelid ei jääks ootama."),
             ]},
            {"type": "cards", "tag": "Levinud probleemid", "h": "Märgid, et midagi läks valesti", "cols": 3,
             "items": [
                 ("Post liigub käega lükates", "Alus on lahti või post mädanenud. Remontige varakult, enne kui vahetada tuleb rohkem."),
                 ("Värav hakkab hõõruma", "Post on kaldu või alus vajunud; liugvärava puhul vaadake üle ka rullikud ja kandurid."),
                 ("Aed on kevadel viltu", "Tüüpiline külmakerke märk. Üksikud postid saab sageli sirgeks seada ja uuesti betoneerida."),
                 ("Aia jalamil on lumi ja kivid", "Aed on teele liiga lähedal. Parandage kõverdunud sektsioonid enne järgmist talve."),
                 ("Paneeli alla tekib vahe", "Maa on kaldu või vajunud. Vahe sulgeb aluslaud või astmeline paigaldus."),
                 ("Naaber küsib piiri kohta", "Laske litsentsiga maamõõtjal piir üle kontrollida enne, kui sellest saab vaidlus."),
             ]},
        ],
        "faq": [
            ("Mis on kõige kallim viga aia ehitamisel?", "Tavaliselt vale piir või nõrgad postid, sest siis tuleb aed osaliselt uuesti ehitada. Mõlemat saab vältida enne tööd: otsige üles piirimärgid ja laske postid valida pinnase, kõrguse ja tuule järgi."),
            ("Kas piisab jooksva meetri hinna võrdlemisest?", "Ei. Lõpphinna määravad ka väravad, nurgad, kalle, pinnas, vana aia eemaldus ja äravedu. Võrrelge kirjalikke pakkumisi rida-realt."),
            ("Kas automaatikakaabel tuleb planeerida juba aia ehitusel?", "Jah, kui automaatvärav võib kunagi tulla. Kaitsetoru on aia ehitusel lihtne maasse panna, hiljem tuleb kaevata läbi sissesõidu või muru."),
            ("Kuidas vältida aia viltu vajumist?", "Valige postide sügavus ja alus pinnase ning aia kõrguse järgi ja kasutage kinnise aia puhul tugevamaid poste. Kui aed juba vajub, saab selle sageli remontida ilma kogu aeda vahetamata."),
            ("Kes vastutab, kui puur tabab maa-alust kaablit?", "Vastutus sõltub sellest, kas kaabli asukoht oli teada ja kas sellest paigaldajale teatati. LuxAedi tingimuste järgi ei vastuta me varjatud tehnovõrkude kahjustuste eest, millest klient ei teavitanud. Seepärast küsige asukohad enne tööd võrkude omanikelt."),
            ("Mida kontrollida pärast esimest talve?", "Vaadake aiajoont küljelt, lükake poste käega ja proovige, kas väravad liiguvad vabalt. Kui mõni post on kaldu, on mõistlik see kevadel sirgeks seada, enne kui kalle suureneb."),
        ],
        "links_keys": ["permit_guide", "contractor", "neighbour"],
        "links_extra": [("/aia-remont/viltu-aed/", "Aed on viltu või post logiseb?", "Postide sirgeks seadmine ja vahetus.")],
        "cta": ("Planeerime aia korrektselt", "Tasuta mõõdistusel kontrollime piiri, pinnast, väravate ruumi ja tee äärt ning anname kirjaliku pakkumise.", "/#form", "Küsi pakkumist"),
    },
    "ru": {
        "title": "Ошибки при установке забора и как их избежать | LuxAed",
        "desc": "Забор на участке соседа, неподанное уведомление, слабые столбы, нет трубы для кабеля. 10 ошибок при установке забора и как их избежать до начала работ.",
        "short": "Ошибки при установке забора",
        "image": "luxaed-g7",
        "kicker": "Руководство · перед заказом",
        "h1": "Ошибки при установке<br><em>забора и как их избежать</em>",
        "lead": "Большинство проблем с забором начинается до первого столба: при планировании, поиске границы и выборе столбов. Ниже десять частых ошибок и объяснение, что происходит, почему и как этого избежать.",
        "direct": ("Дороже всего обходятся неверная граница, неподанное уведомление о строительстве и слабые столбы: их исправляют только переделкой забора.",
                   "До заказа проверьте межевые знаки, требования планировки и сети, а столбы подбирайте по грунту и ветру. Ворота и кабель автоматики планируйте вместе с линией забора, а не после неё."),
        "blocks": [
            {"type": "sections", "tag": "До работ", "h": "Пять ошибок до первого столба",
             "intro": "Эти ошибки возникают при планировании, и потом их труднее всего исправить.",
             "items": [
                 ("1. Забор оказывается на земле соседа", [
                     "Межевые знаки потерялись или заросли, и линию забора ставят по старому забору или на глаз. Ошибка в несколько сантиметров остаётся незаметной, пока дом не продают, сосед не начинает стройку или не возникает спор.",
                     "По закону о вещном праве (Asjaõigusseadus) сосед должен терпеть забор, добросовестно построенный с заходом на его участок, но может потребовать выкупить землю под ним или платить периодическую компенсацию. Если строитель действовал недобросовестно или сосед возражал до начала работ или позже, пока убрать эту часть можно было без чрезмерных затрат, он может потребовать убрать забор со своей земли. Тогда столбы придётся выкопать и поставить заново.",
                     "Найдите межевые знаки и сфотографируйте их до работ. Восстанавливать пропавшие знаки может только землемер с лицензией; соседей приглашают, а расходы делят поровну, если не договорились иначе. Подробнее в статье <a href=\"/ru/zabor-s-sosedom/\">забор между соседями</a>.",
                 ]),
                 ("2. Не подали уведомление о строительстве", [
                     "По приложению 1 строительного кодекса, действующему с 01.08.2026, для забора или ворот, при строительстве которых копают глубже 30 см, нужны уведомление о строительстве (ehitusteatis) и проект. При бетонировании столбов обычно копают глубже, так что рассчитывайте на уведомление.",
                     "Уведомление подают через строительный регистр не позже чем за 10 дней до начала работ; если волость за это время не сообщит о дополнительной проверке, можно начинать. Подайте его до заказа материалов, а если работы уже начались без уведомления, поговорите со строительным специалистом волости, прежде чем продолжать.",
                     "LuxAed предоставляет технические данные забора, а кто готовит проект и подаёт уведомление, договариваемся отдельно. Подробнее в статье <a href=\"/ru/razreshenie-na-zabor/\">нужно ли разрешение на забор</a>.",
                 ]),
                 ("3. Требование планировки всплыло слишком поздно", [
                     "Забор должен соответствовать детальной планировке, а если её нет, общей, и планировка может задавать допустимую высоту, прозрачность и материал. В волости Харку сетчатый или частично прозрачный деревянный забор у частного дома может быть не выше 1,5 м, а глухие дощатые заборы запрещены, кроме шумовых барьеров и заборов вокруг промышленных территорий. В волости Саку забор на земле частных и рядных домов должен быть прозрачным не менее чем на 25%.",
                     "Глухой забор из профнастила там, где требуется прозрачность, возможно, придётся переделать, и тогда вы заплатите дважды. Проверьте детальную планировку до выбора типа забора; требования волостей собраны в статье <a href=\"/ru/vysota-zabora-v-harjumaa/\">высота забора в Харьюмаа</a>.",
                 ]),
                 ("4. Бур задевает кабель", [
                     "Бур или копёр не отличает камень от кабеля, а повреждённый электрический кабель или кабель связи означает опасность, остановку работ и счёт за ремонт.",
                     "По строительному кодексу в охранной зоне электрических кабелей и кабелей связи нельзя вести земляные работы глубже 0,3 м и работать ударными механизмами, например копром для забивки столбов, без согласия владельца кабеля. Охранная зона подземного кабеля обычно составляет 1 м в каждую сторону, а данные о расположении сетей владелец даёт бесплатно.",
                     "Узнайте расположение сетей до бурения и отметьте трассы на участке, включая кабели, которые прокладывали сами для освещения или автоматики ворот. По нашим условиям LuxAed не отвечает за повреждение скрытых коммуникаций, о которых заказчик не предупредил. Подробнее в статье <a href=\"/ru/zabor-u-dorogi-i-kommunikacij/\">забор у дороги и коммуникаций</a>.",
                 ]),
                 ("5. Не учли край дороги", [
                     "В охранной зоне дороги владелец участка обязан позволить отбрасывать снег за пределы дороги, поэтому забору у улицы достаются снег, лёд и гравий от снегоуборщика.",
                     "В волости Харку забор должен стоять не ближе 2 м от края дорожного покрытия, если граница участка ближе к дороге. И в других местах отступ бережёт забор, а на угловом участке высокий глухой забор лучше не ставить так, чтобы он закрывал водителям обзор перекрёстка. Погнутые столбы и секции приходится выпрямлять или менять.",
                 ]),
             ],
             "sources": ["aos", "maaamet", "lisa1", "ehs", "kvoond", "harku", "saku"]},
            {"type": "sections", "tag": "Конструкция", "h": "Пять ошибок в столбах, воротах и цене",
             "items": [
                 ("6. Слабые столбы у глухого забора", [
                     "Глухой забор из профнастила, плотный деревянный забор или плотный металлический штакетник работает как парус. Если столбы подобраны как для сетки, после бури они начинают крениться, а крепления расшатываются.",
                     "Столбы, шаг и основание подбирают по высоте забора, грунту и ветру; в открытом поле или у моря ветер сильнее, чем между домами. Спросите в предложении сечение и шаг столбов и сравните. Более мощный столб вначале стоит немного дороже, но это гораздо дешевле, чем потом менять покосившиеся столбы.",
                 ]),
                 ("7. Не учли морозное пучение", [
                     "Влажный глинистый грунт при морозе расширяется и выталкивает столбы, у которых основание или глубина не подходят к грунту. Весной столб не возвращается на место, и крен обычно заметен после первой зимы.",
                     "Глубину и основание выбирают по грунту, ведь глина, песок, насыпной грунт и высокие грунтовые воды ведут себя по-разному, и хороший монтажник объясняет свой выбор. Выровнять или заново забетонировать несколько столбов гораздо дешевле нового забора: ремонт и диагностика от 90 € (выезд и первичная диагностика), столбы и работа отдельно. Читайте, <a href=\"/ru/remont-zaborov/pokosilsya-zabor/\">как ремонтируют покосившийся забор</a>.",
                 ]),
                 ("8. Нет места для ворот", [
                     "Линию забора размечают раньше, чем кто-то подумал о воротах. Полотно консольных откатных ворот длиннее проёма из-за противовесной части, и ему нужно свободное место сбоку, а створкам распашных ворот нужна свободная зона круглый год, и на въезде с уклоном они могут задевать землю.",
                     "Измерьте ширину проёма, место сбоку и уклон до установки столбов, потому что потом ради места приходится переносить секции и столбы. Выбрать поможет сравнение <a href=\"/ru/otkatnye-ili-raspashnye-vorota/\">откатных и распашных ворот</a>.",
                 ]),
                 ("9. Не заложили трубу под кабель автоматики", [
                     "Многие планируют автоматические ворота на потом. Если защитную трубу для кабелей привода и фотоэлементов не заложили, позже придётся копать через въезд, газон или брусчатку.",
                     "Заложите трубу при установке столбов забора и ворот, оставьте концы доступными и продумайте, откуда пойдёт питание. В нашем прайсе автоматика на существующие ворота стоит 500–1 250 €, если конструкция ворот и электроподготовка подходят; без трубы и питания добавляются земляные и кабельные работы. Подробнее на странице <a href=\"/ru/vorota-avtomatika/\">автоматические ворота с установкой</a>.",
                 ]),
                 ("10. Сравнивают только цену за метр", [
                     "Цена за погонный метр удобна для первого сравнения, но итог определяют ворота, углы, уклон, грунт, демонтаж старого забора и вывоз. Предложение без этих строк кажется дешевле.",
                     "По нашему прайсу 40 м забора из 3D-панелей стоят 1 400–2 400 €, а вместе с откатными воротами с автоматикой и калиткой весь проект стоит 4 050–6 350 €, и больше половины суммы приходится на ворота. Просите письменное предложение, где каждая работа указана отдельной строкой, и сравнивайте построчно; диапазоны цен есть на странице <a href=\"/ru/ceny/\">цены на заборы и ворота</a>.",
                 ]),
             ]},
            {"type": "text", "tag": "Закон", "h": "Что ещё важно знать из закона",
             "paras": [
                 "Замена старого забора не всегда считается ремонтом. Для забора, при строительстве которого копают глубже 30 см, уведомление не нужно при перестройке и при замене отдельной части равноценной, но нужно при сносе. Если старый забор сносят, чтобы поставить по существу новый, это снос и строительство нового; восстановление по существу такого же забора можно рассматривать как перестройку. В обоснованных случаях волость может потребовать уведомление и для сооружения, которого нет в приложении 1.",
                 "По уведомлению можно строить четыре года, волость может привлечь владельца соседнего участка, а по данным волости Харку госпошлины за уведомление нет. Владелец сооружения с охранной зоной не вправе без причины отказывать в согласии или брать за него плату, в охранной зоне высоковольтной воздушной линии запрещены проволочные и металлические заборы, а охранная зона улицы составляет 10 м от внешнего края крайней полосы.",
             ],
             "sources": ["lisa1", "ehs", "harku"]},
            {"type": "table", "tag": "Чек-лист", "h": "Что и когда проверять",
             "headers": ("Этап", "Что проверить", "Кто поможет"),
             "rows": [
                 ("До предложения", "Межевые знаки, детальная планировка, сети, место ворот", "Вы, волость, владельцы сетей"),
                 ("На замере", "Линия забора, уклон, грунт, край дороги, место сбоку для ворот, трасса кабеля", "Монтажник"),
                 ("В предложении", "Столбы и шаг, основания, ворота, защитная труба, демонтаж старого забора, график оплаты", "Вы и монтажник"),
                 ("До земляных работ", "Уведомление подано, сети отмечены, с соседом договорились", "Вы или тот, кто подаёт уведомление"),
                 ("При сдаче", "Линия относительно межевых знаков, столбы по уровню, ворота ходят свободно", "Вы и монтажник"),
                 ("После первой зимы", "Положение столбов, ход ворот, крепления", "Вы, при необходимости ремонт"),
             ],
             "note": "Это наш практический чек-лист; требования закона и источники приведены выше."},
            {"type": "cards", "tag": "Наш совет", "h": "Что на самом деле важно", "cols": 2,
             "items": [
                 ("Граница и столбы прежде всего", "Материал можно поменять потом, а неверную линию и слабые основания нельзя. При ограниченном бюджете выбирайте более простой забор, а не более слабые столбы."),
                 ("Один замер избавляет от нескольких ошибок", "Сразу проверяем границу, уклон, грунт, место для ворот и край дороги."),
                 ("Ворота и кабель вместе с забором", "Тип ворот, место сбоку и защитную трубу определите до того, как зафиксирована линия забора."),
                 ("Бумаги до материалов", "Подайте уведомление и договоритесь с соседом до заказа, чтобы панели не ждали."),
             ]},
            {"type": "cards", "tag": "Частые проблемы", "h": "Признаки того, что что-то пошло не так", "cols": 3,
             "items": [
                 ("Столб шатается от руки", "Основание расшаталось или столб сгнил. Ремонтируйте рано, пока менять нужно немного."),
                 ("Ворота начали цеплять", "Столб накренился или основание просело; у откатных ворот проверьте и ролики с каретками."),
                 ("Весной забор перекосило", "Типичный признак морозного пучения. Отдельные столбы часто можно выровнять и заново забетонировать."),
                 ("Снег и камни у забора", "Забор стоит слишком близко к дороге. Исправьте погнутые секции до следующей зимы."),
                 ("Под панелью щель", "Земля с уклоном или просела. Щель закроет цокольная доска или ступенчатый монтаж."),
                 ("Сосед спрашивает о границе", "Пусть землемер с лицензией проверит границу, пока это не стало спором."),
             ]},
        ],
        "faq": [
            ("Какая ошибка при установке забора самая дорогая?", "Обычно неверная граница или слабые столбы, потому что тогда забор приходится частично переделывать. Обеих ошибок можно избежать до работ: найдите межевые знаки и подбирайте столбы по грунту, высоте и ветру."),
            ("Достаточно ли сравнить цену за метр?", "Нет. Итог определяют и ворота, углы, уклон, грунт, демонтаж старого забора и вывоз. Сравнивайте письменные предложения построчно."),
            ("Нужно ли планировать кабель автоматики уже при строительстве забора?", "Да, если автоматические ворота когда-нибудь могут понадобиться. Защитную трубу легко заложить при строительстве забора, а позже придётся копать через въезд или газон."),
            ("Как избежать того, чтобы забор покосился?", "Подбирайте глубину и основание столбов по грунту и высоте забора, а для глухого забора ставьте более мощные столбы. Если забор уже кренится, его часто можно отремонтировать без полной замены."),
            ("Кто отвечает, если бур повредил подземный кабель?", "Ответственность зависит от того, было ли известно расположение кабеля и сообщили ли о нём монтажнику. По нашим условиям LuxAed не отвечает за скрытые коммуникации, о которых заказчик не предупредил. Поэтому запросите расположение сетей у владельцев до работ."),
            ("Что проверить после первой зимы?", "Посмотрите на линию забора сбоку, покачайте столбы рукой и проверьте, свободно ли ходят ворота. Если какой-то столб накренился, его разумно выровнять весной, пока наклон не увеличился."),
        ],
        "links_keys": ["permit_guide", "contractor", "neighbour"],
        "links_extra": [("/ru/remont-zaborov/pokosilsya-zabor/", "Покосился забор или шатается столб?", "Выравнивание и замена столбов.")],
        "cta": ("Спланируем забор правильно", "На бесплатном замере проверим границу, грунт, место для ворот и край дороги и дадим письменное предложение.", "/ru/#form", "Оставить заявку"),
    },
    "en": {
        "title": "10 fence-building mistakes and how to avoid them | LuxAed",
        "desc": "A fence on the neighbour's land, a missing building notice, weak posts, no duct for the gate cable. Ten fence-building mistakes and how to avoid them.",
        "short": "Fence-building mistakes",
        "image": "luxaed-g7",
        "kicker": "Guide · before you order",
        "h1": "Fence-building mistakes<br><em>and how to avoid them</em>",
        "lead": "Most fence problems start before the first post goes in: in planning, finding the boundary and choosing the posts. Below are ten common mistakes, with what happens, why, and how to avoid them.",
        "direct": ("The costliest mistakes are a wrong boundary, a missing building notice and weak posts: fixing them means rebuilding part of the fence.",
                   "Before you order, check the boundary markers, planning rules and utilities, and have the posts chosen for the ground and wind. Plan the gates and the automation cable with the fence line, not after it."),
        "blocks": [
            {"type": "sections", "tag": "Before work", "h": "Five mistakes before the first post",
             "intro": "These happen at the planning stage and are the hardest to put right later.",
             "items": [
                 ("1. The fence ends up on the neighbour's land", [
                     "The markers are lost or overgrown, so the line is set out along the old fence or by eye. Being a few centimetres out goes unnoticed until the house is sold, the neighbour builds or a dispute starts.",
                     "Under the Law of Property Act, a neighbour must tolerate a fence built over the boundary in good faith, but may demand that you buy the land under it or pay periodic compensation. If the builder acted in bad faith, or the neighbour objected before building or later while removal was still possible without excessive cost, they may demand its removal from their land, which means digging out and resetting the posts.",
                     "Find the markers and photograph them before work starts. Only a licensed land surveyor may restore missing markers; neighbours are invited and the costs are shared equally unless agreed otherwise. More in our guide to a <a href=\"/en/boundary-fence-neighbour/\">boundary fence with a neighbour</a>.",
                 ]),
                 ("2. The building notice is not filed", [
                     "Under Annex 1 of the Building Code, in force since 1 August 2026, a fence or gate whose construction involves digging deeper than 30 cm needs a building notice and a design. Posts set in concrete usually mean deeper digging, so plan on a notice.",
                     "File it through the Building Register at least 10 days before work starts; if the municipality announces no further checks in that time, you may begin. Do it before ordering materials, and if work has started without one, talk to the municipality's building officer first.",
                     "LuxAed provides the fence's technical data; who prepares the design and files the notice is agreed separately. More in our <a href=\"/en/fence-permit/\">fence permit guide</a>.",
                 ]),
                 ("3. A planning rule turns up too late", [
                     "A fence must comply with the detailed plan, or the general plan if there is none, and the plan can set its permitted height, transparency and material. In Harku Municipality a mesh or partly transparent timber fence around a house may not exceed 1.5 m, and solid plank fences are banned except as noise barriers or around industrial sites. In Saku Municipality a fence on family and terraced-house land must be at least 25% transparent.",
                     "A solid profiled-sheet fence where transparency is required may have to be rebuilt, and then you pay twice. Check the detailed plan before choosing the fence type; our guide to <a href=\"/en/fence-height-rules-harju-county/\">fence height rules in Harju County</a> sums up the rules by municipality.",
                 ]),
                 ("4. The auger hits a cable", [
                     "An auger or post driver cannot tell a stone from a cable, and a damaged power or telecom cable means danger, a halt to the work and a repair bill.",
                     "Under the Building Code, in the protection zone of electricity and telecom cables you may not dig deeper than 0.3 m or use impact tools such as a post driver without the cable owner's consent. An underground cable's zone is generally 1 m on each side, and the network owner provides location data free of charge.",
                     "Get the locations before drilling and mark them on the plot, including cables you laid yourself for lighting or gate automation. Under our terms, LuxAed is not liable for damage to hidden utilities that the customer did not disclose. More in our guide to <a href=\"/en/fence-near-road-and-utilities/\">fences near roads and utilities</a>.",
                 ]),
                 ("5. The road edge is ignored", [
                     "In a road protection zone the landowner must allow snow to be thrown off the road, so a street-side fence gets snow, ice and grit from the plough.",
                     "In Harku Municipality a fence must stand at least 2 m from the edge of the road surface where the boundary is closer than that. Elsewhere, too, a setback protects the fence, and on a corner plot a tall solid fence should not block drivers' view of the junction. Bent posts and panels have to be straightened or replaced.",
                 ]),
             ],
             "sources": ["aos", "maaamet", "lisa1", "ehs", "kvoond", "harku", "saku"]},
            {"type": "sections", "tag": "Structure", "h": "Five mistakes in posts, gates and price",
             "items": [
                 ("6. A solid fence gets weak posts", [
                     "A solid profiled-sheet fence, close-boarded timber or dense steel picket fence acts like a sail. Posts chosen as if for mesh start to lean after a storm, and the fixings work loose.",
                     "Posts, spacing and foundations are chosen for the fence height, the ground and the wind; an open field or seaside plot gets stronger wind than one between houses. Ask for the post size and spacing in the quote and compare. A stronger post costs little extra at the start compared with replacing leaning posts later.",
                 ]),
                 ("7. Frost heave is ignored", [
                     "Wet clay expands as it freezes and lifts posts whose base or depth does not suit the ground. In spring the post does not settle back, and the lean usually shows after the first winter.",
                     "Depth and base are chosen for the ground, because clay, sand, fill and a high water table behave differently, and a good installer explains the choice. Straightening or re-concreting a few posts costs far less than a new fence: repair and diagnostics start from €90 (call-out and initial diagnosis), with posts and labour extra. See <a href=\"/en/fence-repair/leaning-fence/\">how we repair a leaning fence</a>.",
                 ]),
                 ("8. No room for the gate", [
                     "The fence line is fixed before anyone thinks about the gate. A cantilever sliding gate is longer than the opening because of its counterweight section and needs clear space to the side, while swing gate leaves need a clear arc all year and can scrape the ground on a sloping driveway.",
                     "Measure the opening, side space and slope before the posts go in, because making room later often means moving panels and posts. Our comparison of a <a href=\"/en/sliding-or-swing-gate/\">sliding or swing gate</a> helps you choose.",
                 ]),
                 ("9. No duct for the automation cable", [
                     "Many people plan an automatic gate for later. Without a protective duct for the drive and photocell cables, you will later have to dig through the driveway, lawn or paving.",
                     "Lay the duct when the posts go in, leave the ends accessible and plan the power supply. Our price guide lists automation for an existing gate at €500–1,250 where the gate structure and electrical preparation are suitable; without a duct and power supply, digging and cabling are extra. More on our <a href=\"/en/gates-automation/\">automatic gate installation</a> page.",
                 ]),
                 ("10. Only the price per metre is compared", [
                     "The price per metre is fine for a first look, but gates, corners, slope, ground, old-fence removal and disposal decide the total. A quote without those lines looks cheaper.",
                     "In our price guide, 40 m of 3D panel fence costs €1,400–2,400, but with an automated sliding gate and a pedestrian gate the project comes to €4,050–6,350, more than half of it for the gates. Ask for an itemised written quote and compare line by line; the ranges are on our <a href=\"/en/prices/\">fence and gate prices</a> page.",
                 ]),
             ]},
            {"type": "text", "tag": "The law", "h": "What else the law says",
             "paras": [
                 "Replacing an old fence is not always a repair. For a fence whose construction involves digging deeper than 30 cm, reconstruction and replacing a single part with an equivalent one need no notice, but demolition does. Demolishing a fence to build a substantively new one counts as demolition plus new construction, while restoring a substantively similar fence may be treated as reconstruction. In justified cases the municipality may also require a notice for a structure not listed in Annex 1.",
                 "Under a building notice you may build for four years, the municipality may involve the neighbouring owner, and according to Harku Municipality there is no state fee for the notice. The owner of a structure with a protection zone may not refuse consent without good reason or charge for it, wire and metal fences are banned in the protection zone of high-voltage overhead lines, and a street's protection zone is 10 m from the outer edge of the outermost lane.",
             ],
             "sources": ["lisa1", "ehs", "harku"]},
            {"type": "table", "tag": "Checklist", "h": "What to check and when",
             "headers": ("Stage", "What to check", "Who helps"),
             "rows": [
                 ("Before the quote", "Boundary markers, detailed plan, utilities, gate positions", "You, the municipality, network owners"),
                 ("Site visit", "Fence line, slope, ground, road edge, gate side space, cable route", "The installer"),
                 ("Quote", "Posts and spacing, foundations, gates, duct, old-fence removal, payment schedule", "You and the installer"),
                 ("Before digging", "Notice filed, utilities marked, neighbour agreed", "You or the agreed filer"),
                 ("Handover", "Line against the markers, posts plumb, gates moving freely", "You and the installer"),
                 ("After the first winter", "Post alignment, gate movement, fixings", "You, with a repair if needed"),
             ],
             "note": "This is our practical checklist; the legal requirements and sources are above."},
            {"type": "cards", "tag": "Our advice", "h": "What really matters", "cols": 2,
             "items": [
                 ("Boundary and posts come first", "Materials can be changed later; a wrong line and weak foundations cannot. On a tight budget, choose a simpler fence type rather than weaker posts."),
                 ("One site visit prevents several mistakes", "We check the boundary, slope, ground, gate space and road edge in one go."),
                 ("Gates and cables with the fence", "Decide the gate type, side space and duct before the fence line is fixed."),
                 ("Paperwork before materials", "File the notice and agree with your neighbour before ordering, so panels are not left waiting."),
             ]},
            {"type": "cards", "tag": "Common problems", "h": "Signs that something went wrong", "cols": 3,
             "items": [
                 ("A post moves when pushed", "The base is loose or the post has rotted. Repair it early, before more has to be replaced."),
                 ("The gate starts to rub", "A post leans or the base has settled; on a sliding gate, check the rollers and carriages too."),
                 ("The fence leans in spring", "A typical sign of frost heave. Single posts can often be straightened and re-concreted."),
                 ("Snow and stones at the fence", "It stands too close to the road. Fix bent panels before next winter."),
                 ("A gap under a panel", "The ground slopes or has settled. A gravel board or stepped installation closes it."),
                 ("Your neighbour asks about the line", "Have a licensed land surveyor check the boundary before it becomes a dispute."),
             ]},
        ],
        "faq": [
            ("What is the costliest fence-building mistake?", "Usually a wrong boundary or weak posts, because part of the fence then has to be rebuilt. Both can be avoided before work starts: find the boundary markers and have the posts chosen for the ground, height and wind."),
            ("Is comparing the price per metre enough?", "No. Gates, corners, slope, ground, old-fence removal and disposal also decide the total. Compare written quotes line by line."),
            ("Should the automation cable be planned while the fence is built?", "Yes, if you might ever want an automatic gate. A protective duct is easy to lay while the fence goes in; later you have to dig through the driveway or lawn."),
            ("How do I stop a fence from leaning?", "Choose post depth and base for the ground and fence height, and use stronger posts for a solid fence. If the fence already leans, it can often be repaired without replacing the whole fence."),
            ("Who is responsible if the auger hits an underground cable?", "It depends on whether the cable's location was known and passed on to the installer. Under our terms, LuxAed is not liable for hidden utilities the customer did not disclose. So ask the network owners for locations before work starts."),
            ("What should I check after the first winter?", "Look along the fence line, push the posts by hand and check that the gates move freely. If a post has started to lean, straighten it in spring before the lean gets worse."),
        ],
        "links_keys": ["permit_guide", "contractor", "neighbour"],
        "links_extra": [("/en/fence-repair/leaning-fence/", "Leaning fence or loose post?", "Straightening and replacing fence posts.")],
        "cta": ("Let's plan the fence properly", "At a free site visit we check the boundary, ground, gate space and road edge, then give you a written quote.", "/en/#form", "Get a quote"),
    },
}
