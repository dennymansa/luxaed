// LuxAed lead handler — Vercel serverless (Node). Sends the site form to the owner's
// inbox via Gmail SMTP + App Password, as a polished HTML email with the client's
// details + Google Maps / Waze links to the site address. It then sends the
// customer a confirmation from the same Gmail sender: a recap of what they
// submitted plus a short factual checklist, in the language of the page.
//
// ENV (Vercel → Project → Settings → Environment Variables):
//   GMAIL_USER          — the Gmail that SENDS (e.g. operationsatljc@gmail.com)
//   GMAIL_APP_PASSWORD  — 16-char App Password from Google Account → Security → App passwords
//                         (needs 2-Step Verification on). NOT the normal Gmail password.
//   LEAD_TO             — recipient inbox (default iamdenisg@gmail.com for testing).
// Without GMAIL_USER/APP_PASSWORD the endpoint returns 503 so the site never
// shows a false success or records a conversion for an undelivered lead.

import nodemailer from 'nodemailer';

function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}

// smart-form chip codes → readable label + "needs …" headline
const SVC  = { aed:'Забор', varav:'Въездные ворота', jalgvarav:'Калитка', automaatika:'Автоматика', intercom:'Домофон / видеодомофон', remont:'Ремонт' };
const NEED = {
  aed:'Новая заявка: забор',
  varav:'Новая заявка: въездные ворота',
  jalgvarav:'Новая заявка: калитка',
  automaatika:'Новая заявка: автоматика',
  intercom:'Новая заявка: домофон / видеодомофон',
  remont:'Новая заявка: ремонт'
};
// Public LuxAed contacts, mirrored from build_pages.py (PHONE / TEL / EMAIL).
const PHONE = '+372 5695 8285';
const TEL = '+37256958285';
const CONTACT_EMAIL = 'luxaed9@gmail.com';

// ---------------------------------------------------------------------------
// Customer confirmation email ("your request was received" + a short factual
// checklist). Sent from the same Gmail sender as the owner notification, right
// after the owner mail succeeds. A failure here is logged and swallowed: the
// lead itself is already delivered and must still count as a success.
// ---------------------------------------------------------------------------
const LANGS = ['et', 'ru', 'en'];
const SVC_L10N = {
  et: { aed:'Aed', varav:'Väravad', jalgvarav:'Jalgvärav', automaatika:'Automaatika', intercom:'Domofon', remont:'Remont' },
  ru: { aed:'Забор', varav:'Ворота', jalgvarav:'Калитка', automaatika:'Автоматика', intercom:'Домофон', remont:'Ремонт' },
  en: { aed:'Fence', varav:'Gates', jalgvarav:'Pedestrian gate', automaatika:'Automation', intercom:'Intercom', remont:'Repair' }
};

