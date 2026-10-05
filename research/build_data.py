"""Build a provenance-preserving directory. Never promote historical days to future exact dates."""
import json,re
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parent
registry=json.loads((ROOT/'moe115.json').read_text())
sit={r['code']:r for r in json.loads((ROOT/'sit-schools.json').read_text()) if r.get('code')}
CITIES={'臺北市':'Taipei','新北市':'New Taipei','基隆市':'Keelung','桃園市':'Taoyuan','新竹市':'Hsinchu City','新竹縣':'Hsinchu County','苗栗縣':'Miaoli','臺中市':'Taichung','彰化縣':'Changhua','南投縣':'Nantou','雲林縣':'Yunlin','嘉義市':'Chiayi City','嘉義縣':'Chiayi County','臺南市':'Tainan','高雄市':'Kaohsiung','屏東縣':'Pingtung','宜蘭縣':'Yilan','花蓮縣':'Hualien','臺東縣':'Taitung','澎湖縣':'Penghu','金門縣':'Kinmen'}
SHORT='''0001 政大 NCCU;0002 清華 NTHU;0003 臺大 NTU;0004 臺師大 NTNU;0005 成大 NCKU;0006 中興 NCHU;0007 陽明交大 NYCU;0008 中央 NCU;0009 中山 NSYSU;0012 海大 NTOU;0013 中正 CCU;0014 高師大 NKNU;0015 彰師大 NCUE;0017 北大 NTPU;0018 嘉大 NCYU;0019 高大 NUK;0020 東華 NDHU;0021 暨南 NCNU;0022 臺科 NTUST;0023 雲科 YunTech;0024 屏科 NPUST;0025 北科 NTUT;0028 北藝 TNUA;0029 臺藝 NTUA;0030 臺東 NTTU;0031 宜蘭 NIU;0032 聯合 NUU;0033 虎尾 NFU;0035 南藝 TNNUA;0036 臺南 NUTN;0037 北教 NTUE;0039 中教 NTCU;0042 澎科 NPU;0043 勤益 NCUT;0044 國體 NTSU;0046 北護 NTUNHS;0047 高餐 NKUHT;0048 金門 NQU;0049 臺體 NTUS;0050 中科 NUTC;0051 北商 NTUB;0052 屏大 NPTU;0053 高科 NKUST;0144 臺灣戲曲 TCPA;0221 臺南護專 NTIN;0222 臺東專科 NTC;1001 東海 THU;1002 輔仁 FJU;1003 東吳 SCU;1004 中原 CYCU;1005 淡江 TKU;1006 文化 PCCU;1007 逢甲 FCU;1008 靜宜 PU;1009 長庚 CGU;1010 元智 YZU;1011 中華 CHU;1012 大葉 DYU;1013 華梵 HFU;1014 義守 ISU;1015 世新 SHU;1016 銘傳 MCU;1017 實踐 USC;1018 朝陽 CYUT;1019 高醫 KMU;1020 南華 NHU;1021 真理 AU;1022 大同 TTU;1023 南臺 STUST;1024 崑山 KSU;1025 嘉藥 CNU;1026 樹德 STU;1027 慈濟 TCU;1028 北醫 TMU;1029 中山醫 CSMU;1030 龍華 LHU;1031 輔英 FYU;1032 明新 MUST;1033 長榮 CJCU;1034 弘光 HKU;1035 中國醫 CMU;1036 健行 UCH;1037 正修 CSU;1038 萬能 VNU;1039 玄奘 HCU;1040 建國 CTU;1041 明志 MCUT;1042 台鋼 TSUST;1043 大仁 TAJEN;1044 聖約翰 SJU;1045 嶺東 LTU;1046 中國科大 CUTE;1047 中臺 CTUST;1048 亞洲 ASIA;1049 開南 KNU;1050 佛光 FGU;1051 南應 TUT;1052 中信科大 CTUST-TN;1053 元培 YPU;1054 景文 JUST;1055 中華醫大 HWAI;1056 東南 TNU;1057 德明 TAKMING;1060 南開 NKUT;1061 中華科大 CUST;1062 僑光 OCU;1063 育達 YDU;1064 美和 MEIHO;1065 吳鳳 WFU;1069 修平 HUST;1070 長庚科大 CGUST;1071 北城 TPCU;1072 敏實 MITUST;1073 醒吾 HWU;1075 文藻 WZU;1076 華夏 HWH;1078 致理 CLUT;1079 康寧 UKN;1080 德霖 HDUT;1082 崇右 CUFA;1083 海洋科大 TUMT;1084 亞東 AEUST;1085 馬偕醫大 MMU;1125 中信金融 CTBC;1168 南亞 NANYA;1183 黎明 LIT;1185 德育 DYHU;1196 法鼓 DILA;1282 馬偕護專 MKC;1283 仁德 JENTE;1284 樹人 SZMC;1285 慈惠 TZUHUI;1286 耕莘 CTCN;1287 敏惠 MHCHCM;1289 育英 YUHING;1291 聖母 SMC;1292 新生 HSC;1293 崇仁 CJC;3002 北市大 UT'''
names={p.split()[0]:p.split()[1:] for p in SHORT.split(';')}
# Editorial ordinal estimates, not entrance scores. Specialized schools remain unrated.
BANDS={5:'0001 0002 0003 0005 0007 0022',4:'0004 0006 0008 0009 0012 0013 0017 0023 0025',3:'0014 0015 0018 0019 0020 0021 0024 0030 0031 0032 0033 0036 0037 0039 0043 0047 0050 0051 0052 0053 1001 1002 1003 1004 1005 1007 1009 1010 1018 1022 1023 1041 1075 1078 3002',2:'0042 0048 1006 1008 1011 1012 1014 1015 1016 1017 1020 1021 1024 1026 1030 1032 1033 1034 1036 1037 1038 1040 1042 1043 1044 1045 1046 1048 1049 1050 1051 1052 1054 1056 1057 1060 1061 1062 1063 1065 1069 1071 1072 1073 1080 1083 1084 1125 1168 1183'}
bands={code:n for n,cs in BANDS.items() for code in cs.split()}
def bi(zh,my='အသေးစိတ်ကို တရားဝင်ဝင်ခွင့်လမ်းညွှန်တွင် အတည်ပြုပါ။'):return dict(zh=zh,my=my)
def exact(d):return dict(date=d,status='official')
def approx(label,sort,basis='115',status='historical'):
    my=label.replace('約','ခန့် ').replace('月上旬',' လအစ').replace('月中旬',' လလယ်').replace('月下旬',' လကုန်ပိုင်း').replace('月初',' လအစ').replace('月底',' လကုန်').replace('月',' လ').replace('前',' မတိုင်မီ')
    return dict(label=bi(label,my),sort=sort,status=status,basis=basis)
