#!/usr/bin/env python3
# English tree: /en/ service pages. Mirrors gen_et structure.
import json, html
from build_pages import head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN, SVC

def form_html():
    chips=[("fence","Fence"),("gate","Gate"),("automation","Automation"),("repair","Repair")]
    ov='<svg class="chip-oval" viewBox="0 0 220 64" preserveAspectRatio="none" aria-hidden="true"><path d="M40 16C92 5 158 6 196 18 215 24 210 49 172 56 110 66 48 64 20 50 7 43 12 17 50 11 78 7 104 9 126 13"/></svg>'
    ch="".join(f'<button type="button" class="chip" data-svc="{s}">{ov}{t}<span class="chip-tick" aria-hidden="true">✓</span></button>' for s,t in chips)
    return f'''<div class="form-slot"><div class="form-card" id="form">
  <span class="form-tag">Get a quote</span>
  <h2>What do you need? <span class="pick-hint">(choose)</span></h2>
  <form id="leadForm">
    <input type="hidden" name="service" id="serviceField">
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:0;top:0;width:1px;height:1px;opacity:0;overflow:hidden">
    <div class="chips" id="svcChips" role="radiogroup">{ch}</div>
    <div class="ff" data-svc="fence"><select name="material" class="form-select"><option value="">Fence material</option><option>Wood</option><option>Corrugated sheet</option><option>Mesh (3D welded)</option><option>Not sure — advise me</option></select></div>
    <div class="ff form-grid2" data-svc="fence"><input type="text" name="length" inputmode="numeric" placeholder="Length, m"><select name="height" class="form-select"><option value="">Height</option><option>up to 1.5 m</option><option>1.5–2 m</option><option>over 2 m</option></select></div>
    <div class="ff" data-svc="gate,automation"><select name="gate_type" class="form-select"><option value="">Gate type</option><option>Sliding</option><option>Swing</option><option>Not sure</option></select></div>
    <div class="ff" data-svc="gate"><select name="automation" class="form-select"><option value="">Automation?</option><option>With automation</option><option>Without automation</option><option>Not sure</option></select></div>
    <div class="ff form-grid2"><select name="plot" class="form-select"><option value="">Site</option><option>Flat</option><option>Sloped</option><option>Old fence (removal)</option><option>Not sure</option></select><select name="timeline" class="form-select"><option value="">When?</option><option>As soon as possible</option><option>Within 1–3 months</option><option>Just a price</option></select></div>
    <div class="ff-base"><input type="text" name="address" placeholder="Site address (city / district)"></div>
    <div class="form-grid">
      <input type="text" name="name" placeholder="Your name *" required style="grid-column:1/-1">
      <input type="tel" name="phone" placeholder="Phone *" required>
      <input type="email" name="email" placeholder="Email *" required>
    </div>
    <div class="ff"><textarea name="msg" placeholder="Comment: details, wishes, what to repair..."></textarea></div>
    <label class="photo-upload ff" id="photoLabel"><input type="file" name="photos" accept="image/*" multiple id="photoInput" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);border:0"><svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg><span id="photoLabel-txt">Attach a photo (optional)</span></label>
    <button class="btn btn-accent" type="submit" style="width:100%;padding:13px;font-size:15px">Send request →</button>
    <p class="form-consent">By submitting you agree to our <a href="/en/privacy/">privacy policy</a> and <a href="/en/terms/">terms</a></p>
    <div class="form-ok" id="formOk" role="status"><b>Thank you! Request received.</b><br>We'll get back to you shortly.</div>
  </form>
</div></div>'''

PROCESS='''<div class="hsteps">
  <div class="hstep"><div class="hstep-num">1</div><h3>You send a request</h3><p>One call or message — and we take the fence off your hands. We come for a free measurement at a time that suits you.</p></div>
  <div class="hstep"><div class="hstep-num">2</div><h3>We advise & quote</h3><p>We suggest the material and solution for your plot and budget and give an honest price — no surprises on the invoice.</p></div>
  <div class="hstep"><div class="hstep-num">3</div><h3>We install with care</h3><p>We set the posts, sections, gates and automation. We keep you posted at every stage.</p></div>
  <div class="hstep"><div class="hstep-num">4</div><h3>We hand it over</h3><p>We check every detail together with you and hand over the finished fence. After that — you simply enjoy it.</p></div>
</div>'''

