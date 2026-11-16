#!/usr/bin/env python3
"""Exact exploratory search for a higher-exponent two-coordinate obstruction.

The common characters are computed from the literal A.57 finite stabilizers.
Actual local points are certified by the local eighth-power criterion.
A failed finite search is not a constancy theorem.
"""
from fractions import Fraction as Q
from itertools import product
from math import gcd
from sympy import factorint
from picard_obstruction_certificate import hilbert_two


def add(x, y):
    return ((x[0] + y[0]) % 4,) + tuple(a ^ b for a, b in zip(x[1:], y[1:]))


def generated(gs, rank):
    out = {(0,) * rank}
    for g in gs:
        frontier = list(out)
        for x in frontier:
            for j in range(1, 4):
                xx = x
                for _ in range(j):
                    xx = add(xx, g)
                out.add(xx)
    return out


def pair(ch, g):
    return (ch[0] * g[0] + 2 * sum(x * y for x, y in zip(ch[1:], g[1:]))) % 4


def common_characters(primes, rows):
    odd = [p for p in primes if p != 2]
    rank = 2 + len(odd)
    gamma = list(product(range(4), *([range(2)] * (rank - 1))))
    images = set()
    for g in gamma:
        e, sign = g[:2]
        u = ((-1) ** sign * pow(5, e, 16)) % 16
        eps = [e % 2 if p == 2 else g[2 + odd.index(p)] for p in primes]
        for h in product(range(4), repeat=len(primes)):
            ks = [ee + 2 * hh for ee, hh in zip(eps, h)]
            if all(
                any(
                    ((u - 1) * (delta + 2 * root) + 2 * sum(w * k for w, k in zip(ws, ks))) % 16 == 0
                    for root in range(8)
                )
                for delta, ws in rows
            ):
                images.add(g)
                break
    hgroup = generated(images, rank)
    return {ch for ch in gamma if all(pair(ch, g) == 0 for g in hgroup)}


def valuation_unit(x, p, modulus=None):
    if modulus is None:
        modulus = p
    a, b = x.numerator, x.denominator
    val = 0
    while a % p == 0:
        a //= p
        val += 1
    while b % p == 0:
        b //= p
        val -= 1
    return val, a * pow(b, -1, modulus) % modulus


def eighth_power(x, p):
    if not x:
        return False
    v, unit = valuation_unit(x, p, 32 if p == 2 else p)
    if v % 8:
        return False
    if p == 2:
        return unit == 1
    return pow(unit, (p - 1) // gcd(8, p - 1), p) == 1


def hilbert(a, b, p):
    if p == 2:
        return hilbert_two(a, b)
    va, ua = valuation_unit(a, p)
    vb, ub = valuation_unit(b, p)
    la = int(pow(ua, (p - 1) // 2, p) == p - 1)
    lb = int(pow(ub, (p - 1) // 2, p) == p - 1)
    return (va * vb * ((p - 1) // 2) + la * vb + lb * va) % 2


def cyclo_e(unit):
    for sign, e in product(range(2), range(4)):
        if (-1) ** sign * pow(5, e, 16) % 16 == unit % 16:
            return e
    raise AssertionError(unit)


def value(ch, f, primes, p):
    # Invariants are represented in (1/4)Z/Z.
    if p == 2:
        _, unit = valuation_unit(f, 2, 16)
        result = -ch[0] * cyclo_e(unit)
    else:
        v, _ = valuation_unit(f, p)
        result = ch[0] * v * cyclo_e(p)
    d = Q(-1) ** ch[1]
    for pp, coeff in zip([pp for pp in primes if pp != 2], ch[2:]):
        d *= Q(pp) ** coeff
    return (result + 2 * hilbert(f, d, p)) % 4


def prime_support(x):
    return set(map(int, factorint(abs(x.numerator)))) | set(map(int, factorint(x.denominator)))


def main():
    covers = newchars = trials = localpoints = nonzero = 0
    for pp in (2, 3, 5, 7, 11):
        primes = (pp,)
        for aa, bb in product(range(-3, 8), range(-3, 8)):
            d0, d1 = -Q(pp) ** aa, Q(pp) ** bb
            if d1 == 1:
                continue
            R = (1 - d1) / (d0 - d1)
            if not 0 < R < 1:
                continue
            c = R * d0
            rows = [(1, (aa,)), (0, (bb,))]
            joint = common_characters(primes, rows)
            normchars = generated(
                common_characters(primes, rows[:1])
                | common_characters(primes, rows[1:])
                | common_characters(primes, [(1, (aa - bb,))]),
                2 + int(pp != 2),
            )
            assert normchars <= joint
            extra = joint - normchars
            if not extra:
                continue
            covers += 1
            newchars += len(extra)
            places = {2, pp}
            for z in (R, R - 1, c, c - 1, R - c):
                places |= prime_support(z)
            for p in sorted(places):
                zs = range(1, 64, 2) if p == 2 else [z for z in range(1, min(p, 48)) if z % p]
                for exponent, unit in product(range(-2, 3), zs):
                    X = Q(p) ** exponent * unit
                    Xn = X**8
                    target = (R * Xn - 1) / (R - 1)
                    trials += 1
                    if not eighth_power(target, p):
                        continue
                    f = (Xn - d0) / (1 - d0)
                    if not f:
                        continue
                    localpoints += 1
                    for ch in extra:
                        ev = value(ch, f, primes, p)
                        if ev:
                            nonzero += 1
                            print("FOUND an exact nonconstant local evaluation.")
                            for key, val in [
                                ("prime parameter", pp), ("D0", d0), ("D1", d1),
                                ("R", R), ("c", c), ("physical prime", p),
                                ("X", X), ("Y^8", target), ("normalized f", f),
                                ("character tuple", ch), ("4*invariant", ev),
                            ]:
                                print(f"{key}: {val}")
                            print(f"covers={covers}, newchars={newchars}, trials={trials}, actualpoints={localpoints}.")
                            return
    print(f"Covers with characters outside the three exact norm fields: {covers}.")
    print(f"Remaining character trials: {newchars}; local trials: {trials}; actual local points: {localpoints}.")
    print(f"Nonzero evaluations: {nonzero}.")
    print("No witness in this finite range; no general constancy claim.")


if __name__ == "__main__":
    main()
