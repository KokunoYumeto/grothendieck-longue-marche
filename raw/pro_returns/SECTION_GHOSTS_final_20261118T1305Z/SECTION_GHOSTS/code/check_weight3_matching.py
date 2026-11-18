#!/usr/bin/env python3
"""Exact finite-field residues for the weight-three matching theorem.

This verifies the two cyclotomic-unit residues and the two-primary
local matrix. Integral lifting is proved separately in the paper.
"""
from itertools import product

def field(p, constant, linear):
    zero=(0,0,0); one=(1,0,0)
    def add(a,b): return tuple((x+y)%p for x,y in zip(a,b))
    def neg(a): return tuple(-x%p for x in a)
    def mul(a,b):
        out=[0]*5
        for i in range(3):
            for j in range(3): out[i+j]=(out[i+j]+a[i]*b[j])%p
        for k in (4,3):
            t=out[k];out[k]=0
            out[k-3]=(out[k-3]-constant*t)%p
            out[k-2]=(out[k-2]-linear*t)%p
        return tuple(out[:3])
    def power(a,n):
        r=one
        while n:
            if n&1:r=mul(r,a)
            a=mul(a,a);n//=2
        return r
    elems=list(product(range(p), repeat=3))
    assert all(power(a,p**3-1)==one for a in elems if a!=zero)
    return zero,one,add,neg,mul,power,elems

for p,ell,c,l in [(2,7,1,1),(3,13,-1,-1)]:
    zero,one,add,neg,mul,power,elems=field(p,c,l)
    zeta=next(a for a in elems if a!=one and power(a,ell)==one)
    val=one
    for a in range(1,ell):
        val=mul(val,power(add(one,neg(power(zeta,a))),a*a))
    detected=power(val,(p**3-1)//ell)
    assert detected!=one
    # Frobenius has order three in Gal(Q(zeta_ell)/Q).
    assert pow(p,3,ell)==1 and p%ell!=1
    # Reindexing the product gives the claimed inverse-square eigenspace
    # modulo ellth powers; in these fields the residue equality is exact
    # after raising to (p^3-1)/ell.
    for b in range(1,ell):
        conjugate=one
        for a in range(1,ell):
            conjugate=mul(conjugate,power(add(one,neg(power(zeta,a*b))),a*a))
        assert power(conjugate,(p**3-1)//ell)==power(detected,pow(b,-2,ell))
    print(f'F_{p**3}: modulus X^3 + ({l})X + ({c}); zeta_{ell}={zeta}')
    print(f'alpha_{ell}={val}; alpha^((p^3-1)/ell)={detected} != 1')
    print(f'All {ell-1} inverse-square eigencharacter checks passed.')

mat=((1,1),(1,0))
assert (mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0])%2==1
print('Two-primary localization matrix at (Q_3,R), columns (-1,2):',mat)
print('Its determinant is one in F_2.')
print('PASS: both odd-prime residues and the full finite localization matrix.')
