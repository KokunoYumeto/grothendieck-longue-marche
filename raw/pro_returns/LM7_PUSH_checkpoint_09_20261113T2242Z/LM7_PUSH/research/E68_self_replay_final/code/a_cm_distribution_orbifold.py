#!/usr/bin/env python3
"""The actual E66/E62 plus E67 common correction image on the same N_B'.

All inputs are read-only.  The E17 origins are replayed in the literal
twelve-map export; no correction is transported from the original E1
word list.  Derivation precedes the coordinate-zero distribution map.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np

from de_ferrari_a6_source_data import load_data
from de_a6_schreier_certificate import read_certificate
from a_cm_gl23_pc import ClassTwoCoordinates, Sifter
from a_cm_distribution_e62 import Distribution, NS, certify


HERE=Path(__file__).resolve().parent


def permword(word,generators):
    out=np.arange(len(generators[0]),dtype=np.uint16)
    letters={1:generators[0],2:generators[1],
             -1:np.argsort(generators[0]),-2:np.argsort(generators[1])}
    for a in word:out=letters[a][out]
    return out


class OrbifoldExport:
    def __init__(self):
        self.meta=json.loads((HERE/'bc_orbifold_CM_export.json').read_text())
        self.data=np.load(HERE/'bc_orbifold_CM_export.npz')
        self.points=[tuple(p) for p in self.meta['points']]
        assert self.points==[(a,b) for a in range(3) for b in range(3)]
        self.F=self.data['F_generator_permutations']
        self.N=self.data['N_generator_permutations']
        assert self.F.shape==(2,108) and self.N.shape==(97,108)
        self.translation_perms={v:np.array([
            self.points.index(((a-v[0])%3,(b-v[1])%3))
            for a,b in self.points],dtype=np.uint16) for v in self.points}
        for a in self.points:
            for b in self.points:
                c=((a[0]+b[0])%3,(a[1]+b[1])%3)
                assert np.array_equal(self.translation_perms[c],
                                      self.translation_perms[b][self.translation_perms[a]])

    def translations(self,v):
        assert len(v)==24
        return np.concatenate([9*j+self.translation_perms[tuple(map(int,v[2*j:2*j+2]))]
                               for j in range(12)])


def main():
    start=time.monotonic()
    export=OrbifoldExport();D=Distribution();source=load_data()
    words=[list(source['fword'](w)) for w in source['Nwords']]
    assert words==export.meta['literal_N_basis_in_F']
    for w,p in zip(words,export.N):assert np.array_equal(permword(w,export.F),p)
    prior=np.load(HERE/'a_cm_distribution_e62.npz')
    oldN=prior['common_N'];olddegree=oldN.shape[1]
    assert oldN.shape==(97,5223)
    assert np.array_equal(oldN[:,:4764],
                          np.load(HERE/'a_cm_gl23_joint.npz')['joint_N_generators'])
    assert np.array_equal(oldN[:,4764:]-4764,
                          np.array([D.source(w) for w in words]))
    common=np.array([np.r_[a,olddegree+b] for a,b in zip(oldN,export.N)])
    assert common.shape==(97,5331)

    ninfo,ncert=certify('a_cm_distribution_orbifold_N',common,greedy=True)
    indices=ninfo['selected_original_indices']
    print('Actual common N image',ninfo['order'],'selected',len(indices),flush=True)
    cinfo,ccert=certify('a_cm_distribution_orbifold_N_derived',common[indices],derived=True)
    print('Actual common derived image',cinfo['order'],flush=True)
    oldpoints=prior['retained_projection_points']
    assert len(oldpoints)==4849
    points=np.r_[oldpoints,olddegree+np.arange(108)]
    inverse=np.full(common.shape[1],-1,dtype=np.int64)
    inverse[points]=np.arange(len(points))
    projected=inverse[ccert['strong'][:,points]]
    assert np.all(projected>=0) and projected.shape[1]==4957
    jinfo,jcert=certify('a_cm_distribution_orbifold_projected',projected,greedy=True)
    print('Actual joined correction image',jinfo['order'],flush=True)
    joint=Sifter(jcert)
    oldcorrection=read_certificate(HERE/'a_cm_distribution_e62_projected.bin')
    oldSifter=Sifter(oldcorrection)
    for g in jcert['strong']:assert oldSifter.contains(g[:4849])
    oinfo,ocert=certify('a_cm_distribution_orbifold_orbifold',
                       projected[:,4849:]-4849,greedy=True)
    assert int(oinfo['order'])==3**9
    oldinfo=json.loads((HERE/'a_cm_distribution_e62.json').read_text())
    oldorder=int(oldinfo['common_projected_correction_image']['order'])
    overlap,remainder=divmod(oldorder*3**9,int(jinfo['order']))
    assert remainder==0

    P=ClassTwoCoordinates('joint')
    origins=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    family=export.meta['families']['E17_E62_actual']
    assert len(origins)==len(family)==len(oldinfo['records'])==24
    records=[];witness_values=[];witness_parameters=[]
    for index,(rec,oldrec,exrec) in enumerate(zip(origins,oldinfo['records'],family)):
        f=rec['actual_commutator_word_f']
        assert f==exrec['literal_origin_F_word'] and exrec['index']==index
        ov=np.array(exrec['origin_translation_values'],dtype=np.uint8)
        assert np.array_equal(ov,export.data['E17_E62_actual_origin_values'][index])
        assert np.array_equal(permword(f,export.F),export.translations(ov))
        qf=D.ordinary(f)
        dvalues=[D.word(f,n) for n in NS]
        assert all(k==0 for k,v in dvalues)
        oldd=[v[0] for k,v in dvalues]
        finals=[]
        for fi,oldfin in enumerate(oldrec['actual_single_source_correction_fibres']):
            coordinate=oldfin['E62_actual_PC_coordinate']
            cp=P.element(coordinate)
            values=[]
            for coeff in oldfin['admissible_distribution_coefficient_tuples']:
                dtarget=[]
                for oldv,c in zip(oldd,coeff):
                    hc=D.hm[D.apower((D.y[0],0),c)[0]][qf]
                    dtarget.append(D.am(D.ai(oldv),(hc,c)))
                dp=D.projected(dtarget)
                oldvalue=np.r_[cp,4764+dp]
                assert oldSifter.contains(oldvalue)
                for oi,targetrec in enumerate(exrec['complete_four_finite_norm_values']):
                    absolute=np.array(targetrec['absolute_twelve_translation_target'],dtype=np.int64)
                    correction=(absolute-ov)%3
                    assert np.array_equal(correction,np.array(targetrec['actual_correction_translation']))
                    assert np.array_equal(absolute,export.data['E17_E62_actual_allowed_absolute_targets'][index,oi])
                    desired=np.r_[oldvalue,4849+export.translations(correction)]
                    passes=joint.contains(desired)
                    entry={'distribution_coefficients':coeff,
                           'Mordell_target_index':targetrec['Mordell_index'],
                           'Gaussian_target_index':targetrec['Gaussian_index'],
                           'orbifold_target_index':oi,'passes':passes}
                    values.append(entry)
                    if passes:
                        witness_parameters.append([index,fi,oi,*coeff])
                        witness_values.append(desired)
            assert len(values)==12
            final={'E62_actual_PC_coordinate':coordinate,'finite_candidate_count':len(values),
                   'simultaneously_passing_count':sum(v['passes'] for v in values),
                   'complete_common_memberships':values}
            finals.append(final)
        assert len(finals)==4
        row={'index':index,'missing_coset':rec['missing_coset'],
             'complete_E62_final_fibres':finals,
             'passing_count':sum(r['simultaneously_passing_count'] for r in finals),
             'passing_E62_final_count':sum(bool(r['simultaneously_passing_count']) for r in finals)}
        records.append(row)
        print('Point',index,'passing',row['passing_count'],'E62 finals',row['passing_E62_final_count'],flush=True)

    inputs=['a_cm_distribution_e62.py','a_cm_distribution_e62.npz','a_cm_distribution_e62.json',
            'a_cm_distribution_e62_projected.bin','de_ferrari_a6_source_data.py',
            'de_ferrari_sl2_5_N.json','de_ferrari_fibres.json','a_cm_gl23_joint.npz',
            'a_cm_gl23_pc.py','a_cm_gl23_joint_pc.npz','bc_orbifold_CM_export.py',
            'bc_orbifold_CM_export.json','bc_orbifold_CM_export.npz','de_a6_schreier.cpp',
            'de_a6_schreier_certificate.py']
    out={'status':'PASS_ACTUAL_E66_E62_E67_COMMON_SOURCE',
         'common_N_source':ninfo,'common_N_derived_source':cinfo,
         'common_projected_correction_image':jinfo,'orbifold_projection':oinfo,
         'old_E66_correction_order':oldorder,'E67_correction_order':3**9,
         'exact_common_quotient_order':overlap,
         'same_97_N_words_compared_letterwise_and_replayed':True,
         'actual_E17_origins_replayed_independently':True,
         'candidate_count':24*4*3*4,'passing_count':len(witness_values),
         'records':records,
         'input_sha256':{name:sha256((HERE/name).read_bytes()).hexdigest() for name in inputs},
         'scope':'Exact common-source finite evaluation conditions. No generation in the '
                 'new distribution/orbifold refinement or full-GT lift is asserted.',
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'a_cm_distribution_orbifold.npz',
                        common_N=common,projected_derived_generators=projected,
                        retained_projection_points=points,
                        successful_membership_parameters=np.array(witness_parameters,dtype=np.int64),
                        successful_membership_values=np.array(witness_values,dtype=np.uint16))
    (HERE/'a_cm_distribution_orbifold.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)


if __name__=='__main__':main()
