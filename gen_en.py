#!/usr/bin/env python3
# English tree: /en/ service pages. Mirrors gen_et structure.
import json, html
from build_pages import head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN, SVC, reel_strip

def form_html():
    chips=[("fence","Fence"),("gate","Gate"),("automation","Automation"),("repair","Repair")]
    ov='<svg class="chip-oval" viewBox="0 0 220 64" preserveAspectRatio="none" aria-hidden="true"><path d="M40 16C92 5 158 6 196 18 215 24 210 49 172 56 110 66 48 64 20 50 7 43 12 17 50 11 78 7 104 9 126 13"/></svg>'
    ch="".join(f'<button type="button" class="chip" data-svc="{s}">{ov}{t}<span class="chip-tick" aria-hidden="true">✓</span></button>' for s,t in chips)
    return f'''<div class="form-slot"><div class="form-card" id="form">
  <span class="form-tag">Get a quote</span>
  <h2>What do you need? <span class="pick-hint">(choose)</span></h2>
  <p class="form-sub">Fill only the main fields. We'll clarify the rest at the measurement.</p>
  <form id="leadForm">
    <input type="hidden" name="service" id="serviceField">
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:0;top:0;width:1px;height:1px;opacity:0;overflow:hidden">
    <div class="chips" id="svcChips" role="group">{ch}</div>
    <div class="ff" data-svc="fence"><select name="material" class="form-select" aria-label="Fence material"><option value="">Fence material</option><option>Wood</option><option>Corrugated sheet</option><option>Mesh (3D welded)</option><option>Not sure, advise me</option></select></div>
    <div class="ff form-grid2" data-svc="fence"><input type="text" name="length" inputmode="numeric" placeholder="Length, m"><select name="height" class="form-select" aria-label="Height"><option value="">Height</option><option>up to 1.5 m</option><option>1.5–2 m</option><option>over 2 m</option></select></div>
    <div class="ff" data-svc="gate,automation"><select name="gate_type" class="form-select" aria-label="Gate type"><option value="">Gate type</option><option>Sliding</option><option>Swing</option><option>Not sure</option></select></div>
    <div class="ff" data-svc="gate"><select name="automation" class="form-select" aria-label="Automation?"><option value="">Automation?</option><option>With automation</option><option>Without automation</option><option>Not sure</option></select></div>
    <div class="ff form-grid2"><select name="plot" class="form-select" aria-label="Site"><option value="">Site</option><option>Flat</option><option>Sloped</option><option>Old fence (removal)</option><option>Not sure</option></select><select name="timeline" class="form-select" aria-label="When?"><option value="">When?</option><option>As soon as possible</option><option>Within 1–3 months</option><option>Just a price</option></select></div>
    <div class="ff-base"><input type="text" name="address" placeholder="Site address (city / district)"></div>
    <div class="form-grid">
      <input type="text" name="name" placeholder="Your name *" required style="grid-column:1/-1">
      <input type="tel" name="phone" placeholder="Phone *" required>
      <input type="email" name="email" placeholder="Email *" required>
    </div>
    <div class="ff"><textarea name="msg" placeholder="Comment: details, wishes, what to repair..."></textarea></div>
    <label class="photo-upload ff" id="photoLabel"><input type="file" name="photos" accept="image/*" multiple id="photoInput" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);border:0"><svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg><span id="photoLabel-txt">Attach a photo (optional)</span></label>
    <button class="btn btn-accent" type="submit" style="width:100%;padding:13px;font-size:15px">Send request →</button>
    <div class="form-assure"><span>Work guarantee</span><span>Reply within 30 minutes</span></div>
    <p class="form-consent">By submitting you agree to our <a href="/en/privacy/">privacy policy</a> and <a href="/en/terms/">terms</a></p>
    <div class="form-ok" id="formOk" role="status"><b>Thank you, request received.</b><br>We'll get back to you shortly.</div>
  </form>
</div></div>'''

PROCESS='''<div class="hsteps">
  <div class="hstep"><div class="hstep-num">1</div><h3>You send a request</h3><p>One call or message. And we take the whole job off your hands. We come for a free measurement at a time that suits you.</p></div>
  <div class="hstep"><div class="hstep-num">2</div><h3>We advise & quote</h3><p>We suggest the material and solution for your plot and budget and give an exact price. No surprises on the invoice.</p></div>
  <div class="hstep"><div class="hstep-num">3</div><h3>We install with care</h3><p>We set the posts, sections, gates and automation. We keep you posted at every stage.</p></div>
  <div class="hstep"><div class="hstep-num">4</div><h3>We hand it over</h3><p>When the work is done we review the result together with you and hand over the finished job. With care and maintenance tips.</p></div>
</div>'''

