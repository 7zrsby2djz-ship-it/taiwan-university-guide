// 偉銓選校板 — decision board for the 39 personal schools.
// Data: ./wq-board.json (built by research/weiquan-board-2026-09-29/build_board.py).
// Only official dates are shown as exact dates; past-year references are labelled.
const root = document.querySelector('#board');
const esc = v => String(v ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const safeURL = u => { try { const x = new URL(u, location.href); return ['http:','https:'].includes(x.protocol) ? x.href : '#'; } catch { return '#'; } };
const store = {
  get(k, f) { try { const v = JSON.parse(localStorage.getItem(k)); return v ?? f; } catch { return f; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} },
};

// ---- today (Taiwan time); ?today=YYYY-MM-DD lets testers pin a date ----
const qs = new URLSearchParams(location.search);
const TODAY = /^\d{4}-\d{2}-\d{2}$/.test(qs.get('today') || '') ? qs.get('today')
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
};
const STATUS = [['', '還沒決定', 'မဆုံးဖြတ်ရသေး'], ['want', '要報', 'လျှောက်မည်'], ['applied', '已報名', 'လျှောက်ပြီး'], ['admitted', '錄取', 'ဝင်ခွင့်ရ'], ['no', '不考慮', 'မလျှောက်']];
const TIERS = {
  A: ['台中近又省錢・首選', 'ထိုင်ချုံးနီး · ငွေသက်သာ · ဦးစားပေး', '市區或近郊、公立或第一年有確定優惠。'],
  P: ['知名學校・遠或貴也值得考慮', 'နာမည်ကြီးကျောင်း · ဝေး/ဈေးကြီးလည်း စဉ်းစားထိုက်', '你說過，名校上了可以多花一點。'],
  B: ['備案・條件普通或資料要你自己看', 'အရန်ကျောင်းများ', '台中私立科大、較遠的公立；有些資料讀不到。'],
  C: ['暫不優先', 'ဦးစားမပေး', '要搬家又不是名校、醫學類學費高，或學士不能報春季。'],
};
const TIER_ORDER = {A: 0, P: 1, B: 2, C: 3};

let data, lang = store.get('wq-lang', 'zh'), statusMap = store.get('wq-board-status', {}), filters = new Set(), sortKey = 'tier', openCards = new Set();
if (!['zh', 'my'].includes(lang)) lang = 'zh';
if (['zh', 'my'].includes(qs.get('lang'))) lang = qs.get('lang');
if (!statusMap || typeof statusMap !== 'object') statusMap = {};
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
  return `${t('past')} ${e.label || ''}`.trim();
}
const evClass = e => !e ? 'none' : e.status === 'official' ? 'ok' : e.status === 'conflict' ? 'bad' : 'past';

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
  if (live) return {cls: 'good', text: (zh() ? '報到 ' : '') + md(live.end) + (zh() ? '' : ' အထိ')};
  if (w.length) return {cls: 'muted', text: zh() ? '已截止' : 'ပိတ်ပြီး'};
  if (T.ug === 'has') return {cls: 'muted', text: zh() ? '只有往年參考' : 'ယခင်နှစ်သာ'};
  return {cls: 'muted', text: zh() ? '沒查到' : 'မသိရ'};
}

