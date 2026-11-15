#!/usr/bin/env python3
"""Exact counting certificate for the universal enlargement registered A.53.
This certificate checks identities, not good reduction of an unspecified cover.
"""
from pathlib import Path
import json
import sympy as s
p,d,r,g=s.symbols('p d r g',integer=True)
assert s.expand(r+(p**2-1)*d-(p**2*d-2*g+2)).subs(r,d-2*g+2)==0
assert s.expand(2-2*g-(p**2*d-2*g+2)+p**2*d)==0

def profile(es,prime):
    degree=sum(es);cusps=len(es)
    assert (degree-cusps)%2==0
    genus=1+(degree-cusps)//2
    assert prime>degree and prime%4==3 and s.isprime(prime)
    clusters=[1+e*(prime**2-1) for e in es]
    assert min(clusters)>=prime**2
    total=sum(clusters)
    assert total==prime**2*degree-2*genus+2
    assert 2-2*genus-total==-prime**2*degree
    return dict(original_degree=degree,original_genus=genus,
                original_ramification_indices=es,prime=prime,
                new_degree=prime**2*degree,new_cusps=total,
                clusters=clusters)
rows=[profile([1],3),profile([3],7),profile([2,2],7),
      profile([3]*9,31),profile([5]*25,127)]
result={'status':'PASS exact identities','scope':'Arithmetic good-model existence is proved in TeX; profiles here certify counts only.',
        'symbolic_count_identity':True,'symbolic_Euler_identity':True,'profiles':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: universal symbolic cusp-count and Euler identities.')
for row in rows:print(json.dumps(row,sort_keys=True))
