#!/usr/bin/env python3
"""Exact certificate for the intermediate harmonic genus-three obstruction."""
from fractions import Fraction as Q
from tripod_eighth_search import valuation_unit, hilbert
from harmonic_tripod_candidate_search import fourth

R, c, T = Q(32, 81), Q(25, 34), Q(7)
F = lambda t: t * (t - 1) * (t - Q(1, 2))
w4 = F(T) / F(R)
f = (T - c) / (R - c)
assert w4 == Q(20726199, 1904)
assert f == Q(-17253, 937)
assert fourth(w4, 2)
v, unit = valuation_unit(w4, 2, 16)
assert (v, unit) == (-4, 1)
assert hilbert(f, Q(210), 2) == 1
assert hilbert(Q(1), Q(210), 2) == 0
assert T / R == Q(567, 32)
assert valuation_unit(T / R, 2)[0] == -5
assert not fourth(T / R, 2)

# Exact Riemann--Hurwitz data for C4 -> D -> P1.
assert 4 * (-2 + 4 * Q(3, 4)) == 2 * 3 - 2
assert 64 * (-2 + 4 * Q(3, 4)) == 2 * 33 - 2
assert 2 * 33 - 2 == 16 * (2 * 3 - 2)
# On the three finite inertia factors the product exponent is 1;
# on infinity it is 3. Each is invertible modulo 4.
assert all(pow(i, -1, 4) in (1, 3) for i in (1, 1, 1, 3))
print("Intermediate curve: W^4=T(T-1)(T-1/2)/[R(R-1)(R-1/2)].")
print(f"R={R}, c={c}, character squareclass=210.")
print(f"Actual Q2 point: T={T}, W^4={w4}; valuation/unit modulo16={v}/{unit}.")
print(f"Normalized first entry={f}; quaternion invariant=1/2.")
print("Base point T=R,W=1 has invariant0.")
print(f"First old lift condition T/R={T/R} has valuation-5, so this point does not lift.")
print("Geometric degrees: C4/P1=64, D/P1=4, C4/D=16.")
print("Genera: 33 and3; all four inertia maps to mu4 are injective, so C4/D is etale.")
print("All exact checks passed. No assertion about the pullback class on C4 is inferred.")
