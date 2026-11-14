#!/usr/bin/env python3
"""Whole affine CM fibres for the finite Ferrari-homology pentagon test.

We retain all18 three-primary generator-image parameters.  Their exact
image in the simultaneous Ferrari targets and the cusp gauge is reduced
by linear algebra on logarithms of the commuting exponent-three N-image.
Every value of the resulting small image is enumerated.  In the remaining
parameters we search for actual invertible G3 maps and for the previously
verified five class-two cusp equations.  Failed random searches are not
used as exclusions.  Actual representative words are retained on success.
"""
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
import io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):e=runpy.run_path(str(here/'de_ferrari_pentagon.py'))
d=e['d'];v=d['d'];n=97;p=3
P=np.load(here/'de_affine_fibres.npz')['p3_image_parameters'].astype(np.int64)
B,A=P[:n],P[n:];dim=P.shape[1];assert dim==18
records=e['records'];old=json.loads((here/'de_fibre_crt_verify.json').read_text())['records']
source=[r for r in json.loads((here/'de_source/d_cm_shadow.json').read_text())['pairs'] if 'mod6_beta_cycles' in r]
points=json.loads((here/'de_fibre_three.json').read_text())['records']
polys=np.load(here/'de_fibre_three_polynomials.npz');quad=polys['quadratic']

def to3(a):return np.array([[a[0],a[1],a[4]],[a[2],a[3],a[5]],[0,0,1]],dtype=np.int64)
def from3(a):return tuple(int(a[i,j])%3 for i,j in ((0,0),(0,1),(1,0),(1,1),(0,2),(1,2)))
I=np.eye(3,dtype=np.int64)
def log(a):
    D=to3(a)-I;assert not np.any(D@D@D%3)
    L=(D+D@D)%3
    assert from3((I+L+2*L@L)%3)==a
    return L
def exp(L):return from3((I+L+2*L@L)%3)
Ns=[e['manyword'](d['fword']([0]+w+[0])) for w in d['Nwords']]
LN=np.array([[log(a) for a in ng] for ng in e['N']],dtype=np.int64)
LS=np.array([[log(a) for a in ng] for ng in Ns],dtype=np.int64)
fab=np.array([[sum(1 if a==i else -1 if a==-i else 0 for a in w)
               for w in d['Nfwords']] for i in (1,2)],dtype=np.int64)
assert not np.any((fab[1]-fab[0])%2)
ell=(fab[1]-fab[0])//2
test=np.vstack((LN.reshape(n,-1).T,LS.reshape(n,-1).T,ell[None,:]))@B%3
rr,selected=e['rref'](test);rdim=len(selected)
zero_solution=e['solve'](test,np.zeros(test.shape[0],dtype=np.int64));K=zero_solution[1]
assert K.shape==(dim,dim-rdim)
U=np.eye(dim,dtype=np.int64)[:,selected]
print(json.dumps({'full_affine_image_dimension':dim,'Ferrari_parameter_image_dimension':rdim,
                  'remaining_parameter_dimension':K.shape[1],
                  'complete_auxiliary_choices':3**rdim}),flush=True)
assert rdim<=9,('Auxiliary dimension requires a different exhaustive algorithm',rdim)

pulls=np.stack([v['permutation'][v['index'][v['inverse'](q)]][v['chords']] for q in v['Q']])
C=v['C'];delta=np.stack([C.T@(C@(A[:,j]-B[:,j]))[pulls]%3 for j in range(dim)])
def values(rec,z):
    change=B@z%3
    logsN=np.einsum('i,ijkl->jkl',change,LN)%3
    logsS=np.einsum('i,ijkl->jkl',change,LS)%3
    g=rec['integral_cusp_gauge']+2*int(ell@change%3)
    ans=[]
    for j,(x,y) in enumerate(e['pairs']):
        ans.append(e['mul'](e['mul'](e['mul'](e['mul'](e['power'](y,g),exp(logsS[j])),
                    rec['f_beta_values'][j]),e['inv'](exp(logsN[j]))),e['power'](x,-g)))
    return tuple(ans)
