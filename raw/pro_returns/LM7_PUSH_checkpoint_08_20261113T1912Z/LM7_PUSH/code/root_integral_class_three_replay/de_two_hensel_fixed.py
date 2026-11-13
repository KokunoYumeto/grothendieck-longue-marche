#!/usr/bin/env python3
"""Check the complete E.15 tangent certificate with multiplier fixed at one.

The full integral Jacobians modulo four were independently recovered by
step-two substitutions in de_two_hensel_tangent.py.  This program removes
the multiplier column, computes the *entire* binary kernel again, and
checks all 24 reduced Smith ranks through valuation one.  It relies on
the primitive norm compression proved in E.15 for the tower consequence.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    e=runpy.run_path(str(here/'de_class2_sixteen_fibres.py'),
                    init_globals={'DE_LOAD_ONLY':True})
n,m,nr=e['n'],e['m'],e['nr']
A=e['A0'][:,:m]
K=e['d']['nullspace'](A)
rank0=m-K.shape[1]
assert (rank0,K.shape[1])==(3927,826)
data=np.load(here/'de_two_hensel_tangent_certificate.npz')
rows=[]
start=time.time()
for ix,record in enumerate(e['records']):
    J=np.zeros((nr,m),dtype=np.uint8)
    J[:,n:m]=e['central']%4
    J[:,:n]=data[f'J4_{ix}_homology_and_multiplier_columns'][:,:n]
    assert np.array_equal(J%2,A)
    JK=e['mm'](J,K,4)
    assert not np.any(JK%2)
    _,piv=e['d']['rref'](np.column_stack((A,JK//2)))
    rank1=len(piv)
    assert rank1==3953
    row={'certificate_index':ix,'missing_coset':record['missing_coset'],
         'fixed_multiplier':1,'domain_dimension':m,
         'binary_kernel_dimension':K.shape[1],
         'jacobian_rank_mod2':rank0,
         'jacobian_rank_through_second_layer':rank1,
         'elementary_divisors_valuation_zero':rank0,
         'elementary_divisors_valuation_one':rank1-rank0}
    rows.append(row)
    print(json.dumps(row),flush=True)
out={'records':rows,'compressed_norm_target_dimension':3953,
     'all_twenty_four_fixed_multiplier_checks_pass':True,
     'elapsed_seconds':round(time.time()-start,3),
     'scope':'Exact fixed-multiplier tangent certificate. Together with the primitive integral norm compression and exponent-sixteen base points in E.15 this proves compatible relative class-two shadows with multiplier one.'}
(here/'de_two_hensel_fixed.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
