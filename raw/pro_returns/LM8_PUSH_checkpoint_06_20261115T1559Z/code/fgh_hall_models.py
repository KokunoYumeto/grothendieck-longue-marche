#!/usr/bin/env python3
"""Exact characteristic-two obstructions for specified class-two models.

The rank-five matrix is taken from the already rechecked integral q2
cocycle output. This is a negative test of the naive Hall group scheme,
not an assertion that it is the actual relative integral completion.
"""
from itertools import combinations, product
from pathlib import Path
import json
from fgh_additive_lifts import f, ra, rm


def hall_product(g, h, n=5):
    v, z = g
    w, t = h
    return (tuple(a ^ b for a, b in zip(v, w)),
            tuple(a ^ b ^ (v[i] & w[j])
                  for a, b, (i, j) in zip(z, t, combinations(range(n), 2))))


def deformed_heisenberg(g, h, parameter):
    a, b, c = g
    d, e, z = h
    return ra(a, d), ra(b, e), ra(ra(c, z), rm(parameter, rm(a, e)))


def main():
    model = json.loads(Path(__file__).with_name('fgh_q2_recheck_model.json').read_text())
    assert model['representatives'][1] == [1]
    assert model['quotient_matrices_mod4'][1] == [0, 1, 3, 1]
    rho = model['actions'][1]
    column = tuple(rho[i][1] & 1 for i in range(5))
    assert column == (1, 0, 0, 1, 0)
    zero_c = (0,) * 10
    e2 = (0, 1, 0, 0, 0)
    assert hall_product((e2, zero_c), (e2, zero_c)) == ((0,) * 5, zero_c)
    pairs = list(combinations(range(5), 2))
    expected_square = tuple(int(pair == (0, 3)) for pair in pairs)
    tested = 0
    for center in product(range(2), repeat=10):
        assert hall_product((column, center), (column, center)) == ((0,) * 5, expected_square)
        tested += 1
    # H_2 reduces to the additive group in characteristic two, so the
    # same coordinatewise f is an automorphism. Check all generating
    # coordinate pairs over the 16-element ring, enough by additivity.
    coordinate_checks = 0
    for i, j, a, b in product(range(3), range(3), range(16), range(16)):
        g = tuple(a if k == i else 0 for k in range(3))
        h = tuple(b if k == j else 0 for k in range(3))
        lhs = tuple(f(z) for z in deformed_heisenberg(g, h, 0))
        rhs = deformed_heisenberg(tuple(map(f, g)), tuple(map(f, h)), 0)
        assert lhs == rhs
        coordinate_checks += 1
    result = {
        'hall_model': 'rank-five Hall class-two group over F2, center wedge^2 F2^5',
        'rho_matrix': rho,
        'source_vector': [0, 1, 0, 0, 0],
        'source_square': [0] * 10,
        'rho_vector': list(column),
        'every_lift_square': list(expected_square),
        'wedge_basis_one_based': [[i + 1, j + 1] for i, j in pairs],
        'all_central_lifts_tested': tested,
        'rho_lift_exists': False,
        'two_integral_models': {
            'law': '(a,b,c)*(d,e,z)=(a+d,b+e,c+z+t*a*e)',
            'parameters_over_Z': [1, 2],
            'generic_fibre_isomorphism_H2_to_H1': '(a,b,c) -> (a,b,c/2)',
            'same_abelian_projection': '(a,b,c) -> (a,b)',
            'H1_mod2_nonlinear_lift': False,
            'H2_mod2_nonlinear_lift': True,
            'H2_coordinate_checks_over_F4_dual_numbers': coordinate_checks,
        },
        'scope': 'The naive Hall modular model is impossible at 2; generic fibre and first abelian quotient do not determine the nonlinear-lift answer.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
