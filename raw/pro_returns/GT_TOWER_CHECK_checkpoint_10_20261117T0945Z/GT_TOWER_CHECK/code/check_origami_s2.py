#!/usr/bin/env python3
"""Exact cover and monodromy audit of Moeller's two-step origami."""
import itertools
import sympy as s

x,t=s.symbols('x t')
P=4*x*(x-1)
source=(P**2-(1-t))*(P-1)
v2=s.expand((2*x-1)**2*source)
elliptic=(P-1)*(P+1)*(P**2-(1-t))
assert s.expand(v2-elliptic)==0
assert s.expand(P**2*v2-P**2*(P**2-1)*(P**2-(1-t)))==0
print('PASS: (x,y) -> (4x(x-1),(2x-1)y) maps the genus-two model to E1.')
print('PASS: (w,v) -> (w^2,wv) maps E1 to v^2=u(u-1)(u-(1-t)).')

I=tuple(range(4))
a=(1,0,3,2)
b=(0,2,1,3)
def mul(p,q):return tuple(p[q[i]] for i in range(4))
def inv(p):return tuple(p.index(i) for i in range(4))
G={I};todo=[I]
while todo:
 p=todo.pop()
 for q in [a,b]:
  r=mul(p,q)
  if r not in G:G.add(r);todo.append(r)
C=[p for p in itertools.permutations(range(4)) if all(mul(p,q)==mul(q,p) for q in [a,b])]
comm=mul(mul(mul(a,b),inv(a)),inv(b))
assert len(G)==8 and len(C)==2
assert comm==(3,2,1,0)
blocks=[frozenset([0,3]),frozenset([1,2])]
assert all(frozenset(p[i] for i in B) in blocks for p in G for B in blocks)
print('PASS: monodromy group order 8; deck centralizer order 2; commutator has two 2-cycles.')
print('PASS: intermediate degree-two block system is {1,4}|{2,3}.')
print('The genus-two cover has degree 4 and is not regular: its deck group has order 2.')
print('No GT-equivariance or separating-invariant assertion is inferred from these checks.')
