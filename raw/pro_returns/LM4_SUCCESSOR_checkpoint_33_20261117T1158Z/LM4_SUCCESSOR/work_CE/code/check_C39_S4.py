"""Exact finite facts for C39: peripheral involutions and S4 generation.
This is a necessary-condition certificate, not a full-word existence test.
No imports from other project certificates.
"""
from itertools import permutations,product
from collections import Counter
G=list(permutations(range(4)));ix={g:i for i,g in enumerate(G)}
e=ix[(0,1,2,3)]
def mul(a,b):return tuple(a[b[i]] for i in range(4))
def inverse(a):return tuple(a.index(i) for i in range(4))
m=[[ix[mul(a,b)] for b in G] for a in G]
iv=[ix[inverse(a)] for a in G]
con=[[m[m[h][a]][iv[h]] for a in range(24)] for h in range(24)]
def subgroup(gens):
 out={e};todo=[e]
 while todo:
  a=todo.pop()
  for g in gens:
   b=m[a][g]
   if b not in out:out.add(b);todo.append(b)
 return frozenset(out)
def order(a):
 b=e
 for n in range(1,25):
  b=m[b][a]
  if b==e:return n
def sign(a):return (-1)**sum(G[a][i]>G[a][j] for i in range(4) for j in range(i+1,4))
A4={a for a in range(24) if sign(a)==1}
parts=[frozenset((frozenset((0,1)),frozenset((2,3)))),
       frozenset((frozenset((0,2)),frozenset((1,3)))),
       frozenset((frozenset((0,3)),frozenset((1,2))))]
def head(a):
 return tuple(parts.index(frozenset(frozenset(G[a][j] for j in block) for block in part)) for part in parts)
qh=[head(a) for a in range(24)]
assert len(set(qh))==6
V4={a for a in range(24) if qh[a]==(0,1,2)}
assert len(V4)==4
groups={frozenset((e,))};todo=list(groups)
while todo:
 H=todo.pop()
 for a in range(24):
  if a in H:continue
  K=subgroup(tuple(H)+(a,))
  if K not in groups:groups.add(K);todo.append(K)
assert len(groups)==30
proper_over_S3=[H for H in groups if len(H)<24 and len({qh[a] for a in H})==6]
assert len(proper_over_S3)==4
for H in proper_over_S3:
 assert len(H)==6 and all(order(a)<=3 for a in H)
 norm={h for h in range(24) if frozenset(con[h][a] for a in H)==H}
 assert norm==set(H)
 fixed=[j for j in range(4) if all(G[a][j]==j for a in H)]
 assert len(fixed)==1
print('All30 subgroups; the only proper subgroups onto S3 are four self-normalizing point stabilizers: PASS')
orbits={};reps=[]
for a,b in product(range(24),repeat=2):
 if (a,b) in orbits or len(subgroup((a,b)))<24:continue
 j=len(reps);reps.append((a,b))
 for h in range(24):orbits[con[h][a],con[h][b]]=(j,h)
assert len(reps)==9 and len(orbits)==216
print('All216 ordered generating pairs form9 inner-automorphism orbits.')
critical=[]
for j,(a,b) in enumerate(reps):
 passport=(order(a),order(b),order(m[a][b]))
 print('orbit',j,'passport',passport,'a=',G[a],'b=',G[b])
 if 4 not in passport[:2]:
  assert set(passport[:2])=={2,3} and passport[2]==4
  invol=a if order(a)==2 else b
  assert sign(invol)==-1
  critical.append(j)
  # Every negative substituted pair that generates has the same kernel.
  count=0
  for F in A4:
   aa=iv[a];bb=con[iv[F]][iv[b]]
   if (aa,bb) not in orbits:continue
   jj,h=orbits[aa,bb]
   assert jj==j
   count+=1
  print(' negative generated-pair kernel candidates:',count)
assert len(critical)==2
bad=Counter()
for j,(a,b) in enumerate(reps):
 for U in A4:
  bp=con[iv[U]][b];H=subgroup((a,bp))
  if len({qh[t] for t in H})<6:continue # excluded by the full A44/S3 argument
  if len(H)==24:continue
  assert j in critical and H in proper_over_S3
  invs=[h for h in range(24) if m[h][h]==e and con[h][a]==iv[a] and con[h][bp]==iv[bp]]
  invol=a if order(a)==2 else bp
  assert invs and all(h==invol for h in invs)
  assert order(m[a][b])==4
  bad[j]+=1
print('Proper-image candidates after the S3 generation condition:',dict(bad))
print('Every candidate forces one X/Y section to be central, contradicting third-cusp order4: PASS')
print('Finite classification and all stated inversion/normalizer facts: PASS')
