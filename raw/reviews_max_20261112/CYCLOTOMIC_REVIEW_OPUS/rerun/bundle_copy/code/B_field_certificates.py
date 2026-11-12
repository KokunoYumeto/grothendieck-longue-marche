"""Exact finite certificates used in Part B.

Run with Python 3 and SymPy. This certifies the finite algebra and group
calculations only; the infinite Galois statements are proved in the paper.
"""
from itertools import permutations
from platform import python_version
import sympy
from sympy import Poly, Symbol, discriminant, factor_list

print('Python:', python_version(), 'SymPy:', sympy.__version__)
x = Symbol('x')
f = x**5 - x - 1
print('Polynomial f = x^5 - x - 1')
for p in (2, 3):
    coeff, factors = factor_list(f, modulus=p)
    print(f'factorization modulo {p}:', [(str(g), e) for g, e in factors])
    print('degrees:', [Poly(g, x).degree() for g, e in factors for _ in range(e)])
assert Poly(f, x, modulus=3).is_irreducible
assert sorted(Poly(g, x).degree() for g, e in factor_list(f, modulus=2)[1]) == [2, 3]
print('discriminant:', discriminant(f, x))

def mul(a, b):
    return tuple(a[b[i]] for i in range(len(a)))

def inv(a):
    r = [0]*len(a)
    for i, j in enumerate(a):
        r[j] = i
    return tuple(r)

def closure(generators, n):
    identity = tuple(range(n))
    found = {identity}
    todo = [identity]
    gs = set(generators) | {inv(a) for a in generators}
    while todo:
        a = todo.pop()
        for b in gs:
            c = mul(a, b)
            if c not in found:
                found.add(c)
                todo.append(c)
    return found

def commutator(a, b):
    return mul(mul(mul(a, b), inv(a)), inv(b))

S5 = set(permutations(range(5)))
D1 = closure({commutator(a, b) for a in S5 for b in S5}, 5)
D2 = closure({commutator(a, b) for a in D1 for b in D1}, 5)
print('S5 derived-series orders:', len(S5), len(D1), len(D2))
assert len(D1) == len(D2) == 60 and D1 == D2
print('certificate: S5 is nonsolvable')

S3 = set(permutations(range(3)))
transposition = (1, 0, 2)
Sylow2 = {tuple(range(3)), transposition}
conjugates = {
    frozenset(mul(mul(g, h), inv(g)) for h in Sylow2)
    for g in S3
}
print('number of conjugate Sylow-2 subgroups in S3:', len(conjugates))
assert len(conjugates) == 3
print('certificate: S3 is not nilpotent')
print('discriminant of x^3-2:', discriminant(x**3-2, x))

t, T = Symbol('t'), Symbol('T')
print('discriminant in T of T^2-t:', discriminant(T**2-t, T))
assert discriminant(T**2-t, T) == 4*t
print('quadratic ramification witness at t=0: discriminant has order 1')
print('ALL EXACT FINITE CERTIFICATES PASSED')
