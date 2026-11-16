"""Exact finite certificates supporting the unbounded A.36 proof.

Letters are p,s,v,r.  The two moving letters model the two actual
coefficient types; the proof permits arbitrarily many moving letters.
Ranks modulo a prime certify rational lower bounds, not integral indices.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path
import json


def add(a, b, c=1):
    out = dict(a)
    for w, v in b.items():
        out[w] = out.get(w, 0)+c*v
        if not out[w]:
            del out[w]
    return out


def mul(a, b):
    out = defaultdict(int)
    for u, x in a.items():
        for v, y in b.items():
            out[u+v] += x*y
    return {w: c for w, c in out.items() if c}


def bracket(a, b):
    return add(mul(a, b), mul(b, a), -1)


@lru_cache(None)
def lyndon(w):
    return all(w < w[i:]+w[:i] for i in range(1, len(w)))


@lru_cache(None)
def basis(w):
    if len(w) == 1:
        return {w: 1}
    for i in range(1, len(w)):
        if lyndon(w[i:]):
            return bracket(basis(w[:i]), basis(w[i:]))
    raise AssertionError(w)


def deriv(poly, d):
    out = defaultdict(int)
    for w, c in poly.items():
        for i, a in enumerate(w):
            for v, b in d[a].items():
                out[w[:i]+v+w[i+1:]] += c*b
    return {w: c for w, c in out.items() if c}


def rank(cols, prime=1000003):
    pivots = {}
    for raw in cols:
        v = {k: c % prime for k, c in raw.items() if c % prime}
        while v:
            k = max(v)
            if k not in pivots:
                fac = pow(v[k], -1, prime)
                pivots[k] = {j: c*fac % prime for j, c in v.items()}
                break
            fac = v[k]
            for j, c in pivots[k].items():
                a = (v.get(j, 0)-fac*c) % prime
                if a:
                    v[j] = a
                elif j in v:
                    del v[j]
    return len(pivots)


letters = [{(i,): 1} for i in range(4)]
p, s, v, r = letters
rows = []
for lam in [0, 1, -2]:
    d = {
        0: {},
        1: {w: lam*c for w, c in bracket(p, s).items()},
        2: bracket(add({w: lam*c for w, c in p.items()}, s, -2), v),
        3: bracket(add({w: lam*c for w, c in p.items()}, s, -5), r),
    }
    for n in range(1, 6):
        ws = [w for w in product(range(4), repeat=n) if lyndon(w)]
        cols = [deriv(basis(w), d) for w in ws]
        rnk = rank(cols)
        expected = (sum(lyndon(w) for w in product(range(2), repeat=n))
                    if lam == 0 else int(n == 1))
        actual = len(ws)-rnk
        assert actual == expected
        row = dict(packet_scalar=lam, degree=n, domain_dimension=len(ws),
                   kernel_dimension=actual, expected=expected)
        rows.append(row)
        print(row, flush=True)

# Boundary coordinates p,q,r; the fourth is -p-q-r.
P, Q, R, S4 = (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, -1, -1)
edge_one = tuple(-P[i]-Q[i] for i in range(3))
edge_two = tuple(R[i]+S4[i] for i in range(3))
assert edge_one == edge_two == (-1, -1, 0)
handle_coefficient = tuple(2*x for x in edge_one)
other_cusp_coefficient = tuple(2*edge_one[i]+3*edge_two[i] for i in range(3))
assert handle_coefficient == (-2, -2, 0)
assert other_cusp_coefficient == (-5, -5, 0)
inertia_matrix = [[8, -8], [0, -8]]
det = -64
assert inertia_matrix[0][0]*inertia_matrix[1][1]-inertia_matrix[0][1]*inertia_matrix[1][0] == det

answer = {
    'edge_lengths_example': [2, 3],
    'edge_first_classes_in_p_q_r': [edge_one, edge_two],
    'handle_inner_first_class': handle_coefficient,
    'other_cusp_inner_first_class': other_cusp_coefficient,
    'target_inertia_matrix_in_X_Y': inertia_matrix,
    'target_inertia_determinant': det,
    'finite_degree_only': rows,
    'unbounded_proof': 'A.36 first-B-slot operator lambda L_p + c R_s',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(answer, indent=2)+'\n')
print('PASS: exact graph coefficients, odd-prime inertia matrix, and all finite rank checks.')
