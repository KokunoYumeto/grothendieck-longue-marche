#!/usr/bin/env python3
"""Small exact certificate for AG.35, not a fixed-ell tower assertion."""
import json
from pathlib import Path


def polynomial_remainder(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def polynomial_gcd(a, b):
    while b:
        a, b = b, polynomial_remainder(a, b)
    return a


def factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


class BinaryField:
    def __init__(self, degree, modulus):
        self.degree, self.modulus = degree, modulus
        self.q = 1 << degree
        assert modulus.bit_length() == degree + 1
        z = 2
        for i in range(1, degree + 1):
            z = self.mul(z, z)
            if i <= degree // 2:
                assert polynomial_gcd(z ^ 2, modulus) == 1
        assert z == 2

    def mul(self, a, b):
        out = 0
        while b:
            if b & 1:
                out ^= a
            b >>= 1
            a <<= 1
            if a & self.q:
                a ^= self.modulus
        return out

    def power(self, a, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out

    def trace(self, a):
        out, z = 0, a
        for _ in range(self.degree):
            out ^= z
            z = self.mul(z, z)
        assert out in (0, 1)
        return out


records = []
for m, modulus in [(1, 7), (3, 67), (5, 1033)]:
    k = BinaryField(2 * m, modulus)
    traces = [k.trace(x) for x in range(k.q)]
    inverse_squares = [0] + [k.power(x, k.q - 3) for x in range(1, k.q)]
    trials = []
    for a in range(1, k.q):
        count = 2 + 2 * sum(
            traces[x ^ k.mul(a, inverse_squares[x])] == 0
            for x in range(1, k.q)
        )
        trials.append([a, count])
        if count == k.q:
            break
    else:
        raise AssertionError("Trace-one parameter not found")
    orbit, z = [], a
    while z not in orbit:
        orbit.append(z)
        z = k.power(z, 4)
    assert z == a and len(orbit) == m
    order = k.q - 1
    for prime in factors(order):
        while order % prime == 0 and k.power(a, order // prime) == 1:
            order //= prime
    assert order % 2 == 1 and k.power(a, order) == 1
    direct_count = None
    if m <= 3:
        direct_count = 1 + sum(
            (k.mul(y, y) ^ k.mul(x, y)) == (k.power(x, 3) ^ a)
            for x in range(k.q) for y in range(k.q)
        )
        assert direct_count == count
    bits = 2 * m + 4
    beta = 1
    for b in range(1, bits):
        if (beta * beta - beta + k.q) % (1 << (b + 1)):
            beta += 1 << b
        assert (beta * beta - beta + k.q) % (1 << (b + 1)) == 0
    diff = beta - 1
    valuation = (diff & -diff).bit_length() - 1
    assert valuation == 2 * m
    records.append({
        "m": m, "q": k.q, "binary_modulus": modulus,
        "parameter_binary_encoding": a, "parameter_order": order,
        "fourth_power_orbit": orbit, "point_count": count,
        "independent_direct_point_count": direct_count,
        "frobenius_polynomial_descending": [1, -1, k.q],
        "unit_root_modulus": 1 << bits, "unit_root_residue": beta,
        "v2_unit_root_minus_one": valuation,
        "all_parameter_trials": trials,
    })

out = {
    "claim": "AG.35",
    "scope": "Fixed geometric elliptic family; not a fixed-ell-primary torsion sequence or an Abel tower.",
    "all_checks_passed": True,
    "examples": records,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
