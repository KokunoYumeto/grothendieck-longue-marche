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
seed=156
orbit=sorted({vcode(A@vdecode(seed)%3) for A in actions})
lams=np.array([vdecode(k) for k in orbit],dtype=np.int16);lidx={k:i for i,k in enumerate(orbit)}
assert len(orbit)==24
nl=len(orbit)

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
print('PASS exact 24-character target module, quotient coordinates 24*72 over F4',flush=True)

# Evaluate an actual P5 word in the crossed edge-chain quotient. An element
# over the identity of the order-432 base lies in its 192-dimensional F2
# homology kernel. We retain redundant coordinates for transparent checking.
def eval_word(w):
 q=0;v=np.zeros(8,dtype=np.int16);a=np.zeros((nl,72),dtype=np.uint8)
 for j in w:
  if j>0:a^=mt[phase[lams@v%3,None],P[:,5*q+j-1,:]]
  v=(v+shift[q,li[j]])%3;q=int(nextq[q,li[j]])
  if j<0:a^=mt[phase[lams@v%3,None],P[:,5*q-j-1,:]]
 return q,v,a

def pack(a):
 n=0
 for k,v in enumerate(a.ravel()):n|=int(v)<<(2*k)
 return n
nb=nl*72*2;targetbits=8*nb
zero=np.zeros((nl,72),dtype=np.uint8)
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
assert len(Dsmall)==4
JI=(strong['joint_R8_images'].reshape(289,8,8)@Dsmall.T).reshape(289,32)%3
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

def apply(cols,v):
 out=0
 while v:
  bit=v&-v;out^=cols[bit.bit_length()-1];v^=bit
 return out
class Span:
 def __init__(self):self.rows={}
 def add(self,v):
  while v:
   p=v.bit_length()-1
   if p in self.rows:v^=self.rows[p]
   else:self.rows[p]=v;return True
  return False
 def reduce(self,v):
  for p in sorted(self.rows,reverse=True):
   if (v>>p)&1:v^=self.rows[p]
  return v
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

# Source M4 quotient and its exactly selected 24-character support.
jci={e:k for k,e in enumerate(T.jchords)}
Jcoords=coords.copy()
def jchain(q,w):
 a=np.zeros(289,dtype=np.int16)
 for j in w:
  k=abs(j)-1
  if j>0:e=(q,k);q=int(T.jtable[q,T.jgens[k]]);sgn=1
  else:q=int(T.jtable[q,T.jinverse[T.jgens[k]]]);e=(q,k);sgn=-1
  if e in jci:a[jci[e]]+=sgn
 return q,a
ops=[]
for q,sub in [(T.jgens[0],None),(T.jgens[1],None),(0,((2,),(1,))),(0,((2,),(-2,-1)))]:
 images=[]
 for w in T.jloops:
  end,a=jchain(q,w if sub is None else T.subst(w,sub));assert end==q;images.append(a@Jcoords%3)
 images=np.array(images);op=images[chosen]
 assert np.array_equal(Jcoords@op%3,images)
 ops.append(op)
MS=ops[2];MR=ops[3]
assert np.array_equal(MS@MS%3,np.eye(4,dtype=np.int16))
source_chars=set();pullbacks={}
for i in range(8):
 L=np.array([vals[j][i][0] for j in chosen],dtype=np.int16)
 for k,lam in enumerate(lams):
  alpha=tuple(L@lam%3);pullbacks[i,k]=alpha
  if any(alpha):source_chars.add(alpha)
todo=list(source_chars)
for alpha in todo:
 for op in ops:
  a=tuple(op@alpha%3)
  if a not in source_chars:source_chars.add(a);todo.append(a)
source_chars=sorted(source_chars);sc=np.array(source_chars,dtype=np.int16);si={a:i for i,a in enumerate(source_chars)}
assert len(sc)==24
assert sum(np.array_equal(MS@a%3,a) for a in sc)==4
print('PASS exact source support: 24 nontrivial characters, four harmonic fixed characters',flush=True)

# The free source cover over Q_joint has 288 vertices and 576 edges.
snext=np.zeros((288,4),dtype=np.int16);sshift=np.zeros((288,4,4),dtype=np.int16)
for q in range(288):
 for j,g in enumerate(T.jgens):
  h=int(T.jtable[q,g]);snext[q,j]=h
  if (q,j) in jci:sshift[q,j]=Jcoords[jci[q,j]]
for q in range(288):
 for j,g in enumerate(T.jgens):
  h=int(T.jtable[q,T.jinverse[g]]);snext[q,2+j]=h
  sshift[q,2+j]=-sshift[h,j]%3

def sevalbase(w):
 q=0;v=np.zeros(4,dtype=np.int16)
 for j in w:
  l=j-1 if j>0 else -j+1
  v=(v+sshift[q,l])%3;q=int(snext[q,l])
 return q,v
