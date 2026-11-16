#!/usr/bin/env python3
"""Exact finite certificates for A.47--A.48.

These checks exercise the commutator formula, private-prime initialization,
curve bound, local congruence algebra, and precision inequalities.  They
do not execute any full prime-search stage of the infinite construction.
Termination of those searches is proved by A.47 and Chebotarev.
"""
from fractions import Fraction
from itertools import product
from math import factorial, gcd, prod


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))


def primes_through(n):
    return [p for p in range(2, n + 1) if is_prime(p)]


def valuation_integer(value, p):
    if value == 0:
        return float("inf")
    value = abs(value)
    answer = 0
    while value % p == 0:
        answer += 1
        value //= p
    return answer


def valuation(value, p):
    value = Fraction(value)
    return (valuation_integer(value.numerator, p)
            - valuation_integer(value.denominator, p))


def prime_support(value):
    value = abs(value)
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


def semilinear_multiply(first, second, m):
    u, k = first
    v, ell = second
    return u * v % (2 * m), tuple((a + u * b) % m
                                 for a, b in zip(k, ell))


def semilinear_inverse(element, m):
    u, k = element
    inv = pow(u, -1, 2 * m)
    return inv, tuple(-inv * a % m for a in k)


def commutator(first, second, m):
    answer = semilinear_multiply(first, second, m)
    answer = semilinear_multiply(answer, semilinear_inverse(first, m), m)
    return semilinear_multiply(answer, semilinear_inverse(second, m), m)


