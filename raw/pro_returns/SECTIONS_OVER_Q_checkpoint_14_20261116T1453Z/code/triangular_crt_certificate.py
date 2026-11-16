"""Exact finite checks for the arithmetic step in the A.59 recursion.

These verify the comparison of exponent maps, not the analytic
Hensel lemma or the Chebotarev existence theorem.
"""
from math import factorial, gcd
from pathlib import Path


def primes_upto(bound):
    return [p for p in range(2, bound + 1)
            if all(p % d for d in range(2, int(p ** 0.5) + 1))]


def valuation(a, p):
    assert a != 0
    k = 0
    while a % p == 0:
        a //= p
        k += 1
    return k


def crt(pairs):
    value, modulus = 0, 1
    for residue, new_modulus in pairs:
        assert gcd(modulus, new_modulus) == 1
        adjustment = ((residue - value) * pow(modulus, -1, new_modulus)) % new_modulus
        value += modulus * adjustment
        modulus *= new_modulus
    return value % modulus, modulus


primes = primes_upto(71)
valuation_checks = 0
gcd_checks = 0
image_checks = 0
fresh_checks = 0
for j in range(7):
    n = factorial(j + 4)
    next_n = factorial(j + 5)
    D = 48 * n * n
    next_D = 48 * next_n * next_n
    choices = {}
    for ell in primes:
        s = valuation(n, ell)
        precision = max(1, s + 1,
                        max(valuation(p - 1, ell) if p > 2 else 0 for p in primes))
        # Extra +1 separates the exact valuation from a lower bound.
        precision += 1
        residue = 1 + ell ** s if s else 2
        assert gcd(residue, ell) == 1
        if not s:
            assert residue % ell not in (0, 1, ell - 1)
        choices[ell] = (residue, ell ** precision)

    q, full_modulus = crt([choices[ell] for ell in primes])
    assert (q - 1) % n == 0
    exponent = 24 * n * (q*q - 1)
    assert exponent % D == 0
    for ell in primes:
        assert valuation(exponent, ell) == valuation(D, ell)
        valuation_checks += 1
    assert n % gcd(next_D, q - 1) == 0
    fresh_checks += 1

    for p in primes:
        assert gcd(exponent, p - 1) == gcd(D, p - 1)
        gcd_checks += 1
        if n % p == 0:
            continue
        base, lower_modulus = crt([choices[ell] for ell in primes if ell < p])
        assert lower_modulus % (p - 1) == 0
        residues = set()
        noncritical_residues = set()
        fixed_exponent = (24*n*(base*base-1)) % (p-1)
        for unit in range(1, p):
            lift = base + lower_modulus * (((unit-base)*pow(lower_modulus, -1, p)) % p)
            ee = 24*n*(lift*lift-1)
            assert ee % (p-1) == fixed_exponent
            value = pow(unit, ee, p)
            residues.add(value)
            if unit not in (1, p-1):
                noncritical_residues.add(value)
        desired = {pow(unit, D, p) for unit in range(1, p)}
        assert residues == desired
        if len(desired) == 1:
            assert 1 in noncritical_residues
        else:
            assert (desired - {1}) <= noncritical_residues
        image_checks += 1

output = (
    f"Exact minimal exponent valuations: {valuation_checks} passed.\n"
    f"gcd(E,p-1)=gcd(D,p-1): {gcd_checks} passed.\n"
    f"Triangular CRT power-image and noncritical common-value checks: {image_checks} passed.\n"
    f"Fresh-prime gcd(D_next,q-1) divides n: {fresh_checks} passed.\n"
    "All tested CRT classes are units and are 1 modulo the current factorial n.\n"
)
Path(__file__).with_name("triangular_crt_certificate_output.txt").write_text(output)
print(output, end="")
