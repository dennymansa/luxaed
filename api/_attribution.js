// How a visitor came to the site, in plain Russian for the lead email.
// The browser part (assets/lead-form.js) sends `attribution`: first visit, this visit, the
// last 15 pages with times, language, screen. Files starting with "_" in api/ are helpers,
// not endpoints, on Vercel.

const UTM = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
const CLICK = ['gclid', 'gbraid', 'wbraid', 'fbclid', 'msclkid'];
const TZ = 'Europe/Tallinn';

const str = (v, max = 300) => (typeof v === 'string' ? v.trim().slice(0, max) : '');
const num = v => (typeof v === 'number' && Number.isFinite(v) && v > 0 ? Math.round(v) : undefined);

function cleanTouch(r) {
  if (!r || typeof r !== 'object') return undefined;
  const t = { ts: num(r.ts), landing: str(r.landing || r.landing_page, 500), referrer: str(r.referrer, 500) };
  for (const k of [...UTM, ...CLICK]) { const v = str(r[k], 200); if (v) t[k] = v; }
  return t;
}

/** Whitelist + trim. Accepts the new shape and the old flat one (landing_page, referrer, utm_*). */
export function cleanAttribution(raw) {
  if (!raw || typeof raw !== 'object') return {};
  const legacy = !raw.first && !raw.session ? cleanTouch(raw) : undefined;
  const journey = Array.isArray(raw.journey)
    ? raw.journey.slice(-15).map(j => (j && typeof j === 'object' ? { p: str(j.p, 200), t: num(j.t) || 0 } : null)).filter(j => j && j.p)
    : [];
  return {
    first: cleanTouch(raw.first) || legacy,
    session: cleanTouch(raw.session),
    journey,
    now: num(raw.now),
    lang: str(raw.lang, 20),
    langs: str(raw.langs, 60),
    screen: str(raw.screen, 20),
    tz: str(raw.tz, 60),
  };
}

const ICON = { ai: '🤖', ads: '💰', search: '🔎', social: '👥', utm: '🏷️', referral: '🔗', direct: '⌨️' };
const NOTE = {
  ai: 'ИИ-ассистент посоветовал сайт',
  ads: 'платная реклама',
  search: 'бесплатный поиск (SEO)',
  social: 'соцсети',
  utm: 'ссылка с меткой UTM',
  referral: 'переход по ссылке с другого сайта',
  direct: 'ввёл адрес, закладка или ссылка из мессенджера',
};
export const kindNote = k => NOTE[k] || '';
const src = (label, kind, why) => ({ label, kind, icon: ICON[kind], why });

const hostOf = u => { try { return new URL(u).hostname.toLowerCase().replace(/^www\./, ''); } catch { return ''; } };

const AI = [[/chatgpt|openai/, 'ChatGPT'], [/perplexity/, 'Perplexity'], [/gemini|bard/, 'Gemini'], [/copilot/, 'Copilot'], [/claude|anthropic/, 'Claude'], [/deepseek/, 'DeepSeek'], [/grok/, 'Grok']];
const AI_HOSTS = [
  [/(^|\.)chatgpt\.com$|(^|\.)openai\.com$/, 'ChatGPT'],
  [/(^|\.)perplexity\.ai$/, 'Perplexity'],
  [/^(gemini|bard)\.google\.com$/, 'Gemini'],
  [/^copilot\.microsoft\.com$|^edgeservices\.bing\.com$|(^|\.)copilot\.cloud\.microsoft$/, 'Copilot'],
  [/(^|\.)claude\.ai$/, 'Claude'],
  [/(^|\.)deepseek\.com$/, 'DeepSeek'],
  [/(^|\.)grok\.com$/, 'Grok'],
];
const PAID = /^(cpc|ppc|paid|paidsearch|paid_search|paid-social|paid_social|paidsocial|cpm|display|ads?)$/;

