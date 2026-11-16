#!/usr/bin/env python3
"""Finite arithmetic checks supporting A.83's proved prime-product argument.

The program verifies finite ray classes and inequalities.  It does not
claim that a finite list of primes executes the global initialization.
"""
from math import gcd, isqrt


def primes_through(bound):
    sieve = [True] * (bound + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, isqrt(bound) + 1):
        if sieve[p]:
            for x in range(p * p, bound + 1, p):
                sieve[x] = False
    return [p for p in range(2, bound + 1) if sieve[p]]


def bit_5(a):
    return 1 if a % 5 in (1, 4) else -1


def bit_minus_5(a):
    return bit_5(a) * (1 if a % 4 == 1 else -1)


def main():
    units = {a for a in range(20) if gcd(a, 20) == 1}
    allowed = {a for a in units if 1 in (bit_5(a), bit_minus_5(a))}
    assert allowed == {1, 3, 7, 9, 11, 19}
    assert 13 not in allowed and 17 not in allowed
    assert 3 * 11 % 20 == 13 and 7 * 11 % 20 == 17
    products = {(a * b) % 20 for a in allowed for b in allowed}
    assert products == units
    checks = 0
    for p in primes_through(20000):
        if p in (2, 5):
            continue
        # In F_p^*, x^4=25 iff 25^((p-1)/gcd(4,p-1))=1.
        literal = pow(25 % p, (p - 1) // gcd(4, p - 1), p) == 1
        assert literal == (p % 20 in allowed)
        checks += 1
    print(f"Literal fourth-power fibre tests agree with ray characters at {checks} primes.")
    print("Admissible ray classes: 1,3,7,9,11,19; twofold products give all eight units modulo20.")

    bounds = 0
    for n in range(4, 65, 4):
        for k in range(1, 9):
            degree = n ** (k + 1)
            twice_genus_minus_two = -2 * degree + (k + 2) * n**k * (n - 1)
            assert twice_genus_minus_two % 2 == 0
            genus = (twice_genus_minus_two + 2) // 2
            boundary = (k + 2) * n**k
            lower_sqrt = 2 * genus + boundary + 2
            # For sqrt(p)>lower_sqrt, the monotone quadratic
            # z^2-2g*z+1-b is positive.  Check the endpoint exactly.
            assert lower_sqrt**2 - 2 * genus * lower_sqrt + 1 - boundary > 0
            assert lower_sqrt > genus
            bounds += 1
    print(f"Exact genus, boundary, and positive Hasse--Weil endpoint checks: {bounds}.")

    local = 0
    for p in (2, 3, 5, 7):
        for n in (4, 8, 12, 20, 24):
            a = 0
            m = n
            while m % p == 0:
                a += 1
                m //= p
            depth = 2 * a + 1
            # A finite check on Hensel's exact sufficient inequality,
            # using f(1)=1-(1+p^depth*u), f'(1)=n.
            for u in (1, 2, 3, 5, 11):
                value = -(p**depth) * u
                valuation = 0
                while value % p == 0:
                    valuation += 1
                    value //= p
                assert valuation > 2 * a
                local += 1
    print(f"Exact local n-th-power Hensel input checks: {local}.")
    print("All A.83 finite certificates passed; no giant-prime construction was simulated.")


if __name__ == '__main__':
    main()
