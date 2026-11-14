#!/usr/bin/env python3
"""Exact full tangent ranks for the class-two three-adic cusp lifting.

Combines the 97-dimensional homology derivative, the central rank 4648,
the order-three centralizer transgression, and the five quadratic equations.
The resulting derivative rank is 4753 for every retained CM-fibre witness.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_class2_refinement.py'))
v=d['v'];n=97;S,R=d['S'],d['R'];T=S@R%3;I=np.eye(n,dtype=np.int64)
P=np.load(here/'de_affine_fibres.npz')['p3_image_parameters'];B,A=P[:n],P[n:]
forms=np.stack(d['invariant_matrices']);ts=np.stack(d['tau_s'],axis=1);tr=np.stack(d['tau_r'],axis=1);tt=(ts@R+tr)%3
quad=np.stack([2*B.T@f@(T-I)@A%3 for f in forms])
points=json.loads((here/'de_fibre_three.json').read_text())['records']
cert=[r for r in d['cert'] if 'mod6_beta_cycles' in r];rows=[]
for j,(point,rec) in enumerate(zip(points,cert)):
    b=v['representative'](rec['beta']);bi=v['act'](v['inverse'](b),v['C'])[v['chords']]%3
    bv=np.array([rec['mod6_beta_cycles'].get(str(i),0) for i in range(n)])
    tb=np.zeros((8,n),dtype=np.int64)
    for letter in d['d']['Bpaths'][b]:
        if letter==0:ag,tg=S,ts
        elif letter==1:ag,tg=R,tr
        else:ag=R@R%3;tg=-tr@ag%3
        tb=(tb@ag+tg)%3
    ts0=(tb@(S-I)@bi+ts@bi+np.stack([bv@f@(S-I) for f in forms]))%3
    linear=(ts0@(A-B)-tt@A)%3;x=np.array(point['parameters'])
    jac=(linear+np.einsum('kij,j->ki',quad+quad.transpose(0,2,1),x))%3
    rank=len(d['rref'](np.column_stack((d['variation_r'],jac)))[1])
    assert rank==8
    row={'certificate_index':j,'missing_coset':bool(rec['missing_coset']),
         'homology_derivative_rank':97,'central_derivative_rank':4648,
         'remaining_derivative_rank':rank,'full_derivative_rank':97+4648+rank}
    rows.append(row);print(json.dumps(row),flush=True)
out={'class_two_three_adic_dimension':4753,'all_full_derivatives_surjective':True,
     'records':rows,'scope':'Exact tangent certificate for the successive class-two three-adic Hensel argument. This tower kills gamma3(N_B) and is not cofinal in the full profinite group.'}
(here/'de_fibre_three_smooth.json').write_text(json.dumps(out,indent=2)+'\n')
