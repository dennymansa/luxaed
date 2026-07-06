#!/usr/bin/env python3
# Estonian tree: /et/ home, service pages, support pages. Targets ET keywords.
import json, html
from build_pages import head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN, SVC

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
    <div class="chips" id="svcChips" role="radiogroup">{ch}</div>
    <div class="ff" data-svc="aed"><select name="material" class="form-select"><option value="">Aia materjal</option><option>Puit</option><option>Profiilplekk</option><option>Võrkaed (keevispaneel)</option><option>Ei tea — soovitage</option></select></div>
    <div class="ff form-grid2" data-svc="aed"><input type="text" name="length" inputmode="numeric" placeholder="Pikkus, m"><select name="height" class="form-select"><option value="">Kõrgus</option><option>kuni 1,5 m</option><option>1,5–2 m</option><option>üle 2 m</option></select></div>
    <div class="ff" data-svc="varav,automaatika"><select name="gate_type" class="form-select"><option value="">Värava tüüp</option><option>Lükandvärav</option><option>Tiibvärav</option><option>Ei tea</option></select></div>
    <div class="ff" data-svc="varav"><select name="automation" class="form-select"><option value="">Automaatika?</option><option>Automaatikaga</option><option>Ilma automaatikata</option><option>Ei tea</option></select></div>
    <div class="ff form-grid2"><select name="plot" class="form-select"><option value="">Krunt</option><option>Tasane</option><option>Kaldega</option><option>Vana aed (lammutus)</option><option>Ei tea</option></select><select name="timeline" class="form-select"><option value="">Millal?</option><option>Võimalikult kiiresti</option><option>1–3 kuu jooksul</option><option>Lihtsalt hind teada</option></select></div>
    <div class="ff-base"><input type="text" name="address" placeholder="Krundi aadress (linn / piirkond)"></div>
    <div class="form-grid">
      <input type="text" name="name" placeholder="Teie nimi *" required style="grid-column:1/-1">
      <input type="tel" name="phone" placeholder="Telefon *" required>
      <input type="email" name="email" placeholder="E-post *" required>
    </div>
    <div class="ff"><textarea name="msg" placeholder="Kommentaar: detailid, soovid, mida remontida..."></textarea></div>
    <label class="photo-upload ff" id="photoLabel"><input type="file" name="photos" accept="image/*" multiple id="photoInput" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);border:0"><svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg><span id="photoLabel-txt">Lisa foto (valikuline)</span></label>
    <button class="btn btn-accent" type="submit" style="width:100%;padding:13px;font-size:15px">Saada päring →</button>
    <p class="form-consent">Vormi saates nõustud <a href="/et/privaatsus/">privaatsuspoliitikaga</a> ja <a href="/et/tingimused/">tingimustega</a></p>
    <div class="form-ok" id="formOk" role="status"><b>Aitäh! Päring on vastu võetud.</b><br>Võtame teiega peagi ühendust.</div>
  </form>
</div></div>'''

PROCESS='''<div class="hsteps">
  <div class="hstep"><div class="hstep-num">1</div><h3>Jätke päring</h3><p>Üks kõne või sõnum — ja võtame aia enda peale. Tuleme tasuta mõõdistusele teile sobival ajal.</p></div>
  <div class="hstep"><div class="hstep-num">2</div><h3>Valime ja arvutame</h3><p>Pakume materjali ja lahenduse teie krundi ja eelarve järgi ning ütleme ausa hinna — ilma üllatusteta.</p></div>
  <div class="hstep"><div class="hstep-num">3</div><h3>Paigaldame korralikult</h3><p>Paigaldame postid, sektsioonid, väravad ja automaatika. Hoiame teid kursis igal etapil.</p></div>
  <div class="hstep"><div class="hstep-num">4</div><h3>Anname võtmed kätte</h3><p>Kontrollime iga detaili koos teiega ja anname valmis aia üle. Edasi — lihtsalt nautige.</p></div>
