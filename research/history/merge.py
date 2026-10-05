"""Reproducible additive merge. Backup is immutable; superseded rows are retained."""
import json, copy, calendar, re
from pathlib import Path
from collections import defaultdict,Counter
from facts import records
ROOT=Path(__file__).resolve().parents[2]
base=json.loads((ROOT/'research/backups/schools-before-history-2026-09-20.json').read_text())
schools={s['id']:s for s in base['schools']}
fields={'start':'applicationStart','end':'applicationEnd','result':'resultDate'}
def interval(date):
    y,m,d=map(int,date.split('-'));part=0 if d<=10 else 1 if d<=20 else 2
    return {'zh':f'{m} 月'+['上旬','中旬','下旬'][part], 'my':f'{m} လ '+['အစပိုင်း','အလယ်ပိုင်း','နှောင်းပိုင်း'][part]}
def event(r,key):
    field=fields[key]; date=r.get(field); label=r.get(field+'Text');status=r['status']
    if field in r.get('conflicts',{}):
        return dict(status='conflict',label={'zh':'官方資料存在差異，待確認','my':'တရားဝင်ရင်းမြစ်များ မတူညီ၊ အတည်ပြုရန်'},sourceYear=r['sourceYear'],sourceUrl=r['sourceUrl'])
    if not(date or label):return None
    e=dict(scope=r['scope'],round=r['round'],status=status,basis=r['sourceYear'],sourceYear=r['sourceYear'],sourceUrl=r['sourceUrl'],sourceTitle=r['sourceTitle'],confidence=r['confidence'],rawDate=date)
    if date and status=='official':e['date']=date
    elif date:
        # Sort coordinate ONLY: align source admission year to target admission year.
        # The source date is retained unchanged in rawDate and admissionRecords.
        sy=int(r['sourceYear'].split('-')[0])+1911+(1 if r['semester']=='spring' else 0)
        y,m,d=map(int,date.split('-')); sortYear=y+(2027-sy)
        e.update(label=interval(date),sort=f'{sortYear:04}-{m:02}-{[1,11,21][0 if d<=10 else 1 if d<=20 else 2]:02}',precision='ten-day',sortIsReference=True)
    else:e.update(label={'zh':label,'my':r.get(field+'TextMy',label)},sort=r.get(key+'Sort'),precision=r.get(key+'Precision','interval'))
    return e
# Historical reference coordinates are never displayed as target-year dates.
for school in base['schools']:
    for tm in school['terms'].values():
        for rr in tm['rounds']:
            for key in fields:
                e=rr.get(key)
                if e and e.get('status')=='historical':
                    e['label']={lang:re.sub(r'202[67]/','',text) for lang,text in e.get('label',{}).items()}
                    e['sourceType']='user-provided-reference'
                    e['confidence']='low'
                    if e.get('basis')=='115春':
                        e['originalBasis']='115春'
                        e['basis']='原始年度待複核'
                    e['sortIsReference']=True
# Normalize legacy rows into the schema without inventing an original source date.
for s in base['schools']:
    for season,term in s['terms'].items():
        term['admissionRecords']=[]
        for i,rr in enumerate(term['rounds']):
            events=[rr.get(k) for k in fields if rr.get(k)]
            status='official' if any(e['status']=='official' for e in events) else 'historical' if any(e['status']=='historical' for e in events) else 'unknown'
            target='115-2' if season=='spring' else '116-1'
            r=dict(schoolId=s['id'],semester=season,targetYear=target,sourceYear=target if status=='official' else next((e.get('basis') for e in events if e.get('basis')),None),status=status,confidence='high' if status=='official' else 'low',sourceTitle='既有已核對時程（原版保留）' if status=='official' else '原始資料包歷年參考（原始年度日期待複核）',sourceUrl=next(iter(term.get('sources',[])),s['website']),lastChecked=s.get('checked','2026-09-19'),round=str(i+1),scope=term.get('scope'))
            for key,field in fields.items():
                e=rr.get(key) or {};r[field]=e.get('date') if e.get('status')=='official' else None
                if not r[field]:r[field+'Text']=(e.get('label') or {}).get('zh')
            r['sourceType']='retained-official' if status=='official' else 'user-provided-reference'
            r['note']='原版保留；不由排序用的2027座標反推原始日期。' if status!='official' else ''
            term['admissionRecords'].append(r)
        if not term['admissionRecords']:
            term['admissionRecords']=[dict(schoolId=s['id'],semester=season,targetYear='115-2' if season=='spring' else '116-1',sourceYear=None,applicationStart=None,applicationEnd=None,resultDate=None,status='unknown',confidence='unknown',sourceTitle=None,sourceUrl=None,lastChecked=s.get('checked'))]

