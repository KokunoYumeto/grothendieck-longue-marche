#!/usr/bin/env python3
"""Literal characteristic quaternion surface cover and its modular matrix action."""
import numpy as np,json,itertools
from pathlib import Path
def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(int(x))
 return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,images):return red(x for j in w for x in (images[j-1] if j>0 else inv(images[-j-1])))
# q=sign*{1,i,j,k}; sign encoded by adding4.
def qm(a,b):
 sa=-1 if a>=4 else 1;sb=-1 if b>=4 else 1;a%=4;b%=4;s=sa*sb
 if a==0:c=b
 elif b==0:c=a
 elif a==b:c=0;s=-s
 else:
  c=6-a-b
  if (a,b) not in ((1,2),(2,3),(3,1)):s=-s
 return c+(4 if s<0 else 0)
qi=[next(j for j in range(8) if qm(i,j)==0) for i in range(8)]
def image(w):
 q=0
 for x in w:q=qm(q,abs(x) if x>0 else qi[abs(x)])
 return q
assert image((1,1))==image((2,2))==4 and image((1,2,-1,-2))==4
sections={0:()};queue=[0];tree=set()
for q in queue:
 for k in (1,2,-1,-2):
  dest=qm(q,k if k>0 else qi[-k])
  if dest in sections:continue
  sections[dest]=sections[q]+(k,);queue.append(dest)
  tree.add((q,k) if k>0 else (dest,-k))
chords=[(q,k) for q in range(8) for k in (1,2) if (q,k) not in tree]
assert len(chords)==9;ci={e:i+1 for i,e in enumerate(chords)}
def rewrite(w):
 q=0;out=[]
 for x in w:
  if x>0:
   e=(q,x);q=qm(q,x)
   if e in ci:out.append(ci[e])
  else:
   q=qm(q,qi[-x]);e=(q,-x)
   if e in ci:out.append(-ci[e])
 assert q==0
 return red(out)
