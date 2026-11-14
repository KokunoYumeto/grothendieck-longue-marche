#!/usr/bin/env python3
"""Complete literal derived-word inclusions for the binary joint target.

The selected mixtures are only asserted to be words in their parent.
The final mathematical comparison uses their proved subgroup orders,
their actual S_L images, and the complete derived inclusions.
"""
from pathlib import Path
from hashlib import sha256
import json
import subprocess
import time
from de_a6_triple_source_certificate import report

HERE = Path(__file__).resolve().parent


def run(command, stem):
    with (HERE/(stem+'.out')).open('w') as out, (HERE/(stem+'.err')).open('w') as err:
        subprocess.run(command, cwd=HERE, stdout=out, stderr=err, check=True)


def main():
    started = time.monotonic()
    names = ['de_a6_triple_target_mix.py', 'de_a6_schreier.cpp',
             'e_a6_double_target_root.bin', 'e_a6_double_target_root.out',
             'e_a6_double_target_derived1_root.bin', 'e_a6_double_target_derived1_root.out',
             'e_a6_double_target_quotient_root.npz']
    hashes = {n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    full = int(report('e_a6_double_target_root.out')['order'])
    stages = []
    for stage in range(2, 9):
        parent = f'e_a6_double_target_derived{stage-1}_root'
        stem = f'e_a6_double_target_derived{stage}_root'
        assert not (HERE/(stem+'.bin')).exists()
        command = ['python', 'de_a6_triple_target_mix.py', parent+'.bin', stem]
        if stage == 2:
            command += ['--quotient-input', 'e_a6_double_target_quotient_root.npz',
                        '--quotient-key', 'quotient_generator_permutations']
        else:
            command += ['--quotient-input', parent+'_input.npz']
        run(command, stem+'_prepare')
        run([str(HERE/'e_a6_double_target_engine_root'), '--derived',
             stem+'.input', stem+'.bin'], stem)
        result = report(stem+'.out')
        order, previous = int(result['order']), int(report(parent+'.out')['order'])
        assert full % order == 0 and previous % order == 0
        row = {'stage':stage, 'order':str(order), 'index':full//order,
               'equal_to_containing_parent_order':order == previous,
               'complete_final_Schreier_relations':result['complete_final_Schreier_relations']}
        stages.append(row)
        print(json.dumps(row), flush=True)
        if order == previous:
            break
    else:
        raise AssertionError('No stable derived-word subgroup within eight stages.')
    result = {
        'status':'PASS_COMPLETE_DOUBLE_A6_TARGET_DERIVED_WORD_CHAIN',
        'new_stages':stages, 'final_stage':stages[-1]['stage'],
        'final_index':stages[-1]['index'],
        'actual_quotient_and_terminal_kernel_comparison_is_separate_certificate':True,
        'input_sha256':hashes, 'seconds':round(time.monotonic()-started, 3),
    }
    (HERE/'e_a6_double_target_continue_root.json').write_text(json.dumps(result, indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
