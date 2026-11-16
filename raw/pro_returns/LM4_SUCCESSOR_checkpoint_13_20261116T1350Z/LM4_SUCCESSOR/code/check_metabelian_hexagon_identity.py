#!/usr/bin/env python3
"""Independent exact algebra checks for the C.33 metabelian argument.

This verifies identities and first-denominator polynomials. It does not
construct a pentagon solution or certify a full profinite hexagon.
"""
import sympy as sp

a, b, t, u, v, w, m = sp.symbols("a b T U V W m")


def mul(left, right):
    d, x = left
    e, y = right
    return sp.expand(d * e), sp.expand(x + d * y)


def product(items):
    answer = (sp.Integer(1), sp.Integer(0))
    for item in items:
        answer = mul(answer, item)
    return tuple(sp.factor(z) for z in answer)


# b denotes a^m. U=F(a,a^-1), V=F(1,a), W=F(a^-1,1).
hexagon = product([
    (1, t * (1 - 1 / a) * u),
    (b, t * (b - 1) / (a - 1)),
    (1, t * (a - 1) * v),
    (1, -m * t),
    (1, t * (1 - 1 / a) * w),
    (1 / b, 0),
])
expected = (
    t * (1 - 1 / a) * u + t * (b - 1) / (a - 1)
    + b * t * (a - 1) * v - b * m * t
    + b * t * (1 - 1 / a) * w
)
assert hexagon[0] == 1
assert sp.cancel(hexagon[1] - expected) == 0
print("AFFINE_SIX_FACTOR_PRODUCT: exact equality")

eq = sp.cancel(expected / (t * b)).subs(t, a - 1)
inverse_eq = eq.subs({a: 1 / a, b: 1 / b, v: w, w: v}, simultaneous=True)
combined = sp.factor((eq + inverse_eq) * (a - 1) * b)
target = (a * b**2 - 1) * (1 - (a - 1)**2 * u / a) - (2 * m + 1) * (a - 1) * b
assert sp.cancel(combined - target) == 0
print("INVERSE_SPECIALIZATION_SUM: (a*b^2-1)*(1-(a-1)^2*U/a)=(2*m+1)*(a-1)*b")
print("SUBSTITUTION: b=a^m and mu=2*m+1 give the C.33 identity")

mu = sp.symbols("mu")
for p in [3, 5, 7, 11, 13, 17, 19]:
    numerator = sp.prod(mu - j for j in range(1, p))
    reduced = sp.Poly(numerator - (mu**(p - 1) - 1), mu, modulus=p)
    assert reduced.is_zero
    n = sp.factorial(p)
    valuation = 0
    while n % p == 0:
        n //= p
        valuation += 1
    assert valuation == 1
    assert sp.factorial(p - 1) % p != 0
    print(f"p={p}: numerator=mu^(p-1)-1 mod p; v_p(p!)=1; (p-1)! is a unit")

# A known integral root gives the expected quadratic coefficient.
rhs3 = 3 * (1 + t) * t / ((1 + t)**3 - 1)
coeff2 = sp.expand(sp.series(rhs3, t, 0, 3).removeO()).coeff(t, 2)
assert coeff2 == -sp.Rational(1, 3)
print("SIGN_CHECK mu=3: coefficient(T^2)=-1/3=-(mu^2-1)/24")
print("SCOPE: symbolic algebra and finite-prime checks only; no full profinite conclusion")
