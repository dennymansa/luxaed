#!/usr/bin/env python3
# English tree: /en/ service pages. Mirrors gen_et structure.
import json, html
from build_pages import head, nav, footer, SCRIPTS, write, PHONE, TEL, EMAIL, FB, DOMAIN, SVC, reel_strip, webp_sources
from lead_form import render_lead_form
from service_catalog import assert_service_coverage, service_paths
from service_layout import write_service

def form_html(default_service="", default_material=""):
    return render_lead_form("en", default_service, default_material)

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
        return (f'<article class="gtype"><div class="gtype-img"><span class="gtype-badge"><span class="gt-ic">{ic}</span>{eb}</span>'
                f'<picture>{webp_sources(im)}<img src="/img/{im}.jpg" alt="{html.escape(a)}" width="640" height="480" loading="lazy" decoding="async"{st}></picture></div>'
                f'<div class="gtype-txt"><h3>{t}</h3><p>{d}</p><ul class="gtype-specs">{chips}</ul></div></article>')
    count_class=f'gtypes--n{min(len(items),4)}'
    return f'<div class="gtypes {count_class}">'+"".join(one(i+1,x) for i,x in enumerate(items))+'</div>'
def gal(imgs): return '<div class="gal" id="gal">'+"".join(f'<a href="/img/{i}.jpg" data-lb="1"><picture>{webp_sources(i)}<img src="/img/{i}.jpg" alt="{html.escape(a)}" width="600" height="400" loading="lazy"></picture></a>' for i,a in imgs)+'</div>'
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
    visual_note=f'<p class="visual-note">{c["visual_note"]}</p>' if c.get("visual_note") else ''
    types_sec=f'<section class="section"><div class="wrap"><span class="tag">{c["types_tag"]}</span><h2 class="big">{c["types_h"]}</h2>{gtypes(c["types"])}{visual_note}{_tcta}</div></section>\n' if c.get("types") else ''
    auto_note=f'<p class="visual-note">{c["autotypes_note"]}</p>' if c.get("autotypes_note") else ''
    auto_sec=f'<section class="section section--alt"><div class="wrap"><span class="tag">{c.get("autotypes_tag","")}</span><h2 class="big">{c.get("autotypes_h","")}</h2>{gtypes(c["autotypes"])}{auto_note}{cta_band}</div></section>\n' if c.get("autotypes") else ''
    variants_sec=f'<section class="section section--alt"><div class="wrap"><span class="tag">Options</span><h2 class="big">{c["variants_h"]}</h2>{cards(c["variants"])}{cta_band}</div></section>\n' if c.get("variants") else ''
    final_by_service={
        "aed":("Let's plan the <em>right fence</em> for your site","Send a request or call us.<br>We'll measure the site free of charge and prepare an exact quote."),
        "varav":("Let's choose the right <em>gate and automation</em> for your entrance","Send a request or call us.<br>We'll measure the entrance and recommend a suitable gate with automation."),
        "remont":("Let's get your <em>fence or gate working properly again</em>","Send a request or call us.<br>We'll inspect the structure and quote the repair before work begins."),
    }
    final_cta,final_cta_text=final_by_service[c["form_service"]]
    body=f'''{nav("en",c["path"])}
<main id="main">
<section class="hero">
  <div class="hero-photo-bg" style="background:url('/img/{c["hero"]}.webp') center 55%/cover no-repeat"></div>
  <div class="wrap"><div class="hero-grid"><div>
    <div class="hero-trust"><span class="ht-stars">★★★★★</span><span class="ht-score">100%</span><span class="ht-sep">·</span><a class="ht-label" href="{FB}" target="_blank" rel="noopener">34 reviews on Facebook · recommend</a></div>
    <div class="hero-service-kicker">{c["kicker"]}</div>
    <h1>{c["h1"]}</h1>
    <div class="hero-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>{form_html(c["form_service"],c.get("form_material",""))}</div>
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
<section class="cta-final"><div class="wrap"><h2>{final_cta}</h2>
  <p>{final_cta_text}</p>
  <div class="hero-btns"><a class="btn btn-accent" href="#form">Get a quote →</a><a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div></div></section>
</main>
<div class="lb" id="lb"><button class="lb-x" aria-label="Close">&times;</button><img src="" alt="" id="lbImg"></div>
{footer("en")}
<div class="mob-bar"><a class="btn btn-accent mob-call" href="tel:{TEL}"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="vertical-align:-3px;margin-right:6px"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>Call</a></div>
{SCRIPTS}
</body></html>'''
    print("wrote", write(c["path"],H+"\n"+body))

