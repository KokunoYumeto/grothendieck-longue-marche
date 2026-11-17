#!/usr/bin/env python3
"""A successive 3-then-2 homology target retaining the cubic obstruction.

Construct R8, an actual P5 quotient of order 48*3^8, from the odd
homology character over C2(total linking) x SL2(F3). Then compute
all characteristic-two homology blocks for ker(P5 -> R8), using F4
characters of its elementary-three normal subgroup. No finite GT
image or parity exclusion is inferred from a homology dimension.
"""
import numpy as np,json
from pathlib import Path
here=Path(__file__).parent
source=np.load(here/'check_cubic_centralizer_homology.npz')
small=np.load(here/'reduce_cubic_detector_module.npz')
Z=source['cycle31'];P=source['projection31'];dual=small['dual_basis']
P8=P@dual.T%3;Z8=Z[:8]
assert np.array_equal(Z8@P8%3,np.eye(8,dtype=np.int16))
I=(1,0,0,1);U=(1,1,0,1);L=(1,0,2,1)
def mul(a,b):return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%3 for i in range(2) for j in range(2))
def inv(a):return a[3],-a[1]%3,-a[2]%3,a[0]
def inverse(w):return tuple(-j for j in reversed(w))
def band(i,j):return tuple(range(j-1,i,-1))+(i,i)+tuple(-k for k in range(i+1,j))
def beval(w):
 q=I
 for j in w:q=mul(q,(U,L,U)[j-1] if j>0 else inv((U,L,U)[-j-1]))
 return q
gens=[beval(band(i,j)) for i,j in ((1,3),(2,3),(1,4),(2,4),(3,4))]
Q3=[I];i3={I:0}
for q in Q3:
 for g in gens:
  h=mul(q,g)
  if h not in i3:i3[h]=len(Q3);Q3.append(h)
tab3=np.array([[i3[mul(q,r)] for r in Q3] for q in Q3],dtype=np.int16)
g3=[i3[g] for g in gens];ig3=[i3[inv(g)] for g in gens]

def chain(start,w):
 a,q=start;v=np.zeros(120,dtype=np.int16)
 for j in w:
  k=abs(j)-1
  if j>0:v[5*q+k]+=(-1 if a else 1);a^=1;q=int(tab3[q,g3[k]])
  else:a^=1;q=int(tab3[q,ig3[k]]);v[5*q+k]-=(-1 if a else 1)
 return (a,q),v%3
base=[(0,0)];bi={base[0]:0};paths={base[0]:()}
for q in base:
 for j,g in enumerate(g3):
  h=(q[0]^1,int(tab3[q[1],g]))
  if h not in bi:bi[h]=len(base);base.append(h);paths[h]=paths[q]+(j+1,)
assert len(base)==48
section=np.array([chain((0,0),paths[q])[1] for q in base],dtype=np.int16)
actions=[]
for a,q in base:
 D=np.zeros((120,120),dtype=np.int16)
 for h in range(24):
  for j in range(5):D[5*h+j,5*int(tab3[q,h])+j]=(-1 if a else 1)
 A=Z8@D@P8%3
 # Factorization on all twelve old cycle coordinates proves quotient stability.
 assert np.array_equal(Z@D@P8%3,(Z@P8)@A%3)
 actions.append(A)
actions=np.array(actions,dtype=np.int16)
letters=list(range(1,6))+list(range(-1,-6,-1));li={j:i for i,j in enumerate(letters)}
nextq=np.zeros((48,10),dtype=np.int16);shift=np.zeros((48,10,8),dtype=np.int16)
for k,q in enumerate(base):
 for l,j in enumerate(letters):
  h,v=chain(q,(j,));hk=bi[h];nextq[k,l]=hk
  shift[k,l]=(section[k]+v-section[hk])@P8%3

