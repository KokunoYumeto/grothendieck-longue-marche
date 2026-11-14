#!/usr/bin/env python3
"""Exact target derived inclusions and the specified maximal solvable map.

The complete C++ replays certify each recorded subgroup order.  This
independent NumPy replay verifies every strong-generator word, every
interstage literal substitution, and the actual 105-point quotient map.
No assertion that a selected list generates its containing parent is
needed: the quotient order bounds and the retained derived inclusions
give all equalities, including perfection of the entire quotient kernel.
"""
from pathlib import Path
from hashlib import sha256
from math import prod
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_a6_schreier_certificate import read_certificate,verify_words
from de_a6_triple_base_prepare import evaluate
from de_a6_triple_source_certificate import report

HERE=Path(__file__).resolve().parent


def words_in_generators(words,generators):
    inverses=np.argsort(generators,axis=1).astype(np.uint16)
    values=[]
    for word in words:
        value=np.arange(generators.shape[1],dtype=np.uint16)
        for letter in word:
            assert letter and abs(letter)<=len(generators)
            factor=generators[letter-1] if letter>0 else inverses[-letter-1]
            value=factor[value]
        values.append(value)
    return np.asarray(values,dtype=np.uint16)


def permutation_order(generators):
    return int(PermutationGroup([Permutation(v.tolist()) for v in generators]).order())


