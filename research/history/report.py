"""Build the public coverage audit from shipped data, without separate counts."""
import json,csv,io
from pathlib import Path
from html import escape as h
root=Path(__file__).resolve().parents[2]
data=json.loads((root/'dist/schools.json').read_text())
labels={'official':'官方公告 · တရားဝင်','historical':'歷年參考 · ယခင်နှစ်ကိုးကား','estimated':'歷年推估 · ခန့်မှန်း','unknown':'尚未核得 · မအတည်ပြုရသေး'}
summary=data['coverage']
def status(s,term):
 return next(k for k,v in summary[term]['schools'].items() if any(x['id']==s['id'] for x in v))
def namelist(items):return '、'.join(h(s['name']+' '+s['abbr']) for s in items) or '—'
parts=['''<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>139校時程資料報告｜臺灣選校</title><style>@font-face{font-family:Myanmar;src:url('./fonts/Padauk-Regular.ttf')}*{box-sizing:border-box}body{font:16px/1.8 system-ui,Myanmar,sans-serif;color:#172b32;background:#f5f7f7;margin:0}main{max-width:1100px;margin:auto;padding:30px 20px}h1{font-size:28px}h2{font-size:22px;margin-top:36px}a{color:#087262}section,details{background:white;border:1px solid #d7e3e0;border-radius:12px;padding:18px;margin:16px 0}.scroll{overflow:auto}table{border-collapse:collapse;width:100%;min-width:620px}td,th{padding:12px;text-align:left;border-bottom:1px solid #d7e3e0}summary{cursor:pointer;font-weight:650}.muted{color:#50636a}.links{display:flex;gap:20px;flex-wrap:wrap}.small{font-size:14px}li{margin-bottom:8px}article{border-top:1px solid #d7e3e0;padding:14px 0;overflow-wrap:anywhere}@media print{details{break-inside:avoid}a{color:inherit}}</style><main><a href="./">← 臺灣選校 · ကျောင်းရွေးရန်</a><h1>139 校招生時程資料報告</h1><p>ဝင်ခွင့်အချိန်ဇယား အချက်အလက်အစီရင်ခံစာ · 2026-09-27</p><p>2027 秋季 = 116-1；2027 春季 = 115-2。每校每季以最高已核得狀態計入一次；有任一開始、截止或放榜日期即納入。部分資料僅適用研究所或指定系所，請看學校詳情。</p><p class="muted">尚未核得不代表不招生。139 校為既有教育部校單，含專科及停招註記學校；不是 139 校均已確認本期招收外國學生。歷年日期保留原始年度，不是 2027 正式日期。</p><p lang="my">ယခင်နှစ်ရက်စွဲများသည် 2027 တရားဝင်ရက်စွဲများ မဟုတ်ပါ။ အချက်အလက်မရှိခြင်းသည် ကျောင်းသားမခေါ်ယူဟု မဆိုလိုပါ။ ဘွဲ့လွန်နှင့် သတ်မှတ်ဘာသာရပ်များအတွက်သာ ဖြစ်နိုင်သည်။</p><div class="links"><a href="coverage.csv" download>下載逐校清單 CSV</a><a href="admission-records.json" download>原始年度與來源 JSON</a><a href="coverage.json" download>統計 JSON</a></div><section><div class="scroll"><table><thead><tr><th>入學學期</th><th>官方公告</th><th>歷年參考</th><th>歷年推估</th><th>尚未核得</th><th>總校數</th></tr></thead><tbody>''']
for term,title in [('fall','116-1 秋季'),('spring','115-2 春季')]:
 c=summary[term]['counts'];parts.append('<tr><th>'+title+'</th>'+''.join('<td>'+str(c[k])+'</td>' for k in labels)+'<td>139</td></tr>')
