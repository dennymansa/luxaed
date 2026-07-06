#!/usr/bin/env python3
# EN home + EN support pages (about, faq, contact, privacy, terms)
import json, html
from build_pages import head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN
from gen_en import form_html, faqx, PROCESS
from reviews_data import REVIEWS as ALLREV, card as revcard

def page(path,title,desc,inner,og="/img/luxaed-hero.jpg",sch=None):
    H=head("en",path,title,desc,og_img=og,schema_blocks=sch)
    body=f'''{nav("en",path)}
<main id="main">
{inner}
</main>
<div class="lb" id="lb"><button class="lb-x" aria-label="Close">&times;</button><img src="" alt="" id="lbImg"></div>
{footer("en")}
<div class="mob-bar"><a class="btn btn-accent mob-call" href="tel:{TEL}"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="vertical-align:-3px;margin-right:6px"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>Call</a></div>
{SCRIPTS}
</body></html>'''
    print("wrote", write(path,H+"\n"+body))

def hero(kicker,h1,lead,img="luxaed-wide-wood",crumb=None):
    cr=f'<div class="crumb"><a href="/en/">Home</a><span>›</span>{crumb}</div>' if crumb else ''
    return f'''<section class="svc-hero"><div class="hero-photo-bg" style="background:url('/img/{img}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap">{cr}<span class="tag">{kicker}</span><h1>{h1}</h1><p class="lead">{lead}</p>
  <div class="hero-btns"><a class="btn btn-accent" href="/en/contact/#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></section>'''

# ---------------- EN HOME ----------------
rev_cards="".join(revcard(i,n,t,meta="Facebook review",date="recommends",more="View on Facebook →") for i,(n,t) in enumerate(ALLREV[:9]))

TILES=[("/en/services/wooden-fence/","luxaed-svc-wood","Wood","Wooden fences","Wooden fences & gates on a steel frame. A warm, tidy look."),
 ("/en/services/metal-fence/","luxaed-svc-profnastil","Corrugated","Corrugated (metal) fences","A solid profiled-sheet fence for privacy. Affordable and fast."),
 ("/en/services/mesh-fence/","luxaed-svc-mesh","Mesh","Mesh / 3D fences","Welded panels (3D), anthracite RAL. Strong and modern."),
 ("/en/services/gates-automation/","luxaed-svc-gates","Automation","Gates & automation","Sliding & swing gates, automation and intercoms.")]
tiles_html="".join(f'''<a class="step-ph" href="{u}"><div class="img-wrap"><picture><source type="image/webp" srcset="/img/{im}.webp"><img src="/img/{im}.jpg" alt="{n}" loading="lazy"></picture></div>
<div class="sp-top-label"><span>{lbl}</span></div><div class="sp-body"><h3>{n}</h3><p>{d}</p></div></a>''' for u,im,lbl,n,d in TILES)

AREAS=["Tallinn","Kesklinn","Lasnamäe","Mustamäe","Haabersti","Kristiine","Põhja-Tallinn","Pirita","Nõmme","Viimsi","Maardu","Saue","Keila","Harku","Rae","Harjumaa"]
areas_html="".join(f'<span class="area-pill">{a}</span>' for a in AREAS)

HOME_FAQ=[("How much does a fence or gate cost?","We can't give an exact price upfront — it depends on the material, fence length and height, terrain and gates. After a free measurement we give a specific price with no hidden fees."),
 ("What kinds of fences do you make?","Wooden fences (on a steel frame), corrugated-sheet fences and welded mesh fences (3D). We'll help you choose the material for your budget and plot."),
 ("Do you install gate automation?","Yes, we install automation for sliding and swing gates, remotes, photocells and intercoms. We can add automation to existing gates too."),
 ("Which areas do you serve?","Tallinn and all of Harjumaa. Further afield — by arrangement, just write to us."),
 ("Do you repair fences?","Yes, we repair fences and gates: replacing sections and posts, adjusting gates, repairing automation.")]
