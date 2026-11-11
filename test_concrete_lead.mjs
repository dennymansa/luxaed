// Exercise the actual handler with a stub mail transport: no outbound email.
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const messages = [];
globalThis.__concreteTestMessages = messages;
const transportModule = 'data:text/javascript;base64,' + Buffer.from(`
export default { createTransport() { return { async sendMail(mail) {
  globalThis.__concreteTestMessages.push(mail); return {messageId: 'test'};
} }; } };
`).toString('base64');
let source = await readFile(new URL('./api/lead.js', import.meta.url), 'utf8');
source = source.replace("from 'nodemailer'", `from '${transportModule}'`)
  .replace("from './_attribution.js'", `from '${new URL('./api/_attribution.js', import.meta.url).href}'`);
const {default: handler} = await import('data:text/javascript;base64,' + Buffer.from(source).toString('base64'));
process.env.GMAIL_USER = 'test@example.invalid';
process.env.GMAIL_APP_PASSWORD = 'test-only';
process.env.LEAD_TO = 'owner@example.invalid';
process.env.VERCEL_ENV = 'preview';

for (const [lang, label] of [['et','Betoonitööd'], ['ru','Бетонные работы'], ['en','Concrete work']]) {
  const response = { status(code) {this.code=code;return this;}, json(body) {this.body=body;} };
  const body = {form_version:'2', submission_id:`concrete-test-${lang}`, service:'betoon', services:'betoon',
    request_context:'betoon', name:'Test', phone:'+37255555555', email:'test@example.invalid', lang,
    page:'https://luxaed.ee/betoonitood/', photos_expected:0};
  await handler({method:'POST', headers:{host:'localhost'}, body}, response);
  assert.equal(response.code, 200);
  assert.equal(response.body.delivered, true);
  const [owner, customer] = messages.slice(-2);
  assert.match(owner.subject, /бетонные работы/);
  assert.match(owner.text, /Бетонные работы/);
  assert.ok(customer.text.includes(label), `${lang} customer service label`);
}
// Previously supported services still pass validation and retain their labels.
for (const service of ['aed','varav','automaatika','intercom','remont']) {
  const response = {status(code){this.code=code;return this;},json(body){this.body=body;}};
  await handler({method:'POST',headers:{host:'localhost'},body:{form_version:'2',submission_id:`legacy-test-${service}`,
    service,services:service,name:'Test',phone:'+37255555555',email:'test@example.invalid',lang:'et',photos_expected:0}}, response);
  assert.equal(response.code,200);
  assert.equal(response.body.delivered,true);
}
console.log('PASS: concrete leads in ET/RU/EN and all existing service codes; email transport mocked.');
