#!/usr/bin/env python3
"""Exact field/character, coordinate and depth identities for A.116."""
import sympy as S
from itertools import product

CHI={}
for k in range(4):
    for sign in (1,-1):CHI[sign*pow(5,k,16)%16]=k
root_cases=fixed_cases=0
for u,e,j in product(range(1,16,2),range(2),range(1,16,2)):
    root_cases+=1
    fixes=(j*(u-1)+8*e)%16==0
    if fixes:
        assert u==(1+8*e)%16
        assert (CHI[u]+2*e)%4==0
        fixed_cases+=1
assert all((2*(CHI[u]+2*e))%4==2*CHI[u]%4 for u,e in product(range(1,16,2),range(2)))
product_fibres=[0]*8
for exponents in product(range(8),repeat=3):
    product_fibres[sum(exponents)%8]+=1
assert product_fibres==[64]*8

T,R,c,X,D,b,w,z=S.symbols('T R c X D b w z',nonzero=True)
F=lambda x:x*(x-1)*(x-S.Rational(1,2))
g1=lambda x:1-x
g2=lambda x:1/(2*x)
assert S.cancel(F(g1(T))+F(T))==0
assert S.cancel(F(g2(T))-F(T)/(4*T**4))==0
f=(T-c)/(R-c)
assert S.cancel((g2(T)-g2(c))/(g2(R)-g2(c))-f*R/T)==0
assert S.cancel((F(g2(c))/F(g2(R)))/(F(c)/F(R))-(R/c)**4)==0
assert S.expand((X**4)**2-D-(X**8-D))==0
assert S.expand(1-D-(1-D))==0
assert S.resultant(z**8+b**4,X-z,z)==X**8+b**4
assert S.expand((1+8*w)**4-1-32*(w+12*w*w+64*w**3+128*w**4))==0
poly=w+12*w*w+64*w**3+128*w**4
assert S.Poly(S.diff(poly,w)-1,w,modulus=2).is_zero

# Literal depth implications of the restricted remaining branches.
depth_checks=0
for e,eT,k in product(range(1,49),range(1,49),range(-8,49)):
    if (e-eT)%8:continue
    delta=min(e,eT) if e!=eT else e+5
    if delta<5:continue
    if e<=4:
        assert eT==e
        if k!=e:assert delta-min(e,k)>=5
        else:assert delta-(e+1)>=4
        depth_checks+=1
    elif k<=0:
        assert delta-k>=5;depth_checks+=1
    elif k<=4 and (k-e)%4==0:
        assert min(e,eT)-k>=4
        depth_checks+=1

print('Literal cyclotomic/quadratic/root-action cases:',root_cases)
print('Fixed-root cases killing the order-four character:',fixed_cases)
print('Literal product-root map:512 root tuples,8 fibres of size64.')
print('Exact tested depth implications:',depth_checks)
print('Coordinate changes, eighth-degree norm resultant and principal-unit fourth-root polynomial passed.')
print('The local proof is A.116.1--A.116.12; these checks do not infer full common-field generation.')

