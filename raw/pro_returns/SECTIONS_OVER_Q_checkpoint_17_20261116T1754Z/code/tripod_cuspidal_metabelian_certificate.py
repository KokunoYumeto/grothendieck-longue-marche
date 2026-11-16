#!/usr/bin/env python3
"""Literal order-81 cusp detector and cover checks for A.172.

The global finite-fibre Selmer and compact-conjugator steps are in the
proof.  This script certifies the actual finite group presentation,
the Fermat-cubic elliptic map and its separating local calculation.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json
import sympy as S

# R=Z[zeta_3]/(3(zeta_3-1)) = Z/9 + (Z/3)delta,
# delta^2=-3, 3delta=0.  Elements are (a,b)=a+b delta.
R = list(product(range(9), range(3)))
zero = (0, 0)
one = (1, 0)
delta = (0, 1)
zeta = (1, 1)

def ra(x, y): return ((x[0]+y[0]) % 9, (x[1]+y[1]) % 3)
def rn(x): return ((-x[0]) % 9, (-x[1]) % 3)
def rm(x, y):
    a, b = x; c, d = y
    return ((a*c-3*b*d) % 9, (a*d+b*c) % 3)
def rp(x, e):
    result = one
    for _ in range(e): result = rm(result, x)
    return result

assert rm(delta, delta) == (6, 0)
assert rp(delta, 3) == zero
assert rp(zeta, 3) == one
assert ra(ra(one, zeta), rp(zeta, 2)) == zero
for x, y, z in product(R, repeat=3):
    assert rm(rm(x, y), z) == rm(x, rm(y, z))

# Q=R additively semidirect C3, action multiplication by zeta.
Q = [(a, b, i) for a, b in R for i in range(3)]
identity = (0, 0, 0)
def mul(g, h):
    a, b, i = g; c, d, j = h
    r = ra((a, b), rm(rp(zeta, i), (c, d)))
    return (*r, (i+j) % 3)
def inv(g):
    a, b, i = g
    r = rm(rp(zeta, (-i) % 3), rn((a, b)))
    return (*r, (-i) % 3)
def power(g, n):
    answer = identity
    for _ in range(n): answer = mul(answer, g)
    return answer
def comm(g, h): return mul(mul(mul(g, h), inv(g)), inv(h))
def subgroup(gens):
    gens = tuple(set(gens) | {inv(g) for g in gens})
    answer = {identity}
    todo = deque([identity])
    while todo:
        g = todo.popleft()
        for h in gens:
            gh = mul(g, h)
            if gh not in answer:
                answer.add(gh); todo.append(gh)
    return answer

X = (0, 0, 1)
Y = (1, 0, 1)
assert len(subgroup([X, Y])) == 81
assert power(X, 3) == power(Y, 3) == power(mul(X, Y), 3) == identity
assert comm(X, Y) == (0, 1, 0)
weight_three = comm(comm(X, Y), X)
assert weight_three == (3, 0, 0)

lower = [set(Q)]
while len(lower[-1]) > 1:
    lower.append(subgroup([comm(g, h) for g in lower[-1] for h in Q]))
assert list(map(len, lower)) == [81, 9, 3, 1]
assert lower[1] == {(a, b, 0) for a in (0, 3, 6) for b in range(3)}
assert all(power(g, 3) == identity for g in lower[1])

# The further quotient by Gamma3 is the literal Heisenberg group of
# order27: reduce the constant ring coordinate modulo3.
Q27 = list(product(range(3), repeat=3))
def q27(g): return (g[0] % 3, g[1], g[2])
def m27(g, h): return q27(mul(g, h))
assert len({q27(g) for g in Q}) == 27
assert {g for g in Q if q27(g) == identity} == lower[2]
for g, h in product(Q, repeat=2):
    assert q27(mul(g, h)) == m27(q27(g), q27(h))
comm27 = {q27(comm(g, h)) for g, h in product(Q, repeat=2)}
assert len(comm27) == 3
assert all(m27(c, g) == m27(g, c) for c in comm27 for g in Q27)
assert q27(comm(X, Y)) != identity

# This is the exact abelian exponent map for x->X,y->Y.
# Its inverse sends (a mod3,i) to (i-a,a), the x/y exponents.
def ab(g):
    a, b, i = g
    return ((i-a) % 3, a % 3)
assert ab(X) == (1, 0) and ab(Y) == (0, 1)
for g, h in product(Q, repeat=2):
    gh = ab(mul(g, h)); ag, ah = ab(g), ab(h)
    assert gh == tuple((ag[j]+ah[j]) % 3 for j in range(2))
assert {g for g in Q if ab(g) == (0, 0)} == lower[1]

# Every compactified boundary generator is a conjugate of one of
# these three powers.  All are killed in the literal quotient.
boundary_checks = 0
for i, j in product(range(3), repeat=2):
    g = mul(power(X, i), power(Y, j))
    for inertia in (power(X, 3), power(Y, 3), power(mul(X, Y), 3)):
        assert mul(mul(g, inertia), inv(g)) == identity
        boundary_checks += 1

# Fermat cubic: U^3+V^3=Z^3, origin (1:-1:0).
# Xell=12Z/(U+V), Yell=36(U-V)/(U+V), inverse on Z=1.
U, V, Z, xe, ye = S.symbols('U V Z xe ye')
xe_map = 12*Z/(U+V)
ye_map = 36*(U-V)/(U+V)
equation_num = S.fraction(S.factor(ye_map**2-xe_map**3+432))[0]
assert S.factor(equation_num.subs(Z**3, U**3+V**3)) == 0
uinv = (36+ye)/(6*xe)
vinv = (36-ye)/(6*xe)
inverse_num = S.fraction(S.factor(uinv**3+vinv**3-1))[0]
assert S.factor(inverse_num.subs(ye**2, xe**3-432)) == 0
assert S.factor((12/(uinv+vinv))-xe) == 0
assert S.factor(36*(uinv-vinv)/(uinv+vinv)-ye) == 0
assert (xe_map.subs({U: 0, V: 1, Z: 1}),
        ye_map.subs({U: 0, V: 1, Z: 1})) == (12, -36)
assert (xe_map.subs({U: 1, V: 0, Z: 1}),
        ye_map.subs({U: 1, V: 0, Z: 1})) == (12, 36)
assert 36**2 == 12**3-432
assert (3*12**2)//(2*36) == 6
assert 6**2-2*12 == 12
assert 6*(12-12)-36 == -36

# Exact degree-three isogenies and the projected Kummer character.
# Work literally in the function fields of the two elliptic curves.
xx, yy, XX, YY = S.symbols('xx yy XX YY')
phix = (xx**3-1728)/xx**2
phiy = yy*(xx**3+3456)/xx**3
psix = (XX**3+46656)/(9*XX**2)
psiy = YY*(XX**3-93312)/(27*XX**3)
def curve_reduce(expr, xv, yv, rhs):
    numerator = S.together(expr).as_numer_denom()[0]
    return S.factor(S.rem(numerator, yv**2-rhs, yv))
assert curve_reduce(phiy**2-phix**3-11664, xx, yy, xx**3-432) == 0
assert curve_reduce(psiy**2-psix**3+432, XX, YY, XX**3+11664) == 0
assert S.factor(S.diff(phix, xx)*yy-phiy) == 0
assert S.factor(S.diff(psix, XX)*YY-3*psiy) == 0
assert (phix.subs(xx, 12), phiy.subs({xx: 12, yy: 36})) == (0, 108)

# The composition equals the literal tangent-and-chord tripling map.
double_slope = 3*xx**2/(2*yy)
double_x = double_slope**2-2*xx
double_y = double_slope*(xx-double_x)-yy
triple_slope = (double_y-yy)/(double_x-xx)
triple_x = triple_slope**2-double_x-xx
triple_y = triple_slope*(xx-triple_x)-yy
composition_x = psix.subs(XX, phix)
composition_y = psiy.subs({XX: phix, YY: phiy}, simultaneous=True)
assert curve_reduce(composition_x-triple_x, xx, yy, xx**3-432) == 0
assert curve_reduce(composition_y-triple_y, xx, yy, xx**3-432) == 0

u = S.symbols('u')
f = u**3-3*u**2+1
def cubic_reduce(expr):
    numerator, denominator = S.together(expr).as_numer_denom()
    return S.rem(numerator*S.invert(denominator, f), f, u)
Qx = 36*u
Qy = 108*(2*u**2-2*u-1)
assert S.discriminant(f, u) == 81
assert all(f.subs(u, t) != 0 for t in (-1, 1))
assert cubic_reduce(Qy**2-Qx**3-11664) == 0
assert cubic_reduce(psix.subs(XX, Qx)-12) == 0
assert cubic_reduce(psiy.subs({XX: Qx, YY: Qy}, simultaneous=True)-36) == 0
sigma_u = -u**2+2*u+2
assert cubic_reduce(f.subs(u, sigma_u)) == 0
assert cubic_reduce(sigma_u.subs(u, sigma_u).subs(u, sigma_u)-u) == 0
slope_R = cubic_reduce((Qy-108)/Qx)
plus_R_x = cubic_reduce(slope_R**2-Qx)
plus_R_y = cubic_reduce(slope_R*(Qx-plus_R_x)-Qy)
assert cubic_reduce(plus_R_x-36*sigma_u) == 0
assert cubic_reduce(plus_R_y-Qy.subs(u, sigma_u)) == 0

# u=1-(zeta9+zeta9^-1), and sigma2 acts by the displayed polynomial.
z9 = S.symbols('z9')
cyclo9 = z9**6+z9**3+1
invz9 = S.invert(z9, cyclo9)
u_zeta = 1-z9-invz9
assert S.rem(S.expand(f.subs(u, u_zeta)), cyclo9, z9) == 0
u_sigma = 1-z9**2-invz9**2
assert S.rem(S.expand(u_sigma-sigma_u.subs(u, u_zeta)), cyclo9, z9) == 0
cyclotomic_character = {a: ((a*a % 9)-1)//3 for a in (1, 2, 4, 5, 7, 8)}
assert cyclotomic_character[2] == 1 and cyclotomic_character[5] == 2
for a, b in product(cyclotomic_character, repeat=2):
    assert cyclotomic_character[(a*b) % 9] == (cyclotomic_character[a]+cyclotomic_character[b]) % 3

# The global 3-primary central class has the literal nonintegral
# cobounding scalar 1/24.  At any prime different from3, a residue
# degree f gives q=p^f; its unramified value has exact order3 in
# Z3/(q^2-1).  These finite checks accompany, not replace, the
# all-local-field nonintegral-scalar argument in the proof.
local_central_checks = []
def v3(n):
    e = 0
    while n % 3 == 0:
        n //= 3; e += 1
    return e
for prime in list(S.primerange(2, 101)):
    p0 = int(prime)
    if p0 == 3: continue
    for residue_degree in range(1, 13):
        q = p0**residue_degree
        e = v3(q*q-1)
        modulus = 3**e
        eta = ((q*q-1)//3)*pow(8, -1, modulus) % modulus
        assert eta and 3*eta % modulus == 0
        assert v3(eta) == e-1
        assert all(k*eta % modulus for k in (1, 2))
        local_central_checks.append([p0, residue_degree, e, eta])
for depth in range(1, 13):
    for sign in (-1, 1):
        chi = sign*(1+3**depth)
        e = v3(chi*chi-1)
        modulus = 3**e
        eta = ((chi*chi-1)//3)*pow(8, -1, modulus) % modulus
        assert e == depth and eta and 3*eta % modulus == 0
        local_central_checks.append(['coefficient3', sign, depth, eta])

# Good reduction at five.  The three boundary points remain distinct
# and every nonzero difference is outside 3E(F5).
p = 5
points = [None] + [(x, y) for x, y in product(range(p), repeat=2)
                   if (y*y-x*x*x+432) % p == 0]
assert len(points) == 6
def add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x, y = P; u, v = Q
    if x == u and (y+v) % p == 0: return None
    slope = ((v-y)*pow(u-x, -1, p) if x != u
             else 3*x*x*pow(2*y, -1, p)) % p
    xx = (slope*slope-x-u) % p
    yy = (slope*(x-xx)-y) % p
    return (xx, yy)
def neg(P): return None if P is None else (P[0], -P[1] % p)
def emul(P, k):
    ans = None
    for _ in range(k): ans = add(ans, P)
    return ans
boundary_points = {'P0': (2, 4), 'P1': (2, 1), 'Pinf': None}
three_image = {emul(P, 3) for P in points}
assert len(three_image) == 2
differences = []
for (name, P), (other, Qp) in product(boundary_points.items(), repeat=2):
    if name == other: continue
    difference = add(P, neg(Qp))
    assert difference is not None
    assert emul(difference, 3) is None
    assert difference not in three_image
    differences.append({'from': name, 'to': other, 'difference': difference})

# Cross-label mod-three coordinate lines meet only at zero.  Since
# -1 is a cube, the infinity line is exactly (c,c) at this level.
lines = [set((a, 0) for a in range(3)),
         set((0, a) for a in range(3)),
         set((a, a) for a in range(3))]
for i in range(3):
    for j in range(i): assert lines[i] & lines[j] == {(0, 0)}
fixed_decks = [(a, b) for a, b in product(range(3), repeat=2)
               if ((-a) % 3, (-b) % 3) == (a, b)]
assert fixed_decks == [(0, 0)]

# Actual Fermat twists used in the compactness proof, retaining a
# rational boundary point for each possible cuspidal coordinate row.
A, B, z = S.symbols('A B z', nonzero=True)
tower_rows = []
for level in range(3, 13):
    assert (A*U**level+V**level-Z**level).subs({U: 0, V: 1, Z: 1}) == 0
    assert (U**level+B*V**level-Z**level).subs({U: 1, V: 0, Z: 1}) == 0
    assert (A*U**level-A*V**level-Z**level).subs({U: 1, V: 1, Z: 0}) == 0
    genus = (level-1)*(level-2)//2
    assert 2*genus-2 == -2*level**2+3*level*(level-1)
    tower_rows.append({'n': level, 'degree': level**2,
                       'genus': genus, 'geometric_boundary_points': 3*level})

data = {
    'group_order': 81, 'lower_central_orders': list(map(len, lower)),
    'nilpotency_class': 3, 'X': X, 'Y': Y,
    'nonzero_weight_three_commutator': weight_three,
    'compact_kernel_order': 9, 'compact_kernel_exponent': 3,
    'boundary_conjugate_checks': boundary_checks,
    'fermat_cubic_elliptic_model': 'y^2=x^3-432',
    'residue_prime': p, 'elliptic_reduction_points': points,
    'boundary_reductions': boundary_points,
    'image_of_three': sorted(three_image, key=str),
    'six_nondivisible_differences': differences,
    'arithmetic_fixed_decks_at_five': fixed_decks,
    'smaller_group_order': 27, 'smaller_nilpotency_class': 2,
    'projected_kummer_cubic': str(f),
    'projected_kummer_point': [str(Qx), str(Qy)],
    'cyclotomic_cubic_character': cyclotomic_character,
    'central_local_scalar_checks': local_central_checks,
    'fermat_tower_rows': tower_rows,
    'status': 'all exact finite checks passed',
    'scope': 'The complete cuspidal fibres use the global Selmer and compactness proof in A172.',
}
path = Path(__file__).with_name('tripod_cuspidal_metabelian_certificate_data.json')
path.write_text(json.dumps(data, indent=2)+'\n')
print('PASS: literal ring and group of order81; X,Y generate; all three boundary powers vanish')
print('PASS: lower central orders81,9,3,1; exact class3 and nonzero weight-three word')
print('PASS: standard x/y abelian exponent map; kernel C3^2;27 boundary conjugates')
print('PASS: Fermat-cubic elliptic map and its inverse; boundary points are O and ±(12,36)')
print('PASS: six reduction points at5; all six nonzero boundary differences fail3-divisibility')
print('PASS: pairwise intersections of the three mod3 cusp lines and zero fixed deck group')
print('PASS: actual class2 quotient of order27 and its nonzero central commutator')
print('PASS: both literal degree-three isogenies, their composition and the cubic Kummer preimage')
print('PASS: sigma2 sends the preimage to itself+(0,108); exact character (chi9^2-1)/3')
print('PASS:', len(local_central_checks), 'local scalar checks for the full pro3 central class')
print('PASS: ten actual cuspidal Fermat twists, rational boundary points and genus identities')
print('Data:', path)
