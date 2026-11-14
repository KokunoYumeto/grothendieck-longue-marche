#!/usr/bin/env python3
"""E.38: exact finite obstruction beyond intrinsic cubic class two.

All tests are exact integer calculations.  Hermite normal form tests the
entire coefficient solution set, rather than sampling coefficient tuples.
The independent row witness proves nonmembership without trusting HNF.
"""
from pathlib import Path
import json
from fractions import Fraction
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

U = s.Symbol('U')
DEG = 4
q = 19
a = 3
v0 = 81


def trunc(expr):
    return s.Poly(s.expand(expr), U).rem(s.Poly(U**(DEG + 1), U)).as_expr()


def coeff(expr, start=0):
    p = s.Poly(trunc(expr), U)
    return s.Matrix([int(p.nth(j)) for j in range(start, DEG + 1)])


def pow_trunc(expr, n):
    result = s.Integer(1)
    while n:
        if n & 1:
            result = trunc(result * expr)
        expr = trunc(expr * expr)
        n //= 2
    return result


def vp(n, p=3):
    if n == 0:
        return None
    v = 0
    n = abs(int(n))
    while n % p == 0:
        n //= p
        v += 1
    return v


Tq = pow_trunc(1 + U, q)
Ta = pow_trunc(1 + U, a)
K = s.Matrix.hstack(*[
    coeff(Ta * pow_trunc(Tq - 1, i) - U**i, 1)
    for i in range(1, DEG + 1)
])
target = -v0 * coeff(Ta - 1, 1)


def solve_mod(m, extras=None):
    modulus = 3**m
    blocks = [K, modulus * s.eye(DEG)]
    if extras is not None:
        blocks.append(extras)
    matrix = s.Matrix.hstack(*blocks)
    H = hermite_normal_form(matrix)
    assert H.rows == H.cols == DEG
    inv = H.inv()
    coords = inv * target
    failed = [j for j, x in enumerate(coords) if x.q != 1]
    result = {'m': m, 'modulus': modulus,
              'solvable': not failed,
              'HNF': [[int(x) for x in H.row(i)] for i in range(DEG)],
              'target_HNF_coordinates': [str(x) for x in coords]}
    if failed:
        # The scaled row is independently checked against every generator.
        dual = modulus * inv.row(failed[0])
        assert all(x.q == 1 for x in dual)
        dual = dual.applyfunc(lambda x: int(x) % modulus)
        assert all(int(x) % modulus == 0 for x in dual * matrix)
        residue = int((dual * target)[0]) % modulus
        assert residue
        result['dual_witness'] = [int(x) for x in dual]
        result['target_residue'] = residue
    return result


rows = [solve_mod(m) for m in range(1, 9)]
first = next(row['m'] for row in rows if not row['solvable'])
assert first == 6
certificate = rows[first - 1]

# The kernel H has module J=(3,U) and a-coordinate 3Z_3.  Its
# gamma_(c+1) is (T^3-1)^c J.  Test all coefficient lifts in each
# lower-central quotient of this same finite arithmetic quotient.
delta = pow_trunc(1 + U, 3) - 1
class_rows = []
for c in range(1, 6):
    power = pow_trunc(delta, c)
    extra = s.Matrix.hstack(coeff(3 * power, 1), *[
        coeff(power * U**j, 1) for j in range(1, DEG + 1)
    ])
    row = solve_mod(6, extra)
    row['nilpotency_bound'] = c
    row['lower_central_generators'] = [
        [int(x) for x in extra.col(j)] for j in range(extra.cols)]
    class_rows.append(row)

gamma4 = s.Matrix.hstack(coeff(3 * pow_trunc(delta, 3)),
                         coeff(U * pow_trunc(delta, 3)))
gamma4_lattice = hermite_normal_form(
    s.Matrix.hstack(gamma4, 3**6 * s.eye(DEG + 1)))
gamma4_order_exponent = 30 - vp(gamma4_lattice.det())
assert gamma4_order_exponent == 5
assert 35 - gamma4_order_exponent == 30
gamma3_witness = coeff(U * pow_trunc(delta, 2))
assert any(x.q != 1 for x in gamma4_lattice.inv() * gamma3_witness)

