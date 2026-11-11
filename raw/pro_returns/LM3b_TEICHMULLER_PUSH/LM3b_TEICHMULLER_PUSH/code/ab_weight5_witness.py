#!/usr/bin/env python3
"""An explicit integral non-S3-invariant tripod derivation in degree five."""
from ab_lie import *

def transposition(D):
 def sub(p):return {tuple(1-i for i in w):v for w,v in p.items()}
 return (sub(D[1]),sub(D[0]))

def fmt(w):
 if len(w)==1:return 'xy'[w[0]]
 for j in range(1,len(w)):
  if is_lyndon(w[j:]):return '['+fmt(w[:j])+','+fmt(w[j:])+']'

def conjugator(p,i,n):
 bas=[expand(w) for w in lyndon(2,n)]
 cols=[coords(bracket(a,gen(i)),2,n+1) for a in bas]
 M=sp.zeros(len(lyndon(2,n+1)),len(bas))
 for j,c in enumerate(cols):
  for k,v in c.items():M[k,j]=v
 b=sp.zeros(M.rows,1)
 for k,v in coords(p,2,n+1).items():b[k]=v
 sol=M.gauss_jordan_solve(b)[0]
 return [{'coefficient':str(c),'bracket':fmt(w)} for c,w in zip(sol,lyndon(2,n)) if c]

for D in special(2,5):
 T=transposition(D)
 if D!=T:
  den=sp.ilcm(*[sp.denom(v) for d in D for v in d.values()])
  D=tuple({w:int(v*den) for w,v in d.items()} for d in D)
  assert not add(*D)
  assert D!=transposition(D)
  out={'a_x':conjugator(D[0],0,5),'a_y':conjugator(D[1],1,5),
       'convention':'D(x)=[a_x,x], D(y)=[a_y,y]',
       'sum_zero':True,'transposition_invariant':False}
  with open(Path(__file__).with_name('ab_weight5_witness.json'),'w') as f:json.dump(out,f,indent=2)
  print(json.dumps(out,indent=2));break
else:raise AssertionError('No witness')
