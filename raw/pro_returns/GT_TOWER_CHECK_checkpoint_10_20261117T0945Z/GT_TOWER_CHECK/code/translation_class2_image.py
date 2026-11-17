#!/usr/bin/env python3
"""Actual genus-one nine-point mapping-class image at class2/exponent3.

The source maps are literal free words. The finite outer IA space is
Hom(V, wedge²V)/ad(V), dimension440. The actual mapping-class kernel
inside this space is computed from a complete presentation of its
homological quotient, not replaced by the ambient IA space.
"""
import translation_cover_basis as F
import numpy as np,json,itertools
from pathlib import Path
from collections import deque
n=10;pairs=[(i,j) for i in range(n) for j in range(i+1,n)];nc=len(pairs);dim=n*nc
identity_words=tuple((i,) for i in range(1,n+1))

def rref(A):
 A=np.array(A,dtype=np.int16).copy()%3;r=0;piv=[]
 if A.ndim==1:A=A[None,:]
 for c in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,c])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*(1 if A[r,c]==1 else 2)%3
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,c,None]*A[r])%3
  piv.append(c);r+=1
  if r==len(A):break
 return A[:r],piv

def minv(M):
 rr,piv=rref(np.hstack((M,np.eye(len(M),dtype=np.int16))))
 assert piv[:len(M)]==list(range(len(M)))
 return rr[:,len(M):]
def wedge(v,w):return np.array([(v[i]*w[j]-v[j]*w[i])%3 for i,j in pairs],dtype=np.int16)
def wedgeM(M):return np.array([[ (M[i,a]*M[j,b]-M[i,b]*M[j,a])%3 for a,b in pairs] for i,j in pairs],dtype=np.int16)
def word_lie(w):
 v=np.zeros(n,dtype=np.int16);z=np.zeros(nc,dtype=np.int16)
 for j in w:
  u=np.zeros(n,dtype=np.int16);u[abs(j)-1]=1 if j>0 else 2
  z=(z+2*wedge(v,u))%3;v=(v+u)%3
 return v,z
inner=[]
for j in range(n):
 v=np.eye(n,dtype=np.int16)[:,j]
 inner.append(np.stack([wedge(v,np.eye(n,dtype=np.int16)[:,i]) for i in range(n)],axis=1).reshape(-1))
inner,ipiv=rref(np.array(inner));assert len(inner)==10
ifree=[i for i in range(dim) if i not in ipiv];odim=len(ifree);assert odim==440

def outer_project(C):
 A=np.array(C,dtype=np.int16).reshape(-1,dim)%3
 ans=(A[:,ifree]-A[:,ipiv]@inner[:,ifree])%3
 return ans[0] if np.asarray(C).ndim==1 else ans

def outer_lift(C):
 C=np.array(C,dtype=np.int16);one=C.ndim==1
 if one:C=C[None,:]
 out=np.zeros((len(C),dim),dtype=np.int16);out[:,ifree]=C
 return out[0] if one else out

linear_cache={}
def act(M,C):
 key=tuple(map(int,M.reshape(-1)))
 if key not in linear_cache:linear_cache[key]=(wedgeM(M),minv(M))
 W,Mi=linear_cache[key];one=np.asarray(C).ndim==1
 A=outer_lift(C).reshape(-1,nc,n)
 out=np.einsum('ij,kjl,lm->kim',W,A,Mi,optimize=True)%3
 result=outer_project(out.reshape(len(A),dim))
 return result[0] if one else result

def aut(words):
 values=[word_lie(w) for w in words]
 M=np.stack([v for v,z in values],axis=1);D=np.stack([z for v,z in values],axis=1)
 C=D@minv(M)%3
 return (outer_project(C.reshape(-1)),M)
Id=(np.zeros(odim,dtype=np.int16),np.eye(n,dtype=np.int16))
def mul(g,h):return ((g[0]+act(g[1],h[0]))%3,g[1]@h[1]%3)
def inv(g):
 Mi=minv(g[1]);return (-act(Mi,g[0])%3,Mi)
def power(g,k):
 if k<0:return power(inv(g),-k)
 out=Id
 for _ in range(k):out=mul(out,g)
 return out
def eq(g,h):return np.array_equal(g[0],h[0]) and np.array_equal(g[1],h[1])
def aword(w,gens):
 out=Id
 for j in w:out=mul(out,gens[j-1] if j>0 else inv(gens[-j-1]))
 return out

