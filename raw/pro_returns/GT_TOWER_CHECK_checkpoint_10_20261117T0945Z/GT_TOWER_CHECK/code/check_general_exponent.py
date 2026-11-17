#!/usr/bin/env python3
"""Finite certificates for the reconstructed A.66 arithmetic lemmas.

The program checks exact modular images, not an unexecuted Chebotarev search.
The proof of the infinite recursion is in ghost_general_exponent.tex.
"""
from math import factorial, gcd
from sympy import primerange


def vp(a, p):
    assert a != 0
    result = 0
    while a % p == 0:
        result += 1
        a //= p
    return result


def exponent(z, C, n, d):
    result = C * n
    for r in range(2, d + 1):
        result *= z ** r - 1
    return result


def exponent_mod(z, C, n, d, modulus):
    result = C * n % modulus
    for r in range(2, d + 1):
        result = result * (pow(z, r, modulus) - 1) % modulus
    return result


def crt_append(value, modulus, residue, new_modulus):
    assert gcd(modulus, new_modulus) == 1
    adjustment = (residue - value) * pow(modulus, -1, new_modulus)
    return (value + modulus * (adjustment % new_modulus),
            modulus * new_modulus)


image_cases = 0
valuation_cases = 0
power_cases = 0
for d in [2, 3, 4, 6, 8]:
    h = 2 * d * d
    n = factorial(h)
    C = 24 * 25
    D = C * factorial(d) * n ** d
    primes = list(primerange(2, h + 1))
    sample = sorted(set(primes[:5] + primes[-2:]))
    for p in sample:
        v, e = vp(n, p), vp(d, p)
        a = 2 if p == 2 else 1
        W = vp(C, p) + (d + 1) * v + vp(factorial(d), p) + a + e
        assert W <= 2 * vp(D, p)
        precision = 1
        while p ** (precision + 1) <= 128:
            precision += 1
        number = p ** precision
        modulus = p ** (W + precision)
        z0 = 1 + p ** v
        F0 = pow(z0, exponent(z0, C, n, d), modulus)
        observed = set()
        for w in range(number):
            z = 1 + p ** v * (1 + p ** a * w)
            Ez = exponent(z, C, n, d)
            assert vp(z - 1, p) == v
            assert vp(Ez, p) == vp(D, p)
            valuation_cases += 1
            Fz = pow(z, Ez, modulus)
            difference = (Fz - F0) % modulus
            assert difference % (p ** W) == 0
            observed.add(difference // (p ** W))
        assert observed == set(range(number)), (d, p, precision)
        image_cases += 1
        print(f"local image: d={d}, p={p}, v_p(n)={v}, "
              f"W={W}, exact permutation modulo p^{precision}: {number} values")

    P = max(211, h + 3)
    all_primes = list(primerange(2, P + 1))
    values = [0, 0, 0]
    modulus = 1
    for p in all_primes:
        v = vp(n, p)
        a = 2 if p == 2 else 1
        L = 1
        while p ** L <= P:
            L += 1
        if v:
            L = max(L, v + a)
            residues = [1 + p ** v * (1 + p ** a * i) for i in range(3)]
        else:
            allowed = [z for z in range(1, p)
                       if all(pow(z, r, p) != 1 for r in range(2, d + 1))]
            assert len(allowed) >= 3
            residues = allowed[:3]
        new_modulus = p ** L
        next_values = []
        for value, residue in zip(values, residues):
            next_value, combined = crt_append(value, modulus, residue, new_modulus)
            next_values.append(next_value)
        values, modulus = next_values, combined

    for p in all_primes:
        expected_gcd = gcd(D, p - 1)
        images = []
        for value in values:
            e = exponent_mod(value, C, n, d, p - 1)
            assert gcd(e, p - 1) == expected_gcd
            images.append({pow(u, e, p) for u in range(1, p)})
            power_cases += 1
            if n % p:
                forbidden = [u for u in range(1, p)
                             if any(pow(u, r, p) == 1 for r in range(2, d + 1))]
                assert all(pow(u, e, p) == 1 for u in forbidden)
        target = {pow(u, D, p) for u in range(1, p)}
        assert images == [target, target, target]
        if n % p:
            lam = min(target - {1}) if len(target) > 1 else 1
            for value in values:
                e = exponent_mod(value, C, n, d, p - 1)
                assert any(pow(u, e, p) == lam and
                           all(pow(u, r, p) != 1 for r in range(2, d + 1))
                           for u in range(1, p))
    next_D = C * factorial(d) * factorial(h + 1) ** d
    assert all(gcd(next_D, value - 1) == n for value in values)
    print(f"triangular image: d={d}, h={h}, primes <= {P}; "
          "three independent CRT representatives; all exact images and fresh gcd checked")

print(f"PASS: {image_cases} exact local image permutations; "
      f"{valuation_cases} exact exponent valuations; "
      f"{power_cases} finite-field power-image cases.")
print("No complete prime recursion or Chebotarev prime search is claimed as executed.")
