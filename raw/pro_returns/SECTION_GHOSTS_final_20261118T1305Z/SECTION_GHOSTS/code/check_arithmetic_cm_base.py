"""Independent finite and algebraic checks for E95--E97.

These verify the finite CM conditions, exact Legendre twists, actual division
points and all prescribed reflection matrices at seven composite moduli.
They do not replace the path comparison or compactness proof.
"""
from itertools import product
from pathlib import Path
from math import gcd, prod
import json
import sympy as sp

I = (1, 0, 0, 1)
U = (1, 1, 0, 1)
L = (1, 0, -1, 1)
D = (0, 1, 1, 0)

def red(a, n):
    return tuple(x % n for x in a)

def mul(a, b, n):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % n
                 for i in range(2) for j in range(2))

def det(a, n):
    return (a[0]*a[3]-a[1]*a[2]) % n

def inv(a, n):
    u = pow(det(a, n), -1, n)
    return tuple(u*x % n for x in (a[3], -a[1], -a[2], a[0]))

def power(a, e, n):
    if e < 0:
        return power(inv(a, n), -e, n)
    result = I
    while e:
        if e & 1:
            result = mul(result, a, n)
        a = mul(a, a, n)
        e //= 2
    return result

def conj(a, b, n):
    return mul(mul(a, b, n), inv(a, n), n)

S = (0, 1, -1, 0)
R = (0, -1, 1, -1)
X = power(U, 2, 3)
SL3 = [a for a in product(range(3), repeat=4) if det(a, 3) == 1]
epsilon = {I: 0}
queue = [I]
while queue:
    a = queue.pop()
    for g in [power(U, 2, 3), power(L, 2, 3)]:
        b = mul(a, g, 3)
        value = (epsilon[a]+1) % 3
        if b in epsilon:
            assert epsilon[b] == value
        else:
            epsilon[b] = value
            queue.append(b)
assert len(epsilon) == len(SL3) == 24
good = set()
for g in SL3:
    f = mul(conj(S, g, 3), inv(g, 3), 3)
    cube = power(mul(inv(f, 3), R, 3), 3, 3)
    assert cube in {I, red((-1, 0, 0, -1), 3)}
    if cube == I:
        good.add(g)
        k = epsilon[g]
        assert f == red((1, k, k, 1+k*k), 3)
assert good == {mul(power(X, k, 3), power(S, j, 3), 3)
                for k in range(3) for j in range(4)}
assert len(good) == 12

B = (9, 4, 8, 9)
assert red(B, 4) == I
assert power(B, 2, 12) == (5, 0, 0, 5)
assert power(B, 4, 12) == I
assert red(B, 3) in {red(S, 3), inv(S, 3)}
assert power((5, 0, 0, 5), 2, 12) == I
for j in range(3):
    t = red(tuple(-x for x in power(R, j, 3)), 3)
    assert power(t, 3, 3) == red((-1, 0, 0, -1), 3)

# Exact twists of the specified Legendre fibres.
x, z, lam = sp.symbols("x z lam")
assert sp.expand(64*x*(x-1)*(x-sp.Rational(1, 2))
                 - ((4*x-2)**3-4*(4*x-2))) == 0
d = -(2*lam-1)/3
shifted = sp.expand((z+(1+lam)/3)*(z+(1+lam)/3-1)
                    *(z+(1+lam)/3-lam)-z**3-d**3)
assert sp.rem(shifted, lam**2-lam+1, lam) == 0
assert sp.rem(sp.expand(d*(2*lam-1)-1), lam**2-lam+1, lam) == 0

# Literal four-division points on the Gaussian curve.
def double(P, A):
    x0, y0 = P
    slope = (3*x0*x0+A)/(2*y0)
    xx = sp.simplify(slope*slope-2*x0)
    yy = sp.simplify(slope*(x0-xx)-y0)
    return xx, yy

