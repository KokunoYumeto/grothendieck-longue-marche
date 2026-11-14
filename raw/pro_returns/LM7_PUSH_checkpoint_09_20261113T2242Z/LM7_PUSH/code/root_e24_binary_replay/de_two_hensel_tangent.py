#!/usr/bin/env python3
"""Exact modulo-four integral Jacobians of the full class-two norm system.

First-kind coordinates on the correction group differ from normal ones
by z=v+6*u_i*u_j. Normal-coordinate norm equations have integral quadratic
coefficients: diagonal coefficients divisible by2 and mixed by4. Thus
their Jacobian modulo4 is recovered exactly by step-two differences
modulo8, is independent of the point, and the elementary divisors up to
valuation1 are read from the full binary kernel.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):e=runpy.run_path(str(here/'de_class2_sixteen_fibres.py'),init_globals={'DE_LOAD_ONLY':True})
n=e['n'];m=e['m'];nw=e['nw'];nr=e['nr'];d=e['d'];K=e['K'];A0=e['A0'];rows=[]
points=np.load(here/'de_class2_sixteen_fibres_certificate.npz')
rng=np.random.default_rng(232026);start=time.time();certificates={}
As,Ar,Ar2=e['As'],e['Ar'],e['Ar2']
trS,trR,trR2=map(lambda A:int(np.trace(A)),(As,Ar,Ar2))
assert (trS,trR,trR2)==(-7,-5,-5)
trWS=(trS*trS-n)//2;trWR=(trR*trR-trR2)//2;trWR2=(trR2*trR2-trR)//2
fixedS=(m+trS+trWS)//2
fixedR=(m+trR+trWR+trR2+trWR2)//3
assert (fixedS,fixedR)==(2361,1591)
H=e['H'];s_lattice=np.array([[-2,-1],[3,2]],dtype=np.int64)
assert np.array_equal(H@As,s_lattice@H)
compressed_dimension=fixedS+fixedR+1
for ix,rec in enumerate(e['records']):
    F,direct,S=e['setup'](rec);zero=np.zeros(nw,dtype=np.int64);f0=F(zero)
    J=np.zeros((nr,nw),dtype=np.uint8);J[:,n:m]=e['central']%4
    for j in list(range(n))+[m]:
        u=zero.copy();u[j]=2;delta=(F(u)-f0)%8;assert not np.any(delta%2);J[:,j]=delta//2
    assert np.array_equal(J%2,A0)
    point=points[f'correction_{ix}'];assert not np.any(F(point)%8)
    for check in range(5):
        u=rng.integers(0,2,size=nw)
        delta=(F(point+2*u)-F(point))%8
        assert np.array_equal(delta,2*(J.astype(np.int64)@u%4))
    JK=e['mm'](J,K,4);assert not np.any(JK%2)
    R,piv=d['rref'](np.column_stack((A0,JK//2)))
    r2=len(piv);r0=e['rank0']
    assert r2==compressed_dimension==3953
    row={'certificate_index':ix,'missing_coset':rec['missing_coset'],
         'jacobian_rank_mod2':r0,'jacobian_rank_through_second_layer':r2,
         'elementary_divisors_valuation_zero':r0,
         'elementary_divisors_valuation_one':r2-r0,
         'base_norm_residual_divisible_by8':True,
         'step_two_jacobian_checks':5}
    rows.append(row)
    certificates[f'J4_{ix}_homology_and_multiplier_columns']=J[:,np.r_[np.arange(n),m]]
    print(json.dumps(row),flush=True)
out={'coordinate_dimension':nw,'full_norm_output_dimension':nr,
     'homology_character_traces_s_r_r2':[trS,trR,trR2],
     'exterior_character_traces_s_r_r2':[trWS,trWR,trWR2],
     'fixed_module_dimensions':[fixedS,fixedR],
     'compressed_norm_target_dimension':compressed_dimension,
     'integral_abelianization_relation_H_As_equals_s_lattice_H':True,
     'records':rows,'elapsed_seconds':round(time.time()-start,3),
     'scope':'Integral tangent certificate modulo4. The associated Hensel proof must supply a primitive compression of the norm equations and its exact target rank before any tower conclusion.'}
(here/'de_two_hensel_tangent.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(here/'de_two_hensel_tangent_certificate.npz',**certificates)
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
