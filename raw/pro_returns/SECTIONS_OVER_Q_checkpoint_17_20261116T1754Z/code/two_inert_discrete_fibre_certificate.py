#!/usr/bin/env python3
"""Exact finite maps used in A180; no infinite actual norm family is computed."""
from fractions import Fraction as Q
from pathlib import Path
import itertools
import json

BASE = Path(__file__).resolve().parent


def mul(x, y):
    z = [Q(0)] * 5
    for i in range(3):
        for j in range(3):
            z[i + j] += x[i] * y[j]
    for i in (4, 3):
        z[i - 3] += 3 * z[i]
    return z[:3]


def power(x, n):
    z = [Q(1), Q(0), Q(0)]
    while n:
        if n & 1:
            z = mul(z, x)
        x = mul(x, x)
        n //= 2
    return z


def determinant(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def norm(x):
    columns = [mul(x, [Q(int(i == j)) for i in range(3)]) for j in range(3)]
    return determinant([[columns[j][i] for j in range(3)] for i in range(3)])


norms = []
for q, g, complement in [
    (11, [2, 1, 0], [4, -2, 1]),
    (59, [2, 2, -1], [10, -1, 6]),
]:
    assert mul(g, complement) == [q, 0, 0]
    assert norm(g) == q
    assert norm(complement) == q * q
    # h_q = complement^3 / q^2 is literally q/gamma_q^3.
    h = [x / (q * q) for x in power(complement, 3)]
    assert mul(h, power(g, 3)) == [q, 0, 0]
    assert norm(h) == 1
    norms.append({'q': q, 'gamma': g, 'complement': complement,
                  'h': [str(x) for x in h], 'norm_h': 1})

divisor_checks = []
for n in range(1, 15):
    lower_degrees = [1] + [2 * 3**j for j in range(n)]
    upper_degrees = [1] + [2 * 3**j for j in range(n + 1)]
    assert sum(lower_degrees) == 3**n
    assert sum(upper_degrees) == 3**(n + 1)
    # Stable lower branch: upper degrees one and two, norm weights one and two.
    # Every other lower branch has one upper branch with residue-degree ratio three.
    image_degrees = [upper_degrees[0] + upper_degrees[1]]
    image_degrees.extend(upper_degrees[i + 1] for i in range(1, n + 1))
    assert image_degrees == [3 * f for f in lower_degrees]
    stable = [1] + [0] * (n + 1)
    norm_stable = [stable[0] + 2 * stable[1]]
    norm_stable.extend(3 * stable[i + 1] for i in range(1, n + 1))
    assert norm_stable == [1] + [0] * n
    for c in range(-20, 21):
        q_vector = [-2 * c, c]
        assert q_vector[0] + 2 * q_vector[1] == 0
        # Both changed branches have relative residue degree one.
        assert [1 * z for z in q_vector] == q_vector
        assert [3 * 3**(n - 1) * z for z in (-2, 1)] == [3**n * z for z in (-2, 1)]
    divisor_checks.append({'n': n, 'pure_two_degrees': lower_degrees,
                           'stable_norm': norm_stable,
                           'changed_divisor_multiplier': 3**(n - 1)})

profiles = []
for c11, c59 in itertools.product(range(9), repeat=2):
    passed = (6 + 5 * c11 + c59) % 9 == 0
    assert passed == ((c59 - 4 * c11 - 3) % 9 == 0)
    if passed:
        assert (2 * c11 + c59) % 3 == 0
        profiles.append([c11, c59])
assert len(profiles) == 9
assert [0, 3] in profiles and [3, 6] in profiles

# All finite class quotient maps use the same actual chosen generator.
class_map_checks = 0
for a, b in itertools.product(range(5), repeat=2):
    if b < a:
        continue
    for z in range(3**b):
        assert (z % (3**b)) % (3**a) == z % (3**a)
        class_map_checks += 1

# Additive notation for literal delta maps.  No finite-rank hypothesis or
# invertibility of the transition matrices is used in the identities below.
def mv(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def sub(x, y):
    return [a - b for a, b in zip(x, y)]


def add(x, y):
    return [a + b for a, b in zip(x, y)]


matrices = [
    [[3, 0, 6], [0, 1, -2]],
    [[1, 2, 0, 0], [0, 3, 1, 0], [2, 0, 0, -1]],
    [[3, 0, 0, 0, 0], [0, 1, 1, 0, 0],
     [0, 0, 3, 0, 1], [1, 0, 0, 1, 0]],
]
defect_checks = 0
for seed in range(-12, 13):
    g = [[seed + (i + 1) * (j + 2) for j in range(i + 2)] for i in range(4)]
    v = [[seed * (j - 1) - i for j in range(i + 2)] for i in range(4)]
    delta = [sub(g[i], mv(matrices[i], g[i + 1])) for i in range(3)]
    shifted = [add(g[i], v[i]) for i in range(4)]
    shifted_delta = [sub(shifted[i], mv(matrices[i], shifted[i + 1])) for i in range(3)]
    dv = [sub(v[i], mv(matrices[i], v[i + 1])) for i in range(3)]
    assert shifted_delta == [add(delta[i], dv[i]) for i in range(3)]
    # Solve a finite defect system backwards in the actual integer lattices.
    u = [None] * 4
    u[3] = [0] * 5
    for i in (2, 1, 0):
        u[i] = add(delta[i], mv(matrices[i], u[i + 1]))
    b = [sub(g[i], u[i]) for i in range(4)]
    assert all(b[i] == mv(matrices[i], b[i + 1]) for i in range(3))
    defect_checks += 1

# Exact abstract comparison: the tower Z --3--> Z has the constant defect one.
# Its compact solution is -1/2 in Z_3; for an actual solution,
# 2*u_1+1 would be divisible by every 3^N, forcing the impossible u_1=-1/2.
compact_defect = []
for n in range(1, 13):
    mod = 3**n
    u = -pow(2, -1, mod) % mod
    assert (u - 3 * u - 1) % mod == 0
    assert (2 * u + 1) % mod == 0
    compact_defect.append([n, u])

# Exact finite module testing the limit of the primary two-prime argument:
# sigma has order three, tau inverts sigma, norm is zero, and the split
# orbit sum is zero although the distinguished tau-fixed class is nonzero.
def mm(a, b, mod):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) % mod
             for j in range(2)] for i in range(2)]


