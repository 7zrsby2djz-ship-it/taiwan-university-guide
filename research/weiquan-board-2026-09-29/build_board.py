# -*- coding: utf-8 -*-
"""Build dist/wq-board.json for the 偉銓 decision board.

Run from project root:  python3 research/weiquan-board-2026-09-29/build_board.py
Reads dist/schools.json + dist/school-insights.json (not modified) and the
editorial layer in board_data.py. Safe to rerun; it only writes wq-board.json.
"""
import json, math, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from board_data import S, COORDS, ROUND_OVERRIDE, CHECKED

schools = {s['id']: s for s in json.loads((ROOT/'dist/schools.json').read_text())['schools']}
insights = json.loads((ROOT/'dist/school-insights.json').read_text())['schools']
STATION = (24.1372, 120.6869)

def km(a, b):
    R = 6371
    la1, lo1, la2, lo2 = map(math.radians, [*a, *b])
    d = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return round(2*R*math.asin(math.sqrt(d)))

def ev(e):
    if not e: return None
    st = e.get('status')
    out = {'status': st, 'sourceYear': e.get('sourceYear') or e.get('basis')}
    if st == 'official' and e.get('date'): out['date'] = e['date']
    elif st == 'conflict': out['label'] = '來源有差異'
    else:
        out['label'] = (e.get('label') or {}).get('zh') or '日期待確認'
        if e.get('sort'): out['sort'] = e['sort']
    if e.get('sourceUrl'): out['src'] = e['sourceUrl']
    return out

def ov(t):
    if not t: return None
    st, d, *lab = t
    if st == 'official-month': return {'status': 'official', 'sort': d, 'label': lab[0]}
    if st == 'hist': return {'status': 'historical', 'sourceYear': '115', 'sort': d, 'label': lab[0]}
    return {'status': st, 'date': d}

def term_info(s, key, extra):
    T = s['terms'][key]
    o = ROUND_OVERRIDE.get((s['id'], key))
    if o in ('none', 'grad'):
        return {'ug': o, 'rounds': []}
    if o:
        rounds = [dict(start=ov(r['start']), end=ov(r['end']), result=ov(r['result']), note=r.get('note')) for r in ROUND_OVERRIDE[(s['id'], key)]]
        return {'ug': 'has', 'rounds': rounds}
    if T.get('availability') == 'not_offered_in_source':
        return {'ug': 'none', 'rounds': []}
    ug = []
    grad_only = True
    for r in T.get('rounds', []):
        scope = r.get('scope') or T.get('scope')
        if scope == 'graduate': continue
        grad_only = False
        note = r.get('note')
        ug.append(dict(start=ev(r.get('start')), end=ev(r.get('end')), result=ev(r.get('result')), note=(note or {}).get('zh') if isinstance(note, dict) else note))
    if not T.get('rounds'): status = 'unknown'
    elif grad_only: status = 'grad'
    else: status = 'has'
    letters = extra.get('letter', {}).get(key)
    if letters:
        letters = letters if isinstance(letters, list) else [letters]
        for r, d in zip(ug, letters): r['letter'] = d
    return {'ug': status, 'rounds': ug}

def first_year(e):
    t, f = e.get('tuition'), e['firstYear']
    if f['kind'] == 'full': return {'min': 0, 'max': 0, 'basis': 'sure'}
    if not t: return None
    lo, hi = t['min'], t['max']
    k = f['kind']
    if k == 'full': return {'min': 0, 'max': 0, 'basis': 'sure'}
    if k == 'half': return {'min': round(lo*.5), 'max': round(hi*.5), 'basis': 'sure'}
    if k == 'minus': return {'min': max(0, lo-f['minus']), 'max': max(0, hi-f['minus']), 'basis': 'sure'}
    return {'min': lo, 'max': hi, 'basis': 'worst'}

out = []
for sid, e in S.items():
    s = schools[sid]
    ins = insights.get(sid, {})
    d = km(STATION, COORDS[sid])
    rec = {
        'id': sid, 'name': s['name'], 'short': s['short'], 'abbr': s['abbr'], 'english': s.get('english'),
        'city': s['cities'][0], 'ownership': s['ownership'], 'type': s['type'],
        'km': d, 'commute': 'local' if d <= 20 else 'near' if d <= 60 else 'far',
        'place': e['place'], 'travel': e['travel'], 'tier': e['tier'],
        'fee': e['fee'], 'tuition': e.get('tuition'), 'firstYearKind': e['firstYear']['kind'],
        'semesterCost': first_year(e), 'aid': e['aid'], 'renew': e['renew'], 'lang': e['lang'],
        'after': e['after'], 'verdict': e['verdict'], 'verdictMy': e['verdictMy'],
        'readYourself': e.get('readYourself', []),
        'bizAdmits': e.get('bizAdmits', []),
        'links': {
            'apply': (s.get('admission') or {}).get('url') or s.get('website'),
            'website': s.get('website'),
            'brochureSpring': (s['terms']['spring'].get('brochure') or {}).get('url'),
            'brochureSpringYear': (s['terms']['spring'].get('brochure') or {}).get('academicYear'),
            'brochureFall': (s['terms']['fall'].get('brochure') or {}).get('url'),
            'brochureFallYear': (s['terms']['fall'].get('brochure') or {}).get('academicYear'),
        },
        'lists': [{'year': n['academicYear'], 'term': n['semester'], 'title': n['sourceTitle'], 'url': n['sourceUrl']} for n in ins.get('admissionNotices', [])],
        'terms': {k: term_info(s, k, e) for k in ('spring', 'fall')},
        'checked': e['checked'],
    }
    out.append(rec)

doc = {
    'schemaVersion': 1, 'updated': CHECKED, 'reference': '台中車站直線距離（公里）',
    'arcExpiry': '2027-06-30', 'tocfl': {'now': 'A2', 'nextExam': '2026-11', 'note': '960 分，970 分可拿 B1'},
    'schools': out,
}
(ROOT/'dist/wq-board.json').write_text(json.dumps(doc, ensure_ascii=False, indent=1))
print('wrote', len(out), 'schools')