ENSERV=[
{"path":"/en/fences/mesh/","video":("luxaed-reel-vorkaed","3D welded-mesh fence — finished project"),"name":"Welded 2D & 3D mesh fences","hero":"luxaed-w-mesh-1","og":"/img/luxaed-w-mesh-1.jpg",
 "title":"Mesh & 3D fence installation in Tallinn — LuxAed","desc":"Welded 2D and 3D mesh fences in Tallinn and Harjumaa. Rigid mesh sections, posts, gates and dog runs. Turnkey installation and free measurement.",
 "kicker":"Welded 3D mesh · rigid sections · posts","form_service":"aed","form_material":"2D/3D welded mesh","h1":"<em>Mesh &amp; 3D fence</em><br>installation",
 "lead":"Rigid sections of welded 3D mesh with V-shaped folds make a strong, tidy fence while preserving visibility across the plot. The steel wire is protected with zinc and a coloured coating.",
 "intro_h":"Why choose a 3D mesh fence","intro_p":"A 3D fence is made from welded steel mesh formed into rigid sections. The V-shaped folds add stiffness, so the mesh does not need to be tensioned like a roll fence. It suits homes, housing developments and commercial grounds. We install the posts, make matching gates and dog runs, and source the materials.",
 "bens":["Rigid welded 2D and 3D mesh sections","Zinc and coloured protective coating","Anthracite RAL 7016 and other colours","Good visibility and low wind loading","Galvanised fence posts, caps and clips","Dog runs and animal enclosures from welded mesh"],
 "types_tag":"2D and 3D","types_h":"Welded 2D and 3D mesh fences",
 "types":[("luxaed-w-mesh-1","Anthracite 3D mesh fence by a hedge","3D","Welded mesh","3D mesh fence","V-shaped folds add stiffness to the welded mesh section and give it a profiled appearance. A practical choice for homes and normal-load sites.",["V-shaped folds","Practical choice","Anthracite RAL 7016"]),
          ("luxaed-paneelaed-2d-v1","Illustration of 2D welded mesh with twin horizontal wires","2D","Welded mesh","2D mesh fence","A flat section with one vertical and paired horizontal wires. At comparable dimensions, 2D mesh is generally stiffer and suits higher-load areas.",["Twin horizontal wire","Flat section","Higher stiffness"])],
 "visual_note":"The 2D mesh image is a construction illustration; the 3D fence photos and gallery show real LuxAed projects.",
 "variants_h":"Posts, colours and other mesh solutions",
 "variants":[("▤","Fence posts","Galvanised fence posts with caps, brackets and clips. We install and source the material."),
             ("⌗","Dog runs","Dog runs and animal enclosures from rigid welded-mesh sections. Strong and safe."),
             ("◧","RAL colours","Anthracite RAL 7016, green RAL 6005, black and other coating colours.")],
 "cta_band":"Let's price a mesh fence for your plot","incl":["On-site measurement","Installation of galvanised posts","Mounting of welded-mesh sections and fixings","Levelling to the terrain","Post-installation check"],
 "factors":["Fence length and mesh-section height (1.23–2.03 m)","Mesh type (2D/3D), wire diameter and colour","Number and type of fence posts","Gates, pedestrian gates and dog runs","Terrain and removal of the old fence"],
 "gallery":[("luxaed-w-mesh-1","Anthracite 3D mesh fence"),("luxaed-w-mesh-2","Green welded 3D mesh fence"),("luxaed-w-mesh-gate","Pedestrian gate with welded-mesh infill"),("luxaed-w-gates-green","Swing gates with 3D mesh infill"),("luxaed-w-mesh-detail","Mesh-section fixing on the post"),("luxaed-w-panels","3D mesh sections before installation"),("luxaed-3d-mesh-video-v1","Finished 3D mesh fence — frame from a LuxAed project video"),("luxaed-w-gates-night","Mesh-infill gates in the evening"),("luxaed-mesh-2","3D mesh fence along the plot"),("luxaed-w-van","LuxAed crew on site")],
 "faq":[("Chain-link or welded 3D mesh: which should I choose?","Chain-link comes in a roll and is tensioned between posts. Welded 3D mesh is installed as rigid sections with V-shaped folds and does not need tensioning. We'll price both and help you choose for the site and budget."),
        ("How long does a 3D fence last?","Galvanised and coated welded mesh is designed for long-term outdoor use. Service life depends on the coating, conditions and whether the surface is damaged."),
        ("What heights are available?","Common heights range from 1.23 to 2.03 m. We select the height for boundary marking, safety or enclosing the site."),
        ("Which colour should I choose?","The most popular are anthracite RAL 7016 and green RAL 6005. Other coating colours are available."),
        ("Do you install fence posts too?","Yes, we install galvanised fence posts with caps and clips and source the materials for welded mesh and other fence types."),
        ("Do you build dog runs?","Yes, we build dog runs and animal enclosures from rigid welded-mesh sections."),
        ("Can I get a matching gate?","Yes, we make sliding and swing gates with the same welded-mesh infill and colour.")]},
{"path":"/en/fences/wooden/","video":("luxaed-video-puitvarav","Wooden sliding gate with automation — finished project"),"name":"Wooden fences","hero":"luxaed-svc-wood","og":"/img/luxaed-svc-wood.jpg",
 "title":"Wooden fence & gate installation in Tallinn — LuxAed","desc":"Manufacture and installation of wooden fences and gates in Tallinn and Harjumaa. Horizontal fence, steel frame, timber treatment. Free measurement and quote.",
 "kicker":"Wood · steel frame","form_service":"aed","form_material":"Wood","h1":"<em>Wooden fence</em><br>installation",
 "lead":"A warm, tidy look for your plot. We build fences and gates from treated timber on a sturdy steel frame. Natural wood combined with reliable metal.",
 "intro_h":"Why a wooden fence","intro_p":"Wood looks premium and natural and fits any plot. On a steel frame the structure doesn't sag and lasts a long time.",
 "bens":["Treated timber for the Estonian climate","Sturdy steel frame. No sagging","Horizontal, vertical or louvre","Fence and gates in one style","Gate automation available","Custom design for your plot"],
 "types_tag":"Types of wooden fence","types_h":"Types of wooden fence",
 "types":[("luxaed-svc-wood","Horizontal wooden fence on a steel frame","▤","Fence type","Horizontal fence","A horizontal wooden fence has horizontal boards on a steel frame, the most popular, modern look. We set the gap between boards for privacy or a lighter, airier feel.",["Steel frame","Adjustable gap","Most popular"]),
          ("luxaed-wood-2","Vertical wooden fence and pedestrian gate","▥","Fence type","Vertical fence","A vertical wooden fence has upright boards, classic and tidy, with a gap or fully closed. Works as both a street-side and yard-side screen.",["Upright boards","Gapped or solid","Classic"]),
          ("luxaed-wood-swing-gate-1","Wooden swing gates on a steel frame","⛩","Gates","Wooden gates","We make wooden gates to match the fence: sliding or swing, with timber infill and a steel frame, and automation if you want it.",["Sliding or swing","Matches the fence","Automation ready"])],
 "cta_band":"Let's pick a wooden fence for your home","incl":["On-site measurement","Making the sections and steel frame","Installing posts and mounting sections","Timber treatment and coating","Post-installation check"],
 "factors":["Fence length and height","Type (horizontal, vertical, louvre)","Timber species and treatment","Gates and automation","Terrain and groundwork"],
 "gallery":[("luxaed-svc-wood","Wooden fence on a steel frame"),("luxaed-g1","Wooden fence and sliding gate"),("luxaed-wood-2","Wooden fence on a plot"),("luxaed-wood-3","Wooden fence and gate"),("luxaed-g2","Wooden swing gates"),("luxaed-g7","Wooden fence by the path"),("luxaed-wood-sliding-gate-1","Wooden sliding gate"),("luxaed-wood-swing-gate-1","Wooden swing gate"),("luxaed-g10","Wooden gate lock"),("luxaed-w-van","LuxAed on site")],
 "faq":[("Won't the wood rot?","We use treated timber and coating, and the frame is steel. With proper care the fence lasts for many years."),
        ("Can I have horizontal boards?","Yes, a horizontal fence on a steel frame is one of the most popular options."),
        ("Will you make a matching gate?","Yes, we make sliding and swing gates with timber infill in the same design."),
        ("Does a wooden fence need maintenance?","We recommend refreshing the protective coating periodically. We'll explain how to care for it.")]},
{"path":"/en/fences/metal/","name":"Corrugated (metal) fences","hero":"luxaed-profnastil-2","og":"/img/luxaed-profnastil-2.jpg",
 "title":"Corrugated fence installation in Tallinn — LuxAed","desc":"Profiled-sheet and modular fences (moodulaed) in Tallinn and Harjumaa. Galvanised sheet, wrought iron, concrete walls. Free measurement.",
 "kicker":"Corrugated · profiled sheet","form_service":"aed","form_material":"Corrugated sheet","h1":"<em>Corrugated fence</em><br>installation",
 "lead":"A practical and affordable solution: a solid fence from galvanised profiled sheet. Full privacy, protection from wind and dust, and various coating colours.",
 "intro_h":"Why profiled sheet","intro_p":"Profiled sheet is inexpensive and quick to install. A solid fence closes off the plot and lasts thanks to galvanising and a polymer coating. A profiled-sheet fence is also a modular fence (moodulaed): ready sections that go up fast.",
 "bens":["Full privacy. A solid fence","Galvanised sheet with polymer coating","Various colours (incl. wood-look)","Protection from wind, dust and noise","Wrought-iron and decorative details","Concrete & block fences for a solid wall","Modular fence (moodulaed): ready sections, fast install"],
 "types_tag":"Metal fence options","types_h":"Types of metal fence",
 "types":[("luxaed-profnastil-2","Corrugated profiled-sheet fence","▦","Fence type","Profiled-sheet fence","A profiled-sheet fence is a solid fence of galvanised sheet with a polymer coating. Full privacy and protection from wind, dust and noise. Available in many colours, including wood-look.",["Solid, private","Galvanised + polymer","Many colours"]),
          ("luxaed-concrete-fence-guide","Concrete fence with a stone look","▣","Solid wall","Concrete & block fence","A concrete and block fence is a solid wall for privacy and noise reduction: stone-look concrete panels or block posts. We combine it with metal, sheet or wrought iron.",["Solid wall","Stone look","Wind & noise shield"]),
          ("luxaed-profnastil-gate","Swing gates from profiled sheet","⛩","Gates","Profiled-sheet gates","We make profiled-sheet gates to match the fence colour: sliding or swing, from galvanised sheet, with automation if you want it.",["Sliding or swing","Matches the fence","Automation ready"])],
 "visual_note":"The concrete-fence image is a photorealistic solution illustration.",
 "cta_band":"Let's price a corrugated fence","incl":["On-site measurement","Installing steel posts and rails","Mounting the profiled sheet","Levelling","Post-installation check"],
 "factors":["Fence length and height","Sheet grade and colour","Post type (metal, brick, block)","Gates and pedestrian gates","Terrain and groundwork"],
 "gallery":[("luxaed-profnastil-2","Solid profiled-sheet fence"),("luxaed-svc-profnastil","Sliding gate with profiled-sheet infill"),("luxaed-profnastil-gate","Swing gates from profiled sheet")],
 "faq":[("Won't the sheet fade?","Quality sheet with a polymer coating keeps its colour for a long time. We use proven materials."),
        ("Do you also pour concrete or block walls?","Yes, we build solid concrete and block walls and combine them with metal, sheet or wrought iron."),
        ("Can it be combined with brick posts?","Yes, we build combined fences: sheet between brick or block posts."),
        ("Is profiled sheet cheaper than wood and mesh?","Usually yes. It's one of the most affordable options. We'll give an exact price after the measurement."),("Do you build modular fences (moodulaed)?","Yes. Profiled-sheet and rigid welded-mesh fences can be assembled from ready-made sections and posts, so installation is fast and tidy.")]},
{"path":"/en/fences/steel-picket/","name":"Steel picket fence","hero":"luxaed-w-gates-picket","og":"/img/luxaed-w-gates-picket.jpg",
 "title":"Steel picket fence installation in Tallinn — LuxAed","desc":"Steel picket (euro-picket) fences in Tallinn and Harjumaa: adjustable gaps, galvanised and powder-coated. Free measurement.",
 "kicker":"Steel picket · metal","form_service":"aed","form_material":"Steel picket","h1":"<em>Steel picket</em><br>installation",
 "lead":"A modern steel picket (euro-picket): light, tidy and long-lasting. Galvanised and powder-coated slats with an adjustable gap.",
 "intro_h":"Why a steel picket","intro_p":"A steel picket fence looks light and modern, lets light through and lasts for decades. It suits homes and businesses. And we make the fence and gates in one style.",
 "bens":["A modern semi-open fence","Adjustable gap between the slats","Galvanised + powder-coated. No rust","RAL colours, incl. anthracite RAL 7016","Fence and gates in one style","Single- or double-sided slats"],
 "types_tag":"Steel picket options","types_h":"Types of steel picket fence",
 "types":[("luxaed-w-gates-picket","Vertical steel picket on a sliding gate","▥","Slat orientation","Vertical steel picket","Vertical profiled steel slats create a classic rhythm while letting light through. We set the gap and single- or double-sided layout for the privacy you need.",["Vertical slats","Adjustable gap","Galvanised + coated"]),
          ("luxaed-w-lippaed-1","Graphite fence with horizontal metal slats","▤","Slat orientation","Horizontal metal slats","Horizontal slats give the fence a clean, modern line. Choose a wider gap for an airy look or a tighter arrangement for more privacy.",["Horizontal layout","Adjustable gap","Modern look"]),
          ("luxaed-w-lippaed-3","Brown horizontal metal slats in close-up","◧","Colours","RAL colours and finishes","Metal slats are available in a range of RAL colours. Anthracite RAL 7016, grey and brown are popular; galvanising and a quality finish protect the steel from corrosion.",["Anthracite RAL 7016","Grey, brown and more","Corrosion protection"])],
 "cta_band":"Let's price a steel picket fence","incl":["On-site measurement","Installing steel posts","Mounting the slats at the chosen gap","Levelling","Post-installation check"],
 "factors":["Fence length and height","Gap and type (single-/double-sided)","Colour (RAL)","Gates and pedestrian gates","Terrain and groundwork"],
 "gallery":[("luxaed-w-gates-picket","Sliding gate with vertical steel picket infill"),("luxaed-w-lippaed-1","Graphite fence with horizontal metal slats"),("luxaed-w-lippaed-2","Grey horizontal metal slats by the house"),("luxaed-w-lippaed-3","Brown horizontal metal slats in close-up")],
 "faq":[("What is a steel picket (euro-picket) fence?","A modern fence of vertical metal slats with an adjustable gap, galvanised and powder-coated. More open than solid sheet, tidy and long-lasting."),
        ("Is a picket fence see-through?","You choose the gap between slats: tighter for privacy or wider for a light look. A double-sided picket is more private."),
        ("Which colours are available?","The most popular is anthracite RAL 7016, plus black and brown. Other RAL shades to order."),
        ("Can the gates match?","Yes, we make sliding and swing gates from the same picket slat in one design.")]},
{"path":"/en/gates-automation/","name":"Gates & automation","hero":"luxaed-auto-2","og":"/img/luxaed-auto-2.jpg","videos":[("luxaed-reel-domofon","Hikvision intercom on the gate"),("luxaed-reel-varav-oht","Sliding gate with automation"),("luxaed-video-puitvarav","Sliding gate at one button press"),("luxaed-reel-montaaz","Installation on site")],
 "title":"Gate & automation installation in Tallinn — LuxAed","desc":"Sliding and swing gates, automation, barriers and intercoms in Tallinn and Harjumaa. Turnkey installation. Free measurement.",
 "kicker":"Gates · automation · barriers","form_service":"varav","form_material":"","h1":"<em>Gate &amp; automation</em><br>installation",
 "lead":"Turnkey sliding and swing gates with automation and intercoms. We manufacture, install and connect everything. You drive into your yard at the press of a button.",
 "intro_h":"Gate automation at any scale","intro_p":"We design, make and install gates with automation, turnkey, from a single pedestrian gate to a full entry system for a large property. We size the drive to the gate's weight and width and connect remotes, intercoms and safety photocells.",
 "bens":["Sliding and swing gate automation at any scale","Drives from known brands: Nice, CAME, BFT, Sommer, DoorHan","Control: remote, phone call (GSM), app, code or RFID","Photocells and warning light for safe operation","Battery backup: the gate works during a power cut","Rolling-code encryption: protected against remote grabbers","Intercoms, video panels, barriers and garage doors"],
 "types_tag":"Gate types","types_h":"All gate types",
 "types":[("luxaed-svc-gates","Wooden sliding gate with automation","⇄","Gate type","Sliding gate","A sliding gate is a cantilever gate that moves sideways with no bottom track and takes no space when opening. Ideal as a driveway gate when there's little room in front of the entrance.",["No bottom track","With automation","Wood / sheet / panel"],"center 45%"),
          ("luxaed-w-gates-green","Swing gates with welded-mesh infill","⛩","Gate type","Swing gate","A swing gate is a two-leaf gate that opens inward or outward. Simpler and cheaper when there's room for the leaves to open.",["Two leaves","Cheaper","Any automation"]),
          ("luxaed-gate-closeup-1","Pedestrian gate with wood infill and lock","🚶","Gate type","Pedestrian gate","A pedestrian gate is a walk-through gate matched to the fence. Mechanical or electric lock with intercom and call panel.",["Walk-through","Lock / electric lock","Matched to fence"],"center 40%"),
          ("luxaed-gate-hardware-1","Sliding gate rollers and carriages","⚙","Details","Gate hardware","We use quality rollers, carriages, hinges and locks. Galvanised parts withstand the Estonian climate and keep the gate running smoothly for years.",["Galvanised parts","Rollers & carriages","Long-lasting"])],
 "autotypes_tag":"Gate automation","autotypes_h":"Gate automation types",
 "autotypes":[("luxaed-w-gates-auto","BFT drive on a LuxAed sliding-gate installation","⚙","Automation","Sliding gate automation","We size the drive to the gate's weight, width and duty cycle, then agree the remotes, photocells and warning light for the entrance.",["Sized to weight","Remote & photocells","BFT / Nice / CAME"]),
              ("luxaed-g6","Swing gate ram drive","⚙","Automation","Swing gate automation","Swing gate automation uses arm or ram drives on both leaves. Quiet, smooth opening and stop with no jerking.",["Arm / ram drive","Quiet operation","Both leaves"]),
              ("luxaed-barrier-guide","Automatic barrier at an entrance","⊤","Automation","Barrier","A barrier is an automatic boom arm that controls an entrance or car park. Suits housing associations, car parks and sites.",["Car parks & sites","Remote or code","Fast opening"]),
              ("luxaed-reel-domofon-poster","Hikvision intercom on the gate","🔔","Automation","Intercom & video panel","An intercom and video panel open the gate and pedestrian gate remotely. See the visitor on screen or on your phone and open with one tap.",["Video & call","Remote control","Opens the gate"],"left center")],
 "autotypes_note":"The barrier image is a photorealistic solution illustration.",
 "cta_band":"Let's pick gates and automation for your entrance","incl":["Measurement of the entrance","Making the gate and pedestrian gate","Installation and levelling","Automation mounting and setup","Intercom connection, function check"],
 "factors":["Gate type (sliding / swing)","Leaf width and weight","Automation drive brand and power","Control: remote, GSM, app, RFID","Battery backup, intercom, barrier, garage","Infill (wood, sheet or welded mesh)"],
 "gallery":[("luxaed-svc-gates","Wooden sliding gate with automation"),("luxaed-w-gates-auto","BFT drive on a sliding gate"),("luxaed-w-gates-green","Swing gates with welded-mesh infill"),("luxaed-w-gates-graphite","Graphite swing gates"),("luxaed-w-gates-winter","Sliding gate, winter install"),("luxaed-w-gates-night","Gates in the evening"),("luxaed-w-gates-picket","Sliding picket gate"),("luxaed-w-lock-black","Gate lock and handle"),("luxaed-w-mesh-gate","Pedestrian gate with welded-mesh infill"),("luxaed-w-van","LuxAed on site")],
 "faq":[("Sliding or swing. Which to choose?","Sliding is handy when there's little space in front of the entrance, since it takes no space when opening. Swing is simpler and cheaper when there's room. We'll help you choose at the measurement."),
        ("Whose automation do you install?","We install drives from well-known brands: Nice, CAME, BFT, Sommer, DoorHan and others. We size the drive to the gate's weight, width and duty."),
        ("How can the gate be controlled?","From a remote, a phone call (GSM), an app, a keypad code or an RFID card. One remote can control every gate and barrier on the plot."),
        ("Does the gate work during a power cut?","Yes, with battery backup fitted. Without it, the gate can always be opened manually with the release key."),
        ("Can automation be fitted to existing gates?","In most cases yes. We assess the structure and pick a suitable drive for a sliding or swing gate."),
        ("What about automation safety?","We fit photocells and a warning light so the gate won't close on a car or a person. Our rolling-code drives are protected against interception."),
        ("Do you install intercoms and barriers?","Yes, we install and connect intercoms and call panels, plus automatic barriers for car parks and housing associations.")]},
{"path":"/en/fence-repair/","video":("luxaed-reel-remont","Removing an old concrete post"),"name":"Fence & gate repair","hero":"luxaed-repair-real-v1","og":"/img/luxaed-repair-real-v1.jpg",
 "title":"Fence & gate repair in Tallinn — LuxAed","desc":"Repair of fences and gates in Tallinn and Harjumaa: replacing sections and posts, repairing sliding and swing gates, automation and hardware. Inspection and quote.",
 "kicker":"Repair · maintenance","form_service":"remont","form_material":"","h1":"<em>Fence &amp; gate</em><br>repair",
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
 "gallery":[("luxaed-repair-real-v1","Removing an old concrete post"),("luxaed-w-mesh-detail","Checking a welded-mesh fixing"),("luxaed-w-lock-black","Pedestrian-gate lock and handle"),("luxaed-w-lock-brown","Gate lock in close-up"),("luxaed-w-gates-auto","Sliding-gate drive"),("luxaed-w-crew","LuxAed installer on site"),("luxaed-w-van","LuxAed on site")],
 "faq":[("Can it be repaired instead of replacing the whole fence?","Often yes. We replace only the damaged sections or posts. At the inspection we assess what's more cost-effective."),
        ("Do you repair gate automation?","Yes, we diagnose and repair drives, remotes and photocells, replacing them if needed."),
        ("Do you repair gates you didn't install?","Yes, we work with other builders' structures too. We assess on site."),
        ("How much does repair cost?","It depends on the scope. After inspection we give an exact price with no hidden fees.")]},
]

