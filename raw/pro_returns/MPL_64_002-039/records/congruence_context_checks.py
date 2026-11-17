#!/usr/bin/env python3
"""Small independent finite checks for context comparisons; no image access.

This checks the explicit equivariant quotient requested in LM 140-2,
scans 568-569, and the mod-4 action of the unipotent in LM 140-3, scan 25.
It does not check the historical manuscript or an infinite congruence theorem.
"""
from itertools import product
from pathlib import Path
import json


def mul(a, b, n):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % n
                 for i in range(2) for j in range(2))


def act(a, v, n):
    return tuple(sum(a[2*i+k]*v[k] for k in range(2)) % n for i in range(2))


def det(a, n):
    return (a[0]*a[3]-a[1]*a[2]) % n


def inv(a, n):
    d = pow(det(a, n), -1, n)
    return tuple((d*x) % n for x in (a[3], -a[1], -a[2], a[0]))


def add(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


J = ((0, 1), (1, 0), (1, 1))
GL2 = [a for a in product(range(2), repeat=4) if det(a, 2) == 1]
sl2 = [a for a in product(range(2), repeat=4) if a[0] == a[3]]


def quotient_class(f):
    return min(f, tuple(x ^ 1 for x in f))


def psi(a):
    """A=[[a,b],[c,a]] maps to [delta_(b,c)]; delta_0 is zero."""
    v = (a[1], a[2])
    return quotient_class(tuple(int(j == v) for j in J))


def permute(g, f):
    gi = inv(g, 2)
    return tuple(f[J.index(act(gi, j, 2))] for j in J)


equivariance_cases = 0
for g in GL2:
    for a in sl2:
        assert psi(mul(mul(g, a, 2), inv(g, 2), 2)) == quotient_class(permute(g, psi(a)))
        equivariance_cases += 1
for a in sl2:
    for b in sl2:
        assert psi(add(a, b)) == quotient_class(add(psi(a), psi(b)))
kernel = [a for a in sl2 if psi(a) == (0, 0, 0)]
assert kernel == [(0, 0, 0, 0), (1, 0, 0, 1)]
assert len({psi(a) for a in sl2}) == 4

# This formula was already supplied by the earlier-run LM_P057api R17 note.
# Confirm that the independently derived psi is the same quotient map.
for a in sl2:
    phi = tuple((v[0]*act(a, v, 2)[1] - v[1]*act(a, v, 2)[0]) % 2 for v in J)
    assert sum(phi) % 2 == 0
    assert quotient_class(phi) == psi(a)


def pm_class(v):
    return min(v, tuple((-x) % 4 for x in v))


primitive = [v for v in product(range(4), repeat=2) if any(x % 2 for x in v)]
vertices = sorted({pm_class(v) for v in primitive})
L = (1, 0, 1, 1)
permutation = {v: pm_class(act(L, v, 4)) for v in vertices}
seen, cycles = set(), []
for v in vertices:
    if v in seen:
        continue
    cycle, w = [], v
    while w not in seen:
        cycle.append(w)
        seen.add(w)
        w = permutation[w]
    cycles.append(cycle)
assert sorted(map(len, cycles)) == [1, 1, 4]
assert permutation[(0, 1)] == (0, 1) and permutation[(2, 1)] == (2, 1)
assert det(L, 4) == 1
assert mul(mul(L, L, 4), mul(L, L, 4), 4) == (1, 0, 0, 1)
assert mul(L, L, 4) != (1, 0, 0, 1)
reduction_action = {j: act(L, j, 2) for j in J}
assert sum(v == reduction_action[v] for v in J) == 1

result = {
    "scope": "Independent finite algebra only; no image inspection and no all-level theorem.",
    "equivariant_quotient": {
        "source": "LM_140-2_text.tex scans568-569(68); cote64 scans027(11),028(16)",
        "prior_formula_attribution": "LM_140-2_notes.md LM_P057api R17, scan569; earlier-run claim, independently verified here",
        "formula": "[[a,b],[c,a]] mod F2.I maps to [delta_(b,c)] in F2^J/F2.diag; delta_0=0",
        "J": J,
        "group_order": len(GL2),
        "trace_zero_matrices": len(sl2),
        "equivariance_cases_checked": equivariance_cases,
        "additivity_cases_checked": len(sl2)**2,
        "earlier_R17_formula_comparison_cases_checked": len(sl2),
        "kernel": kernel,
        "image_order": len({psi(a) for a in sl2}),
        "status": "all assertions passed"
    },
    "unipotent_mod4": {
        "source": "LM_140-3_text.tex scan025(9); cote64 scans033(30)-(32),036(42)-(44)",
        "matrix_row_major": L,
        "primitive_vectors": len(primitive),
        "projective_vertices": vertices,
        "cycles": cycles,
        "opposite_fixed_vertices": [(0, 1), (2, 1)],
        "matrix_order": 4,
        "det_mod4": 1,
        "sign_on_three_mod2_directions": -1,
        "status": "all assertions passed"
    }
}
out = Path(__file__).with_name("congruence_context_checks.json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
