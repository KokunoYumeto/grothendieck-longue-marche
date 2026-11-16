#!/usr/bin/env python3
"""Exact finite data for A.149. The global coherence proof is in the TeX."""
from math import gcd, comb

p=11
def mul(a,b):
    # t^2=2t-4 over F_11.
    return ((a[0]*b[0]-4*a[1]*b[1])%p,
            (a[0]*b[1]+a[1]*b[0]+2*a[1]*b[1])%p)
def pw(a,n):
    out=(1,0)
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out
def sub(a,b):return ((a[0]-b[0])%p,(a[1]-b[1])%p)
one=(1,0);t=(0,1)
assert all((x*x-2*x+4)%p for x in range(p))
assert pw(t,3)==(3,0)
units=[(a,b) for a in range(p) for b in range(p) if (a,b)!=(0,0)]
assert len(units)==120 and all(pw(u,120)==one for u in units)
zeta=pw(t,40)
assert zeta!=one and pw(zeta,3)==one
mu3={one,zeta,pw(zeta,2)}
cosets={tuple(sorted(mul(u,z) for z in mu3)) for u in units}
assert len(cosets)==40 and gcd(len(cosets),3)==1
def char(u):
    return next(j for j in range(3) if pw(u,40)==pw(zeta,j))
unitU=sub(pw(t,2),(2,0))
beta0=mul(sub(one,t),unitU)
chars=(char(t),char(sub(one,t)),char(unitU),char(beta0))
assert chars==(1,0,2,2)
assert (8*char(beta0)-char(t))%3==0
assert sorted(x for x in range(1,11) if pow(x,24,11)==9)==[5,6]
assert sorted(x for x in range(1,11) if (-2*pow(x,24,11))%11==1)==[2,9]
assert [x for x in range(11) if pow(x,3,11)==3]==[9]
norm=lambda a,b,c:a**3+3*b**3+9*c**3-9*a*b*c
assert norm(2,1,0)==11 and norm(1,-1,0)==-2 and norm(-2,0,1)==1
assert -2*1+1*2==0

stable_checks=0
for j in range(1,9):
    N=3**j
    a=pow(8,-1,N);b=(1-8*a)//N
    assert 8*a+N*b==1
    assert gcd(N,120)==3
    images={pw(u,N) for u in units}
    assert len(images)==40
    # Exact residue condition after subtracting the uniformizer norm.
    residue=mul(beta0,pw(t,(-a)%120))
    assert residue in images
    for u in units:
        assert (u in images)==(char(u)==0)
        stable_checks+=1

def vp3(x):
    n=0
    while x%3==0:
        n+=1;x//=3
    return n
projection_checks=0
for r in range(1,31):
    flog=0
    while 3**(flog+1)<=r:flog+=1
    j=r+flog
    # Only the first r coefficients are needed; Python handles these integers exactly.
    N=3**j
    for k in range(1,r+1):
        assert vp3(comb(N,k))>=r
        projection_checks+=1

print('A.149 exact certificate PASS')
print('Ray residue group: |F121^x|=120; quotient by mu3 has order40.')
print('Cubic characters (alpha,1-alpha,U,beta0):',chars)
print('Stable norm residue checks:',stable_checks)
print('Old-cover Y coordinates for -2*Y^24=1 modulo11:',[2,9])
print('Norm gamma=11, norm U=1, norm(1-alpha)=-2; q-divisor norm -2+2=0.')
print('Actual derived-to-augmentation coefficient bounds:',projection_checks)
print('Global class-field duality and coherent S-unit existence are proved in A.149, not numerically inferred.')
