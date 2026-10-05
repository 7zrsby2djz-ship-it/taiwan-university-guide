export const TERMS = ['spring','fall'];
export const SORTS = ['city','difficulty-desc','difficulty-asc','start','end','result','name'];
export const defaults = {term:'spring',q:'',city:'',type:'all',ownership:'all',known:false,audited:false,weiquan:false,favorites:false,preferred:'臺中市',priorities:['start','city','difficulty-desc'],page:1};
const rank=e=>({official:0,historical:1,estimated:2,unknown:3}[e?.status]??4);
export function eventKey(e) { return e?.sort || e?.date || null; }
export function firstEvent(school,term,event) {
  const all=(school.terms[term]?.rounds||[]).filter(r=>r[event]).map(r=>({...r[event],scope:r.scope||school.terms[term]?.scope,roundName:r.name}));
  const rows=all.filter(e=>eventKey(e));
  return rows.sort((a,b)=>eventKey(a).localeCompare(eventKey(b))||rank(a)-rank(b))[0] || all[0] || null;
}
function compareNullable(a,b,dir=1) {if(a==null&&b==null)return 0;if(a==null)return 1;if(b==null)return -1;return (a<b?-1:a>b?1:0)*dir;}
export function selectSchools(schools,state,saved=[]) {
  const query=state.q.trim().toLocaleLowerCase().replaceAll('台','臺');
  return schools.filter(s=>{
    const search=[s.name,s.short,s.abbr,s.english,...s.cities,s.cityEn].join(' ').toLocaleLowerCase().replaceAll('台','臺');
    return (!query||search.includes(query)) && (!state.city||s.cities.includes(state.city)) && (state.type==='all'||s.type===state.type) && (state.ownership==='all'||s.ownership===state.ownership) && (!state.known||s.terms[state.term]?.rounds.some(r=>eventKey(r.start)||eventKey(r.end)||eventKey(r.result))) && (!state.favorites||saved.includes(s.id)) && (!state.weiquan||s.weiquan===true) && (!state.audited||['audited','partially_audited'].includes(s.reviewState));
  }).sort((a,b)=>{
    for(const key of state.priorities){
      let result=0;
      if(key==='city'&&state.preferred)result=Number(!a.cities.includes(state.preferred))-Number(!b.cities.includes(state.preferred));
      if(key==='difficulty-desc')result=compareNullable(a.difficulty,b.difficulty,-1);
      if(key==='difficulty-asc')result=compareNullable(a.difficulty,b.difficulty,1);
      if(['start','end','result'].includes(key)){const x=firstEvent(a,state.term,key),y=firstEvent(b,state.term,key);result=compareNullable(eventKey(x),eventKey(y));if(!result&&eventKey(x)&&eventKey(y))result=rank(x)-rank(y);}
      if(key==='name')result=a.abbr.localeCompare(b.abbr);
      if(result)return result;
    }
    return a.id.localeCompare(b.id);
  });
}
export function validateFilter(input,cities) {
  if(!input||typeof input!=='object'||Array.isArray(input))throw new Error('Expected an object');
  const validKeys=['term','q','city','type','ownership','known','audited','weiquan','favorites','preferred','priorities'];
  if(Object.keys(input).some(k=>!validKeys.includes(k)))throw new Error('Unknown filter');
  if(input.term!==undefined&&!TERMS.includes(input.term))throw new Error('Invalid semester');
  for(const k of ['city','preferred'])if(input[k]!==undefined&&input[k]!==''&&!cities.includes(input[k]))throw new Error('Invalid city');
  if(input.q!==undefined&&(typeof input.q!=='string'||input.q.length>150))throw new Error('Invalid search');
  if(input.type!==undefined&&!['all','university','technology','college','junior'].includes(input.type))throw new Error('Invalid school type');
  if(input.ownership!==undefined&&!['all','public','private'].includes(input.ownership))throw new Error('Invalid ownership');
  for(const k of ['known','audited','weiquan','favorites'])if(input[k]!==undefined&&typeof input[k]!=='boolean')throw new Error('Invalid boolean');
  if(input.priorities!==undefined&&(!Array.isArray(input.priorities)||input.priorities.length!==3||new Set(input.priorities).size!==3||input.priorities.some(k=>!SORTS.includes(k))))throw new Error('Choose three distinct sort priorities');
  return input;
}
