import json
from pathlib import Path
from html import escape as h
R=Path(__file__).resolve().parents[2];H=Path(__file__).resolve().parent
facts=json.loads((H/'facts.json').read_text());data=json.loads((R/'dist/schools.json').read_text());ss={s['id']:s for s in data['schools']};ins=json.loads((R/'dist/school-insights.json').read_text())['schools']
confirmed=[id for id,v in facts.items() if v['applicationFee']['amount'] is not None];free=[id for id in confirmed if facts[id]['applicationFee']['amount']==0]
names=lambda ids:'、'.join(ss[id]['short']+' '+ss[id]['abbr'] for id in ids)
parts=['''<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>17校官方資料核對｜臺灣選校</title><style>*{box-sizing:border-box}body{margin:0;background:#f4f7f4;color:#173127;font:17px/1.8 system-ui,sans-serif}main{max-width:1000px;margin:auto;padding:28px 18px}h1{font-size:28px}h2{font-size:22px}h3{font-size:18px}a{color:#156649;overflow-wrap:anywhere}section,details{background:white;padding:20px;border:1px solid #d3e1d7;border-radius:12px;margin:16px 0}summary{cursor:pointer;font-size:19px;font-weight:700}article{border-top:1px solid #d3e1d7;margin-top:18px;padding-top:12px}.muted{color:#526258}.links{display:flex;flex-wrap:wrap;gap:16px}li{margin:8px 0}p{overflow-wrap:anywhere}</style><main><a href="./?lang=zh&audited=1">← 已核對學校快速篩選</a><h1>彰師・暨南・聯合等17校官方資料核對</h1><p>查核日期：2026-09-27。本頁列出本批成果與缺口；「已核對」表示完成一輪官方資料核對，不表示每個欄位都有答案。</p><p>快速篩選共28校：前批臺中11校＋本批17校。保留139校原名單；未新增學校、不做錄取難度的新判定。</p>''']
parts.append(f'<section><h2>本批範圍</h2><p>{h(names(facts))}</p><p>申請費已有明文依據：{len(confirmed)}校，其中明確免收{len(free)}校。仍無可靠全校金額：{h(names(id for id in facts if id not in confirmed))}。部分費用僅涵蓋某季或特定學位，不能跨季或跨身分直接套用。</p><p>有官方原始榜單或結果查詢公告：{sum(bool(v.get("admissionNotices")) for v in facts.values())}校。只提供連結；不下載解析名冊、不保存學生個資、不計算錄取率。</p></section>')
parts.append('''<section><h2>重要修正</h2><ul><li>清華115秋季學士與研究所分開；學士簡章放榜4/24保留原始年度。一般春季招生不能被錯限成研究所。</li><li>中央、陽明交大、臺科、雲科春季研究所時程明確標示，不當作學士申請。</li><li>成大115起新獎學金制度與113／114舊制分開；臺科獎學金區分英文研究所、中文研究所與學士。</li><li>政大申請費按最新116簡章列每件1,600元；臺大、清華、陽明交大保留多志願與免收例外，不把例外寫成全校免費。</li><li>臺北大學春季本期申請期間保留官方值，尚缺本期放榜時用114-2放榜作歷年參考；北科秋季正式日期改正來源年度為116-1。</li><li>臺師大秋季第二梯3/2與系所3/16差異保留；北科春季11/6與11月中旬差異保留，爭議欄位不選一日排序。</li><li>聯合115秋季官方指定表單只放秋季；雲科目前春季申請系統不套用到秋季。</li></ul></section><section><h2>年度與保留缺口</h2><p>116秋季已公布的資料直接採用；其餘以115秋季參考。春季優先115-2，暨南保留114-2原始簡章。原始精確日期留於資料層，卡片上的歷年月份區間不代表2027正式日期。</p><p>獎學金採本次查得官方現行頁引用的辦法並保留版本；舊辦法不寫成2027新制。沒有最新名額、續領門檻或明確收費的欄位保留缺口。</p></section><div class="links"><a href="school-insights.json" download>費用、獎學金與榜單 JSON</a><a href="admission-records.json" download>原始年度招生時程 JSON</a><a href="taichung-audit.html">前一批臺中11校</a></div>''')
for id in facts:
 s=ss[id];v=ins[id];f=v['applicationFee'];amount='未核得全校明確金額' if f['amount'] is None else ('NT$0／官方明確免收' if f['amount']==0 else 'NT$'+format(f['amount'],','))
 parts.append(f'<details id="{id}"><summary>{h(s["name"])} {h(s["abbr"])} · 部分完整</summary><h3>申請費：{h(amount)}</h3><p>{h(f["academicYear"] or "年度未明")} · {h("／".join("春季" if t=="spring" else "秋季" for t in f["intakes"]))}</p><p>{h(f["notes"])}</p><a href="{h(f["sourceUrl"],quote=True)}" target="_blank" rel="noopener">官方費用依據／待確認文件 ↗</a>')
 for sch in v['scholarships']:
  parts.append('<article><h3>'+h(sch['scope'])+'</h3><p>'+h(sch['award'])+'</p><p>'+h(sch['continuation'])+'</p><p class="muted">'+h(sch['academicYear'])+'</p><a target="_blank" rel="noopener" href="'+h(sch['sourceUrl'],quote=True)+'">官方制度 ↗</a></article>')
 parts.append('<h3>官方原始榜單／結果公告</h3><ul>')
 for n in v['admissionNotices']:parts.append('<li><a target="_blank" rel="noopener" href="'+h(n['sourceUrl'],quote=True)+'">'+h(n['sourceTitle'])+'</a></li>')
 if not v['admissionNotices']:parts.append('<li>尚未找到官方公開原始榜單；個人結果仍以校方系統為準。</li>')
 parts.append('</ul><h3>尚待確認</h3><ul>'+''.join('<li>'+h(x)+'</li>' for x in v['audit']['gaps'])+'</ul></details>')
parts.append('</main></html>');(R/'dist/national-audit.html').write_text(''.join(parts))
print('Report:17; confirmed fees',len(confirmed),'explicit free',len(free),'with notices',sum(bool(v.get('admissionNotices')) for v in facts.values()))
