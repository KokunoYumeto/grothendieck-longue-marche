#!/usr/bin/env python3
"""Exact arithmetic for the supplied formulas only; no manuscript interpretation.

Basis keys (n, e) denote x^[n] (dx)^e, n >= 0 and e in {0,1}.
Multiplication uses binomial(i+j,i), commuting dx, and (dx)^2 = 0.
"""
from math import comb
from pathlib import Path
import json


def clean(terms, modulus=None):
    reduced = {key: (value % modulus if modulus else value)
               for key, value in terms.items()}
    return {key: value for key, value in reduced.items() if value != 0}


def add(left, right, modulus=None):
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, 0) + value
    return clean(result, modulus)


def scale(scalar, value, modulus=None):
    return clean({key: scalar * coeff for key, coeff in value.items()}, modulus)


def multiply(left, right, modulus=None):
    result = {}
    for (i, e), a in left.items():
        for (j, f), b in right.items():
            if e + f >= 2:
                continue
            key = (i + j, e + f)
            result[key] = result.get(key, 0) + a * b * comb(i + j, i)
    return clean(result, modulus)


def serial(value):
    return [{'n': n, 'dx_exponent': e, 'coefficient': c}
            for (n, e), c in sorted(value.items())]


x1, x2, x3, dx = {(1, 0): 1}, {(2, 0): 1}, {(3, 0): 1}, {(0, 1): 1}
f_x1, f_x2, f_x3 = x1, add(x2, dx), x3

a_square = multiply(f_x1, f_x1)
a_twice = scale(2, f_x2)
a_difference = add(a_square, scale(-1, a_twice))
assert a_difference == {(0, 1): -2}

b_product = multiply(f_x1, f_x2, 2)
b_threefold = scale(3, f_x3, 2)
b_difference = add(b_product, scale(-1, b_threefold, 2), 2)
assert b_difference == {(1, 1): 1}

results = {
    'A_over_Z': {
        'f_x1_squared': serial(a_square),
        'two_f_x2': serial(a_twice),
        'difference': serial(a_difference),
        'display': '-2 dx',
    },
    'B_over_F2': {
        'f_x1_times_f_x2': serial(b_product),
        'three_f_x3': serial(b_threefold),
        'difference': serial(b_difference),
        'display': 'x^[1] dx',
    },
}
output = Path(__file__).with_name('supplied_divided_power_arithmetic_results.json')
output.write_text(json.dumps(results, indent=2) + '\n')
print('A over Z: f(x^[1])^2 - 2 f(x^[2]) = -2 dx')
print('B over F2: f(x^[1]) f(x^[2]) - 3 f(x^[3]) = x^[1] dx')