basis=[red(sections[q]+(k,)+inv(sections[qm(q,k)])) for q,k in chords]
for i,w in enumerate(basis):assert rewrite(w)==(i+1,)
Uwords=((1,),(2,1));Lwords=((1,-2),(2,))
automorphisms=[tuple(rewrite(sub(w,g)) for w in basis) for g in (Uwords,Lwords)]
automorphisms += [tuple(rewrite((g,)+w+(-g,)) for w in basis) for g in (1,2)]
def matrix(words):return np.array([[w.count(i)-w.count(-i) for w in words] for i in range(1,10)],dtype=np.int16)%3
M=[matrix(w) for w in automorphisms]
def rank_mod3(A):
 A=A.copy()%3;r=0
 for j in range(A.shape[1]):
  rows=np.flatnonzero(A[r:,j])
  if not len(rows):continue
  k=r+int(rows[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*(1 if A[r,j]==1 else 2)%3
  for k in range(len(A)):
   if k!=r and A[k,j]:A[k]=(A[k]-A[k,j]*A[r])%3
  r+=1
 return r
for A in M:assert rank_mod3(A)==9
# Check B3, its actual inner central correction, and the normal quaternion deck group.
assert np.array_equal(M[0]@M[1]@M[0]%3,M[1]@M[0]@M[1]%3)
Z=np.linalg.matrix_power(M[0]@M[1]%3,3)%3
Z2=Z@Z%3;minus=np.linalg.matrix_power(M[2],2)%3
assert np.array_equal(Z2,minus)
assert np.array_equal(np.linalg.matrix_power(M[2],4)%3,np.eye(9,dtype=np.int16))
assert np.array_equal(np.linalg.matrix_power(M[3],2)%3,minus)
deck=[np.eye(9,dtype=np.int16)];ds={deck[0].tobytes()}
for A in deck:
 for B in M[2:]:
  C=A@B%3
  if C.tobytes() not in ds:ds.add(C.tobytes());deck.append(C)
assert len(deck)==8
print('PASS characteristic Q8 cover, rank9, exact braid action and eight faithful deck matrices',flush=True)

# Faithful finite permutation action of the matrix group, together with
# the literal signed mod12 action (mod4 primitive vectors and mod3 nonzero vectors).
vectors=np.array(list(itertools.product(range(3),repeat=9)),dtype=np.int16)
powers=3**np.arange(8,-1,-1,dtype=np.int64)
v4=np.array([(a,b) for a,b in itertools.product(range(4),repeat=2) if a%2 or b%2],dtype=np.int16)
v3=np.array([(a,b) for a,b in itertools.product(range(3),repeat=2) if a or b],dtype=np.int16)
i4={tuple(v):i for i,v in enumerate(v4)};i3={tuple(v):i for i,v in enumerate(v3)}
U=np.array([[1,1],[0,1]],dtype=np.int16);L=np.array([[1,0],[-1,1]],dtype=np.int16)
perms=[];baseperms=[]
for A,B in zip(M,(U,L,np.eye(2,dtype=np.int16),np.eye(2,dtype=np.int16))):
 p=(vectors@A%3)@powers+1
 p4=[i4[tuple(v@B%4)]+1 for v in v4]
 p3=[i3[tuple(v@B%3)]+13 for v in v3]
 baseperms.append(p4+p3)
 perms.append(p.tolist()+[len(vectors)+j for j in p4+p3])
assert all(len(set(p))==len(p) for p in perms)
modular=[np.eye(2,dtype=np.int16)];mi={tuple(modular[0].reshape(-1)):0}
for A in modular:
 for B in (U,L):
  C=A@B%12;key=tuple(C.reshape(-1))
  if key not in mi:mi[key]=len(modular);modular.append(C)
assert len(modular)==1152
modperms=[]
for A in modular:
 modperms.append([i4[tuple(v@A%4)]+1 for v in v4]+[i3[tuple(v@A%3)]+13 for v in v3])
script=[]
for name,p in zip(('a','b','di','dj'),perms):script.append(name+':=PermList('+str(p)+');;')
script += ['G:=Group(a,b,di,dj);;', 'Print("JOINT_ORDER ",Size(G),"\\n");',
 'Deck:=Group(di,dj);;', 'Print("DECK_ORDER ",Size(Deck)," NORMAL ",IsNormal(G,Deck),"\\n");',
 'pi:=NaturalHomomorphismByNormalSubgroup(G,Deck);;', 'J:=Image(pi);;',
 'Print("OUTER_ORDER ",Size(J),"\\n");',
 'CM:=Image(pi,a*b);;', 'C:=Centralizer(J,CM);;',
 'Print("CENTRALIZER_ORDER ",Size(C),"\\n");',
 'Back:=PreImage(pi,C);;',f'base:=ActionHomomorphism(G,[{len(vectors)+1}..{len(vectors)+20}],OnPoints);;',
 'BaseC:=Image(base,Back);;', 'Print("CM_BASE_IMAGE_ORDER ",Size(BaseC),"\\n");']
script.append('modperms:='+str(modperms)+';;')
script.append('modmatrices:='+str([A.reshape(-1).tolist() for A in modular])+';;')
script += ['for i in [1..Length(modperms)] do if PermList(modperms[i]) in BaseC then Print("CM_BASE_RESIDUE ",modmatrices[i],"\\n"); fi; od;', 'QUIT;']
Path(__file__).with_name('modular_quaternion_surface.g').write_text('\n'.join(script)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),normalizer_and_deck_matrices=np.array(M),
 deck_matrices=np.array(deck),modular_matrices=np.array(modular))
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Actual characteristic quaternion surface homology target; complete linear census is the input to the class-two certificate',
 'quaternion_quotient_order':8,'homology_kernel_rank':9,'surface_group_quotient_order':'8*3^9',
 'schreier_basis':basis,'actual_automorphism_words':automorphisms,
 'matrix_permutation_degree':len(vectors)+20,'modular_base_order':1152},indent=2)+'\n')
print('WROTE exact degree',len(vectors)+20,'joint permutation generators and GAP centralizer script',flush=True)
