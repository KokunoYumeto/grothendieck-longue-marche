#!/usr/bin/env python3
"""Quadratic obstruction on all affine homology parameters at three.

The five obstruction polynomials are constructed exactly, then checked
against direct collection of words in the free class-two group. Searches
are used only to produce positive witnesses; no failed search is an
exclusion claim. Generation is checked by the complete 97-dimensional map.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_class2_refinement.py'))
v=d['v'];base=d['d'];n=97;S,R=d['S'],d['R'];T=S@R%3;I=np.eye(n,dtype=np.int64)
V=d['variation_r'];projection=d['nullspace'](V.T);assert projection.shape==(8,5)
forms=np.einsum('kj,kab->jab',projection,np.stack(d['invariant_matrices']))%3
tau_s=np.stack(d['tau_s'],axis=1);tau_r=np.stack(d['tau_r'],axis=1)
ts=projection.T@tau_s%3;tr=projection.T@tau_r%3;tt=(ts@R+tr)%3
aff=np.load(here/'de_affine_fibres.npz');P=aff['p3_image_parameters'];B,A=P[:n],P[n:];dim=P.shape[1]
assert dim==18 and not np.any(v['L']@P%3)
quad=np.stack([2*B.T@f@(T-I)@A%3 for f in forms])
cert=[a for a in d['cert'] if 'mod6_beta_cycles' in a]
pulls=np.stack([v['permutation'][v['index'][v['inverse'](q)]][v['chords']] for q in v['Q']])
C=v['C'];delta=[]
for j in range(dim):
    edge=C@(A[:,j]-B[:,j]);delta.append(C.T@edge[pulls]%3)
delta=np.stack(delta)
def word_from_vector(a):
    out=[]
    for c,w in zip(a,base['Nwords']):out+=w*int(c)
    return out
def original_words(rec):
    a=v['representative'](rec['A']);b=v['representative'](rec['beta'])
    av=np.array([rec['mod6_A_cycles'].get(str(i),0) for i in range(n)])
    bv=np.array([rec['mod6_beta_cycles'].get(str(i),0) for i in range(n)])
    return a,b,av,bv,word_from_vector(av)+base['Bpaths'][a],word_from_vector(bv)+base['Bpaths'][b]
def direct_values(wa,wb):
    error=wb+[0]+base['binv'](wb)+wa+[1]+base['binv'](wa)+[-1,0]
    return d['dual_values'](d['class2'](error))@projection%3
def poly_values(xs,c,lin):
    return (c+xs@lin.T+np.einsum('bi,kij,bj->bk',xs,quad,xs,optimize=True))%3
rng=np.random.default_rng(142026);records=[];saved={'quadratic':quad,'parameters':P,'obstruction_projection':projection};start=time.time()
for j,rec in enumerate(cert):
    a,b,av,bv,wa,wb=original_words(rec)
    ab=v['act'](b,C)[v['chords']]%3
    abinv=v['act'](v['inverse'](b),C)[v['chords']]%3
    tb=np.zeros((5,n),dtype=np.int64)
    for letter in base['Bpaths'][b]:
        if letter==0:ag,tg=S,ts
        elif letter==1:ag,tg=R,tr
        else:ag=R@R%3;tg=-tr@ag%3
        tb=(tb@ag+tg)%3
    ts0=(tb@(S-I)@abinv+ts@abinv+np.stack([bv@f@(S-I) for f in forms]))%3
    linear=(ts0@(A-B)-tt@A)%3
    constant=np.array(d['records'][j]['obstruction_coordinates'])@projection%3
    assert np.array_equal(poly_values(np.zeros((1,dim),dtype=np.int64),constant,linear)[0],direct_values(wa,wb))
    for check in range(3 if j==0 else 1):
        x=rng.integers(0,3,size=dim);dx=P@x%3
        assert np.array_equal(poly_values(x[None,:],constant,linear)[0],direct_values(word_from_vector(dx[n:])+wa,word_from_vector(dx[:n])+wb))
    edge=v['P'][a]+C@av-v['P'][b]-C@bv;edge[v['index'][a]]+=1
    m0=C.T@edge[pulls]%3
    rank0=len(d['rref'](m0)[1]);assert rank0==97
    found=None;obstruction_passes=0;tried=0
    for batch in range(100):
        xs=rng.integers(0,3,size=(10000,dim));zs=poly_values(xs,constant,linear)
        for i in np.flatnonzero(~np.any(zs,axis=1)):
            x=xs[i];obstruction_passes+=1
            mat=(m0+np.einsum('i,ijk->jk',x,delta))%3
            if len(d['rref'](mat)[1])==97:
                found=x;break
        tried+=len(xs)
        if found is not None:break
    row={'certificate_index':j,'missing_coset':bool(rec['missing_coset']),
         'samples_examined_at_most':tried,'obstruction_solutions_tested_for_generation':obstruction_passes,
         'replacement_found':found is not None}
    if found is not None:
        dx=P@found%3;assert not np.any(direct_values(word_from_vector(dx[n:])+wa,word_from_vector(dx[:n])+wb))
        row.update({'parameters':found.tolist(),'beta_change_mod3':dx[:n].tolist(),'A_change_mod3':dx[n:].tolist(),'generation_rank_mod3':97})
    records.append(row);saved[f'linear_{j}']=linear;saved[f'constant_{j}']=constant
    print(json.dumps({k:w for k,w in row.items() if k not in ('parameters','beta_change_mod3','A_change_mod3')}),flush=True)
np.savez_compressed(here/'de_fibre_three_polynomials.npz',**saved)
out={'parameter_dimension':dim,'obstruction_dimension':5,'all_polynomial_checks_by_direct_words':True,
     'elapsed_seconds':round(time.time()-start,3),'records':records,
     'scope':'Positive finite peripheral lifts for complete affine CM fibres at three; failed random searches carry no exclusion claim. Each retained candidate has full generation rank.'}
(here/'de_fibre_three.json').write_text(json.dumps(out,indent=2)+'\n')
