#!/usr/bin/env python3
"""Finite check of the level-four lift/face distinction in cote 64/066–069.

No manuscript readings are changed.  A frame has columns lifting (1,0),(0,1),
and its third marked nonzero mod-2 vector is represented by minus their sum.
The quotient to an octahedral face forgets simultaneous sign.
"""
from collections import Counter, defaultdict
from itertools import product

M = list(product(range(4), repeat=2))
J = ((1, 0), (0, 1), (1, 1))

def add(a, b):
    return tuple((x+y) % 4 for x, y in zip(a,b))

def neg(a):
    return tuple(-x % 4 for x in a)

def red(a):
    return tuple(x % 2 for x in a)

def sign_class(a):
    return min(a,neg(a))

def det(a,b):
    return (a[0]*b[1]-a[1]*b[0]) % 4

lifts = {j:[a for a in M if red(a)==j] for j in J}
P = [triple for triple in product(*(lifts[j] for j in J))
     if add(add(triple[0],triple[1]),triple[2])==(0,0)]
assert len(P)==16
assert all(p[2]==neg(add(p[0],p[1])) for p in P)
assert all(det(p[0],p[1]) in (1,3) for p in P)

faces=defaultdict(list)
for p in P:
    faces[tuple(sign_class(a) for a in p)].append(p)
all_faces=set(product(*(sorted({sign_class(a) for a in lifts[j]}) for j in J)))
assert set(faces)==all_faces
assert len(faces)==8
assert set(map(len,faces.values()))=={2}
assert all(set(ps)=={ps[0],tuple(neg(a) for a in ps[0])} for ps in faces.values())
assert Counter(det(p[0],p[1]) for p in P)=={1:8,3:8}
assert Counter(det(ps[0][0],ps[0][1]) for ps in faces.values())=={1:4,3:4}

# The action of V_J(M_0) adds twice a zero-sum F_2 triple.
V0 = [v for v in product(list(product(range(2),repeat=2)),repeat=3)
      if tuple(sum(a[k] for a in v)%2 for k in range(2))==(0,0)]
base=P[0]
orbit={tuple(add(base[i],tuple(2*x for x in v[i])) for i in range(3)) for v in V0}
assert len(V0)==16 and orbit==set(P)

# Full and determinant-one module frame counts, before quotienting by ±I.
GL=[(a,b) for a,b in product(M,repeat=2) if det(a,b) in (1,3)]
SL=[(a,b) for a,b in GL if det(a,b)==1]
assert len(GL)==96 and len(SL)==48
assert len({min(g,tuple(neg(a) for a in g)) for g in GL})==48
assert len({min(g,tuple(neg(a) for a in g)) for g in SL})==24

print('PASS: all assertions checked by complete enumeration in (Z/4)^2.')
print('Fixed reduction mod 2: 16 zero-sum lifts; 8 faces; exactly 2 lifts per face, related by simultaneous minus sign.')
print('Fixed determinant 1 or 3: 8 zero-sum lifts and 4 faces each.')
print('V_J(M_0) has 16 elements and acts simply transitively on the zero-sum lifts.')
print('GL_2(Z/4): 96; SL_2(Z/4): 48; quotients by ±I: 48 and 24 respectively.')
print('Interpretive limit: this is a finite module/face certificate, not a global moduli representability or GT-congruence-kernel proof.')
