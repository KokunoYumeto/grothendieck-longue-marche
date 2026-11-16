#!/usr/bin/env python3
"""Exact finite checks for A.87; no finite computation constructs a section."""

from itertools import product
from math import comb
import sympy as sp


def vp(n, p):
    if n == 0:
        return float("inf")
    n = abs(int(n))
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def mm(a, b):
    return ((a[0]*b[0]+a[1]*b[2]) % 3,
            (a[0]*b[1]+a[1]*b[3]) % 3,
            (a[2]*b[0]+a[3]*b[2]) % 3,
            (a[2]*b[1]+a[3]*b[3]) % 3)


identity = (1, 0, 0, 1)
upper, lower = (1, 1, 0, 1), (1, 0, 1, 1)
sl2 = {a for a in product(range(3), repeat=4)
       if (a[0]*a[3]-a[1]*a[2]) % 3 == 1}
generated = {identity}
while True:
    enlarged = generated | {mm(a, g) for a in generated for g in (upper, lower)}
    if enlarged == generated:
        break
    generated = enlarged
assert len(sl2) == 24 and generated == sl2
assert mm(mm(upper, upper), upper) == identity
assert mm(mm(lower, lower), lower) == identity
assert upper != identity and lower != identity

# Derived subgroup: its quotient has order3, independently checking no index2 subgroup.
inverse = {a: next(b for b in sl2 if mm(a, b) == identity) for a in sl2}
commutators = {mm(mm(mm(a, b), inverse[a]), inverse[b]) for a in sl2 for b in sl2}
derived = {identity}
while True:
    enlarged = derived | {mm(a, b) for a in derived for b in commutators}
    if enlarged == derived:
        break
    derived = enlarged
assert len(derived) == 8

u, X, Y = sp.symbols("u X Y")
twisted_cubic = (4*X)*(4*X+1)*(4*X+16*u)
assert sp.expand(((8*Y+4*X)**2-twisted_cubic)/64
                 -(Y**2+X*Y-X**3-4*u*X**2-u*X)) == 0
b2, b4, b6, b8 = 1+16*u, 2*u, 0, -u*u
good_delta = sp.expand(-b2*b2*b8-8*b4**3-27*b6**2+9*b2*b4*b6)
assert sp.expand(good_delta-u*u*(1-16*u)**2) == 0

