#!/usr/bin/env python3
"""Exact support for D88's all-depth cusp calculation.

The finite boundary Smith matrices are independently retained in
pbc_D88_boundary_certificate.py/.json/.out.  This complementary certificate
checks the actual distinguished relation, finite shell functions and their
refinements, integral invariant-measure transition maps, the actual kernel
generator, and the explicit tangential examples.  The infinite/topological
conclusions are proved in the written draft, not inferred from these samples.
"""
from pathlib import Path
import json

import sympy as sp


def valuation(n, p=5):
    n = abs(int(n))
    if not n:
        return None
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def run():
    u, v = sp.symbols('u v')
    w = u + v + u*v
    P = u*v*w
    norm_rows = []
    for N in range(1, 4):
        for r in range(N):
            e = N-r
            qr = (1+u)**(5**r)-1
            qN = (1+u)**(5**N)-1
            F, rem = sp.div(qN, qr, domain=sp.ZZ)
            assert rem == 0
            F = sp.Poly(F, u, domain=sp.ZZ)
            degree = 5**N-5**r
            assert F.degree() == degree and F.LC() == 1
            assert F.nth(0) == 5**e
            assert all(F.nth(j) % 5 == 0 for j in range(degree))
            norm_rows.append({'global_depth': r, 'local_depth': N,
                              'relative_depth': e, 'degree': degree,
                              'constant_term': 5**e,
                              'distinguished_mod_five': True})

    shell_rows = []
    for exponent in range(1, 4):
        coefficient_modulus = 5**exponent
        inverse_two = pow(2, -1, coefficient_modulus)
        for shell in range(3):
            level = shell+exponent
            order = 5**level

            def value(x):
                x %= order
                if valuation(x) != shell:
                    return 0
                return pow(x//(5**shell), -1, coefficient_modulus)

            vals = [value(x) for x in range(order)]
            assert vals[0] == 0 and vals[5**shell] == 1
            assert all(value(2*x) == inverse_two*vals[x] % coefficient_modulus
                       for x in range(order))
            # Pulling this function to the next group-ring quotient gives
            # the same shell formula; no scalar factor is inserted.
            larger_order = 5*order
            for x in range(larger_order):
                if valuation(x) == shell:
                    expected = pow(x//(5**shell), -1, coefficient_modulus)
                else:
                    expected = 0
                assert vals[x % order] == expected
            shell_rows.append({'coefficient_exponent': exponent,
                               'shell': shell, 'finite_level': level,
                               'function_order': coefficient_modulus,
                               'exact_weighted_action': True,
                               'refinement_is_literal_pullback': True})

    # Literal integer pushforward of invariant orbit sums.  This records
    # the divisibility mechanism used to exclude integral Haar measures
    # on every nonzero orbit in the inverse limit.
    transition_rows = []
    for small_level in range(1, 4):
        small_order = 5**small_level
        for refinement in range(1, 4):
            large_level = small_level+refinement
            large_order = 5**large_level
            for shell in range(small_level):
                counts = [0]*small_order
                for x in range(large_order):
                    if valuation(x) == shell:
                        counts[x % small_order] += 1
                expected = [5**refinement if valuation(x) == shell else 0
                            for x in range(small_order)]
                assert counts == expected
                transition_rows.append({'small_level': small_level,
                                        'large_level': large_level,
                                        'nonzero_shell': shell,
                                        'orbit_coefficient_multiplier': 5**refinement})

    actual_zero_rows = []
    for r in range(5):
        qr = sp.expand((1+u)**(5**r)-1)
        Sr, rem = sp.div(qr, u, domain=sp.ZZ)
        assert rem == 0
        assert sp.expand(qr*v*w-P*Sr) == 0
        actual_zero_rows.append({'global_depth': r,
                                 'retained_actual_generator': 'q_r*v*w',
                                 'image_is_P_times_qr_over_u': True})

    # The actual Cartier-untwisted two-jet action for chi=2 is
    # 2*(2+v)*f(2v+v^2), not an arbitrarily assigned diagonal matrix.
    jets = []
    for basis in (sp.Integer(1), v):
        f = sp.expand(2*(2+v)*basis.subs(v, 2*v+v*v))
        jets.append([f.coeff(v, 0), f.coeff(v, 1)])
    M = sp.Matrix.hstack(*[sp.Matrix(c) for c in jets])
    assert M == sp.Matrix([[4, 0], [2, 8]])
    assert (M-sp.eye(2)).det() == 21

    examples = []
    for e in range(13):
        t = 1+5**(e+1)
        assert valuation(t, 2) == 1 and t % 5 == 1
        assert valuation(t**4-1) == e+1
        for r in range(4):
            # The actual rational tangent is t^(5^r).  Its two-valuation
            # is exactly5^r, and the logarithm coefficient is scaled by it.
            examples.append({'base_tangent': t, 'exponent': 5**r,
                             'global_depth': r, 'local_depth': r+e,
                             'relative_depth': e, 'five_valuation': 0})

    lam2 = ((2**4-1)//5)*pow(4, -1, 5) % 5
    lam3 = ((3**4-1)//5)*pow(4, -1, 5) % 5
    assert (lam2, lam3) == (2, 4)
    return {'status': 'PASS', 'candidate': 'D.88, unregistered all-depth draft',
            'distinguished_relative_norms': norm_rows,
            'weighted_shell_functions': shell_rows,
            'literal_invariant_orbit_pushforwards': transition_rows,
            'actual_infinite_kernel_generator': actual_zero_rows,
            'actual_two_jet_matrix': [[int(x) for x in M.row(i)] for i in range(2)],
            'two_jet_difference_determinant': 21,
            'actual_rational_tangents': examples,
            'zero_local_completed_tangent': {'formula': '5^r*(lambda3*kappa2-lambda2*kappa3)',
                                             'lambda2_mod5': lam2, 'lambda3_mod5': lam3},
            'independent_boundary_certificate': 'notes/pbc_D88_boundary_certificate.py/.json/.out',
            'scope': 'Exact supporting finite computations only. The proof establishes the all-depth snake map, transfer exponent, compact topology, and the actual infinite endpoint.'}


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
