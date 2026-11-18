#!/usr/bin/env python3
"""Small exact checks accompanying the source-scope audit.

These checks do not prove an infinite Galois lifting theorem.  The text proves
those statements and the all-level tangential Kummer calculation separately.
"""

from fractions import Fraction
from itertools import product


def valuation(value, prime):
    value = Fraction(value)
    numerator, denominator = abs(value.numerator), value.denominator
    exponent = 0
    while numerator and numerator % prime == 0:
        numerator //= prime
        exponent += 1
    while denominator % prime == 0:
        denominator //= prime
        exponent -= 1
    return exponent


def cusp_valuation_pattern(a, b):
    return b == 0 or a == 0 or a == b


def main():
    # Q(zeta_3) has prime-to-3 roots of unity +/-1.
    sums = sorted({3 * s + 3 * t for s, t in product((-1, 1), repeat=2)})
    assert sums == [-6, 0, 6] and 1 not in sums
    print("HT2021 omitted-infinity example: F=Q(zeta_3), pair=(3,3)")
    print("Prime-to-3 root-of-unity sums:", sums, "; none equals 1")
    tangent = Fraction(1, 3)
    pair = (1 / tangent, -1 / tangent)
    assert pair == (3, -3)
    assert pair[1] / pair[0] == -1
    assert all((-1) ** (3 ** n) == -1 for n in range(1, 10))
    print("Infinity tangent 1/3 has leading-coefficient pair:", tuple(map(str, pair)))
    print("The ratio -1 is its own 3^n-th root (n=1,...,9 checked).")

    for prime in (2, 3, 5, 7):
        a, b = prime, prime ** 2
        vals = valuation(a, prime), valuation(b, prime)
        assert vals == (1, 2)
        assert not cusp_valuation_pattern(*vals)
        assert valuation(1 - a, prime) == 0
        print(f"pair=({a},{b}), coefficient prime={prime}: valuations={vals}; "
              "ordinary and all cusp valuation patterns excluded")

    # Exact square classes relevant to the proof that Q is 2-rational.
    odd_square_residues = {r * r % 8 for r in (1, 3, 5, 7)}
    assert odd_square_residues == {1}
    print("Odd 2-adic units that are squares have residue 1 modulo 8.")
    print("Among rational classes {1,-1,2,-2}, only 1 can be a Q_2 square.")
    print("All finite checks passed; infinite existence assertions are proved in P.3--P.4.")


if __name__ == "__main__":
    main()
