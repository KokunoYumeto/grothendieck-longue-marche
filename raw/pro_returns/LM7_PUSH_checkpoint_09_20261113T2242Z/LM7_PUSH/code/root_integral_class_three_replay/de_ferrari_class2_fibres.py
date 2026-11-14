#!/usr/bin/env python3
"""Complete affine CM-fibre check in the class-two Ferrari quotient.

This uses all 18 affine parameters.  The six N-images are verified to
be elementary abelian in explicitly additive coordinates, so the
complete joint parameter image is calculated, not sampled.
"""
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
import io,json,runpy,time
import numpy as np
import de_ferrari_class2_model as h

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
P=np.load(here/'de_affine_fibres.npz')['p3_image_parameters'].astype(np.int64)
B=P[:97];dim=B.shape[1];assert dim==18
old=np.load(here/'de_ferrari_fibres_certificate.npz')
base=json.loads((here/'de_fibre_sixteen_crt_verify.json').read_text())['records']
witnesses=json.loads((here/'de_ferrari_fibres.json').read_text())['records']
N=[h.manyword(w) for w in d['Nfwords']]
Ns=[h.manyword(d['fword']([0]+w+[0])) for w in d['Nwords']]
unit=np.array(h.one,dtype=np.int64)

def rref(A):
    A=np.array(A,dtype=np.int64)%3;rank=0;piv=[]
    for col in range(A.shape[1]):
        ix=np.flatnonzero(A[rank:,col])
        if not len(ix):continue
        k=rank+int(ix[0]);A[[rank,k]]=A[[k,rank]]
        A[rank]=A[rank]*int(A[rank,col])%3
        for j in range(A.shape[0]):
            if j!=rank and A[j,col]:A[j]=(A[j]-A[j,col]*A[rank])%3
        piv.append(col);rank+=1
        if rank==A.shape[0]:break
    return A,piv

def nullspace(A):
    R,p=rref(A);free=[j for j in range(A.shape[1]) if j not in p]
    K=np.zeros((A.shape[1],len(free)),dtype=np.int64)
    for k,j in enumerate(free):K[j,k]=1;K[p,k]=-R[:len(p),j]%3
    assert not np.any(A@K%3)
    return K

def additive_vector(x):return (np.array(x,dtype=np.int64)-unit)%3
def from_additive(x):return tuple(int(t)%3 for t in x+unit)

# The complete generated subgroup in each target has additive coordinates.
# Checking the generators' pair products suffices here because their span
# has only 9 elements at most; we also check every element of that span.
for j in range(6):
    values=[x[j] for x in N]
    subgroup=h.generated(values)
    assert len(subgroup)<=9
    for x in subgroup:
        assert h.power(x,3)==h.one
        for y in subgroup:
            assert h.comm(x,y)==h.one
            assert h.mul(x,y)==from_additive(additive_vector(x)+additive_vector(y))
    assert all(x[j] in subgroup for x in Ns)
for i in range(97):
    for j in range(i+1,97):
        assert all(h.comm(x,y)==h.one for x,y in zip(N[i],N[j]))
LN=(np.array(N,dtype=np.int64)-unit)%3
LS=(np.array(Ns,dtype=np.int64)-unit)%3
fab=old['N_F_abelianization'].astype(np.int64)
assert not np.any((fab[1]-fab[0])%2)
ell=(fab[1]-fab[0])//2
test=np.vstack((LN.reshape(97,-1).T,LS.reshape(97,-1).T,ell[None,:]))@B%3
rr,piv=rref(test);rank=len(piv);K=nullspace(test);U=np.eye(dim,dtype=np.int64)[:,piv]
assert rank==2 and K.shape==(18,16)
oldtest=old['linear_auxiliary_parameter_map']
assert len(rref(np.vstack((test,oldtest)))[1])==2
assert np.array_equal(U,old['auxiliary_section'])

def values(rec,z):
    change=B@z%3
    valsN=np.einsum('i,ijk->jk',change,LN)%3
    valsS=np.einsum('i,ijk->jk',change,LS)%3
    g=rec['integral_cusp_gauge']+2*int(ell@change%3)
    out=[]
    for j,(x,y) in enumerate(h.pairs):
        out.append(h.mul(h.mul(h.mul(h.mul(h.power(y,g),from_additive(valsS[j])),
                           rec['f_beta_values'][j]),h.inv(from_additive(valsN[j]))),h.power(x,-g)))
    return tuple(out)

rng=np.random.default_rng(182026);rows=[];start=time.time()
for ix,(rec,witness) in enumerate(zip(base,witnesses)):
    rec=dict(rec);beta=rec['base_beta_word_B']
    rec['f_beta_values']=h.manyword(d['fword']([0]+beta+[0]+d['binv'](beta)))
    for _ in range(3):
        z=rng.integers(0,3,size=dim);change=B@z%3
        wb=[]
        for c,w in zip(4*change,d['Nwords']):wb+=w*int(c)
        wb+=beta;ab=fab@(4*change)
        g=rec['integral_cusp_gauge']+int(ab[1]-ab[0]);cg=d['bpower'](d['xword'],g)
        fw=d['fword']([0]+cg+wb+[0]+d['binv'](wb)+d['binv'](cg))
        assert values(rec,z)==h.manyword(fw)
    table=[];passing=0
    for bits in product(range(3),repeat=rank):
        vals=values(rec,U@np.array(bits,dtype=np.int64));pent=h.pentagon(vals)
        projected=witness['complete_auxiliary_table'][len(table)]['pentagon_residual']
        assert list(pent[4:6])==projected
        assert (pent==h.one)==(projected==[0,0])
        if pent==h.one:
            h.check_braids(h.braid_images(vals));passing+=1
        table.append({'auxiliary_coordinates':list(bits),'pentagon_residual':list(pent[4:]),
                      'pentagon_holds':pent==h.one})
    assert passing==3
    actual=h.manyword(witness['actual_commutator_word_f'])
    assert h.pentagon(actual)==h.one
    h.check_braids(h.braid_images(actual))
    assert len(h.generated(h.braid_images(actual)))==648
    row={'certificate_index':ix,'missing_coset':rec['missing_coset'],
         'complete_auxiliary_table':table,'passing_auxiliary_values':passing,
         'same_pentagon_zero_set_as_Ferrari_homology':True,
         'retained_E17_word_passes_complete_pentagon':True,
         'retained_E17_word_gives_surjective_B4_map':True,
         'all_three_braid_relations_verified':True}
    rows.append(row);print(json.dumps({k:v for k,v in row.items() if k!='complete_auxiliary_table'}),flush=True)

out={'finite_Ferrari_quotient_order':648,'pure_four_strand_quotient_order':15552,
     'all_N_cubes_and_commutators_trivial':True,
     'full_affine_parameter_dimension':18,'auxiliary_image_dimension':rank,
     'auxiliary_kernel_dimension':K.shape[1],
     'auxiliary_image_equal_to_E17_homology_image':True,
     'new_affine_pentagon_constraints':0,'records':rows,
     'pass_counts':[sum(r['missing_coset']==b for r in rows) for b in (False,True)],
     'elapsed_seconds':round(time.time()-start,3),
     'scope':'Complete necessary pentagon and braid-image test in the actual class-two Ferrari quotient, throughout all affine G3 CM parameters. No extension to every four-strand quotient is asserted.'}
here.joinpath('de_ferrari_class2_fibres.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(here/'de_ferrari_class2_fibres_certificate.npz',
                    N_coordinates=LN,s_N_s_coordinates=LS,
                    auxiliary_parameter_map=test,auxiliary_section=U,auxiliary_kernel=K)
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
