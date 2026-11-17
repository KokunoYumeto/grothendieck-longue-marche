#!/usr/bin/env python3
"""Exact character lattice and rational-origin coordinate certificates."""
import sympy as s
from fractions import Fraction as F

chars=s.Matrix([[1]*9+[0]*9+[-1]*9,[0]*9+[1]*9+[-1]*9])
blocks=s.zeros(27,2)
for j in range(9): blocks[j,0]=1; blocks[9+j,1]=1
assert chars*s.ones(27,1)==s.zeros(2,1)
assert chars.rank()==2
assert chars*blocks==9*s.eye(2)
assert 3*chars*blocks==27*s.eye(2)
print('PASS: both boundary characters kill the diagonal and have rank two')
print('PASS: block constants give 9*I_2 on (u,v) and 27*I_2 on the original coordinates')

x,y=F(7),F(10)
R=(y-27)/(3*x); S=(y+27)/(3*x)
X=(x**3-972)/(9*x*x); Y=y*(x**3+1944)/(27*x**3)
k=(Y-15)/(X-6); Xf=k*k-X-6
u=Xf*S/(6*(k-3)); v=Xf*R/(6*(k-2))
assert u==F(253,655) and v==F(-488,655)
assert 3*u**3-2*v**3==1
assert 3*u**3==F(48582831,281011375)
assert (F(6)**3+36)/F(6)**2==7
assert F(15)*(F(6)**3-72)/F(6)**3==10
print('PASS: phi(P0)=(7,10), u(P0)=253/655, v(P0)=-488/655')
print('PASS: t(P0)=48582831/281011375 and the cubic equation holds exactly')
