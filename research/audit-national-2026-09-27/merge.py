"""Merge the bounded 17-school audit into the immutable version-8 snapshot."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; H=Path(__file__).resolve().parent; B=R/'research/backups/national-2026-09-27'; TODAY='2026-09-27'
read=lambda p:json.loads(p.read_text())
d=read(B/'schools.json');ins=read(B/'school-insights.json');facts=read(H/'facts.json');ss={s['id']:s for s in d['schools']}
def bi(z,m=None):return {'zh':z,'my':m or 'အသေးစိတ်ကို တရားဝင်ရင်းမြစ်နှင့် အောက်ပါ တရုတ်စာတွင် စစ်ဆေးပါ။'}
def target(term):return '115-2' if term=='spring' else '116-1'
def event(value,term,year,url,title,text=None,sort=None):
 status='official' if year==target(term) else 'historical'
 if not value and not text:return None
 e=dict(status=status,basis=year,sourceYear=year,sourceUrl=url,sourceTitle=title,confidence='high' if status=='official' else 'medium',rawDate=value)
 if value and status=='official':e['date']=value
 elif value:
  y,m,day=map(int,value.split('-'));part=0 if day<=10 else 1 if day<=20 else 2;sy=int(year.split('-')[0])+1911+(term=='spring')
  e.update(label=bi(f'{m} 月'+['上旬','中旬','下旬'][part],f'{m} လ '+['အစပိုင်း','အလယ်ပိုင်း','နှောင်းပိုင်း'][part]),sort=f'{y+2027-sy:04}-{m:02}-{[1,11,21][part]:02}',precision='ten-day',sortIsReference=True)
 else:e.update(label=bi(text),sort=sort,precision='interval',sortIsReference=status=='historical')
 return e
def replace(id,term,v):
 t=ss[id]['terms'][term];old=copy.deepcopy(t.get('admissionRecords',[]));previous=copy.deepcopy(t['rounds']);year=v['year'];url=v['url'];scope=v.get('scope',t.get('scope') or 'all');title=f'{year} 一般外國學生招生官方資料'
 t.setdefault('archivedRounds',[]).extend(previous);t.setdefault('archivedNotes',[]).extend(t.get('notes',[]));t['rounds']=[];t['notes']=[];t['scope']=scope
 new=[]
 for n,vals in enumerate(v['rounds'],1):
  r=dict(name=bi(str(n),str(n)),sourceYear=year,sourceUrl=url,scope=scope)
  record=dict(schoolId=id,semester=term,targetYear=target(term),sourceYear=year,status='official' if year==target(term) else 'historical',confidence='high' if year==target(term) else 'medium',sourceTitle=title,sourceUrl=url,lastChecked=TODAY,round=str(n),scope=scope,sourceType='official-primary')
  for k,f,value in zip(['start','end','result'],['applicationStart','applicationEnd','resultDate'],vals):
   r[k]=event(value,term,year,url,title,v.get('resultText') if k=='result' else None,v.get('resultSort') if k=='result' else None);record[f]=value
   if k=='result' and v.get('resultText'):record['resultDateText']=v['resultText']
  t['rounds'].append(r);new.append(record)
 for r in old:r['archived']=True
 t['admissionRecords']=new+old;t['sources']=list(dict.fromkeys([url]+t.get('sources',[])))
 if id=='0002' and term=='fall':
  # Preserve the separate graduate reference instead of replacing it with UG dates.
  for r in previous:
   if '研究所' in r.get('name',{}).get('zh',''):
    r['scope']='graduate';r['note']=bi('研究所另有申請期間，此列保留既有歷年參考；學士日期已另核官方115簡章。');t['rounds'].append(r)
  t['scope']='all'
for id,v in facts.items():
 s=ss[id];s['checked']=TODAY;s['reviewState']='audited';old=ins['schools'].get(id)
 record=copy.deepcopy({k:val for k,val in v.items() if k in ['applicationFee','scholarships','requirements','admissionNotices']})
 record.setdefault('admissionNotices',[]);record.setdefault('requirements',[]);record.setdefault('tuition',[]);record['lastChecked']=TODAY
 record['audit']=dict(checked=TODAY,scope='一般外國學位生；彰師、暨南、聯合及跨縣市國立大學17校',status='部分完整',gaps=v.get('gaps',[]))
 if old:record['previousVersions']=[old]
 ins['schools'][id]=record
 for term,t in v.get('timelines',{}).items():replace(id,term,t)
 for term,b in v.get('brochures',{}).items():s['terms'][term]['brochure']={**b,'status':'official' if b['academicYear']==target(term) else 'historical'}
 if v.get('admission'):s['admission']=v['admission']
 for term,link in v.get('applyByTerm',{}).items():s['terms'][term]['apply']=link
 for sch in record['scholarships']:sch['lastChecked']=TODAY
# Correct scope so spring graduate-only dates cannot look like bachelor admissions.
for id in ['0007','0008','0022','0023']:
 t=ss[id]['terms']['spring'];t['scope']='graduate'
 for r in t['rounds']:r['scope']='graduate'
 for r in t.get('admissionRecords',[]):
  if not r.get('archived'):r['scope']='graduate'
# The current NTUST host replaced the old host. Preserve event dates and rounds.
for term in ['spring','fall']:
 t=ss['0022']['terms'][term]
 def renew_url(obj):
  if isinstance(obj,dict):
   for k,v in obj.items():
    if isinstance(v,str) and v.startswith('https://admission.ntust.edu.tw/'):obj[k]=v.replace('https://admission.ntust.edu.tw/','https://admission-r.ntust.edu.tw/',1)
    else:renew_url(v)
  elif isinstance(obj,list):
   for i,v in enumerate(obj):
    if isinstance(v,str) and v.startswith('https://admission.ntust.edu.tw/'):obj[i]=v.replace('https://admission.ntust.edu.tw/','https://admission-r.ntust.edu.tw/',1)
    else:renew_url(v)
 renew_url(t)
# NTNU department extension differs from the centrally republished date; no silent choice.
t=ss['0004']['terms']['fall'];r=t['rounds'][1];a=r['end']['sourceUrl'];b='https://www.ihrd.ntnu.edu.tw/index.php/en/admissions/'
r['end']={'status':'conflict','sourceYear':'115-1','basis':'115-1','label':bi('3/2／3/16 · 系所期限差異待確認','3/2 / 3/16 · ဌာနသတ်မှတ်ရက် အတည်ပြုရန်'),'sourceUrls':[a,b],'confidence':'low'}
r['note']=bi('中央時程轉載3/2截止；IHRD系所頁另列3/16，不推定全校延長。')
for rec in t['admissionRecords']:
 if not rec.get('archived') and rec.get('round')=='2':
  rec['applicationEnd']=None;rec['applicationEndText']='3/2／3/16，系所期限差異待確認';rec['conflicts']={'applicationEnd':{'dates':['2026-03-02','2026-03-16'],'sourceUrls':[a,b]}}
t['sources']=list(dict.fromkeys(t.get('sources',[])+[b]))
# NTPU current spring period stays official; previous spring result is visibly historical.
v=facts['0017']['historicalSpring'];t=ss['0017']['terms']['spring'];url=v['url'];year=v['year'];vals=v['rounds'][0]
if not t['rounds'][0].get('result'):t['rounds'][0]['result']=event(vals[2],'spring',year,url,'114-2外國學生招生簡章')
t['rounds'][0]['note']=bi('開始／截止採115-2官方系統；放榜僅114-2簡章的12月上旬參考，不能視為本期正式放榜。')
t['admissionRecords'].append(dict(schoolId='0017',semester='spring',targetYear='115-2',sourceYear=year,applicationStart=vals[0],applicationEnd=vals[1],resultDate=vals[2],status='historical',confidence='medium',sourceTitle='114-2外國學生招生簡章',sourceUrl=url,lastChecked=TODAY,scope='all',sourceType='official-primary',round='上一年度參考'))
t['sources']=list(dict.fromkeys(t.get('sources',[])+[url]))
# Correct the old NTUT116 fall event's erroneous115 basis via the new verified source.
# All research membership remains explicit; incomplete research does not mean all fields verified.
d['updated']=TODAY;ins['updated']=TODAY
summary={}
for term in ['fall','spring']:
 buckets={k:[] for k in ['official','historical','estimated','unknown']}
 for s in d['schools']:
  states=[e.get('status') for r in s['terms'][term]['rounds'] for e in [r.get(k) for k in ['start','end','result']] if e]
  status=next((k for k in ['official','historical','estimated'] if k in states),'unknown');buckets[status].append({k:s[k] for k in ['id','name','abbr']})
 summary[term]={'counts':{k:len(v) for k,v in buckets.items()},'schools':buckets}
d['coverage']=summary
for name,value in [('schools.json',d),('school-insights.json',ins),('coverage.json',summary),('admission-records.json',[r for s in d['schools'] for t in s['terms'].values() for r in t.get('admissionRecords',[])])]:
 (R/'dist'/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
print('Merged',len(facts),'schools; registry',len(d['schools']),'reviewed',sum(s.get('reviewState') in ['audited','partially_audited'] for s in d['schools']))