const CUSTOMER_COPY = {
  et: {
    subject: 'Aitäh päringu eest | LuxAed',
    kicker: 'Päring on vastu võetud',
    greeting: n => (n ? `Tere, ${n}!` : 'Tere!'),
    intro: 'Aitäh, et pöördusite LuxAedi poole. Teie päring on meieni jõudnud. Võtame teiega peatselt ühendust, täpsustame üksikasjad ja lepime kokku tasuta mõõdistuse.',
    summaryTitle: 'Teie päring',
    mapLink: 'Ava Google Mapsis',
    home: 'https://luxaed.ee/',
    rows: { service:'Teenus', material:'Aia tüüp', length:'Aia pikkus', gate:'Värava tüüp', address:'Aadress', comment:'Kommentaar', photos:'Fotod' },
    guideTitle: 'Kuni ootate kõnet: millele tasub mõelda',
    blocks: {
      fence: { title: 'Aed', items: [
        ['Postide sügavus', 'Harjumaal külmub pinnas umbes meetri sügavuseni. Sellest kõrgemale betoonitud post surutakse kahe või kolme talvega üles ja aed vajub viltu. Seetõttu lähevad postid külmumissügavusest allapoole.'],
        ['Kinnine või piludega', 'Kinnine aed lõuna pool annab pideva varju umbes oma kõrguse laiuselt. Sinna, kus on muru või peenrad, sobib pigem piludega aed ja kinnine jääb tänava poole.'],
        ['Tuul', 'Kinnine aiapind töötab nagu puri. Kahe meetri kõrgusel kasvab koormus postidele mitmekordseks, seega tehakse postisamm tihedam ja vundament sügavam. 20–30% pilu võtab suure osa koormusest maha.'],
        ['Lumi', 'Kinnise aia taha tuiskab talvel vall. Kui see jääb sissesõidu peale, tuleb väravat lahti kaevata. Sektsioonide paigutusel arvestame sellega.'],
        ['Esikülg', 'Enamikul aedadel on esikülg ja tagakülg. Otsustage ette, kummale poole esikülg vaatab, tänavale või õue: sellest sõltub, kummale poole talad kinnituvad.'],
        ['Piir ja trassid', 'Aed püstitatakse oma maale, täpselt piiri peale on vaja naabri nõusolekut. Piiri ääres jooksevad sageli kaabel, vesi või drenaaž, seepärast kontrollime trassid enne puurimist üle.']
      ]},
      gates: { title: 'Väravad ja automaatika', items: [
        ['Liug või tiib', 'Liugväraval on vaja aia ääres vaba käiku umbes poolteist korda avast laiemalt. Kui sellist ruumi ei ole, paigaldatakse tiibvärav.'],
        ['Kummale poole avaneb', 'Sissepoole avanev tiibvärav vajab tasast platsi ja jääb talvel lume taha kinni. Väljapoole ei tohi avaneda, kui tiib ulatub kõnniteele või sõiduteele.'],
        ['Elekter', 'Automaatika vajab värava juures 230 V. Kaabel on odavam paigaldada enne, kui õu on valmis ja kivi laotud.'],
        ['Elektrikatkestus', 'Ajamil on käsivabastus. Eraldi tasub otsustada, kas soovite akuvaru, et vooluta välja sõita.'],
        ['Ohutus', 'Fotosilmad on vajalikud, kui õues on lapsed või loomad: tiib peatub, kui avas on midagi ees.'],
        ['Eraldi jalgvärav', 'Ajami ressurss käib avamistsüklites. Kui iga päev jalgsi läbi suure värava käia, kulub ajam kiiremini, seega tasub jalgvärav kõrvale ära.']
      ]},
      intercom: { title: 'Domofon', items: [
        ['Paneeli kõrgus', 'Kutsepaneel on mugav panna auto akna kõrgusele, et vihmaga välja astuma ei peaks.'],
        ['Kes avab', 'Mõelge ette, kellel on ligipääsu vaja: pere, kuller, külaline, koristaja. Sellest sõltub, kas piisab koodist või on vaja RFID-võtit ja rakendust.'],
        ['Kaamera', 'Kaamera vaatab teie enda sissepääsu. Naabri krunti see filmima ei pea, see on paigaldusele eraldi nõue.']
      ]}
    },
    contact: 'Kui soovite midagi lisada või muuta, vastake sellele kirjale või helistage.',
    footer: 'Kiri saadeti automaatselt luxaed.ee vormi põhjal.'
  },
  ru: {
    subject: 'Спасибо за заявку | LuxAed',
    kicker: 'Заявка принята',
    greeting: n => (n ? `Здравствуйте, ${n}!` : 'Здравствуйте!'),
    intro: 'Спасибо, что обратились в LuxAed. Ваша заявка у нас. Мы свяжемся с вами в ближайшее время, уточним детали и договоримся о бесплатном замере.',
    summaryTitle: 'Ваша заявка',
    mapLink: 'Открыть в Google Maps',
    home: 'https://luxaed.ee/ru/',
    rows: { service:'Услуга', material:'Тип забора', length:'Длина забора', gate:'Тип ворот', address:'Адрес', comment:'Комментарий', photos:'Фото' },
    guideTitle: 'Пока ждёте звонка: о чём стоит подумать',
    blocks: {
      fence: { title: 'Забор', items: [
        ['Глубина столбов', 'В Харьюмаа грунт промерзает примерно на метр. Столб, забетонированный выше этой отметки, за две-три зимы выдавливает морозным пучением, и забор ведёт. Поэтому опоры уходят ниже глубины промерзания.'],
        ['Глухой или с просветами', 'Глухое полотно с южной стороны кладёт сплошную тень полосой примерно в свою высоту. Там, где газон или посадки, обычно берут забор с просветами, а глухой оставляют со стороны улицы.'],
        ['Ветер', 'Глухой забор работает как парус. На высоте 2 м нагрузка на опоры вырастает в разы, поэтому шаг столбов уменьшают, а бетонирование делают глубже. Просветы в 20–30% снимают заметную часть нагрузки.'],
        ['Снег', 'За глухим забором зимой наметает вал. Если он ложится на въезд, ворота придётся откапывать. Это учитывается при расстановке секций.'],
        ['Лицевая сторона', 'У большинства заборов есть лицевая сторона и изнанка. Решите заранее, куда смотрит лицо, на улицу или во двор: от этого зависит, с какой стороны крепятся лаги.'],
        ['Граница и коммуникации', 'Забор ставится на своей земле, а ровно по меже нужна договорённость с соседом. Вдоль границы часто идут кабель, вода или дренаж, поэтому до бурения мы проверяем трассы.']
      ]},
      gates: { title: 'Ворота и автоматика', items: [
        ['Откатные или распашные', 'Откатным нужен свободный ход вдоль забора примерно в полтора раза шире проёма. Если такого места нет, ставят распашные.'],
        ['Куда открывать', 'Распашные внутрь требуют ровной площадки и зимой упираются в снег. Наружу нельзя, если створка выходит на тротуар или проезжую часть.'],
        ['Электричество', 'Автоматике нужно 230 В у ворот. Кабель дешевле проложить до того, как сделан двор и уложена брусчатка.'],
        ['Отключение света', 'У привода есть ручная разблокировка. Отдельно стоит решить, нужен ли аккумулятор, чтобы выехать, когда электричества нет.'],
        ['Безопасность', 'Фотоэлементы нужны, если во дворе дети или животные: створка останавливается, когда в проёме что-то есть.'],
        ['Отдельная калитка', 'Ресурс привода считается в циклах открывания. Если каждый день ходить пешком через большие ворота, привод изнашивается быстрее, поэтому калитка рядом обычно окупается.']
      ]},
      intercom: { title: 'Домофон', items: [
        ['Высота панели', 'Вызывную панель удобно ставить на уровне окна автомобиля, чтобы не выходить в дождь.'],
        ['Кто открывает', 'Прикиньте заранее, кому нужен доступ: семья, курьер, гость, уборка. От этого зависит, хватит ли кода или нужны RFID-ключ и приложение.'],
        ['Камера', 'Камера смотрит на ваш собственный вход. Снимать участок соседа она не должна, это отдельное требование к установке.']
      ]}
    },
    contact: 'Если нужно что-то добавить или изменить, ответьте на это письмо или позвоните.',
    footer: 'Письмо отправлено автоматически по заявке с сайта luxaed.ee.'
  },
  en: {
    subject: 'Thank you for your enquiry | LuxAed',
    kicker: 'Enquiry received',
    greeting: n => (n ? `Hello, ${n}!` : 'Hello!'),
    intro: 'Thank you for contacting LuxAed. We have your enquiry. We will get in touch shortly to go through the details and arrange a free site measurement.',
    summaryTitle: 'Your enquiry',
    mapLink: 'Open in Google Maps',
    home: 'https://luxaed.ee/en/',
    rows: { service:'Service', material:'Fence type', length:'Fence length', gate:'Gate type', address:'Address', comment:'Comment', photos:'Photos' },
    guideTitle: 'While you wait for our call: what is worth thinking about',
    blocks: {
      fence: { title: 'Fence', items: [
        ['Post depth', 'In Harju county the ground freezes to roughly one metre. A post concreted above that line is pushed up by frost heave within two or three winters and the fence goes crooked. That is why the posts go below the frost line.'],
        ['Solid or with gaps', 'A solid fence on the south side casts a continuous shadow about as wide as it is tall. Where there is lawn or planting, a fence with gaps usually works better and the solid run stays on the street side.'],
        ['Wind', 'A solid panel works like a sail. At two metres the load on the posts grows several times over, so the posts go closer together and the footings deeper. Gaps of 20–30% take a noticeable part of that load away.'],
        ['Snow', 'A drift builds up behind a solid fence in winter. If it lands on the driveway, the gate has to be dug out. We take that into account when setting out the sections.'],
        ['Front face', 'Most fences have a front and a back. Decide in advance which way the front looks, to the street or into the yard, because that determines which side the rails are fixed to.'],
        ['Boundary and utilities', 'A fence goes on your own land, and a fence right on the boundary line needs the neighbour to agree. Cable, water or drainage often runs along the boundary, so we check the routes before drilling.']
      ]},
      gates: { title: 'Gates and automation', items: [
        ['Sliding or swing', 'A sliding gate needs a clear run along the fence about one and a half times the width of the opening. Where there is no such room, swing gates are used.'],
        ['Which way it opens', 'A swing gate opening inwards needs level ground and jams against snow in winter. It must not open outwards if the leaf reaches the pavement or the road.'],
        ['Power', 'Automation needs 230 V at the gate. The cable is cheaper to lay before the yard is finished and the paving is down.'],
        ['Power cuts', 'Every drive has a manual release. Whether you also want a battery backup, so you can drive out with no mains power, is a separate decision.'],
        ['Safety', 'Photocells are needed if there are children or animals in the yard: the leaf stops when something is in the opening.'],
        ['A separate pedestrian gate', 'Drive life is counted in opening cycles. Walking through the main gate every day wears the drive out faster, so a pedestrian gate next to it usually pays for itself.']
      ]},
      intercom: { title: 'Intercom', items: [
        ['Panel height', 'The call panel is best placed at car window height so you do not have to step out in the rain.'],
        ['Who opens it', 'Think in advance about who needs access: family, couriers, guests, a cleaner. That decides whether a code is enough or you need an RFID key and an app.'],
        ['Camera', 'The camera looks at your own entrance. It should not film the neighbour’s plot, which is a separate requirement for the installation.']
      ]}
    },
    contact: 'To add or change anything, reply to this email or call us.',
    footer: 'This email was sent automatically for your request from luxaed.ee.'
  }
};

