#!/usr/bin/env python3
"""Independent exact certificates for the genus-two projected norm obstruction."""
from itertools import product
from fractions import Fraction
import json
import sympy as sp

x,y,t,z=sp.symbols('x y t z')
curve=y*y-x**5+54*x
t_of=x**4/(x**4-54); z_of=3*x/y
numer=sp.together(z_of**8+t_of*(1-t_of)**3/24).as_numer_denom()[0]
assert sp.rem(numer,curve,y)==0
x_of=-6*z*z/(1-t); y_of=-18*z/(1-t)
cover=24*z**8+t*(1-t)**3
numer=sp.together(y_of*y_of-x_of**5+54*x_of).as_numer_denom()[0]
assert sp.rem(numer,cover,z)==0
for left,right in ((x_of,x),(y_of,y)):
    numer=sp.together(left.subs({t:t_of,z:z_of}, simultaneous=True)-right).as_numer_denom()[0]
    assert sp.rem(numer,curve,y)==0
for left,right in ((t_of,t),(z_of,z)):
    numer=sp.together(left.subs({x:x_of,y:y_of}, simultaneous=True)-right).as_numer_denom()[0]
    assert sp.rem(numer,cover,z)==0

def shift(a,j,k):
    j%=k; mask=(1<<k)-1
    return ((a<<j)|(a>>(k-j)))&mask if j else a
def mul(g,h,k):return (g[0]^shift(h[0],g[1],k),(g[1]+h[1])%8)
def inv(g,k):return (shift(g[0],-g[1],k),-g[1]%8)
def comm(g,h,k):return mul(mul(mul(g,h,k),inv(g,k),k),inv(h,k),k)
def power(g,n,k):
    if n<0:g,n=inv(g,k),-n
    a=(0,0)
    while n:
        if n&1:a=mul(a,g,k)
        g=mul(g,g,k);n//=2
    return a
def closure(generators,k):
    out={(0,0)};todo=[(0,0)]
    while todo:
        a=todo.pop()
        for g in generators:
            b=mul(a,g,k)
            if b not in out:out.add(b);todo.append(b)
    return out

groups={}
for k in (4,2):
    v=(0,1);u=(1,0);other=mul(u,power(v,3,k),k)
    G=closure([v,u],k);assert len(G)==8*2**k
    assert power(v,8,k)==power(other,8,k)==(0,0)
    assert power(mul(v,other,k),2,k)==(0,0)
    sizes=[len(G)];current=G
    while len(current)>1:
        current=closure([comm(a,b,k) for a in current for b in G],k)
        sizes.append(len(current))
    assert sizes==([128,8,4,2,1] if k==4 else [32,2,1])
    groups[str(8*2**k)]={'lower_central_sizes':sizes}

def quotient(g):
    a,j=g; return ((((a>>0)^(a>>2))&1)|(((((a>>1)^(a>>3))&1))<<1),j)
G=list(product(range(16),range(8)))
for g in G:
    for h in G:
        assert quotient(mul(g,h,4))==mul(quotient(g),quotient(h),2)

def algmul(a,b):return (a[0]*b[0]+6*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
assert algmul((2,1),(2,1))==(10,4)
assert algmul((3,1),(3,1))==(15,6)
assert algmul((9,-3),(3,1))==(9,0)
assert algmul((-2,-1),(9,-3))==(0,-3)
candidates=[]
for a,b,c,d in product(range(2),repeat=4):
    if a==c and b==0:candidates.append([a,b,c,d])
assert len(candidates)==4

p=1129
assert all(p%d for d in range(2,34))
assert pow(2,24,p)==276 and pow(56,24,p)==978
assert (3*276-2*978)%p==1
assert (3*276)%p==828
rad=(-828*pow(1-828,3,p)*pow(24,-1,p))%p
assert rad==1115
roots=[a for a in range(p) if pow(a,8,p)==rad]
assert roots==[35,44,235,511,618,894,1085,1094]
r_values=[838,291]
assert all(r*r%p==6 for r in r_values)
square_witnesses=[[17,426],[29,221]]
for j,r in enumerate(r_values):
    assert square_witnesses[0][j]**2%p==(-2-r)%p
    assert square_witnesses[1][j]**2%p==(3+r)%p
sheets=[]
for zz in roots:
    xx=-6*zz*zz*pow(1-828,-1,p)%p
    yy=-18*zz*pow(1-828,-1,p)%p
    assert yy*yy%p==(xx**5-54*xx)%p
    norms=[(xx*xx-3*r)%p for r in r_values]
    assert all(pow(a,(p-1)//2,p)==p-1 for a in norms)
    assert (8*pow(zz,7,p))%p
    sheets.append({'z':zz,'x':xx,'y':yy,'norms':norms,'squareclass_vector':[1,1]})

print(json.dumps({'birational_maps':'all four compositions and curve identities verified',
 'geometric_groups':groups,'quotient_multiplication_checks':len(G)**2,
 'supported_squareclass_survivors':candidates,'prime':p,'radicand':rad,
 'all_local_sheets':sheets,'scope':'Finite identities only; the paper proves all-place Selmer exhaustiveness.'},indent=2))
print('PASS: exact genus-two norm certificates.')
