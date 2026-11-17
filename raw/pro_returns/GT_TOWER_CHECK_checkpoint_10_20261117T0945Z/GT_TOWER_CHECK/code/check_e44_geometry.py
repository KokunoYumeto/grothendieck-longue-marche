#!/usr/bin/env python3
"""Independent finite and rational checks of EXIT_TOWER E.44.
This checks the stated finite permutations and rational identities only.
The infinite-group centralizer and naturality proofs are in the audit.
"""
from itertools import product, permutations
from math import prod
import sympy as sp

def comp(p,q): return tuple(p[q[i]] for i in range(len(p)))
def ident(n): return tuple(range(n))
def perm(n,*cycles):
 p=list(range(n))
 for cyc in cycles:
  for x,y in zip(cyc,cyc[1:]+cyc[:1]): p[x]=y
 return tuple(p)
def subgroup(gens,n):
 G={ident(n)}; todo=list(G)
 while todo:
  g=todo.pop()
  for h in gens:
   k=comp(g,h)
   if k not in G: G.add(k); todo.append(k)
 return G
def image(g,S): return frozenset(g[s] for s in S)
I=ident(10)
a=perm(10,(2,3),(4,5),(6,7),(8,9))
b=perm(10,(0,1),(4,5),(6,8),(7,9))
H=subgroup([a,b],10)
flips=[perm(10,(0,1)),perm(10,(2,3)),perm(10,(4,5))]
Da=perm(10,(6,7),(8,9)); Db=perm(10,(6,8),(7,9))
C=subgroup(flips+[Da,Db],10)
assert len(H)==4 and len(C)==32
assert all(comp(g,h)==comp(h,g) for g in C for h in H)
# Any centralizer preserves the three distinct orbit types and acts by a
# translation on the regular orbit: 2^3*4=32, so C is the full centralizer.
m0=comp(flips[0],flips[2]); m1=comp(flips[1],flips[2])
Nimage=subgroup(list(H)+[m0,m1],10)
assert len(Nimage)==16
assert all(g in C for g in Nimage)
Nb={g for g in Nimage if image(g,{6,8})==frozenset({6,8})}
Na={g for g in Nimage if image(g,{6,7})==frozenset({6,7})}
assert len(Nb)==len(Na)==8
assert H & Nb == {I,b}
assert H & Na == {I,a}
assert {comp(h,n) for h in H for n in Nb}==Nimage
assert {comp(h,n) for h in H for n in Na}==Nimage
P=flips[2]
assert P in C and P not in Nimage
assert all(P[i]==i for i in [0,1,2,3,6,7,8,9])
print('H order:',len(H))
print('Permutation centralizer order:',len(C))
print('Predicted geometric normalizer permutation image:',len(Nimage))
print('Pure conjugacy double-coset index:',len(C)//len(Nimage))
print('Na and Nb indices:',len(Nimage)//len(Na),len(Nimage)//len(Nb))
print('H intersections with Na,Nb: <a>,<b>; checked')
print('Correction (C1 C2) is killed by all three relevant forgettings; checked')
C4=subgroup([perm(4,(0,1)),perm(4,(2,3))],4)
V=subgroup([perm(4,(0,1),(2,3)),perm(4,(0,2),(1,3))],4)
D8={g for g in permutations(range(4)) if frozenset([image(g,{0,1}),image(g,{2,3})])==frozenset([frozenset({0,1}),frozenset({2,3})])}
assert len(C4)==4 and len(V)==4 and len(D8)==8
assert len(C4 & V)==2
assert {comp(g,h) for g in C4 for h in V}==D8
print('Colored quartet: |C4|=4, |V|=4, |C4 intersect V|=2, C4 V=D8; checked')
z,L,U=sp.symbols('z lambda U')
u=(z*z+1)**2/(4*z*z)
lam=((z*z-1)/(z*z+1))**2
lb=z*z
la=((z-1)/(z+1))**2
Q=lambda x:(x+1)**2/(4*x)
S=lambda x:x/(x-1)
identities={'lambda = 1 - 1/u':lam-(1-1/u),
 'U_b = u':Q(lb)-u,
 'U_a = u/(u-1)':Q(la)-S(u),
 'S squared is identity':S(S(U))-U,
 'S fixes cone 0':S(0),
 'ell inversion preserves U':Q(1/lb)-Q(lb)}
for name,ex in identities.items():
 assert sp.factor(ex)==0,(name,sp.factor(ex))
 print('Rational identity:',name,'OK')
polys=[z*z-L,z*z-2*z+L,z*z-2*L*z+L]
discs=[sp.factor(sp.discriminant(p,z)) for p in polys]
assert all(sp.expand(a-b)==0 for a,b in zip(discs,[4*L,4*(1-L),4*L*(L-1)]))
print('Canonical Klein-four fixed-pair discriminants:',*map(str,discs),sep='\n  ')
orders=[]
for point in [0,1]:
 row=[]
 for d in discs:
  e=sp.Poly(d,L)
  k=0
  while sp.expand(e.as_expr()).subs(L,point)==0:
   e=sp.Poly(sp.div(e.as_expr(),L-point,L)[0],L); k+=1
  row.append(k%2)
 orders.append(tuple(row))
assert orders==[(1,0,1),(0,1,1)]
print('Fixed-pair monodromy flips around 0,1:',orders)
print('ALL FINITE AND RATIONAL CHECKS PASSED')
