#!/usr/bin/env python3
"""Compare ordinary and reflection generating passports for S6/A6."""
from itertools import permutations
from collections import Counter
S=list(permutations(range(6)));idx={g:i for i,g in enumerate(S)};one=idx[tuple(range(6))]
def par(a):return sum(a[i]>a[j] for i in range(6) for j in range(i+1,6))%2
def typ(a):
 seen=set();ans=[]
 for i in range(6):
  if i not in seen:
   j=i;k=0
   while j not in seen:seen.add(j);k+=1;j=a[j]
   ans.append(k)
 return tuple(sorted(ans))
T=[typ(g) for g in S];P=[par(g) for g in S]
M=[[idx[tuple(a[b[i]] for i in range(6))] for b in S] for a in S]
Inv=[idx[tuple(a.index(i) for i in range(6))] for a in S]
A=[i for i in range(720) if P[i]==0];I=[i for i in range(720) if P[i] and M[i][i]==one]
def size(gens):
 gs=list(gens)+[Inv[g] for g in gens];seen={one};queue=[one]
 for a in queue:
  for g in gs:
   b=M[a][g]
   if b not in seen:seen.add(b);queue.append(b)
 return len(seen)
allowed={T[M[u][v]] for u in I for v in I}
allowed.discard((1,1,1,1,1,1))
ordinary=Counter();examples={}
for ct in sorted(allowed):
 x=next(i for i in A if T[i]==ct);factor=sum(T[i]==ct for i in A)
 for y in A:
  z=Inv[M[x][y]];key=(T[x],T[y],T[z])
  if T[y] not in allowed or T[z] not in allowed:continue
  if size((x,y))==360:ordinary[key]+=factor;examples.setdefault(key,(S[x],S[y],S[z]))
real=Counter()
for it in sorted({T[t] for t in I}):
 t=next(i for i in I if T[i]==it);factor=sum(T[i]==it for i in I)
 for u in I:
  for v in I:
   x=M[t][u];y=M[u][v];z=M[v][t];key=(T[x],T[y],T[z])
   if key in ordinary and size((x,y))==360:real[key]+=factor
print('ordinary passport counts:',dict(sorted(ordinary.items())))
print('proper real passport counts:',dict(sorted(real.items())))
missing=[k for k in ordinary if real[k]==0]
print('ordinary but not proper real:',sorted(missing))
for k in sorted(missing):print('missing example',k,examples[k])
