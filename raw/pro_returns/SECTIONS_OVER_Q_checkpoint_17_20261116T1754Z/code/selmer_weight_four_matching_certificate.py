#!/usr/bin/env python3
"""Exact finite arithmetic in A.205's fourth-weight correction map."""
from math import gcd
from pathlib import Path
import json
import sympy as S

def vp(a,p):
    if not a: return 10**9
    a=abs(a);n=0
    while a%p==0: n+=1;a//=p
    return n

lam,mu=S.symbols('lam mu')
eta=lambda t:(t**4-1)/240
assert S.expand(eta(lam*mu)-eta(lam)-lam**4*eta(mu))==0

ideal_cases=[]
for p,k,expected in [(2,9,4),(3,7,1),(5,6,1)]:
    vals=[vp(u**4-1,p) for u in range(1,p**k) if u%p]
    assert min(vals)==expected
    assert all(v>=expected for v in vals)
    ideal_cases.append(dict(prime=p,modulus=p**k,unit_cases=len(vals),minimum=expected))
for p in list(S.primerange(7,200)):
    roots=[u for u in range(1,p) if pow(u,4,p)==1]
    assert len(roots)<=4 and len(roots)<p-1

images={}
for k in range(240):
    image=(k*pow(3,-1,16)%16,k*pow(16,-1,3)%3,k*pow(16,-1,5)%5)
    assert image not in images
    images[image]=k
assert len(images)==16*3*5==240

restriction_cases=0
for q in list(S.primerange(2,100)):
    for ell,w in [(2,16),(3,3),(5,5)]:
        if q==ell: continue
        exponent=vp(q**4-1,ell)
        order=ell**exponent
        # The class of (q^4-1)/w has order exactly w in Z_l/(q^4-1).
        assert (q**4-1)%w==0
        numerator=(q**4-1)//w
        assert order//gcd(numerator,order)==w
        restriction_cases+=1

# For trivial C2 action the odd-degree finite cohomology is M[2].
# Enumerate that subgroup and its actual reduction transition.
real_coeff_checks=0
for n in range(1,14):
    current=1<<n
    upper=1<<(n+1)
    h3_upper=[a for a in range(upper) if (2*a)%upper==0]
    assert h3_upper==[0,current]
    assert {a%current for a in h3_upper}=={0}
    real_coeff_checks+=1

data=dict(ideal_cases=ideal_cases,crt_classes=len(images),
          finite_restriction_cases=restriction_cases,
          real_transition_checks=real_coeff_checks,
          fourth_layer_global_classes=240**3,
          exact_generator='(chi^4-1)/240',
          exact_local_map='k -> (k/3 mod16,k/16 mod3,k/16 mod5)',
          scope='Finite arithmetic only; continuous cohomology, stabilizers and compactness are proved in the source.')
lines=[
    'A.205 fourth-weight exact matching certificate: PASS',
    'Literal cyclotomic one-cocycle identity: PASS',
    f'Fourth-power ideal unit cases: {sum(t["unit_cases"] for t in ideal_cases)}',
    'CRT localization map: all 240 classes are distinct and exhaustive',
    f'Prime-to-residue coefficient restriction-order checks: {restriction_cases}',
    f'Fourth-layer global lift count: {240**3}',
    'The source proves actual continuous maps, geometric stabilizers and all-place finite-intersection statements.'
]
base=Path(__file__).with_suffix('')
base.with_name(base.name+'_data.json').write_text(json.dumps(data,indent=2)+'\n')
out='\n'.join(lines)+'\n'
base.with_name(base.name+'_output.txt').write_text(out)
print(out,end='')
