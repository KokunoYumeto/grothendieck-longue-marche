#!/usr/bin/env python3
"""Exact certificates for D.28; no numerical Galois-image assumption.

The actual arithmetic image is proved in D.28 by Kummer theory. This
program independently checks its finite Heisenberg algebra and the full
class-three BCH tame relation used to contradict integral continuity.
"""
import itertools
import json
from collections import deque
from fractions import Fraction
from pathlib import Path

import sympy as s


def bracket(u, v):
    a, b, c, d, e = u
    A, B, C, D, E = v
    return s.Matrix([0, 0, a*B-b*A, a*C-c*A, b*C-c*B])


def bch(u, v):
    uv = bracket(u, v)
    return (u+v+uv/2+(bracket(u, uv)+bracket(v, bracket(v, u)))/12).applyfunc(s.factor)


def ad(u, v):
    return (v+bracket(u, v)+bracket(u, bracket(u, v))/2).applyfunc(s.factor)


def scale(u, q):
    return s.diag(q, q, q**2, q**3, q**3)*u


q, a, b, c, d, e, t, zA, zB = s.symbols('q a b c d e t zA zB')
w = s.Matrix([a, b, c, d, e])
h = s.Matrix([a/(q-1), b/(q-1), 0, 0, 0])
normalized_w = bch(bch(h, w), -scale(h, q))
assert normalized_w[:3, 0] == s.Matrix([0, 0, c])
inertia = s.Matrix([0, t, -a*t/(q-1), zA, zB])
normalized_inertia = ad(h, inertia)
assert normalized_inertia[:3, 0] == s.Matrix([0, t, 0])
assert (bch(bch(h, inertia), -h)-normalized_inertia).applyfunc(s.factor) == s.zeros(5, 1)

wn = s.Matrix([0, 0, c, d, e])
vn = s.Matrix([0, t, 0, zA, zB])
relation = (ad(wn, scale(vn, q))-q*vn).applyfunc(s.factor)
expected = s.Matrix([0, 0, 0, q*(q*q-1)*zA, q*((q*q-1)*zB-c*t)])
assert (relation-expected).applyfunc(s.factor) == s.zeros(5, 1)
solution = relation.subs({zA: 0, zB: c*t/(q*q-1)}).applyfunc(s.factor)
assert solution == s.zeros(5, 1)

# General class-three residue, with the actual class-two tame relation.
aa, bb, cc, uu, vv, dd = s.symbols('a_q b_q c_q u_q v_q d_q')
wv = s.Matrix([uu, vv, dd, 0, 0])
iv = s.Matrix([aa, bb, cc, 0, 0])
rel2 = (q-1)*cc + uu*bb-vv*aa
res_general = (ad(wv, scale(iv, q))-q*iv)/q
R_A = (q+1)*cc*uu/2-dd*aa
R_B = (q+1)*cc*vv/2-dd*bb
assert s.factor(res_general[3]-R_A-uu*rel2/2) == 0
assert s.factor(res_general[4]-R_B-vv*rel2/2) == 0
delta_log = bch(ad(wv, scale(iv, q)), -q*iv)/q
class_two_substitution = {cc: -(uu*bb-vv*aa)/(q-1)}
assert s.factor((delta_log[3]-R_A).subs(class_two_substitution)) == 0
assert s.factor((delta_log[4]-R_B).subs(class_two_substitution)) == 0

P = 5
HALF = 3
zero = (0, 0, 0)


def hm(u, v):
    a, b, c = u
    A, B, C = v
    return ((a+A) % P, (b+B) % P, (c+C+HALF*(a*B-b*A)) % P)


def hi(u):
    return tuple(-x % P for x in u)


def ha(lam, u):
    return (lam*u[0] % P, lam*u[1] % P, lam*lam*u[2] % P)


def gm(u, v):
    x, lam = u
    y, mu = v
    return (hm(x, ha(lam, y)), lam*mu % P)


def gi(u):
    x, lam = u
    il = pow(lam, -1, P)
    return (ha(il, hi(x)), il)


x, y = (1, 0, 0), (0, 1, 0)
seen = {zero}
queue = deque([zero])
while queue:
    v = queue.popleft()
    for g in (x, y, hi(x), hi(y)):
        w = hm(v, g)
        if w not in seen:
            seen.add(w)
            queue.append(w)
assert len(seen) == 125
commutator = hm(hm(hm(x, y), hi(x)), hi(y))
assert commutator == (0, 0, 1)

group = list(itertools.product(sorted(seen), (1, 2, 3, 4)))
target = ((0, 0, 1), 4)
conjugates = {gm(gm(g, target), gi(g)) for g in group}
central_units = set()
for v, lam in conjugates:
    assert lam == 4
    h = (v[0]*pow(lam-1, -1, P) % P,
         v[1]*pow(lam-1, -1, P) % P, 0)
    vnorm, _ = gm(gm((h, 1), (v, lam)), gi((h, 1)))
    assert vnorm[:2] == (0, 0)
    assert vnorm[2] != 0
    central_units.add(vnorm[2])


def val5(n):
    n = abs(n)
    if not n:
        raise ValueError('zero valuation')
    k = 0
    while n % 5 == 0:
        n //= 5
        k += 1
    return k


valuation_checks = []
for r in range(1, 13):
    Q = -1 + 5**r
    den = Q*Q-1
    ratio = Fraction(5**r, den)
    assert val5(den) == r
    assert val5(ratio.numerator) == val5(ratio.denominator) == 0
    valuation_checks.append({'r': r, 'v5_q_plus_1': val5(Q+1),
                             'v5_q_squared_minus_1': val5(den),
                             'divided_inertia_mod5': ratio.numerator*pow(ratio.denominator, -1, 5) % 5})

out = {
    'status': 'all exact assertions passed',
    'basis': ['X', 'Y', '[X,Y]', '[X,[X,Y]]', '[Y,[X,Y]]'],
    'bch_denominators': [2, 12],
    'normalized_frobenius_first_three_coordinates': ['0', '0', 'c'],
    'normalized_inertia_first_three_coordinates': ['0', 't', '0'],
    'tame_relation': [str(x) for x in relation],
    'forced_degree_three_inertia': ['0', 'c*t/(q**2-1)'],
    'general_class_two_tame_relation': str(rel2),
    'general_class_three_residues': [str(R_A), str(R_B)],
    'generated_heisenberg_order': len(seen),
    'commutator_X_Y': commutator,
    'semidirect_order': len(group),
    'target_conjugacy_class_size': len(conjugates),
    'normalized_central_coordinates': sorted(central_units),
    'valuation_checks': valuation_checks,
    'scope': 'Finite algebra and exact symbolic relations only; actual arithmetic finite-image surjectivity and Chebotarev are proved in D.28.'
}
target_path = Path(__file__).with_suffix('.json')
target_path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
