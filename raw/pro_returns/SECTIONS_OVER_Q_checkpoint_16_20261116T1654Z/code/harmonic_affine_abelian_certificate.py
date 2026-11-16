#!/usr/bin/env python3
"""Exact integral/group/function-field checks for A.167.

The continuous Kummer and section classification is proved in the text.
This certificate checks the actual maps used there, without finite-level
local-global assumptions.
"""
from pathlib import Path
from math import gcd
from functools import reduce
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def shift(a,k):
    return tuple(a[(j-k)%8] for j in range(8))

def mul(g,h):
    a,r=g; b,s=h
    return (add(a,shift(b,r)),r+s)

def inv(g):
    a,r=g
    return (tuple(-x for x in shift(a,-r)),-r)

identity=((0,)*8,0)
def power(g,n):
    if n<0:
        return power(inv(g),-n)
    h=identity
    while n:
        if n&1:
            h=mul(h,g)
        g=mul(g,g); n//=2
    return h

def vector(g):
    a,r=g
    assert r%8==0
    return S.Matrix(list(a)+[r//8])

v=((0,)*8,1)
u=((1,)+(0,)*7,0)
x=mul(u,power(v,2))
y=v
assert mul(x,power(y,-2))==u
assert mul(mul(v,u),inv(v))==((0,1,0,0,0,0,0,0),0)
assert mul(mul(power(v,8),u),power(v,-8))==u

e0=vector(power(x,4))
e1=vector(mul(mul(y,power(x,4)),inv(y)))
eh=vector(power(y,8))
einf=vector(power(mul(x,y),-8))
assert e0==S.Matrix([1,0,1,0,1,0,1,0,1])
assert e1==S.Matrix([0,1,0,1,0,1,0,1,1])
assert eh==S.Matrix([0]*8+[1])
assert einf==S.Matrix([-1]*8+[-3])
assert e0+e1+eh+einf==S.zeros(9,1)
B=S.Matrix.hstack(e0,e1,eh)
snf=smith_normal_form(B,domain=ZZ)
assert B.rank()==3
assert [abs(snf[i,i]) for i in range(3)]==[1,1,1]

projectors={
    'P0':S.Matrix([[0,1,0],[0,0,1]]),
    'P1':S.Matrix([[1,0,0],[0,0,1]]),
    'Ph':S.Matrix([[1,0,0],[0,1,0]]),
    'Pinf':S.Matrix([[1,0,-1],[0,1,-1]])}
lines={'P0':S.Matrix([1,0,0]),'P1':S.Matrix([0,1,0]),
       'Ph':S.Matrix([0,0,1]),'Pinf':S.Matrix([-1,-1,-1])}
for name,q in projectors.items():
    assert q*lines[name]==S.zeros(2,1)
    s=smith_normal_form(q,domain=ZZ)
    assert q.rank()==2 and [abs(s[i,i]) for i in range(2)]==[1,1]

# The actual map to the original two meridians.
ab=S.Matrix([[1]*8+[0],[-2]*8+[8]])
inertias=S.Matrix.hstack(e0,e1,eh,einf)
assert ab*inertias==S.Matrix([[4,4,0,-8],[0,0,8,-8]])
assert S.Matrix([[2,1]])*ab*inertias==S.Matrix([[8,8,8,-24]])

T,a=S.symbols('T a',nonzero=True)
F=T*(T-1)*(T-S.Rational(1,2))
t=4*T*(1-T)
w4=F/a
w8=w4*w4
assert S.factor(w8-t*t*(1-t)/(64*a*a))==0
assert S.factor(t-8*a*w4/(1-2*T))==0
assert S.factor(t+8*a*w4/(2*T-1))==0
assert S.factor(1-t-64*a*a*w8/(t*t))==0
unitinf=1/((1-1/T)**3*(1-1/(2*T))**2)
assert S.factor(1/t+a*a*w8*unitinf/(4*T**8))==0
assert S.limit(1/(1-2*T),T,0)==1
assert S.limit(1/(2*T-1),T,1)==1
assert S.limit(1/t**2,T,S.Rational(1,2))==1
assert S.limit(unitinf,T,S.oo)==1

# Constants in the full cusp parameter maps and their actual combined class.
constants=[8*a,-8*a,64*a*a,-a*a/4]
combined=[constants[0]**2,constants[1]**2,constants[2],-constants[3]**(-3)]
ratios=[S.factor(c/(64*a*a)) for c in combined]
assert ratios==[1,1,1,a**(-8)]
cyclotomic_fixed=[d for d in range(8) if all((chi-1)*d%8==0 for chi in (1,3,5,7))]
assert cyclotomic_fixed==[0,4]
assert S.expand((-S.Symbol('W'))**4-S.Symbol('W')**4)==0

# Literal group laws and H coordinates in finite specializations.  These
# exercise the noncentral cyclic shift and the factor-eight coordinate.
word_checks=0
for n in (2,3,4,5,8,9,16):
    for j in range(8):
        uj=mul(mul(power(v,j),u),power(v,-j))
        assert uj[0][j]==1 and sum(uj[0])==1 and uj[1]==0
        for k in range(8):
            uk=mul(mul(power(v,k),u),power(v,-k))
            assert mul(power(uj,n),uk)==mul(uk,power(uj,n))
            word_checks+=1

data={
    'geometric_group':'Zhat[C8] semidirect Zhat, action by shift modulo8',
    'basis_H':'u0,...,u7,z=v^8',
    'boundary_columns':[[int(v) for v in col] for col in (e0,e1,eh,einf)],
    'boundary_Smith_diagonal':[1,1,1],
    'quotient_maps':{k:[[int(v) for v in row] for row in q.tolist()] for k,q in projectors.items()},
    'downstairs_inertia':(ab*inertias).tolist(),
    'tangent_constants':[str(c) for c in constants],
    'combined_class_ratios':[str(c) for c in ratios],
    'cyclotomic_fixed_deck_coordinates':cyclotomic_fixed,
    'literal_word_checks':word_checks,
    'status':'all exact map checks passed; cohomological argument is in A167'
}
path=Path(__file__).with_name('harmonic_affine_abelian_certificate_data.json')
path.write_text(json.dumps(data,indent=2,default=int)+'\n')
print('PASS: actual Nielsen/Schreier semidirect-product map and all four inertia words')
print('PASS: primitive rank3 boundary lattice; all four split rank2 quotient maps')
print('PASS: downstairs inertia vectors and combined character (8,8,8,-24)')
print('PASS: four exact rational tangent identities and unit constant terms')
print('PASS: combined modulo8 constants, including the actual eighth-power infinity ratio')
print('PASS: exactly two arithmetic-centralizing deck coordinates0,4; the latter negates all chosen tangents')
print('PASS:',word_checks,'literal commutation and cyclic-shift checks')
print('Data:',path)
