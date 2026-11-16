#!/usr/bin/env python3
"""Exact supporting algebra for D85; no finite-to-infinite inference.

Monic integral ideal reduction checks the actual extra generator and
local relation. The cohomology and infinite natural map are proved in
the adjacent draft. All output is retained for independent replay.
"""
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

x, y = sp.symbols('x y')
INF = 10**6

def vp(a):
    if not a:
        return INF
    n = 0
    while a % 5 == 0:
        n += 1
        a //= 5
    return n

def rem(poly, basis):
    return sp.expand(basis.reduce(sp.Poly(poly, x, y, domain=ZZ).as_expr())[1])

action_rows, relation_rows = [], []
for h in (1, 2, 3):
    N = 5**h
    g = sp.expand((1+y)**N-1)
    assert sp.gcd(x, g) == 1
    # This monic integral basis is exactly y I_L=(xy, y g).
    gb = sp.groebner([x*y, y*g], x, y, domain=ZZ)
    assert all(p.LC() == 1 for p in gb.polys)
    assert rem(x*g, gb) == rem(y*g, gb) == rem(g*g, gb) == 0
    assert rem(g, gb) != 0
    for gamma in (2, 3, 6, 7):
        # Nonconstant multiplier with the actual augmentation gamma².
        # The proof treats arbitrary higher coefficients, not just this sample.
        M = gamma**2+x*(1+y+2*x)+y*(3-x+y)
        sigma_g = sp.expand((1+y)**(N*gamma)-1)
        assert rem(M*sigma_g-gamma**3*g, gb) == 0
        wrong = rem(M*sigma_g-gamma**2*g, gb)
        assert wrong != 0
        assert sp.expand(wrong-(gamma**3-gamma**2)*g) == 0
        action_rows.append({'h': h, 'gamma': gamma,
                            'integral_ideal_remainder': '0',
                            'exact_character': 'gamma^3',
                            'wrong_gamma_squared_detected': True,
                            'Cartier_untwisted_character': 'gamma^2'})
    for lam in (-1, 0, 1, 5):
        for nu in (-1, 0, 2, 5):
            if h == 3 and (lam, nu) not in [(0, -1), (5, 5)]:
                continue
            # Negative exponents: clear only the units1+x and1+g.
            U, V = (1+x)**max(-lam, 0), (1+g)**max(-nu, 0)
            fz = sp.expand((1+x)**max(lam, 0)*(1+g)**max(nu, 0)-U*V)
            fl = sp.expand(((1+x)**max(lam, 0)-U)*V)
            assert rem(fz-fl-nu*g*U*V, gb) == 0
            relation_rows.append({'h': h, 'lambda': lam, 'nu': nu,
                                  'cleared_only_units': True,
                                  'local_relation_remainder': '0'})

# Every ordered basis of F5², with every local lambda residue.
vectors = [(a, b) for a in range(5) for b in range(5)]
boundary = {(a, 0) for a in range(1, 5)}
boundary |= {(0, a) for a in range(1, 5)}
boundary |= {(a, a) for a in range(1, 5)}
counts = {'bases': 0, 'cases': 0, 'epsilon_one': 0,
          'rank_two_span': 0, 'boundary_line': 0}
for u in vectors:
    for r in vectors:
        if (u[0]*r[1]-u[1]*r[0]) % 5 == 0:
            continue
        counts['bases'] += 1
        for lam in range(5):
            z = (lam*u[0] % 5, lam*u[1] % 5)
            rank_two = (r[0]*z[1]-r[1]*z[0]) % 5 != 0
            epsilon = int(not rank_two and r not in boundary)
            assert epsilon == int(lam == 0 and r not in boundary)
            assert rank_two == (lam != 0)
            counts['cases'] += 1
            counts['epsilon_one'] += epsilon
            counts['rank_two_span'] += int(rank_two)
            counts['boundary_line'] += int(not rank_two and r in boundary)
assert counts == {'bases': 480, 'cases': 2400, 'epsilon_one': 240,
                  'rank_two_span': 1920, 'boundary_line': 240}

depth_count = cancellation_count = infinite_count = 0
for boundary_type in range(3):
    for d in [1, 2, 3, 4, INF]:
        t = 0 if d == INF else 5**d
        if boundary_type == 0:
            r, u = (t, 1), (1, 0)
        elif boundary_type == 1:
            r, u = (1, t), (0, 1)
        else:
            r, u = (1, 1+t), (1, 0)
        assert (u[0]*r[1]-u[1]*r[0]) % 5
        for e in [0, 1, 2, 3, 4, 5, 6, INF]:
            lam = 0 if e == INF else 5**e
            for h in (1, 2, 3):
                for nu in (-1, 0, 1, 5):
                    z = tuple(lam*u[j]+5**h*nu*r[j] for j in range(2))
                    rv = [r[0], r[1], r[0]-r[1]]
                    zv = [z[0], z[1], z[0]-z[1]]
                    depths = [min(vp(a), vp(b)) for a, b in zip(rv, zv)]
                    actual = INF if INF in depths else sum(depths)
                    assert actual == min(d, e)
                    depth_count += 1
                    infinite_count += int(actual == INF)
                    if d != INF and e != INF and zv[boundary_type] == 0:
                        cancellation_count += 1
assert cancellation_count > 0 and infinite_count > 0

point = {'t': -799, 'one_minus_t': 800,
         'a_prime_coefficients': {'17': 1, '47': 1},
         'b_prime_coefficients': {'2': 5, '5': 2},
         'away_matrix': [[1, 1, 0], [0, 0, 5]],
         'valuation_vector': [0, 2], 'away_primitive_vector': [1, 0],
         'away_lattice_index': 5,
         'e': vp(799**4-1)-1, 'd': 'infinity',
         'compact_kernel': 'Z5'}
assert sp.isprime(17) and sp.isprime(47)
assert 17*47 == 799 and 2**5*5**2 == 800
smith = smith_normal_form(sp.Matrix(point['away_matrix']), domain=ZZ)
assert list(smith.diagonal()) == [1, 5]
assert point['e'] == 1
point['away_smith_diagonal'] = [int(a) for a in smith.diagonal()]
point['799_fourth_minus_one'] = 799**4-1
point['exact_five_valuation'] = vp(799**4-1)

result = {'status': 'PASS', 'candidate': 'D.85, unregistered',
          'integral_extra_generator_action_rows': action_rows,
          'local_relation_rows': relation_rows,
          'residue_case_partition': counts,
          'depth_case_count': depth_count,
          'exact_cancellation_case_count': cancellation_count,
          'simultaneous_infinite_case_count': infinite_count,
          'extra_generator_Cartier_tame_difference': 2**2-1,
          'actual_point': point,
          'scope': 'Integral polynomial reductions and arithmetic; the all-index cohomology and natural invariant maps are proved in the draft.'}
assert result['extra_generator_Cartier_tame_difference'] % 5

if __name__ == '__main__':
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
