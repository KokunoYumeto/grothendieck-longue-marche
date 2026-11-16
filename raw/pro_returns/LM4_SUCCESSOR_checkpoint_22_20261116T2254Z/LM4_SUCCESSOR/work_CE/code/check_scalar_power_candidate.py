"""An exact obstruction to the naive scalar cubic power automorphism.

This checks only x -> x^2, y -> y^2 in the free class-four exponent-seven
quotient.  It does not exclude a peripheral IA correction, or a full scalar
cubic torus action.  The associative algebra realizes the Lazard Lie group;
degree <= 4 is below the characteristic 7.
"""
from itertools import product

P = 7
DEGREE = 4

def clean(a):
    return {w: c % P for w, c in a.items() if c % P}

def add(a, b):
    out = dict(a)
    for w, c in b.items():
        out[w] = out.get(w, 0) + c
    return clean(out)

def scale(a, c):
    return clean({w: c * x for w, x in a.items()})

def mul(a, b):
    out = {}
    for u, c in a.items():
        for v, d in b.items():
            if len(u) + len(v) <= DEGREE:
                w = u + v
                out[w] = out.get(w, 0) + c * d
    return clean(out)

def power(a, n):
    out = {(): 1}
    for _ in range(n):
        out = mul(out, a)
    return out

def inv(a):
    assert a.get((), 0) == 1
    u = add(a, {(): -1})
    out = {(): 1}
    for n in range(1, DEGREE + 1):
        out = add(out, scale(power(u, n), (-1) ** n))
    return out

def exp(a):
    assert not a.get((), 0)
    out = {(): 1}
    factorial = 1
    for n in range(1, DEGREE + 1):
        factorial *= n
        out = add(out, scale(power(a, n), pow(factorial, -1, P)))
    return out

def comm(a, b):
    return mul(mul(mul(a, b), inv(a)), inv(b))

def bracket(a, b):
    return add(mul(a, b), scale(mul(b, a), -1))

def conjugate(a, b):
    return mul(mul(a, b), inv(a))

def truncate(a, degree):
    return {w: c for w, c in a.items() if len(w) <= degree}

X, Y = {(0,): 1}, {(1,): 1}
C = bracket(X, Y)
x, y = exp(X), exp(Y)
c = comm(x, y)
candidate = comm(power(x, 2), power(y, 2))
target = power(c, 4)

# Every conjugator has a logarithm.  Terms of degree >= 3 centralize c
# in this class-four quotient.  Degree-one terms are aX+bY and degree-two
# terms are d[X,Y]; these exhaust all possible effective conjugators.
orbit = set()
class_three_conjugators = []
for a, b, d in product(range(P), repeat=3):
    L = add(add(scale(X, a), scale(Y, b)), scale(C, d))
    translated = conjugate(exp(L), target)
    orbit.add(tuple(sorted(translated.items())))
    assert translated != candidate
    if truncate(translated, 3) == truncate(candidate, 3):
        class_three_conjugators.append((a, b, d))

assert power(x, P) == {(): 1}
assert power(y, P) == {(): 1}
assert pow(2, 3, P) == 1 and 2 != 1
assert len(class_three_conjugators) == P
print('Coefficient field: F7; nilpotency class: 4')
print('Scalar 2 has order3; generator powers have exponent7: PASS')
print('Exhaustive effective conjugators:', P**3)
print('Distinct conjugates of cusp^4:', len(orbit))
print('Class-three conjugators:', class_three_conjugators)
print('The candidate [x^2,y^2] is not conjugate to [x,y]^4: PASS')
print('No conclusion is drawn about a cusp-preserving IA correction.')
