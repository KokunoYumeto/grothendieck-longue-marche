"""Finite arithmetic checks for A.52, including the exact binomial error.

The output checks local square conditions only; the global Brauer and
continuous-cohomology arguments are proved in the TeX fragment.
"""
import math
import random


def b2(x):
    return x*(x-1)//2


def W(lam, a, b, aa, bb, hh):
    eps, eta = (lam-1)//2, (lam*lam-1)//24
    return (-(a+eps)*lam*lam*hh-b2(a)*lam*bb,
            (b+eps)*lam*lam*(aa*bb-hh)+b2(b)*lam*aa-eta*lam*bb)


rng = random.Random(520046)
binomial_checks = 0
cochain_checks = 0
coefficient_checks = 0
for r in range(1,10):
    modulus = 2**r
    for odd in (1,3,5,15):
        N = modulus*odd
        for a0 in range(-12,13):
            for a1 in range(-12,13):
                assert (b2(a0+N*a1)-b2(a0)+(N//2)*a1) % modulus == 0
                binomial_checks += 1
        for lam in (1,5,7,11,13,17,19,23):
            assert ((lam**3-1)*(N//2)) % modulus == 0
            coefficient_checks += 1
            for _ in range(40):
                a,b,aa,bb,hh,a1,b1,aa1,bb1,hh1 = [rng.randrange(-30,31) for _ in range(10)]
                old = W(lam,a,b,aa,bb,hh)
                new = W(lam,a+N*a1,b+N*b1,aa+N*aa1,bb+N*bb1,hh+N*hh1)
                expected = ((N//2)*a1*lam*bb, -(N//2)*b1*lam*aa)
                assert all((nv-ov-ev) % modulus == 0 for nv,ov,ev in zip(new,old,expected))
                cochain_checks += 2


def prime(n):
    return n >= 2 and all(n%d for d in range(2,math.isqrt(n)+1))


primes = [p for p in range(25,3000,24) if prime(p)]
for p in primes:
    assert pow(-2 % p, (p-1)//2, p) == 1
    assert pow(3, (p-1)//2, p) == 1
    assert p % 8 == 1
    assert p % 3 == 1

for K in range(4,11):
    N = math.factorial(K)
    # The completed Nth-root classes reduce to a finite product modulo 2.
    ratios = [math.factorial(K+j)//N for j in range(10)]
    first_even = next(j for j,z in enumerate(ratios) if z % 2 == 0)
    assert all(z % 2 == 0 for z in ratios[first_even:])
    assert N % 24 == 0

print(f'Exact mod-2^r binomial congruences: {binomial_checks} passed.')
print(f'Pointwise obstruction-cochain difference checks: {cochain_checks} passed.')
print(f'Galois-equivariance checks for the order-two coefficient map: {coefficient_checks} passed.')
print(f'Primes 1 mod24 tested for both (-2/p)=(3/p)=1 and local unit conditions: {len(primes)}.')
print('The factorial-root square classes have finite support modulo2 for all seven starting factorials tested.')
