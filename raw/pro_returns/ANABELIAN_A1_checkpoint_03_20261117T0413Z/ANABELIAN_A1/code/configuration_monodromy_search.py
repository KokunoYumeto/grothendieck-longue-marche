"""Exact Schreier homology experiment for genus-two point pushes.
Not a certificate until the final assertions and explicit even-order witness succeed.
"""
import itertools, collections, json, random
import numpy as np

def red(w):
 o=[]
 for x in w:
  if o and o[-1]==-x:o.pop()
  else:o.append(x)
 return o
def inv(w):return [-x for x in w[::-1]]
def mul(*ws):return red(sum((list(w) for w in ws),[]))
def comm(a,b):return mul(a,b,inv(a),inv(b))
t=mul(comm([1],[-2]),comm([3],[-4]))
def apply(phi,w):return mul(*(phi[x] if x>0 else inv(phi[-x]) for x in w))
phis=[]
for own in range(1,5):
 u=mul(t,[-own],t,[own],inv(t));w=mul(inv(u),t)
 phi={j:[j] for j in range(1,5)}
 phi[own]=mul(t,[own],inv(t))
 if own%2:phi[own+1]=mul(t,[own+1],inv(t),u)
 else:phi[own-1]=mul([own-1],inv(t))
 if own<=2:
  phi[3]=mul(w,[3],inv(w));phi[4]=mul(w,[4],inv(w))
 assert apply(phi,t)==u
 phis.append(phi)
# Q=Heisenberg group over F_3, xy'=conventional cocycle.
Q=list(itertools.product(range(3),repeat=3));index={q:i for i,q in enumerate(Q)};one=(0,0,0)
def qm(a,b):return ((a[0]+b[0])%3,(a[1]+b[1])%3,(a[2]+b[2]+a[0]*b[1])%3)
def qi(a):return ((-a[0])%3,(-a[1])%3,(-a[2]+a[0]*a[1])%3)
gens={1:(1,0,0),2:(0,1,0),3:one,4:one}
for i in range(1,5):gens[-i]=qi(gens[i])
def qe(w):
 q=one
 for x in w:q=qm(q,gens[x])
 return q
# Schreier tree in Cayley graph, selected positive oriented edges.
reps={one:[]};tree=set();todo=collections.deque([one])
while todo:
 q=todo.popleft()
 for j in [1,2,3,4,-1,-2,-3,-4]:
  v=qm(q,gens[j])
  if v not in reps:
   reps[v]=reps[q]+[j];todo.append(v)
   tree.add((q,j) if j>0 else (v,-j))
assert len(reps)==27 and len(tree)==26
edges=[(q,j) for q in Q for j in range(1,5) if (q,j) not in tree];ei={v:i for i,v in enumerate(edges)};n=len(edges)
basis=[mul(reps[q],[j],inv(reps[qm(q,gens[j])])) for q,j in edges]
assert n==82 and all(qe(w)==one for w in basis)
def hom(w,prime=5):
 q=one;v=np.zeros(n,dtype=np.int64)
 for j in w:
  vq=qm(q,gens[j]);ed=(q,j) if j>0 else (vq,-j)
  if ed in ei:v[ei[ed]]+=1 if j>0 else -1
  q=vq
 assert q==one
 return v%prime
def mat(phi):return np.column_stack([hom(apply(phi,w)) for w in basis])
def rank(M,prime=5):
 a=M.copy()%prime;row=0
 for col in range(a.shape[1]):
  inds=np.nonzero(a[row:,col])[0]
  if not len(inds):continue
  k=row+inds[0];a[[row,k]]=a[[k,row]];a[row]=(a[row]*pow(int(a[row,col]),-1,prime))%prime
  inds=np.nonzero(a[:,col])[0];inds=inds[inds!=row]
  a[inds]=(a[inds]-a[inds,col,None]*a[row])%prime
  row+=1
  if row==a.shape[0]:break
 return row
mats=[]
for k in [0,1,2,3]:
 phi=phis[k]
 if k>=2:
  phi={j:apply(phis[k],apply(phis[k],phi[j])) for j in range(1,5)}
  print('cube word lengths',k,[len(w) for w in phi.values()],flush=True)
 imgs={j:qe(phi[j]) for j in range(1,5)}
 # Evaluation factors through Q: standard class-2, exponent-3 and c=d=1 relators.
 test=[ [1]*3,[2]*3,[3],[4],comm(comm([1],[2]),[1]),comm(comm([1],[2]),[2]) ]
 assert all(qe(apply(phi,w))==one for w in test)
 M=mat(phi);assert rank(M)==n;mats.append(M)
for j in [1,2,3,4]:
 phi={k:mul([j],[k],[-j]) for k in range(1,5)}
 mats.append(mat(phi))
print('rank',n,'matrices',len(mats),flush=True)
I=np.eye(n,dtype=np.int64);rng=random.Random(170112)
M=I.copy();word=[]
for step in range(1,1501):
 j=rng.randrange(len(mats));M=(mats[j]@M)%5;word.insert(0,j)
 d=n-rank(M+I)
 if d:
  print('FOUND eigenvalue -1 at step',step,'dimension',d,'word',word,flush=True)
  np.savez_compressed('ANABELIAN_A1/code/configuration_negative_matrices.npz',**{f'M{i}':m for i,m in enumerate(mats)},witness=M)
  with open('ANABELIAN_A1/code/configuration_negative_data.json','w') as f:json.dump({'prime':5,'quotient':'Heisenberg F3','dimension':n,'word':word,'phis':phis,'tree':[[list(q),j] for q,j in sorted(tree)],'edges':[[list(q),j] for q,j in edges]},f,indent=2)
  break
 if step%50==0:print('searched',step,flush=True)
else:print('NO WITNESS',flush=True)
