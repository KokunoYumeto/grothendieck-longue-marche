#!/usr/bin/env python3
"""A literal finite B4/Z quotient retaining class-two pointpush at three.

The pointpush group is the order27 Heisenberg group, not its homology.
The quotient is constructed from Ferrari B4=F2 semidirect B3 and the
actual central relation z4. It is then combined with pure linking parity.
"""
import test_fivepoint_cm_level as T
import numpy as np,json,itertools
from pathlib import Path
I=(1,0,0,1);U=(1,1,0,1);L=(1,0,2,1)
def mm(a,b):return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%3 for i in range(2) for j in range(2))
def mi(a):return (a[3],-a[1]%3,-a[2]%3,a[0])
def mv(a,v):return ((a[0]*v[0]+a[1]*v[1])%3,(a[2]*v[0]+a[3]*v[1])%3,v[2])
def hm(a,b):return ((a[0]+b[0])%3,(a[1]+b[1])%3,(a[2]+b[2]+2*(a[0]*b[1]-a[1]*b[0]))%3)
def hi(a):return tuple(-x%3 for x in a)
Q=[I];qi={I:0};char={I:0}
for q in Q:
 for g in (U,L):
  z=mm(q,g);value=(char[q]+1)%3
  if z not in qi:qi[z]=len(Q);Q.append(z);char[z]=value
  assert char[z]==value
assert len(Q)==24
# Prequotient H3 semidirect {(M,t): t mod3=char(M)}, t mod9.
def pre_mul(g,h):return (hm(g[0],mv(g[1],h[0])),mm(g[1],h[1]),(g[2]+h[2])%9)
one=((0,0,0),I,0);pa=((0,0,0),U,1);pb=((0,0,0),L,1);pc=((1,0,2),U,1)
abc=pre_mul(pre_mul(pa,pb),pc);z4=one
for _ in range(4):z4=pre_mul(z4,abc)
assert z4[0][:2]==(0,0) and z4[1]==I and z4[2]==3
central=int(z4[0][2]);print('Literal z4 in the prequotient:',z4,flush=True)
# Reduce the t coordinate to its canonical representative char(M).
def reduce_pre(g):
 h,M,t=g;j=((t-char[M])%9)//3
 return ((h[0],h[1],(h[2]-j*central)%3),M)
def mul(g,h):
 return reduce_pre(pre_mul((g[0],g[1],char[g[1]]),(h[0],h[1],char[h[1]])))
def inv(g):
 h,M=g;N=mi(M)
 return reduce_pre((mv(N,hi(h)),N,-char[M]%9))
one=((0,0,0),I);a=reduce_pre(pa);b=reduce_pre(pb);c=reduce_pre(pc)
def power(g,n):
 if n<0:return power(inv(g),-n)
 h=one
 for _ in range(n):h=mul(h,g)
 return h
assert mul(a,c)==mul(c,a)
assert mul(mul(a,b),a)==mul(mul(b,a),b)
assert mul(mul(b,c),b)==mul(mul(c,b),c)
assert power(mul(mul(a,b),c),4)==one
Bgens=[a,b,c]
def bw(w):
 h=one
 for j in w:h=mul(h,Bgens[j-1] if j>0 else inv(Bgens[-j-1]))
 return h
words=[(2,1,1,-2),(2,2),(3,2,1,1,-2,-3),(3,2,2,-3),(3,3)]
Pgens=[bw(w) for w in words]
print('Exact five pure generators:',Pgens,flush=True)
# Enumerate the actual image, without assuming its order.
G=[one];ids={one:0}
for g in G:
 for h in Bgens:
  z=mul(g,h)
  if z not in ids:ids[z]=len(G);G.append(z)
assert len(G)==648
PG=[one];pids={one:0}
for g in PG:
 for h in Pgens:
  z=mul(g,h)
  if z not in pids:pids[z]=len(PG);PG.append(z)
assert len(PG)==648
# Every relation of P is checked in the exact nonabelian target.
def eval_P(w):
 h=one
 for j in w:h=mul(h,Pgens[j-1] if j>0 else inv(Pgens[-j-1]))
 return h
for w in T.C.relations:assert eval_P(w)==one
# The combined pure parity quotient has order32*648. Each finite image
# generator has odd order, so its even powers generate the same648 group;
# hence the parity factor is independent.
assert all(power(g,9)==one for g in Pgens)
print('PASS B4/Z image648, pure image648, combined linking-parity image20736',flush=True)
images=np.zeros((289,8,3),dtype=np.int16)
for i,ws in enumerate(T.mappedloops):
 for j,w in enumerate(ws):
  h,M=eval_P(w);assert M==I;images[j,i]=h
V=images[:,:,:2].reshape(289,16)
W=np.array([[ (images[j,i,0]*images[k,i,1]-images[j,i,1]*images[k,i,0])%3 for i in range(8)]
            for j in range(289) for k in range(j)],dtype=np.int16)
commbasis,_=T.row_space_projection(W,3)
vbasis,_=T.row_space_projection(V,3)
print('Joint J image: pointpush abelian rank',len(vbasis),'commutator central rank',len(commbasis),flush=True)
# Pass central coordinates through the actual commutator quotient.
_,Cproj=T.row_space_projection(commbasis,3)
AJ=np.hstack((V,images[:,:,2]@Cproj%3))
B,_=T.row_space_projection(AJ,3)
print('Joint J abelianization rank:',len(B),'joint J group order 3^',len(B)+len(commbasis),flush=True)
strong=np.load(Path(__file__).with_name('extract_coupled_base_fibers.npz'))
D,_=T.row_space_projection(strong['nullspace3']@AJ%3,3)
base=strong['particular3']@AJ%3
print('Image of the exact old odd source fiber: dimension',len(D),'base',base.tolist(),flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),images=images,V=V,commutator_basis=commbasis,
                   central_projection=Cproj,J_abelian_map=AJ,fiber_base=base,fiber_directions=D)
Path(__file__).with_suffix('.json').write_text(json.dumps({'L_image_order':648,'P_combined_order':20736,
 'z4_prequotient':z4,'pointpush_abelian_rank':len(vbasis),'joint_commutator_rank':len(commbasis),
 'joint_J_abelian_rank':len(B),'joint_J_order_power3':len(B)+len(commbasis),
 'odd_fiber_abelian_dimension':len(D),'odd_fiber_base':base.tolist()},indent=2)+'\n')
