"""Exact independent group certificate for a nonabelian norm obstruction.
Reads only generator matrices, regenerates the group, its conjugacy
classes, and normal closures by finite congruence closure.
"""
from pathlib import Path
from collections import deque,Counter
import json,time
R=Path(__file__).resolve().parent;t=time.monotonic()
source=json.loads((R/'criterion_nonabelian_norm_group.json').read_text())
p=source['p'];d=source['dimension'];gens=[tuple(g) for g in source['generators']]
I=tuple(int(i==j) for i in range(d) for j in range(d))
def mm(A,B):
 cols=[B[j::d] for j in range(d)]
 return tuple(sum(a*b for a,b in zip(A[i*d:(i+1)*d],col))%p for i in range(d) for col in cols)
assert mm(mm(gens[0],gens[0]),gens[0])==I
assert mm(mm(gens[1],gens[1]),gens[1])==I
assert mm(gens[2],gens[2])==I
assert mm(gens[0],gens[1])!=mm(gens[1],gens[0])
index={I:0};G=[I];right=[[] for g in gens]
for A in G:
 for j,g in enumerate(gens):
  B=mm(A,g)
  if B not in index:index[B]=len(G);G.append(B)
  right[j].append(index[B])
assert len(G)==25920 and set(G)=={tuple(A) for A in source['elements']}
left=[[index[mm(g,A)] for A in G] for g in gens]
right_inverse=[]
for r in right:
 inv=[0]*len(G)
 for a,b in enumerate(r):inv[b]=a
 assert sorted(r)==list(range(len(G)))
 right_inverse.append(inv)
conjugation=[[l[ri[a]] for a in range(len(G))] for l,ri in zip(left,right_inverse)]
unseen=set(range(len(G)));classes=[]
while unseen:
 a=min(unseen);orbit={a};queue=[a]
 for x in queue:
  for c in conjugation:
   y=c[x]
   if y not in orbit:orbit.add(y);queue.append(y)
 unseen.difference_update(orbit);classes.append(sorted(orbit))
assert sum(map(len,classes))==len(G)

# The least equivalence relation identifying 1 with a and stable under
# both left and right generator multiplication is the quotient by the
# normal closure of a. Every successful merge adds at most six pairs.
def normal_closure_size(a):
 parent=list(range(len(G)));sizes=[1]*len(G)
 def find(x):
  while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
  return x
 queue=deque([(0,a)])
 while queue:
  x,y=queue.popleft();rx,ry=find(x),find(y)
  if rx==ry:continue
  if sizes[rx]<sizes[ry]:rx,ry=ry,rx
  parent[ry]=rx;sizes[rx]+=sizes[ry]
  for e in left+right:queue.append((e[x],e[y]))
 return sizes[find(0)]
class_records=[]
for C in classes:
 a=C[0];n=normal_closure_size(a)
 assert n==(1 if a==0 else len(G))
 class_records.append({'representative_index':a,'size':len(C),'normal_closure_order':n})

def rank(A):
 A=[list(r) for r in A];rank=0
 for j in range(d):
  h=next((h for h in range(rank,len(A)) if A[h][j]),None)
  if h is None:continue
  A[rank],A[h]=A[h],A[rank];inv=pow(A[rank][j],-1,p)
  A[rank]=[a*inv%p for a in A[rank]]
  for i in range(len(A)):
   if i!=rank:
    c=A[i][j];A[i]=[(a-c*b)%p for a,b in zip(A[i],A[rank])]
  rank+=1
 return rank
fixed_equations=[[((g[i*d+j]-(i==j))%p) for j in range(d)] for g in gens for i in range(d)]
fixed_rank=rank(fixed_equations);assert fixed_rank==d
assert len(G)%p!=0 and p**d<len(G)
assert all(sum(A[i] for A in G)%p==0 for i in range(d*d))
result={'verified':True,'scope':'Finite group and module certificate; no claimed curve realization',
 'characteristic':p,'dimension':d,'group_order':len(G),'group_order_factorization':{'2':6,'3':4,'5':1},
 'generators':[ [list(g[i*d:(i+1)*d]) for i in range(d)] for g in gens],
 'simple':True,'nonabelian':True,'conjugacy_class_count':len(classes),'class_records':class_records,
 'fixed_space_dimension':d-fixed_rank,'module_order':p**d,'all_level_free_vector_count':0,
 'normal_subgroups':['identity','whole group'],'whole_relative_module_dimension':d,
 'seconds':time.monotonic()-t}
(R/'criterion_nonabelian_norm_verify.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('verified','group_order','module_order','simple','conjugacy_class_count','fixed_space_dimension','all_level_free_vector_count','seconds')},indent=2))
print('conjugacy class sizes',sorted(map(len,classes)))
