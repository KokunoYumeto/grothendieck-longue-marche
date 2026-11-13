#!/usr/bin/env python3
"""Isolated replay of E50's four complete actual-source certificates.

All literal maps, arrays, relations, and mathematical JSON values are
compared.  Runtime metadata are separated only after every declared
input digest is checked against its actual source file.  The original
programs and outputs remain read-only throughout the replay.
"""
from pathlib import Path
from hashlib import sha256
import ast
import json
import shutil
import subprocess
import sys
import time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup

HERE = Path(__file__).resolve().parent
STEPS = ['bc_symplectic_five_p5_' + s
         for s in ('residual', 'modular', 'signed', 'common')]
RUNTIME_KEYS = {'seconds', 'total_seconds', 'elapsed_seconds'}

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def mathematical(value):
    if isinstance(value, dict):
        return {k: mathematical(v) for k, v in value.items()
                if k not in RUNTIME_KEYS and k != 'input_sha256'}
    if isinstance(value, list):
        return [mathematical(v) for v in value]
    return value

def input_closure():
    scripts, names, todo = set(), set(), list(STEPS)
    while todo:
        stem = todo.pop()
        path = HERE / (stem + '.py')
        if stem in scripts or not path.is_file():
            continue
        scripts.add(stem)
        names.add(path.name)
        for node in ast.walk(ast.parse(path.read_text())):
            if isinstance(node, ast.Import):
                todo.extend(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                todo.append(node.module)
            elif isinstance(node, ast.Constant) and isinstance(node.value, str):
                literal = node.value
                if '/' not in literal and '\n' not in literal:
                    p = HERE / literal
                    if p.is_file() and p.suffix in ('.json', '.npz', '.bin', '.input', '.py'):
                        names.add(literal)
                        if p.suffix == '.py':
                            todo.append(p.stem)
    # These are generated in dependency order, never copied as replay inputs.
    names.difference_update(stem + ext for stem in STEPS for ext in ('.json', '.npz'))
    return sorted(names)

def compare_arrays(original, repeated):
    with np.load(original) as old, np.load(repeated) as new:
        assert set(old.files) == set(new.files), original.name
        records = []
        for name in old.files:
            a, b = old[name], new[name]
            if np.array_equal(a, b):
                records.append({'array': name, 'literally_equal': True})
                continue
            assert name.endswith('generators'), (original.name, name, a.shape, b.shape)
            assert a.ndim == b.ndim == 2 and a.shape[1] == b.shape[1]
            indices = np.arange(a.shape[1])
            assert np.all(np.sort(a, axis=1) == indices)
            assert np.all(np.sort(b, axis=1) == indices)
            A = PermutationGroup([Permutation(g.tolist()) for g in a])
            B = PermutationGroup([Permutation(g.tolist()) for g in b])
            assert all(B.contains(g) for g in A.generators)
            assert all(A.contains(g) for g in B.generators)
            ao, bo = int(A.order()), int(B.order())
            assert ao == bo
            records.append({'array': name, 'literally_equal': False,
                            'old_in_new': True, 'new_in_old': True,
                            'common_subgroup_order': ao})
        return records

def main():
    start = time.time()
    replay = HERE / 'root_symplectic_five_p5_replay'
    replay.mkdir(exist_ok=False)
    names = input_closure()
    protected = {name: digest(HERE / name) for name in names}
    for stem in STEPS:
        for ext in ('.py', '.json', '.npz', '.out'):
            path = HERE / (stem + ext)
            assert path.is_file(), path
            protected[path.name] = digest(path)
    for name in names:
        shutil.copy2(HERE / name, replay / name)
    rows = []
    for stem in STEPS:
        tick = time.time()
        with (replay / (stem + '_root_check.out')).open('x') as log:
            run = subprocess.run([sys.executable, str(replay / (stem + '.py'))],
                                 cwd=replay, stdout=log, stderr=subprocess.STDOUT)
        assert run.returncode == 0, stem
        original = json.loads((HERE / (stem + '.json')).read_text())
        repeated = json.loads((replay / (stem + '.json')).read_text())
        provenance = set()
        for directory, data in ((HERE, original), (replay, repeated)):
            for name, expected in data.get('input_sha256', {}).items():
                assert digest(directory / name) == expected, (stem, str(directory), name)
                provenance.add(name)
        assert mathematical(original) == mathematical(repeated), stem
        arrays = compare_arrays(HERE / (stem + '.npz'), replay / (stem + '.npz'))
        row = {'program': stem + '.py', 'exit_code': 0,
               'all_mathematical_records_equal': True,
               'all_declared_input_hashes_verified': True,
               'provenance_files': sorted(provenance),
               'NPZ_arrays': arrays, 'seconds': round(time.time() - tick, 3)}
        rows.append(row)
        print(json.dumps({k: v for k, v in row.items()
                          if k not in ('provenance_files', 'NPZ_arrays')}), flush=True)
    assert all(digest(HERE / name) == h for name, h in protected.items())
    out = {'all_passed': True, 'steps': rows,
           'original_artifacts_unchanged': True,
           'copied_input_files': names, 'protected_sha256': protected,
           'seconds': round(time.time() - start, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
    print('ROOT_PRIME_FIVE_SYMPLECTIC_SOURCE_AUDIT_PASS', flush=True)

if __name__ == '__main__':
    main()
