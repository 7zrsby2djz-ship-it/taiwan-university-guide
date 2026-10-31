import assert from 'node:assert/strict';
import fs from 'node:fs';
import {parseHTML} from 'linkedom';
import {isDate, isLateRound, officialWindows, isOpen, nextResult, compareNullable, matchesQuery, readView,
  cleanComparison, roundChoices, selectRound, resolveRound, taskForRound} from './dist/wq-core.js';

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

const storage = new Map();
let mountCount = 0, blocked = false, copied = '';
async function mount(url = 'https://guide.test/weiquan.html?lang=zh&today=2026-10-31', snapshot = board, services = {}) {
  const {window, document} = parseHTML(fs.readFileSync(new URL('./dist/weiquan.html', import.meta.url), 'utf8'));
  Object.assign(globalThis, {window, document, location: new URL(url)});
  globalThis.history = {replaceState: (_state, _title, value) => { globalThis.location = new URL(value, location); }};
  globalThis.localStorage = {
    getItem: key => storage.get(key) || null,
    setItem: (key, value) => { if (blocked) throw new Error('Quota exceeded'); storage.set(key, value); },
  };
  Object.defineProperty(globalThis, 'navigator', {configurable: true, value: {clipboard: {writeText: async text => { copied = text; }}}});
  globalThis.fetch = async () => ({ok: true, json: async () => structuredClone(snapshot)});
  if (services.claude) window.claude = services.claude;
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
await click('#now [data-jump="0039"]');
assert.equal(find('#q').value, '');
assert.equal(find('#d-0039').hidden, false, 'cross-section jump reveals the school even after a failed search');
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
assert.match(find('#now').textContent, /目前沒有官方公告的學士報名期/);
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