# English content follows the same eight-service matrix as Estonian.  The
# renderer is shared; this file intentionally contains translations only.
ENSERV.extend([
{"path":"/en/fences/roll-mesh/","name":"Roll mesh and chain-link fences","hero":"luxaed-rullvork-slope-v1","og":"/img/luxaed-rullvork-slope-v1.jpg",
 "title":"Chain-link & roll-mesh fence installation in Tallinn — LuxAed","desc":"Chain-link and welded roll-mesh fence installation in Tallinn and Harjumaa. A practical solution for long boundaries, sloping plots and enclosures. Free measurement.",
 "kicker":"Chain-link · welded roll mesh · long boundaries","form_service":"aed","form_material":"Roll mesh / chain-link","h1":"<em>Roll mesh &amp; chain-link</em><br>fence installation",
 "lead":"A practical, cost-effective fence for a long boundary, garden or enclosure. Woven chain-link and welded roll mesh follow changes in the terrain and preserve an open view.",
 "intro_h":"A flexible fence for long and uneven boundaries","intro_p":"Roll mesh is supplied in rolls and tensioned between installed posts. Unlike rigid 2D or 3D welded-mesh sections, it follows slopes and bends more easily. We set the corner and intermediate posts, tension the mesh correctly and install a matching pedestrian or vehicle gate where required.",
 "bens":["Suitable for long fence lines","Follows sloping and uneven ground","Woven chain-link or welded roll mesh","Galvanised or colour-coated finish","Good visibility and low wind loading","Matching pedestrian and vehicle gates"],
 "types_tag":"Roll-mesh options","types_h":"Chain-link and welded roll mesh",
 "types":[("luxaed-rullvork-slope-v1","Roll-mesh fence following a sloping garden boundary","⌁","Woven mesh","Chain-link fence","Interwoven wire forms a flexible mesh that works well on long boundaries and uneven ground. Available galvanised or with a colour coating.",["Flexible roll","Good on slopes","Galvanised or coated"]),
          ("luxaed-vorkaed-roll-v1","Welded roll-mesh fence along a residential boundary","▦","Welded roll mesh","Welded roll-mesh fence","Wire intersections are welded before the mesh is rolled. It gives a more regular grid while remaining easier to adapt to the terrain than rigid fence sections.",["Regular grid","Supplied in rolls","Open appearance"]),
          ("luxaed-rullvork-corner-v1","Tensioned roll mesh at a corner post","⌑","Installation detail","Posts, corners and tensioning","A durable result depends on the post spacing, braced corner posts and even tension. We specify these details for the length, height and ground conditions.",["Braced corners","Even tension","Correct post spacing"])],
 "visual_note":"The roll-mesh images are photorealistic solution illustrations showing the construction and typical finished appearance.",
 "cta_band":"Let's calculate a roll-mesh fence for your boundary",
 "incl":["Free site measurement","Setting and levelling the fence posts","Bracing corners and end posts","Tensioning and fixing the mesh","Final alignment and function check"],
 "factors":["Fence length and height","Woven chain-link or welded roll mesh","Galvanised or colour-coated finish","Number of corners and changes in level","Pedestrian gates, vehicle gates and removal work"],
 "local_h":"Roll-mesh fences across Tallinn and Harjumaa","local_p":"We install chain-link and welded roll-mesh fences for homes, gardens, housing associations and commercial plots throughout Tallinn and Harjumaa. The free measurement lets us check the boundary, access, slopes and soil before we specify the posts and mesh.",
 "price_lead":"The price depends mainly on the fence length, height, mesh finish, number of corners and terrain. After the free site measurement, you receive a clear quote for materials and installation.",
 "gallery":[("luxaed-rullvork-slope-v1","Roll-mesh fence on sloping ground"),("luxaed-vorkaed-roll-v1","Welded roll-mesh fence along a boundary"),("luxaed-rullvork-corner-v1","Roll mesh tensioned at a corner post")],
 "faq":[("Is chain-link the same as a 2D or 3D mesh fence?","No. Chain-link and welded roll mesh are supplied in rolls and tensioned between posts. A 2D or 3D fence uses rigid welded sections fixed to posts. Roll mesh is usually more economical and adapts more easily to slopes; rigid sections are stiffer."),
        ("Which mesh works best on a sloping plot?","Roll mesh usually follows gradual changes in level better than rigid sections. We inspect the slope and recommend woven chain-link, welded roll mesh or stepped rigid sections."),
        ("Can the mesh be green or anthracite?","Yes. Depending on the mesh type, galvanised and colour-coated finishes are available, including common green and anthracite shades."),
        ("Do you install the posts and tension wire?","Yes. The installation includes the required intermediate, corner and end posts, bracing, tension wire and mesh fixings."),
        ("Can you add a matching gate?","Yes. We can install a pedestrian gate, swing gate or sliding gate suited to the fence and entrance.")]},

{"path":"/en/fences/metal-bar/","name":"Welded metal-bar fences","hero":"luxaed-varbaed-gate-v2","og":"/img/luxaed-varbaed-gate-v2.jpg",
 "title":"Welded metal-bar fence installation in Tallinn — LuxAed","desc":"Custom welded steel-bar fences and matching gates in Tallinn and Harjumaa. Durable open metal sections, galvanised or coated, manufactured and installed to suit the property.",
 "kicker":"Welded steel sections · custom design · matching gates","form_service":"aed","form_material":"Welded metal-bar fence","h1":"<em>Welded metal-bar</em><br>fences",
 "lead":"A strong, open metal fence made as welded steel sections. We adapt the spacing, top line, colour and gate design to the building and boundary, then manufacture and install the complete solution.",
 "intro_h":"A durable metal fence made for the property","intro_p":"A metal-bar fence uses welded steel uprights and rails rather than thin picket slats or wire mesh. It is suitable when you want a robust, open boundary with a clean architectural rhythm. Sections, pedestrian gates and vehicle gates can be made in one design and protected for outdoor use by galvanising, coating or a specified finish.",
 "bens":["Rigid welded steel sections","Straight, decorative or custom top line","Spacing selected for the required openness","Sections and gates in one design","Galvanised and coated finish options","Suitable for homes and commercial sites"],
 "types_tag":"Design options","types_h":"Metal-bar fence, details and gates",
 "types":[("luxaed-varbaed-v1","Straight welded metal-bar fence sections on a residential boundary","▥","Fence sections","Straight metal-bar fence","Vertical steel bars and horizontal rails form a strong, uncluttered boundary. Bar spacing and section height are specified for the site and desired appearance.",["Welded steel","Selected spacing","Clean straight line"]),
          ("luxaed-varbaed-detail-v1","Close-up of a decorative welded metal-bar fence detail","◇","Custom details","Decorative metal-bar fence","A shaped top line, finials or restrained decorative details can give the fence a more traditional character without changing the basic welded construction.",["Custom top line","Decorative details","Made to measure"]),
          ("luxaed-varbaed-gate-v2","Matching welded metal-bar pedestrian and vehicle gate","⛩","Matching entrance","Metal-bar gates","Pedestrian, swing and sliding gates can use the same bars, spacing and finish as the fence. Automation is specified together with a vehicle gate.",["One visual system","Sliding or swing","Automation available"])],
 "visual_note":"The metal-bar fence images are photorealistic solution illustrations showing typical construction and design options.",
 "cta_band":"Let's design a metal-bar fence and matching entrance",
 "incl":["Free measurement and site assessment","Agreeing the section and gate design","Fabrication of steel sections and frames","Installation, alignment and fastening","Final function and finish check"],
 "factors":["Fence length and section height","Bar profile, spacing and design complexity","Galvanising, coating and colour","Pedestrian, swing or sliding gates","Ground conditions and removal of existing structures"],
 "local_h":"Custom metal-bar fences in Tallinn and Harjumaa","local_p":"We measure, manufacture and install welded metal-bar fences for private homes, apartment properties and commercial sites across Tallinn and Harjumaa. During the measurement we check the levels, post locations and entrance so the fence and gates form one coherent solution.",
 "price_lead":"Each welded metal-bar fence is specified for its dimensions, design and finish. After the free measurement, we provide a quote covering the steelwork, protective finish, installation and any matching gates.",
 "gallery":[("luxaed-varbaed-v1","Welded metal-bar fence sections"),("luxaed-varbaed-detail-v1","Decorative detail on a metal-bar fence"),("luxaed-varbaed-gate-v2","Matching metal-bar gate and fence")],
 "faq":[("How is a metal-bar fence different from a steel picket fence?","A metal-bar fence is made from welded structural steel bars and rails. A steel picket fence uses lighter profiled slats fixed to rails. We can price both if you are deciding between them."),
        ("Can the fence be made to a custom design?","Yes. We agree the height, bar spacing, top line, colour and gate design before fabrication. Decorative details can be added where appropriate."),
        ("How is the steel protected from corrosion?","The protection is selected for the project and can include galvanising and a durable exterior coating. We explain the proposed finish in the quote."),
        ("Can the pedestrian and vehicle gates match the fence?","Yes. We make matching pedestrian, swing or sliding gates with the same bar spacing and finish. Vehicle-gate automation is specified as part of the gate solution."),
        ("Do you install metal-bar fences in winter?","Yes, installation is possible year-round when site and ground conditions allow safe, durable work.")]},
])

