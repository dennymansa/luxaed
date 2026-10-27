#!/usr/bin/env python3
# Generate llms.txt — a plain-text site summary for AI crawlers (ChatGPT, Perplexity, etc.),
# per the llmstxt.org convention. Built from build_pages so it never drifts from the real site.
import io
from build_pages import (DOMAIN, PHONE, EMAIL, FB, EXPERIENCE_YEARS,
                         RECOMMEND_PERCENT, REVIEW_COUNT)
from service_catalog import LANGS, SERVICE_MATRIX
from problem_content import PROBLEM_ROWS, GUIDE_ROWS, ARTICLE_ORDER, _CARD_COPY

L = []
L.append("# LuxAed")
L.append("")
L.append("> Aedade ja väravate tootmine ja paigaldus Tallinnas ja Harjumaal. "
         "Заборы, ворота и калитки под ключ в Таллинне и Харьюмаа. "
         "Fences, gates and pedestrian gates in Tallinn and Harju County, Estonia. "
         "Puit, rullvõrk, 2D/3D-keevisvõrk, metall-lipp, varbaed, profiilplekk, väravaautomaatika ja domofonid. "
         f"Üle {EXPERIENCE_YEARS} aasta kogemust, tasuta mõõdistus, "
         f"{RECOMMEND_PERCENT}% soovitab ({REVIEW_COUNT} arvustust Facebookis).")
L.append("")
L.append("## Main pages")
L.append(f"- [Avaleht — Eesti (ET)]({DOMAIN}/)")
L.append(f"- [Главная — Русский (RU)]({DOMAIN}/ru/)")
L.append(f"- [Home — English (EN)]({DOMAIN}/en/)")
L.append(f"- About / Meist / О компании: [ET]({DOMAIN}/meist/) · [RU]({DOMAIN}/ru/o-nas/) · [EN]({DOMAIN}/en/about/)")
L.append(f"- FAQ / KKK / Вопросы: [ET]({DOMAIN}/kkk/) · [RU]({DOMAIN}/ru/faq/) · [EN]({DOMAIN}/en/faq/)")
L.append(f"- Prices / Hinnad / Цены: [ET]({DOMAIN}/hinnad/) · [RU]({DOMAIN}/ru/ceny/) · [EN]({DOMAIN}/en/prices/)")
L.append(f"- Fence selection guide / Kuidas valida aeda / Как выбрать забор: [ET]({DOMAIN}/kuidas-valida-aeda/) · [RU]({DOMAIN}/ru/kak-vybrat-zabor/) · [EN]({DOMAIN}/en/how-to-choose-a-fence/)")
L.append(f"- Harju County service area / Teeninduspiirkond / Зона обслуживания: [ET]({DOMAIN}/piirkonnad/harjumaa/) · [RU]({DOMAIN}/ru/rajony/harjumaa/) · [EN]({DOMAIN}/en/areas/harju-county/)")
L.append("")
L.append("## Services")
for service in SERVICE_MATRIX:
    name = " / ".join(service[lang]["title"] for lang in LANGS)
    links = " · ".join(
        f"[{lang.upper()}]({DOMAIN}{service[lang]['path']})" for lang in LANGS
    )
    L.append(f"- {name}: {links}")
L.append("")
L.append("## Repair problems")
_problem_names = ["Gate won't open or close / Värav ei avane / Не открываются ворота",
                  "Sliding gate sticking or sagging / Liugvärava remont / Ремонт откатных ворот",
                  "Leaning fence or loose post / Viltu aed / Покосился забор",
                  "Fence damaged by a storm or car / Kahjustatud aed / Повреждённый забор"]
for _name, _row in zip(_problem_names, PROBLEM_ROWS):
    L.append(f"- {_name}: " + " · ".join(f"[{lang.upper()}]({DOMAIN}{_row[lang]})" for lang in ("et", "ru", "en")))
L.append("")
L.append("## Guides")
_guide_names = ["Fence permits and neighbours / Kas aia ehitamiseks on vaja luba / Разрешение на забор",
                "Sliding or swing gate / Liugvärav või tiibvärav / Откатные или распашные ворота",
                "All guides / Nõuanded / Советы"]
