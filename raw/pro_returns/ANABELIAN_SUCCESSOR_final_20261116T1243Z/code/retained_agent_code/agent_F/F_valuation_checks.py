"""Finite checks accompanying FF.17 and the failed substitution in FF.18.

The factorial-gap proof is symbolic and infinite in the paper.  This script
only checks the displayed inequalities for sample degree bounds and the
finite initial coefficients witnessing failure of valuation preservation.
"""
from math import factorial


def initial_series(max_degree):
    coefficients = {}
    n = 1
    while factorial(n) <= max_degree:
        exponent = factorial(n)
        coefficients[exponent] = coefficients.get(exponent, 0) + 1
        n += 1
    return coefficients


def subtract(a, b):
    c = a.copy()
    for exponent, coefficient in b.items():
        c[exponent] = c.get(exponent, 0) - coefficient
        if c[exponent] == 0:
            del c[exponent]
    return c


def multiply(a, b):
    c = {}
    for i, ai in a.items():
        for j, bj in b.items():
            c[i+j] = c.get(i+j, 0) + ai*bj
    return {i: ai for i, ai in c.items() if ai}


print('Factorial-gap checks: m=degree_t P, e=degree_U P')
for m, e in [(0, 1), (20, 2), (1000, 8), (10**9, 30)]:
    n = max(2, e)
    while factorial(n+1) <= m+e*factorial(n):
        n += 1
    assert factorial(n+1) > m+e*factorial(n)
    print(f'm={m}, e={e}: N={n}, gap={factorial(n+1)}, bound={m+e*factorial(n)}')

u = initial_series(24)
t = {1: 1}
t2 = {2: 1}
s = {1: 1, 2: 1}
original = subtract(subtract(u, t), t2)
substituted = subtract(subtract(u, s), multiply(s, s))
assert min(original) == 6
assert min(substituted) == 2
assert substituted[2] == -1
print('v(u-t-t^2) =', min(original))
print('v(u-(t+t^2)-(t+t^2)^2) =', min(substituted))
print('Substituted coefficients through degree 24:', sorted(substituted.items()))
print('PASS: fixing u and sending t to t+t^2 does not preserve this valuation.')
