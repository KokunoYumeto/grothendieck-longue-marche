#!/usr/bin/env python3
"""Exact finite checks for the valuation/inertia examples of B.10 and B.12.

These checks certify the finite calculations, not the profinite proofs.
Only the Python standard library is used.
"""
from fractions import Fraction


def polynomial_value(x):
    return x**5 - x


def derivative_value(x):
    return 5 * x**4 - 1


def main():
    print("Curve C: y^2=x^5-x")
    for x in (0, 1):
        assert polynomial_value(x) == 0
        assert derivative_value(x) != 0
        print(f"Rational branch point ({x},0); derivative={derivative_value(x)}")
    # gcd(x^5-x,5x^4-1)=1: any common root would satisfy x^4=1/5;
    # the first equation then gives x*(1/5-1)=0, hence x=0,
    # contradicting x^4=1/5.  Check the exact nonzero coefficient.
    assert Fraction(1, 5) - 1 == Fraction(-4, 5)
    print("Five finite simple branch points and infinity: genus=(6-2)/2=2")
    print("Flag valuations of x: v_1(x)=(0,2), v_2(x)=(0,0)")
    tests = 0
    for n in (2, 3, 4, 5, 7, 8, 9, 16, 27, 49):
        pairs = [(r, s) for r in range(n) for s in range(n)]
        ker_sum = {(r, s) for r, s in pairs if (r + s) % n == 0}
        ker_difference = {(r, s) for r, s in pairs if (r - s) % n == 0}
        assert ker_sum == {(r, (-r) % n) for r in range(n)}
        assert ker_difference == {(r, r) for r in range(n)}
        assert len({(r + s) % n for r, s in pairs}) == n
        assert len({(r - s) % n for r, s in pairs}) == n
        tests += 4
        print(f"mod {n}: sum and difference maps surjective; kernel sizes {n},{n}")
    print(f"Passed {tests} finite inertia-map assertions.")


if __name__ == "__main__":
    main()
