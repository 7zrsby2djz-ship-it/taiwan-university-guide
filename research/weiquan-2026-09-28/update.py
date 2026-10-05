import json,copy
from pathlib import Path
R=Path(__file__).resolve().parents[2];H=Path(__file__).resolve().parent
read=lambda p:json.loads(p.read_text());d=read(H/'schools-before.json');ins=read(H/'insights-before.json');ss={s['id']:s for s in d['schools']};TODAY='2026-09-28'
ids=[s['id'] for s in d['schools'] if '臺中市' in s['cities'] or s['abbr'] in ['NIU','NTPU','NCYU','NPUST','NUTN','NKUHT','NTUT','NTUB','NCNU','NUU']]
for id in ids:ss[id]['weiquan']=True
bi=lambda z:{'zh':z,'my':z}
def official(date,year,u,title):return dict(status='official',date=date,rawDate=date,sourceYear=year,basis=year,sourceUrl=u,sourceTitle=title,confidence='high')
def snapshot(id):
 v=ins['schools'][id];v.setdefault('previousVersions',[]).append(copy.deepcopy({k:x for k,x in v.items() if k!='previousVersions'}));v['lastChecked']=TODAY
# School-specific updates only. Recent reliable research for other chosen schools is reused.
u='https://examstd.nkuht.edu.tw/EnrollSTDFS/';t=ss['0047']['terms']['fall'];t.setdefault('archivedRounds',[]).append(copy.deepcopy(t['rounds'][0]));r=t['rounds'][0]
for k,date in [('start','2026-11-02'),('end','2026-12-17')]:r[k]=official(date,'116-1',u,'116-1一般外國學生線上申請系統')
r['sourceYear']='116-1';r['sourceUrl']=u;r['note']=bi('第一梯申請期間已採116-1系統；放榜仍為115-1歷年參考，第二梯亦仍為歷年參考。各系截止時刻不同，請以系統個別欄位為準。')
t['notes'].append(bi('116-1系統已公告11/2–12/17；觀光所碩士班截止12:59，其他多數系為23:59。尚未確認本期放榜日期。'))
t['sources']=list(dict.fromkeys([u]+t['sources']));t['apply']=dict(url=u,kind='apply');ss['0047']['checked']=TODAY
for rec in t.get('admissionRecords',[]):
 if str(rec.get('round'))=='1':rec['archived']=True
t['admissionRecords'].insert(0,dict(schoolId='0047',semester='fall',targetYear='116-1',sourceYear='116-1',applicationStart='2026-11-02',applicationEnd='2026-12-17',resultDate=None,status='official',confidence='high',sourceTitle='116-1外國學生申請系統',sourceUrl=u,lastChecked=TODAY,round='1',scope='all'))
snapshot('0047');ins['schools']['0047']['admissionNotices'].append(dict(academicYear='115',semester='fall',sourceTitle='115一般外國學生第二梯次錄取公告入口（與國際專修部分列）',sourceUrl='https://international.nkuht.edu.tw/p/404-1045-21221.php?Lang=en',scope='foreign_degree'))
# NTUT has explicit no-fee text. Preserve spring-only coverage and result conflict.
snapshot('0025');v=ins['schools']['0025'];u='https://oia.ntut.edu.tw/var/file/32/1032/img/2027SpringAdmissionHandbook.pdf'
v['applicationFee']=dict(amount=0,currency='TWD',status='confirmed',academicYear='115-2',intakes=['spring'],sourceUrl=u,sourceTitle='2027 Spring Admission Handbook 第6頁',notes='簡章第6頁明載「無申請費用／None」。本筆確認115-2春季；不以此直接宣稱116-1秋季已公告免費。',lastChecked=TODAY)
pres=v['scholarships'][0];pres.update(award='第一學年全額學雜費補助：全額獎每月15,000元（6名）；半額獎每月8,000元（20名）。兩類均補助全額學雜費，不含住宿、保險、網路、書籍與代辦費。',sourceUrl='https://oia.ntut.edu.tw/p/404-1032-150266.php?Lang=zh-tw',academicYear='113秋季起適用；現行官網2026查核',continuation='僅第一學年、不可續領；高中GPA2.8/4或70分以上，非僑生、無中華民國國籍、未全職工作，不能兼領政府或校內其他獎助。入學申請時勾選獎學金並同步擇優審查；達門檻不保證獲獎，休學不保留。',selection='competitive')
v.setdefault('audit',{}).setdefault('gaps',[]);v['audit']['gaps']=[x for x in v['audit']['gaps'] if '申請費' not in x];v['audit']['gaps'].append('116-1秋季申請費未由本次春季簡章推定；春季招生系所表只有碩博士，年度總名額中的學士60名不代表春季開放學士。')
t=ss['0025']['terms']['spring'];t['scope']='graduate';t['brochure']=dict(url=u,academicYear='115-2',status='official')
for r in t['rounds']:
 r['scope']='graduate'
 for k in ['start','end','result']:
  if r.get(k):r[k]['scope']='graduate'
for r in t.get('admissionRecords',[]):
 if not r.get('archived'):r['scope']='graduate'
