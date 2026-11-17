#!/usr/bin/env python3
"""Exact finite checks of ingredients of the reconstructed A.72 proof.

The program checks the cyclic subgroup inclusions and their fixed-field
indices, the genus estimate, the component exponents, and actual local
Hensel roots at all small coefficient-prime types. It does not assert
that these finite checks replace the Chebotarev existence proof.
"""
from math import gcd, lcm, factorial
from sympy import divisors, expand, symbols


def valuation(n, p):
    if n == 0:
        raise ValueError("valuation of zero not used")
    result = 0
    while n % p == 0:
        result += 1
        n //= p
    return result


count = 0
for degree in range(1, 65):
    for multiplier in range(1, 10):
        n = lcm(24, 4 * degree) * multiplier
        order = n // 2
        for index in divisors(gcd(degree, order)):
            # H=Z/order; H_F=index*H.  Exact containment of cyclic
            # subgroups reduces to divisibility of their generators.
            generator_MH = gcd(degree, order)
            generator_HF = gcd(index, order)
            assert generator_MH % generator_HF == 0
            generator_2MH = gcd(2 * degree, order)
            generator_2HF = gcd(2 * index, order)
            assert generator_2MH % generator_2HF == 0
            assert generator_2MH == 2 * degree
            # Fixed field of 2M H has degree exactly 2M over Q(mu_n).
            assert order // (order // generator_2MH) == 2 * degree
            count += 1
print(f"Cyclic intersection calculation: {count} degree/index cases passed")

D, s = symbols("D s", positive=True)
lower_bound = s ** 2 + 1 - (D + 2) * s - 3 * D
assert expand(lower_bound.subs(s, 4 * D + 10)) == 12 * D ** 2 + 59 * D + 81
assert expand((2 * s - (D + 2)).subs(s, 4 * D + 10)) == 7 * D + 18
print("Exact Hasse--Weil lower bound and its increasing range passed")

component_cases = 0
for N0 in (24, 48, 72, 120, 168, 264):
    for j in range(7):
        n, m = N0 * factorial(j + 4), N0 * factorial(j + 5)
        for e in divisors(N0):
            assert (n // e) * (m // n) == m // e
            assert m % n == 0 and n % e == 0
            component_cases += 1
print(f"Literal common-coordinate transition: {component_cases} cases passed")

N0 = 24
n, m, nnext = N0 * factorial(4), N0 * factorial(5), N0 * factorial(6)
for p in (2, 3, 5, 7, 11, 13):
    a, b = 3, -2
    V = max(valuation(a, p), valuation(b, p))
    L = V + 2 * valuation(nnext, p) + 4
    precision = L + 12
    modulus = p ** precision
    Q, R = 1 + p ** L, 1 + 2 * p ** L
    coefficient = b * pow(R, n, modulus)
    constant = (1 - a * pow(Q, n, modulus)) % modulus
    derivative_order = valuation(b, p) + valuation(m, p)
    assert L > 2 * derivative_order
    root = 1
    for iteration in range(20):
        error = (coefficient * pow(root, m, modulus) - constant) % modulus
        if error == 0:
            break
        derivative = coefficient * m * pow(root, m - 1, modulus)
        assert valuation(derivative, p) == derivative_order
        assert error % (p ** derivative_order) == 0
        smaller = p ** (precision - derivative_order)
        correction = ((error // (p ** derivative_order))
                      * pow((derivative // (p ** derivative_order)) % smaller,
                            -1, smaller)) % smaller
        root = (root - correction) % modulus
    else:
        raise AssertionError("Hensel iteration did not terminate")
    assert (coefficient * pow(root, m, modulus) - constant) % modulus == 0
    claimed = L - valuation(b, p) - valuation(m, p)
    assert (root - 1) % (p ** claimed) == 0
    assert claimed >= valuation(nnext, p)
    assert (a * pow(Q, n, modulus)
            + b * pow(R, n, modulus) * pow(root, m, modulus) - 1) % modulus == 0
    print(f"Actual local root: p={p}, n={n}, m={m}, L={L}, "
          f"precision={precision}, guaranteed v_p(Z-1)>={claimed}, "
          f"Newton steps={iteration}")

print("PASS. Chebotarev and the geometric specialization are proved in the text.")
