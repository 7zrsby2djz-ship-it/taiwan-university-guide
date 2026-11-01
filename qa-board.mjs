import assert from 'node:assert/strict';
import fs from 'node:fs';
import {parseHTML} from 'linkedom';
import {isDate, isLateRound, admissionLetter, officialWindows, isOpen, nextResult, compareNullable, matchesQuery, readView,
  cleanComparison, roundChoices, selectRound, resolveRound, taskForRound, matchesIntake} from './dist/wq-core.js';

const board = JSON.parse(fs.readFileSync(new URL('./dist/wq-board.json', import.meta.url)));
const school = id => board.schools.find(s => s.id === id);
const official = date => ({status: 'official', date});
assert.equal(isDate('2026-02-30'), false);
assert.equal(isDate('2028-02-29'), true);
assert.equal(isDate('2026-2-01'), false);
assert.equal(isDate(null), false);

const earlyLetter = {start: official('2027-03-01'), end: official('2027-05-01'), result: official('2027-07-20'), letter: '2027-05-27'};
assert.equal(isLateRound(earlyLetter, board.arcExpiry), false, 'admission letter can precede the public list');
assert.equal(isLateRound({...earlyLetter, letter: '2027-07-01'}, board.arcExpiry), true);
const julyLetter = {status: 'historical', sort: '2027-07-01', label: '115往年7月初', sourceYear: '115'};
assert.equal(isLateRound({...earlyLetter, letter: julyLetter}, board.arcExpiry), true, 'a month-only historical letter can reveal an ARC risk without becoming an exact current date');
assert.deepEqual(admissionLetter({...earlyLetter, letter: julyLetter}), julyLetter);
assert.deepEqual(taskForRound({...earlyLetter, letter: julyLetter}, 'admitted', '2026-11-01'), {kind: 'documents'}, 'an official application deadline never promotes a historical letter');
const graduate = {terms: {spring: {ug: 'grad', rounds: [earlyLetter]}, fall: {ug: 'none', rounds: []}}};
assert.deepEqual(officialWindows(graduate, board.arcExpiry), [], 'never advertise graduate rounds as undergraduate');
const cyutWindow = officialWindows(school('1018'), board.arcExpiry)[0];
assert.equal(cyutWindow.start, null);
assert.equal(isOpen(cyutWindow, '2026-10-31'), false, 'a known deadline does not prove that applications are open');
assert.equal(nextResult(school('1008'), 'spring', '2026-10-31', board.arcExpiry).date, '2026-12-24', 'compare the still-available second round');
assert.equal(nextResult(school('1008'), 'spring', '2027-01-01', board.arcExpiry), null);
assert.equal(nextResult(school('0007'), 'fall', '2026-10-31', board.arcExpiry).status, 'official');
for (const dir of [1, -1]) {
  const values = [null, 4, undefined, 1, 2].sort((a, b) => compareNullable(a, b, dir));
  assert.deepEqual(values.slice(0, 3), dir === 1 ? [1, 2, 4] : [4, 2, 1]);
}
assert.equal(matchesQuery(school('0039'), '台中 NTCU'), true);
assert.equal(matchesQuery(school('1001'), 'ＴＨＵ'), true);
const view = readView(new URLSearchParams('q=中教&filters=local,invented,free&sort=bad&dir=desc'));
assert.deepEqual([...view.filters], ['local', 'free']);
assert.equal(view.sortKey, 'tier');
console.log('PASS board rules: valid dates, undergraduate eligibility, unknown opening dates, admission letters, relevant rounds, unknowns last, multiword search, URL validation.');

