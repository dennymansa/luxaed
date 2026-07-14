#!/usr/bin/env python3
# EN home + EN support pages (about, faq, contact, privacy, terms)
import json, html
from build_pages import head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN, partners_marquee, video_block, video_schema, home_video_items, about_page_schema, person_artur_schema, webpage_schema
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
    cr=''  # visible breadcrumbs removed per request (JSON-LD kept for SEO)
    return f'''<section class="svc-hero"><div class="hero-photo-bg" style="background:url('/img/{img}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap">{cr}<span class="tag">{kicker}</span><h1>{h1}</h1><p class="lead">{lead}</p>
  <div class="hero-btns"><a class="btn btn-accent" href="/en/#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></section>'''

# ---------------- EN HOME ----------------
rev_cards="".join(revcard(i,n,t,meta="Facebook review",date="recommends",more="View on Facebook →") for i,(n,t) in enumerate(ALLREV[:9]))

TILES=[("/en/services/wooden-fence/","luxaed-svc-wood","Wood","Wooden fences","Wooden fences & gates on a steel frame. A warm, tidy look."),
 ("/en/services/metal-fence/","luxaed-svc-profnastil","Corrugated","Corrugated (metal) fences","A solid profiled-sheet fence for privacy. Affordable and fast."),
 ("/en/services/mesh-fence/","luxaed-svc-mesh","Mesh","Mesh / 3D fences","Welded panels (3D), anthracite RAL. Strong and modern."),
 ("/en/services/gates-automation/","luxaed-svc-gates","Automation","Gates & automation","Sliding & swing gates, automation and intercoms.")]
tiles_html="".join(f'''<a class="step-ph" href="{u}"><div class="img-wrap"><picture><source type="image/webp" srcset="/img/{im}.webp"><img src="/img/{im}.jpg" alt="{n}" width="600" height="400" loading="lazy"></picture></div>
<div class="sp-top-label"><span>{lbl}</span></div><div class="sp-body"><h3>{n}</h3><p>{d}</p></div></a>''' for u,im,lbl,n,d in TILES)

AREAS=["Tallinn","Kesklinn","Lasnamäe","Mustamäe","Haabersti","Kristiine","Põhja-Tallinn","Pirita","Nõmme","Viimsi","Maardu","Saue","Keila","Harku","Rae","Harjumaa"]
areas_html="".join(f'<span class="area-pill">{a}</span>' for a in AREAS)

