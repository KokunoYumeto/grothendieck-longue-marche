#!/usr/bin/env python3
"""Check Willwacher's t4 representation using exact F2 words and exterior variables.
The mathematical proof in the paper verifies the same finite operator identities
by Leibniz; this is an independent bounded implementation check.
"""
from itertools import product,combinations
from pathlib import Path
import json
# M words (tuple in A,B,C, epsilon exponent, eta exponent), coefficients F2.
def plus(*sets):
 s=set()
 for t in sets:s.symmetric_difference_update(t)
 return s
def left(word,S):return {(word+w,e,h) for w,e,h in S}
def times_eps(S,j):return {(w,1,h) if j==0 else (w,e,1) for w,e,h in S if (e if j==0 else h)==0}
def diff(S,j):return {(w,0,h) if j==0 else (w,e,0) for w,e,h in S if (e if j==0 else h)==1}
Eimg={0:{(0,1),(1,0)},1:set(),2:{(0,1),(1,0)}}
Timg={0:set(),1:{(2,1),(1,2)},2:{(0,1,1),(1,1,0)}}
def deriv(img,S):
 out=set()
 for w,e,h in S:
  for i,a in enumerate(w):
   for v in img[a]:
    q=(w[:i]+v+w[i+1:],e,h)
    if q in out:out.remove(q)
    else:out.add(q)
 return out
def E(S):return deriv(Eimg,S)
def T(S):return deriv(Timg,S)
def G(S):return plus(left((0,),S),left((2,),S),T(S))
def ab(S):return plus(left((0,1),S),left((1,0),S))
def rho(ij,S):
 if ij==(0,1):return times_eps(S,0)
 if ij==(1,2):return left((0,),diff(S,0))
 if ij==(0,2):return plus(times_eps(S,0),times_eps(S,1),left((0,),plus(diff(S,0),diff(S,1))))
 if ij==(2,3):return plus(left((1,),S),left((2,),diff(S,1)))
 if ij==(1,3):return plus(E(S),G(plus(diff(S,0),diff(S,1))),ab(diff(diff(S,0),1)))
 if ij==(0,3):return plus(*(rho(k,S) for k in [(0,1),(0,2),(1,2),(1,3),(2,3)]))
 raise ValueError(ij)
def comm(a,b,S):return plus(rho(a,rho(b,S)),rho(b,rho(a,S)))
rels=[]
for i,j,k in combinations(range(4),3):
 for a,b,c in [(i,j,k),(i,k,j),(j,k,i)]:
  e=tuple(sorted((a,b)));f=tuple(sorted((a,c)));g=tuple(sorted((b,c)))
  rels.append((e,f,g))
for a,b in [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]:rels.append((a,b,None))
count=0
for n in range(5):
 for w in product(range(3),repeat=n):
  for e,h in product(range(2),repeat=2):
   S={(w,e,h)}
   for a,b,c in rels:
    value=comm(a,b,S)
    if c is not None:value=plus(value,comm(a,c,S))
    assert not value,(w,e,h,a,b,c,value)
    count+=1
result={'field':2,'free_word_lengths':'0..4','module_basis_inputs':4*sum(3**n for n in range(5)),'braid_relations':len(rels),'identities_checked':count,'all_zero':True}
Path(__file__).with_name('g_operator_results.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
