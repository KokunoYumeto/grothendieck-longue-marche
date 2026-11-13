#!/usr/bin/env python3
"""Exact integral and tangential certificates for B.36.

This reads the actual modular-extension cocycle constructed in B.24a.
The arithmetic realization is proved in the manuscript from Kummer
covers; finite automorphisms alone are not treated as source lifts.
"""
from pathlib import Path
from itertools import product
from math import gcd
import hashlib
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
source = HERE / 'g_signed_fermat2_model.json'
raw = source.read_bytes()
d = json.loads(raw)
reps = d['representatives']
mul_h = d['multiplication']
coc = d['cocycle']
acts = d['actions']
hi, hr, hs = (reps.index(w) for w in ([], [1], [2]))
he = mul_h[hs][hr]
R, S = (sp.Matrix(acts[h]) for h in (hr, hs))
I = sp.eye(5)
J = S * R
Y = (R * S) ** 2
P = sp.Matrix(d['projection_linear'])
w = sp.Matrix([-1, 1, 0, 1, 0])
v = sp.Matrix([-1, 1, 1, 1, -1])
boundary = [sp.Matrix(a) for a in d['peripheral_vectors']]

assert R ** 3 == S ** 2 == I
assert (J - I).nullspace() == [sp.Matrix([1, 0, 0, 0, 0]),
                              sp.Matrix([0, 1, 0, 1, 0])]
assert sp.Matrix.vstack(J - I, P).nullspace() == [w]
assert sp.Matrix.vstack(R - I, S - I).rank() == 5
assert (I - R) * w == (I - S) * w == v
assert Y * w == -w
assert P * w == sp.zeros(2, 1)
assert boundary[1] - boundary[0] == w
B = sp.Matrix.hstack(*boundary)
assert B.rank() == 5 and sum(boundary, sp.zeros(5, 1)) == sp.zeros(5, 1)
assert B[:, :5].det() in (-1, 1)
assert d['peripheral_permutations'][he] == [0, 1, 4, 5, 3, 2]
assert sp.Matrix(acts[he]) == J

# This is an integral cocycle, with no divisions by |H48| in the output.
delta = [(I - sp.Matrix(A)) * w for A in acts]
integral_cocycle_checks = 0
for h, k in product(range(48), repeat=2):
    assert delta[mul_h[h][k]] == delta[h] + sp.Matrix(acts[h]) * delta[k]
    integral_cocycle_checks += 1
assert delta[he] == sp.zeros(5, 1)
assert all(P * z == sp.zeros(2, 1) for z in delta)

def mv(A, z):
    return tuple(sum(a * b for a, b in zip(row, z)) for row in A)

# The finite reductions are checked as actual affine automorphisms of the
# 48-component group, for every element and both generating edges.
finite = []
for n in (2, 3, 4):
    zero = (0,) * 5
    def mul(a, b):
        h, av = a
        k, bv = b
        ab = mv(acts[h], bv)
        return (mul_h[h][k],
                tuple((av[j] + ab[j] + coc[h][k][j]) % n for j in range(5)))
    def action(a, t):
        h, av = a
        return h, tuple((av[j] + t * int(delta[h][j])) % n for j in range(5))
    generators = [(hr, zero), (hs, zero)]
    elements = [(h, v0) for h in range(48)
                for v0 in product(range(n), repeat=5)]
    checks = 0
    for t in range(n):
        # Injectivity follows already from translation on each component.
        assert len({action(a, t) for a in elements}) == len(elements)
        for a in elements:
            for b in generators:
                assert action(mul(a, b), t) == mul(action(a, t), action(b, t))
                checks += 1
    # The primitive first coordinate of the rho discrepancy measures t.
    rho_discrepancies = {tuple(t * int(z) % n for z in delta[hr])
                         for t in range(n)}
    assert len(rho_discrepancies) == n
    for t, s in product(range(n), repeat=2):
        for a in generators:
            assert action(action(a, t), s) == action(a, (t + s) % n)
    finite.append({'modulus': n, 'group_order': len(elements),
                   'inner_line_order': n,
                   'all_elements_two_generator_edge_checks': checks})