def comm(u,v):return (-v,-u,v,u)
rels=[]
for left,right in [((1,3,-1),(-5,3,5)),((1,4,-1),comm(3,5)+(4,)+inverse(comm(3,5))),
 ((1,5,-1),comm(3,5)+(5,)),((2,3,-2),(3,)),((2,4,-2),(-5,4,5)),
 ((2,5,-2),comm(4,5)+(5,))]:rels.append(left+inverse(right))
# Each lifted relation is exactly trivial in the constructed finite extension.
terms=[]
for q0 in range(48):
 for ri,w in enumerate(rels):
  row=6*q0+ri;q=q0;v=np.zeros(8,dtype=np.int16)
  for j in w:
   if j>0:terms.append((row,5*q+j-1,v.copy()))
   v=(v+shift[q,li[j]])%3;q=int(nextq[q,li[j]])
   if j<0:terms.append((row,5*q-j-1,v.copy()))
  assert q==q0 and not np.any(v)
print('PASS actual quotient R8: base 48, elementary-three kernel dimension 8, order',48*3**8,flush=True)
rows=np.array([r for r,e,v in terms],dtype=np.int16)
edges=np.array([e for r,e,v in terms],dtype=np.int16)
vectors=np.array([v for r,e,v in terms],dtype=np.int16)
# F4=F2[w]/(w^2+w+1), encoded 0,1,w,w+1.
mt=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8)
invt=np.array([0,1,3,2],dtype=np.uint8);phase=np.array([1,2,3],dtype=np.uint8)
def rank4(A):
 A=A.copy();r=0
 for c in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,c])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=mt[invt[A[r,c]],A[r]]
  ns=np.flatnonzero(A[r+1:,c])+r+1
  A[ns]^=mt[A[ns,c,None],A[r]];r+=1
  if r==len(A):break
 return r

def code(v):return sum(int(x)*3**j for j,x in enumerate(v))
def vec(k):
 v=[]
 for _ in range(8):v.append(k%3);k//=3
 return np.array(v,dtype=np.int16)
seen=set();records=[];total=0
for k in range(3**8):
 if k in seen:continue
 lam=vec(k);orbit={code(A@lam%3) for A in actions};seen.update(orbit)
 assert len(orbit)==len({code(A@lam%3) for A in actions})
 assert code(-lam%3) in orbit # Frobenius-stable, so the sum descends to F2.
 D=np.zeros((288,240),dtype=np.uint8)
 np.bitwise_xor.at(D,(rows,edges),phase[vectors@lam%3])
 B=np.zeros((240,48),dtype=np.uint8)
 for q in range(48):
  for j in range(5):
   B[5*q+j,q]^=1;B[5*q+j,int(nextq[q,j])]^=phase[int(shift[q,j]@lam%3)]
 # Verify boundary^2=0 in the actual character block, with F4 arithmetic.
 product=np.zeros((288,48),dtype=np.uint8)
 for e in range(240):product^=mt[D[:,e,None],B[e]]
 assert not np.any(product)
 r1=rank4(B);r2=rank4(D);h1=240-r1-r2
 rec={'character':k,'orbit_size':len(orbit),'boundary_rank':r1,'relation_rank':r2,
      'H1_dimension':h1,'F2_orbit_dimension':h1*len(orbit)}
 records.append(rec);total+=rec['F2_orbit_dimension']
 if h1:print('Nonzero characteristic-two homology block:',rec,flush=True)
assert len(seen)==3**8
print('Complete 3^8-character orbit census:',len(records),'orbits; H1 dimension over F2',total,flush=True)
out={'scope':'Actual successive-prime finite quotient construction and exact cover homology; no GT image claim',
 'base_order':48*3**8,'kernel_H1_F2_dimension':total,'character_orbits':records}
np.savez_compressed(Path(__file__).with_suffix('.npz'),base=np.array(base),Q3=np.array(Q3),
 actions=actions,nextq=nextq,shift=shift,section=section,projection=P8)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