// Admissions corrections that materially change whether, when and at what cost to apply.
assert.equal(board.updated, '2026-11-01');
assert.equal(school('1001').terms.spring.ug, 'grad');
assert.equal(school('1062').fee.amount, 1000);
assert.equal(school('1062').terms.spring.rounds[0].end.date, '2026-11-27');
assert.equal(school('0002').terms.fall.rounds[0].end.date, '2027-01-25');
assert.equal(school('0015').terms.fall.rounds[0].letter, '2027-05-28');
assert.match(school('0015').tuition.text, /47,594/);
assert.equal(school('0021').fee.kind, 'silent', 'last autumn\'s free fee cannot imply the new spring intake is free');
assert.equal(school('0021').terms.spring.rounds[0].end.date, '2026-11-29');
assert.equal(school('0022').terms.fall.rounds.length, 1, 'preliminary and final results are one application round');
assert.equal(school('0018').terms.fall.rounds[0].letter.status, 'unknown', 'an acceptance reply form is not an admission letter');
assert.equal(school('0032').firstYearKind, 'review', 'a waiver subject to approval is not an unconditional zero-cost promise');
assert.deepEqual(school('0053').terms.fall.rounds, []);
assert.deepEqual(school('0006').terms.fall.rounds, []);
assert.equal(school('0003').terms.fall.rounds[0].end.date, undefined, 'maintenance notice invalidates the original exact deadline');
assert.equal(officialWindows(school('0003'), board.arcExpiry).some(w => w.round === 1), false);
assert.deepEqual(officialWindows(school('0047'), board.arcExpiry), []);
assert.deepEqual(officialWindows(school('0050'), board.arcExpiry), [], 'conflicting official page versions do not start a countdown');
for (const s of board.schools) {
  assert.ok(s.audit.fields.length && s.audit.sources.length, `${s.id}: explicit audit coverage and sources`);
  assert.equal(s.audit.date, '2026-11-01');
  for (const term of Object.values(s.terms)) for (const r of term.rounds) {
    for (const e of [r.start, r.end, r.result, typeof r.letter === 'object' ? r.letter : null].filter(Boolean)) {
      assert.ok(e.src && e.sourceYear, `${s.id}: event provenance`);
      if (e.status !== 'official') assert.equal(e.date, undefined, `${s.id}: uncertain/historical values are not exact dates`);
    }
  }
}
console.log('PASS admissions audit: 39 scoped records, official years, spring eligibility, corrected fees, letter timing, outdated and conflicting deadlines, one-round results, conditional aid.');

const storage = new Map();
let mountCount = 0, blocked = false, copied = '', clipboardBlocked = false;
async function mount(url = 'https://guide.test/weiquan.html?lang=zh&today=2026-10-31', snapshot = board, services = {}) {
  const {window, document} = parseHTML(fs.readFileSync(new URL('./dist/weiquan.html', import.meta.url), 'utf8'));
  Object.assign(globalThis, {window, document, location: new URL(url)});
  globalThis.history = {replaceState: (_state, _title, value) => { globalThis.location = new URL(value, location); }};
  globalThis.localStorage = {
    getItem: key => storage.get(key) || null,
    setItem: (key, value) => { if (blocked) throw new Error('Quota exceeded'); storage.set(key, value); },
  };
  Object.defineProperty(globalThis, 'navigator', {configurable: true, value: {clipboard: {writeText: async text => { if (clipboardBlocked) throw new Error('NotAllowedError'); copied = text; }}}});
  globalThis.fetch = async () => ({ok: true, json: async () => structuredClone(snapshot)});
  if (services.claude) window.claude = services.claude;
  else delete window.claude;
  window.HTMLElement.prototype.scrollIntoView = function () {};
  window.HTMLElement.prototype.select = function () {};
  window.scrollTo = () => {};
  await import(`./dist/wq-board.js?qa=${++mountCount}`);
  return document;
}
const settle = () => new Promise(resolve => setImmediate(resolve));
const find = selector => { const node = document.querySelector(selector); assert.ok(node, selector); return node; };
async function click(selector) { find(selector).dispatchEvent(new window.Event('click', {bubbles: true})); await settle(); }
async function change(selector, value) { const node = find(selector); Object.defineProperty(node, 'value', {value, configurable: true}); node.dispatchEvent(new window.Event('change', {bubbles: true})); await settle(); }
function input(selector, value) { const node = find(selector); node.value = value; node.dispatchEvent(new window.Event('input', {bubbles: true})); }
const ids = () => [...document.querySelectorAll('.cmp tbody tr [data-jump]')].map(node => node.dataset.jump);

