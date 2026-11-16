"""Exact Q8 cyclic-eight model and finite-degree Ceresa kernel checks.

The Lie calculation is a finite certificate only, never an all-degree theorem.
All coefficients before Gaussian elimination are integers.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
import sympy as s


def add(a, b, c=1):
    out = dict(a)
    for w, v in b.items():
        out[w] = out.get(w, 0) + c*v
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


letters = [{(i,): 1} for i in range(6)]
Dp, Dm = {}, {}
for i in range(3):
    j, k = (i+1) % 3, (i+2) % 3
    Dp[i], Dp[i+3] = {}, bracket(letters[j], letters[k])
    Dm[i], Dm[i+3] = bracket(letters[j+3], letters[k+3]), {}


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


z, T, W = s.symbols('z T W')
t = (1+s.I*z)/(1-s.I*z)
identity = s.factor((1-t**4)*(1-s.I*z)**4)
assert s.expand(identity-8*s.I*z*(z*z-1)) == 0
assert s.expand(identity**2+64*z*z*(z*z-1)**2) == 0

omega = {}
for i in range(3):
    omega = add(omega, bracket(letters[i], letters[i+3]))
assert not deriv(omega, Dp)
assert not deriv(omega, Dm)

results = []
for n in range(1, 6):
    ws = [w for w in product(range(6), repeat=n) if lyndon(w)]
    cols = []
    for w in ws:
        p = basis(w)
        col = {(0,)+u: c for u, c in deriv(p, Dp).items()}
        col.update({(1,)+u: c for u, c in deriv(p, Dm).items()})
        cols.append(col)
    r = rank(cols)
    row = dict(degree=n, dimension=len(ws), joint_rank_mod_1000003=r,
               joint_kernel_dimension_mod_1000003=len(ws)-r)
    results.append(row)
    print(row, flush=True)

answer = {
    'cyclic8_equation': 'U^8=-64 B(B-1)^2',
    'T_substitution': '(1+i*z)/(1-i*z)',
    'U_substitution': 'W*(1-i*z)',
    'branch_indices': [8, 4, 8],
    'points_above_branch_values': [1, 2, 1],
    'genus': 3,
    'proper_deck_characters': [1, 2, 3, 5, 6, 7],
    'boundary_deck_characters': [0, 0, 4],
    'omega_in_joint_kernel': True,
    'finite_degree_only': results,
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(answer, indent=2)+'\n')
print('Saved', out)
