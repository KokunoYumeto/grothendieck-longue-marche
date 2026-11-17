from collections import deque,Counter
import json,time
from pathlib import Path
R=Path(__file__).resolve().parent;t=time.monotonic();p=7;d=5
I=tuple(int(i==j) for i in range(d) for j in range(d))
U=(1,4,1,4,4);perm=(0,1,3,4,2)
F=tuple(v for row in ((2,4,4,4,4),(2,5,4,5,5),(2,4,5,5,5),(2,5,5,5,4),(2,5,5,4,5)) for v in row)
def fu(A):return tuple(A[5*i+j]*U[j]%7 for i in range(5) for j in range(5))
def fp(A):return tuple(A[5*i+perm[j]] for i in range(5) for j in range(5))
def ff(A):
 return tuple(sum(A[5*i+k]*F[5*k+j] for k in range(5))%7 for i in range(5) for j in range(5))
assert ff(F)==I
seen={I:0};G=[I]
for A in G:
 for B in (fu(A),fp(A),ff(A)):
  if B not in seen:
   seen[B]=len(G);G.append(B)
 if len(G)>60000:raise ValueError('large group')
print('order',len(G),'seconds',time.monotonic()-t,flush=True)
(R/'criterion_nonabelian_norm_group.json').write_text(json.dumps({'p':7,'dimension':5,'generators':[fu(I),fp(I),F],'order':len(G),'elements':G},separators=(',',':')))
