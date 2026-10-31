// 偉銓選校板 — decision board for the 39 personal schools.
// Data: ./wq-board.json (built by research/weiquan-board-2026-09-29/build_board.py).
// Only official dates are shown as exact dates; past-year references are labelled.
import {isDate, isLateRound, undergraduateRounds, officialWindows, isOpen as openOn,
  isSoon as soonOn, isUnconfirmed, nextResult, compareNullable, matchesQuery, readView,
  cleanComparison, roundChoices, selectRound, resolveRound, taskForRound} from './wq-core.js';

const root = document.querySelector('#board');
const esc = v => String(v ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const safeURL = u => { try { const x = new URL(u, location.href); return ['http:','https:'].includes(x.protocol) ? x.href : '#'; } catch { return '#'; } };
const store = {
  get(k, f) { try { const v = JSON.parse(localStorage.getItem(k)); return v ?? f; } catch { return f; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); return true; } catch { return false; } },
};

// ---- today (Taiwan time); ?today=YYYY-MM-DD lets testers pin a date ----
const qs = new URLSearchParams(location.search);
const TODAY = isDate(qs.get('today')) ? qs.get('today')
  : new Intl.DateTimeFormat('en-CA', {timeZone: 'Asia/Taipei', year: 'numeric', month: '2-digit', day: '2-digit'}).format(new Date());
const dayDiff = (a, b) => Math.round((Date.parse(b + 'T00:00:00Z') - Date.parse(a + 'T00:00:00Z')) / 864e5);

// ---- words ----
const W = {
  title: ['偉銓選校板', '偉銓 · ကျောင်းရွေးဘုတ်'],
  lead: ['39 間學校，只看學士。先看現在能報的，再比第一年要付多少、獎學金好不好拿。', 'ကျောင်း ၃၉ ကျောင်း၊ ဘွဲ့ကြိုသာ။ ယခုလျှောက်နိုင်သည့်ကျောင်းကို အရင်ကြည့်ပြီး ပထမနှစ် ကုန်ကျစရိတ်နှင့် ပညာသင်ဆုကို နှိုင်းယှဉ်ပါ။'],
  allSite: ['全部 139 校・按月份看', 'ကျောင်းအားလုံး · လအလိုက်'],
  now: ['現在可以報名', 'ယခု လျှောက်နိုင်သည်'],
  nowSub: ['學士可報、官方日期、依截止日排序', 'ဘွဲ့ကြို · တရားဝင်ရက် · နောက်ဆုံးရက်အလိုက်'],
  soon: ['接下來開放', 'မကြာမီ ဖွင့်မည်'],
  nothingNow: ['目前沒有官方公告的學士報名期。', 'ယခု တရားဝင် လျှောက်လွှာကာလ မရှိပါ။'],
  left: ['剩', 'ကျန်'], days: ['天', 'ရက်'], lastDay: ['今天截止', 'ယနေ့ နောက်ဆုံး'],
  opens: ['開始', 'ဖွင့်'], deadline: ['截止', 'ပိတ်'], result: ['放榜', 'ရလဒ်'], letter: ['入學許可', 'ဝင်ခွင့်စာ'],
  apply: ['報名入口', 'လျှောက်ရန်'], brochure: ['簡章', 'လမ်းညွှန်'],
  chances: ['ARC 到期前還有 2 次機會', 'ARC မကုန်ခင် အခွင့်အရေး ၂ ကြိမ်'],
  schools: ['學校', 'ကျောင်းများ'],
  compare: ['比較表', 'နှိုင်းယှဉ်ဇယား'],
  fSpring: ['2027 春', '2027 နွေဦး'], fFee: ['申請費', 'လျှောက်လွှာကြေး'], fCost: ['第一學期學雜費', 'ပထမ စာသင်နှစ်ဝက် ကျောင်းလခ'], fKm: ['距台中車站', 'ထိုင်ချုံးဘူတာမှ'],
  details: ['看全部重點', 'အသေးစိတ်ကြည့်ရန်'], hide: ['收起', 'ပိတ်ရန်'],
  aidHow: ['獎學金怎麼拿', 'ပညာသင်ဆု ဘယ်လိုရမလဲ'], sure: ['錄取或有證書就有', 'ဝင်ခွင့်ရရင် / လက်မှတ်ရှိရင် ရမည်'], review: ['要審查，不一定有', 'စစ်ဆေးရွေးချယ် · မသေချာ'],
  renew: ['怎麼續領', 'ဆက်ရရန် စည်းကမ်း'], tuition: ['學費', 'ကျောင်းလခ'], lang: ['語言門檻', 'ဘာသာစကား လိုအပ်ချက်'],
  schedule: ['學士時程', 'ဘွဲ့ကြို အချိန်ဇယား'], after: ['錄取後', 'ဝင်ခွင့်ရပြီးနောက်'], lists: ['歷年榜單（官方）', 'ယခင်နှစ် ဝင်ခွင့်စာရင်း'], biz: ['商管系外籍生上榜人數', 'စီးပွားရေးဌာန နိုင်ငံခြားသား ဝင်ခွင့်ရသူ'],
  links: ['官方連結', 'တရားဝင် link'], yourself: ['這些我讀不到，請你自己看', 'ဒါတွေ ဖတ်မရ — ကိုယ်တိုင်ကြည့်ပါ'],
  round: ['梯', 'အဆင့်'], official: ['官方', 'တရားဝင်'], past: ['往年', 'ယခင်နှစ်'], diff: ['來源有差異', 'ရင်းမြစ်မတူ'],
  springT: ['2027 春（115-2）', '2027 နွေဦး (115-2)'], fallT: ['2027 秋（116-1）', '2027 ဆောင်းဦး (116-1)'],
  gradOnly: ['只收研究所，學士不能報', 'ဘွဲ့လွန်သာ · ဘွဲ့ကြို မရ'], noneTerm: ['這季不招生', 'ဤရာသီ မလက်ခံ'], unknownTerm: ['還沒查到時程', 'အချိန်ဇယား မသိရသေး'],
  status: ['我的進度', 'ကျွန်ုပ်၏ အခြေအနေ'],
  copy: ['複製進度給他看', 'အခြေအနေ ကူးရန်'], copied: ['已複製，可以貼到 LINE', 'ကူးပြီးပါပြီ'], copyFail: ['無法自動複製，請手動選取下面文字', 'ကိုယ်တိုင် ကူးပါ'],
  filterNow: ['現在能報', 'ယခုလျှောက်နိုင်'], filterLocal: ['台中通勤圈', 'ထိုင်ချုံး နီး'], filterSure: ['錄取就有學費優惠', 'ဝင်ခွင့်ရရင် ကျောင်းလခလျှော့'], filterFree: ['明文免申請費', 'လျှောက်လွှာကြေး အခမဲ့'],
  noMatch: ['沒有學校同時符合這些條件。', 'ကိုက်ညီသော ကျောင်းမရှိပါ။'], clear: ['清除', 'ရှင်းရန်'],
  residence: ['拿到入學許可後：換居留', 'ဝင်ခွင့်စာရပြီးနောက် · ARC ပြောင်းရန်'],
  prep: ['每一間都要準備', 'ကျောင်းတိုင်းအတွက် ပြင်ဆင်ရန်'],
  foot: ['資料查核：2026/09/29。只有官方當期公告才顯示確切日期；「往年」是上一年的月份參考。金額與日期以官方簡章為準；分組是我的建議，不是官方排名。', '2026/09/29 စစ်ဆေးထားသည်။ တရားဝင်ကြေညာချက်မှသာ ရက်အတိအကျပြသည်။ "ယခင်နှစ်" သည် ကိုးကားချက်သာ။'],
  kmUnit: ['公里', 'km'], yuan: ['元', 'NT$'],
  navNews: ['這次更新', 'အသစ်'], navMine: ['我的申請', 'ကျွန်ုပ်၏'], navNow: ['現在可報', 'ယခု'], navSchools: ['學校', 'ကျောင်း'], navCompare: ['比較', 'နှိုင်းယှဉ်'], navAfter: ['換居留', 'ARC'],
  news: ['這次更新', 'နောက်ဆုံး ပြင်ဆင်ချက်'], mine: ['我的申請', 'ကျွန်ုပ်၏ လျှောက်လွှာများ'],
  search: ['找學校（名稱、縮寫、地點）', 'ကျောင်းရှာရန်'], filterBiz: ['商管有外籍生上榜', 'စီးပွားရေး နိုင်ငံခြားသား ဝင်ဖူး'],
  note: ['備註', 'မှတ်ချက်'], save: ['存備註', 'သိမ်းရန်'], saved: ['已存', 'သိမ်းပြီး'],
  bizShort: ['商管外籍上榜', 'စီးပွားရေး ဝင်ခွင့်'], isNew: ['新', 'အသစ်'],
  filterMine: ['我的申請', 'ကျွန်ုပ်၏ လျှောက်လွှာ'],
  clearSearch: ['清除搜尋', 'ရှာဖွေမှု ရှင်းရန်'],
  resetView: ['清除搜尋與篩選', 'ရှာဖွေမှုနှင့် စစ်ထုတ်မှု ရှင်းရန်'],
  shareView: ['複製篩選連結', 'စစ်ထုတ်ထားသောလင့်ခ် ကူးရန်'],
  viewCopied: ['篩選連結已複製；不包含申請進度或備註', 'လင့်ခ် ကူးပြီး။ မှတ်ချက်နှင့် လျှောက်လွှာအခြေအနေ မပါ။'],
  draft: ['草稿已保留；按「存備註」才會更新進度', 'မူကြမ်း သိမ်းထားသည်။ အတည်ပြုရန် သိမ်းပါ။'],
  saveError: ['這台裝置無法儲存，請先複製進度備份', 'ဤဖုန်းတွင် မသိမ်းနိုင်ပါ။ အခြေအနေကို ကူးထားပါ။'],
  pendingStart: ['開放狀態待確認', 'ဖွင့်မဖွင့် အတည်ပြုရန်'],
  unknownDate: ['待確認', 'အတည်ပြုရန်'],
  openSummary: ['已確認可報', 'ယခု လျှောက်နိုင်'],
  urgentSummary: ['7 天內截止', '၇ ရက်အတွင်း ပိတ်မည်'],
  trackedSummary: ['我的申請', 'ကျွန်ုပ်၏ လျှောက်လွှာ'],
  addCompare: ['加入比較', 'နှိုင်းယှဉ်ရန် ရွေး'], compared: ['已加入比較', 'ရွေးထားပြီး'],
  focusedCompare: ['我選的學校', 'ရွေးထားသောကျောင်းများ'],
  compareLimit: ['最多比較 3 間，先移除一間再加入', 'အများဆုံး ၃ ကျောင်း။ တစ်ကျောင်းဖယ်ပြီး ထပ်ရွေးပါ။'],
  removeCompare: ['移出比較', 'နှိုင်းယှဉ်မှုမှ ဖယ်ရန်'],
  clearCompare: ['清空比較', 'ရွေးထားမှု ရှင်းရန်'],
  goCompare: ['前往比較', 'နှိုင်းယှဉ်ကြည့်ရန်'],
  chooseRound: ['申請哪一梯', 'လျှောက်သည့်အကြိမ်'],
  roundAuto: ['尚未指定・僅顯示參考', 'မရွေးရသေး · ကိုးကားသာ'],
  roundStale: ['時程資料已變動，請重新確認申請梯次', 'ရက်စွဲပြောင်းထားသည်။ အကြိမ်ကို ပြန်ရွေးပါ။'],
  roundSource: ['這一梯的官方來源', 'ဤအကြိမ်၏ တရားဝင်ရင်းမြစ်'],
  noRound: ['沒有可核對的學士梯次，請向學校確認', 'ဘွဲ့ကြိုအချိန်ဇယား အတည်ပြုရန် ကျောင်းကို မေးပါ။'],
  chosenRound: ['已指定梯次', 'ရွေးထားသည့်အကြိမ်'],
};
const STATUS = [['', '還沒決定', 'မဆုံးဖြတ်ရသေး'], ['want', '要報', 'လျှောက်မည်'], ['applied', '已報名', 'လျှောက်ပြီး'], ['admitted', '錄取', 'ဝင်ခွင့်ရ'], ['no', '不考慮', 'မလျှောက်']];
const TIERS = {
  A: ['台中近又省錢・首選', 'ထိုင်ချုံးနီး · ငွေသက်သာ · ဦးစားပေး', '市區或近郊、公立或第一年有確定優惠。'],
  P: ['知名學校・遠或貴也值得考慮', 'နာမည်ကြီးကျောင်း · ဝေး/ဈေးကြီးလည်း စဉ်းစားထိုက်', '你說過，名校上了可以多花一點。'],
  B: ['備案・條件普通或資料要你自己看', 'အရန်ကျောင်းများ', '台中私立科大、較遠的公立；有些資料讀不到。'],
  C: ['暫不優先', 'ဦးစားမပေး', '要搬家又不是名校、醫學類學費高，或學士不能報春季。'],
};
const TIER_ORDER = {A: 0, P: 1, B: 2, C: 3};

