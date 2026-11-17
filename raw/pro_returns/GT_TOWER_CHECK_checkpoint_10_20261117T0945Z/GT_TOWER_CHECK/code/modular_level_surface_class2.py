#!/usr/bin/env python3
"""Test the actual Γ(12) action on the class-two mod3 quotient of K4.

K4=ker(F(a,b)->(Z/4)^2). The characteristic finite source is
F(a,b)/(gamma3(K4) K4^3), of order16*3^153.
No identification with the modular rank97 layer is assumed.
"""
import numpy as np,json
from pathlib import Path
from collections import deque
m=4;n=17
def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(int(x))
 return tuple(out)
def inverse(w):return tuple(-x for x in reversed(w))
def sub(w,images):return red(x for a in w for x in (images[a-1] if a>0 else inverse(images[-a-1])))
labels=[(i,j) for j in range(m) for i in range(m)];index={x:i for i,x in enumerate(labels)}
def step(q,k,s=1):
 a=list(q);a[k]=(a[k]+s)%m;return tuple(a)
def section(q):return (2,)*q[1]+(1,)*q[0]
tree={(index[(i,j)],0) for j in range(m) for i in range(m-1)}|{(index[(0,j)],1) for j in range(m-1)}
chords=[(q,k) for q in range(m*m) for k in range(2) if (q,k) not in tree]
assert len(chords)==n;chordindex={x:i+1 for i,x in enumerate(chords)}
def rewrite(w):
 q=(0,0);out=[]
 for x in w:
  k=abs(x)-1
  if x>0:
   edge=(index[q],k);q=step(q,k)
   if edge in chordindex:out.append(chordindex[edge])
  else:
   q=step(q,k,-1);edge=(index[q],k)
   if edge in chordindex:out.append(-chordindex[edge])
 assert q==(0,0)
 return red(out)
basis=[section(labels[q])+(k+1,)+inverse(section(step(labels[q],k))) for q,k in chords]
for i,w in enumerate(basis):assert rewrite(w)==(i+1,)
def restrict(g):return tuple(rewrite(sub(w,g)) for w in basis)
normalizer_words=[restrict(((1,),(2,1))),restrict(((1,-2),(2,)))]
deck_words=[tuple(rewrite((g,)+w+(-g,)) for w in basis) for g in (1,2)]
pairs=[(i,j) for i in range(n) for j in range(i+1,n)];nc=len(pairs);dim=n*nc
def rref(A):
 A=np.array(A,dtype=np.int16).copy()%3;r=0;p=[]
 for c in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,c])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*(1 if A[r,c]==1 else 2)%3
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r]
  A[ns]=(A[ns]-A[ns,c,None]*A[r])%3;p.append(c);r+=1
  if r==len(A):break
 return A[:r],p
def minv(M):
 A,p=rref(np.hstack((M,np.eye(n,dtype=np.int16))))
 assert p[:n]==list(range(n));return A[:,n:]
def wedge(v,w):return np.array([(v[i]*w[j]-v[j]*w[i])%3 for i,j in pairs],dtype=np.int16)
def wedgeM(M):
 a=np.array([i for i,j in pairs]);b=np.array([j for i,j in pairs])
 return (M[a[:,None],a[None,:]]*M[b[:,None],b[None,:]]-M[a[:,None],b[None,:]]*M[b[:,None],a[None,:]])%3
inner=[]
for i in range(n):
 inner.append(np.stack([wedge(np.eye(n,dtype=np.int16)[i],np.eye(n,dtype=np.int16)[j]) for j in range(n)],axis=1).reshape(-1))
inner,ipiv=rref(inner);free=[i for i in range(dim) if i not in ipiv];odim=len(free)
assert odim==2295
def project(C):
 C=np.asarray(C).reshape(-1,dim)%3;out=(C[:,free]-C[:,ipiv]@inner[:,free])%3
 return out[0] if len(out)==1 else out