export function classifyTouch(t, ownHosts = []) {
  if (!t) return src('Нет данных', 'direct', 'браузер не прислал данные');
  const s = (t.utm_source || '').toLowerCase();
  const m = (t.utm_medium || '').toLowerCase();
  if (t.gclid || t.gbraid || t.wbraid) return src('Google Ads', 'ads', `в ссылке есть ${t.gclid ? 'gclid' : t.gbraid ? 'gbraid' : 'wbraid'}`);
  if (t.msclkid) return src('Microsoft Ads (Bing)', 'ads', 'в ссылке есть msclkid');
  if (s) {
    const why = `utm_source=${t.utm_source}${m ? `, utm_medium=${t.utm_medium}` : ''}`;
    for (const [re, name] of AI) if (re.test(s)) return src(name, 'ai', `utm_source=${t.utm_source}`);
    if (/google/.test(s)) return PAID.test(m) ? src('Google Ads', 'ads', why) : src('Google (метка UTM)', 'utm', why);
    if (/facebook|^fb$|instagram|^ig$|meta/.test(s)) return src(PAID.test(m) ? 'Facebook / Instagram (реклама)' : 'Facebook / Instagram', 'social', why);
    if (/bing/.test(s)) return PAID.test(m) ? src('Microsoft Ads (Bing)', 'ads', why) : src('Bing', 'search', why);
    if (/yandex/.test(s)) return src('Yandex', PAID.test(m) ? 'ads' : 'search', why);
    return src(`Метка UTM: ${t.utm_source}`, PAID.test(m) ? 'ads' : 'utm', why);
  }
  if (t.fbclid) return src('Facebook / Instagram', 'social', 'в ссылке есть fbclid');
  const ref = t.referrer || '';
  const h = hostOf(ref) || (/^android-app:\/\/com\.google/.test(ref) ? 'google.com' : '');
  if (h && !ownHosts.some(own => h === own || h.endsWith('.' + own))) {
    for (const [re, name] of AI_HOSTS) if (re.test(h)) return src(name, 'ai', `реферер ${h}`);
    if (/(^|\.)google\.[a-z.]+$/.test(h)) return src('Google поиск', 'search', `реферер ${h}`);
    if (/(^|\.)bing\.com$/.test(h)) return src('Bing поиск', 'search', `реферер ${h}`);
    if (/(^|\.)(facebook\.com|fb\.com|instagram\.com|messenger\.com)$/.test(h)) return src('Facebook / Instagram', 'social', `реферер ${h}`);
    if (/(^|\.)yandex\.[a-z.]+$|(^|\.)ya\.ru$/.test(h)) return src('Yandex', 'search', `реферер ${h}`);
    if (/(^|\.)duckduckgo\.com$/.test(h)) return src('DuckDuckGo', 'search', `реферер ${h}`);
    return src(`Другой сайт: ${h}`, 'referral', `реферер ${h}`);
  }
  return src('Прямой заход', 'direct', ref ? 'реферер — сам сайт' : 'реферера нет');
}

export function deviceFromUA(u = '') {
  const kind = /iPad|Tablet|PlayBook|Silk|(Android(?!.*Mobile))/i.test(u) ? 'планшет' : /Mobi|iPhone|iPod|Android|Windows Phone/i.test(u) ? 'телефон' : 'компьютер';
  const os = /iPhone|iPad|iPod/.test(u) ? (/iPad/.test(u) ? 'iPad' : 'iPhone') : /Android/.test(u) ? 'Android' : /Windows/.test(u) ? 'Windows' : /Mac OS X|Macintosh/.test(u) ? 'Mac' : /Linux/.test(u) ? 'Linux' : '';
  const app = /FBAN|FBAV|FB_IAB/.test(u) ? 'в приложении Facebook' : /Instagram/.test(u) ? 'в приложении Instagram' : /Telegram/i.test(u) ? 'в Telegram' : '';
  const br = /Edg\//.test(u) ? 'Edge' : /SamsungBrowser/.test(u) ? 'Samsung Internet' : /OPR\/|Opera/.test(u) ? 'Opera' : /Firefox|FxiOS/.test(u) ? 'Firefox' : /CriOS|Chrome\//.test(u) ? 'Chrome' : /Safari/.test(u) ? 'Safari' : '';
  return { kind, detail: [os, app || br].filter(Boolean).join(', ') };
}

export const fmtTime = (ts, withDate = false) =>
  new Intl.DateTimeFormat('ru-RU', { timeZone: TZ, hour: '2-digit', minute: '2-digit', ...(withDate ? { day: '2-digit', month: '2-digit', year: 'numeric' } : { second: '2-digit' }) }).format(ts);

export function fmtDuration(ms) {
  const s = Math.max(0, Math.round(ms / 1000));
  if (s < 60) return `${s} с`;
  const m = Math.floor(s / 60);
  if (m < 60) return `${m} мин ${s % 60} с`;
  const h = Math.floor(m / 60);
  if (h < 48) return `${h} ч ${m % 60} мин`;
  return `${Math.floor(h / 24)} дн.`;
}

const pathOf = u => { try { const x = new URL(u); return x.pathname + (x.search.length > 1 ? x.search : ''); } catch { return u; } };

