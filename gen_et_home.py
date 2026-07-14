#!/usr/bin/env python3
# ET home + ET support pages (meist, kkk, kontakt, privaatsus, tingimused)
import json, html
from build_pages import head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN, partners_marquee, video_block, video_schema, home_video_items, about_page_schema, person_artur_schema, webpage_schema
from gen_et import form_html, faqx, PROCESS
from reviews_data import REVIEWS as ALLREV, card as revcard

def page(path,title,desc,inner,og="/img/luxaed-hero.jpg",sch=None):
    H=head("et",path,title,desc,og_img=og,schema_blocks=sch)
    body=f'''{nav("et",path)}
<main id="main">
{inner}
</main>
<div class="lb" id="lb"><button class="lb-x" aria-label="Sulge">&times;</button><img src="" alt="" id="lbImg"></div>
{footer("et")}
<div class="mob-bar"><a class="btn btn-accent mob-call" href="tel:{TEL}"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="vertical-align:-3px;margin-right:6px"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>Helista</a></div>
{SCRIPTS}
</body></html>'''
    print("wrote", write(path,H+"\n"+body))

def hero(kicker,h1,lead,img="luxaed-wide-wood",crumb=None):
    cr=''  # visible breadcrumbs removed per request (JSON-LD kept for SEO)
    return f'''<section class="svc-hero"><div class="hero-photo-bg" style="background:url('/img/{img}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap">{cr}<span class="tag">{kicker}</span><h1>{h1}</h1><p class="lead">{lead}</p>
  <div class="hero-btns"><a class="btn btn-accent" href="/#form">Küsi pakkumist →</a><a class="btn btn-ghost" href="tel:{TEL}">Helista {PHONE}</a></div></div></section>'''

# ---------------- ET HOME ----------------
rev_cards="".join(revcard(i,n,t,meta="Arvustus Facebookis",date="soovitab",more="Vaata Facebookis →") for i,(n,t) in enumerate(ALLREV[:9]))

TILES=[("/aiad/puitaed/","luxaed-svc-wood","Puit","Puitaiad","Puitaiad ja -väravad teraskarkassil. Soe ja korralik välimus."),
 ("/aiad/metallaed/","luxaed-svc-profnastil","Profiilplekk","Metallaed / profiilplekk","Kinnine profiilplekk-aed privaatsuseks. Soodne ja kiire."),
 ("/aiad/vorkaed/","luxaed-svc-mesh","Võrkaed","Võrkaed / paneelaed","Keevispaneelid (3D), antratsiit RAL. Tugev ja kaasaegne."),
 ("/varavad/","luxaed-svc-gates","Automaatika","Väravad ja automaatika","Lükand- ja tiibväravad, automaatika ja domofonid.")]
tiles_html="".join(f'''<a class="step-ph" href="{u}"><div class="img-wrap"><picture><source type="image/webp" srcset="/img/{im}.webp"><img src="/img/{im}.jpg" alt="{n}" width="600" height="400" loading="lazy"></picture></div>
<div class="sp-top-label"><span>{lbl}</span></div><div class="sp-body"><h3>{n}</h3><p>{d}</p></div></a>''' for u,im,lbl,n,d in TILES)

AREAS=["Tallinn","Kesklinn","Lasnamäe","Mustamäe","Haabersti","Kristiine","Põhja-Tallinn","Pirita","Nõmme","Viimsi","Maardu","Saue","Keila","Harku","Rae","Harjumaa"]
areas_html="".join(f'<span class="area-pill">{a}</span>' for a in AREAS)

