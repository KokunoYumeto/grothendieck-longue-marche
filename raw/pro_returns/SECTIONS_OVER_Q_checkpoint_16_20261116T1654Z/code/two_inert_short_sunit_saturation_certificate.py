"""Rank12 certificate for the FINAL literal S-generators, not discovery products."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import json
import sys

sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parent
units=json.loads((base/'two_inert_relative_unit_repair_certificate_data.json').read_text())['units']
gen=json.loads((base/'two_inert_norm2_generator_certificate_data.json').read_text())
short=json.loads((base/'two_inert_short_sunit_principal_certificate_data.json').read_text())['generators']
detectors=json.loads((base/'two_inert_compact_sunit_saturation_search_data.json').read_text())['rows']
beta2=[-F(int(n),int(gen['generator_common_denominator'])) for n in gen['generator_numerators']]


def evaluate(poly,t,p):
    value=0
    for coefficient in reversed(poly):
        c=F(coefficient)
        value=(value*t+c.numerator*pow(c.denominator,-1,p))%p
    return value


rows=[]
echelon={}
for detector in detectors:
    p,t,omega=detector['p'],detector['t'],detector['omega']
    assert p>=2 and all(p%q for q in range(2,isqrt(p)+1))
    assert pow(t,9,p)==3*pow(649,6,p)%p
    assert omega!=1 and pow(omega,3,p)==1
    alpha=pow(t,3,p)*pow(649,-2,p)%p
    assert pow(alpha,3,p)==3
    r={i:evaluate(short[str(i)]['coefficients'],t,p) for i in (6,7,8)}
    b2=evaluate(beta2,t,p)
    values=[evaluate(row['candidate'],t,p) for row in units]
    values.extend([b2,(1-alpha)*pow(b2,-1,p)%p,2*pow(alpha-1,-1,p)%p,
                   t*pow(r[6]*r[7]*r[8],-2,p)%p,(2+alpha)%p,r[6],r[7],r[8]])
    assert all(values)
    logs={1:0,omega:1,omega*omega%p:2}
    row=[logs[pow(value,(p-1)//3,p)] for value in values]
    new=row[:]
    for pivot,basisrow in sorted(echelon.items()):
        c=new[pivot];new=[(a-c*b)%3 for a,b in zip(new,basisrow)]
    pivot=next((i for i,a in enumerate(new) if a),None)
    assert pivot is not None
    echelon[pivot]=[a*pow(new[pivot],-1,3)%3 for a in new]
    rows.append({'p':p,'t':t,'omega':omega,'values':values,'row':row})
    print('FINAL ROW',p,t,row)
assert len(echelon)==12
(base/'two_inert_short_sunit_saturation_certificate_data.json').write_text(json.dumps(
    {'rank':12,'rows':rows,'basis':'u1,u2,u3,u4,s1,...,s8 exactly as A165.12'},indent=2)+'\n')
print('PASS: final literal representatives have residue rank12 directly; no compact-product replacement is needed.')
