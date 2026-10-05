import assert from 'node:assert/strict';
import fs from 'node:fs';
import {parseHTML} from 'linkedom';
import {selectSchools,defaults,firstEvent,eventKey,validateFilter} from './dist/core.js';
const data=JSON.parse(fs.readFileSync(new URL('./dist/schools.json',import.meta.url)));
const insights=JSON.parse(fs.readFileSync(new URL('./dist/school-insights.json',import.meta.url)));
const registry=JSON.parse(fs.readFileSync(new URL('./research/moe115.json',import.meta.url)));
assert.equal(data.schools.length,139);
assert.deepEqual(data.schools.map(s=>s.id).sort(),registry.map(s=>s['代碼']).sort());
for(const s of data.schools){
 assert.ok(s.short&&s.abbr&&s.cities.length);
 for(const tm of ['spring','fall']) for(const r of s.terms[tm].rounds) for(const k of ['start','end','result']){
  const e=r[k];if(!e)continue;
  if(e.date)assert.equal(e.status,'official');
  if(e.status==='historical')assert.ok(!e.date&&e.label.zh);
  if(e.status==='conflict')assert.equal(eventKey(e),null);
 }
}
const ntut=data.schools.find(s=>s.id==='0025');
assert.equal(firstEvent(ntut,'spring','result').status,'conflict');
const sorted=selectSchools(data.schools,{...defaults,priorities:['city','difficulty-desc','result']});
assert.equal(sorted[0].cities.includes('臺中市'),true);
let nonCity=false;for(const s of sorted){if(!s.cities.includes('臺中市'))nonCity=true;else assert.equal(nonCity,false);}
for(const key of ['start','end','result']){
 let unknown=false;for(const s of selectSchools(data.schools,{...defaults,priorities:[key,'city','name']})){
  if(!eventKey(firstEvent(s,'spring',key)))unknown=true;else assert.equal(unknown,false);
 }
}
assert.throws(()=>validateFilter({priorities:['city','city','start']},Object.keys(data.cities)));
assert.throws(()=>validateFilter({term:'winter'},Object.keys(data.cities)));
const {window,document}=parseHTML(fs.readFileSync(new URL('./dist/index.html',import.meta.url),'utf8'));
globalThis.window=window;globalThis.document=document;
globalThis.location=new URL('https://example.test/?lang=zh');globalThis.history={replaceState:(a,b,url)=>{globalThis.location=new URL(url,location)}};
const saved=new Map();globalThis.localStorage={getItem:k=>saved.get(k)||null,setItem:(k,v)=>saved.set(k,v)};
globalThis.fetch=async url=>({ok:true,json:async()=>String(url).includes('school-insights')?insights:data});
window.HTMLElement.prototype.scrollIntoView=function(){};
const dialog=document.querySelector('dialog');dialog.showModal=function(){this.open=true;};dialog.close=function(){this.open=false;};
const tools=new Map();document.modelContext={registerTool:t=>tools.set(t.name,t)};
await import('./dist/app.js');
const click=selector=>{const el=document.querySelector(selector);assert.ok(el,selector);el.dispatchEvent(new window.Event('click',{bubbles:true}));};
assert.equal(document.querySelectorAll('article.school').length,12);
assert.equal(document.querySelector('.result-count').textContent,'139');
click('[data-lang="my"]');assert.equal(document.documentElement.lang,'my');
click('[data-term="fall"]');assert.ok(document.body.className.includes('fall'));
click('[data-lang="zh"]');
const filter=tools.get('filter_taiwan_schools');assert.ok(filter);
const result=filter.execute({city:'臺中市',priorities:['city','difficulty-desc','result']});
assert.ok(result.count>0);assert.ok(result.firstSchools.every(s=>s.cities.includes('臺中市')));
assert.equal(Number(document.querySelector('.result-count').textContent),result.count);
const first=document.querySelector('[data-save]').dataset.save;click('[data-save]');assert.ok(JSON.parse(saved.get('tsf-saved')).includes(first));
click('[data-action="favorites"]');assert.equal(document.querySelector('.result-count').textContent,'1');
click('[data-detail]');assert.equal(dialog.open,true);assert.ok(document.querySelector('#dialog-body').textContent.includes('116 學年度第 1 學期'));
click('[data-action="close"]');assert.equal(dialog.open,false);
filter.execute({favorites:false,city:'臺中市',q:'NCHU',term:'fall'});
click('[data-detail]');
assert.ok(document.querySelector('.school-insights'));
assert.ok(document.querySelector('.original-list a').href.includes('nchu.edu.tw'));
assert.equal(document.querySelectorAll('.insight-total,.insight-row').length,0);
assert.ok(document.querySelector('.fee-result').textContent.includes('未找到可靠申請費'));
assert.ok(document.querySelector('.source-year').textContent.includes('115'));
click('[data-action="close"]');
filter.execute({q:'FCU'});click('[data-detail]');
assert.ok(document.querySelector('.school-insights').textContent.includes('官方原始榜單'));
assert.ok(document.querySelector('.fee-result').textContent.includes('未找到可靠申請費'));
assert.ok(document.querySelector('.scholarship-conditions').textContent.includes('70'));
click('[data-action="close"]');
click('[data-lang="my"]');filter.execute({q:'PU'});click('[data-detail]');
assert.ok(document.querySelector('.school-insights').textContent.includes('လျှောက်လွှာကြေး'));
click('[data-action="close"]');click('[data-lang="zh"]');
filter.execute({favorites:false,city:'',q:'NTUT',term:'spring'});assert.equal(document.querySelector('.result-count').textContent,'1');
assert.ok(document.querySelector('.dates').textContent.includes('11/6'));
filter.execute({q:'zzzzzz'});assert.ok(document.querySelector('.empty'));
click('[data-action="reset"]');assert.equal(document.querySelector('.result-count').textContent,'139');
click('[data-action="sources"]');assert.ok(document.querySelector('#dialog-body').textContent.includes('139'));
for(const a of document.querySelectorAll('a[target="_blank"]'))assert.ok(a.rel.includes('noopener'));
console.log('PASS: registry coverage, date provenance, conflict visibility, three-priority ordering, unknowns last, bilingual toggle, semester selection, filtering, bookmarks, details, empty-state recovery, and tool function readback. DOM simulation only; no browser visual QA.');