def bens(items): return '<ul class="svc-bens">'+"".join(f"<li>{x}</li>" for x in items)+'</ul>'
def cards(cc): return '<div class="svc-cards">'+"".join(f'<div class="svc-card"><div class="ic">{i}</div><h4>{n}</h4><p>{d}</p></div>' for i,n,d in cc)+'</div>'
def gal(imgs): return '<div class="gal" id="gal">'+"".join(f'<a href="/img/{i}.jpg" data-lb="1"><picture><source type="image/webp" srcset="/img/{i}.webp"><img src="/img/{i}.jpg" alt="{html.escape(a)}" loading="lazy"></picture></a>' for i,a in imgs)+'</div>'
def faqx(fq): return '<div class="faq" id="faqList">'+"".join(f'<div class="faq-item"><button class="faq-q">{q}</button><div class="faq-a"><p>{a}</p></div></div>' for q,a in fq)+'</div>'
def related(cur):
    cc=[(p,t) for p,t in SVC["en"] if p!=cur][:3]
    return '<div class="svc-cards">'+"".join(f'<a class="svc-card" href="{p}" style="text-decoration:none"><div class="ic">→</div><h4>{t}</h4><p>Learn more →</p></a>' for p,t in cc)+'</div>'

def schema(name,desc,path,fq):
    j=lambda o:'<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False)+'</script>'
    return [j({"@context":"https://schema.org","@type":"Service","serviceType":name,"description":desc,"url":DOMAIN+path,
              "provider":{"@type":"HomeAndConstructionBusiness","name":"LuxAed","telephone":PHONE,"email":EMAIL,"url":DOMAIN+"/en/"},
              "areaServed":["Tallinn","Harjumaa"]}),
            j({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
              {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/en/"},
              {"@type":"ListItem","position":2,"name":name,"item":DOMAIN+path}]}),
            j({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in fq]})]

def service(c):
    H=head("en",c["path"],c["title"],c["desc"],og_img=c.get("og","/img/luxaed-hero.jpg"),schema_blocks=schema(c["name"],c["desc"],c["path"],c["faq"]))
    body=f'''{nav("en",c["path"])}
<main id="main">
<section class="svc-hero">
  <div class="hero-photo-bg" style="background:url('/img/{c["hero"]}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap"><div class="hero-grid"><div>
    <div class="crumb"><a href="/en/">Home</a><span>›</span>{c["name"]}</div>
    <span class="tag">{c["kicker"]}</span><h1>{c["h1"]}</h1><p class="lead">{c["lead"]}</p>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><span class="ht-label">34 reviews on Facebook · recommend</span></div>
    <div class="hero-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>{form_html()}</div></div>
</section>
<section class="section"><div class="wrap"><span class="tag">What you get</span><h2 class="big">{c["intro_h"]}</h2><p class="lead">{c["intro_p"]}</p>{bens(c["bens"])}</div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">Options</span><h2 class="big">{c["variants_h"]}</h2>{cards(c["variants"])}
  <div class="svc-cta"><b>{c["cta_band"]}</b><a class="btn" href="#form">Get a quote →</a></div></div></section>
<section class="section"><div class="wrap"><span class="tag">Honest about pricing</span><h2 class="big">What affects the price</h2>
  <p class="lead">There is no fixed price list — we quote after a free on-site measurement. Here's what's always included and what affects the total.</p>
  <div class="honest"><div class="hon good"><h3>Always included</h3><ul>{"".join(f"<li>{x}</li>" for x in c["incl"])}<li>We work year-round, including winter</li><li>Warranty on completed work</li></ul></div>
  <div class="hon bad"><h3>Affects the price</h3><ul>{"".join(f"<li>{x}</li>" for x in c["factors"])}</ul></div></div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">How we work</span><h2 class="big">Four steps to a finished result</h2>{PROCESS}</div></section>
<section class="section"><div class="wrap"><span class="tag">Gallery</span><h2 class="big">Examples of our work</h2>{gal(c["gallery"])}</div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">FAQ</span><h2 class="big">Frequently asked questions</h2>{faqx(c["faq"])}</div></section>
<section class="section"><div class="wrap"><span class="tag">Other services</span><h2 class="big">See also</h2>{related(c["path"])}</div></section>
<section class="cta-final"><div class="wrap"><h2>Shall we discuss <em>{c["name"].lower()}</em> for your property?</h2>
  <p>Leave a request or call — we'll come for a free measurement and give you an exact price.</p>
  <div class="hero-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></section>
</main>
<div class="lb" id="lb"><button class="lb-x" aria-label="Close">&times;</button><img src="" alt="" id="lbImg"></div>
{footer("en")}
<div class="mob-bar"><a href="tel:{TEL}" class="btn btn-ghost">Call</a><a href="#form" class="btn btn-accent">Quote</a></div>
{SCRIPTS}
</body></html>'''
    print("wrote", write(c["path"],H+"\n"+body))