</div>'''

def bens(items): return '<ul class="svc-bens">'+"".join(f"<li>{x}</li>" for x in items)+'</ul>'
def cards(cc): return '<div class="svc-cards">'+"".join(f'<div class="svc-card"><div class="ic">{i}</div><h4>{n}</h4><p>{d}</p></div>' for i,n,d in cc)+'</div>'
def gal(imgs): return '<div class="gal" id="gal">'+"".join(f'<a href="/img/{i}.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/{i}.webp"><img src="/img/{i}.jpg" alt="{html.escape(a)}" loading="lazy"></picture></a>' for i,a in imgs)+'</div>'
def faqx(fq): return '<div class="faq" id="faqList">'+"".join(f'<div class="faq-item"><button class="faq-q">{q}</button><div class="faq-a"><p>{a}</p></div></div>' for q,a in fq)+'</div>'
def related(cur):
    cc=[(p,t) for p,t in SVC["et"] if p!=cur][:3]
    return '<div class="svc-cards">'+"".join(f'<a class="svc-card" href="{p}" style="text-decoration:none"><div class="ic">→</div><h4>{t}</h4><p>Loe lähemalt →</p></a>' for p,t in cc)+'</div>'

def schema(name,desc,path,fq):
    j=lambda o:'<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False)+'</script>'
    return [j({"@context":"https://schema.org","@type":"Service","serviceType":name,"description":desc,"url":DOMAIN+path,
              "provider":{"@type":"HomeAndConstructionBusiness","name":"LuxAed","telephone":PHONE,"email":EMAIL,"url":DOMAIN+"/et/"},
              "areaServed":["Tallinn","Harjumaa"]}),
            j({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
              {"@type":"ListItem","position":1,"name":"Avaleht","item":DOMAIN+"/et/"},
              {"@type":"ListItem","position":2,"name":name,"item":DOMAIN+path}]}),
            j({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in fq]})]

def service(c):
    H=head("et",c["path"],c["title"],c["desc"],og_img=c.get("og","/img/luxaed-hero.jpg"),schema_blocks=schema(c["name"],c["desc"],c["path"],c["faq"]))
    body=f'''{nav("et",c["path"])}
<main id="main">
<section class="svc-hero">
  <div class="hero-photo-bg" style="background:url('/img/{c["hero"]}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap"><div class="hero-grid"><div>
    <div class="crumb"><a href="/et/">Avaleht</a><span>›</span>{c["name"]}</div>
    <span class="tag">{c["kicker"]}</span><h1>{c["h1"]}</h1><p class="lead">{c["lead"]}</p>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><span class="ht-label">34 arvustust Facebookis · soovitavad</span></div>
    <div class="hero-btns"><a class="btn btn-accent" href="#form">Küsi pakkumist →</a><a class="btn btn-ghost" href="tel:{TEL}">Helista {PHONE}</a></div>
  </div>{form_html()}</div></div>
</section>
<section class="section"><div class="wrap"><span class="tag">Mida saate</span><h2 class="big">{c["intro_h"]}</h2><p class="lead">{c["intro_p"]}</p>{bens(c["bens"])}</div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">Valikud</span><h2 class="big">{c["variants_h"]}</h2>{cards(c["variants"])}
  <div class="svc-cta"><b>{c["cta_band"]}</b><a class="btn" href="#form">Küsi pakkumist →</a></div></div></section>
<section class="section"><div class="wrap"><span class="tag">Ausalt hinnast</span><h2 class="big">Millest sõltub hind</h2>
  <p class="lead">Fikseeritud hinnakirja ei ole — täpse hinna ütleme pärast tasuta mõõdistust.</p>
  <div class="honest"><div class="hon good"><h3>Alati sisaldub</h3><ul>{"".join(f"<li>{x}</li>" for x in c["incl"])}<li>Töötame aastaringselt, ka talvel</li><li>Garantii tehtud töödele</li></ul></div>
  <div class="hon bad"><h3>Mõjutab hinda</h3><ul>{"".join(f"<li>{x}</li>" for x in c["factors"])}</ul></div></div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">Kuidas töötame</span><h2 class="big">Neli sammu valmis tulemuseni</h2>{PROCESS}</div></section>