await mount();
assert.equal(document.querySelectorAll('.school').length, 39);
assert.equal(document.querySelectorAll('.cmp tbody tr').length, 39);
const openTickets = find('#now .tickets');
assert.equal(openTickets.querySelector('[data-jump="1018"]'), null);
assert.ok(find('.pending-windows [data-jump="1018"]'));
assert.equal(find('#reference-fold').hasAttribute('open'), false);
assert.ok([...document.querySelectorAll('.ref .tk-count')].every(n => !n.textContent.includes('天')), 'historical months do not have fake daily countdowns');
assert.ok(!find('#d-1018').textContent.includes('往年 第2梯開始待確認'), 'unknown dates do not look historical');
assert.ok(find('.cmp [data-jump="0007"]').closest('tr').textContent.includes('2027 年 5 月中旬'));
assert.ok(!find('.cmp [data-jump="0007"]').closest('tr').textContent.includes('往年'), 'official approximate dates retain official status');
assert.ok(find('.cmp [data-jump="1008"]').closest('tr').textContent.includes('2026/12/24'));
const nextCell = id => find(`#s-${id} .quad div`).textContent;
assert.ok(nextCell('1008').includes('2027 春') && nextCell('1008').includes('11/15'), 'next chance shows the open spring round');
assert.ok(nextCell('0043').includes('2027 秋') && nextCell('0043').includes('往年') && !nextCell('0043').includes('往年 115 往年'), 'past-year fall reference is labelled once');
assert.ok(nextCell('0025').includes('12/1'), 'official fall opening is shown when spring is graduate-only');
assert.ok(nextCell('0001').includes('1/19'), 'second-round official opening is shown after round 1 closes');
assert.ok(document.querySelector('main').innerHTML.indexOf('id="now"') < document.querySelector('main').innerHTML.indexOf('id="news"'), 'actions come before old update notes');
assert.equal([...document.querySelectorAll('.ticks .tick')].length, 4, 'timeline ticks do not crowd at the end');
console.log('PASS next chance: open spring, official fall opening, single past-year label, second-round opening, section order, timeline ticks.');

input('#q', '台中 NTCU');
assert.equal(document.querySelectorAll('.school').length, 1);
assert.deepEqual(ids(), ['0039']);
assert.equal(find('#compare-count').textContent, '1/39');
assert.equal(new URL(location).searchParams.get('q'), '台中 NTCU');
await click('[data-action="clear-search"]');
await click('#f-local'); await click('#f-free');
const expected = board.schools.filter(s => s.commute === 'local' && s.fee.kind === 'free').map(s => s.id).sort();
assert.deepEqual([...document.querySelectorAll('.school')].map(n => n.id.slice(2)).sort(), expected);
assert.deepEqual(ids().sort(), expected);
await click('[data-filter="clear"]');

input('#q', '找不到的學校');
assert.equal(document.querySelectorAll('.school').length, 0);
assert.equal(document.querySelectorAll('.cmp tbody tr').length, 0);
assert.equal(document.querySelector('#now .ticket'), null, 'no-match search also applies to intake tickets');
await click('#news [data-jump="0015"]');
assert.equal(find('#q').value, '');
assert.equal(find('#d-0015').hidden, false, 'an update link reveals its school even after a failed search');
input('#q', '找不到的學校'); await click('#compare [data-action="reset-view"]');
assert.equal(document.querySelectorAll('.school').length, 39);

for (const key of ['biz', 'cost', 'fee', 'fall']) {
  for (let direction = 0; direction < 2; direction++) {
    await click(`[data-sort="${key}"]`);
    const known = id => {
      const s = school(id);
      return key === 'biz' ? !!s.bizAdmits?.length : key === 'cost' ? !!s.semesterCost
        : key === 'fee' ? ['free', 'paid'].includes(s.fee.kind) : !!nextResult(s, 'fall', '2026-10-31', board.arcExpiry);
    };
    let unknownSeen = false;
    for (const id of ids()) { if (!known(id)) unknownSeen = true; else assert.equal(unknownSeen, false, `${key}: unknown values last in both directions`); }
  }
}
await click('[data-sort="biz"]');
assert.equal(find('[data-sort="biz"]').closest('th').getAttribute('aria-sort'), 'descending');
assert.equal(ids()[0], '1001', 'largest business count first, not missing data');
console.log('PASS board interactions: shared search/filter results, no-match recovery, cross-section jump, official labels, current-round comparison, reversible sorts.');

