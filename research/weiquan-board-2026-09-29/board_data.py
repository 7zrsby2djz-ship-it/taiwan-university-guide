# -*- coding: utf-8 -*-
"""Editorial layer for the 偉銓 decision board (2026-09-29, Claude).

Everything here is either (a) copied from the already-audited dist/schools.json /
dist/school-insights.json, or (b) newly read from an official source listed in
`src` with the check date CHECKED. Nothing is inferred from a previous year and
promoted to an official date. Where an official document could not be read, the
school gets a `readYourself` link instead of a guessed value.

Tiers are Claude's editorial suggestion for this applicant only (first-time
bachelor applicant, TOCFL A2 now, lives near Taichung, sponsor pays tuition).
"""
CHECKED = '2026-09-29'

# Taichung Station reference point; straight-line km computed in build_board.py
COORDS = {'0008':(24.9680,121.1930),'0009':(22.6260,120.2660),'0013':(23.4970,120.4530),'1004':(24.9580,121.2420),'1006':(25.1370,121.5370),'1011':(24.7860,121.0140),'1046':(25.0160,121.5350),'1052':(22.9600,120.2900),'1055':(22.9330,120.2700),'1061':(25.0330,121.6100),'1125':(22.9570,120.2650),'0006':(24.1235,120.6750),'0017':(24.9430,121.3710),'0018':(23.4700,120.4870),'0021':(23.9510,120.9290),'0024':(22.6450,120.6060),'0025':(25.0425,121.5350),'0031':(24.7460,121.7480),'0032':(24.5450,120.8120),'0036':(22.9850,120.2050),'0039':(24.1440,120.6720),'0043':(24.1450,120.7310),'0047':(22.5760,120.3350),'0049':(24.1558,120.6852),'0050':(24.1500,120.6840),'0051':(25.0420,121.5260),'1001':(24.1800,120.6000),'1007':(24.1790,120.6470),'1008':(24.2270,120.5780),'1018':(24.0680,120.7150),'1029':(24.1220,120.6520),'1034':(24.2220,120.5770),'1035':(24.1570,120.6800),'1045':(24.1280,120.6108),'1047':(24.1780,120.7200),'1048':(24.0460,120.6860),'1062':(24.1810,120.6290),'1069':(24.0900,120.7240)}

# tier: A = 台中近又省錢（首選）, P = 知名學校（遠或貴也值得考慮）,
#       B = 台中備案（私立、資料待補）, C = 暫不優先
# fee.kind: free(明文免收) / paid / silent(簡章沒寫收費，未明文免收) / unknown(讀不到)
# aid.sure: 錄取或達語言門檻就有的優惠; aid.review: 要審查、可能拿不到
S = {
'0039': dict(tier='A', place='台中西區・市中心', travel='市區公車/機車 10–15 分',
  fee=dict(kind='paid', amount=1200, text='學士 NT$1,200（US$50）；只可報一個系', src='https://oia.ntcu.edu.tw/storage/media/W4NT9CD1uUPo9eA6KMtDqVYo5skoJ5OoHJhO2mNI.pdf', year='115'),
  tuition=dict(min=46030, max=53405, year='115', text='依學院：文 46,030／商 47,900／理 53,405（每學期）', src='https://oia.ntcu.edu.tw/storage/media/W4NT9CD1uUPo9eA6KMtDqVYo5skoJ5OoHJhO2mNI.pdf'),
  firstYear=dict(kind='full', net=0),
  aid=dict(sure='第一年兩學期免學雜費：錄取就有，不用另外審查（轉學生除外）。', review='第二年起每年申請分級獎學金：每月 6,000／4,000／2,000 元並搭配宿舍全免或半免。'),
  renew='第二年起：學士平均 80 分拿 6,000/月、75 分拿 4,000/月（有名額排序）、70 分拿 2,000/月；操行 80；每學期服務 64 小時；每年 1/31、8/31 前申請。',
  lang='多數系要 TOCFL B1。A2 可報：體育系、科學教育與應用學系、臺灣語文學系、美術學系。B1 後可報數學教育、資工、數位內容、國際企業（聽讀都 B1）、區域與社會發展等。',
  after='春季：12/17 放榜，12/24 寄發入學通知（郵寄，地址要寫對）。報到時要交驗證過的學歷，否則可能取消錄取。簡章沒有寫要付保證金。',
  letter={
    "spring": "2026-12-24"
  },
  verdict='台中市中心、公立、第一年學雜費全免而且錄取就有，是這份名單裡第一年最省錢的。A2 只能報 4 個系，要報就在 10/31 前。',
  verdictMy='ထိုင်ချုံးမြို့လယ်၊ အစိုးရကျောင်း။ ဝင်ခွင့်ရရင် ပထမနှစ် ကျောင်းလခ အခမဲ့ (အလိုအလျောက်)။ A2 ဖြင့် ဌာန ၄ ခုသာ လျှောက်နိုင်။ 10/31 မတိုင်ခင် လျှောက်ပါ။',
  checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "國際企業學系",
      "count": 13,
      "year": "114",
      "term": "fall",
      "src": "https://insch.ntcu.edu.tw/downloader.php?sn=4&config=news",
      "basis": "學士正取；第 35–47 號，原圖第 3–4 頁已核對"
    },
    {
      "dept": "國際企業學系",
      "count": 3,
      "year": "114",
      "term": "spring",
      "src": "https://insch.ntcu.edu.tw/en/downloader.php?sn=9&config=news_en",
      "basis": "學士正取；第 6–8 號，原圖第 1 頁已核對"
    }
  ],),
'0043': dict(tier='A', place='台中太平區', travel='市區公車約 30 分／機車 20 分',
  fee=dict(kind='free', amount=0, text='簡章明載外國學生申請不收任何申請費', src='https://admission.ncut.edu.tw/parts/proofReaderNews.ashx?ii=_281969417709349.pdf', year='115'),
  tuition=dict(min=46200, max=54058, year='115', text='每學期 46,200–54,058（依系）；宿舍四人房 11,500／學期', src='https://admission.ncut.edu.tw/parts/proofReaderNews.ashx?ii=_281969417709349.pdf'),
  firstYear=dict(kind='half', factor=0.5),
  aid=dict(sure='115 學年起入學的學士新生，第一學年學雜費減半（依身分核給）。', review='另有每學期 30,000 元獎學金，要符合條件並審查。'),
  renew='30,000/學期：每學期至少 9 學分、班級前 50%、沒有不及格、沒有懲處、體育 70 分以上。不能和政府獎學金同領。第一年之後的學雜費減免不能假設會繼續。',
  lang='多數學士系要 TOCFL A2（含）以上。',
  after="115 春季簡章已公告，但招生表只有碩博士，學士仍報秋季。115 秋季第一梯 3/23–5/10 報名、5/27 寄通知；116 尚未公告。",
  verdict='公立、免申請費、第一年學雜費減半、A2 多數系可報。只收秋季，所以是 2027 秋季的主力。',
  verdictMy='အစိုးရကျောင်း၊ လျှောက်လွှာကြေး အခမဲ့၊ ပထမနှစ် ကျောင်းလခ တစ်ဝက်လျှော့။ A2 ဖြင့် ဌာနအများစု ရ။ ဆောင်းဦး (၂၀၂၇ စက်တင်ဘာ) သာ။',
  checked="2026-10-05",
  bizAdmits=[],
  bizAdmitsNote="官網榜單入口讀取逾時，尚未取得可分系計數的學士榜單；不填成 0 人。",),
'0050': dict(tier='A', place='台中北區・市中心', travel='市區公車/機車 10 分',
  fee={
    "kind": "silent",
    "text": "已重讀 115 簡章；未找到申請費或明文免收的說明，不能當免費。",
    "src": "https://oia.nutc.edu.tw/var/file/42/1042/img/1597/313422402.pdf",
    "year": "115"
  },
  tuition={
    "min": 47344,
    "max": 56452,
    "year": "114",
    "text": "每學期學費＋雜費參考 47,344–56,452 元。115 簡章引用 114 表：一般商／語文 47,344，資管／設計等 56,452。住宿、保險與電腦費另計。",
    "src": "https://oia.nutc.edu.tw/var/file/42/1042/img/1597/313422402.pdf"
  },
  firstYear=dict(kind='minus', minus=25000),
  aid=dict(sure='新生第一學年註冊時直接減免，每學期最高 25,000 元（115 起適用，依預算）。', review='第二年起依成績審查，最高可到每學期 50,000（前 1/5 名額）。'),
  renew='學士平均 75、操行 80；每學期服務 60 小時；最多 4 年；不能和政府獎學金同領。',
  lang='依系 A2 到 B2 不等（例：企管系要 B2）。報名前逐系確認。',
  after='只收秋季。入學許可原則上寄電子檔。往年早梯 11 月中開放、2 月初放榜，是秋季最早知道結果的學校之一。',
  verdict='市中心、公立、第一年直接減免。只收秋季，但早梯往年 11 月開、2 月放榜，很早就能知道結果。',
  verdictMy="မြို့လယ်၊ အစိုးရကျောင်း။ ပထမနှစ် တစ်စာသင်ကာလလျှင် NT$25,000 အထိ လျှော့။ ဆောင်းဦးသာ၊ နိုဝင်ဘာတွင် စောစောလျှောက်ရင် ဖေဖော်ဝါရီမှာ ရလဒ်သိ။",
  checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "企業管理系（第2梯）",
      "count": 2,
      "year": "115",
      "term": "fall",
      "src": "https://oia.nutc.edu.tw/p/404-1042-134790.php",
      "basis": "官方第 2 階段圖片：四技正取；排除二技、轉學、碩博士與備取",
      "round": 2
    },
    {
      "dept": "國際貿易與經營系（第2梯）",
      "count": 4,
      "year": "115",
      "term": "fall",
      "src": "https://oia.nutc.edu.tw/p/404-1042-134790.php",
      "basis": "官方第 2 階段圖片：四技正取；排除二技、轉學、碩博士與備取",
      "round": 2
    },
    {
      "dept": "資訊管理系（第2梯）",
      "count": 2,
      "year": "115",
      "term": "fall",
      "src": "https://oia.nutc.edu.tw/p/404-1042-134790.php",
      "basis": "官方第 2 階段圖片：四技正取；排除二技、轉學、碩博士與備取",
      "round": 2
    },
    {
      "dept": "流通管理系（第2梯）",
      "count": 1,
      "year": "115",
      "term": "fall",
      "src": "https://oia.nutc.edu.tw/p/404-1042-134790.php",
      "basis": "官方第 2 階段圖片：四技正取；排除二技、轉學、碩博士與備取",
      "round": 2
    },
    {
      "dept": "休閒事業經營系（第2梯）",
      "count": 3,
      "year": "115",
      "term": "fall",
      "src": "https://oia.nutc.edu.tw/p/404-1042-134790.php",
      "basis": "官方第 2 階段圖片：四技正取；排除二技、轉學、碩博士與備取",
      "round": 2
    }
  ],),
'1008': dict(tier='A', place='台中沙鹿區（海線）', travel='開車/客運約 30–40 分',
  fee={
    "kind": "silent",
    "text": "已重讀 115 簡章；未找到申請費或明文免收的說明，不能當免費。",
    "src": "https://oia.pu.edu.tw/var/file/48/1048/img/1126/516627917.pdf",
    "year": "115"
  },
  tuition=dict(min=44811, max=53874, year='114', text='114 學年各院學雜費（每學期）；宿舍 10,000–15,500', src='https://oia.pu.edu.tw/var/file/48/1048/img/1126/516627917.pdf'),
  firstYear=dict(kind='lang'),
  aid=dict(sure='看語言證書就給：TOCFL B1（三級）→ 第一學年學雜費同額助學金；A2（二級）→ 第一學年學費同額（雜費自付）。', review='第二年起依班排名審核。'),
  renew='第二年起依前一學期排名：前 15% 35,000、15–30% 20,000、30–50% 8,000 元；無懲處並完成 10 小時國際學習。',
  lang='中文授課學士：TOCFL A2 即可。春季入學跟原班一起上課，不另開班。',
  after='春季第 1 梯 10/15 截止、11/30 放榜；第 2 梯 11/15 截止、12/24 放榜；放榜後 email 並寄書面通知；2027/2/22 註冊。',
  verdict='A2 就能報，而且憑 TOCFL 證書就有第一年學費補助，不是比運氣的獎學金。春季第 1 梯 10/15 截止，最急。',
  verdictMy='A2 ဖြင့် လျှောက်နိုင်။ TOCFL လက်မှတ်ရှိရင် ပထမနှစ် ကျောင်းလခ ထောက်ပံ့ငွေ ရ (B1 ဆို ပိုကောင်း)။ နွေဦး အဆင့် ၁ နောက်ဆုံးရက် 10/15 — အမြန်ဆုံး။',
  checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "行銷與流通管理學系（第1梯）",
      "count": 8,
      "year": "115",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/257/728221571.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "國際企業學系（第1梯）",
      "count": 6,
      "year": "115",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/257/728221571.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "觀光事業學系（第1梯）",
      "count": 7,
      "year": "115",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/257/728221571.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "寰宇管理學士學位學程（第1梯）",
      "count": 52,
      "year": "115",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/257/728221571.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "行銷與流通管理學系（第2梯）",
      "count": 10,
      "year": "115",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/257/519749998.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "國際企業學系（第2梯）",
      "count": 15,
      "year": "115",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/257/519749998.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "會計學系（第2梯）",
      "count": 2,
      "year": "115",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/257/519749998.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "觀光事業學系（第2梯）",
      "count": 13,
      "year": "115",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/257/519749998.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "財務金融學系（第2梯）",
      "count": 2,
      "year": "115",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/257/519749998.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "資訊管理學系（第2梯）",
      "count": 3,
      "year": "115",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/257/519749998.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "寰宇管理學士學位學程（第2梯）",
      "count": 36,
      "year": "115",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/257/519749998.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "行銷與流通管理學系（第1梯）",
      "count": 7,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/174/317234510.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "國際企業學系（第1梯）",
      "count": 14,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/174/317234510.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "會計學系（第1梯）",
      "count": 2,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/174/317234510.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "觀光事業學系（第1梯）",
      "count": 9,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/174/317234510.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "財務金融學系（第1梯）",
      "count": 3,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/174/317234510.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "資訊管理學系（第1梯）",
      "count": 7,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/174/317234510.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "寰宇管理學士學位學程（第1梯）",
      "count": 24,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/174/317234510.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "行銷與流通管理學系（第2梯）",
      "count": 7,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/p/406-1048-64344%2Cr13.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "國際企業學系（第2梯）",
      "count": 15,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/p/406-1048-64344%2Cr13.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "會計學系（第2梯）",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/p/406-1048-64344%2Cr13.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "觀光事業學系（第2梯）",
      "count": 15,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/p/406-1048-64344%2Cr13.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "財務金融學系（第2梯）",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/p/406-1048-64344%2Cr13.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "資訊管理學系（第2梯）",
      "count": 2,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/p/406-1048-64344%2Cr13.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "寰宇管理學士學位學程（第2梯）",
      "count": 19,
      "year": "114",
      "term": "fall",
      "src": "https://oia.pu.edu.tw/p/406-1048-64344%2Cr13.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "行銷與流通管理學系（第1梯）",
      "count": 1,
      "year": "114",
      "term": "spring",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/720225637.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "國際企業學系（第1梯）",
      "count": 3,
      "year": "114",
      "term": "spring",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/720225637.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "觀光事業學系（第1梯）",
      "count": 1,
      "year": "114",
      "term": "spring",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/720225637.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "寰宇管理學士學位學程（第1梯）",
      "count": 14,
      "year": "114",
      "term": "spring",
      "src": "https://oia.pu.edu.tw/var/file/48/1048/img/720225637.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "行銷與流通管理學系（第2梯）",
      "count": 7,
      "year": "114",
      "term": "spring",
      "src": "https://oia.pu.edu.tw/p/16-1048-68428.php?Lang=zh-tw",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "國際企業學系（第2梯）",
      "count": 6,
      "year": "114",
      "term": "spring",
      "src": "https://oia.pu.edu.tw/p/16-1048-68428.php?Lang=zh-tw",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "觀光事業學系（第2梯）",
      "count": 4,
      "year": "114",
      "term": "spring",
      "src": "https://oia.pu.edu.tw/p/16-1048-68428.php?Lang=zh-tw",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "寰宇管理學士學位學程（第2梯）",
      "count": 5,
      "year": "114",
      "term": "spring",
      "src": "https://oia.pu.edu.tw/p/16-1048-68428.php?Lang=zh-tw",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    }
  ],
  bizAdmitsNote="依梯次分列，沒有跨梯次相加；只數一般學士新生正取。",),
'0006': dict(tier='P', place='台中南區・市中心', travel='市區公車/機車 10 分',
  fee={
    "kind": "silent",
    "text": "已重讀 115 簡章；未找到申請費或明文免收的說明，不能當免費。",
    "src": "https://oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/115_Academic_Year_Application_Guidelines_re.pdf",
    "year": "115"
  },
  tuition=dict(min=45691, max=53914, year='114', text='114 學年外國學生學士班學雜費（每學期，依學院）', src='https://www.oia.nchu.edu.tw/index.php/zh/2-prospective-students-tw/2-4-fees-and-financing-tw/2-4-1-tuition-fees-tw'),
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='報名系統勾選「申請中興獎學金」：學費減免到本國生標準或全免，少數每月 6,000／8,000 元；審查，不保證。'),
  renew='每年再申請；學士前兩學期平均 70 以上，院系排序；最長 4 年。',
  lang='全校最低 TOCFL A2；各系可以要求更高，報名前逐系確認。最多填兩個志願。',
  after='春季只收研究所。學士只能報秋季：往年 1 月中–3 月中報名、5 月底放榜。',
  verdict='台中最有名的國立大學，就在市區。學士只收秋季，放榜 5 月底較晚；獎學金要審查。值得報 2027 秋季。',
  verdictMy='ထိုင်ချုံးမြို့ထဲရှိ နာမည်ကြီး အစိုးရတက္ကသိုလ်။ ဘွဲ့ကြို ဆောင်းဦးသာ (ဇန်နဝါရီ–မတ်)။ ပညာသင်ဆု စစ်ဆေးရွေးချယ်သည်။',
  checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "企業管理學系",
      "count": 3,
      "year": "115",
      "term": "fall",
      "src": "https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2026_Fall_Semester_NCHU.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "行銷學系",
      "count": 3,
      "year": "115",
      "term": "fall",
      "src": "https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2026_Fall_Semester_NCHU.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "資訊管理學系",
      "count": 6,
      "year": "115",
      "term": "fall",
      "src": "https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2026_Fall_Semester_NCHU.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "國際農企業學士學位學程",
      "count": 22,
      "year": "115",
      "term": "fall",
      "src": "https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2026_Fall_Semester_NCHU.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "企業管理學系",
      "count": 7,
      "year": "114",
      "term": "fall",
      "src": "https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2025_Fall_Semester_NCHU.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "會計學系",
      "count": 4,
      "year": "114",
      "term": "fall",
      "src": "https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2025_Fall_Semester_NCHU.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "財務金融學系",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2025_Fall_Semester_NCHU.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "行銷學系",
      "count": 4,
      "year": "114",
      "term": "fall",
      "src": "https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2025_Fall_Semester_NCHU.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "資訊管理學系",
      "count": 3,
      "year": "114",
      "term": "fall",
      "src": "https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2025_Fall_Semester_NCHU.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "國際農企業學士學位學程",
      "count": 12,
      "year": "114",
      "term": "fall",
      "src": "https://www.oia.nchu.edu.tw/images/File/03_Apply_to_NCHU/3-1-Degree-Programs/3-1-2-International-Students/2025_Fall_Semester_NCHU.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    }
  ],),