const coverage=JSON.parse(fs.readFileSync('./dist/coverage.json'));
for(const term of ['fall','spring'])assert.equal(Object.values(coverage[term].counts).reduce((a,b)=>a+b,0),139);
for(const school of data.schools)for(const term of ['fall','spring'])for(const r of school.terms[term].admissionRecords){
 for(const key of ['schoolId','semester','targetYear','sourceYear','applicationStart','applicationEnd','resultDate','status','confidence','sourceTitle','sourceUrl','lastChecked'])assert.ok(key in r,key);
 if(r.status==='official')assert.equal(r.sourceYear,r.targetYear);
 if(r.sourceType==='official-primary'&&r.status==='historical')assert.notEqual(r.sourceYear,r.targetYear);
}
const fake=(id,e)=>({id,abbr:id,name:id,short:id,english:id,cities:[],terms:{spring:{rounds:[{start:e}]}}});
assert.equal(selectSchools([fake('a',{status:'official',date:'2026-12-01'}),fake('b',{status:'historical',sort:'2026-11-11'})],{...defaults,priorities:['start','name','city']})[0].id,'b');
filter.execute({q:'LTU',term:'fall',favorites:false});
click('[data-history]');assert.equal(dialog.open,true);assert.ok(document.querySelector('.history-details').hasAttribute('open'));
let blob;URL.createObjectURL=b=>{blob=b;return 'blob:test'};URL.revokeObjectURL=()=>{};
click('[data-action="close"]');if(!JSON.parse(saved.get('tsf-saved')).includes('1045'))click('[data-save]');
click('[data-action="export"]');const csv=await blob.text();assert.ok(csv.includes('原始開始'));assert.ok(csv.includes('2026-03-04'));assert.ok(csv.includes('historical'));
assert.ok(fs.existsSync('./dist/coverage-report.html'));
console.log('PASS: exclusive coverage counts, schema, original years, historical-before-official chronological sorting, nested history toggle, and CSV provenance.');

