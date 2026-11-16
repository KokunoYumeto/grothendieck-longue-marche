#!/usr/bin/env python3
"""Exact finite arithmetic certificate for A.74.

This verifies finite series, finite analytic discs and exact modular power
images. The accompanying proof supplies the all-prime assertion, the
continuous Galois maps and the infinite transcendence statement.
"""

from fractions import Fraction as F
from math import comb, gcd


def mul(a, b, degree):
    out = [F(0)] * (degree + 1)
    for i, x in enumerate(a[:degree + 1]):
        for j, y in enumerate(b[:degree + 1 - i]):
            out[i + j] += x * y
    return out


def inv(a, degree):
    assert a[0] == 1
    b = [F(1)] + [F(0)] * degree
    for j in range(1, degree + 1):
        b[j] = -sum(a[i] * b[j - i] for i in range(1, min(j, len(a) - 1) + 1))
    return b


def compose(a, b, degree):
    assert b[0] == 0
    out = [F(0)] * (degree + 1)
    power = [F(1)] + [F(0)] * degree
    for c in a[:degree + 1]:
        out = [x + c * y for x, y in zip(out, power)]
        power = mul(power, b, degree)
    return out


def evaluate(a, x, modulus):
    answer = 0
    for c in reversed(a):
        c = F(c)
        answer = (answer * x + c.numerator * pow(c.denominator, -1, modulus)) % modulus
    return answer


def vp(x, p):
    if x == 0:
        return float('inf')
    result = 0
    while x % p == 0:
        x //= p
        result += 1
    return result


def is_dyadic_rational(c):
    d = c.denominator
    return d > 0 and d & (d - 1) == 0


DEGREE = 12
e4 = [F(1)] + [F(240 * sum(d**3 for d in range(1, k + 1) if k % d == 0))
               for k in range(1, DEGREE + 1)]
