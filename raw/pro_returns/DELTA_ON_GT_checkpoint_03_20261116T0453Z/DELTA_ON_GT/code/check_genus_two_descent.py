#!/usr/bin/env python3
"""The standard genus-two B5 homology representation does not descend to Gamma05."""
import sympy as s
J=s.zeros(4)
for i in range(3):
    J[i,i+1]=1
    J[i+1,i]=-1
T=[]
for i in range(4):
    e=s.eye(4)[:,i]
    T.append(s.eye(4)+e*e.T*J)
assert J.det()==1
assert all(A.T*J*A==J for A in T)
assert all(T[i]*T[i+1]*T[i]==T[i+1]*T[i]*T[i+1] for i in range(3))
assert all(T[i]*T[j]==T[j]*T[i] for i in range(4) for j in range(4) if abs(i-j)>=2)
R=T[3]*T[2]*T[1]*T[0]**2*T[1]*T[2]*T[3]
F=(T[0]*T[1]*T[2]*T[3])**5
assert F==-s.eye(4)
E=s.zeros(4);E[0,3]=2;E[2,3]=2
assert R==-s.eye(4)+E
for n in [3,4,12]:
    Rn=R.applyfunc(lambda a:a%n)
    assert Rn not in [s.eye(4),(-s.eye(4)).applyfunc(lambda a:a%n)]
    print(f'PASS sphere relator nontrivial even modulo global sign at N={n}')
print('Unimodular symplectic matrix J:')
print(J)
print('Sphere relator:')
print(R)
print('Full twist:')
print(F)
print('PASS standard B5 genus-two representation fails the Gamma0,[5] sphere relation.')
