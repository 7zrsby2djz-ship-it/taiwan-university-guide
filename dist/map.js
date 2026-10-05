import {countyPaths} from './map-paths.js';
const esc=v=>String(v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const regions=[
 ['北部','မြောက်ပိုင်း',['臺北市','新北市','基隆市','桃園市','新竹市','新竹縣']],
 ['中部','အလယ်ပိုင်း',['苗栗縣','臺中市','彰化縣','南投縣','雲林縣']],
 ['南部','တောင်ပိုင်း',['嘉義市','嘉義縣','臺南市','高雄市','屏東縣']],
 ['東部・離島','အရှေ့ပိုင်းနှင့် ကျွန်းများ',['宜蘭縣','花蓮縣','臺東縣','澎湖縣','金門縣','連江縣']]
];
export function mapMarkup({lang,selected,counts,cities,open}){
 const my=lang==='my';
 const city=n=>my?(cities[n]||'Matsu')+' · '+n:n;
 const title=my?'မြေပုံမှ ကျောင်းရွေးရန်':'地圖選校';
 const total=counts.all||0;
 const selection=selected?city(selected):my?'ထိုင်ဝမ်တစ်နိုင်ငံလုံး':'全臺灣';
 const label=n=>city(n)+' · '+(counts[n]||0)+(my?' ကျောင်း':' 校');
 const button=n=>`<button data-map-city="${n}" class="map-city-button" aria-pressed="${selected===n}" ${cities[n]?'':'disabled'}><span>${esc(city(n))}</span><b>${counts[n]||0}</b></button>`;
 const shapes=countyPaths.map(c=>{
  const enabled=!!cities[c.name],active=selected===c.name;
  const [x,y]=c.label,[cx,cy]=c.center;
  return `<g class="county ${active?'selected':''} ${enabled?'':'unavailable'}" data-map-city="${c.name}" role="button" ${enabled?'tabindex="0"':'aria-disabled="true"'} aria-pressed="${active}" aria-label="${esc(label(c.name))}"><title>${esc(label(c.name))}</title>${c.inset?`<rect class="island-inset" x="${c.inset[0]}" y="${c.inset[1]}" width="80" height="69" rx="8"/>`:''}<path d="${c.path}" fill-rule="evenodd"/>${!c.inset&&Math.hypot(x-cx,y-cy)>18?`<line x1="${cx}" y1="${cy}" x2="${x}" y2="${y-5}"/>`:''}<text x="${x}" y="${y}" text-anchor="middle" dominant-baseline="middle" lang="zh-Hant">${c.name}</text></g>`;
 }).join('');
 return `<details class="map-panel" ${open?'open':''}><summary><span class="map-heading">${esc(title)}</span><span class="map-summary-city">${esc(selection)}</span></summary><div class="map-body"><div class="map-visual"><p class="map-help">${my?'မြို့နယ်ကို နှိပ်ပြီး ကျောင်းစာရင်းကို စစ်ထုတ်ပါ။':'點選縣市版圖，立即篩選學校。'}</p><svg class="taiwan-map" viewBox="0 0 420 570" aria-label="${esc(title)}"><title>${esc(title)}</title>${shapes}</svg><p class="map-attribution">${my?'ကျွန်းငယ်များကို ချဲ့ပြထားသည်။':'離島另框放大顯示，位置不依比例。'} <a href="./map-sources.txt" target="_blank" rel="noopener noreferrer">g0v · CC0</a></p></div><div class="map-options"><div class="map-selection"><strong>${esc(selection)}</strong><span class="map-count" role="status">${selected?counts[selected]||0:total} ${my?'ကျောင်း':'校'}</span><button class="text-btn" data-map-city="" ${selected?'':'disabled'}>${my?'ထိုင်ဝမ်တစ်နိုင်ငံလုံး ပြန်ကြည့်ရန်':'清除地區・顯示全臺'}</button><button class="primary" data-action="map-results">${my?'ကျောင်းစာရင်းကို ကြည့်ရန်':'查看學校結果'} ↓</button></div><details class="map-city-list"><summary>${my?'မြို့စာရင်းမှ ရွေးရန်':'也可點選縣市名稱'}</summary>${regions.map(([zh,mm,names])=>`<section><h3>${my?mm:zh}</h3><div class="map-city-grid">${names.map(button).join('')}</div></section>`).join('')}</details><p class="map-help">${my?'အရေအတွက်သည် လက်ရှိစစ်ထုတ်မှုအပေါ် အခြေခံသည်။':'校數依目前搜尋與篩選條件計算。'}</p></div></div></details>`;
}
