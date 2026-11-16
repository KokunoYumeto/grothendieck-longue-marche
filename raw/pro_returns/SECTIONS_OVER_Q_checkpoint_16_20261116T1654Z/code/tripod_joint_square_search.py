#!/usr/bin/env python3
"""Exact dyadic search for the joint character from D0=-r^2,D1=s^2.

Each accepted root target is an actual Q2 fourth power, not just a
chosen finite congruence. The output distinguishes both boundary-root
symbol requirements from the new joint-character evaluation.
"""
from fractions import Fraction as Q
from itertools import product
from picard_obstruction_certificate import hilbert_two


def v2_and_unit(a, modulus=32):
    if a == 0:
        return None
    n, d = a.numerator, a.denominator
    valuation = 0
    while n % 2 == 0:
        n //= 2
        valuation += 1
    while d % 2 == 0:
        d //= 2
        valuation -= 1
    return valuation, n*pow(d, -1, modulus) % modulus


def main():
    rs = sorted({Q(a, b) for a in range(1, 10) for b in range(1, 10)})
    ss = sorted({Q(a, b) for a in range(2, 17) for b in range(1, a)})
    xs = tuple(Q(2)**e * z for e in range(-4, 5) for z in range(1, 64, 2))
    trials = soluble = character_bad = root_ok = 0
    found = None
    for r, s in product(rs, ss):
        R = (s*s-1)/(s*s+r*r)
        c = -R*r*r
        assert 0 < R < 1 and (c-1)/(R-1) == s*s
        for X in xs:
            Y4 = (1-R*X**4)/(1-R)
            data = v2_and_unit(Y4)
            trials += 1
            if data is None:
                continue
            vy4, unit = data
            if vy4 % 4 or unit % 16 != 1:
                continue
            soluble += 1
            T = R*X**4
            f = (T-c)/(R-c)
            assert f == (X**4+r*r)/(1+r*r)
            if not hilbert_two(f, s):
                continue
            character_bad += 1
            if hilbert_two(X, 1/(1-R)):
                continue
            # The two fourth roots have exactly these two squareclasses.
            root_units = (1, 7) if unit % 32 == 1 else (3, 5)
            allowed = [a for a in root_units
                       if hilbert_two(Q(2)**(vy4//4)*a, 1/R) == 0]
            if not allowed:
                continue
            root_ok += 1
            found = (r, s, R, c, X, Y4, vy4//4, allowed[0], T, f)
            break
        if found is not None:
            break
    print(f"Exact dyadic trials: {trials}; actual fourth-power targets: {soluble}.")
    print(f"Nonzero joint-character values: {character_bad}; both root-symbol conditions: {root_ok}.")
    if found is None:
        print("No witness in this finite range; no general nonexistence assertion.")
    else:
        for label, value in zip(
                ("r", "s", "R", "c", "X", "Y^4", "v2(Y)", "unit_squareclass(Y)", "T", "f"),
                found):
            print(f"{label} = {value}")
        print("Actual local root exists by the exact Q2 fourth-power criterion.")


if __name__ == "__main__":
    main()