const view = readView(qs);
let data, lang = store.get('wq-lang', 'zh'), localStatus = store.get('wq-board-status', {}), localNotes = store.get('wq-board-notes', {}), drafts = store.get('wq-board-drafts', {}),
  localRounds = store.get('wq-board-rounds', {}), compareIds = qs.has('compare') ? view.compareIds : store.get('wq-board-compare', []),
  {filters, sortKey, sortDirection, query} = view, openCards = new Set(), newsAll = false, refsExpanded = false;
// Shared progress (status + note per school). Cloud = artifact db when this view can use it; otherwise this device only.
const cloud = {db: null, ready: false, writable: false, docs: {}};
let statusMap = {};
if (!['zh', 'my'].includes(lang)) lang = 'zh';
if (['zh', 'my'].includes(qs.get('lang'))) lang = qs.get('lang');
const record = v => v && typeof v === 'object' && !Array.isArray(v);
if (!record(localStatus)) localStatus = {};
if (!record(localNotes)) localNotes = {};
if (!record(drafts)) drafts = {};
if (!record(localRounds)) localRounds = {};
const VALID = new Set(['want', 'applied', 'admitted', 'no']);
function syncStatusMap() {
  statusMap = {};
  const src = cloud.ready ? Object.fromEntries(Object.entries(cloud.docs).map(([k, v]) => [k, v.status])) : localStatus;
  for (const [k, v] of Object.entries(src)) if (VALID.has(v)) statusMap[k] = v;
}
const noteOf = id => (cloud.ready ? cloud.docs[id]?.note : localNotes[id]) || '';
const draftOf = id => Object.hasOwn(drafts, id) ? drafts[id] : noteOf(id);
const roundOf = id => (cloud.ready ? cloud.docs[id]?.round : localRounds[id]) || null;
syncStatusMap();
const t = k => (W[k] || [k, k])[lang === 'zh' ? 0 : 1];
const zh = () => lang === 'zh';

// ---- formatting ----
const WD = ['日', '一', '二', '三', '四', '五', '六'];
const md = d => { const [, m, dd] = d.split('-'); return `${+m}/${+dd}`; };
const mdw = d => md(d) + (zh() ? `（${WD[new Date(d + 'T00:00:00Z').getUTCDay()]}）` : '');
const ymd = d => d.replaceAll('-', '/');
const wan = n => (n / 10000).toFixed(n % 10000 === 0 ? 0 : 1).replace(/\.0$/, '');
const money = (a, b) => zh() ? (a === b ? `${wan(a)} 萬` : `${wan(a)}–${wan(b)} 萬`) : (a === b ? `NT$${a.toLocaleString('en')}` : `NT$${a.toLocaleString('en')}–${b.toLocaleString('en')}`);
function evText(e) {
  if (!e) return '—';
  if (e.status === 'official' && e.date) return ymd(e.date);
  if (e.status === 'official' && e.label) return e.label;
  if (e.status === 'conflict') return t('diff');
  if (!['historical', 'estimated'].includes(e.status)) return e.label || t('unknownDate');
  return e.label?.includes('往年') && zh() ? e.label : `${t('past')} ${e.label || ''}`.trim();
}
const evClass = e => !e ? 'none' : e.status === 'official' ? 'ok' : e.status === 'conflict' ? 'bad' : ['historical', 'estimated'].includes(e.status) ? 'past' : 'none';
const letterEvent = r => !r.letter ? null : ['end', 'result'].some(k => r[k]?.status === 'official')
  ? {status: 'official', date: r.letter} : {status: 'historical', label: md(r.letter)};

function feeView(f) {
  if (f.kind === 'free') return {cls: 'good', text: zh() ? '免費（明文）' : 'အခမဲ့'};
  if (f.kind === 'paid') return {cls: 'warn', text: zh() ? `${f.amount.toLocaleString('en')} 元` : `NT$${f.amount.toLocaleString('en')}`};
  if (f.kind === 'silent') return {cls: 'muted', text: zh() ? '簡章沒寫' : 'မဖော်ပြ'};
  return {cls: 'muted', text: zh() ? '讀不到' : 'မသိရ'};
}
function costView(s) {
  const c = s.semesterCost;
  if (!c) return {cls: 'muted', text: zh() ? '還沒查到' : 'မသိရသေး', note: ''};
  if (c.basis === 'sure') {
    if (c.max === 0) return {cls: 'good', text: zh() ? '0 元' : 'NT$0', note: zh() ? '第一年錄取就免' : 'ပထမနှစ် အခမဲ့'};
    return {cls: 'good', text: money(c.min, c.max), note: zh() ? '已扣錄取就有的減免' : 'လျှော့ပြီးနောက်'};
  }
  const note = s.firstYearKind === 'lang' ? (zh() ? '有 A2 證書可再免學費部分' : 'A2 လက်မှတ်ဖြင့် ထပ်လျှော့') : (zh() ? '沒拿到獎學金時' : 'ပညာသင်ဆု မရလျှင်');
  return {cls: s.semesterCost.max > 60000 ? 'bad' : 'warn', text: money(c.min, c.max), note};
}
function springView(s) {
  const T = s.terms.spring;
  if (T.ug === 'grad') return {cls: 'bad', text: zh() ? '只收研究所' : 'ဘွဲ့လွန်သာ'};
  if (T.ug === 'none') return {cls: 'bad', text: zh() ? '只收秋季' : 'ဆောင်းဦးသာ'};
  const w = windowsOf(s).filter(x => x.term === 'spring');
  const live = w.find(x => x.end >= TODAY);
  if (live) return {cls: isUnconfirmed(live, TODAY) ? 'warn' : 'good', text: isUnconfirmed(live, TODAY)
    ? `${t('pendingStart')} · ${md(live.end)}`
    : (isSoon(live) ? `${t('opens')} ${md(live.start)}` : (zh() ? '報名到 ' : '') + md(live.end) + (zh() ? '' : ' အထိ'))};
  if (w.length) return {cls: 'muted', text: zh() ? '已截止' : 'ပိတ်ပြီး'};
  if (T.ug === 'has') return {cls: 'muted', text: zh() ? '只有往年參考' : 'ယခင်နှစ်သာ'};
  return {cls: 'muted', text: zh() ? '沒查到' : 'မသိရ'};
}

const windowsOf = s => officialWindows(s, data.arcExpiry);
// Rounds with past-year references; this does not prove the school has not published newer dates.
function refWindows(s) {
  const out = [];
  for (const term of ['spring', 'fall']) undergraduateRounds(s, term, data.arcExpiry).forEach(r => {
    const e = r.end;
    if (!e || e.status === 'official' || e.status === 'conflict' || !e.sort || e.sort < TODAY) return;
    if (lateRound(r)) return; // result after ARC expiry: dropped
    if (term === 'spring' && s.ownership === 'public') return; // national spring is graduate-only or unverified; live undergrad spring tickets stay above
    out.push({s, term, round: r.round, many: s.terms[term].rounds.length > 1, r, key: (r.start && r.start.sort) || e.sort});
  });
  return out;
}
const refLabel = e => !e ? '—' : e.status === 'conflict' ? t('diff') : (e.label || '—');
const isOpen = w => openOn(w, TODAY);
const isSoon = w => soonOn(w, TODAY);
const hasSure = s => ['full', 'half', 'minus', 'lang', 'mostly'].includes(s.firstYearKind);
// Biggest business-department count on the official lists (ties: newer year first).
function bizTop(s) {
  const l = s.bizAdmits || [];
  if (!l.length) return null;
  return [...l].sort((a, b) => b.count - a.count || String(b.year).localeCompare(String(a.year)))[0];
}
const deptShort = d => String(d).replace(/（.*?）|\(.*?\)/g, '').replace(/學系|學士學位學程|學位學程|學程/g, '').trim();
const latestNews = () => { const c = data.changes || []; const d = c.map(x => x.date).sort().pop(); return d ? c.filter(x => x.date === d) : []; };
const isNewSchool = s => latestNews().some(c => c.id === s.id);
// The next date that matters for one school, given its status.
function nextStep(s, st) {
  const selected = resolveRound(s, roundOf(s.id));
  if (selected.state === 'stale') return {cls: 'warn', text: t('roundStale')};
  if (selected.round) return selectedTask(selected.round, st);
  const ws = windowsOf(s);
  if (st === 'admitted') return {cls: 'good', text: zh() ? '拿入學許可去換居留' : 'ARC ပြောင်းရန်'};
  if (st === 'applied') {
    const results = ['spring', 'fall'].flatMap(term => undergraduateRounds(s, term, data.arcExpiry))
      .map(r => r.result).filter(e => e?.status === 'official' && (e.date || e.sort) >= TODAY)
      .sort((a, b) => (a.date || a.sort).localeCompare(b.date || b.sort));
    const res = results[0];
    if (res?.date) return {cls: 'warn', text: zh() ? `${results.length > 1 ? '最早放榜參考' : '放榜'} ${mdw(res.date)}・還有 ${dayDiff(TODAY, res.date)} 天${results.length > 1 ? '（請核對申請梯次）' : ''}` : `ရလဒ် ${md(res.date)}`};
    return {cls: 'muted', text: zh() ? `等放榜${res ? `（${evText(res)}）` : '（請核對已報名的梯次）'}` : 'ရလဒ် စောင့်'};
  }
  const open = ws.filter(isOpen).sort((a, b) => a.end.localeCompare(b.end))[0];
  if (open) { const d = dayDiff(TODAY, open.end); return {cls: d <= 14 ? 'bad' : 'warn', text: zh() ? `截止 ${mdw(open.end)}・剩 ${d} 天` : `${md(open.end)} ပိတ်`, due: open.end, kind: 'deadline'}; }
  const soon = ws.filter(isSoon).sort((a, b) => a.start.localeCompare(b.start))[0];
  if (soon) return {cls: 'muted', text: zh() ? `${mdw(soon.start)} 開始報名` : `${md(soon.start)} ဖွင့်`};
  const pending = ws.find(w => isUnconfirmed(w, TODAY));
  if (pending) return {cls: 'warn', text: `${t('pendingStart')} · ${t('deadline')} ${mdw(pending.end)}`};
  const ref = refWindows(s).sort((a, b) => a.key.localeCompare(b.key))[0];
  if (ref) return {cls: 'muted', text: zh() ? `往年約 ${refLabel(ref.r.start)} 開始（本期日期待核對）` : 'ယခင်နှစ် ရက်သာ'};
  return {cls: 'muted', text: zh() ? '還沒有可報的梯次' : '—'};
}

