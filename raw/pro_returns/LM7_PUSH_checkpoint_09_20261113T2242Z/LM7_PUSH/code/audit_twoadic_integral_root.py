#!/usr/bin/env python3
"""Protected replay of the complete integral two-adic source calculations."""
from pathlib import Path
import ast
import hashlib
import json
import shutil
import subprocess
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
REPLAY = HERE/'root_e24_binary_replay'
PROGRAMS = ('bc_fermat_class_two_2adic_source',
            'bc_fermat_class_two_integral_family',
            'bc_fermat_class_two_2adic_norms')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mathematical(value):
    if isinstance(value, dict):
        return {k: mathematical(v) for k,v in value.items() if k != 'elapsed_seconds'}
    if isinstance(value, list):
        return [mathematical(v) for v in value]
    return value


def main():
    prior = json.loads((HERE/'audit_threeadic_a6_root.json').read_text())
    assert prior['all_passed'] and prior['original_artifacts_unchanged']
    pending, seen = list(PROGRAMS), set()
    while pending:
        name = pending.pop()
        if name in seen:
            continue
        source = HERE/(name+'.py')
        if not source.exists():
            continue
        seen.add(name)
        for node in ast.walk(ast.parse(source.read_text())):
            names = [a.name for a in node.names] if isinstance(node, ast.Import) else (
                [node.module] if isinstance(node, ast.ImportFrom) and node.module else [])
            pending.extend(n for n in names if (HERE/(n+'.py')).exists())
    protected = [p for p in HERE.iterdir() if p.is_file() and
                 any(p.name.startswith(n+'.') for n in seen)]
    before = {p.name: digest(p) for p in protected}
    for stem in sorted(seen):
        source, target = HERE/(stem+'.py'), REPLAY/(stem+'.py')
        if stem in PROGRAMS:
            assert not target.exists(), target
        if not target.exists():
            shutil.copy2(source, target)
        assert source.read_bytes() == target.read_bytes(), stem
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
        for suffix in ('.json', '.npz'):
            original, replay = HERE/(stem+suffix), REPLAY/(stem+suffix)
            key = suffix[1:]+'_mathematical_equal'
            row[key] = False
            if replay.exists() and original.exists():
                if suffix == '.json':
                    row[key] = mathematical(json.loads(original.read_text())) == mathematical(json.loads(replay.read_text()))
                else:
                    with np.load(original) as a, np.load(replay) as b:
                        row[key] = set(a.files) == set(b.files) and all(np.array_equal(a[k],b[k]) for k in a.files)
        rows.append(row)
        print(json.dumps(row), flush=True)
        if run.returncode or not row['json_mathematical_equal'] or not row['npz_mathematical_equal']:
            break
    result = {'programs': rows,
              'all_passed': len(rows) == len(PROGRAMS) and
                  all(r['exit_code'] == 0 and r['json_mathematical_equal'] and
                      r['npz_mathematical_equal'] for r in rows),
              'original_artifacts_unchanged': all(digest(HERE/n) == h for n,h in before.items()),
              'protected_sha256': before,
              'elapsed_seconds': round(time.time()-begin, 3)}
    (HERE/'audit_twoadic_integral_root.json').write_text(json.dumps(result, indent=2)+'\n')
    assert result['all_passed'] and result['original_artifacts_unchanged']
    print('ROOT_TWOADIC_INTEGRAL_SOURCE_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
