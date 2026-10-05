# -*- coding: utf-8 -*-
"""列出選校板每校還缺的資料 → 寫成 待補清單.md（給 ChatGPT / Claude 接手補資料用）。
執行：python3 research/weiquan-board-2026-09-29/gaps.py
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
b = json.loads((ROOT/'dist/wq-board.json').read_text())
A, T = b['arcExpiry'], b['updated']
TIER = {'A': '第一優先', 'P': '名校', 'B': '備選', 'C': '低優先'}
rows = []
for s in sorted(b['schools'], key=lambda x: ('APBC'.index(x['tier']), x['km'])):
    g = []
    f = s['fee']
    if f['kind'] in ('silent', 'unknown'):
        g.append('申請費：' + ('簡章沒寫' if f['kind'] == 'silent' else '讀不到'))
    for term in ('spring', 'fall'):
        TT = s['terms'][term]
        if TT['ug'] == 'unknown':
            g.append(('春季' if term == 'spring' else '秋季') + '：學士有沒有開不知道')
        for i, r in enumerate(TT.get('rounds') or [], 1):
            res = r.get('result') or {}
            if not (res.get('date') or res.get('sort')):
                g.append(f"{'春' if term == 'spring' else '秋'}季第{i}梯：放榜日沒有")
    if s['firstYearKind'] == 'unknown':
        g.append('新生獎學金：沒查到')
    if not s['aid'].get('sure') and not s['aid'].get('review'):
        g.append('獎學金條件：空白')
    if not s['renew'] or s['renew'].strip() in ('—', '-') or '沒查到' in s['renew']:
        g.append('續領方式：沒查到')
    if not s.get('tuition'):
        g.append('學雜費：沒有數字')
    if not s.get('bizAdmits'):
        g.append('商管系上榜人數：還沒數')
    links = list(dict.fromkeys(s['links'].get(k) for k in ('brochureFall', 'brochureSpring') if s['links'].get(k)))
    if f.get('src') and f['src'] not in links: links.append(f['src'])
    rows.append((s, g, links))

out = [f'# 選校板待補清單（{T} 產生）', '',
       f'共 {len(rows)} 校。ARC 到期 {A}：放榜晚於這天的梯次不要加。',
       '每補一項，都要附官方網址與學年度；簡章沒寫申請費 ≠ 免費。', '',
       '| 優先 | 學校 | 還缺什麼 | 從哪裡查 |', '|---|---|---|---|']
for s, g, links in rows:
    out.append(f"| {TIER[s['tier']]} | {s['id']} {s['short']} | {'<br>'.join(g) or '（大致齊全）'} | {'<br>'.join(f'[連結{i}]({u})' for i, u in enumerate(links[:3], 1)) or '學校官網'} |")
(ROOT/'待補清單.md').write_text('\n'.join(out) + '\n')
print('wrote 待補清單.md,', sum(1 for _, g, _ in rows if g), 'schools with gaps')