function selectedTask(round, status) {
  const task = taskForRound(round, status, TODAY), d = task.date ? dayDiff(TODAY, task.date) : null;
  const date = task.date ? ymd(task.date) : '';
  const labels = {
    deadline: [d === 0 ? `今天截止（${date}）` : `截止 ${date}・剩 ${d} 天`, `${date} ပိတ် · ${d} ရက် ကျန်`],
    opens: [`${date} 開始報名`, `${date} ဖွင့်မည်`],
    closed: [`這一梯已於 ${date} 截止；請確認是否已送出或改選梯次`, `${date} ပိတ်ပြီး။ လျှောက်ပြီးမပြီး စစ်ပါ။`],
    result: [d === 0 ? `今天放榜（${date}），請看官方結果` : `放榜 ${date}・還有 ${d} 天`, `${date} ရလဒ် · ${d} ရက်`],
    letter: [`入學許可預計 ${date} 寄發；請確認收件與後續手續`, `ဝင်ခွင့်စာ ${date} ပို့မည်။ ကျောင်းနှင့် အတည်ပြုပါ။`],
    'result-ready': [`${date} 的放榜日已到；請查結果並更新進度`, `${date} ရလဒ်ထွက်ရက် ရောက်ပြီး။ အခြေအနေ ပြင်ပါ။`],
    'result-window': [`等待放榜：${evText(task.event)}`, `ရလဒ် စောင့် · ${evText(task.event)}`],
    'verify-result': [`放榜待確認${task.event ? `：${evText(task.event)}` : ''}；請查這一梯的官方來源`, 'ရလဒ်ရက်ကို ကျောင်းနှင့် အတည်ပြုပါ။'],
    'verify-deadline': [`這一梯的截止日待確認${task.event ? `：${evText(task.event)}` : ''}`, 'ဤအကြိမ်၏ ပိတ်ရက်ကို အတည်ပြုပါ။'],
    'confirm-open': [`開放狀態待確認；官方截止 ${date}`, `${date} ပိတ်။ ဖွင့်မဖွင့် အတည်ပြုပါ။`],
    documents: ['確認已取得入學許可，再核對註冊與居留手續', 'ဝင်ခွင့်စာ ရရှိပြီးမပြီး၊ မှတ်ပုံတင်ရက်နှင့် ARC စစ်ပါ။'],
  };
  return {cls: ['closed', 'result-ready'].includes(task.kind) || (task.kind === 'deadline' && d <= 7) ? 'bad' : ['opens', 'documents'].includes(task.kind) ? 'muted' : 'warn',
    text: labels[task.kind][zh() ? 0 : 1], due: task.date, kind: task.kind};
}

const roundName = r => `${r.term === 'spring' ? t('springT') : t('fallT')} · ${zh() ? `第 ${r.round} 梯` : `${t('round')} ${r.round}`}`;
function roundControl(s) {
  const choices = roundChoices(s), selected = resolveRound(s, roundOf(s.id));
  if (!choices.length) return `<p class="hint">${t('noRound')}</p>`;
  const canWrite = !cloud.ready || cloud.writable;
  return `<div class="round-control"><label for="round-${s.id}">${t('chooseRound')}</label>
    <select id="round-${s.id}" data-round="${s.id}" ${canWrite ? '' : 'disabled'}><option value="" ${selected.round ? '' : 'selected'}>${selected.state === 'stale' ? t('roundStale') : t('roundAuto')}</option>
    ${choices.map(r => `<option value="${r.key}" ${selected.round?.key === r.key ? 'selected' : ''}>${esc(roundName(r))}${r.end ? ` · ${t('deadline')} ${esc(evText(r.end))}` : ''}</option>`).join('')}</select>
    ${selected.round ? `<a href="${esc(safeURL(selected.round.src || selected.round.end?.src || selected.round.result?.src || s.links.apply))}" target="_blank" rel="noopener noreferrer">${t('roundSource')} ↗</a>` : ''}</div>`;
}