// Official undergraduate windows with an exact deadline.
function windowsOf(s) {
  const out = [];
  for (const term of ['spring', 'fall']) (s.terms[term].rounds || []).forEach((r, i) => {
    if (r.end?.status !== 'official' || !r.end.date) return;
    if (lateRound(r)) return; // result after ARC expiry: dropped
    out.push({s, term, round: i + 1, many: s.terms[term].rounds.length > 1, start: r.start?.status === 'official' ? r.start.date : null, end: r.end.date, result: r.result, letter: r.letter, note: r.note});
  });
  return out;
}
// Rounds whose deadline is only a past-year reference (this year's dates not published yet).
function refWindows(s) {
  const out = [];
  for (const term of ['spring', 'fall']) (s.terms[term].rounds || []).forEach((r, i) => {
    const e = r.end;
    if (!e || e.status === 'official' || e.status === 'conflict' || !e.sort || e.sort < TODAY) return;
    if (lateRound(r)) return; // result after ARC expiry: dropped
    if (term === 'spring' && s.ownership === 'public') return; // national spring is graduate-only or unverified; live undergrad spring tickets stay above
    out.push({s, term, round: i + 1, many: s.terms[term].rounds.length > 1, r, key: (r.start && r.start.sort) || e.sort});
  });
  return out;
}
const refLabel = e => !e ? '—' : e.status === 'conflict' ? t('diff') : (e.label || '—');
const isOpen = w => w.end >= TODAY && (!w.start || w.start <= TODAY);
const isSoon = w => w.start && w.start > TODAY;
const hasSure = s => ['full', 'half', 'minus', 'lang', 'mostly'].includes(s.firstYearKind);