function pickLang(rawLang, pageUrl){
  const raw = String(rawLang || '').slice(0, 5).toLowerCase();
  if (LANGS.includes(raw)) return raw;
  let path = String(pageUrl || '');
  try { path = new URL(path).pathname; } catch { /* not an absolute URL, match on the raw string */ }
  if (/(^|\/)ru(\/|$)/.test(path)) return 'ru';
  if (/(^|\/)en(\/|$)/.test(path)) return 'en';
  return 'et';
}

// Palette shared with the site: warm near-black ink, terracotta accent, sand paper.
const M = {
  ink:'#1c1512', body:'#6d6058', soft:'#9b8d83', brand:'#b5542e', brandLite:'#e08a5f',
  hair:'#efe6dd', panel:'#faf6f3', badge:'#f7e8de', page:'#f0e9e3'
};

// Static map of the site address, fetched server-side and attached by CID so the
// API key never travels inside the email and the picture survives image blocking.
// Without GOOGLE_MAPS_KEY the email simply falls back to the address + a maps link.
export async function staticMapPng(addr){
  const key = process.env.GOOGLE_MAPS_KEY;
  if (!key || !addr) return null;
  const q = encodeURIComponent(addr);
  const url = 'https://maps.googleapis.com/maps/api/staticmap?size=560x210&scale=2&zoom=15'
    + '&maptype=roadmap&center=' + q + '&markers=' + encodeURIComponent('color:0xb5542e|') + q
    + '&key=' + encodeURIComponent(key);
  try {
    const r = await fetch(url, { signal: AbortSignal.timeout(6000) });
    if (!r.ok) return null;
    const buf = Buffer.from(await r.arrayBuffer());
    // Google answers errors with a PNG-shaped error tile or plain text; require a real PNG.
    if (buf.length < 2000 || buf[0] !== 0x89 || buf[1] !== 0x50 || buf[2] !== 0x4e || buf[3] !== 0x47) return null;
    return buf;
  } catch { return null; }
}

