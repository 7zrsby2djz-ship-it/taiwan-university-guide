// Shared decision rules. Sorting keys are never evidence of an exact date.
export const FILTERS = ['now', 'local', 'sure', 'free', 'biz', 'mine'];
export const SORTS = ['tier', 'km', 'cost', 'result', 'fall', 'biz', 'fee'];
export const INTAKES = ['all', 'spring', 'fall'];

export function matchesIntake(school, intake) {
  if (intake === 'all') return true;
  // Unknown scope stays visible for verification, never as a confirmed window.
  return ['has', 'unknown'].includes(school.terms[intake]?.ug);
}

export function isDate(value) {
  return typeof value === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(value)
    && !Number.isNaN(Date.parse(value + 'T00:00:00Z'))
    && new Date(value + 'T00:00:00Z').toISOString().slice(0, 10) === value;
}

export function admissionLetter(round) {
  if (round.letter && typeof round.letter === 'object') return round.letter;
  if (!isDate(round.letter)) return null;
  return ['end', 'result'].some(k => round[k]?.status === 'official')
    ? {status: 'official', date: round.letter}
    : {status: 'historical', sort: round.letter, label: round.letter.slice(5).replace('-', '/')};
}

export function isLateRound(round, arcExpiry) {
  // An earlier admission letter can precede the public result list.
  const letter = admissionLetter(round);
  const available = letter?.date || letter?.sort || round.result?.date || round.result?.sort;
  return (available || round.end?.date || round.end?.sort || '') > arcExpiry;
}

export function undergraduateRounds(school, term, arcExpiry) {
  const intake = school.terms[term];
  if (intake?.ug !== 'has') return [];
  return (intake.rounds || []).map((r, index) => ({...r, round: index + 1}))
    .filter(r => !isLateRound(r, arcExpiry));
}

export function officialWindows(school, arcExpiry) {
  return ['spring', 'fall'].flatMap(term => undergraduateRounds(school, term, arcExpiry)
    .filter(r => r.end?.status === 'official' && isDate(r.end.date))
    .map(r => ({s: school, term, round: r.round, many: school.terms[term].rounds.length > 1,
      start: r.start?.status === 'official' && isDate(r.start.date) ? r.start.date : null,
      end: r.end.date, result: r.result, letter: admissionLetter(r), note: r.note})));
}

export const isOpen = (window, today) => !!window.start && window.start <= today && window.end >= today;
export const isSoon = (window, today) => !!window.start && window.start > today && window.end >= today;
export const isUnconfirmed = (window, today) => !window.start && window.end >= today;

// For new applications, compare a result only with its still-available round.
export function nextResult(school, term, today, arcExpiry) {
  return undergraduateRounds(school, term, arcExpiry)
    .filter(r => (r.end?.date || r.end?.sort || '') >= today)
    .map(r => r.result)
    .filter(e => e && ['official', 'historical', 'estimated'].includes(e.status)
      && (e.date || e.sort) >= today)
    .sort((a, b) => (a.date || a.sort).localeCompare(b.date || b.sort))[0] || null;
}

// Missing values stay at the bottom in both sorting directions.
export function compareNullable(a, b, direction = 1) {
  if (a == null && b == null) return 0;
  if (a == null) return 1;
  if (b == null) return -1;
  return (a < b ? -1 : a > b ? 1 : 0) * direction;
}

const norm = value => String(value || '').normalize('NFKC').toLowerCase().replaceAll('臺', '台').trim();
export function matchesQuery(school, query) {
  const haystack = norm([school.short, school.name, school.abbr, school.english, school.place, school.city].join(' '));
  return norm(query).split(/\s+/).filter(Boolean).every(word => haystack.includes(word));
}

export function readView(params) {
  return {
    query: (params.get('q') || '').slice(0, 150),
    filters: new Set((params.get('filters') || '').split(',').filter(k => FILTERS.includes(k))),
    sortKey: SORTS.includes(params.get('sort')) ? params.get('sort') : 'tier',
    sortDirection: params.get('dir') === 'desc' ? -1 : 1,
    compareIds: (params.get('compare') || '').split(',').filter(Boolean),
    intake: INTAKES.includes(params.get('term')) ? params.get('term') : 'all',
  };
}

export function cleanComparison(values, schoolIds) {
  if (!Array.isArray(values)) return [];
  const known = new Set(schoolIds);
  return [...new Set(values.filter(id => typeof id === 'string' && known.has(id)))].slice(0, 3);
}

export function roundChoices(school) {
  return ['spring', 'fall'].flatMap(term => school.terms[term]?.ug !== 'has' ? []
    : (school.terms[term].rounds || []).map((round, index) => ({...round, term, round: index + 1, key: `${term}:${index + 1}`})));
}

// Detect changed/reordered rounds instead of silently attaching old progress to a new intake.
function roundSignature(round) {
  const values = ['start', 'end', 'result'].map(key => {
    const event = round[key];
    return event ? [event.status, event.date || '', event.sort || '', event.label || '', event.sourceYear || event.year || ''] : null;
  });
  const text = JSON.stringify([round.term, values, round.letter || '']);
  let hash = 2166136261;
  for (let i = 0; i < text.length; i++) hash = Math.imul(hash ^ text.charCodeAt(i), 16777619);
  return (hash >>> 0).toString(16);
}

export function selectRound(school, key) {
  const round = roundChoices(school).find(r => r.key === key);
  return round ? {key, signature: roundSignature(round)} : null;
}

export function resolveRound(school, selection) {
  if (!selection || typeof selection !== 'object') return {state: 'none', round: null};
  const round = roundChoices(school).find(r => r.key === selection.key);
  if (!round || selection.signature !== roundSignature(round)) return {state: 'stale', round: null};
  return {state: 'valid', round};
}

const exact = event => event?.status === 'official' && isDate(event.date) ? event.date : null;
export function taskForRound(round, status, today) {
  const result = exact(round.result), start = exact(round.start), end = exact(round.end);
  const letter = exact(admissionLetter(round));
  if (status === 'admitted') return letter && letter >= today ? {kind: 'letter', date: letter} : {kind: 'documents'};
  if (status === 'applied') {
    if (result) {
      if (result >= today) return {kind: 'result', date: result};
      if (letter && letter >= today) return {kind: 'letter', date: letter};
      return {kind: 'result-ready', date: result};
    }
    if (round.result?.status === 'official' && round.result.label) return {kind: 'result-window', event: round.result};
    return {kind: 'verify-result', event: round.result};
  }
  if (end && end < today) return {kind: 'closed', date: end};
  if (start && start > today) return {kind: 'opens', date: start};
  if (!end) return {kind: 'verify-deadline', event: round.end};
  if (!start) return {kind: 'confirm-open', date: end};
  return {kind: 'deadline', date: end};
}