await change('#st-card-0039', 'want');
input('#note-0039', '  還沒按儲存的備註：A2／B1 補件  ');
assert.equal(JSON.parse(storage.get('wq-board-drafts'))['0039'], '  還沒按儲存的備註：A2／B1 補件  ');
await click('#lang-my');
assert.equal(find('#note-0039').value, '  還沒按儲存的備註：A2／B1 補件  ');
await click('#f-local');
assert.equal(find('#note-0039').value, '  還沒按儲存的備註：A2／B1 補件  ');
input('#q', 'NTCU');
const restoredURL = location.href;
await mount(restoredURL);
assert.equal(document.documentElement.lang, 'my');
assert.equal(find('#q').value, 'NTCU');
assert.equal(find('#f-local').getAttribute('aria-pressed'), 'true');
assert.deepEqual(ids(), ['0039']);
assert.equal(find('#note-0039').value, '  還沒按儲存的備註：A2／B1 補件  ');
await click('[data-save="0039"]');
assert.equal(JSON.parse(storage.get('wq-board-notes'))['0039'], '還沒按儲存的備註：A2／B1 補件');
assert.equal(JSON.parse(storage.get('wq-board-drafts'))['0039'], undefined);
assert.ok(find('#s-0039').textContent.includes('A2／B1 補件'));
await click('[data-action="share-view"]');
assert.equal(new URL(copied).searchParams.get('today'), null, 'testing date is not shared');
assert.equal(new URL(copied).searchParams.get('q'), 'NTCU');
assert.equal(copied.includes('補件'), false, 'notes do not enter share URLs');
assert.equal(new URL(copied).hash, '#schools');
await click('#lang-zh');
input('#note-0039', '<img src=x onerror=alert(1)>');
await click('[data-save="0039"]');
assert.equal(document.querySelector('.chip.note img'), null, 'notes cannot inject HTML');
assert.ok(find('#s-0039 .chip.note').textContent.includes('<img'));
blocked = true;
input('#note-0039', '儲存失敗也要保留的內容');
await click('[data-save="0039"]');
assert.match(find('#wq-toast').textContent, /無法儲存/);
assert.equal(find('#note-0039').value, '儲存失敗也要保留的內容');
await change('#st-card-0039', 'no');
assert.equal(find('#st-card-0039').value, 'want', 'failed status writes keep the last saved value');
assert.notEqual(JSON.parse(storage.get('wq-board-notes'))['0039'], '儲存失敗也要保留的內容');
blocked = false;

// Invalid persistent values and URL fragments cannot break the page.
storage.set('wq-board-status', JSON.stringify(['want']));
storage.set('wq-board-notes', JSON.stringify({'0039': {bad: true}, bogus: 'ignored'}));
storage.set('wq-board-drafts', JSON.stringify({'0039': 12, bogus: 'ignored'}));
await mount('https://guide.test/weiquan.html?lang=zh&today=2026-10-31#%ZZ');
assert.equal(document.querySelectorAll('.school').length, 39);
await change('#st-card-1018', 'applied');
assert.match(find('#mine').textContent, /12\/18/, 'waiting for a result still works when the round deadline is unknown');
await mount('https://guide.test/weiquan.html?lang=zh&today=2027-08-01');
assert.match(find('#now').textContent, /所選條件目前沒有受理中的正式梯次/);
assert.equal(document.querySelectorAll('.cmp tbody tr').length, 39);
console.log('PASS board persistence: draft recovery across language/filter/reload, explicit save, storage-failure feedback, private share URLs, corrupted storage, malformed anchors, expired intakes.');

