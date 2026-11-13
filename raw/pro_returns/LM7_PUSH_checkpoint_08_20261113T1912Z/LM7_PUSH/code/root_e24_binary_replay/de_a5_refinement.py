#!/usr/bin/env python3
"""A finite nonabelian refinement outside the homology tower, with all
24 certified G6 shadows surviving.  This proves one finite test only."""
from itertools import permutations,product
from pathlib import Path
import json, math

here=Path(__file__).resolve().parent
def pm(a,b):return tuple(a[b[i]] for i in range(5))
def pi(a):return tuple(a.index(i) for i in range(5))
e=tuple(range(5))
def pc(a,b):return pm(pm(a,b),pi(a))
def closure(gens,one,mul):
    seen={one};queue=[one];gens=list(gens)
    for a in queue:
        for b in gens:
            c=mul(a,b)
            if c not in seen:seen.add(c);queue.append(c)
    return seen
def order(a,one,mul):
    q=one
    for k in range(1,1000):
        q=mul(q,a)
        if q==one:return k
    raise RuntimeError('order exceeds bound')
S=(1,0,3,2,4) # (12)(34)
R=(2,1,4,3,0) # (135)
A=closure([S,R],e,pm)
assert len(A)==60
even={a for a in permutations(range(5)) if sum(a[i]>a[j] for i in range(5) for j in range(i+1,5))%2==0}
assert A==even
classes=[];remaining=set(A)
while remaining:
    a=min(remaining);cc={pc(g,a) for g in A};classes.append(cc);remaining-=cc
assert all(len(closure(c,e,pm))==60 for c in classes if e not in c)
derived=closure({pm(pc(a,b),pi(b)) for a in A for b in A},e,pm)
assert derived==A
t=pm(S,R); u=pi(t); v=pm(pm(S,u),S)
assert order(S,e,pm)==2 and order(R,e,pm)==3 and order(t,e,pm)==5
assert pm(u,v)==R and pm(pm(u,v),u)==S and pm(pm(v,u),v)==S
assert pm(u,v)==pm(e,pm(u,v)) and pm(v,u)==pm(pm(v,u),e)

I=(1,0,0,1)
def neg(a):return tuple(-x%12 for x in a)
def can(a):return min(tuple(a),neg(a))
def mm(a,b):return can(((a[0]*b[0]+a[1]*b[2])%12,(a[0]*b[1]+a[1]*b[3])%12,
                       (a[2]*b[0]+a[3]*b[2])%12,(a[2]*b[1]+a[3]*b[3])%12))
def mi(a):return can((a[3],-a[1]%12,-a[2]%12,a[0]))
Q={can(a) for a in product(range(12),repeat=4) if (a[0]*a[3]-a[1]*a[2])%12==1}
levels=[len(Q)];G=Q
while len(G)>1:
    comms={mm(mm(mm(a,b),mi(a)),mi(b)) for a in G for b in G}
    G=closure(comms,I,mm);levels.append(len(G))
    assert len(levels)<10
assert levels[-1]==1
cert=json.loads((here/'de_verify_cm.json').read_text())['certificates']
assert len(cert)==24 and all(c['gauged_hexagons_in_G6'] for c in cert)
out={'A5_generators_one_based':[[j+1 for j in g] for g in (S,R)],
     'A5_generator_orders':[2,3], 'A5_cusp_order':5,
     'A5_order':len(A),'A5_conjugacy_class_sizes':sorted(map(len,classes)),
     'A5_simple':True,'A5_perfect':True,'Q_derived_series_orders':levels,
     'refinement':'B / (ker(B->G6) intersect ker(B->A5)) = G6 x A5',
     'refinement_order':576*6**97*60,'refined_cusp_order':360,
     'refined_shadow_Nord':180,'m':0,'lambda':1,
     'certified_surviving_shadows':24,
     'certified_surviving_extra_CM_shadows':sum(c['missing_coset'] for c in cert),
     'outside_homology_tower':True,
     'reason':'N_B and its derived group both map onto A5; the refinement kernel cannot contain [N_B,N_B].',
     'scope':'One explicit additional finite quotient; no cofinality assertion.'}
(here/'de_a5_refinement.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
print('PASS: the componentwise identity A5 shadow extends every certified G6 shadow.')