parts.append('''</tbody></table></div></section><h2>本次修改</h2><ul><li>補入可追溯的年度招生時程；缺項保留空值，原版資料已備份，替換資料保留於歷年詳情。</li><li>加入開始、截止、放榜三種日期排序，歷年區間參與排序；狀態僅在時間相同時作為次序判準。</li><li>歷年標示可展開來源年度、原始日期、適用範圍及來源連結；收藏匯出包含狀態與來源。</li><li>靜宜春季以115簡章11/30、12/24放榜取代舊資料包的約12月初、1月初。中教大秋季採115簡章6/18預定放榜；寄發通知另外保存。</li><li>朝陽依學士／碩士與博士分列截止；嶺東7月審查期不當成第二梯申請。正式入學許可不當成放榜。</li><li>中原、北科、大同、文化、嘉義、宜蘭、玄奘、大葉等來源差異保留說明，有爭議欄位不提供單一日期排序。</li><li>暨南已另核114-2春季原始簡章，保留原始2025申請、2026放榜日期；虎尾原資料包含糊標籤仍待複核。</li></ul><h2>統計範圍與待確認</h2><p>包含原版保留資料；原資料包尚未重新核得的歷年欄位標低可信度，與本輪官方來源紀錄分開。每校未必三項俱全，也未必適用學士班。本次沒有足夠一致的多年度證據，因此未新增「歷年推估」。</p><p>僑光等學校已找到招生入口或簡章線索，但部分附件無法核讀，仍保留「尚未核得」；不把搜尋摘要升格為官方日期。多數秋季學校仍需確認116-1正式簡章。以下清單是資料缺口，不是停招名單。</p>''')
for term,title in [('fall','116-1 秋季'),('spring','115-2 春季')]:
 items=summary[term]['schools']['unknown'];parts.append(f'<section><h2>{title}：尚未核得 {len(items)} 校</h2><p>{namelist(items)}</p></section>')
both=[s for s in data['schools'] if all(status(s,t)=='unknown' for t in ['spring','fall'])]
parts.append(f'<details><summary>春秋兩季均尚未核得：{len(both)} 校</summary><p>{namelist(both)}</p></details><h2>逐校來源與原始年度</h2>')
rows=[['schoolId','學校','簡稱','城市','116-1秋季','115-2春季']]
for s in sorted(data['schools'],key=lambda s:('臺中市' not in s['cities'],s['cities'][0],s['id'])):
 rows.append([s['id'],s['name'],s['abbr'],'/'.join(s['cities']),status(s,'fall'),status(s,'spring')])
 parts.append(f'<details><summary>{h(s["name"])} {h(s["abbr"])} · {h("／".join(s["cities"]))}</summary>')
 for term,title in [('fall','116-1 秋季'),('spring','115-2 春季')]:
  parts.append(f'<h3>{title} — {labels[status(s,term)]}</h3>')
  for r in s['terms'][term]['admissionRecords']:
   if r.get('archived'):continue
   dates='；'.join(n+'：'+h(str(r.get(k) or r.get(k+'Text') or '尚未核得')) for k,n in [('applicationStart','開始'),('applicationEnd','截止'),('resultDate','放榜')])
   parts.append('<article><strong>'+h(str(r.get('sourceYear') or '年度待確認'))+' · '+h(str(r.get('round') or ''))+'</strong><p>'+dates+'</p>')
   parts.append('<p class="small">'+h(str(r.get('scope') or '適用系所以簡章為準'))+' · '+h(str(r.get('sourceTitle') or '尚無可靠日期來源'))+'</p>')
   if r.get('note'):parts.append('<p>'+h(r['note'])+'</p>')
   if r.get('conflicts'):parts.append('<p>官方資料存在差異，待確認：'+h(json.dumps(r['conflicts'],ensure_ascii=False))+'</p>')
   for u in dict.fromkeys(r.get('sourceUrls') or [r.get('sourceUrl')]):
    if u and u.startswith(('http://','https://')):parts.append('<p><a target="_blank" rel="noopener noreferrer" href="'+h(u,quote=True)+'">'+h(u)+'</a></p>')
   parts.append('</article>')
 parts.append('</details>')
parts.append('</main></html>')
(root/'dist/coverage-report.html').write_text(''.join(parts))
with (root/'dist/coverage.csv').open('w',encoding='utf-8-sig',newline='') as f:csv.writer(f,lineterminator='\n').writerows(rows)
print('Report: 139 schools;',len(both),'unknown in both semesters')