export function customerEmail(lang, ctx){
  const C = CUSTOMER_COPY[lang];
  const rows = [
    [C.rows.service, ctx.services], [C.rows.material, ctx.material], [C.rows.length, ctx.length],
    [C.rows.gate, ctx.gateType], [C.rows.comment, ctx.msg],
    [C.rows.photos, ctx.photoCount ? String(ctx.photoCount) : '']
  ].filter(([, v]) => v);

  // Compact two-column rows: label left, value right, hairline between.
  const rowsHtml = rows.map(([k, v], i) => {
    const bd = i < rows.length - 1 ? `border-bottom:1px solid ${M.hair}` : '';
    return `<tr>`
      + `<td valign="top" style="padding:8px 12px 8px 0;${bd};color:${M.soft};font-size:12px;line-height:1.45;white-space:nowrap">${esc(k)}</td>`
      + `<td valign="top" align="right" style="padding:8px 0;${bd};color:${M.ink};font-size:13.5px;font-weight:600;line-height:1.45;text-align:right">${esc(v)}</td>`
      + `</tr>`;
  }).join('');

  const mapHtml = ctx.addr ? `<tr><td style="padding:14px 34px 0">
      <div style="border:1px solid ${M.hair};border-radius:14px;overflow:hidden">
        ${ctx.mapCid ? `<img src="cid:${esc(ctx.mapCid)}" width="532" alt="" style="display:block;width:100%;max-width:532px;height:auto;border:0">` : ''}
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
          <td style="padding:13px 16px;background:${M.panel}">
            <div style="color:${M.soft};font-size:11px;font-weight:700;letter-spacing:.09em;text-transform:uppercase">${esc(C.rows.address)}</div>
            <div style="color:${M.ink};font-size:14.5px;font-weight:600;line-height:1.4;margin-top:3px">${esc(ctx.addr)}</div>
            ${ctx.mapsUrl ? `<a href="${esc(ctx.mapsUrl)}" style="display:inline-block;color:${M.brand};font-size:13px;font-weight:700;margin-top:8px">${esc(C.mapLink)} &rarr;</a>` : ''}
          </td></tr></table>
      </div></td></tr>` : '';

  const blocks = ctx.blockKeys.map(key => C.blocks[key]).filter(Boolean);
  const blocksHtml = blocks.map((b, bi) => {
    const items = b.items.map(([t, body], i) =>
      `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 ${i === b.items.length - 1 ? '0' : '18px'}"><tr>`
      + `<td width="30" valign="top" style="width:30px;padding:1px 14px 0 0">`
      + `<table role="presentation" cellpadding="0" cellspacing="0"><tr><td width="28" height="28" align="center" valign="middle" style="width:28px;height:28px;background:${M.badge};border-radius:14px;color:${M.brand};font-size:12px;font-weight:800;font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif">${i + 1}</td></tr></table>`
      + `</td>`
      + `<td valign="top">`
      + `<div style="color:${M.ink};font-size:15px;font-weight:700;line-height:1.4">${esc(t)}</div>`
      + `<div style="color:${M.body};font-size:14.5px;line-height:1.62;margin-top:4px">${esc(body)}</div>`
      + `</td></tr></table>`
    ).join('');
    return `<div style="margin:0 0 ${bi === blocks.length - 1 ? '4' : '30'}px">`
      + `<div style="color:${M.brand};font-size:11px;font-weight:800;letter-spacing:.11em;text-transform:uppercase">${esc(b.title)}</div>`
      + `<div style="height:1px;background:${M.hair};margin:11px 0 18px;font-size:0;line-height:0">&nbsp;</div>`
      + items + `</div>`;
  }).join('');

  const html = `<!doctype html><html lang="${esc(lang)}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light only"><meta name="supported-color-schemes" content="light"><style>:root{color-scheme:light only;supported-color-schemes:light}body{margin:0}a{text-decoration:none}</style></head>
    <body style="margin:0;background:${M.page};padding:30px 12px;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color-scheme:light only">
    <table role="presentation" width="600" cellpadding="0" cellspacing="0" align="center" style="max-width:600px;width:100%;margin:0 auto;background:#ffffff;border-radius:18px;overflow:hidden;box-shadow:0 10px 34px rgba(45,25,12,.10)">
      <tr><td style="background:${M.ink};padding:28px 34px 26px">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
          <td valign="middle"><div style="font-size:25px;font-weight:800;letter-spacing:-.6px;color:#ffffff;line-height:1">Lux<span style="color:${M.brandLite}">Aed</span></div></td>
          <td valign="middle" align="right" style="text-align:right"><a href="${esc(C.home)}" style="color:#9c8b7f;font-size:12.5px;font-weight:600;white-space:nowrap">luxaed.ee</a></td>
        </tr></table>
        <div style="width:38px;height:3px;background:${M.brand};border-radius:3px;margin-top:13px;font-size:0;line-height:0">&nbsp;</div>
        <div style="color:#a3948a;font-size:11.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;margin-top:13px">${esc(C.kicker)}</div>
      </td></tr>

      <tr><td style="padding:34px 34px 0">
        <div style="color:${M.ink};font-size:25px;font-weight:800;line-height:1.2;letter-spacing:-.4px">${esc(C.greeting(ctx.name))}</div>
        <p style="margin:13px 0 0;color:${M.body};font-size:15.5px;line-height:1.62">${esc(C.intro)}</p>
      </td></tr>

      ${rowsHtml ? `<tr><td style="padding:24px 34px 0">
        <div style="background:${M.panel};border:1px solid ${M.hair};border-radius:14px;padding:6px 18px 12px">
          <div style="color:${M.soft};font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;padding:12px 0 6px">${esc(C.summaryTitle)}</div>
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0">${rowsHtml}</table>
        </div></td></tr>` : ''}
      ${mapHtml}

      ${blocksHtml ? `<tr><td style="padding:34px 34px 0">
        <div style="color:${M.ink};font-size:18px;font-weight:800;line-height:1.3;letter-spacing:-.2px;margin:0 0 24px">${esc(C.guideTitle)}</div>
        ${blocksHtml}</td></tr>` : ''}

      <tr><td style="padding:32px 34px 0">
        <div style="height:1px;background:${M.hair};font-size:0;line-height:0">&nbsp;</div>
      </td></tr>
      <tr><td style="padding:24px 34px 30px">
        <div style="color:${M.body};font-size:14.5px;line-height:1.6;margin:0 0 16px">${esc(C.contact)}</div>
        <a href="tel:${esc(TEL)}" style="display:inline-block;background:${M.brand};color:#ffffff;font-size:14.5px;font-weight:700;padding:13px 22px;border-radius:11px;margin:0 10px 10px 0">${esc(PHONE)}</a>
        <a href="mailto:${esc(CONTACT_EMAIL)}" style="display:inline-block;background:#ffffff;color:${M.brand};border:1.5px solid #ecd0bd;font-size:14.5px;font-weight:700;padding:11.5px 20px;border-radius:11px;margin:0 0 10px 0">${esc(CONTACT_EMAIL)}</a>
      </td></tr>

      <tr><td style="background:${M.panel};padding:16px 34px;border-top:1px solid ${M.hair}">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
          <td valign="middle"><div style="color:${M.soft};font-size:11.5px;line-height:1.5">${esc(C.footer)}</div></td>
          <td valign="middle" align="right" style="text-align:right;padding-left:14px"><a href="${esc(C.home)}" style="color:${M.brand};font-size:12.5px;font-weight:700;white-space:nowrap">luxaed.ee &rarr;</a></td>
        </tr></table>
        ${ctx.submissionId ? `<div style="color:#d3c6bb;font-size:9px;text-align:right;margin-top:6px">${esc(ctx.submissionId)}</div>` : ''}
      </td></tr>
    </table></body></html>`;

  const text = [
    C.greeting(ctx.name), '', C.intro, '',
    rows.length ? C.summaryTitle + '\n' + rows.map(([k, v]) => '  ' + k + ': ' + v).join('\n') : '',
    ctx.addr ? C.rows.address + ': ' + ctx.addr + (ctx.mapsUrl ? '\n' + ctx.mapsUrl : '') : '',
    blocks.length ? C.guideTitle + '\n\n' + blocks.map(b =>
      b.title.toUpperCase() + '\n' + b.items.map(([t, body], i) => '  ' + (i + 1) + '. ' + t + '. ' + body).join('\n')
    ).join('\n\n') : '',
    C.contact, PHONE + '  ·  ' + CONTACT_EMAIL + '  ·  ' + C.home, '', C.footer
  ].filter(x => x !== '').join('\n\n');

  return { subject: C.subject, html, text };
}
const RATE_WINDOW = 10*60*1000;
const RATE_LIMIT = 8;
const rateStore = globalThis.__luxaedLeadRate || (globalThis.__luxaedLeadRate = new Map());
const dedupeStore = globalThis.__luxaedLeadDedupe || (globalThis.__luxaedLeadDedupe = new Map());

