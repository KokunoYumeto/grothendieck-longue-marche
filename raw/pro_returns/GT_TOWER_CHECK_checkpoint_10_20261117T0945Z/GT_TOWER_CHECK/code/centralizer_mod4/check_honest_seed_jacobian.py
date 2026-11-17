#!/usr/bin/env python3
"""Direct full-canonical Jacobian differences at the honest integral seed."""
from pathlib import Path
import json,hashlib
import numpy as np
HERE=Path(__file__).resolve().parent
src=(HERE/'check_mod4_canonical_lift.py').read_text()
env={'__name__':'honest_jacobian_prefix','__file__':str(HERE/'honest_jacobian_prefix.py')}
exec(compile(src.split("S=model['s_action']",1)[0],str(HERE/'check_mod4_canonical_lift.py'),'exec'),env)
lat=np.load(HERE/'check_integral_affine_lattice.npz')
seed=np.load(HERE/'check_honest_hensel_seed.npz')['honest_point_old_mod4'].astype(np.int64)
K=lat['kernel_old_mod4'].astype(np.int64)
target=np.load(HERE.parents[0]/'tower_code/check_integral_frame_jacobian.npz')
E=target['free_embedding'].astype(np.int64)
d0=env['defect'](seed[97:194],seed[194:])
assert env['integral'](d0)
rows=[];raw=[]
for i,k in enumerate(K):
    z=(seed+2*k)%4
    delta=env['defect'](z[97:194],z[194:])-d0
    e=env['embedding'](delta)
    assert not np.any(e%2)
    good,coord,_,_=env['solve2'](E.T,e//2)
    assert good
    rows.append(coord);raw.append(delta)
    if i%16==15: print('Direct honest-seed differences',i+1,flush=True)
D=np.array(rows,dtype=np.int64)
q=target['quadratic_diagonal'].astype(np.int64)
J=(D+q)%2
_,_,_,piv=env['solve2'](J.T,np.zeros(8,dtype=np.int64))
assert len(piv)==8
same=np.array_equal(D,target['finite_difference'])
print('PASS direct honest-seed Jacobian rank8; same as prior tangent:',same,flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),finite_difference=D,jacobian=J,
 independent_directions=np.array(piv,dtype=np.int64),raw_defect_differences=np.array(raw,dtype=np.int64),
 seed=seed,seed_defect=d0,free_embedding=E,quadratic_diagonal=q)
out={'scope':'Direct actual full-canonical finite differences at the honest integral seed, independently of the earlier nonintegral affine point.',
 'directions':96,'jacobian_rank':len(piv),'independent_directions':piv,
 'matches_prior_tangent':bool(same),'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
