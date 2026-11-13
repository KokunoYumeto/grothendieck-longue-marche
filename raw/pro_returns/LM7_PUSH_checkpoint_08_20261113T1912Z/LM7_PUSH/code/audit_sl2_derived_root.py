#!/usr/bin/env python3
"""Exact SL2 derived replay with independent source-expression membership checks."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import time
import numpy as np
from audit_sl2_source_root import digest, mathematical

HERE = Path(__file__).resolve().parent
REPLAY = HERE/'root_e24_binary_replay'
EXPECTED = REPLAY/'expected_sl2'
PROGRAMS = ('de_lifted_schreier_control',
            'de_ferrari_sl2_5_derived_strict_root',
            'de_ferrari_sl2_5_coinvariants')


def main():
    prior = json.loads((HERE/'audit_sl2_source_resolution_root.json').read_text())
    assert prior['all_passed'] and prior['original_artifacts_unchanged']
    protected = [p for p in HERE.iterdir() if p.is_file() and
                 (p.name.startswith('de_ferrari_sl2_5_') or
                  p.name.startswith('de_lifted_schreier')) and
                 p.name != 'de_ferrari_sl2_5_derived_replay.out']
    before = {p.name: digest(p) for p in protected}
    for stem in (*PROGRAMS, 'de_ferrari_sl2_5_derived_replay'):
        target = REPLAY/(stem+'.py')
        assert not target.exists(), target
        shutil.copy2(HERE/(stem+'.py'), target)
    rows, begin = [], time.time()
    for stem in PROGRAMS:
        start = time.time()
        output = REPLAY/(stem+'_root_check.out')
        command = [sys.executable, '-u', str(REPLAY/(stem+'.py'))]
        if stem == 'de_ferrari_sl2_5_derived_strict_root':
            command += ['--expected-dir', str(EXPECTED)]
        with output.open('x') as stream:
            run = subprocess.run(command, cwd=REPLAY, stdout=stream, stderr=subprocess.STDOUT)
        row = {'program': stem+'.py', 'exit_code': run.returncode,
               'elapsed_seconds': round(time.time()-start, 3),
               'replay_output': str(output.relative_to(HERE)),
               'output_sha256': digest(output), 'mathematical_certificate_verified': False}
        if run.returncode == 0:
            if stem == 'de_ferrari_sl2_5_derived_strict_root':
                original = mathematical(json.loads((EXPECTED/'de_ferrari_sl2_5_derived.json').read_text()))
                fresh = mathematical(json.loads((REPLAY/'de_ferrari_sl2_5_derived_replay.json').read_text()))
                comparison = all(fresh[k] == value for k,value in original.items())
                grammar = json.loads((REPLAY/(stem+'.json')).read_text())
                stages = [json.loads((REPLAY/('de_ferrari_sl2_5_'+suffix+'.json')).read_text())
                          for suffix in ('Nprime', 'Nprimeprime', 'Fprime')]
                row['mathematical_certificate_verified'] = bool(
                    comparison and fresh['all_stages_reconstructed_and_completely_replayed'] and
                    len(grammar) == 3 and
                    all(g['all_chosen_words_are_actual_derived_words'] for g in grammar) and
                    all(s['all_chosen_component_and_permutation_arrays_verified'] and
                        s['complete_kernel_equals_supplied_certificate_in_both_directions'] and
                        s['all_saved_relator_words_independently_replayed'] for s in stages))
                row['chosen_source_membership_checks'] = grammar
            else:
                row['mathematical_certificate_verified'] = (
                    mathematical(json.loads((HERE/(stem+'.json')).read_text())) ==
                    mathematical(json.loads((REPLAY/(stem+'.json')).read_text())))
        rows.append(row)
        print(json.dumps(row), flush=True)
        if run.returncode or not row['mathematical_certificate_verified']:
            break
    result = {'programs': rows,
              'all_passed': len(rows) == len(PROGRAMS) and
                  all(r['exit_code'] == 0 and r['mathematical_certificate_verified'] for r in rows),
              'original_artifacts_unchanged': all(digest(HERE/n) == h for n,h in before.items()),
              'protected_sha256': before,
              'elapsed_seconds': round(time.time()-begin, 3)}
    (HERE/'audit_sl2_derived_root.json').write_text(json.dumps(result, indent=2)+'\n')
    assert result['all_passed'] and result['original_artifacts_unchanged']
    print('ROOT_SL2_FERRARI_COMPLETE_DERIVED_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
