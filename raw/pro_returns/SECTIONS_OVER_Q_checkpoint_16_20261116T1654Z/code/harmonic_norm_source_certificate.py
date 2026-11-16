#!/usr/bin/env python3
"""Exact source norm obstructions for the harmonic Jacobian comparison.

These concern the source E torsor, not its pullback to Jac(C4).
For integral d,a,b and nonsplit odd p, a nonintegral m makes the
normalized quartic value -1 modulo p.  At2 it makes that value7
modulo8.  Thus the integral residue exclusions below are complete
local obstructions to the actual projective norm torsor.
"""

from sympy import symbols, expand, legendre_symbol

x, m, d, a, b = symbols("x m d a b")
quad = x*x+(a-m*m)*x+(a*a+a*m*m-d*d+2*m*b)
intersection = x**3-d*d*x-(m*x-b-m*a)**2
assert expand(intersection-(x-a)*quad).subs(b*b, a**3-d*d*a) == 0
disc = expand((a-m*m)**2-4*(a*a+a*m*m-d*d+2*m*b))
assert disc == m**4-6*a*m*m-8*b*m-3*a*a+4*d*d


def valuation(n, p):
    assert n
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e, n


rows = [
    (138, 162, 1080, [(2, 4), (3, 3)], [(23, 0)]),
    (154, 350, 5880, [(2, 4), (7, 3)], [(11, 0)]),
    (210, -90, 1800, [(2, 4), (3, 3)], [(7, 1)]),
    (210, 490, 9800, [(2, 4), (7, 3)], [(3, 2)]),
]
checks = 0
print("Harmonic source norm-torsor certificate: exact source calculations.")
for d, a, b, impossible, soluble in rows:
    assert b*b == a**3-d*d*a
    f = lambda m: -m**4+6*a*m*m+8*b*m+3*a*a-4*d*d
    print(f"Source d={d}, Q=({a},{b}):")
    for p, n in impossible:
        modulus = p**n
        squares = {z*z % modulus for z in range(modulus)}
        possible = [m for m in range(modulus) if f(m) % modulus in squares]
        assert possible == []
        checks += modulus
        print(f"  No integral norm-torsor point modulo {p}^{n}={modulus}.")
    for p, m in soluble:
        value = f(m)
        e, u = valuation(value, p)
        assert e % 2 == 0 and legendre_symbol(u % p, p) == 1
        print(f"  Actual Q_{p} point at m={m}: quartic value={value}, "
              f"valuation={e}, unit residue={u % p}.")
print(f"Exact residue values excluded: {checks}.")
print("Nonintegral m is excluded by the leading unit -1; points at infinity require i.")
print("These are source norm obstructions. No nonzero C4 pullback is inferred.")