home_faq_schema=['<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in HOME_FAQ]},ensure_ascii=False)+'</script>']
lb_schema=['<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"LuxAed","image":DOMAIN+"/img/luxaed-hero.jpg","url":DOMAIN+"/en/","telephone":PHONE,"email":EMAIL,"priceRange":"€€","address":{"@type":"PostalAddress","addressLocality":"Tallinn","addressRegion":"Harjumaa","addressCountry":"EE"},"areaServed":["Tallinn","Harjumaa","Estonia"],"sameAs":[FB]},ensure_ascii=False)+'</script>']

home_inner=f'''<section class="hero">
  <div class="hero-photo-bg"></div>
  <div class="wrap"><div class="hero-grid"><div>
    <div class="hero-kicker hand">Hi! A new fence coming up?</div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><span class="ht-label">34 reviews on Facebook · recommend</span></div>
    <h1>Fences & gates</h1>
    <p class="hero-claim"><em>One call</em><br>and your fence is done</p>
    <div class="hero-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>{form_html()}</div>
  <div class="hero-stats"><div class="hstat"><b>100%</b><span>recommend on Facebook</span></div><div class="hstat"><b>34</b><span>reviews</span></div><div class="hstat"><b>5</b><span>years in business (since 2021)</span></div></div></div>
</section>

<section class="info-strip"><div class="wrap"><div class="info-inner">
  <div><span class="tag">What we do</span><h2 class="info-title">Fences and gates,<br>turnkey.</h2></div>
  <div><p>LuxAed manufactures and installs <b>fences, gates and wickets</b> and fits <b>gate automation and intercoms</b>. We work with wood, profiled sheet and welded mesh in Tallinn and Harjumaa.</p></div>
</div></div></section>

<section class="section svc-hide" id="teenused"><div class="wrap"><span class="tag">Our services</span><h2 class="big big--xl">A solution for every plot</h2>
  <p class="lead lead--lg">Choose a fence or gate type — we'll advise what fits, come for a free measurement and calculate the price.</p>
  <div class="steps-ph">{tiles_html}</div></div></section>

<div class="mini-cta"><div class="wrap"><span>Not sure which fence suits you?</span>
  <div class="mini-cta-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></div>

<section class="section"><div class="wrap"><span class="tag">Reviews on Facebook</span><h2 class="big" style="margin-bottom:32px">Trusted across Tallinn and Harjumaa</h2>
  <div class="gbp-wrap">
    <div class="gbp-panel">
      <div class="gbp-photos"><div class="gbp-photo-main" style="background:url('/img/luxaed-hero.jpg') center/cover"></div>
        <div class="gbp-photo-stack"><div style="background:url('/img/luxaed-svc-wood.jpg') center/cover;flex:1;border-radius:0 12px 0 0"></div><div style="background:url('/img/luxaed-svc-mesh.jpg') center/cover;flex:1;border-radius:0 0 12px 0"></div></div></div>
      <div class="gbp-body">
        <div class="gbp-title-row"><h3 class="gbp-name">Fences and gates LuxAed</h3>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="#1877F2" aria-hidden="true"><path d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.68.24 2.68.24v2.97h-1.51c-1.49 0-1.95.93-1.95 1.88v2.26h3.32l-.53 3.49h-2.79V24C19.61 23.1 24 18.1 24 12.07z"/></svg></div>
        <div class="gbp-rating-row"><span class="gbp-stars">★★★★★</span><a class="gbp-cnt" href="{FB}" target="_blank" rel="noopener">34 reviews on Facebook</a></div>
        <p class="gbp-type">Fences, gates & automation &middot; Tallinn</p>
        <div class="gbp-actions"><a class="gbp-btn" href="{FB}" target="_blank" rel="noopener">Facebook</a><a class="gbp-btn" href="tel:{TEL}">Call</a></div>
        <div class="gbp-opts"><span><span class="gbp-check">&#10003;</span> Fences</span><span><span class="gbp-check">&#10003;</span> Gates</span><span><span class="gbp-check">&#10003;</span> Automation</span></div>
        <hr class="gbp-hr">
        <div class="gbp-details"><div class="gbp-row"><span>Tallinn, Harjumaa</span></div><div class="gbp-row"><b style="color:#188038">100% recommend</b></div><div class="gbp-row"><a href="tel:{TEL}" style="color:#1a73e8">{PHONE}</a></div></div>
      </div>
    </div>
    <div class="gbp-reviews">
      <div class="gbp-rev-hd"><span class="gbp-rev-score">34</span><div class="gbp-rev-divider"></div><div class="gbp-rev-mid"><div class="gbp-rev-stars">★★★★★</div><div class="gbp-rev-cnt">reviews on Facebook · recommend</div></div><a class="gbp-rev-link" href="{FB}/reviews" target="_blank" rel="noopener">All reviews →</a></div>
      <div class="gbp-rev-list">{rev_cards}</div>
    </div>
  </div></div></section>

<section class="section section--alt"><div class="wrap"><span class="tag">How we work</span><h2 class="big">Four simple steps</h2>{PROCESS}</div></section>

<section class="section section--dark svc-hide" id="meist" style="position:relative;overflow:hidden"><div style="position:absolute;inset:0;background:url('/img/luxaed-wide-wood.webp') center/cover no-repeat;opacity:.08"></div>
  <div class="wrap" style="position:relative"><span class="tag">About us</span><h2 class="big big--xl">Fences are what we do every day.</h2>
  <p class="lead lead--lg">LuxAed is a team building fences, gates and wickets in Tallinn and Harjumaa. Wood, profiled sheet, welded mesh, gate automation and intercoms. Neatly, at an honest price and with a quote before we start.</p>
  <div class="nums"><div class="num"><b>100<small>%</small></b><div class="t">Recommend</div><p>Based on Facebook reviews</p></div><div class="num"><b>34</b><div class="t">Reviews</div><p>Real customer reviews on Facebook</p></div><div class="num"><b>5</b><div class="t">Years</div><p>Building fences since 2021</p></div><div class="num"><b>300</b><div class="t">Projects</div><p>Fences and gates installed</p></div></div></div></section>

<section class="section"><div class="wrap"><span class="tag">Gallery</span><h2 class="big">Examples of our fences and gates</h2><p class="lead">Real photos of completed work. Click a photo to open it.</p>
  <div class="gal" id="gal">
    <a href="/img/luxaed-svc-wood.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-svc-wood.webp"><img src="/img/luxaed-svc-wood.jpg" alt="Wooden fence on a steel frame" loading="lazy"></picture></a>
    <a href="/img/luxaed-g1.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-g1.webp"><img src="/img/luxaed-g1.jpg" alt="Wooden fence and sliding gate" loading="lazy"></picture></a>
    <a href="/img/luxaed-svc-mesh.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-svc-mesh.webp"><img src="/img/luxaed-svc-mesh.jpg" alt="Welded mesh fence" loading="lazy"></picture></a>
    <a href="/img/luxaed-g4.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-g4.webp"><img src="/img/luxaed-g4.jpg" alt="Mesh gate with automation" loading="lazy"></picture></a>
    <a href="/img/luxaed-g3.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-g3.webp"><img src="/img/luxaed-g3.jpg" alt="Metal fence in the evening" loading="lazy"></picture></a>
    <a href="/img/luxaed-g6.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-g6.webp"><img src="/img/luxaed-g6.jpg" alt="Gate automation" loading="lazy"></picture></a>
  </div></div></section>

<section class="section section--alt svc-hide" id="piirkonnad" aria-label="Service area"><div class="wrap"><span class="tag">Service area</span><h2 class="big">Where we work</h2>
  <p class="lead">Fences, gates and automation in Tallinn and all of Harjumaa.</p><div class="area-pills">{areas_html}</div></div></section>

<section class="section" id="kkk"><div class="wrap"><span class="tag">FAQ</span><h2 class="big">What people ask before ordering</h2>{faqx(HOME_FAQ)}</div></section>

<section class="cta-final"><div class="wrap"><h2>Ready to discuss <em>a fence or gate</em>?</h2>
  <p>Leave a request or call — we'll come for a free measurement and give an exact price.</p>
  <div class="hero-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></section>'''
page("/en/","Fences and gates in Tallinn and Harjumaa — LuxAed","LuxAed — manufacture and installation of fences and gates in Tallinn and Harjumaa. Wooden, corrugated and mesh fences, gate automation and intercoms. Free measurement. 100% recommend on Facebook.", home_inner, sch=lb_schema+home_faq_schema)

# ---------------- EN ABOUT ----------------
about=f'''{hero("About us","About LuxAed","We build and install fences, gates and wickets in Tallinn and Harjumaa — wood, corrugated sheet, welded 3D mesh, gate automation and intercoms.", crumb="About")}
<section class="section"><div class="wrap"><span class="tag">Who we are</span><h2 class="big">Fences and gates — what we do every day</h2>
<p class="lead">LuxAed has been installing fences, gates and wickets in Tallinn and Harjumaa <b>since 2021</b>. Customers across the region trust us, and our Facebook page has <b>34 reviews and 100% recommendations</b>.</p>
<p class="lead" style="margin-top:14px">We take care of everything: we come for a free measurement, buy the materials, install and hand over the finished job. We keep you posted on what's done and what's next. We work neatly, at an honest price, and quote before we start. And unlike many, <b>we work year-round — even in winter</b>.</p>
<ul class="svc-bens"><li>In business since 2021 in Tallinn and Harjumaa</li><li>Fences from wood, profiled sheet and welded mesh</li><li>Sliding and swing gates, automation and intercoms</li><li>We handle buying the materials</li><li>We keep you posted at every stage</li><li>Free measurement and quote, warranty on the work</li><li>We work year-round, including winter</li><li>Repair and maintenance of existing structures</li></ul></div></section>
<section class="section section--dark" style="position:relative;overflow:hidden"><div style="position:absolute;inset:0;background:url('/img/luxaed-post-install-1.webp') center/cover no-repeat;opacity:.08"></div>
<div class="wrap" style="position:relative"><span class="tag">Trusted by customers</span><h2 class="big big--xl">The reviews speak for us</h2>
<p class="lead lead--lg">Customers recommend LuxAed for speed, quality and a professional approach. See the reviews on our Facebook page.</p>
<div class="nums"><div class="num"><b>100<small>%</small></b><div class="t">Recommend</div><p>Based on Facebook reviews</p></div><div class="num"><b>34</b><div class="t">Reviews</div><p>Real customer reviews</p></div><div class="num"><b>5</b><div class="t">Years</div><p>Building fences since 2021</p></div><div class="num"><b>2</b><div class="t">Regions</div><p>Tallinn and Harjumaa</p></div></div></div></section>
<section class="cta-final"><div class="wrap"><h2>Shall we discuss <em>your fence or gate</em>?</h2><p>Leave a request or call — we'll come for a free measurement.</p>
<div class="hero-btns"><a class="btn btn-accent" href="/en/contact/#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></section>'''
page("/en/about/","About LuxAed — fences and gates in Tallinn","LuxAed — manufacture and installation of fences and gates in Tallinn and Harjumaa. Wood, corrugated sheet, mesh, automation and intercoms. Since 2021.", about)

# ---------------- EN FAQ ----------------
faq_inner=f'''{hero("FAQ","Frequently asked questions","We've gathered answers to the questions people most often ask before ordering a fence or gate.", crumb="FAQ")}
<section class="section"><div class="wrap"><span class="tag">FAQ</span><h2 class="big">What people ask before ordering</h2>{faqx(HOME_FAQ)}</div></section>
<section class="cta-final"><div class="wrap"><h2>Didn't find your answer?</h2><p>Call or write — we'll advise and come for a free measurement.</p>
<div class="hero-btns"><a class="btn btn-accent" href="/en/contact/#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></section>'''
page("/en/faq/","FAQ — fences and gates — LuxAed","Frequently asked questions about fences, gates and automation in Tallinn: price, materials, timing, automation, repair. LuxAed.", faq_inner, sch=home_faq_schema)

# ---------------- EN CONTACT ----------------
contact=f'''{hero("Contact","Get in touch with LuxAed","Fences, gates and automation in Tallinn and Harjumaa. Call, write or leave a request — we'll come for a free measurement.", crumb="Contact")}
<section class="section"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Contact</span><h2 class="big">How to reach us</h2></div>
  <div class="equip-body"><ul class="spec">
    <li><span>Phone</span><span><a href="tel:{TEL}" style="color:var(--accent);font-weight:700">{PHONE}</a></span></li>
    <li><span>Email</span><span><a href="mailto:{EMAIL}" style="color:var(--accent);font-weight:700">{EMAIL}</a></span></li>
    <li><span>Facebook</span><span><a href="{FB}" target="_blank" rel="noopener" style="color:var(--accent);font-weight:700">Fences and gates LuxAed</a></span></li>
    <li><span>Area</span><span>Tallinn, Harjumaa, Estonia</span></li>
    <li><span>Opening hours</span><span>Mon–Fri 09–18, Sat by appointment</span></li></ul>
    <p class="lead">The fastest way is to call or leave a request in the form. We'll call back, clarify the details and arrange a free measurement.</p></div>
  <div class="equip-img">{form_html().replace('<div class="form-slot">','').replace('</div></div>','</div>')}</div>
</div></div></section>'''
page("/en/contact/","Contact — LuxAed fences and gates in Tallinn","LuxAed contact: phone "+PHONE+", email "+EMAIL+", Facebook. Fences, gates and automation in Tallinn and Harjumaa. Leave a request for a free measurement.", contact)

# ---------------- EN LEGAL ----------------
def legal(path,title,h1,kicker,blocks):
    inner=f'''{hero(kicker,h1,"",img="luxaed-g3",crumb=h1)}
<section class="section"><div class="wrap" style="max-width:820px">
{"".join(f"<h2 class='big' style='font-size:24px;margin-top:28px'>{t}</h2><p class='lead' style='margin-top:10px'>{b}</p>" for t,b in blocks)}
<p class="lead" style="margin-top:26px">For questions about this document, write to <a href="mailto:{EMAIL}" style="color:var(--accent)">{EMAIL}</a>.</p></div></section>'''
    page(path,title,h1+" — LuxAed, fences and gates in Tallinn.",inner)

legal("/en/privacy/","Privacy policy — LuxAed","Privacy policy","Privacy",[
 ("Who processes the data","LuxAed (fences and gates, Tallinn, Estonia) processes personal data you provide when contacting us via the website, phone, email or Facebook."),
 ("What data we collect","Name, phone, email, site address and a description of the task, plus any photos you attach to a request. We need this data to prepare a quote and get in touch with you."),
 ("Purpose and legal basis","Data is used only to respond to your request, prepare an offer and provide the service. The legal basis is your consent and the preparation of a contract."),
 ("Data retention","We keep the data as long as needed to process the request and deliver the service, then delete it unless there are other legal grounds for keeping it."),
 ("Sharing with third parties","We do not sell or share your data with third parties, except where required by law."),
 ("Your rights","You have the right to request access to your data, its correction or deletion, and to withdraw consent. To do so, contact us by email."),
 ("Cookies","The website may use technical cookies for correct operation. Analytics and advertising scripts are loaded only with the relevant consent."),
])
legal("/en/terms/","Terms of service — LuxAed","Terms of service","Terms",[
 ("General","These terms describe how LuxAed provides services for manufacturing, installing and repairing fences, gates and automation in Tallinn and Harjumaa."),
 ("Request and quote","You can leave a request by phone, email or the form on the website. The price is determined after a free measurement and agreed before work begins."),
 ("Measurement and agreements","The exact price, materials and timing are fixed after visiting the site. All key terms are agreed with the customer in advance."),
 ("Payment","The order and method of payment are agreed individually before work begins. We do not add hidden charges to the agreed estimate without your consent."),
 ("Warranty and quality","We are responsible for the quality of the work performed. Warranty terms depend on the type of work and materials and are agreed when the arrangement is made."),
 ("Liability","LuxAed is not liable for damage caused by hidden utilities on the site that the customer did not disclose, nor for force majeure."),
 ("Contact","For any questions about the services and terms, contact us at "+PHONE+" or "+EMAIL+"."),
])
print("EN home + support done")