HOME_FAQ=[("Kui palju aed või värav maksab?","Täpset hinda ei saa ette öelda. See sõltub materjalist, aia pikkusest ja kõrgusest, reljeefist ning väravatest. Pärast tasuta mõõdistust ütleme konkreetse hinna ilma varjatud lisatasudeta."),
 ("Milliseid aedu te teete?","Puitaiad (teraskarkassil), profiilplekk-aiad ja keevispaneelaiad (3D). Aitame valida materjali eelarve ja krundi järgi."),
 ("Kas paigaldate väravaautomaatikat?","Jah, paigaldame lük- ja tiibväravate automaatika, pultid, fotoelemendid ja domofonid. Saame automaatika ka olemasolevale väravale."),
 ("Millistes piirkondades töötate?","Tallinnas ja kogu Harjumaal. Kaugemale kokkuleppel, kirjutage meile."),
 ("Kas teete aedade remonti?","Jah, remondime aedu ja väravaid: sektsioonide ja postide vahetus, väravate reguleerimine, automaatika remont."),
 ("Kui kaua paigaldus aega võtab?","Tähtaeg sõltub töömahust ja materjalist. Orienteeruva aja ütleme pärast mõõdistust ja projekti kooskõlastamist."),
 ("Kas pean krundil midagi ette valmistama?","Soovitavalt tagage vaba ligipääs tulevase aia joonele. Ülejäänu lepime kokku individuaalselt vastavalt krundi seisukorrale."),
 ("Kuidas teiega ühendust saada?","Kõige lihtsam on helistada numbril +372 5695 8285 või jätta päring veebilehel. Oleme alati kättesaadavad."),
]
home_faq_schema=['<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in HOME_FAQ]},ensure_ascii=False)+'</script>']
lb_schema=['<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"LuxAed","image":DOMAIN+"/img/luxaed-hero.jpg","logo":DOMAIN+"/img/luxaed-logo.png","url":DOMAIN+"/","telephone":PHONE,"email":EMAIL,"priceRange":"€€","address":{"@type":"PostalAddress","addressLocality":"Tallinn","addressRegion":"Harjumaa","addressCountry":"EE"},"areaServed":["Tallinn","Harjumaa","Estonia"],"sameAs":[FB],"geo":{"@type":"GeoCoordinates","latitude":59.437,"longitude":24.7536},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"18:00"}],"aggregateRating":{"@type":"AggregateRating","ratingValue":"5","bestRating":"5","reviewCount":"34"}},ensure_ascii=False)+'</script>']

home_inner=f'''<section class="hero">
  <div class="hero-photo-bg"></div>
  <div class="wrap"><div class="hero-grid"><div>
    <div class="hero-kicker hand">Hei! Vajad uut aeda?</div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">34 arvustust Facebookis · soovitavad</a></div>
    <h1>Aiad ja väravad</h1>
    <p class="hero-claim"><em>võtmed kätte</em><br>mõõdistusest paigalduseni</p>
    <div class="hero-btns"><a class="btn btn-accent" href="#form">Küsi pakkumist →</a><a class="btn btn-ghost" href="tel:{TEL}">Helista {PHONE}</a></div>
  </div>{form_html()}</div>
  <div class="hero-stats"><div class="hstat"><b>100%</b><span>soovitavad Facebookis</span></div><div class="hstat"><b>34</b><span>arvustust</span></div><div class="hstat"><b>15</b><span>aastat meistrite kogemust</span></div></div></div>
</section>

<section class="info-strip"><div class="wrap"><div class="info-inner">
  <div><span class="tag">Mida me teeme</span><h2 class="info-title">Mõõdame, valmistame ja paigaldame aiad ja väravad.<br>Võtame kogu töö enda peale.</h2></div>
  <div><p>Aitame valida, valmistame ja paigaldame <b>aedu, väravaid ja jalgväravaid</b> era- ja ärikinnistutele Tallinnas ja Harjumaal. Samuti paigaldame <b>väravaautomaatikat</b> ja remondime olemasolevaid konstruktsioone.</p></div>
</div></div></section>

<section class="section svc-hide" id="teenused"><div class="wrap"><span class="tag">Meie teenused</span><h2 class="big big--xl">Aiad ja väravad igale krundile</h2>
  <p class="lead lead--lg">Valige aia või värava tüüp. Aitame valida sobiva lahenduse, tuleme tasuta mõõdistusele ja arvutame hinna.</p>
  <div class="steps-ph">{tiles_html}</div></div></section>

<div class="mini-cta"><div class="wrap"><span>Ei tea, milline aed sobib?</span>
  <div class="mini-cta-btns"><a class="btn btn-accent" href="#form">Küsi pakkumist →</a><a class="btn btn-ghost" href="tel:{TEL}">Helista {PHONE}</a></div></div></div>

<section class="section"><div class="wrap"><span class="tag">Arvustused Facebookis</span><h2 class="big" style="margin-bottom:32px">Meid usaldatakse Tallinnas ja Harjumaal</h2>
  <div class="gbp-wrap">
    <div class="gbp-panel">
      <div class="gbp-photos"><div class="gbp-photo-main" style="background:url('/img/luxaed-hero-mobile.webp') center/cover"></div>
        <div class="gbp-photo-stack"><div style="background:url('/img/luxaed-svc-wood-mobile.webp') center/cover;flex:1;border-radius:0 12px 0 0"></div><div style="background:url('/img/luxaed-svc-mesh-mobile.webp') center/cover;flex:1;border-radius:0 0 12px 0"></div></div></div>
      <div class="gbp-body">
        <div class="gbp-title-row"><h3 class="gbp-name">Aiad ja väravad LuxAed</h3>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="#1877F2" aria-hidden="true"><path d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.68.24 2.68.24v2.97h-1.51c-1.49 0-1.95.93-1.95 1.88v2.26h3.32l-.53 3.49h-2.79V24C19.61 23.1 24 18.1 24 12.07z"/></svg></div>
        <div class="gbp-rating-row"><span class="gbp-stars">★★★★★</span><a class="gbp-cnt" href="{FB}" target="_blank" rel="noopener">34 arvustust Facebookis</a></div>
        <p class="gbp-type">Aiad, väravad ja automaatika &middot; Tallinn</p>
        <div class="gbp-actions"><a class="gbp-btn" href="{FB}" target="_blank" rel="noopener">Facebook</a><a class="gbp-btn" href="tel:{TEL}">Helista</a></div>
        <div class="gbp-opts"><span><span class="gbp-check">&#10003;</span> Aiad</span><span><span class="gbp-check">&#10003;</span> Väravad</span><span><span class="gbp-check">&#10003;</span> Automaatika</span></div>
        <hr class="gbp-hr">
        <div class="gbp-details"><div class="gbp-row"><span>Tallinn, Harjumaa</span></div><div class="gbp-row"><b style="color:#188038">100% soovitab</b></div><div class="gbp-row"><a href="tel:{TEL}" style="color:#1a73e8">{PHONE}</a></div></div>
      </div>
    </div>
    <div class="gbp-reviews">
      <div class="gbp-rev-hd"><span class="gbp-rev-score">34</span><div class="gbp-rev-divider"></div><div class="gbp-rev-mid"><div class="gbp-rev-stars">★★★★★</div><div class="gbp-rev-cnt">arvustust Facebookis · soovitavad</div></div><a class="gbp-rev-link" href="{FB}/reviews" target="_blank" rel="noopener">Kõik arvustused →</a></div>
      <div class="rev-carousel" role="region" aria-label="Klientide arvustused Facebookis">
        <button class="rev-arrow rev-prev" type="button" aria-label="Eelmine arvustus">‹</button>
        <div class="rev-viewport"><div class="gbp-rev-list rev-track">{rev_cards}</div></div>
        <button class="rev-arrow rev-next" type="button" aria-label="Järgmine arvustus">›</button>
      </div>
    </div>
  </div></div></section>

<section class="section section--alt"><div class="wrap"><span class="tag">Kuidas töötame</span><h2 class="big">Aia paigaldus: neli lihtsat sammu</h2>{PROCESS}</div></section>
<section class="section"><div class="wrap"><span class="tag">Ausalt hindadest</span><h2 class="big">Aia ja värava hind: mis kuulub sisse ja mis sõltub projektist</h2>
<p class="lead">Hind sõltub materjalist, aia pikkusest, reljeefist ja väravate keerukusest. Seepärast fikseeritud hinnakirja pole. Täpse hinna ütleme pärast tasuta mõõdistust.</p>
<div class="honest">
  <div class="hon good"><h3>Alati hinna sees</h3><ul><li>Krundi mõõdistamine</li><li>Materjali ja konstruktsiooni konsultatsioon</li><li>Hinnaarvestus enne tööde algust</li><li>Postide ja sektsioonide paigaldus</li><li>Furnituuri ja vajadusel automaatika paigaldus</li><li>Väravate kontroll pärast paigaldust</li></ul></div>
  <div class="hon bad"><h3>Sõltub projektist</h3><ul><li>Materjali valik (puit, profiilplekk, keevispaneel)</li><li>Aia pikkus ja kõrgus, väravate arv</li><li>Reljeefi keerukus ja aluse ettevalmistus</li><li>Väravaautomaatika ja domofonid soovi korral</li><li>Vana aia lammutus</li></ul></div>
</div></div></section>

<section class="section section--dark svc-hide" id="meist" style="position:relative;overflow:hidden"><div style="position:absolute;inset:0;background:url('/img/luxaed-sunset.webp') center 40%/cover no-repeat;pointer-events:none"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(8,10,16,.95) 0%, rgba(10,12,20,.82) 40%, rgba(12,10,16,.9) 100%);pointer-events:none"></div>
  <div class="wrap" style="position:relative"><span class="tag">Ettevõttest</span><h2 class="big big--xl">Aiad on meie käsitöö.</h2>
  <p class="lead lead--lg">LuxAed. Aedade ja väravate meeskond Tallinnas ja Harjumaal.<br>Puit, profiilplekk, keevispaneel, väravaautomaatika ja domofonid.<br>Kvaliteetselt ja kokkulepitud hinnaga, mille ütleme enne tööde algust.</p>
  </div></section>

<section class="section"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Varustus</span><h2 class="big">Õige tehnika, kogenud meeskond, korralik tulemus.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-w-van.webp"><img src="/img/luxaed-w-van.jpg" width="750" height="563" alt="LuxAedi buss objektil" loading="lazy"></picture></div>
  <div class="equip-body"><ul class="spec">
    <li><b>Postiaugupuur ja rammer</b>: postid saavad kindlalt ja loodi maasse</li>
    <li><b>Keevis- ja lõiketööd kohapeal</b>: teraskarkassid ja väravaraamid</li>
    <li><b>Loodimine ja mõõtmine</b>: sektsioonid ühes joones, ka kaldega krundil</li>
    <li><b>Automaatika ja domofonid</b>: seadistame ja ühendame võtmed kätte</li>
    <li><b>Puhas objekt</b>: koristame enda järelt ja anname krundi korras üle</li>
  </ul></div></div></div></section>

<section class="section"><div class="wrap"><span class="tag">Galerii</span><h2 class="big">Meie aedade ja väravate näited</h2><p class="lead">Tehtud tööde päris fotod. Vajuta pildile, et avada.</p>
  <div class="gal" id="gal">
    <a href="/img/luxaed-svc-wood.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-svc-wood.webp"><img src="/img/luxaed-svc-wood.jpg" alt="Puitaed teraskarkassil" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-gates-auto.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-gates-auto.webp"><img src="/img/luxaed-w-gates-auto.jpg" alt="Lükandvärav automaatikaga" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-mesh-1.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-mesh-1.webp"><img src="/img/luxaed-w-mesh-1.jpg" alt="3D keevispaneelaed" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-lippaed-1.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-lippaed-1.webp"><img src="/img/luxaed-w-lippaed-1.jpg" alt="Metall-lippaed" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-g1.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-g1.webp"><img src="/img/luxaed-g1.jpg" alt="Puitaed ja lükandvärav" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-gates-green.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-gates-green.webp"><img src="/img/luxaed-w-gates-green.jpg" alt="Tiibväravad keevispaneelist" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-gates-graphite.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-gates-graphite.webp"><img src="/img/luxaed-w-gates-graphite.jpg" alt="Grafiithallid tiibväravad" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-mesh-2.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-mesh-2.webp"><img src="/img/luxaed-w-mesh-2.jpg" alt="Roheline 3D paneelaed" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-van.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-van.webp"><img src="/img/luxaed-w-van.jpg" alt="LuxAedi buss objektil" width="600" height="400" loading="lazy"></picture></a>
  </div>
  <div style="text-align:center;margin-top:30px"><a class="gal-fb" href="{FB}/photos_by" target="_blank" rel="noopener">Rohkem fotosid meie Facebookis →</a></div></div></section>

{video_block("et")}

<section class="section section--alt svc-hide" id="piirkonnad" aria-label="Teeninduspiirkond"><div class="wrap"><span class="tag">Teeninduspiirkond</span><h2 class="big">Aedade ja väravate paigaldus Tallinnas ja Harjumaal</h2>
  <p class="lead">Aiad, väravad ja automaatika Tallinnas ja kogu Harjumaal.</p><div class="area-pills">{areas_html}</div></div></section>

<section class="section" id="kkk"><div class="wrap"><span class="tag">KKK</span><h2 class="big">Mida enne tellimist küsitakse</h2>{faqx(HOME_FAQ)}</div></section>

<section class="cta-final"><div class="wrap"><h2>Valmis arutama <em>aeda või väravat</em>?</h2>
  <p>Jätke päring või helistage. Tuleme tasuta mõõdistusele ja ütleme täpse hinna.</p>
  <div class="hero-btns"><a class="btn btn-accent" href="#form">Küsi pakkumist →</a><a class="btn btn-ghost" href="tel:{TEL}">Helista {PHONE}</a></div></div></section>'''
page("/","Aedade ja väravate paigaldus Tallinnas ja Harjumaal — LuxAed","Aedade ja väravate tootmine ja paigaldus Tallinnas ja Harjumaal. Puit, profiilplekk, 3D paneelid, väravaautomaatika. Tasuta mõõdistus. 100% soovitab.", home_inner, sch=lb_schema+home_faq_schema+video_schema(home_video_items("et"),"et"))

# ---------------- ET MEIST ----------------
meist=f'''<section class="hero hero--compact">
  <div class="hero-photo-bg" style="background:url('/img/luxaed-hero.webp') center 45%/cover no-repeat"></div>
  <div class="wrap"><div class="hero-grid" style="grid-template-columns:1fr;gap:0"><div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">34 arvustust Facebookis · soovitavad</a></div>
    <h1>Kes me oleme</h1>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:16px;max-width:720px">Oleme spetsialiseerunud aedade, väravate ja jalgväravate valmistamisele ja paigaldusele Tallinnas ja Harjumaal <b>juba üle 15 aasta</b>. Töötame puidu, profiilpleki ja keevispaneeliga, paigaldame väravaautomaatikat ja domofone ning remondime olemasolevaid konstruktsioone. Meie meister on näinud kõiki aiatüüpe, pinnaseid ja vee äravoolu lahendusi.</p>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:12px;max-width:720px">Võtame kogu protsessi enda peale: tuleme tasuta mõõdistusele, ostame materjalid, paigaldame ja anname valmis objekti üle. Ütleme hinna ette. Ilma peidetud lisatasude ja üllatusteta.</p>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:12px;max-width:720px">Uus aed suvila ümber, lükandvärav automaatikaga või terve territooriumi piire: teeme kõik ära.</p>
  </div></div>
  <div class="hero-stats"><div class="hstat"><b>100%</b><span>Soovitavad Facebookis</span></div><div class="hstat"><b>34</b><span>Arvustust</span></div><div class="hstat"><b>15</b><span>Aastat meistrite kogemust</span></div></div></div>
</section>
<section class="section"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Meister</span><h2 class="big">Artur Mustafin.<br>Üle 15 aasta kogemust aedade ja väravate ehitamisel.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-w-crew.webp"><img src="/img/luxaed-w-crew.jpg" width="750" height="1000" alt="LuxAedi meister aeda paigaldamas" loading="lazy"></picture></div>
  <div class="equip-body"><p class="lead" style="margin-bottom:14px">Artur on 15 aastat ehitanud aedu ja väravaid Tallinnas ja Harjumaal. Ta teab juba ette, milline lahendus teie krundile sobib ja kuidas vältida liigseid kulusid.</p><ul class="svc-bens">
    <li>Üle 15 aasta kogemust aedade ja väravate ehitamisel</li>
    <li>Tuhanded valminud objektid Tallinnas ja Harjumaal</li>
    <li>Kvaliteedikontroll töö igas etapis</li>
  </ul></div>
</div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">Põhimõtted</span><h2 class="big">Meie jaoks oluline</h2>
<div class="svc-cards">
<div class="svc-card"><div class="ic">1</div><h3>Kõik ühe kõnega</h3><p>Mõõdistus, materjalid, paigaldus ja remont ühest kohast. Üks kõne, ja kõik on korraldatud.</p></div>
<div class="svc-card"><div class="ic">2</div><h3>Töötame aastaringselt</h3><p>Paigaldame aedu ka talvel. Külmunud pinnas pole takistus. Me ei lükka kevadesse.</p></div>
<div class="svc-card"><div class="ic">3</div><h3>Hoolsad käed</h3><p>Töötame puhtalt, hoiame krunti ja koristame enda järelt. Anname objekti korras üle.</p></div>
<div class="svc-card"><div class="ic">4</div><h3>Täpne hind ette</h3><p>Ütleme hinna enne algust ja peame sellest kinni. Ilma peidetud lisatasude ja üllatusteta.</p></div>
</div></div></section>
<section class="section"><div class="wrap"><span class="tag">Miks meie</span><h2 class="big">Miks LuxAed</h2>
<ul class="svc-bens"><li>Üle <b>15 aasta</b> kogemust Tallinnas ja Harjumaal</li><li>Aiad puidust, profiilplekist ja keevispaneelist</li><li>Lükand- ja tiibväravad, väravaautomaatika ja domofonid</li><li>Materjalide ostu ja kogu protsessi võtame enda peale</li><li>Tasuta mõõdistus, hind enne algust, garantii tööle</li><li>Töötame aastaringselt, ka talvel</li></ul></div></section>
<section class="section section--dark" style="position:relative;overflow:hidden"><div style="position:absolute;inset:0;background:url('/img/luxaed-sunset.webp') center 40%/cover no-repeat;pointer-events:none"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(8,10,16,.95) 0%, rgba(10,12,20,.82) 40%, rgba(12,10,16,.9) 100%);pointer-events:none"></div>
<div class="wrap" style="position:relative"><span class="tag">Meid usaldatakse</span><h2 class="big big--xl">Arvustused räägivad enda eest</h2>
<p class="lead lead--lg">Kliendid kiidavad LuxAedi kiiruse, kvaliteedi ja professionaalse suhtumise eest.<br>Vaadake arvustusi meie <a href="{FB}" target="_blank" rel="noopener" style="color:var(--accent)">Facebooki</a> lehel.</p>
</div></section>
<section class="section section--alt"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Varustus</span><h2 class="big">Õige tehnika, kogenud meeskond, korralik tulemus.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-w-van.webp"><img src="/img/luxaed-w-van.jpg" width="750" height="563" alt="LuxAed, väravate ja aedade paigaldus" loading="lazy"></picture></div>
  <div class="equip-body"><ul class="spec">
    <li><b>Postiaugupuur ja rammer</b>: postid saavad kindlalt ja loodi maasse</li>
    <li><b>Keevis- ja lõiketööd kohapeal</b>: teraskarkassid ja väravaraamid</li>
    <li><b>Loodimine ja mõõtmine</b>: sektsioonid ühes joones, ka kaldega krundil</li>
    <li><b>Automaatika ja domofonid</b>: seadistame ja ühendame võtmed kätte</li>
    <li><b>Puhas objekt</b>: koristame enda järelt ja anname krundi korras üle</li>
  </ul></div>
</div></div></section>
<section class="cta-final"><div class="wrap"><h2>Arutame <em>teie aeda või väravat</em>?</h2><p>Jätke päring või helistage. Tuleme tasuta mõõdistusele.</p>
<div class="hero-btns"><a class="btn btn-accent" href="/#form">Küsi pakkumist →</a><a class="btn btn-ghost" href="tel:{TEL}">Helista {PHONE}</a></div></div></section>'''
page("/meist/","LuxAedist. Aiad ja väravad Tallinnas","LuxAed. Aedade ja väravate tootmine ja paigaldus Tallinnas ja Harjumaal. Puit, profiilplekk, keevispaneel, automaatika ja domofonid.", meist, sch=[about_page_schema("/meist/","et","LuxAedist","Aedade ja väravate meister Artur Mustafin ja LuxAedi lugu Tallinnas ja Harjumaal."),person_artur_schema("et")])

# ---------------- ET KKK ----------------
kkk_inner=f'''{hero("KKK","Korduma kippuvad küsimused","Kogusime vastused küsimustele, mida enne aia või värava tellimist kõige sagedamini küsitakse.", crumb="KKK")}
<section class="section"><div class="wrap"><span class="tag">KKK</span><h2 class="big">Mida enne tellimist küsitakse</h2>{faqx(HOME_FAQ)}</div></section>
<section class="cta-final"><div class="wrap"><h2>Ei leidnud vastust?</h2><p>Helistage või kirjutage.<br>Anname nõu ja tuleme tasuta mõõdistusele.</p>
<div class="hero-btns"><a class="btn btn-accent" href="/#form">Küsi pakkumist →</a><a class="btn btn-ghost" href="tel:{TEL}">Helista {PHONE}</a></div></div></section>'''
page("/kkk/","KKK. Aiad ja väravad — LuxAed","Korduma kippuvad küsimused aedade, väravate ja automaatika kohta Tallinnas: hind, materjalid, tähtajad, automaatika, remont. LuxAed.", kkk_inner, og="/img/luxaed-wide-wood.jpg", sch=home_faq_schema)

# ---------------- ET KONTAKT ----------------

# ---------------- ET LEGAL ----------------
def legal(path,title,h1,kicker,blocks):
    inner=f'''{hero(kicker,h1,"",img="luxaed-g3",crumb=h1)}
<section class="section"><div class="wrap" style="max-width:820px">
{"".join(f"<h2 class='big' style='font-size:24px;margin-top:28px'>{t}</h2><p class='lead' style='margin-top:10px'>{b}</p>" for t,b in blocks)}
<p class="lead" style="margin-top:26px">Selle dokumendiga seotud küsimustes kirjutage <a href="mailto:{EMAIL}" style="color:var(--accent)">{EMAIL}</a>.</p></div></section>'''
    page(path,title,h1+" — LuxAed, aiad ja väravad Tallinnas.",inner,og="/img/luxaed-g3.jpg",sch=[webpage_schema(path,"et",title,h1)])

legal("/privaatsus/","Privaatsuspoliitika — LuxAed","Privaatsuspoliitika","Privaatsus",[
 ("Kes andmeid töötleb","LuxAed (aiad ja väravad, Tallinn, Eesti) töötleb isikuandmeid, mille edastate meiega ühendust võttes veebi, telefoni, e-posti või Facebooki kaudu."),
 ("Milliseid andmeid kogume","Nimi, telefon, e-post, krundi aadress ja ülesande kirjeldus ning fotod, mille lisate päringule. Neid andmeid vajame pakkumise koostamiseks ja teiega ühenduse võtmiseks."),
 ("Eesmärk ja õiguslik alus","Andmeid kasutatakse ainult päringule vastamiseks, pakkumise koostamiseks ja teenuse osutamiseks. Õiguslik alus on teie nõusolek ja lepingu ettevalmistus."),
 ("Andmete säilitamine","Säilitame andmeid nii kaua, kui vaja päringu töötlemiseks ja teenuse osutamiseks, seejärel kustutame, kui pole muid seaduslikke aluseid."),
 ("Edastamine kolmandatele","Me ei müü ega edasta teie andmeid kolmandatele, välja arvatud seaduses ettenähtud juhtudel."),
 ("Teie õigused","Teil on õigus taotleda ligipääsu oma andmetele, nende parandamist või kustutamist ja nõusolek tagasi võtta. Selleks võtke meiega ühendust e-posti teel."),
 ("Küpsised","Veebisait võib kasutada tehnilisi küpsiseid korrektseks tööks. Analüütika- ja reklaamiskriptid laaditakse ainult vastava nõusoleku olemasolul."),
])
legal("/tingimused/","Kasutustingimused — LuxAed","Kasutustingimused","Tingimused",[
 ("Üldsätted","Käesolevad tingimused kirjeldavad LuxAedi teenuste osutamist aedade, väravate ja automaatika valmistamisel, paigaldusel ja remondil Tallinnas ja Harjumaal."),
 ("Päring ja pakkumine","Päringu saab jätta telefoni, e-posti või vormi kaudu. Hind määratakse pärast tasuta mõõdistust ja lepitakse kokku enne tööde algust."),
 ("Mõõdistus ja kokkulepped","Täpne hind, materjalid ja tähtajad fikseeritakse pärast objektile jõudmist. Kõik olulised tingimused lepitakse kliendiga eelnevalt kokku."),
 ("Tasumine","Tasumise kord ja viis lepitakse kokku individuaalselt enne tööde algust. Me ei võta kokkulepitud eelarvest varjatud lisatasusid ilma teie nõusolekuta."),
 ("Garantii ja kvaliteet","Vastutame tehtud tööde kvaliteedi eest. Garantiitingimused sõltuvad tööde ja materjalide liigist ning lepitakse kokku lepingu sõlmimisel."),
 ("Vastutus","LuxAed ei vastuta krundil olevate varjatud tehnovõrkude kahjustuste eest, millest klient ei teavitanud, ega vääramatu jõu eest."),
 ("Kontakt","Kõigis teenuste ja tingimustega seotud küsimustes võtke ühendust telefonil "+PHONE+" või e-postil "+EMAIL+"."),
])
print("ET home + support done")
