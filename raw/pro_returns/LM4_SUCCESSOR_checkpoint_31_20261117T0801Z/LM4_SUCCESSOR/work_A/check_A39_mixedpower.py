"""Exact S4 obstruction to a mixed-sign pronilpotent peripheral substitution.

Permutation products act right to left.  The chosen profinite unit is -1
at 2 and +1 at every odd prime, hence is 7 modulo exponent(S4)=12.
No finite quotient is claimed to detect all pronilpotent information.
"""
from itertools import permutations

I = tuple(range(1, 5))
def compose(a, b):
    return tuple(a[b[i] - 1] for i in range(4))
def power(a, n):
    r = I
    for _ in range(n):
        r = compose(r, a)
    return r
def inverse(a):
    return tuple(a.index(i) + 1 for i in range(1, 5))
def cycles(a):
    seen = set()
    out = []
    for i in range(1, 5):
        if i in seen:
            continue
        c = []
        j = i
        while j not in seen:
            seen.add(j)
            c.append(j)
            j = a[j - 1]
        if len(c) > 1:
            out.append(tuple(c))
    return out

x = (1, 3, 4, 2)  # (234)
y = (2, 3, 4, 1)  # (1234)
mu = 7
G = {I}
frontier = [I]
while frontier:
    a = frontier.pop()
    for b in (x, y):
        c = compose(a, b)
        if c not in G:
            G.add(c)
            frontier.append(c)
assert len(G) == 24
left = compose(power(x, mu), power(y, mu))
right = power(compose(x, y), mu)
conjugates = {compose(compose(inverse(g), right), g) for g in permutations(I)}
assert left not in conjugates
assert cycles(left) == [(1, 2)]
assert cycles(right) == [(1, 4, 2, 3)]
assert power(x, 12) == power(y, 12) == I
print('Generated group order:', len(G))
print('x =', cycles(x), '; y =', cycles(y), '; xy =', cycles(compose(x, y)))
print('Mixed unit mu = 7 mod 12; mu = -1 mod 4 and +1 mod 3.')
print('x^mu y^mu =', cycles(left))
print('(xy)^mu =', cycles(right))
print('Conjugacy class of (xy)^mu has size', len(conjugates))
print('The two elements are not S4-conjugate: PASS')
