#!/usr/bin/env python3
"""Exact two-dimensional certificates for B.28/B.29 and C.19.

No numerical approximation, external algebra package, or inherited code.
The point count, both GL2(F5) classifications, and the central Q12
derived image are enumerated directly.
"""
import itertools
import json
from pathlib import Path

def matmul(a, b, n):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % n
                 for i in range(2) for j in range(2))

def det(a, n):
    return (a[0]*a[3]-a[1]*a[2]) % n

def inv(a, n):
    d = pow(det(a, n), -1, n)
    return (d*a[3] % n, -d*a[1] % n, -d*a[2] % n, d*a[0] % n)

def neg(a, n):
    return tuple(-x % n for x in a)

def conjugate(a, b, n):
    return matmul(matmul(a, b, n), inv(a, n), n)

I = (1, 0, 0, 1)
gl5 = [a for a in itertools.product(range(5), repeat=4) if det(a, 5)]
T3 = (0, 4, 1, 4)
C3 = (1, 0, 1, 4)
J4 = (0, 4, 1, 0)
C4 = (1, 0, 0, 4)
assert matmul(C3, C3, 5) == I == matmul(C4, C4, 5)
assert conjugate(C3, T3, 5) == inv(T3, 5)
assert conjugate(C4, J4, 5) == inv(J4, 5)
assert matmul(T3, matmul(T3, T3, 5), 5) == I
assert matmul(J4, J4, 5) == neg(I, 5)
normal3 = [a for a in gl5 if conjugate(a, T3, 5) in (T3, inv(T3, 5))]
normal4 = [a for a in gl5 if conjugate(a, J4, 5) in (J4, inv(J4, 5))]
cubic = [a for a in normal3 if conjugate(a, C3, 5) == neg(C3, 5)]
quartic = [a for a in normal4 if conjugate(a, C4, 5) == C4]
assert len(gl5) == 480 and len(normal3) == 48 and len(normal4) == 32
assert len(cubic) == len(quartic) == 8
assert {det(a, 5) for a in cubic} == {2, 3}
assert {det(a, 5) for a in quartic} == {1, 4}

p = 13
points = [(x, y) for x in range(p) for y in range(p)
          if (y*y-x*x*x-16) % p == 0]
cardinality = len(points)+1
frobenius_trace = p+1-cardinality
assert cardinality == 9 and frobenius_trace == 5
frobenius_options = [a for a in gl5
    if matmul(a, T3, 5) == matmul(T3, a, 5)
    and (a[0]+a[3]) % 5 == frobenius_trace % 5 and det(a, 5) == p % 5]
assert len(frobenius_options) == 2
assert all(conjugate(a, C3, 5) == neg(C3, 5) for a in frobenius_options)

def projective(a):
    return min(a, neg(a, 12))

def pmul(a, b):
    return projective(matmul(a, b, 12))

def pinv(a):
    return projective(inv(a, 12))

pi = projective(I)
def generated(gens):
    gens = list(set(gens))
    seen, todo = {pi}, [pi]
    while todo:
        a = todo.pop()
        for b in gens:
            c = pmul(a, b)
            if c not in seen:
                seen.add(c)
                todo.append(c)
    return seen

def derived(group):
    return generated(pmul(pmul(a,b),pmul(pinv(a),pinv(b)))
                     for a in group for b in group)

s = projective((0, 11, 1, 0))
r = projective((0, 11, 1, 11))
tau = pmul(s, r)
x = pmul(pinv(tau), pinv(tau))
y = pmul(pmul(s, x), s)
Q12 = generated([s, r])
F12 = generated([x, y])
F12prime = derived(F12)
F12second = derived(F12prime)
assert [len(g) for g in (Q12, F12, F12prime, F12second)] == [576,96,8,2]
assert all(pmul(a, b) == pmul(b, a) for a in F12second for b in Q12)

out = dict(
    GL2_F5_order=len(gl5),
    cubic_normalizer_order=len(normal3),
    quartic_normalizer_order=len(normal4),
    cubic_conjugators=[dict(matrix=a,det=det(a,5)) for a in cubic],
    quartic_conjugators=[dict(matrix=a,det=det(a,5)) for a in quartic],
    cubic_determinants=sorted({det(a,5) for a in cubic}),
    quartic_determinants=sorted({det(a,5) for a in quartic}),
    E_y2_x3_plus16=dict(prime=p,affine_points=points,
        total_points=cardinality,Frobenius_trace=frobenius_trace,
        Frobenius_matrices_mod5=frobenius_options),
    Q12=dict(order=len(Q12),F_order=len(F12),
        F_derived_order=len(F12prime),F_second_derived_order=len(F12second),
        F_second_derived_elements=sorted(F12second),
        F_second_derived_central=True),
    conclusions=dict(negative_Q75_residue_Galois_realized=True,
        two_CM_determinants_incompatible=True,central_Q12_factorization=True))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
