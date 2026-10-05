// Real-browser QA (Chromium via Playwright) for v12.
// Usage (from project root):
//   python3 -m http.server 8765 --directory dist &
//   node research/weiquan-board-2026-09-29/qa-browser.mjs
// Needs the `playwright` package (global install is fine: set PLAYWRIGHT_MODULE to its index.mjs).
import assert from 'node:assert/strict';
import fs from 'node:fs';
const mod = process.env.PLAYWRIGHT_MODULE || 'playwright';
const {chromium} = await import(mod);
const BASE = process.env.BASE || 'http://localhost:8765/';
const read = p => JSON.parse(fs.readFileSync(new URL(p, import.meta.url)));

// ---------- data checks (no browser) ----------
const data = read('../../dist/schools.json'), ins = read('../../dist/school-insights.json'), board = read('../../dist/wq-board.json');
const oldS = read('../weiquan-2026-09-28/schools-before.json'), oldI = read('../weiquan-2026-09-28/insights-before.json');
const ids = data.schools.filter(s => s.weiquan).map(s => s.id);
assert.equal(ids.length, 27); assert.equal(data.schools.length, 139);
for (const s of data.schools) if (!ids.includes(s.id)) { assert.deepEqual(s, oldS.schools.find(x => x.id === s.id)); assert.deepEqual(ins.schools[s.id], oldI.schools[s.id]); }
{ const bid = board.schools.map(s => s.id); assert.equal(bid.length, 39); for (const x of ['1069','1047','1029','1011','1035','0049','1045','0044','0048','0042','0028','0029','0035','0037','0014','0030','0046','1006','1004','1061','1046','1052','1055','1125']) assert.ok(!bid.includes(x), 'closed/removed '+x); for (const x of ['0009','0008','0013','0001','0002','0003','0004','0005','0007','0012','0015','0019','0020','0022','0023','0033','0052','0053']) assert.ok(bid.includes(x), 'added '+x); }
for (const s of board.schools) {
  assert.ok(['A', 'P', 'B', 'C'].includes(s.tier));
  assert.ok(s.fee.src && s.checked, s.id + ' fee source');
  if (s.fee.kind === 'free') assert.equal(s.fee.amount, 0);
  if (s.fee.kind !== 'free' && s.fee.kind !== 'paid') assert.equal(s.fee.amount, undefined, s.id + ' unknown fee must not be a number');
  for (const tm of ['spring', 'fall']) for (const r of s.terms[tm].rounds) for (const k of ['start', 'end', 'result']) {
    const e = r[k]; if (!e) continue;
    if (e.date) assert.equal(e.status, 'official', `${s.id} ${tm} ${k} exact date must be official`);
  }
  if (s.tuition) assert.ok(s.tuition.src && s.tuition.year, s.id + ' tuition source/year');
}
// graduate-only spring schools must not expose spring undergrad rounds
for (const id of ['0006', '0025', '0031', '0036']) assert.equal(board.schools.find(s => s.id === id).terms.spring.ug, 'grad');
console.log('PASS data: 39 board schools, 112 others unchanged, exact dates only when official, fee/tuition sources present, graduate-only spring hidden.');

// ---------- browser checks ----------
const browser = await chromium.launch();
const errors = [];
async function page(url, vp = {width: 390, height: 844}) {
  const p = await browser.newPage({viewport: vp});
  p.on('pageerror', e => errors.push(url + ': ' + e.message));
  p.on('console', m => { if (m.type() === 'error') errors.push(url + ' console: ' + m.text()); });
  await p.goto(BASE + url, {waitUntil: 'networkidle'});
  return p;
}
const noOverflow = async p => assert.equal(await p.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true, 'no horizontal page scroll');

// main site (ports the v11 Weiquan DOM test to a real browser)
{
  const p = await page('index.html?lang=zh&weiquan=1', {width: 1280, height: 900});
  assert.equal(await p.textContent('.result-count'), '27');
  assert.ok(await p.locator('a.weiquan-board-link').count() >= 1, 'board link on main site');
  await p.click('[data-action="weiquan"]');
  assert.equal(await p.locator('.wq-column').count(), 3);
  await p.selectOption('[data-wq-month]', '2026-11');
  assert.match(await p.textContent('.wq-start'), /11\/02/);
  await p.selectOption('[data-wq-term]', 'fall');
  assert.equal(await p.locator('.wq-season.spring').count(), 0);
  await p.click('.wq-start [data-detail="0047"]');
  assert.match(await p.textContent('.detail-semester'), /秋/);
  await p.click('[data-action="wq-back"]');
  assert.equal(await p.inputValue('[data-wq-month]'), '2026-11');
  await p.click('[data-action="close"]');
  await p.click('[data-remove-filter="weiquan"]');
  assert.equal(await p.textContent('.result-count'), '139');
  await p.close();
  console.log('PASS main site: 27/139, month view columns, NKUHT 11/02, fall isolation, detail + back, board link.');
}

// board, pinned date so the "open now" list is deterministic
{
  const p = await page('weiquan.html?lang=zh&today=2026-09-29');
  await noOverflow(p);
  const tickets = await p.locator('#now .tickets').first().locator('.ticket').count();
  assert.ok(tickets >= 5, 'open-now tickets');
  const first = await p.locator('#now .tickets').first().textContent();
  assert.match(first, /中山/); assert.match(first, /靜宜/); assert.match(first, /10\/15/);
  assert.equal(await p.locator('#now .tickets').first().locator('text=中興').count(), 0, 'NCHU spring is graduate-only');
  assert.equal(await p.locator('.school').count(), 39);
  await p.click('#f-local');
  const local = await p.locator('.school').count();
  assert.ok(local < 39 && local > 10);
  await p.click('#f-sure');
  assert.ok(await p.locator('#s-0039').count() === 1, 'NTCU has a sure first-year waiver');
  await p.click('[data-filter="clear"]');
  await p.click('[data-toggle="0039"]');
  assert.equal(await p.isVisible('#d-0039'), true);
  await p.selectOption('#st-card-0039', 'want');
  assert.match(await p.textContent('.prog-in'), /要報\s*1/);
  await p.reload({waitUntil: 'networkidle'});
  assert.equal(await p.inputValue('#st-card-0039'), 'want', 'status persists on this device');
  await p.click('#lang-my');
  assert.match(await p.textContent('h1'), /ကျောင်း/);
  await noOverflow(p);
  await p.click('[data-sort="cost"]');
  assert.ok(await p.locator('.cmp tbody tr').count() >= 39);
  await p.close();
  // after every deadline passed, the page still renders with an empty state
  const q = await page('weiquan.html?lang=zh&today=2027-08-01');
  assert.match(await q.textContent('#now'), /目前沒有官方公告的學士報名期|接下來開放/);
  await q.close();
  console.log('PASS board: open-now order, grad-only excluded, filters, detail, status persistence, Burmese, sort by cost, no page overflow at 390px.');
}
await browser.close();
assert.deepEqual(errors, [], errors.join('\n'));
console.log('PASS no page errors.');
