"""Bounded merge from the immutable version-9 snapshot; no list contents."""
import json,copy,runpy
from pathlib import Path
R=Path(__file__).resolve().parents[2];H=Path(__file__).resolve().parent;B=R/'research/backups/remaining-2026-09-28';C=Path('/workspace/scratch/acf8db14de2d/tmp/remaining');TODAY='2026-09-28'
read=lambda p:json.loads(p.read_text());d=read(B/'schools.json');ins=read(B/'school-insights.json');ss={s['id']:s for s in d['schools']};F=runpy.run_path(str(H/'facts.py'))['FACTS']
manifest={p.name.replace('.source.json',''):read(p) for p in C.glob('*.source.json')}
def url(k):return manifest[k]['url']
def bi(z,m=None):return {'zh':z,'my':m or 'အသေးစိတ်ကို အောက်ပါ တရုတ်စာနှင့် တရားဝင်ရင်းမြစ်တွင် စစ်ဆေးပါ။'}
# Reuse proven event/archival helpers only, not the old batch mutations.
old=(R/'research/audit-national-2026-09-27/merge.py').read_text();exec(old[old.index('def target('):old.index('for id,v in facts.items():')])
T={}
def timeline(id,term,year,rows,key=None,**kwargs):
 T.setdefault(id,{})[term]=dict(year=year,rounds=rows,url=url(key or F[id]['b']),**kwargs)