ENSERV=[
{"path":"/en/services/mesh-fence/","name":"Mesh & 3D fences","hero":"luxaed-svc-mesh","og":"/img/luxaed-svc-mesh.jpg",
 "title":"Mesh & 3D welded-panel fences in Tallinn — LuxAed","desc":"Installation of mesh and 3D welded-panel fences in Tallinn and Harjumaa. Galvanised + powder-coated, anthracite RAL 7016, posts and turnkey mounting. Free measurement.",
 "kicker":"3D mesh · welded panels","h1":"Mesh & 3D fences in Tallinn",
 "lead":"Modern welded 3D panels with stiffening ribs: strong, tidy and with good visibility of the plot. Galvanised plus powder-coated — lasts for decades.",
 "intro_h":"Why a 3D fence","intro_p":"A welded panel with bends (3D) holds its shape without sagging or wind load and looks modern. A great fit for houses, townhouses and grounds.",
 "bens":["Strong welded panels with stiffening ribs","Galvanised + powder-coated — no rust","Anthracite RAL 7016 and other colours","Good visibility, minimal wind load","Fast mounting on posts","2D and 3D panels available"],
 "variants_h":"Types of mesh fence",
 "variants":[("3D","3D panels","Welded panel with V-shaped stiffening ribs — the most popular and durable option."),
             ("2D","2D double-wire","Double horizontal wire — a reinforced flat panel for long spans."),
             ("◧","RAL colours","Anthracite RAL 7016, green RAL 6005, black and other coating colours."),
             ("▤","Posts & fixings","Galvanised posts with caps, brackets and panel clips.")],
 "cta_band":"Let's price a mesh fence for your plot","incl":["On-site measurement","Installation of galvanised posts","Mounting of welded panels and fixings","Levelling to the terrain","Post-installation check"],
 "factors":["Fence length and panel height (1.23–2.03 m)","Panel type (2D/3D) and colour","Terrain and groundwork","Number of gates and wickets","Removal of the old fence"],
 "gallery":[("luxaed-svc-mesh","Welded 3D mesh fence"),("luxaed-mesh-2","Mesh fence along the plot"),("luxaed-mesh-3","Mesh fence with green posts"),("luxaed-mesh-gate","Mesh gates by LuxAed")],
 "faq":[("How long does a 3D fence last?","When galvanised and powder-coated, welded panels last for decades and don't rust."),
        ("What heights are available?","Usually 1.23–2.03 m. We pick the height for your goal — privacy or marking the boundary."),
        ("Which colour should I choose?","The most popular are anthracite RAL 7016 and green RAL 6005. Other coating colours are available."),
        ("Can I get a matching gate?","Yes, we make sliding and swing gates filled with welded panel in the same colour.")]},
{"path":"/en/services/wooden-fence/","name":"Wooden fences","hero":"luxaed-svc-wood","og":"/img/luxaed-svc-wood.jpg",
 "title":"Wooden fences and gates in Tallinn — LuxAed","desc":"Manufacture and installation of wooden fences and gates in Tallinn and Harjumaa. Horizontal fence, steel frame, timber treatment. Free measurement and quote.",
 "kicker":"Wood · steel frame","h1":"Wooden fences in Tallinn",
 "lead":"A warm, tidy look for your plot. We build fences and gates from treated timber on a sturdy steel frame — natural wood combined with reliable metal.",
 "intro_h":"Why a wooden fence","intro_p":"Wood looks premium and natural and fits any plot. On a steel frame the structure doesn't sag and lasts a long time.",
 "bens":["Treated timber for the Estonian climate","Sturdy steel frame — no sagging","Horizontal, vertical or louvre","Fence and gates in one style","Gate automation available","Custom design for your plot"],
 "variants_h":"Types of wooden fence",
 "variants":[("▤","Horizontal","Horizontal boards on a steel frame — the popular modern look."),
             ("▥","Picket","Classic vertical picket, with or without a gap."),
             ("◫","Louvre (ranch)","Angled slats — privacy with airflow."),
             ("⛩","Wooden gates","Sliding and swing gates with timber infill and automation.")],
 "cta_band":"Let's pick a wooden fence for your home","incl":["On-site measurement","Making the sections and steel frame","Installing posts and mounting sections","Timber treatment and coating","Post-installation check"],
 "factors":["Fence length and height","Type (horizontal, picket, louvre)","Timber species and treatment","Gates and automation","Terrain and groundwork"],
 "gallery":[("luxaed-svc-wood","Wooden fence on a steel frame"),("luxaed-g1","Wooden fence and sliding gate"),("luxaed-wood-2","Wooden fence on a plot"),("luxaed-wood-3","Wooden fence and gate")],
 "faq":[("Won't the wood rot?","We use treated timber and coating, and the frame is steel. With proper care the fence lasts for many years."),
        ("Can I have horizontal boards?","Yes, a horizontal fence on a steel frame is one of the most popular options."),
        ("Will you make a matching gate?","Yes, we make sliding and swing gates with timber infill in the same design."),
        ("Does a wooden fence need maintenance?","We recommend refreshing the protective coating periodically — we'll explain how to care for it.")]},
{"path":"/en/services/metal-fence/","name":"Corrugated (metal) fences","hero":"luxaed-svc-profnastil","og":"/img/luxaed-svc-profnastil.jpg",
 "title":"Corrugated (profiled sheet) fences in Tallinn — LuxAed","desc":"Installation of corrugated / profiled-sheet metal fences in Tallinn and Harjumaa. Galvanised sheet, various colours, solid fence for privacy. Affordable and fast. Free measurement.",
 "kicker":"Corrugated · profiled sheet","h1":"Corrugated metal fences in Tallinn",
 "lead":"A practical and affordable solution: a solid fence from galvanised profiled sheet. Full privacy, protection from wind and dust, and various coating colours.",
 "intro_h":"Why profiled sheet","intro_p":"Profiled sheet is inexpensive and quick to install. A solid fence closes off the plot and lasts thanks to galvanising and a polymer coating.",
 "bens":["Full privacy — a solid fence","Galvanised sheet with polymer coating","Various colours (incl. wood-look)","Protection from wind, dust and noise","Economical and fast","Steel posts and rails"],
 "variants_h":"Corrugated fence options",
 "variants":[("▦","Standard sheet","A solid fence from galvanised profiled sheet at the required height."),
             ("◧","Coloured coating","Polymer coating in different colours, including wood-look."),
             ("▣","With brick posts","Profiled sheet combined with brick or block posts."),
             ("⛩","Sheet gates","Sliding and swing gates filled with profiled sheet.")],
 "cta_band":"Let's price a corrugated fence","incl":["On-site measurement","Installing steel posts and rails","Mounting the profiled sheet","Levelling","Post-installation check"],
 "factors":["Fence length and height","Sheet grade and colour","Post type (metal, brick)","Gates and wickets","Terrain and groundwork"],
 "gallery":[("luxaed-svc-profnastil","Corrugated sheet gate"),("luxaed-metal","Metal fence with gates"),("luxaed-profnastil-2","Corrugated metal fence (type example)")],
 "faq":[("Won't the sheet fade?","Quality sheet with a polymer coating keeps its colour for a long time. We use proven materials."),
        ("What height is possible?","Usually 1.5–2.0 m and higher — we pick it for privacy and wind load."),
        ("Can it be combined with brick posts?","Yes, we build combined fences: sheet between brick or block posts."),
        ("Is profiled sheet cheaper than wood and mesh?","Usually yes — it's one of the most affordable options. We'll give an exact price after the measurement.")]},
{"path":"/en/services/gates-automation/","name":"Gates & automation","hero":"luxaed-svc-gates","og":"/img/luxaed-svc-gates.jpg",
 "title":"Gates, wickets & automation in Tallinn — LuxAed","desc":"Sliding and swing gates, wickets, gate automation and intercoms in Tallinn and Harjumaa. Turnkey installation of drives, remotes and intercoms. Free measurement.",
 "kicker":"Gates · automation · intercoms","h1":"Gates & automation in Tallinn",
 "lead":"Turnkey sliding and swing gates with automation and intercoms. We manufacture, install and connect everything — you drive into your yard at the press of a button.",
 "intro_h":"Turnkey gates with automation","intro_p":"We choose the gate type and drive for your entrance, width and terrain. We install automation, remotes, photocells and intercoms, and service existing systems too.",
 "bens":["Sliding (cantilever) gates","Swing gates","Automation: drives, remotes, photocells","Intercoms and call panels","Wickets matching the fence","Servicing and repair of existing gates"],
 "variants_h":"Gate and automation types",
 "variants":[("⇄","Sliding gate","A cantilever gate with no bottom track — convenient and takes no space when opening."),
             ("⛩","Swing gate","A classic two-leaf gate with a drive on each leaf."),
             ("⚙","Automation","Drives, remote controls, safety photocells, warning light."),
             ("🔔","Intercom","Call panels and intercoms that open the gate and wicket.")],
 "cta_band":"Let's pick gates and automation for your entrance","incl":["Measurement of the entrance","Making the gate and wicket","Installation and levelling","Automation mounting and setup","Intercom connection, function check"],
 "factors":["Gate type (sliding / swing)","Leaf width and weight","Automation drive brand","Intercom and extra options","Infill (wood, sheet, mesh panel)"],
 "gallery":[("luxaed-svc-gates","Wooden sliding gate with automation"),("luxaed-profnastil-gate","Swing gates from profiled sheet"),("luxaed-mesh-gate","Mesh gates"),("luxaed-auto-2","Sliding gate drive")],
 "faq":[("Sliding or swing — which to choose?","Sliding is handy when there's little space in front of the entrance. Swing is simpler and cheaper. We'll help you choose at the measurement."),
        ("Can automation be fitted to existing gates?","In most cases yes — we assess the structure and pick a suitable drive."),
        ("Do you install intercoms?","Yes, we install and connect intercoms and call panels that open the gate and wicket."),
        ("What about automation safety?","We fit photocells and a warning light so the gate won't close on a car or a person.")]},
{"path":"/en/services/fence-repair/","name":"Fence & gate repair","hero":"luxaed-g6","og":"/img/luxaed-g6.jpg",
 "title":"Fence & gate repair in Tallinn — LuxAed","desc":"Repair of fences and gates in Tallinn and Harjumaa: replacing sections and posts, repairing sliding and swing gates, automation and hardware. Diagnostics and quote.",
 "kicker":"Repair · maintenance","h1":"Fence & gate repair in Tallinn",
 "lead":"We restore fences, gates and automation: replacing sections and posts, adjusting leaves, repairing drives and hardware. We run diagnostics and give you a price.",
 "intro_h":"What we repair","intro_p":"You don't always need a whole new fence — often it's enough to replace damaged sections or posts, adjust the gates or restore the automation.",
 "bens":["Replacing damaged fence sections","Replacing and levelling posts","Repairing sliding and swing gates","Automation repair and setup","Replacing rollers, tracks and hardware","Diagnostics and a price before work"],
 "variants_h":"Types of repair work",
 "variants":[("▤","Fence sections","Replacing damaged panels, boards or sheet."),
             ("▥","Posts","Replacing, levelling and reinforcing leaning posts."),
             ("⇄","Gates","Adjusting leaves, replacing rollers and tracks."),
             ("⚙","Automation","Diagnostics and repair of drives, remotes and photocells.")],
 "cta_band":"We'll run diagnostics and fix your fence","incl":["Visit and diagnostics","A price before work starts","Replacing sections, posts or hardware","Adjusting gates and automation","Function check after the repair"],
 "factors":["Extent and type of damage","Fence and gate type","Need to replace materials","Automation repair","Access to the site"],
 "gallery":[("luxaed-g6","Gate drive and post"),("luxaed-g9","Sliding gate automation"),("luxaed-auto-2","Gate drive repair"),("luxaed-g8","Gate automation close-up")],
 "faq":[("Can it be repaired instead of replacing the whole fence?","Often yes — we replace only the damaged sections or posts. At the diagnostics we assess what's more cost-effective."),
        ("Do you repair gate automation?","Yes, we diagnose and repair drives, remotes and photocells, replacing them if needed."),
        ("Do you repair gates you didn't install?","Yes, we work with other builders' structures too — we assess on site."),
        ("How much does repair cost?","It depends on the scope. After diagnostics we give an exact price with no hidden fees.")]},
]

for c in ENSERV: service(c)
print("EN services done:", len(ENSERV))
