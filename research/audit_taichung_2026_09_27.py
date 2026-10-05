"""Apply the bounded Taichung audit to the immutable pre-audit snapshot.
Only official admission documents/policies were read. Admission lists are links only.
"""
import json,copy
from pathlib import Path
R=Path(__file__).resolve().parents[1]; B=R/'research/backups/2026-09-27'; C=R/'research/audit-2026-09-27'
d=json.loads((B/'schools.json').read_text()); ins=json.loads((B/'school-insights.json').read_text()); ss={s['id']:s for s in d['schools']}; ii=ins['schools']; TODAY='2026-09-27'
IDS=['1008','1007','1001','1018','1048','0006','0050','0043','1062','1034','1045']
def src(n):return json.loads((C/'sources.json').read_text())[n]['url']
def bi(z,m='တရားဝင်ရင်းမြစ်နှင့် အောက်ပါ တရုတ်စာအသေးစိတ်ကို စစ်ဆေးပါ။'):return {'zh':z,'my':m}
def fee(id,amount,url,intakes,notes,status=None):
 old=copy.deepcopy(ii[id]['applicationFee']);ii[id]['applicationFee']={'amount':amount,'currency':'TWD' if amount is not None else None,'academicYear':'115','intakes':intakes,'status':status or ('confirmed' if amount is not None else 'brochure_no_amount'),'sourceTitle':'115學年度外國學生招生簡章','sourceUrl':url,'notes':notes,'lastChecked':TODAY,'previousRecords':[old]}
def sch(id,scope,award,continuation,url,year,**extra):
 row=dict(scope=scope,award=award,continuation=continuation,sourceUrl=url,academicYear=year,selection='reviewed',lastChecked=TODAY,**extra)
 ii[id].setdefault('scholarships',[]).append(row);return row
def notice(id,year,term,title,url):
 n=dict(academicYear=str(year),semester=term,sourceTitle=title,sourceUrl=url,scope='foreign_degree')
 if n not in ii[id]['admissionNotices']:ii[id]['admissionNotices'].append(n)
def event(date,term,year,url,title,text=None):
 status='official' if year==('115-2' if term=='spring' else '116-1') else 'historical'
 e=dict(status=status,basis=year,sourceYear=year,sourceUrl=url,sourceTitle=title,confidence='high' if status=='official' else 'medium',rawDate=date)
 if date and status=='official':e['date']=date
 elif date:
  y,m,day=map(int,date.split('-'));part=0 if day<=10 else 1 if day<=20 else 2;sy=int(year.split('-')[0])+1911+(term=='spring')
  e.update(label=bi(f'{m} 月'+['上旬','中旬','下旬'][part],f'{m} လ '+['အစပိုင်း','အလယ်ပိုင်း','နှောင်းပိုင်း'][part]),sort=f'{y+2027-sy:04}-{m:02}-{[1,11,21][part]:02}',precision='ten-day',sortIsReference=True)
 elif text:
  e.update(label=bi(text[0],text[1]),sort=text[2],precision='interval',sortIsReference=status=='historical')
 else:return None
 return e
def replace(id,term,year,rows,url,title):
 t=ss[id]['terms'][term]; old=copy.deepcopy(t.get('admissionRecords',[]));t.setdefault('archivedRounds',[]).extend(copy.deepcopy(t['rounds']));t.setdefault('archivedNotes',[]).extend(t.get('notes',[]));t['notes']=[];t['rounds']=[];rr=[]
 for n,vals in enumerate(rows,1):
  r={'name':bi(str(n),str(n)),'sourceYear':year,'sourceUrl':url,'scope':t.get('scope','all')}
  record=dict(schoolId=id,semester=term,targetYear='115-2' if term=='spring' else '116-1',sourceYear=year,status='official' if year==('115-2' if term=='spring' else '116-1') else 'historical',confidence='high' if term=='spring' else 'medium',sourceTitle=title,sourceUrl=url,lastChecked=TODAY,round=str(n),scope=t.get('scope','all'),sourceType='official-primary')
  for key,field,value in zip(['start','end','result'],['applicationStart','applicationEnd','resultDate'],vals):
   date=value if isinstance(value,str) else None;r[key]=event(date,term,year,url,title,value if isinstance(value,tuple) else None);record[field]=date
   if isinstance(value,tuple):record[field+'Text']=value[0];record[field+'TextMy']=value[1]
  t['rounds'].append(r);rr.append(record)
 for r in old:r['archived']=True
 t['admissionRecords']=rr+[r for r in old if r['status']!='unknown'];t['sources']=list(dict.fromkeys([url]+t.get('sources',[])))
