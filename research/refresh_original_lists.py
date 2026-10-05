"""Bounded 114-year booklet fee audit and official original admission-list links.
Run from project root. No PDF admission-list content is parsed.
"""
import json
from pathlib import Path

path = Path('dist/school-insights.json')
all_data = json.loads(path.read_text())
base = all_data['schools']
schools = {s['id']:s for s in json.loads(Path('dist/schools.json').read_text())['schools']}
ids = ['0006','0039','0043','0049','0050','1001','1007','1008','1018','1029','1034','1035','1045','1047','1048','1062','1069']
for sid in ids:
    base.setdefault(sid, {'schoolId':sid,'nameZh':schools[sid]['name']})

# academic year, season, title, original official URL. Announcement pages are valid when attachments are not stable.
L = {
'0006':[
 ('115','fall','秋季外國學位生錄取榜單','https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2026_Fall_Semester_NCHU.pdf'),
 ('114','fall','秋季外國學位生錄取榜單','https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2025_Fall_Semester_NCHU.pdf'),
 ('114','spring','春季外國學位生錄取榜單','https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2026_Spring_Semester_NCHU.pdf')],
'0039':[
 ('114','fall','秋季外國學生錄取公告','https://insch.ntcu.edu.tw/news_detail.php?sn=4'),
 ('114','spring','春季外國學生錄取公告','https://insch.ntcu.edu.tw/en/news_detail.php?sn=9')],
'0049':[
 ('114','fall','秋季外國學生申請入學錄取公告','https://ntusoaa.ntus.edu.tw/index.php?article_id=41736&code=list&flag=detail&ids=962'),
 ('114','spring','春季外國學生申請入學錄取公告','https://admission.ntus.edu.tw/index.php?article_id=43808&code=list&flag=detail&ids=1177')],
'0050':[
 ('115','fall','秋季外國學生第二階段錄取公告','https://oia.nutc.edu.tw/p/404-1042-134790.php')],
'1001':[
 ('114','fall','秋季班外國學生申請入學錄取名單','https://exam2.thu.edu.tw/EXAM/doc/1036711410_public_001.pdf'),
 ('114','spring','春季班外國學生錄取公告索引','https://exam2.thu.edu.tw/EXAM/board_all.jsp?DOC=26')],
'1007':[
 ('115','fall','秋季外國學生各梯次錄取公告索引（頁面可能更新）','https://www.fcu.edu.tw/recurit_list/international-fall-semester/'),
 ('113','spring','春季外國學生第二梯次錄取公告','https://s3.ap-southeast-1.amazonaws.com/web-content.fcu.edu.tw/wp-content/uploads/2024/12/17103119/113-2-%E8%8B%B1%E5%85%AC%E5%91%8A%E7%AC%AC%E4%BA%8C%E6%A2%AF%E6%AC%A1.pdf')],
'1008':[
 ('115','fall','秋季外國學生第一梯次錄取榜單','https://oia.pu.edu.tw/var/file/48/1048/img/257/728221571.pdf'),
 ('115','fall','秋季外國學生第二梯次錄取榜單','https://oia.pu.edu.tw/var/file/48/1048/img/257/519749998.pdf'),
 ('114','fall','秋季外國學生第一梯次錄取榜單','https://oia.pu.edu.tw/var/file/48/1048/img/174/317234510.pdf'),
 ('114','fall','秋季外國學生第二梯次錄取公告','https://oia.pu.edu.tw/p/406-1048-64344%2Cr13.php?Lang=en'),
 ('114','spring','春季外國學生第一梯次錄取榜單','https://oia.pu.edu.tw/var/file/48/1048/img/720225637.pdf')],
'1018':[
 ('115','fall','秋季外國學生錄取公告（各梯次）','https://icsc.cyut.edu.tw/p/404-1008-39949.php?Lang=en'),
 ('113','spring','春季外國學生第一梯次錄取公告','https://icsc.cyut.edu.tw/p/404-1008-51343.php?Lang=en'),
 ('113','spring','春季外國學生第二梯次錄取公告','https://icsc.cyut.edu.tw/p/404-1008-52396.php?Lang=en')],
'1034':[
 ('114','fall','秋季外國學生第二梯次錄取公告','https://ifp.hk.edu.tw/%E5%BC%98%E5%85%89%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%B8114%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%A7%8B%E5%AD%A3%E7%8F%AD%EF%BC%88%E7%AC%AC%E4%BA%8C%E6%A2%AF%E6%AC%A1%EF%BC%89%E5%A4%96%E5%9C%8B%E5%AD%B8/'),
 ('114','fall','秋季外國學生第三梯次錄取公告','https://www.hk.edu.tw/remote/HKifp77141/')],
'1035':[
 ('114','fall','秋季外國學生第一梯次錄取榜單','https://cmucia.cmu.edu.tw/english/doc/cmulist_2025Fall_1st.pdf'),
 ('114','fall','秋季外國學生第二梯次錄取榜單','https://cmucia.cmu.edu.tw/english/doc/cmulist_2025Fall_2nd.pdf')],
'1045':[
 ('114','spring','春季外國學生錄取公告','https://www.ltu.edu.tw/p/406-1000-17077%2Cr11.php?Lang=zh-tw')],
'1048':[
 ('114','fall','秋季外國學生錄取榜單','https://ci.asia.edu.tw/uploads/asset/data/691e6f9d063ca28fd7942d46/114-1%E7%A7%8B%E5%AD%A3%E7%8F%AD_%E9%8C%84%E5%8F%96%E6%A6%9C%E5%96%AE_Asia_University_International_Admission_List_for_Fall_Semester_2025.pdf'),
 ('114','spring','春季外籍學生申請入學錄取公告','https://ci.asia.edu.tw/zh_tw/news/hotnews/%E4%BA%9E%E6%B4%B2%E5%A4%A7%E5%AD%B8114%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%BA%8C%E5%AD%B8%E6%9C%9F%E5%A4%96%E7%B1%8D%E5%AD%B8%E7%94%9F%E7%94%B3%E8%AB%8B%E5%85%A5%E5%AD%B8%E9%8C%84%E5%8F%96%E5%90%8D%E5%96%AE-65638122')],
'1062':[
 ('114','fall','秋季外國學生錄取公告','https://admission.ocu.edu.tw/p/404-1023-69454.php?Lang=zh-tw'),
 ('114','spring','春季外國學生錄取公告','https://admission.ocu.edu.tw/p/405-1023-71761%2Cc5671.php'),
 ('113','spring','春季外國學生錄取公告','https://admission.ocu.edu.tw/p/404-1023-66548.php?Lang=zh-tw')],
'1069':[
 ('114','fall','秋季外國學生第二梯次錄取公告','https://ic.hust.edu.tw/?custom=22899&isEn=0&item=9&type=detail'),
 ('114','spring','春季外國學生錄取公告','https://ic.hust.edu.tw/?custom=24010&isEn=0&item=9&type=detail')]
}
F = {
'0006':('brochure_unreadable',None,'114學年度國際學位生招生簡章','https://idpiilst.nchu.edu.tw/uploads/1745562603797-Application_Guidelines_for_International_Students_of_114_Academic_Year_2025_2026_new2.pdf','官方附件無法讀取'),
'0039':('brochure_unreadable',None,'114學年度春季外國學生招生簡章公告','https://insch.ntcu.edu.tw/news_detail.php?sn=6','附件無法讀取'),
'0043':('brochure_unreadable',None,'114學年度外國學生招生簡章','https://admission.ncut.edu.tw/parts/proofReaderNews.ashx?ii=_225383338393322.pdf','附件無法讀取'),
'0049':('brochure_unreadable',None,'114學年度外國學生招生簡章公告','https://www2.ntus.edu.tw/cht/index.php?article_id=39172&code=list&flag=detail&ids=80','官方公告附件無法讀取'),
'0050':('brochure_no_amount',None,'114學年度外國學生第二階段招生簡章','https://oia.nutc.edu.tw/var/file/42/1042/attach/14/pta_88472_5929430_86315.pdf','第二階段簡章未找到明確申請費；第一階段附件未能讀取'),
'1001':('confirmed',0,'114學年度外國學生招生簡章','https://exam2.thu.edu.tw/EXAM/download_doc_25/114_regulations.pdf?s=20250428041657','簡章明載 Application Fee: Free'),
'1007':('brochure_not_found',None,'',None,'未找到可核對的114學年度外國學生招生簡章'),
'1008':('brochure_no_amount',None,'114學年度外國學生招生簡章','https://oia.pu.edu.tw/var/file/48/1048/img/174/841109358.pdf','簡章未列明申請費'),
'1018':('brochure_unreadable',None,'114學年度外國學生招生簡章公告','https://icsc.cyut.edu.tw/p/406-1008-58742%2Cr1198.php?Lang=zh-tw','簡章附件無法讀取'),
'1029':('brochure_not_found',None,'',None,'未找到可核對的114學年度外國學生招生簡章'),
'1034':('brochure_no_amount',None,'114學年度秋季外國學生招生簡章（修訂版）','https://ifp.hk.edu.tw/wp-content/uploads/2025/03/2025_%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E6%8B%9B%E7%94%9F%E7%B0%A1%E7%AB%A0_%E7%A7%8B%E5%AD%A3%E7%8F%AD_%E4%B8%AD%E6%96%87%E7%89%88%E4%BF%AE%E8%A8%82%E7%89%88.pdf','秋季簡章未列明申請費'),
'1035':('confirmed',0,'114學年度外國學生招生簡章','https://cmucia.cmu.edu.tw/doc/Application_Guidelines114.pdf','簡章明載免報名費 / No Application Fee'),
'1045':('brochure_unreadable',None,'2025秋季外國學生招生簡章公告索引','https://ltu1473.video.ltu.edu.tw/p/page1','簡章附件尚未取得，不能核定金額'),
'1047':('brochure_unreadable',None,'114學年度外國學生招生簡章公告','https://oaic.ctust.edu.tw/p/16-1015-64167.php?Lang=en','官方公告附件無法讀取'),
'1048':('brochure_unreadable',None,'114學年度秋季外國學生招生簡章','https://ci.asia.edu.tw/uploads/asset/data/67d404a3063ca254c249d52e/Fall_Semester_2025_Admission_Application_Brochure_for_International_Students.pdf','簡章附件無法讀取'),
'1062':('brochure_unreadable',None,'114學年度秋季外國學生招生簡章公告','https://admission.ocu.edu.tw/p/404-1023-67431.php?Lang=zh-tw','官方公告附件無法讀取'),
'1069':('brochure_no_amount',None,'114學年度外國學生招生簡章','https://ic.hust.edu.tw/shareFile/file/69/90/6799s7y7x.pdf','簡章未列明申請費')
}
for sid in ids:
    row = base[sid]
    row['lastChecked'] = '2026-09-26'
    row['admissionNotices'] = [dict(academicYear=y,semester=sem,sourceTitle=title,sourceUrl=url,scope='foreign_degree') for y,sem,title,url in L.get(sid,[])]
    status,amount,title,url,note = F[sid]
    row['applicationFee'] = dict(amount=amount,currency='TWD' if amount is not None else None,academicYear='114',status=status,sourceTitle=title or None,sourceUrl=url,notes=note)
    # Former extraction was intentionally retired. No counts or identifying data shipped.
    row.pop('gaps',None)
    row.pop('gapsMy',None)
all_data['schemaVersion'] = 2
all_data['updated'] = '2026-09-26'
all_data['countingPolicy'] = '榜單只連結官方原始來源，不解析內容、統計人數或推估錄取率。'
path.write_text(json.dumps(all_data,ensure_ascii=False,indent=2)+'\n')