'1001': dict(tier='P', place='台中西屯區（大度山）', travel='市區公車約 30–40 分',
  fee=dict(kind='free', amount=0, text='115-2 簡章第 8 頁：申請費「免費」', src='https://exam2.thu.edu.tw/EXAM/download_doc_26/115_regulations.pdf', year='115-2'),
  tuition=dict(min=57860, max=67547, year='115', text='115 學年外國學生學士班學雜費（每學期，依系）；宿舍 9,260–12,760＋網路 800＋維護 1,000', src='https://exam2.thu.edu.tw/EXAM/download_doc_26/26.pdf'),
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='外國學生獎助學金：學士每學年 100,000／60,000／20,000 元，審查並依經費核定。'),
  renew='在校學士 GPA 2.93 以上或班排前 25%；每年重新申請；通常每學期服務 10 小時；最多 4 年。',
  lang='中文授課基本 TOCFL A2，但各系可以更高（例：財金 A2、會計 C1）。',
  after='春季 10/1–10/31 線上報名，文件 11/3 前寄達；12 月上旬放榜；2027/1/4 前回覆入學意願；2 月上旬註冊。',
  verdict='有名、免申請費、台中市內。學費是名單中最高（每學期約 5.8–6.8 萬），獎學金要審查。春季 10/1 開放報名。',
  verdictMy='နာမည်ကြီး၊ လျှောက်လွှာကြေး အခမဲ့၊ ထိုင်ချုံးမြို့ထဲ။ ကျောင်းလခ အမြင့်ဆုံး (တစ်စာသင်နှစ် ~NT$58,000–68,000)။ နွေဦး 10/1–10/31။',
  checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "企業管理學系",
      "count": 12,
      "year": "114",
      "term": "fall",
      "src": "https://exam2.thu.edu.tw/EXAM/doc/1036711410_public_001.pdf",
      "basis": "一般學士正取；以中文 114 年度及 2025 年公告為準，英文表頭誤植 2024"
    },
    {
      "dept": "國際經營與貿易學系",
      "count": 11,
      "year": "114",
      "term": "fall",
      "src": "https://exam2.thu.edu.tw/EXAM/doc/1036711410_public_001.pdf",
      "basis": "一般學士正取；以中文 114 年度及 2025 年公告為準，英文表頭誤植 2024"
    },
    {
      "dept": "財務金融學系",
      "count": 3,
      "year": "114",
      "term": "fall",
      "src": "https://exam2.thu.edu.tw/EXAM/doc/1036711410_public_001.pdf",
      "basis": "一般學士正取；以中文 114 年度及 2025 年公告為準，英文表頭誤植 2024"
    },
    {
      "dept": "國際菁英學位學程（財金）",
      "count": 9,
      "year": "114",
      "term": "fall",
      "src": "https://exam2.thu.edu.tw/EXAM/doc/1036711410_public_001.pdf",
      "basis": "一般學士正取；以中文 114 年度及 2025 年公告為準，英文表頭誤植 2024"
    },
    {
      "dept": "資訊管理學系",
      "count": 8,
      "year": "114",
      "term": "fall",
      "src": "https://exam2.thu.edu.tw/EXAM/doc/1036711410_public_001.pdf",
      "basis": "一般學士正取；以中文 114 年度及 2025 年公告為準，英文表頭誤植 2024"
    },
    {
      "dept": "餐旅管理學系",
      "count": 6,
      "year": "114",
      "term": "fall",
      "src": "https://exam2.thu.edu.tw/EXAM/doc/1036711410_public_001.pdf",
      "basis": "一般學士正取；以中文 114 年度及 2025 年公告為準，英文表頭誤植 2024"
    },
    {
      "dept": "經濟學系",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://exam2.thu.edu.tw/EXAM/doc/1036711410_public_001.pdf",
      "basis": "一般學士正取；以中文 114 年度及 2025 年公告為準，英文表頭誤植 2024"
    },
    {
      "dept": "國際經營管理學位學程",
      "count": 64,
      "year": "114",
      "term": "fall",
      "src": "https://exam2.thu.edu.tw/EXAM/doc/1036711410_public_001.pdf",
      "basis": "一般學士正取；以中文 114 年度及 2025 年公告為準，英文表頭誤植 2024"
    }
  ],),
'1007': dict(tier='P', place='台中西屯區（逢甲商圈）', travel='市區公車約 20–30 分',
  fee=dict(kind='unknown', text='2027 春季簡章放在 SharePoint，要登入才能看，申請費沒辦法核對', src='https://www.fcu.edu.tw/recurit_list/international-spring-semester/', year='115-2'),
  tuition=None,
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='海外華裔暨外國學生獎助學金：每學年 120,000／60,000／30,000／20,000 元，審查、依名額；須先繳清學雜費。'),
  renew='第二年起依成績：學士平均 70 或班排前 50%；最長 4 年；不能和臺灣獎學金同領。',
  lang='簡章要登入才能看，語言門檻請自己確認。',
  after='第 1 梯：9/15–11/8 報名，11/24 放榜，12/4 寄入學許可。第 2 梯：11/11–11/30 報名，12/15 放榜，12/24 寄入學許可。2027/2/22 註冊。',
  letter={'spring':['2026-12-04','2026-12-24']},
  readYourself=[dict(label='2027 春季簡章（SharePoint，要登入或用瀏覽器開）', url='https://fengchia-my.sharepoint.com/:b:/g/personal/osra_o365_fcu_edu_tw/IQD4eGVyErdXTrt1h72VPYg4AeugwmTNp0n9oa1UdvEGcU4?e=rZbQcU', why='看申請費、學費、各系語言門檻')],
  verdict='台中知名私立大學，春季第 1 梯 11/24 就放榜，是春季最早拿到入學許可的（12/4）。學費與申請費要自己看簡章。',
  verdictMy='ထိုင်ချုံး နာမည်ကြီး ပုဂ္ဂလိက တက္ကသိုလ်။ နွေဦး အဆင့် ၁ 11/8 အထိ လျှောက်၊ 11/24 ရလဒ်၊ 12/4 ဝင်ခွင့်စာ — အစောဆုံး။',
  checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "合作經濟暨社會事業經營學系（第2梯）",
      "count": 1,
      "year": "113",
      "term": "spring",
      "src": "https://s3.ap-southeast-1.amazonaws.com/web-content.fcu.edu.tw/wp-content/uploads/2024/12/17103119/113-2-%E8%8B%B1%E5%85%AC%E5%91%8A%E7%AC%AC%E4%BA%8C%E6%A2%AF%E6%AC%A1.pdf",
      "basis": "2025 年春季第 2 梯一般學士正取；不含國企碩士與財金 TDTU 雙聯",
      "round": 2
    }
  ],
  bizAdmitsNote="先核得 113 春季（2025 年）第 2 梯一般學士 1 人；未把國企碩士或財金 TDTU 雙聯算入。較新的簡章下載需登入／無法讀取。",),
'0017': dict(tier='P', place='新北三峽', travel='高鐵到板橋再轉車，約 1.5–2 小時；要搬家',
  fee={
    "kind": "silent",
    "text": "已重讀 115 簡章；未找到申請費或明文免收的說明，不能當免費。",
    "src": "https://cms-carrier.ntpu.edu.tw/uploads/115_1_2026_c93708c94b.pdf",
    "year": "115"
  },
  tuition={
    "min": 45691,
    "max": 52668,
    "year": "114",
    "text": "每學期學費＋雜費參考 45,691–52,668 元。一般商管 46,091；語言、網路等其他費另計。",
    "src": "https://cms-carrier.ntpu.edu.tw/uploads/115_1_2026_c93708c94b.pdf"
  },
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='鳶飛國際優秀新生獎學金：每學期 40,000 元、最多 4 年（外國學士新生；永續創新國際學院除外）；錄取後另外申請並審查。'),
  renew='每學期平均 75 以上並完成註冊；未達先停發；不能全職工作或領政府獎補助。',
  lang='未逐系整理；看簡章。',
  after="115-2 春季系統列 9/3–10/31 報名，放榜尚未核得今年公告，先以 114 往年 12/9 參考。",
  verdict='國立名校、獎學金每學期 4 萬（要審查）。在新北三峽要搬家，住宿與生活費要另外算。',
  verdictMy="နာမည်ကြီး အစိုးရတက္ကသိုလ် (နယူးတိုင်ပေ)။ တစ်စာသင်ကာလ NT$40,000 ပညာသင်ဆု (စစ်ဆေးရွေး)။ အိမ်ပြောင်းရမည်။",
  checked="2026-10-05",
  bizAdmits=[],
  bizAdmitsNote="已讀招生簡章，尚未取得可分系計數的一般學士公開榜單；不填成 0 人。",),
'0025': dict(tier='P', place='台北市大安區', travel='高鐵約 1 小時＋捷運；要搬家',
  fee={
    "kind": "unknown",
    "text": "115-2 春季簡章明載免申請費，但春季僅收研究所；學士秋季適用的申請費尚未核得，不能直接套用。",
    "src": "https://oia.ntut.edu.tw/var/file/32/1032/img/2027SpringAdmissionHandbook.pdf",
    "year": "115-2（僅研究所；學士待核）"
  },
  tuition=None,
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='校長獎學金只有第一年：全額（每月 15,000，6 名）或半額（每月 8,000，20 名），兩者都補全額學雜費；報名時勾選，擇優。另有 TOCFL B1 以上可申請的學雜費 50% 減免。'),
  renew='校長獎學金不能續領。B1 學雜費減免：前學年學業 70、操行 80，而且 TOCFL 要比上次再高 1 級。',
  lang='看系所。B1 以上才有學雜費減免資格。',
  after='春季只收研究所。學士只能報秋季：116-1 已公告 2026/12/1–2027/3/10 報名、2027/5/1 放榜。',
  verdict="台北名校，116-1秋季日期已有正式資料，春季僅研究所。學士申請費仍待確認；第一年全額獎學金須審查、名額少。",
  verdictMy='တိုင်ပေ နာမည်ကြီး နည်းပညာတက္ကသိုလ်။ ဆောင်းဦး 2026/12/1–2027/3/10 လျှောက် (တရားဝင်)။ ပညာသင်ဆု နေရာနည်း။ အိမ်ပြောင်းရမည်။',
  checked="2026-10-05",
  readYourself=[
    {
      "label": "學士秋季招生規定待確認",
      "url": "https://oia.ntut.edu.tw/p/412-1032-13828.php?Lang=en",
      "why": "已讀春季研究所簡章，學士秋季申請費與學雜費仍需確認。"
    }
  ],
  bizAdmits=[
    {
      "dept": "經營管理系",
      "count": 7,
      "year": "115",
      "term": "fall",
      "src": "https://oia.ntut.edu.tw/p/406-1032-105591%2Cr1150.php?Lang=zh-tw",
      "basis": "一般學士正取；同系備取 3 人不計"
    },
    {
      "dept": "資訊與財金管理系",
      "count": 2,
      "year": "115",
      "term": "fall",
      "src": "https://oia.ntut.edu.tw/p/406-1032-105591%2Cr1150.php?Lang=zh-tw",
      "basis": "一般學士正取；同系備取 3 人不計"
    }
  ],),
'0049': dict(tier='B', place='台中北區・市中心', travel='市區公車/機車 10 分',
  fee=dict(kind='paid', amount=1500, text='115-2：學士、碩士 NT$1,500；郵寄送件，期限內寄達', src='https://admission.ntus.edu.tw/index.php?article_id=46767&code=list&flag=detail&ids=1177', year='115-2'),
  tuition=dict(min=53500, max=53500, year='115-2', approx=True, text='網頁列學費 35,700＋雜費約 17,800（數字排版不清，以簡章為準）', src='https://admission.ntus.edu.tw/index.php?article_id=46767&code=list&flag=detail&ids=1177'),
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='成績優異可申請每學期最高 60,000 元；名額有限，新生第一學期能不能申請還沒確認。'),
  renew='每學期開學 2 週內申請；學士前學期至少 10 學分、平均 70。',
  lang='TOCFL A2（含）以上。',
  after='春季 9/1–11/30 報名；2026/12/30 前放榜並寄錄取通知書。',
  letter={'spring':'2026-12-30'},
  verdict='公立、市中心、A2 可報、春季開到 11/30。這是體育專業大學，他要喜歡運動相關科系才適合。',
  verdictMy='အစိုးရ အားကစားတက္ကသိုလ်၊ မြို့လယ်။ A2 ရ။ နွေဦး 11/30 အထိ။ အားကစားဘာသာရပ် ကြိုက်မှ သင့်တော်။',
  checked=CHECKED),
'1034': dict(tier='B', place='台中沙鹿區（海線）', travel='開車/客運約 30–40 分',
  fee=dict(kind='free', amount=0, text='115 簡章第 19 頁：本項招生免收申請費（含 2027 春季）', src='https://ifp.hk.edu.tw/wp-content/uploads/2026/09/%E5%BC%98%E5%85%89115%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E6%8B%9B%E7%94%9F%E7%B0%A1%E7%AB%A0_%E4%BF%AEV2-1106.pdf', year='115'),
  tuition={
    "min": 45547,
    "max": 55057,
    "year": "114",
    "text": "每學期學費＋雜費參考 45,547–55,057 元。115 簡章引用 114 學士表：餐旅 51,936，健康事業管理與文化設計行銷 45,547。原 55,753 為碩士費用，不套用學士。",
    "src": "https://ifp.hk.edu.tw/wp-content/uploads/2026/09/%E5%BC%98%E5%85%89115%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E6%8B%9B%E7%94%9F%E7%B0%A1%E7%AB%A0_%E4%BF%AEV2-1106.pdf"
  },
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='每學期 A 級 50,000／B 級 30,000／C 級 10,000／D 級 5,000 元；要申請並審查。'),
  renew='新生與續讀審核條件不同，續領細則簡章沒寫清楚。',
  lang='TOCFL A2（含）以上。護理、物理治療、語言治療春季不招生。',
  after='春季 10/5–12/1 報名；2027/1/10 放榜；1/15 前 email＋郵寄入學許可。',
  letter={'spring':'2027-01-15'},
  verdict='免申請費、A2、春季開到 12/1。放榜 1/10 較晚；私立科大，獎學金要審查。',
  verdictMy='လျှောက်လွှာကြေး အခမဲ့၊ A2 ရ၊ နွေဦး 10/5–12/1။ ရလဒ် 1/10 (နောက်ကျ)။',
  checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "餐旅管理系（第2梯）",
      "count": 2,
      "year": "114",
      "term": "fall",
      "src": "https://ifp.hk.edu.tw/%E5%BC%98%E5%85%89%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%B8114%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%A7%8B%E5%AD%A3%E7%8F%AD%EF%BC%88%E7%AC%AC%E4%BA%8C%E6%A2%AF%E6%AC%A1%EF%BC%89%E5%A4%96%E5%9C%8B%E5%AD%B8/",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "餐旅管理系（第3梯）",
      "count": 8,
      "year": "114",
      "term": "fall",
      "src": "https://www.hk.edu.tw/remote/HKifp77141/",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 3
    },
    {
      "dept": "健康事業管理系（第3梯）",
      "count": 2,
      "year": "114",
      "term": "fall",
      "src": "https://www.hk.edu.tw/remote/HKifp77141/",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 3
    },
    {
      "dept": "文化設計與行銷系（第3梯）",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://www.hk.edu.tw/remote/HKifp77141/",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 3
    }
  ],
  bizAdmitsNote="114 秋季第 2、3 梯分開計數，掃描榜單已逐頁核對；未含碩士。",),