group=defaultdict(list)
for r in records:
    assert r['schoolId'] in schools
    group[r['schoolId'],r['semester']].append(r)
for (id,season),rows in group.items():
    s=schools[id];term=s['terms'][season]
    term['archivedRounds']=copy.deepcopy(term['rounds'])
    term['archivedNotes']=copy.deepcopy(term.get('notes',[]))
    oldRecords=copy.deepcopy(term['admissionRecords'])
    latest=max(r['sourceYear'] for r in rows)
    active=[r for r in rows if r['sourceYear']==latest]
    # Preserve any existing official/conflicting rounds unless a sourced correction
    # intentionally replaces this term (PU, ASIA, CYUT), archived above.
    preserve= id not in ['1008','1048','1018'] and any(e and e.get('status') in ['official','conflict'] for r in term['rounds'] for e in [r.get('start'),r.get('end'),r.get('result')])
    new=[]
    for r in active:
        rr={key:event(r,key) for key in fields}
        rr.update(name={'zh':r['round'],'my':r['round']},sourceYear=r['sourceYear'],sourceUrl=r['sourceUrl'],scope=r['scope'])
        if r['note']:rr['note']={'zh':r['note'],'my':'အသေးစိတ်ကို တရားဝင်ရင်းမြစ်တွင် စစ်ပါ။ '+r['note']}
        new.append(rr)
    retained=[]
    if preserve:
        for old in term['rounds']:
            # Avoid duplicate official rounds when a freshly read source adds fields.
            matched=any(all((not old.get(k)) or (old[k].get('date') and old[k].get('date')==(nr.get(k) or {}).get('date')) for k in fields) for nr in new)
            if not matched:retained.append(old)
    term['rounds']=retained+new
    for old in oldRecords:old['archived']=True
    term['admissionRecords']=rows+[r for r in oldRecords if r['status']!='unknown']
    term['sources']=list(dict.fromkeys(term.get('sources',[])+[r['sourceUrl'] for r in rows]))
    if not preserve:
        term['notes']=[] # Prior notes refer to archived dates; keep in backup.
        term['scope']='graduate' if all(r['scope']=='graduate' for r in active) else 'all'
    if s['admission']['kind']=='home':s['admission']={'url':rows[0]['sourceUrl'],'kind':'admission'}
    s['checked']='2026-09-20'
    if rows[0]['sourceUrl'].lower().endswith('.pdf'):
        term['brochure']={'url':rows[0]['sourceUrl'],'status':rows[0]['status']}
base['updated']='2026-09-20'
summary={}
for season in ['fall','spring']:
    buckets={k:[] for k in ['official','historical','estimated','unknown']}
    for s in base['schools']:
        statuses=[e.get('status') for r in s['terms'][season]['rounds'] for e in [r.get(k) for k in fields] if e]
        status=next((k for k in ['official','historical','estimated'] if k in statuses),'unknown')
        buckets[status].append({'id':s['id'],'name':s['name'],'abbr':s['abbr']})
    summary[season]={'counts':{k:len(v) for k,v in buckets.items()},'schools':buckets}
base['coverage']=summary
(ROOT/'dist/schools.json').write_text(json.dumps(base,ensure_ascii=False,indent=2))
(ROOT/'dist/admission-records.json').write_text(json.dumps([r for s in base['schools'] for tm in s['terms'].values() for r in tm['admissionRecords']],ensure_ascii=False,indent=2))
(ROOT/'dist/coverage.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
print({k:v['counts'] for k,v in summary.items()})