def brochure(id,term,url,year):ss[id]['terms'][term]['brochure']={'url':url,'status':'official' if year==('115-2' if term=='spring' else '116-1') else 'historical','academicYear':year}
def portal(id,url,term=None,kind='admission'):
 if term:ss[id]['terms'][term]['apply']={'url':url,'kind':kind}
 else:ss[id]['admission']={'url':url,'kind':kind}
for id in IDS:
 ss[id]['checked']=TODAY;ss[id]['reviewState']='audited';ii[id]['lastChecked']=TODAY
 ii[id]['audit']={'checked':TODAY,'scope':'一般外國學位生；臺中核心11校','status':'部分完整','gaps':[]}
# Fee evidence from the actual readable 115 brochures; silence never means free.
for id,name,intakes in [('1008','pu115',['fall','spring']),('1018','cyut115',['fall','spring']),('0006','nchu115',['fall','spring']),('0050','ntcust115',['fall'])]:
 fee(id,None,src(name),intakes,'已檢查115學年度簡章，未能確認明確申請費；目前未找到可靠申請費資料。未知不等於免費。')
fee('1001',0,src('thu115'),['fall','spring'],'115簡章申請費用明載「免費」。116秋季仍須核對新簡章。')
fee('0043',0,src('ncut115'),['fall'],'115簡章明載外國學生申請入學不收取申請費用。')
fee('1045',0,src('ltu'),['fall'],'115秋季簡章明載 Application Fee: None；不得直接套用春季。')
fee('1034',0,src('hku115'),['fall','spring'],'115簡章明載免申請費，涵蓋2026秋季與2027春季；116秋季仍以新簡章為準。')
fee('1007',None,'https://www.fcu.edu.tw/recurit_list/international-fall-semester/',['fall'],'115秋季公告已找到，但所連簡章導向Microsoft登入，無法核讀收費條文；不推定免費。','brochure_unreadable')
fee('1062',None,'https://admission.ocu.edu.tw/p/406-1023-72739%2Cr1364.php',['fall'],'找到115秋季外國學生簡章公告；官方網站回應錯誤，尚無法核讀金額。','brochure_unreadable')
ii['1048']['applicationFee']['notes']='114官方附件本次仍無法讀取；115官方招生簡章亦有線索，但附件無法核讀。搜尋摘要不作金額依據，暫不填0。'
# PU: two independently documented rounds, Chinese/native-language conditions.
u='https://oia.pu.edu.tw/p/426-1048-11.php'
replace('1008','spring','115-2',[('2026-08-01','2026-10-15','2026-11-30'),('2026-10-16','2026-11-15','2026-12-24')],u,'115學年度外國學生招生時程／國際處')
replace('1008','fall','115-1',[('2026-01-12','2026-04-30','2026-06-04'),('2026-05-01','2026-06-15','2026-07-30')],u,'115學年度外國學生招生時程／國際處')
for term in ['spring','fall']:brochure('1008',term,src('pu115'),'115-2' if term=='spring' else '115-1')
x=ii['1008']['scholarships'][0];x.update(academicYear='115',policyDate='2025-06-11',scope='非華語母語之外國新生，中文授課學程',continuation='第二年起依前一學期排名審核：前15% 35,000元，15.01–30% 20,000元，30.01–50% 8,000元。班級少於7人時，僅第1名可申請35,000元。不得視為保證續領。',application='在入學申請系統填寫並上傳助學金申請書。',sourceUrl=src('pu115'))
x['summaryMy']='တရုတ်ဘာသာ မိခင်ဘာသာမဟုတ်သော ကျောင်းသားသစ်များအတွက် ဖြစ်သည်။ TOCFL B1 သို့မဟုတ် သတ်မှတ်သင်ချိန်ဖြင့် ကျောင်းလခနှင့် အထွေထွေကြေး၊ A2 ဖြင့် ကျောင်းလခ ထောက်ပံ့မှုကို လျှောက်နိုင်သည်။ ဒုတိယနှစ်မှ ယခင်စာသင်ကာလ အတန်းအဆင့်ကို စစ်ဆေးသည်။'
ii['1008']['scholarships'][1].update(academicYear='115',scope='非英語母語之外國新生（全英語學程）；博士另依專款',sourceUrl=src('pu115'),application='須隨入學申請提交助學金申請書。')
notice('1008',114,'spring','春季外國學生第二梯次錄取公告','https://oia.pu.edu.tw/p/16-1048-68428.php?Lang=zh-tw')
# FCU: title says2027 but fall body explicitly115; use body/source year, never plus-one as official.
fu='https://www.fcu.edu.tw/recurit_list/international-fall-semester/';su='https://www.fcu.edu.tw/recurit_list/international-spring-semester/'
replace('1007','fall','115-1',[('2025-12-17','2026-03-04','2026-03-24'),('2026-03-06','2026-04-15','2026-05-05'),('2026-04-17','2026-06-10','2026-06-30'),('2026-06-12','2026-07-08','2026-07-24')],fu,'115學年度秋季外國學生招生四梯時程')
ss['1007']['terms']['fall']['notes']=[bi('官方頁面標題含2027，但內文為115學年度2026秋季四梯；本頁依內文標為115歷年參考，不視為116正式公告。')]
replace('1007','spring','115-2',[('2026-09-15','2026-11-08','2026-11-24'),('2026-11-11','2026-11-30','2026-12-15')],su,'115學年度第2學期（2027春季）外國學生招生時程')
portal('1007',fu);portal('1007','https://admissions-fee.fcu.edu.tw/W710107/index.aspx#/tw','spring','apply');portal('1007',fu,'fall')
brochure('1007','spring',su,'115-2');brochure('1007','fall',fu,'115-1')
ii['1007']['scholarships']=[]
fpolicy='https://myfcu.fcu.edu.tw/main/S6800/S680004_Out_Download.aspx?newfilename=9aa467b3c791471f8c4a137a82c41efa_2_1.pdf&originfilename=逢甲大學海外華裔學生暨外國學生獎助學金設置要點_114學年度起獲獎學生適用.pdf'
sch('1007','海外華裔學生暨外國學生獎助學金；一般外國學位生可申請','每學年120,000／60,000／30,000／20,000元，分兩學期核發。須先繳清學雜費；依審查、預算及名額核定。','第二年起由校方依成績評核；學士平均70或班級前50%，研究所80。學士最長4年（部分學制5年），碩博士2年。不得與臺灣獎學金併領。',fpolicy,'114起適用',policyDate='2024-12-09',application='新生須於線上入學申請時提出；續讀自動列入評核不等於自動獲獎。',summaryMy='နိုင်ငံခြားသားဘွဲ့သင်တန်းများအတွက် တစ်နှစ် NT$120,000 / 60,000 / 30,000 / 20,000 ကို ရွေးချယ်ချီးမြှင့်သည်။ ကျောင်းဝင်ခွင့်လျှောက်စဉ် လျှောက်ရသည်။ ကျောင်းလခကို အရင်ပေးရပြီး ဆက်လက်ရရှိရန် အမှတ်နှင့် ဘတ်ဂျက်ကို စစ်ဆေးသည်။')
# THU dates: interval stays interval, document deadline never used as application end.
tu='https://exam2.thu.edu.tw/EXAM/download_doc_25/21.pdf'
replace('1001','fall','115-1',[('2026-01-21','2026-02-28',('4月10日前','4 လ 10 ရက်မတိုင်မီ','2027-04-01')),('2026-03-01','2026-03-31',('5月初','5 လ အစပိုင်း','2027-05-01')),('2026-04-01','2026-04-30',('6月初','6 လ အစပိုင်း','2027-06-01')),('2026-05-01','2026-05-27',('7月初','7 လ အစပိုင်း','2027-07-01'))],tu,'115學年度外國學生招生重要日期')
replace('1001','spring','115-2',[('2026-10-01','2026-10-31',('2026年12月初','2026 ခုနှစ် 12 လ အစပိုင်း','2026-12-01'))],tu,'115學年度第2學期外國學生招生重要日期')
for term,doc in [('spring',26),('fall',25)]:
 portal('1001',f'https://exam2.thu.edu.tw/EXAM/index.jsp?DOC={doc}',term);brochure('1001',term,f'https://exam2.thu.edu.tw/EXAM/index3_1_main.jsp?DOC={doc}','115-2' if term=='spring' else '115-1')
