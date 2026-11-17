#!/usr/bin/env python3
"""Literal rank73 faithful-homology map onto the compact parity target."""
import numpy as np,json
from pathlib import Path
import modular_quaternion_compact_setup as C
D=Path(__file__).parent
F=json.loads((D/'translation_cover_basis.json').read_text());T=json.loads((D/'translation_quaternion_homology.json').read_text())
H=np.load(D/'translation_quaternion_homology.npz');Q=np.load(D/'modular_quaternion_compact_setup.npz')
period9=np.array([[sum(1 if x==j else -1 if x==-j else 0 for x in w) for w in C.D['schreier_basis']] for j in (1,2)],dtype=np.int16)%3
period=period9@Q['quotient_section'][:9]%3
R,p=C.rref(period);free=[j for j in range(14) if j not in p];W=np.zeros((14,12),dtype=np.int16);W[free]=np.eye(12,dtype=np.int16);W[p]=-R[:,free]%3
G=Q['actual_generator_matrices'];z=np.eye(14,dtype=np.int16)
for _ in range(6):z=z@G[2]%3
assert np.array_equal(z@W%3,-W%3)

def inv(w):return tuple(-j for j in reversed(w))
def sub(w,gs):return C.S.red(x for j in w for x in (gs[j-1] if j>0 else inv(gs[-j-1])))
values=[]
for w in T['schreier_basis_K3']:
 wE=sub(w,F['standard_basis_E']);v=C.wordlie(C.S.rewrite(wE));values.append(Q['quotient_projection']@v%3)
Theta=np.stack(values,axis=1);assert len(C.rref(Theta)[0])==12
assert not np.any(period@Theta%3)
assert not np.any(Theta@(np.eye(73,dtype=np.int16)+H['deck_matrices'][4])%3)
assert np.array_equal(W@Theta[free]%3,Theta)
print('PASS actual14x73 homology map, rank12, annihilates every positive central-quaternion summand',flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),period_map=period,T_image_basis=W,central_involution=z,literal_T_homology_map=Theta)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Actual map from the73 displayed T73 basis words to compact parity target; factors through faithful36-dimensional quaternion summand',
 'T_image_dimension':12,'source_faithful_dimension':36,'surface_order':'32*3^14','characteristic_faithful_common_quotient_order':'288*3^36',
 'period_map':period.tolist(),'actual_homology_map':Theta.tolist()},indent=2)+'\n')
