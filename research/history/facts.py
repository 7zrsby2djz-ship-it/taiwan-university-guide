"""Manually checked official-source dates; never shifted to a target year."""
import json
from pathlib import Path
records=[]
def add(id, season, year, start, end, result, url, title, round='1', scope='all', note=''):
    target='115-2' if season=='spring' else '116-1'
    records.append(dict(schoolId=id,semester=season,targetYear=target,sourceYear=year,applicationStart=start,applicationEnd=end,resultDate=result,status='official' if year==target else 'historical',confidence='high' if year==target else 'medium',sourceTitle=title,sourceUrl=url,lastChecked='2026-09-20',sourceType='official-primary',round=round,scope=scope,note=note))
pu='https://oia.pu.edu.tw/var/file/48/1048/img/1126/516627917.pdf'
add('1008','spring','115-2','2026-08-01','2026-10-15','2026-11-30',pu,'115學年度外國學生申請入學簡章 p.1、3','1')
add('1008','spring','115-2',None,'2026-11-15','2026-12-24',pu,'115學年度外國學生申請入學簡章 p.1、3','2',note='簡章列全期開始 8/1；第二梯單獨開始日期未列。')
add('1008','fall','115-1','2026-01-12','2026-04-30','2026-06-04',pu,'115學年度外國學生申請入學簡章 p.1、3','1')
add('1008','fall','115-1',None,'2026-06-15','2026-07-30',pu,'115學年度外國學生申請入學簡章 p.1、3','2')
add('0050','fall','115-1','2025-11-18','2026-01-06','2026-02-06','https://oia.nutc.edu.tw/var/file/42/1042/img/506068650.pdf','115學年度外國學生申請入學第一階段簡章')
add('1047','fall','115-1','2026-01-02','2026-07-03','2026-08-07','https://oaic.ctust.edu.tw/p/405-1015-63629,c4900.php?Lang=en','2026 Fall Semester Application Schedule',note='8/14 入學許可寄發，與 8/7 放榜不同。')
cmu='https://cmucia.cmu.edu.tw/admission_international.html'
add('1035','fall','115-1','2025-11-24','2026-01-23',None,cmu,'115學年度外國學生申請入學','1')
add('1035','fall','115-1','2026-02-16','2026-04-30',None,cmu,'115學年度外國學生申請入學','2')
add('1035','spring','115-2','2026-06-22','2026-08-21',None,cmu,'115學年度春季外國學生申請入學','1','graduate')
add('1035','spring','115-2','2026-09-14','2026-11-06',None,cmu,'115學年度春季外國學生申請入學','2','graduate')
add('1069','fall','114-1',None,None,'2025-06-20','https://ic.hust.edu.tw/shareFile/file/69/90/6799s7y7x.pdf','114學年度外國学生招生簡章','1')
add('1069','fall','114-1',None,'2025-07-26','2025-08-15','https://ic.hust.edu.tw/shareFile/file/69/90/6799s7y7x.pdf','114學年度外國学生招生簡章','2')
add('1069','spring','114-2',None,'2025-11-21','2025-12-22','https://ic.hust.edu.tw/?custom=4171&isEn=0&item=12&type=detail','114學年度春季外國學生招生公告',note='2026/1/6 為入學許可寄發，非放榜。')
add('0039','fall','115-1','2026-02-01','2026-04-30',None,'https://insch.ntcu.edu.tw/en/news_detail.php?sn=10','2026 Fall International Student Admission')
cyut='https://icsc.cyut.edu.tw/p/406-1008-58738,r1198.php?Lang=zh-tw'
add('1018','fall','115-1',None,'2026-07-25',None,cyut,'115學年度外國學生招生簡章','學士／碩士')
add('1018','fall','115-1',None,'2026-06-06',None,cyut,'115學年度外國學生招生簡章','博士','graduate')
add('1018','spring','115-2',None,'2026-12-19',None,cyut,'115學年度外國學生招生簡章','學士／碩士')
add('1018','spring','115-2',None,'2026-11-13',None,cyut,'115學年度外國學生招生簡章','博士','graduate')
add('0043','fall','115-1','2026-03-23','2026-05-10','2026-07-20','https://admission.ncut.edu.tw/parts/proofReaderNews.ashx?ii=_281969417709349.pdf','115學年度秋季外國學生招生簡章','1',note='公開榜單 7/20；5/27 入學通知另列，不混作放榜。')
add('0043','fall','115-1','2026-05-11','2026-06-28','2026-07-20','https://admission.ncut.edu.tw/parts/proofReaderNews.ashx?ii=_281969417709349.pdf','115學年度秋季外國學生招生簡章','2')
add('0049','spring','115-2','2026-09-01','2026-11-30',None,'https://admission.ntus.edu.tw/index.php?article_id=46767&code=list&flag=detail&ids=1177','115學年度外國學生簡章公告')
records[-1].update(resultDateText='2026/12/30 前',resultDateTextMy='2026/12/30 မတိုင်မီ',resultSort='2026-12-30',resultPrecision='by')
tku='https://adms.tku.edu.tw/FrontPointOfEntry.aspx?Sn=203'
add('1005','fall','115-1','2026-02-24','2026-03-23','2026-04-23',tku,'115學年度外國學生秋季班申請入學','1')
add('1005','fall','115-1','2026-04-16','2026-05-06','2026-05-29',tku,'115學年度外國學生秋季班申請入學','2',note='第二梯以名額餘額為準；本屆碩士額滿。')
add('1005','fall','115-1','2026-05-14','2026-06-04','2026-06-25',tku,'115學年度外國學生秋季班申請入學','3','graduate',note='本屆第三梯不開放學士與碩士。')
add('1005','spring','115-2','2026-08-04','2026-09-08',None,'https://adms.tku.edu.tw/FrontPointOfEntry.aspx?Sn=205','115學年度外國學生春季班申請入學','1','graduate',note='本屆學士未開放、碩士額滿，只餘博士名額。')
records[-1].update(resultDateText='2026 年 10 月下旬',resultDateTextMy='2026 အောက်တိုဘာ လနှောင်းပိုင်း',resultSort='2026-10-21',resultPrecision='interval')
asia='https://admission.asia.edu.tw/AsiaGlobalAdmissions/ForeignStudent'
add('1048','spring','115-2','2026-02-21','2026-11-30',None,asia,'2027 Spring Degree Program Application','全期',note='分梯放榜另列；全期截止不能套用較早放榜梯次。')
add('1048','fall','115-1','2026-02-21','2026-06-30',None,asia,'2026 Fall Degree Program Application','全期')
for season,year,round,date in [('spring','115-2','2','2026-05-30'),('spring','115-2','3','2026-06-30'),('fall','115-1','2','2026-05-30'),('fall','115-1','3','2026-06-30'),('fall','115-1','4','2026-07-31')]:
    add('1048',season,year,None,None,date,asia,'International Student Admission List','榜單 '+round)
