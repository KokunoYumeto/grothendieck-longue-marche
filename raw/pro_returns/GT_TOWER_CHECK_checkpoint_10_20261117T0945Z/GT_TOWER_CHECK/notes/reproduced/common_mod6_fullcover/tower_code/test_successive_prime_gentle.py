#!/usr/bin/env python3
"""Exact pentagon image test in a successive-three-then-two quotient.

The target is a character-orbit factor of the F2 homology cover above
P5 -> R8 (order 48*3^8). Character 481 has an 8-point orbit spanning
a 2-dimensional dual module, so this factor already lies over an
order-432 quotient. All images of the joint source kernel are computed
by normal generators and exact module closure, without enumerating its
23,328 base elements. The selected source profile is rho=0,T=-I,W=I.
"""
import test_fivepoint_cm_level as T
import numpy as np,json
from pathlib import Path
from collections import deque
here=Path(__file__).parent
data=np.load(here/'build_coupled_cubic_two_layer.npz')
strong=np.load(here/'extract_coupled_base_fibers.npz')
base=[tuple(map(int,q)) for q in data['base']];bi={q:i for i,q in enumerate(base)}
Q3=[tuple(map(int,q)) for q in data['Q3']];i3={q:i for i,q in enumerate(Q3)}
nextq=data['nextq'];shift=data['shift'];actions=data['actions'];m=8
letters=list(range(1,6))+list(range(-1,-6,-1));li={j:i for i,j in enumerate(letters)}
mt=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8)
invt=np.array([0,1,3,2],dtype=np.uint8);phase=np.array([1,2,3],dtype=np.uint8)
def mul3(a,b):return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%3 for i in range(2) for j in range(2))
btable=np.array([[bi[(a[0]^b[0],i3[mul3(Q3[a[1]],Q3[b[1]])])] for b in base] for a in base],dtype=np.int16)
def vcode(v):return sum(int(x)*3**j for j,x in enumerate(v))
def vdecode(k):
 a=[]
 for _ in range(8):a.append(k%3);k//=3
 return np.array(a,dtype=np.int16)
seed=481
orbit=sorted({vcode(A@vdecode(seed)%3) for A in actions})
lams=np.array([vdecode(k) for k in orbit],dtype=np.int16);lidx={k:i for i,k in enumerate(orbit)}
assert len(orbit)==8

def eval_base(w,start=0):
 q=start;v=np.zeros(8,dtype=np.int16)
 for j in w:v=(v+shift[q,li[j]])%3;q=int(nextq[q,li[j]])
 return q,v
paths={0:()};order=[0]
for q in order:
 for j in range(5):
  h=int(nextq[q,j])
  if h not in paths:paths[h]=paths[q]+(j+1,);order.append(h)
assert len(paths)==48
cocycle=np.zeros((48,48,8),dtype=np.int16)
for q in range(48):
 for r in range(48):
  h,v=eval_base(paths[q]+paths[r]);assert h==btable[q,r];cocycle[q,r]=v

# Exact relator-chain projections in each of the eight F4 characters.
rels=T.C.relations
terms=[]
for q0 in range(48):
 for ri,w in enumerate(rels):
  row=6*q0+ri;q=q0;v=np.zeros(8,dtype=np.int16)
  for j in w:
   if j>0:terms.append((row,5*q+j-1,v.copy()))
   v=(v+shift[q,li[j]])%3;q=int(nextq[q,li[j]])
   if j<0:terms.append((row,5*q-j-1,v.copy()))
  assert q==q0 and not np.any(v)
tr=np.array([r for r,e,v in terms],dtype=np.int16)
te=np.array([e for r,e,v in terms],dtype=np.int16)
tv=np.array([v for r,e,v in terms],dtype=np.int16)
def projection4(A):
 A=A.copy();r=0;piv=[]
 for c in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,c])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=mt[invt[A[r,c]],A[r]]
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r];A[ns]^=mt[A[ns,c,None],A[r]]
  piv.append(c);r+=1
  if r==len(A):break
 free=[j for j in range(A.shape[1]) if j not in piv]
 P=np.zeros((A.shape[1],len(free)),dtype=np.uint8)
 P[free]=np.eye(len(free),dtype=np.uint8);P[piv]=A[:r,free]
 return P,free
