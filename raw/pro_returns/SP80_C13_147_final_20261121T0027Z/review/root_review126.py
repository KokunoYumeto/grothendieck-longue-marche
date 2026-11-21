from pathlib import Path
import json
R=Path('edition');d=json.loads((R/'reports/147_scan126_report.json').read_text())
C=Path('packets/147_scan126/C.tex').read_text();H=Path('packets/147_scan126/H.tex').read_text();F=(R/'reports/147_scan126_proposed.tex').read_text()
for i,fragment in zip((2,3,4),(r'D_d',r"D_{d'}",r"D_{d''}")):
 d['rows'][i]['H']=fragment;d['rows'][i]['marked_in_H']=False
for i in (3,8):d['rows'][i]['math_consequential']=False
d['rows'][5]['H']='';d['rows'][15]['H']=''
d['rows'][8]['C']=r'\arrow[r,no head]';d['rows'][8]['H']=r'\arrow[r]'
d['rows'][9]['C']=C[C.index('(202)\\quad'):C.index('\n\nToutes')]
start=H.rindex(r'\begin{tikzcd}');end=H.index(r'\end{tikzcd}',start)+len(r'\end{tikzcd}')
d['rows'][9]['H']=H[start:end];d['rows'][9]['final']=F[F.index(r'\diagram{\((202)'):F.index('\n\nToutes')];d['rows'][9]['marked_in_H']=False
mapping={'S126-201-READING':[2],'S126-FANS':[3,4],'S126-202-FORMAL':[7],'S126-202-GRAPH':[5],'S126-NORMAL-CROSSINGS':[8]}
covered=set()
for e in d['check_events']:
 nums=mapping[e['statement_id']];covered.update(nums);e['statement_id']+='; '+'; '.join(f'N126-{i:02d}' for i in nums)
for i in (1,6,9):
 d['check_events'].append({'statement_id':f'N126-{i:02d}','type':'carried as background without fault found' if i==6 else 'used and rechecked in this run','outcome':'Recorded the page’s transitivity assertion and references without a general proof.' if i==6 else 'Root checked the descriptive ink/count note against the viewed crops, page and inventory; no further mathematical proof is claimed.'})
(R/'review/147_scan126_reviewed.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (R/'notation.md').open('a') as f:f.write('\n- Scan126: an M-like initial may merge with the following parenthesis; the whole initial/delimiter boundary is kept doubtful. A new lower d′ has a q-like long descending exit, compared with the d of de on the same page. Five short connectors in(202) have single downward terminations, distinct from its four complete arrowheads. Literal de = and tt remain unexpanded.\n')