timeline('0014','fall','115-1',[['2026-01-20','2026-04-15','2026-06-05']])
timeline('0019','fall','116-1',[['2027-02-25','2027-04-23','2027-06-15']])
timeline('0019','spring','115-2',[['2026-10-08','2026-11-02','2026-12-17']])
timeline('0020','fall','115-1',[['2026-01-02','2026-03-15','2026-05-10'],['2026-03-16','2026-04-14','2026-06-10']])
timeline('0028','fall','115-1',[['2026-01-02','2026-03-22',None]],resultText='6月初前（115學年度原文）',resultSort='2027-06-01')
timeline('0029','fall','115-1',[['2025-12-15','2026-03-02',None]],resultText='6/5前（115學年度原文）',resultSort='2027-06-01')
timeline('0033','fall','115-1',[['2026-04-01','2026-05-13','2026-06-08']])
timeline('0035','fall','115-1',[['2026-01-01','2026-03-01','2026-05-05']])
timeline('0037','fall','116-1',[['2026-09-11','2026-11-13','2026-12-18']])
timeline('0042','fall','115-1',[['2026-04-13','2026-06-07','2026-07-08']])
timeline('0044','spring','115-2',[[None,'2026-12-24','2027-01-11']])
timeline('0044','fall','115-1',[[None,None,'2026-07-13']])
timeline('0046','fall','115-1',[['2026-01-01','2026-03-31','2026-04-17'],['2026-04-20','2026-05-29','2026-06-12']])
timeline('0048','fall','116-1',[['2026-10-01','2026-12-31','2027-01-20']])
timeline('0051','fall','115-1',[['2026-01-06','2026-05-01','2026-06-05']])
timeline('0052','fall','115-1',[[None,'2026-04-15','2026-06-15']])
timeline('0052','spring','115-2',[[None,'2026-10-15','2026-11-30']])
# Intake coverage is evidence-specific, never infer annual applicability from fall.
fallOnly={'0028','0029','0033','0035','0037','0042','0046','0047','0048','0051'};springOnly={'0049'}
N={}
def notice(id,y,sem,title,u):N.setdefault(id,[]).append(dict(academicYear=y,semester=sem,sourceTitle=title,sourceUrl=u,scope='foreign_degree'))
for id,y,sem,title,u in [
('0014','114','fall','114-1外國學生錄取公告','https://e.nknu.edu.tw/news-detail.php?id=176'),
('0014','114','spring','114-2外國學生錄取公告','https://oia.nknu.edu.tw/news-detail.php?id=339'),
('0018','115','fall','115外國學生第一梯次錄取公告','https://www.ncyu.edu.tw/oia/Subject/Detail/239647?nodeId=58425'),
('0018','114','fall','114外國學生第一梯次學士班錄取公告','https://www.ncyu.edu.tw/oia/ServerFile/Get/4d3dda85-a5d6-4df4-a5d4-9dae496e6bf8?nodeId=58425&sId=222092'),
('0020','115','fall','115外國學生秋季第二梯次錄取公告','https://oia.ndhu.edu.tw/p/405-1027-259259,c21529.php?Lang=en'),
('0028','115','fall','2026 International Student Admission Result（官方頁內連結）','https://oia.tnua.edu.tw/foreigenstudent'),
('0028','114','fall','2025 International Student Admission Result（官方頁內連結）','https://oia.tnua.edu.tw/foreigenstudent'),
('0030','115','fall','115外國學生秋季錄取公告入口','https://admission.nttu.edu.tw/'),
('0031','115','fall','115第一梯次外國学生錄取公告','https://isa.niu.edu.tw/p/404-1073-70986.php'),
('0031','114','spring','114春季外國學生錄取公告','https://isa.niu.edu.tw/p/405-1073-69070%2Cc5943.php'),
('0033','115','fall','115外國學生錄取公告','https://enrollstudents.nfu.edu.tw/content/60008/admission/115/24841'),
('0035','115','fall','115外國學生錄取公告','https://acad.tnnua.edu.tw/p/406-1003-55456%2Cr108.php?Lang=zh-tw'),
('0036','115','fall','115外國學生錄取公告','https://campus.nutn.edu.tw/newspost3/readPost.aspx?boardNo=103748'),
('0037','115','fall','115外國學生錄取公告','https://academicntue.ntue.edu.tw/p/406-1002-54610%2Cr12.php?Lang=zh-tw'),
('0044','114','spring','114-2外國學生錄取名單公告','https://aca.ntsu.edu.tw/p/405-1004-62559%2Cc2884.php?Lang=zh-tw'),
('0044','114','fall','114-1外國學生錄取名單公告','https://aca.ntsu.edu.tw/p/404-1004-60398.php?Lang=zh-tw'),
('0046','115','fall','115外國學生第二階段錄取名單公告','https://international-rnd.ntunhs.edu.tw/p/406-1037-83255%2Cr82.php?Lang=zh-tw'),
('0052','114','spring','114春季外國學生錄取公告','https://oiais.nptu.edu.tw/p/406-1090-189648,r3222.php?Lang=zh-tw'),
('0052','114','fall','114秋季外國學生原始榜單','https://oiais.nptu.edu.tw/var/file/90/1090/img/381103840.pdf'),
('0053','114','fall','2025 (114-1) Admission List（官方頁內入口）','https://oia.nkust.edu.tw/unit-11-268-6.html'),
('0053','114','spring','2026 (114-2) Admission List（官方頁內入口）','https://oia.nkust.edu.tw/unit-11-268-6.html')]:notice(id,y,sem,title,u)
A={
'0024':('https://oia2.npust.edu.tw/zh/future-students/','https://courseeng.npust.edu.tw/Admission/'),
'0028':('https://oia.tnua.edu.tw/foreigenstudent','https://gasys.tnua.edu.tw/IEC/ApplyForm.aspx'),
'0029':('https://international.ntua.edu.tw/',None),
'0030':('https://admission.nttu.edu.tw/','https://admission.nttu.edu.tw/'),
'0031':('https://isa.niu.edu.tw/',None),
'0033':('https://enrollstudents.nfu.edu.tw/content/60008/download/115/22743','https://enrollstudents.nfu.edu.tw/signup/60008/0'),
'0035':('https://acad.tnnua.edu.tw/p/412-1003-3732.php?Lang=zh-tw',None),
'0037':('https://oia.ntue.edu.tw/p/405-1066-46770%2Cc4763.php?Lang=zh-tw','https://recruit.ntue.edu.tw/EXAM'),
'0039':('https://oia.ntcu.edu.tw/','https://insch.ntcu.edu.tw/en/'),
'0042':('https://www.npu.edu.tw/Sub/form/Details.aspx?Parser=2%2C27%2C552%2C457%2C%2C%2C6493',None),
'0044':('https://aca.ntsu.edu.tw/p/404-1004-63564.php?Lang=zh-tw',None),
'0046':('https://international-rnd.ntunhs.edu.tw/p/412-1037-3799.php?Lang=en','https://applyint.ntunhs.edu.tw/'),
'0047':('https://international.nkuht.edu.tw/p/404-1045-34386.php?Lang=en','https://examstd.nkuht.edu.tw/EnrollSTDFS/'),
'0048':('https://oica.nqu.edu.tw/p/405-1003-31507%2Cc902.php?Lang=zh-tw','https://forms.gle/Tr1wX3wDLLqCoa6W9'),
'0051':('https://admis.ntub.edu.tw/p/406-1028-115006%2Cr87.php','https://mbasignup.ntub.edu.tw/'),
'0052':('https://oiais.nptu.edu.tw/p/412-1090-12629.php?Lang=zh-tw','https://oiais.nptu.edu.tw/p/423-1090-1583.php?Lang=zh-tw'),
'0053':('https://oia.nkust.edu.tw/en/unit-11-262-5.html',None)}
REQ={
'0028':'中文授課至少TOCFL A2，系所可要求更高；英文授課TOEFL iBT79／IELTS6.5／TOEIC800，符合官方語言或前學位英文授課條件可檢附證明免繳。線上填表之外仍須郵寄或親送完整資料與繳費證明，115申請截止為郵戳3/22；語言證明不接受補交。',
'0031':'中文授課母語非中文者至少TOCFL A2或同等證明；英文授課母語非英文者至少CEFR B1。前學位授課語言符合者依規定檢附證明免繳；各系另有規定。須提供足夠就學財力或已獲獎學金證明。',
'0042':'115簡章採電子郵件報名，非独立線上系統；請依簡章指定信箱與主旨送件，不要把招生資訊頁當已完成申請。',
'0051':'115簡章須線上報名並依規定送件；財力或獎學金證明至少US$3,000，存款非本人須資助者保證書。學歷與成績單須驗證，非中英文須譯本。語言門檻依系所表，不把學士A2套用全部碩士。',
'0052':'僅受理線上申請、不接受紙本。中文授課至少CEFR A2相當華語證明；英文授課至少CEFR B1，母語及前學位符合者依簡章例外。學歷與成績單須駐外驗證，非中英文須認證譯本。'}
G={
'0018':['第一梯次放榜來源差異保留；第二梯次僅學士，不能套到碩博。春季未找到一般招生時程。'],
'0020':['春季截止及放榜官方版本差異保留；新生獎學金尚缺足夠制度資料，目前獎助為在校生115-1公告。'],
'0024':['官網常態時程未標學年度，只作每年月份參考；生活津貼金額未確認。'],
'0028':['校級獎學金金額及續領詳細條件未確認；新生尚不能申領完成兩學期後的校獎。'],
'0029':['115簡章明載不招春季；校獎為在校生申請，新生第一年不可假定取得。'],
'0031':['秋季第一梯截止原有來源差異保留；獎學金續領詳細成績門檻未確認。'],
'0033':['春季保留原有歷年參考；獎學金金額由審查決定，無固定保證額。'],
'0035':['獎學金研究生續領中文要求2門、英文9學分存在差異，需校方確認。採郵寄／親送，未找到獨立線上申請系統。'],
'0037':['獎學金完整名額、年限、續領與併領規則未確認。'],
'0044':['115秋季截止：同一本簡章中文6/18、英文6/20不同，保留衝突；各季開始日期未確認。'],
'0046':['一般學位生申請費未知；US$100只限國際蒙特梭利碩士。新系統2027日期為僑港澳，不能套用外國學生。'],
'0047':['在校生獎學金10,000–30,000元的計算期間未明，不自行換算月／年。'],
'0048':['116秋季第一階段已公告；生活津貼英文招生頁與中文／正式辦法不同，依正式辦法列擇優審查並保留差異。'],
'0049':['目前費用來源只涵蓋115-2，秋季不得直接套用；一般新生第一學期校獎資格待確認。'],
'0051':['校獎現行金額、名額、期間與續領規則未核得；115簡章另有9/8文件日期寫2025的疑似舊文，不採作2026截止。'],
'0052':['春秋開始日期未公布於所查簡章；不以截止日倒推。'],
'0053':['已確認115/2/25碩博新版獎學金；學士現行補助金額仍缺，不沿用舊搜尋快取的每月3,000元。']}
POLICY={'0020_s3':'115-1在校生公告','0024_p2':'111/05/05版，現行官網連結','0035_b':'115簡章引用106年辦法','0037_s2':'現行校方學生資源頁（2026查核）','0039_0':'115簡章／114/12/23版','0044_s':'106年版，115簡章仍引用','0046_s':'現行官網（2026查核）','0047_s':'現行官網（2026查核）','0048_p':'114/09/24版，115起入學適用','0049_p':'114/06/18版','0052_p':'113/12/30版','0053_ms':'115/02/25版','0053_phd':'115/02/25版'}
OUT={}
for id,v in F.items():
 s=ss[id];prior=copy.deepcopy(ins['schools'].get(id,{}));rec=copy.deepcopy(prior)
 intake=['fall'] if id in fallOnly else ['spring'] if id in springOnly else ['fall','spring']
 # NCYU source is fall only; NKUST checked both fall/spring.
 if id=='0018':intake=['fall']
 rec.update(applicationFee=dict(amount=v['fee'],currency='TWD',academicYear=v['year'],status='confirmed' if v['fee'] is not None else 'unconfirmed',sourceUrl=url(v['b']),sourceTitle=f"{v['year']} 一般外國學生官方招生資料",intakes=intake,notes=v['feeNote'],lastChecked=TODAY),scholarships=[],lastChecked=TODAY)
 if v.get('feeLabel'):rec['applicationFee']['amountLabel']=v['feeLabel']
 if v.get('feeExceptions'):rec['applicationFee']['exceptions']=v['feeExceptions']
 for scope,award,cont,k in v['sch']:
  rec['scholarships'].append(dict(scope=scope,award=award,continuation=cont,sourceUrl=url(k),academicYear=POLICY.get(k,v['year'] if k==v['b'] else '現行官方頁（2026查核）'),selection='reviewed',lastChecked=TODAY,summaryMy='ပညာသင်ဆုသည် လျှောက်ထားမှု၊ စစ်ဆေးမှုနှင့် သတ်မှတ်ချက်များအပေါ် မူတည်ပါသည်။ ပမာဏနှင့် ဆက်လက်ရယူရန် စည်းမျဉ်းများကို အောက်ပါ တရုတ်စာနှင့် တရားဝင်လင့်ခ်တွင် ကြည့်ပါ။'))
 rec.setdefault('requirements',[]);rec.setdefault('tuition',[])
 if id in REQ:rec['requirements'].append(dict(academicYear=v['year'],text=REQ[id],sourceUrl=url(v['b'])))
 rec['admissionNotices']=list(prior.get('admissionNotices',[]))+N.get(id,[])
 gaps=G.get(id,[]).copy()
 if v['fee'] is None:gaps.append(v['feeNote'])
 if not rec['admissionNotices']:gaps.append('尚未找到一般外國學位生官方公開榜單；不採用僑生或國際專修部名單替代。')
 if id not in REQ and not rec['requirements']:gaps.append('各系語言門檻、財力與文件細項請依本次連結之簡章；本批未逐系摘錄。')
 if not rec['tuition']:gaps.append('學雜費與住宿費未完成同年度逐系整理；尚不能計算第一年總成本。')
 rec['audit']=dict(checked=TODAY,scope='剩餘國立大學／國立科大23校；一般外國學位生',status='部分完整',gaps=gaps)
 if prior:rec.setdefault('previousVersions',[]).append(prior)
 ins['schools'][id]=rec;s['reviewState']='partially_audited';s['checked']=TODAY
 for term,vv in T.get(id,{}).items():replace(id,term,vv)
 for term in intake:
  t=s['terms'][term];y=v['year'] if '-' in v['year'] and '／' not in v['year'] else ('115-2' if term=='spring' else '116-1') if id=='0019' else '115-'+('2' if term=='spring' else '1') if v['year']=='115' else v['year']
  t['brochure']=dict(url=url(v['b']),academicYear=y,status='official' if y==target(term) else 'historical');t['sources']=list(dict.fromkeys(t.get('sources',[])+[url(v['b'])]))
 if id in A:
  hub,app=A[id];s['admission']=dict(url=hub,kind='admission')
  for term in intake:s['terms'][term]['apply']=dict(url=app or hub,kind='apply' if app else 'admission')
 # New spring portal is not silently assigned to fall.
 if id=='0053':s['terms']['spring']['apply']=dict(url='https://oia01.nkust.edu.tw/intladmission/index/index/applyIntladmissionSn/42',kind='apply')
 OUT[id]=rec