sz=[];sfree=[]
for alpha in sc:
 boundary=np.zeros((576,288),dtype=np.uint8)
 for q in range(288):
  for j in range(2):
   boundary[2*q+j,q]^=1
   boundary[2*q+j,int(snext[q,j])]^=phase[int(sshift[q,j]@alpha%3)]
 P0,free=projection4(boundary.T)
 assert P0.shape==(576,288)
 sz.append(P0.T);sfree.append(free)
sz=np.array(sz,dtype=np.uint8);sfree=np.array(sfree,dtype=np.int16)
for i,alpha in enumerate(sc):
 ni=si[tuple(-alpha%3)]
 assert np.array_equal(sfree[i],sfree[ni])
 assert np.array_equal(mt[sz[i],sz[i]],sz[ni])
print('PASS source twisted-cycle bases and Frobenius descent',flush=True)

# Actual action of s on those source cycle bases.
sq=[];sv=[]
for q in range(288):
 end,v=sevalbase(T.subst(T.jpaths[q],((2,),(1,))));sq.append(end);sv.append(v)
sq=np.array(sq,dtype=np.int16);sv=np.array(sv,dtype=np.int16)
sdest=np.array([2*sq[q]+1-j for q in range(288) for j in range(2)],dtype=np.int16)
assert len(set(sdest.tolist()))==576
sback=np.argsort(sdest)
smatrices=[];sout=[]
for i,alpha in enumerate(sc):
 ao=MS@alpha%3;k=si[tuple(ao)];sout.append(k)
 factors=np.repeat(phase[sv@ao%3],2)
 oldedges=sback[sfree[k]]
 smatrices.append(mt[sz[i][:,oldedges],factors[oldedges]])
smatrices=np.array(smatrices,dtype=np.uint8)
# Verify the involution by applying the monomial edge action twice;
# the matrices are exact restrictions to cycle spaces.
for i,k in enumerate(sout):
 product=np.zeros((288,288),dtype=np.uint8)
 for j in range(288):product^=mt[smatrices[i][:,j,None],smatrices[k][j]]
 assert np.array_equal(product,np.eye(288,dtype=np.uint8))

frameblocks=[];seen=set();frame_dimension=0
for i in range(len(sc)):
 if i in seen:continue
 inds=[i] if sout[i]==i else [i,sout[i]];seen.update(inds)
 K=np.zeros((288*len(inds),288*len(inds)),dtype=np.uint8)
 for ii,k in enumerate(inds):
  oo=inds.index(sout[k]);K[ii*288:(ii+1)*288,oo*288:(oo+1)*288]^=smatrices[k]
  scalar=phase[int(sc[k]@basecoords%3)]
  K[ii*288:(ii+1)*288,ii*288:(ii+1)*288]^=scalar*np.eye(288,dtype=np.uint8)
 Pf,_=projection4(K)
 frameblocks.append((inds,Pf,frame_dimension));frame_dimension+=Pf.shape[1]
print('Exact harmonic-conjugator cokernel dimension over F4:',frame_dimension,flush=True)

# Source edge-to-target insertion maps, one character at a time.
# This constructs the morphism on all relevant homology classes.
Hmaps={}
for i,pair in enumerate(T.pairwords):
 edge_maps=np.zeros((nl,576,72),dtype=np.uint8)
 for q in range(288):
  pq,pv=eval_base(T.subst(T.jpaths[q],pair))
  for j in range(2):
   g=pq;v=pv.copy();a=np.zeros((nl,72),dtype=np.uint8)
   for letter in pair[j]:
    if letter>0:a^=mt[phase[lams@v%3,None],P[:,5*g+letter-1,:]]
    v=(v+shift[g,li[letter]])%3;g=int(nextq[g,li[letter]])
    if letter<0:a^=mt[phase[lams@v%3,None],P[:,5*g-letter-1,:]]
   edge_maps[:,2*q+j]=a
 for k in range(nl):
  alpha=pullbacks[i,k]
  if not any(alpha):continue
  z=sz[si[alpha]];H=np.zeros((288,72),dtype=np.uint8)
  for j,row in enumerate(z):
   nz=np.flatnonzero(row)
   H[j]=np.bitwise_xor.reduce(mt[row[nz,None],edge_maps[k,nz]],axis=0)
  Hmaps[i,k]=H
 print('Constructed exact insertion homology map',i+1,flush=True)

# The finite prime-to-two deck group has order 3^4. Averaging decomposes
# H1(source kernel,F2) into the old rank-289 component and the character
# components. It introduces no guessed independent evaluation variables.
frame_offset=eqbits+rr
frame_sources={}
for inds,Pf,off in frameblocks:
 for j,i in enumerate(inds):frame_sources[i]=(Pf[j*288:(j+1)*288],off)
def frame_variable(i,j,scalar):
 row,off=frame_sources[i]
 return pack(mt[scalar,row[j]])<<(2*off)