// A pinned comparison is independent of search and personal application records.
storage.clear();
await mount();
for (const id of ['0039', '1008', '0043']) await click(`#compare-card-${id}`);
assert.equal(document.querySelectorAll('.focus-table thead [data-jump]').length, 3);
assert.equal(find('.compare-tray').textContent.includes('3/3'), true);
assert.equal(new URL(location).searchParams.get('compare'), '0039,1008,0043');
await click('#compare-card-1001');
assert.match(find('#wq-toast').textContent, /最多比較 3 間/);
assert.deepEqual(JSON.parse(storage.get('wq-board-compare')), ['0039', '1008', '0043']);
await click('#f-free');
assert.equal(document.querySelector('#s-0039'), null);
assert.ok(find('[data-focus-school="0039"]'), 'paid school stays pinned through a free-fee filter');
input('#q', '完全沒有的校名');
assert.equal(document.querySelectorAll('.cmp tbody tr').length, 0);
assert.equal(document.querySelectorAll('.focus-table thead [data-jump]').length, 3);
await click('[data-action="share-view"]');
assert.equal(new URL(copied).hash, '#compare');
assert.equal(new URL(copied).searchParams.get('compare'), '0039,1008,0043');
await mount(location.href);
assert.equal(document.querySelectorAll('.focus-table thead [data-jump]').length, 3, 'pinned choices survive reload');
await click('.focus-comparison [data-compare="1008"]');
assert.equal(document.querySelectorAll('.focus-table thead [data-jump]').length, 2);
await click('[data-action="clear-compare"]');
assert.equal(document.querySelector('.compare-tray'), null);
assert.equal(document.body.classList.contains('has-comparison'), false);
assert.deepEqual(JSON.parse(storage.get('wq-board-compare')), []);
assert.deepEqual(cleanComparison(['bogus', '0039', '0039', '1008', '0043', '1001'], board.schools.map(s => s.id)), ['0039', '1008', '0043']);
storage.set('wq-board-compare', JSON.stringify(['0039', '1008', '0043']));
await mount('https://guide.test/weiquan.html?lang=zh&today=2026-10-31&compare=');
assert.equal(document.querySelector('.focus-table'), null, 'an explicitly empty shared selection clears local pins');
await mount();
assert.equal(document.querySelector('.focus-table'), null);
console.log('PASS focused comparison: three-school limit, independent filters, source years, share/reload, removal, empty URLs and invalid selections.');

// Application tasks follow the selected semester and round, including closed rounds.
const secondSelection = selectRound(school('1018'), 'spring:2');
assert.equal(selectRound(graduate, 'spring:1'), null);
assert.equal(roundChoices(school('1018')).length, 2);
assert.equal(resolveRound(school('1018'), secondSelection).round.round, 2);
const secondRound = resolveRound(school('1018'), secondSelection).round;
assert.deepEqual(taskForRound(secondRound, 'applied', '2026-10-31'), {kind: 'result', date: '2027-01-15'});
assert.deepEqual(taskForRound(secondRound, 'applied', '2027-01-16'), {kind: 'letter', date: '2027-01-22'});
assert.deepEqual(taskForRound(secondRound, 'applied', '2027-01-22'), {kind: 'letter', date: '2027-01-22'});
assert.deepEqual(taskForRound(secondRound, 'applied', '2027-01-23'), {kind: 'result-ready', date: '2027-01-15'});
assert.equal(taskForRound(secondRound, 'want', '2026-10-31').kind, 'confirm-open');
assert.equal(taskForRound(secondRound, 'want', '2027-01-01').kind, 'closed');
const nycu = roundChoices(school('0007'))[0];
assert.equal(taskForRound(nycu, 'want', '2026-10-31').kind, 'opens');
assert.equal(taskForRound(nycu, 'applied', '2027-05-20').kind, 'result-window', 'an approximate official result never becomes an exact countdown');
assert.equal(taskForRound(roundChoices(school('0043'))[0], 'applied', '2026-10-31').kind, 'verify-result', 'a historical admission letter is not treated as an official current letter');

