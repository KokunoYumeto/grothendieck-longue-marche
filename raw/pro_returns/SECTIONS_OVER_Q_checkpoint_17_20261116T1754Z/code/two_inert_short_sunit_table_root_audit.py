#!/usr/bin/env python3
"""Reconstruct A165's printed generators and independently verify their norms."""
from pathlib import Path
from fractions import Fraction as Q
import json,re,sys
sys.set_int_max_str_digits(0)
w=Path(__file__).resolve().parents[1]
source=(w/'sections/two_inert_short_sunit_coefficients.tex').read_text()
parts=source.split('Generator $')[1:]
assert len(parts)==3
B=10**40;d=649;coordinates=[];row_count=0
for part in parts:
    rows=re.findall(r'^([0-8]) & ([0-9]+) & ([+-]) & ([0-9]{40}) & ([0-9]{40})',part,re.M)
    signs={};blocks={}
    for i0,k0,sign,lo,hi in rows:
        i,k=int(i0),int(k0)
        assert k%2==0
        signs.setdefault(i,sign);assert signs[i]==sign
        for delta,value in enumerate((lo,hi)):
            assert (i,k+delta) not in blocks
            blocks[i,k+delta]=int(value)
    assert set(signs)==set(range(9))
    ints=[(-1 if signs[i]=='-' else 1)*sum(v*B**k for(j,k),v in blocks.items() if j==i) for i in range(9)]
    coordinates.append([Q(ints[i],d**(2*i//3)) for i in range(9)])
    row_count+=len(rows)

def add(a,b):return [x+y for x,y in zip(a,b)]
def mul(a,b):
    out=[Q(0)]*5
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    for k in [4,3]:out[k-3]+=3*out[k]
    return out[:3]
def cube(a):return mul(mul(a,a),a)
def norm9(cs):
    aa,bb,cc=[[cs[k+3*i]*d**(2*i) for i in range(3)] for k in range(3)]
    rad=[Q(0),Q(d*d),Q(0)]
    return add(add(cube(aa),mul(rad,cube(bb))),
               add(mul(mul(rad,rad),cube(cc)),[-3*x for x in mul(rad,mul(mul(aa,bb),cc))]))
def norm3(x):
    a,b,c=x;return a**3+3*b**3+9*c**3-9*a*b*c

raw=json.loads((w/'code/two_inert_short_sunit_principal_certificate_data.json').read_text())
for index,(cs,expected) in enumerate(zip(coordinates,[-121,-649,-3481]),6):
    assert all((cs[i]*d**(2*i//3)).denominator==1 for i in range(9))
    assert all(6*i-9*(2*i//3)>=0 for i in range(9))
    computed=norm9(cs)
    assert norm3(computed)==expected
    assert cs==[Q(x) for x in raw['generators'][str(index)]['coefficients']]
    assert computed==[Q(x) for x in raw['generators'][str(index)]['relative_norm']]
    print(f'Printed generator {index}: nine coefficients, integral coordinates, exact relative norm, and rational norm {expected}: PASS')
print(f'PASS: {row_count} printed two-block rows reconstruct all27 integer coefficients without a computer-algebra norm routine.')
print('Prime norm support plus the independently certified local valuations gives the exact three divisors used in A165.')