def rnd(start=None,end=None,result=None,name=None,note=None):
    out=dict(start=start,end=end,result=result)
    if name:out['name']=bi(name,name)
    if note:out['note']=bi(note)
    return out
schools={}
for row in registry:
    code=row['代碼'];name=row['學校名稱'];city=re.sub(r'^\[.*?\]','',row['縣市名稱']);ss=sit.get(code,{})
    typ='junior' if '專科學校' in name else 'college' if '學院' in name else 'technology' if row['體系別']=='[2]技職' else 'university'
    web=row['網址'];short,abbr=names[code]
    school=dict(id=code,name=name,short=short,abbr=abbr,english=ss.get('name',''),cities=[city],cityEn=CITIES[city],type=typ,ownership='public' if row['公/私立']=='公立' else 'private',difficulty=bands.get(code),website=web,catalog=ss.get('program'),admission=dict(url=web,kind='home'),terms={t:dict(rounds=[],sources=[],notes=[]) for t in ['spring','fall']},checked='2026-09-19')
    path=ROOT/(code+'.json');research=json.loads(path.read_text()) if path.exists() else dict(pages=[])
    school['reviewState']='page-read' if any(p.get('ok') for p in research['pages']) else 'unavailable'
    candidates=[]
    for page in research['pages']:
        for a in page.get('links',[]):
            title=a['text'];url=a['url']
            if re.search(r'外國學生|外國學位生|foreign student|international student',title,re.I) and not re.search(r'交換|專修|獎學金|轉學|華語|scholarship|exchange|handbook|field trip|handbook|新生手冊|錄取公告',title,re.I):
                if url.startswith('http') and '.edu.tw' in urlparse(url).netloc:candidates.append((len(title),url))
    if candidates:school['admission']=dict(url=sorted(candidates)[0][1],kind='admission')
    schools[code]=school
