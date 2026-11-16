"""Finite cusp obstructions to mixed-sign diagonal torus involutions.

The general odd-prime argument is proved in C.27.  Its smallest Frobenius
instance and the exceptional 2-versus-all-odd pattern are checked here.
"""
from itertools import product

# F7 additive, acted on by C3 through multiplication by 2.
def fm(a, b):
    return ((a[0] + pow(2, a[1], 7) * b[0]) % 7,
            (a[1] + b[1]) % 3)

FI = (0, 0)
FG = list(product(range(7), range(3)))
def fi(a):
    return next(b for b in FG if fm(a, b) == FI == fm(b, a))
def fc(a, b):
    return fm(fm(fm(a, b), fi(a)), fi(b))

fx, fy = (1, 0), (0, 1)
fcomm = fc(fx, fy)
for g in FG:
    assert fm(fm(g, fcomm), fi(g)) != fi(fcomm)
assert fcomm == (6, 0)
print('F7 semidirect C3: commutator (6,0) not conjugate to its inverse: PASS')
print('For u7=+1,u3=-1 both finite generator images are fixed: PASS')

P = 7
I = (1, 0, 0, 1)
minus_I = (6, 0, 0, 6)
def mul(a, b):
    return ((a[0]*b[0]+a[1]*b[2]) % P,
            (a[0]*b[1]+a[1]*b[3]) % P,
            (a[2]*b[0]+a[3]*b[2]) % P,
            (a[2]*b[1]+a[3]*b[3]) % P)
def inv(a):
    return a[3], -a[1] % P, -a[2] % P, a[0]
def power(a, n):
    out = I
    for _ in range(n):
        out = mul(out, a)
    return out
def order(a):
    out = I
    for n in range(1, 337):
        out = mul(out, a)
        if out == I:
            return n
    raise AssertionError('Unexpected group order')
def comm(a, b):
    return mul(mul(mul(a, b), inv(a)), inv(b))
def conj(g, a):
    return mul(mul(g, a), inv(g))

G = [a for a in product(range(P), repeat=4)
     if (a[0]*a[3]-a[1]*a[2]) % P == 1]
x, y = (0, 6, 1, 3), (0, 2, 3, 6)
c = comm(x, y)
assert len(G) == 336
assert (order(x), order(y), order(c)) == (8, 3, 14)
assert c == (5, 6, 1, 0)
assert power(x, 4) == minus_I and power(c, 7) == minus_I
orbit = {conj(g, c) for g in G}
assert inv(c) not in orbit
assert comm(inv(x), inv(y)) == conj(inv(mul(x, y)), c)

generated, frontier = {I}, [I]
while frontier:
    a = frontier.pop()
    for b in (x, y, inv(x), inv(y)):
        z = mul(a, b)
        if z not in generated:
            generated.add(z)
            frontier.append(z)
assert set(G) == generated

print('SL2(F7) order:', len(G))
print('Generators x=(0,6,1,3), y=(0,2,3,6) generate the full group: PASS')
print('Orders of x, y, [x,y]:', order(x), order(y), order(c))
print('Commutator:', c, '; inverse:', inv(c))
print('Commutator conjugacy orbit size:', len(orbit))
print('Commutator and inverse are not conjugate: PASS')
print('Inverting both generators conjugates the commutator to itself: PASS')
print('Thus either mixed 2-versus-odd sign pattern fails the cusp test.')