storage.clear(); await mount();
await change('#st-card-1018', 'applied');
input('#note-1018', '第二梯的待補文件');
await change('#round-1018', 'spring:2');
assert.equal(find('#round-1018').value, 'spring:2');
assert.match(find('[data-progress-school="1018"] .next').textContent, /2027\/01\/15/);
assert.equal(find('#note-1018').value, '第二梯的待補文件', 'changing rounds keeps the note draft');
await click('#lang-my');
assert.equal(find('#round-1018').value, 'spring:2');
await mount('https://guide.test/weiquan.html?lang=zh&today=2026-10-31');
assert.equal(find('#round-1018').value, 'spring:2');
await click('[data-action="copy"]');
assert.match(copied, /第 2 梯/);
assert.match(copied, /2027\/01\/15/);
await click('[data-action="share-view"]');
assert.equal(copied.includes('spring'), false, 'the public filter link omits private chosen application rounds');
await change('#st-card-0039', 'want');
await change('#round-0039', 'spring:1');
assert.equal(find('.mine-row').dataset.progressSchool, '0039', 'a deadline within seven days takes priority over waiting for another result');
blocked = true;
await change('#round-1018', 'spring:1');
assert.equal(find('#round-1018').value, 'spring:2', 'failed writes keep the saved round');
blocked = false;
await mount('https://guide.test/weiquan.html?lang=zh&today=2027-01-16');
assert.match(find('[data-progress-school="1018"] .next').textContent, /2027\/01\/22.*寄發/);
await mount('https://guide.test/weiquan.html?lang=zh&today=2027-01-23');
assert.match(find('[data-progress-school="1018"] .next').textContent, /放榜日已到/);
await change('#st-card-1018', 'want');
assert.match(find('[data-progress-school="1018"] .next').textContent, /這一梯已於.*截止/);
await change('#st-card-1018', 'applied');
const changedBoard = structuredClone(board);
changedBoard.schools.find(s => s.id === '1018').terms.spring.rounds[1].result.date = '2027-01-16';
assert.equal(resolveRound(changedBoard.schools.find(s => s.id === '1018'), secondSelection).state, 'stale');
await mount('https://guide.test/weiquan.html?lang=zh&today=2026-10-31', changedBoard);
assert.match(find('[data-progress-school="1018"] .next').textContent, /時程資料已變動/);
assert.equal(find('#round-1018').value, '');
await change('#round-1018', 'spring:2');
assert.match(find('[data-progress-school="1018"] .next').textContent, /2027\/01\/16/);
await change('#round-1018', '');
assert.equal(JSON.parse(storage.get('wq-board-rounds'))['1018'], undefined);
console.log('PASS intake tracking: exact selected round, pending openings, official intervals, historical dates, note preservation, reload, storage failure, letters/results/closed stages, stale-data confirmation and copy/share separation.');

// Queue cloud writes per school so changing a round and saving a note cannot overwrite each other.
storage.clear();
const cloudDocs = {'1018': {status: 'applied', note: '原本的雲端備註'}};
const pendingWrites = [];
const mockDb = {
  collection: () => ({onSnapshot: callback => callback({docs: Object.entries(cloudDocs).map(([id, value]) => ({id, data: () => value}))})}),
  doc: path => ({set: value => new Promise(resolve => pendingWrites.push(() => {cloudDocs[path.split('/')[1]] = structuredClone(value); resolve();})), delete: async () => {delete cloudDocs[path.split('/')[1]];}}),
};
const claude = {use: async name => name === 'db' ? mockDb : {can: async () => true}};
await mount('https://guide.test/weiquan.html?lang=zh&today=2026-10-31', board, {claude});
await settle();
assert.equal(find('#round-1018').value, '');
await change('#round-1018', 'spring:2');
assert.equal(pendingWrites.length, 1);
input('#note-1018', '同時儲存的新備註');
find('[data-save="1018"]').dispatchEvent(new window.Event('click', {bubbles: true}));
await settle();
assert.equal(pendingWrites.length, 1, 'the second mutation waits for the first');
pendingWrites.shift()(); await settle();
assert.equal(pendingWrites.length, 1);
pendingWrites.shift()(); await settle();
assert.equal(cloudDocs['1018'].note, '同時儲存的新備註');
assert.deepEqual(cloudDocs['1018'].round, secondSelection);
assert.equal(cloudDocs['1018'].status, 'applied');
assert.equal(find('#round-1018').value, 'spring:2');
storage.set('wq-board-status', JSON.stringify({'0039': 'want'}));
storage.set('wq-board-rounds', JSON.stringify({'0039': selectRound(school('0039'), 'spring:1')}));
await mount('https://guide.test/weiquan.html?lang=zh&today=2026-10-31', board, {claude});
await settle();
find('[data-action="upload"]').dispatchEvent(new window.Event('click', {bubbles: true}));
await settle();
assert.equal(pendingWrites.length, 1);
pendingWrites.shift()(); await settle();
assert.deepEqual(cloudDocs['0039'].round, selectRound(school('0039'), 'spring:1'), 'the existing cloud migration carries the chosen intake');
const readonlyClaude = {use: async name => name === 'db' ? mockDb : {can: async () => false}};
await mount('https://guide.test/weiquan.html?lang=zh&today=2026-10-31', board, {claude: readonlyClaude});
await settle();
assert.equal(find('#round-1018').hasAttribute('disabled'), true);
assert.equal(find('#st-mine-1018').hasAttribute('disabled'), true);
console.log('PASS progress store: legacy cloud records, round/note field preservation, queued concurrent writes and read-only controls. Mock service only.');

