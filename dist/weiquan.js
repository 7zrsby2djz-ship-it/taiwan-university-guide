// Membership is explicitly stored on school records; no inferred admission chances.
export function monthlyEvents(schools,semester='all'){
 const rows=[],gaps=[];
 for(const s of schools.filter(s=>s.weiquan))for(const term of ['spring','fall']){
  if(semester!=='all'&&term!==semester)continue;
  const t=s.terms[term],missing=[];
  if(t.availability==='not_offered_reference')continue;
  for(const key of ['start','end','result']){
   let found=false;
   for(const [i,r] of (t.rounds||[]).entries()){
    const e=r[key];if(!e)continue;
    const date=e.status==='conflict'?null:e.date||e.sort;
    if(!date||!/^\d{4}-\d{2}-\d{2}$/.test(date))continue;
    found=true;rows.push({id:s.id,name:s.short,abbr:s.abbr,term,key,round:i+1,scope:e.scope||r.scope||t.scope,e,date,month:date.slice(0,7)});
   }
   if(!found)missing.push(key);
  }
  if(missing.length)gaps.push({id:s.id,name:s.short,abbr:s.abbr,term,missing});
 }
 return {rows:rows.sort((a,b)=>a.date.localeCompare(b.date)||a.abbr.localeCompare(b.abbr)),gaps};
}
export function monthlyView(schools,month,semester,lang,esc,safeURL){
 const zh=lang==='zh',tr=(a,b)=>zh?a:b;const {rows,gaps}=monthlyEvents(schools,semester);
 const labels={start:tr('開始申請','လျှောက်လွှာဖွင့်'),end:tr('申請截止','နောက်ဆုံးလျှောက်ရက်'),result:tr('公告榜單','ရလဒ်ကြေညာ')};
 const season=t=>t==='spring'?tr('春 115-2','နွေဦး 115-2'):tr('秋 116-1','ဆောင်းဦး 116-1');
 const months=Array.from(new Set([month,...Array.from({length:15},(_,i)=>{const d=new Date(Date.UTC(2026,8+i,1));return d.toISOString().slice(0,7)}),...rows.map(r=>r.month)])).sort();
 const current=rows.filter(r=>r.month===month);
 const cnDate=e=>e.status==='official'&&e.date?e.date.slice(5).replace('-','/'):(e.label?.zh||'日期待確認');
 const cols=['start','end','result'].map(key=>`<section class="wq-column wq-${key}"><h3>${labels[key]} <span>${current.filter(r=>r.key===key).length}</span></h3>${current.filter(r=>r.key===key).map(r=>`<article class="wq-event"><div class="wq-event-top"><span class="wq-season ${r.term}">${season(r.term)}</span><strong>${esc(cnDate(r.e))}</strong></div><button data-detail="${esc(r.id)}" data-detail-term="${r.term}" class="wq-school">${esc(r.name)} <span>${esc(r.abbr)}</span></button><p>${tr('第','အကြိမ် ')} ${r.round} ${tr('梯','')} ${r.scope==='graduate'?tr('· 僅研究所','· ဘွဲ့လွန်သာ'):r.scope==='undergraduate'?tr('· 僅學士','· ဘွဲ့ကြိုသာ'):''}</p><small class="wq-status ${r.e.status}">${r.e.status==='official'?tr('官方公告','တရားဝင်'):r.e.status==='estimated'?tr('歷年推估','ခန့်မှန်း'):tr('歷年參考','ယခင်နှစ်ကိုးကား')} · ${esc(r.e.sourceYear||r.e.basis||'年度未明')}</small>${r.e.sourceUrl?`<a href="${esc(safeURL(r.e.sourceUrl))}" target="_blank" rel="noopener noreferrer">${tr('官方來源','တရားဝင်ရင်းမြစ်')} ↗</a>`:''}</article>`).join('')||`<p class="wq-empty">${tr('本月無已知事件','ဤလတွင် သိရှိထားသော အစီအစဉ်မရှိပါ')}</p>`}</section>`).join('');
 return `<div class="wq-toolbar"><label>${tr('月份','လ')}<select data-wq-month>${months.map(m=>`<option value="${m}" ${m===month?'selected':''}>${m} · ${rows.filter(r=>r.month===m).length} ${tr('筆','ခု')}</option>`).join('')}</select></label><label>${tr('入學季','ဝင်ခွင့်ရာသီ')}<select data-wq-term><option value="all" ${semester==='all'?'selected':''}>${tr('春＋秋','နွေဦး + ဆောင်းဦး')}</option><option value="spring" ${semester==='spring'?'selected':''}>115-2 · 2027 ${tr('春','နွေဦး')}</option><option value="fall" ${semester==='fall'?'selected':''}>116-1 · 2027 ${tr('秋','ဆောင်းဦး')}</option></select></label><button data-wq-step="-1" aria-label="${tr('上一月','ယခင်လ')}">←</button><button data-wq-step="1" aria-label="${tr('下一月','နောက်လ')}">→</button></div><p class="wq-reference">${tr('歷年資料按月份放入2027入學規劃，並非本期正式日期。放榜不等於收到入學許可。','ယခင်နှစ်ရက်များကို 2027 အစီအစဉ်အတွက် လအလိုက် ကိုးကားထားသည်။ ယခုနှစ် တရားဝင်ရက် မဟုတ်ပါ။')}</p><div class="wq-grid">${cols}</div><details class="wq-gaps"><summary>${tr('沒有日期或仍有衝突的項目','ရက်မသိရသေးသော အချက်များ')} · ${gaps.length}</summary><p>${tr('沒有事件不代表沒有招生。以下項目不硬塞進任何月份；點校名查看來源或差異。','အစီအစဉ်မရှိခြင်းသည် ဝင်ခွင့်မရှိဟု မဆိုလိုပါ။ အသေးစိတ်ကို ကျောင်းနာမည်နှိပ်၍ ကြည့်ပါ။')}</p>${gaps.map(g=>`<p><button class="wq-school" data-detail="${esc(g.id)}" data-detail-term="${g.term}">${esc(g.name)} ${esc(g.abbr)}</button> · ${season(g.term)} · ${g.missing.map(k=>labels[k]).join('／')}</p>`).join('')}</details>`;
}
