#!/usr/bin/env python3
"""Exact local Kummer exponents; biquadratic CM norm maps at 2 and 3.
No external number-theory system. O_L=Z[i,z], i^2=-1,z^2-z+1=0.
"""
from itertools import product
from math import gcd
from pathlib import Path
import json,time
OUT=Path(__file__).resolve().parent

def primes(n):return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]
def val(a,p):
 e=0
 while a%p==0:a//=p;e+=1
 return e

def norm3(a,b,m):return (a*a+a*b+b*b)%m
def norm4(a,b,m):return (a*a+b*b)%m
def mul3(a,b,c,d,m):return ((a*c-b*d)%m,(a*d+b*c+b*d)%m)
def norms(a,b,c,d,m):
 # element a+b*z+i*(c+d*z)
 A=mul3(a,b,a,b,m);B=mul3(c,d,c,d,m)
 n3=((A[0]+B[0])%m,(A[1]+B[1])%m)
 # (a+ci)^2+(a+ci)(b+di)+(b+di)^2
 n4=((a*a-c*c+a*b-c*d+b*b-d*d)%m,(2*a*c+a*d+b*c+2*b*d)%m)
 return n3+n4

def local(p,k):
 m=p**k;start=time.time();image=set();units=0
 for a,b,c,d in product(range(m),repeat=4):
  v=norms(a,b,c,d,m)
  if norm3(*v[:2],m)%p:
   units+=1;image.add(v)
 A={};B={}
 for a,b in product(range(m),repeat=2):
  n=norm3(a,b,m)
  if n%p:A.setdefault(n,[]).append((a,b))
  n=norm4(a,b,m)
  if n%p:B.setdefault(n,[]).append((a,b))
 target=sum(len(v)*len(B.get(n,[])) for n,v in A.items())
 r1=((-1)%m,0,1,0);r2=(1,0,0,1)
 r12=((-1)%m,0,0,1)
 row={'p':p,'k':k,'modulus':m,'source_units':units,'equal_norm_pairs':target,'norm_image':len(image),'index':target//len(image),'minus_one_one_in_image':r1 in image,'one_i_in_image':r2 in image,'minus_one_i_in_image':r12 in image}
 assert all(norm3(*v[:2],m)==norm4(*v[2:],m) for v in image)
 print(row,'seconds',round(time.time()-start,3),flush=True)
 return row

def d4():
 G=list(product(range(4),range(2)));ident=(0,0)
 def mul(g,h):return ((g[0]+(-1)**g[1]*h[0])%4,(g[1]+h[1])%2)
 def inv(g):return next(h for h in G if mul(g,h)==ident)
 def comm(g,h):return mul(mul(mul(g,h),inv(g)),inv(h))
 A3=[g for g in G if (g[0]+g[1])%2==0];A4=[g for g in G if g[1]==0]
 assert all(comm(g,h)==ident for A in (A3,A4) for g,h in product(A,repeat=2))
 derived=sorted({comm(g,h) for g,h in product(G,repeat=2)})
 pairs=[(g,h) for g,h in product(G,repeat=2) if (g[0]%2,g[1])==(h[0]%2,h[1])]
 row={'group_order':8,'K3_abelian_subgroup':A3,'K4_abelian_subgroup':A4,'commutator_subgroup':derived,'same_abelianization_pairs':len(pairs),'diagonal_image':8,'extra_index':len(pairs)//8}
 print('D4 certificate',row);return row

def main():
 P=primes(50);kum=[]
 for p,l in product(P,repeat=2):
  e=(1 if p==2 else val(p*p-1,2)-2) if l==2 else (0 if p==l else val(p**(l-1)-1,l)-1)
  assert e>=0
  kum.append({'rational_prime':p,'residue_prime':l,'image':f'{l}^{e} Z_{l}','index':l**e})
 print('Non-surjective local I_l^+ Kummer images:',[r for r in kum if r['index']>1])
 rows=[local(2,k) for k in range(1,6)]+[local(3,k) for k in range(1,4)]
 (OUT/'d_local_cm.json').write_text(json.dumps({'local_Kummer_images':kum,'CM_local_norms':rows,'D4_entanglement':d4()},indent=2))
if __name__=='__main__':main()
