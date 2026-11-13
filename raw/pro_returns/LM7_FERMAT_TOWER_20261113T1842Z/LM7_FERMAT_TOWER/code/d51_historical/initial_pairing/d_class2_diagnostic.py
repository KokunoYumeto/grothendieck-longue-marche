#!/usr/bin/env python3
"""Exact ribbon-graph pairing diagnostic for the fixed finite D50 certificate.

This is the separate order-1080 verification base, not the arithmetic G3.
The copied D50 helper's actual stdout and certificate are retained here.
"""
from pathlib import Path
import contextlib,io,json,runpy,time
import numpy as np

out=Path(__file__).resolve().parent
started=time.time()
capture=io.StringIO()
with contextlib.redirect_stdout(capture):
    e=runpy.run_path(str(out/'d_cm_projective_repair.py'))
(out/'d_cm_projective_repair.out').write_text(capture.getvalue())
n=e['size']; rr=e['rr']; rs=e['rs']; IC=e['IC']; rank=e['rank']
rho=len(IC)
mat=np.zeros((n,rho),dtype=np.int64)
for j,c in enumerate(IC):
    for g,a in c.items():mat[g,j]=a
reps=sorted({min(g,rr[g],rr[rr[g]]) for g in range(n)})
assert len(reps)==n//3
assert not np.any(mat+mat[np.array(rs)])
assert not np.any(mat+mat[np.array(rr)]+mat[np.array([rr[x] for x in rr])])
a=mat[reps];b=mat[[rr[g] for g in reps]]
twice=a.T@b-b.T@a
assert not np.any(twice%2)
omega=twice//2
assert np.array_equal(omega,-omega.T)
cols=[]
for j in range(rho):
    cols.append(sum(1<<i for i in range(rho) if omega[i,j]%2))
assert rank(cols)==146
cert=json.loads((out/'d_cm_projective_repair.json').read_text())
tcols=[int(x,16) for x in cert['certificate']['new_full_kernel_columns']]
T=np.array([[(tcols[j]>>i)&1 for j in range(rho)] for i in range(rho)],dtype=np.int64)
defect=(T.T@(omega%2)@T-omega)%2
bad=[(i,j) for i in range(rho) for j in range(i+1,rho) if defect[i,j]]
dcols=[sum(1<<i for i in range(rho) if defect[i,j]) for j in range(rho)]
summary={
 'scope':'The separate fixed order-1080 D50 finite certificate only.',
 'base_order':n,'homology_rank':rho,'cusp_count':n//e['order'](e['t']),
 'ribbon_pairing_rank_mod2':rank(cols),'compact_homology_rank':146,
 'fixed_repaired_action_pairing_defect_rank':rank(dcols),
 'first_nonzero_defect_position':list(bad[0]) if bad else None,
 'nonzero_upper_triangular_defect_positions':len(bad),
 'elapsed_seconds':round(time.time()-started,3)
}
data={'summary':summary,'pairing_columns_mod2':[hex(x) for x in cols],
      'defect_columns_mod2':[hex(x) for x in dcols],
      'pairing_integer_matrix':omega.tolist()}
(out/'d_class2_diagnostic.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(summary,indent=2))
