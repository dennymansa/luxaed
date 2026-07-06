// LuxAed lead handler — Vercel serverless (Node). Sends the site form to the owner's
// inbox via Gmail SMTP + App Password. Email carries a company label + Google Maps /
// Waze links to the client's address.
//
// ENV (Vercel → Project → Settings → Environment Variables):
//   GMAIL_USER          — the Gmail that SENDS (e.g. luxaed9@gmail.com)
//   GMAIL_APP_PASSWORD  — 16-char App Password from Google Account → Security → App passwords
//                         (needs 2-Step Verification on). NOT the normal Gmail password.
//   LEAD_TO             — recipient inbox (default iamdenisg@gmail.com for testing;
//                         later set to luxaed9@gmail.com). If unset, sends to GMAIL_USER.
// Without GMAIL_USER/APP_PASSWORD the form still succeeds (email is just skipped).

import nodemailer from 'nodemailer';

function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}

export default async function handler(req, res){
  if(req.method!=='POST'){ res.status(405).json({error:'Method not allowed'}); return; }
  try{
    const d = (req.body && typeof req.body==='object') ? req.body : JSON.parse(req.body||'{}');
    if(d._gotcha){ res.status(200).json({ok:true}); return; }              // honeypot → silently ok

    const USER = process.env.GMAIL_USER;
    const PASS = process.env.GMAIL_APP_PASSWORD;
    const TO   = process.env.LEAD_TO || USER || 'iamdenisg@gmail.com';
    const LABEL = 'Заявка с сайта LuxAed';

    const f = k => (d[k]==null ? '' : String(d[k]).trim());
    const addr = f('address');
    const enc  = encodeURIComponent(addr);
    const gmaps = addr ? `https://www.google.com/maps/search/?api=1&query=${enc}` : '';
    const waze  = addr ? `https://waze.com/ul?q=${enc}&navigate=yes` : '';

    const fields = [
      ['Услуга', f('service')], ['Материал', f('material')], ['Длина, м', f('length')],
      ['Высота', f('height')], ['Тип ворот', f('gate_type')], ['Автоматика', f('automation')],
      ['Участок', f('plot')], ['Когда', f('timeline')], ['Адрес', addr],
      ['Имя', f('name')], ['Телефон', f('phone')], ['Email', f('email')], ['Комментарий', f('msg')],
    ].filter(([,v])=>v);

    const rows = fields.map(([k,v])=>
      `<tr><td style="padding:7px 14px;color:#5a4a40;white-space:nowrap;border-bottom:1px solid #efe6dd">${esc(k)}</td>`+
      `<td style="padding:7px 14px;font-weight:600;color:#201812;border-bottom:1px solid #efe6dd">${esc(v)}</td></tr>`).join('');

    const maps = addr ? `<p style="margin:16px 0 4px">📍 <b>${esc(addr)}</b></p>`+
      `<p style="margin:0"><a href="${gmaps}" style="display:inline-block;background:#1a73e8;color:#fff;text-decoration:none;padding:9px 16px;border-radius:8px;margin-right:8px">Google Maps →</a>`+
      `<a href="${waze}" style="display:inline-block;background:#33ccff;color:#062a3a;text-decoration:none;padding:9px 16px;border-radius:8px">Waze →</a></p>` : '';

    const html = `<div style="font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;max-width:580px;color:#201812">
      <h2 style="color:#b5542e;margin:0 0 2px">🌿 ${LABEL}</h2>
      <p style="color:#5a4a40;margin:0 0 16px">Новая заявка с формы luxaed.ee</p>
      <table style="border-collapse:collapse;width:100%;border:1px solid #e7ddd3;border-radius:10px;overflow:hidden">${rows}</table>
      ${maps}
      ${f('phone')?`<p style="margin:16px 0 0"><a href="tel:${esc(f('phone'))}">📞 Позвонить клиенту</a></p>`:''}
    </div>`;

    if(!USER || !PASS){ res.status(200).json({ok:true, note:'GMAIL_USER/APP_PASSWORD not set — email skipped (form flow still works)'}); return; }

    const transport = nodemailer.createTransport({
      host:'smtp.gmail.com', port:465, secure:true,
      auth:{ user:USER, pass:PASS }
    });
    await transport.sendMail({
      from: `LuxAed <${USER}>`,
      to: TO,
      replyTo: f('email') || undefined,
      subject: `${LABEL} — ${f('name') || f('service') || 'без имени'}`,
      html
    });
    res.status(200).json({ok:true});
  }catch(e){ res.status(500).json({error:String(e && e.message || e)}); }
}