# Literal Hurwitz B4 action on D4 and its even free kernel.
def red2(w):
 out=[]
 for j in w:
  if out and out[-1]==j:out.pop()
  else:out.append(j)
 return tuple(out)
def sub2(w,images):
 out=()
 for j in w:out=red2(out+images[j-1])
 return out
def compose2(a,b):return tuple(sub2(w,a) for w in b)
id4=tuple((i,) for i in range(1,5))
hurwitz=[];hurwitz_inv=[]
for i in range(1,4):
 a=list(id4);a[i-1]=(i,i+1,i);a[i]=(i,);hurwitz.append(tuple(a))
 a=list(id4);a[i-1]=(i+1,);a[i]=(i+1,i,i+1);hurwitz_inv.append(tuple(a))
for a,b in zip(hurwitz,hurwitz_inv):assert compose2(a,b)==id4 and compose2(b,a)==id4
for i in range(2):assert compose2(hurwitz[i],compose2(hurwitz[i+1],hurwitz[i]))==compose2(hurwitz[i+1],compose2(hurwitz[i],hurwitz[i+1]))
def braid4(w):
 out=id4
 for j in w:out=compose2(out,hurwitz[j-1] if j>0 else hurwitz_inv[-j-1])
 return out
old4=((2,1),(3,1),(4,1))
def free_to_D4(w):
 out=()
 for j in w:out=red2(out+(old4[j-1] if j>0 else tuple(reversed(old4[-j-1]))))
 return out
def even_rewrite(w):
 parity=0;out=[]
 for j in w:
  if j>1:out.append((j-1)*(1 if parity==0 else -1))
  parity^=1
 assert parity==0
 return F.red(out)
std3_old=((2,),(-1,),(-1,2,1,-2,3,-2,1))
old3_std=((-2,),(1,),(1,2,-1,-2,3,2,1))
for i in range(3):
 assert F.sub(std3_old[i],old3_std)==(i+1,)
 assert F.sub(old3_std[i],std3_old)==(i+1,)
std3_D4=tuple(free_to_D4(w) for w in std3_old)
xi_words=((3,-1),(1,2,1,-3,-2,-1));pointpush_words=[]
for w in xi_words:
 ba=braid4(w)
 pp=tuple(F.sub(even_rewrite(sub2(v,ba)),old3_std) for v in std3_D4)
 boundary=(1,2,-1,-2,3)
 assert F.sub(boundary,pp)==boundary
 cc=list(pp[2])
 while len(cc)>1 and cc[0]==-cc[-1]:cc=cc[1:-1]
 assert tuple(cc)==(3,)
 forget=tuple(F.sub(v,((1,),(2,),())) for v in pp)
 print('Literal pointpush words:',pp,'forgetting words',forget,flush=True)
 pointpush_words.append(pp+identity_words[3:])

handle_words=[((1,),(2,1))+identity_words[2:],((1,-2),(2,))+identity_words[2:]]
handles=[aut(w) for w in handle_words]
disk=[]
for i in range(3,10):
 w=list(identity_words);w[i-1]=(i,i+1,-i);w[i]=(i,);disk.append(aut(tuple(w)))
rawpush=[aut(w) for w in pointpush_words]
for g in rawpush:
 assert np.array_equal(g[1][:2,:2],np.eye(2,dtype=np.int16))
 assert np.array_equal(g[1][2:,2:],np.eye(8,dtype=np.int16))
 assert not np.any(g[1][:2,2:]) and not np.any(g[1][3:,:2])
B=np.stack([g[1][2,:2] for g in rawpush]);assert len(rref(B)[0])==2
Bi=minv(B);push=[]
for i in range(8):
 # sigma_i ... sigma_1 sends the first named puncture to number i+1.
 path=tuple(range(i,0,-1));conj=aword(path,disk)
 assert np.argmax(conj[1][:,2])==i+2
 for j in range(2):
  exps=Bi[j];base=mul(power(rawpush[0],int(exps[0])),power(rawpush[1],int(exps[1])))
  g=mul(conj,mul(base,inv(conj)));target=np.eye(n,dtype=np.int16);target[i+2,j]=1
  assert np.array_equal(g[1],target);push.append(g)
