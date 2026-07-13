#!/usr/bin/env python3
# Estonian tree: / home, service pages, support pages. Targets ET keywords.
import json, html
from build_pages import head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN, SVC, reel_strip

def form_html():
    chips=[("aed","Aed"),("varav","Värav"),("automaatika","Automaatika"),("remont","Remont")]
    ov='<svg class="chip-oval" viewBox="0 0 220 64" preserveAspectRatio="none" aria-hidden="true"><path d="M40 16C92 5 158 6 196 18 215 24 210 49 172 56 110 66 48 64 20 50 7 43 12 17 50 11 78 7 104 9 126 13"/></svg>'
    ch="".join(f'<button type="button" class="chip" data-svc="{s}">{ov}{t}<span class="chip-tick" aria-hidden="true">✓</span></button>' for s,t in chips)
    return f'''<div class="form-slot"><div class="form-card" id="form">
  <span class="form-tag">Küsi pakkumist</span>
  <h2>Mida on vaja teha? <span class="pick-hint">(vali)</span></h2>
  <form id="leadForm">
    <input type="hidden" name="service" id="serviceField">
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:0;top:0;width:1px;height:1px;opacity:0;overflow:hidden">
    <div class="chips" id="svcChips" role="group">{ch}</div>
    <div class="ff" data-svc="aed"><select name="material" class="form-select" aria-label="Aia materjal"><option value="">Aia materjal</option><option>Puit</option><option>Profiilplekk</option><option>Võrkaed (keevispaneel)</option><option>Ei tea, soovitage</option></select></div>
    <div class="ff form-grid2" data-svc="aed"><input type="text" name="length" inputmode="numeric" placeholder="Pikkus, m"><select name="height" class="form-select" aria-label="Kõrgus"><option value="">Kõrgus</option><option>kuni 1,5 m</option><option>1,5–2 m</option><option>üle 2 m</option></select></div>
    <div class="ff" data-svc="varav,automaatika"><select name="gate_type" class="form-select" aria-label="Värava tüüp"><option value="">Värava tüüp</option><option>Lükandvärav</option><option>Tiibvärav</option><option>Ei tea</option></select></div>
    <div class="ff" data-svc="varav"><select name="automation" class="form-select" aria-label="Automaatika?"><option value="">Automaatika?</option><option>Automaatikaga</option><option>Ilma automaatikata</option><option>Ei tea</option></select></div>
    <div class="ff form-grid2"><select name="plot" class="form-select" aria-label="Krunt"><option value="">Krunt</option><option>Tasane</option><option>Kaldega</option><option>Vana aed (lammutus)</option><option>Ei tea</option></select><select name="timeline" class="form-select" aria-label="Millal?"><option value="">Millal?</option><option>Võimalikult kiiresti</option><option>1–3 kuu jooksul</option><option>Lihtsalt hind teada</option></select></div>
    <div class="ff-base"><input type="text" name="address" placeholder="Krundi aadress (linn / piirkond)"></div>
    <div class="form-grid">
      <input type="text" name="name" placeholder="Teie nimi *" required style="grid-column:1/-1">
      <input type="tel" name="phone" placeholder="Telefon *" required>
      <input type="email" name="email" placeholder="E-post *" required>
    </div>
    <div class="ff"><textarea name="msg" placeholder="Kommentaar: detailid, soovid, mida remontida..."></textarea></div>
    <label class="photo-upload ff" id="photoLabel"><input type="file" name="photos" accept="image/*" multiple id="photoInput" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);border:0"><svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg><span id="photoLabel-txt">Lisa foto (valikuline)</span></label>
    <button class="btn btn-accent" type="submit" style="width:100%;padding:13px;font-size:15px">Saada päring →</button>
    <p class="form-consent">Vormi saates nõustud <a href="/privaatsus/">privaatsuspoliitikaga</a> ja <a href="/tingimused/">tingimustega</a></p>
    <div class="form-ok" id="formOk" role="status"><b>Aitäh, päring on vastu võetud.</b><br>Võtame teiega peagi ühendust.</div>
  </form>
</div></div>'''

PROCESS='''<div class="hsteps">
  <div class="hstep"><div class="hstep-num">1</div><h3>Jätke päring</h3><p>Üks kõne või sõnum, ja võtame kogu töö enda peale. Tuleme tasuta mõõdistusele teile sobival ajal.</p></div>
  <div class="hstep"><div class="hstep-num">2</div><h3>Leiame sobiva lahenduse</h3><p>Pakume materjali ja lahenduse teie krundi ja eelarve järgi ning ütleme täpse hinna. Ilma üllatusteta.</p></div>
  <div class="hstep"><div class="hstep-num">3</div><h3>Paigaldame korralikult</h3><p>Paigaldame postid, sektsioonid, väravad ja automaatika. Hoiame teid kursis igal etapil.</p></div>
  <div class="hstep"><div class="hstep-num">4</div><h3>Anname töö üle</h3><p>Pärast tööde lõppu vaatame tulemuse koos teiega üle ja anname valmis objekti üle. Koos hooldussoovitustega.</p></div>
</div>'''