'1018': dict(tier='B', place='台中霧峰區', travel='市區公車約 40 分／機車 25 分',
  fee={
    "kind": "silent",
    "text": "已重讀 115 簡章；未找到申請費或明文免收的說明，不能當免費。",
    "src": "https://icsc.cyut.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelV6TDNCMFlWODBNekE1TkY4eE1qSTNNRFE1WHpnNE1EQTBMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKICFCLOQOPPXX00ZS5430YWMONPWWEC34SSMKLPIDCCTSFCNKFDEGFG10KLTSVWPOXT15DG24NKXTMOMOA0YSIGICQLLO00JDQPTW14MK3045OOHGGHUSSS404544VSA0EGGDTWB4WSXSWSB0CGMKVXNPDDA0SW30IGA4QOOKLKFCICKKDHYX44B0TX24DCJGMK25WSEGXSXSHDYTPKA5XWROZWOPQOSSIGWXIC00YXMPLOPONK24ZSPKFHXS34UWXSGCGG05OOA5UWTS45UW00OKOK54LOCCHDHHHCEGEGWS14MOJGWSOP34PKGCJDJDLOA534A41111",
    "year": "115"
  },
  tuition=dict(min=48409, max=55684, year='115', text='管理/人文 48,409；設計/理工/資訊/航空 55,684（每學期，住宿另計）', src='https://icsc.cyut.edu.tw/p/404-1008-58738.php?Lang=zh-tw'),
  firstYear={
    "kind": "review"
  },
  aid={
    "sure": None,
    "review": "新生隨入學申請一併申請。依先前成績、操行及審查給每學期學雜費半額或全額，無保證名額；不能同領政府或校外全額獎學金。",
    "src": "https://icsc.cyut.edu.tw/p/404-1008-20583.php?Lang=en",
    "year": "現行辦法（115簡章引用）"
  },
  renew="學士最多 8 學期；每學期按前一學期學業、操行成績重新核定。詳細分數另由審查基準訂定，本頁未列，尚未核得；不能直接當成續領保證。",
  lang='TOCFL A2。',
  after="115 春季第1梯 12/18 放榜、12/24 寄通知；第2梯最終 12/19 截止、1/15 放榜、1/22 寄通知。各梯報名截止未完全核得；116 秋季尚未公告。",
  verdict='A2、春季開到 12/19（最晚截止），獎學金最多到全額學雜費但要審查。',
  verdictMy='A2 ရ။ နွေဦး 12/19 အထိ (နောက်ဆုံးပိတ်)။ ကျောင်းလခ တစ်ဝက်/အပြည့် ပညာသင်ဆု (စစ်ဆေးရွေး)။',
  checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "企業管理系（第1梯）",
      "count": 26,
      "year": "115",
      "term": "fall",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-39949.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "財務金融系（第1梯）",
      "count": 1,
      "year": "115",
      "term": "fall",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-39949.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "企業管理系（第2梯）",
      "count": 15,
      "year": "115",
      "term": "fall",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-39949.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "資訊管理系（第2梯）",
      "count": 2,
      "year": "115",
      "term": "fall",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-39949.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "休閒事業管理系（第2梯）",
      "count": 2,
      "year": "115",
      "term": "fall",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-39949.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "企業管理系（第3梯）",
      "count": 21,
      "year": "115",
      "term": "fall",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-39949.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 3
    },
    {
      "dept": "行銷與流通管理系（第3梯）",
      "count": 8,
      "year": "115",
      "term": "fall",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-39949.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 3
    },
    {
      "dept": "企業管理系（第1梯）",
      "count": 22,
      "year": "113",
      "term": "spring",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-51343.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "行銷與流通管理系（第1梯）",
      "count": 2,
      "year": "113",
      "term": "spring",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-51343.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "資訊管理系（第1梯）",
      "count": 8,
      "year": "113",
      "term": "spring",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-51343.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "企業管理系（第2梯）",
      "count": 7,
      "year": "113",
      "term": "spring",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-52396.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "行銷與流通管理系（第2梯）",
      "count": 6,
      "year": "113",
      "term": "spring",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-52396.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "資訊管理系（第2梯）",
      "count": 8,
      "year": "113",
      "term": "spring",
      "src": "https://icsc.cyut.edu.tw/p/404-1008-52396.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    }
  ],
  renewSource={
    "src": "https://icsc.cyut.edu.tw/p/404-1008-20583.php?Lang=en",
    "year": "現行辦法（115簡章引用）"
  },),
'1048': dict(tier='B', place='台中霧峰區', travel='市區公車約 40 分／機車 25 分',
  fee={
    "kind": "free",
    "amount": 0,
    "text": "115 學年度一般學位生簡章明載：申請學位課程免申請費。",
    "src": "https://oia.asia.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU1TDNCMFlWOHpPVFZmTnpBd05qUTBOMTg0TXprd09DNXdaR1k9&fname=WW54RPOKIC4441MPHCLKFCZWXSMOWT24PKJCYS35TXVXPO40NKB4OPB4WS1030EGPOCCIHXXVS04GDWWMK3040GCB0B0TS35GGMPB5OONKTS34FGOOA401XXVW4044GDIGPONOYWKKKODG3550NOPONPCC35GGA0XWUSUSSWWSLK01XXMK54A5NPFG10FG24FC14MKKKQOMO10ICQPUXB0TSUSB0ZWA0QODCXWDCYWUSLLZX00B054ICMKTWVXMKQO34CCMK41A1OOA0YSDCFC54GG54A0PKGCPOCDHHA40454TXVWTWMOXS34RKNOWSA1VX44FCWSMKB0FG00HGKLA0SS44LP05EDNOEGMORKB440GCDGVW24MKUT35YXB4POB4YSQOWSKKXXOKPO04POMP",
    "year": "115"
  },
  tuition=None,
  firstYear={
    "kind": "review"
  },
  aid={
    "sure": None,
    "review": "報名表勾選獎學金並上傳文件；名額有限，依資格與預算審查。可核全額或部分學雜費、住宿減免或生活津貼，金額以錄取通知為準。學士最多補助 1 年。",
    "src": "https://oia.asia.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU1TDNCMFlWOHpPVFZmTnpBd05qUTBOMTg0TXprd09DNXdaR1k9&fname=WW54RPOKIC4441MPHCLKFCZWXSMOWT24PKJCYS35TXVXPO40NKB4OPB4WS1030EGPOCCIHXXVS04GDWWMK3040GCB0B0TS35GGMPB5OONKTS34FGOOA401XXVW4044GDIGPONOYWKKKODG3550NOPONPCC35GGA0XWUSUSSWWSLK01XXMK54A5NPFG10FG24FC14MKKKQOMO10ICQPUXB0TSUSB0ZWA0QODCXWDCYWUSLLZX00B054ICMKTWVXMKQO34CCMK41A1OOA0YSDCFC54GG54A0PKGCPOCDHHA40454TXVWTWMOXS34RKNOWSA1VX44FCWSMKB0FG00HGKLA0SS44LP05EDNOEGMORKB440GCDGVW24MKUT35YXB4POB4YSQOWSKKXXOKPO04POMP",
    "year": "115",
    "sources": [
      {
        "src": "https://oia.asia.edu.tw/p/412-1008-1358.php?Lang=en",
        "year": "115"
      }
    ]
  },
  renew="學士受獎最多 1 年，不能當作四年都有。115 簡章另列前學年平均至少 80 分；B 級以上每學期服務 30 小時。新生須先付足學雜費，核准後學期末發放。",
  lang='未核得。',
  after="115 春季第5–7次放榜為 10/30、11/30、12/30；各批截止未單列。官方時程／簡章全期11/29截止、報名頁寫11/30，建議11/29前完成。116 秋季尚未公告。",
  readYourself=[
    {
      "label": "亞洲115一般學位生簡章",
      "url": "https://oia.asia.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU1TDNCMFlWOHpPVFZmTnpBd05qUTBOMTg0TXprd09DNXdaR1k9&fname=WW54RPOKIC4441MPHCLKFCZWXSMOWT24PKJCYS35TXVXPO40NKB4OPB4WS1030EGPOCCIHXXVS04GDWWMK3040GCB0B0TS35GGMPB5OONKTS34FGOOA401XXVW4044GDIGPONOYWKKKODG3550NOPONPCC35GGA0XWUSUSSWWSLK01XXMK54A5NPFG10FG24FC14MKKKQOMO10ICQPUXB0TSUSB0ZWA0QODCXWDCYWUSLLZX00B054ICMKTWVXMKQO34CCMK41A1OOA0YSDCFC54GG54A0PKGCPOCDHHA40454TXVWTWMOXS34RKNOWSA1VX44FCWSMKB0FG00HGKLA0SS44LP05EDNOEGMORKB440GCDGVW24MKUT35YXB4POB4YSQOWSKKXXOKPO04POMP",
      "why": "學士申請费、獎學金與一年受獎上限"
    },
    {
      "label": "亞洲115春秋放榜時程",
      "url": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
      "why": "截止日兩個官方來源不同，建議11/29前完成"
    },
    {
      "label": "亞洲115新生註冊須知",
      "url": "https://oia.asia.edu.tw/p/412-1008-1358.php?Lang=en",
      "why": "先付足學雜費，學期末再核發補助"
    }
  ],
  verdict="115 簡章明文免申請費。春季建議11/29前完成；新生獎學金要審查、學士最多一年，並須先繳足學雜費。",
  verdictMy="လျှောက်လွှာကြေး အခမဲ့။ နွေဦး 11/29 မတိုင်မီ လျှောက်ပါ။ ပညာသင်ဆု စစ်ဆေးရွေးချယ်၊ ဘွဲ့ကြို အများဆုံး တစ်နှစ်။ ကျောင်းလခ အပြည့် အရင်ပေးရမည်။",
  checked="2026-10-05",
  renewSource={
    "src": "https://oia.asia.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU1TDNCMFlWOHpPVFZmTnpBd05qUTBOMTg0TXprd09DNXdaR1k9&fname=WW54RPOKIC4441MPHCLKFCZWXSMOWT24PKJCYS35TXVXPO40NKB4OPB4WS1030EGPOCCIHXXVS04GDWWMK3040GCB0B0TS35GGMPB5OONKTS34FGOOA401XXVW4044GDIGPONOYWKKKODG3550NOPONPCC35GGA0XWUSUSSWWSLK01XXMK54A5NPFG10FG24FC14MKKKQOMO10ICQPUXB0TSUSB0ZWA0QODCXWDCYWUSLLZX00B054ICMKTWVXMKQO34CCMK41A1OOA0YSDCFC54GG54A0PKGCPOCDHHA40454TXVWTWMOXS34RKNOWSA1VX44FCWSMKB0FG00HGKLA0SS44LP05EDNOEGMORKB440GCDGVW24MKUT35YXB4POB4YSQOWSKKXXOKPO04POMP",
    "year": "115",
    "sources": [
      {
        "src": "https://oia.asia.edu.tw/p/412-1008-1358.php?Lang=en",
        "year": "115"
      }
    ]
  },
  bizAdmits=[],
  bizAdmitsNote="原榜單站及 PDF 回應錯誤；新站可查放榜日，但尚未取得可分系計數的一般學士榜單。",),
'1045': dict(tier='B', place='台中南屯區', travel='市區公車約 30 分',
  fee=dict(kind='free', amount=0, text='115 秋季簡章：Application Fee: None（春季不直接套用）', src='https://ltu1470.video.ltu.edu.tw/filedownload/1128', year='115-1'),
  tuition=None,
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='一般每學期 15,000 元；學士班級前 3 名每學期 30,000；審查與經費核定。'),
  renew='前學期平均 85、操行 82，TOCFL B1（新生第一年免語言條件）；須完成服務/講座。',
  lang='TOCFL A2。',
  after='往年秋季 3/4–6/30 報名、8/3 寄結果。春季本期時程沒找到（114 春季有招生紀錄）。',
  readYourself=[dict(label='115 簡章 PDF（第 10 頁學費表）', url='https://ltu1470.video.ltu.edu.tw/filedownload/1128', why='PDF 文字編碼亂碼，學費、宿舍保證金沒辦法可靠讀出')],
  verdict='免申請費、A2。學費表讀不出來，要自己看簡章第 10 頁。',
  verdictMy='လျှောက်လွှာကြေး အခမဲ့၊ A2။ ကျောင်းလခ ဇယား ဖတ်မရ — PDF စာမျက်နှာ 10 ကြည့်ပါ။',
  checked=CHECKED),
'1062': dict(tier='B', place='台中西屯區', travel='市區公車約 30 分',
  fee=dict(kind='unknown', text='官網回應錯誤，簡章讀不到', src='https://admission.ocu.edu.tw/p/412-1023-5671.php', year='115'),
  tuition=None, firstYear=dict(kind='unknown'),
  aid=dict(sure=None, review='獎學金條文讀不到。'), renew='未核得。', lang='未核得。',
  after='114 春季有外國學生錄取公告，今年春季時程未核得。',
  readYourself=[dict(label='僑光外國學生招生頁', url='https://admission.ocu.edu.tw/p/412-1023-5671.php', why='看簡章、日期、申請費'), dict(label='僑光國際事務獎學金頁', url='https://ia.ocu.edu.tw/p/412-1013-2834.php?Lang=zh-tw', why='看獎學金')],
  verdict='資料幾乎都讀不到。只有在其他台中學校都不適合時再看。',
  verdictMy='အချက်အလက် မရသလောက်။ အခြားကျောင်းများ မသင့်တော်မှ ကြည့်ပါ။',
  checked="2026-10-05",
  bizAdmits=[],
  bizAdmitsNote="官網及榜單連結持續回應錯誤，尚未取得可計數的學士榜單；不填成 0 人。",),
'0021': dict(tier='B', place='南投埔里', travel='台中搭客運約 1 小時；住校為主',
  fee=dict(kind='free', amount=0, text='115 秋季公告明載免申請費（春季不直接套用）', src='https://apply.ncnu.edu.tw/', year='115-1'),
  tuition={
    "min": 45691,
    "max": 54615,
    "year": "115",
    "text": "每學期學費＋雜費參考 45,691–54,615 元。簡章估值；一般管理 46,091，資管 52,668。",
    "src": "https://oia.ncnu.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MekV4TDNCMFlWOHlNakUwTTE4eU1UUTJPRE14WHpnek1ETTNMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA0540054JGEGNO0000HHA404ROJGYWSWTS14OPB0FHMPQPMPXWTSYSMKJGOKFHDC45FCRKXWUX25DGA0DCXTPKDGDCGCUSB004MPA1GDQPVWYSDCFCDG14SWYSUSROQO41104410IGGDIG30RLIC20ROWSWS01A104VSSSB4JGECQOKKGHSSWW4001LLEDPOWWMORKMO14GCWSJCUSHCGGGDMLEGOKB0FDUWOOKKMKTSWWTSIDHH44EG54TXMOXSMO35STRODCLKA1VXHGCCSWB4ECFGDG54GHUSPOXWCCOOA4JCEGGDZSB4HGICQOFCMOWSCC35DCA0ZW30JCSWFG54FCROYWDCYT05TSLKNO24QOJGMKYSWSEGXSWSMLMPFCB514YWKO0114DCKLGHSSLKTX1050EGTS14IGMOZTLOQOUWDC10GGA1WWSSUWYWCDUW50OK30OKKKTSZTIHHCXSLK24VWHCMOLKIGRKLOMKA1YTXWTSNKB0ECA4FHDCA0FCA4XWFDKKA4LKHGZWXSOKLOIC50NOCGIC00UXVS31YSUS14QK20KOHHHH"
  }, firstYear=dict(kind='review'),
  aid=dict(sure=None, review='學雜費部分減免到本國生標準或全免，學士最多 4 年；依預算名額審核，新生隨入學申請。'),
  renew='在校前學期平均 80（或系所推薦）；中文授課在校生要 TOCFL A2；每年 4/15–30、10/15–30 申請下學期。',
  lang='依系。',
  after='115-2 一般外國學位生春季時程還沒找到；往年 10 月下旬–11 月上旬報名、1 月初放榜。',
  verdict='公立、免申請費、學雜費減免機會多。埔里離台中約 1 小時，平日要住校。',
  verdictMy='အစိုးရ၊ လျှောက်လွှာကြေး အခမဲ့၊ ကျောင်းလခ လျှော့ပေးမှု အခွင့်များ။ ပူလီ (ထိုင်ချုံးမှ ၁ နာရီ)၊ ကျောင်းအဆောင်နေရမည်။',
  checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "國際企業學系（第2梯）",
      "count": 1,
      "year": "115",
      "term": "fall",
      "src": "https://oia.ncnu.edu.tw/p/406-1017-35110%2Cr44.php?Lang=zh-tw",
      "basis": "第 2 梯一般學士正取；掃描榜單第 2 頁已核對，研究所不計",
      "round": 2
    },
    {
      "dept": "觀光休閒與餐旅管理學系（觀光休閒組）（第2梯）",
      "count": 1,
      "year": "115",
      "term": "fall",
      "src": "https://oia.ncnu.edu.tw/p/406-1017-35110%2Cr44.php?Lang=zh-tw",
      "basis": "第 2 梯一般學士正取；掃描榜單第 2 頁已核對，研究所不計",
      "round": 2
    }
  ],),
'0032': dict(tier='B', place='苗栗市', travel='台中搭火車約 40–50 分；可通勤但遠',
  fee={
    "kind": "silent",
    "text": "已重讀 115 簡章；未找到申請費或明文免收的說明，不能當免費。",
    "src": "https://enroll.nuu.edu.tw/var/file/65/1065/attach/15/pta_76237_4431663_47936.pdf",
    "year": "115"
  },
  tuition={
    "min": 39000,
    "max": 45000,
    "year": "114",
    "text": "每學期學費＋雜費參考 39,000–45,000 元。115 簡章引用 114 表：管理 27,000＋12,000＝39,000；資管 28,000＋17,000＝45,000。",
    "src": "https://enroll.nuu.edu.tw/var/file/65/1065/attach/15/pta_76237_4431663_47936.pdf"
  }, firstYear=dict(kind='mostly'),
  aid=dict(sure='第 1 學年學費減免（不是全部學雜費），學費減免沒有名額上限。', review='生活獎學金學士每月 6,000（每年 9 個月），每年只有 1–10 名。'),
  renew='生活獎學金：學士前學期 65 分、9 學分，操行 80 無小過，20 小時志工。',
  lang='未逐系整理。',
  after='只找到秋季：往年 2 月初–5 月初報名、6 月初放榜。',
  verdict="公立、第一年學費減免不限名額。苗栗可火車通勤但偏遠；目前只核得秋季，一般春季仍待確認。",
  verdictMy="အစိုးရ၊ ပထမနှစ် ကျောင်းလခ လျှော့ (အကန့်အသတ်မရှိ)။ မြောင်လီ၊ ရထားဖြင့် သွားနိုင်။ ဆောင်းဦး အတည်ပြုပြီး၊ နွေဦး မသေချာသေး။",
  checked="2026-10-05",
  bizAdmits=[],
  bizAdmitsNote="官方錄取公告連結回應錯誤，尚未取得可分系計數的學士榜單。",),
'1035': dict(tier='C', place='台中北區・市中心', travel='市區 10 分',
  fee=dict(kind='free', amount=0, text='115 簡章：免報名費', src='https://cmucia.cmu.edu.tw/english/doc/Application_Guidelines115.pdf', year='115'),
  tuition=dict(min=56986, max=144488, year='115', text='一般學系約 56,986；中醫/醫學系 144,488（每學期）', src='https://cmucia.cmu.edu.tw/english/doc/Application_Guidelines115.pdf'),
  firstYear=dict(kind='none'),
  aid=dict(sure=None, review='簡章只列碩博士獎學金，學士沒有。'),
  renew='—', lang='多數學系要 B1，部分 A2；醫學系要 B1（Level 3）或 HSK 5。',
  after='春季只收碩博士。學士只收秋季：往年 11 月下旬–1 月、2 月–4 月兩梯。財力證明美金 5,000。',
  verdict='醫藥大學，學費高、多數系要 B1、學士沒有獎學金、只收秋季。除非他很想讀醫護相關，否則不優先。',
  verdictMy='ဆေးတက္ကသိုလ်။ ကျောင်းလခ များ၊ B1 လို၊ ဘွဲ့ကြို ပညာသင်ဆု မရှိ။ ဦးစားမပေး။',
  checked=CHECKED),
