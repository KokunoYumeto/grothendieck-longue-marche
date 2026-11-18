#!/usr/bin/env python3
"""An actual Fermat-unit necessary test for a harmonic point/cusp collision.

This is a finite certificate. A pass means only that this one necessary
test vanishes; it does not establish a full pro-three collision.
"""


def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n ** .5) + 1))


def mul(a, b, p):
    # F_p[zeta]/(zeta^2+zeta+1), irreducible when p=2 mod3.
    x, y = a
    z, w = b
    return ((x*z-y*w) % p, (x*w+y*z-y*w) % p)


def power(a, n, p):
    ans = (1, 0)
    while n:
        if n & 1:
            ans = mul(ans, a, p)
        a = mul(a, a, p)
        n //= 2
    return ans


def inv(a, p):
    return power(a, p*p-2, p)


def val3(n):
    ans = 0
    while n % 3 == 0:
        ans += 1
        n //= 3
    return ans


rows = []
for p in range(5, 501):
    if not prime(p) or p % 3 != 2:
        continue
    r = pow(2, pow(3, -1, p-1), p)
    assert pow(r, 3, p) == 2
    zeta = (0, 1)
    rzeta = (0, r)
    fP = mul(((2-r) % p, 0), inv((2, -r % p), p), p)
    fR = power(zeta, 2, p)
    ratio = mul(fP, inv(fR, p), p)
    right = power(mul((1, r), inv(((1+r) % p, 0), p), p), 2, p)
    assert ratio == right
    # Trivial 3-primary component iff the prime-to3 order kills the element.
    e = val3(p*p-1)
    prime_to3 = (p*p-1) // (3 ** e)
    test = power((1, r), prime_to3, p)
    passed = test == (1, 0)
    rows.append((p, p % 9, r, e, test, passed))

print('Rows: (p,p mod9,cube root r of2,v3(p²−1),3-primary component of1+r*zeta,passes this test)')
for row in rows:
    print(row)
assert power((1, 3), 8, 5) == (4, 4)
assert (4, 4) == power((0, 1), 2, 5)
assert not next(row[-1] for row in rows if row[0] == 5)
assert not next(row[-1] for row in rows if row[0] == 11)
assert next(row[-1] for row in rows if row[0] == 47)
assert next(row[-1] for row in rows if row[0] == 83)
print('Exact F5 identity: (1+3*zeta)^8=zeta², so the infinity collision is excluded.')

p = 5
affine = [(u, v, 1) for u in range(p) for v in range(p)
          if (u**3+v**3-2) % p == 0]
infinity = [(1, v, 0) for v in range(p) if (1+v**3) % p == 0]
points = affine+infinity
assert len(points) == 6
fixed = [P for P in affine if P[0] == P[1]]
fixed += [P for P in infinity if P[1] != 0 and P[1] * P[1] % p == 1]
assert fixed == [(1, 1, 1), (1, 4, 0)]
assert (0, 3, 1) in points and (3, 0, 1) in points
print('Fermat cubic C(F5):', points)
print('Rational fixed points of swapping u,v:', fixed)
print('With P=(1,1,1) as origin, swap is inversion; the two finite cusps are outside C(F5)[2].')
print('Hence their 3-primary Abel–Jacobi differences are nonzero; together with the unit test, all three cusps are separated from P.')
print('The S3 action on U(F5) is transitive, so every interior point is separated from every cusp in the full geometrically pro3 group.')
print('No claim of separation for every finite field, or of a collision at a passing row, is made.')