# Keep profiled sheet separate from concrete, decorative bar fencing and welded
# mesh: each search intent has its own landing page.
for c in ENSERV:
    if c["path"] == "/en/fences/metal/":
        c.update({
            "path":"/en/fences/profiled-sheet/","name":"Profiled-sheet fences",
            "title":"Profiled-sheet fence installation in Tallinn — LuxAed",
            "desc":"Profiled-sheet fence installation in Tallinn and Harjumaa. A solid coated-steel boundary with matching gates, selected profile and colour. Free measurement.",
            "kicker":"Profiled sheet · solid boundary · steel frame",
            "h1":"<em>Profiled-sheet fence</em><br>installation",
            "lead":"A solid fence made from coated profiled steel on a strong frame. It screens the plot from direct views and wind and is available in a range of profiles and colours.",
            "intro_h":"A practical solid fence with a clean finish",
            "intro_p":"Profiled sheet is fixed to steel rails between correctly spaced posts. The galvanised steel and exterior coating protect the surface, while the selected profile and colour determine the finished look. We install the fence, corners, trims and matching pedestrian or vehicle gates as one system.",
            "bens":["Solid boundary for greater privacy","Galvanised, coated profiled steel","Choice of profile and exterior colour","Strong steel posts and horizontal rails","Matching pedestrian and vehicle gates","Fast, tidy installation after measurement"],
            "types_tag":"Profiled-sheet options","types_h":"Sheet, frame and matching gates",
            "types":[("luxaed-profnastil-2","Dark profiled-sheet fence on a steel frame","▦","Fence infill","Profiled-sheet fence","Coated profiled steel forms a continuous boundary. We specify the sheet profile, thickness, colour and fixing direction for the required look and exposure.",["Solid infill","Coated steel","Several profiles"]),
                     ("luxaed-svc-profnastil","Profiled-sheet fence and sliding gate in one colour","⇄","Complete entrance","Fence and sliding gate","The sliding gate can use the same profiled-sheet infill and colour as the fence, giving the frontage one consistent appearance.",["Matching infill","Sliding gate","Automation available"]),
                     ("luxaed-profnastil-gate","Swing gates with profiled-sheet infill","⛩","Gate option","Profiled-sheet swing gates","Where the entrance has enough opening space, swing gates provide a straightforward matching solution. The steel frame supports the same sheet as the fence.",["Two leaves","Matching colour","Manual or automated"])],
            "visual_note":"",
            "cta_band":"Let's calculate a profiled-sheet fence for your property",
            "incl":["Free site measurement","Installation and alignment of steel posts","Mounting rails, profiled sheet and trims","Careful treatment of corners and transitions","Final alignment and function check"],
            "factors":["Fence length and height","Sheet profile, thickness and coating","Post and rail dimensions","Pedestrian, swing or sliding gates","Terrain, corners and removal of the old fence"],
            "gallery":[("luxaed-profnastil-2","Solid profiled-sheet fence"),("luxaed-svc-profnastil","Profiled-sheet fence with a matching sliding gate"),("luxaed-profnastil-gate","Swing gates with profiled-sheet infill")],
            "faq":[("How long does a profiled-sheet fence last?","Durability depends on the steel, coating, installation and site exposure. We use exterior-grade coated sheet and protect cut edges and fixings during installation."),
                   ("Is a profiled-sheet fence completely private?","It forms a solid visual screen. Small installation clearances remain at the ground and around gates so the structure can work correctly."),
                   ("Which colours and profiles are available?","Availability varies by supplier, but common exterior colours and several sheet profiles are available. We confirm the current options with the quote."),
                   ("Can the gate use the same profiled sheet?","Yes. We make pedestrian, sliding or swing gates with matching profiled-sheet infill and colour. Automation can be included with the vehicle gate."),
                   ("Does a solid fence need special posts?","A solid fence has higher wind loading than an open mesh fence. We specify the post spacing, foundations and rails for the height and exposure of the site.")],
        })
    elif c["path"] == "/en/fences/steel-picket/":
        c.update({
            "name":"Steel picket and metal-slat fences",
            "title":"Steel picket & metal-slat fence installation in Tallinn — LuxAed",
            "desc":"Vertical steel picket and horizontal metal-slat fences in Tallinn and Harjumaa. Adjustable spacing, coated steel and matching gates. Free measurement.",
            "kicker":"Vertical steel picket · horizontal metal slats",
            "lead":"A clean, durable metal fence with either vertical steel pickets or horizontal metal slats. We select the orientation, spacing, colour and gate infill for the privacy and look you want.",
            "intro_h":"Vertical or horizontal metal slats — both are available",
            "intro_p":"Vertical profiled pickets create a familiar fence rhythm; horizontal metal slats give the frontage a more linear, contemporary appearance. Both can be installed with a wider gap for openness or a tighter arrangement for greater privacy, using coated steel and matching gate infill.",
            "bens":["Vertical steel pickets or horizontal metal slats","Spacing selected for openness or privacy","Galvanised and coated steel","RAL colours, including anthracite RAL 7016","Fence and gates in one design","Single- or double-sided vertical picket layouts"],
            "types_h":"Vertical steel picket and horizontal metal-slat options",
            "faq":[("Can the metal slats be horizontal as well as vertical?","Yes. We install classic vertical steel pickets and horizontal metal-slat systems. The suitable profile, support rails and spacing depend on the chosen orientation and design."),
                   ("Is a steel-picket fence see-through?","You choose the spacing. A tighter or double-sided vertical layout gives more privacy; wider gaps keep the fence lighter and more open."),
                   ("Which colours are available?","Anthracite RAL 7016, grey and brown are common choices. We confirm the available profiles and coating colours when preparing the quote."),
                   ("Can the gates match?","Yes. Sliding, swing and pedestrian gates can use the same vertical pickets or horizontal metal slats as the fence."),
                   ("Which orientation works better on my property?","That depends on the architecture, desired privacy, span and wind exposure. We show suitable vertical and horizontal options during the measurement.")],
        })

