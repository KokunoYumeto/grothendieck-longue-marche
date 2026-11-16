#!/usr/bin/env python3
"""Exact finite arithmetic in B16; no infinite deformation is simulated."""
from collections import deque
from math import gcd
from pathlib import Path

def mul(a,b,n):
    return ((a[0]*b[0]+a[1]*b[2])%n,(a[0]*b[1]+a[1]*b[3])%n,
            (a[2]*b[0]+a[3]*b[2])%n,(a[2]*b[1]+a[3]*b[3])%n)

def generated(gens,n):
    identity=(1,0,0,1)
    found={identity}; todo=deque([identity])
    while todo:
        a=todo.popleft()
        for b in gens:
            ab=mul(a,b,n)
            if ab not in found:
                found.add(ab); todo.append(ab)
    return found

def vp(x,p):
    assert x
    v=0
    while x%p==0:
        v+=1; x//=p
    return v

points=1+sum(1 for x in range(5) for y in range(5)
             if (y*y-x*(x-1)*(x-3))%5==0)
assert points==4 and 5+1-points==2
delta=16*3**2*(3-1)**2; c4=16*(3**2-3+1)
assert (delta,c4)==(576,112) and vp(delta,3)==2
records=[]
for ell,primitive in [(7,3),(11,2)]:
    assert (-16)%ell not in {x*x%ell for x in range(ell)}
    upper=(1,1,0,1); lower=(1,0,1,1)
    sl=generated([upper,lower],ell)
    gl=generated([upper,lower,(primitive,0,0,1)],ell)
    assert len(sl)==ell*(ell*ell-1)
    assert len(gl)==(ell*ell-1)*(ell*ell-ell)
    assert {(a[0]*a[3]-a[1]*a[2])%ell for a in gl}==set(range(1,ell))
    records.append((ell,len(sl),len(gl)))
assert 13200%7 and 2016%11
assert gcd(13200,2016)==48 and gcd(6,10)==2
conjugacies=0
for ell,other in [(7,11),(11,7)]:
    for k in range(1,4):
        modulus=ell**k
        for q in range(2,ell-1):
            diagonal=(q,0,0,1)
            for exponent in range(k):
                for b in range(1,2*ell):
                    if b%ell==0: continue
                    B=ell**exponent*b; M=ell**exponent*other**k
                    unit=(other**k*pow(b,-1,modulus))%modulus
                    h=(unit,0,0,1); hi=(pow(unit,-1,modulus),0,0,1)
                    assert mul(mul(h,(1,B%modulus,0,1),modulus),hi,modulus)==(1,M%modulus,0,1)
                    assert mul(mul(h,diagonal,modulus),hi,modulus)==diagonal
                    assert M%(other**k)==0
                    conjugacies+=1
traces=0
for level in range(1,4):
    left,right=7**level,11**level; modulus=left*right
    residues=range(modulus) if level<=2 else range(0,modulus,113)
    for residue in residues:
        a7,a11=residue%left,residue%right
        crt=(a7+left*((a11-a7)*pow(left,-1,right)%right))%modulus
        assert crt==residue
        a=crt if 2*crt<=modulus else crt-modulus
        if a==0: a=modulus
        q=modulus**2+1
        assert a%left==a7 and a%right==a11 and a*a<4*q and a!=0
        traces+=1
out=(f'B16 exact two-coefficient certificate\n'
     f'E3: discriminant{delta}, c4={c4}, #E(F5)={points}, a5=2.\n'
     f'Generated groups (ell,SL2,GL2): {records}.\n'
     'Cross-prime order checks:7 does not divide13200;11 does not divide2016; determinant-degree gcd2.\n'
     f'Exact common-Tate unit conjugacies: {conjugacies}.\n'
     f'CRT and strict Hasse-interval checks: {traces}.\n'
     'All checks passed. The continuous deformation, disjoint-field choices, and simultaneous lattice isogeny are proved in B16; no auxiliary-prime sequence is claimed computed.\n')
Path(__file__).with_name('two_coefficient_elliptic_certificate_output.txt').write_text(out)
print(out,end='')