'0051': dict(tier='C', place='台北市中正區', travel='高鐵約 1 小時＋捷運；要搬家',
  fee=dict(kind='free', amount=0, text='115 簡章：申請費免收', src='https://mplngt.ntub.edu.tw/p/406-1040-107904,r551.php?Lang=zh-tw', year='115'),
  tuition={
    "min": 43040,
    "max": 51560,
    "year": "114",
    "text": "每學期學費＋雜費參考 43,040–51,560 元。115 簡章引用 114 表；商類 43,040。",
    "src": "https://admis.ntub.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9Mell4TDNCMFlWODVPVEU1TTE4ek9UQTROVGt3WHpRd016RTBMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKVWOKNP44XTKKDGLK54TXXS30WSMK20B0YSGCLPJDWSTSNKROGHPO50HGFGOKVWPOTT15A404FCLOFC30EG1034B0NOWSIH35VSTWLKMKXWTWCCTSB550SSPOA5YX00JCWWHGVWKOLOWSSTEGQKWSQPUXYXA0KP3030B0QOOKLKFCICCC210544EG35YWQO14MKYSWS2404NPVXRLPKOKLKROWXFGQO54DGDCSSLKTTXX04EG30GDTW30HG25SSQKCCICIHA1DGCCNKFCYWA4YS10NKXXWW00ZXZX20XSFC14RKDGSW3534MOUSMK00VXNODCNKTSZSTWB0DCXSGHRK44CCID20XWEGXWTW14GDA1PK34SWYSGG35LOQPA0QOJGA020TSSTB0NPCCA5KKB0FGQKCHZS30LOGCQOROB1MOQPIDLKB0A0B414A0&cg=631"
  }, firstYear=dict(kind='review'),
  aid=dict(sure=None, review='每學期 15,000 元（不是每月），要申請並審查。'),
  renew='學士前學期平均 75 以上、操行 80 以上。',
  lang='學士 A2（依系所表）。財力證明美金 3,000。',
  after='只找到秋季：往年 1 月–5 月初報名、6 月初放榜。',
  verdict="免申請費、A2，但在台北，獎學金較少。目前只核得秋季學士；一般春季是否招生尚未確認。",
  verdictMy="တိုင်ပေ၊ ပညာသင်ဆု နည်း။ ဆောင်းဦး ဘွဲ့ကြို အတည်ပြုပြီး၊ နွေဦး မသေချာသေး။",
  checked="2026-10-05",
  bizAdmits=[],
  bizAdmitsNote="官方外國學生招生頁可讀，尚未核得近兩年可分系計數的一般學士榜單。",),
'0031': dict(tier='C', place='宜蘭市', travel='要搬家',
  fee={
    "kind": "silent",
    "text": "已成功讀取 115 簡章全文；未找到申請費或明文免收說明，不能當免費。",
    "src": "https://isa.niu.edu.tw/var/file/73/1073/img/115-regulations-for-academic.pdf",
    "year": "115"
  },
  tuition={
    "min": 38600,
    "max": 49500,
    "year": "115",
    "text": "每學期學費＋雜費參考 38,600–49,500 元。115 簡章估值；管理 38,600。",
    "src": "https://isa.niu.edu.tw/var/file/73/1073/img/115-regulations-for-academic.pdf"
  }, firstYear={
    "kind": "review"
  },
  aid={
    "sure": None,
    "review": "報名時勾選申請。115 簡章列新生第一學年學雜費半額減免，優秀者可審查全免及每月 4,000 津貼；整體名額與項目依年度預算，不先當作一定有。不得同領臺灣或其他政府獎學金。",
    "src": "https://isa.niu.edu.tw/var/file/73/1073/img/115-regulations-for-academic.pdf",
    "year": "115"
  },
  renew="學士最多 8 學期；新生核給 1 學年，第三學期起每學期重申請，以前一學期成績與各項表現由學院審查。115 簡章沒有列統一分數門檻，辦法連結仍無法讀取，尚未核得。", lang='至少 TOCFL A2。',
  after='春季只收研究所。學士秋季往年 12 月開始。', verdict='遠、春季不收學士。', verdictMy='ဝေးသည်၊ နွေဦး ဘွဲ့ကြို မလက်ခံ။', checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "應用經濟與管理學系（第1梯）",
      "count": 2,
      "year": "115",
      "term": "fall",
      "src": "https://isa.niu.edu.tw/p/404-1073-70986.php",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    }
  ],
  renewSource={
    "src": "https://isa.niu.edu.tw/var/file/73/1073/img/115-regulations-for-academic.pdf",
    "year": "115"
  },),
'0018': dict(tier='C', place='嘉義市', travel='高鐵/火車約 1 小時；要搬家',
  fee=dict(kind='free', amount=0, text='115 簡章明載免收申請費，至多申請 3 系', src='https://www.ncyu.edu.tw/oia_eng/ServerFile/Get/786060ff-e628-4e3e-9dc1-35afcc76b7c6?nodeId=60284&sId=237992', year='115'),
  tuition={
    "min": 47407,
    "max": 55463,
    "year": "115",
    "text": "每學期學費＋雜費參考 47,407–55,463 元。文教 47,407，商 48,128，理工／資管 55,463。",
    "src": "https://www.ncyu.edu.tw/oia_eng/ServerFile/Get/786060ff-e628-4e3e-9dc1-35afcc76b7c6?nodeId=60284&sId=237992"
  }, firstYear=dict(kind='review'),
  aid=dict(sure=None, review='新生第一年學雜費比照本國生收費（申請入學時提出）；不是免學費。'),
  renew='第二年起每年申請：班排前 50% 學雜費比照本國生；51–70% 只有學費比照。',
  lang='未逐系整理。', after="115 往年秋季第一梯 1/1–3/1 報名、5/18 放榜、6/5 前寄通知。116 未公告；第二梯 7/10 放榜未列入。",
  verdict='公立、免申請費、可報 3 系，但要搬到嘉義。', verdictMy='အစိုးရ၊ ကြေးအခမဲ့၊ ဌာန ၃ ခု လျှောက်နိုင်၊ ချားယီ — အိမ်ပြောင်းရ။', checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "行銷與觀光管理學系（第1梯）",
      "count": 1,
      "year": "115",
      "term": "fall",
      "src": "https://www.ncyu.edu.tw/oia/Subject/Detail/239647?nodeId=58425",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "行銷與觀光管理學系（第1梯）",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://www.ncyu.edu.tw/oia/ServerFile/Get/4d3dda85-a5d6-4df4-a5d4-9dae496e6bf8?nodeId=58425&sId=222092",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    }
  ],),
'0036': dict(tier='C', place='台南市', travel='要搬家',
  fee={
    "kind": "silent",
    "text": "已重讀 115 簡章；未找到申請費或明文免收的說明，不能當免費。",
    "src": "https://campus.nutn.edu.tw/newsPost3/postFiles/101347_Admissions%20Guide%20for%20International%20Students%20for%20the%20115th%20Academic%20Year.pdf",
    "year": "115"
  },
  tuition={
    "min": 45691,
    "max": 53183,
    "year": "115",
    "text": "每學期學費＋雜費參考 45,691–53,183 元。一般管理 46,091；依學院收費。",
    "src": "https://campus.nutn.edu.tw/newsPost3/postFiles/101347_Admissions%20Guide%20for%20International%20Students%20for%20the%20115th%20Academic%20Year.pdf"
  }, firstYear=dict(kind='review'),
  aid=dict(sure=None, review='全免類含免費宿舍；「減半」類其實是比照本國生收費；審查。'),
  renew='學士前學年平均 70，必修全過。', lang='未逐系整理。',
  after='春季只收研究所。', verdict='遠、春季不收學士。', verdictMy='ဝေးသည်၊ နွေဦး ဘွဲ့ကြို မလက်ခံ။', checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "經營與管理學系",
      "count": 7,
      "year": "115",
      "term": "fall",
      "src": "https://campus.nutn.edu.tw/newspost3/readPost.aspx?boardNo=103748",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    }
  ],),
'0047': dict(tier='C', place='高雄小港', travel='要搬家',
  fee={
    "kind": "silent",
    "text": "已重讀 115 簡章；未找到申請費或明文免收的說明，不能當免費。",
    "src": "https://international.nkuht.edu.tw/var/file/45/1045/img/749130689.pdf",
    "year": "115"
  },
  tuition={
    "min": 45961,
    "max": 45961,
    "year": "115",
    "text": "每學期學費＋雜費參考 45,961–45,961 元。日間四年制學士；制服、材料、住宿等另計。",
    "src": "https://international.nkuht.edu.tw/var/file/45/1045/img/749130689.pdf"
  }, firstYear=dict(kind='review'),
  aid=dict(sure=None, review='學士：學雜費全免／半免或宿舍全免，擇優審查。'),
  renew='第二年起每學期申請；成績與操行 80、前 50%；服務 15–25 小時。', lang='未逐系整理。',
  after='116-1 秋季已公告 2026/11/2–12/17 報名；放榜往年約 3 月。',
  verdict='餐旅專業強，116-1 秋季日期已公告，但在高雄要搬家。', verdictMy='ဟိုတယ်/စားသောက် ပညာ ကောင်း၊ ကောင်ရှုံး — အိမ်ပြောင်းရ။', checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "國際觀光學士學位學程（英語授課）（第2梯）",
      "count": 12,
      "year": "115",
      "term": "fall",
      "src": "https://international.nkuht.edu.tw/p/404-1045-21221.php?Lang=en",
      "basis": "學士第 2 梯正取；原表第 72–83 號，84 號起備取不計",
      "round": 2
    }
  ],
  bizAdmitsNote="本次先核得 115 秋季第 2 梯國際觀光學程 12 名正取；未將備取或烹飪學程計入，其他餐旅系仍待分系核對。",),
'0024': dict(tier='C', place='屏東內埔', travel='要搬家',
  fee=dict(kind='free', amount=0, text='官網招生頁明載免申請費', src='https://oia2.npust.edu.tw/zh/future-students/', year='官網常態'),
  tuition={
    "min": 44030,
    "max": 48540,
    "year": "115",
    "text": "每學期學費＋雜費參考 44,030–48,540 元。管理類 44,030；依學院收費。",
    "src": "https://oia2.npust.edu.tw/zh/wp-content/uploads/sites/2/2025/11/115學年度屏東科技大學招生簡章-中英文版-new-20260105.pdf"
  }, firstYear={
    "kind": "none"
  },
  aid={
    "sure": None,
    "review": "一般商管學士原則從二年級起申請學雜費或宿舍減免；一年級僅特殊情形另審。115 簡章另列熱帶農業學程新生獎學金，不能套給商管系。",
    "src": "https://oia2.npust.edu.tw/zh/wp-content/uploads/sites/2/2025/11/115學年度屏東科技大學招生簡章-中英文版-new-20260105.pdf",
    "year": "115"
  },
  renew="二年級起每年 7/1–7/31 申請；前一學年平均至少 75、操行至少 80，交全年成績單及 2 封推薦函。服務項目與時數另協調，服務成果列入次年審查；已有其他獎學金不得申請。此為 111 修正、115 招生頁仍連結的辦法，當年期限再核對公告。", lang='未逐系整理。',
  after="115 春季系所表僅研究所。秋季以 115 往年 1/1–3/31 報名、6/15 放榜作參考；116 尚未公告。",
  verdict='最遠，而且學士第一年通常沒有減免。', verdictMy='အဝေးဆုံး၊ ပထမနှစ် လျှော့ပေးမှု မရှိသလောက်။', checked="2026-10-05",
  renewSource={
    "src": "https://oia2.npust.edu.tw/zh/wp-content/uploads/sites/2/2023/10/國立屏東科技大學外國學生就學獎助學金辦法20220505修.pdf",
    "year": "115招生頁引用（111/5/5修訂）"
  },
  bizAdmits=[],
  bizAdmitsNote="已讀 115 簡章，尚未核得近兩年可分系計數的一般商管學士榜單。",),
}


# ---- 中字輩學校（2026-09-29 新增） ----
S['0009'] = dict(tier='P', place='高雄西子灣', travel='高鐵到左營再轉車約 1 小時半；要搬家',
  fee=dict(kind='free', amount=0, text='官方外國學位生 FAQ Q8：不收申請費', src='https://oia.nsysu.edu.tw/p/412-1308-20574.php?Lang=en', year='現行FAQ'),
  tuition=dict(min=49460, max=62080, year='115', text='每學期 49,460–62,080（依學院）；宿舍約 36,600／學年', src='https://rpb78.nsysu.edu.tw/static/file/239/1239/img/409586988.pdf'),
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='報名時可一併申請中山獎學金：學士每月 6,000 元，依預算審核。'),
  renew='學士每次 1 年，續申請要至少 9 學分、平均 70 分（GPA 2.44）、無不良紀錄；工作居留或全職工作者排除。',
  lang='依系；例如中文系要 TOCFL 4 級或 HSK 6 級。財力證明 US$4,000 或 NT$12 萬。',
  after='春季簡章只看到碩博士（學士班沒列在春季表），學士只能報秋季。往年秋季 1/15–3/15 報名、6 月初放榜、6/20 前發入學許可。',
  verdict='南部名校、免申請費、每月 6,000 獎學金，但在高雄要搬家，春季不收學士。',
  verdictMy='တောင်ပိုင်း နာမည်ကြီး၊ လျှောက်လွှာကြေး အခမဲ့၊ တစ်လ NT$6,000 ပညာသင်ဆု။ ကောင်ရှုံး — အိမ်ပြောင်းရ၊ နွေဦး ဘွဲ့ကြို မရ။',
  checked="2026-10-05",
  bizAdmits=[],
  bizAdmitsNote="114 秋季官方公告改由申請系統查個別結果，沒有可直接分系計數的榜單；尚未核得其他公開名單。",)
S['0008'] = dict(tier='P', place='桃園中壢', travel='高鐵到桃園再轉車約 1 小時半；要搬家',
  fee=dict(kind='free', amount=0, text='115-1 與 115-2 簡章都明載無須繳申請費', src='https://drive.google.com/uc?export=download&id=1YPMGlysvNc8ydZTcXqOA-4CMqi1xhhVM', year='115'),
  tuition=None, firstYear=dict(kind='review'),
  aid=dict(sure=None, review='每月上限：學士 9,000、碩士 15,000、博士 40,000；可申請學費／學分費減免，雜費仍要自付；上限不保證核給。'),
  renew='在校學士累積平均 60 分，修過 1 門本校華語課或有中文溝通證明（秋季新生第 1 年下學期免）。',
  lang='未逐系整理。',
  after='學士只收秋季；春季只有研究所。往年秋季 1–3 月報名、5 月中放榜。',
  verdict='國立名校、免申請費，獎學金學士每月最高 9,000。在桃園要搬家，春季不收學士。',
  verdictMy='နာမည်ကြီး အစိုးရ၊ ကြေးအခမဲ့၊ ပညာသင်ဆု တစ်လ NT$9,000 အထိ။ တောင်ယွမ် — အိမ်ပြောင်းရ။',
  checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "經濟學系",
      "count": 1,
      "year": "115",
      "term": "fall",
      "src": "https://drive.google.com/uc?export=download&id=1ac6PbCacQVggjciQvKFcX6aA2u7Z1h3a",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    }
  ],
  bizAdmitsNote="115 秋季正取名單的管理學院只有經濟學系 1 筆學士；研究所不計。",)
S['0013'] = dict(tier='B', place='嘉義民雄', travel='高鐵/火車約 1 小時；要搬家',
  fee={
    "kind": "silent",
    "text": "已讀 115 簡章全文；未找到申請費或明文免收的說明，不能當免費。",
    "src": "https://oia.ccu.edu.tw/var/file/8/1008/img/814/372680683.pdf",
    "year": "115"
  },
  tuition={
    "min": 48254,
    "max": 55290,
    "year": "115",
    "text": "每學期學費＋雜費參考 48,254–55,290 元。管理 49,259，資管 54,285；依學院收費。",
    "src": "https://oia.ccu.edu.tw/var/file/8/1008/img/814/372680683.pdf"
  }, firstYear=dict(kind='review'),
  aid=dict(sure=None, review='可核給部分或全額學費、學分費、雜費及宿舍減免與生活津貼，依學院決定，新生隨入學申請。'),
  renew='學士至少 8 學分、平均超過 65 分且品行良好；依審查。', lang='未核得。',
  after='學士只收秋季；春季只有研究所。往年秋季 1–3 月報名、4 月下旬放榜。',
  readYourself=[dict(label='中正 115 簡章 PDF', url='https://oia.ccu.edu.tw/var/file/8/1008/img/814/372680683.pdf', why='看申請費與語言門檻')],
  verdict='國立、往年 4 月下旬放榜較早，但要搬到嘉義，申請費沒讀到。',
  verdictMy='အစိုးရ၊ ရလဒ် စောစော (ဧပြီ)။ ချားယီ — အိမ်ပြောင်းရ။', checked="2026-10-05",
  bizAdmits=[
    {
      "dept": "經濟學系（第1梯）",
      "count": 2,
      "year": "115",
      "term": "fall",
      "src": "https://oia.ccu.edu.tw/p/406-1008-89101,r1716.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "企業管理學系（第1梯）",
      "count": 1,
      "year": "115",
      "term": "fall",
      "src": "https://oia.ccu.edu.tw/p/406-1008-89101,r1716.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "資訊管理學系（第1梯）",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://oia.ccu.edu.tw/p/406-1008-72653,r1716.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 1
    },
    {
      "dept": "企業管理學系（第2梯）",
      "count": 2,
      "year": "114",
      "term": "fall",
      "src": "https://oia.ccu.edu.tw/p/406-1008-73801,r1716.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    },
    {
      "dept": "經濟學系（第2梯）",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://oia.ccu.edu.tw/p/406-1008-73801,r1716.php?Lang=en",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部",
      "round": 2
    }
  ],)
S['1004'] = dict(tier='B', place='桃園中壢', travel='高鐵到桃園再轉車約 1 小時半；要搬家',
  fee=dict(kind='free', amount=0, text='116 簡章第 4 頁：不需申請費', src='https://oia.cycu.edu.tw/wp-content/uploads/116學年度【外國學生】申請入學招生簡章-2.pdf', year='116'),
  tuition=dict(min=58000, max=74000, year='116', text='每學期 58,000–74,000（依學程）；宿舍 15,000＋冷氣 1,500／學期', src='https://oia.cycu.edu.tw/wp-content/uploads/116學年度【外國學生】申請入學招生簡章-2.pdf'),
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='新生擇一：全額學費、半額學費，或 NT$16,000 生活補助（審查）。'),
  renew='班排前 25% 可再申請，附成績單。',
  lang='學士報名時就要 TOCFL B1，入學後要達 B2。他現在 A2，11 月考到 B1 才能報。財力證明 NT$12 萬或 US$4,000。',
  after='116-1 已公告：第 1 梯 2026/12/1–2027/3/1，4/23 放榜，5 月中發入學許可；第 2 梯 3/15–5/31，6/21 放榜，6 月下旬發許可。春季只收研究所。',
  verdict='116-1 日期已正式公告，第 1 梯 4/23 放榜很早。但要 B1 才能報，而且學費是名單裡最貴的一群（每學期 5.8–7.4 萬）。',
  verdictMy='116-1 ရက်စွဲ တရားဝင်။ B1 လိုသည် (သူ့မှာ A2)။ ကျောင်းလခ ကြီးသည်။', checked=CHECKED)
