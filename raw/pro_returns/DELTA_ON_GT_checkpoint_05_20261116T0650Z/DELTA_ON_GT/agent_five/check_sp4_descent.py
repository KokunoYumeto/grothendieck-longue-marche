#!/usr/bin/env python3
import sympy as s
J=s.diag(s.Matrix([[0,1],[-1,0]]),s.Matrix([[0,1],[-1,0]]))
vs=[s.Matrix(x) for x in [(1,0,0,0),(0,1,0,0),(1,0,1,0),(0,0,0,1)]]
T=[s.eye(4)+v*v.T*J for v in vs]
for t in T:assert t.T*J*t==J
for i in range(3):assert T[i]*T[i+1]*T[i]==T[i+1]*T[i]*T[i+1]
for i in range(4):
 for j in range(i+2,4):assert T[i]*T[j]==T[j]*T[i]
P=s.eye(4)
for t in T:P=P*t
H=T[3]*T[2]*T[1]*T[0]**2*T[1]*T[2]*T[3]
assert P**5==-s.eye(4)
print('All Artin braid and symplectic identities hold exactly over Z.')
print('Full twist:',(P**5).tolist())
print('Sphere relator:',H.tolist())
for n in (3,12):
 h=H.applyfunc(lambda x:x%n)
 assert h[2,3]!=0
 print('Sphere relator mod',n,':',h.tolist(),'; nonscalar, so descent fails.')
