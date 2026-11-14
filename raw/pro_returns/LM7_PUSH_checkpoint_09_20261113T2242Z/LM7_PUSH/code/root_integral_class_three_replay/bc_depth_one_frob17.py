#!/usr/bin/env python3
"""The actual cyclic-nine Kummer rows at norm-289 Frobenius.

All arithmetic is exact in F_17[theta]/(theta^2-3).  The geometric
comparison and the unramified local Kummer map are proved in B.17.
This program computes the residue symbols, independently reconstructs
the cyclic group-ring polynomial, and verifies the two B.16 rows.
"""
from math import comb
from pathlib import Path
import json

P = 17
ZERO = (0, 0)
ONE = (1, 0)


def add(x, y):
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def neg(x):
    return ((-x[0]) % P, (-x[1]) % P)


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return ((x[0] * y[0] + 3 * x[1] * y[1]) % P,
            (x[0] * y[1] + x[1] * y[0]) % P)


def power(x, n):
    result = ONE
    while n:
        if n & 1:
            result = mul(result, x)
        x = mul(x, x)
        n >>= 1
    return result


def inverse(x):
    assert x != ZERO
    denominator = (x[0] * x[0] - 3 * x[1] * x[1]) % P
    assert denominator != 0
    scale = pow(denominator, -1, P)
    result = ((x[0] * scale) % P, (-x[1] * scale) % P)
    assert mul(x, result) == ONE
    return result


def divide(x, y):
    return mul(x, inverse(y))


assert pow(3, (P - 1) // 2, P) == P - 1
zeta9 = (7, 4)
assert power(zeta9, 9) == ONE and power(zeta9, 3) != ONE
zeta3 = power(zeta9, 3)
assert zeta3 == (8, 15)
assert add(add(ONE, zeta3), power(zeta3, 2)) == ZERO
assert power(zeta9, 17) == inverse(zeta9)

ratios = [(9, 0)]
for j in range(1, 9):
    z = power(zeta9, j)
    ratios.append(divide(neg(z), sub(ONE, z)))

product_ratio = ONE
for r in ratios:
    product_ratio = mul(product_ratio, r)
assert product_ratio == ONE

mu3 = [ONE, zeta3, power(zeta3, 2)]
symbols = [power(r, 96) for r in ratios]
kappa = [mu3.index(symbol) for symbol in symbols]
assert kappa == [j % 3 for j in range(9)]
cusp_coordinates = [(-k) % 3 for k in kappa]

norm_records = []
for j in range(1, 9):
    opposite = (-j) % 9
    r = ratios[j]
    r_opposite = ratios[opposite]
    assert power(r, 17) == r_opposite
    norm = mul(r, r_opposite)
    assert norm[1] == 0 and norm != ZERO and power(norm, 96) == ONE
    quotient = divide(r, r_opposite)
    assert quotient == neg(power(zeta9, j))
    assert power(quotient, 96) == power(zeta3, 2 * j)
    assert (kappa[j] + kappa[opposite]) % 3 == 0
    assert (kappa[j] - kappa[opposite] - 2 * j) % 3 == 0
    norm_records.append({'j': j, 'norm_to_F17': norm[0],
                         'ratio_to_opposite': quotient})

# m(t) = sum c_j t^j, evaluated at t=1+Y.
m = [sum(cusp_coordinates[j] * comb(j, degree)
         for j in range(degree, 9)) % 3
     for degree in range(9)]
assert m == [0, 0, 0, 0, 0, 0, 0, 1, 1]
assert m[0] == 0
h = [(-m[degree + 1]) % 3 for degree in range(8)]
assert h == [0, 0, 0, 0, 0, 0, 2, 2]

rows = [[(-comb(j, degree)) % 3 if j >= degree else 0
         for j in range(9)] for degree in (4, 6)]
assert rows == [[0, 0, 0, 0, 2, 1, 0, 1, 2],
                [0, 0, 0, 0, 0, 0, 2, 2, 2]]
row_values = [sum(r[j] * cusp_coordinates[j] for j in range(9)) % 3
              for r in rows]
assert row_values == [h[3], h[5]] == [0, 0]

# Check every choice of primitive ninth root in this explicit residue field.
embedding_checks = []
for a in (1, 2, 4, 5, 7, 8):
    root9 = power(zeta9, a)
    root3 = power(root9, 3)
    local_mu3 = [ONE, root3, power(root3, 2)]
    local_ratios = [(9, 0)]
    for j in range(1, 9):
        z = power(root9, j)
        local_ratios.append(divide(neg(z), sub(ONE, z)))
    local_kappa = [local_mu3.index(power(r, 96)) for r in local_ratios]
    assert local_kappa == kappa
    embedding_checks.append({'zeta9_exponent': a, 'zeta9': root9,
                              'zeta3': root3, 'kappa': local_kappa})

output = {
    'field': 'F17[theta]/(theta^2-3)',
    'nonresidue_check': {'3^8_mod17': pow(3, 8, 17)},
    'zeta9': zeta9,
    'zeta3': zeta3,
    'arithmetic_Frobenius_residue_degree': 2,
    'arithmetic_Frobenius_norm': 289,
    'cubic_residue_exponent': 96,
    'framed_ratios': ratios,
    'cubic_residue_symbols': symbols,
    'kappa_j_mod3': kappa,
    'c_j_mod3': cusp_coordinates,
    'norm_and_opposite_ratio_checks': norm_records,
    'm_at_1_plus_Y_mod_Y9': m,
    'h_0Y_mod_3_Y8': h,
    'B16_rows': rows,
    'h03_h05': row_values,
    'all_primitive_ninth_root_embeddings': embedding_checks,
    'scope': ('Actual norm-289 arithmetic Frobenius, via the unramified '
              'local Kummer map of B.17; no division of a Frobenius word '
              'and no unspecified path or cube-root adjustment.'),
    'status': 'PASS'
}
encoded = json.dumps(output, indent=2) + '\n'
print(encoded, end='')
Path(__file__).with_suffix('.json').write_text(encoded)
