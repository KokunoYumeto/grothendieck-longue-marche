#!/usr/bin/env python3
"""Exact local check of the harmonic c3=1/2 quartic candidate R=2."""
from fractions import Fraction as Q
from itertools import product
from math import gcd
from tripod_eighth_search import valuation_unit, hilbert


def fourth(x, p):
    if not x:
        return False
    v, u = valuation_unit(x, p, 16 if p == 2 else p)
    if v % 4:
        return False
    return u == 1 if p == 2 else pow(u, (p - 1) // gcd(4, p - 1), p) == 1


def main():
    print("Old curve: T=2X^4, T-1=Y^4, T-1/2=(3/2)Z^4.")
    print("New c=-1/48; normalized class ((48T+1)/97,70).")
    total = actual = 0
    found = []
    for p in (2, 3, 5, 7, 97):
        local = tested = 0
        units = [u for u in range(1, max(128, 2*p)) if u % p]
        for e, u in product(range(-4, 5), units):
            X = Q(p)**e * u
            T = 2*X**4
            y4, z4 = T-1, (2*T-1)/3
            total += 1
            tested += 1
            if not fourth(y4, p) or not fourth(z4, p):
                continue
            f = (48*T+1)/97
            if not f:
                continue
            actual += 1
            local += 1
            if hilbert(f, Q(70), p):
                found.append((p, X, T, y4, z4, f))
                break
        print(f"p={p}: trials={tested}, actual local root pairs={local}, variation={any(v[0]==p for v in found)}.")
    for row in found:
        print("WITNESS:", row)
    print(f"Total exact trials={total}; actual local points={actual}.")
    if not found:
        print("No variation in this finite search; no general nonexistence claim.")


if __name__ == "__main__":
    main()