def main():
    started=time.time()
    continuation=json.loads((HERE/'de_a6_triple_target_continue.json').read_text())
    assert continuation['final_stage']==5 and continuation['final_index']==20736
    small=json.loads((HERE/'de_a6_triple_target_quotient.json').read_text())
    qraw=np.load(HERE/'de_a6_triple_target_quotient.npz')
    qoriginal=qraw['quotient_generator_permutations'].astype(np.uint16)
    assert permutation_order(qoriginal)==20736
    expected_indices=small['small_complete_derived_indices']+[20736]
    assert expected_indices==[1,6,72,2304,20736,20736]
    names=['de_a6_triple_target_continue.json','de_a6_triple_target_prepare.npz',
           'de_a6_triple_target_quotient.json','de_a6_triple_target_quotient.npz',
           'de_a6_triple_target_old_maps.json','de_a6_gl_target_certificate.json',
           'de_a6_gl_target.out']
    stems=['de_a6_triple_target']+[
        f'de_a6_triple_target_derived{i}' for i in range(1,6)]
    for stage,stem in enumerate(stems):
        names.extend([stem+'.bin',stem+'.out'])
        if stage>=2:names.extend([stem+'_input.json',stem+'_input.npz'])
    names.append('de_a6_triple_target_replay.out')
    hashes={name:sha256((HERE/name).read_bytes()).hexdigest() for name in names}
    prepared=np.load(HERE/'de_a6_triple_target_prepare.npz')
    original=np.asarray([prepared[k] for k in ('a','b','c')],dtype=np.uint16)
    full_report=report('de_a6_triple_target_replay.out')
    full_order=int(full_report['order'])
    assert full_order==prod(full_report['orbit_lengths'])
    stages=[];parent=None;parent_q=None;last_order=None;last_certificate=None
    for stage,stem in enumerate(stems):
        cert=read_certificate(HERE/(stem+'.bin'));verify_words(cert)
        result=full_report if stage==0 else report(stem+'.out')
        order=int(result['order']);assert order==prod(result['orbit_lengths'])
        assert cert['degree']==2221 and len(cert['strong'])==result['strong_generators']
        assert len(cert['nodes'])==result['word_DAG_nodes']
        assert np.array_equal(cert['base'],result['base'])
        assert cert['derived']==(stage>0)
        if stage<=1:
            assert np.array_equal(cert['original'],original)
            qi=qoriginal
        else:
            saved=json.loads((HERE/(stem+'_input.json')).read_text())
            inputs=np.load(HERE/(stem+'_input.npz'))
            assert saved['source_certificate']==stems[stage-1]+'.bin'
            assert np.array_equal(saved['source_word_nodes'],parent['words'])
            literal=saved['one_based_signed_strong_generator_words']
            actual=words_in_generators(literal,parent['strong'])
            qi=words_in_generators(literal,parent_q)
            assert np.array_equal(actual,cert['original'])
            assert np.array_equal(actual,inputs['generators'])
            assert np.array_equal(qi,inputs['quotient_generators'])
            assert np.array_equal(parent_q,inputs['parent_quotient_strong_values'])
            assert permutation_order(qi)==permutation_order(parent_q)
        qdict=evaluate(cert['nodes'],qi,cert['words'])
        qs=np.asarray([qdict[int(w)] for w in cert['words']],dtype=np.uint16)
        quotient_order=permutation_order(qs)
        index=full_order//order
        assert full_order%order==0 and index==expected_indices[stage]
        expected_q=small['small_complete_derived_orders'][stage] if stage<=4 else 1
        assert quotient_order==expected_q
        assert order==full_order//20736*quotient_order
        if stage>=4:
            assert np.array_equal(qs,np.broadcast_to(np.arange(105),(len(qs),105)))
        stages.append({'stage':stage,'order':str(order),'index':index,
                       'specified_small_quotient_image_order':quotient_order,
                       'strong_generator_count':len(cert['strong']),
                       'literal_word_DAG_nodes':len(cert['nodes']),
                       'complete_final_Schreier_relations':result['complete_final_Schreier_relations'],
                       'all_strong_words_independently_replayed':True,
                       'all_interstage_original_words_reconstructed':stage>=2,
                       'derived_inclusion_in_actual_parent':stage>0,
                       'equals_full_preimage_of_small_derived_group_by_order_bounds':True})
        if stage==5:
            assert order==last_order
            assert len(last_certificate['strong'])>0
        parent,parent_q,last_order,last_certificate=cert,qs,order,cert
    old=report('de_a6_gl_target.out');old_order=int(old['order'])
    assert full_order==old_order*8*3**55
    oldmath=json.loads((HERE/'de_a6_gl_target_certificate.json').read_text())
    maps=json.loads((HERE/'de_a6_triple_target_old_maps.json').read_text())
    assert maps['status'].startswith('PASS') and oldmath['status'].startswith('PASS')
    full_target_order=full_order*1080**53*120**19
    factorization={2:406,3:271,5:117,7:8,11:3,13:2}
    assert full_target_order==prod(p**e for p,e in factorization.items())
    out={'status':'PASS_COMPLETE_TRIPLE_SIGNED_TARGET_AND_MAXIMAL_SOLVABLE_MAP',
         'quotient_degree':2221,'quotient_order':str(full_order),
         'actual_perfect_free_kernel_order':str(1080**53*120**19),
         'actual_full_joint_target_order':str(full_target_order),
         'actual_full_joint_target_factorization':factorization,
         'old_781_point_quotient_order':str(old_order),
         'relative_quotient_kernel_order':str(8*3**55),
         'full_target_kernel_over_old_A6_signed_target_order':str(8*3**108),
         'specified_solvable_quotient':'S_L times ASL2(F3)',
         'specified_solvable_quotient_order':20736,
         'all_actual_derived_indices':[s['index'] for s in stages],
         'all_stages':stages,
         'terminal_perfection_from_equal_order_and_literal_derived_inclusion':True,
         'terminal_group_is_entire_specified_quotient_kernel':True,
         'full_kernel_including_perfect_free_factors_is_perfect':True,
         'maximal_solvable_quotient_is_the_specified_literal_map':True,
         'no_parent_generation_assertion_for_selected_mixture_words':True,
         'old_T23_maps_are_verified_by_separate_literal_comparisons':True,
         'source_and_corrected_joint_generation_use_the_printed_Goursat_proof':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_triple_target_certificate.npz',
        actual_quotient_generator_permutations=qoriginal,
        terminal_small_quotient_strong_values=parent_q,
        terminal_strong_word_nodes=parent['words'])
    (HERE/'de_a6_triple_target_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/name).read_bytes()).hexdigest()==value for name,value in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
