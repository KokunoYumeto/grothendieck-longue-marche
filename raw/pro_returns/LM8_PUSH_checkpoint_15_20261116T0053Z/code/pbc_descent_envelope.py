#!/usr/bin/env python3
"""Orders of the explicitly marked six-evaluation finite envelopes."""
from itertools import permutations
from pathlib import Path
import json,time
I=(1,0,0,1)
def mm(a,b,m):return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%m for i in range(2) for j in range(2))
def inv(a,m):return (a[3],-a[1]%m,-a[2]%m,a[0])
rows=[]
for mod in (3,4):
 mats=[(a,b,c,d) for a in range(mod) for b in range(mod) for c in range(mod) for d in range(mod) if (a*d-b*c)%mod==1]
 index={a:i for i,a in enumerate(mats)};mul=[[index[mm(a,b,mod)] for b in mats] for a in mats]
 U=(1,1,0,1);S=(0,1,mod-1,0);R=inv(mm(U,S,mod),mod)
 ps=list(permutations((U,S,R),2));X=bytes(index[a] for a,b in ps);Y=bytes(index[b] for a,b in ps);ident=bytes([index[I]]*6)
 seen={ident};todo=[ident];start=time.time()
 for v in todo:
  for g in (X,Y):
   w=bytes(mul[a][b] for a,b in zip(v,g))
   if w not in seen:seen.add(w);todo.append(w)
  if len(todo)>3000000:raise RuntimeError('declared enumeration cap exceeded')
 row=dict(modulus=mod,ambient_group_order=len(mats),six_evaluation_order=len(todo),seconds=round(time.time()-start,3),X=list(X),Y=list(Y),pairs=ps)
 rows.append(row);print(json.dumps(row),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
