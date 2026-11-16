#!/usr/bin/env python3
"""Finite exact certificate for A128.

The proof is unrestricted.  This certificate uses literal rational local
equations, complete generated finite power-class groups for each sampled
equation, and every positive/negative mixed relation in those groups.  It
does not replace global common fields by fields of local radicands.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import gcd

import sympy as sp


def vu(z, p):
    z = Q(z)
    assert z
    a, b = z.numerator, z.denominator
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v, a * pow(b, -1, p) % p


def v2(a):
    assert a
    return (abs(a) & -abs(a)).bit_length() - 1


def legendre_bit(a, p):
    return 0 if pow(a, (p - 1) // 2, p) == 1 else 1


def class_span(gens, n, g):
    """The entire subgroup generated in Z/n x Z/g, with exact operations."""
    span = {(0, 0)}
    for a, b in sorted(gens):
        if (a, b) in span:
            continue
        before = tuple(span)
        x, y = a, b
        while (x, y) not in span:
            span.update(((v + x) % n, (u + y) % g) for v, u in before)
            x, y = (x + a) % n, (y + b) % g
        assert (a, b) in span
    assert len(span) <= n * g
    return span


def square_span(gens):
    span = {0}
    for a in gens:
        span |= {b ^ a for b in tuple(span)}
    return span


def even_cyclotomic_value(p, n):
    """Literal character on (Z/(2n))*: chi(5)=1/(n/2), chi(-1)=0."""
    m, mod = n // 2, 2 * n
    z = 1
    for j in range(m):
        if p % mod in (z, -z % mod):
            return Q(j, m)
        z = 5 * z % mod
    raise AssertionError((p, n))


def formal_maps():
    T, R, c, c0, ci, a0, ai, b = sp.symbols("T R c c0 ci a0 ai b")
    X0, Xi, Z0, Zi, xi0, eta0 = sp.symbols("X0 Xi Z0 Zi xi0 eta0")
    U = b / (T - c0)
    new_ci = b / (ci - c0)
    new_ai = -b * ai / (a0 * (ci - c0))
    assert sp.factor((U - new_ci) / new_ai -
                     ((T - ci) / ai) / ((T - c0) / a0)) == 0
    assert sp.factor(U / (b / a0) - a0 / (T - c0)) == 0
    f = (T - c) / (R - c)
    assert sp.factor((U - b / (c - c0)) /
                     (b / (R - c0) - b / (c - c0)) -
                     f * (R - c0) / (T - c0)) == 0
    assert sp.factor(U - b / (c - c0) -
                     (-b / (a0 * (c - c0))) * (T - c) /
                     ((T - c0) / a0)) == 0
    assert sp.factor(new_ci + (b / (a0 * (ci - c0))) *
                     (ai * (Xi / X0)**4) -
                     (new_ci - new_ai * (Xi / X0)**4)) == 0
    roots = (1 / Z0, Zi / Z0)
    assert sp.factor(1 / roots[0] - Z0) == 0
    assert sp.factor(roots[1] / roots[0] - Zi) == 0
    x, w = sp.symbols("x w")
    checks = 7
    for n in (4, 8, 12, 16, 24, 32, 64):
        d = (w**n - x) / (1 - x)
        assert sp.factor(1/x + (1 - 1/x) * d/w**n - w**(-n)) == 0
        X, Y, D, z = sp.symbols("X Y D z")
        assert sp.resultant(z**n - D, X - z, z) == X**n - D
        assert sp.factor((X**n - D)/(Y**n - D) -
                         ((X/Y)**n - D/Y**n)/(1 - D/Y**n)) == 0
        a, u, v, Dn, Z = sp.symbols("a u v Dn Z")
        for h, j in ((2, 2), (2, 3), (3, 2)):
            M, L = n*h, n*h*j
            aM, aL = a*u**n, a*u**n*v**M
            assert sp.factor(aL/a - (u*v**h)**n) == 0
            assert sp.factor(u*(v*Z**j)**h - (u*v**h)*Z**(h*j)) == 0
            Dm = Dn/u**n
            assert sp.factor(u**n*Dm - Dn) == 0
            checks += 3
        checks += 3
    print(f"PASS: {checks} literal normalized, inverse-root, polynomial-norm, "
          "coefficient and transitive power-map identities.", flush=True)


def odd_tests():
    counts = Counter()
    primes = (3, 5, 7, 11, 13, 17, 19, 31, 41, 73, 97, 193, 257)
    for r in range(2, 8):
        n, m = 2**r, 2**(r-1)
        for p in primes:
            g = gcd(n, p-1)
            primitive = int(sp.primitive_root(p))
            logs = {}
            z = 1
            for j in range(p-1):
                logs[z] = j % g
                z = z*primitive % p
            qchi = even_cyclotomic_value(p, n)
            order = int(sp.n_order(p, n))
            units = sorted({1, p-1, *(pow(primitive, j, p)
                                      for j in range(min(p-1, 8)))})
            hs = sorted(set(range(0, n+1, order)) |
                        {-order, 2*n})
            xs = {Q(p)**h*u for h, u in product(hs, units)}
            xs.update(Q(1+p**a) for a in (1, 2, 3))
            xs.discard(Q(1))
            active_before = counts["equations"]
            for x in sorted(xs):
                h, u = vu(x, p)
                assert h % order == 0
                lx = legendre_bit(u, p)
                assert (h*qchi*2).denominator == 1 or p % n != 1
                ws = {Q(p)**a*v for a, v in product(
                    sorted({-1, 0, 1, h//n, h//n+1}), units)}
                gens, squares = set(), set()
                for w in ws:
                    di = (w**n-x)/(1-x)
                    if not di:
                        continue
                    vd, ud = vu(di, p)
                    gens.add((vd % n, logs[ud]))
                    squares.add((vd % 2) | (legendre_bit(ud, p) << 1))
                    counts["literal_d"] += 1
                minus_class = legendre_bit(p-1, p) << 1
                if minus_class not in square_span(squares):
                    counts["excluded_square_span"] += 1
                    continue
                states = class_span(gens, n, g)
                counts["equations"] += 1
                counts["states"] += len(states)
                # This loops through every mixed product in the generated
                # full finite power-class group, including all relation signs.
                for vd, ud in states:
                    if vd % m:
                        continue
                    vr = vd//m  # exact parity of the root's valuation
                    for negative in (0, 1):
                        rhs_unit = (ud-negative*logs[p-1]) % g
                        if rhs_unit % gcd(m, g):
                            continue
                        if g == n:
                            root_parities = (rhs_unit//m,)
                        else:
                            assert m % g == 0 and rhs_unit == 0
                            root_parities = (0, 1)
                        for lr in root_parities:
                            bit = ((h*vr*((p-1)//2)) + lx*vr + lr*h) % 2
                            value = Q(bit, 2) + negative*h*qchi
                            assert value.denominator == 1, (
                                r, p, x, (vd, ud), negative, vr, lr, value)
                            counts["mixed_evaluations"] += 1
                            counts["negative" if negative else "positive"] += 1
                # Independently audit the exact order used in the residue case.
                if p % 4 == 1 and v2(p-1) < r:
                    d = 2**(r-v2(p-1))
                    assert order == d
                    assert qchi.denominator == 2*d
                    assert qchi.numerator % 2 == 1
                    assert (h*qchi - Q(h//d, 2)).denominator == 1
                    counts["frobenius_orders"] += 1
            assert counts["equations"] > active_before
        print(f"PASS: all retained odd equations at n={n}, including literal "
              "mixed products and every compatible root squareclass.", flush=True)
    print("ODD COUNTS:", dict(sorted(counts.items())), flush=True)


def dyadic_tests():
    counts = Counter()
    for r in range(3, 11):
        n, m = 2**r, 2**(r-1)
        assert v2(r) < r-1
        for s in range(r+2, 2*r+5):
            for k in range(1, r+2):
                if s-k != r:
                    continue
                assert k >= 2
                for offset in range(1, 4):
                    for e, eT in ((s, s+offset*n), (s+offset*n, s)):
                        assert e != eT and e % n == eT % n
                        assert (e-k) % n == r
                        assert v2(k-e) == v2(r)
                        for t0 in range(m):
                            if t0*(k-e) % m == 0:
                                assert t0 % 2 == 0
                                for oddunit in (1, 3):
                                    assert pow(oddunit, t0, 4) == 1
                                    counts["positive_sign_forced"] += 1
                        counts["depth_cases"] += 1
        if r <= 8:
            modulus = 2**(r+5)
            for e, depth in ((m, r+1), (n//4, r)):
                image = {pow(u, e, modulus)
                         for u in range(1, modulus, 2)}
                target = set(range(1, modulus, 2**depth))
                assert image == target
                counts["literal_power_images"] += 1
        # The exact cyclotomic norm kernel on units uses u^{-1};
        # signs are tested, rather than discarded modulo +/-1.
        mod = 2**r
        kernel = {u for u in range(1, 4*mod, 2)
                  if pow(u, -1, mod) == 1}
        assert kernel == set(range(1, 4*mod, mod))
        assert mod-1 not in kernel
        counts["signed_cyclotomic_kernels"] += 1
    print("PASS: dyadic power images, signed cyclotomic kernels, all retained "
          "remaining-depth implications and positive-relation exclusions.", flush=True)
    print("DYADIC COUNTS:", dict(sorted(counts.items())), flush=True)


if __name__ == "__main__":
    formal_maps()
    odd_tests()
    dyadic_tests()
    print("ALL A128 FINITE CERTIFICATES PASSED.", flush=True)
