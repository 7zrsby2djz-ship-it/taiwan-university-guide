"""Project the CC0 g0v county topology into dependency-free SVG paths."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
j=json.loads((ROOT/'research/map/counties.topo.json').read_text())
arcs=[]
for arc in j['arcs']:
    x=y=0; points=[]
    for dx,dy in arc:
        x+=dx;y+=dy
        points.append((x*j['transform']['scale'][0]+j['transform']['translate'][0],y*j['transform']['scale'][1]+j['transform']['translate'][1]))
    arcs.append(points)
def ring(ids):
    out=[]
    for i in ids:
        p=arcs[i] if i>=0 else arcs[~i][::-1]
        out.extend(p if not out else p[1:])
    return out
def area(p):return abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(p,p[1:]+p[:1])))/2
out=[]
insets={'金門縣':(10,330),'澎湖縣':(10,410),'連江縣':(10,490)}
# Label offsets distinguish small adjacent municipalities without altering borders.
labels={'臺北市':(306,24),'基隆市':(385,54),'新北市':(366,89),'新竹市':(194,92),'新竹縣':(283,119),'嘉義市':(128,294),'嘉義縣':(199,319),'桃園市':(250,68)}
for g in j['objects']['layer1']['geometries']:
    name=g['properties']['COUNTYNAME'].replace('台','臺').replace('桃園縣','桃園市')
    polygons=g['arcs'] if g['type']=='MultiPolygon' else [g['arcs']]
    rings=[ring(r) for poly in polygons for r in poly]
    if name in insets:
        ox,oy=insets[name];ps=[p for r in rings for p in r];xs,ys=zip(*ps)
        scale=min(68/(max(xs)-min(xs)),38/(max(ys)-min(ys)))
        cx=(max(xs)+min(xs))/2;cy=(max(ys)+min(ys))/2
        project=lambda p:(ox+40+(p[0]-cx)*scale,oy+23-(p[1]-cy)*scale)
    else:
        project=lambda p:(130+(p[0]-120)*126,10+(25.4-p[1])*148)
    projected=[[project(p) for p in r] for r in rings]
    largest=max(projected,key=area)
    a=sum(p[0]*q[1]-q[0]*p[1] for p,q in zip(largest,largest[1:]+largest[:1]))
    cx=sum((p[0]+q[0])*(p[0]*q[1]-q[0]*p[1]) for p,q in zip(largest,largest[1:]+largest[:1]))/(3*a)
    cy=sum((p[1]+q[1])*(p[0]*q[1]-q[0]*p[1]) for p,q in zip(largest,largest[1:]+largest[:1]))/(3*a)
    label=labels.get(name,(cx,cy))
    if name in insets:label=(insets[name][0]+40,insets[name][1]+59)
    path=''.join('M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in p)+'Z' for p in projected)
    out.append(dict(name=name,path=path,label=[round(v,1) for v in label],center=[round(cx,1),round(cy,1)],inset=insets.get(name)))
(ROOT/'dist/map-paths.js').write_text('// Derived from g0v/twgeojson (CC0); see map-sources.txt.\nexport const countyPaths='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\n')
print('Generated',len(out),'county paths')