model_count = 0
for a in range(-255, 256, 2):
    for c4, c6, delta in (
        (16*(16*a*a-4*a+1), 64*(4*a+1)*(8*a-1)*(2*a-1),
         256*a*a*(1-4*a)**2),
        (16*(16*a*a-4*a+1), -64*(4*a+1)*(8*a-1)*(2*a-1),
         256*a*a*(1-4*a)**2),
        (16*(a*a-4*a+16), 64*(a+4)*(a-2)*(a-8),
         256*a*a*(a-4)**2),
    ):
        assert (vp(c4, 2), vp(c6, 2), vp(delta, 2)) == (4, 6, 8)
        assert (delta//256) % 8 == 1
        model_count += 1
    assert int(good_delta.subs(u, a)) % 2 == 1

dyadic_labels = {}
for a in (1, 3, 5, 7):
    target = (a, 5)
    labels = set()
    for z in (1, 3, 5, 7):
        if (z, (1-4*z) % 8) == target:
            labels.add(0)
        if ((1-4*z) % 8, z) == target:
            labels.add(1)
        if (z, (4-z) % 8) == target:
            labels.add("infinity")
    dyadic_labels[a] = labels
assert dyadic_labels == {1: {0}, 3: {0}, 5: {0, 1}, 7: {0, "infinity"}}


def mul(a, b, degree):
    c = [0]*(degree+1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j <= degree:
                c[i+j] += x*y
    return c


def inv(a, degree):
    b = [1]+[0]*degree
    assert a[0] == 1
    for k in range(1, degree+1):
        b[k] = -sum(a[i]*b[k-i] for i in range(1, k+1))
    return b


def evaluate(a, x, modulus):
    v = 0
    for c in reversed(a):
        v = (v*x+c) % modulus
    return v


def log_unit(a, p, precision):
    modulus = p**precision
    z = (pow(a, p-1, modulus)-1) % modulus
    if not z:
        return 0
    depth = vp(z, p)
    result = 0
    for n in range(1, p*precision+5):
        d = vp(n, p)
        if n*depth-d < precision:
            term = (z**n//p**d)*pow(n//p**d, -1, modulus)
            result = (result+(-1)**(n+1)*term) % modulus
    return result*pow(p-1, -1, modulus) % modulus


precision = 7
log3_2 = log_unit(2, 3, 2)
assert log3_2 == 6
weighted_count = 0
for prime in (2, 5, 7, 11, 13, 17, 19):
    L = log_unit(prime, 3, 2)
    for weight in range(1, 10):
        for unit in (1, 2, 4, 5, 7, 8):
            assert ((weight*unit*unit-weight)*L) % 9 == 0
            weighted_count += 1
for dA, dB in ((0, 2), (-2, -2)):
    assert ((dA-2)*log3_2) % 9 != 0
    assert (dB*log3_2) % 9 != 0
    assert (dA % 8, dB % 8) != (2, 0)
for exponent in range(1, 121):
    lam = 3**exponent+1
    if exponent % 2:
        assert vp(lam, 2) == 2
        assert (lam//4) % 8 in (1, 3) or lam % 9 == 1
    else:
        assert vp(lam, 2) == 1
L52, L53 = log_unit(2, 5, precision), log_unit(3, 5, precision)
assert (L52 % 25, L53 % 25) == (10, 20)
x5 = (-L52//5)*pow(L53//5, -1, 5**(precision-1)) % 5**(precision-1)
assert x5 % 5 == 2 and pow(x5 % 5, 2, 5) == 4

degree = 12
e4 = [1]+[240*sum(d**3 for d in range(1, n+1) if n % d == 0)
           for n in range(1, degree+1)]
delta = [1]+[0]*degree
for n in range(1, degree+1):
    factor = [0]*(degree+1)
    for k in range(min(24, degree//n)+1):
        factor[n*k] = (-1)**k*comb(24, k)
    delta = mul(delta, factor, degree)
phi = mul(mul(mul(e4, e4, degree), e4, degree), inv(delta, degree), degree)
assert phi[:5] == [1, 744, 196884, 21493760, 864299970]

p, w, modulus = 7, -35, 7**(precision+2)
numerator = 256*(w*w-w+1)**3
denominator = w*w*(1-w)**2
q = 0
for _ in range(precision+4):
    q = denominator*evaluate(phi, q, modulus)*pow(numerator, -1, modulus) % modulus
assert (numerator*q-denominator*evaluate(phi, q, modulus)) % modulus == 0
assert vp(q, 7) == 2
unit_q = q//49
F = 256*unit_q*pow((w//7)**2, -1, 7**precision) % 7**precision
LF = log_unit(F, 7, precision)
Lq = log_unit(unit_q, 7, precision)
L72, L75 = log_unit(2, 7, precision), log_unit(5, 7, precision)
assert (L72//7 % 7, L75//7 % 7) == (5, 1)
assert F % 49 == (1+w) % 49 and LF % 49 == w % 49
assert (2*L75-8*L72+LF-Lq) % 7**precision == 0
tangent_log = (2*L75-8*L72) % 7**precision
assert tangent_log//7 % 7 == 4 and Lq//7 % 7 == 6
gamma7 = (tangent_log//7)*pow(Lq//7, -1, 7**(precision-1)) % 7**(precision-1)
assert gamma7 % 7 == 3 and pow(gamma7 % 7, 3, 7) == 6

print("A.87 exact certificate: all checks passed.")
print("SL2(F3): 24 elements, generated by the two order-three unipotents; derived subgroup order8.")
print(f"Checked {model_count} contact-two minimal-invariant triples, all (4,6,8) with normalized discriminant1mod8.")
print("Symbolic contact-four twist and its unit-discriminant good model agree exactly.")
print("Dyadic contact-two labels for prescribed unit classes(u,5):", dyadic_labels)
print(f"Coefficient-three weighted congruence: {weighted_count} checks, including weights divisible3; both alternate dyadic modes contradict the mod9 cusp equations when lambda=0or1mod9.")
print("Checked the exact family/scope arithmetic for 3^n+1, 1<=n<=120; the uniform proof is in A.87.")
print(f"At coefficient5, log2=10 and log3=20 mod25; X5={x5} mod5^6, residue2 nonsquare.")
print(f"At seven, q={q} mod7^9; F={F} mod7^7; log(q/49)={Lq} mod7^7.")
print(f"Tangent/ordinary normalized logarithm residues are4/6; gamma7={gamma7} mod7^6, residue3 nonsquare.")
print("The faithful inertia and primary symplectic theorem remain explicit proof inputs; this is a finite audit, not a section construction.")
