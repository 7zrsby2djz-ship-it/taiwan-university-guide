import fs from 'node:fs';
import assert from 'node:assert/strict';
import {selectSchools,defaults,eventKey,firstEvent} from '../../dist/core.js';
const read=p=>JSON.parse(fs.readFileSync(new URL(p,import.meta.url)));
const data=read('../../dist/schools.json'),old=read('../backups/remaining-2026-09-28/schools.json');
const ins=read('../../dist/school-insights.json').schools,oldIns=read('../backups/remaining-2026-09-28/school-insights.json').schools;
const facts=read('./facts.json'),ids=Object.keys(facts);
assert.equal(ids.length,23);assert.equal(data.schools.length,139);
assert.deepEqual(data.schools.map(s=>s.id),old.schools.map(s=>s.id));
for(const s of data.schools)if(!ids.includes(s.id))assert.deepEqual(s,old.schools.find(x=>x.id===s.id),'Unrelated school changed '+s.id);
for(const [id,v] of Object.entries(oldIns))if(!ids.includes(id))assert.deepEqual(ins[id],v,'Previous research changed '+id);
const get=id=>data.schools.find(s=>s.id===id);
const audited=selectSchools(data.schools,{...defaults,audited:true});
assert.equal(audited.length,51);assert.equal(audited.filter(s=>s.reviewState==='partially_audited').length,25);
assert.equal(new Set(audited.map(s=>s.id)).size,51);
assert.ok(ids.every(id=>audited.some(s=>s.id===id)));
const fees=ids.map(id=>ins[id].applicationFee);assert.equal(fees.filter(f=>f.status==='confirmed').length,13);
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
for (const id of ['0019','0037','0048']) assert.equal(get(id).terms.fall.rounds[0].start.status,'official');
assert.equal(get('0037').terms.fall.rounds[0].start.date,'2026-09-11');
assert.equal(get('0048').terms.fall.rounds[0].result.date,'2027-01-20');
assert.equal(get('0020').terms.fall.rounds[0].start.rawDate,'2026-01-02');
assert.equal(get('0020').terms.fall.rounds[0].start.status,'historical');
assert.equal(get('0053').terms.fall.brochure.academicYear,'115-1');
assert.equal(get('0053').terms.spring.brochure.academicYear,'115-2');
assert.notEqual(get('0053').terms.fall.brochure.url,get('0053').terms.spring.brochure.url);
assert.equal(get('0029').terms.spring.rounds.length,0);
assert.equal(get('0044').terms.fall.rounds[0].end.status,'conflict');
assert.equal(eventKey(get('0044').terms.fall.rounds[0].end),null);
assert.equal(get('0018').terms.fall.rounds[1].scope,'undergraduate');
assert.equal(ins['0046'].applicationFee.amount,null);
assert.equal(ins['0046'].applicationFee.exceptions[0].currency,'USD');
assert.match(ins['0048'].scholarships[0].award,/擇優/);
assert.ok(ins['0049'].applicationFee.intakes.includes('spring'));
assert.ok(!ins['0049'].applicationFee.intakes.includes('fall'));
assert.equal(ins['0052'].applicationFee.amount,0);
assert.ok(ins['0039'].applicationFee.amountLabel.includes('博士'));
assert.equal(get('0028').terms.fall.rounds[0].result.date,undefined);
for(const term of ['spring','fall']) assert.equal(get('0024').terms[term].rounds[0].start.rawDate,null);
const allRecords=read('../../dist/admission-records.json');
assert.deepEqual(allRecords,data.schools.flatMap(s=>Object.values(s.terms).flatMap(t=>t.admissionRecords||[])));
for(const term of ['fall','spring'])assert.equal(Object.values(data.coverage[term].counts).reduce((a,b)=>a+b,0),139);
console.log('PASS: 23-school scope, 116 school records unchanged, previous insights intact, 51-school membership, fee evidence, semesters, raw years, partial fields, conflicts, and coverage.');
