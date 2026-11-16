#!/usr/bin/env python3
"""Exact local search in the joint negative-fourth-power family.

D0=-s^4/p and D1=p, so their joint eighth-root fibre contains
Q(zeta_16*sqrt(s)).  Its even quartic character is chi_16+chi_s.
The literal curve and local eighth-power tests are retained.
"""
from fractions import Fraction as Q
from itertools import product
from tripod_eighth_search import eighth_power, valuation_unit, cyclo_e, hilbert


def main():
    parameters = sorted({sign * Q(2) ** e * u for sign, e, u in product((-1, 1), range(-2, 3), range(1, 32, 2))})
    ss = sorted({Q(2) ** e * u for e, u in product(range(-2, 3), range(1, 16, 2))})
    xs = sorted({Q(2) ** e * u for e, u in product(range(-2, 3), range(1, 24, 2))})
    covers = trials = actual = 0
    for p, s in product(parameters, ss):
        if p in (0, 1) or p == -(s**4):
            continue
        R = p * (p - 1) / (p**2 + s**4)
        c = -(s**4) * (p - 1) / (p**2 + s**4)
        assert R not in (0, 1) and c not in (0, 1, R)
        assert (c / R) * ((c - 1) / (R - 1)) == -(s**4)
        covers += 1
        for X in xs:
            target = (R * X**8 - 1) / (R - 1)
            trials += 1
            if not eighth_power(target, 2):
                continue
            f = (R * X**8 - c) / (R - c)
            if not f:
                continue
            actual += 1
            _, unit = valuation_unit(f, 2, 16)
            inv4 = (-cyclo_e(unit) + 2 * hilbert(f, s, 2)) % 4
            if inv4:
                print("FOUND an exact nonzero joint quartic evaluation.")
                for key, val in [("p", p), ("s", s), ("R", R), ("c", c), ("X", X), ("Y^8", target), ("normalized f", f), ("4*invariant", inv4)]:
                    print(f"{key}: {val}")
                print(f"covers={covers}, trials={trials}, actualpoints={actual}.")
                return
    print(f"Negative-fourth-power product covers: {covers}.")
    print(f"Exact dyadic trials: {trials}; actual eighth-power points: {actual}.")
    print("No nonzero evaluation in this finite range; no general constancy claim.")


if __name__ == "__main__":
    main()