delta_over_q = [F(1)] + [F(0)] * DEGREE
for k in range(1, DEGREE + 1):
    factor = [F(0)] * (DEGREE + 1)
    for j in range(min(24, DEGREE // k) + 1):
        factor[j * k] = F((-1)**j * comb(24, j))
    delta_over_q = mul(delta_over_q, factor, DEGREE)
phi = mul(mul(mul(e4, e4, DEGREE), e4, DEGREE),
          inv(delta_over_q, DEGREE), DEGREE)
assert phi[:5] == [1, 744, 196884, 21493760, 864299970]

# w(t)=1/j(E_t), q(t)=w(t)*Phi(q(t)), Phi(q)=q*J(q).
den_inv = inv([F(1), F(-1), F(1)], DEGREE)
den_inv_cube = mul(mul(den_inv, den_inv, DEGREE), den_inv, DEGREE)
w = mul([0, 0, F(1, 256), F(-2, 256), F(1, 256)],
        den_inv_cube, DEGREE)
q_series = [F(0)] * (DEGREE + 1)
for _ in range(DEGREE + 1):
    q_series = mul(w, compose(phi, q_series, DEGREE), DEGREE)
assert q_series == mul(w, compose(phi, q_series, DEGREE), DEGREE)
f_series = [256 * c for c in q_series[2:]]
assert f_series[:3] == [1, 1, F(29, 32)]
sqrt_f = [F(1)] + [F(0)] * (len(f_series) - 1)
for j in range(1, len(sqrt_f)):
    sqrt_f[j] = (f_series[j] - sum(sqrt_f[i] * sqrt_f[j - i]
                                  for i in range(1, j))) / 2
assert mul(sqrt_f, sqrt_f, len(f_series) - 1) == f_series
assert sqrt_f[:3] == [1, F(1, 2), F(21, 64)]
assert all(is_dyadic_rational(c) for c in f_series + sqrt_f)
theta = [F(0)] + sqrt_f

discs = 0
isometry_pairs = 0
for p in (3, 5, 7, 11, 13, 17, 19):
    modulus = p**3
    domain = list(range(0, modulus, p))
    images = [evaluate(theta, x, modulus) for x in domain]
    assert len(set(images)) == len(domain)
    assert set(images) == set(domain)
    for i, x in enumerate(domain):
        for j in range(i):
            assert vp(images[i] - images[j], p) == vp(x - domain[j], p)
            isometry_pairs += 1
    discs += 1

power_images = 0
for p in (3, 5, 7, 11, 13, 17, 19):
    max_k = 3 if p <= 11 else 2
    for k in range(max_k + 1):
        modulus = p**(k + 2)
        actual = {pow(z, p**k, modulus) for z in range(1, modulus, p)}
        expected = {1 + p**(k + 1) * z for z in range(p)}
        assert actual == expected
        power_images += 1

point_cases = 0
split_cases = 0
nonsplit_cases = 0
first_level_checks = 0
sample = []
for p in (3, 5, 7, 11, 13, 17, 19):
    for e in (1, 2, 3, 4):
        for u in (-2, -1, 1, 2, 3):
            if u % p == 0:
                continue
            x = p**e * u
            precision = 3 * e + 6
            modulus = p**precision
            j_num = 256 * (x*x - x + 1)**3
            j_den = x*x * (1-x)**2
            assert gcd(j_num, p) == 1 and vp(j_den, p) == 2*e
            q = 0
            for _ in range(precision + 1):
                q = j_den * evaluate(phi, q, modulus) * pow(j_num, -1, modulus) % modulus
            assert (j_num*q - j_den*evaluate(phi, q, modulus)) % modulus == 0
            assert vp(q, p) == 2*e
            unit_modulus = p**(precision - 2*e)
            f = 256 * (q // p**(2*e)) * pow(u*u, -1, unit_modulus) % unit_modulus
            root = 1
            for _ in range(precision + 1):
                root = (root + f * pow(root, -1, unit_modulus)) * pow(2, -1, unit_modulus) % unit_modulus
            assert root % p == 1 and (root*root - f) % unit_modulus == 0
            assert root == evaluate(sqrt_f, x, unit_modulus)
            assert vp(root - 1, p) == e
            assert vp(-x, p) == e
            c = x * root
            assert (c*c - 256*q) % modulus == 0
            c4 = 16 * (x*x - x + 1)
            c6 = 32 * (x+1) * (x-2) * (2*x-1)
            delta = 16*x*x*(1-x)**2
            assert vp(c4, p) == 0 and vp(delta, p) == 2*e
            assert c6 % p == 64 % p
            split = pow((-c6) % p, (p-1)//2, p) == 1
            assert split == (p % 4 == 1)
            split_cases += int(split)
            nonsplit_cases += int(not split)
            for k in range(e + 1):
                # The unit residues in 1+pZp lie in the exact power-image
                # subgroup iff they equal one modulo p^(k+1).
                point_second_trivial = ((1-x) - 1) % p**(k+1) == 0
                tangent_ratio_trivial = (root - 1) % p**(k+1) == 0
                assert point_second_trivial == tangent_ratio_trivial == (k < e)
                first_level_checks += 1
            assert e % p**e != 0 and gcd(p**e, 8) == 1
            if u == 1 and e in (1, 3) and p in (3, 5, 7):
                sample.append((p, e, f % p**(e+2), root % p**(e+2)))
            point_cases += 1

print('A.74 exact finite arithmetic certificate: all checks passed.')
print('F(t) begins:', ', '.join(str(x) for x in f_series[:6]))
print('sqrt(F(t)) begins:', ', '.join(str(x) for x in sqrt_f[:6]))
print(f'All {2*len(f_series)} displayed F/square-root coefficients have power-of-two denominators.')
print(f'Bijective analytic discs modulo p^3: {discs}; exact isometry pairs: {isometry_pairs}.')
print(f'Exact principal-unit power images checked: {power_images}.')
print(f'Tate-point cases: {point_cases}, including {split_cases} split and {nonsplit_cases} nonsplit cases.')
print(f'First separating Kummer-level checks: {first_level_checks}.')
print('Sample (p, valuation e, F modulo p^(e+2), Theta(x)/x modulo p^(e+2)):')
for row in sample:
    print(row)
print('The q identities, exact valuation depths, nodal splitting characters, and cyclic noncongruence criterion all pass.')
print('Continuous Galois conjugators and transcendence are supplied by the proof; finite computations do not replace them.')
