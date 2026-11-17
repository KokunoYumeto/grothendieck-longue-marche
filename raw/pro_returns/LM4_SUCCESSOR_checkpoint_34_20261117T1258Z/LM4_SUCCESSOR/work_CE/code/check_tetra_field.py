"""Exact certificate for B.31, plus the cardinality test in B.32.

This is standalone: it does not import or run the parent cross-ratio
program.  SymPy performs rational polynomial arithmetic throughout.
The choice q=exp(pi*i/10) selects the stated real sign by
q**6-q**4 = -2*cos(2*pi/5) = (1-sqrt(5))/2.
"""
from itertools import combinations
import sympy as S

u, q = S.symbols('u q')
f = u**12 - 33*u**8 - 33*u**4 + 1
g = u**2 * (u**4 - 1)**2
h = u**8 + 14*u**4 + 1
v = f/g

def matnorm(matrix):
    entries = list(matrix)
    lead = next(a for a in entries if a != 0)
    return tuple(S.simplify(a/lead) for a in entries)

def mul(a, b):
    return matnorm(S.Matrix(2, 2, a) * S.Matrix(2, 2, b))

identity = (S.Integer(1), S.Integer(0), S.Integer(0), S.Integer(1))
generators = [matnorm(S.Matrix([[-1, 0], [0, 1]])),
              matnorm(S.Matrix([[0, 1], [1, 0]])),
              matnorm(S.Matrix([[1, S.I], [1, -S.I]]))]
group, todo = [identity], [identity]
while todo:
    a = todo.pop(0)
    for b in generators:
        c = mul(a, b)
        if c not in group:
            group.append(c)
            todo.append(c)
assert len(group) == 12
assert all(mul(a, b) in group for a in group for b in group)
for a, b, c, d in group:
    assert S.cancel(v.subs(u, (a*u+b)/(c*u+d)) - v) == 0
assert S.expand(h**3-f**2-108*g**2) == 0
assert S.cancel(S.diff(v, u)-2*h**2/(u**3*(u**4-1)**3)) == 0

mod = S.Poly(S.cyclotomic_poly(20, q), q, domain=S.QQ)
def red(expression):
    numerator, denominator = S.fraction(S.cancel(expression))
    n = S.Poly(numerator, q, domain=S.QQ).rem(mod)
    d = S.Poly(denominator, q, domain=S.QQ).rem(mod)
    return (n*S.invert(d, mod)).rem(mod).as_expr()

u0 = red(q**5*(q+q**-1+q**2+q**-2))
assert u0 == q**7+q**6+q**4+q**3
v0 = red(v.subs(u, u0))
assert v0 == (44*q**6-44*q**4-22)/5
assert red(v0**2) == S.Rational(484, 5)
sqrt5 = red(1-2*(q**6-q**4))
assert red(sqrt5**2) == 5
assert red(v0+S.Rational(22, 5)*sqrt5) == 0

for cluster_size in (2, 3):
    clusters = [set(range(i, i+cluster_size))
                for i in range(0, 12, cluster_size)]
    checked = 0
    for subset in combinations(range(12), 7):
        counts = [len(set(subset) & cluster) for cluster in clusters]
        assert max(counts) >= 2
        assert sum(c > 0 for c in counts) >= 3
        checked += 1
    assert checked == 792
    print(f'All 792 seven-subsets for {len(clusters)} '
          f'clusters of size {cluster_size}: PASS')

print('Tetrahedral projective group order:', len(group))
print('All 12 rational-function invariance identities: PASS')
print('h^3-f^2 = 108*g^2: PASS')
print('Derivative = 2*h^2/(u^3*(u^4-1)^3): PASS')
print('u0 =', u0)
print('v0 =', v0)
print('v0^2 =', red(v0**2))
print('v0 = -22*sqrt(5)/5 in the chosen embedding: PASS')
print('Certificate uses exact rational polynomial arithmetic only.')
