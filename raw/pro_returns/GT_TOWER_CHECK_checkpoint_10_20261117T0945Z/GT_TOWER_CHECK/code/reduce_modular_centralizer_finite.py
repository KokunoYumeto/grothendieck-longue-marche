#!/usr/bin/env python3
"""A Q-stable quotient retaining all fifteen modular centralizer exclusions."""
import numpy as np,json
from pathlib import Path
D=np.load(Path(__file__).with_name('check_modular_centralizer_finite.npz'))
rec=json.loads(Path(__file__).with_name('check_modular_centralizer_finite.json').read_text())
Z=D['cycles'];ch=D['chords'];table=D['table'];inv=D['inverses'];Pr=D['obstruction_projection']
# The breadth-first Q enumeration has s=1,r=2.
As=Z[:,table[inv[1],ch]]%3;Ar=D['action_r']
functional=Pr[:,[0,1,5,14,23]].sum(axis=1)%3
obs=[r['obstruction'] for r in rec['records']]
assert all((np.array(o)[[0,1,5,14,23]].sum()%3!=0)==(not r['lifts_to_centralizer']) for o,r in zip(obs,rec['records']))
assert not np.any((Ar-np.eye(97,dtype=np.int16))@functional%3)
def rref(A):
 A=A.copy()%3;r=0;piv=[]
 for c in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,c])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*pow(int(A[r,c]),-1,3)%3
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,c,None]*A[r])%3
  piv.append(c);r+=1
  if r==len(A):break
 return A[:r],piv
W=functional[None,:]
while True:
 W1,piv=rref(np.vstack((W,W@As.T%3,W@Ar.T%3)))
 if len(W1)==len(W):W=W1;break
 W=W1
for A in (As,Ar):assert len(rref(np.vstack((W,W@A.T%3)))[0])==len(W)
print('PASS Q-stable dual detecting module dimension:',len(W),flush=True)
print('Functional on all eighteen commuting base residues:',[int(np.array(o)[[0,1,5,14,23]].sum()%3) for o in obs],flush=True)
print('Actual finite quotient orders: B',f'576*3^{len(W)}','SL2Z',f'1152*3^{len(W)}','Gamma05',f'192*3^{len(W)}',flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),dual_basis=W,functional=functional)
Path(__file__).with_suffix('.json').write_text(json.dumps({'module_dimension':len(W),'B_order':f'576*3^{len(W)}',
 'SL2Z_order':f'1152*3^{len(W)}','Gamma05_order':f'192*3^{len(W)}',
 'functional':functional.tolist(),'dual_basis':W.tolist(),
 'obstruction_values':[int(np.array(o)[[0,1,5,14,23]].sum()%3) for o in obs]},indent=2)+'\n')