# Actual degree-four Fermat cover and its two tangential endpoints.
T, eps = sp.symbols('T eps')
u = 2 * T / (1 + T**2)
vv = (1 - T**2) / (1 + T**2)
z = 4 * T**2 / (1 + T**2)**2
assert sp.cancel(u**2 + vv**2 - 1) == 0
assert sp.cancel(u**2 - z) == 0
assert sp.cancel(u.subs(T, 1/T) - u) == 0
assert sp.cancel(vv.subs(T, 1/T) + vv) == 0
assert sp.limit(z.subs(T, eps/2) / eps**2, eps, 0) == 1
assert sp.limit(z.subs(T, 2/eps) / eps**2, eps, 0) == 1
punctures = [sp.Integer(0), sp.Integer(1), -sp.Integer(1), sp.I, -sp.I]
expected = [4, -2, 2, 2*sp.I, -2*sp.I]
exponents = [2, 1, 1, 1, 1]
ratios = []
for a, expect, exponent in zip(punctures, expected, exponents):
    f = T - a
    initial = (sp.limit(f.subs(T, eps/2) / eps, eps, 0)
               if a == 0 else sp.limit(f.subs(T, eps/2), eps, 0))
    terminal = sp.limit(eps * f.subs(T, 2/eps), eps, 0)
    ratio = sp.simplify(terminal / initial)
    assert ratio == expect
    root = sp.simplify(ratio / 2**exponent)
    assert root**4 == 1
    ratios.append({'function': str(f), 'initial_regularized_value': str(initial),
                   'terminal_regularized_value': str(terminal),
                   'endpoint_ratio': str(ratio), 'kummer2_exponent': exponent,
                   'cyclotomic_factor': str(root)})

# Positive boundary classes b_0,b_infty have pairing vectors e_0,-ones
# against the five Kummer covers (T-a)^(1/m).  The original x,y meridians
# are negative, so w=[y x^2 y^-1]-[x^2]=b_0-b_infty.
positive_pairing_b0 = sp.Matrix([1, 0, 0, 0, 0])
positive_pairing_binf = -sp.ones(5, 1)
assert positive_pairing_b0 - positive_pairing_binf == sp.Matrix(exponents)
assert (I - Y) * w == 2*w

out = {
 'status': 'Proved', 'statement': 'B.36',
 'integral_model_input': source.name,
 'integral_model_sha256': hashlib.sha256(raw).hexdigest(),
 'R': R.tolist(), 'S': S.tolist(), 'e0_action': J.tolist(),
 'projection_linear': P.tolist(),
 'e0_fixed_rank': 2, 'e0_fixed_projection_kernel_rank': 1,
 'global_fixed_rank': 0, 'primitive_kernel_generator': list(w),
 'rho_sigma_coboundary': list(v), 'y_action_on_generator': -1,
 'boundary_span_unimodular_minor': int(B[:, :5].det()),
 'e0_boundary_permutation': d['peripheral_permutations'][he],
 'e0_boundary_cycle_type': [1, 1, 4],
 'integral_cocycle_identities_checked': integral_cocycle_checks,
 'finite_actual_group_checks': finite,
 'fermat_cover': {'u': str(u), 'v': str(vv), 'z': str(z),
   'initial_T': 'eps/2', 'terminal_T': '2/eps',
   'both_pushforward_leading_z_values': 'eps^2',
   'y_deck_transformation': 'T -> 1/T'},
 'tangential_kummer_coordinates': ratios,
 'positive_boundary_kummer_pairing': exponents,
 'arithmetic_relation_on_cyclotomic_kernel':
     '2 theta(g) = epsilon_path kappa_2(g), with one fixed global sign',
 'exact_D0_image': 'Zhat times w, realized by the actual arithmetic subgroup',
 'exact_D_image': 'Zhat semidirect E_2, E_2={(k,mu): k mod2=(mu_2^2-1)/8 mod2}',
 'group_law': '(r,k,mu)(s,l,nu)=(r+mu*s,k+mu*l,mu*nu)',
 'scope': 'The abelian-kernel stage C/K_2_prime only. Arithmetic realization is the tangential Kummer proof, not inferred from finite shadows.'
}
def serial(a):
    if isinstance(a, sp.Integer):
        return int(a)
    raise TypeError(type(a).__name__)
payload = json.dumps(out, indent=2, default=serial) + '\n'
(HERE / 'g_fermat2_source.json').write_text(payload)
(HERE / 'g_fermat2_source.out').write_text(payload)
print(payload)
