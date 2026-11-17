#!/usr/bin/env python3
from pathlib import Path
import json
H=Path(__file__).resolve().parent
#1 Cminus,2 Cplus,3 f; only cone squares are reduced.
def red(w):
 o=[]
 for j in w:
  if abs(j)in(1,2):j=abs(j)
  if o and(o[-1]==-j or j in(1,2)and o[-1]==j):o.pop()
  else:o.append(j)
 return tuple(o)
def inv(w):return tuple(-j for j in reversed(w))
def sub(w,A):return red(x for j in w for x in(A[abs(j)]if j>0 else inv(A[-j])))
phi=[{1:(-3,1,3),2:(2,),3:(-3,1,3,1,3)},
     {1:(1,),2:(3,2,-3),3:(3,2,3,2,-3)}]
psi=[{1:(1,3,1,-3,1),2:(2,),3:(1,3,1)},
     {1:(1,),2:(2,-3,2,3,2),3:(2,3,2)}]
for A,B in zip(phi,psi):
 for j in range(1,4):
  assert sub(A[j],B)==(j,)
  assert sub(B[j],A)==(j,)
  assert sum((1 if x>0 else -1)for x in A[j]if abs(x)==3)==int(j==3)
 for j in(1,2):assert not red(A[j]+A[j])
(H/'coarse_annular_actions23.json').write_text(json.dumps({'status':'PASS','phi_conjugation_by_k':phi,'psi_positive_push':psi,'all_inverse_compositions':12,'relations_used':'Cminus²=Cplus²=1 only'},indent=2)+'\n')
print('PASS all12 actual coarse action inverse compositions and both cone/height conditions')