/** { source, sessionSource, rows: [label, value][], journey: [{time, path, after}] } */
export function describeAttribution(raw, ua, ownHosts, serverNow = Date.now()) {
  const a = cleanAttribution(raw);
  const first = a.first || a.session;
  const source = classifyTouch(first, ownHosts);
  const sess = a.session ? classifyTouch(a.session, ownHosts) : undefined;
  const sessionSource = sess && a.first && a.session && a.first.ts !== a.session.ts && sess.label !== source.label ? sess : undefined;
  const t = first || {};
  const utm = UTM.filter(k => t[k]).map(k => `${k.replace('utm_', '')}: ${t[k]}`).join(' · ');
  const click = CLICK.filter(k => t[k]).map(k => `${k}=${String(t[k]).slice(0, 40)}${String(t[k]).length > 40 ? '…' : ''}`).join(' · ');
  const now = a.now || serverNow;
  const onSite = a.session && a.session.ts ? fmtDuration(now - a.session.ts) : '';
  const firstAgo = a.first && a.first.ts && a.session && a.session.ts && a.session.ts - a.first.ts > 30 * 60000 ? `${fmtTime(a.first.ts, true)} (${fmtDuration(now - a.first.ts)} назад)` : '';
  const dev = deviceFromUA(ua);
  const journey = (a.journey || []).map((j, i, all) => ({
    time: j.t ? fmtTime(j.t) : '',
    path: j.p,
    after: i > 0 && j.t && all[i - 1].t ? `+${fmtDuration(j.t - all[i - 1].t)}` : '',
  }));
  const rows = [
    ['Страница входа', t.landing ? pathOf(t.landing) : ''],
    ['Реферер', t.referrer || 'нет (прямой заход)'],
    ['UTM', utm],
    ['Click ID', click],
    ['Первый визит', firstAgo],
    ['Этот визит', sessionSource ? `${sessionSource.icon} ${sessionSource.label} (${sessionSource.why})` : ''],
    ['На сайте', onSite ? `${onSite} в этот визит${journey.length ? `, страниц: ${journey.length}` : ''}` : ''],
    ['Устройство', [dev.kind, dev.detail, a.screen ? `экран ${a.screen}` : ''].filter(Boolean).join(', ')],
    ['Язык браузера', [a.langs || a.lang, a.tz && a.tz !== TZ ? `часовой пояс ${a.tz}` : ''].filter(Boolean).join(' · ')],
  ].filter(([, v]) => v);
  return { source, sessionSource, rows, journey };
}

const escH = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

/**
 * Email HTML for the attribution block, themed by the caller.
 * theme: { accent, soft, line, ink, muted, rowLine }
 */
export function attributionHtml(view, th) {
  const rows = view.rows.map(([k, v], i) => {
    const bd = i < view.rows.length - 1 ? `border-bottom:1px solid ${th.rowLine}` : '';
    return `<tr><td style="padding:8px 12px 8px 0;color:${th.muted};font-size:13px;width:130px;vertical-align:top;${bd}">${escH(k)}</td><td style="padding:8px 0;color:${th.ink};font-size:14px;font-weight:600;word-break:break-word;${bd}">${escH(v)}</td></tr>`;
  }).join('');
  const journey = view.journey.length
    ? `<div style="margin-top:12px;color:${th.muted};font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.05em">Путь по сайту</div>
       <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:4px">${view.journey.map((j, i) =>
         `<tr><td style="padding:5px 10px 5px 0;color:${th.muted};font-size:12px;font-family:ui-monospace,Menlo,Consolas,monospace;width:64px;vertical-align:top">${escH(j.time)}</td><td style="padding:5px 0;color:${th.ink};font-size:13px;word-break:break-all">${i + 1}. ${escH(j.path)}</td><td style="padding:5px 0 5px 8px;color:${th.muted};font-size:12px;text-align:right;white-space:nowrap;vertical-align:top">${escH(j.after)}</td></tr>`).join('')}</table>`
    : '';
  return `<div style="color:${th.accent};font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px">📍 Откуда пришёл</div>
    <div style="background:${th.soft};border:1px solid ${th.line};border-radius:14px;padding:14px 16px;margin-bottom:8px">
      <div style="font-size:24px;font-weight:800;color:${th.ink};line-height:1.2">${view.source.icon} ${escH(view.source.label)}</div>
      <div style="font-size:13px;color:${th.muted};margin-top:4px">${escH(kindNote(view.source.kind))} · определено: ${escH(view.source.why)}</div>
    </div>
    ${rows ? `<table role="presentation" width="100%" cellpadding="0" cellspacing="0">${rows}</table>` : ''}${journey}`;
}

export function attributionText(view) {
  return [
    `ОТКУДА ПРИШЁЛ: ${view.source.label} — ${kindNote(view.source.kind)} (${view.source.why})`,
    ...view.rows.map(([k, v]) => `${k}: ${v}`),
    view.journey.length ? 'Путь по сайту:\n' + view.journey.map((j, i) => `  ${j.time}  ${i + 1}. ${j.path} ${j.after}`.trimEnd()).join('\n') : '',
  ].filter(Boolean).join('\n');
}