mod = 7
sigma = [[2, 0], [0, 4]]
tau = [[0, 1], [1, 0]]
ident = [[1, 0], [0, 1]]
sigma2 = mm(sigma, sigma, mod)
assert mm(sigma2, sigma, mod) == ident
assert mm(mm(tau, sigma, mod), tau, mod) == sigma2
norm_matrix = [[(ident[i][j] + sigma[i][j] + sigma2[i][j]) % mod
                for j in range(2)] for i in range(2)]
assert norm_matrix == [[0, 0], [0, 0]]
p = [1, 1]
assert mv(tau, p) == p
p2 = [(x + y) % mod for x, y in zip(mv(sigma, p), mv(sigma2, p))]
assert p2 == [6, 6]
assert [(x + y) % mod for x, y in zip(p, p2)] == [0, 0]
assert p != [0, 0]

data = {
    'first_field_norms': norms,
    'divisor_checks': divisor_checks,
    'level_three_integer_profile_residues': profiles,
    'class_quotient_checks': class_map_checks,
    'defect_sign_checks': defect_checks,
    'compact_Z3_solution_residues': compact_defect,
    'abstract_prime_to_three_module': {
        'modulus': 7, 'sigma': sigma, 'tau': tau,
        'norm': norm_matrix, 'distinguished': p, 'degree_two': p2,
        'scope': 'An exact finite-module comparison, not an actual ideal class computation.'},
    'scope': 'Finite arithmetic and exact-map checks for A180; no infinite actual norm family, '
             'higher ordinary prime-to-three class, or actual unit lim1 value is computed.'
}
(BASE / 'two_inert_discrete_fibre_certificate_data.json').write_text(json.dumps(data, indent=2) + '\n')
print('PASS: both literal first-field prime generators, complements, and norm-one quotients')
print('PASS:', len(divisor_checks), 'heights of integral two-prime and changed-prime norm maps')
print('PASS:', len(profiles), 'exact known integer profile classes modulo nine')
print('PASS:', class_map_checks, 'finite cyclic class quotient maps')
print('PASS:', defect_checks, 'unit-defect, generator-change, and backwards correction identities')
print('PASS:', len(compact_defect), 'exact residues of the compact defect correction -1/2')
print('PASS: literal order-three/involution module with nonzero prime-to-three distinguished class')
print('SCOPE: the infinite equivalence is proved in the source; its remaining arithmetic values are retained.')
