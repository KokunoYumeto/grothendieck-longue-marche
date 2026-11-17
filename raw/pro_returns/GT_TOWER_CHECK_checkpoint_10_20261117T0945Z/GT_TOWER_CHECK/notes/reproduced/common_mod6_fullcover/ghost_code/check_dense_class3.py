#!/usr/bin/env python3
"""Exact residue and factorial certificate for the dense-exclusion construction.

The first calculation starts from both full Hall-coordinate residues, not
from the simplified obstruction used in the theorem.  The prime checks
certify the original-exponent and Hensel indices at several coefficient
primes.  The Chebotarev existence argument is a proof in the TeX source.
"""
from math import factorial
import sympy as s

q, m, n, t, alpha, beta, gamma, u = s.symbols(
    'q m n t alpha beta gamma u')
e = (q - 1) / 2
e2 = (q*q - 1) / 24
choose2 = lambda z: z*(z-1)/2
B = lambda z: (q-1)*((2*q-1)*z*z-3*z)/12
ZD = (m*gamma-q*(alpha+e)*t-n*choose2(alpha)
      + beta*choose2(q*m)/q+e*m*t+n*B(m))
ZF = (n*(gamma-alpha*beta)+q*(beta+e)*(m*n-t)
      +m*choose2(beta)-e2*n-alpha*choose2(q*n)/q
      -e*(m*n*n-n*t)-m*B(n))
positive = {n: 0, t: m*u, beta: (q-1)*u}
ZDpos = s.factor(ZD.subs(positive, simultaneous=True))
ZFpos = s.factor(ZF.subs(positive, simultaneous=True))
assert s.expand(ZDpos - (m*(gamma-q*alpha*u)
                        +(q*q-1)*u*choose2(m))) == 0
assert s.expand(ZFpos + (q*q-1)*m*u*(u+1)/2) == 0
print('PASS: both full Hall residues give the two positive-support formulas')

ell, Q, M, A, G = s.symbols('ell Q M A G')
special = {q: 1+ell**2*Q, m: ell*M, alpha: ell*A, gamma: G}
error = s.Poly(s.expand(2*ZDpos.subs(special)-2*ell*M*G), ell)
assert all(power[0] >= 2 for power, coeff in error.terms() if coeff != 0)
print('PASS: 2*Z_D = 2*ell*M*G modulo ell^2 as an exact integral polynomial')

def valuation(x, p):
    assert x != 0
    out = 0
    while x % p == 0:
        x //= p
        out += 1
    return out

checked = []
for p in [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
    assert s.isprime(p)
    J = p-4
    nJ, n1, n2 = factorial(J+4), factorial(J+5), factorial(J+6)
    assert valuation(nJ, p) == valuation(n1, p) == valuation(n2, p) == 1
    assert all(factorial(i+4) % p for i in range(J))
    HJ, LJ = 2*valuation(n1, p)+J+3, 2*valuation(n2, p)+J+4
    assert HJ == p+1 and LJ == p+2
    assert HJ-valuation(nJ, p) == p
    assert (nJ//p) % p == p-1
    checked.append(p)
print('PASS: original factorial and Hensel indices at coefficient primes', checked)
print('PASS: n_J/ell is a nonzero unit; the displayed mod-ell^2 residue cannot vanish')
