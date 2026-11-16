#!/usr/bin/env python3
"""Independent finite-image checks for the exact p-adic coefficient-prime lemma."""
from pathlib import Path
from math import gcd
import json

def vp(n,p):
    s=0
    while n%p==0:n//=p;s+=1
    return s
records=[]
for n,p,M in [(24,2,20),(24,3,9),(120,5,7),(840,7,6),(720,2,23),(720,3,12)]:
    s=vp(n,p);h=3*s+vp(48,p);depth=h+(3 if p==2 else 1)
    modulus=p**M
    q_precision=M-(2*s+vp(96,p))
    q_precision=max(q_precision,s+2)
    values=set();domain=0
    for q in range(1+p**s,p**q_precision,p**(s+1)):
        E=24*n*(q*q-1)
        assert vp(q-1,p)==s
        assert vp(E,p)==vp(48*n*n,p)
        values.add(pow(q,E,modulus));domain+=1
    q0=1+p**s
    first=pow(q0,24*n*(q0*q0-1),modulus)
    expected={(first+p**depth*z)%modulus for z in range(p**max(0,M-depth))}
    assert values==expected,(n,p,M,len(values),len(expected),values^expected)
    records.append({'n':n,'p':p,'s':s,'modulus':modulus,'domain_count':domain,'image_count':len(values),'predicted_coset_depth':depth,'base_value':first,'result':'exact equality'})
# The common finite-field image is controlled only by gcd(E,p-1).
finite=0
for n in [24,120,720]:
    D=48*n*n
    for p in [5,7,11,13,17,19,23,29,31,37]:
        if n%p==0:continue
        for e in range(2,p-1,2):
            if gcd(e,p-1)!=gcd(D,p-1):continue
            lhs={pow(q,e,p) for q in range(1,p)}
            rhs={pow(q,D,p) for q in range(1,p)}
            assert lhs==rhs
            if len(lhs)>1:
                for a in lhs-{1}:
                    assert all(q not in (1,p-1) for q in range(1,p) if pow(q,e,p)==a)
            else:
                assert any(q not in (1,p-1) for q in range(1,p) if pow(q,e,p)==1)
            finite+=1
result={'local_images':records,'finite_field_power_image_checks':finite,'scope':'Finite exact integer-power checks; the restricted-series proof establishes all precisions and all permitted primes.'}
text=json.dumps(result,indent=2)+'\n'
Path(__file__).with_name('class3_coefficient_image_certificate_output.txt').write_text(text)
print(text,end='')