VARUSTUS='''<section class="section"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Varustus</span><h2 class="big">Õige tehnika, kogenud meeskond, korralik tulemus.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-w-van.webp"><img src="/img/luxaed-w-van.jpg" width="750" height="563" alt="LuxAedi buss objektil" loading="lazy"></picture></div>
  <div class="equip-body"><ul class="spec">
    <li><b>Postiaugupuur ja rammer</b>: postid saavad kindlalt ja loodi maasse</li>
    <li><b>Keevis- ja lõiketööd kohapeal</b>: teraskarkassid ja väravaraamid</li>
    <li><b>Loodimine ja mõõtmine</b>: sektsioonid ühes joones, ka kaldega krundil</li>
    <li><b>Automaatika ja domofonid</b>: seadistame ja ühendame võtmed kätte</li>
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
        return (f'<div class="gtype"><div class="gtype-img"><span class="gtype-badge"><span class="gt-ic">{ic}</span>{eb}</span>'
                f'<picture><source type="image/webp" srcset="/img/{im}.webp"><img src="/img/{im}.jpg" alt="{html.escape(a)}" width="640" height="480" loading="lazy" decoding="async"{st}></picture></div>'
                f'<div class="gtype-txt"><h3>{t}</h3><p>{d}</p><ul class="gtype-specs">{chips}</ul></div></div>')
    return '<div class="gtypes">'+"".join(one(i+1,x) for i,x in enumerate(items))+'</div>'
def gal(imgs): return '<div class="gal" id="gal">'+"".join(f'<a href="/img/{i}.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/{i}.webp"><img src="/img/{i}.jpg" alt="{html.escape(a)}" width="600" height="400" loading="lazy"></picture></a>' for i,a in imgs)+'</div>'
def faqx(fq): return '<div class="faq" id="faqList">'+"".join(f'<div class="faq-item"><button class="faq-q">{q}</button><div class="faq-a"><p>{a}</p></div></div>' for q,a in fq)+'</div>'
def related(cur):
    cc=[(p,t) for p,t in SVC["et"] if p!=cur][:3]
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
    types_sec=f'<section class="section"><div class="wrap"><span class="tag">{c["types_tag"]}</span><h2 class="big">{c["types_h"]}</h2>{gtypes(c["types"])}{_tcta}</div></section>\n' if c.get("types") else ''
    auto_sec=f'<section class="section section--alt"><div class="wrap"><span class="tag">{c.get("autotypes_tag","")}</span><h2 class="big">{c.get("autotypes_h","")}</h2>{gtypes(c["autotypes"])}{cta_band}</div></section>\n' if c.get("autotypes") else ''
    variants_sec=f'<section class="section section--alt"><div class="wrap"><span class="tag">Valikud</span><h2 class="big">{c["variants_h"]}</h2>{cards(c["variants"])}{cta_band}</div></section>\n' if c.get("variants") else ''
    body=f'''{nav("et",c["path"])}
<main id="main">
<section class="hero">
  <div class="hero-photo-bg" style="background:url('/img/{c["hero"]}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap"><div class="hero-grid"><div>
    <div class="hero-kicker hand">Hei! Vajad uut aeda?</div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">34 arvustust Facebookis · soovitavad</a></div>
    <h1>{c["h1"]}</h1>
    <div class="hero-btns"><a class="btn btn-accent" href="#form">Küsi pakkumist →</a><a class="btn btn-ghost" href="tel:{TEL}">Helista {PHONE}</a></div>
  </div>{form_html()}</div>
  <div class="hero-stats"><div class="hstat"><b>100%</b><span>soovitavad Facebookis</span></div><div class="hstat"><b>34</b><span>arvustust</span></div><div class="hstat"><b>15</b><span>aastat meistrite kogemust</span></div></div></div>
</section>
<section class="section"><div class="wrap"><span class="tag">Mida saate</span><h2 class="big">{c["intro_h"]}</h2><p class="lead">{c["intro_p"]}</p>{bens(c["bens"])}</div></section>
{types_sec}{auto_sec}{variants_sec}
<section class="section"><div class="wrap"><span class="tag">Ausalt hinnast</span><h2 class="big">Millest sõltub hind</h2>
  <p class="lead">Fikseeritud hinnakirja ei ole. Täpse hinna ütleme pärast tasuta mõõdistust.</p>
  <div class="honest"><div class="hon good"><h3>Alati sisaldub</h3><ul>{"".join(f"<li>{x}</li>" for x in c["incl"])}<li>Töötame aastaringselt, ka talvel</li><li>Garantii tehtud töödele</li></ul></div>
  <div class="hon bad"><h3>Mõjutab hinda</h3><ul>{"".join(f"<li>{x}</li>" for x in c["factors"])}</ul></div></div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">Kuidas töötame</span><h2 class="big">Neli lihtsat sammu</h2>{PROCESS}</div></section>