// Browsing one intake must agree across counts, tickets, cards, comparisons and URLs.
assert.equal(readView(new URLSearchParams('term=fall')).intake, 'fall');
assert.equal(readView(new URLSearchParams('term=graduate')).intake, 'all');
assert.equal(matchesIntake(school('1001'), 'spring'), false);
assert.equal(matchesIntake(school('0012'), 'fall'), true, 'unknown undergraduate scope stays available for verification');
storage.clear();
await mount('https://guide.test/weiquan.html?lang=zh&today=2026-11-01');
assert.ok(find('main').innerHTML.indexOf('id="browse"') < find('main').innerHTML.indexOf('id="now"'));
assert.equal(document.querySelectorAll('#now .soon-windows > .ticket').length, 3);
assert.equal(find('#upcoming-fold').hasAttribute('open'), false, 'more distant openings start folded');
assert.ok(document.querySelectorAll('#upcoming-fold .ticket').length > 0);
await click('#term-fall');
assert.ok([...document.querySelectorAll('#now .ticket')].every(n => n.dataset.term === 'fall'));
assert.equal(find('#term-fall').getAttribute('aria-pressed'), 'true');
assert.equal(document.querySelector('#chances .band.spring'), null);
assert.equal(document.querySelector('#compare [data-sort="result"]'), null);
assert.match(nextCell('1008'), /2027 秋/);
await click('#f-local');
assert.ok([...document.querySelectorAll('#now .ticket')].every(n => school(n.dataset.school).commute === 'local'));
assert.equal(find('#board-overview .overview strong').textContent, '1', 'only the local fall intake is currently open');
input('#q', '彰師大');
assert.equal(find('#view-count').textContent, '1/39');
assert.equal(find('#compare-count').textContent, '1/39');
assert.equal(find('#board-overview .overview strong').textContent, '0');
assert.ok([...document.querySelectorAll('#now .ticket')].every(n => n.dataset.school === '0015'));
input('#q', '找不到的學校');
assert.equal(document.querySelectorAll('#now .ticket').length, 0);
assert.equal(document.querySelectorAll('#chances .band').length, 0, 'no fake application bar when the filtered set has no dates');
await click('[data-action="clear-search"]');
assert.equal(find('#term-fall').getAttribute('aria-pressed'), 'true');
assert.equal(find('#f-local').getAttribute('aria-pressed'), 'true');
await click('[data-action="reset-view"]');
assert.equal(find('#term-all').getAttribute('aria-pressed'), 'true');
assert.equal(document.querySelectorAll('.school').length, 39);
await click('#term-spring');
assert.equal(document.querySelector('#s-1001'), null, 'spring browsing excludes graduate-only schools');
assert.ok([...document.querySelectorAll('#now .ticket')].every(n => n.dataset.term === 'spring'));
await click('[data-sort="result"]');
await click('#term-fall');
assert.ok(find('[data-sort="fall"]').closest('th').getAttribute('aria-sort') !== 'none', 'sorting follows the visible result column');
console.log('PASS intake browsing: shared controls, scoped tickets/counts/cards/chart, unknown scope, folded openings and visible sorting.');

