#!/usr/bin/env python3
"""Exact rational-point search for a two-coordinate counterpart of A.90.

Each trial has two actual rational points on the same quartic cover.
We test the common fibre character from D0*D1=-r^2, and require
the separate boundary-root symbols to vanish at the selected prime.
A negative search result proves no general nonexistence assertion.
"""
from fractions import Fraction as Q
from itertools import product
from sympy import factorint
from picard_obstruction_certificate import hilbert_two


def primes_of(a):
    return set(map(int, factorint(abs(a.numerator)))) | set(map(int, factorint(a.denominator)))


def valuation_unit(a, p):
    numerator, denominator = a.numerator, a.denominator
    v = 0
    while numerator % p == 0:
        numerator //= p
        v += 1
    while denominator % p == 0:
        denominator //= p
        v -= 1
    return v, numerator * pow(denominator, -1, p) % p


def hilbert(a, b, p):
    if p == 2:
        return hilbert_two(a, b)
    va, ua = valuation_unit(a, p)
    vb, ub = valuation_unit(b, p)
    la = int(pow(ua, (p-1)//2, p) == p-1)
    lb = int(pow(ub, (p-1)//2, p) == p-1)
    return (va*vb*((p-1)//2) + la*vb + lb*va) % 2


def main():
    candidates = sorted({Q(a, b) for a in range(1, 8) for b in range(1, 8)})
    parameters = sorted({Q(a, b) for a in range(1, 12) for b in range(1, 12)})
    points = trials = ramified = 0
    first = None
    for X, Y in product(candidates, repeat=2):
        if X == Y or X == 1 or Y == 1:
            continue
        R = (1-Y**4)/(X**4-Y**4)
        if not 0 < R < 1:
            continue
        T = R*X**4
        assert T-1 == (R-1)*Y**4
        points += 1
        for tau in parameters:
            denominator = tau*tau + R*(R-1)
            if denominator == 0:
                continue
            c = tau*tau/denominator
            r = tau/denominator
            if c in (Q(0), Q(1), R, T):
                continue
            d = 2*r
            f = (T-c)/(R-c)
            D0, D1 = c/R, (c-1)/(R-1)
            assert D0*D1 == -r*r
            places = {2} | primes_of(f) | primes_of(d)
            bad = [p for p in sorted(places) if hilbert(f, d, p)]
            # Include the real invariant as an independent reciprocity check.
            assert (len(bad) + int(f < 0 and d < 0)) % 2 == 0
            trials += 1
            for p in bad:
                ramified += 1
                x_symbol = hilbert(X, 1/(1-R), p)
                y_symbol = hilbert(Y, 1/R, p)
                if x_symbol == 0 and y_symbol == 0:
                    first = (R, T, X, Y, tau, c, r, d, f, p)
                    break
            if first is not None:
                break
        if first is not None:
            break
    print(f"Rational second-point covers tested: {points}.")
    print(f"Exact common-character trials: {trials}; nonzero finite evaluations: {ramified}.")
    if first is None:
        print("No witness in this finite search; no general nonexistence claim.")
    else:
        labels = ("R", "T", "X", "Y", "tau", "c", "r", "d", "f", "bad_prime")
        for label, value in zip(labels, first):
            print(f"{label} = {value}")
        print("Found an exact two-coordinate witness with both old root symbols zero.")


if __name__ == "__main__":
    main()