def commutator_checks():
    checked = 0
    for m in (4, 8, 12, 16, 24, 40, 48):
        for s in range(1, 5):
            conjugation = (2 * m - 1, (0,) * s)
            for u in range(1, 2 * m):
                if gcd(u, 2 * m) != 1:
                    continue
                for k in product(range(4), repeat=s):
                    result = commutator(conjugation, (u, k), m)
                    assert result == (1, tuple(-2 * a % m for a in k))
                    assert tuple((a // 2) % 2 for a in result[1]) == tuple(a % 2 for a in k)
                    checked += 1
    decompositions = 0
    for h in (2, 4, 6, 12):
        for s in range(1, 5):
            for vector in product(range(h), repeat=s):
                parity = tuple(t % 2 for t in vector)
                even_half = tuple((t - e) // 2 for t, e in zip(vector, parity))
                assert tuple((e + 2 * a) % h
                             for e, a in zip(parity, even_half)) == vector
                decompositions += 1
    print(f"Exact complex-conjugation commutator checked in {checked} semilinear cases.")
    print(f"Generation of N by 2N and all quadratic sign vectors checked in {decompositions} cases.")


def crt(residues, moduli):
    modulus = prod(moduli)
    result = sum(a * (modulus // q) * pow(modulus // q, -1, q)
                 for a, q in zip(residues, moduli)) % modulus
    return result, modulus


def initial_coefficients(punctures):
    largest_difference = max(abs(a - b) for a in punctures for b in punctures)
    candidates = []
    candidate = max(3, largest_difference + 1)
    while len(candidates) < len(punctures):
        if is_prime(candidate):
            candidates.append(candidate)
        candidate += 1
    residues = [c + p for c, p in zip(punctures, candidates)]
    R, modulus = crt(residues, [p * p for p in candidates])
    while R <= max(punctures):
        R += modulus
    return R, candidates, [R - c for c in punctures]


def private_prime_checks():
    total = 0
    examples = [(0, 1), (0, 1, 2), (-1, 0, 1, 2), (-3, 2, 7), (-3, 2, 5)]
    for punctures in examples:
        R, private, coefficients = initial_coefficients(punctures)
        assert all(a > 0 for a in coefficients)
        for i, p in enumerate(private):
            for j, a in enumerate(coefficients):
                assert valuation(a, p) == int(i == j)
            assert all((c - d) % p for c in punctures for d in punctures if c != d)
        forbidden = set(private)
        for a in coefficients:
            forbidden |= prime_support(a)
        for c in punctures:
            for d in punctures:
                if c != d:
                    forbidden |= prime_support(c - d)
        fresh = []
        candidate = max(forbidden) + 1
        while len(fresh) < len(coefficients):
            if is_prime(candidate):
                fresh.append(candidate)
            candidate += 1
        for i in range(len(punctures)):
            updated = [a * q**8 if t < i else a
                       for t, (a, q) in enumerate(zip(coefficients, fresh))]
            indices = [t for t in range(len(punctures)) if t != i]
            radicands = [abs(Fraction(punctures[i] - punctures[t], updated[t]))
                         for t in indices]
            for t, d in zip(indices, radicands):
                for u in indices:
                    assert valuation(d, private[u]) == (-1 if u == t else 0)
                    total += 1
                old = abs(Fraction(punctures[i] - punctures[t], coefficients[t]))
                ratio = d / old
                expected = Fraction(1, fresh[t]**8) if t < i else Fraction(1)
                assert ratio == expected
                # In particular the squareclass and eighth-power form are unchanged.
                square_root = Fraction(1, fresh[t]**4) if t < i else Fraction(1)
                assert square_root * square_root == ratio
        print(f"Private-prime initialization: punctures={punctures}, R={R}, primes={tuple(private)}.")
    print(f"Private-prime independence after sequential updates checked in {total} valuation entries.")
    # Exact rational coordinate change, including its unit-coordinate functions.
    original = (Fraction(-1, 2), Fraction(1, 3), Fraction(5, 6))
    D = 6
    assert tuple(D * c for c in original) == (-3, 2, 5)
    for t in (Fraction(7, 5), Fraction(-13, 7)):
        for c in original:
            assert (D * t - D * c) / D == t - c
    print("The rational-puncture comparison T=6t was checked exactly on all three functions.")


def curve_checks():
    algebraic = 0
    for k in range(2, 10):
        for m in range(2, 61):
            degree = m**k
            boundary = (k + 1) * m**(k - 1)
            twice_genus = 2 + (k - 1) * degree - boundary
            assert twice_genus >= 0 and twice_genus % 2 == 0
            assert twice_genus - 2 == -2 * degree + (k + 1) * (degree - degree // m)
            threshold = (k + 1) * degree + 3
            assert threshold - twice_genus == 2 * degree + boundary + 1
            assert threshold * threshold - twice_genus * threshold + 1 - boundary > 0
            assert 2 * threshold - twice_genus > 0
            algebraic += 1
    finite = 0
    direct = 0
    for p in primes_through(31):
        for k in range(2, min(4, p - 1) + 1):
            punctures = tuple(range(k))
            for m in range(2, 9):
                if m % p == 0:
                    continue
                d = gcd(m, p - 1)
                powers = {pow(x, m, p) for x in range(1, p)}
                twice_genus = 2 + (k - 1) * m**k - (k + 1) * m**(k - 1)
                boundary = (k + 1) * m**(k - 1)
                for coefficients in product(range(1, min(4, p)), repeat=k):
                    allowed_sets = [{(c + a * u) % p for u in powers}
                                    for a, c in zip(coefficients, punctures)]
                    t_values = set.intersection(*allowed_sets)
                    count = len(t_values) * d**k
                    gap = p + 1 - boundary - count
                    assert gap <= 0 or gap * gap <= twice_genus**2 * p
                    if p in (5, 7) and k <= 3 and m in (2, 3) and coefficients == (1,) * k:
                        brute = 0
                        for roots in product(range(1, p), repeat=k):
                            values = {(c + a * pow(x, m, p)) % p
                                      for a, c, x in zip(coefficients, punctures, roots)}
                            brute += len(values) == 1
                        assert count == brute
                        direct += 1
                    finite += 1
    print(f"Genus, boundary, and uniform positivity identities checked in {algebraic} (k,m) cases.")
    print(f"Exact interior counts satisfy the curve bound in {finite} finite-field cases.")
    print(f"Interior count formula agrees with full root-tuple enumeration in {direct} cases.")


def simple_root_lift(target, exponent, p, precision, root):
    modulus = p**precision
    assert (pow(root, exponent, p) - target) % p == 0
    for _ in range(precision + 2):
        error = (pow(root, exponent, modulus) - target) % modulus
        if error == 0:
            break
        derivative = exponent * pow(root, exponent - 1, modulus) % modulus
        assert gcd(derivative, p) == 1
        root = (root - error * pow(derivative, -1, modulus)) % modulus
    assert (pow(root, exponent, modulus) - target) % modulus == 0
    return root


def new_prime_local_checks():
    checks = 0
    n, m, precision = 4, 8, 5
    for q in (17, 41, 73, 89):
        assert q % m == 1
        modulus = q**precision
        for k in range(2, 6):
            punctures = tuple(range(k))
            for h in range(k):
                # All coefficients except h have the exact required split residue.
                # For later indices, the extra prime residue converts it to 1.
                final_coefficients = [None] * k
                root_residues = [None] * k
                for i in range(k):
                    if i == h:
                        final_coefficients[i] = 3 * q**n
                        root_residues[i] = 1
                        continue
                    chosen_root = i + 2
                    difference = punctures[h] - punctures[i]
                    old_coefficient = difference * pow(pow(chosen_root, m, q), -1, q) % q
                    assert old_coefficient != 0
                    if i < h:
                        final_coefficients[i] = old_coefficient
                        root_residues[i] = chosen_root
                    else:
                        later_prime_residue = pow(chosen_root, m // n, q)
                        assert old_coefficient * pow(later_prime_residue, n, q) % q == difference % q
                        final_coefficients[i] = old_coefficient * later_prime_residue**n
                        root_residues[i] = 1
                T = punctures[h] + final_coefficients[h]
                for i in range(k):
                    if i == h:
                        assert T - punctures[i] == final_coefficients[i]
                        continue
                    target = ((T - punctures[i]) * pow(final_coefficients[i], -1, modulus)) % modulus
                    root = simple_root_lift(target, m, q, precision, root_residues[i])
                    assert ((T - punctures[i]) - final_coefficients[i] * pow(root, m, modulus)) % modulus == 0
                    checks += 1
    print(f"Earlier/later-coordinate congruences and simultaneous Hensel roots checked in {checks} cases.")


def precision_checks():
    checked = 0
    for N0 in (8, 24, 120, 840):
        for j in range(16):
            n, m, later = (N0 * factorial(j + shift) for shift in (1, 2, 3))
            for p in primes_through(47):
                for V in range(8):
                    H = V + 2 * valuation_integer(2 * m, p) + j + 3
                    L = V + 2 * valuation_integer(2 * later, p) + j + 4
                    for coefficient_valuation in range(V + 1):
                        assert H - coefficient_valuation > 2 * valuation_integer(n, p)
                        assert H - coefficient_valuation - valuation_integer(n, p) >= valuation_integer(2 * m, p)
                        assert L - coefficient_valuation > 2 * valuation_integer(m, p)
                    assert L >= valuation_integer(2 * m, p)
                    if 2 * m % p == 0:
                        assert 2 * N0 % p == 0 or p <= j + 2
                        assert p <= ((2 + 1) * n**2 + 3)**2
                    checked += 1
    print(f"V_p-corrected anticipatory precision inequalities checked in {checked} cases.")


if __name__ == "__main__":
    commutator_checks()
    private_prime_checks()
    curve_checks()
    new_prime_local_checks()
    precision_checks()
    print("All finite certificates passed. No full Chebotarev prime-search stage was executed.")