VARUSTUS='''<section class="section"><div class="wrap"><div class="equip">
  <div class="equip-head"><span class="tag">Equipment</span><h2 class="big">The right kit, an experienced crew, a tidy result.</h2></div>
  <div class="equip-img"><picture><source type="image/webp" srcset="/img/luxaed-w-van.webp"><img src="/img/luxaed-w-van.jpg" width="750" height="563" alt="LuxAed van on site" loading="lazy"></picture></div>
  <div class="equip-body"><ul class="spec">
    <li><b>Post auger and rammer</b>: posts go in firm and level</li>
    <li><b>Welding and cutting on site</b>: steel frames and gate frames</li>
    <li><b>Levelling and measuring</b>: sections in one line, even on a slope</li>
    <li><b>Automation and intercoms</b>: set up and connected turnkey</li>
    <li><b>Clean site</b>: we clean up after ourselves and hand the plot over tidy</li>
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
    cc=[(p,t) for p,t in SVC["en"] if p!=cur][:3]
    return '<div class="svc-cards">'+"".join(f'<a class="svc-card" href="{p}" style="text-decoration:none"><div class="ic">→</div><h3>{t}</h3><p>Learn more →</p></a>' for p,t in cc)+'</div>'

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
    blocks=schema(c["name"],c["desc"],c["path"],c["faq"])
    _tl=(c.get("types",[]) or [])+(c.get("autotypes",[]) or [])
    if _tl:
        _items=[{"@type":"ListItem","position":i+1,"name":x[4],"description":x[5],"image":DOMAIN+"/img/"+x[0]+".jpg"} for i,x in enumerate(_tl)]
        blocks=blocks+['<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"ItemList","name":c.get("types_h",c["name"]),"itemListElement":_items},ensure_ascii=False)+'</script>']
    H=head("en",c["path"],c["title"],c["desc"],og_img=c.get("og",f'/img/{c["hero"]}.jpg'),schema_blocks=blocks)
    cta_band=f'<div class="svc-cta"><b>{c["cta_band"]}</b><a class="btn" href="#form">Get a quote →</a></div>'
    _tcta=cta_band if (c.get("types") and not c.get("autotypes") and not c.get("variants")) else ''
    types_sec=f'<section class="section"><div class="wrap"><span class="tag">{c["types_tag"]}</span><h2 class="big">{c["types_h"]}</h2>{gtypes(c["types"])}{_tcta}</div></section>\n' if c.get("types") else ''
    auto_sec=f'<section class="section section--alt"><div class="wrap"><span class="tag">{c.get("autotypes_tag","")}</span><h2 class="big">{c.get("autotypes_h","")}</h2>{gtypes(c["autotypes"])}{cta_band}</div></section>\n' if c.get("autotypes") else ''
    variants_sec=f'<section class="section section--alt"><div class="wrap"><span class="tag">Options</span><h2 class="big">{c["variants_h"]}</h2>{cards(c["variants"])}{cta_band}</div></section>\n' if c.get("variants") else ''
    body=f'''{nav("en",c["path"])}
<main id="main">
<section class="hero">
  <div class="hero-photo-bg" style="background:url('/img/{c["hero"]}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap"><div class="hero-grid"><div>
    <div class="hero-kicker hand">Hey! Need a new fence?</div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">34 reviews on Facebook · recommend</a></div>
    <h1>{c["h1"]}</h1>
    <div class="hero-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>{form_html()}</div>
  <div class="hero-stats"><div class="hstat"><b>100%</b><span>recommend on Facebook</span></div><div class="hstat"><b>34</b><span>reviews</span></div><div class="hstat"><b>15</b><span>years of craft experience</span></div></div></div>
