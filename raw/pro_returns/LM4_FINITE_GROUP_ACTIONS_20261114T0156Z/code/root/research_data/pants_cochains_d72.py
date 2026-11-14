#!/usr/bin/env python3
"""Exact finite cochain, support and matrix identities used in D.72.

The full continuous cohomology comparison and the existence of the lifted
defining systems are proved in d72.tex. Finite checks do not replace them.
"""
from collections import Counter
from pathlib import Path
import itertools
import json

COUNTS = Counter()


def check(label, value):
    assert value, label
    COUNTS[label] += 1


def matrix_product(a, b):
    return [[sum(x*y for x, y in zip(row, col)) % 2
             for col in zip(*b)] for row in a]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def cochain(i, args):
    # Quotient coordinates are (u, xi_x, xi_y), encoded by bits 0,1,2.
    vertices = (1, 3, 5)
    return int(bool(args) and all(g == vertices[i] for g in args))


def differential(i, args):
    # Characteristic-two normalized inhomogeneous differential on C2^3.
    value = cochain(i, args[1:]) ^ cochain(i, args[:-1])
    for k in range(len(args)-1):
        merged = args[:k]+(args[k] ^ args[k+1],)+args[k+2:]
        value ^= cochain(i, merged)
    return value


def allowed_tuples(n, prefix=()):
    if len(prefix) == n:
        yield prefix
        return
    for mask in range(8):
        if not prefix or not (prefix[-1] & mask):
            yield from allowed_tuples(n, prefix+(mask,))


def main():
    restriction = [[1, 1, 1], [0, 1, 0], [0, 0, 1]]
    inverse_basis = [[1, 1, 1], [0, 1, 0], [0, 0, 1]]
    check('restriction_matrix_inverse',
          matrix_product(inverse_basis, restriction) == identity(3))
    for coefficients in itertools.product(range(2), repeat=3):
        evaluations = tuple(sum(coefficients[i]*restriction[i][j]
                                for i in range(3)) % 2 for j in range(3))
        restored = tuple(sum(evaluations[i]*inverse_basis[i][j]
                             for i in range(3)) % 2 for j in range(3))
        check('all_character_values', restored == coefficients)
    for a, b in itertools.product(range(8), repeat=2):
        pointwise = sum((((a >> i) & 1)*((b >> i) & 1)) << i
                        for i in range(3))
        check('boolean_support_products', pointwise == (a & b))

    vertices = (1, 3, 5)
    for degree in range(1, 17):
        for i, j in itertools.product(range(3), repeat=2):
            check('finite_quotient_cochain_sections',
                  cochain(i, (vertices[j],)*degree) == int(i == j))
            check('restricted_differential',
                  differential(i, (vertices[j],)*(degree+1)) == 0)
        for i in range(3):
            for position in range(degree):
                args = [vertices[i]]*degree
                args[position] = 0
                check('normalization', cochain(i, tuple(args)) == 0)
    for a, b in itertools.product(range(1, 7), repeat=2):
        for i, j, k in itertools.product(range(3), repeat=3):
            actual = (cochain(i, (vertices[k],)*a)
                      *cochain(j, (vertices[k],)*b))
            expected = int(i == j == k)
            check('restricted_cup_products', actual == expected)

    fibonacci = [0, 1]
    for _ in range(42):
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
    transfer = [1]*8
    image_counts = []
    for n in range(1, 41):
        if n > 1:
            transfer = [sum(transfer[previous] for previous in range(8)
                            if not (previous & current))
                        for current in range(8)]
        actual_count = sum(transfer)
        check('eight_state_transfer_counts', actual_count == fibonacci[n+2]**3)
        image_counts.append({'n': n, 'tuples': actual_count,
                             'fibonacci_cube': fibonacci[n+2]**3})
    enumerated = []
    for n in range(1, 7):
        count = 0
        for masks in allowed_tuples(n):
            count += 1
            for section in range(3):
                mat = identity(n+1)
                for j, mask in enumerate(masks):
                    mat[j][j+1] = (mask >> section) & 1
                check('actual_section_matrix_squares',
                      matrix_product(mat, mat) == identity(n+1))
        check('enumerated_character_tuple_counts', count == fibonacci[n+2]**3)
        enumerated.append({'n': n, 'tuples': count})
    result = {
        'claim': 'D.72', 'status': 'PASS',
        'restriction_matrix': restriction,
        'inverse_basis': inverse_basis,
        'finite_quotient_section_values': vertices,
        'enumerated_counts': enumerated,
        'transfer_counts': image_counts,
        'checks': dict(COUNTS), 'total_checks': sum(COUNTS.values()),
        'scope': 'Finite identities for the displayed section restrictions, '
                 'Boolean support multiplication, normalized cochain lifts, '
                 'Fibonacci count, and actual upper unitriangular section '
                 'matrices. Full continuous cohomology and representation '
                 'existence are proved by the explicit acyclic-kernel argument.'
    }
    Path(__file__).with_name('pants_cochains_d72_output.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in
                     ['claim', 'status', 'enumerated_counts', 'checks',
                      'total_checks', 'scope']}, indent=2))


if __name__ == '__main__':
    main()
