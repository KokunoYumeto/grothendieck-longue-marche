#!/usr/bin/env python3
"""Exact finite identities used in A.77; not a computation of infinite norms."""
from pathlib import Path
from math import gcd
import sympy as sp

lines = []
def record(s):
    lines.append(s)
    print(s)

group_cases = transition_checks = fixed_element_checks = 0
for ell, exponents in ((3, (1, 2, 3, 4)), (5, (1, 2, 3)),
                       (7, (1, 2)), (11, (1, 2)), (13, (1, 2))):
    for n in exponents:
        m = ell ** n
        phi = m // ell * (ell - 1)
        r = int(sp.primitive_root(m))
        units = {pow(r, j, m) for j in range(phi)}
        assert units == {j for j in range(m) if gcd(j, m) == 1}
        assert gcd(r - 1, m) == 1
        assert {((r - 1) * j) % m for j in range(m)} == set(range(m))
        # The invariant numerator in cyclic H_1(C_phi,C_m) is zero.
        invariants = [j for j in range(m) if (r - 1) * j % m == 0]
        assert invariants == [0]
        fixed_element_checks += m
        # A translation followed by multiplication gives all affine maps,
        # uniquely, as seen already from their values at zero and one.
        affine_images = {(a, (a + u) % m) for a in range(m) for u in units}
        assert len(affine_images) == m * phi
        group_cases += 1
        # The root map j modulo ell*m -> j modulo m commutes with every
        # tested affine action. The module map sends basis vector to basis
        # vector, so these are exact linear equivariance checks.
        higher = ell * m
        for a in (0, 1, ell - 1, higher - 1):
            for u in (1, int(sp.primitive_root(higher)), higher - 1):
                assert gcd(u, higher) == 1
                for j in range(higher):
                    assert ((a + u*j) % higher) % m == (a + u*(j % m)) % m
                    transition_checks += 1

T, a, z, d, alpha = sp.symbols('T a z d alpha')
norm_identities = tower_identities = 0
for m in (3, 5, 7, 9, 11, 13, 25, 27):
    norm = sp.resultant(T**m - a, 1-z*T, T)
    assert sp.expand(norm - (1-a*z**m)) == 0
    norm_identities += 1
for ell in (3, 5, 7, 11, 13):
    norm = sp.resultant(T**ell - d*alpha, 1-z*T, T)
    assert sp.expand(norm - (1-d*alpha*z**ell)) == 0
    # This is the norm transition after alpha_(n+1)^ell=d*alpha_n.
    assert sp.expand(norm.subs({d: 1, z: 1}) - (1-alpha)) == 0
    tower_identities += 1

record('A.77 exact finite certificate: all checks passed.')
record(f'Full affine group and primitive-unit cases: {group_cases}.')
record(f'Cyclic homology invariant-element checks: {fixed_element_checks}.')
record(f'Equivariant root/module transition checks: {transition_checks}.')
record(f'Exact norm polynomial identities: {norm_identities}.')
record(f'Exact compatible radical-tower norm identities: {tower_identities}.')
record('The proof gives Schur-multiplier vanishing, the Hasse norm application, and continuous Shapiro/Kummer comparison.')
record('No compatible infinite norm preimages or full metabelian lift are inferred from these finite checks.')
Path(__file__).with_name('norm_tower_certificate_output.txt').write_text('\n'.join(lines)+'\n')