// ---- sections ----
function header() {
  return `<header class="bar"><div class="wrap bar-in"><a class="brand" href="./index.html?lang=${lang}&weiquan=1" title="${esc(t('allSite'))}"><span class="mark" aria-hidden="true">偉</span><span><strong>${esc(t('title'))}</strong><small>${zh() ? '給第一次上大學的他' : 'ပထမဆုံး တက္ကသိုလ်တက်မည့်သူအတွက်'}</small></span></a>
  <div class="bar-actions"><a class="ghost" href="./index.html?lang=${lang}&weiquan=1">${esc(t('allSite'))}</a><div class="seg" role="group" aria-label="Language"><button id="lang-zh" data-lang="zh" aria-pressed="${zh()}">繁中</button><button id="lang-my" data-lang="my" aria-pressed="${!zh()}" lang="my">မြန်မာ</button></div></div></div></header>`;
}
function navBar() {
  const N = [['news', 'navNews'], ['mine', 'navMine'], ['now', 'navNow'], ['schools', 'navSchools'], ['compare', 'navCompare'], ['after', 'navAfter']].filter(([k]) => k !== 'news' || (data.changes || []).length);
  return `<nav class="jump" aria-label="${zh() ? '跳到' : 'သွားရန်'}"><div class="wrap jump-in">${N.map(([k, w]) => `<a href="#${k}">${esc(t(w))}${k === 'mine' && Object.keys(statusMap).length ? ` <b>${Object.values(statusMap).filter(v => v !== 'no').length}</b>` : ''}</a>`).join('')}</div></nav>`;
}
function newsSection() {
  const all = [...(data.changes || [])].sort((a, b) => b.date.localeCompare(a.date));
  if (!all.length) return '';
  const latest = all[0].date, top = all.filter(c => c.date === latest);
  const shown = newsAll ? all : top.slice(0, 6);
  const by = Object.fromEntries(data.schools.map(s => [s.id, s]));
  const kindTxt = {new: zh() ? '新公布' : 'အသစ်', change: zh() ? '有變動' : 'ပြောင်း', check: zh() ? '確認' : 'စစ်', drop: zh() ? '拿掉' : 'ဖယ်'};
  return `<section class="wrap block" id="news"><div class="block-head"><h2>${t('news')} <span class="count">${ymd(latest)}</span></h2><p>${zh() ? `這次查到 ${top.length} 項變動。點學校名稱看詳情。` : `${top.length} ခု`}</p></div>
  <ul class="news">${shown.map(c => { const sc = by[c.id]; return `<li class="k-${esc(c.kind || 'change')}"><span class="nk">${esc(kindTxt[c.kind] || kindTxt.change)}</span><div>${sc ? `<button class="linkish" data-jump="${sc.id}">${esc(sc.short)}</button> ` : ''}${esc(c.text)}${c.date !== latest ? ` <small class="muted">${ymd(c.date)}</small>` : ''}</div></li>`; }).join('')}</ul>
  ${all.length > shown.length || newsAll ? `<button class="more" data-action="news">${newsAll ? t('hide') : (zh() ? `顯示全部 ${all.length} 項` : `${all.length} ခု အားလုံး`)}</button>` : ''}</section>`;
}
function mineSection() {
  const order = {applied: 0, want: 1, admitted: 2};
  const priority = s => { const task = nextStep(s, statusMap[s.id]);
    return task.kind === 'deadline' && dayDiff(TODAY, task.due) <= 7 ? 0 : ['closed', 'result-ready'].includes(task.kind) || (task.kind === 'result' && task.due === TODAY) ? 1 : 2 + order[statusMap[s.id]]; };
  const mine = data.schools.filter(s => order[statusMap[s.id]] !== undefined).sort((a, b) => priority(a) - priority(b) || TIER_ORDER[a.tier] - TIER_ORDER[b.tier]);
  const counts = STATUS.slice(1).map(([k, a, b]) => [k, zh() ? a : b, data.schools.filter(s => statusMap[s.id] === k).length]).filter(x => x[2]);
  const pending = cloud.ready && cloud.writable && Object.entries(localStatus).some(([k, v]) => VALID.has(v) && !cloud.docs[k]);
  const sync = cloud.ready ? (cloud.writable ? (zh() ? '☁ 雲端同步：在任何裝置打開這頁都看到同一份' : '☁ ထပ်တူ') : (zh() ? '☁ 雲端資料（你只能看，不能改）' : '☁ ကြည့်ရုံသာ')) : (zh() ? '只存在這台裝置（換手機看不到）' : 'ဤဖုန်းတွင်သာ');
  return `<section class="wrap block" id="mine"><div class="block-head"><h2>${t('mine')}</h2><p class="sync">${esc(sync)}</p></div>
  <div class="mine-sum">${counts.map(([k, l, n]) => `<span class="st-${k}">${esc(l)} <b>${n}</b></span>`).join('') || `<span class="muted">${zh() ? '在學校卡片右上角選「要報」「已報名」，這裡就會列出下一步要做什麼。' : 'ကျောင်းကတ်တွင် အခြေအနေ ရွေးပါ။'}</span>`}<button class="btn ghost" data-action="copy">${t('copy')}</button></div>
  ${pending ? `<p class="hint">${zh() ? '這台裝置有之前存的標記還沒放上雲端。' : ''}<button class="fclear" data-action="upload">${zh() ? '放上雲端' : 'တင်ရန်'}</button></p>` : ''}
  <textarea id="copy-box" class="copy-box" readonly hidden></textarea>
  ${mine.length ? `<p class="hint">${zh() ? '先選實際申請的季別與梯次；7 天內截止、已到放榜日的項目優先顯示。' : 'လျှောက်သည့်အကြိမ်ကို ရွေးပါ။ အရေးကြီးသောရက် အရင်ပြသည်။'}</p><div class="mine-list">${mine.map(s => { const st = statusMap[s.id], n = nextStep(s, st), note = draftOf(s.id), canWrite = !cloud.ready || cloud.writable; return `<article class="mine-row st-${st}" data-progress-school="${s.id}"><div class="mr-top"><h3><button class="linkish" data-jump="${s.id}">${esc(s.short)}</button> <span class="km">${s.km} ${t('kmUnit')}</span></h3>${statusSelect(s, 'mine')}</div>
    ${roundControl(s)}
    <p class="next ${n.cls}">${esc(n.text)}</p>
    <div class="note-box"><label for="note-${s.id}" class="sr">${t('note')} ${esc(s.short)}</label><textarea id="note-${s.id}" data-note="${s.id}" aria-describedby="draft-${s.id}" rows="2" maxlength="500" placeholder="${zh() ? '備註：例如「國際處要補高中文件」「已寄出 10/20」' : 'မှတ်ချက်'}" ${canWrite ? '' : 'readonly'}>${esc(note)}</textarea>${canWrite ? `<button class="btn ghost" data-save="${s.id}">${t('save')}</button>` : ''}</div><small class="draft-hint" id="draft-${s.id}" ${Object.hasOwn(drafts, s.id) ? '' : 'hidden'}>${t('draft')}</small></article>`; }).join('')}</div>` : ''}</section>`;
}
function profile() {
  const arcDays = dayDiff(TODAY, data.arcExpiry);
  return `<section class="wrap hero"><div class="hero-text"><p class="eyebrow">${zh() ? `今天 ${ymd(TODAY)}・台灣時間` : `ယနေ့ ${ymd(TODAY)}`}</p><h1>${esc(t('title'))}</h1><p class="lead">${esc(t('lead'))}</p></div>
  <dl class="facts"><div><dt>${zh() ? '華語' : 'တရုတ်စာ'}</dt><dd>TOCFL A2</dd><small>${zh() ? '960 分，差 10 分到 B1；11 月再考' : '960 မှတ်၊ B1 အတွက် 10 မှတ်လို · နိုဝင်ဘာ'}</small></div><div><dt>ARC ${zh() ? '到期' : 'ကုန်ဆုံးရက်'}</dt><dd>2027/06/30</dd><small>${zh() ? `民國 116/06/30・還有 ${arcDays} 天` : `${arcDays} ရက် ကျန်`}</small></div><div><dt>${zh() ? '目標' : 'ရည်မှန်းချက်'}</dt><dd>${zh() ? '學士' : 'ဘွဲ့ကြို'}</dd><small>${zh() ? '拿入學許可 → 變更居留' : 'ဝင်ခွင့်စာ → ARC ပြောင်း'}</small></div></dl></section>`;
}
function overview() {
  const open = data.schools.flatMap(windowsOf).filter(isOpen);
  const schoolCount = items => new Set(items.map(w => w.s.id)).size;
  const tracked = data.schools.filter(s => ['want', 'applied', 'admitted'].includes(statusMap[s.id])).length;
  const stats = [['now', schoolCount(open), 'openSummary'], ['now', schoolCount(open.filter(w => dayDiff(TODAY, w.end) <= 7)), 'urgentSummary'], ['mine', tracked, 'trackedSummary']];
  return `<div class="wrap"><nav class="overview" aria-label="${zh() ? '申請摘要' : 'အကျဉ်းချုပ်'}">${stats.map(([id, n, label]) => `<a href="#${id}"><strong>${n}</strong><span>${t(label)}</span><span aria-hidden="true">↗</span></a>`).join('')}</nav><p class="snapshot">${zh() ? `招生資料查核 ${ymd(data.updated)}。倒數依台灣日期計算；不是即時公告。` : `${ymd(data.updated)} အထိ စစ်ဆေးထားသည်။ အချိန်နှင့်တပြေးညီ မဟုတ်ပါ။`}</p></div>`;
}
function windowCard(w, soon, pending = false) {
  const s = w.s, left = dayDiff(TODAY, w.end), fee = feeView(s.fee), cost = costView(s);
  const urgent = !soon && !pending && left <= 21;
  const leftTxt = pending ? t('pendingStart') : soon ? `${t('opens')} ${mdw(w.start)}` : left === 0 ? t('lastDay') : zh() ? `剩 ${left} 天` : `${left} ${t('days')} ${t('left')}`;
  const res = w.result ? `${t('result')} ${evText(w.result)}` : '';
  return `<article class="ticket ${urgent ? 'urgent' : ''} ${soon ? 'soon' : ''} tier-${s.tier}"><div class="tk-left"><span class="tk-count">${esc(leftTxt)}</span><span class="tk-term">${w.term === 'spring' ? t('springT') : t('fallT')}${w.many ? ` · ${zh() ? `第 ${w.round} 梯` : `${t('round')} ${w.round}`}` : ''}</span></div>
  <div class="tk-main"><h3><button class="linkish" data-jump="${s.id}">${esc(s.short)}</button> <span class="abbr">${esc(s.abbr)}</span> <span class="km">${s.km} ${t('kmUnit')}</span></h3>
  <p class="tk-dates"><span>${w.start ? `${ymd(w.start)} → ` : ''}<b>${t('deadline')} ${mdw(w.end)}</b></span>${res ? `<span>${esc(res)}</span>` : ''}${w.letter ? `<span>${t('letter')} ${md(w.letter)}</span>` : ''}</p>
  <p class="tk-chips">${statusMap[s.id] && statusMap[s.id] !== 'no' ? `<span class="chip mine st-${statusMap[s.id]}">${esc(STATUS.find(x => x[0] === statusMap[s.id])[zh() ? 1 : 2])}</span>` : ''}${lateResult(w.result) ? lateChip() : ''}<span class="chip ${fee.cls}">${t('fFee')} ${esc(fee.text)}</span><span class="chip ${cost.cls}">${zh() ? '第一學期' : 'ကျောင်းလခ'} ${esc(cost.text)}</span></p>
  ${w.note ? `<p class="tk-note">${esc(w.note)}</p>` : ''}</div>
  <div class="tk-go"><a class="btn ${pending ? 'ghost' : ''}" href="${esc(safeURL(s.links.apply))}" target="_blank" rel="noopener noreferrer">${pending ? (zh() ? '向校方確認' : 'ကျောင်းကို မေးရန်') : t('apply')} ↗</a></div></article>`;
}
const lateResult = e => { const d = e && (e.date || e.sort); return !!d && d > data.arcExpiry; };
// An admission letter takes precedence over the public result date.
const lateRound = r => isLateRound(r, data.arcExpiry);
const lateChip = () => `<span class="chip warn">${zh() ? '入學許可先於公開榜單；請核對寄發日' : 'ဝင်ခွင့်စာရက်ကို အတည်ပြုပါ'}</span>`;
function refCount() {
  return zh() ? '往年月份參考' : 'ယခင်နှစ် ကိုးကား';
}
function refCard(w) {
  const s = w.s, r = w.r, fee = feeView(s.fee), cost = costView(s), yr = r.end.sourceYear || r.start?.sourceYear || '';
  return `<article class="ticket ref tier-${s.tier}"><div class="tk-left"><span class="tk-count">${esc(refCount(r))}</span><span class="tk-term">${w.term === 'spring' ? t('springT') : t('fallT')}${w.many ? ` · ${zh() ? `第 ${w.round} 梯` : `${t('round')} ${w.round}`}` : ''}</span></div>
  <div class="tk-main"><h3><button class="linkish" data-jump="${s.id}">${esc(s.short)}</button> <span class="abbr">${esc(s.abbr)}</span> <span class="km">${s.km} ${t('kmUnit')}</span></h3>
  <p class="tk-dates"><span>${t('opens')} ${esc(refLabel(r.start))}</span><span><b>${t('deadline')} ${esc(refLabel(r.end))}</b></span><span>${t('result')} ${esc(refLabel(r.result))}</span></p>
  <p class="tk-chips"><span class="chip past">${zh() ? `往年推算（${esc(yr)}），不是今年正式日期` : `ယခင်နှစ် ${esc(yr)} · ယခုနှစ် တရားဝင်ရက် မဟုတ်`}</span>${lateResult(r.result) ? lateChip() : ''}<span class="chip ${fee.cls}">${t('fFee')} ${esc(fee.text)}</span><span class="chip ${cost.cls}">${zh() ? '第一學期' : 'ကျောင်းလခ'} ${esc(cost.text)}</span></p></div>
  <div class="tk-go"><a class="btn ghost" href="${esc(safeURL(s.links.apply))}" target="_blank" rel="noopener noreferrer">${zh() ? '看官網' : 'ဝက်ဘ်ဆိုက်'} ↗</a></div></article>`;
}
function nowSection() {
  const all = data.schools.flatMap(windowsOf);
  const open = all.filter(isOpen).sort((a, b) => a.end.localeCompare(b.end));
  const soon = all.filter(isSoon).sort((a, b) => a.start.localeCompare(b.start));
  const pending = all.filter(w => isUnconfirmed(w, TODAY)).sort((a, b) => a.end.localeCompare(b.end));
  const ref = data.schools.flatMap(refWindows).sort((a, b) => a.key.localeCompare(b.key) || a.s.km - b.s.km);
  return `<section class="wrap block" id="now"><div class="block-head"><h2>${t('now')}</h2><p>${t('nowSub')}</p></div>
  <div class="tickets">${open.length ? open.map(w => windowCard(w, false)).join('') : `<p class="empty">${t('nothingNow')}</p>`}</div>
  ${soon.length ? `<h3 class="sub">${t('soon')}</h3><div class="tickets">${soon.map(w => windowCard(w, true)).join('')}</div>` : ''}
  ${pending.length ? `<h3 class="sub">${t('pendingStart')}</h3><p class="hint">${zh() ? '已查到官方截止日，但開始日期尚未確認；請先向校方確認是否已開放。' : 'ပိတ်ရက်သာ သိသည်။ စတင်လက်ခံပြီလား ကျောင်းကို မေးပါ။'}</p><div class="tickets pending-windows">${pending.map(w => windowCard(w, false, true)).join('')}</div>` : ''}
  ${ref.length ? `<details class="reference-fold" id="reference-fold" ${refsExpanded ? 'open' : ''}><summary>${zh() ? '本期正式日期待查・往年月份參考' : 'တရားဝင်ရက် အတည်ပြုရန် · ယခင်နှစ် ကိုးကား'} <span>${ref.length} ${zh() ? '梯次' : 'ခု'}</span></summary><p class="hint">${zh() ? '這些梯次尚未核得本期正式日期，不代表校方尚未公告。只顯示往年月份，不做逐日倒數；申請前請打開官方簡章。' : 'ယခင်နှစ် ကိုးကားသာ။ ယခုနှစ် ရက်စွဲ မအတည်ပြုနိုင်သေးပါ။'}</p><div class="tickets">${ref.map(refCard).join('')}</div></details>` : ''}
  <p class="hint">${zh() ? '沒有列在這裡的學校，是學士不收該季、只收研究所，或還沒查到任何日期。' : 'မပါသောကျောင်းများသည် ဘွဲ့ကြို မလက်ခံ သို့မဟုတ် ရက်စွဲ မသိရသေးပါ။'}</p></section>`;
}

