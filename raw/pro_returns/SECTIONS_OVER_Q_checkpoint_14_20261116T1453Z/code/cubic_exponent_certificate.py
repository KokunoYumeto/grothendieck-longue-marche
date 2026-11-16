#!/usr/bin/env python3
"""Finite exact certificates for A.62's class-four-useful prime recursion.

No full large-prime recursion is run. CRT integers test the congruence
mechanism; the proof uses Chebotarev to choose primes in these classes.
All local-image calculations below use literal modular integer powers.
"""
from fractions import Fraction
from itertools import product
from math import factorial, gcd, prod


def is_prime(value):
    return value >= 2 and all(value % d for d in range(2, int(value**0.5) + 1))


def primes_through(bound):
    return [p for p in range(2, bound + 1) if is_prime(p)]


def valuation(value, p):
    if value == 0:
        return float("inf")
    value = abs(value)
    answer = 0
    while value % p == 0:
        answer += 1
        value //= p
    return answer


def factors(value):
    answer = set()
    d = 2
    while d * d <= value:
        if value % d == 0:
            answer.add(d)
            while value % d == 0:
                value //= d
        d += 1
    if value > 1:
        answer.add(value)
    return answer


def primitive_root(p):
    divisors = factors(p - 1)
    return next(u for u in range(1, p)
                if all(pow(u, (p - 1) // ell, p) != 1 for ell in divisors))


def crt(residues, moduli):
    modulus = prod(moduli)
    result = sum(a * (modulus // m) * pow(modulus // m, -1, m)
                 for a, m in zip(residues, moduli)) % modulus
    return result, modulus


def triangular_checks():
    valuations = 0
    images = 0
    fresh = 0
    prime_list = primes_through(53)
    for C in (24, 48, 120, 264):
        J = max(6, max(factors(C)))
        for j in range(4):
            n = factorial(J + j)
            following = factorial(J + j + 1)
            D = 6 * C * n**3
            residues, moduli = [], []
            for p in prime_list:
                s = valuation(n, p)
                L = 1
                while p**L <= 53:
                    L += 1
                if s:
                    L = max(L, s + 1)
                    residue = 1 + p**s
                else:
                    residue = primitive_root(p)
                    assert pow(residue, 2, p) != 1 and pow(residue, 3, p) != 1
                residues.append(residue)
                moduli.append(p**L)
            Q, modulus = crt(residues, moduli)
            if Q <= 1:
                Q += modulus
            E = C * n * (Q**2 - 1) * (Q**3 - 1)
            for p in prime_list:
                assert valuation(E, p) == valuation(D, p)
                assert gcd(E, p - 1) == gcd(D, p - 1)
                actual = {pow(u, E, p) for u in range(1, p)}
                target = {pow(u, D, p) for u in range(1, p)}
                assert actual == target
                valuations += 1
                images += 1
            divisor = gcd(6 * C * following**3, Q - 1)
            assert n % divisor == 0
            fresh += 1
    print(f"Exact cubic-exponent valuations and triangular gcd identities checked in {valuations} cases.")
    print(f"Actual finite-field power images agree in {images} cases.")
    print(f"The fresh gcd(D_next,Q-1)|n implication holds for {fresh} explicit CRT integers.")


def primitive_preimage_checks():
    checked = 0
    for p in primes_through(127):
        if p < 7:
            continue
        N = p - 1
        generator = primitive_root(p)
        primitive = {pow(generator, k, p) for k in range(N) if gcd(k, N) == 1}
        assert all(pow(u, 2, p) != 1 and pow(u, 3, p) != 1 for u in primitive)
        for e in range(N):
            g = gcd(e, N)
            M = N // g
            image_generators = {pow(generator, g * t, p)
                                for t in range(M) if gcd(t, M) == 1}
            actual = {pow(u, e, p) for u in primitive}
            assert actual == image_generators
            checked += len(image_generators)
    print(f"Every generator has a primitive preimage in {checked} exact power-map cases.")


def local_image_checks():
    trials = 0
    balls = 0
    for p, n in ((2, 720), (2, 1440), (3, 720), (3, 2160), (5, 720), (5, 3600), (7, 5040)):
        s = valuation(n, p)
        assert s >= (4 if p == 2 else 2 if p == 3 else 1)
        for C in (24, 48):
            h = 4 * s + valuation(6 * C, p)
            depth = h + 1 + valuation(3, p)
            z0 = 1 + p**s
            for precision in (1, 2, 3):
                modulus = p ** (depth + precision)
                base_exponent = C * n * (z0**2 - 1) * (z0**3 - 1)
                base_value = pow(z0, base_exponent, modulus)
                outputs = set()
                for t in range(p**precision):
                    z = z0 + p**(s + 1) * t
                    assert valuation(z - 1, p) == s
                    exponent = C * n * (z**2 - 1) * (z**3 - 1)
                    difference = (pow(z, exponent, modulus) - base_value) % modulus
                    assert difference % p**depth == 0
                    outputs.add(difference // p**depth)
                    trials += 1
                assert outputs == set(range(p**precision))
                balls += 1
    print(f"The exact cubic local image is bijective in {balls} finite quotient balls ({trials} inputs).")


def series_and_precision_checks():
    coefficients = (Fraction(1), Fraction(3, 2), Fraction(5, 6), Fraction(1, 6))
    checked = 0
    for p, s in ((2, 4), (2, 5), (3, 2), (3, 3), (5, 1), (7, 1)):
        for k in range(1, 101):
            coefficient = sum((coefficients[r] * Fraction((-1)**(k - r), k - r + 1)
                               for r in range(min(3, k) + 1)), Fraction())
            if coefficient:
                order = k * s + valuation(coefficient.numerator, p) - valuation(coefficient.denominator, p)
                assert order >= s
            checked += 1
    precision_cases = 0
    for C in (24, 48, 120, 264):
        J = max(6, max(factors(C)))
        for j in range(21):
            n = factorial(J + j)
            D = 6 * C * n**3
            for p in primes_through(43):
                s = valuation(n, p)
                delta = 3 * s + valuation(18 * C, p) if s else 0
                H = 2 * delta + j + 3
                assert H > 2 * valuation(D, p)
                if s:
                    required = 4 * s + valuation(6 * C, p) + 1 + valuation(3, p)
                    assert H >= required
                precision_cases += 1
    for D in range(2, 501):
        assert (D + 1)**4 > 15 * D
    print(f"Normalized cubic-series coefficient bounds checked in {checked} exact rational cases.")
    print(f"Local inverse and next-stage Hensel inequalities checked in {precision_cases} cases.")
    print("The fifteen-target scaling bound holds for every tested D=2,...,500.")


if __name__ == "__main__":
    triangular_checks()
    primitive_preimage_checks()
    local_image_checks()
    series_and_precision_checks()
    print("All finite cubic-exponent certificates passed. No full prime-search stage was executed.")
