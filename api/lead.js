// LuxAed lead handler — Vercel serverless (Node 18+, zero deps: global fetch).
// Receives the site form as JSON, emails the owner with a company label + Google
// Maps / Waze links to the client's address. Sends via Resend (RESEND_API_KEY).
//
// ENV (set in Vercel → Project → Settings → Environment Variables):
//   RESEND_API_KEY  — from resend.com (required to actually send; without it the form
//                     still succeeds, email is just skipped so you can test the flow)
//   LEAD_TO         — recipient (default iamdenisg@gmail.com; change to luxaed9@gmail.com later)
//   LEAD_FROM       — sender (default "LuxAed <onboarding@resend.dev>"; use a verified
//                     luxaed.ee sender once the domain is verified in Resend)

function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}

export default async function handler(req, res){
  if(req.method!=='POST'){ res.status(405).json({error:'Method not allowed'}); return; }
  try{
    const d = (req.body && typeof req.body==='object') ? req.body : JSON.parse(req.body||'{}');
    if(d._gotcha){ res.status(200).json({ok:true}); return; }          // honeypot → silently ok

    const TO   = process.env.LEAD_TO   || 'iamdenisg@gmail.com';
    const FROM = process.env.LEAD_FROM || 'LuxAed <onboarding@resend.dev>';
    const KEY  = process.env.RESEND_API_KEY;
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

    if(!KEY){ res.status(200).json({ok:true, note:'RESEND_API_KEY not set — email skipped (form flow still works)'}); return; }

    const r = await fetch('https://api.resend.com/emails',{
      method:'POST',
      headers:{'Authorization':`Bearer ${KEY}`,'Content-Type':'application/json'},
      body: JSON.stringify({
        from: FROM, to: [TO],
        reply_to: f('email') || undefined,
        subject: `${LABEL} — ${f('name') || f('service') || 'без имени'}`,
        html
      })
    });
    if(!r.ok){ const t = await r.text(); res.status(502).json({error:'send failed', detail:t}); return; }
    res.status(200).json({ok:true});
  }catch(e){ res.status(500).json({error:String(e && e.message || e)}); }
}
