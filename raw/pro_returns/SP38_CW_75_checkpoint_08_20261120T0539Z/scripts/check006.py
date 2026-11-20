"""Finite check of the two proposed adjacency conditions; no image processing."""
from itertools import permutations
import json
from pathlib import Path
O=Path(__file__).resolve().parents[1]
S=tuple(range(4)); E=tuple(frozenset((i,(i+1)%4)) for i in S)
rows=[]
for p in permutations(S):
 im=tuple(frozenset(p[v] for v in e) for e in E)
 if set(im)!=set(E):continue
 q=tuple(E.index(e) for e in im)
 one=all(frozenset((s,p[s])) in E for s in S)
 two=all(i!=q[i] and len(E[i]&E[q[i]])==1 for i in S)
 rows.append({'vertex_permutation':p,'edge_permutation':q,'condition_1':one,'condition_2':two})
r={'interpretation':'lié means distinct adjacent vertices, and distinct edges sharing a vertex in the dual contour','graph':'four-cycle, S=Z/4, edge i={i,i+1}','automorphisms':rows,'counts':{'all':len(rows),'condition_1':sum(x['condition_1'] for x in rows),'condition_2':sum(x['condition_2'] for x in rows),'both':sum(x['condition_1'] and x['condition_2'] for x in rows)},'counterexample':'g(s)=1-s mod4; edge i goes to -i. Every vertex is adjacent to its image. Edges 0 and 2 are fixed, while 1 and 3 are disjoint; condition 2 fails. Conversely g(s)=-s has condition 2 but not condition 1.'}
assert r['counts']=={'all':8,'condition_1':4,'condition_2':4,'both':2}
(O/'decisions/scan006_adjacency_certificate.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r['counts']))
