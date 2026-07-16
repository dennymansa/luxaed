// LuxAed lead handler — Vercel serverless (Node). Sends the site form to the owner's
// inbox via Gmail SMTP + App Password, as a polished HTML email with the client's
// details + Google Maps / Waze links to the site address.
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
const SVC  = { aed:'Забор', varav:'Въездные ворота', jalgvarav:'Калитка', automaatika:'Автоматика', remont:'Ремонт' };
const NEED = { aed:'Забор ннада?', varav:'Ворота ннада?', jalgvarav:'Калитка ннада?', automaatika:'Автоматика ннада?', remont:'Ремонт ннада?' };
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
    const invalidV2 = !submissionId || !serviceCodes.length || !name || phoneDigits.length < 7 || phoneDigits.length > 15 || !validEmail || !addr;
    // Every public form is V2 now. Keeping the old permissive branch would let a
    // direct POST omit the service, email and address even though the UI requires them.
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
          <div style="color:#f3d9cc;font-size:13px;margin-top:2px">Работаем, Артурик, работаем!</div>
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
          Перезвони типу, скажи папа едет ставить забор!
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
      replyTo: email || undefined,
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
    res.status(200).json({ok:true});
  }catch(e){
    console.error('LuxAed lead send failed:', e && e.message ? e.message : 'unknown error');
    res.status(500).json({error:'send_failed'});
  }
}
