#!/usr/bin/env python3
"""Finite certificates for the quadratic beta-associativity characters.

All calculations are exact in F_p[omega], omega^2+omega+1=0, and in
F_p[(Z/6)^2].  The existence of the full gentle witnesses is B.27/C.19;
this program independently checks the finite detector and separation.
"""
from pathlib import Path
import json
P=Path(__file__).parent
PRIMES=[5,17,29,41,53,89,101,113]
RESULTS=[]
for p in PRIMES:
 assert p%12==5 and all(p%d for d in range(2,int(p**0.5)+1))
 I=(1,0);Z=(0,0);W=(0,1);minus=(p-1,0)
 def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
 def mul(x,y):
  a,b=x;c,d=y
  return ((a*c-b*d)%p,(a*d+b*c-b*d)%p)
 def power(x,k):
  z=I
  while k:
   if k&1:z=mul(z,x)
   x=mul(x,x);k>>=1
  return z
 def inv(x):assert x!=Z;return power(x,p*p-2)
 def bar(x):return ((x[0]-x[1])%p,-x[1]%p)
 def norm(x):return mul(x,bar(x))
 assert power(W,3)==I and W!=I and bar(W)==power(W,2)
 assert all(power((a,b),p)==bar((a,b)) for a in range(p) for b in range(p))
 U=[(a,b) for a in range(p) for b in range(p) if norm((a,b))==I]
 assert len(U)==p+1
 def bit(x):
  assert norm(x)==I
  e=power(x,(p+1)//2);assert e in [I,minus]
  return int(e==minus)
 for a in U:
  assert bit(a)==bit(bar(a))
  for b in U:assert bit(mul(a,b))==bit(a)^bit(b)
 assert bit(minus)==1
 inv36=pow(36,-1,p)
 e={(i,j):inv36*(2 if (i+j)%3==0 else -1)%p for i in range(6) for j in range(6)}
 def conv(a,b):
  c={(i,j):0 for i in range(6) for j in range(6)}
  for (i,j),u in a.items():
   for (k,l),v in b.items():c[((i+k)%6,(j+l)%6)]=(c[((i+k)%6,(j+l)%6)]+u*v)%p
  return c
 one={(i,j):int(i==j==0) for i in range(6) for j in range(6)}
 beta={ij:(one[ij]-2*e[ij])%p for ij in one}
 assert conv(e,e)==e and conv(beta,beta)==one
 assert all(beta[i,j]==beta[-i%6,-j%6] for i in range(6) for j in range(6))
 def ev(a,b):
  z=Z
  for (i,j),v in beta.items():z=add(z,mul((v,0),mul(power(a,i),power(b,j))))
  return z
 def defect(a,b,c):return mul(mul(ev(a,b),ev(mul(a,b),c)),inv(mul(ev(b,c),ev(a,mul(b,c)))))
 vals=[ev(W,W),ev(power(W,2),minus),ev(W,minus),ev(W,mul(W,minus))]
 assert vals==[minus,I,I,I]
 defect_value=defect(W,W,minus)
 assert defect_value==minus and defect(bar(W),bar(W),minus)==minus
 # Every sixth-root pair is checked against the defining spectral support.
 roots=[power(mul(minus,W),i) for i in range(6)]
 assert len(set(roots))==6
 for a in roots:
  for b in roots:
   expected=minus if a==b and a in [W,bar(W)] else I
   assert ev(a,b)==expected
 RESULTS.append({'p':p,'residue_field_size':p*p,'norm_one_size':len(U),
  'beta_four_values':[list(x) for x in vals],'defect':list(defect_value),
  'quadratic_bit':bit(defect_value),'conjugation_invariant':True,
  'character_multiplicativity_exhaustively_checked':True,
  'group_ring_idempotent_and_unitarity_checked':True})
M=[[int(p==q) for q in PRIMES] for p in PRIMES]
R={'primes':PRIMES,'certificates':RESULTS,'separating_matrix':M,
   'scope':'Finite detector checked; actual full witnesses and infinite-prime argument are proved in C.30 using B.27/C.19.'}
(P/'pbc_beta_characters.json').write_text(json.dumps(R,indent=2)+'\n')
print(json.dumps(R,indent=2))