def lift(C):
 out=np.zeros(dim,dtype=np.int16);out[free]=C;return out.reshape(nc,n)
def wordlie(w):
 v=np.zeros(n,dtype=np.int16);z=np.zeros(nc,dtype=np.int16)
 for a in w:
  u=np.zeros(n,dtype=np.int16);u[abs(a)-1]=1 if a>0 else 2
  z=(z+2*wedge(v,u))%3;v=(v+u)%3
 return v,z
def aut(words):
 vz=[wordlie(w) for w in words];M=np.stack([v for v,z in vz],axis=1);D=np.stack([z for v,z in vz],axis=1)
 return project(D@minv(M)%3),M
gens=[aut(w) for w in normalizer_words];deck=[aut(w) for w in deck_words]
actcache={}
def act(M,C):
 key=tuple(map(int,M.reshape(-1)))
 if key not in actcache:actcache[key]=(wedgeM(M),minv(M))
 W,Mi=actcache[key];return project(W@lift(C)@Mi%3)
def mul(g,h):return ((g[0]+act(g[1],h[0]))%3,g[1]@h[1]%3)
def power(g,k):
 out=(np.zeros(odim,dtype=np.int16),np.eye(n,dtype=np.int16))
 for _ in range(k):out=mul(out,g)
 return out
central=power(mul(mul(gens[0],gens[1]),gens[0]),4)
assert not np.any(central[0]) and np.array_equal(central[1],np.eye(n,dtype=np.int16))
print('PASS actual SL2(Z) outer action on the characteristic order16*3^153 surface quotient',flush=True)

linear=[np.eye(2,dtype=np.int16)];idx={tuple(linear[0].reshape(-1)):0};paths=[()]
reps=[(np.zeros(odim,dtype=np.int16),np.eye(n,dtype=np.int16))]
UG=np.array([[1,1],[0,1]],dtype=np.int16);LG=np.array([[1,0],[-1,1]],dtype=np.int16)
for qi,M in enumerate(linear):
 for j,L in enumerate((UG,LG)):
  N=M@L%12;key=tuple(map(int,N.reshape(-1)))
  if key not in idx:
   idx[key]=len(linear);linear.append(N);paths.append(paths[qi]+(j+1,));reps.append(mul(reps[qi],gens[j]))
assert len(linear)==1152
print('PASS all1152 matrices in SL2(Z/12), with actual surface representatives',flush=True)
rels=[];bad=0
for qi,M in enumerate(linear):
 for j,L in enumerate((UG,LG)):
  ri=idx[tuple(map(int,(M@L%12).reshape(-1)))];h=mul(reps[qi],gens[j])
  if not np.array_equal(h[1],reps[ri][1]):bad+=1
  rels.append((h[0]-reps[ri][0])%3)
print('Γ(12) Schreier words with nontrivial K4 homology:',bad,flush=True)
assert bad==0
rows=np.array(rels);W,piv=rref(rows)
print('Actual Γ(12) outer IA image rank:',len(W),'of modular source rank97',flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),schreier_rows=rows,image_basis=W,image_pivots=np.array(piv),
 inner=inner,inner_pivots=np.array(ipiv),outer_free=np.array(free),
 modular_matrices=np.array(linear),representative_C=np.array([g[0] for g in reps]),
 representative_M=np.array([g[1] for g in reps]),
 deck_C=np.array([g[0] for g in deck]),deck_M=np.array([g[1] for g in deck]))
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Executed Γ12 comparison, with actual source and surface quotient',
 'source_surface_group':'F(a,b)','cover':'kernel of abelianization modulo4','cover_rank':17,
 'characteristic_quotient_order':'16*3^153','modular_base_order':1152,
 'modular_kernel_free_rank':97,'modular_kernel_IA_rank':len(W),
 'nontrivial_homology_schreier_words':bad,'schreier_basis_F2':basis,
 'normalizer_free_words':normalizer_words,'deck_free_words':deck_words,
 'modular_schreier_paths':paths},indent=2)+'\n')
