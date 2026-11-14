#!/usr/bin/env python3
"""Four proved actual standard elements in an explicit finite M image.

The full input is h=1, t=tau, w=x. This verifies their finite images,
the separate quotient and conjugacy signs, and the exact cusp defects.
It does not replace the proof of the full four-point set by a finite count.
"""
from collections import deque
from pathlib import Path
import json

prime = 5


def canon(matrix):
    matrix = tuple(value % prime for value in matrix)
    return min(matrix, tuple(-value % prime for value in matrix))


def mm(a, b):
    return canon((a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                  a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))


def pm(a, b):
    return tuple(a[b[i]] for i in range(3))


def mul(a, b):
    return (mm(a[0], b[0]), pm(a[1], b[1]),
            ((a[2][0]+b[2][0]) % 2, (a[2][1]+b[2][1]) % 3))


one = ((1, 0, 0, 1), (0, 1, 2), (0, 0))
A = (canon((0, -1, 1, 0)), (1, 0, 2), (1, 0))
B = (canon((0, -1, 1, 1)), (1, 2, 0), (0, 1))


def inv(a):
    aa, bb, cc, dd = a[0]
    perm = tuple(a[1].index(i) for i in range(3))
    return (canon((dd, -bb, -cc, aa)), perm, (a[2][0], -a[2][1] % 3))


def power(a, n):
    if n < 0:
        return power(inv(a), -n)
    result = one
    while n:
        if n & 1:
            result = mul(result, a)
        a = mul(a, a)
        n >>= 1
    return result


def prod(*values):
    result = one
    for value in values:
        result = mul(result, value)
    return result


def conj(a, b):
    return prod(a, b, inv(a))


def subgroup(generators):
    seen = {one}
    queue = deque([one])
    while queue:
        value = queue.popleft()
        for generator in generators:
            image = mul(value, generator)
            if image not in seen:
                seen.add(image)
                queue.append(image)
    return seen


def j_action(value):
    J = canon((0, 1, 1, 0))
    return (mm(mm(J, value[0]), J), pm(pm(A[1], value[1]), A[1]),
            (value[2][0], -value[2][1] % 3))


checks = []


def check(name, condition):
    assert condition, name
    checks.append({'name': name, 'passed': True})


check('actual_full_coproduct_factor_relations', power(A, 2) == power(B, 3) == one)
Q = subgroup((A, B))
check('explicit_actual_M_image_order_1080', len(Q) == 1080)
check('finite_j_action_matches_the_actual_standard_generators',
      j_action(A) == A and j_action(B) == inv(B))
check('finite_j_action_preserves_the_actual_image_and_squares_to_one',
      all(j_action(value) in Q and j_action(j_action(value)) == value for value in Q))
x = power(mul(A, B), -2)
y = conj(B, x)
p = mul(x, A)
check('original_standard_cusp_words', p == prod(inv(B), A, inv(B))
      and power(p, 2) == mul(x, y))
kappas = (B, inv(B), conj(A, B), conj(A, inv(B)))
check('four_retained_full_elements_have_distinct_finite_images', len(set(kappas)) == 4)
rows = []
for index, (kappa, epsilon, sigma, nu) in enumerate(zip(
        kappas, (1, -1, -1, 1), (1, -1, 1, -1), (1, -1, 1, -1))):
    check('kappa_%d_order_three_and_j_inversion' % index,
          power(kappa, 3) == one and kappa != one and j_action(kappa) == inv(kappa))
    check('kappa_%d_separate_S3_coset_and_full_abelian_signs' % index,
          kappa[1] == power(B, epsilon)[1] and kappa[2] == (0, sigma % 3))
    check('kappa_%d_common_entire_finite_image' % index, subgroup((A, kappa)) == Q)
    phi_p = prod(inv(kappa), A, inv(kappa))
    target = conj(inv(x), power(p, nu))
    defect = mul(phi_p, inv(target))
    check('kappa_%d_original_cusp_comparison' % index, (defect == one) == (index in (2, 3)))
    rows.append({'standard_kappa': ('xi', 'xi^-1', 'tau xi tau', 'tau xi^-1 tau')[index],
                 'epsilon_in_M_over_F': epsilon, 'sigma_in_M_abelianization': sigma,
                 'original_standard_nu': nu, 'finite_image_order': len(Q),
                 'original_cusp_word_is_identity_in_this_image': defect == one,
                 'cusp_defect_image': {'PSL2_F5_matrix': list(defect[0]),
                                       'S3_permutation': list(defect[1]),
                                       'C2_plus_C3': list(defect[2])}})

output = {'status': 'PASS',
          'scope': 'Original standard full h=1, t=tau, w=x, and the four full elements already proved in the note.',
          'finite_map': 'M -> PSL2(F5) x S3 x (C2 x C3), using the displayed A and B images.',
          'A_image': A, 'B_image': B, 'actual_finite_image_order': len(Q),
          'checks': checks, 'assertion_count': len(checks), 'rows': rows,
          'limits': 'No finite enumeration is used to assert the global four-point completeness; no remaining original h or cusp zero is assigned.'}
text = json.dumps(output, indent=2) + '\n'
Path(__file__).with_name('actual_four_order_three_standard_output.json').write_text(text)
print(text, end='')