ii['1001']['scholarships']=[]
sch('1001','外國學生獎助學金；新生與在校學士、碩士、博士','學士每學年100,000／60,000／20,000元；碩博士100,000／60,000元。審查型、依年度經費核定。','在校學士GPA2.93以上或班級前25%；碩博士GPA3.38以上。新生入學後第一年採前一學期、第二年起採前兩學期成績。學士最多4年（建築5年）、碩博士2年；每年重新申請，通常每學期服務10小時。',src('thuRule'),'2023-06-07辦法（115招生仍引用）',policyDate='2023-06-07',application='新生於入學申請勾選；續讀年度另申請。不得與臺灣政府獎學金或本校傑出新生獎學金併領。',summaryMy='ဘွဲ့ကြိုအတွက် တစ်နှစ် NT$100,000 / 60,000 / 20,000၊ မဟာနှင့်ဒေါက်တာအတွက် NT$100,000 / 60,000 ကို စစ်ဆေးရွေးချယ်ပေးသည်။ နှစ်စဉ် ပြန်လျှောက်ရပြီး အမှတ်နှင့် ဝန်ဆောင်မှုသတ်မှတ်ချက်များ ရှိသည်။')
# Keep good existing CYUT rules/requirements; current brochure available for both seasons.
portal('1018','https://icsc.cyut.edu.tw/p/404-1008-58738.php?Lang=zh-tw')
for term in ['spring','fall']:brochure('1018',term,src('cyut115'),'115-2' if term=='spring' else '115-1')
ii['1018']['scholarships'][0]['academicYear']='現行官網辦法（查核2026-09-27；頁面未明列修訂年）'
# NCHU scope and current scholarship entry.
portal('0006','https://oiaapply.nchu.edu.tw',kind='apply')
ss['0006']['terms']['spring']['scopeLabel']=bi('春季僅研究所','နွေဦး ဘွဲ့လွန်သာ')
for term in ['spring','fall']:brochure('0006',term,src('nchu115'),'115-2' if term=='spring' else '115-1')
ii['0006']['scholarships'][0]['sourceUrl']='https://oia.nchu.edu.tw/index.php/4-current-student-en/4-1-international-degree-and-dual-degree-students-en/4-1-2-current-students-en/4-1-2-5-scholarship-en'
ii['0006']['scholarships'][0]['restrictions']='學費減免不含住宿、保險及電腦網路費。新生勾選申請，在校生須依每年公告另申請；生活津貼僅少數名額。'
# NTCUST: second round + current policy supersedes brochure's older half/full text.
nu='https://oia.nutc.edu.tw/var/file/42/1042/img/506068650.pdf'
replace('0050','fall','115-1',[('2025-11-18','2026-01-06','2026-02-06'),('2026-04-22','2026-07-05','2026-07-31')],src('ntcust115'),'115學年度外國學生第一、第二階段招生簡章')
# First round keeps its own source, rather than attributing it to second-stage PDF.
for obj in [ss['0050']['terms']['fall']['rounds'][0],ss['0050']['terms']['fall']['admissionRecords'][0]]:obj['sourceUrl']=nu
for key in ['start','end','result']:ss['0050']['terms']['fall']['rounds'][0][key]['sourceUrl']=nu
portal('0050','https://recruit.nutc.edu.tw/oia/ITNS',kind='apply');ss['0050']['terms']['spring']['notes']=[bi('115學年度簡章僅開放秋季入學；未提供115-2春季申請。','115 လမ်းညွှန်တွင် ဆောင်းဦးဝင်ခွင့်သာ ဖော်ပြထားသည်။ 115-2 နွေဦး လျှောက်လွှာ မဖွင့်ထားပါ။')];ss['0050']['terms']['spring']['availability']='not_offered_in_source'
brochure('0050','fall',src('ntcust115'),'115-1');ii['0050']['scholarships']=[]
sch('0050','外國學生獎助學金；一般外國學位生','新生第一學年註冊時直接減免，每學期最高25,000元。其他受獎者中，前1/5名額每學期最高50,000元，其餘最高25,000元；依預算核給。','續讀學士平均75、研究所80、操行80；每學期須完成60小時服務。獎助以學年核定；學士最多4年、二技及碩博士2年；不得與政府獎學金併領。','https://oia.nutc.edu.tw/var/file/42/1042/img/422285790.pdf','115起適用',policyDate='2026-05-19',application='新生第一年免申請；在校生於第一學期開學兩週內提出。',restrictions='115簡章較早版本載半額／全額；本頁採2026-05-19新辦法的金額上限，保留較早簡章作比較。',summaryMy='115 မှစ၍ ကျောင်းသားသစ် ပထမနှစ်တွင် တစ်စာသင်ကာလ အများဆုံး NT$25,000 လျှော့ပေးသည်။ ဆက်လက်ရယူရန် အမှတ်၊ အကျင့်စာရိတ္တနှင့် တစ်ကာလ ဝန်ဆောင်မှု နာရီ 60 လိုသည်။ ဘတ်ဂျက်အရ ဆုံးဖြတ်သည်။')
# NCUT: 115 cohort rules, not older 108–110 conditions.
portal('0043','https://admission.ncut.edu.tw/',kind='apply');brochure('0043','fall',src('ncut115'),'115-1');ii['0043']['scholarships']=[]
sch('0043','115入學一般外國學位新生；特殊專班另依專案','學士第一學年學雜費減半；碩士第一學期減半（原外國學生專修部升碩士者另依規定）；博士前兩學年學雜費全免。碩士另每學期5,000元，原則最多4學期，特定身分最多2學期。','入學減免依身分與在學狀態核給，不能推定其後學年全免；不得與政府或同類校內獎助併領。',src('ncut115'),'115入學起',policyDate='2026-01-05',application='入學註冊後由承辦單位造冊辦理；金額及排除身分依簡章附錄。',summaryMy='115 ဝင်ခွင့်မှစ၍ ဘွဲ့ကြို ပထမနှစ် ကျောင်းလခနှင့် အထွေထွေကြေး တစ်ဝက်၊ မဟာဘွဲ့ ပထမစာသင်ကာလ တစ်ဝက် လျှော့ပေးသည်။ ဒေါက်တာ ပထမနှစ်နှစ် အပြည့်လျှော့ပေးသည်။ အထူးအစီအစဉ်များအတွက် သီးခြားစည်းမျဉ်း ရှိသည်။')
sch('0043','115起入學一般外國學士生，第二學年起學業優良獎學金','每學期30,000元；須符合條件及審查。','每學期至少9學分、班級前50%、無不及格或缺漏成績、無懲處；體育70分以上（免修／選修例外）、已繳學雜費。排除產學、INTENSE、僑港澳、交換及雙聯等身分，不得與政府或同類獎助併領。',src('ncut115'),'115入學起',application='由承辦單位依成績資料造冊審查。',summaryMy='115 မှ ဝင်ခွင့်ရသော ပုံမှန်နိုင်ငံခြားသားဘွဲ့ကြိုများသည် ဒုတိယနှစ်မှ တစ်စာသင်ကာလ NT$30,000 ကို သတ်မှတ်ချက်နှင့်အညီ ရနိုင်သည်။ အနည်းဆုံး ခရက်ဒစ် 9၊ အတန်းရှေ့ 50% နှင့် ဘာသာရပ်မကျခြင်း စသည့်လိုအပ်ချက် ရှိသည်။')
sch('0043','一般外國博士生生活助學金','每月10,000元，每學期6個月，至多4學期。','續領前一學期學業70、操行80且無記過；論文階段得依指導教授審核規定辦理。',src('ncut115'),'115簡章所附2022-01-05辦法',application='依在學狀態及每學期續領規定審核；不是學士或碩士普遍補助。')
notice('0043',115,'fall','115學年度外國學生錄取公告（招生系統公告入口）','https://admission.ncut.edu.tw/')
# LTU new July115 regulation supersedes earlier brochure scholarship ceiling.
portal('1045','https://ltu1473.video.ltu.edu.tw/p/page1');brochure('1045','fall',src('ltu'),'115-1');ii['1045']['scholarships']=[]
sch('1045','115起一般外國學士／碩士生；不含國際專修部、產學及其他特殊專班','一般每學期15,000元；學士班級前3名可核給每學期30,000元。依審查及經費核定。','續領前學期平均85、操行82，TOCFL B1（新生第一年免此語言條件）；須完成規定服務／講座。不得與政府獎學金併領。','https://ltu1475.video.ltu.edu.tw/filedownload/587','115入學起',policyDate='2026-06-22',application='新生隨入學申請，在校生依公告申請。',restrictions='較早115秋季簡章寫首學期最高25,000元；較新115年7月公布辦法改為15,000元。本頁採新辦法；保留兩個來源，申請前請向國際處確認適用批次。',relatedSourceUrl=src('ltu'),summaryMy='115 မှ ဝင်ခွင့်ရသော ပုံမှန်နိုင်ငံခြားသားများအတွက် တစ်စာသင်ကာလ NT$15,000၊ ဘွဲ့ကြို အတန်းထိပ်ဆုံး 3 ဦးအတွက် NT$30,000 ကို စစ်ဆေးပေးသည်။ ဆက်လက်ရရှိရန် ပျမ်းမျှ 85၊ အကျင့်စာရိတ္တ 82 နှင့် TOCFL B1 လိုသည်။ ကျောင်းသားသစ် ပထမနှစ်တွင် B1 ကင်းလွတ်သည်။')
# HKU: 115 brochure covers2027spring;116fall web conflict intentionally preserved.
portal('1034','https://ifp.hk.edu.tw/入學申請/外國學生/');portal('1034','https://forms.gle/Yoz15TzePD1HMLzY9','spring','apply');brochure('1034','spring',src('hku115'),'115-2');ii['1034']['scholarships']=[]
sch('1034','境外學生獎學金；包括一般外國學位生','115簡章列每學期A級50,000、B級30,000、C級10,000、D級5,000元；須申請及審核。','新生與續讀依不同審核條件。最新續領細則、名額及可否併領請以校方獎學金辦法確認，尚未核得的門檻不當作已確認。',src('hku115'),'115',application='並非錄取自動取得；依國際處當期申請公告辦理。',summaryMy='115 လမ်းညွှန်တွင် တစ်စာသင်ကာလ NT$50,000 / 30,000 / 10,000 / 5,000 ဟု ဖော်ပြသည်။ လျှောက်ထားပြီး စစ်ဆေးရွေးချယ်မည်။ ဆက်လက်ရယူရန် စည်းမျဉ်းနှင့် အခြားဆု ပူးတွဲယူခွင့်ကို ကျောင်းနှင့် အတည်ပြုပါ။')
# Partial access: preserve verified existing ASIA schedules, not search-snippet fee.
for term in ['spring','fall']:
 ss['1048']['terms'][term]['notes'].append(bi('本次確認官方線上系統仍列115時程；簡章及獎學金附件暫時無法重讀。春季系統截止11/30，另有簡章11/29線索，請提早於11月底前送件並向校方確認。'))
