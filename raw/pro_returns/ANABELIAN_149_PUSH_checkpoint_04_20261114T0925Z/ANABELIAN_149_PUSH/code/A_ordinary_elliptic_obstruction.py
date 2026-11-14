#!/usr/bin/env python3
"""Exact certificate for A.29a; standard-library arithmetic only.

Curve over F4, c^2+c+1=0:
    y^2+y = s^3+c+c/(s^3+c).
Counts include the smooth normalization's ramified points and infinity.
The two point-count implementations are: an Artin--Schreier trace sum,
and exhaustive enumeration of y.  Polynomial gcds use exact Fractions.
"""

from fractions import Fraction
from itertools import product
from math import prod
from pathlib import Path
import json


def binary_remainder(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


class BinaryField:
    def __init__(self, degree, modulus):
        self.degree = degree
        self.modulus = modulus
        self.q = 1 << degree
        assert modulus.bit_length() == degree + 1
        # Exhaustive trial division proves irreducibility for these d<=8.
        for d in range(1, degree // 2 + 1):
            for candidate in range(1 << d, 1 << (d + 1)):
                assert binary_remainder(modulus, candidate) != 0

    def mul(self, a, b):
        out = 0
        while b:
            if b & 1:
                out ^= a
            b >>= 1
            a <<= 1
            if a >> self.degree:
                a ^= self.modulus
        return out

    def power(self, a, exponent):
        out = 1
        while exponent:
            if exponent & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            exponent >>= 1
        return out

    def trace(self, a):
        out = 0
        for _ in range(self.degree):
            out ^= a
            a = self.mul(a, a)
        assert out in (0, 1)
        return out


def count_points(degree, modulus):
    field = BinaryField(degree, modulus)
    c = next(x for x in range(field.q) if field.mul(x, x) ^ x ^ 1 == 0)
    trace_count = 1  # The unique point over infinity, an odd-order pole.
    exhaustive_count = 1
    finite_poles = 0
    for s in range(field.q):
        denominator = field.power(s, 3) ^ c
        if denominator == 0:
            finite_poles += 1
            trace_count += 1
            exhaustive_count += 1
            continue
        value = denominator ^ field.mul(c, field.power(denominator, field.q - 2))
        trace_count += 2 * (1 - field.trace(value))
        exhaustive_count += sum(
            field.mul(y, y) ^ y == value for y in range(field.q)
        )
    assert trace_count == exhaustive_count
    return {
        "degree_over_F2": degree,
        "modulus_binary": bin(modulus),
        "c_binary": bin(c),
        "count_by_trace": trace_count,
        "count_by_exhaustive_y": exhaustive_count,
        "rational_finite_poles": finite_poles,
    }


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def divide(a, b):
    a, b = list(map(Fraction, trim(a))), list(map(Fraction, trim(b)))
    assert b != [0]
    quotient = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        shift = len(a) - len(b)
        coefficient = a[-1] / b[-1]
        quotient[shift] += coefficient
        for i, value in enumerate(b):
            a[i + shift] -= coefficient * value
        a = trim(a)
    return trim(quotient), a


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def polynomial_gcd(a, b):
    a, b = trim(a), trim(b)
    while b != [0]:
        _, remainder = divide(a, b)
        a, b = b, remainder
    return [x / a[-1] for x in a]


def cyclotomics(maximum):
    out = {}
    for n in range(1, maximum + 1):
        p = [-1] + [0] * (n - 1) + [1]
        for d in range(1, n):
            if n % d == 0:
                p, remainder = divide(p, out[d])
                assert remainder == [0]
        assert all(x.denominator == 1 if isinstance(x, Fraction) else True for x in p)
        out[n] = [int(x) for x in p]
    return out


def phi(n):
    count, value, p = n, n, 2
    while p * p <= value:
        if value % p == 0:
            count -= count // p
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        count -= count // value
    return count


def main():
    rows = [count_points(d, f) for d, f in ((2, 0b111), (4, 0b10011), (6, 0b1000011), (8, 0b100011011))]
    counts = [row["count_by_trace"] for row in rows]
    assert counts == [7, 33, 82, 225]

    # Newton identities plus the genus-four functional equation.
    power_sums = [4**r + 1 - counts[r - 1] for r in range(1, 5)]
    high_coefficients = [1]
    for r in range(1, 5):
        numerator = -sum(high_coefficients[r - j] * power_sums[j - 1] for j in range(1, r + 1))
        assert numerator % r == 0
        high_coefficients.append(numerator // r)
    coefficients = high_coefficients + [0] * 4
    for i in range(4):
        coefficients[8 - i] = 4 ** (4 - i) * coefficients[i]
    assert coefficients == [1, 2, 10, 23, 52, 92, 160, 128, 256]
    # For polynomial arithmetic below, coefficients run from constant upward.
    frobenius = list(reversed(coefficients))
    elliptic = [4, -1, 1]
    remaining = [64, 48, 36, 20, 9, 3, 1]
    assert multiply(elliptic, remaining) == frobenius

    # If phi(m)<=8, every prime p|m has p-1<=8, and hence p is 2,3,5,7.
    # The same inequality bounds their exponents by 4,2,1,1 respectively.
    candidates = {
        2**a * 3**b * 5**c * 7**d
        for a, b, c, d in product(range(5), range(3), range(2), range(2))
    }
    orders = sorted(n for n in candidates if phi(n) <= 8)
    assert orders == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 24, 30]
    cyc = cyclotomics(max(orders))
    scaled = [coefficient * 2**i for i, coefficient in enumerate(frobenius)]
    gcds = {}
    for n in orders:
        value = polynomial_gcd(scaled, cyc[n])
        assert value == [1]
        gcds[str(n)] = 1

    # Exact flex calculation certifying that x(d)=c is a 3-torsion pair.
    field = BinaryField(4, 0b10011)
    c = next(x for x in range(field.q) if field.mul(x, x) ^ x ^ 1 == 0)
    c2 = field.mul(c, c)
    y = next(y for y in range(field.q) if field.mul(y, y) ^ y == c2)
    tangent_slope = y ^ c2
    assert field.mul(tangent_slope, tangent_slope) ^ tangent_slope == c
    # Y=xy+c; tangent Y=(y+c^2)x+c^2 intersects in (x+c)^3.
    assert field.power(c, 3) == 1
    assert field.power(c, 4) ^ c2 == 1

    result = {
        "claim": "A.29a",
        "curve": "y^2+y=s^3+c+c/(s^3+c), c^2+c+1=0 over F4",
        "method": "Exact standard-library finite fields, exhaustive point counts, Newton identities and rational polynomial gcds",
        "point_counts": rows,
        "power_sums": power_sums,
        "frobenius_coefficients_high_to_low": coefficients,
        "factorization": "(X^2-X+4)(X^6+3X^5+9X^4+20X^3+36X^2+48X+64)",
        "all_root_of_unity_orders_with_phi_at_most_8": orders,
        "gcd_of_P_2X_with_cyclotomic": gcds,
        "three_torsion_flex_checked": True,
        "geometric_genus": 4,
        "geometric_p_rank": 3,
        "p_rank_proof": "Regular basis ds and ds/(s-a_i); Cartier kills the first and fixes the three logarithmic forms. See manuscript proof.",
        "conclusion": "No nonconstant map to any positive-dimensional p-rank-zero abelian variety, even over Fbar2; this is an obstruction to one auxiliary-target method, not a counterexample to A1.",
        "all_passed": True,
    }
    output = json.dumps(result, indent=2, sort_keys=True)
    Path(__file__).with_suffix(".json").write_text(output + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
