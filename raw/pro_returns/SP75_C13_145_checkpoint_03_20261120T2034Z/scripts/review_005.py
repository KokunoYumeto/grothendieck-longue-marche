from pathlib import Path
import json
ED=Path(__file__).resolve().parents[1]
r=json.loads((ED/'reader_reports/145_scan005.json').read_text())
r['main_reader_reviewed']=True
r['root_review']={'whole_image':True,'crops_viewed':'All 15 reader crops, plus root crops 16_vraie and 17_bottom_number','decisions':'Accepted the lexical and insertion readings after direct image review; retained uncertain struck layers and alphabet distinctions; rejected double-prime speculation because the adjacent points are round detached ink dots.'}
for row in r['inventory']:
 row['sheet_kind']='text'
 if row['hand']=='main cursive hand':row['hand']='his hand'
for c in r['changes']:
 if c['id']=='s005-05':c['h_changed']=True
 if c['id']=='s005-19':c.update(crop='crops/145_scan005_16_vraie.png',box=[180,2172,580,2305])
 if c['id']=='s005-20':c.update(crop='crops/145_scan005_17_bottom_number.png',box=[28,2255,100,2340])
r['doubts']=[d for d in r['doubts'] if d['place']!='last occurrence of pi, before en respectant']
for b in r['second_boxes']:b['reading']=b['reading'].replace(r"\unsure{\pi|\pi''}",r'\pi')
r['notes'][6]='Two small dark points beside the final prose pi were examined in crop 14. Their compact round forms are not prime strokes; the ordinary comma is separate below-right. The main reader treats these points as incidental ink, leaves the agreed unprimed pi, and records the observation here rather than inserting unsupported mathematical punctuation.'
for n in r['notation']:
 if 'qualification' in n:n['qualification']=n['qualification'].replace('The last occurrence also has two small adjacent dark points, whose status is unresolved.','Two adjacent round points at the last occurrence are treated as incidental ink, not primes.')
extra=[
('B15','generator indices and displayed relation',[248,268,1585,527],r'On prend la présentation par les générateurs $l_0,l_1,l_\infty$ liés par $l_0l_1l_\infty=1$'),
('B16','primed generators and numeric indices',[246,531,1639,703],r"Un endomorphisme de $\unsure{\pi_{0,3}|\Pi_{0,3}}$ est donc donné par des éléments $l_0',l_1',l_\infty'$ satisfaisant la"),
('B17','rho display numeric indices',[476,1067,1200,1157],r'$\rho(l_0)=l_1,\quad\rho(l_1)=l_\infty,\quad\rho(l_\infty)=l_0$'),
('B18','sigma display numeric indices',[475,1233,1069,1336],r'$\sigma_\infty(l_0)=l_1,\quad\sigma_\infty(l_1)=l_0$'),
('B19','involution numeric exponent',[205,1352,1240,1427],r"on a évidemment $\sigma_\infty^2=\mathrm{id}$. On définit de"),
('B20','conjugation formula numeric exponent',[600,1555,970,1670],r'$\rho\sigma_i\rho^{-1}=\sigma_{\rho(i)}$'),
('B21','permutation entries in prose',[195,1667,1648,1815],r"en désignant par $\rho$ aussi la permutation circulaire sur $0,1,\infty$. On considère $\rho$ et les $\sigma_i$ comme des éléments"),
('B22','set of three labels',[195,1913,789,2015],r"permutations de l'ens. $\{0,1,\infty\}$")]
for name,kind,coords,reading in extra:r['second_boxes'].append(dict(box=name,kind=kind,coords=coords,reading=reading))
r['crop_count']=17
(ED/'reader_reports/145_scan005_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
s=(ED/'reader_reports/145_scan005.tex').read_text().replace(r"\unsure{\pi|\pi''}",r'\pi')
(ED/'pages/145_scan005.tex').write_text(s)
