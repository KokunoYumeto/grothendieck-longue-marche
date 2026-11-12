#!/usr/bin/env python3
"""Exact finite scalar images, coinvariants, and n=4 boundary cochains."""
import math,json,csv
from pathlib import Path
out=Path(__file__).resolve().parent
rows=[]
for a in range(1,23):
 for b in range(a,500//a+1,a):
  units=[u for u in range(b) if math.gcd(u,b)==1]
  # Scalar maps on C_a x C_b; faithful scalar image is modulo exponent b.
  assert all(math.gcd(u,a)==1 for u in units)
  assert all((u*v)%b in units for u in units for v in units)
  rows.append(dict(a=a,b=b,order=a*b,exponent=b,image_order=len(units),units=' '.join(map(str,units)),galois_realized='all',marking_field=f'Q(zeta_{b})'))
with open(out/'fh_abelian_images.csv','w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
shadows=[]
for N in range(1,23):
 good=[m for m in range(N) if math.gcd(2*m+1,N)==1]
 # Cyclotomic lift modulo 2N realizes both half-parameter choices at even N.
 units=[u for u in range(1,2*N+1) if math.gcd(u,2*N)==1]
 realised=sorted(set(((u-1)//2)%N for u in units))
 assert realised==good
 shadows.append({'N_ord':N,'shadow_m':good,'number':len(good),'all_galois':True})
def valuation(n,p):
 r=0
 while n and n%p==0:r+=1;n//=p
 return r
coin=[]
for p in [2,3,5,7,11,13]:
 for w in range(1,13):
  e=(1 if w%2 else 2+valuation(w,2)) if p==2 else (1+valuation(w,p) if w%(p-1)==0 else 0)
  modulus=p**(e+1)
  g=modulus
  for u in range(modulus):
   if math.gcd(u,p)==1:g=math.gcd(g,(pow(u,w,modulus)-1)%modulus)
  assert g==p**e
  coin.append({'prime':p,'weight':w,'quotient_order':p**e})
# Boundary restriction H1(F2;Z/m) -> H1(Z;Z/m)^3.
cochains=[]
for m in range(2,40):
 image={ (a,b,(-a-b)%m) for a in range(m) for b in range(m)}
 assert len(image)==m*m
 assert all((a+b+c)%m==0 for a,b,c in image)
 cochains.append({'modulus':m,'H0_order':m,'H1_order':1,'H2_order':m,'higher_trivial':True,'image_order':len(image)})
# Q8: central invariant character does not extend across nonsplit quotient.
# (sign, element) elements base {1,i,j,k}, i^2=j^2=k^2=-1.
table=[[(0,0),(0,1),(0,2),(0,3)],[(0,1),(1,0),(0,3),(1,2)],[(0,2),(1,3),(1,0),(0,1)],[(0,3),(0,2),(1,1),(1,0)]]
elems=[(s,i) for s in range(2) for i in range(4)]
def mul(a,b):
 s,i=table[a[1]][b[1]];return ((a[0]+b[0]+s)%2,i)
idx={g:i for i,g in enumerate(elems)}
assert all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a in elems for b in elems for c in elems)
characters=[]
for mask in range(256):
 v=[(mask>>i)&1 for i in range(8)]
 if all(v[idx[mul(a,b)]]==(v[idx[a]]+v[idx[b]])%2 for a in elems for b in elems):characters.append(v)
assert len(characters)==4 and all(v[idx[(1,0)]]==0 for v in characters)
result={'abelian_quotients_through_order500':len(rows),'scope':'all isomorphism types of finite two-generated abelian quotients, with scalar images; not nonabelian enumeration','shadows':shadows,'coinvariants':coin,'boundary_cochains':cochains,'Q8':{'characters_to_C2':len(characters),'restriction_to_central_C2_all_zero':True}}
(out/'fh_finite_results.json').write_text(json.dumps(result,indent=2))
print(json.dumps({'abelian_types':len(rows),'shadow_levels':len(shadows),'coinvariant_cases':len(coin),'boundary_moduli':len(cochains),'Q8_characters':len(characters)},indent=2))