S['1006'] = dict(tier='B', place='台北陽明山', travel='高鐵約 1 小時＋轉車；要搬家',
  fee=dict(kind='unknown', text='簡章讀不到', src='https://ap2.pccu.edu.tw/enroll/exampublic/50/', year='—'),
  tuition=None, firstYear=dict(kind='unknown'), aid=dict(sure=None, review='官網有境外學生獎助學金頁，請自己看。'),
  renew='未核得。', lang='未核得。', after='只有往年參考：秋季約 6 月下旬截止、7 月下旬放榜（放榜晚於 ARC 到期）。',
  readYourself=[dict(label='文化大學外國學生招生', url='https://ap2.pccu.edu.tw/enroll/exampublic/50/', why='看簡章、申請費、日期'), dict(label='文化大學境外學生獎助學金', url='https://oima.pccu.edu.tw/%E4%B8%AD%E5%9C%8B%E6%96%87%E5%8C%96%E5%A4%A7%E5%AD%B8%E5%90%84%E9%A0%85%E7%8D%8E%E5%8A%A9%E5%AD%B8%E9%87%91%E9%81%A9%E7%94%A8%E5%A2%83%E5%A4%96%E5%AD%B8%E7%94%9F/', why='看新生獎學金')],
  verdict='往年放榜太晚，趕不上 ARC；資料要自己看。', verdictMy='ရလဒ် နောက်ကျ — ARC မမီ။', checked=CHECKED)
S['1011'] = dict(tier='B', place='新竹市', travel='高鐵約 30 分＋轉車；要搬家',
  fee=dict(kind='unknown', text='招生頁沒列申請費', src='https://admission.chu.edu.tw/p/412-1047-664.php?Lang=zh-tw', year='—'),
  tuition=None, firstYear=dict(kind='unknown'), aid=dict(sure=None, review='獎學金頁面沒有寫金額，請自己看。'),
  renew='未核得。', lang='中文授課 TOCFL A2；財力證明 US$4,000。',
  after='只有往年參考：第 1 梯約 2–4 月報名、5 月放榜；第 2 梯 5–7 月報名、7 月下旬放榜（來不及）。',
  readYourself=[dict(label='中華大學外國學生申請入學', url='https://admission.chu.edu.tw/p/412-1047-664.php?Lang=zh-tw', why='看簡章、申請費、獎學金'), dict(label='線上報名系統', url='https://exam2.chu.edu.tw/', why='今年梯次')],
  verdict='A2 可報，第 1 梯往年 5 月放榜趕得上，資料要自己看。', verdictMy='A2 ရ၊ အဆင့် ၁ မေလ ရလဒ်။', checked=CHECKED)
S['1061'] = dict(tier='B', place='台北南港', travel='高鐵約 1 小時＋捷運；要搬家',
  fee=dict(kind='unknown', text='招生頁沒列申請費', src='https://www.cust.edu.tw/enroll/international-2.html', year='115-2'),
  tuition=None, firstYear=dict(kind='unknown'), aid=dict(sure=None, review='未核得。'), renew='未核得。', lang='見簡章第 3 頁。',
  after='春季 2026/11/2–12/15 報名，2027 年 1 月放榜（日期未定）。招生四技與碩士。',
  readYourself=[dict(label='中華科大國際生招生（含簡章）', url='https://www.cust.edu.tw/enroll/international-2.html', why='看申請費、學費、獎學金、可報系所')],
  verdict='春季 11/2 才開始報名，資料要自己看，要搬到台北。', verdictMy='နွေဦး 11/2–12/15။ ကိုယ်တိုင်ကြည့်ပါ။', checked=CHECKED)
for sid, place, note in [('1046','台北／新竹','中國科大'),('1052','台南','中信科大'),('1055','台南','中華醫大'),('1125','台南','中信金融')]:
    S[sid] = dict(tier='C', place=place, travel='要搬家',
      fee=dict(kind='unknown', text='官網沒有查到外國學生簡章', src={'1046':'http://www.cute.edu.tw/','1052':'http://www.feu.edu.tw','1055':'http://www.hwai.edu.tw','1125':'https://www.ctbc.edu.tw/'}[sid], year='—'),
      tuition=None, firstYear=dict(kind='unknown'), aid=dict(sure=None, review='未核得。'), renew='未核得。', lang='未核得。',
      after='沒有查到今年或往年的外國學位生日期。',
      readYourself=[dict(label=note+' 官網', url={'1046':'http://www.cute.edu.tw/','1052':'http://www.feu.edu.tw','1055':'http://www.hwai.edu.tw','1125':'https://www.ctbc.edu.tw/'}[sid], why='找外國學生招生')],
      verdict='資料查不到，而且在外縣市，不優先。', verdictMy='အချက်အလက် မတွေ့ — ဦးစားမပေး။', checked=CHECKED)

# Manual undergrad-round overrides where schools.json mixes scopes or carries
# results that belong to another intake. Values are copied from official sources.
ROUND_OVERRIDE = {
 ('0039','spring'): 'none',
 ('0049','spring'): 'none',
 ('1004','spring'): 'grad',
 ('0008','spring'): 'grad',
 ('0013','spring'): 'grad',
 ('0017','spring'): [dict(start=('official','2026-09-03'), end=('official','2026-10-31'), result=None, note='學士班是否開放春季請以簡章為準；放榜往年約 12 月初')],
 ('0043','spring'): 'none',
 ('1035','spring'): 'grad',
 ('1048','spring'): [dict(start=('official','2026-02-21'), end=('official','2026-11-30'), result=None, note='放榜日請看報名系統公告')],
 ('1001','spring'): [dict(start=('official','2026-10-01'), end=('official','2026-10-31'), result=('official-month','2026-12-01','12 月上旬'), note='文件 11/3 前寄達；1/4 前回覆入學意願')],
 ('1018','spring'): [dict(start=None, end=('official','2026-12-19'), result=None, note='學士/碩士截止；開始日頁面未寫，目前開放中')],
}

# 2026-09-29: user removed non-national 「中」 schools (not the traditional national 中字輩)
for _k in ('1011','1035','1006','1004','1061','1046','1052','1055','1125'):
    S.pop(_k, None)

# ---- 2026-09-29 晚：國立大學／國立科大補齊 ----
# 排除：藝術（北藝、臺藝、南藝、戲曲）、體育（體大、臺體）、醫護（北護）、
# 沒有商管學院的教育大學（北教、高師大、臺東）、外島（金門、澎湖）、專科、市立（北市大）。
# 排除 ARC 來不及：嶺東（唯一查到的秋季梯次 8 月才寄入學通知，春季沒查到）。
for _k in ('0049', '1045'):
    S.pop(_k, None)
COORDS.update({'0001':(24.9870,121.5760),'0002':(24.7960,120.9960),'0003':(25.0170,121.5400),'0004':(25.0260,121.5280),
 '0005':(22.9990,120.2200),'0007':(24.7870,120.9970),'0012':(25.1500,121.7750),'0015':(24.0810,120.5590),
 '0019':(22.7340,120.2830),'0020':(23.8970,121.5410),'0022':(25.0130,121.5410),'0023':(23.6940,120.5340),
 '0033':(23.7020,120.4300),'0052':(22.6680,120.4990),'0053':(22.6510,120.3280)})
# 勤益：第 1 梯公開榜單 7/20，但 5/27 就寄入學通知（入學許可），可趕上 ARC。
ROUND_OVERRIDE[('0043','fall')] = [
 dict(start=('hist','2027-03-21','3 月下旬'), end=('hist','2027-05-01','5 月上旬'), result=('hist','2027-05-27','往年 5/27 寄入學通知（公開榜單 7/20）'), note='第 1 梯：入學通知 5/27 就寄，趕得上 ARC'),
 dict(start=('hist','2027-05-11','5 月中旬'), end=('hist','2027-06-21','6 月下旬'), result=('hist','2027-07-11','7 月中旬'), note='第 2 梯 7 月才放榜，ARC 來不及'),
]

_R = lambda: None
def _e(**k):
    k.setdefault('checked', CHECKED); k.setdefault('tuition', None); return k

S['0015'] = _e(tier='A', place='彰化市', travel='火車台中→彰化約 15 分，再轉公車；可通勤',
  fee=dict(kind='free', amount=0, text='115 簡章明載免繳申請費；最多報 3 個系', src='https://oicaweb.ncue.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelEwTDNCMFlWOHlORE01T1Y4M09UWTJOekF6WHpBeE9ETTVMbkJrWmc9PQ==', year='115'),
  firstYear=dict(kind='full'),
  aid=dict(sure='一般外國學士新生：第一年免學雜費＋校內住宿減免（寒暑假除外），錄取註冊就核定，不用另外申請。', review=None),
  renew='學士只有第一年；第二年起沒有這項減免（研究所才可續領）。',
  lang='TOCFL／英語門檻依系，不是全校統一；報名前要逐系看。財力證明 US$2,500。',
  after='春季 9/18 已截止。往年秋季 12 月上旬–3 月上旬報名、4 月中旬放榜（第 1 梯）；第 2 梯 7 月才放榜，ARC 來不及。',
  verdict="離台中很近，免申請費，第一年學雜費及宿舍錄取註冊後減免。115往年秋季第一梯4月放榜；116時程未公告。",
  verdictMy='ထိုင်ချုံးနှင့် နီး၊ အစိုးရ၊ လျှောက်လွှာကြေး အခမဲ့၊ ပထမနှစ် ကျောင်းလခ+အဆောင် အခမဲ့ (အလိုအလျောက်)။ ဆောင်းဦး ပထမအကြိမ် ဧပြီ ရလဒ်။',
  checked="2026-10-05",
  tuition={
    "min": 46936,
    "max": 54031,
    "year": "114",
    "text": "每學期學費＋雜費參考 46,936–54,031 元。一般管理 47,491；依學院收費。",
    "src": "https://oicaweb.ncue.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelEwTDNCMFlWOHlORE01T1Y4M09UWTJOekF6WHpBeE9ETTVMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKVWOKWW44FD00TSJCKPWWZSPKGDYWOPB035XSNPZTDCCCKPFGFDSW3410KLSSSSWWGDLPDG2441XTWW14MOKKDGRKQLXW00JDML50WSEC3050PKKKB5A0WWPONPZXEDNONO24ZSB4SSICSTEGGGMK44UXUTFGSW30ZS01YSCCJGROVWWWMPYXNOLKNP34DCJGMK2520FCXSXSVXVXHGB5ZWB050POYSSSUWB0YWPOOOZXIGLKNKXTZSPKWWKKOPQKXSGCGGRLWWCCROFCYWPOLO10JCOKSS00YTLPFGHGLKGDUSJG30HCECICMOHCMLXTDCA0LKA4B4ECFH10UWFC4440QLKKFGLKEGWSPKB0QLQL"
  },
  bizAdmits=[
    {
      "dept": "企業管理學系（第1梯）",
      "count": 1,
      "year": "115",
      "term": "fall",
      "src": "https://oicaweb.ncue.edu.tw/p/406-1019-33396%2Cr676.php?Lang=zh-tw",
      "basis": "一般學士正取；原掃描榜單已核對，研究所與國際專修部不計",
      "round": 1
    },
    {
      "dept": "企業管理學系（第1梯）",
      "count": 2,
      "year": "114",
      "term": "fall",
      "src": "https://oicaweb.ncue.edu.tw/p/406-1019-30176%2Cr142.php?Lang=zh-tw",
      "basis": "一般學士正取；原掃描榜單已核對，研究所與國際專修部不計",
      "round": 1
    },
    {
      "dept": "資訊管理學系（資訊管理組）（第1梯）",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://oicaweb.ncue.edu.tw/p/406-1019-30176%2Cr142.php?Lang=zh-tw",
      "basis": "一般學士正取；原掃描榜單已核對，研究所與國際專修部不計",
      "round": 1
    }
  ],
  bizAdmitsNote="115／114 秋季第 1 梯，掃描榜單已逐列及原圖核對；不含國際專修部。",)

S['0003'] = _e(tier='P', place='台北公館', travel='高鐵約 1 小時＋捷運；要搬家',
  fee=dict(kind='paid', amount=2000, text='每系 NT$2,000（US$80），第 3 系起每系 1,500；最多 5 系', src='https://admissions.ntu.edu.tw/wp-content/uploads/116-1Admission-Guidelines-for-Intl-Degree-Students_ENG-1.pdf', year='116-1'),
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='報名時勾選國際學位生獎學金：每學期學雜費減免上限 10 萬＋每月 8,000，審核核給。'),
  renew='每學年平均 GPA 3.38 以上才續領。',
  lang='依系；多數中文授課系要求高，報名前逐系看。',
  after='2027 秋季（116-1）第 1 梯 9/29–11/5 報名、1/14 放榜；第 2 梯 12/1–1/19 報名、4/8 放榜。春季只收研究所。',
  verdict='台灣第一名校，秋季第 1 梯 1 月就放榜。每系 2,000 元，錄取難度最高。',
  verdictMy='ထိုင်ဝမ် နံပါတ် ၁ ကျောင်း၊ ဇန်နဝါရီ ရလဒ်။ ဌာနတစ်ခု NT$2,000၊ အခက်ဆုံး။',
  checked="2026-10-05",
  tuition={
    "min": 50460,
    "max": 79120,
    "year": "115",
    "text": "每學期學費＋雜費參考 50,460–79,120 元。116 簡章引用 2026/27（115）表；管理 51,220。",
    "src": "https://admissions.ntu.edu.tw/wp-content/uploads/116-1Admission-Guidelines-for-Intl-Degree-Students_ENG-1.pdf"
  },
  bizAdmits=[],
  bizAdmitsNote="尚未核得近兩年可分系計數的外國學士公開榜單；不由個別查詢結果或招生名額推算。",)
S['0001'] = _e(tier='P', place='台北文山木柵', travel='高鐵約 1 小時＋捷運／公車；要搬家',
  fee=dict(kind='paid', amount=1600, text='每件 NT$1,600（US$60），逐件收、不退', src='https://drive.google.com/uc?export=download&id=1RC6EOaByXy7hqe6_2ddinrZZk64UGu3k', year='116-1'),
  firstYear={
    "kind": "review"
  },
  aid={
    "sure": None,
    "review": "兩項都由錄取系院推薦審查，不能自行保證取得。116 簡章列新生學雜費減免；另有全額獎學金免學雜費＋每學年總補助 15 萬元，或半額獎學金只免學雜費。依 115 公告，15 萬含每月 1 萬及機票每年最高 3 萬、實報實銷。",
    "src": "https://drive.google.com/uc?export=download&id=1RC6EOaByXy7hqe6_2ddinrZZk64UGu3k",
    "year": "116",
    "sources": [
      {
        "src": "https://oic.nccu.edu.tw/Post/15947",
        "year": "115"
      }
    ]
  },
  renew="115 獲獎公告：學士最多 4 年，成績至少 75，系院可訂更高標準；每學期按時完成註冊，不能同領其他全額獎學金。學雜費減免另要求無申誡以上處分；休學、退學或保留學籍取消資格。116 須再核對獲獎通知。",
  lang='依系；商學院多要求中文或英文程度，報名前逐系看。',
  after="116 秋季第1梯 9/22–10/15 報名、11/27 放榜；第2梯完整時程尚未公告，放榜使用 115 往年 5/12 參考，不能當作116正式日期。春季僅研究所。",
  verdict='商管最強的國立大學之一。第 1 梯 10/15 截止、11 月就放榜，但獎學金要學院推薦。',
  verdictMy='စီးပွားရေး အကောင်းဆုံး အစိုးရကျောင်း။ ပထမအကြိမ် 10/15 ပိတ်၊ နိုဝင်ဘာ ရလဒ်။',
  checked="2026-10-05",
  tuition={
    "min": 49020,
    "max": 56860,
    "year": "115",
    "text": "每學期學費＋雜費參考 49,020–56,860 元。116 簡章引用 115 表；商 49,780，資管 56,860。",
    "src": "https://drive.google.com/uc?export=download&id=1RC6EOaByXy7hqe6_2ddinrZZk64UGu3k"
  },
  bizAdmits=[
    {
      "dept": "企業管理學系（第2梯）",
      "count": 12,
      "year": "115",
      "term": "fall",
      "src": "https://oic.nccu.edu.tw/Home/Download?FileId=9598DD47-68B6-4C2B-8096-4CE346645316",
      "basis": "依 Bachelor's 及 Admitted 欄計數，Waiting、研究所與未分商管的學院學程不計",
      "round": 2
    },
    {
      "dept": "金融學系（第2梯）",
      "count": 2,
      "year": "115",
      "term": "fall",
      "src": "https://oic.nccu.edu.tw/Home/Download?FileId=9598DD47-68B6-4C2B-8096-4CE346645316",
      "basis": "依 Bachelor's 及 Admitted 欄計數，Waiting、研究所與未分商管的學院學程不計",
      "round": 2
    },
    {
      "dept": "國際經營與貿易學系（第2梯）",
      "count": 1,
      "year": "115",
      "term": "fall",
      "src": "https://oic.nccu.edu.tw/Home/Download?FileId=9598DD47-68B6-4C2B-8096-4CE346645316",
      "basis": "依 Bachelor's 及 Admitted 欄計數，Waiting、研究所與未分商管的學院學程不計",
      "round": 2
    },
    {
      "dept": "經濟學系（第2梯）",
      "count": 1,
      "year": "115",
      "term": "fall",
      "src": "https://oic.nccu.edu.tw/Home/Download?FileId=9598DD47-68B6-4C2B-8096-4CE346645316",
      "basis": "依 Bachelor's 及 Admitted 欄計數，Waiting、研究所與未分商管的學院學程不計",
      "round": 2
    }
  ],
  bizAdmitsNote="115 秋季第 2 梯一般學士正取，依學位及正取欄逐筆計數；同一人錄取不同系各計一筆，不代表註冊人數。",
  renewSource={
    "src": "https://oic.nccu.edu.tw/Post/15938",
    "year": "115",
    "sources": [
      {
        "src": "https://oic.nccu.edu.tw/Post/15947",
        "year": "115"
      }
    ]
  },)
