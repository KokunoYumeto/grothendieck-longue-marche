#!/usr/bin/env python3
"""Finite exact certificates for A.44's infinite recursive construction.

This does NOT execute the extremely large first prime search.  Existence
and termination of those searches are proved by the field-intersection
lemma and Chebotarev in ghost_agent.tex.  All checks below use integers.
"""
from functools import reduce
from math import factorial, gcd


def primes_through(limit):
    return [p for p in range(2, limit + 1)
            if all(p % d for d in range(2, int(p**0.5) + 1))]


def valuation(value, p):
    if value == 0:
        return float("inf")
    answer = 0
    while value % p == 0:
        answer += 1
        value //= p
    return answer


def compose(first, second):
    return tuple(first[second[j]] for j in range(4))


def inverse(perm):
    return tuple(perm.index(j) for j in range(4))


def group_checks():
    moduli = sorted(set([24 * j for j in range(1, 61)]
                        + [factorial(j) for j in range(4, 9)]))
    for h in moduli:
        values = [u - 1 for u in range(1, h) if gcd(u, h) == 1]
        assert reduce(gcd, values, h // 2) == 2
    identity = (0, 1, 2, 3)
    rotation = (1, 2, 3, 0)
    conjugation = (0, 3, 2, 1)
    generated = {identity}
    changed = True
    while changed:
        enlarged = generated | {compose(a, b) for a in generated
                                 for b in (rotation, conjugation)}
        changed = len(enlarged) != len(generated)
        generated = enlarged
    assert len(generated) == 8
    commutator = compose(compose(compose(conjugation, rotation),
                                inverse(conjugation)), inverse(rotation))
    assert commutator == (2, 3, 0, 1)
    assert commutator != identity
    print(f"Kummer commutator gcd checked at {len(moduli)} multiples of 24.")
    print("Fourth-root rotation/conjugation generate D4 of order 8; commutator is rotation squared.")


def finite_field_checks():
    count = 0
    direct_count = 0
    for p in primes_through(43):
        for m in range(2, 31):
            if m % p == 0:
                continue
            d = gcd(m, p - 1)
            power_set = {pow(x, m, p) for x in range(1, p)}
            assert len(power_set) == (p - 1) // d
            for a in range(1, p):
                avalues = {a * u % p for u in power_set}
                for b in range(1, p):
                    bvalues = {b * u % p for u in power_set}
                    number = d * d * sum((1 - t) % p in bvalues for t in avalues)
                    base = p - 2 - 3 * (d - 1)
                    coefficient = (d - 1) * (d - 2)
                    gap = base - number
                    # number >= base - coefficient*sqrt(p), with no floating point.
                    assert gap <= 0 or gap * gap <= coefficient * coefficient * p
                    if p in (7, 13, 19) and m in (2, 3, 4, 6) and a <= 3 and b <= 3:
                        direct = sum((a * pow(x, m, p) + b * pow(y, m, p) - 1) % p == 0
                                     for x in range(1, p) for y in range(1, p))
                        assert number == direct
                        direct_count += 1
                    count += 1
    for m in range(2, 501):
        threshold = (m + 1) ** 2
        coefficient = (m - 1) * (m - 2)
        lower = threshold * threshold - coefficient * threshold - 3 * m + 1
        assert lower == m * m * (5 * m + 9) > 0
        assert 2 * threshold > coefficient
    print(f"Jacobi-sum integer lower bound checked for {count} coefficient/exponent/prime cases.")
    print(f"Power-coset counts compared with full pair enumeration in {direct_count} cases.")
    print("Large-prime positivity identity and increasing-polynomial condition checked for m=2,...,500.")


def root_near_one(n, p, error_order, precision):
    e = valuation(n, p)
    assert error_order > 2 * e
    target = 1 + p ** error_order
    modulus = p ** precision
    enlarged = p ** (precision + e)
    root = 1
    for _ in range(32):
        if (pow(root, n, modulus) - target) % modulus == 0:
            break
        error = (pow(root, n, enlarged) - target) % enlarged
        assert error % p ** e == 0
        derivative_unit = (n // p ** e) * pow(root, n - 1, modulus) % modulus
        increment = (error // p ** e) * pow(derivative_unit, -1, modulus) % modulus
        root = (root - increment) % modulus
    assert (pow(root, n, modulus) - target) % modulus == 0
    assert valuation(root - 1, p) >= error_order - e
    return root


def precision_checks():
    prime_list = primes_through(47)
    inequalities = 0
    roots = 0
    for j in range(41):
        n, m, later = factorial(j + 4), factorial(j + 5), factorial(j + 6)
        for p in prime_list:
            e, d = valuation(n, p), valuation(m, p)
            old_error = 2 * d + j + 3
            new_error = 2 * valuation(later, p) + j + 4
            if m % p == 0:
                assert p <= j + 5 <= (n + 1) ** 4
                assert old_error > 2 * e
                assert old_error - e >= d
            assert new_error > 2 * d
            assert new_error >= d
            inequalities += 1
            if j <= 3 and p <= 19:
                root_near_one(n, p, old_error, old_error + 8)
                roots += 1
    print(f"Anticipatory Hensel inequalities checked in {inequalities} index/prime cases.")
    print(f"Exact modular Newton lifts with the claimed displacement checked in {roots} cases.")
    annihilations = 0
    for p in primes_through(31):
        for k in range(1, 9):
            exponent_bound = (p - 1) * p ** (k - 1)
            j = 0
            while factorial(j + 4) % exponent_bound:
                j += 1
            assert factorial(j + 4) % exponent_bound == 0
            annihilations += 1
    print(f"Factorial annihilation of local-unit exponent bounds checked in {annihilations} cases.")


if __name__ == "__main__":
    group_checks()
    finite_field_checks()
    precision_checks()
    print("All finite certificates passed. No giant prime-search stage was executed.")
