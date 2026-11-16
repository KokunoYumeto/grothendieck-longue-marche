#!/usr/bin/env python3
"""Exact finite arithmetic checks for A.67 over Q_5.

The Tate parameter is certified only modulo the displayed prime power.
Its existence and the full integral Tate/pro-2 comparisons are proved in
the accompanying text; no finite computation substitutes for those maps.
"""

from fractions import Fraction
from math import comb, gcd


def multiply(left, right, degree):
    answer = [0] * (degree + 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            if i + j <= degree:
                answer[i + j] += x * y
    return answer


def inverse_unit(series, degree):
    assert series[0] == 1
    answer = [1] + [0] * degree
    for n in range(1, degree + 1):
        answer[n] = -sum(series[k] * answer[n - k] for k in range(1, n + 1))
    return answer


def evaluate(series, value, modulus):
    answer = 0
    for coefficient in reversed(series):
        answer = (answer * value + coefficient) % modulus
    return answer


def valuation(value, p):
    if value == 0:
        return float("inf")
    count = 0
    while value % p == 0:
        value //= p
        count += 1
    return count


precision = 14
degree = precision // 2 + 1
E4 = [1] + [240 * sum(d**3 for d in range(1, n + 1) if n % d == 0)
             for n in range(1, degree + 1)]
delta_over_q = [1] + [0] * degree
for m in range(1, degree + 1):
    factor = [0] * (degree + 1)
    for k in range(min(24, degree // m) + 1):
        factor[k * m] = (-1)**k * comb(24, k)
    delta_over_q = multiply(delta_over_q, factor, degree)
Phi = multiply(multiply(multiply(E4, E4, degree), E4, degree),
               inverse_unit(delta_over_q, degree), degree)
assert Phi[:5] == [1, 744, 196884, 21493760, 864299970]

lam = 5
c4 = 16 * (lam * lam - lam + 1)
c6 = 32 * (lam + 1) * (lam - 2) * (2 * lam - 1)
discriminant = 16 * lam * lam * (1 - lam)**2
j = Fraction(c4**3, discriminant)
assert (c4, c6, discriminant, j) == (336, 5184, 6400, Fraction(148176, 25))
assert c6 == 72**2
assert valuation(discriminant, 5) == 2 and valuation(c4, 5) == 0

modulus = 5**precision
q = 0
for _ in range(precision + 2):
    q = 25 * evaluate(Phi, q, modulus) * pow(148176, -1, modulus) % modulus
assert (148176 * q - 25 * evaluate(Phi, q, modulus)) % modulus == 0
assert valuation(q, 5) == 2

unit_modulus = 5**(precision - 2)
F = 256 * (q // 25) % unit_modulus
assert F % 5 == 1
root = 1
for _ in range(precision):
    root = (root + F * pow(root, -1, unit_modulus)) * pow(2, -1, unit_modulus) % unit_modulus
assert root % 5 == 1 and (root * root - F) % unit_modulus == 0
C = 5 * root
assert (C * C - 256 * q) % modulus == 0
assert F % 25 == 6 and root % 25 == 16
assert valuation(C - 5, 5) == 2

fifth_power_units = {pow(u, 5, 25) for u in range(1, 25) if gcd(u, 25) == 1}
assert fifth_power_units == {1, 7, 18, 24}
assert (-4) % 25 not in fifth_power_units
assert pow(1, 5, 25) == 1

print(f"E_5 invariants: c4={c4}, c6={c6}=72^2, Delta={discriminant}, j={j}.")
print(f"The series q*J(q) begins {Phi[:5]}.")
print(f"Tate parameter q modulo 5^{precision}: {q}.")
print(f"The exact equation 148176*q=25*(q*J(q)) holds modulo 5^{precision}.")
print(f"F=256*q/25 modulo 5^{precision-2}: {F}; F=6 modulo25.")
print(f"C/5=sqrt(F) modulo 5^{precision-2}: {root}; C/5=16 modulo25.")
print(f"C^2=256*q modulo 5^{precision}, and v5(C-5)=2 at this precision.")
print(f"Fifth powers of units modulo25: {sorted(fifth_power_units)}; -4=21 is excluded.")
print("The cusp sheet z=1 is rational. All finite arithmetic certificates passed.")
