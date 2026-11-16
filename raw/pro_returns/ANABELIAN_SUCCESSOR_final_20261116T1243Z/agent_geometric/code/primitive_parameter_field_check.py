#!/usr/bin/env python3
"""Standard-library Rabin irreducibility certificate for the explicit field."""
import json
from pathlib import Path

EXPONENTS = (0, 1, 2, 5, 8, 9, 10, 14, 38)
MODULUS = sum(1 << i for i in EXPONENTS)


def remainder(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a


def square_mod(a):
    square = sum(((a >> i) & 1) << (2*i) for i in range(a.bit_length()))
    return remainder(square, MODULUS)


def gcd(a, b):
    while b:
        a, b = b, remainder(a, b)
    return a


if __name__ == "__main__":
    residues = {0: 2}
    for i in range(1,39):
        residues[i] = square_mod(residues[i-1])
    assert residues[38] == 2
    checks = {i: gcd(MODULUS, residues[i] ^ 2) for i in (2,19)}
    assert checks == {2:1,19:1}
    result = {
        "modulus_exponents": EXPONENTS,
        "modulus_binary_integer": MODULUS,
        "rabin_degree": 38,
        "prime_divisors_of_degree": [2,19],
        "X_to_2_power_residues": residues,
        "required_gcds": checks,
        "irreducible": True,
        "parameter_binary_integer": 2,
    }
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
