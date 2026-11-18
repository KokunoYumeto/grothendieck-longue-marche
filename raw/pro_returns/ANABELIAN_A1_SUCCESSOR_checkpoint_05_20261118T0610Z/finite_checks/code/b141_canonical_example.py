"""Exact finite certificate for B141, C/F5: y^2=x^6+1, P=(0,1).

The proof identifies the elliptic norm, the Lang pullback cover, and its
character Euler factors. This code independently checks the finite field,
point, group, character, and polynomial data used in that proof.
Coefficient lists are in ascending degree.
"""
from pathlib import Path
import json
import sympy as sp


class Field:
    """F5 or F5[u]/(u^2-2), represented by a+5*b."""
    def __init__(self, degree):
        assert degree in (1, 2)
        self.degree = degree
        self.order = 5**degree

    def add(self, x, y):
        a, b, c, d = x % 5, x // 5, y % 5, y // 5
        return (a+c) % 5 + 5*((b+d) % 5)

    def mul(self, x, y):
        a, b, c, d = x % 5, x // 5, y % 5, y // 5
        return (a*c+2*b*d) % 5 + 5*((a*d+b*c) % 5)

    def power(self, x, n):
        z = 1
        while n:
            if n & 1:
                z = self.mul(z, x)
            x = self.mul(x, x)
            n >>= 1
        return z


assert 2 not in {i*i % 5 for i in range(5)}
point_records = []
for degree in (1, 2):
    F = Field(degree)
    assert all(F.power(x, F.order) == x for x in range(F.order))
    affine = [
        (x, y)
        for x in range(F.order)
        for y in range(F.order)
        if F.mul(y, y) == F.add(F.power(x, 6), 1)
    ]
    point_records.append({
        'degree_over_F5': degree,
        'modulus': 'u^2-2' if degree == 2 else 'prime field',
        'affine_points': affine,
        'infinity_points': ['infinity_plus', 'infinity_minus'],
        'count': len(affine)+2,
    })
assert [r['count'] for r in point_records] == [6, 46]

# E/F5: v^2=u^3+1, with O represented by None.
O = None
E = [O] + [(u, v) for u in range(5) for v in range(5)
           if (v*v-u**3-1) % 5 == 0]
assert len(E) == 6


def eadd(A, B):
    if A is O:
        return B
    if B is O:
        return A
    x, y = A
    u, v = B
    if x == u and (y+v) % 5 == 0:
        return O
    if A == B:
        m = (3*x*x) * pow(2*y, -1, 5) % 5
    else:
        m = (v-y) * pow(u-x, -1, 5) % 5
    z = (m*m-x-u) % 5
    return z, (m*(x-z)-y) % 5


def emul(n, A):
    if n < 0:
        return emul(-n, None if A is None else (A[0], -A[1] % 5))
    B = O
    while n:
        if n & 1:
            B = eadd(B, A)
        A = eadd(A, A)
        n >>= 1
    return B


R, T = (0, 1), (4, 0)
assert emul(3, R) is O and R is not O
assert emul(2, T) is O and T is not O
for A in E:
    for B in E:
        assert eadd(A, B) in E and eadd(A, B) == eadd(B, A)
        for C in E:
            assert eadd(eadd(A, B), C) == eadd(A, eadd(B, C))
chi = {}
for a in range(3):
    for b in range(2):
        A = eadd(emul(a, R), emul(b, T))
        assert A not in chi
        chi[A] = a
assert set(chi) == set(E)
for A in E:
    for B in E:
        assert chi[eadd(A, B)] == (chi[A]+chi[B]) % 3
three_E = {emul(3, A) for A in E}
assert R not in three_E
assert emul(-2, R) == R

curve_points = list(point_records[0]['affine_points']) + ['infinity_plus', 'infinity_minus']
rows = []
occupancies = [0, 0, 0]
for P in curve_points:
    image = O if isinstance(P, str) else (P[0]**2 % 5, P[1])
    assert image in E
    exponent = (chi[image]-chi[R]) % 3
    occupancies[exponent] += 1
    rows.append({'C_point': P, 'elliptic_image': image, 'pointed_character': exponent})
assert occupancies == [1, 1, 4]
canonical_exponent = (-2*chi[R]) % 3
assert canonical_exponent == 1


def qadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def qmul(a, b):
    # zeta^2+zeta+1=0.
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]-a[1]*b[1]


def conjugate(a):
    return a[0]-a[1], -a[1]


L = [(1, 0), (-3, -3), (0, 5)]
Lc = [conjugate(a) for a in L]
product = [(0, 0)]*5
for i, a in enumerate(L):
    for j, b in enumerate(Lc):
        product[i+j] = qadd(product[i+j], qmul(a, b))
assert all(b == 0 for a, b in product)
relative = [a for a, b in product]
assert relative == [1, -3, 4, -15, 25]

# A second polynomial calculation uses a symbolic integer resultant.
z, U = sp.symbols('z U')
expression = 1+(1+z+4*z**2)*U+5*z*U**2
resultant = sp.Poly(sp.resultant(z*z+z+1, expression, z), U)
assert [int(resultant.nth(i)) for i in range(5)] == relative

N1, N2 = [r['count'] for r in point_records]
jacobian_order = (N1*N1+N2)//2-5
assert jacobian_order == 36
relative_order = sum(relative)
assert relative_order == 12 and relative_order % 5 != 0

output = {
    'verified': True,
    'curve': 'C/F5: y^2=x^6+1',
    'point': [0, 1],
    'elliptic_curve': 'E/F5: v^2=u^3+1',
    'map': '(x,y) -> (x^2,y); both infinity points -> O',
    'point_counts': point_records,
    'elliptic_points': E,
    'elliptic_addition_table': [[E.index(eadd(A, B)) for B in E] for A in E],
    'elliptic_character_table': [chi[A] for A in E],
    'three_times_elliptic_group': [A for A in E if A in three_E],
    'norm_canonical_class': R,
    'canonical_class_not_three_divisible': True,
    'pointed_occupancy_rows': rows,
    'pointed_occupancies': occupancies,
    'canonical_character_exponent': canonical_exponent,
    'relative_zeta_numerator_low_to_high': relative,
    'base_jacobian_order': jacobian_order,
    'cover_jacobian_order': jacobian_order*relative_order,
    'relative_class_number': relative_order,
    'cover_degree': 3,
    'cover_genus': 4,
    'scope': 'Finite certificate for this example. The elliptic norm and Lang geometry, the all-prime congruence family, and persistence under constant extensions are proved in the text, not inferred from a finite test.',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2)+'\n')
print('PASS C/F5 and F25 counts:6,46; #J_C(F5)=36')
print('PASS E(F5) order6; R=(0,1) order3 and R not in3E(F5)')
print('PASS canonical class norm R; occupancies[1,1,4], canonical exponent1')
print('PASS two polynomial computations: relative numerator[1,-3,4,-15,25]')
print('PASS relative class number12, #J_D(F5)=432')
