"""Finite checks for E.123--E.124, not a numerical ghost construction.

The actual primes supplied by the proof obey a much larger CRT modulus.
This program checks the finite group, local root shells, and parity orders
used in that proof.  It does not replace any Chebotarev existence argument.
"""

from collections import deque
from math import factorial, gcd


def vp(a, p):
    if a == 0:
        return float("inf")
    a = abs(a)
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v


def mul(g, h):
    a, b, c, u = g
    d, e, f, v = h
    return ((a + u*d) % 9, (b + u*e) % 9,
            (c + u*u*f + a*u*e) % 9, (u*v) % 9)


identity = (0, 0, 0, 1)


def power(g, n):
    out = identity
    while n:
        if n & 1:
            out = mul(out, g)
        g = mul(g, g)
        n //= 2
    return out


def inverse(g):
    a, b, c, u = g
    v = pow(u, -1, 9)
    return ((-v*a) % 9, (-v*b) % 9, (v*v*(a*b-c)) % 9, v)


def commutator(g, h):
    return mul(mul(mul(g, h), inverse(g)), inverse(h))


def closure(generators):
    seen = {identity}
    queue = deque([identity])
    while queue:
        g = queue.popleft()
        for h in generators:
            z = mul(g, h)
            if z not in seen:
                seen.add(z)
                queue.append(z)
    return seen


x, y, d = (1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 0, 2)
H = closure([x, y])
G = closure([x, y, d])
derived = closure([commutator(x, y), commutator(d, x),
                   commutator(d, y)])
