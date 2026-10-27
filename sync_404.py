#!/usr/bin/env python3
"""Keep the hand-built 404 page on the shared LuxAed tracking container."""

import io
import re

import build_pages


PATH = "404.html"
html = io.open(PATH, encoding="utf-8").read()
original = html

html = re.sub(
    r'\s*<!-- LUX_TRACKING_START -->.*?<!-- LUX_TRACKING_END -->\s*',
    '\n',
    html,
    flags=re.DOTALL,
)
html = re.sub(
    r'\s*<!-- LUX_GTM_NOSCRIPT_START -->.*?<!-- LUX_GTM_NOSCRIPT_END -->\s*',
    '\n',
    html,
    flags=re.DOTALL,
)

tracking_head = build_pages.tracking_head()
if tracking_head:
    html, count = re.subn(
        r'(<meta name="viewport"[^>]*>\s*)',
        lambda match: match.group(1) + tracking_head + '\n',
        html,
        count=1,
    )
    if count != 1:
        raise SystemExit("sync_404: viewport anchor not found")

tracking_body = build_pages.tracking_body()
if tracking_body:
    html, count = re.subn(
        r'(<body[^>]*>\s*)',
        lambda match: match.group(1) + tracking_body + '\n',
        html,
        count=1,
    )
    if count != 1:
        raise SystemExit("sync_404: body anchor not found")

if 'id="lux-css"' not in html and 'href="/assets/luxaed.css' not in html:
    html, count = re.subn(
        r'(<link rel="apple-touch-icon"[^>]*>\s*)',
        lambda match: match.group(1) + '<link rel="stylesheet" href="/assets/luxaed.css">\n',
        html,
        count=1,
    )
    if count != 1:
        raise SystemExit("sync_404: stylesheet anchor not found")

html = re.sub(
    r'\s*<!-- LUX_404_COOKIE_START -->.*?<!-- LUX_404_COOKIE_END -->\s*',
    '\n',
    html,
    flags=re.DOTALL,
)
cookie_block = '''<!-- LUX_404_COOKIE_START -->
<a class="cookie-settings-404" id="cookieSettings404" href="#cc" data-cookie-settings>Küpsiste seaded</a>
__COOKIE_BANNER__
__SHARED_SCRIPTS__
<script>
(function(){
  var lang=(location.pathname||"").indexOf("/ru/")===0?"ru":((location.pathname||"").indexOf("/en/")===0?"en":"et");
  var t={
    et:{aria:"Küpsiste nõusolek",title:"Küpsised",text:'Kasutame küpsiseid analüütika ja reklaami mõõtmiseks. <a href="/privaatsus/">Loe lähemalt</a>',cats:[["Vajalikud","Vormi, turvalisuse ja nõusolekuvaliku jaoks. Alati aktiivne."],["Analüütika","Aitab Google Analyticsi kaudu mõista veebisaidi kasutamist."],["Reklaami mõõtmine","Google Adsi kampaaniate ja konversioonide mõõtmiseks. Isikupärastatud reklaami ei lubata."]],buttons:["Ainult vajalikud","Seaded","Nõustun kõigega","Salvesta valik"],settings:"Küpsiste seaded"},
    ru:{aria:"Согласие на cookie",title:"Cookie",text:'Мы используем cookie для аналитики и измерения рекламы. <a href="/ru/privaatsus/">Подробнее</a>',cats:[["Необходимые","Для формы, безопасности и сохранения выбора. Всегда активны."],["Аналитика","Помогает понять использование сайта через Google Analytics."],["Измерение рекламы","Для измерения кампаний и конверсий Google Ads. Персонализация рекламы не включается."]],buttons:["Отклонить","Настроить","Принять все","Сохранить выбор"],settings:"Настройки cookie"},
    en:{aria:"Cookie consent",title:"Cookies",text:'We use cookies for analytics and advertising measurement. <a href="/en/privacy/">Learn more</a>',cats:[["Necessary","For the form, security and saving your choice. Always active."],["Analytics","Helps us understand website use through Google Analytics."],["Advertising measurement","For measuring Google Ads campaigns and conversions. Ad personalisation is not enabled."]],buttons:["Necessary only","Settings","Accept all","Save selection"],settings:"Cookie settings"}
  }[lang],cc=document.getElementById("cc");
  if(!cc)return;
  cc.setAttribute("aria-label",t.aria);
  cc.querySelector(".cc-title").textContent=t.title;
  cc.querySelector(".cc-txt").innerHTML=t.text;
  cc.querySelectorAll(".cc-cat").forEach(function(row,i){row.querySelector("b").textContent=t.cats[i][0];row.querySelector("i").textContent=t.cats[i][1];});
  cc.querySelector(".cc-dec").textContent=t.buttons[0];
  cc.querySelector(".cc-cust").textContent=t.buttons[1];
  cc.querySelector(".cc-acc").textContent=t.buttons[2];
  cc.querySelector(".cc-save").textContent=t.buttons[3];
  document.getElementById("cookieSettings404").textContent=t.settings;
})();
</script>
<!-- LUX_404_COOKIE_END -->'''.replace(
    "__COOKIE_BANNER__", build_pages.cookie_banner("et")
).replace(
    "__SHARED_SCRIPTS__", build_pages.SCRIPTS
)
html, count = re.subn(
    r'(</body>)',
    lambda match: cookie_block + '\n' + match.group(1),
    html,
    count=1,
)
if count != 1:
    raise SystemExit("sync_404: body end anchor not found")

if html != original:
    io.open(PATH, "w", encoding="utf-8").write(html)
    print("sync_404: updated tracking")
else:
    print("sync_404: already in sync")