projections=[];frees=[]
for lam in lams:
 D=np.zeros((288,240),dtype=np.uint8)
 np.bitwise_xor.at(D,(tr,te),phase[tv@lam%3])
 P,free=projection4(D);assert P.shape==(240,72)
 projections.append(P);frees.append(free)
P=np.array(projections,dtype=np.uint8)
print('PASS exact eight-character target module, quotient coordinates 8*72 over F4',flush=True)

# Evaluate an actual P5 word in the crossed edge-chain quotient. An element
# over the identity of the order-432 base lies in its 192-dimensional F2
# homology kernel. We retain redundant coordinates for transparent checking.
def eval_word(w):
 q=0;v=np.zeros(8,dtype=np.int16);a=np.zeros((8,72),dtype=np.uint8)
 for j in w:
  if j>0:a^=mt[phase[lams@v%3,None],P[:,5*q+j-1,:]]
  v=(v+shift[q,li[j]])%3;q=int(nextq[q,li[j]])
  if j<0:a^=mt[phase[lams@v%3,None],P[:,5*q-j-1,:]]
 return q,v,a

def pack(a):
 n=0
 for k,v in enumerate(a.ravel()):n|=int(v)<<(2*k)
 return n
nb=8*72*2;targetbits=8*nb
zero=np.zeros((8,72),dtype=np.uint8)
def value_mul(a,b):
 va,aa=a;vb,ab=b
 return (va+vb)%3,aa^mt[phase[lams@va%3,None],ab]
def value_inv(a):
 va,aa=a;return -va%3,mt[phase[-lams@va%3,None],aa]
def value_power(a,n):
 out=(np.zeros(8,dtype=np.int16),zero.copy())
 if n<0:a=value_inv(a)
 for _ in range(abs(n)):out=value_mul(out,a)
 return out

# The source J is free on the 289 recorded Schreier generators.
vals=[]
for ji,w in enumerate(T.jloops):
 row=[]
 for pair in T.pairwords:
  q,v,a=eval_word(T.subst(w,pair));assert q==0
  row.append((v,a))
 vals.append(row)
 if ji%60==0:print('Evaluated source Schreier generators',ji,flush=True)

# Select the actual normal generators for the kernel of the joint base map.
def rref3(A):
 A=A.copy()%3;r=0;piv=[]
 for c in range(A.shape[1]):
  z=np.flatnonzero(A[r:,c])
  if not len(z):continue
  k=r+int(z[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*pow(int(A[r,c]),-1,3)%3
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,c,None]*A[r])%3
  piv.append(c);r+=1
  if r==len(A):break
 return A[:r],piv
Dsmall,_=rref3(np.array([A@vdecode(seed)%3 for A in actions],dtype=np.int16))
assert len(Dsmall)==2
JI=(strong['joint_R8_images'].reshape(289,8,8)@Dsmall.T).reshape(289,16)%3
chosen=[];B=[]
for j,row in enumerate(JI):
 rr,_=rref3(np.array(B+[row],dtype=np.int16))
 if len(rr)>len(B):chosen.append(j);B.append(row)
assert len(chosen)==4
B=np.array(B,dtype=np.int16);_,piv=rref3(B)
aug=np.hstack((B[:,piv],np.eye(4,dtype=np.int16)))
red,_=rref3(aug);inverse=red[:,4:]
assert np.array_equal(B[:,piv]@inverse%3,np.eye(4,dtype=np.int16))
coords=JI[:,piv]@inverse%3
assert np.array_equal(coords@B%3,JI)
print('PASS joint source kernel: base order 288*3^4 =',288*3**4,'selected J indices',chosen,flush=True)
relations=[]
for j in range(289):
 if j not in chosen:relations.append([(j,1)]+[(k,-int(c)) for k,c in zip(chosen,coords[j]) if c])
