"""Finite checks for A168; the nonzero class proof is the exact norm argument."""
from itertools import product
from pathlib import Path
import json

base=Path(__file__).resolve().parent
classes=[]
for z,a,b,c in product(range(9),repeat=4):
    if a==0 and (b-z-3)%9==0 and (c-4*z-6)%9==0:
        classes.append([z,a,b,c])
assert len(classes)==9
assert all((c-4*b)%9==3 for z,a,b,c in classes)
assert not any(a==b==c==0 for z,a,b,c in classes)
assert [z for z in range(9) if (-z-3)%9==0]==[6]
assert [z for z in range(9) if (-4*z-6)%9==0]==[3]
print('PASS: all6561 residue tuples; nine surviving seed classes; none has a=b=c=0.')
print('PASS: exact eliminated affine constraint c59-4*c11=3 modulo9.')

records=[]
for n in range(2,9):
    modulus=3**n
    remaining=set(range(0,modulus,9))
    cycles=[]
    while remaining:
        a=min(remaining);orbit=[];b=a
        while b not in orbit:
            orbit.append(b);b=2*b%modulus
        assert b==a
        remaining.difference_update(orbit)
        cycles.append(orbit)
    assert sum(map(len,cycles))==3**(n-2)
    assert [o for o in cycles if len(o)==1]==[[0]]
    record={'n':n,'residue_degrees':[len(o) for o in cycles],
            'extension_degree':3**(n-2),'distinguished_norm_weight':1}
    records.append(record)
    print('LEVEL',n,'extension of old two-prime:',record['residue_degrees'],
          'sum',record['extension_degree'])

result={'surviving_mod9_classes':classes,'extension_cycles':records,
        'scope':'Finite congruence and norm-weight checks. The ordinary ideal-class nonvanishing and balanced order bounds are proved in A168.'}
(base/'two_inert_raw_two_class_certificate_data.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: unique degree-one branch and all seven balanced extension sums.')