_LOCAL_COPY = {
    "/en/fences/wooden/": ("Wooden fences made for Tallinn and Harjumaa properties", "We build wooden fences and matching gates across Tallinn and Harjumaa. During the free measurement we check levels, exposure, access and the entrance so the timber layout, steel frame and foundations are specified for the actual property."),
    "/en/fences/mesh/": ("Welded 2D and 3D mesh fences in Tallinn and Harjumaa", "We install rigid welded-mesh sections for private plots, housing associations and commercial sites throughout Tallinn and Harjumaa. We measure the boundary, check level changes and specify section height, posts, clips and matching gates before quoting."),
    "/en/fences/profiled-sheet/": ("Profiled-sheet fences in Tallinn and Harjumaa", "We install solid profiled-sheet fences and matching gates throughout Tallinn and Harjumaa. The free measurement lets us assess wind exposure, ground conditions, corners and entrance dimensions before sizing the posts and steel frame."),
    "/en/fences/steel-picket/": ("Steel picket and metal-slat fences in Tallinn and Harjumaa", "We install vertical steel pickets and horizontal metal-slat fences for homes and commercial properties across Tallinn and Harjumaa. At the measurement we agree the orientation, spacing, colour, foundations and matching gate design."),
    "/en/gates-automation/": ("Gates and automation installed across Tallinn and Harjumaa", "We measure, manufacture and install sliding, swing and pedestrian gates throughout Tallinn and Harjumaa. Automation is specified together with the gate, entrance geometry, usage level, safety devices and preferred access control."),
    "/en/fence-repair/": ("Fence and gate repairs in Tallinn and Harjumaa", "We inspect and repair fences, gates, hardware and automation across Tallinn and Harjumaa. The visit establishes what can be adjusted or replaced locally and whether repair is more sensible than a new structure."),
}
for c in ENSERV:
    if c["path"] in _LOCAL_COPY:
        c["local_h"], c["local_p"] = _LOCAL_COPY[c["path"]]
    c.setdefault("price_lead", "The final price depends on the dimensions, materials, site conditions and any gates or removal work. After a free measurement, we provide a clear project quote.")

_order = {path: index for index, path in enumerate(service_paths("en"))}
assert len(ENSERV) == 8, f"English service list must contain 8 pages, got {len(ENSERV)}"
assert_service_coverage("en", [c["path"] for c in ENSERV])
ENSERV.sort(key=lambda c: _order[c["path"]])

for c in ENSERV:
    write_service("en", c)
print("EN services done:", len(ENSERV))
