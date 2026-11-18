#!/usr/bin/env python3
"""Direct affine fixed-point counts for A.33, not a density computation."""
from fractions import Fraction
from hashlib import sha256
from math import gcd
from pathlib import Path
import json

def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))

rows=[]
for n in [p for p in range(2,48) if prime(p)]+[6,10,15,30,105,210]:
    units=[a for a in range(n) if gcd(a,n)==1]
    fixed=0
    distribution={}
    for a in units:
        for b in range(n):
            count=sum((a*x+b)%n==x for x in range(n))
            distribution[count]=distribution.get(count,0)+1
            fixed+=bool(count)
    total=n*len(units)
    observed=Fraction(fixed,total)
    expected=Fraction(len(units),n)
    assert observed==expected,(n,observed,expected)
    rows.append(dict(modulus=n,total_affine_elements=total,
                     elements_with_fixed_points=fixed,
                     fraction=str(observed),fixed_point_distribution=distribution))
data={'scope':'Direct enumeration of finite affine permutations for squarefree moduli; no prime-density census or section existence claim.',
      'rows':rows,'total_permutations':sum(r['total_affine_elements'] for r in rows)}
data['sha256']=sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS:',len(rows),'squarefree moduli;',data['total_permutations'],'affine permutations.')
for r in rows: print(r['modulus'],r['elements_with_fixed_points'],r['total_affine_elements'],r['fraction'])
print('SHA256:',data['sha256'])