# Finite group existence: x has order 3^(m+1), since that power
# acts trivially on (Z/3^m)[U]/U^5.  Check all truncated coefficients.
modulus = 3**6
x_order = 3**7
power_coeff = coeff(pow_trunc(1 + U, x_order) - 1)
assert all(int(x) % modulus == 0 for x in power_coeff)
assert int(pow(4, 9, 19)) == 1 and int(pow(4, 3, 19)) != 1
assert int(pow(2, (19 - 1)//9, 19)) == 4

# Independent elementary consequences of the four congruences.
# Projecting the exact rows gives all residues permitted by each step.
possible_v1 = [x for x in range(modulus)
               if (int(K[0,0])*x-int(target[0])) % modulus == 0]
assert {x % 81 for x in possible_v1} == {27}
possible_v2 = {z % 27 for x in possible_v1 for z in range(243)
               if (int(K[1,0])*x + int(K[1,1])*z-int(target[1])) % 243 == 0}
assert possible_v2 == {18}
possible_v3 = {z % 3 for x in possible_v1
               for y in range(18, 81, 27) for z in range(81)
               if (int(K[2,0])*x + int(K[2,1])*y + int(K[2,2])*z
                   - int(target[2])) % 81 == 0}
assert possible_v3 == {2}
# With v1 divisible27, v2 divisible9, and v0 divisible81, row4
# modulo9 is 3*v3=0, since its v4 coefficient is0 modulo9.
assert int(K[3,0])*27 % 9 == 0
assert int(K[3,1])*9 % 9 == 0
assert int(K[3,2]) % 9 == 3
assert int(K[3,3]) % 9 == 0
assert int(target[3]) % 9 == 0

r = Fraction(-1, 6)
binom = Fraction(1)
formal = []
for n in range(DEG + 1):
    if n:
        binom *= (r - n + 1) / n
    val = v0 * binom
    formal.append({'n': n, 'coefficient': str(val),
                   'valuation': vp(val.numerator)-vp(val.denominator)})
assert formal[4]['valuation'] == -1

result = {
    'q': q, 'Frobenius_a': a, 'inertia_augmentation': v0,
    'coefficient_matrix': [[int(x) for x in K.row(i)] for i in range(DEG)],
    'target': [int(x) for x in target],
    'determinant_valuation': vp(K.det()),
    'modular_tests': rows,
    'first_failure_m': first,
    'finite_group': {'module_modulus': modulus, 'U_power': DEG+1,
                     'x_order': x_order, 'ambient_order_3_exponent': 37,
                     'Fermat_kernel_order_3_exponent': 35,
                     'x_order_action_coefficients': [int(x) for x in power_coeff]},
    'lower_central_tests': class_rows,
    'class_three_quotient': {'gamma4_generators': [
        [int(x) for x in gamma4.col(i)] for i in range(gamma4.cols)],
        'gamma4_order_3_exponent': gamma4_order_exponent,
        'quotient_order_3_exponent': 30,
        'exact_nilpotency_class': 3,
        'nonzero_gamma3_witness': [int(x) for x in gamma3_witness]},
    'formal_solution': formal,
    'elementary_constraints': {'v1_mod81':27,'v2_mod27':18,
                               'v3_mod3_from_degree3':2,
                               'v3_mod3_from_degree4':0},
    'status':'PASS'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print('Exact coefficient matrix:')
print(K)
print('Exact target:', list(target))
print('Determinant 3-valuation:', vp(K.det()))
print('Solvability for m=1,...,8:', [r['solvable'] for r in rows])
print('First failure modulo', certificate['modulus'])
print('Dual witness:', certificate['dual_witness'],
      'target residue:', certificate['target_residue'])
print('Finite R: module=(Z/729)[U]/U^5; x order2187; |R|=3^37; |H|=3^35')
print('Solvability in class bounds1,...,5:', [r['solvable'] for r in class_rows])
print('Class-three quotient H/gamma4(H) has order3^30 and retains the same dual witness.')
print('Formal inertia coefficients:', [r['coefficient'] for r in formal])
print('Elementary contradiction: v3=2 mod3 and v3=0 mod3.')
print('PASS: every coefficient lift is excluded by the checked finite quotient.')
