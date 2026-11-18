"""Independent group-order check by unitriangular collection, without logs.
Construct a common invariant flag, then close a pivot-normalized generating
sequence under actual matrix commutators. Its normal forms have 5^40 elements.
"""
import json,itertools,time
from pathlib import Path
import numpy as np
r=Path(__file__).resolve().parent;t=time.time();d=json.loads((r/'s3_nonnilpotent.json').read_text())
I=np.eye(55,dtype=np.int64);pairs=list(itertools.combinations(range(10),2))
def rref(A):
 A=A.copy()%5;rr=0;pivs=[]
 for col in range(A.shape[1]):
  j=next((j for j in range(rr,len(A)) if A[j,col]),None)
  if j is None:continue
  A[[rr,j]]=A[[j,rr]];A[rr]=A[rr]*pow(int(A[rr,col]),-1,5)%5
  for j in range(len(A)):
   if j!=rr and A[j,col]:A[j]=(A[j]-A[j,col]*A[rr])%5
  pivs.append(col);rr+=1
  if rr==len(A):break
 return A[:rr],pivs
def ns(A):
 R,pivs=rref(A);free=[j for j in range(A.shape[1]) if j not in pivs];vs=[]
 for j in free:
  v=np.zeros(A.shape[1],dtype=np.int64);v[j]=1
  for h,i in enumerate(pivs):v[i]=-R[h,j]%5
  vs.append(v)
 return np.array(vs,dtype=np.int64).reshape((-1,A.shape[1])).T
def inv(A):return rref(np.column_stack([A,I]))[0][:,55:]
def power(A,n):
 B=I
 while n:
  if n%2:B=B@A%5
  A=A@A%5;n//=2
 return B
def full(g):
 A=np.array(g['linear'],dtype=np.int64);B=np.array(g['central'],dtype=np.int64)
 E=np.array([[(A[i,k]*A[j,l]-A[i,l]*A[j,k])%5 for k,l in pairs] for i,j in pairs],dtype=np.int64)
 return np.block([[A,np.zeros((10,45),dtype=np.int64)],[B,E]])
Hs=[full(h) for h in d['H_Schreier_generators']];Ds=[(M-I)%5 for M in Hs]
W=np.zeros((55,0),dtype=np.int64);basis=[];dims=[]
for step in range(1,6):
 left=ns(W.T).T
 new=ns(np.vstack([left@D%5 for D in Ds]))
 oldrank=len(basis)
 for v in new.T:
  test=np.column_stack(basis+[v])
  if len(rref(test)[1])>len(basis):basis.append(v)
 W=np.column_stack(basis);dims.append(W.shape[1])
 if W.shape[1]==55:break
assert W.shape==(55,55)
Wi=inv(W);assert np.array_equal(Wi@W%5,I)
Gs=[Wi@M@W%5 for M in Hs]
for M in Gs:assert not np.any(np.tril(M-I)) and np.array_equal(power(M,5),I)
positions=[(i,i+j) for j in range(1,55) for i in range(55-j)]
pos_index={pos:j for j,pos in enumerate(positions)}
records={};derivations=[]
def insert(M,origin):
 M=M.copy()
 for pos in sorted(records,key=pos_index.get):
  ps=records[pos]['powers'];a=int(M[pos])
  if a:M=M@ps[(-a)%5]%5
 pos=next(((i,j) for i,j in positions if M[i,j]),None)
 if pos is None:
  assert np.array_equal(M,I);return False
 a=int(M[pos]);M=power(M,pow(a,-1,5));assert M[pos]==1
 assert np.array_equal(power(M,5),I)
 assert pos not in records
 records[pos]={'matrix':M,'powers':[I,M,M@M%5,power(M,3),power(M,4)],'origin':origin}
 return True
for j,M in enumerate(Gs):insert(M,{'original_schreier_generator':j})
initial=len(records)
while True:
 keys=sorted(records,key=pos_index.get);changed=False
 for i,pos in enumerate(keys):
  a=records[pos]
  for old in keys[:i]:
   b=records[old]
   changed=insert(a['matrix']@b['matrix']@a['powers'][4]@b['powers'][4]%5,
                  {'commutator_pivots':[pos,old]}) or changed
 if not changed:break
pivots=sorted(records,key=pos_index.get)
gens=[records[pos]['matrix'] for pos in pivots]
powers=[records[pos]['powers'] for pos in pivots]
derivations=[records[pos]['origin'] for pos in pivots]
for M in Gs:assert not insert(M,{'final_original':True})
# Closure under actual commutators and fifth powers is the collection
# criterion for a generating sequence in increasing triangular pivot order.
# Multiplication can only change entries strictly later than the operands'
# leading pivots, so reduction and collection terminate uniquely.
for i in range(len(gens)):
 for j in range(i):assert not insert(gens[i]@gens[j]@powers[i][4]@powers[j][4]%5,{'final_check':[i,j]})
dim=len(gens);assert dim==json.loads((r/'s3_group_order.json').read_text())['generated_Lie_algebra_dimension']
out={'verified':True,'method':'actual matrix commutator collection; no logarithms',
 'invariant_flag_dimensions':dims,'initial_collecting_generators':initial,'closed_collecting_generators':dim,
 'five_kernel_order':str(5**dim),'total_quotient_order':str(9*5**dim),
 'pivots':pivots,'derivations':derivations,'change_of_basis':W.tolist(),
 'collecting_generators':[M.tolist() for M in gens],'seconds':time.time()-t}
(r/'s3_order_collect.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS independent unitriangular collection:',dim,'cyclic order5 factors; T order',9*5**dim)
print('flag dimensions',dims,'seconds',time.time()-t)
