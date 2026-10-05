"""Additional dates checked directly against official pages on 2026-09-20."""
def append(add, records):
    add('1029','fall','115-1','2026-01-10','2026-03-31','2026-06-12','https://recruit.csmu.edu.tw/var/file/19/1019/attach/60/pta_36360_8141526_13481.pdf','115學年度中山醫學大學外國學生招生簡章 p.1')
    add('1022','fall','115-1','2026-02-01',None,None,'https://ao.ttu.edu.tw/var/file/73/1073/img/325/186014133.pdf','115學年度大同大學外國學生招生簡章 p.3、9',note='截止日期 p.3 與中文 p.9 為 5/6，英文 p.9 為 5/7，待確認。6/12 為通知寄發，不當作公開放榜。')
    records[-1]['conflicts']={'applicationEnd':['2026-05-06','2026-05-07']}
    records[-1]['admissionLetterDate']='2026-06-12'
    add('0039','spring','115-2','2026-08-01','2026-10-31','2026-12-17','https://oia.ntcu.edu.tw/storage/media/W4NT9CD1uUPo9eA6KMtDqVYo5skoJ5OoHJhO2mNI.pdf','2026/2027 臺中教育大學外國學位生招生簡章 p.2')
    add('1014','fall','115-1','2026-02-01','2026-07-05',None,'https://enroll.isu.edu.tw/di/','義守大學外國學生線上申請系統 Fall Application Schedule')
    add('1014','spring','115-2','2026-09-01','2026-12-15',None,'https://enroll.isu.edu.tw/di/','義守大學外國學生線上申請系統 Spring Application Schedule')
    add('1003','spring','115-2','2026-09-14','2026-10-31','2026-12-07','https://web-en.scu.edu.tw/entrance/web_page/460','東吳大學 2027 Spring International Admission')
    add('1049','fall','115-1','2026-05-25','2026-07-03','2026-08-07','https://knuoica.knu.edu.tw/p/404-1004-56689.php?Lang=zh-tw','開南大學115學年度外國學生招生簡章（2026秋季）')
    add('1019','spring','115-2','2026-07-13','2026-10-12',None,'https://admission.kmu.edu.tw/','高雄醫學大學 Spring Intake 2027','1','graduate')
    add('1024','fall','115-1','2026-01-26','2026-05-31','2026-06-26','https://my.ksu.edu.tw/file/bbcode/w3Pages/41421/4365ff49-d19f-4bcc-abb3-423f02649d9c/2026%20Fall%20Semester%20Application%20Prospectus%20for%20General%20International%20Students.pdf','崑山科技大學115學年度國際學生秋季班申請入學簡章',note='7/1 開始寄發入學許可，與 6/26 放榜分列。')

    add('0032','fall','115-1','2026-02-10','2026-05-05',None,'https://enroll.nuu.edu.tw/p/405-1065-76354,c735.php','聯合大學2026外國學生招生公告')
    add('1033','fall','115-1','2025-12-16','2026-05-29','2026-07-02','https://dweb.cjcu.edu.tw/ShepherdFiles/B2902/Article/20251125094544398.pdf','長榮大學115學年度秋季外國學生招生簡章','第一次榜單')
    add('1033','fall','115-1',None,None,'2026-07-23','https://dweb.cjcu.edu.tw/ShepherdFiles/B2902/Article/20251125094544398.pdf','長榮大學115學年度秋季外國學生招生簡章','第二次榜單（如有需要）')
    nuk='https://interadmission.nuk.edu.tw/p/412-1063-4996.php?Lang=zh-tw'
    add('0019','fall','116-1','2027-02-25','2027-04-23','2027-06-15',nuk,'國立高雄大學2027外國學生申請時程',note='官方已刊時程；秋季簡章另定2027/1/22公布。')
    add('0019','spring','115-2','2026-10-08','2026-11-02','2026-12-17',nuk,'國立高雄大學2027外國學生申請時程',note='時程頁明列2027春季；Apply Now頁同列115-2/2027.2與英文Spring，但中文誤寫秋季，季別文字差異待校方更正。')
    records[-1]['sourceUrls']=[nuk,'https://interadmission.nuk.edu.tw/p/406-1063-81458,r1780.php?Lang=zh-tw']
    records[-1]['semesterConflictNote']='Apply Now 中文秋季與115-2、2027.2、英文Spring及時程頁有差異。'
    ncyu='https://www.ncyu.edu.tw/oia_eng/ServerFile/Get/786060ff-e628-4e3e-9dc1-35afcc76b7c6?nodeId=60284&sId=237992'
    add('0018','fall','115-1','2026-01-01','2026-03-01',None,ncyu,'嘉義大學115學年度外國學生招生簡章','1',note='簡章預定5/18放榜，國際處公告列表顯示5/20；實際公告日期待核。')
    records[-1]['conflicts']={'resultDate':['2026-05-18','2026-05-20']}
    records[-1]['sourceUrls']=[ncyu,'https://www.ncyu.edu.tw/oia_eng/Subject?IsAll=True&ListType=1&NodeId=27&SiteBlockId=4940&SiteId=253&nodeName=All']
    add('0018','fall','115-1','2026-04-18','2026-05-17','2026-07-10',ncyu,'嘉義大學115學年度外國學生招生簡章','2')
    stust='https://portal.stust.edu.tw/intstudweb/images/2026_2027%20Academic%20Year%20Application%20Guide%20for%20International%20Students_115%20%E5%AD%B8%E5%B9%B4%E5%BA%A6%E5%8D%97%E8%87%BA%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%B8%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E7%94%B3%E8%AB%8B%E5%85%A5%E5%AD%B8%E7%B0%A1%E7%AB%A0114.11.13.pdf'
    for season,year,start,end,bound,round in [('fall','115-1','2026-01-01','2026-03-10','2026-04-10','1'),('fall','115-1','2026-03-11','2026-05-15','2026-06-15','2'),('spring','115-2','2026-07-05','2026-09-15','2026-10-15','1'),('spring','115-2','2026-09-15','2026-11-30','2026-12-25','2')]:
        add('1023',season,year,start,end,None,stust,'南臺科技大學115學年度外國學生招生簡章',round)
        records[-1].update(resultDateText=bound+' 前',resultDateTextMy=bound+' မတိုင်မီ',resultSort=bound if season=='spring' else '2027'+bound[4:],resultPrecision='by',resultDateUpperBound=bound)

    yzu='https://gao.yzu.edu.tw/index.php/en/admissions-2/int-student'
    add('1010','fall','115-1','2025-12-15','2026-06-01',None,yzu,'元智大學 Fall Intake 2026',note='3–4月與6月所列為審查區間，不當作放榜。')
    add('1010','spring','115-2','2026-09-01','2026-10-15','2026-11-20',yzu,'元智大學 Spring Intake 2027',note='來源入學許可年份誤列2024，該欄保留待確認，不自行更改。')
    add('1016','fall','115-1','2026-02-01','2026-05-31',None,'https://iee.mcu.edu.tw/en/16186/','銘傳大學2026秋季國際學位生招生公告')
    add('1006','fall','115-1',None,'2026-06-30','2026-07-23','https://ap2.pccu.edu.tw/enroll/exampublic/50/','中國文化大學2026秋季外國學生第二梯次','2',note='同頁開始日分別寫5/4與5/11，待確認；中文段落季別誤寫春季，標題與英文均為秋季九月入學。')
    records[-1]['conflicts']={'applicationStart':['2026-05-04','2026-05-11']}
    fgu='https://oica.fgu.edu.tw/zh_tw/admission/04'
    add('1050','fall','115-1','2026-02-11','2026-03-20','2026-04-30',fgu,'佛光大學2026秋季外國學生招生公告（3/26更新）','1')
    add('1050','fall','115-1','2026-04-20','2026-06-19','2026-07-23',fgu,'佛光大學2026秋季外國學生招生公告（3/26更新）','2')
    tcu='https://oga.tcu.edu.tw/wp-content/uploads/2026/04/115%E9%87%8D%E8%A6%81%E6%97%A5%E7%A8%8B%E4%B8%AD%E6%96%87.pdf'
    for start,end,result,round in [('2025-11-20','2025-12-31','2026-02-16','1'),('2026-01-05','2026-02-18','2026-03-30','2'),('2026-02-23','2026-04-08','2026-06-01','3'),('2026-04-09','2026-05-11','2026-07-08','4')]:
        add('1027','fall','115-1',start,end,result,tcu,'慈濟大學115學年度外國學生招生重要日程',round,note='醫學、學士後中醫、藥學僅第一梯，另於5/1放榜。')
    add('1027','fall','115-1','2025-11-20','2025-12-31','2026-05-01',tcu,'慈濟大學115學年度外國學生招生重要日程','醫學／學士後中醫／藥學',scope='selected-programs')
    add('1027','spring','115-2','2026-08-10','2026-11-06','2026-12-18',tcu,'慈濟大學115學年度外國學生招生重要日程')
    nhu='https://nhuwebfile.nhu.edu.tw/UploadedFiles/2026/2/2250d02d-81ad-46d8-8bf0-4bea6289d29d.pdf'
    for i,(end,bound) in enumerate([('2026-02-28','2026-03-20'),('2026-04-30','2026-05-20'),('2026-05-31','2026-06-20'),('2026-06-30','2026-07-20'),('2026-07-31','2026-08-20')],1):
        add('1020','fall','115-1',None,end,None,nhu,'南華大學2026–2027外國學生招生簡章',str(i))
        records[-1].update(resultDateText=bound+' 前',resultDateTextMy=bound+' မတိုင်မီ',resultSort='2027'+bound[4:],resultPrecision='by',resultDateUpperBound=bound)
    for i,(end,bound) in enumerate([('2026-10-31','2026-11-20'),('2026-12-15','2027-01-20')],1):
        add('1020','spring','115-2',None,end,None,nhu,'南華大學2026–2027外國學生招生簡章',str(i))
        records[-1].update(resultDateText=bound+' 前',resultDateTextMy=bound+' မတိုင်မီ',resultSort=bound,resultPrecision='by',resultDateUpperBound=bound)

    tajen='https://a29.tajen.edu.tw/p/412-1029-6275.php?Lang=en'
    add('1043','fall','115-1','2026-05-06','2026-08-01','2026-08-15',tajen,'大仁科技大學2026–2027外國學生招生時程')
    add('1043','spring','115-2','2026-11-17','2027-01-16','2027-01-30',tajen,'大仁科技大學2026–2027外國學生招生時程')
    add('1031','fall','115-1','2026-03-01',None,None,'https://intlstudent.fy.edu.tw/p/406-1075-75327,r200.php?Lang=zh-tw','輔英科技大學115學年度外國學生招生簡章更新版公告',note='已確認新版開放報名日；新版附件尚待核讀，不直接沿用舊版截止／放榜。')
    ntsu='https://aca.ntsu.edu.tw/p/404-1004-63564.php?Lang=zh-tw'
    add('0044','fall','115-1',None,'2026-06-18',None,ntsu,'國立體育大學115學年度外國學生招生公告')
    add('0044','spring','115-2',None,'2026-12-24',None,ntsu,'國立體育大學115學年度外國學生招生公告')
    nkuht='https://international.nkuht.edu.tw/p/404-1045-34386.php?Lang=en'
    add('0047','fall','115-1','2025-10-30','2025-12-15','2026-03-20',nkuht,'高雄餐旅大學115學年度外國學生招生時程','1')
    add('0047','fall','115-1','2026-01-20','2026-03-23','2026-05-29',nkuht,'高雄餐旅大學115學年度外國學生招生時程','2')
    nutn='https://campus.nutn.edu.tw/newsPost3/postFiles/101347_Admissions%20Guide%20for%20International%20Students%20for%20the%20115th%20Academic%20Year.pdf'
    add('0036','fall','115-1','2026-01-05','2026-04-09','2026-05-21',nutn,'臺南大學115學年度外國學生招生簡章 p.2')
    add('0036','spring','115-2','2026-09-01','2026-10-31','2026-12-21',nutn,'臺南大學115學年度外國學生招生簡章 p.2','1','graduate')
    cnu='https://www.cnu.edu.tw/d_files/56/docs/20260507085639.pdf'
    add('1025','fall','115-1',None,None,None,cnu,'嘉南藥理大學2026–2027外國學生招生簡章 p.12',note='紙本收件截止中文2026/7/24、英文2025/7/25，官方資料存在差異，待確認；放榜僅列8月中前。')
    records[-1].update(conflicts={'applicationEnd':['2026-07-24','2025-07-25']},resultDateText='2026年8月中前',resultDateTextMy='2026 ဩဂုတ် လလယ်မတိုင်မီ',resultSort='2027-08-15',resultPrecision='by-mid-month')
    add('1025','spring','115-2',None,'2027-01-08',None,cnu,'嘉南藥理大學2026–2027外國學生招生簡章 p.12')
    records[-1].update(resultDateText='2027年1月中前',resultDateTextMy='2027 ဇန်နဝါရီ လလယ်မတိုင်မီ',resultSort='2027-01-15',resultPrecision='by-mid-month')

    uch='https://ico.uch.edu.tw/var/file/7/1007/img/702142081.pdf'
    add('1036','fall','115-1','2026-01-30','2026-06-07','2026-07-16',uch,'健行科技大學115學年度一般外國學生招生簡章')
    add('1036','spring','115-2','2026-09-01','2026-11-29','2027-01-13',uch,'健行科技大學115學年度一般外國學生招生簡章')
    vnu='https://www.oia.vnu.edu.tw/DOC/oia/1071/fb9a30486edc43e3b94de9acdb779f85.pdf'
    add('1038','fall','115-1','2026-05-15','2026-06-30','2026-07-08',vnu,'萬能科技大學115學年度外國學生招生簡章')
    add('1038','spring','115-2','2026-11-02','2026-11-30','2026-12-09',vnu,'萬能科技大學115學年度外國學生招生簡章')
    add('1028','fall','115-1','2025-11-17','2026-02-12',None,'https://oge.tmu.edu.tw/zh-hant/外國學生大學部申請/','臺北醫學大學2026秋季大學部申請時程','1','undergraduate')
    records[-1].update(resultDateText='2026年4月',resultDateTextMy='2026 ဧပြီလ',resultSort='2027-04-01',resultPrecision='month')
    add('0037','fall','115-1','2026-02-02','2026-04-30','2026-05-27','https://enroll.ntue.edu.tw/foreign','國立臺北教育大學2026外國學生申請入學系統')
    nchu='https://oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/115_Academic_Year_Application_Guidelines_re.pdf'
    add('0006','fall','115-1','2026-01-15','2026-03-20','2026-05-31',nchu,'中興大學115學年度秋季暨春季國際學位生招生簡章 p.3',note='原定5/31，如逢假日順延，請核對當屆實際公告。')
    add('0006','spring','115-2','2026-08-15','2026-09-30','2026-11-30',nchu,'中興大學115學年度秋季暨春季國際學位生招生簡章 p.3',scope='graduate')

    ntnu='https://cantor.math.ntnu.edu.tw/index.php/en/admissions/international-students/'
    add('0004','fall','115-1','2025-11-03','2025-12-15','2026-03-02',ntnu,'臺師大國際學生招生 Calendar of Events','1',note='數學系官方轉載全校時程；個別系所延長期限請另查。')
    add('0004','fall','115-1','2026-01-12','2026-03-02','2026-05-04',ntnu,'臺師大國際學生招生 Calendar of Events','2')
    add('0004','spring','115-2','2026-08-03','2026-09-14','2026-11-20',ntnu,'臺師大國際學生招生 Calendar of Events')
    tut='https://oiss-rd.tut.edu.tw/p/406-1042-57193,r1487.php?Lang=zh-tw'
    add('1051','fall','115-1',None,'2026-03-31','2026-04-10',tut,'台南應用科技大學115學年度外國學生招生重要日程','1',note='開始僅寫即日起，不推定開始日。')
    records[-1]['admissionLetterDate']='2026-04-13'
    add('1051','fall','115-1','2026-04-14','2026-07-31','2026-08-07',tut,'台南應用科技大學115學年度外國學生招生重要日程','2')
    records[-1]['admissionLetterDate']='2026-08-10'
    ctu='https://cia.ctu.edu.tw/p/406-1005-48771,r1159.php?Lang=zh-tw'
    add('1040','fall','115-1',None,'2025-12-31','2026-01-25',ctu,'建國科技大學2026秋季–2027春季外國學生招生日程表','1')
    add('1040','fall','115-1',None,'2026-07-15','2026-08-05',ctu,'建國科技大學2026秋季–2027春季外國學生招生日程表','2')
    add('1040','spring','115-2',None,'2026-11-25','2026-12-15',ctu,'建國科技大學2026秋季–2027春季外國學生招生日程表')
    add('1075','fall','115-1','2025-12-01','2026-05-31','2026-06-30','https://d021.wzu.edu.tw/datas/upload/files/%E6%8B%9B%E7%94%9F%E7%B0%A1%E7%AB%A0/Wenzao_University_Master_program.pdf','文藻外語大學2026外國學生碩士班招生簡章',scope='graduate')
    add('0017','spring','115-2','2026-09-03','2026-10-31',None,'https://webap.ntpu.edu.tw/interstud/index.php','臺北大學2027春季外國學生線上申請',note='頁面結尾台灣時間括號前另列2027，與明列2026的報名日期有文字差異，保留此註記。')
    niu='https://isa.niu.edu.tw/var/file/73/1073/img/115-regulations-for-academic.pdf'
    add('0031','fall','115-1','2025-12-01',None,'2026-03-20',niu,'宜蘭大學115學年度外國學生招生簡章 p.4、9','1',note='截止日期重要日程及中文為2026/1/20，英文內文p.9為2025/1/20，年份差異待確認。')
    records[-1]['conflicts']={'applicationEnd':['2026-01-20','2025-01-20']}
    add('0031','fall','115-1','2026-03-14','2026-04-28','2026-06-12',niu,'宜蘭大學115學年度外國學生招生簡章 p.4','2')
    add('0031','spring','115-2','2026-09-14','2026-10-13','2026-12-08',niu,'宜蘭大學115學年度外國學生招生簡章 p.4','1','graduate')
    nttu='https://rd.nttu.edu.tw/var/file/7/1007/img/49/701322365.pdf'
    add('0030','fall','115-1','2026-03-01','2026-04-30','2026-06-12',nttu,'臺東大學115學年度外國學生招生簡章 p.1')
    add('0030','spring','115-2','2026-08-15','2026-09-30','2026-11-13',nttu,'臺東大學115學年度外國學生招生簡章 p.1')

    nsysu='https://rpb78.nsysu.edu.tw/static/file/239/1239/img/409586988.pdf'
    for season,year,start,end,bound in [('fall','115-1','2026-01-15','2026-03-15','2026-06-05'),('spring','115-2','2026-08-01','2026-09-30','2026-12-10')]:
        add('0009',season,year,start,end,None,nsysu,'中山大學115學年度外國學生招生簡章 p.3')
        records[-1].update(resultDateText=bound+' 前',resultDateTextMy=bound+' မတိုင်မီ',resultDateUpperBound=bound,resultSort=bound if season=='spring' else '2027'+bound[4:],resultPrecision='by')
    add('0053','fall','115-1','2026-03-04','2026-04-30','2026-06-26','https://oia.nkust.edu.tw/images/upload/files/2026%E7%A7%8B%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E6%8B%9B%E7%94%9F%E7%B0%A1%E7%AB%A0%202026%20Fall%20International%20Degree%20Student%20Prospectus.pdf','高雄科技大學2026秋季外國學生招生簡章 p.2')
    ntust='https://admission.ntust.edu.tw/p/412-1052-9572.php?Lang=en'
    add('0022','fall','115-1','2026-01-01','2026-03-11','2026-05-27',ntust,'臺灣科技大學2026秋季學士班外國學生申請日程','初步錄取','undergraduate',note='6/24 為最終錄取結果，5/27 不代表已取得正式入學許可。')
    add('0022','fall','115-1',None,None,'2026-06-24',ntust,'臺灣科技大學2026秋季學士班外國學生申請日程','最終錄取','undergraduate')
    ntustg='https://admission.ntust.edu.tw/p/412-1052-8763.php?Lang=en'
    add('0022','spring','115-2','2026-07-01','2026-09-11','2026-10-30',ntustg,'臺灣科技大學2027春季研究所外國學生申請日程','預錄取','graduate',note='11/30 最終錄取及獎學金結果；本期不招學士班。')
    add('0022','spring','115-2',None,None,'2026-11-30',ntustg,'臺灣科技大學2027春季研究所外國學生申請日程','最終錄取','graduate')
    chu='https://bm16.chu.edu.tw/p/412-1054-1184.php?Lang=zh-tw'
    add('1011','fall','114-1','2025-02-17','2025-04-14',None,chu,'中華大學114學年度秋季外國学生招生時程','1')
    add('1011','fall','114-1','2025-05-07','2025-07-11',None,chu,'中華大學114學年度秋季外國学生招生時程','2')

    add('1045','fall','115-1','2026-03-04','2026-06-30','2026-08-03','https://ltu1470.video.ltu.edu.tw/filedownload/1128','嶺東科技大學2026秋季外國學生招生簡章 p.2',note='已核對PDF表格：7/1–7/31為審查，不是第二梯申請；8/4為寄發入學通知。')
    records[-1]['admissionLetterDate']='2026-08-04'
    hcu='https://www.hcu.edu.tw/upload/userfiles/7C38F4ED57614E278365DBC8FA404F1A/files/2026%20%E7%A7%8B115%20%E5%A4%96%E7%B1%8D%E7%94%9F%E7%94%B3%E8%AB%8B%E5%85%A5%E5%AD%B8%E7%B0%A1%E7%AB%A0(%E4%BF%AE).pdf'
    add('1039','fall','115-1','2026-04-01','2026-07-20',None,hcu,'玄奘大學115秋季外國學生招生簡章 p.2',note='簡章p.2放榜7/29，招生頁常態時程為7/30，保留差異；p.1混留2025春季截止，不移入秋季。')
    records[-1].update(conflicts={'resultDate':['2026-07-29','2026-07-30']},sourceUrls=[hcu,'https://www.hcu.edu.tw/newstu/newstu/zh-tw/BC215007EF684DBA9C6D403D41F64B7F/CCA71ED259BA48E7A6643D039C5A5473'])
    for r in records:
        if r['schoolId']=='1011' and r['sourceYear']=='114-1':
            r['resultDate']='2025-05-02' if r['round']=='1' else '2025-07-30'
            r['sourceUrls']=[r['sourceUrl'],'https://bm16.chu.edu.tw/var/file/54/1054/img/463194920.pdf']

    add('1054','fall','115-1','2026-02-25','2026-07-31',None,'https://rdie.just.edu.tw/p/406-1029-70336,r11.php?Lang=zh-tw','景文科技大學115學年度外國學生秋季班招生簡章',scope='undergraduate',note='通知書寄發區間2/25–8/31，不假定為單一放榜日。')
    add('1057','fall','115-1','2026-05-15','2026-07-20','2026-08-05','https://www.takming.edu.tw/inetoffice/post/show.asp?key=118700','德明財經科技大學115學年度外國學生一般班招生公告')

    add('0048','fall','115-1','2026-03-01','2026-06-30','2026-07-23','https://lhc.nqu.edu.tw/p/404-1045-27952.php?Lang=zh-tw','金門大學115學年度外國學生招生公告',note='已找到116新公告線索但無法核读完整版本，暫以115官方原始日期參考；公告內另有僑生表單，不作外國學生報名入口。')
    add('1032','fall','115-1','2026-06-11','2026-07-14','2026-07-20','https://admin.must.edu.tw/files/%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E5%85%A5%E5%AD%B8%E6%8B%9B%E7%94%9F%E7%B0%A1%E7%AB%A0(115%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%A7%8B%E5%AD%A3%E7%8F%AD)_260701(%E6%9B%B4%E6%96%B0)_20260702094723.pdf','明新科技大學115秋季外國學生簡章（7/1更新）',note='新版明列6/11–7/14，優先於未註年度常態4–6月三梯時程。')

    csu='https://oia.csu.edu.tw/var/file/75/1075/img/26/368808995.pdf'
    add('1037','fall','115-1',None,'2026-06-15','2026-07-06',csu,'正修科技大學115秋季外國學生招生簡章','初榜',note='7/6 初榜，7/9 複查後榜單及入學許可；本簡章明列僅秋季招生。')
    add('1037','fall','115-1',None,None,'2026-07-09',csu,'正修科技大學115秋季外國學生招生簡章','複查後榜單')
    records[-1]['admissionLetterDate']='2026-07-09'
    dyu='https://bulletin.dyu.edu.tw/view.php?file=ZmlsZS9BMDI1MS8xNDkwMDIucGRm'
    add('1012','fall','114-1','2025-03-05','2025-07-28',None,dyu,'大葉大學114學年度外國學生招生簡章 p.1')
    add('1012','spring','114-2',None,'2025-12-29',None,dyu,'大葉大學114學年度外國學生招生簡章 p.1',note='簡章開始10/1，招生公告10/14，未核明版本修訂順序，保留差異。')
    records[-1].update(conflicts={'applicationStart':['2025-10-01','2025-10-14']},sourceUrls=[dyu,'https://bulletin.dyu.edu.tw/index.php?isHidden=1&msg_ID=78879&pool_ID=265'])

    add('1064','fall','115-1',None,'2026-06-30',None,'https://ieco.meiho.edu.tw/var/file/9/1009/img/1096/811416569.pdf','美和科技大學115學年度外國學生學士班簡章（7/17修正）',scope='undergraduate')
    records[-1].update(resultDateText='2026年7月31日前',resultDateTextMy='2026-07-31 မတိုင်မီ',resultDateUpperBound='2026-07-31',resultSort='2027-07-31',resultPrecision='by')

    add('0013','fall','114-1','2025-02-05','2025-03-15',None,'https://oia.ccu.edu.tw/p/406-1008-68327,r1721.php?Lang=en','中正大學2025秋季外國學生申請公告',note='保留已核讀的2025日期；2026簡章附件待完成核讀，不以常態流程頁替代年度簡章。')
    for r in records:
        if r['schoolId']=='0039' and r['semester']=='fall':
            r.update(resultDate='2026-06-18',admissionLetterDate='2026-06-26',sourceUrls=[r['sourceUrl'],'https://oia.ntcu.edu.tw/storage/media/W4NT9CD1uUPo9eA6KMtDqVYo5skoJ5OoHJhO2mNI.pdf'],note='115簡章p.2預定6/18放榜、6/26寄發通知；實際放榜以申請系統公告為準。取代原資料包6/17參考值，原值存於備份。')

    ccu='https://oia.ccu.edu.tw/var/file/8/1008/img/814/372680683.pdf'
    add('0013','fall','115-1','2026-01-15','2026-03-15','2026-04-30',ccu,'中正大學115學年度外國學生招生簡章 p.1',note='IBP-ME、ELMD、EESL、INTENSE另行公告，不套用本表。')
    add('0013','spring','115-2','2026-08-15','2026-09-30','2026-11-25',ccu,'中正大學115學年度外國學生招生簡章 p.1',scope='graduate',note='春季限碩博士；使用115年度表，不採舊常態頁10/15截止。')
    for r in records:
        if r['schoolId']=='0013' and r['sourceYear']=='114-1':r['note']='保留上一年度原始日期；首頁以115年度資料為準。'
