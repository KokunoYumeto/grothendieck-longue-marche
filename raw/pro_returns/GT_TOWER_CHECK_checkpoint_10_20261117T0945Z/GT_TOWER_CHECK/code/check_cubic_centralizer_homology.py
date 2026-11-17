#!/usr/bin/env python3
"""Exact cubic-centralizer obstruction in a five-point homology quotient.

P=Gamma_0,5, Q=C2^5 x SL2(F3), N=ker(P->Q), R=P/(N' N^3).
The order-three braid d=sigma1^2 sigma2 sigma3 acts on R. We enumerate
which Q-centralizer residues lift to its centralizer in R, using the
full 114-dimensional H1(N,F3), not ambient permutation modules.
"""
import test_cm_cubic_refinement as R
T=R.T
import numpy as np
from functools import lru_cache
from pathlib import Path
import json

p=3
# Standalone exact braid combing, with all identities checked by the
# faithful Artin action before passing to any quotient.
def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return tuple(out)
def inverse(w):return tuple(-x for x in reversed(w))
def concat(*ws):return red(x for w in ws for x in w)
def subst(w,images):return concat(*(images[i-1] if i>0 else inverse(images[-i-1]) for i in w))
def gen_artin(i):
 j=abs(i);im=[(k,) for k in range(1,5)]
 if i>0:im[j-1]=(j,j+1,-j);im[j]=(j,)
 else:im[j-1]=(j+1,);im[j]=(-(j+1),j,j+1)
 return tuple(im)
@lru_cache(None)
def artin(w):
 im=tuple((j,) for j in range(1,5))
 for x in w:im=tuple(subst(v,gen_artin(x)) for v in im)
 return im
def A(i,j):return tuple(range(j-1,i,-1))+(i,i)+tuple(-k for k in range(i+1,j))
generators=[A(1,3),A(2,3),A(1,4),A(2,4),A(3,4)]
omega=(1,2,3)*4
def delete_strand(w,n):
 order=list(range(1,n+1));out=[]
 for k in w:
  i=abs(k)-1;pos=order.index(n)
  if pos not in (i,i+1):out.append((1 if k>0 else -1)*(abs(k)-(1 if pos<i else 0)))
  order[i],order[i+1]=order[i+1],order[i]
 assert order==list(range(1,n+1))
 return red(out)
def kernel_conjugator(w,n):
 image=list(artin(tuple(w))[n-1]);stem=[]
 while len(image)>1:
  assert image[0]==-image[-1]
  stem.append(image.pop(0));image.pop()
 assert image==[n]
 return red(x for x in stem if abs(x)!=n)
def comb(w):
 w=tuple(w);scalar=delete_strand(delete_strand(w,4),3)
 assert len(scalar)%2==0
 m=sum(scalar)//2
 w0=concat(w,*([inverse(omega) if m>=0 else omega]*abs(m)))
 b0=delete_strand(w0,4);u=concat(inverse(b0),w0)
 ker=kernel_conjugator(u,4);base2=delete_strand(b0,3);assert not base2
 ba=kernel_conjugator(b0,3)
 result=tuple(ba)+tuple((1 if x>0 else -1)*(abs(x)+2) for x in ker)
 assert artin(w0)==artin(subst(result,generators))
 return red(result)
d=(1,1,2,3)
assert artin(d*3)==artin(omega)
dgen=[comb(concat(d,g,inverse(d))) for g in generators]
for j,w in enumerate(dgen):
 w3=subst(subst(w,dgen),dgen)
 assert artin(subst(w3,generators))==artin(generators[j])
print('PASS cubic braid action and all five exact combed images:',dgen,flush=True)

Dpar=np.array([[sum(1 if j==k else -1 if j==-k else 0 for j in w)%2
               for w in dgen] for k in range(1,6)],dtype=np.int16)
def dbits(a):
 v=np.array([(a>>j)&1 for j in range(5)],dtype=np.int16)
 return sum(int(x)<<j for j,x in enumerate(Dpar@v%2))
D3=(0,1,2,2) # U^2 L U modulo three; verify directly below.
U=(1,1,0,1);Lo=(1,0,2,1)
D3=R.mul(R.mul(R.mul(U,U),Lo),U)
def dQ(q):return R.idx[R.mul(R.mul(D3,R.Q[q]),R.inv(D3))]
def db(q):return dbits(q[0]),dQ(q[1])
for j,w in enumerate(dgen):
 end,_=R.chain((0,0),w,0)
 assert end==db((1<<j,R.ig[j]))
assert all(db(db(db(q)))==q for q in ((a,q) for a in range(32) for q in range(24)))

def kernel_basis(A):
 A=A.copy()%3;r=0;piv=[]
 for j in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,j])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*pow(int(A[r,j]),-1,3)%3
  ns=np.flatnonzero(A[:,j]);ns=ns[ns!=r]
  A[ns]=(A[ns]-A[ns,j,None]*A[r])%3;piv.append(j);r+=1
  if r==len(A):break
 free=[j for j in range(A.shape[1]) if j not in piv]
 N=np.zeros((len(free),A.shape[1]),dtype=np.int16)
 N[:,free]=np.eye(len(free),dtype=np.int16);N[:,piv]=-A[:r,free].T;N%=3
 return N

