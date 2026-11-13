#!/usr/bin/env python3
"""Replay all exact exponent-three class-three representations, fibres and tower comparisons."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import time
import numpy as np
from audit_twoadic_integral_root import digest, mathematical

HERE = Path(__file__).resolve().parent
REPLAY = HERE/'root_e24_binary_replay'
PROGRAMS = ('bc_fermat_class_three_burnside',
            'bc_fermat_class_three_norms',
            'bc_fermat_class_three_tower_comparison')


def main():
    prior = json.loads((HERE/'audit_twoadic_integral_root.json').read_text())
    assert prior['all_passed'] and prior['original_artifacts_unchanged']
    protected = [p for p in HERE.iterdir() if p.is_file() and
                 (p.name.startswith('bc_fermat_class_two_') or
                  p.name.startswith('bc_fermat_class_three_') or
                  p.name.startswith('bc_cm_fermat_'))]
    before = {p.name: digest(p) for p in protected}
    for stem in PROGRAMS:
        target = REPLAY/(stem+'.py')
        assert not target.exists(), target
        shutil.copy2(HERE/(stem+'.py'), target)
    rows, begin = [], time.time()
    for stem in PROGRAMS:
        start = time.time()
        output = REPLAY/(stem+'_root_check.out')
        with output.open('x') as stream:
            run = subprocess.run([sys.executable, '-u', str(REPLAY/(stem+'.py'))],
                                 cwd=REPLAY, stdout=stream, stderr=subprocess.STDOUT)
        row = {'program': stem+'.py', 'exit_code': run.returncode,
               'elapsed_seconds': round(time.time()-start, 3),
               'replay_output': str(output.relative_to(HERE)),
               'output_sha256': digest(output)}
        equal = True
        for suffix in ('.json', '.npz'):
            original, replay = HERE/(stem+suffix), REPLAY/(stem+suffix)
            if not original.exists():
                continue
            key = suffix[1:]+'_mathematical_equal'
            row[key] = False
            if replay.exists():
                if suffix == '.json':
                    row[key] = mathematical(json.loads(original.read_text())) == mathematical(json.loads(replay.read_text()))
                else:
                    with np.load(original) as a, np.load(replay) as b:
                        row[key] = set(a.files) == set(b.files) and all(np.array_equal(a[k],b[k]) for k in a.files)
            equal = equal and row[key]
        row['all_artifacts_equal'] = equal
        rows.append(row)
        print(json.dumps(row), flush=True)
        if run.returncode or not equal:
            break
    result = {'programs': rows,
              'all_passed': len(rows) == len(PROGRAMS) and
                  all(r['exit_code'] == 0 and r['all_artifacts_equal'] for r in rows),
              'original_artifacts_unchanged': all(digest(HERE/n) == h for n,h in before.items()),
              'protected_sha256': before,
              'elapsed_seconds': round(time.time()-begin, 3)}
    (HERE/'audit_class_three_boundary_root.json').write_text(json.dumps(result, indent=2)+'\n')
    assert result['all_passed'] and result['original_artifacts_unchanged']
    print('ROOT_EXPONENT_THREE_CLASS_THREE_BOUNDARY_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
