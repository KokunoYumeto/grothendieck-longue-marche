#!/usr/bin/env python3
"""Finite exact unit-power and norm-exponent checks for A.135."""
from math import gcd
from pathlib import Path
import sympy as sp
lines=[];tests=0
for r in range(1,7):
    m=3**r;modulus=3**(r+3)
    image={pow(u,m,modulus) for u in range(modulus) if u%3}
    expected={u for u in range(modulus) if u%3**(r+1) in [1,3**(r+1)-1]}
    assert image==expected
    positive={u for u in image if u%3==1}
    assert all(u%3**(r+1)==1 for u in positive)
    for a in range(1,m):
        if gcd(a,m)>1:continue
        A=pow(a,-1,m);B=(1-A*a)//m
        assert A*a+B*m==1
        for q in [1+3**r,1+2*3**r,1+3**(r+1)]:
            assert (pow(q,a,3**(r+1))==1)==(q%3**(r+1)==1)
            tests+=1
    lines.append(f'r={r}: exact unit-power image modulo3^{r+3} has '
                 f'{len(image)} elements; all positive classes are1mod3^{r+1}.')
for q in [61,67]:
    assert sp.isprime(q) and q%3==1
    roots=[a for a in range(q) if pow(a,3,q)==3]
    assert len(roots)==3 and (q-1)%9!=0
    lines.append(f'q={q}: roots of X^3=3 are {roots}; residue modulo9 is {q%9}.')
assert (61*67)%9==1
lines.append(f'ALL CHECKS PASSED: {tests} norm-exponent tests; '
             '61 and67 are individually noncubes in Q3 but their product is a cube.')
out='\n'.join(lines)+'\n'
Path(__file__).with_name('scalar_cyclotomic_precision_certificate_output.txt').write_text(out)
print(out,end='')
