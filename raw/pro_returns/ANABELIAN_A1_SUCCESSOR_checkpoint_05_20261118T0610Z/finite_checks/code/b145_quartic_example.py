"""Exact B145 example: y^3-y=x^4 over F27, with a new F27 marking.

Base field: F3[t]/(t^3-t-1), digits a+3b+9c.
Quadratic field: F27[s]/(s^2+1), encoding a+27b.
The geometric character-factor formulas and norm interpretation are
proved in the text; no universal statement is inferred from these data.
"""
from pathlib import Path
from collections import defaultdict
import json
import sympy as sp


class F27:
    order = 27
    @staticmethod
    def add(x, y):
        return sum(((x//3**i+y//3**i) % 3)*3**i for i in range(3))
    @staticmethod
    def neg(x):
        return sum((-(x//3**i) % 3)*3**i for i in range(3))
    @staticmethod
    def mul(x, y):
        a = [(x//3**i) % 3 for i in range(3)]
        b = [(y//3**i) % 3 for i in range(3)]
        c = [0]*5
        for i in range(3):
            for j in range(3):
                c[i+j] += a[i]*b[j]
        for i in (4, 3):
            c[i-2] += c[i]
            c[i-3] += c[i]
        return sum((c[i] % 3)*3**i for i in range(3))
    @classmethod
    def power(cls, x, n):
        z = 1
        while n:
            if n & 1:
                z = cls.mul(z, x)
            x = cls.mul(x, x)
            n >>= 1
        return z
    @classmethod
    def inverse(cls, x):
        assert x != 0
        return cls.power(x, 25)


class F729:
    order = 729
    @staticmethod
    def add(x, y):
        return F27.add(x % 27, y % 27)+27*F27.add(x//27, y//27)
    @staticmethod
    def neg(x):
        return F27.neg(x % 27)+27*F27.neg(x//27)
    @staticmethod
    def mul(x, y):
        a, b, c, d = x % 27, x//27, y % 27, y//27
        return F27.add(F27.mul(a, c), F27.neg(F27.mul(b, d)))+27*F27.add(F27.mul(a, d), F27.mul(b, c))
    @classmethod
    def power(cls, x, n):
        z = 1
        while n:
            if n & 1:
                z = cls.mul(z, x)
            x = cls.mul(x, x)
            n >>= 1
        return z
    @staticmethod
    def inverse(x):
        assert x != 0
        a, b = x % 27, x//27
        inv = F27.inverse(F27.add(F27.mul(a, a), F27.mul(b, b)))
        return F27.mul(a, inv)+27*F27.neg(F27.mul(b, inv))
    @staticmethod
    def conjugate(x):
        return x % 27+27*F27.neg(x//27)


assert all((i**3-i-1) % 3 != 0 for i in range(3))
assert F27.power(3, 3) == F27.add(3, 1)
assert F27.power(2, 13) == 2  # -1 is a nonsquare in F27.
for F in (F27, F729):
    assert all(F.power(x, F.order) == x for x in range(F.order))
    assert all(F.mul(x, F.inverse(x)) == 1 for x in range(1, F.order))
assert all(F729.power(x, 27) == F729.conjugate(x) for x in range(729))


def cpoints(F, elements):
    table = defaultdict(list)
    for y in elements:
        table[F.add(F.power(y, 3), F.neg(y))].append(y)
    return [(x, y) for x in elements for y in table[F.power(x, 4)]] + [None]


C27 = cpoints(F27, range(27))
C729 = cpoints(F729, range(729))
C3 = cpoints(F27, range(3))
C9 = cpoints(F729, [a+27*b for a in range(3) for b in range(3)])
assert [len(C3), len(C9), len(C27), len(C729)] == [4, 4, 28, 676]


def eadd(F, A, B):
    if A is None:
        return B
    if B is None:
        return A
    x, y = A
    u, v = B
    if x == u and F.add(y, v) == 0:
        return None
    if A == B:
        numerator, denominator = F.neg(1), F.add(y, y)
    else:
        numerator, denominator = F.add(v, F.neg(y)), F.add(u, F.neg(x))
    m = F.mul(numerator, F.inverse(denominator))
    z = F.add(F.add(F.mul(m, m), F.neg(x)), F.neg(u))
    w = F.add(F.mul(m, F.add(x, F.neg(z))), F.neg(y))
    return z, w


def emul(F, n, A):
    if n < 0:
        return emul(F, -n, None if A is None else (A[0], F.neg(A[1])))
    B = None
    while n:
        if n & 1:
            B = eadd(F, B, A)
        A = eadd(F, A, A)
        n >>= 1
    return B


E27 = [None] + [(u, v) for u in range(27) for v in range(27)
               if F27.mul(v, v) == F27.add(F27.power(u, 3), F27.neg(u))]
assert len(E27) == 28
G = next(emul(F27, 4, A) for A in E27 if emul(F27, 4, A) is not None)
dlog = {emul(F27, i, G): i for i in range(7)}
assert len(dlog) == 7 and emul(F27, 7, G) is None
chi = {A: dlog[emul(F27, 4, A)] for A in E27}
for A in E27:
    for B in E27:
        assert eadd(F27, A, B) in E27
        assert chi[eadd(F27, A, B)] == (chi[A]+chi[B]) % 7


def tau_e(A):
    return None if A is None else (F27.add(A[0], 1), A[1])


eigenvalues = {(chi[tau_e(A)]*pow(chi[A], -1, 7)) % 7 for A in E27 if chi[A]}
assert len(eigenvalues) == 1
u = eigenvalues.pop()
assert u in (2, 4) and pow(u, 3, 7) == 1 and u != 1
assert all(chi[tau_e(A)] == u*chi[A] % 7 for A in E27)


def pi(F, P):
    return None if P is None else (P[1], F.mul(P[0], P[0]))


P = (1, 3)  # (x,y)=(1,t), with t^3-t=1.
assert P in C27
R = pi(F27, P)
h = chi[R]
assert h != 0
a = ((u-1)*h) % 7
assert a != 0
tau_P = (P[0], F27.add(P[1], 1))
assert tau_P in C27
assert chi[eadd(F27, pi(F27, tau_P), emul(F27, -1, R))] == a
eps = (-4*h) % 7
point_rows = []
c1 = [0]*7
for Q in C27:
    exponent = (chi[pi(F27, Q)]-h) % 7
    c1[exponent] += 1
    point_rows.append({'point': Q, 'elliptic_image': pi(F27, Q), 'pointed_character': exponent})

c2 = [0]*7
for i, row in enumerate(point_rows):
    for row2 in point_rows[i:]:
        c2[(row['pointed_character']+row2['pointed_character']) % 7] += 1
degree2_rows = []
for Q in C729:
    if Q is None:
        continue
    Qbar = tuple(F729.conjugate(v) for v in Q)
    if Q >= Qbar:
        continue
    norm = eadd(F729, pi(F729, Q), pi(F729, Qbar))
    assert norm is None or all(v < 27 for v in norm)
    assert norm in E27
    exponent = (chi[norm]-2*h) % 7
    c2[exponent] += 1
    degree2_rows.append({'point': Q, 'conjugate': Qbar, 'elliptic_norm': norm, 'pointed_character': exponent})
assert len(degree2_rows) == 324
assert sum(c1) == 28 and sum(c2) == 730

# Full degree-four factor from genus-three Riemann--Roch reciprocity.
coeff = [[0]*7 for _ in range(5)]
coeff[0][0] = 1
coeff[1] = c1
coeff[2] = c2
for j, count in enumerate(c1):
    coeff[3][(eps-j) % 7] += 27*count
coeff[4][eps] = 27**2
value = [sum(coeff[d][j] for d in range(5)) for j in range(7)]
z, T, X = sp.symbols('z T X')
phi = sum(z**i for i in range(7))
valuepoly = sum(value[i]*z**i for i in range(7))
relative = int(sp.resultant(phi, valuepoly, z))
assert relative > 0 and relative % 3 != 0
modgcd = sp.Poly(sp.gcd(sp.Poly(phi, z, modulus=3), sp.Poly(valuepoly, z, modulus=3)), z, modulus=3)
assert modgcd.degree() == 0

# Independent exact norm as the determinant of multiplication on Z[z]/Phi7.
columns = []
for j in range(6):
    r = sp.Poly(sp.rem(valuepoly*z**j, phi, z), z)
    columns.append([r.nth(i) for i in range(6)])
matrix = sp.Matrix(6, 6, lambda i, j: columns[j][i])
assert int(matrix.det()) == relative
L = sum(sum(coeff[d][j]*z**j for j in range(7))*T**d for d in range(5))
relative_zeta = sp.Poly(sp.resultant(phi, L, z), T)
assert relative_zeta.degree() == 24
assert int(relative_zeta.eval(1)) == relative

twist_records = []
imaginary_unit = 1+2*(z+z**2+z**4)
assert sp.Poly(sp.rem(sp.expand(imaginary_unit**2+1),phi,z),z,modulus=3).is_zero
for twist in range(7):
    value_twist = [0]*7
    for d in range(5):
        for j in range(7):
            value_twist[(j+d*twist) % 7] += coeff[d][j]
    polynomial = sum(value_twist[j]*z**j for j in range(7))
    twist_norm = int(sp.resultant(phi, polynomial, z))
    assert twist_norm > 0 and twist_norm % 3 != 0
    twist_columns = []
    for j in range(6):
        r = sp.Poly(sp.rem(polynomial*z**j,phi,z),z)
        twist_columns.append([r.nth(i) for i in range(6)])
    assert int(sp.Matrix(6,6,lambda i,j:twist_columns[j][i]).det()) == twist_norm
    reduced = sp.Poly(sp.rem(polynomial, phi, z), z, modulus=3)
    beta = sp.Poly(sp.rem(imaginary_unit*z**((twist-1)%7),phi,z),z,modulus=3)
    expected = sp.Poly((1-beta.as_expr()*T)**2,T)
    for d in range(5):
        actual_coefficient = sum(coeff[d][j]*z**((j+d*twist)%7) for j in range(7))
        error = sp.rem(sp.expand(actual_coefficient-expected.nth(d)),phi,z)
        assert sp.Poly(error,z,modulus=3).is_zero
    order = 4 if twist == 1 else 28
    def beta_power(n):
        result = sp.Poly(1,z,modulus=3)
        base = beta
        modulus = sp.Poly(phi,z,modulus=3)
        while n:
            if n & 1:
                result = (result*base).rem(modulus)
            base = (base*base).rem(modulus)
            n >>= 1
        return result
    assert beta_power(order) == sp.Poly(1,z,modulus=3)
    for divisor_prime in ((2,) if order == 4 else (2,7)):
        assert beta_power(order//divisor_prime) != sp.Poly(1,z,modulus=3)
    twist_records.append({
        'twist': twist,
        'value_coefficients': value_twist,
        'reduced_value_mod3': [int(reduced.nth(j)) % 3 for j in range(6)],
        'relative_class_number': twist_norm,
        'nonzero_frobenius_eigenvalue_order_mod3': order,
        'extension_degree_unit_condition': f'{order} does not divide n',
    })
assert twist_records[1]['reduced_value_mod3'] == [1,2,2,0,2,0]

base_poly_3 = (X**2-3)**2*(X**2+3)
base_poly_9 = sp.Poly(sp.resultant(base_poly_3, T-X**2, X), T)
base_poly_27 = sp.Poly(sp.resultant(base_poly_3, T-X**3, X), T)
assert int(base_poly_3.subs(X,1)) == 16
assert sp.expand(base_poly_9.as_expr()-(T-3)**4*(T+3)**2) == 0
assert int(base_poly_9.eval(1)) == 256
assert sp.expand(base_poly_27.as_expr()-(T*T-27)**2*(T*T+27)) == 0
base_class_number = (1-27)**2*(1+27)
assert base_class_number == 18928
original_shifts = []
for Q in C3:
    tau_Q = None if Q is None else (Q[0],F27.add(Q[1],1))
    image = pi(F27,Q)
    shift = chi[eadd(F27,pi(F27,tau_Q),emul(F27,-1,image))]
    assert chi[image] == 0 and shift == 0
    original_shifts.append(shift)

out = {
    'verified': True,
    'base_field': 'F27=F3[t]/(t^3-t-1), encoded a+3*b+9*c',
    'quadratic_field': 'F729=F27[s]/(s^2+1), encoded a+27*b',
    'curve': 'y^3-y=x^4; smooth plane quartic Y^3 Z-Y Z^3=X^4',
    'marking': P,
    'marking_expression': '(x,y)=(1,t), not defined over F3',
    'automorphism': '(x,y)->(x,y+1)',
    'elliptic_curve': 'v^2=u^3-u',
    'elliptic_map': '(u,v)=(y,x^2)',
    'elliptic_points': E27,
    'elliptic_generator_for_dlog': G,
    'elliptic_character_table': [chi[A] for A in E27],
    'elliptic_addition_table': [[E27.index(eadd(F27,A,B)) for B in E27] for A in E27],
    'eigenvalue_u': u,
    'marking_image_character_h': h,
    'automorphism_shift_character_a': a,
    'canonical_character_epsilon': eps,
    'possibly_bad_twist': a*pow(u-1,-1,7) % 7,
    'point_counts': {'F3':len(C3),'F9':len(C9),'F27':len(C27),'F729':len(C729)},
    'degree1_rows': point_rows,
    'degree2_closed_point_rows': degree2_rows,
    'degree1_occupancies': c1,
    'degree2_effective_divisor_occupancies': c2,
    'character_factor_coefficients': coeff,
    'character_value_at_one_coefficients': value,
    'relative_zeta_numerator_low_to_high': [int(relative_zeta.nth(i)) for i in range(25)],
    'relative_class_number': relative,
    'all_constant_twists': twist_records,
    'base_class_number': base_class_number,
    'cover_class_number': base_class_number*relative,
    'cover_degree': 7,
    'cover_genus': 15,
    'original_F3_pointings': C3,
    'original_F3_shift_characters': original_shifts,
    'original_F3_pointings_at_F27_twist': 1,
    'original_F3_field_first_minimum': {'degree_over_F3':3,'least_prime_at_that_field':7},
    'base_class_numbers_first_three_fields': [16,256,18928],
    'scope': 'Finite certificate for this quartic, all its F27 pointings, and all twists of the specified character. The original F3 pointings have field-first minimum(degree3,prime7). This does not give the least prime over arbitrary extension degrees, the complete B6 census, or universal B1.',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS field and point counts: C(F3,F9,F27,F729)=4,4,28,676')
print('PASS E(F27) order28; character eigenvalue', u, 'h=', h, 'a=', a, 'epsilon=', eps)
print('PASS degree1 occupancies', c1, 'degree2 occupancies', c2)
print('PASS exact relative class number', relative, 'mod3=', relative%3)
print('PASS #J_C(F27)=',base_class_number,'#J_D(F27)=',base_class_number*relative)
print('PASS all seven twist norms:', [row['relative_class_number'] for row in twist_records])
print('PASS exact extension tests: twist1 has unit-root order4; every other twist has unit-root order28')
print('Scope: original F3 markings are certified at F27 by the separate twist calculation, not the nonzero-shift criterion')
