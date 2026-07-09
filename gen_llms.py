#!/usr/bin/env python3
# Generate llms.txt — a plain-text site summary for AI crawlers (ChatGPT, Perplexity, etc.),
# per the llmstxt.org convention. Built from build_pages so it never drifts from the real site.
import io
from build_pages import DOMAIN, PHONE, EMAIL, FB

svc = [
 ("Puitaiad / Деревянные заборы / Wooden fences", "/aiad/puitaed/", "/ru/uslugi/derevyannye-zabory/", "/en/services/wooden-fence/"),
 ("Metallaed, profiilplekk / Профнастил / Corrugated metal", "/aiad/metallaed/", "/ru/uslugi/profnastil/", "/en/services/metal-fence/"),
 ("Metall-lippaed / Штакетник / Steel picket", "/aiad/lippaed/", "/ru/uslugi/shtaketnik/", "/en/services/steel-picket/"),
 ("Võrkaed, 3D paneelaed / 3D-сетка / Mesh & 3D panel", "/aiad/vorkaed/", "/ru/uslugi/setka-3d/", "/en/services/mesh-fence/"),
 ("Väravad ja automaatika / Ворота и автоматика / Gates & automation", "/varavad/", "/ru/uslugi/vorota-kalitki/", "/en/services/gates-automation/"),
 ("Aia remont / Ремонт заборов / Fence repair", "/aia-remont/", "/ru/uslugi/remont-zaborov/", "/en/services/fence-repair/"),
]

L = []
L.append("# LuxAed")
L.append("")
L.append("> Aedade ja väravate tootmine ja paigaldus Tallinnas ja Harjumaal. "
         "Заборы, ворота и калитки под ключ в Таллинне и Харьюмаа. "
         "Fences, gates and wickets in Tallinn and Harju County, Estonia. "
         "Puit, profiilplekk, keevispaneel (3D), väravaautomaatika ja domofonid. "
         "Üle 15 aasta kogemust, tasuta mõõdistus, 100% soovitab (34 arvustust Facebookis).")
L.append("")
L.append("## Main pages")
L.append(f"- [Avaleht — Eesti (ET)]({DOMAIN}/)")
L.append(f"- [Главная — Русский (RU)]({DOMAIN}/ru/)")
L.append(f"- [Home — English (EN)]({DOMAIN}/en/)")
L.append(f"- [Meist / О компании / About]({DOMAIN}/meist/)")
L.append(f"- [KKK / Вопросы / FAQ]({DOMAIN}/kkk/)")
L.append("")
L.append("## Services")
for name, et, ru, en in svc:
    L.append(f"- {name}: [ET]({DOMAIN}{et}) · [RU]({DOMAIN}{ru}) · [EN]({DOMAIN}{en})")
L.append("")
L.append("## About")
L.append("- Master craftsman: Artur Mustafin, 15+ years building fences and gates.")
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
