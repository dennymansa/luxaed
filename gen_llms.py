#!/usr/bin/env python3
# Generate llms.txt — a plain-text site summary for AI crawlers (ChatGPT, Perplexity, etc.),
# per the llmstxt.org convention. Built from build_pages so it never drifts from the real site.
import io
from build_pages import (DOMAIN, PHONE, EMAIL, FB, EXPERIENCE_YEARS,
                         RECOMMEND_PERCENT, REVIEW_COUNT)
from service_catalog import LANGS, SERVICE_MATRIX

L = []
L.append("# LuxAed")
L.append("")
L.append("> Aedade ja väravate tootmine ja paigaldus Tallinnas ja Harjumaal. "
         "Заборы, ворота и калитки под ключ в Таллинне и Харьюмаа. "
         "Fences, gates and wickets in Tallinn and Harju County, Estonia. "
         "Puit, rullvõrk, 2D/3D-keevisvõrk, metall-lipp, varbaed, profiilplekk ja väravaautomaatika. "
         f"Üle {EXPERIENCE_YEARS} aasta kogemust, tasuta mõõdistus, "
         f"{RECOMMEND_PERCENT}% soovitab ({REVIEW_COUNT} arvustust Facebookis).")
L.append("")
L.append("## Main pages")
L.append(f"- [Avaleht — Eesti (ET)]({DOMAIN}/)")
L.append(f"- [Главная — Русский (RU)]({DOMAIN}/ru/)")
L.append(f"- [Home — English (EN)]({DOMAIN}/en/)")
L.append(f"- [Meist / О компании / About]({DOMAIN}/meist/)")
L.append(f"- [KKK / Вопросы / FAQ]({DOMAIN}/kkk/)")
L.append("")
L.append("## Services")
for service in SERVICE_MATRIX:
    name = " / ".join(service[lang]["title"] for lang in LANGS)
    links = " · ".join(
        f"[{lang.upper()}]({DOMAIN}{service[lang]['path']})" for lang in LANGS
    )
    L.append(f"- {name}: {links}")
L.append("")
L.append("## About")
L.append(f"- LuxAed team: {EXPERIENCE_YEARS}+ years building fences and gates.")
L.append("- Turnkey: free on-site measurement, materials, installation, exact price up front, no hidden fees.")
L.append("- Works year-round across Tallinn and all of Harju County.")
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