image=Span();var_count=0
for j in range(289):
 w=0
 for i in range(8):
  a=np.zeros((nl,72),dtype=np.uint8)
  for k in range(nl):
   if not any(pullbacks[i,k]):a[k]=vals[j][i][1][k]
  w|=pack(a)<<(i*nb)
 w|=(1<<j)<<targetbits
 image.add(apply(linear,w));var_count+=1
seen=set()
for ci,alpha in enumerate(sc):
 if ci in seen:continue
 ni=si[tuple(-alpha%3)];seen.update((ci,ni))
 for j in range(288):
  for scalar in (1,2):
   w=0
   for i in range(8):
    a=np.zeros((nl,72),dtype=np.uint8)
    for k in range(nl):
     pb=pullbacks[i,k]
     if pb==tuple(alpha):a[k]=mt[scalar,Hmaps[i,k][j]]
     elif pb==tuple(-alpha%3):a[k]=mt[mt[scalar,scalar],Hmaps[i,k][j]]
    w|=pack(a)<<(i*nb)
   f=frame_variable(ci,j,scalar)^frame_variable(ni,j,int(mt[scalar,scalar]))
   image.add(apply(linear,w)^(f<<frame_offset));var_count+=1
 if var_count%500<600:print('Exact source variables processed',var_count,'equation-image rank',len(image.rows),flush=True)
assert var_count==289+24*288
print('PASS complete relevant source homology image, variables',var_count,'rank',len(image.rows),flush=True)

# Evaluate all finite harmonic-frame base choices, not a selected lift.
sfreeidx=np.full((len(sc),576),-1,dtype=np.int16)
for i,free in enumerate(sfree):sfreeidx[i,free]=np.arange(288)
def source_word(w):
 q=0;v=np.zeros(4,dtype=np.int16);a=np.zeros((len(sc),288),dtype=np.uint8)
 for letter in w:
  j=abs(letter)-1
  if letter>0:
   edge=2*q+j;ph=phase[sc@v%3]
   for i in range(len(sc)):
    k=int(sfreeidx[i,edge])
    if k>=0:a[i,k]^=ph[i]
  l=j if letter>0 else j+2
  v=(v+sshift[q,l])%3;q=int(snext[q,l])
  if letter<0:
   edge=2*q+j;ph=phase[sc@v%3]
   for i in range(len(sc)):
    k=int(sfreeidx[i,edge])
    if k>=0:a[i,k]^=ph[i]
 return q,v,a

def gf4row(v,M):
 out=np.zeros(M.shape[1],dtype=np.uint8)
 for j in np.flatnonzero(v):out^=mt[v[j],M[j]]
 return out

def source_Jword(exps):
 out=[]
 for j,n in zip(chosen,exps):out.extend(T.jloops[j]*int(n))
 return tuple(out)
tfword=source_Jword(basecoords)
records=[];equation_image=list(image.rows.values())
for code in range(81):
 t=code;vb=[]
 for _ in range(4):vb.append(t%3);t//=3
 vb=np.array(vb,dtype=np.int16)
 if np.any((vb@MS-vb-basecoords)%3):continue
 tb=source_Jword(vb)
 word=T.subst(tb,((2,),(1,)))+T.inverse(tb)+T.inverse(tfword)
 q,v,a=source_word(word);assert q==0 and not np.any(v)
 fc=0
 for inds,Pf,off in frameblocks:
  f=gf4row(np.concatenate([a[i] for i in inds]),Pf);fc|=pack(f)<<(2*off)
 rhs0=constant^(fc<<frame_offset);res=image.reduce(rhs0)
 rec={'beta_M4_coordinates':vb.tolist(),'consistent':res==0,'residual_hex':hex(res)}
 records.append(rec);print('New harmonic pure-frame equation:',rec,flush=True)
print('COUPLED FINITE TEST:',sum(r['consistent'] for r in records),'of',len(records),'harmonic frame bases survive',flush=True)
out={'scope':'Exact source-framed successive-prime pentagon and harmonic-conjugator test; no full profinite lift asserted',
 'target_character':seed,'target_character_orbit':orbit,'target_base_order':48*3**len(Dsmall),
 'target_homology_factor_dimension_F2':24*nl,'joint_source_base_order':288*3**len(chosen),
 'source_character_count':len(sc),'source_harmonic_fixed_characters':4,
 'source_variable_count':var_count,'frame_cokernel_F4_dimension':frame_dimension,
 'equation_image_rank':len(image.rows),'harmonic_frame_bases':records,
 'odd_profile_excluded':not any(r['consistent'] for r in records)}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
Path(__file__).with_suffix('.certificate.json').write_text(json.dumps({
 'equation_image_basis_hex':[hex(v) for v in equation_image],
 'base_constant_hex':hex(constant)},indent=2)+'\n')
