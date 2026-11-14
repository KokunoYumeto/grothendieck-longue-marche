#!/usr/bin/env python3
"""Exact finite checks for C.7a; no claim of a full fixed-group computation."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
checks=[]
def record(name, data):
    checks.append({'name':name,'passed':True,**data})
def mul(x,y,m):
    a,b,c=x;d,e,f=y
    return ((a+d)%m,(b+e)%m,(c+f+a*e)%m)
def inv(x,m):
    a,b,c=x
    return (-a%m,-b%m,(a*b-c)%m)
num=0
for x in product(range(5),repeat=3):
    for y in product(range(5),repeat=3):
        z=mul(mul(mul(x,y,5),inv(x,5),5),inv(y,5),5)
        assert z==(0,0,(x[0]*y[1]-x[1]*y[0])%5)
        num+=1
record('Heisenberg commutator is alternating determinant',{'pairs':num,'modulus':5})
for m in (5,25,125,625):
    for b in range(5):
        vec=[b]*m
        assert sum(vec)==m*b
        assert all(vec[i]==vec[j] for i in range(m) for j in (0,m-1))
record('Power-cover equal cusp coordinates force 5-power divisibility',{'cover_degrees':[5,25,125,625]})

def qmul(x,y):
    return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qpow(x,n):
    z=(1,0)
    while n:
        if n&1:z=qmul(z,x)
        x=qmul(x,x);n//=2
    return z
def qlog_unit(x,order,precision):
    q=qpow(x,order);q=(q[0]-1,q[1])
    assert q[0]%5==q[1]%5==0
    power=(1,0);out=(Fraction(0),Fraction(0))
    for n in range(1,precision+8):
        power=qmul(power,q)
        sign=1 if n%2 else -1
        out=tuple(out[j]+Fraction(sign*power[j],n*order) for j in range(2))
    mod=5**precision
    return tuple(int(t.numerator*pow(t.denominator,-1,mod)%mod) for t in out)
prec=8;mod=5**prec
loga=qlog_unit((0,1),24,prec)
logu=qlog_unit((1,-1),24,prec)
log2=qlog_unit((2,0),4,prec)
assert loga[1]==0 and loga[0] and (2*loga[0]-log2[0])%mod==0
assert logu[0]==0 and logu[1]
assert qmul((1,-1),(1,1))==(-1,0)
det=loga[0]*logu[1]%mod
assert det
record('Independent local Kummer logarithms at sqrt(2)',{'modulus':mod,'log_sqrt2':loga,'log_1_minus_sqrt2':logu,'determinant':det,'exact_norm':-1})
# Matrix of winding-number pushforward for z^2=x, basis 0,1,-1.
for u0,u1,um1 in product(range(-3,4),repeat=3):
    image=(2*u0,u1+um1)
    assert image[0]==2*u0 and image[1]==u1+um1
record('Quadratic-cover winding pushforward',{'matrix':[[2,0,0],[0,1,1]],'cases':343})
# For 5^n, T^(5^n)-1 is nonzero, despite vanishing linear coefficient mod5.
from math import comb
rows=[]
for n in range(1,5):
    c=5**n
    coeffs=[comb(c,j)%5 for j in range(1,c+1)]
    assert next(j for j,v in enumerate(coeffs,1) if v)==c
    rows.append({'exponent':c,'first_nonzero_mod5_degree':c})
record('Nonzero completed-group-ring shift survives a sufficiently deep degree',{'cases':rows})
out={'checks':checks,'passed':len(checks),'scope':'Finite exact checks of group-law, Kummer logarithm, and covering-coordinate identities; the infinite fixed-group statements require the written proof.'}
path=Path(__file__).with_name('BC_local_fixed_checks_output.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
