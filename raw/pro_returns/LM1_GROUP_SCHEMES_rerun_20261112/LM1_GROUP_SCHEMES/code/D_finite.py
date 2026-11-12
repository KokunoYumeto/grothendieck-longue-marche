#!/usr/bin/env python3
"""Exact finite witnesses for LM1 Part D; Python standard library only."""
from collections import Counter, deque
from itertools import product
from math import gcd
import json

def mul(x,y,n):
 a,b,c,d=x; e,f,g,h=y
 return ((a*e+b*g)%n,(a*f+b*h)%n,(c*e+d*g)%n,(c*f+d*h)%n)
def power(x,k,n):
 e=(1%n,0,0,1%n)
 while k:
  if k&1:e=mul(e,x,n)
  x=mul(x,x,n);k//=2
 return e
def generated(gens,n):
 e=(1%n,0,0,1%n); out={e};q=deque([e])
 while q:
  x=q.popleft()
  for g in gens:
   y=mul(x,g,n)
   if y not in out:out.add(y);q.append(y)
 return out

def phi(n):return sum(gcd(i,n)==1 for i in range(n))
def sl_order(n):
 v=n**3
 for p in range(2,n+1):
  if n%p==0 and all(p%d for d in range(2,int(p**.5)+1)):v=v*(p*p-1)//(p*p)
 return v

def generation():
 rows=[]
 for n in range(1,49):
  r=(0,1%n,(-1)%n,1%n);s=(0,1%n,(-1)%n,0);t=((-1)%n,0,0,1%n)
  h=generated([r,s],n);k=generated([r,s,t],n)
  size=sl_order(n)
  assert len(h)==size
  assert len(k)==size*(1 if n<=2 else 2)
  rows.append(dict(n=n,SL2=size,rho_sigma=len(h),rho_sigma_tau=len(k),GL2=size*phi(n),index_GL2=size*phi(n)//len(k)))
 return rows

def cohomology():
 V=list(product(range(2),repeat=2)); zero=(0,0)
 add=lambda a,b:tuple(x^y for x,y in zip(a,b))
 slots=[(a,b) for a in V[1:] for b in V[1:]]
 def cocycle(mask,a,b):
  return (mask>>slots.index((a,b)))&1 if a!=zero and b!=zero else 0
 Z=[]
 for mask in range(512):
  if all(cocycle(mask,a,b)^cocycle(mask,add(a,b),c)^cocycle(mask,b,c)^cocycle(mask,a,add(b,c))==0 for a,b,c in product(V,repeat=3)): Z.append(mask)
 B=set()
 for mask in range(8):
  f=lambda a:0 if a==zero else (mask>>(V.index(a)-1))&1
  B.add(sum((f(a)^f(b)^f(add(a,b)))<<i for i,(a,b) in enumerate(slots)))
 classes=[];seen=set()
 for z in Z:
  if z in seen:continue
  coset={z^b for b in B};seen|=coset
  e1,e2=(1,0),(0,1)
  signature=[cocycle(z,e1,e1),cocycle(z,e2,e2),cocycle(z,e1,e2)^cocycle(z,e2,e1)]
  classes.append(signature)
 assert len(Z)==16 and len(B)==2 and len(classes)==8
 # Manuscript cocycle c((u,v),(u',v'))=u*(u'+v').
 E=list(product(range(2),repeat=3))
 def emul(a,b):
  z,u,v=a;w,x,y=b
  return (z^w^(u*(x^y)),u^x,v^y)
 one=(0,0,0)
 orders={}
 for a in E:
  b=one
  for k in range(1,9):
   b=emul(b,a)
   if b==one:orders[a]=k;break
 assert sorted(orders.values())==[1,2,2,2,2,2,4,4]
 # Canonical complementary subgroups over u=0 and u=v.
 H1={(0,0,v) for v in range(2)};H2={(0,u,u) for u in range(2)}
 def inv(a):return next(b for b in E if emul(a,b)==one)
 normal=lambda H:all(emul(emul(g,h),inv(g)) in H for g in E for h in H)
 assert not normal(H1) and not normal(H2)
 return dict(normalized_2cocycles=len(Z),normalized_2coboundaries=len(B),H2_dimension=3,extension_signatures=sorted(classes),D8_order_distribution=dict(Counter(orders.values())),complement_u0_normal=normal(H1),complement_u_eq_v_normal=normal(H2))

def dic3():
 n=4;r=(0,1,3,1);s=(0,1,3,0)
 a=(3,2,0,3);b=(3,0,2,3)
 G=generated([r,s],n);K=generated([a,b],n)
 assert len(G)==48 and len(K)==4
 cosets={}; reps=[]
 for g in sorted(G):
  if g not in cosets:
   i=len(reps);reps.append(g)
   for h in K:cosets[mul(g,h,n)]=i
 e=cosets[(1,0,0,1)]
 def cmul(i,j):return cosets[mul(reps[i],reps[j],n)]
 orders=[]
 for i in range(12):
  j=e
  for k in range(1,13):
   j=cmul(j,i)
   if j==e:orders.append(k);break
 assert Counter(orders)==Counter({1:1,2:1,3:2,4:6,6:2})
 # Reduction mod 2 is S3; its sign is determined by permutation of three nonzero vectors.
 vec=[(1,0),(0,1),(1,1)]
 def sign(g):
  a,b,c,d=g;perm=[vec.index(((a*x+b*y)%2,(c*x+d*y)%2)) for x,y in vec]
  return sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))%2
 odd_orders=[orders[i] for i,g in enumerate(reps) if sign(g)]
 assert odd_orders==[4]*6
 return dict(SL2_mod4=len(G),normal_V4=len(K),quotient_order=len(reps),order_distribution=dict(Counter(orders)),orders_over_odd_permutations=odd_orders)

def quaternion():
 # Explicit splitting (-3,3) -> M2(Q): I^2=-3, J^2=3, IJ=-JI.
 I=(0,-3,1,0);J=(0,3,1,0)
 def mm(x,y):
  a,b,c,d=x;e,f,g,h=y
  return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
 assert mm(I,I)==(-3,0,0,-3)
 assert mm(J,J)==(3,0,0,3)
 assert mm(I,J)==tuple(-v for v in mm(J,I))
 # A unit determinant on the four basis matrices proves the map is an isomorphism.
 basis=[(1,0,0,1),I,J,mm(I,J)]
 from fractions import Fraction
 A=[list(map(Fraction,row)) for row in zip(*basis)];det=Fraction(1)
 for j in range(4):
  k=next(k for k in range(j,4) if A[k][j])
  if k!=j:A[j],A[k]=A[k],A[j];det=-det
  v=A[j][j];det*=v
  for k in range(j+1,4):
   q=A[k][j]/v
   for l in range(j,4):A[k][l]-=q*A[j][l]
 assert det!=0
 return dict(I=I,J=J,basis_determinant=str(det),class_minus3_3='split; order 1',quartic='x^4-3',quartic_discriminant=-256*27,possible_ramified_primes=[2,3])

if __name__=='__main__':
 result={'cohomology':cohomology(),'dic3':dic3(),'quaternion':quaternion(),'generation':generation()}
 print(json.dumps(result,indent=2))
