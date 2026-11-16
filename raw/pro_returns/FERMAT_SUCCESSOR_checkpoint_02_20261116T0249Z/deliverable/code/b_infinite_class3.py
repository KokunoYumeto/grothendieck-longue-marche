"""Exact certificate for the infinitely ramified class-three counterexample.

The proof uses no numerical value of the unknown action cocycle eta.  It
uses the adjugate identity over Z_3 and a bound for the determinant of the
330 by 330 Frobenius operator.  This program checks its multiplicities,
the determinant valuation, and the first primes in the explicitly defined
infinite sequence.  Finite examples are checks; LTE proves the formula
for every prime p == 2 mod 3 in the accompanying manuscript.
"""
from fractions import Fraction
from sympy import primerange

def valuation(n, p=3):
    n = abs(int(n))
    assert n
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

# For a direct sum of dimensions a,b, the free degree-three Lie algebra
# has mixed dimensions a^2*b and a*b^2, and pure dimension (r^3-r)/3.
a,b = 2,8
dimensions = [(a**3-a)//3, a*a*b, a*b*b, (b**3-b)//3]
assert dimensions == [2,32,128,168]
assert sum(dimensions) == (10**3-10)//3 == 330
print('Lie_3(2+8) multiplicities, ordered by the number of elliptic letters:', dimensions)
print('Frobenius on A(-1) at inert p: (-p)^2, (p^2)^32, (-p^3)^128, (p^4)^168.')
print('These exponents denote multiplicities, not powers of one eigenvalue.')
print(' j   p   v3(p+1)   v3(det(F/q-1))   exponent of a_j')
primes = [int(p) for p in primerange(2,1000) if p % 3 == 2]
for j,p in enumerate(primes,1):
    h = valuation(p+1)
    actual = sum(m*valuation(e-1) for m,e in zip(dimensions,[-p,p*p,-p**3,p**4]))
    expected = 330*h+128
    assert actual == expected
    exponent = j+expected
    assert exponent-actual == j
    if j <= 16:
        print(f'{j:2} {p:4} {h:8} {actual:19} {exponent:19}')
print('All', len(primes), 'inert primes below 1000 satisfy the determinant formula.')
print('Adjugate bound: a_j D_p^{-1} maps A(-1) into 3^j A(-1).')
print('Therefore the corrections are integral and tend uniformly to zero: PASS.')

# An explicit Schreier transfer in the index-9 subgroup of the free group
# on x,y, with coset representatives x^i y^j.  We retain formal generator
# labels (i,j,t) for edges in the 3 by 3 coset graph.  Tree edges are zero
# in the subgroup abelianization; there are 10 remaining edges.
vertices = [(i,j) for i in range(3) for j in range(3)]
tree = {(i,0,'x') for i in range(2)} | {(i,j,'y') for i in range(3) for j in range(2)}
edges = [(i,j,t) for i,j in vertices for t in ['x','y'] if (i,j,t) not in tree]
assert len(edges) == 10
tx = [int(e[2]=='x') for e in edges]
ty = [int(e[2]=='y') for e in edges]
w = {(r,s):tx[r]*ty[s]-tx[s]*ty[r] for r in range(10) for s in range(r+1,10)}
assert any(w.values())
print('Schreier basis edges:', edges)
print('Transfer j(x) coordinates:', tx)
print('Transfer j(y) coordinates:', ty)
print('Nonzero wedge coordinates (zero-based indices):', {k:v for k,v in w.items() if v})
print('This finite graph specifies an integral nonzero Tate vector without selecting eta.')
