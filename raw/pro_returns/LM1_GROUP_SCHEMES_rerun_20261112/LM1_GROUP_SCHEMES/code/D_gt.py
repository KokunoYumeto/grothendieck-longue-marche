#!/usr/bin/env python3
"""Finite necessary I/II equations; never identifies these with full GT images."""
from D_finite import mul, power, generated
from itertools import product, combinations
from collections import deque
from math import gcd,lcm
import json

def inv(a,n):return (a[3]%n,(-a[1])%n,(-a[2])%n,a[0]%n)
def finite_relations(n):
 E=(1%n,0,0,1%n)
 x=((-1)%n,2%n,0,(-1)%n);y=((-1)%n,0,(-2)%n,(-1)%n)
 z=inv(mul(x,y,n),n)
 A=(x,y,z,y);B=(y,x,x,z);one=(E,)*4
 tm=lambda a,b:tuple(mul(u,v,n) for u,v in zip(a,b))
 ti=lambda a:tuple(inv(u,n) for u in a)
 def closure(gens):
  H={one};q=deque([one])
  while q:
   a=q.popleft()
   for b in gens:
    c=tm(a,b)
    if c not in H:H.add(c);q.append(c)
  return H
 H=closure([A,B]);comm=tm(tm(tm(A,B),ti(A)),ti(B))
 D=closure([tm(tm(h,comm),ti(h)) for h in H])
 K=generated([x,y],n)
 def order(g):
  a=E
  for i in range(1,len(K)+1):
   a=mul(a,g,n)
   if a==E:return i
 per=lcm(order(x),order(y),order(z));modulus=2*per
 def induces_automorphism(lam,f):
  X=power(x,lam,n);Y=mul(mul(inv(f,n),power(y,lam,n),n),f,n)
  images={E:E};q=deque([E])
  while q:
   a=q.popleft()
   for b,c in [(x,X),(y,Y)]:
    ab=mul(a,b,n);im=mul(images[a],c,n)
    if ab in images:
     if images[ab]!=im:return False
    else:images[ab]=im;q.append(ab)
  return len(set(images.values()))==len(K)
 rows=[]
 for lam in range(modulus):
  if gcd(lam,modulus)!=1:continue
  m=(lam-1)//2;sol=[]
  for fxy,fyx,fzx,fyz in sorted(D):
   if mul(fyx,fxy,n)!=E:continue
   h=E
   for u in [fzx,power(z,m,n),fyz,power(y,m,n),fxy,power(x,m,n)]:h=mul(h,u,n)
   if h==E:sol.append((fxy,induces_automorphism(lam,fxy)))
  rows.append(dict(lambda_residue=lam,solutions=len(sol),induced_automorphisms=sum(b for a,b in sol),fxy=[a for a,b in sol]))
 return dict(n=n,loop_image_order=len(K),simultaneous_evaluation_order=len(H),derived_evaluation_order=len(D),lambda_modulus=modulus,rows=rows)

def noncongruence():
 def fmul(a,b):
  c=0
  while b:
   if b&1:c^=a
   b>>=1;a<<=1
   if a&8:a^=11
  return c
 def mm(a,b):
  A,B,C,D=a;E,F,G,H=b
  return (fmul(A,E)^fmul(B,G),fmul(A,F)^fmul(B,H),fmul(C,E)^fmul(D,G),fmul(C,F)^fmul(D,H))
 I=(1,0,0,1);u=(1,2,0,1);v=(0,1,1,1)
 H={I};q=deque([I])
 while q:
  a=q.popleft()
  for b in (u,v):
   c=mm(a,b)
   if c not in H:H.add(c);q.append(c)
 invs={a:(a[3],a[1],a[2],a[0]) for a in H}
 assert mm(u,u)==I and mm(mm(v,v),v)==I and len(H)==504
 seen=set();sizes=[]
 for a in H:
  if a in seen:continue
  C={mm(mm(h,a),invs[h]) for h in H};seen|=C;sizes.append(len(C))
 sizes.sort();rest=sizes[1:]
 good=all(504%(1+sum(c))!=0 for k in range(1,len(rest)) for c in combinations(rest,k))
 assert good
 return dict(field='F2[t]/(t^3+t+1)',generator_order_2=u,generator_order_3=v,order=len(H),conjugacy_class_sizes=sizes,simplicity_by_class_union=True)

def norm_tests():
 rows=[]
 for n in (4,8,16,9,27,25,49):
  q2=sorted({(a*a+b*b)%n for a,b in product(range(n),repeat=2) if gcd((a*a+b*b)%n,n)==1})
  q3=sorted({(a*a+a*b+b*b)%n for a,b in product(range(n),repeat=2) if gcd((a*a+a*b+b*b)%n,n)==1})
  rows.append(dict(modulus=n,Gaussian_unit_norms=q2,Eisenstein_unit_norms=q3))
 return rows

if __name__=='__main__':
 print(json.dumps(dict(finite_I_II=[finite_relations(n) for n in [2,3,4,6,12]],noncongruence=noncongruence(),norm_tests=norm_tests()),indent=2))
