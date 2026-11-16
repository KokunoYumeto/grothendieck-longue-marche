#!/usr/bin/env python3
"""Finite exact certificates for A.66's fixed-product prime recursion.

The analytic-image tests use literal integer powers modulo prime powers.
The triangular tests use exact CRT integers, not primes: Chebotarev is the
proved step producing primes in those classes. No infinite prime search or
full stage with its enormous all-place bound is claimed here.
"""

from fractions import Fraction
from math import comb, factorial, gcd, prod


def primes_through(bound):
    sieve = [True] * (bound + 1)
    sieve[:2] = [False, False]
    for p in range(2, int(bound**0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, bound + 1, p):
                sieve[multiple] = False
    return [p for p in range(2, bound + 1) if sieve[p]]


def valuation(value, p):
    if value == 0:
        return float("inf")
    value = abs(value)
    count = 0
    while value % p == 0:
        value //= p
        count += 1
    return count


def rational_valuation(value, p):
    return valuation(value.numerator, p) - valuation(value.denominator, p)


def floor_log(value, p):
    answer = 0
    while value >= p:
        value //= p
        answer += 1
    return answer


def prime_factors(value):
    answer = set()
    for p in primes_through(value):
        if value % p == 0:
            answer.add(p)
    return answer


def primitive_root(p):
    divisors = prime_factors(p - 1)
    return next(u for u in range(1, p)
                if all(pow(u, (p - 1) // ell, p) != 1 for ell in divisors))


def crt(residues, moduli):
    modulus = prod(moduli)
    result = sum(a * (modulus // m) * pow(modulus // m, -1, m)
                 for a, m in zip(residues, moduli)) % modulus
    return result, modulus


def multiply(left, right):
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            answer[i + j] += x * y
    return answer


def normalized_polynomial(d):
    answer = [Fraction(1)]
    for r in range(2, d + 1):
        factor = [Fraction(comb(r, k + 1), r) for k in range(r)]
        answer = multiply(answer, factor)
    return answer


def local_parameters(d, p, C=24):
    a = valuation(factorial(d), p)
    b = valuation(d, p)
    s = a + b + 2 if p <= d else 1
    # Keep the actual construction's dyadic convergence range as well.
    if p == 2:
        s = max(4, s)
    kappa = s - a - 1 if p <= d else s
    h = (d + 1) * s + valuation(C * factorial(d), p)
    return a, b, s, kappa, h


def series_checks():
    rational_checks = 0
    exponential_checks = 0
    for d in range(2, 9):
        P = normalized_polynomial(d)
        assert P[0] == 1
        assert all((factorial(d) * coefficient).denominator == 1 for coefficient in P)
        for p in (2, 3, 5, 7, 11):
            a, b, s, kappa, h = local_parameters(d, p)
            assert kappa >= b + 1
            for k in range(1, 101):
                coefficient = sum((P[j] * Fraction((-1)**(k - j), k - j + 1)
                                   for j in range(min(k, len(P) - 1) + 1)), Fraction())
                if coefficient:
                    order = rational_valuation(coefficient, p)
                    assert order >= -a - floor_log(k + 1, p)
                    assert order + k * s >= kappa
                rational_checks += 1
            for u in range(2, 61):
                order = (u - 1) * h - valuation(factorial(u), p)
                assert order >= kappa
                exponential_checks += 1
            for k in range(2, d + 1):
                order = valuation(comb(d, k), p) + (b + 1) * k - (2 * b + 1)
                assert order >= 1
    print(f"Exact normalized V-series valuation checks: {rational_checks}.")
    print(f"Exact exponential-denominator checks: {exponential_checks}.")
    print("The binomial terms in the normalized inverse map are all divisible by p.")


def local_image_checks():
    balls = 0
    inputs = 0
    derivative_checks = 0
    C = 24
    for d in range(2, 9):
        for p in (2, 3, 5, 7, 11):
            a, b, s, kappa, h = local_parameters(d, p, C)
            n = p**s
            z0 = 1 + p**s
            step = p**(s + b + 1)
            depth = h + 2 * b + 1
            derivative_depth = d * s + valuation(C * factorial(d), p) + b
            assert depth == derivative_depth + s + b + 1
            for precision in (1, 2, 3):
                modulus = p**(depth + precision)
                base_exponent = C * n * prod(z0**r - 1 for r in range(2, d + 1))
                base_value = pow(z0, base_exponent, modulus)
                outputs = set()
                for t in range(p**precision):
                    z = z0 + step * t
                    assert valuation(z - 1, p) == s
                    exponent = C * n * prod(z**r - 1 for r in range(2, d + 1))
                    difference = (pow(z, exponent, modulus) - base_value) % modulus
                    assert difference % p**depth == 0
                    outputs.add(difference // p**depth)
                    if t == 1:
                        assert valuation(difference, p) == depth
                        derivative_checks += 1
                    inputs += 1
                assert outputs == set(range(p**precision))
                balls += 1
    print(f"Literal integer-power local-image equalities: {balls} quotient balls, {inputs} inputs.")
    print(f"Exact finite-increment derivative-depth checks: {derivative_checks}.")


def triangular_checks():
    checked = 0
    images = 0
    fresh = 0
    C = 24
    for d in range(2, 9):
        J = 2 * d * d
        for j in range(3):
            n = factorial(J + j)
            next_n = factorial(J + j + 1)
            D = C * factorial(d) * n**d
            next_D = C * factorial(d) * next_n**d
            bound = max(53, J + j + 5)
            primes = primes_through(bound)
            residues, moduli = [], []
            for p in primes:
                s = valuation(n, p)
                L = 1
                while p**L <= bound:
                    L += 1
                if s:
                    L = max(L, s + valuation(d, p) + 2)
                    residue = 1 + p**s
                else:
                    residue = primitive_root(p)
                    assert p - 1 > d
                    assert all(pow(residue, r, p) != 1 for r in range(2, d + 1))
                residues.append(residue)
                moduli.append(p**L)
            Q, modulus = crt(residues, moduli)
            if Q <= 1:
                Q += modulus
            E = C * n * prod(Q**r - 1 for r in range(2, d + 1))
            for p in primes:
                assert valuation(E, p) == valuation(D, p)
                assert gcd(E, p - 1) == gcd(D, p - 1)
                # Fermat reduction is exact for these nonzero residues.
                image_E = {pow(u, E % (p - 1), p) for u in range(1, p)}
                image_D = {pow(u, D % (p - 1), p) for u in range(1, p)}
                assert image_E == image_D
                checked += 1
                images += 1
            assert Q % n == 1
            assert gcd(next_D, Q - 1) == n
            fresh += 1
    print(f"Exact LTE and triangular exponent-gcd checks: {checked}.")
    print(f"Exact finite-field common power-image checks: {images}.")
    print(f"Fresh gcd(D_next,Q-1)=n checks for explicit CRT integers: {fresh}.")


def primitive_and_precision_checks():
    preimages = 0
    precision = 0
    for d in range(2, 9):
        for p in primes_through(127):
            N = p - 1
            if N <= d:
                continue
            zeta = primitive_root(p)
            primitive = {pow(zeta, k, p) for k in range(N) if gcd(k, N) == 1}
            assert all(all(pow(u, r, p) != 1 for r in range(2, d + 1)) for u in primitive)
            for e in range(N):
                g = gcd(e, N)
                M = N // g
                generators = {pow(zeta, g * t, p) for t in range(M) if gcd(t, M) == 1}
                assert {pow(u, e, p) for u in primitive} == generators
                preimages += len(generators)
        J = 2 * d * d
        for j in range(11):
            n = factorial(J + j)
            for p in primes_through(J + j + 5):
                s = valuation(n, p)
                a = valuation(factorial(d), p)
                b = valuation(d, p)
                cd = valuation(24 * factorial(d), p)
                delta = d * s + cd + b if s else 0
                H = 2 * delta + j + 3
                assert H > 2 * (d * s + cd)
                if s:
                    kappa = s - a - 1 if p <= d else s
                    assert kappa >= b + 1
                    if p <= d:
                        assert s >= a + b + 2
                    h = (d + 1) * s + cd
                    assert H >= h + 2 * b + 1
                precision += 1
        for D in range(d, 501):
            assert (D + 1)**4 - 1 > 3 * D * sum(range(2, d + 1))
    print(f"Primitive-preimage target checks: {preimages}.")
    print(f"Actual factorial inverse/Hensel precision checks: {precision}.")
    print("Critical-target scaling inequalities checked for d=2,...,8 and d<=D<=500.")


if __name__ == "__main__":
    series_checks()
    local_image_checks()
    triangular_checks()
    primitive_and_precision_checks()
    print("All finite A.66 certificates passed. No full prime-search stage was executed.")
