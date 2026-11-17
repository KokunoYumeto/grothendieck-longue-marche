#!/usr/bin/env python3
"""Exact mod9-to-mod3 centralizer stabilization of the translation subgroup."""
import translation_cover_basis as F
import numpy as np,json,itertools
from pathlib import Path
D=np.load(Path(__file__).with_name('translation_class2_compare.npz'))
old=json.loads(Path(__file__).with_name('translation_class2_compare.json').read_text())
H=np.array([np.array([F.exponent(w) for w in g],dtype=np.int64).T for g in F.deck])
assert all(np.array_equal(M@M@M,np.eye(10,dtype=np.int64)) for M in H)
assert np.array_equal(H[0]@H[1],H[1]@H[0])
assert all(np.array_equal(M[:2,:2],np.eye(2,dtype=np.int64)) and not np.any(M[:2,2:]) for M in H)
P=H[:,2:,2:];t=H[:,2:,:2]
rows=[]
for j in range(16):
 B=np.zeros((8,2),dtype=np.int64);B.reshape(-1)[j]=1
 rows.append(np.concatenate([((np.eye(8,dtype=np.int64)-M)@B).reshape(-1) for M in P]))
L=np.array(rows,dtype=np.int16)%3

def rref(A):
 A=A.copy()%3;r=0;piv=[]
 for c in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,c])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*(1 if A[r,c]==1 else 2)%3
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,c,None]*A[r])%3
  piv.append(c);r+=1
  if r==len(A):break
 return A[:r],piv
R,piv=rref(L);free=[j for j in range(32) if j not in piv]
def obstruction(v):return (v[free]-v[piv]@R[:,free])%3
NK=D['geometric_normalizer_image'];NK,NP=rref(NK);NF=[j for j in range(16) if j not in NP]
def geometric(v):return not np.any((v[NF]-v[NP]@NK[:,NF])%3)
records=[]
for rec in old['records']:
 C3=np.array(rec['closed_matrix']);assert np.array_equal(C3,np.eye(2,dtype=np.int16))
 B0=np.array(rec['pointpush_matrix'],dtype=np.int64)
 corrections=[(np.eye(8,dtype=np.int64)-M)@B0 for M in P]
 assert all(not np.any(v%3) for v in corrections)
 good=[]
 for a,b,c in itertools.product(range(3),repeat=3):
  A=np.array([[a,b],[c,-a]],dtype=np.int64)
  C9=(np.eye(2,dtype=np.int64)+3*A)%9
  assert (C9[0,0]*C9[1,1]-C9[0,1]*C9[1,0])%9==1
  rhs=np.concatenate([(t[i]@A-corrections[i]//3).reshape(-1) for i in range(2)])%3
  if not np.any(obstruction(rhs)):good.append(A.tolist())
 allowed=bool(good);expected=geometric(B0.reshape(-1))
 records.append({'pointpush_matrix_mod3':B0.tolist(),'lifts_mod9':allowed,
                 'geometric_normalizer_image':bool(expected),'closed_corrections_mod3':good})
 assert allowed==expected
print('PASS exact integral translation deck matrices and modulo9 equations',flush=True)
print('Pure homological centralizer images modulo3:',len(records),flush=True)
print('Images admitting a symplectic modulo9 lift:',sum(r['lifts_mod9'] for r in records),flush=True)
print('Exactly the geometric N0 level-three image, dimension:',len(NK),flush=True)
print('Numbers of closed symplectic corrections:',sorted(set(len(r['closed_corrections_mod3']) for r in records if r['lifts_mod9'])),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Exact finite centralizer image, not complete C3² conjugacy recognition',
 'mod3_candidates':len(records),'mod9_liftable':sum(r['lifts_mod9'] for r in records),
 'geometric_image_dimension':len(NK),'records':records},indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),integral_translation_matrices=H,
 lift_equation_matrix=L,lift_reduced_rows=R,lift_pivots=np.array(piv),
 geometric_normalizer_basis=NK)
