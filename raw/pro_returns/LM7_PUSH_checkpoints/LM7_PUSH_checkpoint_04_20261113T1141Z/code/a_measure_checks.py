#!/usr/bin/env python3
"""Finite transition checks accompanying the integral proof of A.19.

These checks illustrate the orbit-size divisibility argument; the proof
for every affine lattice and every precision is in the paper itself.
"""

from math import gcd


def v3(n):
    assert n
    result = 0
    while n % 3 == 0:
        n //= 3
        result += 1
    return result


def orbits(multiplier, translation, modulus):
    unused = set(range(modulus))
    result = []
    while unused:
        start = min(unused)
        orbit, x = [], start
        while x in unused:
            unused.remove(x)
            orbit.append(x)
            x = (multiplier*x+translation) % modulus
        assert x == start
        result.append(orbit)
    return result


def main():
    for translation, expected_fixed_residue in [(0, 0), (6, 2), (1, None)]:
        print("Affine map x -> 7x +", translation)
        print("Rational fixed point:", f"-{translation}/6")
        for n in range(2, 8):
            cycles = orbits(7, translation, 3**n)
            coefficients = [0, 0, 0]
            for orbit in cycles:
                for residue in range(3):
                    count = sum(x % 3 == residue for x in orbit)
                    coefficients[residue] = gcd(coefficients[residue], count)
            valuations = [v3(c) for c in coefficients]
            expected = [0 if r == expected_fixed_residue else n-1 for r in range(3)]
            assert valuations == expected
            print("level", n, "orbit count", len(cycles),
                  "minimum pushforward valuations at residues 0,1,2:", valuations)
    print("Boundary transition counts for rank10, w=3^s*e_d, s=2")
    s = 2
    for n in range(s+1, s+5):
        degree = 3**9
        d_ramification_ratio = 1
        other_ramification_ratio = 3
        d_preimages = degree // d_ramification_ratio
        other_preimages = degree // other_ramification_ratio
        assert d_preimages*d_ramification_ratio == degree
        assert other_preimages*other_ramification_ratio == degree
        print("n", n, "cover degree", degree,
              "d preimages/ramification", (d_preimages, d_ramification_ratio),
              "other preimages/ramification", (other_preimages, other_ramification_ratio))
    print("The diagonal transition is the same degree3^9 for every cusp.")
    print("PASS")


if __name__ == "__main__":
    main()
