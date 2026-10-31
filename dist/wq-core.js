// Shared decision rules. Sorting keys are never evidence of an exact date.
export const FILTERS = ['now', 'local', 'sure', 'free', 'biz', 'mine'];
export const SORTS = ['tier', 'km', 'cost', 'result', 'fall', 'biz', 'fee'];

export function isDate(value) {
  return typeof value === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(value)
    && !Number.isNaN(Date.parse(value + 'T00:00:00Z'))
    && new Date(value + 'T00:00:00Z').toISOString().slice(0, 10) === value;
}

export function isLateRound(round, arcExpiry) {
  // An earlier admission letter can precede the public result list.
  const available = round.letter || round.result?.date || round.result?.sort;
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
      end: r.end.date, result: r.result, letter: r.letter, note: r.note})));
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
  };
}