mcut='https://foreignadm.mcut.edu.tw/APPLICATIONINSTRUCTIONSFORINTERNATIONALSTUDENTS.pdf'
add('1041','fall','115-1','2026-01-01','2026-04-30','2026-06-15',mcut,'115學年度外國學生暨外國學生專班招生簡章')
add('1041','spring','115-2','2026-08-01','2026-10-15','2026-11-16',mcut,'115學年度外國學生暨外國學生專班招生簡章','1','graduate')
cycu='https://oia.cycu.edu.tw/?p=11699&lang=en'
add('1004','fall','116-1','2026-12-01','2027-03-01','2027-04-23',cycu,'116學年度外國學生申請入學招生簡章','1')
add('1004','fall','116-1','2027-03-15',None,'2027-06-21',cycu,'116學年度外國學生申請入學招生簡章','2',note='官方資料存在差異，待確認：封面英文截止 May 1；中文封面、重要日程及內文 May 31。保留兩種說法，截止不參與排序。')
records[-1].update(conflicts={'applicationEnd':['2027-05-01','2027-05-31']})
ncku='https://oia.ncku.edu.tw/var/file/32/1032/img/5041/NCKUAdmissionProspectusforInternationalStudentsFall2026Spring2027v5-3.pdf'
add('0005','fall','115-1','2025-12-20','2026-03-15','2026-06-02',ncku,'115學年度外國學生招生簡章')
add('0005','spring','115-2','2026-07-01','2026-09-15','2026-11-30',ncku,'115學年度外國學生招生簡章',scope='graduate')
au='https://admissions.au.edu.tw/p/406-1023-115912,r113402.php?Lang=zh-tw'
for i,a,b,c in [('1','2026-03-02','2026-04-24','2026-05-11'),('2','2026-05-18','2026-06-22','2026-07-06'),('3','2026-07-07','2026-08-03','2026-08-18')]:
    add('1021','fall','115-1',a,b,c,au,'2026外國學生秋季班招生公告',i)