relations.extend([(j,3)] for j in chosen)
for i,j in enumerate(chosen):
 for k in chosen[:i]:relations.append([(j,1),(k,1),(j,-1),(k,-1)])
assert len(relations)==295

def relation_image(rel):
 out=0
 for i in range(8):
  v=(np.zeros(8,dtype=np.int16),zero.copy())
  for j,n in rel:v=value_mul(v,value_power(vals[j][i],n))
  assert not np.any(lams@v[0]%3)
  out|=pack(v[1])<<(i*nb)
 old=0
 for j,n in rel:
  if n%2:old^=1<<j
 return out|(old<<targetbits)

# Exact conjugation matrices, obtained from left translation of every
# edge in the finite cover; all coordinates remain in actual chain quotients.
invactions=[]
for A in actions:
 aug=np.hstack((A,np.eye(8,dtype=np.int16)));rr,_=rref3(aug);invactions.append(rr[:,8:])
def deck_columns(q,v):
 cols=[0]*nb
 for k,lam in enumerate(lams):
  lo=invactions[q]@lam%3;k2=lidx[vcode(lo)]
  for j,e in enumerate(frees[k]):
   g=e//5;gen=e%5;outg=int(btable[q,g])
   factor=phase[int((v+cocycle[q,g])@lo%3)]
   row=mt[factor,P[k2,5*outg+gen]]
   for scalar in (1,2):
    cols[2*(k*72+j)+(scalar==2)]=pack(mt[scalar,row])<<(2*k2*72)
 return cols

def source_chain(q,w):
 out=0
 for j in w:
  k=abs(j)-1
  if j>0:e=(q,k);q=int(T.jtable[q,T.jgens[k]])
  else:q=int(T.jtable[q,T.jinverse[T.jgens[k]]]);e=(q,k)
  if e in jci:out^=1<<jci[e]
 return q,out
jci={e:k for k,e in enumerate(T.jchords)}
operators=[]
for which in (0,1):
 cols=[]
 for i,pair in enumerate(T.pairwords):
  q,v=eval_base(pair[which]);cols.extend(x<<(i*nb) for x in deck_columns(q,v))
 for w in T.jloops:
  end,a=source_chain(T.jgens[which],w);assert end==T.jgens[which]
  cols.append(a<<targetbits)
 assert len(cols)==targetbits+289;operators.append(cols)

def apply(cols,v):
 out=0
 while v:
  bit=v&-v;out^=cols[bit.bit_length()-1];v^=bit
 return out
class Span:
 def __init__(self):self.rows={};self.queue=deque()
 def add(self,v):
  while v:
   p=v.bit_length()-1
   if p in self.rows:v^=self.rows[p]
   else:self.rows[p]=v;self.queue.append(v);return True
  return False
 def reduce(self,v):
  for p in sorted(self.rows,reverse=True):
   if (v>>p)&1:v^=self.rows[p]
  return v
U=Span()
for rel in relations:U.add(relation_image(rel))
print('Initial exact normal-relator image rank',len(U.rows),flush=True)
processed=0
while U.queue:
 v=U.queue.popleft()
 for op in operators:U.add(apply(op,v))
 processed+=1
 if processed%100==0:print('Normal-closure module rank',len(U.rows),'processed',processed,flush=True)
print('PASS complete joint source-kernel image, rank',len(U.rows),flush=True)

# Choose one exact word over the selected J generators for the only
# joint order-432 base tuple of the chosen source-framed odd profile.
basevalue=strong['particular3']@JI%3
basecoords=basevalue[piv]@inverse%3
assert np.array_equal(basecoords@B%3,basevalue)
tf=[(j,int(c)) for j,c in zip(chosen,basecoords) if c]
fvals=[]
for i in range(8):
 val=(np.zeros(8,dtype=np.int16),zero.copy())
 for j,n in tf:val=value_mul(val,value_power(vals[j][i],n))
 fvals.append(val)
assert not np.any((strong['R8_directions'].reshape(-1,8,8)@Dsmall.T)%3)