S['0002'] = _e(tier='P', place='新竹東區', travel='高鐵新竹約 30 分＋公車；要搬家',
  fee=dict(kind='free', amount=0, text='緬甸屬聯合國 LDC，簡章明文 LDC 國籍免申請費（其他國籍 1–2 系 NT$2,000）', src='https://oga.site.nthu.edu.tw/var/file/524/1524/img/4520/140282968.pdf', year='115-2'),
  firstYear={
    "kind": "review"
  },
  aid={
    "sure": None,
    "review": "報名時勾選申請。115 簡章有兩種學士獎：A 類全免學雜／學分費＋每月 5,000；B 類只全免學雜／學分費。名額與種類須審查，住宿、保險等另付，工作簽證或工作居留者不得領。",
    "src": "https://oga.site.nthu.edu.tw/var/file/524/1524/img/4520/471347603.pdf",
    "year": "115"
  },
  renew="學士最多 4 年，每學年申請、每次核給 1 年；未達當年度校方公布的成績標準，隔年停領。現行辦法沒有固定 GPA 門檻，當年度學士審查門檻及申請時間尚未核得；研究所 GPA 不套給學士。",
  lang='依系；報名前逐系看。',
  after='2027 春季學士 8/3–9/30 報名、12/1 放榜。往年秋季學士 11 月下旬–1 月下旬報名、4 月下旬放榜。',
  readYourself=[dict(label='清華 115-2 簡章 PDF', url='https://oga.site.nthu.edu.tw/var/file/524/1524/img/4520/140282968.pdf', why='確認 LDC 免費名單與 A2 可報的系')],
  verdict="頂尖國立，緬甸國籍免申請費。115 春季學士 9/30 已截止、12/1 放榜；下一次秋季申請待116公告。",
  verdictMy='ထိပ်တန်း အစိုးရ၊ မြန်မာနိုင်ငံသား လျှောက်လွှာကြေး အခမဲ့ (LDC)။ နွေဦး 9/30 ပိတ်။',
  checked="2026-10-05",
  tuition={
    "min": 46100,
    "max": 53200,
    "year": "114",
    "text": "每學期學費＋雜費參考 46,100–53,200 元。115 簡章引用 114 表；科技管理 46,100。",
    "src": "https://oga.site.nthu.edu.tw/var/file/524/1524/img/4520/471347603.pdf"
  },
  renewSource={
    "src": "https://oga.site.nthu.edu.tw/var/file/524/1524/img/4339/320629346.pdf",
    "year": "115招生頁引用（2025/4/18修訂）"
  },
  bizAdmits=[],
  bizAdmitsNote="114 秋季公開公告只有整體錄取資訊，未按學系列出人數；無法填成商管各系人數。",)
S['0005'] = _e(tier='P', place='台南東區', travel='高鐵台南約 45 分＋接駁；要搬家',
  fee=dict(kind='paid', amount=2000, text='一次 NT$2,000，最多 3 系，不退', src='https://oia.ncku.edu.tw/var/file/32/1032/img/5041/NCKUAdmissionProspectusforInternationalStudentsFall2026Spring2027v5-3.pdf', year='115'),
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='優秀國際學生獎助學金（115 起學士免學費），第一年隨入學文件審查，不另填表，但不是人人有。'),
  renew='第 2 年起依學院規則申請。',
  lang='依系。',
  after='春季只收研究所。往年秋季 12 月中旬–3 月中旬報名、6 月上旬放榜。',
  verdict='南部第一名校，2,000 元報 3 系很划算；6 月上旬放榜，離 ARC 到期不遠。',
  verdictMy='တောင်ပိုင်း နံပါတ်၁၊ NT$2,000 ဖြင့် ဌာန ၃ ခု။ ဇွန်လ အစ ရလဒ် — ARC နှင့် နီး။',
  checked="2026-10-05",
  tuition={
    "min": 45071,
    "max": 71891,
    "year": "114",
    "text": "每學期學費＋雜費參考 45,071–71,891 元。115 簡章引用 114 表；商管 45,851。",
    "src": "https://oia.ncku.edu.tw/var/file/32/1032/img/5041/NCKUAdmissionProspectusforInternationalStudentsFall2026Spring2027v5-3.pdf"
  },
  bizAdmits=[
    {
      "dept": "企業管理學系",
      "count": 3,
      "year": "114",
      "term": "fall",
      "src": "https://oia.ncku.edu.tw/p/404-1032-283207.php?Lang=zh-tw",
      "basis": "一般學士正取；工業與資訊管理、統計屬管理學院"
    },
    {
      "dept": "工業與資訊管理學系",
      "count": 2,
      "year": "114",
      "term": "fall",
      "src": "https://oia.ncku.edu.tw/p/404-1032-283207.php?Lang=zh-tw",
      "basis": "一般學士正取；工業與資訊管理、統計屬管理學院"
    },
    {
      "dept": "統計學系",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://oia.ncku.edu.tw/p/404-1032-283207.php?Lang=zh-tw",
      "basis": "一般學士正取；工業與資訊管理、統計屬管理學院"
    }
  ],
  bizAdmitsNote="114 秋季一般學士正取；工業與資訊管理、統計列在管理學院。未計研究所與候補。",)
S['0007'] = _e(tier='P', place='新竹東區（光復校區）', travel='高鐵新竹約 30 分＋公車；要搬家',
  fee=dict(kind='paid', amount=2000, text='每系 NT$2,000，不退（醫學院等少數單位免收）', src='https://oia.nycu.edu.tw/oia/en/app/artwebsite/view?id=788&module=artwebsite&serno=26969921-df03-4ec7-8ad1-f360e404c507', year='現行'),
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='優秀外國新生獎學金：學雜／學分全免或比照本國生，另可能有生活津貼，委員會依預算核給。'),
  renew='學士 GPA 3.0、操行 A，要修華語課。',
  lang='依系。',
  after='春季只收研究所。往年秋季 12 月中旬–3 月中旬報名、5 月中旬放榜。',
  verdict='理工名校，管理學院也不錯；5 月中放榜。每系 2,000 元。',
  verdictMy='နာမည်ကြီး အစိုးရ၊ မေလ ရလဒ်။ ဌာနတစ်ခု NT$2,000။',
  checked="2026-10-05",
  bizAdmits=[],
  bizAdmitsNote="官方錄取公告連結無法讀取，尚未取得可分系計數的一般學士榜單。",)
S['0004'] = _e(tier='P', place='台北大安', travel='高鐵約 1 小時＋捷運；要搬家',
  fee={
    "kind": "paid",
    "amount": 1200,
    "text": "115 簡章：學士班每系／每組 NT$1,200（US$50）；多系分別繳費，不退費。",
    "src": "https://bds.oia.ntnu.edu.tw/api/v1/ap/dl?id=359001",
    "year": "115"
  },
  firstYear={
    "kind": "review"
  },
  aid={
    "sure": None,
    "review": "報名時勾選申請；系所依分配名額排序，再由招生委員會審查。獲獎學士第一學年每學期免學費與雜費；未獲獎須自付，不能同領政府獎學金。",
    "src": "https://web.ntnu.edu.tw/~elisa.asali/shares/InternationalStudentScholarshipGuideline_CN.pdf",
    "year": "115（115/7/8修正）"
  },
  renew="學士只補第一學年，沒有這項獎學金的第二年續領；博士續領條件不適用學士。",
  lang='依系。',
  after="115 春季 9/14 已截止，11/20 放榜、12/14 寄通知；企管學士只收秋季。秋季以 115 往年學士第2梯 1/12–3/2、暫定 5/4 放榜為參考；116 尚未公告。",
  readYourself=[
    {
      "label": "臺師大115招生簡章",
      "url": "https://bds.oia.ntnu.edu.tw/api/v1/ap/dl?id=359001",
      "why": "每系／組1,200元與學士招生梯次"
    }
  ],
  verdict="台北名校，115 學士每系／組申請費1,200元。第一年學雜費須系所推薦審查，學士只有一年；企管只收秋季。",
  verdictMy="ထိုင်ပေ နာမည်ကြီး။ ဌာနတစ်ခု NT$1,200။ ပထမနှစ် ကျောင်းလခ အခမဲ့ ဖြစ်နိုင် (စစ်ဆေးရွေးချယ်)။ စီးပွားရေးဌာန ဆောင်းဦးသာ။",
  checked="2026-10-05",
  tuition={
    "min": 47180,
    "max": 55200,
    "year": "114",
    "text": "每學期學費＋雜費參考 47,180–55,200 元。115 簡章引用 114 表；企管 54,760。",
    "src": "https://bds.oia.ntnu.edu.tw/api/v1/ap/dl?id=359001"
  },
  renewSource={
    "src": "https://web.ntnu.edu.tw/~elisa.asali/shares/InternationalStudentScholarshipGuideline_CN.pdf",
    "year": "115（115/7/8修正）"
  },
  bizAdmits=[],
  bizAdmitsNote="尚未核得近兩年可分系計數的外國學士公開榜單；未混入一般國內招生或轉學生名單。",)
S['0022'] = _e(tier='P', place='台北大安（公館）', travel='高鐵約 1 小時＋捷運；要搬家',
  fee=dict(kind='paid', amount=1000, text='每系 NT$1,000（US$30）', src='https://admission-r.ntust.edu.tw/p/450-1052-148283%2Cc0.php?Lang=en', year='115'),
  firstYear=dict(kind='none'),
  aid=dict(sure=None, review=None),
  renew='官方公告：學士不提供臺科大獎學金。',
  lang='依系。',
  after='春季只收研究所。往年秋季 1 月上旬–3 月中旬報名、5 月下旬放榜。',
  verdict='科大第一名，但學士沒有學校獎學金，學費全自付。',
  verdictMy='နည်းပညာ နံပါတ်၁၊ ဘွဲ့ကြို ပညာသင်ဆု မရှိ။',
  checked="2026-10-05",
  tuition={
    "min": 48960,
    "max": 55180,
    "year": "114",
    "text": "每學期學費＋雜費參考 48,960–55,180 元。115 春季簡章附錄列 114 學士費用表；僅引用學士欄，研究所學分費未混入。",
    "src": "https://admission-r.ntust.edu.tw/p/450-1052-148283%2Cc0.php?Lang=en"
  },
  bizAdmits=[],
  bizAdmitsNote="尚未核得近兩年可分系計數的一般外國學士榜單；研究所榜單不套用。",)
S['0019'] = _e(tier='B', place='高雄楠梓', travel='高鐵左營約 1 小時＋轉車；要搬家',
  fee=dict(kind='free', amount=0, text='2027 春秋簡章明載報名費免費', src='https://interadmission.nuk.edu.tw/p/412-1063-4996.php?Lang=zh-tw', year='115-2／116-1'),
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='新生一次性部分學雜費補助，約 20–50%，依核定。'),
  renew='在校生每年 3 月申請 5,000–20,000 元（一次），學士至少 6 學分、65 分。',
  lang='中文授課原則 TOCFL A2。',
  after='2027 春季 10/8–11/2 報名、12/17 放榜（正式）。2027 秋季 2/25–4/23 報名、6/15 放榜（正式）。',
  verdict='免申請費、A2 可以、春秋日期都已正式公告；春季 12 月就放榜。缺點是在高雄。',
  verdictMy='လျှောက်လွှာကြေး အခမဲ့၊ A2 ရ၊ နွေဦး 10/8–11/2 လျှောက်၊ 12/17 ရလဒ်။ ကောင်းကျိုးမဲ့ — ကောင်ရှုံး။',
  checked="2026-10-05",
  tuition={
    "min": 46000,
    "max": 54000,
    "year": "115-2／116-1",
    "text": "每學期學費＋雜費參考 46,000–54,000 元。2027 春秋簡章估值；管理 47,000。",
    "src": "https://interadmission.nuk.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemcwTDNCMFlWODVNVE14Tmw4ME9ERTVNRFk0WHpVMk56azJMbkJrWmc9PQ==&fname=0054ROB0RKSSTXHHGGXS54XSYWMOA135OPQKYSGCNP5110A5YSA4YS54WWECTTOKNO00XTZXVSZSMO20FCNKIC20B0FGXSHCUTXT31RONKTSWXA4CCPOKLRKLOPOSSZX04NOFC34TWMO5025PKJCUSYSMLA1LOVSROUSUSQO20SW34XXICWWUTNPIG04A434ZS30LKLKYSMOHGXS00GDLK40KPYWZWA020POVWA0RK44QLXXHCLKJGIGTWMOZTXWQO34B1HGTXNPWSPKNKROQO54WWKKKLOKZTPOUT00DGB0ROGDQOOKOOXS50B0LKB1IHXTXW40LKMKXWVWQOOKCDUSTWPOJDKKA4JCQKSXPKJCDCGC14B0MO104151VSCCYSDCZSDGOOKK1450RKPOHD10GG04A0HCFCOKWTRLWSNOQOHCCC05SSB5OKB0RKEG00SSROUWKK04POPO"
  },
  bizAdmits=[],
  bizAdmitsNote="搜尋取得的 115 名單為僑港澳生或國際專修部，未核得一般外國學士分系榜單，兩種名單均未混算。",)
S['0052'] = _e(tier='B', place='屏東市', travel='高鐵左營＋台鐵約 1 小時半；要搬家',
  fee=dict(kind='free', amount=0, text='2026–2027 簡章第 18 頁「免申請費用／NO APPLICATION FEE」', src='https://oiais.nptu.edu.tw/var/file/90/1090/img/2026-2027AdmissionGuide.pdf', year='115'),
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='學士新生三選一：一學年學雜費同額、或每月 4,000、或一學年住宿費，依核定。'),
  renew='前學年排名前 50%，每次一年、最多 4 年。',
  lang='中文授課至少 CEFR A2（A2 可以）。只收線上申請。',
  after='2027 春季截止 10/15、11/30 放榜（正式）。往年秋季 4 月中旬截止、6 月中旬放榜。',
  verdict='免申請費、A2 可報、春季 10/15 截止 11 月底放榜，最快拿到入學許可的選項之一。缺點是遠。',
  verdictMy='လျှောက်လွှာကြေး အခမဲ့၊ A2 ရ၊ နွေဦး 10/15 ပိတ်၊ 11/30 ရလဒ်။ ဝေး။',
  checked="2026-10-05",
  tuition={
    "min": 45405,
    "max": 54232,
    "year": "115",
    "text": "每學期學費＋雜費參考 45,405–54,232 元。115 簡章估值，含表列學分費；資管資訊類 54,232。",
    "src": "https://oiais.nptu.edu.tw/var/file/90/1090/img/2026-2027AdmissionGuide.pdf"
  },
  bizAdmits=[
    {
      "dept": "休閒事業經營學系",
      "count": 3,
      "year": "114",
      "term": "fall",
      "src": "https://oiais.nptu.edu.tw/var/file/90/1090/img/381103840.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "行銷與流通管理學系",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://oiais.nptu.edu.tw/var/file/90/1090/img/381103840.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "財務金融學系",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://oiais.nptu.edu.tw/var/file/90/1090/img/381103840.pdf",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    }
  ],)
S['0023'] = _e(tier='B', place='雲林斗六', travel='火車台中→斗六約 50 分；可通勤但很累',
  fee=dict(kind='paid', amount=1000, text='NT$1,000（US$40），不退', src='https://aax.yuntech.edu.tw/', year='115'),
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='優秀外籍學生獎學金：學雜／學分費全免、1/2 或 1/4，隨入學申請審查。'),
  renew='每次 1 年，操行 80、各科 75；升 2 年級要 TOCFL A1、升 3 年級要 A2，導師推薦。',
  lang='依系。',
  after='春季只收研究所。往年秋季 3 月上旬–4 月中旬報名、6 月上旬放榜。',
  verdict='離台中不遠的國立科大，管理學院強；6 月上旬放榜，時間偏緊。',
  verdictMy='ထိုင်ချုံးနှင့် မဝေး၊ စီမံခန့်ခွဲမှု ကောင်း။ ဇွန်လ အစ ရလဒ်။',
  checked="2026-10-05",
  tuition={
    "min": 46082,
    "max": 52202,
    "year": "114",
    "text": "每學期學費＋雜費參考 46,082–52,202 元。115 簡章引用 2025 秋季表；商管 46,082，資管與工業工程管理按工類 52,202。",
    "src": "https://aax.yuntech.edu.tw/images/content/%E5%9C%8B%E9%9A%9B%E5%AD%B8%E7%94%9F%E7%94%B3%E8%AB%8B%E5%85%A5%E5%AD%B8/115/2026%E5%B9%B4%E7%A7%8B%E5%AD%A3%E7%8F%AD%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E7%94%B3%E8%AB%8B%E5%85%A5%E5%AD%B8%E7%B0%A1%E7%AB%A0%202026%20Fall%20Application%20Guide%20.pdf"
  },
  bizAdmits=[
    {
      "dept": "國際管理學士學位學程",
      "count": 7,
      "year": "114",
      "term": "fall",
      "src": "https://aax.yuntech.edu.tw/images/content/%E5%9C%8B%E9%9A%9B%E5%AD%B8%E7%94%9F%E7%94%B3%E8%AB%8B%E5%85%A5%E5%AD%B8/114/2025%E5%B9%B4%E7%A7%8B%E5%AD%A3%E7%8F%AD%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E9%8C%84%E5%8F%96%E6%A6%9C%E5%96%AEAdmission%20List.pdf",
      "basis": "一般學士正取；工業工程與管理系屬管理學院"
    },
    {
      "dept": "資訊管理系",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://aax.yuntech.edu.tw/images/content/%E5%9C%8B%E9%9A%9B%E5%AD%B8%E7%94%9F%E7%94%B3%E8%AB%8B%E5%85%A5%E5%AD%B8/114/2025%E5%B9%B4%E7%A7%8B%E5%AD%A3%E7%8F%AD%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E9%8C%84%E5%8F%96%E6%A6%9C%E5%96%AEAdmission%20List.pdf",
      "basis": "一般學士正取；工業工程與管理系屬管理學院"
    },
    {
      "dept": "企業管理系",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://aax.yuntech.edu.tw/images/content/%E5%9C%8B%E9%9A%9B%E5%AD%B8%E7%94%9F%E7%94%B3%E8%AB%8B%E5%85%A5%E5%AD%B8/114/2025%E5%B9%B4%E7%A7%8B%E5%AD%A3%E7%8F%AD%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E9%8C%84%E5%8F%96%E6%A6%9C%E5%96%AEAdmission%20List.pdf",
      "basis": "一般學士正取；工業工程與管理系屬管理學院"
    },
    {
      "dept": "財務金融系",
      "count": 1,
      "year": "114",
      "term": "fall",
      "src": "https://aax.yuntech.edu.tw/images/content/%E5%9C%8B%E9%9A%9B%E5%AD%B8%E7%94%9F%E7%94%B3%E8%AB%8B%E5%85%A5%E5%AD%B8/114/2025%E5%B9%B4%E7%A7%8B%E5%AD%A3%E7%8F%AD%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E9%8C%84%E5%8F%96%E6%A6%9C%E5%96%AEAdmission%20List.pdf",
      "basis": "一般學士正取；工業工程與管理系屬管理學院"
    },
    {
      "dept": "工業工程與管理系",
      "count": 5,
      "year": "114",
      "term": "fall",
      "src": "https://aax.yuntech.edu.tw/images/content/%E5%9C%8B%E9%9A%9B%E5%AD%B8%E7%94%9F%E7%94%B3%E8%AB%8B%E5%85%A5%E5%AD%B8/114/2025%E5%B9%B4%E7%A7%8B%E5%AD%A3%E7%8F%AD%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E9%8C%84%E5%8F%96%E6%A6%9C%E5%96%AEAdmission%20List.pdf",
      "basis": "一般學士正取；工業工程與管理系屬管理學院"
    },
    {
      "dept": "工業工程與管理系",
      "count": 8,
      "year": "113",
      "term": "spring",
      "src": "https://aax.yuntech.edu.tw/images/content/%E5%9C%8B%E9%9A%9B%E5%AD%B8%E7%94%9F%E7%94%B3%E8%AB%8B%E5%85%A5%E5%AD%B8/113/2025%E5%B9%B4%E6%98%A5%E5%AD%A3%E7%8F%AD%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E9%8C%84%E5%8F%96%E6%A6%9C%E5%96%AEAdmission%20List.pdf",
      "basis": "2025 年春季一般學士正取；工業工程與管理系屬管理學院"
    }
  ],
  bizAdmitsNote="114 秋季及 113 春季（2025 年）正取；工業工程與管理系屬管理學院。114 春季榜單只有研究所，未填成學士 0 人。",)
