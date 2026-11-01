import {admissionLetter, isDate} from './wq-core.js';

// Planning evidence, never an eligibility score. Keep one intake and one round together.
const exact = e => e?.status === 'official' && isDate(e.date) ? e.date : null;
export const decisionTerm = term => term === 'spring' ? '2027 春季（115-2）' : '2027 秋季（116-1）';

export function matchesSourceYear(year, term) {
  // A label such as "115參考；116待核" must not become current-year evidence.
  const expected = term === 'spring' ? '115' : '116';
  const semester = term === 'spring' ? '2' : '1';
  return [expected, `${expected}-${semester}`, `${expected}學年度`].includes(String(year || '').trim());
}

export function decisionFor(school, term, today, arcExpiry) {
  if (!['spring', 'fall'].includes(term)) return {kind: 'choose-term'};
  const scope = school.terms[term], ug = scope?.ug || 'unknown';
  const rounds = (ug === 'has' ? scope.rounds || [] : []).map((r, index) => ({...r, term, round: index + 1}));
  const future = rounds.filter(r => exact(r.end) && r.end.date >= today).sort((a, b) => a.end.date.localeCompare(b.end.date));
  // Prefer a confirmed, open round, then the nearest future deadline. Do not hide late letters here.
  let round = future.find(r => exact(r.start) && r.start.date <= today) || future[0];
  let timing = 'unknown';
  if (round) timing = !exact(round.start) ? 'confirm-opening' : round.start.date > today ? 'upcoming' : 'open';
  else {
    round = rounds.find(r => r.end?.status === 'conflict')
      || rounds.find(r => !exact(r.end) && !['historical', 'estimated'].includes(r.end?.status))
      || rounds.filter(r => ['historical', 'estimated'].includes(r.end?.status))
        .sort((a, b) => (a.end.sort || '').localeCompare(b.end.sort || ''))[0];
    if (round) timing = round.end?.status === 'conflict' ? 'conflict' : ['historical', 'estimated'].includes(round.end?.status) ? 'historical' : 'unknown';
    else if (rounds.length) { timing = 'closed'; round = [...rounds].sort((a, b) => b.end.date.localeCompare(a.end.date))[0]; }
  }
  const letter = round && admissionLetter(round);
  let letterKind = !round || timing === 'closed' ? 'not-current' : exact(letter) ? 'official' : letter?.status === 'historical' || letter?.status === 'estimated' ? 'historical' : 'unknown';
  const gap = letterKind === 'official' && isDate(arcExpiry)
    ? Math.round((Date.parse(arcExpiry) - Date.parse(letter.date)) / 864e5) : null;
  if (gap !== null) letterKind = gap < 0 ? 'late' : gap < 30 ? 'tight' : 'official';
  return {kind: 'plan', term, ug, round: round || null, timing, letter, letterKind, gap,
    feeCurrent: matchesSourceYear(school.fee?.year, term) && ['free', 'paid'].includes(school.fee?.kind),
    tuitionCurrent: matchesSourceYear(school.tuition?.year, term) && !!school.semesterCost,
    source: round?.end?.src || round?.src || scope?.src || school.links.apply};
}

// This is an editable Chinese draft for a Taiwanese admissions office, never an automatic message.
export function inquiryText(school, term, department, plan) {
  if (plan.kind !== 'plan') return '';
  const target = String(department || '').trim().slice(0, 80) || '尚未決定，請提供可申請的系所';
  const season = decisionTerm(term), end = exact(plan.round?.end), letter = exact(plan.letter);
  const questions = [];
  if (plan.ug === 'grad' || plan.ug === 'none') questions.push('目前資料顯示這一季未開放一般外國學生學士申請，請問是否另有學士招生或追加梯次？若沒有，下一季何時公告？');
  else questions.push(`請問${season}是否招收一般外國學生學士班？上述科系是否開放，以及招生名額、授課語言與正式簡章連結為何？`);
  if (plan.timing === 'closed') questions.push(`已查到的梯次於 ${end} 截止；請問是否另有追加梯次？若沒有，下一次學士申請何時開始？`);
  else if (end) questions.push(`資料列出的申請截止日是 ${end}。請確認適用上述科系及第 ${plan.round.round} 梯，並提供開始日、截止時間（臺灣時間）、補件與繳費期限。`);
  else questions.push('目前申請時程仍有往年參考、資料差異或未確認之處，請提供這一季正式的開始日、截止時間（臺灣時間）與補件期限。');
  questions.push('該系 TOCFL 聽、說、讀、寫各須達哪一級？可接受哪些替代證明，語言成績最晚何時補交？');
  questions.push('高中畢業證書、成績單及翻譯／駐外驗證文件須如何準備？財力證明的金額、開立期限與其他必備文件為何？');
  questions.push(`網站申請費來源標示「${school.fee?.year || '年度待確認'}」、學雜費來源標示「${school.tuition?.year || '年度待確認'}」。請確認${season}的申請費（按人或按系）、學雜費、住宿及其他必繳費用。獎學金是否須另行審查，第一年優惠及續領條件為何？`);
  questions.push(letter && plan.timing !== 'closed'
    ? `資料列入學許可日期 ${letter}；請問是寄發日還是可下載日？是否提供電子正本、郵寄約需多久，以及回覆就讀與繳費期限為何？`
    : '錄取結果公布後，入學許可何時可下載或寄發？是否提供電子正本、郵寄約需多久，以及回覆就讀與繳費期限為何？');
  return [`主旨：詢問${season}一般外國學生學士申請｜${school.short}`, '', `${school.name || school.short}招生承辦您好：`,
    `我想了解${season}的一般外國學生學士申請。`, `預計申請科系：${target}`, '',
    ...questions.map((q, i) => `${i + 1}. ${q}`), '', '煩請提供適用年度的正式簡章或公告連結，謝謝。',
    ...(plan.source ? ['', `目前參考頁面：${plan.source}`] : [])].join('\n');
}
