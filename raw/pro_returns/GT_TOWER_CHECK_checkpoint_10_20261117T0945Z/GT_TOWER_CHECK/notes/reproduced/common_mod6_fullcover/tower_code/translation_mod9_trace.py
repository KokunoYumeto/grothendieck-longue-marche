#!/usr/bin/env python3
"""All81 Bockstein corrections and three actual geometric generators."""
import translation_cover_basis as F
import translation_mod9_centralizer as C
import numpy as np,itertools,json
from pathlib import Path
u=np.array([2,1,1,0,2,2,1,0],dtype=np.int64)
v=np.array([1,2,1,2,0,2,0,1],dtype=np.int64)
correction_map={}
for a,b,c,d in itertools.product(range(3),repeat=4):
 A=np.array([[a,b],[c,d]],dtype=np.int64)
 obs=C.obstruction(np.concatenate([(t@A).reshape(-1) for t in C.t])%3)
 key=tuple(map(int,obs));assert key not in correction_map
 correction_map[key]=A
assert len(correction_map)==81
records=[]
for alpha,beta,gamma,delta in itertools.product(range(3),repeat=4):
 B=np.stack(((alpha*u+gamma*v)%3,(beta*u+delta*v)%3),axis=1)
 defects=[(np.eye(8,dtype=np.int64)-P)@B for P in C.P]
 assert all(not np.any(d%3) for d in defects)
 rhs=np.concatenate([(d//3).reshape(-1) for d in defects])%3
 obs=C.obstruction(rhs)
 A=correction_map[tuple(map(int,obs))]
 expected=np.array([[2*alpha+gamma,2*beta+delta],[alpha+gamma,beta+delta]],dtype=np.int64)%3
 assert np.array_equal(A,expected)
 tr=int(np.trace(A)%3)
 assert tr==(2*alpha+beta+gamma+delta)%3
 records.append({'coordinates':[alpha,beta,gamma,delta],
                 'B_mod3':B.tolist(),'unique_closed_correction':A.tolist(),'trace':tr})
assert sum(r['trace']==0 for r in records)==27
print('PASS all81 residues obey the exact linear Bockstein correction; trace cuts27',flush=True)

def matrix(words):return np.array([F.exponent(w) for w in words],dtype=np.int64).T
U,L=map(matrix,F.normalizer)
Ui=matrix(F.restricted(((1,),(2,-1))))
assert np.array_equal(U@Ui,np.eye(10,dtype=np.int64))
named=[('U_E^3',np.linalg.matrix_power(U,3)),('L_E^3',np.linalg.matrix_power(L,3)),
       ('U_E L_E^3 U_E^-1',U@np.linalg.matrix_power(L,3)@Ui)]
geometric=[]
for name,M in named:
 assert np.array_equal(M[2:,2:]%3,np.eye(8,dtype=np.int64))
 assert np.array_equal(M[:2,:2]%3,np.eye(2,dtype=np.int64))
 b=M[2:,:2]%3
 matches=[r for r in records if np.array_equal(np.array(r['B_mod3']),b)]
 assert len(matches)==1;r=matches[0];assert r['trace']==0
 closed=(M[:2,:2]-np.eye(2,dtype=np.int64))//3%3
 assert np.array_equal(closed,np.array(r['unique_closed_correction']))
 geometric.append({'word':name,'coordinates':r['coordinates'],'closed_correction':closed.tolist()})
 print(name,'coordinates',r['coordinates'],'closed correction',closed.tolist(),flush=True)
assert len(C.rref(np.array([r['coordinates'] for r in geometric]))[0])==3
print('PASS three literal normalizer words span the entire27-element geometric image',flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),u=u,v=v,
 all_coordinates=np.array([r['coordinates'] for r in records]),
 all_B=np.array([r['B_mod3'] for r in records]),
 all_corrections=np.array([r['unique_closed_correction'] for r in records]),
 geometric_integral_matrices=np.array([M for name,M in named]))
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Complete81-residue Bockstein formula and actual geometric words',
 'records':records,'geometric_generators':geometric},indent=2)+'\n')
