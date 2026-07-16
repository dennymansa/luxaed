#!/usr/bin/env python3
# Estonian tree: / home, service pages, support pages. Targets ET keywords.
import json, html
from build_pages import head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN, SVC, reel_strip, webp_sources
from lead_form import render_lead_form
from service_catalog import assert_service_coverage
from service_layout import write_service

def form_html(default_service="", default_material=""):
    return render_lead_form("et", default_service, default_material)

PROCESS='''<div class="hsteps">
  <div class="hstep"><div class="hstep-num">1</div><h3>Jätke päring</h3><p>Üks kõne või sõnum, ja võtame kogu töö enda peale. Tuleme tasuta mõõdistusele teile sobival ajal.</p></div>
  <div class="hstep"><div class="hstep-num">2</div><h3>Leiame sobiva lahenduse</h3><p>Pakume materjali ja lahenduse teie krundi ja eelarve järgi ning ütleme täpse hinna. Ilma üllatusteta.</p></div>
  <div class="hstep"><div class="hstep-num">3</div><h3>Paigaldame korralikult</h3><p>Paigaldame kokkulepitud aia- või väravalahenduse ning seadistame vajaduse korral automaatika. Hoiame teid kursis igal etapil.</p></div>
  <div class="hstep"><div class="hstep-num">4</div><h3>Anname töö üle</h3><p>Pärast tööde lõppu vaatame tulemuse koos teiega üle ja anname valmis objekti üle. Koos hooldussoovitustega.</p></div>
</div>'''

def process_steps(items):
    return '<div class="hsteps">'+"".join(
        f'<div class="hstep"><div class="hstep-num">{i}</div><h3>{h}</h3><p>{p}</p></div>'
        for i,(h,p) in enumerate(items,1))+'</div>'

VARUSTUS='''<section class="section"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Varustus</span><h2 class="big">Õige tehnika, kogenud meeskond, korralik tulemus.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-w-van.webp"><img src="/img/luxaed-w-van.jpg" width="750" height="563" alt="LuxAedi buss objektil" loading="lazy"></picture></div>
  <div class="equip-body"><ul class="spec">
    <li><b>Postiaugupuur ja pinnasetihendaja</b>: postid saavad kindlalt ja loodi maasse</li>
    <li><b>Keevis- ja lõiketööd kohapeal</b>: teraskarkassid ja väravaraamid</li>
    <li><b>Loodimine ja mõõtmine</b>: sektsioonid ühes joones, ka kaldega krundil</li>
    <li><b>Automaatika ja domofonid</b>: paigaldame, ühendame ja seadistame terviklahendusena</li>
    <li><b>Puhas objekt</b>: koristame enda järelt ja anname krundi korras üle</li>
  </ul></div></div></div></section>'''

def bens(items): return '<ul class="svc-bens">'+"".join(f"<li>{x}</li>" for x in items)+'</ul>'
def cards(cc): return '<div class="svc-cards">'+"".join(f'<div class="svc-card"><div class="ic">{i}</div><h3>{n}</h3><p>{d}</p></div>' for i,n,d in cc)+'</div>'
def gtypes(items):
    def one(i,it):
        im,a,ic,eb,t,d,specs=it[:7]
        pos=it[7] if len(it)>7 else ''
        st=f' style="object-position:{pos}"' if pos else ''
        chips="".join(f"<li>{s}</li>" for s in specs)
        return (f'<article class="gtype"><div class="gtype-img"><span class="gtype-badge"><span class="gt-ic">{ic}</span>{eb}</span>'
                f'<picture>{webp_sources(im)}<img src="/img/{im}.jpg" alt="{html.escape(a)}" width="640" height="480" loading="lazy" decoding="async"{st}></picture></div>'
                f'<div class="gtype-txt"><h3>{t}</h3><p>{d}</p><ul class="gtype-specs">{chips}</ul></div></article>')
    count_class=f'gtypes--n{min(len(items),4)}'
    return f'<div class="gtypes {count_class}">'+"".join(one(i+1,x) for i,x in enumerate(items))+'</div>'
def gal(imgs): return '<div class="gal" id="gal">'+"".join(f'<a href="/img/{i}.jpg" data-lb="1"><picture>{webp_sources(i)}<img src="/img/{i}.jpg" alt="{html.escape(a)}" width="600" height="400" loading="lazy"></picture></a>' for i,a in imgs)+'</div>'
def faqx(fq): return '<div class="faq" id="faqList">'+"".join(f'<div class="faq-item"><button class="faq-q">{q}</button><div class="faq-a"><p>{a}</p></div></div>' for q,a in fq)+'</div>'
def related(cur):
    links={
      "/aiad/vorkaed/":["/aiad/paneelaed/","/varavad/","/aia-remont/"],
      "/aiad/paneelaed/":["/aiad/vorkaed/","/varavad/","/aiad/metallaed/"],
      "/aiad/puitaed/":["/aiad/lippaed/","/varavad/","/aia-remont/"],
      "/aiad/lippaed/":["/aiad/puitaed/","/aiad/metallaed/","/varavad/"],
      "/aiad/metallaed/":["/aiad/lippaed/","/aiad/profiilplekk-aed/","/varavad/"],
      "/aiad/profiilplekk-aed/":["/aiad/metallaed/","/aiad/lippaed/","/varavad/"],
      "/varavad/":["/aiad/paneelaed/","/aiad/puitaed/","/aiad/lippaed/"],
      "/aia-remont/":["/varavad/","/aiad/paneelaed/","/aiad/puitaed/"]}
    labels=dict(SVC["et"])
    cc=[(p,labels[p]) for p in links.get(cur,[]) if p in labels]
    return '<div class="svc-cards">'+"".join(f'<a class="svc-card" href="{p}" style="text-decoration:none"><div class="ic">→</div><h3>{t}</h3><p>Loe lähemalt →</p></a>' for p,t in cc)+'</div>'

def schema(name,desc,path,fq):
    j=lambda o:'<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False)+'</script>'
    return [j({"@context":"https://schema.org","@type":"Service","serviceType":name,"description":desc,"url":DOMAIN+path,
              "provider":{"@type":"HomeAndConstructionBusiness","name":"LuxAed","telephone":PHONE,"email":EMAIL,"url":DOMAIN+"/"},
              "areaServed":["Tallinn","Harjumaa"]}),
            j({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
              {"@type":"ListItem","position":1,"name":"Avaleht","item":DOMAIN+"/"},
              {"@type":"ListItem","position":2,"name":name,"item":DOMAIN+path}]}),
            j({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in fq]})]