// ---- sections ----
function header() {
  return `<header class="bar"><div class="wrap bar-in"><a class="brand" href="./index.html?lang=${lang}&weiquan=1" title="${esc(t('allSite'))}"><span class="mark" aria-hidden="true">偉</span><span><strong>${esc(t('title'))}</strong><small>${zh() ? '給第一次上大學的他' : 'ပထမဆုံး တက္ကသိုလ်တက်မည့်သူအတွက်'}</small></span></a>
  <div class="bar-actions"><a class="ghost" href="./index.html?lang=${lang}&weiquan=1">${esc(t('allSite'))}</a><div class="seg" role="group" aria-label="Language"><button id="lang-zh" data-lang="zh" aria-pressed="${zh()}">繁中</button><button id="lang-my" data-lang="my" aria-pressed="${!zh()}" lang="my">မြန်မာ</button></div></div></div></header>`;
}
function profile() {
  const arcDays = dayDiff(TODAY, data.arcExpiry);
  return `<section class="wrap hero"><div class="hero-text"><p class="eyebrow">${zh() ? `今天 ${ymd(TODAY)}・台灣時間` : `ယနေ့ ${ymd(TODAY)}`}</p><h1>${esc(t('title'))}</h1><p class="lead">${esc(t('lead'))}</p></div>
  <dl class="facts"><div><dt>${zh() ? '華語' : 'တရုတ်စာ'}</dt><dd>TOCFL A2</dd><small>${zh() ? '960 分，差 10 分到 B1；11 月再考' : '960 မှတ်၊ B1 အတွက် 10 မှတ်လို · နိုဝင်ဘာ'}</small></div><div><dt>ARC ${zh() ? '到期' : 'ကုန်ဆုံးရက်'}</dt><dd>2027/06/30</dd><small>${zh() ? `民國 116/06/30・還有 ${arcDays} 天` : `${arcDays} ရက် ကျန်`}</small></div><div><dt>${zh() ? '目標' : 'ရည်မှန်းချက်'}</dt><dd>${zh() ? '學士' : 'ဘွဲ့ကြို'}</dd><small>${zh() ? '拿入學許可 → 變更居留' : 'ဝင်ခွင့်စာ → ARC ပြောင်း'}</small></div></dl></section>`;
}
function windowCard(w, soon) {
  const s = w.s, left = dayDiff(TODAY, w.end), fee = feeView(s.fee), cost = costView(s);
  const urgent = !soon && left <= 21;
  const leftTxt = soon ? `${t('opens')} ${mdw(w.start)}` : left === 0 ? t('lastDay') : zh() ? `剩 ${left} 天` : `${left} ${t('days')} ${t('left')}`;
  const res = w.result ? `${t('result')} ${evText(w.result)}` : '';
  return `<article class="ticket ${urgent ? 'urgent' : ''} ${soon ? 'soon' : ''} tier-${s.tier}"><div class="tk-left"><span class="tk-count">${esc(leftTxt)}</span><span class="tk-term">${w.term === 'spring' ? t('springT') : t('fallT')}${w.many ? ` · ${zh() ? `第 ${w.round} 梯` : `${t('round')} ${w.round}`}` : ''}</span></div>
  <div class="tk-main"><h3><button class="linkish" data-jump="${s.id}">${esc(s.short)}</button> <span class="abbr">${esc(s.abbr)}</span> <span class="km">${s.km} ${t('kmUnit')}</span></h3>
  <p class="tk-dates"><span>${w.start ? `${ymd(w.start)} → ` : ''}<b>${t('deadline')} ${mdw(w.end)}</b></span>${res ? `<span>${esc(res)}</span>` : ''}${w.letter ? `<span>${t('letter')} ${md(w.letter)}</span>` : ''}</p>
  <p class="tk-chips">${lateResult(w.result) ? lateChip() : ''}<span class="chip ${fee.cls}">${t('fFee')} ${esc(fee.text)}</span><span class="chip ${cost.cls}">${zh() ? '第一學期' : 'ကျောင်းလခ'} ${esc(cost.text)}</span></p>
  ${w.note ? `<p class="tk-note">${esc(w.note)}</p>` : ''}</div>
  <div class="tk-go"><a class="btn" href="${esc(safeURL(s.links.apply))}" target="_blank" rel="noopener noreferrer">${t('apply')} ↗</a></div></article>`;
}
const lateResult = e => { const d = e && (e.date || e.sort); return !!d && d > data.arcExpiry; };
// Result after ARC expiry, or no result date and the deadline itself is after ARC expiry.
const lateRound = r => lateResult(r.result) || (!(r.result && (r.result.date || r.result.sort)) && ((r.end && (r.end.date || r.end.sort)) || '') > data.arcExpiry);
const lateChip = () => `<span class="chip bad">${zh() ? '往年放榜在 ARC 到期後，來不及' : 'ARC ကုန်ပြီးမှ ရလဒ် · မမီ'}</span>`;
function refCount(r) {
  const toStart = r.start?.sort ? dayDiff(TODAY, r.start.sort) : -1, toEnd = dayDiff(TODAY, r.end.sort);
  if (toStart > 0) return zh() ? `約 ${toStart} 天後開始` : `~${toStart} ရက်နောက် ဖွင့်`;
  return zh() ? `約剩 ${toEnd} 天` : `~${toEnd} ရက် ကျန်`;
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
  const ref = data.schools.flatMap(refWindows).sort((a, b) => a.key.localeCompare(b.key) || a.s.km - b.s.km);
  return `<section class="wrap block" id="now"><div class="block-head"><h2>${t('now')}</h2><p>${t('nowSub')}</p></div>
  <div class="tickets">${open.length ? open.map(w => windowCard(w, false)).join('') : `<p class="empty">${t('nothingNow')}</p>`}</div>
  ${soon.length ? `<h3 class="sub">${t('soon')}</h3><div class="tickets">${soon.map(w => windowCard(w, true)).join('')}</div>` : ''}
  ${ref.length ? `<h3 class="sub">${zh() ? '今年還沒公布・往年日期參考' : 'ယခုနှစ် မကြေညာသေး · ယခင်နှစ် ရက်စွဲ'}</h3><p class="hint">${zh() ? '學校還沒公布這一期日期，倒數天數是照去年的日期推算，只用來抓大概時間。正式日期出來後會換成上面的官方日期。國立學校的春季班已拿掉（多數只收研究所）。' : 'ယခင်နှစ် လများသာ။ တရားဝင်ရက် ထွက်ရင် ပြောင်းမည်။'}</p><div class="tickets">${ref.map(refCard).join('')}</div>` : ''}
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
  const F = [['now', 'filterNow'], ['local', 'filterLocal'], ['sure', 'filterSure'], ['free', 'filterFree']];
  return `<div class="filters" role="group" aria-label="${zh() ? '篩選' : 'စစ်ထုတ်'}">${F.map(([k, w]) => `<button id="f-${k}" class="fchip" data-filter="${k}" aria-pressed="${filters.has(k)}">${esc(t(w))}</button>`).join('')}${filters.size ? `<button class="fclear" data-filter="clear">${t('clear')}</button>` : ''}</div>`;
}
function passes(s) {
  if (filters.has('now') && !windowsOf(s).some(isOpen)) return false;
  if (filters.has('local') && s.commute !== 'local') return false;
  if (filters.has('sure') && !hasSure(s)) return false;
  if (filters.has('free') && s.fee.kind !== 'free') return false;
  return true;
}
function statusSelect(s, where) {
  const v = statusMap[s.id] || '';
  return `<label class="status st-${v || 'none'}"><span class="sr">${t('status')} ${esc(s.short)}</span><select id="st-${where}-${s.id}" data-status="${s.id}">${STATUS.map(([k, a, b]) => `<option value="${k}" ${k === v ? 'selected' : ''}>${esc(zh() ? a : b)}</option>`).join('')}</select></label>`;
}
function roundsTable(s, term) {
  const T = s.terms[term];
  const label = term === 'spring' ? t('springT') : t('fallT');
  if (T.ug === 'grad') return `<p class="term-line"><b>${label}</b> ${t('gradOnly')}</p>`;
  if (T.ug === 'none') return `<p class="term-line"><b>${label}</b> ${t('noneTerm')}</p>`;
  if (!T.rounds.length) return `<p class="term-line"><b>${label}</b> ${t('unknownTerm')}</p>`;
  return `<div class="scroll"><table class="rounds"><caption>${label}</caption><thead><tr><th>${t('round')}</th><th>${t('opens')}</th><th>${t('deadline')}</th><th>${t('result')}</th><th>${t('letter')}</th></tr></thead><tbody>${T.rounds.map((r, i) => `<tr><td>${i + 1}</td>${['start', 'end', 'result'].map(k => `<td class="${evClass(r[k])}">${esc(evText(r[k]))}</td>`).join('')}<td class="${r.letter ? 'ok' : 'none'}">${r.letter ? ymd(r.letter) : '—'}</td></tr>${r.note ? `<tr class="note-row"><td colspan="5">${esc(r.note)}</td></tr>` : ''}`).join('')}</tbody></table></div>`;
}
function schoolCard(s) {
  const fee = feeView(s.fee), cost = costView(s), sp = springView(s), isOpenCard = openCards.has(s.id);
  const sure = s.aid.sure, rev = s.aid.review;
  const lk = s.links, listLinks = s.lists;
  return `<article class="school tier-${s.tier}" id="s-${s.id}"><div class="s-top"><div class="s-name"><h3>${esc(s.short)} <span class="abbr">${esc(s.abbr)}</span></h3><p>${esc(s.name)}・${esc(s.place)}・${s.km} ${t('kmUnit')}</p></div>${statusSelect(s, 'card')}</div>
  <dl class="quad"><div><dt>${t('fSpring')}</dt><dd class="${sp.cls}">${esc(sp.text)}</dd></div><div><dt>${t('fFee')}</dt><dd class="${fee.cls}">${esc(fee.text)}</dd></div><div><dt>${t('fCost')}</dt><dd class="${cost.cls}">${esc(cost.text)}${cost.note ? `<small>${esc(cost.note)}</small>` : ''}</dd></div><div><dt>${zh() ? '新生優惠' : 'ပညာသင်ဆု'}</dt><dd class="${sure ? 'good' : rev && !/未核得|讀不到|沒有/.test(rev) ? 'warn' : 'muted'}">${sure ? (zh() ? '確定有' : 'သေချာ') : rev && !/未核得|讀不到|沒有/.test(rev) ? (zh() ? '要審查' : 'စစ်ဆေး') : (zh() ? '沒有／沒查到' : 'မရှိ/မသိ')}</dd></div></dl>
  <p class="verdict">${esc(zh() ? s.verdict : s.verdictMy)}</p>${!zh() ? `<p class="verdict-zh" lang="zh-Hant">${esc(s.verdict)}</p>` : ''}
  <button class="more" data-toggle="${s.id}" aria-expanded="${isOpenCard}" aria-controls="d-${s.id}">${isOpenCard ? t('hide') : t('details')}</button>
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
function schoolsSection() {
  const list = data.schools.filter(passes);
  const groups = ['A', 'P', 'B', 'C'].map(k => [k, list.filter(s => s.tier === k)]).filter(([, l]) => l.length);
  return `<section class="wrap block" id="schools"><div class="block-head"><h2>${t('schools')} <span class="count">${list.length}/${data.schools.length}</span></h2><p>${zh() ? '分組是我依你的條件（距離、費用、獎學金好拿、早放榜、名校）給的建議。' : 'အုပ်စုခွဲခြင်းသည် အကြံပြုချက်သာ။'}</p></div>${filterBar()}
  ${groups.length ? groups.map(([k, l]) => `<div class="tier-group"><div class="tier-head tier-${k}"><h3>${esc(TIERS[k][zh() ? 0 : 1])}</h3>${zh() ? `<p>${esc(TIERS[k][2])}</p>` : ''}</div><div class="cards">${l.map(schoolCard).join('')}</div></div>`).join('') : `<p class="empty">${t('noMatch')}</p>`}</section>`;
}
function compareSection() {
  const firstResult = s => { const r = windowsOf(s).filter(w => w.term === 'spring' && w.result?.status === 'official' && w.result.date).map(w => w.result.date).sort()[0]; return r || null; };
  const cmp = (a, b) => a == null && b == null ? 0 : a == null ? 1 : b == null ? -1 : a < b ? -1 : a > b ? 1 : 0;
  const keys = {tier: (a, b) => TIER_ORDER[a.tier] - TIER_ORDER[b.tier] || a.km - b.km, km: (a, b) => a.km - b.km, cost: (a, b) => cmp(a.semesterCost?.min, b.semesterCost?.min), result: (a, b) => cmp(firstResult(a), firstResult(b))};
  const rows = [...data.schools].sort((a, b) => keys[sortKey](a, b) || a.km - b.km);
  const th = (k, label) => k ? `<th scope="col" aria-sort="${sortKey === k ? 'ascending' : 'none'}"><button data-sort="${k}">${esc(label)}${sortKey === k ? ' ↓' : ''}</button></th>` : `<th scope="col">${esc(label)}</th>`;
  return `<section class="wrap block" id="compare"><div class="block-head"><h2>${t('compare')}</h2><p>${zh() ? '點表頭排序。第一學期學雜費：綠色＝已扣確定優惠；橘色＝沒拿獎學金時的最高額。' : 'ခေါင်းစဉ်ကို နှိပ်၍ စီပါ။'}</p></div>
  <div class="scroll"><table class="cmp"><thead><tr>${th('tier', zh() ? '學校（分組）' : 'ကျောင်း')}${th('km', zh() ? '距離' : 'km')}${th(null, t('fSpring'))}${th(null, t('fFee'))}${th('cost', t('fCost'))}${th('result', zh() ? '春季最早放榜' : 'နွေဦး ရလဒ်')}${th(null, t('status'))}</tr></thead>
  <tbody>${rows.map(s => { const f = feeView(s.fee), c = costView(s), sp = springView(s), r = firstResult(s); return `<tr class="tier-${s.tier}"><th scope="row"><button class="linkish" data-jump="${s.id}">${esc(s.short)}</button> <span class="tier-dot">${s.tier === 'P' ? (zh() ? '名校' : '★') : s.tier}</span></th><td class="num">${s.km}</td><td class="${sp.cls}">${esc(sp.text)}</td><td class="${f.cls}">${esc(f.text)}</td><td class="${c.cls} num">${esc(c.text)}</td><td class="num">${r ? md(r) : '—'}</td><td>${statusSelect(s, 'row')}</td></tr>`; }).join('')}</tbody></table></div></section>`;
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
  const prep = zh() ? ['護照、居留證（ARC）影本', '高中畢業證書與成績單（多數要駐外館處驗證，外文要附中/英譯本）', 'TOCFL 成績證明（11 月考到 B1 就換新的）', '財力證明：多數 US$3,000–5,000 或 NT$10 萬；中山醫要 US$10,000', '讀書計畫、推薦信（依各校簡章）', '收件地址要寫對：中教等學校的入學通知用郵寄']
    : ['ပတ်စ်ပို့၊ ARC မိတ္တူ', 'အထက်တန်း အောင်လက်မှတ်နှင့် အမှတ်စာရင်း (အတည်ပြုချက်လို)', 'TOCFL လက်မှတ်', 'ငွေကြေးအထောက်အထား US$3,000–5,000', 'ပညာရေး အစီအစဉ်၊ ထောက်ခံစာ', 'လိပ်စာ မှန်ကန်စွာ ရေးပါ'];
  return `<section class="wrap block split" id="after"><div><div class="block-head"><h2>${t('residence')}</h2></div><ol class="steps">${items.map(([h, p]) => `<li><strong>${esc(h)}</strong><p>${esc(p)}</p></li>`).join('')}</ol><p><a href="${nia}" target="_blank" rel="noopener noreferrer">${zh() ? '移民署：外國人申請居留及變更居留原因送件須知' : 'လူဝင်မှုကြီးကြပ်ရေး ညွှန်ကြားချက်'} ↗</a></p></div>
  <div><div class="block-head"><h2>${t('prep')}</h2></div><ul class="checklist">${prep.map(p => `<li>${esc(p)}</li>`).join('')}</ul><p class="hint">${zh() ? '目前查到的簡章都沒有另外收「錄取通知書費」或保證金；錄取後要付的是第一學期學雜費、住宿與保險（外國學生健保每月 826 元）。嶺東簡章提到宿舍保證金，但檔案亂碼無法確認。' : 'ဝင်ခွင့်စာအတွက် ကြေးမရှိ။ ဝင်ခွင့်ရပြီးနောက် ကျောင်းလခ၊ အဆောင်၊ အာမခံ ပေးရမည်။'}</p></div></section>`;
}
function progressBar() {
  const counts = Object.fromEntries(STATUS.map(([k]) => [k, 0]));
  for (const s of data.schools) counts[statusMap[s.id] || '']++;
  const parts = STATUS.slice(1).filter(([k]) => counts[k]).map(([k, a, b]) => `<span class="st-${k}">${esc(zh() ? a : b)} <b>${counts[k]}</b></span>`).join('');
  return `<div class="wrap progress"><div class="prog-in"><strong>${t('status')}</strong>${parts || `<span class="muted">${zh() ? '在每間學校右上角選「要報」「已報名」，這裡會統計，也能複製給他看。' : 'ကျောင်းတိုင်းတွင် အခြေအနေ ရွေးပါ။'}</span>`}<button class="btn ghost" data-action="copy">${t('copy')}</button></div><textarea id="copy-box" class="copy-box" readonly hidden></textarea></div>`;
}
function render() {
  document.documentElement.lang = zh() ? 'zh-Hant' : 'my';
  document.title = zh() ? '偉銓選校板' : '偉銓 · ကျောင်းရွေးဘုတ်';
  root.innerHTML = `${header()}<main>${profile()}${progressBar()}${nowSection()}${chances()}${schoolsSection()}${compareSection()}${residenceSection()}</main><footer class="wrap foot"><p>${esc(t('foot'))}</p><p><a href="./index.html?lang=${lang}&weiquan=1">${esc(t('allSite'))}</a></p></footer>`;
}

// ---- events ----
function toast(msg) { const n = document.querySelector('#wq-toast'); n.textContent = msg; n.classList.add('on'); clearTimeout(toast.t); toast.t = setTimeout(() => n.classList.remove('on'), 3500); }
function progressText() {
  const lines = [zh() ? `偉銓選校進度（${ymd(TODAY)}）` : `偉銓 (${ymd(TODAY)})`];
  for (const [k, a, b] of STATUS.slice(1)) {
    const l = data.schools.filter(s => statusMap[s.id] === k);
    if (!l.length) continue;
    lines.push(`【${zh() ? a : b}】` + l.map(s => { const w = windowsOf(s).filter(isOpen).sort((x, y) => x.end.localeCompare(y.end))[0]; return s.short + (w && k === 'want' ? `（${t('deadline')} ${md(w.end)}）` : ''); }).join('、'));
  }
  if (lines.length === 1) lines.push(zh() ? '還沒標記學校。' : '—');
  return lines.join('\n');
}
document.addEventListener('click', async e => {
  const b = e.target.closest('button'); if (!b) return;
  if (b.dataset.lang) { lang = b.dataset.lang; store.set('wq-lang', lang); render(); document.getElementById('lang-' + lang)?.focus(); return; }
  if (b.dataset.toggle) { const id = b.dataset.toggle; openCards.has(id) ? openCards.delete(id) : openCards.add(id); const d = document.getElementById('d-' + id); d.hidden = !openCards.has(id); b.setAttribute('aria-expanded', String(openCards.has(id))); b.textContent = openCards.has(id) ? t('hide') : t('details'); return; }
  if (b.dataset.filter) { const k = b.dataset.filter; if (k === 'clear') filters.clear(); else filters.has(k) ? filters.delete(k) : filters.add(k); const y = window.scrollY; render(); window.scrollTo(0, y); document.getElementById('f-' + k)?.focus({preventScroll: true}); return; }
  if (b.dataset.sort) { sortKey = b.dataset.sort; const y = window.scrollY; render(); window.scrollTo(0, y); document.querySelector(`[data-sort="${sortKey}"]`)?.focus({preventScroll: true}); return; }
  if (b.dataset.jump) { const id = b.dataset.jump; if (!document.getElementById('s-' + id)) { filters.clear(); } openCards.add(id); render(); const el = document.getElementById('s-' + id); el?.scrollIntoView({block: 'start'}); el?.querySelector('.more')?.focus({preventScroll: true}); return; }
  if (b.dataset.action === 'copy') {
    const text = progressText();
    try { await navigator.clipboard.writeText(text); toast(t('copied')); }
    catch { const box = document.getElementById('copy-box'); box.hidden = false; box.value = text; box.focus(); box.select(); toast(t('copyFail')); }
  }
});
document.addEventListener('change', e => {
  const n = e.target; if (!n.dataset?.status) return;
  const id = n.dataset.status; if (n.value) statusMap[id] = n.value; else delete statusMap[id];
  store.set('wq-board-status', statusMap);
  const y = window.scrollY, focusId = n.id; render(); window.scrollTo(0, y); document.getElementById(focusId)?.focus({preventScroll: true});
});

try {
  const r = await fetch('./wq-board.json'); if (!r.ok) throw new Error('data');
  data = await r.json();
  render();
  if (location.hash && document.querySelector(location.hash)) document.querySelector(location.hash).scrollIntoView();
} catch (err) {
  root.innerHTML = '<main class="wq-loading"><p>資料載入失敗，請重新整理。<br>အချက်အလက် မတင်နိုင်ပါ။</p></main>';
  console.error(err);
}
