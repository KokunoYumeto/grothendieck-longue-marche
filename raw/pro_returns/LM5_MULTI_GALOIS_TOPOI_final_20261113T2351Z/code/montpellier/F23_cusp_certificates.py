"""Exact finite certificates for the resolved cusp in LM5 F.23.

The text proves the unrestricted and profinite kernel assertions.
This program verifies the polynomial identities, intersection updates,
finite congruence equalities, and Heisenberg commutator orders used there.
"""
from math import gcd
import sympy as sp

x, y, u, v, w = sp.symbols("x y u v w")
f = y**2 - x**3
first = sp.expand(f.subs(y, x*v))
assert sp.expand(first - x**2*(v**2-x)) == 0
second = sp.expand(first.subs(x, u*v))
assert sp.expand(second - u**2*v**3*(v-u)) == 0
third = sp.expand(second.subs(v, u*w))
assert sp.expand(third - u**6*w**3*(w-1)) == 0
print("F.23 blow-up chart identities")
print("  y=x*v:", sp.factor(first))
print("  x=u*v:", sp.factor(second))
print("  v=u*w:", sp.factor(third))

squares = {"E1": -1}
squares["E1"] -= 1
squares["E2"] = -1
squares["E1"] -= 1
squares["E2"] -= 1
squares["E3"] = -1
assert squares == {"E1": -3, "E2": -2, "E3": -1}
print("  Exceptional self-intersections:", squares)
print("  Multiplicities on (E1,E2,E3): (2,3,6)")

print("F.23 exact finite congruence certificates")
for name, multiplicity, d in (("E1", 2, 3), ("E2", 3, 2)):
    assert multiplicity*d == 6
    assert gcd(d, 1) == 1
    print(f"  {name}: primitive kernel generator ({-d},1)")
    for n in (2, 3, 4, 5, 8, 9, 12):
        # The degree quotient has modulus multiplicity*n, so it detects
        # exactly r+d*s modulo n, including primes dividing multiplicity.
        kernel = {(r, s) for r in range(n) for s in range(n)
                  if (multiplicity*r+6*s) % (multiplicity*n) == 0}
        expected = {((-d*s) % n, s) for s in range(n)}
        assert kernel == expected
        print(f"    modulo {n}: kernel cardinality {len(kernel)}, exact line verified")

def multiply(a, b, n):
    return ((a[0]+b[0]) % n, (a[1]+b[1]) % n,
            (a[2]+b[2]+a[0]*b[1]) % n)

def inverse(a, n):
    return (-a[0] % n, -a[1] % n, (-a[2]+a[0]*a[1]) % n)

print("F.23 puncture commutator finite quotients")
for n in (2, 3, 4, 5, 6, 8, 9, 12):
    a, b = (1,0,0), (0,1,0)
    commutator = multiply(multiply(multiply(a,b,n),inverse(a,n),n),inverse(b,n),n)
    assert commutator == (0,0,1)
    current, order = (0,0,0), 0
    while True:
        current = multiply(current,commutator,n)
        order += 1
        if current == (0,0,0):
            break
    assert order == n
    print(f"  modulo {n}: commutator {commutator}, exact order {order}")
print("ALL CHECKS PASSED")
