#!/usr/bin/env python3
from pathlib import Path
import json
O=Path(__file__).resolve().parent

def reduce(w):
 ans=[]
 for z in w:
  if ans and ans[-1]==-z:ans.pop()
  else:ans.append(z)
 return tuple(ans)
def inverse(w):return tuple(-z for z in reversed(w))
def subst(w,f):
 out=()
 for z in w:out=reduce(out+(f[z] if z>0 else inverse(f[-z])))
 return out
def comp(f,g):return {i:subst(g[i],f) for i in (1,2)}
def power(f,n):
 h={1:(1,),2:(2,)}
 for _ in range(n):h=comp(f,h)
 return h
A={1:(1,),2:(2,1)}
B={1:(1,-2),2:(2,)}
ABA=comp(A,comp(B,A));BAB=comp(B,comp(A,B))
assert ABA==BAB
AB=comp(A,B)
c=(1,2,-1,-2)
p6=power(AB,6)
for sign in (1,-1):
 w=c if sign==1 else inverse(c)
 expected={i:reduce(w+(i,)+inverse(w)) for i in (1,2)}
 if p6==expected: found=sign;break
else:raise AssertionError(p6)
result={'A':A,'B':B,'ABA_equals_BAB':True,'AB_sixth':p6,
 'conjugating_boundary_word_power':found}
(O/'free_words_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