</section>
<section class="section"><div class="wrap"><span class="tag">What you get</span><h2 class="big">{c["intro_h"]}</h2><p class="lead">{c["intro_p"]}</p>{bens(c["bens"])}</div></section>
{types_sec}{auto_sec}{variants_sec}
<section class="section"><div class="wrap"><span class="tag">Honest about pricing</span><h2 class="big">What affects the price</h2>
  <p class="lead">There is no fixed price list. We quote after a free on-site measurement. Here's what's always included and what affects the total.</p>
  <div class="honest"><div class="hon good"><h3>Always included</h3><ul>{"".join(f"<li>{x}</li>" for x in c["incl"])}<li>We work year-round, including winter</li><li>Warranty on completed work</li></ul></div>
  <div class="hon bad"><h3>Affects the price</h3><ul>{"".join(f"<li>{x}</li>" for x in c["factors"])}</ul></div></div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">How we work</span><h2 class="big">Four simple steps</h2>{PROCESS}</div></section>

<section class="section"><div class="wrap"><span class="tag">Gallery</span><h2 class="big">Examples of our work</h2>{gal(c["gallery"])}<div style="text-align:center;margin-top:30px"><a class="gal-fb" href="{FB}/photos_by" target="_blank" rel="noopener">More photos on our Facebook →</a></div></div></section>
<section class="section section--alt"><div class="wrap"><span class="tag">FAQ</span><h2 class="big">Frequently asked questions</h2>{faqx(c["faq"])}</div></section>
<section class="section"><div class="wrap"><span class="tag">Other services</span><h2 class="big">See also</h2>{related(c["path"])}</div></section>
<section class="cta-final"><div class="wrap"><h2>We'll build your <em>dream fence</em></h2>
  <p>Leave a request or call.<br>We'll come for a free measurement and give you an exact price.</p>
  <div class="hero-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></section>