add('1073','fall','115-1',None,'2026-04-18',None,'https://b001.hwu.edu.tw/Post?PId=102727','115學年度外國學生申請入學簡章','1')
add('1073','fall','115-1',None,'2026-07-31',None,'https://b001.hwu.edu.tw/Post?PId=102727','115學年度外國學生申請入學簡章','2')
add('1013','fall','115-1','2026-02-01','2026-07-20',None,"https://ica.hfu.edu.tw/File/Userfiles/0000000006/files/FINAL-20260126-%E7%A7%8B%E5%AD%A3%E7%8F%AD-2026%E5%B9%B4%20(115%E5%AD%B8%E5%B9%B4%E5%BA%A6)%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E6%8B%9B%E7%94%9F%E7%B0%A1%E7%AB%A0-%E5%B0%81%E9%9D%A2.pdf",'2026 外國學生招生簡章 秋季班')
add('1013','spring','115-2','2026-10-01','2026-12-15',None,"https://ica.hfu.edu.tw/File/Userfiles/0000000006/files/FINAL-20260126-%E6%98%A5%E5%AD%A3%E7%8F%AD-2027%E5%B9%B4%20(115%E5%AD%B8%E5%B9%B4%E5%BA%A6)%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E6%8B%9B%E7%94%9F%E7%B0%A1%E7%AB%A0-%E5%B0%81%E9%9D%A2.pdf",'2027 外國學生招生簡章 春季班')
ntunhs='https://international-rnd.ntunhs.edu.tw/p/412-1037-3799.php?Lang=en'
add('0046','fall','115-1','2026-01-01','2026-03-31','2026-04-17',ntunhs,'2026 Academic Program Application Schedule','1')
add('0046','fall','115-1','2026-04-20','2026-05-29',None,ntunhs,'2026 Academic Program Application Schedule','2',note='時程頁原列 6/12；首頁榜單新聞為 6/11，待核對公告正文後確認。')
records[-1].update(conflicts={'resultDate':['2026-06-11','2026-06-12']})
for scope,date in [('undergraduate','2026-04-23'),('graduate','2026-04-30')]:
    add('1196','fall','115-1','2026-01-15','2026-03-25',date,'https://oia.dila.edu.tw/?p=1298','115學年度外國學生招生簡章',scope,scope)
fju='https://idsaoiedocs.fju.edu.tw/Fall2026/FJCU_115-1Admission.pdf'
add('1002','fall','115-1','2026-02-09','2026-03-05','2026-04-15',fju,'115學年度秋季班外國學生招生簡章','1')
add('1002','fall','115-1','2026-05-01','2026-05-31','2026-07-09',fju,'115學年度秋季班外國學生招生簡章','2')
add('1002','spring','115-2','2026-09-14','2026-10-14',None,'https://idsaoie.fju.edu.tw/','115學年度春季班招生現已開放申請（2026/9/17公告）')
add('1065','fall','115-1',None,'2026-06-30','2026-08-03','https://cia.wfu.edu.tw/wp-content/uploads/2026/06/115學年度外國學生申請入學招生簡章0325.pdf','115學年度外國學生申請入學招生簡章',note='公告簡章 3/17 並不等於開始申請；起始日僅寫即日起，保留未知。')
from continuation import append
append(add, records)
if __name__=='__main__':
    Path(__file__).with_name('records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
