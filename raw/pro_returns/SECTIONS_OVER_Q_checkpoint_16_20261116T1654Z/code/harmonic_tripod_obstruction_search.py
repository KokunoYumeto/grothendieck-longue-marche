#!/usr/bin/env python3
"""Exact finite search on the harmonic four-puncture quartic covers.

A retained search result is a finite computation, not a general vanishing
assertion. Every reported local point is certified by the local fourth-power
criterion and the printed root unit classes.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
from sympy import factorint


def vu(a, p, modulus=None):
    a = F(a)
    n, d, v = a.numerator, a.denominator, 0
    if n == 0:
        return None
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    mod = modulus or p
    return v, n * pow(d, -1, mod) % mod


def hilbert(a, b, p):
    if p == 2:
        va, ua = vu(a, 2, 8)
        vb, ub = vu(b, 2, 8)
        return (((ua-1)//2)*((ub-1)//2) + va*((ub*ub-1)//8)
                + vb*((ua*ua-1)//8)) % 2
    va, ua = vu(a, p)
    vb, ub = vu(b, p)
    la = int(pow(ua, (p-1)//2, p) == p-1)
    lb = int(pow(ub, (p-1)//2, p) == p-1)
    return (va*vb*((p-1)//2) + la*vb + lb*va) % 2


def fourth_roots_units(a, p):
    if a == 0:
        return []
    v, u = vu(a, p, 32 if p == 2 else p)
    if v % 4:
        return []
    if p == 2:
        residues = {1: [1, 7], 17: [3, 5]}.get(u, [])
    else:
        residues = ROOTS.setdefault(p, {}).get(u)
        if residues is None:
            if not ROOTS[p]:
                for z in range(1, p):
                    ROOTS[p].setdefault(pow(z, 4, p), []).append(z)
            residues = ROOTS[p].get(u, [])
    return [F(z) * F(p)**(v//4) for z in residues]


def is_square(a):
    a = F(a)
    return a >= 0 and isqrt(a.numerator)**2 == a.numerator and isqrt(a.denominator)**2 == a.denominator


def primes(a):
    a = F(a)
    return set(map(int, factorint(abs(a.numerator)))) | set(map(int, factorint(a.denominator)))


ROOTS = {}


def main():
    trials = covers = points = nonzero = 0
    parameters = sorted({F(n, d) for d in range(3, 32) for n in range(1, (d+1)//2)}, key=lambda x: (x.denominator, x.numerator))
    for R in parameters:
        boundary = [(1/(1-R), 1/(1-2*R)), (1/R, 1/(2*R-1)), (1/(2*R), 1/(2*(1-R)))]
        if any(is_square(-a) or is_square(-b) or is_square(-a*b) for a, b in boundary):
            continue
        u = 2*R-1
        d = u*(u*u-1)
        x2 = (u*u+1)**2/4
        y2 = (u*u+1)*(u**4-6*u*u+1)/8
        c = (1-x2/d)/2
        r = abs(y2/(d*d))
        if c in (0, F(1,2), 1, R) or r == 0:
            continue
        D = [c/R, (c-1)/(R-1), (c-F(1,2))/(R-F(1,2))]
        assert D[0]*D[1]*D[2] == -r*r
        char = 2*r
        S = {2, 3}
        for value in [R, R-1, R-F(1,2), c, c-1, c-F(1,2), R-c, char]:
            S |= primes(value)
        covers += 1
        for p in sorted(S):
            if p > 5000:
                continue
            limit = 2048 if p == 2 else min(p*p, 1500)
            candidates = [F(x) for x in range(1, limit+1)]
            candidates += [F(x,p) for x in range(1,min(p,500))]
            for X in candidates:
                T = R*X**4
                if T in (0, F(1,2), 1, c):
                    continue
                trials += 1
                Ys = fourth_roots_units((T-1)/(R-1), p)
                if not Ys:
                    continue
                Zs = fourth_roots_units((T-F(1,2))/(R-F(1,2)), p)
                if not Zs:
                    continue
                points += 1
                f = (T-c)/(R-c)
                if not hilbert(f, char, p):
                    continue
                nonzero += 1
                for Y, Z in product(Ys, Zs):
                    symbols = [[hilbert(W, a, p), hilbert(W, b, p)] for W, (a,b) in zip((X,Y,Z), boundary)]
                    if any(any(row) for row in symbols):
                        continue
                    print('EXACT LOCAL WITNESS', flush=True)
                    for key, value in [('R',R),('c',c),('r',r),('character',char),('p',p),('X',X),('T',T),('Y_root_unit_representative',Y),('Z_root_unit_representative',Z),('normalized_function',f),('boundary_symbols',symbols),('D',D)]:
                        print(f'{key}: {value}', flush=True)
                    print(f'covers={covers}, trials={trials}, local_points={points}, nonzero_evaluations={nonzero}', flush=True)
                    return
        if covers % 10 == 0:
            print(f'progress covers={covers}, trials={trials}, local_points={points}, nonzero_evaluations={nonzero}', flush=True)
    print(f'No witness in finite search: covers={covers}, trials={trials}, local_points={points}, nonzero_evaluations={nonzero}', flush=True)
    print('No general constancy or nonexistence conclusion is inferred.', flush=True)


if __name__ == '__main__':
    main()