assert len(H) == 729 and len(G) == 4374
assert derived == H
assert all(power(g, 9) == identity for g in H)
assert all(mul(g, inverse(g)) == identity for g in G)
print("H9 order:", len(H))
print("Arithmetic semidirect group order:", len(G))
print("Derived subgroup order:", len(derived))
print("Arithmetic abelianization order:", len(G)//len(derived))
print("All 729 geometric elements have exponent dividing 9: PASS")


def eta_mod9(u):
    assert u % 3
    return (((u*u - 1)//3) * pow(8, -1, 9)) % 9


units27 = [u for u in range(27) if gcd(u, 27) == 1]
for u in units27:
    for v in units27:
        assert eta_mod9((u*v) % 27) == (
            eta_mod9(u) + u*u*eta_mod9(v)) % 9
assert eta_mod9(8) != eta_mod9(17)
print("Cyclotomic eta cocycle: all 324 unit pairs modulo27 PASS")
print("Same multiplier modulo9, distinct eta:",
      [(u, u % 9, eta_mod9(u)) for u in (8, 17, 26)])


print("Local three-adic root shells (finite precision 3^7):")
print("j f H example v3(R-1) Y_mod_2187 r_mod27 eta_r_mod9")
root_checks = 0
K = 7
for j in range(13):
    n = factorial(j + 7)
    f = vp(n, 3)
    Hbound = 2*vp(factorial(j + 8), 3) + j + 3
    assert Hbound > f + 2
    for label, a, b in (
        ("seed", 3, -2),
        ("error", 3*(1 + 2*3**(Hbound-1))**8, -2),
    ):
        precision = 3**(K + f)
        R = ((1-a*pow(2, n, precision))*pow(b, -1, precision)) % precision
        assert vp(R-1, 3) == f + 2
        roots = [Y for Y in range(1, 3**K, 3)
                 if pow(Y, n, precision) == R]
        assert len(roots) == 1
        Y = roots[0]
        assert vp(Y-1, 3) == 2
        r27 = (-Y) % 27
        assert vp(r27+1, 3) == 2
        assert eta_mod9(r27) in (3, 6)
        assert vp(2*2-1, 3) == 1
        if label == "error":
            assert vp(a+b-1, 3) == Hbound
        root_checks += 1
        print(j, f, Hbound, label, vp(R-1, 3), Y, r27,
              eta_mod9(r27))
print("Root shell checks:", root_checks, "PASS")


parity_checks = 0
for q, e in ((2, 1), (5, 1), (17, 2), (53, 3)):
    assert vp(q*q-1, 3) == e
    for w in range(2, 81):
        if w % 2:
            assert vp(q**w-1, 3) == 0
        else:
            s = 1 + vp(w//2, 3)
            local_exponent = vp(q**w-1, 3)
            assert local_exponent == e + vp(w//2, 3)
            generator_value = (q**w-1)//3**s
            assert vp(generator_value, 3) == e-1
        parity_checks += 1
print("Odd/even local order checks:", parity_checks, "PASS")


def principal_root(R, n, p, K):
    """Unique root in 1+pZp (1+4Z2), to precision p^K.

    R is specified modulo p^(K+v_p(n)); digit lifting retains
    that divided-derivative precision at each step.
    """
    f = vp(n, p)
    start = 2 if p == 2 else 1
    Y = 1
    assert (pow(Y, n, p**(start+f))-R) % p**(start+f) == 0
    for k in range(start, K):
        modulus = p**(k+f+1)
        candidates = [Y+d*p**k for d in range(p)
                      if (pow(Y+d*p**k, n, modulus)-R) % modulus == 0]
        assert len(candidates) == 1
        Y = candidates[0]
    return Y


print("E125 unit-coefficient three-adic shells:")
print("j f H example v3(R-1) Y_mod_2187 r_mod27")
new_root_checks = 0
for j in range(13):
    n = factorial(j + 11)
    f = vp(n, 3)
    Hbound = 2*vp(factorial(j + 12), 3) + j + 3
    precision = 3**(K+f)
    for label, U in (("seed", 1), ("error", 1+110*3**Hbound)):
        R = ((16-5*pow(U, 8, precision)*pow(2, n, precision))
             *pow(11, -1, precision)) % precision
        assert vp(R-1, 3) == f+1
        Y = principal_root(R, n, 3, K)
        assert vp(Y-1, 3) == 1
        r27 = (-Y) % 27
        assert vp(r27+1, 3) == 1
        if label == "error":
            assert vp(5*U**8+11-16, 3) == Hbound
        print(j, f, Hbound, label, vp(R-1, 3), Y, r27)
        new_root_checks += 1
print("E125 three-adic shells:", new_root_checks, "PASS")


print("E125 denominator16 two-adic checks:")
print("j v2(n) H L v2(xi-1) new_rational_error_at_least")
for j in range(13):
    n = factorial(j+11)
    m = factorial(j+12)
    f = vp(n, 2)
    Hbound = 2*vp(m, 2)+j+3
    L = 2*vp(factorial(j+13), 2)+j+4
    U = 1+2**(Hbound+1)
    K2 = L+6
    precision = 2**(K2+f)
    R = pow(pow(U, 8, precision), -1, precision)
    xi = principal_root(R, n, 2, K2)
    assert vp(xi-1, 2) == Hbound+4-f
    assert L+4 > 2*vp(m, 2)
    q = xi+2**(L+4)
    r = 1+3*2**(L+4)
    modulus = 2**(L+5)
    numerator = (5*pow(U, 8, modulus)*pow(q, n, modulus)
                 +11*pow(r, n, modulus)-16) % modulus
    assert numerator % 2**(L+4) == 0
    print(j, f, Hbound, L, vp(xi-1, 2), L)
print("E125 denominator checks: 13 PASS")


for p in (2, 5, 11):
    assert p % 3 == 2 and vp(p*p-1, 3) == 1
for k in range(1, 41):
    s = 1+vp(k, 3)
    for p in (2, 5, 11):
        assert vp((p**(2*k)-1)//3**s, 3) == 0
print("Old support minimal even-weight orders: 120 PASS")


conjugate_checks = 0
for a in range(3):
    for b in range(3):
        h = (a, b, (a+b) % 9, 1)
        k = ((a+1) % 9, (b+2) % 9, (a*b) % 9, 1)
        xc = mul(mul(h, x), inverse(h))
        yc = mul(mul(k, y), inverse(k))
        assert closure([xc, yc]) == H
        conjugate_checks += 1
print("Finite Frattini/conjugate-generator checks:", conjugate_checks, "PASS")
affine_checks = 0
for d in range(1, 6):
    modulus = 3**d
    for u in range(2, modulus, 3):
        inv = pow(u-1, -1, modulus)
        for a in range(modulus):
            k = (-a*inv) % modulus
            assert (a+(u-1)*k) % modulus == 0
            if d <= 3:
                assert sum((a+(u-1)*j) % modulus == 0
                           for j in range(modulus)) == 1
            for parity in (0, 1):
                kk = k+modulus*((parity-k) % 2)
                assert kk % modulus == k and kk % 2 == parity
            affine_checks += 1
print("E128 affine fixed-root and square-root CRT checks:", affine_checks, "PASS")
print("SCOPE: finite identities only; infinite recursion and global lifting are proved in E.123--E.128.")
