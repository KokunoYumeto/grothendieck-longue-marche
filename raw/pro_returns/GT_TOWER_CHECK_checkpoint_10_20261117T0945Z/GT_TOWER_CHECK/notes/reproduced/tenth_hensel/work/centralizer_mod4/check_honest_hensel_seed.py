#!/usr/bin/env python3
"""An exact integral affine point with full canonical defect zero modulo4."""
from pathlib import Path
import json
import numpy as np
from sympy import Matrix

HERE=Path(__file__).resolve().parent
s=(HERE/'check_mod4_canonical_lift.py').read_text()
env={'__name__':'honest_seed_prefix','__file__':str(HERE/'honest_seed_prefix.py')}
exec(compile(s.split("S=model['s_action']",1)[0],str(HERE/'check_mod4_canonical_lift.py'),'exec'),env)
lat=np.load(HERE/'check_integral_affine_lattice.npz')
point=lat['particular_old_mod4'].astype(np.int64)
K=lat['kernel_old_mod4'].astype(np.int64)
d0=env['defect'](point[97:194],point[194:])
e0=env['embedding'](d0)
assert not np.any(e0%2)
images=lat['first_transition_tangent'].astype(np.int64)
good,coeff,_,piv=env['solve2'](images.T,e0//2)
assert good and len(piv)==8
answer=(point+2*coeff@K)%4
defect=env['defect'](answer[97:194],answer[194:])
assert env['integral'](defect)
hnf=env['Hi']*Matrix(defect.tolist());assert all(x.q==1 for x in hnf)
exact=json.loads((HERE/'integral_affine_lattice_exact.json').read_text())
exact_point=[int(x) for x in exact['particular']]
exact_kernel=[[int(x) for x in row] for row in exact['kernel']]
new_point=[a+2*sum(int(coeff[i])*exact_kernel[i][j] for i in range(96)) for j,a in enumerate(exact_point)]
system=np.load(HERE/'check_integral_affine_system.npz')
for row,b in zip(system['free_matrix'],system['free_rhs']):assert sum(int(x)*y for x,y in zip(row,new_point))==int(b)
for row,b in zip(system['torsion_matrix'],system['torsion_rhs']):assert (sum(int(x)*y for x,y in zip(row,new_point))-int(b))%2==0
np.savez_compressed(Path(__file__).with_suffix('.npz'),honest_point_old_mod4=answer,
    correcting_parameters=coeff,uncorrected_defect=d0,corrected_defect=defect,
    integer_hnf_coordinates=np.array([int(x) for x in hnf],dtype=np.int64))
(HERE/'honest_hensel_seed_exact.json').write_text(json.dumps({'point':[str(x) for x in new_point],
    'kernel_file':'integral_affine_lattice_exact.json','parameter_support':np.flatnonzero(coeff).tolist()},indent=2)+'\n')
out={'scope':'An exact integral affine solution with the full coefficient-four canonical cusp defect zero.',
     'honest_tangent_rank':8,'selected_parameter_support':np.flatnonzero(coeff).tolist(),
     'integral_free_equations_exact':True,'binary_torsion_equations_exact':True,
     'full_canonical_defect_mod4_zero':True,'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS honest integral affine seed, binary torsion conditions, and full canonical defect mod4.',flush=True)
print('Selected honest parameter support',np.flatnonzero(coeff).tolist(),flush=True)
