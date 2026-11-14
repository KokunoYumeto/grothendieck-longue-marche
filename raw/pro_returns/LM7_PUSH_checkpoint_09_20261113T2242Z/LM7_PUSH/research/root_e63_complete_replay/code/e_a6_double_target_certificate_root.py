#!/usr/bin/env python3
"""Independent literal target words and the exact maximal solvable map.

All orders have separate complete Schreier replays.  This NumPy replay
checks every strong word, every mixture substitution, and every small
quotient value.  Orders plus literal derived inclusions identify the
entire preimages and prove terminal perfection, without assigning full
parent generation to the selected mixtures.
"""
from pathlib import Path
from hashlib import sha256
from math import prod
import json
import time
import numpy as np
from de_a6_schreier_certificate import read_certificate, verify_words
from de_a6_triple_base_prepare import evaluate
from de_a6_triple_source_certificate import report
from de_a6_triple_target_certificate import words_in_generators, permutation_order

HERE = Path(__file__).resolve().parent


def main():
    started = time.monotonic()
    continuation = json.loads((HERE/'e_a6_double_target_continue_root.json').read_text())
    assert continuation['final_stage'] == 4 and continuation['final_index'] == 96
    complete = json.loads((HERE/'e_a6_double_target_complete_replay_root.json').read_text())
    assert complete['status'].startswith('PASS')
    small = json.loads((HERE/'e_a6_double_target_quotient_root.json').read_text())
    qraw = np.load(HERE/'e_a6_double_target_quotient_root.npz')
    qoriginal = qraw['quotient_generator_permutations'].astype(np.uint16)
    assert permutation_order(qoriginal) == 96
    indices = small['small_complete_derived_indices'] + [96]
    assert indices == [1, 2, 6, 96, 96]
    stems = ['e_a6_double_target_root'] + [f'e_a6_double_target_derived{i}_root' for i in range(1, 5)]
    names = ['e_a6_double_target_continue_root.json', 'e_a6_double_target_prepare_root.npz',
             'e_a6_double_target_quotient_root.json', 'e_a6_double_target_quotient_root.npz',
             'e_a6_double_target_complete_replay_root.json', 'e_a6_double_target_old_maps_root.json', 'de_a6_gl_target.out',
             'de_a6_gl_target_certificate.json', 'de_a6_triple_target_certificate.py']
    for stage, stem in enumerate(stems):
        names += [stem+'.bin', stem+'.out', stem+'_independent.out']
        if stage >= 2:
            names += [stem+'_input.json', stem+'_input.npz']
    hashes = {n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    old_maps = json.loads((HERE/'e_a6_double_target_old_maps_root.json').read_text())
    assert old_maps['status'].startswith('PASS')
    prepared = np.load(HERE/'e_a6_double_target_prepare_root.npz')
    original = np.asarray([prepared[k] for k in ('a', 'b', 'c')], dtype=np.uint16)
    full = int(report(stems[0]+'.out')['order'])
    stages, parent, parent_q = [], None, None
    for stage, stem in enumerate(stems):
        cert = read_certificate(HERE/(stem+'.bin'))
        verify_words(cert)
        result = report(stem+'_independent.out')
        order = int(result['order'])
        assert order == prod(result['orbit_lengths'])
        assert cert['degree'] == 1209
        assert len(cert['strong']) == result['strong_generators']
        assert len(cert['nodes']) == result['word_DAG_nodes']
        assert np.array_equal(cert['base'], result['base'])
        assert cert['derived'] == (stage > 0)
        if stage <= 1:
            assert np.array_equal(cert['original'], original)
            qi = qoriginal
        else:
            saved = json.loads((HERE/(stem+'_input.json')).read_text())
            inputs = np.load(HERE/(stem+'_input.npz'))
            assert saved['source_certificate'] == stems[stage-1]+'.bin'
            assert np.array_equal(saved['source_word_nodes'], parent['words'])
            literal = saved['one_based_signed_strong_generator_words']
            actual = words_in_generators(literal, parent['strong'])
            qi = words_in_generators(literal, parent_q)
            assert np.array_equal(actual, cert['original'])
            assert np.array_equal(actual, inputs['generators'])
            assert np.array_equal(qi, inputs['quotient_generators'])
            assert np.array_equal(parent_q, inputs['parent_quotient_strong_values'])
            assert permutation_order(qi) == permutation_order(parent_q)
        qvalues = evaluate(cert['nodes'], qi, cert['words'])
        qs = np.asarray([qvalues[int(w)] for w in cert['words']], dtype=np.uint16)
        qorder = permutation_order(qs)
        assert full % order == 0 and full//order == indices[stage]
        assert qorder == (small['small_complete_derived_orders'][stage] if stage <= 3 else 1)
        assert order == full//96*qorder
        if stage >= 3:
            assert np.array_equal(qs, np.broadcast_to(np.arange(96), (len(qs), 96)))
        stages.append({
            'stage':stage, 'order':str(order), 'index':full//order,
            'actual_small_quotient_image_order':qorder,
            'strong_generator_count':len(cert['strong']),
            'literal_word_DAG_nodes':len(cert['nodes']),
            'complete_final_Schreier_relations':result['complete_final_Schreier_relations'],
            'all_strong_words_independently_replayed':True,
            'all_interstage_original_words_reconstructed':stage >= 2,
            'derived_inclusion_in_actual_parent':stage > 0,
            'equals_full_preimage_of_small_derived_group_by_order_bounds':True,
        })
        parent, parent_q = cert, qs
    assert stages[-1]['order'] == stages[-2]['order']
    old = int(report('de_a6_gl_target.out')['order'])
    assert full == old*2**98
    full_target = full*720**53*120**19
    factors = {2:554, 3:163, 5:117, 7:8, 11:3, 13:2}
    assert full_target == prod(p**e for p,e in factors.items())
    result = {
        'status':'PASS_COMPLETE_DOUBLE_A6_SIGNED_TARGET_AND_MAXIMAL_SOLVABLE_MAP',
        'quotient_degree':1209, 'quotient_order':str(full),
        'actual_perfect_free_kernel_order':str(720**53*120**19),
        'actual_full_joint_target_order':str(full_target),
        'actual_full_joint_target_factorization':factors,
        'old_781_point_quotient_order':str(old),
        'relative_quotient_kernel_order':str(2**98),
        'full_target_kernel_over_old_A6_signed_target_order':str(2**151),
        'specified_solvable_quotient':'S_L through the retained actual signed target projection',
        'specified_solvable_quotient_order':96,
        'all_actual_derived_indices':indices, 'all_stages':stages,
        'terminal_perfection_from_equal_order_and_literal_derived_inclusion':True,
        'terminal_group_is_entire_specified_quotient_kernel':True,
        'full_kernel_including_perfect_free_factors_is_perfect':True,
        'maximal_solvable_quotient_is_the_specified_literal_map':True,
        'no_parent_generation_assertion_for_selected_mixture_words':True,
        'input_sha256':hashes, 'seconds':round(time.monotonic()-started, 3),
    }
    np.savez_compressed(HERE/'e_a6_double_target_certificate_root.npz',
                        actual_quotient_generator_permutations=qoriginal,
                        terminal_small_quotient_strong_values=parent_q,
                        terminal_strong_word_nodes=parent['words'])
    (HERE/'e_a6_double_target_certificate_root.json').write_text(json.dumps(result, indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n,h in hashes.items())
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
