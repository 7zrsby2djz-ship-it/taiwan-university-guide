import json, re, base64, time, hashlib, sys
from pathlib import Path
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parent
RAW=ROOT/'raw'; RAW.mkdir(parents=True,exist_ok=True)
S=requests.Session(); S.headers['User-Agent']='Mozilla/5.0 (compatible; education directory research)'

def fetch(url):
    key=hashlib.sha256(url.encode()).hexdigest()[:18]; p=RAW/(key+'.json')
    if p.exists(): return json.loads(p.read_text())
    try:
        r=S.get(url,timeout=(8,14)); r.raise_for_status()
        if len(r.content)>6000000: raise ValueError('large response')
        if 'pdf' in r.headers.get('Content-Type','') or r.content[:4]==b'%PDF':
            from pypdf import PdfReader
            import io
            text='\n'.join(pg.extract_text() or '' for pg in PdfReader(io.BytesIO(r.content)).pages)
            result=dict(url=url,final=r.url,text=text,links=[],kind='pdf',ok=True)
        else:
            r.encoding=r.apparent_encoding or 'utf-8'; s=BeautifulSoup(r.text,'html.parser')
            links=[dict(text=a.get_text(' ',strip=True),url=urljoin(r.url,a['href'])) for a in s.select('a[href]')]
            for x in s(['script','style','noscript']): x.decompose()
            result=dict(url=url,final=r.url,text=s.get_text('\n',strip=True),links=links,kind='html',ok=True)
            (RAW/(key+'.html')).write_text(r.text)
    except Exception as e: result=dict(url=url,ok=False,error=str(e)[:180],links=[],text='')
    p.write_text(json.dumps(result,ensure_ascii=False)); return result

def registry():
    data=json.loads((ROOT.parent.parent/'moe.source').read_text()); rows=[r for r in data if r['學年度']=='115']
    (ROOT/'moe115.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
    return rows

def sit_list():
    def page(n):
        url=f'https://www.studyintaiwan.org/how-to-apply/school?p={n}'; f=fetch(url)
        if not f['ok']: return []
        key=hashlib.sha256(url.encode()).hexdigest()[:18]; s=BeautifulSoup((RAW/(key+'.html')).read_text(),'html.parser')
        out=[]
        for item in s.select('.item'):
            title=item.select_one('.school-info .title')
            if not title:continue
            web=item.select_one('.school-btn a.onw'); prog=item.select_one('a[href*="/program?"]'); email=item.select_one('a[data-email]'); im=item.select_one('img')
            q=None; code=None; abbr=None
            if prog:
                q=prog['href'].split('q=')[-1]; val=base64.b64decode(q+'='*(-len(q)%4)).decode(); parts=val.split('=')[-1].rsplit('-',2)
                if len(parts)==3:abbr,code,_=parts
            out.append(dict(name=title.text.strip(),website=web['href'] if web else None,program=urljoin(url,prog['href']) if prog else None,code=code,abbr=abbr,email=email.get('data-email') if email else None))
        return out
    out=[]
    with ThreadPoolExecutor(max_workers=5) as ex:
        for fut in as_completed([ex.submit(page,n) for n in range(1,15)]):out+=fut.result()
    (ROOT/'sit-schools.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print('SIT',len(out),flush=True)

def linkscore(text,url):
    t=text.lower(); u=url.lower(); score=0
    if any(s in t for s in ['外國學生','外國生','international student','foreign student','degree student']):score+=45
    if any(s in t for s in ['招生簡章','application guideline','admission brochure','申請入學']):score+=22
    if any(s in t for s in ['國際事務','國際暨','國際及','國際處','國際合作','國際專修','international affair','international office']):score+=17
    if any(s in t for s in ['admission','招生資訊','招生專區']):score+=9
    if re.search(r'(^|[./])oia[./]|admission|international|foreign',u):score+=5
    if re.search(r'2027|115|2026|116',t):score+=4
    if any(s in t for s in ['僑生','港澳','陸生','exchange','交換','華語中心','出國','訪問','赴外','獎學金','scholarship']):score-=30
    return score

def crawl_one(r):
    code=r['代碼']; dest=ROOT/(code+'.json')
    if dest.exists():return code
    start=r['網址'].replace('http://','https://'); pages=[]; seen=set()
    f=fetch(start); pages.append(f); seen.add(start)
    base=urlparse(start).hostname.split('.')[-3:]; domain='.'.join(base)
    def pick(pages,n):
        candidates={}
        for pg in pages:
            for a in pg.get('links',[]):
                u=a['url'].split('#')[0]
                if u in seen or not u.startswith(('http://','https://')):continue
                h=urlparse(u).hostname or ''
                if not h.endswith(domain):continue
                score=linkscore(a['text'],u)
                if score>8:candidates[u]=max(candidates.get(u,0),score)
        return [u for u,v in sorted(candidates.items(),key=lambda x:-x[1])[:n]]
    for _ in range(2):
        chosen=pick(pages,3)
        for u in chosen:seen.add(u);pages.append(fetch(u))
    result=dict(code=code,name=r['學校名稱'],pages=pages)
    dest.write_text(json.dumps(result,ensure_ascii=False));print(code,r['學校名稱'],sum(x['ok'] for x in pages),flush=True)
    return code

if __name__=='__main__':
    rows=registry()
    if sys.argv[-1]=='list': sit_list()
    else:
        with ThreadPoolExecutor(max_workers=10) as ex:
            list(ex.map(crawl_one,rows))
