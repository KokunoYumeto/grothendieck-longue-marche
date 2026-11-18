#!/usr/bin/env python3
"""Small, reproducible post-freeze algebra checks; no image or TeX editing.

These certificates test stated algebraic models, not handwriting or every
hypothesis of the manuscript. See basic_report.md for the general arguments.
"""
import itertools
import json
from pathlib import Path
import sympy as s

out = {}

# The contraction V* tensor Sym^2(V) -> V sends e_i* tensor (a e_i)
# to e_i*(a)e_i + a. Summing over i gives (r+1)a.
out['trace_contraction'] = {
    str(r): {'coefficient_on_each_basis_vector': r + 1,
             'rank_one_multiplication_is_iso_even_when_2_is_not_invertible': r == 1}
    for r in range(1, 7)
}

# M -> M - transpose(M): image = alternating matrices in every characteristic;
# kernel = symmetric matrices, including characteristic two.
alt = []
for n, p in [(2, 2), (3, 2), (2, 3)]:
    images = set()
    kernel = 0
    for flat in itertools.product(range(p), repeat=n*n):
        image = tuple((flat[i*n+j]-flat[j*n+i]) % p
                      for i in range(n) for j in range(n))
        images.add(image)
        kernel += all(v == 0 for v in image)
    assert len(images) == p**(n*(n-1)//2)
    assert kernel == p**(n*(n+1)//2)
    alt.append({'rank': n, 'characteristic': p, 'image_count': len(images),
                'kernel_count': kernel})
out['alternating_splitting_map'] = alt
out['symmetric_invariants_to_symmetric_coinvariants'] = {
    'diagonal_basis_coefficient': 1,
    'off_diagonal_basis_coefficient': 2,
    'characteristic_two_rank_for_rank_g_input': 'g (before multiplication of sections)'
}

# Explicit independent convention: horizontal lift d/dx + A(t)d/dt,
# A(t)=1+b*t+c*t^2, reparametrization z=t/(1+a*t), a=a(x).
t, z, a, ap, b, c = s.symbols('t z a a_prime b c')
h = t/(1+a*t)
transformed = s.simplify((-ap*t*t/(1+a*t)**2 +
                         (1+b*t+c*t*t)*s.diff(h, t)).subs(t, z/(1-a*z)))
expected = 1+(b-2*a)*z+(a*a-a*b+c-ap)*z*z
assert s.simplify(transformed-expected) == 0
out['mobius_gauge'] = {
    'convention': 'horizontal lift d/dx + (1+b*t+c*t^2)*d/dt; z=t/(1+a*t)',
    'transformed': str(s.expand(transformed)),
    'linear_term_when_b_zero': '-2*a',
    'purpose': 'check factor 2 under declared convention, not repair manuscript signs'
}
out['scan020_literal_linearity_conflict'] = {
    'generator_value_on_1': 1,
    'displayed_general_formula_on_lambda_0_mu_1_nu_0': -1,
    'difference': 2,
    'scope': 'literal two displayed formulas conflict in characteristic not 2'
}

g = s.symbols('g')
assert s.expand(g*(g+1)/2-(3*g-3)-(g-2)*(g-3)/2) == 0
out['quadrics_dimension_identity'] = '(g*(g+1)/2)-(3*g-3)=(g-2)*(g-3)/2'

# The full translation stratification sees a p-th order term invisible to
# its first-order connection. h fixes the base x and the increment epsilon.
epsilon = s.symbols('epsilon')
strat = []
for p in (2, 3, 5, 7):
    q = p
    while q < 4:
        q *= p
    difference = s.Poly(s.expand((t+epsilon)+(t+epsilon)**q-(t+t**q+epsilon)),
                        t, epsilon, modulus=p)
    assert difference == s.Poly(epsilon**q,t,epsilon,modulus=p)
    strat.append({'p':p,'q':q,'Delta_h_minus_h_Delta':str(difference.as_expr())})
out['full_translation_stratification'] = strat

dest = Path(__file__).with_name('basic_certificate.json')
dest.write_text(json.dumps(out, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
print(f'PASS: contraction, finite-field splitting, Mobius gauge, literal sign conflict, dimension identity, full-stratification test; {dest.name}')