S['0033'] = _e(tier='B', place='雲林虎尾', travel='高鐵雲林站約 25 分＋公車；可通勤但很累',
  fee=dict(kind='paid', amount=1000, text='每人 NT$1,000（US$40），最多 3 系，不退', src='https://enrollstudents.nfu.edu.tw/download/20260310003/27261', year='115-1'),
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='就學獎助金：學費減免或每月津貼，委員會依成績、預算核定，沒有保證金額。'),
  renew='每次一學年；前學年平均 80、操行 80。',
  lang='依系。',
  after='春季學士有沒有開沒查到（只有往年 9–10 月的參考）。往年秋季 4 月上旬–5 月中旬報名、6 月上旬放榜。',
  verdict='國立科大、1,000 元報 3 系；6 月上旬放榜，時間偏緊。',
  verdictMy='အစိုးရ နည်းပညာ၊ NT$1,000 ဖြင့် ဌာန ၃ ခု။ ဇွန်လ အစ ရလဒ်။',
  checked="2026-10-05",
  tuition={
    "min": 47500,
    "max": 52800,
    "year": "114",
    "text": "每學期學費＋雜費參考 47,500–52,800 元。企管、休閒 47,500；工業管理 52,800。",
    "src": "https://enrollstudents.nfu.edu.tw/download/20260310003/27261"
  },
  bizAdmits=[],
  bizAdmitsNote="原榜單頁跳回首頁；另找到 114 春秋官方公告，但新站與附件回應錯誤，尚未取得可計數名單。",)
S['0020'] = _e(tier='C', place='花蓮壽豐', travel='火車台中→花蓮約 4–5 小時；要搬家',
  fee=dict(kind='paid', amount=1200, text='NT$1,200，不退', src='https://oia.ndhu.edu.tw/var/file/27/1027/img/4756/894840940.pdf', year='115'),
  firstYear={
    "kind": "review"
  },
  aid={
    "sure": None,
    "review": "申請入學時在系統勾選「是」，不用另交獎學金文件。學院排序後再審查；可核全額或部分學雜費及每學期 20,000–40,000 元生活津貼，依名額與預算，不保證。",
    "src": "https://rb027.ndhu.edu.tw/var/file/27/1027/img/551962500.pdf",
    "year": "113",
    "sources": [
      {
        "src": "https://oia.ndhu.edu.tw/var/file/27/1027/img/4756/894840940.pdf",
        "year": "115"
      }
    ]
  },
  renew="每學期重新線上申請，學士累計最多 8 學期。需完成註冊、學業及格、無申誡以上處分，不可同領政府獎學金。中文班須有 TOCFL B1 或華語修課證明；英文班須通過 2 門華語課或有 TOCFL A1。115-1 受理 9/7–9/21，之後依當期公告。",
  lang='依系。',
  after="115 春季 9/1–10/31 報名、12/20 放榜，以已讀簡章為準。116 秋季尚未公告，既有往年資料僅作參考。",
  verdict="離台中很遠。可隨入學申請新生獎學金，但須審查；115 春季10/31截止、12/20放榜。",
  verdictMy="ထိုင်ချုံးမှ ဝေးသည်။ ပညာသင်ဆုကို စစ်ဆေးရွေးချယ်ပေးသဖြင့် အာမခံမရှိ။ နွေဦး 10/31 ပိတ်၊ 12/20 ရလဒ်။",
  checked="2026-10-05",
  tuition={
    "min": 48000,
    "max": 55580,
    "year": "114",
    "text": "每學期學費＋雜費參考 48,000–55,580 元。115 簡章引用 114 估值，含表列保險、網路等其他費用。",
    "src": "https://oia.ndhu.edu.tw/var/file/27/1027/img/4756/894840940.pdf"
  },
  renewSource={
    "src": "https://oia.ndhu.edu.tw/p/406-1027-260703,r6457.php?Lang=zh-tw",
    "year": "115-1",
    "sources": [
      {
        "src": "https://oia.ndhu.edu.tw/var/file/27/1027/img/4756/894840940.pdf",
        "year": "115"
      }
    ]
  },
  bizAdmits=[],
  bizAdmitsNote="官方入學結果頁未取得分系的公開學士榜單，不能從個別申請結果或招生名額推算。",)
S['0012'] = _e(tier='C', place='基隆中正區', travel='高鐵台北＋客運約 2 小時；要搬家',
  fee={
    "kind": "unknown",
    "text": "目前已讀到 115 春季研究所簡章；學士秋季適用的申請費規定尚未核得，不能推定免費。",
    "src": "https://oia.ntou.edu.tw/var/file/22/1022/img/1458/2027_Spring_Admissionbrochure_Released_2026Julyedition.pdf",
    "year": "115-2（僅研究所；學士待核）"
  },
  firstYear=dict(kind='review'),
  aid=dict(sure=None, review='學士全額或部分學費減免，隨入學申請交獎學金申請表。'),
  renew='一年一核，續年重新申請。',
  lang='依系。',
  after='簡章明寫學士只收秋季。秋季日期還沒公告，也沒有往年資料。',
  readYourself=[
    {
      "label": "海大招生頁",
      "url": "https://oia.ntou.edu.tw/p/403-1022-974-1.php?Lang=en",
      "why": "秋季簡章公告後看日期與申請費"
    },
    {
      "label": "學士秋季招生規定待確認",
      "url": "https://oia.ntou.edu.tw/p/412-1022-7231.php?Lang=zh-tw",
      "why": "已讀春季研究所簡章，學士秋季申請費與學雜費仍需確認。"
    }
  ],
  verdict='有海運管理，但遠、秋季日期與申請費都不明。',
  verdictMy='ဝေး၊ ရက်စွဲနှင့် ကြေး မသိ။',
  checked="2026-10-05",
  bizAdmits=[],
  bizAdmitsNote="114 春秋公告提供個別入學結果說明，尚未取得可分系計數的公開學士榜單。",)
S['0053'] = _e(tier='C', place='高雄三民（建工）等多校區', travel='高鐵左營約 1 小時＋轉車；要搬家',
  fee=dict(kind='paid', amount=800, text='NT$800，不退', src='https://oia.nkust.edu.tw/en/unit-11-262-5.html', year='115'),
  firstYear={
    "kind": "unknown"
  },
  aid={
    "sure": None,
    "review": "現行英文招生頁列學士可審查減免學雜／學分費，獎期 1 年、名額依學院；但最新 115 附件只列碩博士辦法，115 學士是否適用仍待校方確認。研究所每月津貼不套給學士。",
    "src": "https://oia.nkust.edu.tw/unit-11-268-6.html#description2",
    "year": "現行招生頁；115 學士適用內容待校方確認"
  },
  renew="招生頁載受獎期限 1 年；學士續領的成績、學分與申請日未核得。請向國際處確認學士適用辦法。",
  lang='依系。',
  after='春季只收研究所。往年秋季 3 月上旬–4 月下旬報名、6 月下旬放榜（離 ARC 到期只差幾天）。',
  verdict='商管科系多，但 6 月下旬才放榜，ARC 很緊；學士獎學金不明。',
  verdictMy='ဇွန်လကုန် ရလဒ် — ARC နှင့် အလွန်နီး။',
  checked="2026-10-05",
  tuition={
    "min": 45628,
    "max": 54028,
    "year": "114",
    "text": "每學期學費＋雜費參考 45,628–54,028 元。115 簡章引用 114 學士費用表；依系所收費。",
    "src": "https://oia.nkust.edu.tw/images/upload/files/2026%E7%A7%8B%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E6%8B%9B%E7%94%9F%E7%B0%A1%E7%AB%A0%202026%20Fall%20International%20Degree%20Student%20Prospectus.pdf"
  },
  bizAdmits=[
    {
      "dept": "觀光管理系",
      "count": 2,
      "year": "114",
      "term": "fall",
      "src": "https://oia.nkust.edu.tw/unit-11-268-6.html",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "國際企業系",
      "count": 2,
      "year": "114",
      "term": "fall",
      "src": "https://oia.nkust.edu.tw/unit-11-268-6.html",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "運籌管理系",
      "count": 2,
      "year": "114",
      "term": "fall",
      "src": "https://oia.nkust.edu.tw/unit-11-268-6.html",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "企業管理系",
      "count": 4,
      "year": "114",
      "term": "fall",
      "src": "https://oia.nkust.edu.tw/unit-11-268-6.html",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    },
    {
      "dept": "行銷與流通管理系",
      "count": 2,
      "year": "114",
      "term": "fall",
      "src": "https://oia.nkust.edu.tw/unit-11-268-6.html",
      "basis": "一般外國學士正取；排除研究所、備取、轉學與國際專修部"
    }
  ],
  renewSource={
    "src": "https://oia.nkust.edu.tw/unit-11-268-6.html#description2",
    "year": "現行招生頁；115 學士續領待確認"
  },
  readYourself=[
    {
      "label": "高科學士獎學金適用辦法",
      "url": "https://oia.nkust.edu.tw/unit-11-268-6.html#description2",
      "why": "115最新附件只有碩博士；學士是否適用與續領須校方確認"
    }
  ],)