<section class="section"><div class="wrap"><span class="tag">Galerii</span><h2 class="big">Tehtud tööde näited</h2>{gal(c["gallery"])}</div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">KKK</span><h2 class="big">Korduma kippuvad küsimused</h2>{faqx(c["faq"])}</div></section>
<section class="section"><div class="wrap"><span class="tag">Teised teenused</span><h2 class="big">Vaata ka</h2>{related(c["path"])}</div></section>
<section class="cta-final"><div class="wrap"><h2>Arutame <em>{c["name"].lower()}</em> teie krundile?</h2>
  <p>Jätke päring või helistage — tuleme tasuta mõõdistusele ja ütleme täpse hinna.</p>
  <div class="hero-btns"><a class="btn btn-accent" href="#form">Küsi pakkumist →</a><a class="btn btn-ghost" href="tel:{TEL}">Helista {PHONE}</a></div></div></section>
</main>
<div class="lb" id="lb"><button class="lb-x" aria-label="Sulge">&times;</button><img src="" alt="" id="lbImg"></div>
{footer("et")}
<div class="mob-bar"><a href="tel:{TEL}" class="btn btn-ghost">Helista</a><a href="#form" class="btn btn-accent">Päring</a></div>
{SCRIPTS}
</body></html>'''
    print("wrote", write(c["path"],H+"\n"+body))

ETSERV=[
{"path":"/et/aiad/vorkaed/","name":"Võrkaed ja paneelaed","hero":"luxaed-svc-mesh","og":"/img/luxaed-svc-mesh.jpg",
 "title":"Võrkaed ja keevispaneelaed Tallinnas — LuxAed","desc":"Võrkaia ja keevispaneelaia (3D aiapaneelid) paigaldus Tallinnas ja Harjumaal. Tsingitud ja pulbervärvitud paneelid, antratsiit RAL 7016, postid ja paigaldus. Tasuta mõõdistus.",
 "kicker":"Võrkaed · keevispaneelaed","h1":"Võrkaed ja paneelaed Tallinnas",
 "lead":"Kaasaegsed keevispaneelaiad (3D aiapaneelid) jäikusribidega: tugev, korralik ja hea läbipaistvusega piire. Tsingitud ja pulbervärvitud — peab aastakümneid.",
 "intro_h":"Miks valida paneelaed","intro_p":"Keevispaneel (3D) hoiab vormi, ei vaju ega tuuletõmba ning näeb kaasaegne välja. Sobib eramutele, ridaelamutele ja territooriumidele.",
 "bens":["Tugevad keevispaneelid jäikusribidega","Tsink + pulbervärv — ei roosteta","Antratsiit RAL 7016 ja teised värvid","Hea läbipaistvus, vähe tuulekoormust","Kiire paigaldus postidele","3D ja 2D aiapaneelid"],
 "variants_h":"Milliseid võrkaedu teeme",
 "variants":[("3D","3D aiapaneel","Keevispaneel V-kujuliste jäikusribidega — populaarseim ja tugevaim."),
             ("2D","2D topeltvarras","Topelthorisontaalvarras — tugevdatud paneel suurte avade jaoks."),
             ("◧","RAL värvid","Antratsiit RAL 7016, roheline RAL 6005, must jm."),
             ("▤","Postid ja kinnitus","Tsingitud postid, kübarad ja kinnitusklambrid.")],
 "cta_band":"Arvutame võrkaia teie krundile","incl":["Krundi mõõdistus","Tsingitud postide paigaldus","Keevispaneelide ja kinnituste montaaž","Loodimine reljeefi järgi","Kontroll pärast paigaldust"],
 "factors":["Aia pikkus ja paneelide kõrgus (1.23–2.03 m)","Paneeli tüüp (2D/3D) ja värv","Reljeef ja aluse ettevalmistus","Väravate ja jalgvärava arv","Vana aia lammutus"],
 "gallery":[("luxaed-svc-mesh","Keevispaneelaed"),("luxaed-mesh-2","Võrkaed krundi ääres"),("luxaed-mesh-3","Võrkaed roheliste postidega"),("luxaed-mesh-gate","Võrkväravad LuxAed")],
 "faq":[("Kui kaua võrkaed peab?","Tsingitud ja pulbervärvitud paneelid peavad aastakümneid ega roosteta."),
        ("Millised kõrgused on?","Tavaliselt 1.23–2.03 m. Valime kõrguse vajaduse järgi."),
        ("Milline värv valida?","Populaarseimad on antratsiit RAL 7016 ja roheline RAL 6005."),
        ("Kas saab värava samas toonis?","Jah, teeme lük- ja tiibväravaid sama paneeliga samas värvis.")]},
{"path":"/et/aiad/puitaed/","name":"Puitaed","hero":"luxaed-svc-wood","og":"/img/luxaed-svc-wood.jpg",
 "title":"Puitaed ja puitväravad Tallinnas — LuxAed","desc":"Puitaedade ja -väravate valmistamine ja paigaldus Tallinnas ja Harjumaal. Horisontaalne puitaed, teraskarkass, töötlus. Tasuta mõõdistus ja pakkumine.",
 "kicker":"Puit · teraskarkass","h1":"Puitaed Tallinnas",
 "lead":"Soe ja korralik välimus. Valmistame puitaedu ja -väravaid tugeval teraskarkassil — loodusliku puidu ja vastupidava metalli kombinatsioon.",
 "intro_h":"Miks puitaed","intro_p":"Puit näeb väärikas ja looduslik välja ning sobib igale krundile. Teraskarkassil ei vaju konstruktsioon ja peab kaua.",
 "bens":["Töödeldud puit Eesti kliima jaoks","Tugev teraskarkass — ei vaju","Horisontaalne, vertikaalne või ribiline","Aed ja väravad ühes stiilis","Võimalik väravaautomaatika","Individuaalne disain"],
 "variants_h":"Puitaedade tüübid",
 "variants":[("▤","Horisontaalne","Horisontaallauad teraskarkassil — kaasaegne populaarne lahendus."),
             ("▥","Piirdeaed (lippaed)","Klassikaline vertikaalne lippaed vahega või ilma."),
             ("◫","Ribiline (žalusii)","Kaldu lamellid — privaatsus koos õhutusega."),
             ("⛩","Puitväravad","Lük- ja tiibväravad puidutäitega ja automaatikaga.")],
 "cta_band":"Valime puitaia teie maja juurde","incl":["Krundi mõõdistus","Sektsioonide ja teraskarkassi valmistamine","Postide ja sektsioonide paigaldus","Puidu töötlus ja kate","Kontroll pärast paigaldust"],
 "factors":["Aia pikkus ja kõrgus","Tüüp (horisontaalne, lippaed, žalusii)","Puidu liik ja töötlus","Väravad ja automaatika","Reljeef ja alus"],
 "gallery":[("luxaed-svc-wood","Puitaed teraskarkassil"),("luxaed-g1","Puitaed ja lükandvärav"),("luxaed-wood-2","Puitaed krundil"),("luxaed-wood-3","Puitaed ja värav")],
 "faq":[("Kas puit ei mädane?","Kasutame töödeldud puitu ja katet ning karkass on terasest. Korralik hooldus tagab pika eluea."),
        ("Kas saab horisontaallauad?","Jah, horisontaalne puitaed teraskarkassil on üks populaarsemaid."),
        ("Kas teete väravad samas stiilis?","Jah, valmistame lük- ja tiibväravaid puidutäitega ühises disainis."),
        ("Kas puitaed vajab hooldust?","Perioodiliselt tasub uuendada puidu kaitsekihti — selgitame, kuidas hooldada.")]},
{"path":"/et/aiad/metallaed/","name":"Metallaed ja profiilplekk-aed","hero":"luxaed-svc-profnastil","og":"/img/luxaed-svc-profnastil.jpg",
 "title":"Metallaed ja profiilplekk-aed Tallinnas — LuxAed","desc":"Metall- ja profiilplekk-aedade paigaldus Tallinnas ja Harjumaal. Tsingitud profiilplekk, erinevad värvid, kinnine aed privaatsuseks. Soodne ja kiire. Tasuta mõõdistus.",
 "kicker":"Metall · profiilplekk","h1":"Metallaed ja profiilplekk-aed Tallinnas",
 "lead":"Praktiline ja soodne lahendus: kinnine aed tsingitud profiilplekist. Täielik privaatsus, tuule- ja tolmukaitse, erinevad värvid.",
 "intro_h":"Miks profiilplekk","intro_p":"Profiilplekk on soodne ja kiiresti paigaldatav. Kinnine aed katab krundi ja peab kaua tänu tsingile ja polümeerkattele.",
 "bens":["Täielik privaatsus — kinnine aed","Tsingitud plekk polümeerkattega","Erinevad värvid (ka puidu imitatsioon)","Kaitse tuule, tolmu ja müra eest","Ökonoomne ja kiire","Metallpostid ja -latid"],
 "variants_h":"Profiilplekk-aia valikud",
 "variants":[("▦","Standard profiilplekk","Kinnine aed tsingitud plekist vajalikus kõrguses."),
             ("◧","Värviline kate","Polümeerkate eri värvides, ka puidu imitatsioon."),
             ("▣","Kivipostidega","Profiilplekk kombineeritud kivi- või plokkpostidega."),
             ("⛩","Profiilplekk-väravad","Lük- ja tiibväravad plekitäitega.")],
 "cta_band":"Arvutame profiilplekk-aia","incl":["Krundi mõõdistus","Metallpostide ja -lattide paigaldus","Profiilpleki montaaž","Loodimine","Kontroll pärast paigaldust"],
 "factors":["Aia pikkus ja kõrgus","Pleki mark ja värv","Postide tüüp (metall, kivi)","Väravad ja jalgväravad","Reljeef ja alus"],
 "gallery":[("luxaed-svc-profnastil","Profiilplekk-värav"),("luxaed-metal","Metallaed väravaga"),("luxaed-profnastil-2","Profiilplekk-aed (näide)")],
 "faq":[("Kas profiilplekk ei pleegi?","Kvaliteetne polümeerkattega plekk hoiab värvi kaua. Kasutame tõestatud materjale."),
        ("Milline kõrgus on võimalik?","Tavaliselt 1.5–2.0 m ja kõrgem — valime privaatsuse ja tuulekoormuse järgi."),
        ("Kas saab kombineerida kivipostidega?","Jah, teeme kombineeritud aedu: plekk kivi- või plokkpostide vahel."),
        ("Kas profiilplekk on odavam kui puit ja võrkaed?","Reeglina jah — üks soodsamaid lahendusi. Täpse hinna ütleme pärast mõõdistust.")]},
{"path":"/et/varavad/","name":"Väravad ja automaatika","hero":"luxaed-svc-gates","og":"/img/luxaed-svc-gates.jpg",
 "title":"Väravad, jalgväravad ja väravaautomaatika Tallinnas — LuxAed","desc":"Lük- ja tiibväravad, jalgväravad, väravaautomaatika ja fonolukud Tallinnas ja Harjumaal. Ajamite, pultide ja domofonide paigaldus võtmed kätte. Tasuta mõõdistus.",
 "kicker":"Väravad · automaatika · domofon","h1":"Väravad ja automaatika Tallinnas",
 "lead":"Lük- ja tiibväravad võtmed kätte koos automaatika ja domofonidega. Valmistame, paigaldame ja ühendame — sõidate õue ühe nupuvajutusega.",
 "intro_h":"Väravad automaatikaga võtmed kätte","intro_p":"Valime väravatüübi ja ajami teie sissesõidu, laiuse ja reljeefi järgi. Paigaldame automaatika, pultid, fotoelemendid ja domofonid ning hooldame olemasolevaid.",
 "bens":["Lükandväravad (liugväravad)","Tiibväravad","Automaatika: ajamid, pultid, fotoelemendid","Domofonid ja kutsepaneelid","Jalgväravad aiaga ühes stiilis","Olemasolevate väravate hooldus ja remont"],
 "variants_h":"Väravate ja automaatika tüübid",
 "variants":[("⇄","Lükandvärav","Liugvärav ilma alumise siinita — mugav, ei võta avades ruumi."),
             ("⛩","Tiibvärav","Klassikaline kahe tiivaga värav ajamitega."),
             ("⚙","Automaatika","Ajamid, kaugjuhtimispultid, fotoelemendid, signaallamp."),
             ("🔔","Domofon","Kutsepaneelid ja domofonid värava ja jalgvärava avamisega.")],
 "cta_band":"Valime värava ja automaatika teie sissesõidule","incl":["Sissesõidu mõõdistus","Värava ja jalgvärava valmistamine","Paigaldus ja loodimine","Automaatika montaaž ja seadistus","Domofoni ühendus, töö kontroll"],
 "factors":["Värava tüüp (lük- / tiibvärav)","Tiiva laius ja kaal","Automaatika ajami mark","Domofon ja lisavõimalused","Täide (puit, plekk, võrkpaneel)"],
 "gallery":[("luxaed-svc-gates","Puidust lükandvärav automaatikaga"),("luxaed-profnastil-gate","Profiilplekk-tiibväravad"),("luxaed-mesh-gate","Võrkväravad"),("luxaed-auto-2","Lükandvärava ajam")],
 "faq":[("Lük- või tiibvärav — kumb valida?","Lükandvärav on mugav, kui sissesõidu ees on vähe ruumi. Tiibvärav on lihtsam ja soodsam. Aitame valida."),
        ("Kas saab automaatika olemasolevale väravale?","Enamasti jah — hindame konstruktsiooni ja valime sobiva ajami."),
        ("Kas paigaldate domofone?","Jah, paigaldame ja ühendame domofonid ning kutsepaneelid värava avamisega."),
        ("Kuidas on automaatika ohutusega?","Paigaldame fotoelemendid ja signaallambi, et värav ei sulguks auto või inimese peale.")]},
{"path":"/et/aia-remont/","name":"Aia ja värava remont","hero":"luxaed-g6","og":"/img/luxaed-g6.jpg",
 "title":"Aia ja värava remont Tallinnas — LuxAed","desc":"Aedade ja väravate remont Tallinnas ja Harjumaal: sektsioonide ja postide vahetus, lük- ja tiibväravate ning automaatika remont. Diagnostika ja hinnapakkumine.",
 "kicker":"Remont · hooldus","h1":"Aia ja värava remont Tallinnas",
 "lead":"Taastame aedu, väravaid ja automaatikat: sektsioonide ja postide vahetus, tiibade reguleerimine, ajamite ja furnituuri remont. Teeme diagnostika ja ütleme hinna.",
 "intro_h":"Mida remondime","intro_p":"Kogu aeda ei pea alati vahetama — sageli piisab kahjustatud sektsioonide või postide vahetusest, väravate reguleerimisest või automaatika taastamisest.",
 "bens":["Kahjustatud sektsioonide vahetus","Postide vahetus ja loodimine","Lük- ja tiibväravate remont","Automaatika remont ja seadistus","Rullikute, siinide ja furnituuri vahetus","Diagnostika ja hind enne tööd"],
 "variants_h":"Remonditööde liigid",
 "variants":[("▤","Aia sektsioonid","Kahjustatud paneelide, laudade või pleki vahetus."),
             ("▥","Postid","Viltuvajunud postide vahetus, loodimine ja kindlustamine."),
             ("⇄","Väravad","Tiibade reguleerimine, rullikute ja siinide vahetus."),
             ("⚙","Automaatika","Ajamite, pultide ja fotoelementide diagnostika ja remont.")],
 "cta_band":"Teeme diagnostika ja parandame aia","incl":["Väljasõit ja diagnostika","Hind enne tööde algust","Sektsioonide, postide või furnituuri vahetus","Väravate ja automaatika reguleerimine","Töö kontroll pärast remonti"],
 "factors":["Kahjustuste maht ja liik","Aia ja värava tüüp","Materjalide vahetuse vajadus","Automaatika remont","Ligipääs krundile"],
 "gallery":[("luxaed-g8","Lükandvärava automaatika"),("luxaed-g9","Värava ajam alusel"),("luxaed-auto-2","Ajami remont"),("luxaed-g6","Post ja ajam")],
 "faq":[("Kas saab remontida, mitte vahetada kogu aeda?","Sageli jah — vahetame ainult kahjustatud sektsioonid või postid. Diagnostikal hindame, mis on soodsam."),
        ("Kas parandate väravaautomaatikat?","Jah, diagnoosime ja remondime ajamid, pultid ja fotoelemendid, vajadusel vahetame."),
        ("Kas remondite ka teiste paigaldatud väravaid?","Jah, töötame ka teiste meistrite konstruktsioonidega — hindame kohapeal."),
        ("Kui palju remont maksab?","Sõltub tööde mahust. Pärast diagnostikat ütleme täpse hinna ilma varjatud lisatasudeta.")]},
]

for c in ETSERV: service(c)
print("ET services done:", len(ETSERV))
