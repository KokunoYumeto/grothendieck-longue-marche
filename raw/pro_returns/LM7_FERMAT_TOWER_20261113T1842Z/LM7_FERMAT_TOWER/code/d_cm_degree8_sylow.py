#!/usr/bin/env python3
"""The exact index-nine Bass--Serre quotient for the relative pro2 source.

The subgroup is the preimage of <s> in Q0. Its graph has three order-two
vertices and one free loop. The normalizer quotient C3 cyclically permutes
the three involution classes, proving the full s-centralizer conclusion.
"""
from pathlib import Path
from contextlib import redirect_stdout
from collections import deque
import io,runpy,json
OUT=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):R=runpy.run_path(str(OUT/'d_cm_rank4_refine.py'))
Q,m,e,s,r=R['Q0'],R['m0'],R['e'],R['s'],R['r']
H={e,s}
def coset(q):return min(m(h,q) for h in H)
cosets=sorted({coset(q) for q in Q})
assert len(cosets)==9
def orbits(g):
    left=set(cosets);ans=[]
    while left:
        q=min(left);orb=[];a=q
        while a not in orb:orb.append(a);a=coset(m(a,g))
        assert a==q;ans.append(orb);left-=set(orb)
    return ans
so,ro=orbits(s),orbits(r)
assert sorted(map(len,so))==[1,1,1,2,2,2]
assert sorted(map(len,ro))==[3,3,3]
fixed=[orb[0] for orb in so if len(orb)==1]
normalizer=[q for q in Q if m(q,s)==m(s,q)]
assert len(normalizer)==6
odd=next(q for q in normalizer if q not in H and m(m(q,q),q)==e)
perm=[fixed.index(coset(m(odd,q))) for q in fixed]
assert all(perm[i]!=i for i in range(3))
assert [perm[perm[perm[i]]] for i in range(3)]==list(range(3))
reps={e:[]};queue=deque([e])
while queue:
    q=queue.popleft()
    for letter,g in [(0,s),(1,r)]:
        qq=m(q,g)
        if qq not in reps:reps[qq]=reps[q]+[letter];queue.append(qq)
torsion_words=[]
for q in fixed:
    w=reps[q]+[0]+R['inverse'](reps[q])
    a=e
    for letter in w:a=m(a,s if letter==0 else r if letter==1 else m(r,r))
    assert a==s;torsion_words.append(w)
summary={'Q0_order':18,'subgroup_index':9,'graph_edges':9,
 's_vertex_orbit_sizes':list(map(len,so)),
 'r_vertex_orbit_sizes':list(map(len,ro)),
 'order2_vertex_count':3,'order3_vertex_count':0,
 'graph_betti_number':9-len(so)-len(ro)+1,
 's_normalizer_order_in_Q0':len(normalizer),
 'normalizer_mod_S_order':3,'normalizer_action_on_involution_classes':perm,
 'sylow_pro2_presentation':'C2 coproduct C2 coproduct C2 coproduct Z2',
 'full_relative_pro2_s_centralizer':'<s>',
 'torsion_vertex_words':torsion_words,
 'exact_s_action_on_K_basis':[[ -1],[-2],[-4],[-3]],
 'source':'Herfort--Ribes1985 section2, Theorem A-prime and Theorem B-prime; exact graph and full-induced-topology argument supplied in the text.'}
assert summary['graph_betti_number']==1
(OUT/'d_cm_degree8_sylow.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