def qvalues(xs,ix):
    return (polys[f'constant_{ix}']+xs@polys[f'linear_{ix}'].T+
            np.einsum('bi,kij,bj->bk',xs,quad,xs,optimize=True))%3
def wordfrom(a):
    out=[]
    for coefficient,w in zip(a,d['Nwords']):out+=w*int(coefficient)
    return out
def check_braids(images):
    aa,bb,cc=images;mul=e['mul']
    assert mul(mul(aa,bb),aa)==mul(mul(bb,aa),bb)
    assert mul(mul(bb,cc),bb)==mul(mul(cc,bb),cc)
    assert mul(aa,cc)==mul(cc,aa)

rng=np.random.default_rng(242028);rows=[];start=time.time()
certificates={'linear_auxiliary_parameter_map':test,'auxiliary_section':U,
              'auxiliary_kernel':K,'N_logarithms':LN,'s_N_s_logarithms':LS,
              'N_F_abelianization':fab}
for ix,(rec,oldrec,srec) in enumerate(zip(records,old,source)):
    rec=dict(rec);beta=rec['base_beta_word_B']
    rec['f_beta_values']=e['manyword'](d['fword']([0]+beta+[0]+d['binv'](beta)))
    qbeta=v['representative'](rec['beta']);qa=v['representative'](rec['A'])
    bv=np.array([srec['mod6_beta_cycles'].get(str(i),0) for i in range(n)])+np.array(oldrec['beta_change_mod6'])
    av=np.array([srec['mod6_A_cycles'].get(str(i),0) for i in range(n)])+np.array(oldrec['A_change_mod6'])
    edge=v['P'][qa]+C@av-v['P'][qbeta]-C@bv;edge[v['index'][qa]]+=1
    full_m0=C.T@edge[pulls]
    m0=full_m0%3;assert len(e['rref'](m0)[1])==97
    m02=full_m0%2;assert len(v['rref'](m02,2)[1])==97
    # Independent literal substitutions check the logarithmic parameter map.
    for check in range(3):
        z=rng.integers(0,3,size=dim);change=B@z%3
        w=wordfrom(4*change)+beta
        ab=fab@(4*change);g=rec['integral_cusp_gauge']+int(ab[1]-ab[0])
        cg=d['bpower'](d['xword'],g)
        fw=d['fword']([0]+cg+w+[0]+d['binv'](w)+d['binv'](cg))
        assert values(rec,z)==e['manyword'](fw)
    passing=[];pentagon_passes=0;intertwiner_passes=0;tables=[]
    pconstant=e['system'](values(rec,np.zeros(dim,dtype=np.int64)))[0][:2]
    pcols=np.column_stack([(e['system'](values(rec,U[:,j]))[0][:2]-pconstant)%3
                          for j in range(rdim)])
    for bits in product(range(3),repeat=rdim):
        z=U@np.array(bits,dtype=np.int64)
        err,mat,images=e['system'](values(rec,z))
        assert np.array_equal(err[:2],(pconstant+pcols@np.array(bits))%3)
        tables.append({'auxiliary_coordinates':list(bits),'pentagon_residual':err[:2].tolist(),
                       'Ferrari_homology_matrix':mat.tolist()})
        pentagon_passes+=int(not np.any(err[:2]))
        if np.any(err):continue
        intertwiner_passes+=1
        if (mat[0,0]*mat[1,1]-mat[0,1]*mat[1,0])%3:
            check_braids(images);passing.append(z)
    row={'certificate_index':ix,'missing_coset':rec['missing_coset'],
         'auxiliary_parameter_dimension':rdim,'all_auxiliary_choices_tested':3**rdim,
         'pentagon_choices':pentagon_passes,'pentagon_and_intertwiner_choices':intertwiner_passes,
         'invertible_auxiliary_choices':len(passing),
         'affine_pentagon_constraint_rank':len(e['rref'](pcols)[1]),
         'complete_auxiliary_table':tables,
         'simultaneous_class_two_and_generation_witness_found':False}
    assert row['affine_pentagon_constraint_rank']==1
    certificates[f'pentagon_constant_{ix}']=pconstant
    certificates[f'pentagon_auxiliary_linear_map_{ix}']=pcols
    found=None;tested=0;quadratic_hits=0
    initial=np.array(points[ix]['parameters'],dtype=np.int64)
    for batch in range(100):
        if not passing:break
        number=3000
        aux=np.array([passing[int(j)] for j in rng.integers(0,len(passing),size=number)])
        remain=rng.integers(0,3,size=(number,K.shape[1]))
        changes=(aux+remain@K.T)%3;total=(initial+changes)%3
        zeros=~np.any(qvalues(total,ix),axis=1);tested+=number
        for k in np.flatnonzero(zeros):
            z=changes[k];quadratic_hits+=1
            image=(m0+np.einsum('i,ijk->jk',z,delta))%3
            if len(e['rref'](image)[1])==97:
                found=z;break
        if found is not None:break
    row['sampled_parameter_values_at_most']=tested;row['quadratic_zeros_tested_for_generation']=quadratic_hits
    if found is not None:
        change=P@found%3;wb=wordfrom(4*change[:n])+beta
        wa=wordfrom(4*change[n:])+oldrec['base_A_word_B']
        ab=fab@(4*change[:n]);g=rec['integral_cusp_gauge']+int(ab[1]-ab[0]);cg=d['bpower'](d['xword'],g)
        fw=d['fword']([0]+cg+wb+[0]+d['binv'](wb)+d['binv'](cg))
        vv=e['manyword'](fw);assert vv==values(rec,found)
        err,mat,images=e['system'](vv);assert not np.any(err)
        check_braids(images)
        assert all(sum(1 if a==i else -1 if a==-i else 0 for a in fw)==0 for i in (1,2))
        assert not np.any(qvalues(((initial+found)%3)[None,:],ix))
        bp=(qbeta,(v['P'][qbeta]+C@(bv+4*change[:n]))%6)
        ap=(qa,(v['P'][qa]+C@(av+4*change[n:]))%6)
        ss=(v['ss'],np.zeros(576,dtype=np.int64));rr=(v['rr'],v['Pr']%6)
        assert v['equal'](v['gm'](v['gc'](bp,ss,6),v['gc'](ap,rr,6),6),v['gm'](ss,rr,6))
        newedge=edge+C@(4*change[n:]-4*change[:n])
        assert np.array_equal(C.T@newedge[pulls]%2,m02)
        row.update({'simultaneous_class_two_and_generation_witness_found':True,
                    'affine_parameter_change':found.tolist(),
                    'new_class_two_parameter':((initial+found)%3).tolist(),
                    'beta_homology_change_mod3':change[:n].tolist(),
                    'A_homology_change_mod3':change[n:].tolist(),
                    'integral_cusp_gauge':g,'base_beta_word_B':wb,'base_A_word_B':wa,
                    'actual_commutator_word_f':list(fw),'generation_ranks':[97,97],
                    'Ferrari_homology_matrix_mod3':mat.tolist(),
                    'pentagon_direct_substitution_verified':True,
                    'all_three_braid_relations_directly_verified':True,
                    'full_generation_matrix_mod2_verified_unchanged':True,
                    'literal_cusp_relation_G6_verified':True})
    rows.append(row)
    print(json.dumps({k:v for k,v in row.items() if k not in ('base_beta_word_B','base_A_word_B','actual_commutator_word_f','beta_homology_change_mod3','A_homology_change_mod3','complete_auxiliary_table')}),flush=True)
out={'full_affine_three_primary_image_dimension':dim,'auxiliary_parameter_image_dimension':rdim,
     'remaining_parameter_dimension':K.shape[1],
     'auxiliary_images_exhaustively_enumerated':True,
     'pass_counts':[sum(r['simultaneous_class_two_and_generation_witness_found'] and r['missing_coset']==b for r in rows) for b in (False,True)],
     'elapsed_seconds':round(time.time()-start,3),'records':rows,
     'scope':'The finite Ferrari-homology pentagon conditions are enumerated over all affine G3 parameters. Actual positive witnesses also satisfy the five class-two cusp equations and full G6 generation. No failed random search is an exclusion, and no full profinite pentagon lift is asserted.'}
(here/'de_ferrari_fibres.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(here/'de_ferrari_fibres_certificate.npz',**certificates)
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