// Existing spring progress and private notes survive browsing fall candidates.
await click('#term-all');
await change('#st-card-1018', 'applied');
await change('#round-1018', 'spring:2');
input('#note-1018', '私人補件內容，不可出現在比較摘要');
await click('[data-save="1018"]');
for (const id of ['1018', '0015', '1008']) await click(`#compare-card-${id}`);
await click('#term-fall');
await click('#f-local');
input('#q', '彰師大');
assert.equal(find('#round-1018').value, 'spring:2');
assert.match(find('[data-progress-school="1018"] .next').textContent, /2027\/01\/15/);
assert.equal(find('#note-1018').value, '私人補件內容，不可出現在比較摘要');
assert.equal(document.querySelectorAll('.focus-table thead [data-jump]').length, 3);
const nearestDeadlineRow = [...document.querySelectorAll('.focus-table tbody tr')].find(row => row.querySelector('th').textContent === '最近官方截止');
assert.equal(nearestDeadlineRow.querySelector('[data-focus-school="1008"]').textContent.includes('2026/11/15'), false, 'fall comparison never borrows the spring deadline');
assert.match(nearestDeadlineRow.querySelector('[data-focus-school="0015"]').textContent, /2027\/03\/05/);
await click('[data-action="copy-compare"]');
assert.match(copied, /2027 秋（116-1）/);
for (const name of ['朝陽', '彰師大', '靜宜']) assert.ok(copied.includes(name));
assert.match(copied, /114/);
assert.match(copied, /https:\/\//);
assert.match(copied, /有 A2 證書可再免學費部分/);
for (const date of ['2026/12/07', '2027/03/05', '2027/05/21', '2027/05/28']) assert.ok(copied.includes(date), 'public comparison includes the selected intake\'s official schedule');
for (const value of ['私人補件內容', 'spring:2', '已報名', '2027/01/15']) assert.equal(copied.includes(value), false, 'comparison export only includes public selection data');
const comparisonSummary = copied;
clipboardBlocked = true;
await click('[data-action="copy-compare"]');
assert.equal(find('#compare-copy-box').hidden, false);
assert.equal(find('#compare-copy-box').value, comparisonSummary);
clipboardBlocked = false;
await click('[data-action="share-view"]');
assert.equal(new URL(copied).searchParams.get('term'), 'fall');
assert.equal(new URL(copied).searchParams.get('compare'), '1018,0015,1008');
assert.equal(copied.includes('私人'), false);
storage.set('wq-board-intake', JSON.stringify('spring'));
await mount(copied);
assert.equal(find('#term-fall').getAttribute('aria-pressed'), 'true', 'shared intake overrides the viewer\'s previous local choice');
assert.equal(document.querySelectorAll('.focus-table thead [data-jump]').length, 3);
await mount('https://guide.test/weiquan.html?lang=zh&today=2026-11-01');
assert.equal(find('#term-fall').getAttribute('aria-pressed'), 'true', 'chosen intake survives a clean return visit');
await click('#term-all');
await click('[data-action="share-view"]');
assert.equal(new URL(copied).searchParams.get('term'), 'all', 'an all-intakes link resets a viewer\'s previously saved fall scope');
storage.set('wq-board-intake', JSON.stringify('fall'));
await mount(copied);
assert.equal(find('#term-all').getAttribute('aria-pressed'), 'true');
await click('#lang-my');
await click('[data-action="copy-compare"]');
assert.match(copied, /နှိုင်းယှဉ်ချက်/);
assert.equal(copied.includes('私人補件內容'), false);
console.log('PASS comparison sharing: intake persistence, source years, language/aid caveats, private progress retained, clipboard fallback, no notes/status/rounds exported, Myanmar export.');
