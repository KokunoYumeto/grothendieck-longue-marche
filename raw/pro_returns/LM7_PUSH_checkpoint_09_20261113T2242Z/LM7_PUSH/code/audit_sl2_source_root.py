#!/usr/bin/env python3
"""Protected replay of the SL2(F5) Ferrari model, full source and quotient maps."""
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
EXPECTED = REPLAY/'expected_sl2'
PROGRAMS = ('de_ferrari_sl2_5_model', 'de_ferrari_sl2_5_nielsen',
            'de_ferrari_sl2_5_source', 'de_ferrari_sl2_5_N',
            'de_ferrari_sl2_5_modular', 'de_ferrari_sl2_5_solvable')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mathematical(value):
    if isinstance(value, dict):
        return {k: mathematical(v) for k,v in value.items()
                if k not in ('elapsed_seconds', 'seconds', 'total_seconds')}
    if isinstance(value, list):
        return [mathematical(v) for v in value]
    return value


def main():
    assert not EXPECTED.exists()
    EXPECTED.mkdir()
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
                 (p.name.startswith('de_ferrari_sl2_5_') or
                  p.name.startswith('de_lifted_schreier') or
                  any(p.name == n+'.py' for n in seen))]
    before = {p.name: digest(p) for p in protected}
    for path in protected:
        if path.name.startswith('de_ferrari_sl2_5_') and path.suffix in ('.json','.npz'):
            shutil.copy2(path, EXPECTED/path.name)
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
        equal = True
        for suffix in ('.json', '.npz'):
            original, replay = EXPECTED/(stem+suffix), REPLAY/(stem+suffix)
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
    (HERE/'audit_sl2_source_root.json').write_text(json.dumps(result, indent=2)+'\n')
    assert result['all_passed'] and result['original_artifacts_unchanged']
    print('ROOT_SL2_FERRARI_SOURCE_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
