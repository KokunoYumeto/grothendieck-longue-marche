"""Finite certificates for the full congruence abelianization in A.56.

The passage from the mod-32 leading terms to the full 2-adic subgroup
is proved in the accompanying text by repeated squaring and completeness.
This script does not substitute finite checks for that passage.
"""
from itertools import product
import sympy as sp


def mul(a, b, n):
    return ((a[0]*b[0]+a[1]*b[2]) % n,
            (a[0]*b[1]+a[1]*b[3]) % n,
            (a[2]*b[0]+a[3]*b[2]) % n,
            (a[2]*b[1]+a[3]*b[3]) % n)


def inv(a, n):
    return (a[3], -a[1] % n, -a[2] % n, a[0])


def powers(a, bound, n):
    out = [(1, 0, 0, 1)]
    for _ in range(bound-1):
        out.append(mul(out[-1], a, n))
    return out


def generated(gs, n):
    ans = {(1, 0, 0, 1)}
    todo = list(ans)
    while todo:
        a = todo.pop()
        for g in gs:
            b = mul(a, g, n)
            if b not in ans:
                ans.add(b)
                todo.append(b)
    return ans


def derived_of_two_generators(x, y, n):
    c = mul(mul(mul(x, y, n), inv(x, n), n), inv(y, n), n)
    orbit, todo = {c}, [c]
    while todo:
        a = todo.pop()
        for g in (x, y):
            b = mul(mul(g, a, n), inv(g, n), n)
            if b not in orbit:
                orbit.add(b)
                todo.append(b)
    return generated(orbit, n)


x0 = sp.Matrix([[1, 2], [0, 1]])
y0 = sp.Matrix([[1, 0], [-2, 1]])
c0 = x0*y0*x0.inv()*y0.inv()
print("Integer commutator c:", list(c0))
for label, a in (("c^4", c0**4),
                 ("[x,c]", x0*c0*x0.inv()*c0.inv()),
                 ("[y,c]", y0*c0*y0.inv()*c0.inv())):
    leading = ((a-sp.eye(2))/16).applyfunc(lambda z: z % 2)
    assert all(z.is_Integer for z in (a-sp.eye(2))/16)
    print(label, "integer matrix:", list(a), "leading term mod2:", list(leading))

n = 16
x, y = (1, 2, 0, 1), (1, 0, 14, 1)
c = tuple(int(z) % n for z in c0)
H = generated((x, y), n)
D = derived_of_two_generators(x, y, n)
assert len(H) == 256 and len(D) == 4
assert D == set(powers(c, 4, n))
normal_forms = {}
for a, b, k in product(range(8), range(8), range(4)):
    M = mul(mul(powers(x, 8, n)[a], powers(y, 8, n)[b], n), powers(c, 4, n)[k], n)
    assert M not in normal_forms
    normal_forms[M] = (a, b, k)
assert set(normal_forms) == H
for M in H:
    for N in H:
        a, b, _ = normal_forms[M]
        a1, b1, _ = normal_forms[N]
        a2, b2, _ = normal_forms[mul(M, N, 16)]
        assert (a2, b2) == ((a+a1) % 8, (b+b1) % 8)
print("H2 modulo16:", len(H), "derived:", len(D), "abelianization: C8 x C8")
print("Unique x^a y^b c^k forms checked for all 256 matrices;")
print("abelian coordinate multiplication checked for all 65536 pairs.")

for n in (3, 9):
    x, y = (1, 1, 0, 1), (1, 0, 1, 1)
    H = generated((x, y), n)
    D = derived_of_two_generators(x, y, n)
    print("SL2 modulo", n, "order:", len(H), "derived:", len(D),
          "abelianization order:", len(H)//len(D))
    assert len(H)//len(D) == 3
    u2, lm2 = (1, 2 % n, 0, 1), (1, 0, -2 % n, 1)
    assert mul(u2, inv(lm2, n), n) in D
    assert u2 not in D
print("U(2) and L(-2) have the same nonzero order-three abelian image.")
print("Full result proved in text: H^ab = (Z/8)^2 x Z/3, exponent24.")
print("All checks passed.")
