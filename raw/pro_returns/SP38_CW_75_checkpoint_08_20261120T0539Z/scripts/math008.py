"""Exact finite counterexamples for the two adjacency tests on scan008.
No image/text recognition; checks graph incidence and explicit permutations.
"""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
def check(n,p,q):
 edges=[{i,(i+1)%n} for i in range(n)]
 inc=all({p[v] for v in edges[i]}==edges[q[i]] for i in range(n))
 c1=all(p[i]!=i and any({i,p[i]}<=e for e in edges) for i in range(n))
 c2=all(q[i]!=i and bool(edges[i]&edges[q[i]]) for i in range(n))
 return {'n':n,'vertices':p,'edges':q,'incidence_automorphism':inc,'condition_1':c1,'condition_2':c2}
results=[check(4,[1,0,3,2],[0,3,2,1]),check(4,[0,3,2,1],[3,2,1,0]),check(2,[1,0],[0,1]),check(2,[0,1],[1,0])]
assert all(x['incidence_automorphism'] for x in results)
assert [(x['condition_1'],x['condition_2']) for x in results]==[(True,False),(False,True),(True,False),(False,True)]
p=root/'decisions/scan008_adjacency_certificate.json';p.write_text(json.dumps(results,indent=2)+'\n');print(p);print(json.dumps(results,indent=2))
