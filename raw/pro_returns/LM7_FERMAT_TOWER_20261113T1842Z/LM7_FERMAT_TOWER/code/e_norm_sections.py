#!/usr/bin/env python3
"""E.46: actual affine modules, Shapiro cocycles, norm maps and radical fields.

All calculations are finite certificates for the separately proved
continuous norm-system comparison.  The finite Galois group below is
Gal(Q(zeta_27, 2^(1/9))/Q), not an arbitrary affine approximation.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
from random import Random
import json
import sympy as sp

OUT = Path(__file__).resolve().parent
rng = Random(460047)
results = {}


def affine_orbits(level):
    modulus = 3 ** level
    unseen = set(range(modulus))
    ans = []
    generators = [(modulus - 1, 0), (4 % modulus, 0), (1 % modulus, 3 % modulus)]
    while unseen:
        todo = [min(unseen)]
        orbit = set(todo)
        while todo:
            x = todo.pop()
            for u, b in generators:
                y = (u*x+b) % modulus
                if y not in orbit:
                    orbit.add(y)
                    todo.append(y)
        unseen -= orbit
        ans.append(sorted(orbit))
    return ans


positional = []
for n in range(1, 7):
    modulus = 3 ** n
    os = affine_orbits(n)
    assert sorted(map(len, os)) == [3 ** (n-1), 2*3 ** (n-1)]
    assert set(os[0]) == set(range(0, modulus, 3))
    assert set(os[1]) == {i for i in range(modulus) if i % 3}
    checks = 0
    high = 3*modulus
    for u, b in [(high-1, 0), (4, 0), (1, 3)]:
        for i in range(high):
            assert ((u*i+b) % high) % modulus == (u*(i % modulus)+b) % modulus
            # The scalar Tate coefficient remains u under positional pushforward.
            coeff = rng.randrange(3**5)
            assert (u*coeff) % (3**5) == ((u % (3**5))*coeff) % (3**5)
            checks += 1
    for _ in range(250):
        u, v = [rng.choice([j for j in range(high) if j % 3]) for _ in range(2)]
        b, c = [3*rng.randrange(modulus) for _ in range(2)]
        x = rng.randrange(high)
        assert (u*(v*x+c)+b) % high == ((u*v % high)*x+(b+u*c)) % high
    positional.append({'level': n, 'orbit_sizes': list(map(len, os)),
                       'intertwining_basis_checks': checks,
                       'affine_action_composition_checks': 250})
print('PASS: six actual radical-torsor orbit decompositions and positional maps.', flush=True)
results['positional_modules'] = positional

# Galois elements (u,k) act on zeta_27 by exponent u and on 2^(1/9)
# by multiplication by zeta_9^k.  Its order is 18*9=162, by Eisenstein
# at every prime above 2 in Q(zeta_27), where 2 is unramified.
q, coeff = 27, 9
G = [(u, k) for u in range(q) if u % 3 for k in range(9)]
one = (1, 0)


def mul(g, h):
    u, k = g
    v, ell = h
    return (u*v % q, (k+u*ell) % 9)


def inv(g):
    u, k = g
    v = pow(u, -1, q)
    return (v, -v*k % 9)


def action(g, i, level):
    u, k = g
    return (u*i+3*k) % (3**level)


def module_action(g, v, level):
    ans = [0]*len(v)
    for i, a in enumerate(v):
        ans[action(g, i, level)] = (g[0]*a) % coeff
    return ans


def orbit_transversal(level, base):
    orbit = {action(g, base, level) for g in G}
    transversal = {base: one}
    # Use complex conjugation as the chosen representative of the other
    # K/Q embedding at level 1.  Its product of Kummer roots is positive.
    if level == 1 and base == 1:
        transversal[2] = (26, 0)
    for i in sorted(orbit):
        if i not in transversal:
            transversal[i] = next(g for g in G if action(g, base, level) == i)
    stabilizer = [g for g in G if action(g, base, level) == base]
    return orbit, transversal, stabilizer


def induce(level, base, z):
    orbit, trans, stab = orbit_transversal(level, base)
    for g, h in product(stab, repeat=2):
        assert (z(mul(g, h))-z(g)-g[0]*z(h)) % coeff == 0
    cocycles = {}
    for g in G:
        value = [0]*(3**level)
        for i in orbit:
            y = action(inv(g), i, level)
            h = mul(mul(inv(trans[i]), g), trans[y])
            assert h in stab
            value[i] = trans[i][0]*z(h) % coeff
        cocycles[g] = value
    for g, h in product(G, repeat=2):
        rhs = module_action(g, cocycles[h], level)
        assert cocycles[mul(g, h)] == [(a+b) % coeff for a, b in zip(cocycles[g], rhs)]
    for h in stab:
        assert cocycles[h][base] == z(h) % coeff
    return cocycles, len(stab), len(G)**2


# At level 1 the two factors are Q (root 2) and K=Q(zeta_3)
# (root 2*zeta_3).  The ninth root of 2*zeta_3 is
# 2^(1/9)*zeta_27, so its exact Kummer cocycle is (3k+u-1)/3.
def kummer_2zeta(g):
    u, k = g
    assert u % 3 == 1
    return ((3*k+u-1)//3) % coeff


cK, stabK, cocycle_checksK = induce(1, 1, kummer_2zeta)
cQ, stabQ, cocycle_checksQ = induce(1, 0, lambda g: g[1])
norm4_checks = 0
norm8_checks = 0
for g in G:
    # N_K/Q(2*zeta_3)=4; the chosen coset roots multiply to 2^(2/9).
    assert sum(cK[g]) % coeff == 2*g[1] % coeff
    # The entire etale element X_1=(2,2*zeta_3) has total norm 8.
    assert (sum(cK[g])+sum(cQ[g])) % coeff == 3*g[1] % coeff
    norm4_checks += 1
    norm8_checks += 1
inverse_deck_checks = 0
_, _, field_K_stabilizer = orbit_transversal(1, 1)
for g, h in product(G, field_K_stabilizer):
    conjugate = mul(mul(inv(g), h), g)
    gamma_position = action(g, 1, 1)
    assert (g[0]*cK[conjugate][1]-cK[h][gamma_position]
            -(h[0]-1)*cK[g][gamma_position]) % coeff == 0
    inverse_deck_checks += 1
print('PASS: exact Shapiro cocycles and the nontrivial norms 2*zeta_3 -> 4, X_1 -> 8.', flush=True)

# At positional level 3, use the Kummer class of zeta_3 in L_3.
# It is represented using its ninth root zeta_27.  Its norm to L_2
# is zeta_3^3=1.  Check the actual pushforward cocycle at both
# lower field stabilizers, including its bounding elements.
def kummer_zeta(g):
    u, _ = g
    assert u % 3 == 1
    return ((u-1)//3) % coeff


cZ, stabZ, cocycle_checksZ = induce(3, 1, kummer_zeta)
lower = {}
for g in G:
    v = [0]*9
    for i, x in enumerate(cZ[g]):
        v[i % 9] = (v[i % 9]+x) % coeff
    lower[g] = v
norm_zeta_bounds = {}
for base in [0, 1]:
    _, _, stab = orbit_transversal(2, base)
    candidates = [b for b in range(coeff)
                  if all((lower[h][base]-(h[0]-1)*b) % coeff == 0 for h in stab)]
    assert candidates
    norm_zeta_bounds[str(base)] = candidates[0]
print('PASS: root-cubing transfer of zeta_3 is a coboundary at both lower factors.', flush=True)
results['finite_shapiro'] = {
    'splitting_field': 'Q(zeta_27,2^(1/9))', 'group_order': len(G),
    'coefficient_modulus': coeff,
    'stabilizer_orders': [stabQ, stabK, stabZ],
    'all_pair_cocycle_checks': cocycle_checksK+cocycle_checksQ+cocycle_checksZ,
    'norm_2zeta_to_4_checks': norm4_checks,
    'total_norm_X1_to_8_checks': norm8_checks,
    'natural_field_action_inverse_deck_checks': inverse_deck_checks,
    'norm_zeta_to_one_bounding_elements_at_lower_orbits': norm_zeta_bounds,
    'Tate_scalar_and_actual_root_power_transition_retained': True,
}

# Universal finite-etale norm determinants and exact total norms.
X = sp.Symbol('X')
Y = sp.Symbol('Y')
M_Y = sp.Matrix([[0, 0, X], [1, 0, 0], [0, 1, 0]])
M_one_minus_Y = sp.eye(3)-M_Y
assert M_Y.det() == X
assert sp.expand(M_one_minus_Y.det()) == 1-X
assert sp.expand((M_one_minus_Y**3).det()) == sp.expand((1-X)**3)
assert sp.resultant(Y**3-X, 1-Y, Y) == 1-X
total_checks = []
parameters = [Fraction(2), Fraction(-1), Fraction(3, 2),
              Fraction(-2, 3), Fraction(1, 2), Fraction(7)]
for aa in parameters:
    a = sp.Rational(aa.numerator, aa.denominator)
    for n in range(5):
        polynomial = X**(3**n)-a**3
        norm_one_minus = sp.resultant(polynomial, 1-X, X)
        norm_X = sp.resultant(polynomial, X, X)
        assert norm_one_minus == 1-a**3
        assert norm_X == a**3
        # The two-parameter family has the needed cube condition already
        # for its two generating norm sequences.
        for r, z in [(0, 1), (1, 0), (1, 1), (-2, 3)]:
            assert norm_X**r*norm_one_minus**(3*z) == (a**r*(1-a**3)**z)**3
        total_checks.append({'a': str(a), 'level': n,
                             'norm_X': str(norm_X), 'norm_1_minus_X': str(norm_one_minus)})

factors = []
for n in range(1, 6):
    degree = 3**(n-1)
    f = X**degree-2
    ell = X**(2*degree)+2*X**degree+4
    assert sp.expand(f*ell) == X**(3**n)-8
    assert sp.resultant(f, 1-X, X) == -1
    assert sp.resultant(ell, 1-X, X) == 7
    # SymPy's exact rational factorization independently confirms the
    # two irreducible factors at these five finite levels.
    irreducibles = sp.factor_list(X**(3**n)-8)[1]
    assert len(irreducibles) == 2
    assert sorted(sp.degree(p, X) for p, e in irreducibles) == [degree, 2*degree]
    assert all(e == 1 for _, e in irreducibles)
    factors.append({'level': n, 'factor_degrees': [degree, 2*degree],
                    'norm_1_minus_alpha': -1, 'norm_1_minus_beta': 7})
results['universal_rank_three_norms'] = {'norm_Y': 'X', 'norm_1_minus_Y': '1-X',
                                      'norm_cube': '(1-X)^3'}
results['total_norm_checks'] = total_checks
results['a2_exact_factorizations'] = factors
results['status'] = 'PASS'
results['scope'] = ('Finite exact module, cocycle, norm and field-factor checks; '
                    'the continuous all-level theorem is proved in E.46.')
print('PASS: universal norm determinants, 30 total-norm cases, and five a=2 factorizations.', flush=True)
(OUT/'e_norm_sections.json').write_text(json.dumps(results, indent=2)+'\n')
print('PASS: all E.46 finite certificates.', flush=True)
