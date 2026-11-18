"""Compute the exact total quotient order using a nilpotent matrix algebra.
Every product of five augmentation matrices is zero, so log/exp and BCH
over F5 are valid through degree four. The generated Lie algebra has
the same cardinality as the generated five-group.
"""
from pathlib import Path
import json,itertools
import numpy as np
r=Path(__file__).resolve().parent;d=json.loads((r/'s3_nonnilpotent.json').read_text())
n=10;p=5;pairs=list(itertools.combinations(range(n),2));I=np.eye(n,dtype=np.int64)
def ext(A):return np.array([[(A[i,k]*A[j,l]-A[i,l]*A[j,k])%p for k,l in pairs] for i,j in pairs],dtype=np.int64)
def dext(N):return np.array([[(N[i,k]*(j==l)+(i==k)*N[j,l]-N[i,l]*(j==k)-(i==l)*N[j,k])%p for k,l in pairs] for i,j in pairs],dtype=np.int64)
logs=[]
for h in d['H_Schreier_generators']:
 A=np.array(h['linear'],dtype=np.int64);B=np.array(h['central'],dtype=np.int64)
 M=np.block([[A,np.zeros((10,45),dtype=np.int64)],[B,ext(A)]])
 D=(M-np.eye(55,dtype=np.int64))%5;L=np.zeros_like(D);power=np.eye(55,dtype=np.int64)
 for j in range(1,6):
  power=power@D%5
  if j<5:L=(L+((-1)**(j+1))*pow(j,-1,5)*power)%5
  else:assert not np.any(power)
 assert np.array_equal(L[10:,10:],dext(L[:10,:10]))
 logs.append(np.concatenate([L[:10,:10].reshape(-1),L[10:,:10].reshape(-1)]))
def unpack(v):return v[:100].reshape(10,10),v[100:].reshape(45,10)
def bracket(v,w):
 N,B=unpack(v);M,C=unpack(w);assert not np.any((N@M-M@N)%5)
 return np.concatenate([np.zeros(100,dtype=np.int64),((dext(N)@C+B@M-dext(M)@B-C@N)%5).reshape(-1)])
basis=[];pivots=[]
def insert(v):
 v=v.copy()%5
 for pivot,row in zip(pivots,basis):v=(v-v[pivot]*row)%5
 nz=np.nonzero(v)[0]
 if not len(nz):return False
 pivot=int(nz[0]);v=v*pow(int(v[pivot]),-1,5)%5
 # Append only; preceding pivots remain zero, sufficient for elimination.
 pivots.append(pivot);basis.append(v);return True
for v in logs:insert(v)
initial=len(basis);generators=[v.copy() for v in basis]
i=0
while i<len(basis):
 v=basis[i];i+=1
 for w in generators:insert(bracket(v,w))
dim=len(basis)
for v in basis:
 for w in basis:
  z=bracket(v,w)
  for pivot,row in zip(pivots,basis):z=(z-z[pivot]*row)%5
  assert not np.any(z)
def span(vs):
 rows=[];ps=[]
 for v in vs:
  v=v.copy()%5
  for q,row in zip(ps,rows):v=(v-v[q]*row)%5
  nz=np.nonzero(v)[0]
  if len(nz):
   q=int(nz[0]);rows.append(v*pow(int(v[q]),-1,5)%5);ps.append(q)
 return rows
lower=[dim];cur=basis
while cur:
 cur=span(bracket(v,w) for v in cur for w in basis)
 lower.append(len(cur))
assert lower[-1]==0 and len(lower)<=5
out={'verified':True,'nilpotent_augmentation_index_at_most':5,'characteristic':5,
 'lower_central_dimensions':lower,'exact_nilpotency_class':len(lower)-1,
 'initial_log_span_dimension':initial,'generated_Lie_algebra_dimension':dim,
 'five_kernel_order':str(5**dim),'total_order':str(9*5**dim),
 'basis_pivots':pivots,'Lie_basis':[v.tolist() for v in basis],
 'proof_condition':'All N_iN_j=0 and all (Lambda²A_i−1)(Lambda²A_j−1)(Lambda²A_k−1)=0; block-triangular structure implies any product of5 augmentation matrices is0.'}
(r/'s3_group_order.json').write_text(json.dumps(out,indent=2)+'\n')
print('lower central dimensions',lower)
print('initial logarithm span',initial,'Lie closure dimension',dim,'T order',9*5**dim)