# 2026-10-05：官方時程覆蓋；來源學年度與歷史參考明確分開。
ROUND_OVERRIDE.update({
 ("0039", "spring"): {
   "ug": "has",
   "rounds": [
     {
       "start": {
         "status": "official",
         "date": "2026-08-01",
         "sourceYear": "115",
         "src": "https://oia.ntcu.edu.tw/storage/media/W4NT9CD1uUPo9eA6KMtDqVYo5skoJ5OoHJhO2mNI.pdf",
         "year": "115"
       },
       "end": {
         "status": "official",
         "date": "2026-10-31",
         "sourceYear": "115",
         "src": "https://oia.ntcu.edu.tw/storage/media/W4NT9CD1uUPo9eA6KMtDqVYo5skoJ5OoHJhO2mNI.pdf",
         "year": "115"
       },
       "result": {
         "status": "official",
         "date": "2026-12-17",
         "sourceYear": "115",
         "src": "https://oia.ntcu.edu.tw/storage/media/W4NT9CD1uUPo9eA6KMtDqVYo5skoJ5OoHJhO2mNI.pdf",
         "year": "115"
       },
       "letter": "2026-12-24",
       "src": "https://oia.ntcu.edu.tw/storage/media/W4NT9CD1uUPo9eA6KMtDqVYo5skoJ5OoHJhO2mNI.pdf",
       "year": "115",
       "note": "115 春季學士；12/24 寄入學通知。"
     }
   ],
   "note": "115 招生系所表列春季學士，國際企業亦有春季招生。",
   "src": "https://oia.ntcu.edu.tw/storage/media/W4NT9CD1uUPo9eA6KMtDqVYo5skoJ5OoHJhO2mNI.pdf",
   "year": "115"
 },
 ("1018", "spring"): {
   "ug": "has",
   "rounds": [
     {
       "start": {
         "status": "official",
         "date": "2026-09-20",
         "sourceYear": "115",
         "src": "https://icsc.cyut.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelV6TDNCMFlWODBNekE1TkY4eE1qSTNNRFE1WHpnNE1EQTBMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKICFCLOQOPPXX00ZS5430YWMONPWWEC34SSMKLPIDCCTSFCNKFDEGFG10KLTSVWPOXT15DG24NKXTMOMOA0YSIGICQLLO00JDQPTW14MK3045OOHGGHUSSS404544VSA0EGGDTWB4WSXSWSB0CGMKVXNPDDA0SW30IGA4QOOKLKFCICKKDHYX44B0TX24DCJGMK25WSEGXSXSHDYTPKA5XWROZWOPQOSSIGWXIC00YXMPLOPONK24ZSPKFHXS34UWXSGCGG05OOA5UWTS45UW00OKOK54LOCCHDHHHCEGEGWS14MOJGWSOP34PKGCJDJDLOA534A41111",
         "year": "115"
       },
       "end": {
         "status": "unknown",
         "label": "第1梯截止未單列（全期最終12/19）",
         "sourceYear": "115",
         "src": "https://icsc.cyut.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelV6TDNCMFlWODBNekE1TkY4eE1qSTNNRFE1WHpnNE1EQTBMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKICFCLOQOPPXX00ZS5430YWMONPWWEC34SSMKLPIDCCTSFCNKFDEGFG10KLTSVWPOXT15DG24NKXTMOMOA0YSIGICQLLO00JDQPTW14MK3045OOHGGHUSSS404544VSA0EGGDTWB4WSXSWSB0CGMKVXNPDDA0SW30IGA4QOOKLKFCICKKDHYX44B0TX24DCJGMK25WSEGXSXSHDYTPKA5XWROZWOPQOSSIGWXIC00YXMPLOPONK24ZSPKFHXS34UWXSGCGG05OOA5UWTS45UW00OKOK54LOCCHDHHHCEGEGWS14MOJGWSOP34PKGCJDJDLOA534A41111",
         "year": "115"
       },
       "result": {
         "status": "official",
         "date": "2026-12-18",
         "sourceYear": "115",
         "src": "https://icsc.cyut.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelV6TDNCMFlWODBNekE1TkY4eE1qSTNNRFE1WHpnNE1EQTBMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKICFCLOQOPPXX00ZS5430YWMONPWWEC34SSMKLPIDCCTSFCNKFDEGFG10KLTSVWPOXT15DG24NKXTMOMOA0YSIGICQLLO00JDQPTW14MK3045OOHGGHUSSS404544VSA0EGGDTWB4WSXSWSB0CGMKVXNPDDA0SW30IGA4QOOKLKFCICKKDHYX44B0TX24DCJGMK25WSEGXSXSHDYTPKA5XWROZWOPQOSSIGWXIC00YXMPLOPONK24ZSPKFHXS34UWXSGCGG05OOA5UWTS45UW00OKOK54LOCCHDHHHCEGEGWS14MOJGWSOP34PKGCJDJDLOA534A41111",
         "year": "115"
       },
       "letter": "2026-12-24",
       "note": "第1梯；12/19 是全期最終截止，不當作第一梯截止。",
       "src": "https://icsc.cyut.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelV6TDNCMFlWODBNekE1TkY4eE1qSTNNRFE1WHpnNE1EQTBMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKICFCLOQOPPXX00ZS5430YWMONPWWEC34SSMKLPIDCCTSFCNKFDEGFG10KLTSVWPOXT15DG24NKXTMOMOA0YSIGICQLLO00JDQPTW14MK3045OOHGGHUSSS404544VSA0EGGDTWB4WSXSWSB0CGMKVXNPDDA0SW30IGA4QOOKLKFCICKKDHYX44B0TX24DCJGMK25WSEGXSXSHDYTPKA5XWROZWOPQOSSIGWXIC00YXMPLOPONK24ZSPKFHXS34UWXSGCGG05OOA5UWTS45UW00OKOK54LOCCHDHHHCEGEGWS14MOJGWSOP34PKGCJDJDLOA534A41111",
       "year": "115"
     },
     {
       "start": {
         "status": "unknown",
         "label": "第2梯開始待確認",
         "sourceYear": "115",
         "src": "https://icsc.cyut.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelV6TDNCMFlWODBNekE1TkY4eE1qSTNNRFE1WHpnNE1EQTBMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKICFCLOQOPPXX00ZS5430YWMONPWWEC34SSMKLPIDCCTSFCNKFDEGFG10KLTSVWPOXT15DG24NKXTMOMOA0YSIGICQLLO00JDQPTW14MK3045OOHGGHUSSS404544VSA0EGGDTWB4WSXSWSB0CGMKVXNPDDA0SW30IGA4QOOKLKFCICKKDHYX44B0TX24DCJGMK25WSEGXSXSHDYTPKA5XWROZWOPQOSSIGWXIC00YXMPLOPONK24ZSPKFHXS34UWXSGCGG05OOA5UWTS45UW00OKOK54LOCCHDHHHCEGEGWS14MOJGWSOP34PKGCJDJDLOA534A41111",
         "year": "115"
       },
       "end": {
         "status": "official",
         "date": "2026-12-19",
         "sourceYear": "115",
         "src": "https://icsc.cyut.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelV6TDNCMFlWODBNekE1TkY4eE1qSTNNRFE1WHpnNE1EQTBMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKICFCLOQOPPXX00ZS5430YWMONPWWEC34SSMKLPIDCCTSFCNKFDEGFG10KLTSVWPOXT15DG24NKXTMOMOA0YSIGICQLLO00JDQPTW14MK3045OOHGGHUSSS404544VSA0EGGDTWB4WSXSWSB0CGMKVXNPDDA0SW30IGA4QOOKLKFCICKKDHYX44B0TX24DCJGMK25WSEGXSXSHDYTPKA5XWROZWOPQOSSIGWXIC00YXMPLOPONK24ZSPKFHXS34UWXSGCGG05OOA5UWTS45UW00OKOK54LOCCHDHHHCEGEGWS14MOJGWSOP34PKGCJDJDLOA534A41111",
         "year": "115"
       },
       "result": {
         "status": "official",
         "date": "2027-01-15",
         "sourceYear": "115",
         "src": "https://icsc.cyut.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelV6TDNCMFlWODBNekE1TkY4eE1qSTNNRFE1WHpnNE1EQTBMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKICFCLOQOPPXX00ZS5430YWMONPWWEC34SSMKLPIDCCTSFCNKFDEGFG10KLTSVWPOXT15DG24NKXTMOMOA0YSIGICQLLO00JDQPTW14MK3045OOHGGHUSSS404544VSA0EGGDTWB4WSXSWSB0CGMKVXNPDDA0SW30IGA4QOOKLKFCICKKDHYX44B0TX24DCJGMK25WSEGXSXSHDYTPKA5XWROZWOPQOSSIGWXIC00YXMPLOPONK24ZSPKFHXS34UWXSGCGG05OOA5UWTS45UW00OKOK54LOCCHDHHHCEGEGWS14MOJGWSOP34PKGCJDJDLOA534A41111",
         "year": "115"
       },
       "letter": "2027-01-22",
       "note": "第2梯；1/22 寄入學通知。",
       "src": "https://icsc.cyut.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelV6TDNCMFlWODBNekE1TkY4eE1qSTNNRFE1WHpnNE1EQTBMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKICFCLOQOPPXX00ZS5430YWMONPWWEC34SSMKLPIDCCTSFCNKFDEGFG10KLTSVWPOXT15DG24NKXTMOMOA0YSIGICQLLO00JDQPTW14MK3045OOHGGHUSSS404544VSA0EGGDTWB4WSXSWSB0CGMKVXNPDDA0SW30IGA4QOOKLKFCICKKDHYX44B0TX24DCJGMK25WSEGXSXSHDYTPKA5XWROZWOPQOSSIGWXIC00YXMPLOPONK24ZSPKFHXS34UWXSGCGG05OOA5UWTS45UW00OKOK54LOCCHDHHHCEGEGWS14MOJGWSOP34PKGCJDJDLOA534A41111",
       "year": "115"
     }
   ],
   "note": "115 春季兩梯；各梯報名截止與最終截止分開看。",
   "src": "https://icsc.cyut.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelV6TDNCMFlWODBNekE1TkY4eE1qSTNNRFE1WHpnNE1EQTBMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKICFCLOQOPPXX00ZS5430YWMONPWWEC34SSMKLPIDCCTSFCNKFDEGFG10KLTSVWPOXT15DG24NKXTMOMOA0YSIGICQLLO00JDQPTW14MK3045OOHGGHUSSS404544VSA0EGGDTWB4WSXSWSB0CGMKVXNPDDA0SW30IGA4QOOKLKFCICKKDHYX44B0TX24DCJGMK25WSEGXSXSHDYTPKA5XWROZWOPQOSSIGWXIC00YXMPLOPONK24ZSPKFHXS34UWXSGCGG05OOA5UWTS45UW00OKOK54LOCCHDHHHCEGEGWS14MOJGWSOP34PKGCJDJDLOA534A41111",
   "year": "115"
 },
 ("1018", "fall"): {
   "ug": "has",
   "rounds": [],
   "note": "115 往年第一梯 7/3 放榜、7/10 寄通知，晚於 ARC 參考期限，未列成可用梯次；116 尚未公告，須等較早時程。",
   "src": "https://icsc.cyut.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelV6TDNCMFlWODBNekE1TkY4eE1qSTNNRFE1WHpnNE1EQTBMbkJrWmc9PQ==&fname=WW54RPOKIC4441MPHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54FGOKPOPOZX10A404GDXTRKPKTSIG34B0NOYSVXVXDCTSWSB0VSOKUSKKYWFCNPPO44OOHCA0UWIGTWMODC35WSB040MKZTGDQPROWS30IGB4GGOK45USPOWSB510DGFGA0SXKO30B4ICIGRO35WWNPVX04OKYSB4JGUSPKKKICFCLOQOPPXX00ZS5430YWMONPWWEC34SSMKLPIDCCTSFCNKFDEGFG10KLTSVWPOXT15DG24NKXTMOMOA0YSIGICQLLO00JDQPTW14MK3045OOHGGHUSSS404544VSA0EGGDTWB4WSXSWSB0CGMKVXNPDDA0SW30IGA4QOOKLKFCICKKDHYX44B0TX24DCJGMK25WSEGXSXSHDYTPKA5XWROZWOPQOSSIGWXIC00YXMPLOPONK24ZSPKFHXS34UWXSGCGG05OOA5UWTS45UW00OKOK54LOCCHDHHHCEGEGWS14MOJGWSOP34PKGCJDJDLOA534A41111",
   "year": "115"
 },
 ("0020", "spring"): {
   "ug": "has",
   "rounds": [
     {
       "start": {
         "status": "official",
         "date": "2026-09-01",
         "sourceYear": "115",
         "src": "https://oia.ndhu.edu.tw/var/file/27/1027/img/4756/894840940.pdf",
         "year": "115"
       },
       "end": {
         "status": "official",
         "date": "2026-10-31",
         "sourceYear": "115",
         "src": "https://oia.ndhu.edu.tw/var/file/27/1027/img/4756/894840940.pdf",
         "year": "115"
       },
       "result": {
         "status": "official",
         "date": "2026-12-20",
         "sourceYear": "115",
         "src": "https://oia.ndhu.edu.tw/var/file/27/1027/img/4756/894840940.pdf",
         "year": "115"
       },
       "note": "115 春季簡章時程。"
     }
   ],
   "note": "以 115 簡章 10/31 截止、12/20 放榜為準。",
   "src": "https://oia.ndhu.edu.tw/var/file/27/1027/img/4756/894840940.pdf",
   "year": "115"
 },
 ("0024", "spring"): {
   "ug": "grad",
   "rounds": [],
   "note": "115 系所招生表春季僅研究所，商管學士報秋季。",
   "src": "https://oia2.npust.edu.tw/zh/wp-content/uploads/sites/2/2025/11/115學年度屏東科技大學招生簡章-中英文版-new-20260105.pdf",
   "year": "115"
 },
 ("0024", "fall"): {
   "ug": "has",
   "rounds": [
     {
       "start": {
         "status": "historical",
         "sort": "2027-01-01",
         "label": "115 往年 1/1 開始",
         "sourceYear": "115",
         "src": "https://oia2.npust.edu.tw/zh/wp-content/uploads/sites/2/2025/11/115學年度屏東科技大學招生簡章-中英文版-new-20260105.pdf",
         "year": "115"
       },
       "end": {
         "status": "historical",
         "sort": "2027-03-31",
         "label": "115 往年 3/31 截止",
         "sourceYear": "115",
         "src": "https://oia2.npust.edu.tw/zh/wp-content/uploads/sites/2/2025/11/115學年度屏東科技大學招生簡章-中英文版-new-20260105.pdf",
         "year": "115"
       },
       "result": {
         "status": "historical",
         "sort": "2027-06-15",
         "label": "115 往年 6/15 放榜",
         "sourceYear": "115",
         "src": "https://oia2.npust.edu.tw/zh/wp-content/uploads/sites/2/2025/11/115學年度屏東科技大學招生簡章-中英文版-new-20260105.pdf",
         "year": "115"
       },
       "note": "116 未公告，僅以 115 往年時程參考。"
     }
   ],
   "note": "116 未公告；115 往年時程。",
   "src": "https://oia2.npust.edu.tw/zh/wp-content/uploads/sites/2/2025/11/115學年度屏東科技大學招生簡章-中英文版-new-20260105.pdf",
   "year": "115"
 },
 ("0018", "fall"): {
   "ug": "has",
   "rounds": [
     {
       "start": {
         "status": "historical",
         "sort": "2027-01-01",
         "label": "115 往年 1/1 開始",
         "sourceYear": "115",
         "src": "https://www.ncyu.edu.tw/oia_eng/ServerFile/Get/786060ff-e628-4e3e-9dc1-35afcc76b7c6?nodeId=60284&sId=237992",
         "year": "115"
       },
       "end": {
         "status": "historical",
         "sort": "2027-03-01",
         "label": "115 往年 3/1 截止",
         "sourceYear": "115",
         "src": "https://www.ncyu.edu.tw/oia_eng/ServerFile/Get/786060ff-e628-4e3e-9dc1-35afcc76b7c6?nodeId=60284&sId=237992",
         "year": "115"
       },
       "result": {
         "status": "historical",
         "sort": "2027-05-18",
         "label": "115 往年 5/18 放榜",
         "sourceYear": "115",
         "src": "https://www.ncyu.edu.tw/oia_eng/ServerFile/Get/786060ff-e628-4e3e-9dc1-35afcc76b7c6?nodeId=60284&sId=237992",
         "year": "115"
       },
       "letter": "2027-06-05",
       "note": "115 往年 6/5 前寄通知；116 尚未公告。"
     }
   ],
   "note": "只列 ARC 前可用的第一梯；往年第二梯 7/10 放榜，未列入。",
   "src": "https://www.ncyu.edu.tw/oia_eng/ServerFile/Get/786060ff-e628-4e3e-9dc1-35afcc76b7c6?nodeId=60284&sId=237992",
   "year": "115"
 },
 ("0017", "spring"): {
   "ug": "has",
   "rounds": [
     {
       "start": {
         "status": "official",
         "date": "2026-09-03",
         "sourceYear": "115-2",
         "src": "https://webap.ntpu.edu.tw/interstud/index.php",
         "year": "115-2"
       },
       "end": {
         "status": "official",
         "date": "2026-10-31",
         "sourceYear": "115-2",
         "src": "https://webap.ntpu.edu.tw/interstud/index.php",
         "year": "115-2"
       },
       "result": {
         "status": "historical",
         "sort": "2026-12-09",
         "label": "114 往年 12/9 放榜",
         "sourceYear": "114",
         "src": "https://cms-carrier.ntpu.edu.tw/uploads/114_NTPU_Admission_Brochure_Spring_semester_2026_1_628562954d.pdf",
         "year": "114"
       },
       "note": "115 春季報名日期已公告；放榜使用 114 往年參考。"
     }
   ],
   "note": "目前系統列 115-2 報名，放榜仍以往年參考。",
   "src": "https://webap.ntpu.edu.tw/interstud/index.php",
   "year": "115-2"
 },
 ("0004", "fall"): {
   "ug": "has",
   "rounds": [
     {
       "start": {
         "status": "historical",
         "sort": "2027-01-12",
         "label": "115 往年 1/12 開始",
         "sourceYear": "115",
         "src": "https://bds.oia.ntnu.edu.tw/api/v1/ap/dl?id=359001",
         "year": "115"
       },
       "end": {
         "status": "historical",
         "sort": "2027-03-02",
         "label": "115 往年 3/2 截止",
         "sourceYear": "115",
         "src": "https://bds.oia.ntnu.edu.tw/api/v1/ap/dl?id=359001",
         "year": "115"
       },
       "result": {
         "status": "historical",
         "sort": "2027-05-04",
         "label": "115 往年暫定 5/4 放榜",
         "sourceYear": "115",
         "src": "https://bds.oia.ntnu.edu.tw/api/v1/ap/dl?id=359001",
         "year": "115"
       },
       "note": "115 學士秋季第2梯；116 未公告。企管學士只收秋季。"
     }
   ],
   "note": "學士依 115 簡章第2梯；研究所秋季第1梯未套入學士。",
   "src": "https://bds.oia.ntnu.edu.tw/api/v1/ap/dl?id=359001",
   "year": "115"
 },
 ("0004", "spring"): {
   "ug": "has",
   "rounds": [
     {
       "start": {
         "status": "official",
         "date": "2026-08-03",
         "sourceYear": "115",
         "src": "https://bds.oia.ntnu.edu.tw/api/v1/ap/dl?id=359001",
         "year": "115"
       },
       "end": {
         "status": "official",
         "date": "2026-09-14",
         "sourceYear": "115",
         "src": "https://bds.oia.ntnu.edu.tw/api/v1/ap/dl?id=359001",
         "year": "115"
       },
       "result": {
         "status": "official",
         "date": "2026-11-20",
         "sourceYear": "115",
         "src": "https://bds.oia.ntnu.edu.tw/api/v1/ap/dl?id=359001",
         "year": "115"
       },
       "letter": "2026-12-14",
       "note": "115 春季已截止；企管學士不開春季。"
     }
   ],
   "note": "全校部分學士有春季，但企管學士只收秋季；9/14 已截止。",
   "src": "https://bds.oia.ntnu.edu.tw/api/v1/ap/dl?id=359001",
   "year": "115"
 },
 ("0043", "spring"): {
   "ug": "grad",
   "rounds": [],
   "note": "115-2 新簡章系所表僅碩博士；学士仍報秋季。",
   "src": "https://admission.ncut.edu.tw/parts/proofReaderNews.ashx?ii=_837988978077643.pdf",
   "year": "115-2"
 },
 ("0043", "fall"): {
   "ug": "has",
   "rounds": [
     {
       "start": {
         "status": "historical",
         "sort": "2027-03-23",
         "label": "115 往年 3/23 開始",
         "sourceYear": "115",
         "src": "https://admission.ncut.edu.tw/parts/proofReaderNews.ashx?ii=_281969417709349.pdf",
         "year": "115"
       },
       "end": {
         "status": "historical",
         "sort": "2027-05-10",
         "label": "115 往年 5/10 截止",
         "sourceYear": "115",
         "src": "https://admission.ncut.edu.tw/parts/proofReaderNews.ashx?ii=_281969417709349.pdf",
         "year": "115"
       },
       "result": {
         "status": "historical",
         "sort": "2027-05-27",
         "label": "115 往年 5/27 寄入學通知（公開榜單 7/20）",
         "sourceYear": "115",
         "src": "https://admission.ncut.edu.tw/parts/proofReaderNews.ashx?ii=_281969417709349.pdf",
         "year": "115"
       },
       "letter": "2027-05-27",
       "note": "115 往年入學通知先於榜單；116 尚未公告。"
     }
   ],
   "note": "以先寄入學通知為準；116 年時程需再核對。",
   "src": "https://admission.ncut.edu.tw/parts/proofReaderNews.ashx?ii=_281969417709349.pdf",
   "year": "115"
 },
 ("1048", "spring"): {
   "ug": "has",
   "rounds": [
     {
       "start": {
         "status": "official",
         "date": "2026-02-21",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "end": {
         "status": "unknown",
         "label": "各批截止未單列（全期11/29）",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "result": {
         "status": "official",
         "date": "2026-10-30",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "note": "官方第5次放榜；簡章／時程全期11/29截止，報名頁寫11/30，建議11/29前完成。"
     },
     {
       "start": {
         "status": "official",
         "date": "2026-02-21",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "end": {
         "status": "unknown",
         "label": "各批截止未單列（全期11/29）",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "result": {
         "status": "official",
         "date": "2026-11-30",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "note": "官方第6次放榜；簡章／時程全期11/29截止，報名頁寫11/30，建議11/29前完成。"
     },
     {
       "start": {
         "status": "official",
         "date": "2026-02-21",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "end": {
         "status": "official",
         "date": "2026-11-29",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "result": {
         "status": "official",
         "date": "2026-12-30",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "note": "官方第7次放榜；簡章／時程全期11/29截止，報名頁寫11/30，建議11/29前完成。"
     }
   ],
   "note": "列目前尚未到的第5、6、7次放榜；各批截止未單列。官方時程與報名頁截止差異保留。",
   "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
   "year": "115"
 },
 ("1048", "fall"): {
   "ug": "has",
   "rounds": [
     {
       "start": {
         "status": "historical",
         "sort": "2027-02-21",
         "label": "115 往年 2/21 開始",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "end": {
         "status": "unknown",
         "label": "各批截止未單列（115往年全期6/30）",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "result": {
         "status": "historical",
         "sort": "2027-04-30",
         "label": "115 往年 4/30 放榜",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "note": "116 未公告，115 往年供參考；7/30 才放榜的批次未列入。"
     },
     {
       "start": {
         "status": "historical",
         "sort": "2027-02-21",
         "label": "115 往年 2/21 開始",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "end": {
         "status": "unknown",
         "label": "各批截止未單列（115往年全期6/30）",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "result": {
         "status": "historical",
         "sort": "2027-05-30",
         "label": "115 往年 5/30 放榜",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "note": "116 未公告，115 往年供參考；7/30 才放榜的批次未列入。"
     },
     {
       "start": {
         "status": "historical",
         "sort": "2027-02-21",
         "label": "115 往年 2/21 開始",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "end": {
         "status": "unknown",
         "label": "各批截止未單列（115往年全期6/30）",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "result": {
         "status": "historical",
         "sort": "2027-06-30",
         "label": "115 往年 6/30 放榜",
         "sourceYear": "115",
         "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
         "year": "115"
       },
       "note": "116 未公告，115 往年供參考；7/30 才放榜的批次未列入。"
     }
   ],
   "note": "116 未公告；115 往年各批放榜參考。",
   "src": "https://oia.asia.edu.tw/p/404-1008-2484.php?Lang=en",
   "year": "115"
 },
 ("0001", "fall"): {
   "ug": "has",
   "rounds": [
     {
       "start": {
         "status": "official",
         "date": "2026-09-22",
         "sourceYear": "116",
         "src": "https://drive.google.com/uc?export=download&id=1RC6EOaByXy7hqe6_2ddinrZZk64UGu3k",
         "year": "116"
       },
       "end": {
         "status": "official",
         "date": "2026-10-15",
         "sourceYear": "116",
         "src": "https://drive.google.com/uc?export=download&id=1RC6EOaByXy7hqe6_2ddinrZZk64UGu3k",
         "year": "116"
       },
       "result": {
         "status": "official",
         "date": "2026-11-27",
         "sourceYear": "116",
         "src": "https://drive.google.com/uc?export=download&id=1RC6EOaByXy7hqe6_2ddinrZZk64UGu3k",
         "year": "116"
       }
     },
     {
       "start": {
         "status": "unknown",
         "label": "116 第2梯開始待公告",
         "sourceYear": "116",
         "src": "https://nccuadmission.nccu.edu.tw/Post/331",
         "year": "116"
       },
       "end": {
         "status": "unknown",
         "label": "116 第2梯截止待公告",
         "sourceYear": "116",
         "src": "https://nccuadmission.nccu.edu.tw/Post/331",
         "year": "116"
       },
       "result": {
         "status": "historical",
         "sort": "2027-05-12",
         "label": "115 往年 5/12 已放榜",
         "sourceYear": "115",
         "src": "https://oic.nccu.edu.tw/Post/15941",
         "year": "115"
       },
       "note": "116 第二梯完整時程尚未公告；115 往年 5/28 後陸續寄正取通知，需先完成線上報到。"
     }
   ],
   "note": "第一梯正式；第二梯完整時程待公告，結果使用 115 往年參考。",
   "src": "https://drive.google.com/uc?export=download&id=1RC6EOaByXy7hqe6_2ddinrZZk64UGu3k",
   "year": "116"
 }
})
