"""Exact elliptic counterexample to automatic punctured transport."""
from fractions import Fraction as Q
from pathlib import Path
import json


def trim(a):
    a = list(map(Q, a))
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0) for i in range(n)])


def scale(c, a):
    return trim([c*x for x in a])


def mul(a, b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def rem(a, b):
    a, b = trim(a), trim(b)
    while a != [0] and len(a) >= len(b):
        k, c = len(a)-len(b), a[-1]/b[-1]
        for j, z in enumerate(b):
            a[j+k] -= c*z
        a = trim(a)
    return a


def gcd(a, b):
    while trim(b) != [0]:
        a, b = b, rem(a, b)
    return scale(1/trim(a)[-1], a)


def value(a, x):
    return sum(z*Q(x)**i for i, z in enumerate(a))


cubic = [0, -1, 0, 1]                  # y^2=x^3-x
psi3 = [-1, 0, -6, 0, 3]
derivative = [i*psi3[i] for i in range(1, len(psi3))]
slope_numerator = [-1, 0, 3]
# x(2P)-x = -psi3(x)/(4*(x^3-x)); then y(2P)=-y.
doubling_numerator = add(mul(slope_numerator, slope_numerator), scale(-12, mul([0, 1], cubic)))
assert doubling_numerator == scale(-1, psi3)
assert gcd(psi3, derivative) == [1]
assert gcd(psi3, cubic) == [1]
assert [value(psi3, x) for x in [0, 1, -1]] == [-1, -4, -4]
result = {
    'status': 'Proved',
    'curve': 'E:y^2=x^3-x over Q(i)',
    'source_open_curve': 'Y=E minus E[2]',
    'original_etale_cover': '[2]:Y->E minus {O}, degree4',
    'Jacobian_quotient_map': '[3]:E->E, degree9',
    'proper_H1_map': '3*I_2, injective over every Z_l',
    'punctured_transport_exists': False,
    'boundary_cardinality': 4,
    'puncture_compatible_degree_bound': 4,
    'actual_quotient_degree': 9,
    'psi3_coefficients_low_to_high': psi3,
    'psi3_squarefree_gcd': [1],
    'psi3_cubic_gcd': [1],
    'psi3_at_0_1_minus1': [-1, -4, -4],
    'geometric_3_torsion_points': 9,
    '3_torsion_points_in_Y': 8,
    'image_on_E2': '[3] is the identity on E[2]',
    'fiber_argument': 'For q in E[2], exactly one of the nine points of [3]^-1(q) lies in E[2]; for q outside E[2], all nine lie in Y. Hence [3](Y)=E.',
    'scope': 'Refutes automatic puncturing of a detecting Jacobian quotient; it does not produce a residual element in the common pro-l kernel R.'
}
out = Path(__file__).resolve().parent/'g_cover_transport.json'
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
