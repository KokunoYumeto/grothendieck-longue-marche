#!/usr/bin/env python3
"""Locate target factors whose source support meets harmonic fixed characters."""
import test_fivepoint_cm_level as T
import numpy as np,json
from pathlib import Path
here=Path(__file__).parent
D=np.load(here/'build_coupled_cubic_two_layer.npz')
E=np.load(here/'extract_coupled_base_fibers.npz')
L=E['joint_R8_images']%3

def rr(A):
 A=A.copy()%3;r=0;piv=[]
 for c in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,c])
  if not len(nz):continue
  j=r+int(nz[0]);A[[r,j]]=A[[j,r]];A[r]=A[r]*pow(int(A[r,c]),-1,3)%3
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,c,None]*A[r])%3
  piv.append(c);r+=1
  if r==len(A):break
 return A[:r],piv
chosen=[];B=[]
for j,row in enumerate(L):
 R,_=rr(np.array(B+[row],dtype=np.int16))
 if len(R)>len(B):chosen.append(j);B.append(row)
assert len(B)==12
B=np.array(B,dtype=np.int16);_,piv=rr(B)
R,_=rr(np.hstack((B[:,piv],np.eye(12,dtype=np.int16))));C=L[:,piv]@R[:,12:]%3
assert np.array_equal(C@B%3,L)
jci={q:j for j,q in enumerate(T.jchords)}
def chain(q,w):
 a=np.zeros(289,dtype=np.int16)
 for j in w:
  k=abs(j)-1
  if j>0:edge=(q,k);q=int(T.jtable[q,T.jgens[k]]);sign=1
  else:q=int(T.jtable[q,T.jinverse[T.jgens[k]]]);edge=(q,k);sign=-1
  if edge in jci:a[jci[edge]]+=sign
 return q,a
ops=[]
for q,sub in [(T.jgens[0],None),(T.jgens[1],None),(0,((2,),(1,))),(0,((2,),(-2,-1)))]:
 rows=[]
 for w in T.jloops:
  end,a=chain(q,w if sub is None else T.subst(w,sub));assert end==q;rows.append(a@C%3)
 rows=np.array(rows);A=rows[chosen]
 assert np.array_equal(C@A%3,rows),'Full joint kernel fails marked S3 invariance'
 ops.append(A)
print('PASS full rank-12 source kernel is B-normal',flush=True)
powers=3**np.arange(12,dtype=np.int64);allcodes=np.arange(3**12,dtype=np.int64)
vectors=(allcodes[:,None]//powers)%3
lookups=[((vectors@A.T)%3)@powers for A in ops]
ids=np.full(3**12,-1,dtype=np.int32);orbits=[]
for start in range(3**12):
 if ids[start]>=0:continue
 n=len(orbits);todo=[start];ids[start]=n
 for v in todo:
  for look in lookups:
   w=int(look[v])
   if ids[w]<0:ids[w]=n;todo.append(w)
 fixed=sum(int(lookups[2][v])==v for v in todo)
 orbits.append({'size':len(todo),'S_fixed':fixed})
print('Exact source character orbits:',len(orbits),flush=True)
Jimages=E['joint_R8_images'].reshape(289,8,8)[chosen]
recs=json.loads((here/'build_coupled_cubic_two_layer.json').read_text())['character_orbits']
def vec8(k):
 a=[]
 for _ in range(8):a.append(k%3);k//=3
 return np.array(a,dtype=np.int16)
records=[]
for r in recs:
 seed=r['character'];lam=vec8(seed)
 targetchars={tuple(A@lam%3) for A in D['actions']}
 support=set()
 for targetchar in targetchars:
  for i in range(8):
   a=Jimages[:,i,:]@targetchar%3;k=int(a@powers)
   if k:support.add(int(ids[k]))
 record={'target_character':seed,'target_orbit_size':r['orbit_size'],
  'source_support_size':sum(orbits[j]['size'] for j in support),
  'source_S_fixed_count':sum(orbits[j]['S_fixed'] for j in support),
  'source_orbits':[orbits[j] for j in sorted(support)]}
 records.append(record)
ranked=sorted((r for r in records if r['source_S_fixed_count']),key=lambda r:(r['source_support_size'],r['target_orbit_size'],r['target_character']))
print('Target factors with harmonic fixed-character support:',len(ranked),flush=True)
for r in ranked[:20]:print(r,flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),coords=C,chosen=np.array(chosen),
 X=ops[0],Y=ops[1],S=ops[2],R=ops[3])
Path(__file__).with_suffix('.json').write_text(json.dumps({'source_character_orbits':orbits,
 'target_factors':records,'ranked_candidates':ranked},indent=2)+'\n')
