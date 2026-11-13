#!/usr/bin/env python3
"""Exact free-word certificates for extracting rational Kummer cocycles.

The calculation uses independent Fox and Schreier algorithms.  The theorem
identifying the resulting exponent with kappa_n is IharaII Theorem1.
"""
from collections import defaultdict
from pathlib import Path
import json,random

OUT=Path(__file__).resolve().parent
def inverse(w):return [-a for a in reversed(w)]
def comm(a,b):return a+b+inverse(a)+inverse(b)
def power(a,k):return (a if k>=0 else inverse(a))*abs(k)
def clean(d):return {k:v for k,v in d.items() if v}
def add(a,b):
 d=defaultdict(int,a)
 for k,v in b.items():d[k]+=v
 return clean(d)
def mul(a,b):
 d=defaultdict(int)
 for (i,j),u in a.items():
  for (k,l),v in b.items():d[i+k,j+l]+=u*v
 return clean(d)
def fox_u(w):
 """For w in F', divide the abelian Fox derivative d_y(w) by s-1."""
 a=b=0;q=defaultdict(int)
 for v in w:
  if v==1:a+=1
  elif v==-1:a-=1
  elif v==2:q[a,b]+=1;b+=1
  else:b-=1;q[a,b]-=1
 assert (a,b)==(0,0)
 q=clean(q);u={}
 for j in {j for i,j in q}:
  coeff={i:c for (i,b),c in q.items() if b==j}
  acc=0
  for i in range(min(coeff),max(coeff)+1):
   acc-=coeff.get(i,0)
   if acc:u[i,j]=acc
  assert acc==0
 assert mul({(1,0):1,(0,0):-1},u)==q
 return u
def schreier_y0(w,n):
 """Coefficient of y in H_n^ab, with e_j=x^-j y x^j."""
 a=0;out=0
 for v in w:
  if abs(v)==1:a+=v
  elif a%n==0:out+=1 if v==2 else -1
 assert a%n==0
 return out
def extract(u,n):
 out=[0]*n
 for (a,b),v in u.items():out[a%n]+=v
 return out[0]-out[n-1]
def ageom(k,axis):
 rg=range(k) if k>0 else range(k,0)
 return {(a,0) if axis==0 else (0,a):1 if k>0 else -1 for a in rg}
def spow_minus1(k,axis):
 return {(k,0) if axis==0 else (0,k):1,(0,0):-1}

rng=random.Random(410731)
c=comm([1],[2]);words=[[],c,inverse(c)]
for _ in range(157):
 w=[]
 for _ in range(rng.randrange(1,8)):
  h=[rng.choice([1,-1,2,-2]) for _ in range(rng.randrange(0,13))]
  w+=h+power(c,rng.choice([-3,-2,-1,1,2,3]))+inverse(h)
 words.append(w)
tests=0;commtests=0
for j,w in enumerate(words):
 u=fox_u(w)
 for n in range(1,25):
  assert extract(u,n)==-schreier_y0(w,n),(j,n)
  tests+=1
 if j<35:
  for k in [-5,-3,-1,1,3,5]:
   auto_c=comm(power([1],k),inverse(w)+power([2],k)+w)
   got=fox_u(auto_c)
   predicted=add(mul(ageom(k,0),ageom(k,1)),
                 mul(mul(spow_minus1(k,0),spow_minus1(k,1)),u))
   assert got==predicted,(j,k)
   commtests+=1

result={'free_words':len(words),'levels':list(range(1,25)),
        'Fox_Schreier_comparisons':tests,'commutator_action_comparisons':commtests,
        'formula':'kappa_n=coefficient_0(u(s,1) mod(s^n-1))-coefficient_(n-1)(u(s,1) mod(s^n-1))',
        'measure_formula':'F_g=A_chi(s) A_chi(t) [1+(s-1)(t-1)u_g]',
        'scope':'Exact combinatorial identities. Galois interpretation uses IharaII Theorem1.'}
(OUT/'d_kummer_measure.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