// Month-positioned bar from 2026-09 to 2027-08.
const T0 = Date.UTC(2026, 8, 1), T1 = Date.UTC(2027, 7, 1);
const pos = d => Math.max(0, Math.min(100, (Date.parse(d + 'T00:00:00Z') - T0) / (T1 - T0) * 100)).toFixed(2);
function chances() {
  const C = [
    {k: 'spring', a: TODAY, b: '2026-12-19', r: '2026-11 ～ 2027-01', name: ['2027 春', '2027 နွေဦး'], ref: false,
      zh: '現在到 12 月報名，11 月底到 1 月放榜。用現在的 A2。', my: 'ယခု–ဒီဇင်ဘာ လျှောက်၊ နိုဝင်ဘာ–ဇန်နဝါရီ ရလဒ်။ A2 ဖြင့်။'},
    {k: 'fall', a: '2026-12-01', b: '2027-05-31', r: '2027-02 ～ 06', name: ['2027 秋', '2027 ဆောင်းဦး'], ref: false,
      zh: '2026/12 到 2027/5 報名。放榜在 ARC 到期（6/30）之後的梯次，板上已經拿掉。11 月若考到 B1：中教、中科可報的系變多，靜宜第一年補助從「學費」升到「學雜費」。', my: '2026/12–2027/5 လျှောက်။ နိုဝင်ဘာတွင် B1 ရရင် ဌာနပိုများ၊ ပညာသင်ဆု ပိုကောင်း။'},
  ];
  const bands = C.map((c, i) => `<span class="band ${c.k} ${c.ref ? 'ref' : ''}" style="left:${pos(c.a)}%;width:${Math.max(0, pos(c.b) - pos(c.a)).toFixed(2)}%"><i>${i + 1}</i></span>`).join('');
  const ticks = ['2026-09-01', '2027-01-01', '2027-04-01', '2027-07-01', '2027-08-01'].map(d => `<span class="tick" style="left:${pos(d)}%">${d.slice(0, 7).replace('-', '/')}</span>`).join('');
  return `<section class="wrap block" id="chances"><div class="block-head"><h2>${t('chances')}</h2><p>${zh() ? '變更居留要在到期前送件，建議 2027/5 前拿到入學許可。' : '2027/5 မတိုင်ခင် ဝင်ခွင့်စာ ရအောင်လုပ်ပါ။'}</p></div>
  <div class="track" role="img" aria-label="${zh() ? '2026/09 到 2027/08 的報名期與 ARC 到期日' : 'Timeline'}"><div class="rail">${bands}<span class="mk today" style="left:${pos(TODAY)}%"><b>${zh() ? '今天' : 'ယနေ့'}</b></span><span class="mk exam" style="left:${pos('2026-11-15')}%"><b>TOCFL</b></span><span class="mk arc" style="left:${pos('2027-06-30')}%"><b>ARC</b></span></div><div class="ticks">${ticks}</div></div>
  <ol class="chance-list">${C.map((c, i) => `<li class="${c.k}"><span class="num">${i + 1}</span><div><strong>${esc(c.name[zh() ? 0 : 1])}</strong>${c.ref ? `<em>${zh() ? '往年推估' : 'ခန့်မှန်း'}</em>` : ''}<p>${esc(zh() ? c.zh : c.my)}</p><small>${t('result')} ${c.r}</small></div></li>`).join('')}</ol></section>`;
}