t['notes'].append(bi('115-2簡章招生系所表僅列碩博士；學士申請請看秋季。本期放榜簡章11/6、招生首頁11月中旬，保留差異。'))
# NTUB: currently linked official English program, undated version is explicit.
snapshot('0051');v=ins['schools']['0051'];v['scholarships']=[dict(scope='外國籍學生獎學金（一般外國學位生）',award='每位受獎學生每學期NT$15,000；實際名額視申請人數與年度經費，不是每月15,000元。',continuation='新入學與在校學士／研究生均可申請，僑生及陸生不適用；已領其他獎學金者不得申請。在校學士前學期平均高於75分、操行高於80；研究生平均高於80、操行高於80，無處分。論文階段可依指導教授推薦與論文計畫另申請一次；須提出申請，非錄取自動發放。',sourceUrl='https://oia.ntub.edu.tw/p/412-1006-2161.php?Lang=en',relatedSourceUrl='https://stud.ntub.edu.tw/p/406-1007-53808,r937.php?Lang=zh-tw',academicYear='現行官方英文說明（未標辦法年份），2026-09-28查核',selection='reviewed',lastChecked=TODAY)]
v['audit']['gaps']=[x for x in v['audit']['gaps'] if '校獎現行金額' not in x];v['audit']['gaps'].append('獎學金英語頁未標修訂年份；實際本期申請期限與預算名額依學務處公告。')
# CMU current general admissions hub now lists spring round 2; no list parsing.
u='https://cmucia.cmu.edu.tw/admission_international.html';t=ss['1035']['terms']['spring'];t['scope']='graduate'
r=dict(name=bi('2'),scope='graduate',sourceYear='115-2',sourceUrl=u,start=official('2026-09-14','115-2',u,'115春季第二梯次一般外國學生'),end=official('2026-11-06','115-2',u,'115春季第二梯次一般外國學生'),result=None,note=bi('春季僅碩博士；截止當日17:00，放榜日未核得。'))
t['rounds']=[x for x in t['rounds'] if x.get('name',{}).get('zh')!='2']+[r]
t['brochure']=dict(url='https://cmucia.cmu.edu.tw/english/doc/Application_Guidelines115.pdf',academicYear='115-2',status='official');t['admissionRecords'].append(dict(schoolId='1035',semester='spring',targetYear='115-2',sourceYear='115-2',applicationStart='2026-09-14',applicationEnd='2026-11-06',resultDate=None,status='official',confidence='high',sourceTitle='115春季第二梯次一般外國學生',sourceUrl=u,lastChecked=TODAY,scope='graduate',round='2'));ss['1035']['checked']=TODAY
ins['schools']['1035']['admissionNotices'].append(dict(academicYear='115',semester='spring',sourceTitle='115-2春季第一梯次外國學生原始榜單',sourceUrl='https://cmucia.cmu.edu.tw/english/doc/cmulist_2027spring_1st.pdf',scope='foreign_degree'))
# Preserve disputed user-supplied free claims as unconfirmed, not zero.
for id in ['0031','0017','0036','0047']:
 v=ins['schools'][id];f=v['applicationFee'];f['notes']+=' 未找到適用全校及當期的官方免費明文；簡章未列收費不等於免收。'
# Extra Taichung admissions portal and original notice, no aggregate student figures.
ss['1047']['terms']['fall']['apply']=dict(url='https://adm.ctust.edu.tw/CTUSTWeb/signup.htm',kind='apply')
ins['schools']['1029'].setdefault('admissionNotices',[]).append(dict(academicYear='115',semester='fall',sourceTitle='115秋季外國學生錄取公告',sourceUrl='https://recruit.csmu.edu.tw/p/406-1019-77265%2Cr1.php?Lang=zh-tw',scope='foreign_degree'))
# Registry stays139 and verified-school membership stays51; personal group is independent.
d['updated']=TODAY;ins['updated']=TODAY
old=(R/'research/audit-national-2026-09-27/merge.py').read_text();exec(old[old.index('summary={}'):old.index("print('Merged'")])
(H/'scope.json').write_text(json.dumps([dict(id=id,name=ss[id]['name'],abbr=ss[id]['abbr']) for id in ids],ensure_ascii=False,indent=2)+'\n')
(H/'README.md').write_text('''# 偉銓27校／每月申請視窗
2026-09-28更新。只修改選定27校與所需介面。重用9/27–9/28核對過且無新衝突的官方資料。
新增：高餐116-1申請11/2–12/17；保留115-1放榜及第二梯歷年參考。中國醫115-2研究所第二梯9/14–11/6。北科春季簡章明載免申請費，不能套到尚未核實的秋季；春季系所表限研究所，既有放榜衝突保留。北科校長獎學雜費與津貼分全半額、名額及第一年限制；北商官方每學期15000元含申請與成績條件。
宜蘭／北大／臺南／高餐本次0元說法未獲適用全校及當期的官方明文支持，未改0。北大找到部分英語研究所免費不能套到學士。高餐舊FAQ只寫2019–2020免費，不當作本期資料。
榜單只提供原始連結；未把使用者提供的科系人數、緬甸國籍或錄取情形當已驗證統計。
月份依原資料date/sort安排；參考日期保留來源年度和區間，不生成虛構正式日期。衝突、缺日期不放入月事件，另列待確認。學校詳情能返回原月份。
「偉銓」27校與「已核對」51校獨立，不因加入個人名單而自動升格為已核對。
''')
print('Personal group',len(ids),'registry',len(ss))
