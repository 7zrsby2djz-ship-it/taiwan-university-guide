import fs from 'node:fs';
import assert from 'node:assert/strict';
import {renderInsights} from '../../dist/insights.js';
const read=p=>JSON.parse(fs.readFileSync(new URL(p,import.meta.url)));
const data=read('../../dist/schools.json'), old=read('../backups/2026-09-27/schools.json');
const ins=read('../../dist/school-insights.json').schools;
const ids=['1008','1007','1001','1018','1048','0006','0050','0043','1062','1034','1045'];
for(const s of data.schools)if(!ids.includes(s.id))assert.deepEqual(s,old.schools.find(x=>x.id===s.id),'non-core school changed '+s.id);
assert.equal(data.schools.length,139);
for(const id of ids){
 const fee=ins[id].applicationFee;
 if(fee.amount===0){assert.equal(fee.status,'confirmed');assert.equal(fee.academicYear,'115');assert.ok(fee.sourceUrl);assert.match(fee.notes,/免|None|免費|不收取/);}
 else assert.equal(fee.amount,null);
 for(const s of ins[id].scholarships||[])assert.ok(s.sourceUrl.startsWith('https://'));
 const html=renderInsights(ins[id],'spring','zh',s=>String(s??''),s=>s);
 assert.ok(!html.includes('僅查114'));
 for(const s of ins[id].scholarships||[])if(s.continuation)assert.ok(html.includes(s.continuation));
}
assert.equal(ids.filter(id=>ins[id].applicationFee.amount===0).length,4);
const fcu=data.schools.find(s=>s.id==='1007');assert.equal(fcu.terms.spring.rounds[0].start.date,'2026-09-15');assert.equal(fcu.terms.spring.rounds.length,2);assert.equal(fcu.terms.fall.rounds.length,4);
assert.equal(data.schools.find(s=>s.id==='0050').terms.spring.availability,'not_offered_in_source');
assert.match(ins['0043'].scholarships[0].award,/第一學年學雜費減半/);
assert.match(ins['1045'].scholarships[0].restrictions,/25,000.*15,000/);
const springNcut=renderInsights(ins['0043'],'spring','zh',s=>String(s??''),s=>s);assert.match(springNcut,/不涵蓋目前選取的入學季/);
console.log('PASS: 128 non-core records untouched; four explicitly free115 fees; source years/intakes; FCU seasons; NTCUST availability; NCUT/LTU policy changes; renewal conditions visible.');