HOME_FAQ=[("How much does a fence or gate cost?","We can't give an exact price upfront. It depends on the material, fence length and height, terrain and gates. After a free measurement we give a specific price with no hidden fees."),
 ("What kinds of fences do you make?","Wooden fences (on a steel frame), corrugated-sheet fences and welded mesh fences (3D). We'll help you choose the material for your budget and plot."),
 ("Do you install gate automation?","Yes, we install automation for sliding and swing gates, remotes, photocells and intercoms. We can add automation to existing gates too."),
 ("Which areas do you serve?","Tallinn and all of Harjumaa. Further afield by arrangement, just write to us."),
 ("Do you repair fences?","Yes, we repair fences and gates: replacing sections and posts, adjusting gates, repairing automation."),
 ("How long does installation take?","The timeline depends on the scope of work and the material. We give an estimated date after the measurement and project approval."),
 ("Do I need to prepare anything on the plot?","Ideally, clear access along the line of the future fence. We agree the rest individually depending on the state of the plot."),
 ("How can I reach you?","The easiest way is to call +372 5695 8285 or leave a request on the website. We are always available."),
]
home_faq_schema=['<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in HOME_FAQ]},ensure_ascii=False)+'</script>']
lb_schema=['<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"LuxAed","image":DOMAIN+"/img/luxaed-hero.jpg","logo":DOMAIN+"/img/luxaed-logo.png","url":DOMAIN+"/en/","telephone":PHONE,"email":EMAIL,"priceRange":"€€","address":{"@type":"PostalAddress","addressLocality":"Tallinn","addressRegion":"Harjumaa","addressCountry":"EE"},"areaServed":["Tallinn","Harjumaa","Estonia"],"sameAs":[FB],"geo":{"@type":"GeoCoordinates","latitude":59.437,"longitude":24.7536},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"18:00"}],"aggregateRating":{"@type":"AggregateRating","ratingValue":"5","bestRating":"5","reviewCount":"34"}},ensure_ascii=False)+'</script>']

home_inner=f'''<section class="hero">
  <div class="hero-photo-bg"></div>
  <div class="wrap"><div class="hero-grid"><div>
    <div class="hero-kicker hand">Hey! Need a new fence?</div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">34 reviews on Facebook · recommend</a></div>
    <h1>Fences & gates</h1>
    <p class="hero-claim"><em>turnkey</em><br>from measurement to install</p>
    <div class="hero-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>{form_html()}</div>
  <div class="hero-stats"><div class="hstat"><b>100%</b><span>recommend on Facebook</span></div><div class="hstat"><b>34</b><span>reviews</span></div><div class="hstat"><b>15</b><span>years of craft experience</span></div></div></div>
</section>

<section class="info-strip"><div class="wrap"><div class="info-inner">
  <div><span class="tag">What we do</span><h2 class="info-title">Fences and gates,<br>turnkey.</h2></div>
  <div><p>We help choose, build and install <b>fences, gates and pedestrian gates</b> for private homes and commercial sites in Tallinn and Harjumaa. We also fit <b>gate automation</b> and repair existing structures.</p></div>
</div></div></section>

<section class="section svc-hide" id="teenused"><div class="wrap"><span class="tag">Our services</span><h2 class="big big--xl">Fences and gates for every plot</h2>
  <p class="lead lead--lg">Choose a fence or gate type. We'll help you pick the right solution, come for a free measurement and calculate the price.</p>
  <div class="steps-ph">{tiles_html}</div></div></section>

<div class="mini-cta"><div class="wrap"><span>Not sure which fence suits you?</span>
  <div class="mini-cta-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></div>

<section class="section"><div class="wrap"><span class="tag">Reviews on Facebook</span><h2 class="big" style="margin-bottom:32px">Trusted across Tallinn and Harjumaa</h2>
  <div class="gbp-wrap">
    <div class="gbp-panel">
      <div class="gbp-photos"><div class="gbp-photo-main" style="background:url('/img/luxaed-hero-mobile.webp') center/cover"></div>
        <div class="gbp-photo-stack"><div style="background:url('/img/luxaed-svc-wood-mobile.webp') center/cover;flex:1;border-radius:0 12px 0 0"></div><div style="background:url('/img/luxaed-svc-mesh-mobile.webp') center/cover;flex:1;border-radius:0 0 12px 0"></div></div></div>
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
      <div class="gbp-rev-hd"><span class="gbp-rev-score">34</span><div class="gbp-rev-divider"></div><div class="gbp-rev-mid"><div class="gbp-rev-stars">★★★★★</div><div class="gbp-rev-cnt">reviews on Facebook · recommended</div></div><a class="gbp-rev-link" href="{FB}/reviews" target="_blank" rel="noopener">All reviews →</a></div>
      <div class="rev-carousel" role="region" aria-label="Customer reviews on Facebook">
        <button class="rev-arrow rev-prev" type="button" aria-label="Previous review">‹</button>
        <div class="rev-viewport"><div class="gbp-rev-list rev-track">{rev_cards}</div></div>
        <button class="rev-arrow rev-next" type="button" aria-label="Next review">›</button>
      </div>
    </div>
  </div></div></section>

<section class="section section--alt"><div class="wrap"><span class="tag">How we work</span><h2 class="big">Fence installation: four simple steps</h2>{PROCESS}</div></section>
<section class="section"><div class="wrap"><span class="tag">Honest about prices</span><h2 class="big">Fence and gate price: what's included and what depends</h2>
<p class="lead">The price depends on the material, fence length, terrain and gate complexity. So there's no fixed price list. We give the exact price after a free measurement.</p>
<div class="honest">
  <div class="hon good"><h3>Always included</h3><ul><li>Site measurement</li><li>Advice on material and construction</li><li>A quote before the work begins</li><li>Installing posts and sections</li><li>Fitting the hardware and, if needed, automation</li><li>Checking the gates after installation</li></ul></div>
  <div class="hon bad"><h3>Depends on the project</h3><ul><li>Choice of material (wood, corrugated sheet, 3D mesh)</li><li>Fence length and height, number of gates</li><li>Terrain complexity and base preparation</li><li>Gate automation and intercom. Optional</li><li>Removing the old fence</li></ul></div>
</div></div></section>

<section class="section section--dark svc-hide" id="meist" style="position:relative;overflow:hidden"><div style="position:absolute;inset:0;background:url('/img/luxaed-sunset.webp') center 40%/cover no-repeat;pointer-events:none"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(8,10,16,.95) 0%, rgba(10,12,20,.82) 40%, rgba(12,10,16,.9) 100%);pointer-events:none"></div>
  <div class="wrap" style="position:relative"><span class="tag">About us</span><h2 class="big big--xl">Fences are our craft.</h2>
  <p class="lead lead--lg">LuxAed is a team building fences, gates and pedestrian gates in Tallinn and Harjumaa.<br>Wood, profiled sheet, welded mesh, gate automation and intercoms.<br>Neatly, at a fair price and with a quote before the work begins.</p>
  </div></section>

<section class="section"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Equipment</span><h2 class="big">The right kit, an experienced crew, a tidy result.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-w-van.webp"><img src="/img/luxaed-w-van.jpg" width="750" height="563" alt="LuxAed van on site" loading="lazy"></picture></div>
  <div class="equip-body"><ul class="spec">
    <li><b>Post auger and rammer</b>: posts go in firm and level</li>
    <li><b>Welding and cutting on site</b>: steel frames and gate frames</li>
    <li><b>Levelling and measuring</b>: sections in one line, even on a slope</li>
    <li><b>Automation and intercoms</b>: set up and connected turnkey</li>
    <li><b>Clean site</b>: we clean up after ourselves and hand the plot over tidy</li>
  </ul></div></div></div></section>

<section class="section"><div class="wrap"><span class="tag">Gallery</span><h2 class="big">Examples of our fences and gates</h2><p class="lead">Real photos of completed work. Click a photo to open it.</p>
  <div class="gal" id="gal">
    <a href="/img/luxaed-svc-wood.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-svc-wood.webp"><img src="/img/luxaed-svc-wood.jpg" alt="Wooden fence on a steel frame" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-gates-auto.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-gates-auto.webp"><img src="/img/luxaed-w-gates-auto.jpg" alt="Sliding gate with automation" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-mesh-1.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-mesh-1.webp"><img src="/img/luxaed-w-mesh-1.jpg" alt="3D welded-panel fence" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-lippaed-1.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-lippaed-1.webp"><img src="/img/luxaed-w-lippaed-1.jpg" alt="Steel picket fence" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-g1.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-g1.webp"><img src="/img/luxaed-g1.jpg" alt="Wooden fence and sliding gate" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-gates-green.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-gates-green.webp"><img src="/img/luxaed-w-gates-green.jpg" alt="Swing gates from panels" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-gates-graphite.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-gates-graphite.webp"><img src="/img/luxaed-w-gates-graphite.jpg" alt="Graphite swing gates" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-mesh-2.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-mesh-2.webp"><img src="/img/luxaed-w-mesh-2.jpg" alt="Green 3D panel fence" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-van.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-van.webp"><img src="/img/luxaed-w-van.jpg" alt="LuxAed van on site" width="600" height="400" loading="lazy"></picture></a>
  </div>
  <div style="text-align:center;margin-top:30px"><a class="gal-fb" href="{FB}/photos_by" target="_blank" rel="noopener">More photos on our Facebook →</a></div></div></section>

{video_block("en")}

<section class="section section--alt svc-hide" id="piirkonnad" aria-label="Service area"><div class="wrap"><span class="tag">Service area</span><h2 class="big">Fence and gate installation in Tallinn and Harjumaa</h2>
  <p class="lead">Fences, gates and automation in Tallinn and all of Harjumaa.</p><div class="area-pills">{areas_html}</div></div></section>

<section class="section" id="kkk"><div class="wrap"><span class="tag">FAQ</span><h2 class="big">What people ask before ordering</h2>{faqx(HOME_FAQ)}</div></section>

<section class="cta-final"><div class="wrap"><h2>Ready to discuss <em>a fence or gate</em>?</h2>
  <p>Leave a request or call. We'll come for a free measurement and give an exact price.</p>
  <div class="hero-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></section>'''
page("/en/","Fences and gates installation in Tallinn and Harjumaa — LuxAed","Fences and gates in Tallinn and Harjumaa. Wood, corrugated sheet, 3D mesh panels, gate automation. Free measurement. 100% recommend on Facebook.", home_inner, sch=lb_schema+home_faq_schema+video_schema(home_video_items("en"),"en"))

# ---------------- EN ABOUT ----------------
about=f'''<section class="hero hero--compact">
  <div class="hero-photo-bg" style="background:url('/img/luxaed-hero.webp') center 45%/cover no-repeat"></div>
  <div class="wrap"><div class="hero-grid" style="grid-template-columns:1fr;gap:0"><div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">34 reviews on Facebook · recommend</a></div>
    <h1>Who we are</h1>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:16px;max-width:720px">We have been manufacturing and installing fences, gates and pedestrian gates in Tallinn and Harjumaa <b>for over 15 years</b>. We work with wood, profiled sheet and welded 3D mesh, fit gate automation and intercoms, and repair existing structures. Our lead installer has worked with every fence type, soil and drainage situation.</p>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:12px;max-width:720px">We take the whole process off your hands: we come for a free measurement, buy the materials, install and hand over the finished job. We name the price up front. No hidden extras or surprises.</p>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:12px;max-width:720px">A new fence around the cottage, a sliding gate with automation, or a full perimeter. We handle it all.</p>
  </div></div>
  <div class="hero-stats"><div class="hstat"><b>100%</b><span>Recommend on Facebook</span></div><div class="hstat"><b>34</b><span>Reviews</span></div><div class="hstat"><b>15</b><span>Years of craft experience</span></div></div></div>
</section>
<section class="section"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Master craftsman</span><h2 class="big">Artur Mustafin.<br>Over 15 years of experience building fences and gates.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-w-crew.webp"><img src="/img/luxaed-w-crew.jpg" width="750" height="1000" alt="LuxAed master installing a fence" loading="lazy"></picture></div>
  <div class="equip-body"><p class="lead" style="margin-bottom:14px">Artur has been building fences and gates in Tallinn and Harjumaa for 15 years. He knows in advance which solution suits your plot and how to avoid unnecessary costs.</p><ul class="svc-bens">
    <li>Over 15 years of experience building fences and gates</li>
    <li>Thousands of completed projects in Tallinn and Harjumaa</li>
    <li>Quality control at every stage of the work</li>
  </ul></div>
</div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">Principles</span><h2 class="big">What matters to us</h2>
<div class="svc-cards">
<div class="svc-card"><div class="ic">1</div><h3>Everything with one call</h3><p>Measurement, materials, installation and repair from one place. One call, and it's all arranged.</p></div>
<div class="svc-card"><div class="ic">2</div><h3>We work year-round</h3><p>We install fences in winter too. Frozen ground is no obstacle. We don't push you to spring.</p></div>
<div class="svc-card"><div class="ic">3</div><h3>Careful hands</h3><p>We work cleanly, protect your plot and clean up after ourselves. We hand the site over tidy.</p></div>
<div class="svc-card"><div class="ic">4</div><h3>Exact price up front</h3><p>We name the price before we start and stick to it. No hidden extras or surprises on the invoice.</p></div>
</div></div></section>
<section class="section"><div class="wrap"><span class="tag">Why us</span><h2 class="big">Why LuxAed</h2>
<ul class="svc-bens"><li>Over <b>15 years</b> of experience in Tallinn and Harjumaa</li><li>Fences from wood, profiled sheet and welded mesh</li><li>Sliding and swing gates, automation and intercoms</li><li>We handle buying the materials and the whole process</li><li>Free measurement, price up front, warranty on the work</li><li>We work year-round, including winter</li></ul></div></section>
<section class="section section--dark" style="position:relative;overflow:hidden"><div style="position:absolute;inset:0;background:url('/img/luxaed-sunset.webp') center 40%/cover no-repeat;pointer-events:none"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(8,10,16,.95) 0%, rgba(10,12,20,.82) 40%, rgba(12,10,16,.9) 100%);pointer-events:none"></div>
<div class="wrap" style="position:relative"><span class="tag">Trusted by customers</span><h2 class="big big--xl">The reviews speak for us</h2>
<p class="lead lead--lg">Customers recommend LuxAed for speed, quality and a professional approach.<br>See the reviews on our <a href="{FB}" target="_blank" rel="noopener" style="color:var(--accent)">Facebook</a> page.</p>
</div></section>
<section class="section section--alt"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Equipment</span><h2 class="big">The right kit, an experienced crew, a tidy result.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-w-van.webp"><img src="/img/luxaed-w-van.jpg" width="750" height="563" alt="LuxAed crew and branded van on site" loading="lazy"></picture></div>
  <div class="equip-body"><ul class="spec">
    <li><b>Post auger and rammer</b>: posts go in firm and level</li>
    <li><b>Welding and cutting on site</b>: steel frames and gate frames</li>
    <li><b>Levelling and measuring</b>: sections in one line, even on a slope</li>
    <li><b>Automation and intercoms</b>: set up and connected turnkey</li>
    <li><b>Clean site</b>: we clean up after ourselves and hand the plot over tidy</li>
  </ul></div>
</div></div></section>
<section class="cta-final"><div class="wrap"><h2>Shall we discuss <em>your fence or gate</em>?</h2><p>Leave a request or call. We'll come for a free measurement.</p>
<div class="hero-btns"><a class="btn btn-accent" href="/en/#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></section>'''
page("/en/about/","About LuxAed. Fences and gates in Tallinn","LuxAed. Fences and gates in Tallinn and Harjumaa. Wood, corrugated sheet, mesh, automation and intercoms. Over 15 years of experience.", about, sch=[about_page_schema("/en/about/","en","About LuxAed","Fence and gate master Artur Mustafin and the LuxAed story in Tallinn and Harjumaa."),person_artur_schema("en")])

# ---------------- EN FAQ ----------------
faq_inner=f'''{hero("FAQ","Frequently asked questions","We've gathered answers to the questions people most often ask before ordering a fence or gate.", crumb="FAQ")}
<section class="section"><div class="wrap"><span class="tag">FAQ</span><h2 class="big">What people ask before ordering</h2>{faqx(HOME_FAQ)}</div></section>
<section class="cta-final"><div class="wrap"><h2>Didn't find your answer?</h2><p>Call or write.<br>We'll advise and come for a free measurement.</p>
<div class="hero-btns"><a class="btn btn-accent" href="/en/#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></section>'''
page("/en/faq/","FAQ. Fences and gates — LuxAed","Frequently asked questions about fences, gates and automation in Tallinn: price, materials, timing, automation, repair. LuxAed.", faq_inner, og="/img/luxaed-wide-wood.jpg", sch=home_faq_schema)

# ---------------- EN CONTACT ----------------

# ---------------- EN LEGAL ----------------
def legal(path,title,h1,kicker,blocks):
    inner=f'''{hero(kicker,h1,"",img="luxaed-g3",crumb=h1)}
<section class="section"><div class="wrap" style="max-width:820px">
{"".join(f"<h2 class='big' style='font-size:24px;margin-top:28px'>{t}</h2><p class='lead' style='margin-top:10px'>{b}</p>" for t,b in blocks)}
<p class="lead" style="margin-top:26px">For questions about this document, write to <a href="mailto:{EMAIL}" style="color:var(--accent)">{EMAIL}</a>.</p></div></section>'''
    page(path,title,h1+" — LuxAed, fences and gates in Tallinn.",inner,og="/img/luxaed-g3.jpg",sch=[webpage_schema(path,"en",title,h1)])

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
 ("Payment","Payment terms and method are agreed individually before work begins. We do not add hidden charges to the agreed estimate."),
 ("Warranty and quality","We are responsible for the quality of the work performed. Warranty terms depend on the type of work and materials and are agreed when the arrangement is made."),
 ("Liability","LuxAed is not liable for damage caused by hidden utilities on the site that the customer did not disclose, nor for force majeure."),
 ("Contact","For any questions about the services and terms, contact us at "+PHONE+" or "+EMAIL+"."),
])
print("EN home + support done")