gaussian_halves = [
    (sp.I, 1-sp.I, (0, 0)),
    (-sp.I, 1+sp.I, (0, 0)),
    (1+sp.sqrt(2), 2+sp.sqrt(2), (1, 0)),
    (1-sp.sqrt(2), 2-sp.sqrt(2), (1, 0)),
]
for xx, yy, target in gaussian_halves:
    assert sp.simplify(yy*yy-xx**3+xx) == 0
    assert double((xx, yy), -1) == target

r = sp.symbols("r")
def rem_r(expr):
    numerator, denominator = sp.fraction(sp.cancel(expr))
    assert denominator != 0
    return sp.factor(sp.rem(numerator, r**4-sp.Rational(3, 4), r))

sqrt3 = 2*r*r
P = (-1+sqrt3, sqrt3*(sqrt3-1)*r)
assert rem_r(P[1]**2-P[0]**3-1) == 0
xx, yy = double(P, 0)
assert rem_r(xx+1) == rem_r(yy) == 0
a = (1/r+2*r)/2
b = (1/r-2*r)/(2*sp.I)
for u in [a, b]:
    assert rem_r(3*u**4-6*u**2-1) == 0
    assert sp.simplify(u.subs(r, -r)+u) == 0
assert rem_r(sqrt3*a*b-sp.I) == 0

def prime_powers(n):
    out = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            q = 1
            while n % p == 0:
                q *= p
                n //= p
            out.append((p, q))
        p += 1
    if n > 1:
        out.append((n, n))
    return out

def local_conjugator(T, p, q):
    if p == 2:
        assert red(T, 4) == D
        H0 = (1, T[0], 0, T[2])
        assert det(H0, 4) == 1
    else:
        for v0, v1 in product(range(p), repeat=2):
            H0 = (v0, (T[0]*v0+T[1]*v1) % q,
                  v1, (T[2]*v0+T[3]*v1) % q)
            if gcd(det(H0, q), q) == 1:
                break
        else:
            raise AssertionError("No cyclic vector for reflection")
    delta = det(H0, q)
    if p == 2:
        delta_inv = pow(delta, -1, 2*q)
        v, w = (delta_inv+1)//2, (delta_inv-1)//2
        assert (v % 2, w % 2) == (1, 0)
    else:
        delta_inv = pow(delta, -1, q)
        inv2 = pow(2, -1, q)
        v, w = (delta_inv+1)*inv2, (delta_inv-1)*inv2
    H = mul(H0, (v % q, w % q, w % q, v % q), q)
    assert det(H, q) == 1
    assert conj(H, D, q) == T
    if p == 2:
        assert red(H, 2) == I
    return H

reflection_counts = {}
for n in [12, 24, 48, 60, 84, 120, 132]:
    parts = prime_powers(n)
    count = 0
    for v, w in product(range(n), repeat=2):
        u = (v, -w % n, w, (v-w) % n)
        if det(u, n) != 1 or red(u, 4) != I:
            continue
        count += 1
        assert mul(u, R, n) == mul(R, u, n)
        assert conj(D, u, n) == inv(u, n)
        T = mul(inv(u, n), D, n)
        assert power(T, 2, n) == I
        assert (T[0]+T[3]) % n == 0
        Hs = [local_conjugator(red(T, q), p, q) for p, q in parts]
        def crt(index):
            return sum(H[index]*(n//q)*pow(n//q, -1, q)
                       for H, (p, q) in zip(Hs, parts)) % n
        H = tuple(crt(i) for i in range(4))
        assert det(H, n) == 1 and red(H, 2) == I
        assert conj(H, D, n) == T
    reflection_counts[str(n)] = count

result = {
    "SL2_F3_elements_checked": 24,
    "exact_cubic_condition_solutions": len(good),
    "CM_order_four_matrix_and_two_primary_power": True,
    "Legendre_harmonic_twist_by_two": True,
    "Legendre_equianharmonic_twist_by_inverse_sqrt_minus_three": True,
    "Gaussian_four_division_points_checked": len(gaussian_halves),
    "Mordell_four_division_point_and_Gaussian_third_polynomial": True,
    "pure_reflection_conjugators_by_modulus": reflection_counts,
    "all_checks_passed": True,
    "scope": "Finite equations and exact algebra; marked geometric paths and infinite compactness are proved in E95--E97."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
