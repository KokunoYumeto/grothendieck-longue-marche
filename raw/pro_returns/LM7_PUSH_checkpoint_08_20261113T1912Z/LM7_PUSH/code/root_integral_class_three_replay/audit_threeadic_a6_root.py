#!/usr/bin/env python3
"""Protected independent replay of the integral class-two tower and A6 data."""
from pathlib import Path
import ast
import hashlib
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPLAY = HERE/'root_e24_binary_replay'
PROGRAMS = ('bc_fermat_class_two_integral_model', 'bc_fermat_class_two_3adic_norms',
            'bc_fermat_class_two_3adic_tower', 'a_peripheral_a6_outer',
            'a_peripheral_a6_obstruction')


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    prior = json.loads((HERE/'audit_torsion_class_four_root.json').read_text())
    assert prior['all_passed'] and prior['original_artifacts_unchanged']
    protected = [p for p in HERE.iterdir() if p.is_file() and
                 any(p.name.startswith(s) for s in PROGRAMS)]
    before = {p.name: digest(p) for p in protected}
    pending, seen = [*PROGRAMS, 'a_peripheral_count'], set()
    while pending:
        name = pending.pop()
        if name in seen:
            continue
        source = HERE/(name+'.py')
        if not source.exists():
            continue
        seen.add(name)
        for node in ast.walk(ast.parse(source.read_text())):
            modules = []
            if isinstance(node, ast.Import):
                modules = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules = [node.module]
            pending.extend(m for m in modules if (HERE/(m+'.py')).exists())
    dependencies = {}
    for stem in sorted(seen):
        source, target = HERE/(stem+'.py'), REPLAY/(stem+'.py')
        if stem in PROGRAMS:
            assert not target.exists(), target
        if not target.exists():
            shutil.copy2(source, target)
        assert source.read_bytes() == target.read_bytes(), stem
        dependencies[source.name] = digest(source)
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
        rows.append(row)
        print(json.dumps(row), flush=True)
        if run.returncode:
            break
    result = {'programs': rows, 'all_passed': len(rows) == len(PROGRAMS) and
              all(r['exit_code'] == 0 for r in rows),
              'original_artifacts_unchanged': all(digest(HERE/n) == h for n, h in before.items()),
              'protected_sha256': before, 'dependency_sha256': dependencies,
              'elapsed_seconds': round(time.time()-begin, 3)}
    (HERE/'audit_threeadic_a6_root.json').write_text(json.dumps(result, indent=2)+'\n')
    assert result['all_passed'] and result['original_artifacts_unchanged']
    print('ROOT_THREEADIC_CLASS_TWO_AND_A6_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
