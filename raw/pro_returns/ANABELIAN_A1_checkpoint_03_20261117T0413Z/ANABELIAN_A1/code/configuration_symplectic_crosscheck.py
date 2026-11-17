#!/usr/bin/env python3
"""Independent genus-three/r=2/ell=3 check of the transvection mechanism.
It computes monodromy on a 41-dimensional Schreier H1, extracts the
four-dimensional central-sheet-difference module, and enumerates Sp4(F3).
"""
from pathlib import Path
import itertools,collections,json
import numpy as np
OUT=Path(__file__).resolve().parent

def red(w):
 a=[]
 for x in w:
  if a and a[-1]==-x:a.pop()
  else:a.append(x)
 return a
def inv(w):return [-x for x in w[::-1]]
def mul(*ws):return red([x for w in ws for x in w])
def comm(a,b):return mul(a,b,inv(a),inv(b))
def apply(phi,w):return mul(*(phi[x] if x>0 else inv(phi[-x]) for x in w))
def comp(phi,psi):return {i:apply(phi,psi[i]) for i in range(1,7)}
t=mul(*(comm([i],[-i-1]) for i in (1,3,5)))
phis={}
for i in range(3,7):
 u=mul(t,[-i],t,[i],inv(t));w=mul(inv(u),t)
 phi={j:[j] for j in range(1,7)};phi[i]=mul(t,[i],inv(t))
 if i%2:phi[i+1]=mul(t,[i+1],inv(t),u)
 else:phi[i-1]=mul([i-1],inv(t))
 for j in range(i+2 if i%2 else i+1,7):phi[j]=mul(w,[j],inv(w))
 assert apply(phi,t)==u
 phis[i]=phi
Q=list(itertools.product(range(2),repeat=3));one=(0,0,0);z=(0,0,1)
def qm(a,b):return ((a[0]+b[0])%2,(a[1]+b[1])%2,(a[2]+b[2]+a[0]*b[1])%2)
def qi(a):return (a[0],a[1],(a[2]+a[0]*a[1])%2)
gens={i:one for i in range(1,7)};gens[1]=(1,0,0);gens[2]=(0,1,0)
for i in range(1,7):gens[-i]=qi(gens[i])
def qe(w):
 q=one
 for x in w:q=qm(q,gens[x])
 return q
reps={one:[]};tree=set();todo=collections.deque([one])
while todo:
 q=todo.popleft()
 for j in list(range(1,7))+list(range(-1,-7,-1)):
  q2=qm(q,gens[j])
  if q2 not in reps:
   reps[q2]=reps[q]+[j];todo.append(q2);tree.add((q,j) if j>0 else(q2,-j))
edges=[(q,j) for q in Q for j in range(1,7) if(q,j) not in tree];ei={e:i for i,e in enumerate(edges)}
basis=[mul(reps[q],[j],inv(reps[qm(q,gens[j])])) for q,j in edges];n=len(basis)
assert n==41
W=np.zeros((n,4),dtype=np.int64)
for j in range(3,7):W[ei[(one,j)],j-3]=1;W[ei[(z,j)],j-3]=-1
pick=[ei[(one,j)] for j in range(3,7)]
def hom(w):
 q=one;v=np.zeros(n,dtype=np.int64)
 for j in w:
  q2=qm(q,gens[j]);e=(q,j) if j>0 else(q2,-j)
  if e in ei:v[ei[e]]+=1 if j>0 else -1
  q=q2
 assert q==one
 return v
base=[phis[i] for i in range(3,7)]+[comp(phis[3],phis[5])]
names=['C^2','D^2','E^2','F^2','(CE)^2'];mats=[]
for name,phi in zip(names,base):
 phi=comp(phi,phi)
 assert all(qe(phi[j])==gens[j] for j in range(1,7))
 M=np.column_stack([hom(apply(phi,w)) for w in basis]);small=(M@W)[pick,:]
 assert np.array_equal(M@W,W@small),(name,'not invariant')
 mats.append(small%3);print(name,small.tolist(),flush=True)
J=np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]],dtype=np.int64)
assert all(np.array_equal(M.T@J@M%3,J%3) for M in mats)
def key(M):return bytes((M%3).reshape(-1).tolist())
I=np.eye(4,dtype=np.int64);seen={key(I):[]};todo=collections.deque([I]);ord5=None
while todo:
 M=todo.popleft();word=seen[key(M)]
 if ord5 is None and not np.array_equal(M,I):
  M2=M@M%3;M5=M2@M2@M%3
  if np.array_equal(M5,I):ord5=(M,word)
 for j,A in enumerate(mats):
  N=A@M%3;k=key(N)
  if k not in seen:seen[k]=[j]+word;todo.append(N)
print('Generated group order',len(seen),'expected Sp4(F3)',3**4*(3**2-1)*(3**4-1),flush=True)
assert len(seen)==51840 and ord5 is not None
M,word=ord5
print('Order-five element word:',[names[j] for j in word],flush=True)
print('Order-five matrix:',M.tolist(),flush=True)
(OUT/'configuration_symplectic_crosscheck.json').write_text(json.dumps({'genus':3,'r':2,'ell':3,'Schreier_rank':41,'generators':dict(zip(names,[M.tolist() for M in mats])),'group_order':len(seen),'order5_word':[names[j] for j in word],'order5_matrix':M.tolist()},indent=2)+'\n')
