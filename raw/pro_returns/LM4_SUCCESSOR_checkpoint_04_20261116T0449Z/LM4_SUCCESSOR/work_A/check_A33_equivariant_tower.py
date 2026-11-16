"""Exact controls for the all-congruence reflection adjustment in A.33.

The general proof works over each Z_p.  This script checks every determinant-one
R-centralizer which is identity modulo four, at the listed composite moduli.
It constructs the pure SL2 conjugator, rather than merely searching for one.
"""

from itertools import product
from math import gcd


def mul(a, b, n):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % n
                 for i in range(2) for j in range(2))


def det(a, n):
    return (a[0]*a[3]-a[1]*a[2]) % n


def inverse(a, n):
    d = pow(det(a, n), -1, n)
    return tuple(d*v % n for v in (a[3], -a[1], -a[2], a[0]))


def factors(n):
    answer = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            q = 1
            while n % p == 0:
                n //= p
                q *= p
            answer.append((p, q))
        p += 1
    if n > 1:
        answer.append((n, n))
    return answer


def crt(values, moduli):
    n = 1
    for q in moduli:
        n *= q
    return sum(v*(n//q)*pow(n//q, -1, q)
               for v, q in zip(values, moduli)) % n


def conjugator(t, p, q):
    # First h0*d*h0^-1=t, via a cyclic basis (v,t*v).
    if p == 2:
        assert tuple(z % 4 for z in t) == (0, 1, 1, 0)
        h0 = (1, t[0], 0, t[2])
        assert det(h0, 4) == 1
    else:
        for v0, v1 in product(range(p), repeat=2):
            h0 = (v0, (t[0]*v0+t[1]*v1) % q,
                  v1, (t[2]*v0+t[3]*v1) % q)
            if gcd(det(h0, q), q) == 1:
                break
        else:
            raise AssertionError('No cyclic vector')
    delta = det(h0, q)
    if p == 2:
        delta_inv = pow(delta, -1, 2*q)
        u, v = (delta_inv+1)//2, (delta_inv-1)//2
        assert u % 2 == 1 and v % 2 == 0
    else:
        delta_inv = pow(delta, -1, q)
        inv2 = pow(2, -1, q)
        u, v = (delta_inv+1)*inv2, (delta_inv-1)*inv2
    k = (u % q, v % q, v % q, u % q)
    d = (0, 1, 1, 0)
    assert mul(k, d, q) == mul(d, k, q)
    h = mul(h0, k, q)
    assert det(h, q) == 1
    assert mul(mul(h, d, q), inverse(h, q), q) == tuple(x % q for x in t)
    if p == 2:
        assert tuple(x % 2 for x in h) == (1, 0, 0, 1)
    return inverse(h, q)


for n in (12, 24, 48, 60, 84, 120, 132):
    r = (0, n-1, 1, n-1)
    d = (0, 1, 1, 0)
    identity = (1, 0, 0, 1)
    fq = factors(n)
    count = 0
    for u, v in product(range(n), repeat=2):
        a = (u, -v % n, v, (u-v) % n)
        if det(a, n) != 1 or tuple(z % 4 for z in a) != identity:
            continue
        count += 1
        assert mul(a, r, n) == mul(r, a, n)
        assert mul(mul(d, a, n), d, n) == inverse(a, n)
        t = mul(inverse(a, n), d, n)
        assert mul(t, t, n) == identity
        parts = [conjugator(tuple(z % q for z in t), p, q) for p, q in fq]
        h = tuple(crt([hp[i] for hp in parts], [q for p, q in fq])
                  for i in range(4))
        assert det(h, n) == 1
        assert tuple(z % 2 for z in h) == identity
        assert mul(mul(h, t, n), inverse(h, n), n) == d
    print(f'modulus {n}: checked all {count} pure R-Cartan frames and constructed pure SL2 reflection conjugators')

print('All assertions passed; general lifting and compactness are proved in A.33.')
