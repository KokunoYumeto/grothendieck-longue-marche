#!/usr/bin/env python3
"""Integral Z_p H1 and H2 from exact saved modular S3 module matrices.

For p=2,3, positive integral S3 cohomology is killed by p.  The exact
coefficient sequence gives
 dim H1(S3,M) = dim (M/p)^S3 - rank M^S3,
 dim H2(S3,M) = dim H1(S3,M/p) - dim H1(S3,M).
The rational invariant rank is recomputed from the integral character
formula; modular invariant ranks are independently recomputed from the
saved two generator matrices, then checked against the saved d0 ranks.
"""
from pathlib import Path
import json
from flint import nmod_mat

BASE = Path(__file__).resolve().parent


def mobius(n):
    sign, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        sign = -sign
    return sign


def trace_lie(n, order):
    def trace_v(d):
        if order == 1 or d % order == 0:
            return 2
        return 0 if order == 2 else -1
    numerator = sum(mobius(d) * trace_v(d) ** (n // d)
                    for d in range(1, n + 1) if n % d == 0)
    assert numerator % n == 0
    return numerator // n


def invariant_rank(n):
    if n == 1:
        return 0
    chars = [trace * trace_lie(n, order) - trace_lie(n + 1, order)
             for order, trace in ((1, 2), (2, 0), (3, -1))]
    numerator = chars[0] + 3 * chars[1] + 2 * chars[2]
    assert numerator % 6 == 0
    return numerator // 6


saved = json.loads((BASE / 'b_modcohom.json').read_text())
saved = {(r['degree'], r['prime']): r for r in saved}
matrices = json.loads((BASE / 'b_modcohom_matrices.json').read_text())
rows = []
for item in matrices:
    n, p = item['degree'], item['prime']
    old = saved[n, p]
    d = old['module_dimension']
    if d:
        eqs = [[item[k][i][j] - int(i == j) for j in range(d)]
               for k in ('r', 's') for i in range(d)]
        generator_rank = nmod_mat(eqs, p).rank()
    else:
        generator_rank = 0
    assert generator_rank == old['d0_rank']
    modular_h0 = d - generator_rank
    rational_h0 = invariant_rank(n)
    integral_h1 = modular_h0 - rational_h0
    integral_h2 = old['H1'] - integral_h1
    assert integral_h1 >= 0 and integral_h2 >= 0
    result = {
        'degree': n, 'prime': p, 'module_dimension': d,
        'rational_invariant_rank': rational_h0,
        'modular_invariant_dimension': modular_h0,
        'integral_H1_Fp_dimension': integral_h1,
        'integral_H2_Fp_dimension': integral_h2,
        'modular_H1_dimension': old['H1'],
        'saved_d0_rank_independently_verified': True,
    }
    rows.append(result)
    print(json.dumps(result), flush=True)
assert all(row['integral_H1_Fp_dimension'] == 0 for row in rows)
output = {
    'status': 'Proved',
    'scope': 'Integral Z_p special outer S3 modules M_n, degrees1..9, p=2,3.',
    'positive_integral_cohomology_killed_by_p': True,
    'cohomology_groups_are_Fp_vector_spaces': True,
    'rows': rows,
    'all_integral_H1_groups_vanish': True,
    'uniform_all_degree_vanishing_claimed': False,
    'method': 'Coefficient long exact sequence; exact modular generator matrices; independently computed rational invariant character ranks.',
}
(BASE / 'g_integral_cohomology.json').write_text(json.dumps(output, indent=2) + '\n')