// Interface update: filters, reversible bookmarks, type scale and disclosures.
click('[data-action="text-size"]');assert.ok(document.documentElement.classList.contains('large-text'));
assert.equal(saved.get('tsf-large-text'),'true');
click('[data-action="text-size"]');assert.ok(!document.documentElement.classList.contains('large-text'));
filter.execute({q:'LTU',city:'臺中市',favorites:false});
assert.equal(document.querySelectorAll('[data-remove-filter]').length,2);
click('[data-remove-filter="city"]');assert.equal(document.querySelector('[data-filter="city"]').value,'');
click('[data-action="clear-search"]');assert.equal(document.querySelector('#search').value,'');
assert.equal(document.querySelector('.result-count').textContent,'139');
assert.ok(document.querySelector('.clear-search').hidden);
filter.execute({q:'LTU',favorites:false});
const beforeUndo=saved.get('tsf-saved');click('[data-save]');click('[data-action="undo-save"]');assert.equal(saved.get('tsf-saved'),beforeUndo);
click('[data-action="filters"]');assert.equal(document.querySelector('[data-action="filters"]').getAttribute('aria-expanded'),'true');
click('[data-action="apply-filters"]');assert.equal(document.querySelector('[data-action="filters"]').getAttribute('aria-expanded'),'false');
click('[data-detail]');assert.ok(document.querySelector('.quick-links a'));assert.equal(dialog.getAttribute('aria-labelledby'),'dialog-title');click('[data-action="close"]');
filter.execute({preferred:''});assert.equal(new URLSearchParams(location.search).get('preferred'),'');
click('[data-lang="my"]');assert.equal(document.querySelector('[data-lang="my"]').getAttribute('lang'),'my');
assert.ok(document.querySelector('.sort-disclosure summary').textContent.includes('၃'));
assert.ok(document.querySelector('[data-action="favorites"]').getAttribute('aria-label'));
console.log('PASS: text-size persistence, removable filter chips, search clear, bookmark undo, mobile filters, dialog quick links, no-city share URLs and Myanmar labels.');

// Map uses the exact same city filter and does not mutate school records.
filter.execute({q:'',city:'',term:'fall',known:false,favorites:false,type:'all',ownership:'all'});
assert.equal(document.querySelectorAll('g[data-map-city]').length,22);
assert.equal(document.querySelectorAll('.map-city-button:not([disabled])').length,21);
for(const c of Object.keys(data.cities)){
 click('g[data-map-city="'+c+'"]');
 const expected=data.schools.filter(s=>s.cities.includes(c)).length;
 assert.equal(Number(document.querySelector('.result-count').textContent),expected,c);
 assert.equal(document.querySelector('[data-filter="city"]').value,c);
 assert.equal(document.querySelector('g[data-map-city="'+c+'"]').getAttribute('aria-pressed'),'true');
 assert.ok(document.querySelector('.map-panel').hasAttribute('open'));
 assert.equal(new URLSearchParams(location.search).get('city'),c);
}
click('.map-city-button[data-map-city="臺中市"]');
click('[data-term="spring"]');assert.equal(document.querySelector('[data-filter="city"]').value,'臺中市');
assert.equal(document.querySelector('g[data-map-city="臺中市"]').getAttribute('aria-pressed'),'true');
filter.execute({city:'臺北市'});assert.equal(document.querySelector('g[data-map-city="臺北市"]').getAttribute('aria-pressed'),'true');
click('[data-map-city=""]');assert.equal(document.querySelector('.result-count').textContent,'139');
click('[data-action="map-results"]');assert.ok(!document.querySelector('.map-panel').hasAttribute('open'));
console.log('PASS: 22 map regions; all 21 registered cities match list counts, dropdowns and share URLs; islands, clearing, semester persistence and map collapse.');
