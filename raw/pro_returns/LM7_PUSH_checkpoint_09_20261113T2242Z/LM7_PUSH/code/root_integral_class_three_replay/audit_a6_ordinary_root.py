#!/usr/bin/env python3
"""Replay the complete ordinary A6 chief obstruction without changing inputs."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPLAY = HERE/'root_e24_binary_replay'
PROGRAMS = ('a_peripheral_a6_nielsen', 'a_peripheral_a6_ordinary')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    prior = json.loads((HERE/'audit_threeadic_a6_root.json').read_text())
    assert prior['all_passed'] and prior['original_artifacts_unchanged']
    protected = [p for p in HERE.iterdir() if p.is_file() and
                 (p.name.startswith('a_peripheral_a6_') or
                  p.name == 'a_peripheral_count.py')]
    before = {p.name: digest(p) for p in protected}
    for name in ('a_peripheral_count.py', 'a_peripheral_a6_outer.json'):
        assert (HERE/name).read_bytes() == (REPLAY/name).read_bytes(), name
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
        generated = REPLAY/(stem+'.json')
        row = {'program': stem+'.py', 'exit_code': run.returncode,
               'elapsed_seconds': round(time.time()-start, 3),
               'replay_output': str(output.relative_to(HERE)),
               'output_sha256': digest(output),
               'json_byte_identical': generated.exists() and
                   generated.read_bytes() == (HERE/(stem+'.json')).read_bytes()}
        rows.append(row)
        print(json.dumps(row), flush=True)
        if run.returncode or not row['json_byte_identical']:
            break
    result = {'programs': rows,
              'all_passed': len(rows) == len(PROGRAMS) and
                  all(r['exit_code'] == 0 and r['json_byte_identical'] for r in rows),
              'original_artifacts_unchanged': all(digest(HERE/n) == h for n,h in before.items()),
              'protected_sha256': before,
              'elapsed_seconds': round(time.time()-begin, 3)}
    (HERE/'audit_a6_ordinary_root.json').write_text(json.dumps(result, indent=2)+'\n')
    assert result['all_passed'] and result['original_artifacts_unchanged']
    print('ROOT_A6_ORDINARY_CHIEF_OBSTRUCTION_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
