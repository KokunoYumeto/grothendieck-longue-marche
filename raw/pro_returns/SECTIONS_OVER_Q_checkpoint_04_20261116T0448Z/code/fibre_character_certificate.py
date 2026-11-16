#!/usr/bin/env python3
"""Exact finite certificates for the fibre-character calculation A.57.

The Galois group is represented by its cyclotomic action and the signs
on square roots of the support primes.  The group presentation itself
is proved in A.57; these computations check its stabilizers, the
equivalent divisibility criterion, and explicit norm identities.
"""
from fractions import Fraction
from itertools import product
from math import gcd, lcm


def quadratic_conductor(p):
    return 8 if p == 2 else (p if p % 4 == 1 else 4 * p)


def quadratic_bit(p, a):
    if p == 2:
        return ((a * a - 1) // 8) % 2
    bit = int(pow(a % p, (p - 1) // 2, p) == p - 1)
    return (bit + ((a - 1) // 2 if p % 4 == 3 else 0)) % 2


def gamma_group(n, primes):
    modulus = lcm(2 * n, *(quadratic_conductor(p) for p in primes))
    gamma = {(a % (2 * n), tuple(quadratic_bit(p, a) for p in primes))
             for a in range(1, modulus) if gcd(a, modulus) == 1}
    return gamma


def gamma_multiply(first, second, n):
    return (first[0] * second[0] % (2 * n),
            tuple(a ^ b for a, b in zip(first[1], second[1])))


def generated_subgroup(generators, n, s):
    subgroup = {(1, (0,) * s)}
    pending = list(subgroup)
    while pending:
        element = pending.pop()
        for generator in generators:
            candidate = gamma_multiply(element, generator, n)
            if candidate not in subgroup:
                subgroup.add(candidate)
                pending.append(candidate)
    return subgroup


def admissible(gamma, n, weights, signs):
    u, eps = gamma
    d = gcd(n, u - 1)
    for k in product(*(range(e, n, 2) for e in eps)):
        if all(((u - 1) // 2 * delta + sum(w * exponent for w, exponent in zip(row, k))) % d == 0
               for row, delta in zip(weights, signs)):
            return True
    return False


def fibre_quotient(n, primes, weights, signs):
    gamma = gamma_group(n, primes)
    generators = {g for g in gamma if admissible(g, n, weights, signs)}
    subgroup = generated_subgroup(generators, n, len(primes))
    assert subgroup <= gamma
    r = 0
    odd = n
    while odd % 2 == 0:
        odd //= 2
        r += 1
    upper_field_kernel = {g for g in gamma
                          if g[0] % (2 ** (r + 1)) == 1 and not any(g[1])}
    assert upper_field_kernel <= subgroup
    degree = len(gamma) // len(subgroup)
    assert degree >= 1 and degree & (degree - 1) == 0
    return gamma, subgroup, degree


def stabilizer_checks():
    cases = 0
    for n in (4, 8, 12):
        for primes in ((2,), (5,), (3, 5)):
            gamma = gamma_group(n, primes)
            rows = [tuple(((i + 1) * (j + 2)) % 5 - 2
                          for j in range(len(primes))) for i in range(3)]
            for g in gamma:
                u, eps = g
                d = gcd(n, u - 1)
                for k in product(*(range(e, n, 2) for e in eps)):
                    for row in rows:
                        for delta in (0, 1):
                            via_roots = any(((u - 1) * (delta + 2 * e)
                                             + 2 * sum(w * exponent for w, exponent in zip(row, k)))
                                            % (2 * n) == 0 for e in range(n))
                            via_divisibility = (((u - 1) // 2 * delta
                                                 + sum(w * exponent for w, exponent in zip(row, k))) % d == 0)
                            assert via_roots == via_divisibility
                            cases += 1
    print(f"Exact root stabilizers agree with the divisibility criterion in {cases} cases.")


def explicit_examples():
    for n, expected in ((4, 8), (8, 16), (24, 16), (40, 16), (120, 16)):
        gamma, subgroup, degree = fibre_quotient(n, (5,), ((-1,), (-1,)), (0, 1))
        assert degree == expected
        print(f"D=(1/5,-1/5), n={n}: |Gamma|={len(gamma)}, |H|={len(subgroup)}, [B:Q]={degree}.")
        if n == 4:
            assert subgroup == {(1, (0,))}
            ordering = sorted(gamma)
            first = tuple(g[1][0] for g in ordering)
            second = tuple(g[1][0] ^ (((g[0] - 1) // 2) % 2) for g in ordering)
            extra_two = tuple(((g[0] * g[0] - 1) // 8) % 2 for g in ordering)
            span = {tuple(a * x ^ b * y for x, y in zip(first, second))
                    for a, b in product((0, 1), repeat=2)}
            assert extra_two not in span
    examples = [
        ("D=(2,8)", 4, (2,), ((1,), (3,)), (0, 0), 2),
        ("D=(1/25)", 4, (5,), ((-2,),), (0,), 1),
        ("D=(-1/25)", 4, (5,), ((-2,),), (1,), 4),
        ("D=(3,75,-1)", 4, (3, 5), ((1, 0), (1, 2), (0, 0)), (0, 0, 1), 16),
    ]
    for label, n, primes, rows, signs, expected in examples:
        gamma, subgroup, degree = fibre_quotient(n, primes, rows, signs)
        assert degree == expected
        print(f"{label}, n={n}: |Gamma|={len(gamma)}, |H|={len(subgroup)}, [B:Q]={degree}.")
    checked = 0
    for n in (4, 8, 12, 24):
        for primes in ((2,), (5,), (3, 5)):
            s = len(primes)
            for seed in range(12):
                rows = tuple(tuple(((seed + 2 * i + 3 * j) % 7) - 3
                                   for j in range(s)) for i in range(1 + seed % 3))
                signs = tuple((seed + i) % 2 for i in range(len(rows)))
                fibre_quotient(n, primes, rows, signs)
                checked += 1
    print(f"The two-primary upper-field kernel inclusion holds in {checked} further examples.")


def determinant_bareiss(matrix):
    matrix = [list(row) for row in matrix]
    size = len(matrix)
    sign = 1
    previous = 1
    for k in range(size - 1):
        if matrix[k][k] == 0:
            exchange = next((j for j in range(k + 1, size) if matrix[j][k] != 0), None)
            if exchange is None:
                return 0
            matrix[k], matrix[exchange] = matrix[exchange], matrix[k]
            sign *= -1
        pivot = matrix[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = matrix[i][j] * pivot - matrix[i][k] * matrix[k][j]
                assert numerator % previous == 0
                matrix[i][j] = numerator // previous
            matrix[i][k] = 0
        previous = pivot
    return sign * matrix[-1][-1]


def cyclotomic_norm(A, B, degree):
    # Multiplication by A-B*z in Q[z]/(z^degree+1), in the power basis.
    matrix = [[0] * degree for _ in range(degree)]
    for j in range(degree):
        matrix[j][j] = A
        if j + 1 < degree:
            matrix[j + 1][j] = -B
        else:
            matrix[0][j] = B
    return determinant_bareiss(matrix)


def norm_checks():
    quadratic = 0
    for X, Y in product(range(-12, 13), repeat=2):
        assert X**4 + Y**4 == (X * X + Y * Y)**2 - 2 * (X * Y)**2
        quadratic += 1
    cyclotomic = 0
    for r in range(2, 6):
        for odd in (1, 3, 5):
            n = 2**r * odd
            for X, Y in ((0, 1), (1, 0), (1, 1), (2, 3), (-3, 2)):
                assert cyclotomic_norm(X**odd, Y**odd, 2**r) == X**n + Y**n
                cyclotomic += 1
    polynomial = 0
    for a in (Fraction(3), Fraction(13), Fraction(5, 3)):
        for b in (Fraction(2), Fraction(12), Fraction(7, 5)):
            for n in (4, 8, 24):
                for X, Y in ((1, 1), (2, 3), (-3, 2)):
                    residual = ((a + b) * (a * X**n - a / (a + b))
                                - a * b * (X**n + Y**n))
                    assert residual == a * (a * X**n - b * Y**n - 1)
                    polynomial += 1
    print(f"The quadratic norm identity was checked at {quadratic} integer pairs.")
    print(f"The full 2-power cyclotomic norm was checked by {cyclotomic} exact determinants.")
    print(f"The old-curve substitution identity was checked in {polynomial} rational coefficient cases.")


if __name__ == "__main__":
    stabilizer_checks()
    explicit_examples()
    norm_checks()
    print("All finite fibre-character certificates passed.")
