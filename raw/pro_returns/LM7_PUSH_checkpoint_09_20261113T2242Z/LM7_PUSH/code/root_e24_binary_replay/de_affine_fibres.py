#!/usr/bin/env python3
"""Complete linear parameter spaces above each admissible CM matrix pair.

Computes cusp-preserving conjugator changes, the changes which fix both
generator images, and finite inner-conjugacy spaces.  Only conjugations by
powers of t are asserted to preserve liftability to every finer quotient.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_verify_cm.py'))
n=97;I=np.eye(n,dtype=np.int64);S=d['act'](d['ss'],d['C'])[d['chords']];R=d['act'](d['rr'],d['C'])[d['chords']]
L=d['L'];c=d['ct'][d['chords']];rref=d['rref'];data={};out=[]
def kernel(A,p):
    RR,pp=rref(A,p);free=[j for j in range(A.shape[1]) if j not in pp]
    K=np.zeros((A.shape[1],len(free)),dtype=np.int64)
    for k,j in enumerate(free):K[j,k]=1;K[pp,k]=-RR[:len(pp),j]%p
    assert not np.any(A@K%p)
    return K
for p in (2,3):
    A=kernel(L,p);cs=kernel(S-I,p);cr=kernel(R-I,p);ct=kernel(S@R-I,p)
    Z=np.block([[cs,np.zeros((n,cr.shape[1]),dtype=np.int64)],
                [np.zeros((n,cs.shape[1]),dtype=np.int64),cr]])
    inner=np.vstack((ct,ct));cusp=np.concatenate((c,c)).reshape(-1,1)%p
    assert not np.any(L@Z%p) and not np.any(L@inner%p) and not np.any(L@cusp%p)
    pp=rref(np.column_stack((Z,A)),p)[1]
    comp=A[:,[j-Z.shape[1] for j in pp if j>=Z.shape[1]]]
    pp2=rref(np.column_stack((Z,cusp,A)),p)[1]
    comp_cusp=A[:,[j-Z.shape[1]-1 for j in pp2 if j>=Z.shape[1]+1]]
    pp3=rref(np.column_stack((Z,inner,A)),p)[1]
    comp_inner=A[:,[j-Z.shape[1]-inner.shape[1] for j in pp3 if j>=Z.shape[1]+inner.shape[1]]]
    qinv=kernel(np.vstack((S-I,R-I)),p).shape[1]
    row={'p':p,'all_affine_conjugator_dimension':A.shape[1],
         's_centralizer_dimension':cs.shape[1],'r_centralizer_dimension':cr.shape[1],
         'distinct_generator_image_dimension':comp.shape[1],
         't_centralizer_in_N_ab_dimension':ct.shape[1],
         'Q_invariants_dimension':qinv,
         'quotient_by_cusp_powers_dimension':comp_cusp.shape[1],
         'quotient_by_all_finite_inner_conjugacies_dimension':comp_inner.shape[1]}
    out.append(row);print(json.dumps(row),flush=True)
    for key,value in {'affine_kernel':A,'centralizer_kernel':Z,'image_parameters':comp,
                      'cusp_power_quotient':comp_cusp,'all_inner_quotient':comp_inner,
                      'finite_inner_space':inner}.items():data[f'p{p}_{key}']=value%p
np.savez_compressed(here/'de_affine_fibres.npz',**data)
result={'fixed_multiplier_mod72':1,'admissible_CM_pairs':24,'rows':out,
        'scope':'Complete affine cusp solutions at fixed admissible matrix pair. Invertibility is an additional condition. The all-finite-inner quotient is a classification only at G_p; no liftability invariance is asserted for centralizers of t without centralizing lifts.'}
(here/'de_affine_fibres.json').write_text(json.dumps(result,indent=2)+'\n')