def service(c):
    blocks=schema(c["name"],c["desc"],c["path"],c["faq"])
    _tl=(c.get("types",[]) or [])+(c.get("autotypes",[]) or [])
    if _tl:
        _items=[{"@type":"ListItem","position":i+1,"name":x[4],"description":x[5],"image":DOMAIN+"/img/"+x[0]+".jpg"} for i,x in enumerate(_tl)]
        blocks=blocks+['<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"ItemList","name":c.get("types_h",c["name"]),"itemListElement":_items},ensure_ascii=False)+'</script>']
    H=head("et",c["path"],c["title"],c["desc"],og_img=c.get("og",f'/img/{c["hero"]}.jpg'),schema_blocks=blocks)
    cta_band=f'<div class="svc-cta"><b>{c["cta_band"]}</b><a class="btn" href="#form">Küsi pakkumist →</a></div>'
    _tcta=cta_band if (c.get("types") and not c.get("autotypes") and not c.get("variants")) else ''
    visual_note=f'<p class="visual-note">{c["visual_note"]}</p>' if c.get("visual_note") else ''
    types_sec=f'<section class="section"><div class="wrap"><span class="tag">{c["types_tag"]}</span><h2 class="big">{c["types_h"]}</h2>{gtypes(c["types"])}{visual_note}{_tcta}</div></section>\n' if c.get("types") else ''
    auto_note=f'<p class="visual-note">{c["autotypes_note"]}</p>' if c.get("autotypes_note") else ''
    auto_sec=f'<section class="section section--alt"><div class="wrap"><span class="tag">{c.get("autotypes_tag","")}</span><h2 class="big">{c.get("autotypes_h","")}</h2>{gtypes(c["autotypes"])}{auto_note}{cta_band}</div></section>\n' if c.get("autotypes") else ''
    variants_sec=f'<section class="section section--alt"><div class="wrap"><span class="tag">Valikud</span><h2 class="big">{c["variants_h"]}</h2>{cards(c["variants"])}{cta_band}</div></section>\n' if c.get("variants") else ''
    local_sec=f'<section class="section svc-local"><div class="wrap"><span class="tag">Tallinn ja Harjumaa</span><h2 class="big">{c["local_h"]}</h2><p class="lead">{c["local_p"]}</p></div></section>' if c.get("local_p") else ''
    process_markup=process_steps(c["process"]) if c.get("process") else PROCESS
    process_h=c.get("process_h","Neli lihtsat sammu")
    gallery_sec=(f'<section class="section"><div class="wrap"><span class="tag">Galerii</span><h2 class="big">{c.get("gallery_h","Tehtud tööde näited")}</h2>{gal(c["gallery"])}<div style="text-align:center;margin-top:30px"><a class="gal-fb" href="{FB}/photos_by" target="_blank" rel="noopener">Vaata rohkem fotosid Facebookis →</a></div></div></section>' if c.get("gallery") else '')
    _videos=c.get("videos") or ([c["video"]] if c.get("video") else [])
    video_sec=reel_strip(_videos,"Videod",c.get("video_h","Vaata paigaldust ja valmis lahendusi")) if _videos else ''
    body=f'''{nav("et",c["path"])}
<main id="main">
<section class="hero">
  <div class="hero-photo-bg" style="background:url('/img/{c["hero"]}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap"><div class="hero-grid"><div>
    <div class="hero-kicker hand">{c.get("hero_prompt", "Hei! Vajad uut aeda?")}</div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">34 arvustust Facebookis · soovitavad</a></div>
    <div class="hero-service-kicker">{c.get("kicker","")}</div>
    <h1>{c["h1"]}</h1>
    <p class="hero-service-lead">{c.get("lead","")}</p>
    <div class="hero-btns"><a class="btn btn-accent" href="#form">Küsi pakkumist →</a><a class="btn btn-ghost" href="tel:{TEL}">Helista {PHONE}</a></div>
  </div>{form_html(c.get("form_service",""),c.get("form_material",""))}</div>
  <div class="hero-stats"><div class="hstat"><b>100%</b><span>soovitavad Facebookis</span></div><div class="hstat"><b>34</b><span>arvustust</span></div><div class="hstat"><b>15+</b><span>aastat kogemust</span></div></div></div>
</section>
<section class="section"><div class="wrap"><span class="tag">Mida saate</span><h2 class="big">{c["intro_h"]}</h2><p class="lead">{c["intro_p"]}</p>{bens(c["bens"])}</div></section>
{types_sec}{auto_sec}{variants_sec}{local_sec}
<section class="section"><div class="wrap"><span class="tag">Ausalt hinnast</span><h2 class="big">Millest sõltub hind</h2>
  <p class="lead">{c.get("price_lead", "Fikseeritud hinnakirja ei ole. Täpse hinna ütleme pärast tasuta mõõdistust.")}</p>
  <div class="honest"><div class="hon good"><h3>Alati hinna sees</h3><ul>{"".join(f"<li>{x}</li>" for x in c["incl"])}<li>Töötame aastaringselt, ka talvel</li><li>Garantii tehtud töödele</li></ul></div>
  <div class="hon bad"><h3>Mõjutab hinda</h3><ul>{"".join(f"<li>{x}</li>" for x in c["factors"])}</ul></div></div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">Kuidas töötame</span><h2 class="big">{process_h}</h2>{process_markup}</div></section>

{gallery_sec}{video_sec}
<section class="section section--alt"><div class="wrap"><span class="tag">KKK</span><h2 class="big">Korduma kippuvad küsimused</h2>{faqx(c["faq"])}</div></section>
<section class="section"><div class="wrap"><span class="tag">Teised teenused</span><h2 class="big">Vaata ka</h2>{related(c["path"])}</div></section>
<section class="cta-final"><div class="wrap"><h2>{c.get("final_cta", "Ehitame teie <em>unistuste aia</em>")}</h2>
  <p>{c.get("final_cta_text", "Jätke päring või helistage.<br>Tuleme tasuta mõõdistusele ja ütleme täpse hinna.")}</p>
  <div class="hero-btns"><a class="btn btn-accent" href="#form">Küsi pakkumist →</a><a class="btn btn-ghost" href="tel:{TEL}">Helista {PHONE}</a></div></div></section>
</main>
<div class="lb" id="lb"><button class="lb-x" aria-label="Sulge">&times;</button><img src="" alt="" id="lbImg"></div>
{footer("et")}
<div class="mob-bar"><a class="btn btn-accent mob-call" href="tel:{TEL}"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="vertical-align:-3px;margin-right:6px"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>Helista</a></div>
{SCRIPTS}
</body></html>'''
    print("wrote", write(c["path"],H+"\n"+body))

ETSERV=[
{"path":"/aiad/vorkaed/","video":("luxaed-reel-vorkaed","3D keevispaneelaed — valmis objekt"),"name":"Võrkaed ja 3D paneelaed","hero":"luxaed-w-mesh-1","og":"/img/luxaed-w-mesh-1.jpg",
 "title":"Võrkaia paigaldus ja 3D paneelaed Tallinnas — LuxAed","desc":"Võrkaia paigaldus ja 3D paneelaia paigaldus Tallinnas ja Harjumaal. Keevispaneelid 2D/3D, aiapostid, koeraaedikud, antratsiit RAL 7016. Tasuta mõõdistus.",
 "kicker":"Võrkaed · 3D paneelaed · aiapostid","h1":"Võrk- ja 3D-paneelaedade<br><em>paigaldus</em>",
 "lead":"Kaasaegsed keevispaneelaiad (3D aiapaneelid) jäikusribidega: tugev, korralik ja hea läbipaistvusega piire. Tsingitud ja pulbervärvitud lahendus kestab aastakümneid.",
 "intro_h":"Miks valida paneelaed","intro_p":"Keevispaneel (3D) hoiab vormi, ei vaju ega paindu tuules ning näeb kaasaegne välja. Selline piirdeaed sobib eramutele, ridaelamutele ja territooriumidele. Võrkaia paigaldus algab täpsest mõõdistusest: postide samm ja paigaldussügavus valitakse paneeli kõrguse ning pinnase järgi. Paigaldame ka aiaposte ja ehitame koeraaedikuid. Vajaliku materjali valime ja hangime teie eest.",
 "bens":["Tugevad keevispaneelid jäikusribidega","Tsink + pulbervärv. Ei roosteta","Antratsiit RAL 7016 ja teised värvid","2D ja 3D aiapaneelid, keevisvõrkaed","Tsingitud aiapostid, kübarad ja klambrid","Koeraaedikud ja loomatarad keevispaneelist"],
 "types_tag":"2D ja 3D","types_h":"2D ja 3D paneelaed",
 "types":[("luxaed-w-mesh-1","Antratsiit 3D paneelaed heki ääres","3D","Paneelaed","3D keevispaneel","Keevispaneel V-kujuliste jäikusribidega. Need annavad jäikuse ja kaasaegse mahulise ilme. Kõige tugevam ja populaarseim valik, mis ei vaju ega paindu tuules.",["V-jäikusribid","Kõige tugevam","Antratsiit RAL 7016"]),
          ("luxaed-mesh-2","2D keevispaneelaed krundi ääres","2D","Paneelaed","2D keevispaneel","Sile paneel topelthorisontaalvarrastega, kaks varrast reas. Vastupidav ja soodsam kui 3D. Hea valik pikkadele lõikudele.",["Topeltvarras","Soodsam kui 3D","Pikkadele lõikudele"])],
 "variants_h":"Lisaks paneelaedadele",
 "variants":[("▤","Aiapostid","Tsingitud aiapostid (metallist aiapostid) kübarate ja kinnitusklambritega. Paigaldame ja hangime materjali."),
             ("⌗","Koeraaedik","Keevispaneelidest koeraaedikud ja loomatarad. Tugevad ja turvalised."),
             ("◧","RAL värvid","Antratsiit RAL 7016, roheline RAL 6005, must jm.")],
 "cta_band":"Arvutame võrkaia teie krundile","incl":["Krundi mõõdistus","Tsingitud postide paigaldus","Keevispaneelide ja kinnituste montaaž","Loodimine reljeefi järgi","Kontroll pärast paigaldust"],
 "factors":["Aia pikkus ja paneelide kõrgus (1,23–2,03 m)","Paneeli tüüp (2D/3D) ja värv","Aiapostide arv ja tüüp","Väravate, jalgvärava ja koeraaediku vajadus","Reljeef ja vana aia lammutus"],
 "gallery":[("luxaed-w-mesh-1","Antratsiit 3D paneelaed heki ääres"),("luxaed-w-mesh-2","3D keevispaneelaed rohelises toonis"),("luxaed-w-mesh-gate","Jalgvärav keevispaneelist"),("luxaed-w-gates-green","Tiibväravad keevispaneelist"),("luxaed-w-mesh-detail","Paneeli kinnitus postile"),("luxaed-w-panels","2D aiapaneelid enne paigaldust"),("luxaed-3d-mesh-fence-1","3D paneelaed eramaja ümber"),("luxaed-w-gates-night","Paneelväravad õhtuvalguses"),("luxaed-mesh-2","Võrkaed krundi ääres"),("luxaed-w-van","LuxAed meeskond objektil")],
 "faq":[("Võrkaed (aiavõrk) või paneelaed. Kumb valida?","Klassikaline aiavõrk rullis on odav, aga venib ja vajub aja jooksul. Soovitame keevispaneeli või keevisvõrkaeda: sama läbipaistvus, kuid jäik ja korralik. Peab kordades kauem. Arvutame mõlema hinna ja aitame valida."),
        ("Mis vahe on keevisvõrkaial ja keevispaneelaial?","Keevisvõrkaed on tihe keevisvõrk raamil, keevispaneelaed on jäikusribidega paneel. Mõlemad tsingitud ja pulbervärvitud. Paneel on jäigem, võrk soodsam."),
        ("Millised kõrgused on?","Tavaliselt 1,23–2,03 m. Valime kõrguse vajaduse järgi."),
        ("Milline värv valida?","Populaarseimad on antratsiit RAL 7016 ja roheline RAL 6005."),
        ("Kas paigaldate ka aiaposte?","Jah, paigaldame tsingitud aiaposte (metallist aiapostid) koos kübarate ja kinnitusklambritega. Vajaliku materjali hangime ise, nii paneelaia kui muude aedade jaoks."),
        ("Kas teete koeraaedikuid?","Jah, ehitame keevispaneelidest koeraaedikuid ja loomatarasid. Tugevad, turvalised ja pika elueaga."),
        ("Kas värava saab samas toonis?","Jah, valmistame lükand- ja tiibväravaid sama paneeliga ning samas värvitoonis.")]},
{"path":"/aiad/puitaed/","video":("luxaed-video-puitvarav","Puidust lükandvärav automaatikaga — valmis objekt"),"name":"Puitaed","hero":"luxaed-svc-wood","og":"/img/luxaed-svc-wood.jpg",
 "title":"Puitaedade ja väravate paigaldus Tallinnas — LuxAed","desc":"Puitaedade ja -väravate valmistamine ja paigaldus Tallinnas ja Harjumaal. Horisontaalne puitaed, teraskarkass, töötlus. Tasuta mõõdistus ja pakkumine.",
 "kicker":"Puit · teraskarkass","h1":"Puitaedade<br><em>paigaldus</em>",
 "lead":"Soe ja korralik välimus. Valmistame puitaedu ja -väravaid tugeval teraskarkassil. Loodusliku puidu ja vastupidava metalli kombinatsioon.",
 "intro_h":"Miks puitaed","intro_p":"Puit näeb väärikas ja looduslik välja ning sobib eri stiiliga kruntidele. Tugev teraskarkass aitab konstruktsioonil püsida sirge ja kaua kesta.",
 "bens":["Töödeldud puit Eesti kliima jaoks","Tugev teraskarkass. Ei vaju","Horisontaalne, vertikaalne või ribiline","Aed ja väravad ühes stiilis","Võimalik väravaautomaatika","Individuaalne disain"],
 "types_tag":"Puitaia tüübid","types_h":"Puitaedade tüübid",
 "types":[("luxaed-svc-wood","Horisontaalne puitaed teraskarkassil","▤","Puitaia tüüp","Horisontaalne puitaed","Horisontaalne puitaed on teraskarkassil horisontaallaudadega aed, kõige populaarsem ja kaasaegsem valik. Laudade vahe valime privaatsuse või õhulisema ilme järgi.",["Teraskarkassil","Valitav laudade vahe","Populaarseim"]),
          ("luxaed-wood-2","Vertikaalne puitaed ja jalgvärav","▥","Puitaia tüüp","Vertikaalne puitaed","Vertikaalne puitaed on püstlaudadega aed, klassikaline ja korralik, vahega või täiskinnine. Sobib nii tänava- kui õuepoolseks piirdeks.",["Püstlauad","Vahega või kinnine","Klassikaline"]),
          ("luxaed-wood-swing-gate-1","Puidust tiibväravad teraskarkassil","⛩","Väravad","Puitväravad","Puitväravad valmistame aiaga ühes stiilis: lükand- või tiibväravad puidutäite ja teraskarkassiga, soovi korral automaatikaga.",["Lükand- või tiibvärav","Aiaga ühes stiilis","Automaatikaga"])],
 "cta_band":"Valime puitaia teie maja juurde","incl":["Krundi mõõdistus","Sektsioonide ja teraskarkassi valmistamine","Postide ja sektsioonide paigaldus","Puidu töötlus ja kate","Kontroll pärast paigaldust"],
 "factors":["Aia pikkus ja kõrgus","Tüüp (horisontaalne, vertikaalne, žalusii)","Puidu liik ja töötlus","Väravad ja automaatika","Reljeef ja alus"],
 "gallery":[("luxaed-svc-wood","Puitaed teraskarkassil"),("luxaed-g1","Puitaed ja lükandvärav"),("luxaed-wood-2","Puitaed krundil"),("luxaed-wood-3","Puitaed ja värav"),("luxaed-g2","Puidust tiibväravad"),("luxaed-g7","Puitaed kivisillutise ääres"),("luxaed-wood-sliding-gate-1","Puidust lükandvärav"),("luxaed-wood-swing-gate-1","Puidust tiibvärav"),("luxaed-g10","Puidust värava lukk"),("luxaed-w-van","LuxAed objektil")],
 "faq":[("Kas puit ei mädane?","Kasutame välitingimustesse sobivalt töödeldud puitu ja teraskarkassi. Kaitsekihti õigel ajal uuendades kestab puitaed kaua."),
        ("Kas puitaia saab teha horisontaallaudadega?","Jah. Horisontaalne puitaed teraskarkassil on üks populaarsemaid lahendusi."),
        ("Kas teete väravad samas stiilis?","Jah, valmistame lük- ja tiibväravaid puidutäitega ühises disainis."),
        ("Kas puitaed vajab hooldust?","Perioodiliselt tasub uuendada puidu kaitsekihti. Selgitame, kuidas hooldada.")]},
{"path":"/aiad/metallaed/","name":"Metallaed ja profiilplekk-aed","hero":"luxaed-svc-profnastil","og":"/img/luxaed-svc-profnastil.jpg",
 "title":"Metall- ja profiilplekk-aedade paigaldus Tallinnas — LuxAed","desc":"Metallaed, profiilplekk-aed ja moodulaed Tallinnas ja Harjumaal. Tsingitud plekk, kunstsepis, betoonaiad, eri värvid. Tasuta mõõdistus.",
 "kicker":"Metall · profiilplekk","h1":"Metall- ja profiilplekk-aedade<br><em>paigaldus</em>",
 "lead":"Praktiline ja soodne lahendus: kinnine aed tsingitud profiilplekist. Täielik privaatsus, tuule- ja tolmukaitse, erinevad värvid.",
 "intro_h":"Miks profiilplekk","intro_p":"Profiilplekk on soodne ja kiiresti paigaldatav. Kinnine aed varjab krundi ja peab kaua tänu tsingile ja polümeerkattele. Profiilplekk-aed on ühtlasi moodulaed: valmis sektsioonidest, mis lähevad kiiresti üles.",
 "bens":["Täielik privaatsus. Kinnine aed","Tsingitud plekk polümeerkattega","Erinevad värvid, ka puidu imitatsioon","Kaitse tuule, tolmu ja müra eest","Kunstsepis ja dekoratiivdetailid","Ka betoon- ja plokkaed massiivseks müüriks","Moodulaed: valmis sektsioonidest, kiire paigaldus"],
 "types_tag":"Metallaia valikud","types_h":"Metallaedade tüübid",
 "types":[("luxaed-profnastil-2","Profiilplekk-aed tsingitud plekist","▦","Metallaia tüüp","Profiilplekk-aed","Profiilplekk-aed on kinnine aed tsingitud plekist polümeerkattega. Täielik privaatsus ning kaitse tuule, tolmu ja müra eest. Saadaval eri värvides, ka puidu imitatsioon.",["Kinnine, privaatne","Tsink + polümeerkate","Eri värvid"]),
          ("luxaed-concrete-fence-guide","Betoonaed kivi-imitatsiooniga","▣","Massiivne piire","Betoon- ja plokkaed","Betoon- ja plokkaed on massiivne müür privaatsuseks ja müravaigistuseks: betoonpaneelidest kivi-imitatsiooniga või plokkpostidega. Kombineerime seda metalli, pleki või sepisega.",["Massiivne müür","Kivi-imitatsioon","Müra- ja tuulekaitse"]),
          ("luxaed-profnastil-gate","Profiilplekk-tiibväravad","⛩","Väravad","Profiilplekk-väravad","Profiilplekk-väravad valmistame aiaga ühes toonis: lükand- või tiibväravad tsingitud plekist, soovi korral automaatikaga.",["Lükand- või tiibvärav","Aiaga ühes toonis","Automaatikaga"])],
 "cta_band":"Arvutame profiilplekk-aia hinna","incl":["Krundi mõõdistus","Metallpostide ja -lattide paigaldus","Profiilpleki montaaž","Loodimine","Kontroll pärast paigaldust"],
 "factors":["Aia pikkus ja kõrgus","Pleki mark ja värv","Postide tüüp (metall, kivi)","Väravad ja jalgväravad","Reljeef ja alus"],
 "gallery":[("luxaed-svc-profnastil","Profiilplekk-värav"),("luxaed-metal","Metallväravad õhtuvalguses"),("luxaed-profnastil-2","Profiilplekk-aed"),("luxaed-profnastil-gate","Profiilplekk-tiibväravad"),("luxaed-w-lippaed-1","Metall-lippaed grafiithallis"),("luxaed-w-lippaed-2","Hall metall-lippaed"),("luxaed-w-lippaed-3","Pruun metall-lippaed"),("luxaed-w-lock-brown","Värava lukk"),("luxaed-w-lock-black","Värava lukk ja käepide"),("luxaed-w-van","LuxAed objektil")],
 "faq":[("Kas profiilplekk ei pleegi?","Kvaliteetne polümeerkattega plekk säilitab värvi kaua. Kasutame Eesti kliimasse sobivaid materjale."),
        ("Kas ehitate ka betoon- või plokkaedu?","Jah, ehitame massiivseid betoon- ja plokkmüüre ning kombineerime neid metalli, pleki või sepisega."),
        ("Kas profiilplekk-aeda saab kombineerida kivipostidega?","Jah, valmistame kombineeritud aedu, kus profiilplekk paikneb kivi- või plokkpostide vahel."),
        ("Kas profiilplekk on odavam kui puit ja võrkaed?","Reeglina jah. Üks soodsamaid lahendusi. Täpse hinna ütleme pärast mõõdistust."),("Kas teete moodulaeda?","Jah. Meie profiilplekk- ja paneelaiad ongi moodulaed: valmis moodulsektsioonid ja postid, mis paigalduvad kiiresti ja korralikult.")]},
{"path":"/aiad/lippaed/","name":"Metall-lippaed","hero":"luxaed-w-lippaed-1","og":"/img/luxaed-w-lippaed-1.jpg",
 "title":"Metall-lippaedade paigaldus Tallinnas — LuxAed","desc":"Horisontaalne või vertikaalne metall-lippaed Tallinnas ja Harjumaal. Tsingitud ja pulbervärvitud lamellid, valitav vahe ja RAL-toon. Tasuta mõõdistus.",
 "kicker":"Metall-lippaed · štaketnik","h1":"Metall-lippaedade<br><em>paigaldus</em>",
 "lead":"Kaasaegne metallist lippaed (euro-lippaed) horisontaalsete või vertikaalsete lamellidega. Valida saab lamellide vahe, paigutuse ja värvitooni.",
 "intro_h":"Miks metall-lippaed","intro_p":"Metall-lippaed ehk metallpiire näeb kerge ja kaasaegne välja, laseb valgust läbi ning kestab aastakümneid. Valmistame nii horisontaalse kui ka vertikaalse paigutusega lippaedu eramutele ja ettevõtetele. Aia ning väravad teeme ühes stiilis.",
 "bens":["Horisontaalne või vertikaalne paigutus","Valitav vahe lamellide vahel","Tsingitud ja pulbervärvitud pind","RAL-värvid, ka antratsiit RAL 7016","Aed ja väravad ühes stiilis","Ühe- või kahepoolne lahendus"],
 "types_tag":"Lippaia valikud","types_h":"Metall-lippaedade tüübid",
 "types":[("luxaed-w-lippaed-1","Grafiithall horisontaalne metall-lippaed","▤","Lippaia tüüp","Horisontaalne või vertikaalne metall-lippaed","Metall-lippaia lamellid saab paigutada horisontaalselt või vertikaalselt. Horisontaalne lahendus mõjub modernselt, vertikaalne klassikalisemalt. Lamellide vahe valite ise: hõredam õhulisuse või tihedam privaatsuse jaoks.",["Horisontaalne või vertikaalne","Valitav lamellide vahe","Tsink + pulbervärv"]),
          ("luxaed-w-lippaed-3","Pruun metall-lippaed lähivaates","◧","Värvid","Värvid ja RAL-toonid","Lippaia teeme igas RAL-toonis. Populaarseimad on antratsiit RAL 7016, hall ja pruun. Tsingitud ja pulbervärvitud pind ei roosteta ega pleegi.",["Antratsiit RAL 7016","Hall, pruun jt","Ei roosteta"]),
          ("luxaed-w-gates-picket","Lükandvärav lippaiast","⛩","Väravad","Lippaed ja väravad","Väravad teeme sama lippaia lamelliga ja toonis: lükand- ja tiibväravad koos aiaga ühtses stiilis, soovi korral automaatikaga.",["Sama lamell ja toon","Lükand- või tiibvärav","Automaatikaga"])],
 "cta_band":"Arvutame metall-lippaia teie krundile","incl":["Krundi mõõdistus","Metallpostide paigaldus","Lamellide montaaž valitud vahega","Loodimine reljeefi järgi","Kontroll pärast paigaldust"],
 "factors":["Aia pikkus ja kõrgus","Lamellide suund ja vahe","Ühe- või kahepoolne lahendus","Värv (RAL)","Väravate ja jalgvärava arv","Reljeef ja alus"],
 "gallery":[("luxaed-w-lippaed-1","Grafiithall metall-lippaed"),("luxaed-w-lippaed-2","Hall metall-lippaed maja juures"),("luxaed-w-lippaed-3","Pruun metall-lippaed lähivaates"),("luxaed-w-gates-picket","Lükandvärav lippaiast"),("luxaed-w-lock-brown","Locinox lukk lippaia väraval"),("luxaed-metall-lippaed-vertical-v1","Vertikaalne metall-lippaed ja liugvärav")],
 "faq":[("Mis on metall-lippaed (štaketnik)?","Metallist lippaed on tsingitud ja pulbervärvitud lamellidest piire. Lamellid võivad olla horisontaalsed või vertikaalsed ning nende vahe valitakse soovitud privaatsuse järgi."),
        ("Kas lippaed on läbipaistev?","Vahe lamellide vahel valite ise: tihedam privaatsuseks või hõredam kergema ilme jaoks. Kahepoolne lippaed on privaatsem."),
        ("Millised värvid on?","Populaarseim on antratsiit RAL 7016, samuti must ja pruun. Teeme teisi RAL-toone tellimusel."),
        ("Kas väravad saab teha samas stiilis?","Jah, valmistame lükand- ja tiibväravad sama paigutuse, lamelli ning värvitooniga nagu lippaia.")]},
{"path":"/varavad/","name":"Väravad ja automaatika","hero":"luxaed-auto-2","og":"/img/luxaed-auto-2.jpg","videos":[("luxaed-reel-domofon","Hikvisioni domofon väraval"),("luxaed-reel-varav-oht","Lükandvärav automaatikaga"),("luxaed-video-puitvarav","Lükandvärav ühe nupuvajutusega"),("luxaed-reel-montaaz","Paigaldus objektil")],
 "title":"Liugvärava ja väravaautomaatika paigaldus Tallinnas — LuxAed","desc":"Liugvärav, tiibvärav ja väravaautomaatika Tallinnas ja Harjumaal. Valmistamine, paigaldus, tõkkepuud ja fonolukud terviklahendusena. Tasuta mõõdistus.",
 "kicker":"Liugvärav · tiibvärav · automaatika","h1":"Väravate ja automaatika<br><em>paigaldus</em>",
 "hero_prompt":"Hei! Vajad uut väravat?",
 "lead":"Liugvärav või tiibvärav koos sobiva automaatikaga terviklahendusena. Valmistame ka jalgväravaid ning paigaldame fonolukke, videopaneele ja tõkkepuid. Mõõdame, valmistame, paigaldame ja seadistame.",
 "intro_h":"Liugvärav ja väravaautomaatika terviklahendusena","intro_p":"Projekteerime ja paigaldame kogu sissesõidulahenduse, alates jalgväravast kuni liugvärava, automaatika ja läbipääsusüsteemini. Sobitame ajami liugvärava kaalu, laiuse ja kasutussageduse järgi ning ühendame puldid, fonoluku ja turvafotoelemendid.",
 "bens":["Liugvärav ja automaatika ühest kohast","Tiibväravad koos sobiva automaatikaga","Tuntud tootjate ajamid: Nice, CAME, BFT, Sommer, DoorHan","Juhtimine: pult, telefonikõne (GSM), rakendus, kood või RFID","Fotoelemendid ja signaallamp turvaliseks tööks","Aku-varutoide elektrikatkestuse puhuks","Fonolukud, videopaneelid, tõkkepuud ja garaažiuksed"],
 "types_tag":"Väravatüübid","types_h":"Kõik väravatüübid",
 "types":[("luxaed-svc-gates","Puidust liugvärav automaatikaga","⇄","Väravatüüp","Liugvärav (lükandvärav)","Liugvärav liigub külgsuunas ega vaja avamiseks ruumi sissesõidu ees. Konsoolne liugvärav töötab ilma üle sõidetava alumise siinita ning sobib hästi nii eramule kui ka ettevõtte territooriumile.",["Ilma alumise siinita","Automaatikaga","Puit / plekk / keevisvõrk"],"center 45%"),
          ("luxaed-w-gates-green","Tiibväravad keevisvõrktäitega","⛩","Väravatüüp","Tiibvärav","Tiibvärav on kahe tiivaga värav, mis avaneb sisse- või väljapoole. Konstruktsioonilt on see sageli lihtsam lahendus, kui sissesõidu ees on piisavalt ruumi.",["Kaks tiiba","Sageli lihtsam konstruktsioon","Sobib automaatikale"]),
          ("luxaed-gate-closeup-1","Jalgvärav puittäidise ja lukuga","🚶","Väravatüüp","Jalgvärav","Jalgvärav on käigutee värav, mis tehakse aiaga ühes stiilis. Mehaaniline lukk või elektrilukk domofoni ja kutsepaneeliga.",["Käigutee värav","Lukk / elektrilukk","Aiaga ühes stiilis"],"center 40%"),
          ("luxaed-gate-hardware-1","Liugvärava rullikud ja kandurid","⚙","Detailid","Väravafurnituur","Kasutame kvaliteetseid rullikuid, kandureid, hingi ja lukke. Õigesti valitud ning hooldatud furnituur aitab väraval sujuvalt liikuda.",["Tsingitud detailid","Rullikud ja kandurid","Hooldatav"])],
 "autotypes_tag":"Väravaautomaatika","autotypes_h":"Väravaautomaatika tüübid",
 "autotypes":[("luxaed-g9","Liugvärava BFT ajam","⚙","Automaatika","Liugvärava automaatika","Liugvärava automaatika ühendab ajami, juhtimise ja turvaseadmed. Ajami valime värava kaalu, laiuse ning kasutussageduse järgi; komplekti täpsustame vastavalt objektile.",["Ajami valik kaalu järgi","Juhtimine ja turvaseadmed","BFT / Nice / CAME"]),
              ("luxaed-g6","Tiibvärava hoobajam","⚙","Automaatika","Tiibvärava automaatika","Tiibvärava automaatika kasutab hoob- või kruviajameid mõlemale tiivale. Ajami tüüp ja tööparameetrid valitakse värava mõõtude, kaalu ning konstruktsiooni järgi.",["Hoob- või kruviajam","Seadistus värava järgi","Mõlemale tiivale"]),
              ("luxaed-barrier-guide","Automaatne tõkkepuu sissesõidul","⊤","Automaatika","Tõkkepuu","Tõkkepuu on automaatne piirdepoom sissesõidu või parkla juhtimiseks. Sobib korteriühistutele, parklatele ja territooriumidele.",["Parklad ja ühistud","Pult või kood","Kontrollitud läbipääs"]),
              ("luxaed-reel-domofon-poster","Hikvisioni domofon väraval","🔔","Automaatika","Fonolukk ja videopaneel","Fonolukk (domofon) ja videopaneel avavad värava ja jalgvärava kaugelt. Näete külalist ekraanil või telefonis ja avate värava ühe puudutusega.",["Video ja kõne","Kaugjuhtimine","Värava avamine"],"left center")],
 "autotypes_note":"Tõkkepuu pilt on fotorealistlik illustratiivne lahenduse näidis.",
 "cta_band":"Valime liugvärava ja automaatika teie sissesõidule","incl":["Sissesõidu mõõdistus","Sobiva konstruktsiooni ja ajami valik","Kokkulepitud tööde hinnapakkumine","Paigaldus ja seadistus vastavalt pakkumisele","Töö kontroll ning kasutusjuhised"],
 "final_cta":"Valime teie sissesõidule <em>sobiva väravalahenduse</em>",
 "final_cta_text":"Jätke päring või helistage.<br>Mõõdame sissesõidu ja soovitame sobiva värava ning automaatika.",
 "factors":["Liugvärav või tiibvärav","Väravalehe laius ja kaal","Automaatika ajami mark ja võimsus","Juhtimine: pult, GSM, rakendus või RFID","Aku-varutoide, fonolukk, tõkkepuu või garaažiuks","Täide: puit, plekk või keevisvõrk"],
 "gallery":[("luxaed-svc-gates","Puidust lükandvärav automaatikaga"),("luxaed-w-gates-auto","BFT ajam lükandväraval"),("luxaed-w-gates-green","Tiibväravad keevisvõrktäitega"),("luxaed-w-gates-graphite","Grafiithallid tiibväravad"),("luxaed-w-gates-winter","Lükandvärav, paigaldus talvel"),("luxaed-w-gates-night","Väravad õhtuvalguses"),("luxaed-w-gates-picket","Lükandvärav lippaiast"),("luxaed-w-lock-black","Värava lukk ja käepide"),("luxaed-w-mesh-gate","Jalgvärav keevisvõrgust"),("luxaed-w-van","LuxAed objektil")],
 "faq":[("Liugvärav või tiibvärav – kumb valida?","Liugvärav on mugav, kui sissesõidu ees on vähe ruumi, sest väravaleht liigub aia kõrvale. Tiibvärav on lihtsam lahendus, kui avamiseks on piisavalt ruumi. Mõõdistusel aitame valida."),
        ("Milliste tootjate automaatikat paigaldate?","Paigaldame tuntud tootjate ajameid: Nice, CAME, BFT, Sommer, DoorHan jt. Ajami valime värava kaalu, laiuse ja kasutuskoormuse järgi."),
        ("Kuidas väravat juhtida saab?","Puldist, telefonikõnega (GSM), nutirakendusest, koodpaneelist või RFID-kaardiga. Sobiva süsteemi korral saab ühe puldiga juhtida mitut väravat või tõkkepuud."),
        ("Kas värav töötab elektrikatkestuse ajal?","Jah, kui paigaldada aku-varutoide. Ilma selleta saab värava tavaliselt avada käsitsi vabastusvõtmega."),
        ("Kas olemasolevale väravale saab lisada automaatika?","Enamasti jah. Kontrollime konstruktsiooni ja valime liugväravale või tiibväravale sobiva ajami."),
        ("Kuidas tagate väravaautomaatika ohutuse?","Paigaldame fotoelemendid ja seadistame jõupiirangu, et takistuse tuvastamisel värav peatuks või liiguks tagasi. Vajaduse korral lisame signaallambi."),
        ("Kas paigaldate fonolukke, domofone ja tõkkepuid?","Jah. Fonoluku ühendame värava või jalgväravaga. Tõkkepuu sobib parklale ja ühistule, kus on vaja kiiret läbipääsu.")]},
{"path":"/aia-remont/","video":("luxaed-reel-remont","Vana betoonposti eemaldamine"),"name":"Aia ja värava remont","hero":"luxaed-g6","og":"/img/luxaed-g6.jpg",
 "title":"Aia ja värava remont Tallinnas — LuxAed","desc":"Aedade ja väravate remont Tallinnas ja Harjumaal: sektsioonide ja postide vahetus, lük- ja tiibväravate ning automaatika remont. Diagnostika ja hinnapakkumine.",
 "kicker":"Remont · hooldus","h1":"Aedade ja väravate<br><em>remont</em>",
 "hero_prompt":"Hei! Vajad aia või värava remonti?",
 "lead":"Taastame aedu, väravaid ja automaatikat: sektsioonide ja postide vahetus, tiibade reguleerimine, ajamite ja furnituuri remont. Teeme diagnostika ja ütleme hinna.",
 "intro_h":"Mida remondime","intro_p":"Aia remont on sageli mõistlikum kui uue aia ehitamine: kogu aeda ei pea alati vahetama. Sageli piisab kahjustatud sektsioonide või postide vahetusest, väravate reguleerimisest või automaatika taastamisest.",
 "bens":["Kahjustatud sektsioonide vahetus","Postide vahetus ja loodimine","Lük- ja tiibväravate remont","Automaatika remont ja seadistus","Rullikute, siinide ja furnituuri vahetus","Diagnostika ja hind enne tööd"],
 "variants_h":"Remonditööde liigid",
 "variants":[("▤","Aia sektsioonid","Kahjustatud võrgusektsioonide, laudade või pleki vahetus."),
             ("▥","Postid","Viltuvajunud postide vahetus, loodimine ja kindlustamine."),
             ("⇄","Väravad","Tiibade reguleerimine, rullikute ja siinide vahetus."),
             ("⚙","Automaatika","Ajamite, pultide ja fotoelementide diagnostika ja remont.")],
 "cta_band":"Teeme diagnostika ja parandame aia","incl":["Väljasõit ja diagnostika","Hind enne tööde algust","Sektsioonide, postide või furnituuri vahetus","Väravate ja automaatika reguleerimine","Töö kontroll pärast remonti"],
 "factors":["Kahjustuste maht ja liik","Aia ja värava tüüp","Materjalide vahetuse vajadus","Automaatika remont","Ligipääs krundile"],
 "gallery":[("luxaed-reel-remont-poster","Vana betoonposti eemaldamine"),("luxaed-w-mesh-detail","Kinnituste kontroll"),("luxaed-w-lock-black","Lukkude vahetus"),("luxaed-g6","Post ja ajam"),("luxaed-g8","Lükandvärava automaatika"),("luxaed-g9","Värava ajam"),("luxaed-auto-2","Ajami remont"),("luxaed-w-lock-brown","Luku vahetus"),("luxaed-w-crew","Meister tööl"),("luxaed-w-van","LuxAed objektil")],
 "final_cta":"Teeme teie aia või värava <em>taas korda</em>",
 "final_cta_text":"Jätke päring või helistage.<br>Vaatame olukorra üle ja ütleme remondi hinna enne tööde algust.",
 "faq":[("Kas aeda saab remontida ilma kogu piiret välja vahetamata?","Sageli jah. Vahetame ainult kahjustatud sektsioonid või postid. Ülevaatusel hindame, milline lahendus on mõistlikum."),
        ("Kas parandate väravaautomaatikat?","Jah, diagnoosime ja remondime ajameid, pulte ning fotoelemente; vajaduse korral vahetame rikkis osad."),
        ("Kas remondite ka teiste paigaldatud väravaid?","Jah, töötame ka teiste meistrite konstruktsioonidega. Hindame kohapeal."),
        ("Kui palju remont maksab?","Sõltub tööde mahust. Pärast diagnostikat ütleme täpse hinna ilma varjatud lisatasudeta.")]},
]

# ET-first semantic split: keep the established URLs live, but give each one a
# single search intent. RU/EN equivalents are added only after their copy is ready.
ET_OVERRIDES={
"/aiad/vorkaed/":{
 "video":None,"name":"Rullvõrkaed","hero":"luxaed-rullvork-corner-v1","og":"/img/luxaed-rullvork-corner-v1.jpg",
 "title":"Rullvõrkaia paigaldus Tallinnas ja Harjumaal — LuxAed","desc":"Punutud ja keevitatud rullvõrkaia paigaldus Tallinnas ja Harjumaal. Postid, pingutustraat, väravad ja vana aia eemaldus. Tasuta mõõdistus.",
 "kicker":"Rullvõrkaed · aiavõrk · punutud võrk","h1":"Rullvõrkaia<br><em>paigaldus</em>",
 "lead":"Praktiline ja õhuline piire eramule, suvilale või suuremale territooriumile. Paigaldame punutud ja keevitatud rullvõrku koos postide, pingutuse ning väravatega.",
 "intro_h":"Millal valida rullvõrkaed","intro_p":"Rullvõrkaed sobib hästi siis, kui soovite piirata pikema aiajoone mõistliku eelarvega, kuid säilitada valguse ja vaate. Mõõdistusel valime võrgu tüübi, traadi, postide sammu ja pingutuse vastavalt aia kõrgusele, pinnasele ning nurkade arvule.",
 "bens":["Punutud või keevitatud rullvõrk","Tsingitud või tsingitud ja PVC-kattega võrk","Postid, pingutustraat ja kinnitused","Sobib ka kaldega aiajoonele","Jalg- ja sõiduväravad samas lahenduses","Vana võrkaia eemaldus kokkuleppel"],
 "types_tag":"Rullvõrgu lahendused","types_h":"Pingutus, nurgad ja kaldega aiajoon",
 "types":[("luxaed-rullvork-corner-v1","Punutud rullvõrkaia tugevdatud nurgapost ja pingutustraadid — illustratiivne näidis","◇","Paigaldus","Tugevdatud nurgad","Punutud rullvõrk pingutatakse sirgete lõikude kaupa. Nurga- ja lõpp-postid toestatakse ning üla- ja alaserva lisatakse pingutustraat, et võrk säilitaks kuju.",["Tugevdatud nurgapost","Üla- ja alapingutus","Tsink + PVC-kate"]),("luxaed-rullvork-slope-v1","Punutud rullvõrkaed kaldega aiajoonel — illustratiivne näidis","◇","Reljeef","Rullvõrk kaldega krundil","Painduv rullvõrk järgib mõõdukat kõrguste vahet paremini kui jäik sektsioon. Postide samm ja võrgu pingutus valitakse pärast aiajoone mõõdistamist.",["Paindlik reljeefil","Postide samm mõõdistuse järgi","Ühtlane pingutus"])],
 "variants_h":"Võrgu, katte ja väravate valik","variants":[("▦","Keevitatud rullvõrk","Ristumiskohtades keevitatud, korrapärase silmaga rullvõrk jätab sirgema mulje, kuid on endiselt paindlikum kui jäik 2D/3D-võrgusektsioon."),("◧","Tsink ja PVC-kate","Valime traadi läbimõõdu, silmasuuruse ning tsingitud või tsingitud ja PVC-kattega viimistluse kasutuskoha järgi."),("⛩","Väravad","Valmistame rullvõrkaia juurde jalg-, tiib- või liugvärava ning vajaduse korral paigaldame automaatika.")],
 "visual_note":"Pildid on fotorealistlikud lahenduse illustratsioonid. Valmis LuxAedi objektide galeriisse lisame ainult meie enda tööde fotod.",
 "cta_band":"Arvutame rullvõrkaia lahenduse teie krundile","incl":["Krundi ja aiajoone mõõdistus","Postide paigaldus ja loodimine","Võrgu kinnitamine ja pingutamine","Nurkade ning lõpp-punktide tugevdamine","Valmis aia kontroll"],
 "factors":["Aia pikkus ja kõrgus","Punutud või keevitatud rullvõrk","Traadi läbimõõt ja pinnakate","Nurkade, postide ja väravate arv","Reljeef, pinnas ja vana aia eemaldus"],
 "local_h":"Rullvõrkaia paigaldus Tallinnas ja Harjumaal","local_p":"Paigaldame rullvõrkaedu Tallinnas ja kogu Harjumaal. Mõõdistusel arvestame aiajoone, nurkade, pinnase ja kõrguste vahega, et valida postide samm ning võrgu pingutamise lahendus.",
 "gallery":[],"form_service":"aed","form_material":"Rullvõrkaed",
 "faq":[("Mis vahe on rullvõrkaial ja 2D/3D-võrkaial?","Rullvõrk paigaldatakse rullist ja pingutatakse postide vahel. 2D/3D-võrkaed koosneb jäikadest keevisvõrgust sektsioonidest ning on üldjuhul jäigem. Rullvõrkaed sobib sageli paremini pika aiajoone ja väiksema eelarve korral."),("Kas rullvõrkaed vajab hiljem pingutamist?","Õigesti paigaldatud võrk püsib pingul, kuid pinnase liikumise, löökide või tugeva koormuse järel võib mõni lõik vajada järelpingutamist."),("Kas rullvõrkaed sobib kaldega krundile?","Jah. Rullvõrk järgib reljeefi paremini kui jäik võrgusektsioon. Mõõdistusel vaatame üle kõrguste vahed ning postide asukohad."),("Kas valida tsingitud või tsingitud ja PVC-kattega võrk?","Mõlemad lahendused sobivad välitingimustesse. PVC-kate lisab tsingitud terastraadile kaitsekihi ja võimaldab valida näiteks rohelise või musta tooni. Valik sõltub soovitud välimusest ja eelarvest."),("Kas paigaldate ka väravad?","Jah. Valmistame rullvõrkaia juurde jalgvärava, tiibvärava või liugvärava ning vajaduse korral paigaldame automaatika.")]},
"/aiad/puitaed/":{
 "form_service":"aed","form_material":"Puit",
 "intro_p":"Puit näeb väärikas ja looduslik välja ning sobib eri stiiliga kruntidele. Õigesti valitud teraskarkass, laudade vahe ja pinnatöötlus aitavad aial kuju säilitada ning lihtsustavad hooldust.",
 "bens":["Töödeldud puit Eesti kliima jaoks","Teraskarkass aitab aial kuju säilitada","Horisontaalne, vertikaalne või ribiline","Aed ja väravad ühes stiilis","Võimalik väravaautomaatika","Individuaalne disain"],
 "local_h":"Puitaedade valmistamine Tallinnas ja Harjumaal","local_p":"Valmistame puitaedu Tallinnas ja Harjumaal. Objektil täpsustame laudise suuna ja vahe, teraskarkassi, pinnakatte ning väravate lahenduse."},
"/aiad/metallaed/":{
 "name":"Metallaed ja varbaed","hero":"luxaed-varbaed-gate-v2","og":"/img/luxaed-varbaed-gate-v2.jpg",
 "title":"Metallaia ja varbaia paigaldus Tallinnas — LuxAed","desc":"Metall- ja varbaedade valmistamine ning paigaldus Tallinnas ja Harjumaal. Keevitatud sektsioonid, väravad, tsinkimine ja RAL-toonid.",
 "kicker":"Metallaed · varbaed · metallpiire","h1":"Metall- ja varbaedade<br><em>paigaldus</em>",
 "lead":"Keevitatud terasprofiilidest tugev ja esinduslik piire. Valmistame lihtsa joonega varbaedu, dekoratiivseid metallpiirdeid ning aiaga sobivaid väravaid.",
 "intro_h":"Metallaed vastavalt teie krundile","intro_p":"Metallaia sektsioonid valmistatakse objekti mõõtude ja soovitud kujunduse järgi. Valida saab varbade profiili, vahe, kõrguse, ülaserva ja dekoratiivdetailid. Pinnakaitse, näiteks tsinkimine ja pulbervärvimine, valitakse vastavalt projektile ning kasutuskohale.",
 "bens":["Keevitatud metallsektsioonid","Valitav varbade profiil ja vahe","Sirge või dekoratiivne ülaserv","Tsingitud ja värvitud pinnalahendused","RAL-värvitoonid","Väravad ja jalgväravad samas stiilis"],
 "types_tag":"Metallaia valikud","types_h":"Varbaed, väravad ja konstruktsioon",
 "types":[("luxaed-varbaed-gate-v2","Sirge joonega must varbaed ja jalgvärav — illustratiivne näidis","▥","Metallaed","Klassikaline varbaed","Vertikaalsetest terasprofiilidest keevitatud sektsioonid. Varbade vahe, profiil ja kõrgus valitakse vastavalt soovitud läbipaistvusele ning aia kasutusele.",["Keevitatud terasprofiil","Valitav vahe ja kõrgus","RAL-värvitoonid"]),("luxaed-varbaed-detail-v1","Varbaia värava raam, keevisliited ja lukk — illustratiivne näidis","⚙","Detailid","Värav samas konstruktsioonis","Jalg-, tiib- või liugvärava raam, varbade jaotus ja pinnakaitse kavandatakse aiaga üheks tervikuks. Furnituur valitakse värava mõõtude ning kasutussageduse järgi.",["Aed ja värav ühes stiilis","Keevitatud raam","Sobiv lukk ja furnituur"])],
 "variants_h":"Disain, väravad ja pinnakaitse","variants":[("✦","Dekoratiivne metallaed","Sirgete või kujundatud detailidega metallpiiret saab kombineerida plokkpostide, sokli ja väravatega."),("⛩","Metallväravad","Liug-, tiib- ja jalgväravad valmistame aiaga samast profiilist ning samas värvitoonis. Sõiduväravale lisame sobiva automaatika."),("◧","Pinnakaitse","Tsingi- ja värvkattesüsteem valitakse vastavalt konstruktsioonile, keskkonnale ning soovitud RAL-toonile.")],
 "visual_note":"Pildid on fotorealistlikud lahenduse illustratsioonid. Valmis LuxAedi objektide galeriisse lisame ainult meie enda tööde fotod.",
 "cta_band":"Kavandame metallaia teie maja ja krundi järgi","incl":["Objekti mõõdistus","Sektsioonide valmistamine vastavalt tellimusele","Postide ning sektsioonide paigaldus","Furnituuri ja viimistluse kontroll","Valmis aia üleandmine"],
 "factors":["Aia pikkus ja kõrgus","Varbade profiil, vahe ja kujundus","Pinnakaitse ja RAL-toon","Postid, sokkel ning dekoratiivdetailid","Väravad, automaatika ja reljeef"],
 "local_h":"Metall- ja varbaiad Tallinnas ning Harjumaal","local_p":"Valmistame metall- ja varbaedu Tallinnas ning Harjumaal objekti mõõtude järgi. Kooskõlastame sektsioonide jaotuse, varbade vahe, pinnakaitse ja väravate kujunduse.",
 "gallery":[],"form_service":"aed","form_material":"Metallaed / varbaed",
 "faq":[("Mis vahe on varbaial ja metall-lippaial?","Varbaed valmistatakse tavaliselt jäikadest terasprofiilidest või -varbadest. Metall-lippaed koosneb õhematest profileeritud lamellidest. Mõlemal saab valida vahe, värvi ja väravatega sobiva kujunduse."),("Kas metallaed tsingitakse ja värvitakse?","Pinnakaitse valime projekti järgi. Tsingitud ja õigesti värvitud pind aitab kaitsta terast korrosiooni eest, kuid lõplik süsteem sõltub konstruktsioonist ja kasutuskohast."),("Kas teete dekoratiivseid metallaedu?","Jah. Saame kasutada lihtsat sirget joont või dekoratiivseid detaile ning kombineerida metallsektsioone plokkpostide ja sokliga."),("Kas väravad saab teha samas stiilis?","Jah. Valmistame liug-, tiib- ja jalgväravad sama profiili, jaotuse ja värvitooniga ning lisame vajaduse korral automaatika.")]},
"/aiad/lippaed/":{
 "form_service":"aed","form_material":"Metall-lippaed",
 "desc":"Horisontaalne või vertikaalne metall-lippaed Tallinnas ja Harjumaal. Tsingitud ja värvkattega metall-lipid, valitav vahe ja RAL-toon. Tasuta mõõdistus.",
 "kicker":"Metall-lippaed · metallist aialipid",
 "lead":"Horisontaalsete või vertikaalsete metall-lippidega kaasaegne piire. Valida saab lippide vahe, ühe- või kahepoolse paigutuse ning värvitooni.",
 "intro_p":"Metallist lippaed mõjub kerge ja kaasaegsena ning sobib nii eramule kui ka ettevõtte territooriumile. Tsingitud ja värvkattega lamellid on nõuetekohase paigalduse ning hoolduse korral pika kasutuseaga. Aia ja väravad teeme ühes stiilis.",
 "bens":["Horisontaalne või vertikaalne paigutus","Valitav vahe metall-lippide vahel","Tsingitud ja värvkattega pind","RAL-värvid, ka antratsiit RAL 7016","Aed ja väravad ühes stiilis","Ühe- või kahepoolne lahendus"],
 "types":[("luxaed-w-lippaed-1","Grafiithall horisontaalne metall-lippaed","▤","Lippaia suund","Horisontaalne metall-lippaed","Horisontaalsed metall-lipid annavad aiale modernse joone. Lippide vahe valitakse soovitud õhulisuse ja privaatsuse järgi.",["Modernne joon","Valitav lippide vahe","Tsink + värvkate"]),("luxaed-w-gates-picket","Vertikaalne metall-lippaed ja liugvärav LuxAedi objektil","▥","Lippaia suund","Vertikaalne metall-lippaed","Vertikaalsed profileeritud metall-lipid annavad aiale klassikalise joone. Ühe- või kahepoolse paigutusega saab muuta aia läbipaistvust ning värava valmistame sama jaotuse ja tooniga.",["Klassikaline suund","Ühe- või kahepoolne","Väravad samas stiilis"]),("luxaed-w-lippaed-3","Pruun metall-lippaed lähivaates","◧","Värvid","RAL-toonid ja pinnakate","Populaarsed on antratsiit RAL 7016, pruun, hall ja must. Tsingitud ning kvaliteetse värvkattega pind aitab kaitsta terast korrosiooni eest.",["Antratsiit RAL 7016","Pruun, hall ja must","Korrosioonikaitse"])],
 "visual_note":None,
 "local_h":"Metall-lippaiad Tallinnas ja Harjumaal","local_p":"Paigaldame metall-lippaedu Tallinnas ja Harjumaal. Mõõdistusel valime metall-lippide suuna ja vahe, ühe- või kahepoolse paigutuse, RAL-tooni ning sobivad väravad.",
 "faq":[("Mis on metall-lippaed (nn štaketnik)?","Metall-lippaed koosneb tsingitud ja värvkattega metall-lippidest. Lipid võivad paikneda horisontaalselt või vertikaalselt ning nende vahe valitakse soovitud privaatsuse järgi."),("Kas lippaed on läbipaistev?","Metall-lippide vahe valite ise: tihedam paigutus annab rohkem privaatsust ja hõredam kergema ilme. Kahepoolne lippaed on vähem läbipaistev."),("Millised värvid on saadaval?","Populaarsed on antratsiit RAL 7016, must, hall ja pruun. Teisi RAL-toone pakume vastavalt valitud tootele."),("Kas väravad saab teha samas stiilis?","Jah. Valmistame liug- ja tiibväravad sama paigutuse, metall-lippide ning värvitooniga nagu aia.")]},
"/varavad/":{
 "form_service":"varav","form_material":"",
 "hero":"luxaed-auto-2","og":"/img/luxaed-auto-2.jpg",
 "autotypes":[("luxaed-w-gates-auto","BFT ajam LuxAedi paigaldatud liugväraval","⚙","Automaatika","Liugvärava automaatika","Liugvärava automaatika ühendab ajami, juhtimise ja turvaseadmed. Ajami valime värava kaalu, laiuse ning kasutussageduse järgi; komplekti täpsustame vastavalt objektile.",["Ajami valik kaalu järgi","Juhtimine ja turvaseadmed","BFT / Nice / CAME"]),("luxaed-g6","Tiibvärava hoobajam","⚙","Automaatika","Tiibvärava automaatika","Tiibvärava automaatika kasutab hoob- või kruviajameid mõlemale tiivale. Ajami tüüp ja tööparameetrid valitakse värava mõõtude, kaalu ning konstruktsiooni järgi.",["Hoob- või kruviajam","Seadistus värava järgi","Mõlemale tiivale"]),("luxaed-barrier-guide","Automaatne tõkkepuu sissesõidul","⊤","Automaatika","Tõkkepuu","Tõkkepuu on automaatne piirdepoom sissesõidu või parkla juhtimiseks. Sobib korteriühistutele, parklatele ja territooriumidele.",["Parklad ja ühistud","Pult või kood","Kontrollitud läbipääs"]),("luxaed-reel-domofon-poster","Hikvisioni domofon väraval","🔔","Automaatika","Fonolukk ja videopaneel","Fonolukk (domofon) ja videopaneel avavad värava ja jalgvärava kaugelt. Näete külalist ekraanil või telefonis ja avate värava ühe puudutusega.",["Video ja kõne","Kaugjuhtimine","Värava avamine"],"left center")],
 "local_h":"Väravad ja automaatika Tallinnas ning Harjumaal","local_p":"Valmistame ja paigaldame väravaid Tallinnas ning Harjumaal. Mõõdistame ava, külgruumi ja kalde ning valime värava konstruktsiooni, ajami ja juhtimise kasutussageduse järgi."},
"/aia-remont/":{
 "title":"Piirdeaia ja värava remont Tallinnas — LuxAed","desc":"Piirdeaia, värava ja automaatika remont Tallinnas ja Harjumaal: sektsioonid, postid, hinged, rullikud, ajamid ja diagnostika.",
 "hero":"luxaed-repair-real-v1","og":"/img/luxaed-repair-real-v1.jpg",
 "form_service":"remont","form_material":"","process_h":"Remont nelja selge sammuga",
 "process":[("Saatke kirjeldus ja fotod","Kirjeldage probleemi ning lisage võimalusel fotod aiast, väravast või automaatikast. Nii saame enne väljasõitu töö ulatusest parema ülevaate."),("Teeme diagnostika","Kontrollime sektsioone, poste, hingi, rullikuid, lukke, ajamit ja turvaseadmeid vastavalt probleemile."),("Kooskõlastame lahenduse","Selgitame, mida saab remontida ja mida on mõistlik vahetada. Lepime enne töö algust kokku materjalid, hinna ja ajakava."),("Remondime ja kontrollime","Vahetame või reguleerime vajalikud osad ning kontrollime pärast remonti värava liikumist, kinnitusi ja automaatika ohutust.")],
 "local_h":"Aia ja värava remont Tallinnas ning Harjumaal","local_p":"Töötame Tallinnas ja kogu Harjumaal. Esmase hinnangu jaoks saatke fotod ning aadress; vajaduse korral tuleme objektile, teeme diagnostika ja kooskõlastame töö enne remondi alustamist.",
 "price_lead":"Remondi hind sõltub vea põhjusest, ligipääsust ja vajalikest detailidest. Esmase hinnangu anname kirjelduse ning fotode põhjal; täpse töömahu ja hinna kooskõlastame pärast ülevaatust või diagnostikat.",
 "incl":["Rikke või kahjustuse ülevaatus","Töö ulatuse ja hinna kooskõlastamine","Kokkulepitud remonditööd","Reguleerimine või detailide vahetus vastavalt pakkumisele","Töö kontroll pärast remonti"],
 "video_h":"Vaata vana betoonposti eemaldamist",
 "gallery_h":"Remonditööde ja detailide näited","gallery":[("luxaed-repair-real-v1","Vana betoonposti eemaldamine LuxAedi remonditööl"),("luxaed-w-crew","Meister objektil"),("luxaed-w-lock-black","Värava lukk ja käepide"),("luxaed-w-gates-auto","Liugvärava BFT ajam")],
 }
}

NEW_ETSERV=[
{"path":"/aiad/paneelaed/","videos":[("luxaed-reel-vorkaed","3D-võrkaed — valmis objekt"),("luxaed-reel-vorkaed2","Vana rullvõrkaia asendamine 3D-võrkaiaga")],"name":"2D- ja 3D-keevisvõrkaed","hero":"luxaed-w-mesh-1","og":"/img/luxaed-w-mesh-1.jpg",
 "title":"2D- ja 3D-võrkaedade paigaldus Tallinnas — LuxAed","desc":"2D- ja 3D-keevisvõrkaedade paigaldus Tallinnas ja Harjumaal. Jäigad võrgusektsioonid, postid, aluslauad, väravad ja koeraaedikud. Tasuta mõõdistus.",
 "kicker":"Keevisvõrkaed · 2D · 3D","h1":"2D- ja 3D-võrkaedade<br><em>paigaldus</em>",
 "lead":"Jäikadest keevisvõrgust sektsioonidest korralik piire eramule, korteriühistule või ettevõtte territooriumile. Valime 2D- või 3D-võrgusektsiooni vastavalt kasutuskohale ja soovitud jäikusele.",
 "intro_h":"Miks valida 2D/3D-keevisvõrkaed","intro_p":"Erinevalt rullvõrgust on 2D- ja 3D-võrk keevitatud jäikadeks sektsioonideks. 3D-võrgusektsioon saab jäikuse V-kujulistest painetest. 2D-võrgusektsioon on sile ning selle vertikaaltraate toetavad topelt-horisontaaltraadid. Lõplik tugevus sõltub traadi läbimõõdust, postidest, kinnitustest ja paigaldusest.",
 "bens":["Jäigad 2D- ja 3D-keevisvõrgust sektsioonid","Tsingitud või värvkattega lahendused","Eri kõrgused ja värvitoonid","Postid, kinnitused ja aluslauad","Väravad sama võrktäitega","Koeraaedikud ja territooriumipiirded"],
 "types_tag":"2D või 3D","types_h":"2D- ja 3D-võrkaia erinevused",
 "types":[("luxaed-w-mesh-1","Antratsiit 3D-võrkaed heki ääres","3D","Keevisvõrk","3D-võrkaed","Keevitatud võrgu V-kujulised painutused lisavad sektsioonile jäikust ja annavad profileeritud ilme. Praktiline valik eramute ja tavapäraste territooriumide piiramiseks.",["V-kujulised painutused","Praktiline valik","Eri kõrgused"]),("luxaed-paneelaed-2d-v1","2D-võrkaia lahenduse näidis topelt-horisontaaltraatidega","2D","Keevisvõrk","2D-võrkaed","Sile keevisvõrgust sektsioon ühe vertikaaltraadi ning topelt-horisontaaltraatidega. Võrreldava kõrguse ja traadimõõdu korral on 2D-võrk üldjuhul jäigem ning sobib suurema koormusega aladele.",["Topelt-horisontaaltraat","Sile sektsioon","Suurem jäikus"])],
 "variants_h":"Postid, aluslauad ja erilahendused","variants":[("▤","Aiapostid ja kinnitused","Valime postide profiili, sammu ja kinnitused võrgusektsiooni kõrguse, pinnase ning koormuse järgi."),("▱","Aluslaud","Betoonist aluslaud aitab hoida pinnast ja jätab aia alumise serva viimistletuks."),("⌗","Koeraaedik ja territoorium","Jäigast keevisvõrgust saab ehitada tugeva koeraaediku või piiritleda ettevõtte territooriumi.")],
 "visual_note":"2D-võrgu pilt on konstruktsiooni illustratsioon; 3D-võrkaia fotod ja galerii on LuxAedi objektid.",
 "cta_band":"Valime teie krundile sobiva keevisvõrkaia","incl":["Aiajoone mõõdistus","Postide paigaldus ja loodimine","Võrgusektsioonide ning kinnituste montaaž","Reljeefi ja kõrguste vahe arvestamine","Valmis aia kontroll"],
 "factors":["Aia pikkus ja võrgusektsioonide kõrgus","2D- või 3D-võrk ja traadimõõt","Postide ning kinnituste tüüp","Aluslauad, väravad ja koeraaedikud","Reljeef ja vana aia eemaldus"],
 "local_h":"2D- ja 3D-võrkaiad Tallinnas ning Harjumaal","local_p":"Paigaldame 2D- ja 3D-keevisvõrkaedu Tallinnas ning Harjumaal. Võrgusektsioonide kõrguse, postid, kinnitused ja võimaliku aluslaua valime kasutusotstarbe, reljeefi ning väravate järgi.",
 "form_service":"aed","form_material":"2D/3D keevisvõrkaed",
 "gallery":[("luxaed-w-mesh-1","Antratsiit 3D-võrkaed heki ääres"),("luxaed-w-mesh-2","Roheline 3D-võrkaed"),("luxaed-3d-mesh-video-v1","Valmis 3D-võrkaed LuxAedi videost"),("luxaed-w-mesh-gate","Jalgvärav keevisvõrgust"),("luxaed-mesh-gate","Keevisvõrgust värav ja LuxAedi buss"),("luxaed-w-gates-green","Tiibväravad keevisvõrktäitega"),("luxaed-w-gates-graphite","Grafiithall keevisvõrktäitega värav"),("luxaed-w-mesh-detail","Võrgusektsiooni kinnitus postile"),("luxaed-w-panels","3D-võrgusektsioonid enne paigaldust")],
 "faq":[("Mis vahe on 2D- ja 3D-võrkaial?","3D-võrgul on V-kujulised painutused, mis annavad sektsioonile jäikust. 2D-võrk on sile ja topelt-horisontaaltraatidega. Võrreldavate mõõtude korral on 2D tavaliselt jäigem, kuid valik sõltub kasutuskohast ja eelarvest."),("Kas 3D-võrkaed sobib eramule?","Jah. 3D-võrk on praktiline valik eramule, suvilale ja tavapärase koormusega territooriumile. Valime sobiva kõrguse, traadi ning postid."),("Kas 3D-võrkaed ja 3D-paneelaed tähendavad sama lahendust?","Jah. Tootjad ja müüjad kasutavad jäiga keevisvõrgust sektsiooni kohta ka nimetusi 3D-paneel ja keevispaneelaed. Materjal on keevitatud terastraadist võrk; paneel tähendab siin ainult jäiga sektsiooni kuju."),("Millest keevisvõrkaia tugevus sõltub?","Tugevust ei määra üksnes tähis 2D või 3D, vaid ka traadi läbimõõt, võrgusektsiooni kõrgus, postide profiil, kinnitused, pinnas ja paigaldus."),("Kas keevisvõrkaiale saab lisada aluslaua?","Jah. Betoonist aluslaud aitab hoida pinnast, lihtsustab serva hooldust ja jätab aia viimistletuks."),("Kas väravad saab teha sama keevisvõrguga?","Jah. Valmistame jalg-, tiib- ja liugväravad sama võrktäite ning värvitooniga, sõiduväravale lisame sobiva automaatika.")]},
{"path":"/aiad/profiilplekk-aed/","name":"Profiilplekk-aed","hero":"luxaed-profnastil-2","og":"/img/luxaed-profnastil-2.jpg",
 "title":"Profiilplekk-aia paigaldus Tallinnas ja Harjumaal — LuxAed","desc":"Profiilplekk-aedade valmistamine ja paigaldus Tallinnas ja Harjumaal. Tsingitud ja pinnakattega terasplekk, metallkarkass, plokkpostid ning väravad.",
 "kicker":"Profiilplekk · kinnine aed","h1":"Profiilplekk-aedade<br><em>paigaldus</em>",
 "lead":"Vähe läbipaistev ja praktiline piire, kui soovite hoovi rohkem eraldada. Valmistame metallkarkassi, paigaldame profiilpleki ning teeme väravad aiaga samas toonis.",
 "intro_h":"Millal valida profiilplekk-aed","intro_p":"Profiilplekist aed piirab vaadet ning aitab vähendada tuule ja tänavatolmu mõju. Kuna kinnisele aiale mõjub suurem tuulekoormus kui avatud piirdele, valime postide profiili, sammu ja paigaldussügavuse aia kõrguse, pinnase ning asukoha järgi.",
 "bens":["Kinnine ja vähe läbipaistev lahendus","Tsingitud ja pinnakattega terasplekk","Metallkarkass ja tugevdatud postid","Eri profiilid ja värvitoonid","Võimalik kombineerida plokkpostidega","Väravad sama täite ja tooniga"],
 "types_tag":"Profiilplekk-aia valikud","types_h":"Karkass, postid ja väravad",
 "types":[("luxaed-profnastil-2","Pikk hall profiilplekk-aed","▦","Kinnine piire","Profiilplekk metallpostidel","Metallpostidele ja -lattidele kinnitatud profiilplekk on praktiline kinnine piire. Postide profiil ning samm valitakse aia kõrguse, pinnase ja tuulekoormuse järgi.",["Metallkarkass","Eri profiilid ja toonid","Tuulekoormuse arvestus"]),("luxaed-profnastil-gate","Profiilplekk-tiibväravad","⛩","Väravad","Väravad sama täitega","Liug-, tiib- ja jalgväravad valmistame aiaga samas toonis ning sama profiilplekiga. Sõiduväravale valime sobiva automaatika.",["Liug- või tiibvärav","Sama täide ja toon","Automaatika"])],
 "variants_h":"Postid, toonid ja kombineeritud lahendused","variants":[("▣","Plokkpostid ja sokkel","Profiilplekki saab kombineerida plokkpostide või madala sokliga, kui soovite massiivsemat ja viimistletud tulemust."),("◧","Profiil ja värvitoon","Valime pleki profiili, paksuse ja pinnakatte vastavalt välimusele, kasutuskohale ning eelarvele."),("↔","Kombineeritud aed","Kinniseid lõike saab ühendada metall-lippaia, varbaia või 3D-võrkaiaga vastavalt krundi eri külgede vajadusele.")],
 "cta_band":"Arvutame profiilplekk-aia teie krundile","incl":["Krundi ja aiajoone mõõdistus","Postide ning metallkarkassi paigaldus","Profiilpleki lõikamine ja kinnitamine","Servade ning liitekohtade viimistlus","Valmis aia kontroll"],
 "factors":["Aia pikkus ja kõrgus","Pleki profiil, paksus ja pinnakate","Metall- või plokkpostid","Tuulekoormus ja pinnas","Väravad, jalgväravad ja vana aia eemaldus"],
 "local_h":"Profiilplekk-aiad Tallinnas ja Harjumaal","local_p":"Paigaldame profiilplekk-aedu Tallinnas ja Harjumaal. Kinnise piirde puhul arvestame eriti aia kõrguse, asukoha, pinnase ning tuulekoormusega.",
 "form_service":"aed","form_material":"Profiilplekk-aed",
 "gallery":[("luxaed-profnastil-2","Pikk hall profiilplekk-aed"),("luxaed-profnastil-gate","Profiilplekk-tiibväravad"),("luxaed-svc-profnastil","Profiilplekk-värava täide")],
 "faq":[("Kas profiilplekk-aed peab tugevale tuulele vastu?","Kinnise aia konstruktsioon valitakse kõrguse, asukoha, pinnase, postide profiili ja sammu järgi. Mõõdistusel hindame tuulekoormust mõjutavaid tingimusi ning dimensioneerime karkassi vastavalt."),("Kas profiilplekk pleegib või roostetab?","Tsingitud alus ja kvaliteetne pinnakate aitavad värvitoonil säilida ning vähendavad korrosiooniriski. Lõikeservad ja võimalikud pinnakahjustused tuleb õigesti töödelda."),("Kas profiilplekk-aed vähendab müra?","Kinnine piire võib mõnevõrra vähendada otsest tänavamüra, kuid tavaline profiilplekk-aed ei ole sertifitseeritud müratõke."),("Kas profiilplekki saab kombineerida plokkpostidega?","Jah. Valmistame kombineeritud lahendusi, kus profiilplekk paikneb plokkpostide või madala sokli vahel."),("Kas väravad saab teha samas toonis?","Jah. Valmistame liug-, tiib- ja jalgväravad sama profiilpleki ning värvitooniga ja lisame sõiduväravale sobiva automaatika.")]}
]

for c in ETSERV:
    c.update(ET_OVERRIDES.get(c["path"],{}))
ETSERV.extend(NEW_ETSERV)

assert_service_coverage("et", [c["path"] for c in ETSERV])
for c in ETSERV:
    write_service("et", c)
print("ET services done:", len(ETSERV))
