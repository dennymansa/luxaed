#!/usr/bin/env python3
# EN home + EN support pages (about, faq, contact, privacy, terms)
import json, html
from build_pages import head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN, partners_marquee, video_block, video_schema, home_video_items, about_page_schema, person_artur_schema, webpage_schema, service_tiles_html, REVIEW_COUNT, EXPERIENCE_YEARS, RECOMMEND_PERCENT, business_schema, website_schema
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

tiles_html=service_tiles_html("en")

AREAS=["Tallinn","Kesklinn","Lasnamäe","Mustamäe","Haabersti","Kristiine","Põhja-Tallinn","Pirita","Nõmme","Viimsi","Maardu","Saue","Keila","Harku","Rae","Harjumaa"]
areas_html="".join(f'<span class="area-pill">{a}</span>' for a in AREAS)

HOME_FAQ=[("How much does a fence or gate cost?","Typical installed prices: roll mesh €25–45/m, 3D panel €35–60/m and timber €90–160/m. Gates and automation are in our price guide. We confirm the exact price after a free measurement, with no hidden fees."),
 ("What kinds of fences do you make?","We build wooden fences, roll-mesh and chain-link fences, welded 2D/3D mesh fences, steel picket fences, welded metal-bar fences and profiled-sheet fences. If you have another design in mind, send us a photo or example."),
 ("How do you install fence posts?","We measure and mark the fence line, check the ground and choose the post spacing and installation depth for the fence height and expected load. We prepare or drill the holes for the ground conditions, level the posts and secure them for the chosen construction. We agree any old-post removal during the site survey."),
 ("Do you install gate automation?","Yes, we install automation for sliding and swing gates, remotes, photocells and intercoms. We can add automation to a suitable existing gate after checking its structure."),
 ("Which areas do you serve?","Tallinn and all of Harju County. Further afield by arrangement, just write to us."),
 ("Do you repair fences?","Yes, we repair fences and gates: replacing sections and posts, adjusting gates, repairing automation. Repair and diagnostics start from €90."),
 ("How long does installation take?","We put the exact schedule in the quote after the site measurement, because it depends on the fence length, material and gates. If the fence needs digging deeper than 30 cm, a building notice with a building design must be filed at least 10 days before work starts."),
 ("Do I need to prepare anything on the plot?","Clear access along the future fence line and know where your boundary markers are. Show us any underground cables or pipes at the measurement."),
 ("How can I reach you?","Call +372 5695 8285 (Mon–Fri 9–18), email luxaed9@gmail.com or leave a request on the website. We reply within one working day."),
]
# /en/faq/ adds questions that belong on the FAQ page only. The contact question
# stays last on both pages.
FAQ_ONLY=[("Do I need a building notice for a fence?","Usually, yes: since 1 August 2026, a fence whose construction involves digging deeper than 30 cm needs a building notice and a building design. The notice is filed in the Building Register at least 10 days before work starts, and we provide the fence's technical data."),
 ("Do you give a warranty on your work?","Yes. We give a 24-month warranty on installing new fences, gates and automation and on repair work, and materials also carry the manufacturer's warranty. The exact terms are in the quote and the contract."),
 ("How does payment work?","Payment terms and method are agreed before work starts. Nothing is added to the agreed price without your consent."),
]
FAQ_PAGE=HOME_FAQ[:-1]+FAQ_ONLY+HOME_FAQ[-1:]
# FAQPage schema only on /en/faq/; the homepage shows its questions without FAQ markup.
faq_page_schema=['<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ_PAGE]},ensure_ascii=False)+'</script>']
lb_schema=[business_schema(), website_schema()]

home_inner=f'''<section class="hero">
  <div class="hero-photo-bg"></div>
  <div class="wrap"><div class="hero-grid"><div>
    <div class="hero-kicker hand">Hey! Need a new fence?</div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">{RECOMMEND_PERCENT}% recommend</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">{REVIEW_COUNT} Facebook reviews</a></div>
    <h1>Fences & gates</h1>
    <p class="hero-claim"><em>turnkey</em><br>from measurement to installation</p>
    <div class="hero-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>{form_html()}</div>
  <div class="hero-stats"><div class="hstat"><b>{RECOMMEND_PERCENT}%</b><span>recommend on Facebook</span></div><div class="hstat"><b>{REVIEW_COUNT}</b><span>reviews</span></div><div class="hstat"><b>{EXPERIENCE_YEARS}+</b><span>years of experience</span></div></div></div>
</section>

<section class="info-strip"><div class="wrap"><div class="info-inner">
  <div><span class="tag">What we do</span><h2 class="info-title">Fence construction and installation</h2></div>
  <div><p>LuxAed is a fence installation company serving Tallinn and Harju County, from the first site measurement to the finished fence. Choose timber, profiled sheet, steel pickets, roll mesh or 2D/3D panels. We also provide <a href="/en/gates-automation/">automatic gate installation</a> and <a href="/en/intercoms-video-intercoms/">video intercoms with pedestrian-gate access</a>, so your whole entrance works together.</p></div>
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
        <div class="gbp-photo-stack"><div style="background:url('/img/luxaed-svc-wood-mobile.webp') center/cover;flex:1;border-radius:0 12px 0 0"></div><div style="background:url('/img/luxaed-w-mesh-1-mobile.webp') center/cover;flex:1;border-radius:0 0 12px 0"></div></div></div>
      <div class="gbp-body">
        <div class="gbp-title-row"><h3 class="gbp-name">Fences and gates LuxAed</h3>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="#1877F2" aria-hidden="true"><path d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.68.24 2.68.24v2.97h-1.51c-1.49 0-1.95.93-1.95 1.88v2.26h3.32l-.53 3.49h-2.79V24C19.61 23.1 24 18.1 24 12.07z"/></svg></div>
        <div class="gbp-rating-row"><span class="gbp-stars">★★★★★</span><a class="gbp-cnt" href="{FB}" target="_blank" rel="noopener">{REVIEW_COUNT} reviews on Facebook</a></div>
        <p class="gbp-type">Fences, gates & automation &middot; Tallinn</p>
        <div class="gbp-actions"><a class="gbp-btn" href="{FB}" target="_blank" rel="noopener">Facebook</a><a class="gbp-btn" href="tel:{TEL}">Call</a></div>
        <div class="gbp-opts"><span><span class="gbp-check">&#10003;</span> Fences</span><span><span class="gbp-check">&#10003;</span> Gates</span><span><span class="gbp-check">&#10003;</span> Automation</span></div>
        <hr class="gbp-hr">
        <div class="gbp-details"><div class="gbp-row"><span>Tallinn, Harjumaa</span></div><div class="gbp-row"><b style="color:#188038">{RECOMMEND_PERCENT}% recommend</b></div><div class="gbp-row"><a href="tel:{TEL}" style="color:#1a73e8">{PHONE}</a></div></div>
      </div>
    </div>
    <div class="gbp-reviews">
      <div class="gbp-rev-hd"><span class="gbp-rev-score">{REVIEW_COUNT}</span><div class="gbp-rev-divider"></div><div class="gbp-rev-mid"><div class="gbp-rev-stars">★★★★★</div><div class="gbp-rev-cnt">reviews on Facebook · recommended</div></div><a class="gbp-rev-link" href="{FB}/reviews" target="_blank" rel="noopener">All reviews →</a></div>
      <div class="rev-carousel" role="region" aria-label="Customer reviews on Facebook">
        <button class="rev-arrow rev-prev" type="button" aria-label="Previous review">‹</button>
        <div class="rev-viewport"><div class="gbp-rev-list rev-track">{rev_cards}</div></div>
        <button class="rev-arrow rev-next" type="button" aria-label="Next review">›</button>
      </div>
    </div>
  </div></div></section>

<section class="section section--alt"><div class="wrap"><span class="tag">How we work</span><h2 class="big">Fence installation: four simple steps</h2>{PROCESS}</div></section>
<section class="section"><div class="wrap"><span class="tag">Honest about prices</span><h2 class="big">Fence and gate price: what's included and what depends</h2>
<p class="lead">The price depends on the material, fence length, terrain and gates. You'll find typical ranges in our <a href="/en/prices/">price guide</a>, and we give the exact price after a free measurement.</p>
<div class="honest">
  <div class="hon good"><h3>Always included</h3><ul><li>Site measurement</li><li>Advice on material and construction</li><li>A quote before the work begins</li><li>Installing posts and sections</li><li>Fitting the hardware and any automation you order</li><li>Checking the gates after installation</li></ul></div>
  <div class="hon bad"><h3>Depends on the project</h3><ul><li>Choice of fence material and construction</li><li>Fence length and height, number of gates</li><li>Terrain complexity and base preparation</li><li>Gate automation and intercom. Optional</li><li>Removing the old fence</li></ul></div>
</div></div></section>

<section class="section section--dark svc-hide" id="meist" style="position:relative;overflow:hidden"><div style="position:absolute;inset:0;background:url('/img/luxaed-sunset.webp') center 40%/cover no-repeat;pointer-events:none"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(8,10,16,.95) 0%, rgba(10,12,20,.82) 40%, rgba(12,10,16,.9) 100%);pointer-events:none"></div>
  <div class="wrap" style="position:relative"><span class="tag">About us</span><h2 class="big big--xl">Fences are our craft.</h2>
  <p class="lead lead--lg">LuxAed is a team building fences, gates and pedestrian gates in Tallinn and Harjumaa.<br>We work with all main fence types and provide gate automation and intercoms.<br>Neatly, at a fair price and with a quote before the work begins.</p>
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
    <a href="/img/luxaed-svc-gates.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-svc-gates.webp"><img src="/img/luxaed-svc-gates.jpg" alt="Wooden sliding gate with automation" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-mesh-1.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-mesh-1.webp"><img src="/img/luxaed-w-mesh-1.jpg" alt="3D welded-mesh fence" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-lippaed-1.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-lippaed-1.webp"><img src="/img/luxaed-w-lippaed-1.jpg" alt="Steel picket fence" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-g1.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-g1.webp"><img src="/img/luxaed-g1.jpg" alt="Wooden fence and sliding gate" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-gates-green.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-gates-green.webp"><img src="/img/luxaed-w-gates-green.jpg" alt="Swing gates from panels" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-gates-graphite.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-gates-graphite.webp"><img src="/img/luxaed-w-gates-graphite.jpg" alt="Graphite swing gates" width="600" height="400" loading="lazy"></picture></a>
    <a href="/img/luxaed-w-mesh-2.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/luxaed-w-mesh-2.webp"><img src="/img/luxaed-w-mesh-2.jpg" alt="Green 3D welded-mesh fence" width="600" height="400" loading="lazy"></picture></a>
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
page("/en/","Fence and gate installation in Tallinn and Harju County — LuxAed",f"Fences and gates in Tallinn and Harju County: wood, roll mesh, 2D/3D mesh, steel picket, metal bar and profiled sheet. Free measurement, {RECOMMEND_PERCENT}% recommend on Facebook.", home_inner, sch=lb_schema+video_schema(home_video_items("en"),"en"))

# ---------------- EN ABOUT ----------------
about=f'''<section class="hero hero--compact">
  <div class="hero-photo-bg" style="background:url('/img/luxaed-hero.webp') center 45%/cover no-repeat"></div>
  <div class="wrap"><div class="hero-grid" style="grid-template-columns:1fr;gap:0"><div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">{RECOMMEND_PERCENT}% recommend</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">{REVIEW_COUNT} Facebook reviews</a></div>
    <h1>Who we are</h1>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:16px;max-width:720px">We have been manufacturing and installing fences, gates and pedestrian gates in Tallinn and Harjumaa <b>for over {EXPERIENCE_YEARS} years</b>. We work with wood, roll mesh, welded 2D/3D mesh, steel picket, welded metal-bar sections and profiled sheet, fit gate automation and intercoms, and repair existing structures. Our experience helps us account for different soils, slopes and drainage conditions.</p>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:12px;max-width:720px">We take the whole process off your hands: we come for a free measurement, buy the materials, install and hand over the finished job. We name the price up front. No hidden extras or surprises.</p>
    <p class="lead" style="color:#fff;font-size:16px;line-height:1.55;margin-top:12px;max-width:720px">A new fence around the cottage, a sliding gate with automation, or a full perimeter. We handle it all.</p>
  </div></div>
  <div class="hero-stats"><div class="hstat"><b>{RECOMMEND_PERCENT}%</b><span>Recommend on Facebook</span></div><div class="hstat"><b>{REVIEW_COUNT}</b><span>Reviews</span></div><div class="hstat"><b>{EXPERIENCE_YEARS}+</b><span>Years of experience</span></div></div></div>
</section>
<section class="section"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Master craftsman</span><h2 class="big">Artur Mustafin.<br>Over {EXPERIENCE_YEARS} years of experience building fences and gates.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-w-crew.webp"><img src="/img/luxaed-w-crew.jpg" width="1000" height="1333" alt="LuxAed master installing a fence" loading="lazy"></picture></div>
  <div class="equip-body"><p class="lead" style="margin-bottom:14px">Artur has been building fences and gates in Tallinn and Harjumaa for over {EXPERIENCE_YEARS} years. He helps choose a suitable solution for the plot and avoid unnecessary costs.</p><ul class="svc-bens">
    <li>Over {EXPERIENCE_YEARS} years of experience building fences and gates</li>
    <li>Completed projects across Tallinn and Harjumaa</li>
    <li>Quality control at every stage of the work</li>
  </ul></div>
</div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">Principles</span><h2 class="big">What matters to us</h2>
<div class="svc-cards">
<div class="svc-card"><div class="ic">1</div><h3>Everything with one call</h3><p>Measurement, materials, installation and repair from one place. One call, and it's all arranged.</p></div>
<div class="svc-card"><div class="ic">2</div><h3>We work year-round</h3><p>We install fences in winter too, when the ground and conditions allow. We don't automatically push the work to spring.</p></div>
<div class="svc-card"><div class="ic">3</div><h3>Careful hands</h3><p>We work cleanly, protect your plot and clean up after ourselves. We hand the site over tidy.</p></div>
<div class="svc-card"><div class="ic">4</div><h3>Exact price up front</h3><p>We name the price before we start and stick to it. No hidden extras or surprises on the invoice.</p></div>
</div></div></section>
<section class="section"><div class="wrap"><span class="tag">Why us</span><h2 class="big">Why LuxAed</h2>
<ul class="svc-bens"><li>Over <b>{EXPERIENCE_YEARS} years</b> of experience in Tallinn and Harjumaa</li><li>Wood, roll mesh, welded 2D/3D mesh, steel picket, metal-bar and profiled-sheet fences</li><li>Sliding and swing gates, automation and intercoms</li><li>We handle buying the materials and the whole process</li><li>Free measurement, price up front, 24-month warranty on the work</li><li>We work year-round, including winter</li></ul></div></section>
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
page("/en/about/","About Us: Fence and Gate Installers in Tallinn | LuxAed",f"LuxAed builds and installs fences, gates, automation and intercoms in Tallinn and Harju County. Over {EXPERIENCE_YEARS} years of experience and a free site measurement.", about, sch=[about_page_schema("/en/about/","en","About LuxAed","Fence and gate master Artur Mustafin and the LuxAed story in Tallinn and Harjumaa."),person_artur_schema("en")])

# ---------------- EN FAQ ----------------
faq_inner=f'''{hero("FAQ","Frequently asked questions","We've gathered answers to the questions people most often ask before ordering a fence or gate.", crumb="FAQ")}
<section class="section"><div class="wrap"><span class="tag">FAQ</span><h2 class="big">What people ask before ordering</h2>{faqx(FAQ_PAGE)}</div></section>
<section class="cta-final"><div class="wrap"><h2>Didn't find your answer?</h2><p>Call or write.<br>We'll advise and come for a free measurement.</p>
<div class="hero-btns"><a class="btn btn-accent" href="/en/#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></section>'''
page("/en/faq/","FAQ: fences, gates and automation in Tallinn — LuxAed","Frequently asked questions about fences, gates and automation in Tallinn: price, materials, timing, automation, repair. LuxAed.", faq_inner, og="/img/luxaed-wide-wood.jpg", sch=faq_page_schema)

# ---------------- EN CONTACT ----------------

# ---------------- EN LEGAL ----------------
def legal(path,title,h1,kicker,blocks,desc=None):
    inner=f'''{hero(kicker,h1,"",img="luxaed-g3",crumb=h1)}
<section class="section"><div class="wrap" style="max-width:820px">
{"".join(f"<h2 class='big' style='font-size:24px;margin-top:28px'>{t}</h2><p class='lead' style='margin-top:10px'>{b}</p>" for t,b in blocks)}
<p class="lead" style="margin-top:26px">For questions about this document, write to <a href="mailto:{EMAIL}" style="color:var(--accent)">{EMAIL}</a>.</p></div></section>'''
    page(path,title,desc or h1+": LuxAed, fences and gates in Tallinn and Harju County.",inner,og="/img/luxaed-g3.jpg",sch=[webpage_schema(path,"en",title,h1)])

legal("/en/privacy/","Privacy policy — LuxAed","Privacy policy","Privacy",desc="LuxAed privacy policy: what data we collect through the enquiry form, why we use it and how you can exercise your rights.",blocks=[
 ("Data controller","The controller of personal data is LuxAed, Tallinn, Estonia. For data protection matters, contact us by email at "+EMAIL+" or by phone at "+PHONE+"."),
 ("What data we collect","When you send an enquiry via the web form, by phone, email or Facebook, we may process your name, phone number, email address, site address or area, requested service, message and any attached photos. A form enquiry may also include the first landing page, referrer and advertising campaign parameters so that we can understand which channel generated the enquiry. To maintain security and reliability, the web server may also process technical data such as your IP address, request time, browser type and log entries."),
 ("Purposes and legal bases of processing","We use contact and site details to respond to your enquiry, arrange a site survey, prepare a quotation and provide the service. The legal basis is taking steps before entering into a contract or performing a contract. We may rely on legitimate interests for security, prevention of misuse and administration. We use Google Analytics and Google Ads measurement based on your consent."),
 ("Service providers and data transfers","We do not sell your personal data. To operate the service, data may be processed to the necessary extent by Vercel (website hosting, server logs and technical processing of the web form) and Google services (Gmail for forwarding and storing enquiries; Tag Manager, Analytics and Ads for measurement according to your choice). Providers may use subprocessors. If data is processed outside the European Economic Area, the transfer mechanisms and safeguards described in the provider’s documentation apply, such as the European Commission’s standard contractual clauses where relevant."),
 ("Cookies, Google Analytics and Google Ads","The website stores your choice in the browser’s local storage. We use the advanced implementation of Google Consent Mode: analytics and advertising storage are denied by default and those cookies are not set before consent. Google measurement code may still receive limited cookieless technical signals about page views, events and consent state; contact details entered in the enquiry form are not included in those measurement events. You can allow or deny Analytics and advertising measurement separately; this website does not grant consent for ad personalisation. You can change your choice at any time through the “Cookie settings” link in the footer."),
 ("Cookie and preference lifetimes","The <code>luxaed_consent_v3</code> preference remains in local storage for up to 6 months. With Analytics consent, Google Analytics <code>_ga</code> and <code>_ga_*</code> cookies may by default remain for up to 2 years. With Advertising consent, <code>_gcl_*</code> measurement cookies may remain for up to 90 days. A browser or our Google configuration may shorten these periods."),
 ("Retention and security","We retain enquiry data for as long as necessary to handle the enquiry, prepare the quotation and perform any resulting contract, resolve claims or comply with a legal obligation. Once the data is no longer needed, it is deleted or anonymised. We restrict access to data and use reasonable technical and organisational security measures."),
 ("Your rights","You have the right to request access to your personal data, require its rectification or erasure, restrict processing, object to processing based on legitimate interests and withdraw consent at any time. Where processing is based on consent or a contract and the applicable conditions are met, you may request data portability. To submit a request, write to "+EMAIL+". You also have the right to lodge a complaint with the Estonian Data Protection Inspectorate (Andmekaitse Inspektsioon)."),
 ("Policy updates","We may update this privacy policy if our services or legal requirements change. The current version is published on this page. Last updated: 28.07.2026."),
])
legal("/en/terms/","Terms of service — LuxAed","Terms of service","Terms",desc="LuxAed terms of service: how enquiries, quotations and work are agreed. Fences and gates in Tallinn and Harju County.",blocks=[
 ("General","These terms describe how LuxAed provides services for manufacturing, installing and repairing fences, gates and automation in Tallinn and Harjumaa."),
 ("Request and quote","You can leave a request by phone, email or the form on the website. The price is determined after a free measurement and agreed before work begins."),
 ("Measurement and agreements","The exact price, materials and timing are agreed in a written quotation after the site measurement. All key terms are agreed with the customer in advance."),
 ("Payment","Payment terms and method are agreed individually before work begins. Nothing is added to the agreed price without your consent."),
 ("Warranty and quality","We give a 24-month warranty on installing new fences, gates and automation and on repair work. Materials and equipment also carry the manufacturer's warranty, which may be longer. The warranty does not cover mechanical damage (for example a vehicle impact or a storm), faults caused by lack of maintenance or changes made by others, and it does not reduce your statutory rights."),
 ("Liability","LuxAed is not liable for damage caused by hidden utilities on the site that the customer did not disclose, nor for force majeure."),
 ("Contact","For any questions about the services and terms, contact us at "+PHONE+" or "+EMAIL+"."),
])
print("EN home + support done")
