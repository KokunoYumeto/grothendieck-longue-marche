#!/usr/bin/env python3
"""Exploratory necessary Fermat-unit tests for harmonic point/cusp equality.

For p=2 or5 mod9, Phi_{3^n} is irreducible over F_p, by the exact
order ord_{3^n}(p)=2*3^(n-1). Every printed pass concerns only the
single tangent-line unit at that Fermat level. It is not a collision.
"""
import numpy as np


def test(p, n):
    N = 3**n
    m = N//3
    d = 2*m
    one = np.zeros(d, dtype=np.int64)
    one[0] = 1

    def mul(a, b):
        c = np.convolve(a, b) % p
        for i in range(len(c)-1, d-1, -1):
            z = int(c[i])
            c[i-m] = (c[i-m]-z) % p
            c[i-2*m] = (c[i-2*m]-z) % p
        return c[:d] % p

    def power(a, k):
        ans = one.copy()
        while k:
            if k & 1:
                ans = mul(ans, a)
            a = mul(a, a)
            k //= 2
        return ans

    zeta = np.zeros(d, dtype=np.int64)
    zeta[1] = 1
    assert np.array_equal(power(zeta, N), one)
    assert not np.array_equal(power(zeta, N//3), one)
    r = pow(2, pow(N, -1, p-1), p)
    assert pow(r, N, p) == 2
    alpha = one.copy()
    alpha[1] = -r % p
    group_order = p**d-1
    assert group_order % N == 0 and (group_order//N) % 3 != 0
    primary = power(alpha, group_order//N)
    passed = np.array_equal(primary, one)
    exponent = None
    z = one.copy()
    for j in range(N):
        if np.array_equal(z, primary):
            exponent = j
            break
        z = mul(z, zeta)
    assert exponent is not None
    return r, d, exponent, passed


print('Rows: (p,n,root r_n of2,constant-field degree,3-primary component exponent in zeta_(3^n),passes single unit)')
for p in (5, 11, 23, 29, 41, 47, 59, 83, 101, 113, 131, 137, 149, 167, 173, 191):
    assert p % 9 in (2, 5)
    for n in range(1, 5):
        print((p, n, *test(p, n)), flush=True)
print('All rows are necessary tests only. No universal separation or surviving full collision is inferred.')
