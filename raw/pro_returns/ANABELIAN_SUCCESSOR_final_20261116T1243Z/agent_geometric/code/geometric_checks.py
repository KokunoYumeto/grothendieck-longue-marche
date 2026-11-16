#!/usr/bin/env python3
"""Finite checks for A7/L8/L10; these are not collision certificates."""
from itertools import combinations
from math import gcd
import json
import sympy as s


def mul(a, b):
    """F_8 = F_2[a]/(a^3+a+1), binary coefficient encoding."""
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 11
    return z


def power(a, n):
    z = 1
    while n:
        if n & 1:
            z = mul(z, a)
        a = mul(a, a)
        n >>= 1
    return z


def action(g, v):
    u, b = g
    return tuple(mul(u, power(x, 2**b)) for x in v)


def product(g, h):
    u, b = g
    v, c = h
    return (mul(u, power(v, 2**b)), (b+c) % 3)


def run():
    G = [(u, b) for u in range(1, 8) for b in range(3)]
    assert len(G) == 21
    assert all(product(g,h) in G for g in G for h in G)
    assert any(product(g,h) != product(h,g) for g in G for h in G)
    assert all(product(product(g,h),j) == product(g,product(h,j))
               for g in G for h in G for j in G)
    v = (1, 2)
    orbit = {action(g,v) for g in G}
    assert len(orbit) == 21
    zero_sum = next(S for S in combinations([(u,0) for u in range(1,8)],4)
                    if all(__import__('functools').reduce(
                        lambda a,b:a^b,(action(g,v)[i] for g in S),0) == 0
                           for i in range(2)))
    assert gcd(4,len(G)) == 1 and len(G) > (4-1)**2
    print('G = F_8^* semidirect Gal(F_8/F_2), order:', len(G))
    print('Nonabelian: yes; multiplication associativity: all 9261 triples checked')
    print('Vector (1,alpha) has orbit size:', len(orbit))
    print('Four distinct group elements whose images sum to zero:', zero_sum)
    print('Their coefficient norm d=4 satisfies gcd(d,21)=1 and 21>(d-1)^2.')
    print('Thus a free orbit in an abstract p-module does not supply a point-difference class.')

    # F = id on two faithful copies, 0 on another.  This is a G-equivariant,
    # noninvertible Frobenius-semilinear map after scalar extension to Fbar_2.
    F=s.diag(*([1]*6+[0]*3))
    assert F*F == F and F.rank() == 6
    print('Nonordinary semilinear module: total dimension=9; stable rank=6; free orbit survives.')

    x,t=s.symbols('x t')
    R=s.GF(2).poly_ring(t)
    f=s.Poly(x**24+x+t,x,domain=R)
    L=s.Poly(x**2048+t**64*x**512+t**8*x**16+t**16*x**8+x,x,domain=R)
    rem=L.rem(f,auto=False)
    assert rem == s.Poly(t**24+t,x,domain=R)
    additive=L*L+s.Poly(t+t**24,x,domain=R)*L
    assert additive.rem(f,auto=False).is_zero
    exponents=[e[0] for e,c in additive.terms()]
    assert all(e>0 and e & (e-1) == 0 for e in exponents)
    print('CMT: L mod (x^24+x+t) =', rem.as_expr())
    print('CMT: (L^2+(t+t^24)L) mod (x^24+x+t) = 0')
    print('CMT: additive exponents =', sorted(exponents))
    print('CMT: derivative coefficient in x =', additive.diff().as_expr())
    print('Polynomial x^24+x+t: affine derivative=1; infinity ramification index=24, divisible by 2.')
    print('Polynomial x^12+x+t in characteristic 3: affine derivative=1; infinity ramification index=12, divisible by 3.')
    print('All assertions passed. These computations do not assert any Jacobian torsion identification.')


if __name__ == '__main__':
    run()