</main>
<div class="lb" id="lb"><button class="lb-x" aria-label="Close">&times;</button><img src="" alt="" id="lbImg"></div>
{footer("en")}
<div class="mob-bar"><a class="btn btn-accent mob-call" href="tel:{TEL}"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="vertical-align:-3px;margin-right:6px"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>Call</a></div>
{SCRIPTS}
</body></html>'''
    print("wrote", write(c["path"],H+"\n"+body))

ENSERV=[
{"path":"/en/services/mesh-fence/","video":("luxaed-reel-vorkaed","3D welded-panel fence — finished project"),"name":"Mesh & 3D fences","hero":"luxaed-w-mesh-1","og":"/img/luxaed-w-mesh-1.jpg",
 "title":"Mesh & 3D fence installation in Tallinn — LuxAed","desc":"Mesh and 3D welded-panel fences in Tallinn and Harjumaa. Fence posts, dog runs, anthracite RAL 7016. Turnkey install. Free measurement.",
 "kicker":"3D mesh · panels · posts","h1":"<em>Mesh &amp; 3D fence</em><br>installation",
 "lead":"Modern welded 3D panels with stiffening ribs: strong, tidy and with good visibility of the plot. Galvanised plus powder-coated. Lasts for decades.",
 "intro_h":"Why a 3D fence","intro_p":"A welded panel with bends (3D) holds its shape without sagging and stands up to wind and looks modern. A great fit for houses, townhouses and grounds. We also install fence posts and build dog runs. We choose and source the material for you.",
 "bens":["Strong welded panels with stiffening ribs","Galvanised + powder-coated. No rust","Anthracite RAL 7016 and other colours","2D and 3D panels, welded mesh","Galvanised fence posts, caps and clips","Dog runs and animal enclosures from panels"],
 "types_tag":"2D and 3D","types_h":"2D and 3D panel fence",
 "types":[("luxaed-w-mesh-1","Anthracite 3D panel fence by a hedge","3D","Panel","3D welded panel","A welded panel with V-shaped stiffening ribs. They give strength and a modern three-dimensional look. The strongest and most popular choice, and it won't sag or bend in the wind.",["V-shaped ribs","Strongest","Anthracite RAL 7016"]),
          ("luxaed-mesh-2","2D welded panel fence by a plot","2D","Panel","2D welded panel","A flat panel with a double horizontal wire, two wires per row. Durable and cheaper than 3D. A good choice for long runs.",["Double wire","Cheaper than 3D","For long runs"])],
 "variants_h":"Beyond panel fences",
 "variants":[("▤","Fence posts","Galvanised fence posts with caps, brackets and clips. We install and source the material."),
             ("⌗","Dog runs","Dog runs and animal enclosures from welded panels. Strong and safe."),
             ("◧","RAL colours","Anthracite RAL 7016, green RAL 6005, black and other coating colours.")],
 "cta_band":"Let's price a mesh fence for your plot","incl":["On-site measurement","Installation of galvanised posts","Mounting of welded panels and fixings","Levelling to the terrain","Post-installation check"],
 "factors":["Fence length and panel height (1.23–2.03 m)","Panel type (2D/3D) and colour","Number and type of fence posts","Gates, pedestrian gates and dog runs","Terrain and removal of the old fence"],
 "gallery":[("luxaed-w-mesh-1","Anthracite 3D panel fence"),("luxaed-w-mesh-2","Green 3D welded-panel fence"),("luxaed-w-mesh-gate","Wicket from welded panel"),("luxaed-w-gates-green","Swing gates from panels"),("luxaed-w-mesh-detail","Panel fixing on the post"),("luxaed-w-panels","2D panels before installation"),("luxaed-w-gates-auto","Sliding gate with automation"),("luxaed-w-gates-night","Panel gates in the evening"),("luxaed-mesh-2","Mesh fence along the plot"),("luxaed-w-van","LuxAed crew on site")],
 "faq":[("Chain-link mesh or welded panels. Which to choose?","Rolled chain-link is cheaper, but it stretches and sags over time. We recommend a welded 3D panel: the same visibility, but rigid and neat. It lasts far longer. We'll price both and help you decide."),
        ("How long does a 3D fence last?","When galvanised and powder-coated, welded panels last for decades and don't rust."),
        ("What heights are available?","Usually 1.23–2.03 m. We pick the height for your goal. Privacy or marking the boundary."),
        ("Which colour should I choose?","The most popular are anthracite RAL 7016 and green RAL 6005. Other coating colours are available."),
        ("Do you install fence posts too?","Yes, we install galvanised fence posts with caps and clips, and source the material ourselves. For panel fences and other fence types."),
        ("Do you build dog runs?","Yes, we build dog runs and animal enclosures from welded panels. Strong, safe and long-lasting."),
        ("Can I get a matching gate?","Yes, we make sliding and swing gates filled with welded panel in the same colour.")]},
{"path":"/en/services/wooden-fence/","video":("luxaed-video-puitvarav","Wooden sliding gate with automation — finished project"),"name":"Wooden fences","hero":"luxaed-svc-wood","og":"/img/luxaed-svc-wood.jpg",
 "title":"Wooden fence & gate installation in Tallinn — LuxAed","desc":"Manufacture and installation of wooden fences and gates in Tallinn and Harjumaa. Horizontal fence, steel frame, timber treatment. Free measurement and quote.",
 "kicker":"Wood · steel frame","h1":"<em>Wooden fence</em><br>installation",
 "lead":"A warm, tidy look for your plot. We build fences and gates from treated timber on a sturdy steel frame. Natural wood combined with reliable metal.",
 "intro_h":"Why a wooden fence","intro_p":"Wood looks premium and natural and fits any plot. On a steel frame the structure doesn't sag and lasts a long time.",
 "bens":["Treated timber for the Estonian climate","Sturdy steel frame. No sagging","Horizontal, vertical or louvre","Fence and gates in one style","Gate automation available","Custom design for your plot"],
 "types_tag":"Types of wooden fence","types_h":"Types of wooden fence",
 "types":[("luxaed-svc-wood","Horizontal wooden fence on a steel frame","▤","Fence type","Horizontal fence","A horizontal wooden fence has horizontal boards on a steel frame, the most popular, modern look. We set the gap between boards for privacy or a lighter, airier feel.",["Steel frame","Adjustable gap","Most popular"]),
          ("luxaed-wood-2","Vertical wooden fence and pedestrian gate","▥","Fence type","Vertical fence","A vertical wooden fence has upright boards, classic and tidy, with a gap or fully closed. Works as both a street-side and yard-side screen.",["Upright boards","Gapped or solid","Classic"]),
          ("luxaed-wood-swing-gate-1","Wooden sliding gate on a steel frame","⛩","Gates","Wooden gates","We make wooden gates to match the fence: sliding or swing, with timber infill and a steel frame, and automation if you want it.",["Sliding or swing","Matches the fence","Automation ready"])],
 "cta_band":"Let's pick a wooden fence for your home","incl":["On-site measurement","Making the sections and steel frame","Installing posts and mounting sections","Timber treatment and coating","Post-installation check"],
 "factors":["Fence length and height","Type (horizontal, vertical, louvre)","Timber species and treatment","Gates and automation","Terrain and groundwork"],
 "gallery":[("luxaed-svc-wood","Wooden fence on a steel frame"),("luxaed-g1","Wooden fence and sliding gate"),("luxaed-wood-2","Wooden fence on a plot"),("luxaed-wood-3","Wooden fence and gate"),("luxaed-g2","Wooden swing gates"),("luxaed-g7","Wooden fence by the path"),("luxaed-wood-sliding-gate-1","Wooden sliding gate"),("luxaed-wood-swing-gate-1","Wooden swing gate"),("luxaed-g10","Wooden gate lock"),("luxaed-w-van","LuxAed on site")],
 "faq":[("Won't the wood rot?","We use treated timber and coating, and the frame is steel. With proper care the fence lasts for many years."),
        ("Can I have horizontal boards?","Yes, a horizontal fence on a steel frame is one of the most popular options."),
        ("Will you make a matching gate?","Yes, we make sliding and swing gates with timber infill in the same design."),
        ("Does a wooden fence need maintenance?","We recommend refreshing the protective coating periodically. We'll explain how to care for it.")]},
{"path":"/en/services/metal-fence/","name":"Corrugated (metal) fences","hero":"luxaed-svc-profnastil","og":"/img/luxaed-svc-profnastil.jpg",
 "title":"Corrugated fence installation in Tallinn — LuxAed","desc":"Corrugated profiled-sheet fences in Tallinn and Harjumaa. Galvanised sheet, wrought iron, concrete walls. Affordable. Free measurement.",
 "kicker":"Corrugated · profiled sheet","h1":"<em>Corrugated fence</em><br>installation",
 "lead":"A practical and affordable solution: a solid fence from galvanised profiled sheet. Full privacy, protection from wind and dust, and various coating colours.",
 "intro_h":"Why profiled sheet","intro_p":"Profiled sheet is inexpensive and quick to install. A solid fence closes off the plot and lasts thanks to galvanising and a polymer coating.",
 "bens":["Full privacy. A solid fence","Galvanised sheet with polymer coating","Various colours (incl. wood-look)","Protection from wind, dust and noise","Wrought-iron and decorative details","Concrete & block fences for a solid wall"],
 "types_tag":"Metal fence options","types_h":"Types of metal fence",
 "types":[("luxaed-profnastil-2","Corrugated profiled-sheet fence","▦","Fence type","Profiled-sheet fence","A profiled-sheet fence is a solid fence of galvanised sheet with a polymer coating. Full privacy and protection from wind, dust and noise. Available in many colours, including wood-look.",["Solid, private","Galvanised + polymer","Many colours"]),
          ("luxaed-concrete-tmp","Concrete fence with a stone look","▣","Solid wall","Concrete & block fence","A concrete and block fence is a solid wall for privacy and noise reduction: stone-look concrete panels or block posts. We combine it with metal, sheet or wrought iron.",["Solid wall","Stone look","Wind & noise shield"]),
          ("luxaed-profnastil-gate","Swing gates from profiled sheet","⛩","Gates","Profiled-sheet gates","We make profiled-sheet gates to match the fence colour: sliding or swing, from galvanised sheet, with automation if you want it.",["Sliding or swing","Matches the fence","Automation ready"])],
 "cta_band":"Let's price a corrugated fence","incl":["On-site measurement","Installing steel posts and rails","Mounting the profiled sheet","Levelling","Post-installation check"],
 "factors":["Fence length and height","Sheet grade and colour","Post type (metal, brick, block)","Gates and pedestrian gates","Terrain and groundwork"],
 "gallery":[("luxaed-svc-profnastil","Corrugated sheet gate"),("luxaed-concrete-tmp","Concrete and block fence"),("luxaed-profnastil-2","Corrugated metal fence"),("luxaed-profnastil-gate","Swing gates from profiled sheet"),("luxaed-w-lippaed-1","Graphite steel picket"),("luxaed-w-lippaed-2","Grey steel picket"),("luxaed-w-lippaed-3","Brown steel picket"),("luxaed-w-lock-brown","Gate lock"),("luxaed-w-lock-black","Gate lock and handle"),("luxaed-w-van","LuxAed on site")],
 "faq":[("Won't the sheet fade?","Quality sheet with a polymer coating keeps its colour for a long time. We use proven materials."),
        ("Do you also pour concrete or block walls?","Yes, we build solid concrete and block walls and combine them with metal, sheet or wrought iron."),
        ("Can it be combined with brick posts?","Yes, we build combined fences: sheet between brick or block posts."),
        ("Is profiled sheet cheaper than wood and mesh?","Usually yes. It's one of the most affordable options. We'll give an exact price after the measurement.")]},
{"path":"/en/services/steel-picket/","name":"Steel picket fence","hero":"luxaed-w-lippaed-1","og":"/img/luxaed-w-lippaed-1.jpg",
 "title":"Steel picket fence installation in Tallinn — LuxAed","desc":"Steel picket (euro-picket) fences in Tallinn and Harjumaa: adjustable gaps, galvanised and powder-coated. Free measurement.",
 "kicker":"Steel picket · metal","h1":"<em>Steel picket</em><br>installation",
 "lead":"A modern steel picket (euro-picket): light, tidy and long-lasting. Galvanised and powder-coated slats with an adjustable gap.",
 "intro_h":"Why a steel picket","intro_p":"A steel picket fence looks light and modern, lets light through and lasts for decades. It suits homes and businesses. And we make the fence and gates in one style.",
 "bens":["A modern semi-open fence","Adjustable gap between the slats","Galvanised + powder-coated. No rust","RAL colours, incl. anthracite RAL 7016","Fence and gates in one style","Single- or double-sided slats"],
 "types_tag":"Steel picket options","types_h":"Types of steel picket fence",
 "types":[("luxaed-w-lippaed-1","Graphite steel picket fence","▤","Picket type","Steel picket fence","A steel picket fence is a screen of horizontal slats that lets light through and looks modern. You choose the gap between slats: wider for an airy look or tighter for privacy. Single- or double-sided.",["Adjustable slat gap","Single- or double-sided","Galvanised + powder-coated"]),
          ("luxaed-w-lippaed-3","Brown steel picket close-up","◧","Colours","Colours and RAL shades","We make the picket fence in any RAL shade. The most popular are anthracite RAL 7016, grey and brown. The galvanised, powder-coated surface won't rust or fade.",["Anthracite RAL 7016","Grey, brown and more","Won't rust"]),
          ("luxaed-w-gates-picket","Sliding picket gate","⛩","Gates","Picket fence and gates","We make gates from the same slat and colour: sliding and swing gates in one style with the fence, with automation if you want it.",["Same slat and colour","Sliding or swing","Automation ready"])],
 "cta_band":"Let's price a steel picket fence","incl":["On-site measurement","Installing steel posts","Mounting the slats at the chosen gap","Levelling","Post-installation check"],
 "factors":["Fence length and height","Gap and type (single-/double-sided)","Colour (RAL)","Gates and pedestrian gates","Terrain and groundwork"],
 "gallery":[("luxaed-w-lippaed-1","Graphite steel picket fence"),("luxaed-w-lippaed-2","Grey steel picket by the house"),("luxaed-w-lippaed-3","Brown steel picket close-up"),("luxaed-w-gates-picket","Sliding gate from picket"),("luxaed-w-lock-brown","Locinox lock on the pedestrian gate"),("luxaed-w-van","LuxAed van on site")],
 "faq":[("What is a steel picket (euro-picket) fence?","A modern fence of vertical metal slats with an adjustable gap, galvanised and powder-coated. More open than solid sheet, tidy and long-lasting."),
        ("Is a picket fence see-through?","You choose the gap between slats: tighter for privacy or wider for a light look. A double-sided picket is more private."),
        ("Which colours are available?","The most popular is anthracite RAL 7016, plus black and brown. Other RAL shades to order."),
        ("Can the gates match?","Yes, we make sliding and swing gates from the same picket slat in one design.")]},
{"path":"/en/services/gates-automation/","name":"Gates & automation","hero":"luxaed-auto-2","og":"/img/luxaed-auto-2.jpg","videos":[("luxaed-reel-domofon","Hikvision intercom on the gate"),("luxaed-reel-varav-oht","Sliding gate with automation"),("luxaed-video-puitvarav","Sliding gate at one button press"),("luxaed-reel-montaaz","Installation on site")],
 "title":"Gate & automation installation in Tallinn — LuxAed","desc":"Sliding and swing gates, automation, barriers and intercoms in Tallinn and Harjumaa. Turnkey installation. Free measurement.",
 "kicker":"Gates · automation · barriers","h1":"<em>Gate &amp; automation</em><br>installation",
 "lead":"Turnkey sliding and swing gates with automation and intercoms. We manufacture, install and connect everything. You drive into your yard at the press of a button.",
 "intro_h":"Gate automation at any scale","intro_p":"We design, make and install gates with automation, turnkey, from a single pedestrian gate to a full entry system for a large property. We size the drive to the gate's weight and width and connect remotes, intercoms and safety photocells.",
 "bens":["Sliding and swing gate automation at any scale","Drives from known brands: Nice, CAME, BFT, Sommer, DoorHan","Control: remote, phone call (GSM), app, code or RFID","Photocells and warning light for safe operation","Battery backup: the gate works during a power cut","Rolling-code encryption: protected against remote grabbers","Intercoms, video panels, barriers and garage doors"],
 "types_tag":"Gate types","types_h":"All gate types",
 "types":[("luxaed-w-gates-auto","Sliding gate with automation","⇄","Gate type","Sliding gate","A sliding gate is a cantilever gate that moves sideways with no bottom track and takes no space when opening. Ideal as a driveway gate when there's little room in front of the entrance.",["No bottom track","With automation","Wood / sheet / panel"],"center 45%"),
          ("luxaed-w-gates-green","Swing gates from welded panels","⛩","Gate type","Swing gate","A swing gate is a two-leaf gate that opens inward or outward. Simpler and cheaper when there's room for the leaves to open.",["Two leaves","Cheaper","Any automation"]),
          ("luxaed-gate-closeup-1","Pedestrian gate with wood infill and lock","🚶","Gate type","Pedestrian gate","A pedestrian gate is a walk-through gate matched to the fence. Mechanical or electric lock with intercom and call panel.",["Walk-through","Lock / electric lock","Matched to fence"],"center 40%"),
          ("luxaed-gate-hardware-1","Sliding gate rollers and carriages","⚙","Details","Gate hardware","We use quality rollers, carriages, hinges and locks. Galvanised parts withstand the Estonian climate and keep the gate running smoothly for years.",["Galvanised parts","Rollers & carriages","Long-lasting"])],
 "autotypes_tag":"Gate automation","autotypes_h":"Gate automation types",
 "autotypes":[("luxaed-g9","BFT sliding gate drive","⚙","Automation","Sliding gate automation","Sliding gate automation is a drive sized to the gate's weight and width. It comes with a remote, photocells and a smooth soft start.",["Sized to weight","Remote & photocells","BFT / Nice / CAME"]),
              ("luxaed-g6","Swing gate ram drive","⚙","Automation","Swing gate automation","Swing gate automation uses arm or ram drives on both leaves. Quiet, smooth opening and stop with no jerking.",["Arm / ram drive","Quiet operation","Both leaves"]),
              ("luxaed-barrier-tmp","Automatic barrier at an entrance","⊤","Automation","Barrier","A barrier is an automatic boom arm that controls an entrance or car park. Suits housing associations, car parks and sites.",["Car parks & sites","Remote or code","Fast opening"]),
              ("luxaed-reel-domofon-poster","Hikvision intercom on the gate","🔔","Automation","Intercom & video panel","An intercom and video panel open the gate and pedestrian gate remotely. See the visitor on screen or on your phone and open with one tap.",["Video & call","Remote control","Opens the gate"],"left center")],
 "cta_band":"Let's pick gates and automation for your entrance","incl":["Measurement of the entrance","Making the gate and pedestrian gate","Installation and levelling","Automation mounting and setup","Intercom connection, function check"],
 "factors":["Gate type (sliding / swing)","Leaf width and weight","Automation drive brand and power","Control: remote, GSM, app, RFID","Battery backup, intercom, barrier, garage","Infill (wood, sheet, mesh panel)"],
 "gallery":[("luxaed-w-gates-auto","Sliding gate with automation"),("luxaed-w-gates-green","Swing gates from welded panels"),("luxaed-w-gates-graphite","Graphite swing gates"),("luxaed-w-gates-winter","Sliding gate, winter install"),("luxaed-w-gates-night","Gates in the evening"),("luxaed-w-gates-picket","Sliding picket gate"),("luxaed-w-lock-black","Gate lock and handle"),("luxaed-w-mesh-gate","Panel pedestrian gate"),("luxaed-auto-2","Sliding gate drive"),("luxaed-w-van","LuxAed on site")],
 "faq":[("Sliding or swing. Which to choose?","Sliding is handy when there's little space in front of the entrance, since it takes no space when opening. Swing is simpler and cheaper when there's room. We'll help you choose at the measurement."),
        ("Whose automation do you install?","We install drives from well-known brands: Nice, CAME, BFT, Sommer, DoorHan and others. We size the drive to the gate's weight, width and duty."),
        ("How can the gate be controlled?","From a remote, a phone call (GSM), an app, a keypad code or an RFID card. One remote can control every gate and barrier on the plot."),
        ("Does the gate work during a power cut?","Yes, with battery backup fitted. Without it, the gate can always be opened manually with the release key."),
        ("Can automation be fitted to existing gates?","In most cases yes. We assess the structure and pick a suitable drive for a sliding or swing gate."),
        ("What about automation safety?","We fit photocells and a warning light so the gate won't close on a car or a person. Our rolling-code drives are protected against interception."),
        ("Do you install intercoms and barriers?","Yes, we install and connect intercoms and call panels, plus automatic barriers for car parks and housing associations.")]},
{"path":"/en/services/fence-repair/","video":("luxaed-reel-remont","Removing an old concrete post"),"name":"Fence & gate repair","hero":"luxaed-g6","og":"/img/luxaed-g6.jpg",
 "title":"Fence & gate repair in Tallinn — LuxAed","desc":"Repair of fences and gates in Tallinn and Harjumaa: replacing sections and posts, repairing sliding and swing gates, automation and hardware. Inspection and quote.",
 "kicker":"Repair · maintenance","h1":"<em>Fence &amp; gate</em><br>repair",
 "lead":"We restore fences, gates and automation: replacing sections and posts, adjusting leaves, repairing drives and hardware. We run inspection and give you a price.",
 "intro_h":"What we repair","intro_p":"You don't always need a whole new fence. Often it's enough to replace damaged sections or posts, adjust the gates or restore the automation.",
 "bens":["Replacing damaged fence sections","Replacing and levelling posts","Repairing sliding and swing gates","Automation repair and setup","Replacing rollers, tracks and hardware","Inspection and a price before work"],
 "variants_h":"Types of repair work",
 "variants":[("▤","Fence sections","Replacing damaged panels, boards or sheet."),
             ("▥","Posts","Replacing, levelling and reinforcing leaning posts."),
             ("⇄","Gates","Adjusting leaves, replacing rollers and tracks."),
             ("⚙","Automation","Inspection and repair of drives, remotes and photocells.")],
 "cta_band":"We'll run inspection and fix your fence","incl":["Visit and inspection","A price before work starts","Replacing sections, posts or hardware","Adjusting gates and automation","Function check after the repair"],
 "factors":["Extent and type of damage","Fence and gate type","Need to replace materials","Automation repair","Access to the site"],
 "gallery":[("luxaed-w-gates-winter","We work in winter too"),("luxaed-w-mesh-detail","Checking the fixings"),("luxaed-w-lock-black","Lock replacement"),("luxaed-g6","Gate drive and post"),("luxaed-g8","Sliding gate automation"),("luxaed-g9","Gate drive"),("luxaed-auto-2","Drive repair"),("luxaed-w-lock-brown","Lock replacement"),("luxaed-w-crew","Craftsman at work"),("luxaed-w-van","LuxAed on site")],
 "faq":[("Can it be repaired instead of replacing the whole fence?","Often yes. We replace only the damaged sections or posts. At the inspection we assess what's more cost-effective."),
        ("Do you repair gate automation?","Yes, we diagnose and repair drives, remotes and photocells, replacing them if needed."),
        ("Do you repair gates you didn't install?","Yes, we work with other builders' structures too. We assess on site."),
        ("How much does repair cost?","It depends on the scope. After inspection we give an exact price with no hidden fees.")]},
]

for c in ENSERV: service(c)
print("EN services done:", len(ENSERV))