# Officially hosted external brochure, via verified official hub.
ss['0028']['terms']['fall']['brochure']['url']='https://drive.google.com/file/d/1FYSiKMBElYPpNvj_DQjsQgJGJyQrgx0m/view?usp=drive_link'
# Separate NKUST fall handbook from its spring handbook.
ss['0053']['terms']['fall']['brochure']=dict(url=url('0053_1'),academicYear='115-1',status='historical')
ss['0053']['terms']['fall']['sources']=list(dict.fromkeys(ss['0053']['terms']['fall']['sources']+[url('0053_1')]))
# Annual NPUST window: no invented year or day in source dates.
for term,a,b in [('fall',1,3),('spring',8,10)]:
 t=ss['0024']['terms'][term];t['archivedRounds']=t['rounds'];t['rounds']=[dict(name=bi('官網常態時程'),start=event(None,term,'未標學年度',url('0024_h'),'官網每年申請期間',f'{a}月開始（官網常態時程）',f'{2027 if term=="fall" else 2026}-{a:02}-01'),end=event(None,term,'未標學年度',url('0024_h'),'官網每年申請期間',f'{b}月底截止（官網常態時程）',f'{2027 if term=="fall" else 2026}-{b:02}-21'),result=None)]
 t['admissionRecords'].append(dict(schoolId='0024',semester=term,targetYear=target(term),sourceYear='未標學年度',applicationStart=None,applicationEnd=None,resultDate=None,applicationStartText=f'每年{a}月1日',applicationEndText=f'每年{b}月31日',status='historical',confidence='medium',sourceTitle='官網常態申請期間',sourceUrl=url('0024_h'),lastChecked=TODAY))
 t['notes'].append(bi('官網列常態每年時程，未指定2027年度；申請前須確認當期系統。'))
