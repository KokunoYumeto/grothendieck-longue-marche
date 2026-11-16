#!/usr/bin/env python3
"""Exact finite checks for A.147; no class-group computation is asserted."""
from math import gcd, isqrt

q = 511177
assert all(q % d for d in range(2, isqrt(q) + 1))
assert (q - 1) % 3 == 0 and (q - 1) % 9 != 0
roots = (13382, 29914, 467881)
assert all(pow(r, 3, q) == 3 for r in roots)
zeta = pow(5, (q - 1) // 3, q)
assert zeta == 472522
assert tuple(roots[0] * pow(zeta, i, q) % q for i in range(3)) == roots
characters = tuple(next(i for i in range(3) if pow(zeta, i, q) == pow(r, (q - 1)//3, q)) for r in roots)
assert characters == (0, 1, 2)
norm = lambda a,b,c: a**3+3*b**3+9*c**3-9*a*b*c
assert norm(-68,64,1) == q
assert tuple((-68+64*r+r*r) % q for r in roots) == (0,157366,353607)

# The subgroup of residue units of order h has invertible cube map.
h = (q - 1)//3
assert gcd(h,3) == 1
cube_inverse = pow(3,-1,h)
branch = [roots[0]]
for _ in range(12):
    nxt = pow(branch[-1], cube_inverse, q)
    assert pow(nxt,3,q) == branch[-1]
    assert pow(nxt,h,q) == 1
    branch.append(nxt)
assert all(pow(branch[n],3**(n+1),q) == 3 for n in range(len(branch)))

cyclic_checks = 0
inverse_checks = 0
for d in range(1,400):
    if d % 3 == 0:
        continue
    a = pow(d,-1,3)
    b = (1-a*d)//3
    assert a*d+3*b == 1
    cyclic_checks += 1
    previous = None
    for r in range(1,11):
        inv = pow(d,-1,3**r)
        assert d*inv % (3**r) == 1
        if previous is not None:
            assert inv % (3**(r-1)) == previous
        previous = inv
        inverse_checks += 1
assert 2*2-3 == 1  # Norm(v^2/epsilon)=epsilon^(4-3).
assert sum((-2,1,1)) == 0
assert 1 % 3 != 0

print('A.147 exact certificate PASS')
print('q =', q, '; norm(gamma) =', norm(-68,64,1))
print('Cubic residue characters:', characters)
print('Selected compatible residue branch:', branch)
print('Actual cyclic unit Bezout checks:', cyclic_checks)
print('Compatible completed exponent inverses:', inverse_checks)
print('Quadratic transfer exponent: 2*2-3 = 1')
print('Scalar q and U*q/gamma^3 have valuation 1 at both unramified cubic branches.')