function tooMany(req){
  const raw = String(req.headers?.['x-forwarded-for'] || req.headers?.['x-real-ip'] || '').split(',')[0].trim();
  if(!raw) return false;
  const now = Date.now();
  const recent = (rateStore.get(raw) || []).filter(ts=>now-ts<RATE_WINDOW);
  recent.push(now); rateStore.set(raw,recent);
  if(rateStore.size>1000){ for(const [ip,hits] of rateStore){ if(!hits.some(ts=>now-ts<RATE_WINDOW)) rateStore.delete(ip); } }
  return recent.length>RATE_LIMIT;
}

export default async function handler(req, res){
  if(req.method!=='POST'){ res.status(405).json({error:'Method not allowed'}); return; }
  let submissionId = '';
  try{
    const d = (req.body && typeof req.body==='object') ? req.body : JSON.parse(req.body||'{}');
    if(d._gotcha){ res.status(200).json({ok:true}); return; }              // honeypot → silently ok
    if(tooMany(req)){ res.status(429).json({error:'rate_limited'}); return; }

    const USER = process.env.GMAIL_USER;
    const PASS = process.env.GMAIL_APP_PASSWORD;
    const _to = process.env.LEAD_TO || USER || 'iamdenisg@gmail.com';
    const owner = process.env.VERCEL_ENV==='production' ? ['luxaed9@gmail.com'] : [];
    const TO   = [..._to.split(','), ...owner].map(x=>x.trim()).filter((x,i,a)=>x && a.indexOf(x)===i).join(',');
    const AC = '#b5542e';   // brand terracotta

    const f = (k,max=1200) => (d[k]==null ? '' : String(d[k]).trim().slice(0,max));
    const name = f('name',100), phone = f('phone',40), email = f('email',160);
    const phoneDigits = phone.replace(/\D/g,'');
    const addr = f('address',200);
    const isV2 = f('form_version',10)==='2';
    submissionId = f('submission_id',80).replace(/[^A-Za-z0-9_-]/g,'');
    const serviceCodes = f('services',100).split(',').map(x=>x.trim()).filter((x,i,a)=>SVC[x] && a.indexOf(x)===i);
    const primaryService = f('service',40);
    if(!serviceCodes.length && SVC[primaryService]) serviceCodes.push(primaryService);
    const validEmail = /^[^\s@]{1,80}@[^\s@]{1,120}\.[^\s@]{2,30}$/.test(email);
    const invalidV2 = !submissionId || !serviceCodes.length || !name || phoneDigits.length < 7 || phoneDigits.length > 15 || !validEmail;
    // Every public form is V2 now. Service, name, phone and email are mandatory:
    // the email address is where the customer confirmation goes. Address, photos
    // and the comment stay optional to keep the mobile form short.
    if(!isV2 || invalidV2){
      res.status(400).json({error:'required_fields'});
      return;
    }
    const enc  = encodeURIComponent(addr);
    const gmaps = addr ? `https://www.google.com/maps/search/?api=1&query=${enc}` : '';
    const waze  = addr ? `https://waze.com/ul?q=${enc}&navigate=yes` : '';
    const sc    = primaryService;
    const serviceLabels = serviceCodes.map(code=>SVC[code]);
    const svc   = serviceLabels.join(' + ') || SVC[sc] || sc;
    const need  = serviceLabels.length > 1 ? ('Новая заявка: '+svc) : (NEED[sc] || (svc ? ('Заявка: '+svc) : 'Новая заявка'));
    const msg   = f('msg',1200);
    const page  = f('page',500);
    const lang  = pickLang(f('lang',5), page);
    const requestContextCode = f('request_context',40);
    const requestContext = SVC[requestContextCode] || requestContextCode;

    // detail rows (name/phone/email/address/comment shown separately)
    const fields = [
      ['Что нужно', svc], ['Контекст страницы', requestContext], ['Материал', f('material',120)], ['Примерная длина', f('length',80)], ['Высота', f('height',80)],
      ['Тип ворот', f('gate_type',80)], ['Автоматика', f('automation',80)],
      ['Участок', f('plot',120)], ['Когда', f('timeline',120)],
    ].filter(([,v])=>v);

    const attr = d.attribution && typeof d.attribution==='object' ? d.attribution : {};
    const af = k => (attr[k]==null ? '' : String(attr[k]).trim().slice(0,500));
    const attributionFields = [
      ['Источник', [af('utm_source'),af('utm_medium')].filter(Boolean).join(' / ')],
      ['Кампания', af('utm_campaign')], ['Ключ / объявление', [af('utm_term'),af('utm_content')].filter(Boolean).join(' / ')],
      ['Google click ID', af('gclid') || af('gbraid') || af('wbraid')], ['Первый вход', af('landing_page')], ['Реферер', af('referrer')]
    ].filter(([,v])=>v);
    fields.push(...attributionFields);

    const rows = fields.map(([k,v],i)=>{
      const bd = i<fields.length-1 ? 'border-bottom:1px solid #f0e7de' : '';
      return `<tr><td style="padding:9px 0;color:#8a7a6c;font-size:13px;width:130px;vertical-align:top;${bd}">${esc(k)}</td>`+
             `<td style="padding:9px 0;color:#201812;font-size:14px;font-weight:600;${bd}">${esc(v)}</td></tr>`;
    }).join('');

    const btn = (href,bg,fg,extra,txt)=>`<a href="${href}" style="display:inline-block;background:${bg};color:${fg};font-size:13px;font-weight:700;text-decoration:none;padding:10px 16px;border-radius:10px;margin:0 8px 8px 0;${extra}">${txt}</a>`;

    const contactBtns =
      (phone?btn('tel:'+esc(phone),AC,'#ffffff','','📞&nbsp;'+esc(phone)):'')+
      (email?btn('mailto:'+esc(email),'#ffffff',AC,'border:1.5px solid #e6bda9','✉&nbsp;'+esc(email)):'');

    const addrBlock = addr ? `<tr><td style="padding:2px 26px 8px">
        <div style="background:#faf5f1;border:1px solid #f0e2d8;border-radius:12px;padding:14px 16px">
          <div style="color:#201812;font-size:15px;font-weight:700">📍 ${esc(addr)}</div>
          <div style="margin-top:10px">${btn(gmaps,'#1a73e8','#ffffff','','🗺 Google Maps →')}${btn(waze,'#33ccff','#062a3a','','Waze →')}</div>
        </div></td></tr>` : '';

    const msgBlock = msg ? `<tr><td style="padding:2px 26px 10px">
        <div style="background:#fff7f2;border-left:4px solid ${AC};border-radius:0 12px 12px 0;padding:13px 16px">
          <div style="color:${AC};font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin-bottom:5px">💬 Комментарий клиента</div>
          <div style="color:#201812;font-size:15px;line-height:1.55">${esc(msg)}</div>
        </div></td></tr>` : '';

    const rowsBlock = rows ? `<tr><td style="padding:4px 26px 14px">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0">${rows}</table></td></tr>` : '';

    const html = `<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light only"><meta name="supported-color-schemes" content="light"><style>:root{color-scheme:light only;supported-color-schemes:light}body{margin:0}</style></head>
      <body style="margin:0;background:#f1e8e1;padding:26px 10px;font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;color-scheme:light only">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" align="center" style="max-width:600px;width:100%;margin:0 auto;background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 6px 28px rgba(40,20,10,.12)">
        <tr><td style="background:linear-gradient(135deg,${AC},#9a4526);padding:20px 26px">
          <div style="font-size:23px;font-weight:800;letter-spacing:-.5px;color:#ffffff">Lux<span style="color:#f4cdb6">Aed</span></div>
          <div style="color:#f3d9cc;font-size:13px;margin-top:2px">Новая заявка с сайта luxaed.ee</div>
        </td></tr>
        <tr><td style="padding:18px 26px 2px">
          <div style="display:inline-block;background:#f7e7dd;color:${AC};font-size:13px;font-weight:800;padding:6px 14px;border-radius:20px">🔔 ${esc(need)}</div>
        </td></tr>
        <tr><td style="padding:12px 26px 4px">
          <div style="font-size:22px;font-weight:800;color:#201812">${esc(name)||'Без имени'}</div>
          <div style="margin-top:11px">${contactBtns||'<span style="color:#8a7a6c;font-size:13px">контакты не указаны</span>'}</div>
        </td></tr>
        ${addrBlock}
        ${rowsBlock}
        ${msgBlock}
        <tr><td style="background:#faf7f4;padding:13px 26px;color:#9a8c80;font-size:12px;border-top:1px solid #f0e7de">
          ${page?`Со страницы: ${esc(page)}<br>`:''}
          Заявка отправлена через форму на сайте LuxAed.
        </td></tr>
      </table></body></html>`;

    // Never report a successful lead (and therefore an Ads conversion) when
    // delivery is not configured. The browser will show its normal retry/call
    // fallback for this 503 response.
    if(!USER || !PASS){ res.status(503).json({error:'mail_not_configured'}); return; }

    const transport = nodemailer.createTransport({
      host:'smtp.gmail.com', port:465, secure:true,
      auth:{ user:USER, pass:PASS }, connectionTimeout:10000, greetingTimeout:10000, socketTimeout:15000
    });
    // photo attachments: client downsizes to <=1600px JPEG and sends base64 (like the
    // PHP $_FILES + addAttachment flow, adapted to a JSON serverless function)
    const attachments = [];
    if(Array.isArray(d.photos_b64)){
      let total = 0;
      for(const p of d.photos_b64.slice(0,4)){
        if(!p || typeof p.data !== 'string' || p.data.length > 950000 || !/^[A-Za-z0-9+/]+={0,2}$/.test(p.data)) continue;
        const buf = Buffer.from(p.data, 'base64');
        // Canvas-generated uploads must be a complete JPEG, not just data with a
        // forged three-byte header. The client always emits the standard SOI/EOI pair.
        if(buf.length < 128 || buf[0]!==0xff || buf[1]!==0xd8 || buf[2]!==0xff || buf.at(-2)!==0xff || buf.at(-1)!==0xd9) continue;
        total += buf.length; if(total > 3.5*1024*1024) break;   // stay under the 4.5MB fn limit
        const base = String(p.name||'photo.jpg').replace(/\.[^.]*$/,'').replace(/[^\w\-]+/g,'_').slice(0,70) || 'photo';
        attachments.push({ filename: base+'.jpg', content: buf, contentType:'image/jpeg' });
      }
    }
    const photosExpected = Math.max(0,Math.min(4,Number.parseInt(f('photos_expected',2),10)||0));
    if(isV2 && photosExpected!==attachments.length){ res.status(400).json({error:'invalid_photos'}); return; }
    const mail = {
      from: `LuxAed <${USER}>`,
      to: TO,
      replyTo: email,
      messageId: `<${submissionId}@luxaed.ee>`,
      subject: `${need} — ${name || 'заявка с сайта'}`,
      html: html.replace('</table>', (attachments.length?`<tr><td style="padding:10px 26px;background:#eef4ff;color:#1d4ed8;font-size:13px;font-weight:600">&#128206; Фото во вложении: ${attachments.length} шт.</td></tr>`:'')+'</table>'),
      attachments
    };
    // Share the in-flight SMTP promise inside one warm serverless instance. A
    // parallel retry now waits for the original result instead of reporting a
    // false success while the original delivery may still fail.
    while(true){
      const now = Date.now();
      const existing = dedupeStore.get(submissionId);
      if(existing && now-existing.ts<30*60*1000){
        if(existing.status==='sent'){ res.status(200).json({ok:true,duplicate:true}); return; }
        try{
          await existing.promise;
          res.status(200).json({ok:true,duplicate:true});
          return;
        }catch{
          if(dedupeStore.get(submissionId)===existing) dedupeStore.delete(submissionId);
          continue;
        }
      }
      if(existing) dedupeStore.delete(submissionId);
      if(dedupeStore.size>1000){
        for(const [id,entry] of dedupeStore){ if(now-entry.ts>=30*60*1000) dedupeStore.delete(id); }
      }
      const promise = transport.sendMail(mail);
      const entry = {ts:now,status:'pending',promise};
      dedupeStore.set(submissionId,entry);
      try{
        await promise;
        if(dedupeStore.get(submissionId)===entry) dedupeStore.set(submissionId,{ts:Date.now(),status:'sent'});
        break;
      }catch(err){
        if(dedupeStore.get(submissionId)===entry) dedupeStore.delete(submissionId);
        throw err;
      }
    }
    // Owner mail is delivered at this point. The confirmation to the customer is
    // best-effort: a failure here must not turn a delivered lead into an error.
    try{
      // The whole checklist goes in every confirmation, not just the sections that
      // match the services ticked on the form: a customer asking about a fence still
      // has to think about the gate and the intercom before we call.
      const blockKeys = ['fence', 'gates', 'intercom'];
      const mapPng = await staticMapPng(addr);
      const mapCid = mapPng ? 'luxaed-site-map' : '';
      const confirmation = customerEmail(lang, {
        name, addr, msg, submissionId, blockKeys, mapCid, mapsUrl: gmaps,
        services: serviceCodes.map(c=>SVC_L10N[lang][c]).filter(Boolean).join(' + '),
        material: f('material',120), length: f('length',80), gateType: f('gate_type',80),
        photoCount: attachments.length
      });
      await transport.sendMail({
        from: `LuxAed <${USER}>`,
        to: email,
        replyTo: CONTACT_EMAIL,
        messageId: `<${submissionId}-customer@luxaed.ee>`,
        subject: confirmation.subject,
        text: confirmation.text,
        html: confirmation.html,
        attachments: mapPng ? [{filename:'map.png', content:mapPng, cid:mapCid, contentType:'image/png'}] : []
      });
    }catch(err){
      console.error('LuxAed customer confirmation failed:', err && err.message ? err.message : 'unknown error');
    }
    res.status(200).json({ok:true});
  }catch(e){
    console.error('LuxAed lead send failed:', e && e.message ? e.message : 'unknown error');
    res.status(500).json({error:'send_failed'});
  }
}