# Explicitly unavailable spring is different from not researched.
t=ss['0029']['terms']['spring'];t['archivedRounds']=t['rounds'];t['rounds']=[];t['notes'].append(bi('115簡章明載本校不招收春季班；116如有變動請以新簡章為準。','115 လမ်းညွှန်အရ နွေဦးဝင်ခွင့် မဖွင့်ပါ။'));t['availability']='not_offered_reference';t['sources'].append(url('0029_b'))
# NCYU second round applies to bachelor's only; preserve pre-existing conflict.
if len(ss['0018']['terms']['fall']['rounds'])>1:ss['0018']['terms']['fall']['rounds'][1]['scope']='undergraduate'
for r in ss['0018']['terms']['fall'].get('admissionRecords',[]):
 if not r.get('archived') and str(r.get('round'))=='2':r['scope']='undergraduate'
# NTSU bilingual discrepancy: neither date is selected as authoritative.
t=ss['0044']['terms']['fall'];r=t['rounds'][0];r['end']=dict(status='conflict',basis='115-1',sourceYear='115-1',label=bi('6/18（中文）／6/20（英文）待確認'),sourceUrl=url('0044_b'),sourceTitle='115外國學生招生簡章',confidence='low',conflicts=['2026-06-18','2026-06-20']);t['notes'].append(bi('同一本簡章中英文截止日期不同；放榜7/13可作歷年參考。'))
t['admissionRecords'][0]['applicationEndText']='中文6/18／英文6/20，待確認';t['admissionRecords'][0]['conflicts']={'applicationEnd':['2026-06-18','2026-06-20']}
# Explicit document/postal/e-mail submission reminders.
for id,text in {'0028':'線上填表後仍須郵寄／親送，詳見简章；不是只按線上送出即可。','0033':'115秋季申請截止為5/13中午12時，繳費另至17時，不是相同截止。','0035':'採郵寄或親送文件，未找到獨立線上申請入口。','0042':'115秋季採電子郵件報名，請依簡章指定信箱寄件。','0046':'入口含多種身分，請選外國學生 International Student Admission；2027僑港澳日期不適用。','0051':'115簡章線上報名後須依規定送件，請詳讀送件流程。'}.items():ss[id]['terms']['fall']['notes'].append(bi(text))
d['updated']=TODAY;ins['updated']=TODAY
# Reuse coverage writer only.
exec(old[old.index('summary={}'):old.index("print('Merged'")])
(H/'facts.json').write_text(json.dumps(OUT,ensure_ascii=False,indent=2)+'\n')
used={v['b'] for v in F.values()}|{q[3] for v in F.values() for q in v['sch']}
(H/'source-manifest.json').write_text(json.dumps({k:manifest[k] for k in sorted(used)},ensure_ascii=False,indent=2)+'\n')
print('Merged',len(F),'registry',len(ss),'audited',sum(s.get('reviewState') in ['audited','partially_audited'] for s in ss.values()),'confirmedFees',sum(v['fee'] is not None for v in F.values()))
