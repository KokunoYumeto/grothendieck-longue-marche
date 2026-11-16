#!/usr/bin/env python3
"""Exact base restriction classes of the three normalized K2 units.

The twelve residue maps are the complete saturated A165 S-unit test.
Equality of their rows therefore proves equality of the actual classes
modulo cubes, not just agreement at a selected set of primes.
"""
from fractions import Fraction
from pathlib import Path
from itertools import product
import json,sys
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parent
rows=json.loads((B/'two_inert_short_sunit_saturation_certificate_data.json').read_text())['rows']
units=json.loads((B/'two_inert_relative_unit_repair_certificate_data.json').read_text())['units']

def rank(a):
    a=[list(row) for row in a];r=0
    for j in range(len(a[0])):
        k=next((k for k in range(r,len(a))if a[k][j]%3),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];iv=pow(a[r][j]%3,-1,3)
        a[r]=[iv*x%3 for x in a[r]]
        for k in range(len(a)):
            if k!=r:
                q=a[k][j]%3;a[k]=[(x-q*y)%3 for x,y in zip(a[k],a[r])]
        r+=1
    return r

def ev(poly,t,p):
    s=0
    for raw in reversed(poly):
        v=Fraction(raw);s=(s*t+v.numerator*pow(v.denominator,-1,p))%p
    return s

assert rank([r['row']for r in rows])==12
mat=[];targetcols=[[],[],[]]
for r in rows:
    p,t,om=r['p'],r['t'],r['omega']
    assert pow(t,9,p)==3*pow(649,6,p)%p
    alpha=pow(t,3,p)*pow(649,-2,p)%p
    assert pow(alpha,3,p)==3%p
    U=(alpha*alpha-2)%p
    values=[U,alpha,(alpha-1)%p,(2+alpha)%p,
            (2+2*alpha-alpha*alpha)%p,2,11,59]
    logs={1:0,om:1,om*om%p:2}
    row=[logs[pow(v,(p-1)//3,p)]for v in values]
    assert row[0]==r['row'][0]
    mat.append(row)
    for col,(j,g) in enumerate(((1,19),(2,-1),(3,538))):
        ui=ev(units[j]['candidate'],t,p)
        assert logs[pow(ui,(p-1)//3,p)]==r['row'][j]
        v=ui*pow(U,-g,p)%p
        targetcols[col].append(logs[pow(v,(p-1)//3,p)])

assert rank(mat)==7
def image(e):return tuple(sum(a*b for a,b in zip(row,e))%3 for row in mat)
radical=(0,1,0,0,0,0,2,2)
assert image(radical)==(0,)*12
kernel=[e for e in product(range(3),repeat=8)if image(e)==(0,)*12]
assert kernel==[tuple(i*x%3 for x in radical)for i in range(3)]
assert len({image(e)for e in product(range(3),repeat=8)})==3**7
print('PASS: base restriction rank7 and exact radical kernel <d^2 alpha>')

expected=[(0,0,0,2,0,0,2,1),
          (2,0,0,0,2,0,2,0),
          (2,0,0,1,0,0,0,1)]
out=[]
for index,(target,want) in enumerate(zip(targetcols,expected),2):
    sols=[e for e in product(range(3),repeat=8)if image(e)==tuple(target)]
    assert len(sols)==3
    actual=next(e for e in sols if e[1]==0)
    assert actual==want
    assert set(sols)=={tuple((a+i*b)%3 for a,b in zip(want,radical))for i in range(3)}
    out.append({'unit_index':index,'normalized_base_class':actual,
                'all_base_representatives':sols,'twelve_residue_values':target})
    print('PASS: normalized unit',index,'base coordinates',actual)

data={'base_order':['U','alpha','gamma2','gamma11','gamma59','2','11','59'],
      'detector_rank':12,'restriction_matrix':mat,'restriction_rank':7,
      'radical_kernel':radical,'normalized_units':out,
      'scope':'Actual S-unit class identities modulo cubes via the proved complete A165 quotient; no secondary character or least-weight value is asserted.'}
(B/'two_inert_base_restriction_unit_classes_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: complete residue-lattice comparison of all three normalized relative units')