function filterBar() {
  const F = [['now', 'filterNow'], ['local', 'filterLocal'], ['sure', 'filterSure'], ['free', 'filterFree'], ['biz', 'filterBiz'], ['mine', 'filterMine']];
  return `<div class="filters" role="group" aria-label="${zh() ? '篩選' : 'စစ်ထုတ်'}">${F.map(([k, w]) => `<button id="f-${k}" class="fchip" data-filter="${k}" aria-pressed="${filters.has(k)}">${esc(t(w))}</button>`).join('')}${filters.size ? `<button class="fclear" data-filter="clear">${t('clear')}</button>` : ''}</div>`;
}
function passes(s) {
  if (filters.has('now') && !windowsOf(s).some(isOpen)) return false;
  if (filters.has('local') && s.commute !== 'local') return false;
  if (filters.has('sure') && !hasSure(s)) return false;
  if (filters.has('free') && s.fee.kind !== 'free') return false;
  if (filters.has('biz') && !(s.bizAdmits || []).length) return false;
  if (filters.has('mine') && !['want', 'applied', 'admitted'].includes(statusMap[s.id])) return false;
  return true;
}
function statusSelect(s, where) {
  const v = statusMap[s.id] || '';
  return `<label class="status st-${v || 'none'}"><span class="sr">${t('status')} ${esc(s.short)}</span><select id="st-${where}-${s.id}" data-status="${s.id}" ${cloud.ready && !cloud.writable ? 'disabled' : ''}>${STATUS.map(([k, a, b]) => `<option value="${k}" ${k === v ? 'selected' : ''}>${esc(zh() ? a : b)}</option>`).join('')}</select></label>`;
}
function compareButton(s) {
  const active = compareIds.includes(s.id);
  return `<button id="compare-card-${s.id}" class="compare-button" data-compare="${s.id}" aria-pressed="${active}">${active ? '✓ ' : '＋ '}${active ? t('compared') : t('addCompare')}<span class="sr"> ${esc(s.short)}</span></button>`;
}
function roundsTable(s, term) {
  const T = s.terms[term];
  const label = term === 'spring' ? t('springT') : t('fallT');
  if (T.ug === 'grad') return `<p class="term-line"><b>${label}</b> ${t('gradOnly')}</p>`;
  if (T.ug === 'none') return `<p class="term-line"><b>${label}</b> ${t('noneTerm')}</p>`;
  if (!T.rounds.length) return `<p class="term-line"><b>${label}</b> ${T.note ? esc(T.note) : t('unknownTerm')}</p>`;
  return `<div class="scroll" tabindex="0" role="region" aria-label="${esc(label)}"><table class="rounds"><caption>${label}</caption><thead><tr><th>${t('round')}</th><th>${t('opens')}</th><th>${t('deadline')}</th><th>${t('result')}</th><th>${t('letter')}</th></tr></thead><tbody>${T.rounds.map((r, i) => `<tr><td>${i + 1}</td>${['start', 'end', 'result'].map(k => `<td class="${evClass(r[k])}">${esc(evText(r[k]))}</td>`).join('')}<td class="${evClass(letterEvent(r))}">${esc(evText(letterEvent(r)))}</td></tr>${r.note ? `<tr class="note-row"><td colspan="5">${esc(r.note)}</td></tr>` : ''}`).join('')}</tbody></table></div>`;
}
function schoolCard(s) {
  const fee = feeView(s.fee), cost = costView(s), sp = springView(s), isOpenCard = openCards.has(s.id);
  const sure = s.aid.sure, rev = s.aid.review;
  const lk = s.links, listLinks = s.lists;
  return `<article class="school tier-${s.tier}" id="s-${s.id}"><div class="s-top"><div class="s-name"><h3>${esc(s.short)} <span class="abbr">${esc(s.abbr)}</span>${isNewSchool(s) ? ` <span class="newb">${t('isNew')}</span>` : ''}</h3><p>${esc(s.name)}・${esc(s.place)}・${s.km} ${t('kmUnit')}</p></div>${statusSelect(s, 'card')}</div>
  <dl class="quad"><div><dt>${t('fSpring')}</dt><dd class="${sp.cls}">${esc(sp.text)}</dd></div><div><dt>${t('fFee')}</dt><dd class="${fee.cls}">${esc(fee.text)}</dd></div><div><dt>${t('fCost')}</dt><dd class="${cost.cls}">${esc(cost.text)}${cost.note ? `<small>${esc(cost.note)}</small>` : ''}</dd></div><div><dt>${zh() ? '新生優惠' : 'ပညာသင်ဆု'}</dt><dd class="${sure ? 'good' : rev && !/未核得|讀不到|沒有/.test(rev) ? 'warn' : 'muted'}">${sure ? (zh() ? '確定有' : 'သေချာ') : rev && !/未核得|讀不到|沒有/.test(rev) ? (zh() ? '要審查' : 'စစ်ဆေး') : (zh() ? '沒有／沒查到' : 'မရှိ/မသိ')}</dd></div></dl>
  ${(() => { const b = bizTop(s), note = noteOf(s.id); const c = []; if (b) c.push(`<span class="chip biz">${t('bizShort')}：${esc(deptShort(b.dept))} ${b.count} ${zh() ? '人' : 'ဦး'}（${esc(b.year)}${b.term === 'spring' ? (zh() ? '春' : '') : b.term === 'fall' ? (zh() ? '秋' : '') : ''}）</span>`); if (note) c.push(`<span class="chip note">✎ ${esc(note.length > 26 ? note.slice(0, 26) + '…' : note)}</span>`); return c.length ? `<p class="s-chips">${c.join('')}</p>` : ''; })()}
  <p class="verdict">${esc(zh() ? s.verdict : s.verdictMy)}</p>${!zh() ? `<p class="verdict-zh" lang="zh-Hant">${esc(s.verdict)}</p>` : ''}
  <div class="school-actions">${compareButton(s)}<button class="more" data-toggle="${s.id}" aria-expanded="${isOpenCard}" aria-controls="d-${s.id}">${isOpenCard ? t('hide') : t('details')}</button></div>
  <div class="s-detail" id="d-${s.id}" ${isOpenCard ? '' : 'hidden'}>
   <section><h4>${t('aidHow')}</h4>${sure ? `<p><span class="tag good">${t('sure')}</span> ${esc(sure)}</p>` : ''}${rev ? `<p><span class="tag warn">${t('review')}</span> ${esc(rev)}</p>` : ''}</section>
   <section><h4>${t('renew')}</h4><p>${esc(s.renew)}</p></section>
   <section class="two"><div><h4>${t('fFee')}</h4><p>${esc(s.fee.text)}${s.fee.year ? `（${esc(s.fee.year)}）` : ''} <a href="${esc(safeURL(s.fee.src))}" target="_blank" rel="noopener noreferrer">${zh() ? '來源' : 'ရင်းမြစ်'} ↗</a></p></div>
   <div><h4>${t('tuition')}</h4><p>${s.tuition ? `${esc(s.tuition.text)}（${esc(s.tuition.year)}${s.tuition.approx ? (zh() ? '，約略' : '') : ''}） <a href="${esc(safeURL(s.tuition.src))}" target="_blank" rel="noopener noreferrer">${zh() ? '來源' : 'ရင်းမြစ်'} ↗</a>` : (zh() ? '還沒查到同年度學費表。' : 'မသိရသေး။')}</p></div></section>
   <section><h4>${t('lang')}</h4><p>${esc(s.lang)}</p></section>
   <section><h4>${t('schedule')}</h4>${roundsTable(s, 'spring')}${roundsTable(s, 'fall')}</section>
   <section><h4>${t('after')}</h4><p>${esc(s.after)}</p></section>
   ${s.readYourself.length ? `<section class="yourself"><h4>${t('yourself')}</h4><ul>${s.readYourself.map(r => `<li><a href="${esc(safeURL(r.url))}" target="_blank" rel="noopener noreferrer">${esc(r.label)} ↗</a><small>${esc(r.why)}</small></li>`).join('')}</ul></section>` : ''}
   ${(s.bizAdmits || []).length || s.bizAdmitsNote ? `<section><h4>${t('biz')}</h4>${(s.bizAdmits || []).length ? `<ul class="linklist">${s.bizAdmits.map(b => `<li><a href="${esc(safeURL(b.src))}" target="_blank" rel="noopener noreferrer">${esc(b.dept)}：${esc(String(b.count))} ${zh() ? '人' : 'ဦး'}（${esc(b.year)}${b.term === 'spring' ? (zh() ? ' 春' : ' နွေဦး') : b.term === 'fall' ? (zh() ? ' 秋' : ' ဆောင်းဦး') : ''}${b.round && !String(b.dept).includes('梯') ? (zh() ? ` 第${esc(String(b.round))}梯` : ` #${esc(String(b.round))}`) : ''}）↗</a></li>`).join('')}</ul>` : ''}${s.bizAdmitsNote ? `<p>${esc(s.bizAdmitsNote)}</p>` : ''}<small class="muted-note">${zh() ? '數字是從官方榜單數出來的；人多代表這個系較常收外籍生，不是錄取率。各梯不能相加。' : 'တရားဝင်စာရင်းမှ ရေတွက်။'}</small></section>` : ''}
   ${listLinks.length ? `<section><h4>${t('lists')}</h4><ul class="linklist">${listLinks.map(n => `<li><a href="${esc(safeURL(n.url))}" target="_blank" rel="noopener noreferrer">${esc(n.year)} ${n.term === 'spring' ? (zh() ? '春' : 'နွေဦး') : (zh() ? '秋' : 'ဆောင်းဦး')}・${esc(n.title)} ↗</a></li>`).join('')}</ul><small class="muted-note">${zh() ? '榜單只放官方連結；上榜人數不是錄取率。' : 'တရားဝင် link သာ။'}</small></section>` : ''}
   <section><h4>${t('links')}</h4><p class="btnrow"><a class="btn" href="${esc(safeURL(lk.apply))}" target="_blank" rel="noopener noreferrer">${t('apply')} ↗</a>${lk.brochureSpring ? `<a class="btn ghost" href="${esc(safeURL(lk.brochureSpring))}" target="_blank" rel="noopener noreferrer">${t('brochure')} ${zh() ? '春' : 'နွေဦး'} ${esc(lk.brochureSpringYear || '')} ↗</a>` : ''}${lk.brochureFall && lk.brochureFall !== lk.brochureSpring ? `<a class="btn ghost" href="${esc(safeURL(lk.brochureFall))}" target="_blank" rel="noopener noreferrer">${t('brochure')} ${zh() ? '秋' : 'ဆောင်းဦး'} ${esc(lk.brochureFallYear || '')} ↗</a>` : ''}<a class="btn ghost" href="./index.html?lang=${lang}&term=spring&q=${encodeURIComponent(s.abbr)}">${zh() ? '原始研究資料' : 'မူရင်း'}</a></p><small class="muted-note">${zh() ? '查核' : 'စစ်ဆေး'} ${ymd(s.checked)}</small></section>
  </div></article>`;
}
const matchQ = s => matchesQuery(s, query);
const selectedSchools = () => data.schools.filter(s => passes(s) && matchQ(s));
const emptyView = () => `<div class="empty"><p>${t('noMatch')}</p><button class="btn ghost" data-action="reset-view">${t('resetView')}</button></div>`;
function schoolsList() {
  const list = selectedSchools();
  const groups = ['A', 'P', 'B', 'C'].map(k => [k, list.filter(s => s.tier === k)]).filter(([, l]) => l.length);
  return {n: list.length, html: groups.length ? groups.map(([k, l]) => `<div class="tier-group"><div class="tier-head tier-${k}"><h3>${esc(TIERS[k][zh() ? 0 : 1])}</h3>${zh() ? `<p>${esc(TIERS[k][2])}</p>` : ''}</div><div class="cards">${l.map(schoolCard).join('')}</div></div>`).join('') : emptyView()};
}
function schoolsSection() {
  const L = schoolsList();
  return `<section class="wrap block" id="schools"><div class="block-head"><h2>${t('schools')} <span class="count" id="school-count" role="status" aria-live="polite">${L.n}/${data.schools.length}</span></h2><p>${zh() ? '分組是我依你的條件（距離、費用、獎學金好拿、早放榜、名校）給的建議。' : 'အုပ်စုခွဲခြင်းသည် အကြံပြုချက်သာ။'}</p></div>
  <div class="searchbox"><input id="q" type="search" value="${esc(query)}" maxlength="150" placeholder="${esc(t('search'))}" aria-label="${esc(t('search'))}" autocomplete="off"><button class="ghost" data-action="clear-search" ${query ? '' : 'hidden'}>${t('clearSearch')}</button></div>${filterBar()}
  <div class="view-tools"><p>${zh() ? '搜尋與篩選同時套用到下方比較表。連結只分享篩選，不含備註。' : 'ရှာဖွေမှုနှင့် စစ်ထုတ်မှုသည် နှိုင်းယှဉ်ဇယားတွင်လည်း အကျုံးဝင်သည်။'}</p><button class="btn ghost" data-action="share-view">${t('shareView')}</button></div><input id="share-box" aria-label="${esc(t('shareView'))}" class="copy-box" readonly hidden>
  <div id="school-list">${L.html}</div></section>`;
}
function sourceLink(url, year = '') {
  if (!url) return '';
  return `<a class="cell-source" href="${esc(safeURL(url))}" target="_blank" rel="noopener noreferrer">${esc(year)} ${zh() ? '官方來源' : 'ရင်းမြစ်'} ↗</a>`;
}
function focusComparison() {
  const schools = compareIds.map(id => data.schools.find(s => s.id === id));
  if (!schools.length) return `<div class="compare-intro"><strong>${zh() ? '先挑 2–3 間，逐項比較' : '၂–၃ ကျောင်းရွေး၍ နှိုင်းယှဉ်ပါ'}</strong><p>${zh() ? '在學校卡片按「加入比較」。費用、語言與獎學金會放在同一張表，搜尋或改篩選也不會清掉已選學校。' : 'ကျောင်းကတ်တွင် ရွေးပါ။ ရှာဖွေမှု ပြောင်းလည်း ရွေးထားမှု မပျောက်ပါ။'}</p></div>`;
  const rows = [
    [t('fCost'), s => { const c = costView(s); return `<strong class="${c.cls}">${esc(c.text)}</strong><small>${esc(c.note)}</small>${sourceLink(s.tuition?.src, s.tuition?.year)}`; }],
    [t('fFee'), s => { const f = feeView(s.fee); return `<strong class="${f.cls}">${esc(f.text)}</strong><small>${esc(s.fee.text)}</small>${sourceLink(s.fee.src, s.fee.year)}`; }],
    [t('fKm'), s => `${s.km} ${t('kmUnit')}<small>${esc(s.place)}</small><small>${zh() ? '距離不等於通勤時間' : 'ခရီးချိန် မဟုတ်ပါ'}</small>`],
    [zh() ? '最近官方截止' : 'နောက်ဆုံးရက်', s => {
      const window = windowsOf(s).filter(w => w.end >= TODAY).sort((a, b) => a.end.localeCompare(b.end))[0];
      if (!window) return `<span class="muted">${zh() ? '沒有尚未截止的官方梯次' : 'တရားဝင်အချိန်ဇယား မရှိပါ'}</span>`;
      const r = roundChoices(s).find(r => r.key === `${window.term}:${window.round}`);
      return `<strong>${ymd(window.end)}</strong><small>${esc(roundName({...window, round: window.round}))}</small>${isUnconfirmed(window, TODAY) ? `<small class="warn">${t('pendingStart')}</small>` : ''}${sourceLink(r?.end?.src || r?.src)}`;
    }],
    [zh() ? '春季可報情況' : 'နွေဦး', s => { const spring = springView(s); return `<span class="${spring.cls}">${esc(spring.text)}</span>`; }],
    [zh() ? '秋季可報梯次放榜' : 'ဆောင်းဦး ရလဒ်', s => { const e = nextResult(s, 'fall', TODAY, data.arcExpiry); return `<span class="${evClass(e)}">${esc(evText(e))}</span>${sourceLink(e?.src, e?.sourceYear)}`; }],
    [t('lang'), s => esc(s.lang)],
    [t('sure'), s => s.aid.sure ? `<span class="good">${esc(s.aid.sure)}</span>` : `<span class="muted">${zh() ? '未核得確定優惠' : 'မအတည်ပြုနိုင်သေး'}</span>`],
    [t('review'), s => esc(s.aid.review || (zh() ? '尚未核得' : 'မသိရသေး'))],
    [t('renew'), s => esc(s.renew)],
    [t('bizShort'), s => { const b = bizTop(s); return b ? `${esc(b.dept)} <b>${b.count}</b> ${zh() ? '人' : 'ဦး'}<small>${esc(b.year)} ${b.term === 'spring' ? (zh() ? '春' : 'နွေဦး') : b.term === 'fall' ? (zh() ? '秋' : 'ဆောင်းဦး') : ''}</small>${sourceLink(b.src)}` : '—'; }],
    [t('status'), s => statusSelect(s, 'focus')],
  ];
  return `<div class="focus-comparison"><div class="focus-head"><h2>${t('focusedCompare')} <span class="count">${schools.length}/3</span></h2><button class="fclear" data-action="clear-compare">${t('clearCompare')}</button></div>
    <p class="hint">${zh() ? '固定保留這幾間，與上方篩選分開。手機可左右滑；學雜費不含申請費、住宿與生活費。各項金額仍須核對來源年度。' : 'ရွေးထားမှုသည် စစ်ထုတ်မှုနှင့် မဆိုင်ပါ။ ဇယားကို ဘယ်ညာရွှေ့ပါ။ အဆောင်နှင့် နေထိုင်စရိတ် မပါ။'}</p>
    <div class="scroll focus-scroll" tabindex="0" role="region" aria-label="${esc(t('focusedCompare'))}"><table class="focus-table" style="--schools:${schools.length}"><caption class="sr">${t('focusedCompare')}：${schools.map(s => esc(s.short)).join('、')}</caption><thead><tr><th scope="col">${zh() ? '比較項目' : 'အချက်အလက်'}</th>${schools.map(s => `<th scope="col"><button class="linkish" data-jump="${s.id}">${esc(s.short)}</button><small>${esc(s.abbr)}</small><button class="remove-compare" data-compare="${s.id}" aria-label="${esc(t('removeCompare') + ' ' + s.short)}">× ${t('removeCompare')}</button></th>`).join('')}</tr></thead>
    <tbody>${rows.map(([label, cell]) => `<tr><th scope="row">${esc(label)}</th>${schools.map(s => `<td data-focus-school="${s.id}">${cell(s)}</td>`).join('')}</tr>`).join('')}</tbody></table></div></div>`;
}
function compareTray() {
  if (!compareIds.length) return '';
  return `<aside class="compare-tray" aria-label="${esc(t('focusedCompare'))}"><div class="wrap"><div><strong>${t('focusedCompare')} ${compareIds.length}/3</strong><small>${compareIds.map(id => esc(data.schools.find(s => s.id === id).short)).join(' · ')}</small></div><a class="btn" href="#compare">${t('goCompare')} ↗</a><button class="fclear" data-action="clear-compare">${t('clearCompare')}</button></div></aside>`;
}
function compareSection() {
  const resultFor = (s, term) => nextResult(s, term, TODAY, data.arcExpiry);
  const resultKey = (s, term) => { const e = resultFor(s, term); return e?.date || e?.sort || null; };
  const direction = sortDirection;
  const compare = (a, b) => compareNullable(a, b, direction);
  const feeAmount = s => ['free', 'paid'].includes(s.fee.kind) ? s.fee.amount : null;
  const keys = {
    tier: (a, b) => (TIER_ORDER[a.tier] - TIER_ORDER[b.tier]) * direction,
    km: (a, b) => compare(a.km, b.km),
    cost: (a, b) => compare(a.semesterCost?.min, b.semesterCost?.min),
    result: (a, b) => compare(resultKey(a, 'spring'), resultKey(b, 'spring')),
    fall: (a, b) => compare(resultKey(a, 'fall'), resultKey(b, 'fall')),
    biz: (a, b) => compare(bizTop(a)?.count, bizTop(b)?.count),
    fee: (a, b) => compare(feeAmount(a), feeAmount(b)),
  };
  const rows = selectedSchools().sort((a, b) => keys[sortKey](a, b) || a.km - b.km);
  const th = (key, label) => key
    ? `<th scope="col" aria-sort="${sortKey === key ? (direction === 1 ? 'ascending' : 'descending') : 'none'}"><button data-sort="${key}">${esc(label)}${sortKey === key ? (direction === 1 ? ' ↑' : ' ↓') : ''}</button></th>`
    : `<th scope="col">${esc(label)}</th>`;
  const resultCell = e => `<td class="num ${evClass(e)}">${e ? esc(evText(e)) : '—'}</td>`;
  return `<section class="wrap block" id="compare" tabindex="-1">${focusComparison()}<div class="block-head all-compare-head"><h2>${zh() ? '全部符合篩選的學校' : 'စစ်ထုတ်ထားသောကျောင်းများ'} <span class="count" id="compare-count">${rows.length}/${data.schools.length}</span></h2>
    <p>${zh() ? '跟隨上方搜尋與篩選。點表頭切換升冪／降冪；未知值排最後。放榜只比較尚未截止的梯次，已報名者請看「我的申請」。' : 'အပေါ်မှ စစ်ထုတ်မှုအတိုင်း။ ခေါင်းစဉ်နှိပ်၍ အစဉ်ပြောင်းပါ။ မသိသောတန်ဖိုး နောက်ဆုံးထားသည်။'}</p></div>
    <p class="hint compare-legend">${zh() ? '學雜費：綠色已扣確定優惠；橘色尚未扣審查型獎學金。商管上榜人數保留原榜單口徑，不是錄取率。表格可左右滑動。' : 'ဇယားကို ဘယ်ညာ ရွှေ့ကြည့်နိုင်သည်။'}</p>
    ${rows.length ? `<div class="scroll" tabindex="0" role="region" aria-label="${esc(t('compare'))}"><table class="cmp"><thead><tr>
      ${th('tier', zh() ? '學校（分組）' : 'ကျောင်း')}${th('km', zh() ? '距離' : 'km')}${th(null, t('fSpring'))}${th('fee', t('fFee'))}${th('cost', t('fCost'))}${th('result', zh() ? '春季可報梯次放榜' : 'နွေဦး ရလဒ်')}${th('fall', zh() ? '秋季可報梯次放榜' : 'ဆောင်းဦး ရလဒ်')}${th('biz', t('bizShort'))}${th(null, t('status'))}
    </tr></thead><tbody>${rows.map(s => {
      const fee = feeView(s.fee), cost = costView(s), spring = springView(s), biz = bizTop(s);
      return `<tr class="tier-${s.tier}"><th scope="row"><button class="linkish" data-jump="${s.id}">${esc(s.short)}</button> <span class="tier-dot">${s.tier === 'P' ? (zh() ? '名校' : '★') : s.tier}</span></th>
        <td class="num">${s.km}</td><td class="${spring.cls}">${esc(spring.text)}</td><td class="${fee.cls}">${esc(fee.text)}</td><td class="${cost.cls} num">${esc(cost.text)}</td>
        ${resultCell(resultFor(s, 'spring'))}${resultCell(resultFor(s, 'fall'))}
        <td class="${biz ? '' : 'muted'}">${biz ? `${esc(deptShort(biz.dept))} <b class="num">${biz.count}</b>` : '—'}</td><td>${statusSelect(s, 'row')}</td></tr>`;
    }).join('')}</tbody></table></div>` : emptyView()}</section>`;
}