portal('1048','https://admission.asia.edu.tw/AsiaGlobalAdmissions/ForeignStudent',kind='apply')
ii['1048']['scholarships']=[{'scope':'一般外國學位生校級獎學金','award':None,'continuation':None,'academicYear':None,'sourceUrl':'https://oia.asia.edu.tw/p/412-1008-265.php?Lang=en','selection':'unverified','restrictions':'已找到官方獎學金入口，但本次附件回應錯誤；金額、期間及續領條件尚未能核讀，不將搜尋摘要當正式制度。','summaryMy':'တရားဝင် ပညာသင်ဆုစာမျက်နှာ ရှိသော်လည်း ယခုစစ်ဆေးစဉ် ဖိုင်ကို ဖတ်မရပါ။ ငွေပမာဏနှင့် သတ်မှတ်ချက်ကို မအတည်ပြုရသေးပါ။'}]
ii['1062']['scholarships']=[{'scope':'一般外國學位生獎學金及境外生活助學金','award':None,'continuation':None,'academicYear':None,'sourceUrl':'https://ia.ocu.edu.tw/p/412-1013-2834.php?Lang=zh-tw','selection':'unverified','restrictions':'官方法規入口有外國學生獎學金及境外生活助學金辦法，但本次網站回應錯誤，未核讀條文；不推定金額或可併領。','summaryMy':'တရားဝင် ပညာသင်ဆုနှင့် နေထိုင်မှုထောက်ပံ့ကြေး စည်းမျဉ်းစာမျက်နှာ ရှိသည်။ ဖိုင်ကို ဖတ်မရသဖြင့် ပမာဏနှင့် သတ်မှတ်ချက် မအတည်ပြုရသေးပါ။'}]
brochure('1062','fall','https://admission.ocu.edu.tw/p/406-1023-72739%2Cr1364.php','115-1')
# Audit gaps are data, not fake zeros or discontinued-admission claims.
gaps={
'1008':['申請費尚無明確官方金額；116秋季待公布'], '1007':['簡章附件導向登入，申請費未核得；116秋季待公布'], '1001':['116秋季未公布；沿用115四梯參考'], '1018':['申請費及部分開始／放榜日期未核得；具體續領門檻待當期公告'], '0006':['申請費未核得；春季僅研究所，不能當學士招生'], '0050':['申請費未核得；115簡章僅秋季'], '0043':['春季時程未找到；116秋季未公布'], '1045':['春季費用／時程未核得；較早簡章與較新獎學金辦法差異已保留'], '1034':['116秋季第二梯中英文申請期不一致；獎學金最新續領細則未完整核讀'], '1048':['115簡章附件及獎學金條文無法讀取；申請費未核得；春季截止有11/29與11/30線索差異'], '1062':['官方網站回應錯誤；近年申請時程、申請費、獎學金條文未核得；未找到獨立線上申請入口']}
for id in IDS:
 ii[id]['audit']['gaps']=gaps[id]
 if id in ['1048','1062']:ss[id]['reviewState']='partially_audited'
 for s in ii[id].get('scholarships',[]):s.setdefault('lastChecked',TODAY)
# Recompute derived data from active events only; no new schools.
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
print('Audited 11 Taichung schools; registry stays',len(d['schools']));print({k:v['counts'] for k,v in summary.items()})