# Compress the exact first-level source constraints to independent rows.
A=strong['A2'].copy()%2;b=strong['b2'].copy()%2;rr=0
for c in range(289):
 z=np.flatnonzero(A[rr:,c])
 if not len(z):continue
 k=rr+int(z[0]);A[[rr,k]]=A[[k,rr]];b[[rr,k]]=b[[k,rr]]
 ns=np.flatnonzero(A[:,c]);ns=ns[ns!=rr];A[ns]^=A[rr];b[ns]^=b[rr];rr+=1
 if rr==len(A):break
assert not np.any(A[rr:]) and not np.any(b[rr:]);A=A[:rr];b=b[:rr]
assert rr==241

# Impose all four necessary identities in this same successive-prime target.
cache_deck={}
def dcols(q,v):
 key=(q,tuple(int(x) for x in (Dsmall@v%3)))
 if key not in cache_deck:cache_deck[key]=deck_columns(q,v)
 return cache_deck[key]
def gmul(g,h):
 ag,q,v=g;ah,r,w=h
 return ag^apply(dcols(q,v),ah),int(btable[q,r]),(v+w@actions[q]+cocycle[q,r])%3
def ginv(g):
 ag,q,v=g;rq=next(r for r in range(48) if btable[q,r]==0)
 rv=(-(v+cocycle[q,rq])@actions[rq])%3
 return apply(dcols(rq,rv),ag),rq,rv
def gword(w):
 q,v,a=eval_word(w);return pack(a),q,v
fgroup=[(pack(a),0,v) for v,a in fvals]
expression_list=list(T.expressions.items())
linear=[0]*(targetbits+289);constant=0
for ei,(name,tokens) in enumerate(expression_list):
 current=(0,0,np.zeros(8,dtype=np.int16))
 for token in tokens:
  if isinstance(token,tuple):current=gmul(current,gword(token));continue
  i=abs(token)-1;fi=fgroup[i]
  h=current if token>0 else gmul(current,ginv(fi))
  cols=dcols(h[1],h[2])
  for j,v in enumerate(cols):linear[i*nb+j]^=v<<(ei*nb)
  current=gmul(current,fi if token>0 else ginv(fi))
 assert current[1]==0 and not np.any(lams@current[2]%3),(name,current[1],current[2])
 constant|=current[0]<<(ei*nb)
oldtf=np.zeros(289,dtype=np.uint8)
for j,n in tf:oldtf[j]^=n%2
rhs=b^(A@oldtf%2);eqbits=len(expression_list)*nb
for j in range(289):
 bits=sum(int(v)<<i for i,v in enumerate(A[:,j]));linear[targetbits+j]=bits<<eqbits
constant|=sum(int(v)<<i for i,v in enumerate(rhs))<<eqbits
image=Span()
for row in U.rows.values():image.add(apply(linear,row))
residual=image.reduce(constant)
print('Successive-prime pentagon plus gentle equations: image rank',len(image.rows),
      'odd profile consistent',residual==0,flush=True)
out={'scope':'Exact necessary source-framed pentagon and gentle equations over the specified successive-prime target; no lifting assertion',
 'character_seed':seed,'character_orbit':orbit,'target_base_order':432,
 'target_kernel_orbit_dimension_F2':192,'joint_source_base_order':288*3**4,
 'selected_J_indices':chosen,'normal_relator_count':len(relations),
 'joint_source_kernel_image_rank':len(U.rows),'source_constraint_rank':rr,
 'pentagon_and_gentle_joint_image_rank':len(image.rows),'odd_profile_consistent':residual==0,
 'residual_hex':hex(residual),'base_word_J_coordinates':tf}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
# Save exact bit-vector row spaces for independent replay of membership.
Path(__file__).with_suffix('.certificate.json').write_text(json.dumps({
 'joint_kernel_basis_hex':[hex(v) for v in U.rows.values()],
 'equation_image_basis_hex':[hex(v) for v in image.rows.values()],
 'constant_hex':hex(constant),'residual_hex':hex(residual)},indent=2)+'\n')