function residenceSection() {
  const nia = 'https://www.immigration.gov.tw/5385/7244/7250/7317/%E5%B1%85%E7%95%99/29996/';
  const items = zh() ? [
    ['先確認他能不能換', '先打移民署 1996 或到台中服務站問：以他「現在的居留事由」，拿到入學許可後能不能變更為就學。這一步最重要，報名前就問。'],
    ['拿到入學許可就能送件', '移民署送件須知：已錄取尚未註冊，附入學許可；已註冊，附一個月內在學證明。規費一年效期 1,000 元，到居住地服務站辦。'],
    ['一定要在 ARC 到期前', '延期或變更都要在居留期限屆滿前申請。建議至少提早一個月拿到入學許可。'],
    ['注意獎學金排除條件', '北大、暨大、嘉大、北科等多校獎學金排除「全職工作」或「工作居留」身分；換成就學後打工也要另外申請工作許可。'],
  ] : [
    ['အရင်မေးပါ', 'လက်ရှိ ARC အကြောင်းရင်းဖြင့် ကျောင်းသားအဖြစ် ပြောင်းနိုင်မလား ဆိုတာ 1996 (လူဝင်မှုကြီးကြပ်ရေး) ကို အရင်မေးပါ။'],
    ['ဝင်ခွင့်စာ ရရင် တင်ပါ', 'မှတ်ပုံမတင်ရသေးရင် ဝင်ခွင့်စာ၊ မှတ်ပုံတင်ပြီးရင် ကျောင်းသားအထောက်အထား။ တစ်နှစ် NT$1,000။'],
    ['ARC မကုန်ခင်', 'သက်တမ်းမကုန်ခင် လျှောက်ရမည်။ တစ်လ စောပြီး ဝင်ခွင့်စာ ရထားပါ။'],
    ['ပညာသင်ဆု သတိ', 'အချိန်ပြည့်အလုပ်လုပ်သူ / အလုပ်ARC ကို ပညာသင်ဆု မပေးသော ကျောင်းများ ရှိသည်။'],
  ];
  const prep = zh() ? ['護照、居留證（ARC）影本', '高中畢業證書與成績單（多數要駐外館處驗證，外文要附中/英譯本）', 'TOCFL 成績證明（11 月考到 B1 就換新的）', '財力證明：多數 US$2,500–5,000 或 NT$10–12 萬（依各校簡章）', '讀書計畫、推薦信（依各校簡章）', '收件地址要寫對：中教等學校的入學通知用郵寄']
    : ['ပတ်စ်ပို့၊ ARC မိတ္တူ', 'အထက်တန်း အောင်လက်မှတ်နှင့် အမှတ်စာရင်း (အတည်ပြုချက်လို)', 'TOCFL လက်မှတ်', 'ငွေကြေးအထောက်အထား US$3,000–5,000', 'ပညာရေး အစီအစဉ်၊ ထောက်ခံစာ', 'လိပ်စာ မှန်ကန်စွာ ရေးပါ'];
  return `<section class="wrap block split" id="after"><div><div class="block-head"><h2>${t('residence')}</h2></div><ol class="steps">${items.map(([h, p]) => `<li><strong>${esc(h)}</strong><p>${esc(p)}</p></li>`).join('')}</ol><p><a href="${nia}" target="_blank" rel="noopener noreferrer">${zh() ? '移民署：外國人申請居留及變更居留原因送件須知' : 'လူဝင်မှုကြီးကြပ်ရေး ညွှန်ကြားချက်'} ↗</a></p></div>
  <div><div class="block-head"><h2>${t('prep')}</h2></div><ul class="checklist">${prep.map(p => `<li>${esc(p)}</li>`).join('')}</ul><p class="hint">${zh() ? '目前查到的簡章都沒有另外收「錄取通知書費」或保證金；錄取後要付的是第一學期學雜費、住宿與保險（外國學生健保每月 826 元）。嶺東簡章提到宿舍保證金，但檔案亂碼無法確認。' : 'ဝင်ခွင့်စာအတွက် ကြေးမရှိ။ ဝင်ခွင့်ရပြီးနောက် ကျောင်းလခ၊ အဆောင်၊ အာမခံ ပေးရမည်။'}</p></div></section>`;
}
function render() {
  document.documentElement.lang = zh() ? 'zh-Hant' : 'my';
  document.title = zh() ? '偉銓選校板' : '偉銓 · ကျောင်းရွေးဘုတ်';
  syncStatusMap();
  document.body.classList.toggle('has-comparison', compareIds.length > 0);
  root.innerHTML = `${header()}${navBar()}<main>${profile()}${overview()}${newsSection()}${mineSection()}${nowSection()}${chances()}${schoolsSection()}${compareSection()}${residenceSection()}</main><footer class="wrap foot"><p>${esc(t('foot')).replace('2026/09/29', ymd(data.updated))}</p><p><a href="./index.html?lang=${lang}&weiquan=1">${esc(t('allSite'))}</a></p></footer>${compareTray()}`;
  updateURL();
}
function updateURL() {
  const url = new URL(location.href);
  const values = {lang, q: query, filters: [...filters].sort().join(','), sort: sortKey === 'tier' ? '' : sortKey, dir: sortDirection === -1 ? 'desc' : '', compare: compareIds.join(',')};
  for (const [key, value] of Object.entries(values)) value ? url.searchParams.set(key, value) : url.searchParams.delete(key);
  if (url.href !== location.href) history.replaceState(null, '', url.href);
}
function updateLists() {
  const list = schoolsList();
  document.getElementById('school-list').innerHTML = list.html;
  document.getElementById('school-count').textContent = `${list.n}/${data.schools.length}`;
  const template = document.createElement('template');
  template.innerHTML = compareSection();
  document.getElementById('compare').replaceWith(template.content.firstElementChild);
  document.querySelector('[data-action="clear-search"]').hidden = !query;
  updateURL();
}