# Multiple teaching locations must not be collapsed into Taipei.
for code,more in {'0007':['臺北市'],'0017':['臺北市'],'1016':['桃園市'],'1017':['高雄市'],'1046':['新竹縣'],'1070':['嘉義縣'],'1282':['新北市']}.items():schools[code]['cities']+=more
def portal(code,url,kind='admission'):schools[code]['admission']=dict(url=url,kind=kind)
def term(code,semester,rounds,sources,scope=None,brochure=None,notes=None,programs=None,apply=None):
    d=schools[code]['terms'][semester];d.update(rounds=rounds,sources=sources,notes=notes or [])
    if scope:d['scope']=scope;d['scopeLabel']=bi('學士／碩士／博士依當屆開放系所','ဘွဲ့ကြို / မဟာဘွဲ့ / ပါရဂူ — လမ်းညွှန်ပါ ဘာသာရပ်အတိုင်း')
    if brochure:d['brochure']=dict(url=brochure,status='official')
    if programs:d['programs']=programs
    if apply:d['apply']=dict(url=apply,kind='apply')
NTU='https://admissions.ntu.edu.tw/apply/degree-students/international-students/'
portal('0003',NTU)
term('0003','spring',[rnd(exact('2026-08-03'),exact('2026-09-17'),exact('2026-11-10'))],[NTU],'graduate','https://admissions.ntu.edu.tw/wp-content/uploads/115-2Admission-Guidelines-for-Intl-Degree-Students_ENG_V2.pdf')
term('0003','fall',[rnd(exact('2026-09-29'),exact('2026-11-05'),exact('2027-01-14'),'1'),rnd(exact('2026-12-01'),exact('2027-01-19'),exact('2027-04-08'),'2')],[NTU],'all','https://admissions.ntu.edu.tw/wp-content/uploads/116-1Admission-Guidelines-for-Intl-Degree-Students_ENG-1.pdf',notes=[bi('第一梯若結果為 Postponed，需等第二梯公布；尚未開放的報名系統由此官方頁進入。','ပထမအဆင့်တွင် Postponed ဖြစ်ပါက ဒုတိယအဆင့်ရလဒ်ကို စောင့်ရန် လိုသည်။')])
NCCU='https://nccuadmission.nccu.edu.tw/Post/331';nccuapply='https://admission.nccu.edu.tw/intladmission/index/index/applyIntladmissionSn/26';nccubook='https://drive.google.com/file/d/1RC6EOaByXy7hqe6_2ddinrZZk64UGu3k/view';portal('0001',nccuapply,'apply')
term('0001','spring',[rnd(exact('2026-09-22'),exact('2026-10-15'),exact('2026-11-27'))],[NCCU,'https://oic.nccu.edu.tw/Post/16113'],'graduate',nccubook,notes=[bi('116 招生第一梯容許研究所提前至 115-2 春季入學；學士不可套用春季。','ဘွဲ့လွန်လျှောက်သူများသာ 115-2 နွေဦးတွင် စော၍ ဝင်ခွင့်ယူနိုင်သည်။')])
term('0001','fall',[rnd(exact('2026-09-22'),exact('2026-10-15'),exact('2026-11-27'),'1'),rnd(exact('2027-01-19'),exact('2027-03-04'),None,'2')],[NCCU,'https://oic.nccu.edu.tw/Post/16113'],'all',nccubook,notes=[bi('簡章連結為第一梯；第一梯未招生系所可能於第二梯開放。')]);schools['0001']['terms']['fall']['programLink']='https://docs.google.com/spreadsheets/d/187k9n7AZig-AlyFjELKLgTs1BLzdL1Vg/edit'
NTHU='https://apply.nthu.edu.tw/article/70-%E7%94%B3%E8%AB%8B%E5%89%8D%E9%A0%88%E7%9F%A5';portal('0002','https://nthuoga-admission.vm.nthu.edu.tw/','apply')
term('0002','spring',[rnd(exact('2026-08-03'),exact('2026-09-30'),exact('2026-12-01'))],[NTHU],'all',NTHU)
term('0002','fall',[rnd(approx('約2026/11月下旬','2026-11-21'),approx('約2027/01月底','2027-01-21'),None,'學士 / Undergraduate'),rnd(approx('約2026/12月中旬','2026-12-11'),approx('約2027/02月下旬','2027-02-21'),None,'研究所 / Graduate')],[NTHU],notes=[bi('以 2026 秋學士 2025/11/25–2026/01/31、研究所 2025/12/15–2026/02/25 推估。2027 正式日期待核。')])
NCU='https://cis.ncu.edu.tw/admissions//menu.content/view/sn/72';portal('0008','https://cis.ncu.edu.tw/admissions/')
term('0008','spring',[rnd(exact('2026-08-01'),exact('2026-09-30'),exact('2026-11-24'))],[NCU])
term('0008','fall',[rnd(approx('約2027/01月初','2027-01-01'),approx('約2027/03月中旬','2027-03-11'),approx('約2027/05月中下旬','2027-05-11'))],[NCU],notes=[bi('前屆 2026/01/01–03/15 申請、05/20 公告正取；備取另有通知，不與正取混用。')])
NYCU='https://oia.nycu.edu.tw/oia/en/app/artwebsite/view?id=785&module=artwebsite&serno=07d9ede2-e896-4efe-a671-2b86dbc2a0d8';portal('0007','https://oia.nycu.edu.tw/oia/en/app/folder/782')
term('0007','spring',[rnd(exact('2026-08-10'),exact('2026-09-30'),exact('2026-11-13'))],[NYCU],'graduate')
term('0007','fall',[rnd(approx('約2026/12月下旬','2026-12-21'),approx('約2027/03月中旬','2027-03-11'),approx('約2027/05月中旬','2027-05-11'))],[NYCU],notes=[bi('前屆 2025/12/20–2026/03/15 申請、原訂 2026/05 月中放榜；校方註明可能隨審查進度調整。')])
NTUT='https://oia.ntut.edu.tw/p/412-1032-13828.php?Lang=en';ntutbook='https://oia.ntut.edu.tw/var/file/32/1032/img/2027SpringAdmissionHandbook.pdf';portal('0025',NTUT)
term('0025','spring',[rnd(exact('2026-08-01'),exact('2026-09-30'),dict(label=bi('11/6／11月中 · 待確認','11/6 / 11 လလယ် · အတည်ပြုရန်'),status='conflict'),note='簡章 p.i 及 p.5 為 2026/11/06；招生網頁寫 11 月中。未確認修訂先後，不擅自選一天。')],[NTUT,ntutbook],brochure=ntutbook,notes=[bi('放榜日期有官方來源衝突，因此不加入確定放榜日排序。','တရားဝင်ရင်းမြစ်နှစ်ခု၏ ရလဒ်ရက် မတူသဖြင့် အတည်ပြုရက်အဖြစ် မစီထားပါ။')])
term('0025','fall',[rnd(exact('2026-12-01'),exact('2027-03-10'),approx('2027/05月初','2027-05-01',status='official'))],[NTUT],notes=[bi('官方招生頁列出 116-1 時程；2027 秋各系是否開放仍須以該期簡章確認。')])
THU='https://exam2.thu.edu.tw/EXAM/download_doc_26/21.pdf';portal('1001','https://exam2.thu.edu.tw/EXAM/forlist.jsp')
term('1001','spring',[rnd(exact('2026-10-01'),exact('2026-10-31'),approx('2026/12月初','2026-12-01',status='official'))],[THU],'all',THU)
term('1001','fall',[rnd(approx('約2027/01月下旬','2027-01-21'),approx('約2027/02月底','2027-02-21'),approx('約2027/04月上旬','2027-04-01'),'1'),rnd(approx('約2027/03月初','2027-03-01'),approx('約2027/03月底','2027-03-21'),approx('約2027/05月初','2027-05-01'),'2'),rnd(approx('約2027/04月初','2027-04-01'),approx('約2027/04月底','2027-04-21'),approx('約2027/06月初','2027-06-01'),'3'),rnd(approx('約2027/05月初','2027-05-01'),approx('約2027/05月下旬','2027-05-21'),approx('約2027/07月初','2027-07-01'),'4')],[THU],notes=[bi('使用 115 學年度秋季四梯規劃；116 各梯日期尚待當屆公告確認。')])
PU='https://oia.pu.edu.tw/p/426-1048-11.php';portal('1008','https://mypu.pu.edu.tw/Framework/International/oia_oversea/admission/overseas?lang=en','apply')
term('1008','spring',[rnd(approx('約2026/08月初','2026-08-01','一般時程'),approx('約2026/10月中旬','2026-10-11','一般時程'),approx('約2026/12月初','2026-12-01','歷年'),'1'),rnd(approx('約2026/10月中旬','2026-10-11','一般時程'),approx('約2026/11月中旬','2026-11-11','一般時程'),approx('約2027/01月初','2027-01-01','歷年'),'2')],[PU],notes=[bi('官網一般時程第一梯 8/1–10/15、第二梯 10/16–11/15；放榜月初為提供資料所載歷年規劃，當屆仍待核。')])
term('1008','fall',[rnd(approx('約2027/01月初','2027-01-01','一般時程'),approx('約2027/04月底','2027-04-21','一般時程'),approx('約2027/06月初','2027-06-01'),'1'),rnd(approx('約2027/05月初','2027-05-01','一般時程'),approx('約2027/06月中旬','2027-06-11','一般時程'),None,'2')],[PU],notes=[bi('官網一般招生時程未指定 116 年；前屆第一梯 2026/06/04 放榜資料尚待官方複核。')])
HK='https://ifp.hk.edu.tw/入學申請/外國學生/';hkbook='https://ifp.hk.edu.tw/wp-content/uploads/2026/09/%E5%BC%98%E5%85%89115%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E6%8B%9B%E7%94%9F%E7%B0%A1%E7%AB%A0_%E4%BF%AEV2-1106.pdf';portal('1034',HK)
term('1034','spring',[rnd(exact('2026-10-05'),exact('2026-12-01'),exact('2027-01-10'))],[HK,hkbook],'all',hkbook+'#page=6',programs=[bi('春季不招：護理系學士／碩士、物理治療系、語言治療與聽力學系。','နွေဦးတွင် Nursing ဘွဲ့ကြို/မဟာဘွဲ့၊ Physical Therapy၊ Speech-Language Pathology & Audiology မလက်ခံပါ။'),bi('營養、動物保健、餐旅、國際溝通英語、化妝品、美髮、幼保、文化設計與行銷、運動休閒、多媒體遊戲等：完整學位別見簡章第 5–7 頁。','Nutrition၊ Animal Healthcare၊ Hospitality၊ English၊ Cosmetology၊ Hair Styling၊ Child Care၊ Design & Marketing၊ Sports၊ Games စသည့်ဘာသာရပ်များ။ ဘွဲ့အဆင့်ကို စာမျက်နှာ 5–7 တွင် စစ်ပါ။')],apply='https://pse.is/79fakm')
term('1034','fall',[rnd(exact('2026-10-05'),exact('2027-01-10'),exact('2027-02-25'),'1'),rnd(dict(label=bi('起訖中英不一致','စရက်/ဆုံးရက် မတူညီ'),status='conflict'),None,exact('2027-08-06'),'2',note='第二梯中文版為 2027/03/01–07/01，英文版為 2027/01/01–05/01。請向校方確認。')],[HK],notes=[bi('已核得 2027 秋招生網頁時程；網頁尚無可下載的 116 簡章，系所不可直接沿用春季。','2027 ဆောင်းဦးရက်စွဲ ရှိသော်လည်း လမ်းညွှန် မရသေးပါ။ နွေဦးဘာသာရပ်စာရင်းကို မသုံးပါနှင့်။')])
CYUT='https://icsc.cyut.edu.tw/p/406-1008-58738,r1198.php?Lang=zh-tw';portal('1018',CYUT)
term('1018','spring',[rnd(None,exact('2026-12-19'),None)],[CYUT],scope='all',notes=[bi('學士／碩士截止 2026/12/19；博士截止不同，不能套用。開始申請與放榜未核得。')])
NPTU='https://oiais.nptu.edu.tw/p/412-1090-12629.php?Lang=zh-tw';portal('0052',NPTU)
term('0052','spring',[rnd(None,exact('2026-10-15'),exact('2026-11-30'))],[NPTU])
term('0052','fall',[rnd(None,approx('約2027/04月中旬','2027-04-11'),approx('約2027/06月中旬','2027-06-11'))],[NPTU],notes=[bi('前屆 2026 秋截止 04/15、放榜 06/15；開始日未核得，不自行補入。')])
# Historical information supplied with the original school research pack: keep the uncertainty explicit.
REFNOTE=bi('日期為提供資料包的歷年參考；本次尚未完成官方附件的逐項複核，不代表本期正式公告。','ရက်စွဲများသည် ပေးထားသော ယခင်နှစ်ကိုးကားစာရင်းမှ ဖြစ်သည်။ တရားဝင်ဖိုင်နှင့် အပြည့်အစုံ ထပ်မစစ်နိုင်သေးပါ။ ယခုကာလ တရားဝင်ရက် မဟုတ်ပါ။')
FCU='https://oia.fcu.edu.tw/';portal('1007',FCU)
term('1007','spring',[rnd(approx('約2026/09月','2026-09-01','歷年'),approx('約2026/11月','2026-11-01','歷年'),approx('約2026/12月','2026-12-01','歷年'))],[FCU],notes=[REFNOTE])
term('1007','fall',[rnd(approx('約2026/12月中旬','2026-12-11'),approx('約2027/03月初','2027-03-01'),approx('約2027/03月下旬','2027-03-21'),'1'),rnd(approx('約2027/03月初','2027-03-01'),approx('約2027/04月中旬','2027-04-11'),approx('約2027/05月初','2027-05-01'),'2')],[FCU],notes=[REFNOTE])
NCNU='https://admission.ncnu.edu.tw/p/403-1055-608-1.php?Lang=zh-tw';portal('0021',NCNU)
term('0021','spring',[rnd(approx('約2026/10月下旬','2026-10-21','115春'),approx('約2026/11月中旬','2026-11-11','115春'),approx('約2027/01月初','2027-01-01','115春'))],[NCNU],notes=[REFNOTE,bi('前屆申請 2025/10/27–11/14、實際放榜 2026/01/05；2026/01/16 為入學通知寄發規劃，不能當作放榜或收到日。')])
term('0021','fall',[rnd(approx('約2026/12月下旬','2026-12-21'),approx('約2027/02月下旬','2027-02-21'),approx('約2027/04月初','2027-04-01'),'1'),rnd(None,None,approx('約2027/06月中旬','2027-06-11'),'2')],[NCNU],notes=[REFNOTE,bi('前屆第二梯開始／截止在來源資料未列明，保留空白。')])
NCUE='https://oicaweb.ncue.edu.tw/p/406-1019-24585,r142.php?Lang=zh-tw';portal('0015',NCUE)
term('0015','spring',[rnd(approx('約2026/07–11月','2026-07-01','歷年'),None,approx('約2026/11–12月','2026-11-01','歷年'))],[NCUE],notes=[REFNOTE])
term('0015','fall',[rnd(None,None,approx('約2027/04月中旬','2027-04-11'))],[NCUE],notes=[REFNOTE])
NFU='https://oia.nfu.edu.tw/';portal('0033',NFU)
term('0033','spring',[rnd(approx('約2026/09月中旬','2026-09-11','115春'),approx('約2026/10月底','2026-10-21','115春'),approx('約2026/12月初','2026-12-01','115春'))],[NFU],notes=[REFNOTE,bi('前屆 2025/09/17–10/31 申請；實際 2025/12/04 放榜，原訂 11/27 不再當作實際榜單日。')])
term('0033','fall',[rnd(approx('約2027/04月初','2027-04-01'),approx('約2027/05月中旬','2027-05-11'),approx('約2027/06月上旬','2027-06-01'))],[NFU],notes=[REFNOTE])
ASIA='https://admission.asia.edu.tw/AsiaGlobalAdmissions/ForeignStudent';portal('1048',ASIA,'apply')
term('1048','spring',[rnd(None,approx('約2026/11月底','2026-11-21','提供資料'),dict(label=bi('分梯／滾動，待核','အဆင့်လိုက်၊ အတည်ပြုရန်'),status='historical',basis='提供資料'))],[ASIA],notes=[REFNOTE])
term('1048','fall',[rnd(approx('約2027/02月下旬','2027-02-21'),None,approx('約2027/05月上旬','2027-05-01'),'1'),rnd(None,None,approx('約2027/05月底','2027-05-21'),'2')],[ASIA],notes=[REFNOTE,bi('前屆第一梯實際 2026/05/07 放榜，非原訂 04/30；不可保證滾動申請即時放榜。')])
NCHU='https://oia.nchu.edu.tw/';portal('0006',NCHU)
term('0006','spring',[],[NCHU],'graduate',notes=[bi('既有來源春季僅列碩博士；學士春季不沿用研究所日期。')])
term('0006','fall',[rnd(approx('約2027/01月中旬','2027-01-11'),approx('約2027/03月中下旬','2027-03-11'),approx('約2027/05月底','2027-05-21'))],[NCHU],notes=[REFNOTE])
YUN='https://aax.yuntech.edu.tw/';portal('0023',YUN)
term('0023','spring',[],[YUN],'graduate',notes=[bi('提供資料中的 115 春季為碩博士招生；學士不可使用研究所日期。')])
term('0023','fall',[rnd(None,None,approx('約2027/06月初','2027-06-01'))],[YUN],notes=[REFNOTE])
NCUT='https://admission.ncut.edu.tw/';portal('0043',NCUT)
term('0043','fall',[rnd(approx('約2027/03月下旬','2027-03-21'),approx('約2027/05月上旬','2027-05-01'),approx('約2027/07月中下旬','2027-07-11'))],[NCUT],notes=[REFNOTE])
portal('1062','https://admission.ocu.edu.tw/p/412-1023-5671.php')
for code,url in {'0022':'https://oia.ntust.edu.tw/','0009':'https://oia.nsysu.edu.tw/','0013':'https://oia.ccu.edu.tw/','0017':'https://oia.ntpu.edu.tw/home.jsp?lang=tw','0005':'https://oia.ncku.edu.tw/','1035':'https://cmucia.cmu.edu.tw/admission_international.html','1027':'https://admissions.tcu.edu.tw/?page_id=5125','0031':'https://isa.niu.edu.tw/'}.items():portal(code,url)
# Official schedules checked against the semester-specific notices.
NTOU='https://oia.ntou.edu.tw/p/412-1022-7231.php?Lang=en';portal('0012',NTOU)
term('0012','spring',[rnd(exact('2026-07-15'),exact('2026-10-31'),exact('2026-12-18'))],[NTOU],'graduate',NTOU,apply='https://oia.ntou.edu.tw/p/423-1022-863.php?Lang=zh-tw')
NKNU='https://oia.nknu.edu.tw/news-detail.php?id=343';nknubook='https://oia.nknu.edu.tw/uploads/news/attachments/attachment_20260119152512_696ddc588cf7c.pdf';portal('0014','https://sso.nknu.edu.tw/InternationalAdmissions/Default.aspx','apply')
term('0014','spring',[rnd(exact('2026-07-20'),exact('2026-10-15'),exact('2026-12-05'))],[NKNU,nknubook],'all',nknubook+'#page=3')
term('0014','fall',[rnd(approx('約2027/01月下旬','2027-01-21'),approx('約2027/04月中旬','2027-04-11'),approx('約2027/06月上旬','2027-06-01'))],[NKNU,nknubook],notes=[bi('依前屆 2026/01/20–04/15、06/05 放榜推估；116 正式簡章未核得。')])
NTUST='https://admissions.ntust.edu.tw/graduateapp';portal('0022',NTUST,'apply')
term('0022','spring',[rnd(exact('2026-07-01'),exact('2026-09-11'),exact('2026-10-30'))],[NTUST],'graduate',notes=[bi('10/30 是預分發錄取狀態與獎學金結果；11/30 為獎學金遞補結果及寄發錄取通知，兩者不同。','10/30 သည် ယာယီဝင်ခွင့်နှင့် ပညာသင်ဆုရလဒ် ဖြစ်သည်။ 11/30 တွင် ပညာသင်ဆုအရန်ရလဒ်နှင့် ဝင်ခွင့်စာ ပေးပို့သည်။')])
NKUST='https://oia.nkust.edu.tw/news_det-970.html';nkustbook='https://oia.nkust.edu.tw/images/upload/files/2027%E6%98%A5(115-2)%E5%A4%96%E5%9C%8B%E5%AD%B8%E7%94%9F%E6%8B%9B%E7%94%9F%E7%B0%A1%E7%AB%A0%202027%20Spring%20Semester%20International%20Student%20Admission%20Guidelines.pdf';portal('0053',NKUST)
term('0053','spring',[rnd(exact('2026-09-07'),exact('2026-10-07'),exact('2026-11-30'))],[NKUST,nkustbook],'graduate',nkustbook+'#page=19',notes=[bi('11/30 放榜；12 月上旬確認意願後才開放入學許可下載。','11/30 ရလဒ်ထွက်သည်။ တက်ရောက်မည်ဟု အတည်ပြုပြီးမှ ဒီဇင်ဘာလအစတွင် ဝင်ခွင့်စာ ရယူနိုင်သည်။')])
CUST='https://www.cust.edu.tw/enroll/international-2.html';portal('1061',CUST)
term('1061','spring',[rnd(exact('2026-11-02'),exact('2026-12-15'),approx('2027/01月','2027-01-01',status='official'))],[CUST],'all',CUST,notes=[bi('官方只公布 1 月，未提供確定放榜日；招生四技及碩士。','တရားဝင်ကြေညာချက်တွင် ဇန်နဝါရီလဟုသာ ဖော်ပြသည်။ ဘွဲ့ကြိုနှင့် မဟာဘွဲ့ လက်ခံသည်။')])
term('1061','fall',[rnd(approx('約2027/02月下旬','2027-02-21'),approx('約2027/06月中旬','2027-06-11'),approx('約2027/08月','2027-08-01'))],[CUST],notes=[bi('依 2026 秋 02/23–06/12 申請、8 月放榜推估；116 日期待公告。')])
CGUS='https://www.cgu.edu.tw/recruit_intl-ch/Subject/Detail/70660?nodeId=14133';CGUF='https://www.cgu.edu.tw/recruit_intl-ch/Subject/Detail/83974?nodeId=14133';portal('1009','https://recruit-intl.cgu.edu.tw/','apply')
term('1009','spring',[rnd(exact('2026-08-03'),exact('2026-09-25'),None)],[CGUS],brochure='https://drive.google.com/file/d/1GfUGXVXaxL7PiOr72w5tM1UBW2Iwdet6/view')
term('1009','fall',[rnd(exact('2026-09-25'),exact('2026-11-17'),None,'1'),rnd(exact('2026-12-29'),exact('2027-02-20'),None,'2')],[CGUF],brochure='https://drive.google.com/file/d/12V5elgjqLkb6pbukFOpLTRh5xZTd4DxQ/view')
NDHU='https://oia.ndhu.edu.tw/p/412-1027-21529.php?Lang=en';ndhubook='https://oia.ndhu.edu.tw/var/file/27/1027/img/4756/894840940.pdf';portal('0020',NDHU)
term('0020','spring',[rnd(exact('2026-09-01'),dict(label=bi('簡章10/31；網頁年份有誤','လမ်းညွှန် 10/31; ဝက်ဘ်နှစ် မတူ'),status='conflict'),dict(label=bi('簡章12/20；網頁不一致','လမ်းညွှန် 12/20; ဝက်ဘ်နှင့် မတူ'),status='conflict'))],[NDHU,ndhubook],'all',ndhubook+'#page=5',notes=[bi('115 簡章中英均列截止 2026/10/31、放榜 2026/12/20；官網 2027 春欄卻寫截止 2025/10/31、放榜 2025/12/15。保留衝突，向校方確認。','လမ်းညွှန်တွင် 2026/10/31 နောက်ဆုံးရက်၊ 2026/12/20 ရလဒ်ဟု ရှိသော်လည်း ဝက်ဘ်စာမျက်နှာတွင် 2025 ခုနှစ် ရက်စွဲများ ဖြစ်နေသည်။ ကျောင်းနှင့် အတည်ပြုပါ။')])
term('0020','fall',[rnd(approx('約2027/01月初','2027-01-01'),approx('約2027/03月中旬','2027-03-11'),approx('約2027/05月上旬','2027-05-01'),'1'),rnd(approx('約2027/03月中旬','2027-03-11'),approx('約2027/04月中旬','2027-04-11'),approx('約2027/06月上旬','2027-06-01'),'2')],[NDHU,ndhubook],notes=[bi('依 2026 秋兩梯 01/02–03/15、03/16–04/14；05/10、06/10 放榜推估。')])
TSUST='https://forstud.tsust.edu.tw/p/412-1024-365.php';portal('1042',TSUST)
term('1042','spring',[rnd(None,exact('2026-12-18'),None)],[TSUST],notes=[bi('官網「即日起」無發布日，無法確定開始日；2027/01/05 標示寄發入學許可，不能代替放榜日。','ဝက်ဘ်တွင် စတင်ရက် မပါပါ။ 2027/01/05 သည် ဝင်ခွင့်စာပို့ရက် ဖြစ်ပြီး ရလဒ်ကြေညာရက် မဟုတ်ပါ။')])
term('1042','fall',[rnd(None,approx('約2027/07月下旬','2027-07-21'),None)],[TSUST],notes=[bi('前屆截止 2026/07/20，開始與放榜無法分別核得。')])
NTCU='https://insch.ntcu.edu.tw/en/news_detail.php?sn=16';portal('0039','https://insch.ntcu.edu.tw/en/','apply')
term('0039','spring',[rnd(exact('2026-08-01'),exact('2026-10-31'),None)],[NTCU],'all','https://insch.ntcu.edu.tw/en/enroll_detail.php?sn=7')
term('0039','fall',[rnd(None,approx('約2027/04月底','2027-04-21'),approx('約2027/06月中旬','2027-06-11'))],['https://insch.ntcu.edu.tw/en/'],notes=[bi('依校方前屆 2026/04/30 截止、2026/06/17 實際公告推估。')])
# Additional verified records can be appended without changing registry identity.
extra=ROOT/'verified_extra.json'
if extra.exists():
    for code,patch in json.loads(extra.read_text()).items():
        for key,value in patch.items():
            if key=='terms':schools[code]['terms'].update(value)
            else:schools[code][key]=value
out=dict(updated='2026-09-19',registryYear='115',registrySource='https://stats.moe.gov.tw/files/opendata/u1_new.json',cities=CITIES,schools=list(schools.values()))
(ROOT.parent/'dist'/'schools.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('Schools:',len(schools),'with date information:',sum(any(s['terms'][t]['rounds'] for t in ['spring','fall']) for s in schools.values()))
