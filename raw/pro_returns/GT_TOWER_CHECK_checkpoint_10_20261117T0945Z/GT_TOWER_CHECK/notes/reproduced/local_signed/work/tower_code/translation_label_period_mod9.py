#!/usr/bin/env python3
"""All finite translation-normalizer labels versus the actual period mod3.
Exact integer deck matrices, all48 linear label maps, all648 SL2 mod9
periods; quotient conditions use Smith-style row/column reduction mod9.
"""
import numpy as np,itertools,json
from pathlib import Path
D=Path(__file__).parent;F=json.loads((D/'translation_cover_basis.json').read_text())
def exponent(w):return np.array([sum(1 if j==i else -1 if j==-i else 0 for j in w) for i in range(1,11)],dtype=np.int16)
ha,hb=[np.stack([exponent(w) for w in g],axis=1) for g in F['deck_automorphisms']]
I10=np.eye(10,dtype=np.int16);I8=np.eye(8,dtype=np.int16)
assert np.array_equal(ha@ha@ha,I10) and np.array_equal(hb@hb@hb,I10) and np.array_equal(ha@hb,hb@ha)
labels=[tuple(p) for p in F['standard_peripheral_labels']]+[tuple(F['last_peripheral_label'])];li={q:i for i,q in enumerate(labels)}
def pmatrix(nu):
 P=np.empty((8,8),dtype=np.int16)
 for i,p in enumerate(labels[:8]):
  j=li[tuple(nu@np.array(p)%3)];P[:,i]=I8[:,j] if j<8 else -np.ones(8,dtype=np.int16)
 return P
H={}
for a in range(3):
 for b in range(3):H[a,b]=np.linalg.matrix_power(ha,a)@np.linalg.matrix_power(hb,b)
nus=[np.array(t,dtype=np.int16).reshape(2,2) for t in itertools.product(range(3),repeat=4) if (t[0]*t[3]-t[1]*t[2])%3]
Cs=[np.array(t,dtype=np.int16).reshape(2,2) for t in itertools.product(range(9),repeat=4) if (t[0]*t[3]-t[1]*t[2])%9==1]
assert len(nus)==48 and len(Cs)==648
Cs=np.array(Cs);J=np.array([[0,1],[1,0]],dtype=np.int16)

def diagonalize(A):
 A=A.copy()%9;U=np.eye(len(A),dtype=np.int16);V=np.eye(A.shape[1],dtype=np.int16);r=0;diag=[]
 while r<min(A.shape):
  unit=np.argwhere((A[r:,r:]%3)!=0)
  if len(unit):i,j=unit[0]+r;val=1
  else:
   nonzero=np.argwhere(A[r:,r:]!=0)
   if not len(nonzero):break
   i,j=nonzero[0]+r;val=3
  A[[r,i]]=A[[i,r]];U[[r,i]]=U[[i,r]];A[:,[r,j]]=A[:,[j,r]];V[:,[r,j]]=V[:,[j,r]]
  scalar=pow(int(A[r,r]//val),-1,9);A[r]=A[r]*scalar%9;U[r]=U[r]*scalar%9
  assert A[r,r]==val
  for i in range(len(A)):
   if i==r:continue
   assert A[i,r]%val==0;k=int(A[i,r]//val);A[i]=(A[i]-k*A[r])%9;U[i]=(U[i]-k*U[r])%9
  for j in range(A.shape[1]):
   if j==r:continue
   assert A[r,j]%val==0;k=int(A[r,j]//val);A[:,j]=(A[:,j]-k*A[:,r])%9;V[:,j]=(V[:,j]-k*V[:,r])%9
  diag.append(val);r+=1
 return A,U,V,diag
records=[];certs=[]
for nu in nus:
 P=pmatrix(nu);hs=[H[tuple(nu[:,j])] for j in (0,1)]
 assert all(np.array_equal(P@h[2:,2:],hh[2:,2:]@P) for h,hh in zip((ha,hb),hs))
 L=[]
 for h in hs:L.append(np.kron(I8-h[2:,2:],np.eye(2,dtype=np.int16)))
 L=np.vstack(L)%9;A,U,V,diag=diagonalize(L)
 assert diag==[1]*12+[3]*4
 assert np.array_equal(U@L%9@V%9,A)
 rhs=np.concatenate([(np.einsum('ij,kjl->kil',h[2:,:2],Cs)-P@hh[2:,:2]).reshape(648,16) for h,hh in zip(hs,(ha,hb))],axis=1)%9
 z=rhs@U.T%9;good=np.logical_and(~np.any(z[:,12:16]%3,axis=1),~np.any(z[:,16:],axis=1));ids=np.flatnonzero(good)
 expected=np.all(Cs%3==J@nu@J%3,axis=(1,2))
 # The test below is the precise claim to establish, not a presupposed filter.
 assert np.array_equal(good,expected),(nu.tolist(),len(ids),int(np.sum(expected)))
 records.append({'label_matrix':nu.tolist(),'determinant_mod3':int(nu[0,0]*nu[1,1]-nu[0,1]*nu[1,0])%3,'periods_mod9':[Cs[j].tolist() for j in ids],
                 'surviving_period_count':len(ids),'homology_B_fibre_order':81 if len(ids) else 0})
 certs.append((L,U,V,A))
print('PASS all48 label maps and648 periods: exactly24 labels, each with27 period lifts',flush=True)
print('PASS exact relation nu=J*(ordinary upstairs period mod3)*J; each period has81 pointpush lifts',flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),label_matrices=np.array(nus),period_matrices=Cs,
 coefficient_matrices=np.array([c[0] for c in certs]),row_operations=np.array([c[1] for c in certs]),column_operations=np.array([c[2] for c in certs]),diagonals=np.array([c[3] for c in certs]))
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Complete actual homology-mod9 normalizer census for the literal nine-point translation subgroup, modulo actual deck translations on labels',
 'label_candidates':48,'period_candidates':648,'checked_pairs':48*648,'surviving_label_count':sum(r['surviving_period_count']>0 for r in records),
 'normalizer_order':9*24*27*81,'label_period_relation':'nu=J C_mod3 J in original downstairs deck labels', 'records':records},indent=2)+'\n')
