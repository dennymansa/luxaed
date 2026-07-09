// LuxAed lead handler — Vercel serverless (Node). Sends the site form to the owner's
// inbox via Gmail SMTP + App Password, as a polished HTML email with the client's
// details + Google Maps / Waze links to the site address.
//
// ENV (Vercel → Project → Settings → Environment Variables):
//   GMAIL_USER          — the Gmail that SENDS (e.g. operationsatljc@gmail.com)
//   GMAIL_APP_PASSWORD  — 16-char App Password from Google Account → Security → App passwords
//                         (needs 2-Step Verification on). NOT the normal Gmail password.
//   LEAD_TO             — recipient inbox (default iamdenisg@gmail.com for testing).
// Without GMAIL_USER/APP_PASSWORD the form still succeeds (email is just skipped).

import nodemailer from 'nodemailer';

function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}

// smart-form chip codes → readable label + "needs …" headline
const SVC  = { aed:'Забор', varav:'Ворота / калитка', automaatika:'Автоматика', remont:'Ремонт' };
const NEED = { aed:'Забор ннада?', varav:'Ворота ннада?', automaatika:'Автоматика ннада?', remont:'Ремонт ннада?' };

export default async function handler(req, res){
  if(req.method!=='POST'){ res.status(405).json({error:'Method not allowed'}); return; }
  try{
    const d = (req.body && typeof req.body==='object') ? req.body : JSON.parse(req.body||'{}');
    if(d._gotcha){ res.status(200).json({ok:true}); return; }              // honeypot → silently ok

    const USER = process.env.GMAIL_USER;
    const PASS = process.env.GMAIL_APP_PASSWORD;
    const TO   = process.env.LEAD_TO || USER || 'iamdenisg@gmail.com';
    const AC = '#b5542e';   // brand terracotta

    const f = k => (d[k]==null ? '' : String(d[k]).trim());
    const name = f('name'), phone = f('phone'), email = f('email');
    const addr = f('address');
    const enc  = encodeURIComponent(addr);
    const gmaps = addr ? `https://www.google.com/maps/search/?api=1&query=${enc}` : '';
    const waze  = addr ? `https://waze.com/ul?q=${enc}&navigate=yes` : '';
    const sc    = f('service');
    const svc   = SVC[sc] || sc;
    const need  = NEED[sc] || (svc ? ('Заявка: '+svc) : 'Новая заявка');
    const msg   = f('msg');
    const page  = f('page');

    // detail rows (name/phone/email/address/comment shown separately)
    const fields = [
      ['Материал', f('material')], ['Длина, м', f('length')], ['Высота', f('height')],
      ['Тип ворот', f('gate_type')], ['Автоматика', f('automation')],
      ['Участок', f('plot')], ['Когда', f('timeline')],
    ].filter(([,v])=>v);

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
          Перезвони типу пояснить, кто здесь папа.
        </td></tr>
      </table></body></html>`;

    if(!USER || !PASS){ res.status(200).json({ok:true, note:'GMAIL_USER/APP_PASSWORD not set — email skipped (form flow still works)'}); return; }

    const transport = nodemailer.createTransport({
      host:'smtp.gmail.com', port:465, secure:true,
      auth:{ user:USER, pass:PASS }
    });
    await transport.sendMail({
      from: `LuxAed <${USER}>`,
      to: TO,
      replyTo: email || undefined,
      subject: `${need} — ${name || 'заявка с сайта'}`,
      html
    });
    res.status(200).json({ok:true});
  }catch(e){ res.status(500).json({error:'send_failed'})}); }
}
