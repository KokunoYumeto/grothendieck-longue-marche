#!/usr/bin/env python3
"""All ternary planes and central translates in the order-three torsion test."""
from pathlib import Path
from itertools import product
from contextlib import redirect_stdout
import io,json,runpy,time
import numpy as np
from de_ferrari_degree6_kernel import CombinedSix,InducedSix
from de_ferrari_three_conjugacy import Conjugacy,braid_word

here=Path(__file__).resolve().parent

def main():
    start=time.time();H=CombinedSix()
    epsilon=H.mul(H.mul(H.power(H.a,2),H.b),H.c)
    z4=H.power(H.mul(H.mul(H.a,H.b),H.c),4)
    assert np.array_equal(H.power(epsilon,3),z4)
    assert np.array_equal(H.power(z4,9),H.one) and not np.array_equal(H.power(z4,3),H.one)
    assert np.array_equal(H.power(epsilon,27),H.one)
    assert all(np.array_equal(H.comm(z4,g),H.one) for g in (H.a,H.b,H.c))
    assert np.array_equal(H.power(epsilon,73),H.mul(epsilon,H.power(z4,6)))
    solver=Conjugacy(H,epsilon)
    print(json.dumps({'stage':'complete_conjugacy_solver',**solver.metadata(),
                      'seconds':round(time.time()-start,3)}),flush=True)
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    W=InducedSix(H,d);x=W.word(d['xword'])
    CM=np.load(here/'de_ferrari_degree6_lift_certificate.npz')['top_kernel_basis']
    rows=json.loads((here/'de_ferrari_degree6_lift.json').read_text())['records']
    origins=json.loads((here/'de_ferrari_fibres.json').read_text())['records']
    records=[];targets=[];target_lookup={};witnesses=[];witness_lookup={}
    zpow=[H.power(z4,j) for j in range(9)]
    for rec,origin in zip(rows,origins):
        ix=rec['certificate_index'];base=rec['chosen_witness']
        baseimages=[H.decode(g) for g in base['actual_braid_images']]
        K=np.array(base['homogeneous_top_correction'],dtype=np.int64)
        assert K.shape==(6,2)
        xg=W.power(x,origin['integral_cusp_gauge']);plane=[]
        for a,b in product(range(3),repeat=2):
            corr=W.conj(xg,W.element(CM@(K@np.array([a,b],dtype=np.int64)%3)%3))[1][W.root]
            images=[baseimages[0],H.conj(H.inv(corr[4]),baseimages[1]),H.conj(H.inv(corr[5]),baseimages[2])]
            H.check_braids(images)
            assert all(np.array_equal(H.power(g,73),g) for g in images)
            aa,bb,cc=images;y=H.mul(H.mul(H.power(aa,2),bb),cc)
            assert np.array_equal(H.power(y,3),z4)
            key=bytes(np.asarray(y,dtype=np.int64));ti=target_lookup.get(key)
            if ti is None:
                ti=len(targets);target_lookup[key]=ti;translates=[]
                for j in range(9):
                    target=H.mul(y,zpow[j]);ans=solver.conjugator(target)
                    if ans is None:
                        translates.append({'central_exponent':j,'conjugate':False,
                            'base_failures':solver.failed_certificates[bytes(np.asarray(target,dtype=np.int64))]})
                    else:
                        wk=tuple(ans['literal_B4_conjugator']);wi=witness_lookup.get(wk)
                        if wi is None:
                            wi=len(witnesses);witness_lookup[wk]=wi;witnesses.append(ans)
                        assert np.array_equal(H.conj(braid_word(H,list(wk)),epsilon),target)
                        translates.append({'central_exponent':j,'conjugate':True,'witness_index':wi})
                targets.append({'target_index':ti,'epsilon_image':H.encode(y),'all_central_translates':translates})
            positive=[r['central_exponent'] for r in targets[ti]['all_central_translates'] if r['conjugate']]
            plane.append({'ternary_parameters':[a,b],'target_index':ti,
                          'conjugate_in_central_quotient':bool(positive),
                          'lambda1_passing_central_exponents':positive,
                          'lambda73_passing_central_exponents':sorted((j+6)%9 for j in positive)})
        record={'certificate_index':ix,'missing_coset':rec['missing_coset'],
                'all_nine_ternary_points':plane,
                'passing_points':sum(r['conjugate_in_central_quotient'] for r in plane)}
        records.append(record)
        print(json.dumps({'certificate_index':ix,'missing_coset':rec['missing_coset'],
                          'passing_points':record['passing_points'],
                          'target_indices':[r['target_index'] for r in plane]}),flush=True)
    out={'source':'all24 degree-six ternary planes retained by E24',
         'ternary_points':216,'joint_E24_points':864,'central_order':9,
         'epsilon_order':27,'epsilon_cubed_is_full_twist':True,
         'all_binary_parameters_preserve_ternary_inputs_by_verified_CRT':True,
         'both_multiplier_branches_and_all_higher_lifts_covered_by_central_translation':True,
         'conjugacy_solver':solver.metadata(),'records':records,'distinct_targets':targets,
         'literal_witnesses':witnesses,'distinct_untranslated_target_count':len(targets),
         'distinct_translated_target_count':len(solver.cache),
         'literal_conjugator_count':len(witnesses),
         'passing_ternary_points':sum(r['passing_points'] for r in records),
         'whole_retained_fibres_removed':[r['certificate_index'] for r in records if not r['passing_points']],
         'seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_three_torsion.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_three_torsion_certificate.npz',
                        kernel_basis=solver.M,central_derived_basis=solver.ZM,
                        central_quotient_matrix=solver.Q,epsilon_conjugation=solver.A,
                        first_matrix=solver.first,first_kernel=solver.C1,
                        second_matrix=solver.second,full_centralizer=solver.C2)
    print(json.dumps({k:v for k,v in out.items() if k not in ('records','distinct_targets','literal_witnesses')},indent=2),flush=True)

if __name__=='__main__':main()