<section class="section"><div class="wrap"><span class="tag">Galerii</span><h2 class="big">Tehtud tööde näited</h2>{gal(c["gallery"])}<div style="text-align:center;margin-top:30px"><a class="gal-fb" href="{FB}/photos_by" target="_blank" rel="noopener">Vaata rohkem fotosid Facebookis →</a></div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">KKK</span><h2 class="big">Korduma kippuvad küsimused</h2>{faqx(c["faq"])}</div></section>
<section class="section"><div class="wrap"><span class="tag">Teised teenused</span><h2 class="big">Vaata ka</h2>{related(c["path"])}</div></section>
<section class="cta-final"><div class="wrap"><h2>Ehitame teie <em>unistuste aia</em></h2>
  <p>Jätke päring või helistage.<br>Tuleme tasuta mõõdistusele ja ütleme täpse hinna.</p>
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
 "lead":"Kaasaegsed keevispaneelaiad (3D aiapaneelid) jäikusribidega: tugev, korralik ja hea läbipaistvusega piire. Tsingitud ja pulbervärvitud. Peab aastakümneid.",
 "intro_h":"Miks valida paneelaed","intro_p":"Keevispaneel (3D) hoiab vormi, ei vaju ega paindu tuules ning näeb kaasaegne välja. Selline piirdeaed sobib eramutele, ridaelamutele ja territooriumidele. Paigaldame ka aiaposte ja ehitame koeraaedikuid. Vajaliku materjali valime ja hangime teie eest.",
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
 "gallery":[("luxaed-w-mesh-1","Antratsiit 3D paneelaed heki ääres"),("luxaed-w-mesh-2","3D keevispaneelaed rohelises toonis"),("luxaed-w-mesh-gate","Jalgvärav keevispaneelist"),("luxaed-w-gates-green","Tiibväravad keevispaneelist"),("luxaed-w-mesh-detail","Paneeli kinnitus postile"),("luxaed-w-panels","2D aiapaneelid enne paigaldust"),("luxaed-w-gates-auto","Lükandvärav automaatikaga"),("luxaed-w-gates-night","Paneelväravad õhtuvalguses"),("luxaed-mesh-2","Võrkaed krundi ääres"),("luxaed-w-van","LuxAed meeskond objektil")],
 "faq":[("Võrkaed (aiavõrk) või paneelaed. Kumb valida?","Klassikaline aiavõrk rullis on odav, aga venib ja vajub aja jooksul. Soovitame keevispaneeli või keevisvõrkaeda: sama läbipaistvus, kuid jäik ja korralik. Peab kordades kauem. Arvutame mõlema hinna ja aitame valida."),
        ("Mis vahe on keevisvõrkaial ja keevispaneelaial?","Keevisvõrkaed on tihe keevisvõrk raamil, keevispaneelaed on jäikusribidega paneel. Mõlemad tsingitud ja pulbervärvitud. Paneel on jäigem, võrk soodsam."),
        ("Millised kõrgused on?","Tavaliselt 1,23–2,03 m. Valime kõrguse vajaduse järgi."),
        ("Milline värv valida?","Populaarseimad on antratsiit RAL 7016 ja roheline RAL 6005."),
        ("Kas paigaldate ka aiaposte?","Jah, paigaldame tsingitud aiaposte (metallist aiapostid) koos kübarate ja kinnitusklambritega. Vajaliku materjali hangime ise, nii paneelaia kui muude aedade jaoks."),
        ("Kas teete koeraaedikuid?","Jah, ehitame keevispaneelidest koeraaedikuid ja loomatarasid. Tugevad, turvalised ja pika elueaga."),
        ("Kas saab värava samas toonis?","Jah, teeme lük- ja tiibväravaid sama paneeliga samas värvis.")]},
{"path":"/aiad/puitaed/","video":("luxaed-video-puitvarav","Puidust lükandvärav automaatikaga — valmis objekt"),"name":"Puitaed","hero":"luxaed-svc-wood","og":"/img/luxaed-svc-wood.jpg",
 "title":"Puitaedade ja väravate paigaldus Tallinnas — LuxAed","desc":"Puitaedade ja -väravate valmistamine ja paigaldus Tallinnas ja Harjumaal. Horisontaalne puitaed, teraskarkass, töötlus. Tasuta mõõdistus ja pakkumine.",
 "kicker":"Puit · teraskarkass","h1":"Puitaedade<br><em>paigaldus</em>",
 "lead":"Soe ja korralik välimus. Valmistame puitaedu ja -väravaid tugeval teraskarkassil. Loodusliku puidu ja vastupidava metalli kombinatsioon.",
 "intro_h":"Miks puitaed","intro_p":"Puit näeb väärikas ja looduslik välja ning sobib igale krundile. Teraskarkassil ei vaju konstruktsioon ja peab kaua.",
 "bens":["Töödeldud puit Eesti kliima jaoks","Tugev teraskarkass. Ei vaju","Horisontaalne, vertikaalne või ribiline","Aed ja väravad ühes stiilis","Võimalik väravaautomaatika","Individuaalne disain"],
 "types_tag":"Puitaia tüübid","types_h":"Puitaedade tüübid",
 "types":[("luxaed-svc-wood","Horisontaalne puitaed teraskarkassil","▤","Puitaia tüüp","Horisontaalne puitaed","Horisontaalne puitaed on teraskarkassil horisontaallaudadega aed, kõige populaarsem ja kaasaegsem valik. Laudade vahe valime privaatsuse või õhulisema ilme järgi.",["Teraskarkassil","Valitav laudade vahe","Populaarseim"]),
          ("luxaed-wood-2","Vertikaalne puitaed ja jalgvärav","▥","Puitaia tüüp","Vertikaalne puitaed","Vertikaalne puitaed on püstlaudadega aed, klassikaline ja korralik, vahega või täiskinnine. Sobib nii tänava- kui õuepoolseks piirdeks.",["Püstlauad","Vahega või kinnine","Klassikaline"]),
          ("luxaed-wood-swing-gate-1","Puidust lükandvärav teraskarkassil","⛩","Väravad","Puitväravad","Puitväravad valmistame aiaga ühes stiilis: lükand- või tiibväravad puidutäite ja teraskarkassiga, soovi korral automaatikaga.",["Lükand- või tiibvärav","Aiaga ühes stiilis","Automaatikaga"])],
 "cta_band":"Valime puitaia teie maja juurde","incl":["Krundi mõõdistus","Sektsioonide ja teraskarkassi valmistamine","Postide ja sektsioonide paigaldus","Puidu töötlus ja kate","Kontroll pärast paigaldust"],
 "factors":["Aia pikkus ja kõrgus","Tüüp (horisontaalne, vertikaalne, žalusii)","Puidu liik ja töötlus","Väravad ja automaatika","Reljeef ja alus"],
 "gallery":[("luxaed-svc-wood","Puitaed teraskarkassil"),("luxaed-g1","Puitaed ja lükandvärav"),("luxaed-wood-2","Puitaed krundil"),("luxaed-wood-3","Puitaed ja värav"),("luxaed-g2","Puidust tiibväravad"),("luxaed-g7","Puitaed kivisillutise ääres"),("luxaed-wood-sliding-gate-1","Puidust lükandvärav"),("luxaed-wood-swing-gate-1","Puidust tiibvärav"),("luxaed-g10","Puidust värava lukk"),("luxaed-w-van","LuxAed objektil")],
 "faq":[("Kas puit ei mädane?","Kasutame töödeldud puitu ja katet ning karkass on terasest. Korralik hooldus tagab pika eluea."),
        ("Kas saab horisontaallauad?","Jah, horisontaalne puitaed teraskarkassil on üks populaarsemaid."),
        ("Kas teete väravad samas stiilis?","Jah, valmistame lük- ja tiibväravaid puidutäitega ühises disainis."),
        ("Kas puitaed vajab hooldust?","Perioodiliselt tasub uuendada puidu kaitsekihti. Selgitame, kuidas hooldada.")]},
{"path":"/aiad/metallaed/","name":"Metallaed ja profiilplekk-aed","hero":"luxaed-svc-profnastil","og":"/img/luxaed-svc-profnastil.jpg",
 "title":"Metall- ja profiilplekk-aedade paigaldus Tallinnas — LuxAed","desc":"Metallaed ja profiilplekk-aed Tallinnas ja Harjumaal. Tsingitud plekk, kunstsepis, betoonaiad, eri värvid. Soodne ja kiire. Tasuta mõõdistus.",
 "kicker":"Metall · profiilplekk","h1":"Metall- ja profiilplekk-aedade<br><em>paigaldus</em>",
 "lead":"Praktiline ja soodne lahendus: kinnine aed tsingitud profiilplekist. Täielik privaatsus, tuule- ja tolmukaitse, erinevad värvid.",
 "intro_h":"Miks profiilplekk","intro_p":"Profiilplekk on soodne ja kiiresti paigaldatav. Kinnine aed varjab krundi ja peab kaua tänu tsingile ja polümeerkattele.",
 "bens":["Täielik privaatsus. Kinnine aed","Tsingitud plekk polümeerkattega","Erinevad värvid, ka puidu imitatsioon","Kaitse tuule, tolmu ja müra eest","Kunstsepis ja dekoratiivdetailid","Ka betoon- ja plokkaed massiivseks müüriks"],
 "types_tag":"Metallaia valikud","types_h":"Metallaedade tüübid",
 "types":[("luxaed-profnastil-2","Profiilplekk-aed tsingitud plekist","▦","Metallaia tüüp","Profiilplekk-aed","Profiilplekk-aed on kinnine aed tsingitud plekist polümeerkattega. Täielik privaatsus ning kaitse tuule, tolmu ja müra eest. Saadaval eri värvides, ka puidu imitatsioon.",["Kinnine, privaatne","Tsink + polümeerkate","Eri värvid"]),
          ("luxaed-concrete-tmp","Betoonaed kivi-imitatsiooniga","▣","Massiivne piire","Betoon- ja plokkaed","Betoon- ja plokkaed on massiivne müür privaatsuseks ja müravaigistuseks: betoonpaneelidest kivi-imitatsiooniga või plokkpostidega. Kombineerime seda metalli, pleki või sepisega.",["Massiivne müür","Kivi-imitatsioon","Müra- ja tuulekaitse"]),
          ("luxaed-profnastil-gate","Profiilplekk-tiibväravad","⛩","Väravad","Profiilplekk-väravad","Profiilplekk-väravad valmistame aiaga ühes toonis: lükand- või tiibväravad tsingitud plekist, soovi korral automaatikaga.",["Lükand- või tiibvärav","Aiaga ühes toonis","Automaatikaga"])],
 "cta_band":"Arvutame profiilplekk-aia hinna","incl":["Krundi mõõdistus","Metallpostide ja -lattide paigaldus","Profiilpleki montaaž","Loodimine","Kontroll pärast paigaldust"],
 "factors":["Aia pikkus ja kõrgus","Pleki mark ja värv","Postide tüüp (metall, kivi)","Väravad ja jalgväravad","Reljeef ja alus"],
 "gallery":[("luxaed-svc-profnastil","Profiilplekk-värav"),("luxaed-concrete-tmp","Betoon- ja plokkaed"),("luxaed-profnastil-2","Profiilplekk-aed"),("luxaed-profnastil-gate","Profiilplekk-tiibväravad"),("luxaed-w-lippaed-1","Metall-lippaed grafiithallis"),("luxaed-w-lippaed-2","Hall metall-lippaed"),("luxaed-w-lippaed-3","Pruun metall-lippaed"),("luxaed-w-lock-brown","Värava lukk"),("luxaed-w-lock-black","Värava lukk ja käepide"),("luxaed-w-van","LuxAed objektil")],
 "faq":[("Kas profiilplekk ei pleegi?","Kvaliteetne polümeerkattega plekk hoiab värvi kaua. Kasutame tõestatud materjale."),
        ("Kas valate ka betoon- või plokkaeda?","Jah, ehitame massiivseid betoon- ja plokkmüüre ning kombineerime neid metalli, pleki või sepisega."),
        ("Kas saab kombineerida kivipostidega?","Jah, teeme kombineeritud aedu: profiilplekk kivi- või plokkpostide vahel."),
        ("Kas profiilplekk on odavam kui puit ja võrkaed?","Reeglina jah. Üks soodsamaid lahendusi. Täpse hinna ütleme pärast mõõdistust.")]},
{"path":"/aiad/lippaed/","name":"Metall-lippaed","hero":"luxaed-w-lippaed-1","og":"/img/luxaed-w-lippaed-1.jpg",
 "title":"Metall-lippaedade paigaldus Tallinnas — LuxAed","desc":"Metallist lippaed ehk metallpiire Tallinnas ja Harjumaal: kaasaegne aed valitava vahega, tsingitud ja pulbervärvitud. Tasuta mõõdistus.",
 "kicker":"Metall-lippaed · štaketnik","h1":"Metall-lippaedade<br><em>paigaldus</em>",
 "lead":"Kaasaegne metallist lippaed (euro-lippaed): läbipaistev, korralik ja pika elueaga. Tsingitud ja pulbervärvitud lamellid valitava vahega.",
 "intro_h":"Miks metall-lippaed","intro_p":"Metall-lippaed ehk metallpiire näeb kerge ja kaasaegne välja, laseb valgust läbi ja peab aastakümneid. Sobib eramutele ja ettevõtetele. Aia ja väravad teeme ühes stiilis.",
 "bens":["Kaasaegne läbipaistev lippaed","Valitav vahe lamellide vahel","Tsingitud ja pulbervärvitud. Ei roosteta","RAL-värvid, ka antratsiit RAL 7016","Aed ja väravad ühes stiilis","Ühe- või kahepoolne lamell"],
 "types_tag":"Lippaia valikud","types_h":"Metall-lippaedade tüübid",
 "types":[("luxaed-w-lippaed-1","Grafiithall metall-lippaed","▤","Lippaia tüüp","Metall-lippaed","Metall-lippaed on horisontaalsete lamellidega piire, mis laseb valgust läbi ja näeb kaasaegne välja. Lamellide vahe valite ise: hõredam õhulisuse või tihedam privaatsuse jaoks. Võimalik ühe- või kahepoolne lamell.",["Valitav lamellide vahe","Ühe- või kahepoolne","Tsingitud + pulbervärvitud"]),
          ("luxaed-w-lippaed-3","Pruun metall-lippaed lähivaates","◧","Värvid","Värvid ja RAL-toonid","Lippaia teeme igas RAL-toonis. Populaarseimad on antratsiit RAL 7016, hall ja pruun. Tsingitud ja pulbervärvitud pind ei roosteta ega pleegi.",["Antratsiit RAL 7016","Hall, pruun jt","Ei roosteta"]),
          ("luxaed-w-gates-picket","Lükandvärav lippaiast","⛩","Väravad","Lippaed ja väravad","Väravad teeme sama lippaia lamelliga ja toonis: lükand- ja tiibväravad koos aiaga ühtses stiilis, soovi korral automaatikaga.",["Sama lamell ja toon","Lükand- või tiibvärav","Automaatikaga"])],
 "cta_band":"Arvutame metall-lippaia teie krundile","incl":["Krundi mõõdistus","Metallpostide paigaldus","Lamellide montaaž valitud vahega","Loodimine reljeefi järgi","Kontroll pärast paigaldust"],
 "factors":["Aia pikkus ja kõrgus","Lamelli vahe ja tüüp (ühe-/kahepoolne)","Värv (RAL)","Väravate ja jalgvärava arv","Reljeef ja alus"],
 "gallery":[("luxaed-w-lippaed-1","Grafiithall metall-lippaed"),("luxaed-w-lippaed-2","Hall metall-lippaed maja juures"),("luxaed-w-lippaed-3","Pruun metall-lippaed lähivaates"),("luxaed-w-gates-picket","Lükandvärav lippaiast"),("luxaed-w-lock-brown","Locinox lukk lippaia väraval"),("luxaed-w-van","LuxAed buss objektil")],
 "faq":[("Mis on metall-lippaed (štaketnik)?","Kaasaegne metallist lippaed. Vertikaalsed lamellid valitava vahega, tsingitud ja pulbervärvitud. Läbipaistvam kui plekk-aed, korralik ja pika elueaga."),
        ("Kas lippaed on läbipaistev?","Vahe lamellide vahel valite ise: tihedam privaatsuseks või hõredam kergema ilme jaoks. Kahepoolne lippaed on privaatsem."),
        ("Millised värvid on?","Populaarseim on antratsiit RAL 7016, samuti must ja pruun. Teeme teisi RAL-toone tellimusel."),
        ("Kas väravad tulevad sama moodi?","Jah, lükand- ja tiibväravad teeme samamoodi lippaia lamelliga ühes stiilis.")]},
{"path":"/varavad/","name":"Väravad ja automaatika","hero":"luxaed-auto-2","og":"/img/luxaed-auto-2.jpg","videos":[("luxaed-reel-domofon","Hikvisioni domofon väraval"),("luxaed-reel-varav-oht","Lükandvärav automaatikaga"),("luxaed-video-puitvarav","Lükandvärav ühe nupuvajutusega"),("luxaed-reel-montaaz","Paigaldus objektil")],
 "title":"Liugvärav ja väravaautomaatika paigaldus Tallinnas — LuxAed","desc":"Liugväravad (lükandväravad), tiibväravad ja autoväravad, väravaautomaatika, tõkkepuud ja domofonid Tallinnas ja Harjumaal. Paigaldus võtmed kätte. Tasuta mõõdistus.",
 "kicker":"Liugvärav · tiibvärav · automaatika","h1":"Väravate ja automaatika<br><em>paigaldus</em>",
 "lead":"Liug- ja tiibväravad, autoväravad ja jalgväravad võtmed kätte koos automaatika ja domofonidega. Valmistame, paigaldame ja ühendame. Sõidate õue ühe nupuvajutusega.",
 "intro_h":"Väravaautomaatika igas mahus","intro_p":"Projekteerime, valmistame ja paigaldame väravaid koos automaatikaga võtmed kätte, ühest jalgväravast kuni terve territooriumi sissesõidusüsteemini. Sobitame ajami värava kaalu ja laiuse järgi ning ühendame puldid, domofonid ja turvafotoelemendid.",
 "bens":["Liugvärava ja tiibvärava automaatika igas mahus","Tuntud tootjate ajamid: Nice, CAME, BFT, Sommer, DoorHan","Juhtimine: pult, telefonikõne (GSM), rakendus, kood või RFID","Fotoelemendid ja signaallamp turvaliseks tööks","Aku-varutoide: värav töötab ka elektrikatkestuse ajal","Ujuv (rolling) kood: kaitse puldi pealtkuulamise eest","Domofonid, videopaneelid, tõkkepuud ja garaažiuksed"],
 "types_tag":"Väravatüübid","types_h":"Kõik väravatüübid",
 "types":[("luxaed-w-gates-auto","Liugvärav automaatikaga","⇄","Väravatüüp","Liugvärav (lükandvärav)","Liugvärav on konsoolvärav, mis liigub külgsuunas ilma alumise siinita ega võta avades ruumi. Ideaalne autoväravaks, kui sissesõidu ees on vähe maad.",["Ilma alumise siinita","Automaatikaga","Puit / plekk / paneel"],"center 45%"),
          ("luxaed-w-gates-green","Tiibväravad keevispaneelist","⛩","Väravatüüp","Tiibvärav","Tiibvärav on kahe tiivaga värav, mis avaneb sisse- või väljapoole. Soodne ja lihtne lahendus, kui sissesõidu ees on piisavalt ruumi.",["Kaks tiiba","Soodne lahendus","Sobib automaatikale"]),
          ("luxaed-gate-closeup-1","Jalgvärav puittäidise ja lukuga","🚶","Väravatüüp","Jalgvärav","Jalgvärav on käigutee värav, mis tehakse aiaga ühes stiilis. Mehaaniline lukk või elektrilukk domofoni ja kutsepaneeliga.",["Käigutee värav","Lukk / elektrilukk","Aiaga ühes stiilis"],"center 40%"),
          ("luxaed-gate-hardware-1","Liugvärava rullikud ja kandurid","⚙","Detailid","Väravafurnituur","Kasutame kvaliteetseid rullikuid, kandureid, hingi ja lukke. Tsingitud detailid peavad Eesti kliimas vastu ja tagavad sujuva liikumise aastateks.",["Tsingitud detailid","Rullikud ja kandurid","Vastupidav"])],
 "autotypes_tag":"Väravaautomaatika","autotypes_h":"Väravaautomaatika tüübid",
 "autotypes":[("luxaed-g9","Liugvärava BFT ajam","⚙","Automaatika","Liugvärava automaatika","Liugvärava automaatika on ajam, mis sobitatakse värava kaalu ja laiuse järgi. Komplektis kaugjuhtimispult, fotoelemendid ja sujuv käivitus.",["Ajam kaalu järgi","Pult ja fotoelemendid","BFT / Nice / CAME"]),
              ("luxaed-g6","Tiibvärava hoobajam","⚙","Automaatika","Tiibvärava automaatika","Tiibvärava automaatika on hoob- või kruviajamid mõlemale tiivale. Vaikne ja sujuv avamine ning seiskamine ilma tõmblemiseta.",["Hoob- või kruviajam","Vaikne töö","Mõlemale tiivale"]),
              ("luxaed-barrier-tmp","Automaatne tõkkepuu sissesõidul","⊤","Automaatika","Tõkkepuu","Tõkkepuu on automaatne piirdepoom sissesõidu või parkla juhtimiseks. Sobib korteriühistutele, parklatele ja territooriumidele.",["Parklad ja ühistud","Pult või kood","Kiire avamine"]),
              ("luxaed-reel-domofon-poster","Hikvisioni domofon väraval","🔔","Automaatika","Domofon ja videopaneel","Domofon ja videopaneel avavad värava ja jalgvärava kaugelt. Näete külalist ekraanil või telefonis ja avate värava ühe puudutusega.",["Video ja kõne","Kaugjuhtimine","Värava avamine"],"left center")],
 "cta_band":"Valime värava ja automaatika teie sissesõidule","incl":["Sissesõidu mõõdistus","Värava ja jalgvärava valmistamine","Paigaldus ja loodimine","Automaatika montaaž ja seadistus","Domofoni ühendus, töö kontroll"],
 "factors":["Värava tüüp (liug- / tiibvärav)","Tiiva/lehe laius ja kaal","Automaatika ajami mark ja võimsus","Juhtimine: pult, GSM, rakendus, RFID","Aku-varutoide, domofon, tõkkepuu, garaažiuks","Täide (puit, plekk, võrkpaneel)"],
 "gallery":[("luxaed-w-gates-auto","Lükandvärav automaatikaga"),("luxaed-w-gates-green","Tiibväravad keevispaneelist"),("luxaed-w-gates-graphite","Grafiithallid tiibväravad"),("luxaed-w-gates-winter","Lükandvärav, paigaldus talvel"),("luxaed-w-gates-night","Väravad õhtuvalguses"),("luxaed-w-gates-picket","Lükandvärav lippaiast"),("luxaed-w-lock-black","Värava lukk ja käepide"),("luxaed-w-mesh-gate","Jalgvärav paneelist"),("luxaed-auto-2","Lükandvärava ajam"),("luxaed-w-van","LuxAed objektil")],
 "faq":[("Liug- või tiibvärav. Kumb valida?","Liugvärav (lükandvärav) on mugav, kui sissesõidu ees on vähe ruumi, sest see ei võta avades ruumi. Tiibvärav on lihtsam ja soodsam, kui ruumi jagub. Aitame valida."),
        ("Milliste tootjate automaatikat paigaldate?","Paigaldame tuntud tootjate ajameid: Nice, CAME, BFT, Sommer, DoorHan jt. Ajami valime värava kaalu, laiuse ja kasutuskoormuse järgi."),
        ("Kuidas väravat juhtida saab?","Puldist, telefonikõnega (GSM), nutirakendusest, koodpaneelist või RFID-kaardiga. Üks pult võib juhtida kõiki väravaid ja tõkkepuid krundil."),
        ("Kas värav töötab elektrikatkestuse ajal?","Jah, kui paigaldada aku-varutoide. Ilma selleta saab värava alati avada käsitsi vabastusvõtmega."),
        ("Kas saab automaatika olemasolevale väravale?","Enamasti jah. Hindame konstruktsiooni ja valime sobiva ajami liug- või tiibväravale."),
        ("Kuidas on automaatika ohutusega?","Paigaldame fotoelemendid ja signaallambi, et värav ei sulguks auto või inimese peale. Kasutame ujuva koodiga ajameid, mis on kaitstud puldi pealtkuulamise eest."),
        ("Kas paigaldate domofone ja tõkkepuid?","Jah, paigaldame ja ühendame domofonid ning kutsepaneelid, samuti automaatsed tõkkepuud parklatesse ja korteriühistutele.")]},
{"path":"/aia-remont/","video":("luxaed-reel-remont","Vana betoonposti eemaldamine"),"name":"Aia ja värava remont","hero":"luxaed-g6","og":"/img/luxaed-g6.jpg",
 "title":"Aia ja värava remont Tallinnas — LuxAed","desc":"Aedade ja väravate remont Tallinnas ja Harjumaal: sektsioonide ja postide vahetus, lük- ja tiibväravate ning automaatika remont. Diagnostika ja hinnapakkumine.",
 "kicker":"Remont · hooldus","h1":"Aedade ja väravate<br><em>remont</em>",
 "lead":"Taastame aedu, väravaid ja automaatikat: sektsioonide ja postide vahetus, tiibade reguleerimine, ajamite ja furnituuri remont. Teeme diagnostika ja ütleme hinna.",
 "intro_h":"Mida remondime","intro_p":"Aia remont on sageli mõistlikum kui uue aia ehitamine: kogu aeda ei pea alati vahetama. Sageli piisab kahjustatud sektsioonide või postide vahetusest, väravate reguleerimisest või automaatika taastamisest.",
 "bens":["Kahjustatud sektsioonide vahetus","Postide vahetus ja loodimine","Lük- ja tiibväravate remont","Automaatika remont ja seadistus","Rullikute, siinide ja furnituuri vahetus","Diagnostika ja hind enne tööd"],
 "variants_h":"Remonditööde liigid",
 "variants":[("▤","Aia sektsioonid","Kahjustatud paneelide, laudade või pleki vahetus."),
             ("▥","Postid","Viltuvajunud postide vahetus, loodimine ja kindlustamine."),
             ("⇄","Väravad","Tiibade reguleerimine, rullikute ja siinide vahetus."),
             ("⚙","Automaatika","Ajamite, pultide ja fotoelementide diagnostika ja remont.")],
 "cta_band":"Teeme diagnostika ja parandame aia","incl":["Väljasõit ja diagnostika","Hind enne tööde algust","Sektsioonide, postide või furnituuri vahetus","Väravate ja automaatika reguleerimine","Töö kontroll pärast remonti"],
 "factors":["Kahjustuste maht ja liik","Aia ja värava tüüp","Materjalide vahetuse vajadus","Automaatika remont","Ligipääs krundile"],
 "gallery":[("luxaed-w-gates-winter","Töötame ka talvel"),("luxaed-w-mesh-detail","Kinnituste kontroll"),("luxaed-w-lock-black","Lukkude vahetus"),("luxaed-g6","Post ja ajam"),("luxaed-g8","Lükandvärava automaatika"),("luxaed-g9","Värava ajam"),("luxaed-auto-2","Ajami remont"),("luxaed-w-lock-brown","Luku vahetus"),("luxaed-w-crew","Meister tööl"),("luxaed-w-van","LuxAed objektil")],
 "faq":[("Kas saab remontida, mitte vahetada kogu aeda?","Sageli jah. Vahetame ainult kahjustatud sektsioonid või postid. Diagnostikal hindame, mis on soodsam."),
        ("Kas parandate väravaautomaatikat?","Jah, diagnoosime ja remondime ajamid, pultid ja fotoelemendid, vajadusel vahetame."),
        ("Kas remondite ka teiste paigaldatud väravaid?","Jah, töötame ka teiste meistrite konstruktsioonidega. Hindame kohapeal."),
        ("Kui palju remont maksab?","Sõltub tööde mahust. Pärast diagnostikat ütleme täpse hinna ilma varjatud lisatasudeta.")]},
]

for c in ETSERV: service(c)
print("ET services done:", len(ETSERV))
