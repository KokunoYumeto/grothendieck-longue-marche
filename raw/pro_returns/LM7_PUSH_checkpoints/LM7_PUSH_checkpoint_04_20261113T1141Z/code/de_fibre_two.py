#!/usr/bin/env python3
"""Exact quadratic obstruction on the affine CM fibres at two.

The free class-two exponent-four normal form gives a bilinear cocycle
kappa on N_ab/2 with values in each Q-invariant central quotient. Its
automorphism cochains are quadratic. We derive the five obstruction
polynomials, verify them against direct words, and seek positive witnesses.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_class2_two.py'))
v=d['v'];base=d['d'];n=97;S,R=d['S'].astype(np.int64),d['R'].astype(np.int64);T=S@R%2;I=np.eye(n,dtype=np.int64)
projection=d['nullspace'](d['variation'].T).astype(np.int64);assert projection.shape==(16,5)
funs=d['invariants'].astype(np.int64)@projection%2;up=d['upper']
kappas=[]
for functional in funs.T:
    K=np.diag(functional[:n]);K[up[1],up[0]]=functional[n:];kappas.append(K)
kappas=np.stack(kappas)
def pair(w):
    a=np.zeros(n,dtype=np.int64);z=np.zeros((n,n),dtype=np.int64)
    for t in d['nword'](w):
        k=abs(t)-1;z[k,k+1:]^=a[k+1:]%2;a[k]=(a[k]+(1 if t>0 else -1))%4
    return a,z
etas=[]
for g,gi,Ag in (([0],[0],S),([1],[-1],R)):
    tau=[]
    for j,w in enumerate(base['Nwords']):
        a,z=pair(g+w+gi);assert np.array_equal(a%2,Ag[:,j])
        cc=np.concatenate(((a//2)%2,z[up]));tau.append(cc@funs%2)
    tau=np.stack(tau,axis=1);eta=[]
    for k,K in enumerate(kappas):
        E=np.zeros((n,n),dtype=np.int64);E[up]=(Ag.T@K@Ag)[up]%2
        E[np.diag_indices(n)]=tau[k]
        assert not np.any((E+E.T+K+Ag.T@K@Ag)%2)
        eta.append(E)
    etas.append(np.stack(eta))
es,er=etas;et=np.stack([R.T@E@R for E in es])+er;et%=2
aff=np.load(here/'de_affine_fibres.npz');P=aff['p2_image_parameters'];B,A=P[:n],P[n:];dim=P.shape[1]
assert dim==17 and not np.any(v['L']@P%2)
cert=[r for r in d['cert'] if 'mod6_beta_cycles' in r]
pulls=np.stack([v['permutation'][v['index'][v['inverse'](q)]][v['chords']] for q in v['Q']])
C=v['C'];delta=[]
for j in range(dim):
    edge=C@(A[:,j]-B[:,j]);delta.append(C.T@edge[pulls]%2)
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
    return d['kernel_coordinate'](error)@funs%2
def poly_values(xs,c,Q):return (c+np.einsum('bi,kij,bj->bk',xs,Q,xs,optimize=True))%2
rng=np.random.default_rng(152026);records=[];saved={'parameters':P,'obstruction_projection':projection};start=time.time()
for j,rec in enumerate(cert):
    a,b,av,bv,wa,wb=original_words(rec)
    abinv=v['act'](v['inverse'](b),C)[v['chords']]%2
    eb=np.zeros((5,n,n),dtype=np.int64)
    for letter in base['Bpaths'][b]:
        if letter==0:ag,eg=S,es
        elif letter==1:ag,eg=R,er
        else:ag=R@R%2;eg=np.stack([ag.T@E@ag for E in er])%2
        eb=(np.stack([ag.T@E@ag for E in eb])+eg)%2
    es0=[];quadratic=[]
    for k,K in enumerate(kappas):
        E=abinv.T@(S.T@eb[k]@S+es[k]+eb[k])@abinv
        E+=np.diag(bv@(K+K.T)@(S-I));E%=2;es0.append(E)
        quadratic.append((B.T@K@(I+T)@A+(A+B).T@E@(A+B)+A.T@et[k]@A)%2)
    quadratic=np.stack(quadratic);constant=np.array(d['records'][j]['obstruction'])@projection%2
    assert np.array_equal(poly_values(np.zeros((1,dim),dtype=np.int64),constant,quadratic)[0],direct_values(wa,wb))
    for check in range(3 if j==0 else 1):
        x=rng.integers(0,2,size=dim);dx=P@x%2
        assert np.array_equal(poly_values(x[None,:],constant,quadratic)[0],direct_values(word_from_vector(dx[n:])+wa,word_from_vector(dx[:n])+wb))
    edge=v['P'][a]+C@av-v['P'][b]-C@bv;edge[v['index'][a]]+=1
    m0=C.T@edge[pulls]%2;assert len(d['rref'](m0)[1])==97
    found=None;obstruction_passes=0;tried=0
    for batch in range(100):
        xs=rng.integers(0,2,size=(10000,dim));zs=poly_values(xs,constant,quadratic)
        for i in np.flatnonzero(~np.any(zs,axis=1)):
            x=xs[i];obstruction_passes+=1
            mat=(m0+np.einsum('i,ijk->jk',x,delta))%2
            if len(d['rref'](mat)[1])==97:found=x;break
        tried+=len(xs)
        if found is not None:break
    row={'certificate_index':j,'missing_coset':bool(rec['missing_coset']),
         'samples_examined_at_most':tried,'obstruction_solutions_tested_for_generation':obstruction_passes,
         'replacement_found':found is not None}
    if found is not None:
        dx=P@found%2;assert not np.any(direct_values(word_from_vector(dx[n:])+wa,word_from_vector(dx[:n])+wb))
        row.update({'parameters':found.tolist(),'beta_change_mod2':dx[:n].tolist(),'A_change_mod2':dx[n:].tolist(),'generation_rank_mod2':97})
    records.append(row);saved[f'quadratic_{j}']=quadratic;saved[f'constant_{j}']=constant
    print(json.dumps({k:w for k,w in row.items() if k not in ('parameters','beta_change_mod2','A_change_mod2')}),flush=True)
np.savez_compressed(here/'de_fibre_two_polynomials.npz',**saved)
out={'parameter_dimension':dim,'obstruction_dimension':5,'all_polynomial_checks_by_direct_words':True,
     'elapsed_seconds':round(time.time()-start,3),'records':records,
     'scope':'Positive finite peripheral lifts for complete affine CM fibres at two; failed random searches carry no exclusion claim. Each retained candidate has full generation rank.'}
(here/'de_fibre_two.json').write_text(json.dumps(out,indent=2)+'\n')