# Exact pure disk pair twists.
pairtwists=[]
for i in range(1,8):
 for j in range(i+1,9):
  t=tuple(range(j-1,i,-1));g=mul(aword(t,disk),mul(power(disk[i-1],2),inv(aword(t,disk))))
  assert np.array_equal(g[1],Id[1]);pairtwists.append(g)
assert len(push)==16 and len(pairtwists)==28

H=[aut(w) for w in F.deck];normalizers=[aut(w) for w in F.normalizer]
assert all(eq(power(h,3),Id) for h in H)
assert eq(mul(H[0],H[1]),mul(H[1],H[0]))
# Check the nine actual labelled peripheral vectors, including the last.
periph=F.periph%3
for j,h in enumerate(H):
 for k,q in enumerate(F.Q):
  dest=F.qi[F.step(q,j)]
  assert np.array_equal(h[1]@periph[k]%3,periph[dest])
print('PASS exact class-two translation action and all nine peripheral labels',flush=True)
print('PASS actual pure generators: two handles, sixteen pointpushes, twenty-eight pair twists',flush=True)

# Complete finite presentation of the homological quotient.
linear2=[np.eye(2,dtype=np.int16)];li2={tuple(linear2[0].reshape(-1)):0};paths={0:()}
for M in linear2:
 q=li2[tuple(M.reshape(-1))]
 for j,h in enumerate(handles,1):
  N=M@h[1][:2,:2]%3;key=tuple(N.reshape(-1))
  if key not in li2:li2[key]=len(linear2);linear2.append(N);paths[li2[key]]=paths[q]+(j,)
assert len(linear2)==24
rels=[]
for q,M in enumerate(linear2):
 for j,h in enumerate(handles,1):
  r=li2[tuple((M@h[1][:2,:2]%3).reshape(-1))]
  g=aword(paths[q]+(j,)+F.inv(paths[r]),handles);assert np.array_equal(g[1],Id[1]);rels.append(g[0])
for g in push:rels.append(power(g,3)[0]);assert np.array_equal(power(g,3)[1],Id[1])
for i,g in enumerate(push):
 for h in push[:i]:
  z=mul(g,mul(h,mul(inv(g),inv(h))));assert np.array_equal(z[1],Id[1]);rels.append(z[0])

def push_word(B):
 out=Id
 for j,c in enumerate(np.array(B).reshape(-1)):
  if c:out=mul(out,power(push[j],int(c)))
 return out
for h in handles:
 for g in push:
  z=mul(h,mul(g,inv(h)));B=z[1][2:,:2]
  z=mul(z,inv(push_word(B)));assert np.array_equal(z[1],Id[1]);rels.append(z[0])
rels += [g[0] for g in pairtwists]
W,_=rref(np.array(rels));print('Initial actual outer IA span:',len(W),'from',len(rels),'complete quotient relators',flush=True)
linear_generators=[g[1] for g in handles+push]
iteration=0
while True:
 old=len(W);W,_=rref(np.vstack([W]+[act(M,W) for M in linear_generators]));iteration+=1
 print('Actual IA normal closure iteration',iteration,'dimension',len(W),flush=True)
 if len(W)==old:break
for h in H:assert len(rref(np.vstack((W,act(h[1],W))))[0])==len(W)
print('PASS actual Γ1,9 pure image: kernel dimension',len(W),'over homological image 24*3^16',flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),W=W,inner=inner,inner_pivots=np.array(ipiv),
 inner_free=np.array(ifree),H_C=np.array([g[0] for g in H]),H_M=np.array([g[1] for g in H]),
 handle_C=np.array([g[0] for g in handles]),handle_M=np.array([g[1] for g in handles]),
 push_C=np.array([g[0] for g in push]),push_M=np.array([g[1] for g in push]),
 normalizer_C=np.array([g[0] for g in normalizers]),normalizer_M=np.array([g[1] for g in normalizers]),
 linear2=np.array(linear2))
Path(__file__).with_suffix('.json').write_text(json.dumps({'source':'actual Γ1,9 pure mapping-class image in Out of F10 class2 exponent3',
 'outer_IA_dimension':odim,'actual_IA_kernel_dimension':len(W),'homological_image_order':'24*3^16',
 'actual_pure_image_order':f'24*3^{16+len(W)}','pointpush_free_words':pointpush_words,
 'initial_relator_count':len(rels),'normal_closure_iterations':iteration},indent=2)+'\n')