// ---- events ----
function toast(msg) { const n = document.querySelector('#wq-toast'); n.textContent = msg; n.classList.add('on'); clearTimeout(toast.t); toast.t = setTimeout(() => n.classList.remove('on'), 3500); }
function progressText() {
  const lines = [zh() ? `偉銓選校進度（${ymd(TODAY)}）` : `偉銓 (${ymd(TODAY)})`];
  for (const [k, a, b] of STATUS.slice(1)) {
    const l = data.schools.filter(s => statusMap[s.id] === k);
    if (!l.length) continue;
    lines.push(`【${zh() ? a : b}】` + l.map(s => { const n = k === 'no' ? null : nextStep(s, k), note = noteOf(s.id), r = resolveRound(s, roundOf(s.id)).round; return s.short + (r ? `・${roundName(r)}` : '') + (n ? `（${n.text}）` : '') + (note ? `：${note}` : ''); }).join('\n  '));
  }
  if (lines.length === 1) lines.push(zh() ? '還沒標記學校。' : '—');
  return lines.join('\n');
}
// ---- progress writes (cloud when available, else this device) ----
function rerenderKeep(focusId) { const y = window.scrollY; render(); window.scrollTo(0, y); if (focusId) document.getElementById(focusId)?.focus({preventScroll: true}); }
const progressWrites = new Map();
async function saveProgress(id, patch) {
  const previous = progressWrites.get(id) || Promise.resolve();
  const pending = previous.catch(() => {}).then(() => writeProgress(id, patch));
  progressWrites.set(id, pending);
  try { return await pending; }
  finally { if (progressWrites.get(id) === pending) progressWrites.delete(id); }
}
async function writeProgress(id, patch) {
  if (!data.schools.some(s => s.id === id)) return false;
  if ('status' in patch && patch.status !== '' && !VALID.has(patch.status)) return false;
  if (patch.round && resolveRound(data.schools.find(s => s.id === id), patch.round).state !== 'valid') return false;
  if (cloud.ready) {
    if (!cloud.writable) { toast(zh() ? '你沒有修改權限' : 'ပြင်ခွင့်မရှိ'); return false; }
    const cur = cloud.docs[id] || {};
    const next = {status: patch.status ?? cur.status ?? '', note: patch.note ?? cur.note ?? '', round: 'round' in patch ? patch.round : cur.round || null, updatedAt: new Date().toISOString()};
    try {
      if (!next.status && !next.note && !next.round) await cloud.db.doc('progress/' + id).delete();
      else await cloud.db.doc('progress/' + id).set(next);
      if (!next.status && !next.note && !next.round) delete cloud.docs[id]; else cloud.docs[id] = next;
      return true;
    } catch (err) {
      if (err?.code === 'invalid_argument') { cloud.writable = false; toast(zh() ? '這個帳號不能修改雲端資料' : 'ပြင်ခွင့်မရှိ'); }
      else toast(zh() ? '沒存成功，請再試一次' : 'မသိမ်းနိုင်ပါ');
      return false;
    }
  }
  for (const [key, current, storageKey] of [['status', localStatus, 'wq-board-status'], ['note', localNotes, 'wq-board-notes'], ['round', localRounds, 'wq-board-rounds']]) {
    if (!(key in patch)) continue;
    const next = {...current};
    if (patch[key]) next[id] = patch[key]; else delete next[id];
    if (!store.set(storageKey, next)) { toast(t('saveError')); return false; }
    if (key === 'status') localStatus = next; else if (key === 'note') localNotes = next; else localRounds = next;
  }
  return true;
}
document.addEventListener('click', async e => {
  const b = e.target.closest('button'); if (!b) return;
  if (b.dataset.compare) {
    const id = b.dataset.compare;
    const fromComparison = !!b.closest('.focus-comparison');
    if (!data.schools.some(s => s.id === id)) return;
    if (!compareIds.includes(id) && compareIds.length === 3) { toast(t('compareLimit')); return; }
    compareIds = compareIds.includes(id) ? compareIds.filter(value => value !== id) : [...compareIds, id];
    if (!store.set('wq-board-compare', compareIds)) toast(t('saveError'));
    const y = window.scrollY; render();
    const focus = fromComparison ? document.querySelector('.focus-comparison [data-compare]') || document.getElementById('compare') : document.getElementById('compare-card-' + id);
    focus?.focus({preventScroll: true}); window.scrollTo(0, y);
    return;
  }
  if (b.dataset.action === 'clear-compare') {
    if (!store.set('wq-board-compare', [])) { toast(t('saveError')); return; }
    compareIds = []; rerenderKeep('compare'); return;
  }
  if (b.dataset.action === 'news') { newsAll = !newsAll; rerenderKeep(); return; }
  if (b.dataset.save) {
    const id = b.dataset.save, v = (document.getElementById('note-' + id)?.value || '').trim().slice(0, 500);
    if (await saveProgress(id, {note: v})) { delete drafts[id]; store.set('wq-board-drafts', drafts); toast(t('saved')); rerenderKeep('note-' + id); }
    return;
  }
  if (b.dataset.action === 'upload') {
    let success = true;
    for (const [k, v] of Object.entries(localStatus)) if (VALID.has(v) && !cloud.docs[k]) {
      const s = data.schools.find(s => s.id === k), r = s && resolveRound(s, localRounds[k]).state === 'valid' ? localRounds[k] : null;
      success = await saveProgress(k, {status: v, note: localNotes[k] || '', round: r}) && success;
    }
    if (success) toast(zh() ? '已放上雲端' : 'တင်ပြီး'); rerenderKeep(); return;
  }
  if (b.dataset.lang) { lang = b.dataset.lang; store.set('wq-lang', lang); render(); document.getElementById('lang-' + lang)?.focus(); return; }
  if (b.dataset.toggle) { const id = b.dataset.toggle; openCards.has(id) ? openCards.delete(id) : openCards.add(id); const d = document.getElementById('d-' + id); d.hidden = !openCards.has(id); b.setAttribute('aria-expanded', String(openCards.has(id))); b.textContent = openCards.has(id) ? t('hide') : t('details'); return; }
  if (b.dataset.filter) { const k = b.dataset.filter; if (k === 'clear') filters.clear(); else filters.has(k) ? filters.delete(k) : filters.add(k); const y = window.scrollY; render(); window.scrollTo(0, y); document.getElementById('f-' + k)?.focus({preventScroll: true}); return; }
  if (b.dataset.sort) { sortDirection = sortKey === b.dataset.sort ? -sortDirection : b.dataset.sort === 'biz' ? -1 : 1; sortKey = b.dataset.sort; const y = window.scrollY; render(); window.scrollTo(0, y); document.querySelector(`[data-sort="${sortKey}"]`)?.focus({preventScroll: true}); return; }
  if (b.dataset.jump) { const id = b.dataset.jump; if (!document.getElementById('s-' + id)) { filters.clear(); query = ''; } openCards.add(id); render(); const el = document.getElementById('s-' + id); el?.scrollIntoView({block: 'start'}); el?.querySelector('.more')?.focus({preventScroll: true}); return; }
  if (b.dataset.action === 'reset-view') { filters.clear(); query = ''; rerenderKeep('q'); return; }
  if (b.dataset.action === 'clear-search') { query = ''; document.getElementById('q').value = ''; updateLists(); document.getElementById('q').focus({preventScroll: true}); return; }
  if (b.dataset.action === 'share-view') {
    const url = new URL(location.href); url.hash = compareIds.length ? 'compare' : 'schools'; url.searchParams.delete('today'); url.searchParams.set('compare', compareIds.join(','));
    try { await navigator.clipboard.writeText(url.href); toast(t('viewCopied')); }
    catch { const box = document.getElementById('share-box'); box.hidden = false; box.value = url.href; box.focus(); box.select(); toast(t('copyFail')); }
    return;
  }
  if (b.dataset.action === 'copy') {
    const text = progressText();
    try { await navigator.clipboard.writeText(text); toast(t('copied')); }
    catch { const box = document.getElementById('copy-box'); box.hidden = false; box.value = text; box.focus(); box.select(); toast(t('copyFail')); }
  }
});
document.addEventListener('change', async e => {
  const n = e.target;
  if (n.dataset?.round) {
    const s = data.schools.find(s => s.id === n.dataset.round); if (!s) return;
    if (n.value && !selectRound(s, n.value)) { rerenderKeep(n.id); return; }
    await saveProgress(s.id, {round: n.value ? selectRound(s, n.value) : null});
    rerenderKeep(n.id); return;
  }
  if (!n.dataset?.status) return;
  const id = n.dataset.status, focusId = n.id;
  if (await saveProgress(id, {status: n.value})) rerenderKeep(focusId); else rerenderKeep(focusId);
});
document.addEventListener('input', e => {
  if (e.target.dataset?.note) {
    const id = e.target.dataset.note;
    drafts[id] = e.target.value.slice(0, 500);
    if (!store.set('wq-board-drafts', drafts)) toast(t('saveError'));
    const hint = document.getElementById('draft-' + id); if (hint) hint.hidden = false;
    return;
  }
  if (e.target.id === 'q') { query = e.target.value.slice(0, 150); updateLists(); }
});
document.addEventListener('toggle', e => { if (e.target.id === 'reference-fold') refsExpanded = e.target.open; }, true);

// Light up shared progress when this view can use the artifact database. Never blocks first paint.
async function initCloud() {
  if (!window.claude?.use) return;
  try {
    const [db, user] = await Promise.all([window.claude.use('db'), window.claude.use('user')]);
    if (!db) return;
    const can = user ? await user.can('data.write') : null;
    cloud.db = db; cloud.writable = can !== false;
    db.collection('progress').onSnapshot(snap => {
      const docs = {};
      for (const d of snap.docs) { if (!data.schools.some(s => s.id === d.id)) continue; const v = d.data() || {}; docs[d.id] = {status: VALID.has(v.status) ? v.status : '', note: typeof v.note === 'string' ? v.note.slice(0, 500) : '', round: record(v.round) && typeof v.round.key === 'string' && typeof v.round.signature === 'string' ? {key: v.round.key, signature: v.round.signature} : null}; }
      cloud.docs = docs; cloud.ready = true;
      const a = document.activeElement;
      if (a && (a.dataset?.note || a.id === 'q')) return; // don't wipe what someone is typing
      rerenderKeep(a?.id);
    }, () => {});
  } catch { /* stay on this-device mode */ }
}

try {
  const r = await fetch('./wq-board.json'); if (!r.ok) throw new Error('data');
  data = await r.json();
  const known = new Set(data.schools.map(s => s.id));
  compareIds = cleanComparison(compareIds, known);
  if (qs.has('compare')) store.set('wq-board-compare', compareIds);
  localRounds = Object.fromEntries(Object.entries(localRounds).filter(([id, value]) => known.has(id) && record(value) && typeof value.key === 'string' && typeof value.signature === 'string').map(([id, value]) => [id, {key: value.key.slice(0, 20), signature: value.signature.slice(0, 20)}]));
  localStatus = Object.fromEntries(Object.entries(localStatus).filter(([id, value]) => known.has(id) && VALID.has(value)));
  for (const [kind, entries] of [['notes', localNotes], ['drafts', drafts]]) {
    const clean = Object.fromEntries(Object.entries(entries).filter(([id, value]) => known.has(id) && typeof value === 'string').map(([id, value]) => [id, value.slice(0, 500)]));
    if (kind === 'notes') localNotes = clean; else drafts = clean;
  }
  render();
  initCloud();
  let anchor; try { anchor = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch { /* ignore malformed anchors */ }
  anchor?.scrollIntoView();
} catch (err) {
  root.innerHTML = '<main class="wq-loading"><p>資料載入失敗，請重新整理。<br>အချက်အလက် မတင်နိုင်ပါ။</p></main>';
  console.error(err);
}
