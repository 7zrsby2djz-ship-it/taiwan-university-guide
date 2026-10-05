import fs from 'node:fs';
import assert from 'node:assert/strict';
import {selectSchools,defaults,eventKey,firstEvent} from '../../dist/core.js';
const read=p=>JSON.parse(fs.readFileSync(new URL(p,import.meta.url)));
const data=read('../../dist/schools.json'),old=read('../backups/national-2026-09-27/schools.json');
const ins=read('../../dist/school-insights.json').schools,oldIns=read('../backups/national-2026-09-27/school-insights.json').schools;
const facts=read('./facts.json'),ids=Object.keys(facts);
assert.equal(ids.length,17);assert.equal(data.schools.length,139);
assert.deepEqual(data.schools.map(s=>s.id),old.schools.map(s=>s.id));
for(const s of data.schools)if(!ids.includes(s.id))assert.deepEqual(s,old.schools.find(x=>x.id===s.id),'Unrelated school changed '+s.id);
for(const [id,v] of Object.entries(oldIns))if(!ids.includes(id))assert.deepEqual(ins[id],v,'Previous research changed '+id);
const get=id=>data.schools.find(s=>s.id===id);
const audited=selectSchools(data.schools,{...defaults,audited:true});
assert.equal(audited.length,28);assert.equal(audited.filter(s=>s.reviewState==='partially_audited').length,2);
assert.equal(new Set(audited.map(s=>s.id)).size,28);
assert.ok(ids.every(id=>audited.some(s=>s.id===id)));
const fees=ids.map(id=>ins[id].applicationFee);assert.equal(fees.filter(f=>f.status==='confirmed').length,11);
for(const f of fees){assert.ok(f.sourceUrl&&f.academicYear);if(f.amount===0){assert.equal(f.status,'confirmed');assert.match(f.notes,/免|不收|無須/);}if(f.status!=='confirmed')assert.equal(f.amount,null);}
for(const id of ids){
 assert.ok(ins[id].audit.gaps.length);
 for(const sch of ins[id].scholarships)assert.ok(sch.sourceUrl&&sch.academicYear&&sch.continuation);
 for(const n of ins[id].admissionNotices){assert.ok(n.sourceUrl&&n.sourceTitle&&n.academicYear);assert.ok(!('count' in n)&&!('students' in n));}
 for(const [term,t] of Object.entries(get(id).terms))for(const r of t.rounds)for(const key of ['start','end','result']){
  const e=r[key];if(!e)continue;if(e.date)assert.equal(e.status,'official');
  if(e.status==='historical')assert.ok(!e.date&&e.label.zh);
  if(e.status==='conflict')assert.equal(eventKey(e),null);
 }
}
assert.equal(get('0021').terms.spring.rounds[0].result.rawDate,'2026-01-05');
assert.equal(get('0021').terms.spring.rounds[0].result.status,'historical');
assert.equal(get('0017').terms.spring.rounds[0].start.status,'official');
assert.equal(get('0017').terms.spring.rounds[0].result.sourceYear,'114-2');
assert.equal(get('0002').terms.fall.rounds[0].scope,'undergraduate');
assert.ok(get('0002').terms.fall.rounds.some(r=>r.scope==='graduate'));
assert.equal(get('0002').terms.fall.rounds[0].result.rawDate,'2026-04-24');
for(const id of ['0007','0008','0022','0023'])assert.equal(get(id).terms.spring.scope,'graduate');
assert.equal(get('0025').terms.fall.rounds[0].result.sourceYear,'116-1');
assert.equal(get('0025').terms.fall.rounds[0].result.date,undefined);
assert.equal(get('0004').terms.fall.rounds[1].end.status,'conflict');
assert.equal(firstEvent(get('0025'),'spring','result').status,'conflict');
assert.match(ins['0022'].scholarships[0].continuation,/學士.*不提供/);
assert.match(ins['0005'].scholarships[0].award,/115.*不能沿用/);
const allRecords=read('../../dist/admission-records.json');
assert.deepEqual(allRecords,data.schools.flatMap(s=>Object.values(s.terms).flatMap(t=>t.admissionRecords||[])));
for(const term of ['fall','spring'])assert.equal(Object.values(data.coverage[term].counts).reduce((a,b)=>a+b,0),139);
console.log('PASS: 17-school scope, 122 school records unchanged, previous insights intact, 28-school membership, fee evidence, semesters, raw years, partial fields, conflicts, and coverage.');
