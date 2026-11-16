#!/usr/bin/env python3
"""Exact D16 subgroup/cusp certificate for the A68 addendum."""
from pathlib import Path
import json

G=frozenset((a,e) for a in range(8) for e in range(2))
def mul(x,y):return ((x[0]+(-1 if x[1] else 1)*y[0])%8,(x[1]+y[1])%2)
def generated(gens):
    H={(0,0)}
    while True:
        N=H|{mul(x,y) for x in H for y in gens}
        if N==H:return frozenset(H)
        H=N
subgroups={generated(gens) for x in G for y in G for gens in [(x,y)]}
assert len(subgroups)==19
I=generated([(2,0)])
maximal=[H for H in subgroups if H!=G and not any(H<J<G for J in subgroups)]
assert frozenset.intersection(*maximal)==I
assert all({mul(x,y) for x in H for y in I}=={mul(y,x) for x in H for y in I} for H in subgroups)
rows=[]
for H in sorted(subgroups,key=lambda h:(len(h),sorted(h))):
    double={frozenset(mul(mul(h,g),i) for h in H for i in I) for g in G}
    HI={mul(h,i) for h in H for i in I}
    assert len(double)==16//len(HI)
    assert (HI==G)==(H==G)
    degree=16//len(H);cusps=len(double)
    assert (degree-cusps+2)%2==0
    genus=(degree-cusps+2)//2
    assert genus>=1
    assert H==G or cusps>=2
    rows.append({'subgroup':[list(x) for x in sorted(H)],'subgroup_order':len(H),'degree':degree,'cusps':cusps,'genus':genus})
out={'status':'PASS','group':'D16 of order16','actual_inertia_generator':[2,0],
     'inertia_order':len(I),'frattini_equals_inertia':True,'subgroup_count':len(rows),
     'all_proper_subgroups_have_distinct_companion_cusps':True,'subgroups':rows,
     'scope':'Finite subgroup/orbit certificate; actual norm and stable reduction arguments are in the addendum.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all19 D16 subgroups; exact Frattini/inertia equality; every proper intermediate has at least2 cusps and positive compact genus.')