_guide_names += [" / ".join(_CARD_COPY[lang][key][0] for lang in ("en", "et", "ru")) for key in ARTICLE_ORDER]
assert len(_guide_names) == len(GUIDE_ROWS)
for _name, _row in zip(_guide_names, GUIDE_ROWS):
    L.append(f"- {_name}: " + " · ".join(f"[{lang.upper()}]({DOMAIN}{_row[lang]})" for lang in ("et", "ru", "en")))
L.append("")
L.append("## Service finder by customer need")
L.append("- Privacy fence / privaatne aed / забор для приватности: close-boarded timber, profiled sheet or a dense double-sided steel-picket layout. Use solid sections towards the street and open mesh elsewhere when appropriate.")
L.append("- Fence for dogs or children / koera- ja lastekindel aed / забор для собаки и детей: rigid 2D/3D welded panels are often practical; height, mesh size, bottom clearance, pedestrian-gate gaps and locks must suit the household.")
L.append("- Fence for a windy site / aed tuulisele krundile / забор для ветреного участка: roll mesh, welded panels and metal-bar fencing let air pass. Solid timber and profiled sheet need posts and foundations sized for exposure.")
L.append("- Fence for a slope / aed kaldega krundile / забор на склоне: roll mesh follows a gentle slope; rigid panels, timber and metal can follow the levels or be stepped after measurement.")
L.append("- Long affordable boundary / soodne aed pikale piirile / недорогой забор для длинной границы: roll mesh is usually the lowest-cost solution; 3D panels provide a more rigid line at a higher budget.")
L.append("- Low-maintenance modern frontage / vähese hooldusega moodne aed / современный забор без постоянной покраски: steel pickets, horizontal metal slats, coated welded panels, metal bars and profiled sheet.")
L.append("- Automatic gates for a fence / automaatväravad aiale / автоматические ворота для забора: LuxAed measures, manufactures and installs sliding or swing gates, drives, photocells and remote, phone, app, code or RFID control where supported.")
L.append("- Video intercom / videodomofon / видеодомофон: visitor calls, two-way talk, supported mobile access, PIN/RFID entry, event history and pedestrian-gate electric-lock release in one specified system.")
L.append("- Fence and gate repair / aia ja värava remont / ремонт забора и ворот: sections, posts, hinges, rollers, locks, foundations, controls, photocells and gate drives are inspected before repair or replacement is recommended.")
L.append("")
L.append("## About")
L.append(f"- LuxAed team: {EXPERIENCE_YEARS}+ years building fences and gates.")
L.append("- Turnkey: free on-site measurement, materials, installation, exact price up front, no hidden fees.")
L.append("- Works year-round across Tallinn and all of Harju County.")
L.append("- Core service area: Tallinn and Harju County; not a nationwide Estonia service.")
L.append("- Warranty: 24 months on installation and repair work, plus the manufacturer's warranty on materials and equipment. Automatic gates are handed over with the EC declaration of conformity, CE marking and instructions in Estonian. LuxAed also installs automatic barriers.")
L.append("")
L.append("## Direct answers")
L.append("- Indicative installed fence budgets: roll mesh 25–45 €/m, 3D panel 35–60 €/m, 2D panel 50–85 €/m, profiled sheet 70–135 €/m, timber 90–160 €/m, steel picket 85–155 €/m. These are provisional market ranges; the written quotation after measurement is authoritative.")
L.append("- Best privacy: close-boarded timber, profiled sheet, or dense/double-sided steel picket.")
L.append("- Best for exposed windy sites: open roll mesh, welded panels, or metal-bar fencing. Solid fences require stronger posts and foundations sized for wind load.")
L.append("- Noise: a normal timber or profiled-sheet fence may slightly reduce perceived road noise but is not a certified acoustic barrier.")
L.append("- Lowest-maintenance options: galvanised coated mesh panels, steel pickets, metal bars and profiled sheet. Timber needs periodic finish renewal.")
L.append("- Permit requirements vary by municipality, detailed plan, location and digging depth; check the local authority and Building Register before work.")
L.append("- Estonian Building Code, Annex 1 (in force since 01.08.2026): building a fence or gate that involves digging deeper than 30 cm requires a building notice and a building design (ehitusteatis ja ehitusprojekt); extending or demolishing it requires a building notice; reconstructing (altering) it or replacing a single part with an equivalent one requires neither; demolishing a fence to build a substantively new one counts as demolition plus new construction (§ 4(4)). A notice allows building for four years (§ 37), and a municipality may require a notice in justified cases even when Annex 1 does not (§ 35(4)). Law of Property Act § 151: a boundary structure between two plots is in the neighbours' joint use; if both use it, they share its maintenance costs equally.")
L.append("- There is no national maximum fence height in Estonia; height and transparency come from the detailed or general plan. In most Harju County plans checked on 27.09.2026 the limit for a house fence is 1.5 m (Kiili street side 1.4 m; Loo, Liivamäe and northern Saha 1.2 m); Saku, Keila and Maardu require at least 25% transparency.")
L.append("- A gate with an electric drive is a machine under the Equipment Safety Act and the Machinery Directive (Regulation (EU) 2023/1230 from 20.01.2027): the manufacturer, usually the installer when a gate and drive are assembled on site, provides the EC declaration of conformity, CE marking and instructions in Estonian; connecting a 230 V drive is not work a layperson may do.")
L.append("- Automatic gate won't open or close: check breakers, the remote battery, clean photocells, that the manual release is locked, and ice or debris in the gate's path; otherwise the drive, control board or mechanics need diagnosis. LuxAed repairs gates and automation in Tallinn and Harju County, including gates installed by others; repair and diagnostics from €90.")
L.append("- Sliding gate sticking or sagging: usually worn carriage rollers, loose carriages, a shifted top guide or a settled base; rollers and guides are normally replaced or adjusted on site.")
L.append("- Leaning fence: mostly frost heave, wind load on solid fences, or posts rotted or rusted at ground level; single posts can be straightened, re-concreted or replaced.")
L.append("- Fence hit by a car in Estonia: a known vehicle's compulsory motor insurance (liikluskindlustus) normally covers the damage; if the vehicle is unidentified, the Estonian Traffic Insurance Fund (LKF) can be contacted. LuxAed provides a written repair quote after inspection.")
L.append("- Automatic gate installation: sliding gates save space in front of the entrance; swing gates are often simpler where there is enough room for the leaves. The drive is selected for gate weight, width, usage and wind exposure, with photocells, emergency release and suitable controls.")
L.append("- Indicative automatic-gate budgets: an installed sliding gate with automation is about €2,100–3,000; automation fitted to a suitable existing gate is about €500–1,250. The exact written quotation follows measurement and a structural check.")
L.append("- Intercoms: LuxAed installs audio and video intercoms, outdoor panels, indoor monitors, supported mobile access, PIN/RFID entry and electric pedestrian-gate locks in Tallinn and Harju County. A standard system releases the lock; motorised physical opening needs a separate drive and safety design.")
L.append("- Supported video-intercom systems can send call or event alerts to a phone, show live video, support two-way talk, release the electric lock, and provide snapshots, clips or call history. Recording, motion detection, storage and multi-user access depend on the selected model, network and storage. The camera should be aimed mainly at the owner's entrance and must not record a neighbour's property; continuous audio is not configured as video surveillance.")
L.append("- Indicative video-intercom budget for one pedestrian gate: about €650–1,600 for equipment, electric lock and standard installation. Cabling, power, monitors, mobile support and gate alterations affect the final quotation.")
L.append("")
L.append("## Contact")
L.append(f"- Phone: {PHONE}")
L.append(f"- Email: {EMAIL}")
L.append(f"- Facebook: {FB}")
L.append("- Area: Tallinn, Harjumaa, Estonia")
L.append("- Hours: Mon–Fri 09:00–18:00, Sat by appointment")
L.append("")

io.open("llms.txt", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("llms.txt written")
