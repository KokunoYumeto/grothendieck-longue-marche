#!/usr/bin/env python3
"""Exact arithmetic input for the weight-12, coefficient-691 example.

This certificate checks Bernoulli arithmetic and the Teichmuller character
test.  It does not computationally certify the quoted K-theory comparison
or global/local duality; their exact source statements are recorded in
ghost_h2_counterexample.tex.
"""
from fractions import Fraction
from math import comb, isqrt

B = [Fraction(1)]
for m in range(1, 13):
    B.append(-sum(Fraction(comb(m + 1, k)) * B[k] for k in range(m)) / (m + 1))
assert B[12] == Fraction(-691, 2730)
ell = 691
assert all(ell % d for d in range(2, isqrt(ell) + 1))
assert 690 % 11 != 0
assert pow(2, 11, ell) != 1
assert pow(ell - 1, -11, ell) == ell - 1
assert (pow(ell - 1, -11, ell) - 1) % ell != 0
print("B_12 =", B[12])
print("691 is prime; numerator(B_12) has 691-adic valuation exactly 1.")
print("690 does not divide 11.")
print("The order-two Teichmuller element -1 acts on twist -11 by -1.")
print("Its action minus identity is -2, a 691-adic unit.")
print("Therefore all invariants of (Q_691/Z_691)(-11) are zero.")
print("PASS: exact arithmetic only; K-theory and duality are cited separately.")