def image_basis_with_lifts(Z,P):
 A=Z@P%3;Z=Z.copy();r=0;piv=[]
 for j in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,j])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];Z[[r,k]]=Z[[k,r]]
  scale=pow(int(A[r,j]),-1,3);A[r]=A[r]*scale%3;Z[r]=Z[r]*scale%3
  ns=np.flatnonzero(A[:,j]);ns=ns[ns!=r];sc=A[ns,j,None].copy()
  A[ns]=(A[ns]-sc*A[r])%3;Z[ns]=(Z[ns]-sc*Z[r])%3
  piv.append(j);r+=1
  if r==len(A):break
 return Z[:r],P[:,piv]

cycles={};proj={};offsets={};total=0
for ch in range(32):
 B=np.zeros((120,24),dtype=np.int16)
 for q in range(24):
  for j,g in enumerate(R.ig):
   B[5*q+j,q]-=1;B[5*q+j,int(R.tab[q,g])]+=(-1 if ch&(1<<j) else 1)
 Z=kernel_basis(B.T)
 Z,P=image_basis_with_lifts(Z,R.projections[ch])
 assert len(Z)==R.dimensions[ch]
 assert np.all(Z@B%3==0) and np.array_equal(Z@P%3,np.eye(len(Z),dtype=np.int16))
 cycles[ch]=Z;proj[ch]=P;offsets[ch]=total;total+=len(Z)
assert total==114

def dcharacter(ch):
 # ch' dot d(a)=ch dot a, so ch'=ch composed with d^-1.
 return sum(((ch&dbits(dbits(1<<j))).bit_count()%2)<<j for j in range(5))
M=np.zeros((total,total),dtype=np.int16)
for ch in range(32):
 ch2=dcharacter(ch);rows=[]
 for q in range(24):
  for w in dgen:
   _,v=R.chain((0,dQ(q)),w,ch2);rows.append(v)
 Dedge=np.array(rows,dtype=np.int16)
 block=cycles[ch]@Dedge@proj[ch2]%3
 a,b=offsets[ch],offsets[ch2]
 M[a:a+len(cycles[ch]),b:b+len(cycles[ch2])]=block
assert np.array_equal(M@M@M%3,np.eye(total,dtype=np.int16))
rank,_=T.row_space_projection(M-np.eye(total,dtype=np.int16),3)
print('PASS full H1 cubic action: dimension',total,'rank(D-I)',len(rank),flush=True)

# Exact discrete lifts to every base element; no extension cocycle is guessed.
bpaths={(0,0):()};order=[(0,0)]
for q in order:
 for j,g in enumerate(R.ig):
  h=(q[0]^(1<<j),int(R.tab[q[1],g]))
  if h not in bpaths:bpaths[h]=bpaths[q]+(j+1,);order.append(h)
assert len(order)==768

def h1(w):
 vs=[]
 for ch in range(32):
  q,v=R.chain((0,0),w,ch);assert q==(0,0)
  vs.append(v@proj[ch]%3)
 return np.concatenate(vs)
# Check the Fourier action on many actual loops, including all base edges.
for i,q in enumerate(order):
 if i%13:continue
 for j,g in enumerate(R.ig):
  h=(q[0]^(1<<j),int(R.tab[q[1],g]))
  w=concat(bpaths[q],(j+1,),inverse(bpaths[h]))
  assert np.array_equal(h1(w)@M%3,h1(subst(w,dgen)))
print('PASS cubic homology action on sampled actual Schreier generators',flush=True)

_,coker=T.row_space_projection(M-np.eye(total,dtype=np.int16),3)
records=[]
for q in order:
 if db(q)!=q:continue
 w=bpaths[q];difference=concat(subst(w,dgen),inverse(w));v=h1(difference)
 obstruction=v@coker%3
 liftable=not np.any(obstruction)
 records.append({'parity':q[0],'matrix':R.Q[q[1]],'lift_word':w,
                 'liftable':liftable,'obstruction':obstruction.tolist()})
 print('Cubic centralizer base',q,'liftable',liftable,flush=True)
odd_target=next(r for r in records if r['parity']==26 and tuple(r['matrix'])==R.I)
print('EXACT odd cubic ambiguity (X5 parity, signed matrix I):',odd_target['liftable'],flush=True)
out={'scope':'Exact image of C_R(d) in Q for R=P/(Nprime N^3)',
     'base_order':768,'kernel_dimension':114,'rank_D_minus_I':len(rank),
     'd_generator_images':dgen,'parity_matrix':Dpar.tolist(),
     'centralizer_residues':records,'odd_cubic_ambiguity_survives':odd_target['liftable']}
np.savez_compressed(Path(__file__).with_suffix('.npz'),D=M,coker=coker,**{
 'cycle'+str(ch):cycles[ch] for ch in range(32)},**{'projection'+str(ch):proj[ch] for ch in range(32)})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
