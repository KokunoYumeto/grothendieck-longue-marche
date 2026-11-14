#!/usr/bin/env python3
"""Complete K2/K3 fixed-tuple fibres on K6 intersect F-prime.

Every orbit transversal is a word in an independently certified actual
strong generating set.  Old values are lifted through the prescribed
old-base prefix; their remaining choices are precisely the actual kernel.
No coordinate outside the displayed Kn equations is constrained.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
from math import prod
import json
import time
import numpy as np

from a_cm_distribution_e62 import Distribution, NS
from a_cm_distribution_orbifold import OrbifoldExport
from a_cm_gl23_pc import ClassTwoCoordinates, Sifter
from a_cm_kn23_model import permword
from de_a6_schreier_certificate import read_certificate, verify_words


HERE=Path(__file__).resolve().parent


class PrefixTransversals:
    def __init__(self,cert,count):
        self.cert=cert;self.count=count;self.n=cert['degree']
        self.one=np.arange(self.n,dtype=np.uint16);self.levels=[]
        for lev,base in enumerate(cert['base'][:count]):
            indices=np.flatnonzero(cert['depths']>=lev)
            orbit=[int(base)];at={int(base):0};trans=[self.one];paths=[()]
            for j,v in enumerate(orbit):
                for ix in indices:
                    g=cert['strong'][ix];w=int(g[v])
                    if w not in at:
                        at[w]=len(orbit);orbit.append(w)
                        trans.append(g[trans[j]])
                        paths.append(paths[j]+(int(ix),))
            self.levels.append({'base':int(base),'orbit':orbit,'at':at,
                                'trans':trans,'inverse':[np.argsort(t).astype(np.uint16)
                                                          for t in trans],
                                'paths':paths})

    def old_preimage(self,p):
        """Return u with the literal old permutation p, and its sift points."""
        oldn=len(p);h=p;answer=self.one;points=[]
        for level in self.levels:
            v=int(h[level['base']]);ix=level['at'][v];points.append(v)
            h=level['inverse'][ix][:oldn][h]
            answer=answer[level['trans'][ix]]
        assert np.array_equal(h,np.arange(oldn))
        assert np.array_equal(answer[:oldn],p)
        return answer,points

    def tuple_to_base(self,current):
        """Solve current.k=base, recording every actual inverse transversal."""
        h=current.copy();points=[]
        for lev,level in enumerate(self.levels):
            v=int(h[lev]);ix=level['at'].get(v)
            if ix is None:return False,lev,points,None
            points.append(v);h=level['inverse'][ix][h]
        target=np.array([level['base'] for level in self.levels])
        assert np.array_equal(h,target)
        # This is the actual right product of the inverse transversals.
        k=self.one
        for level,v in zip(self.levels,points):
            k=level['inverse'][level['at'][v]][k]
        assert np.array_equal(k[current],target)
        return True,len(self.levels),points,k


def main():
    started=time.monotonic()
    meta=json.loads((HERE/'a_cm_kn23_model.json').read_text())
    model=np.load(HERE/'a_cm_kn23_model.npz')
    full=json.loads((HERE/'a_cm_kn23_full.json').read_text())
    source=read_certificate(HERE/full['source_certificate'])
    kernel=read_certificate(HERE/full['kernel_certificate'])
    old=read_certificate(HERE/full['old_projection_certificate'])
    for cert in (source,kernel,old):verify_words(cert)
    oldn=old['degree'];newn=kernel['degree']
    assert oldn==4957 and newn==2544 and source['degree']==7501
    prefix=full['old_prefix_base_length'];targets=model['fixed_targets_in_projection']
    assert np.array_equal(kernel['base'][:len(targets)],targets)
    upper=PrefixTransversals(source,prefix)
    lower=PrefixTransversals(kernel,len(targets))
    upper_order=prod(len(l['orbit']) for l in upper.levels)
    tuple_orbit=prod(len(l['orbit']) for l in lower.levels)
    assert upper_order==int(full['entire_old_projection_order'])
    assert tuple_orbit==int(full['kernel_over_old_order'])
    assert len(kernel['base'])==len(targets)
    old_sifter=Sifter(old)

    P=ClassTwoCoordinates('joint');D=Distribution();O=OrbifoldExport()
    origins=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    finals=json.loads((HERE/'a_cm_gl23_joint_pentagon.json').read_text())['records']
    exorigins=O.meta['families']['E17_E62_actual']
    expected=np.load(HERE/'a_cm_distribution_orbifold.npz')
    expected_by_parameters={tuple(map(int,p)):v for p,v in
                            zip(expected['successful_membership_parameters'],
                                expected['successful_membership_values'])}
    retained=model['retained_projection_points']
    inverse=np.full(model['F_generators'].shape[1],-1,dtype=np.int64)
    inverse[retained]=np.arange(len(retained))
    groups={}
    for kind,prefix0 in [('GL23','GL2'),('SL23','SL2')]:
        data=np.load(HERE/('a_cm_'+kind.lower()+'_model.npz'))
        groups[kind]=(data[prefix0+'_multiplication'],int(data[prefix0+'_one']))

    input_points={}
    for a,b in product(range(24),repeat=2):
        points=[]
        for block in meta['blocks']:
            coeff=a if block['n']==2 else b
            if block['kind']=='matrix':
                q=meta['literal_quotients'][block['quotient_index']]
                multiplication,one=groups[q['kind']];v=one
                for _ in range(coeff):v=int(multiplication[v,q['y']])
                p=block['start']+v
            else:p=block['start']+(-coeff)%24
            points.append(int(inverse[p]))
        assert len(points)==70 and min(points)>=0
        input_points[(a,b)]=np.array(points,dtype=np.int64)

    old_parameters=[];old_paths=[];old_values=[];old_preimages=[]
    success_parameters=[];success_paths=[];success_values=[]
    query_parameters=[];query_failure=[];records=[];old_candidate_count=0
    for index,(origin,fin,exorigin) in enumerate(zip(origins,finals,exorigins)):
        f=origin['actual_commutator_word_f']
        assert f==exorigin['literal_origin_F_word']
        assert all(sum(1 if a==j else -1 if a==-j else 0 for a in f)==0 for j in (1,2))
        pfull=permword(f,model['F_generators']);pfi=inverse[pfull[retained]]
        assert np.all(pfi>=0)
        ov=np.array(exorigin['origin_translation_values'],dtype=np.int64)
        assert np.array_equal(permword(f,O.F),O.translations(ov))
        qf=D.ordinary(f);dvalues=[D.word(f,n) for n in NS]
        assert all(k==0 for k,v in dvalues)
        oldd=[v[0] for k,v in dvalues]
        origin_old_start=len(old_parameters);origin_pass_start=len(success_parameters)
        fibres=[]
        for fi,coordinate in enumerate(fin['all_surviving_correction_coordinates']):
            cp=P.element(coordinate)
            for a,b in product(range(6),repeat=2):
                coeff=(a,b,2*a%6,(a+b)%6,(2*a+b)%6)
                dtarget=[]
                for oldv,c in zip(oldd,coeff):
                    hc=D.hm[D.apower((D.y[0],0),c)[0]][qf]
                    dtarget.append(D.am(D.ai(oldv),(hc,c)))
                dp=D.projected(dtarget)
                for oi,targetrec in enumerate(exorigin['complete_four_finite_norm_values']):
                    absolute=np.array(targetrec['absolute_twelve_translation_target'],dtype=np.int64)
                    oldvalue=np.r_[cp,4764+dp,4849+O.translations((absolute-ov)%3)].astype(np.uint16)
                    pars=(index,fi,oi,*coeff);old_candidate_count+=1
                    passing=old_sifter.contains(oldvalue)
                    assert passing==(pars in expected_by_parameters)
                    if not passing:continue
                    assert np.array_equal(oldvalue,expected_by_parameters[pars])
                    u0,siftpoints=upper.old_preimage(oldvalue)
                    row=len(old_parameters);old_parameters.append(pars);old_paths.append(siftpoints)
                    old_values.append(oldvalue);old_preimages.append(u0)
                    pfi_u0=(u0[oldn:]-oldn)[pfi]
                    local_success=[]
                    for aa,bb in product(range(a,24,6),range(b,24,6)):
                        current=pfi_u0[input_points[(aa,bb)]]
                        ok,failed_at,paths,k=lower.tuple_to_base(current)
                        query_parameters.append((row,aa,bb));query_failure.append(failed_at)
                        if not ok:continue
                        correction=np.r_[u0[:oldn],oldn+k[u0[oldn:]-oldn]].astype(np.uint16)
                        assert np.array_equal(correction[:oldn],oldvalue)
                        assert np.array_equal((correction[oldn:]-oldn)[pfi[input_points[(aa,bb)]]],targets)
                        success_parameters.append((row,aa,bb));success_paths.append(paths)
                        success_values.append(correction);local_success.append([aa,bb])
                    fibres.append({'old_parameter_index':row,'E62_final_index':fi,
                                   'orbifold_target_index':oi,'coefficients_mod6':coeff,
                                   'passing_coefficients_mod24':local_success,
                                   'finite_correction_count':len(local_success)})
        records.append({'index':index,'missing_coset':origin['missing_coset'],
                        'old_value_count':len(old_parameters)-origin_old_start,
                        'passing_old_value_count':sum(bool(f['finite_correction_count']) for f in fibres),
                        'passing_correction_count':len(success_parameters)-origin_pass_start,
                        'complete_old_value_fibres':fibres})
        print('Origin',index,'old',records[-1]['old_value_count'],
              'surviving old',records[-1]['passing_old_value_count'],
              'finite corrections',records[-1]['passing_correction_count'],flush=True)
    assert old_candidate_count==24*4*36*4
    assert len(old_parameters)==len(expected_by_parameters)==1152
    assert len(query_parameters)==16*len(old_parameters)
    inputs=['a_cm_kn23_model.json','a_cm_kn23_model.npz','a_cm_kn23_full.json',
            full['source_certificate'],full['kernel_certificate'],full['old_projection_certificate'],
            'a_cm_kn23_ab_lattice.json','a_cm_kn23_ab_lattice.npz',
            'a_cm_distribution_orbifold.npz','bc_orbifold_CM_export.json',
            'bc_orbifold_CM_export.npz','de_ferrari_fibres.json',
            'a_cm_gl23_joint_pentagon.json','a_cm_gl23_joint_pc.npz']
    out={'status':'PASS_COMPLETE_KN23_FIBRES_ON_ENTIRE_K6_INTERSECT_FPRIME',
         'old_candidates_exhaustively_checked':old_candidate_count,
         'old_values_passing':len(old_parameters),'old_values_equal_frozen_E68_values':True,
         'coefficient_modulus':24,'coefficient_lifts_per_old_value':16,
         'complete_fixed_tuple_queries':len(query_parameters),
         'successful_finite_corrections':len(success_parameters),
         'kernel_order':int(full['kernel_over_old_order']),
         'fixed_tuple_orbit_size':tuple_orbit,'fixed_tuple_stabilizer_order':1,
         'exact_domain':'K6 intersect F-prime',
         'old_parameter_columns':['E17_origin','E62_final','E67_target','c2','c3','c4','c6','c12'],
         'query_parameter_columns':['old_parameter_index','c2_mod24','c3_mod24'],
         'all_successful_fixed_point_values_directly_replayed':True,
         'records':records,'input_sha256':{n:sha256((HERE/n).read_bytes()).hexdigest() for n in inputs},
         'scope':'Entire finite correction fibres over the stated E68 conditions and all literal K2/K3 matrix maps. No full-GT lift or extra source-generation property is inferred.',
         'seconds':round(time.monotonic()-started,6)}
    np.savez_compressed(HERE/'a_cm_kn23_fibres.npz',
                        old_parameters=np.array(old_parameters,dtype=np.int64),
                        old_sift_points=np.array(old_paths,dtype=np.int64),
                        old_values=np.array(old_values,dtype=np.uint16),
                        old_preimages=np.array(old_preimages,dtype=np.uint16),
                        query_parameters=np.array(query_parameters,dtype=np.int64),
                        query_failure_level=np.array(query_failure,dtype=np.int64),
                        success_parameters=np.array(success_parameters,dtype=np.int64).reshape(-1,3),
                        success_kernel_sift_points=np.array(success_paths,dtype=np.int64).reshape(-1,70),
                        success_values=np.array(success_values,dtype=np.uint16).reshape(-1,7501))
    (HERE/'a_cm_kn23_fibres.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)


if __name__=='__main__':main()
