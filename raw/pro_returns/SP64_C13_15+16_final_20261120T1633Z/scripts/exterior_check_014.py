"""Exact exterior-algebra calculation for N16-014-C1/C2; no image processing."""
import sympy as s
N=16
def wedge(a,b):
 if a&b:return 0,0
 swaps=sum(1 for i in range(4) for j in range(4) if (a>>i)&1 and (b>>j)&1 and i>j)
 return (-1)**swaps,a|b
def contract(k,b):
 if not (b>>k)&1:return 0,0
 return (-1)**sum((b>>j)&1 for j in range(k)),b^(1<<k)
L=s.zeros(N);C=s.zeros(N)
for b in range(N):
 for a in (3,12):
  sign,out=wedge(a,b)
  if sign:L[out,b]+=sign
 for e,f in ((0,1),(2,3)):
  sign,a=contract(e,b)
  if sign:
   sign2,out=contract(f,a)
   if sign2:C[out,b]+=sign*sign2
v=s.eye(N)[:,0]
print('L^2(1):',[(i,x) for i,x in enumerate(L*L*v) if x])
print('C L(1):',[(i,x) for i,x in enumerate(C*L*v) if x])
print('C(top):',[(i,x) for i,x in enumerate(C*s.eye(N)[:,15]) if x])
print('det(L: wedge^1 -> wedge^3):',L.extract([7,11,13,14],[1,2,4,8]).det())
assert L*L*v==2*s.eye(N)[:,15]
assert C*L*v==2*v
assert L.extract([7,11,13,14],[1,2,4,8]).det()==1
