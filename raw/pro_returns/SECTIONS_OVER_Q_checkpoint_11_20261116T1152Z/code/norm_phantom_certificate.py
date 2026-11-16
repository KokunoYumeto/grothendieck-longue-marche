"""A.81 exact coefficient-kernel and binomial-divisibility checks."""
from math import comb
import sympy as sy

def vp(a, p):
    assert a
    a = abs(a)
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v

S = sy.symbols("S")
binomial_checks = 0
quotient_checks = 0
projection_checks = 0

for ell in (2, 3, 5, 7):
    for n in range(1, 7):
        N = ell**n
        for j in range(1, min(N, 80) + 1):
            assert vp(comb(N, j), ell) == n - vp(j, ell)
            binomial_checks += 1
        for r in range(1, 33):
            if N < r:
                continue
            floorlog = 0
            while ell**(floorlog + 1) <= r:
                floorlog += 1
            k = n - floorlog
            if k < 0:
                continue
            assert all(comb(N, j) % ell**k == 0
                       for j in range(1, r + 1))
            projection_checks += 1

for ell in (2, 3, 5):
    for n in range(1, 4):
        N = ell**n
        X = 1 + S
        Ln = sy.Poly(sum(comb(N, j)*S**(j-1)
                         for j in range(1, N+1)), S)
        fn = sy.Poly(X**N - 1, S)
        assert sy.Poly(S, S)*Ln == fn
        assert Ln.degree() == N - 1 and Ln.LC() == 1
        Ln1 = sy.Poly(sum(comb(ell*N, j)*S**(j-1)
                          for j in range(1, ell*N+1)), S)
        transition = sy.Poly(sum(X**(N*j) for j in range(ell)), S)
        assert Ln*transition == Ln1
        quotient_checks += 1

print("A.81 exact derived norm-kernel certificate")
print("Exact valuations of binomial coefficients:", binomial_checks)
print("Finite-weight coefficient projection bounds:", projection_checks)
print("Derived kernels S L_n=X^(ell^n)-1 and tower divisibility:",
      quotient_checks)
print("All exact identities passed.")
