#!/usr/bin/env python3
"""Isolated root replay of every exact E72 integral and induced map."""
from pathlib import Path
from hashlib import sha256
import ast
import json
import shutil
import subprocess
import sys
import time
import numpy as np

ROOT = Path(__file__).resolve().parent.parent


def main():
    started = time.monotonic()
    out = ROOT / 'research/root_E72_replay'
    out.mkdir(exist_ok=False)
    code = out / 'code'; code.mkdir()
    pending = ['de_wajnryb_homology.py']
    modules = set()
    while pending:
        name = pending.pop()
        if name in modules:
            continue
        modules.add(name)
        tree = ast.parse((ROOT / 'code' / name).read_text())
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [a.name.split('.')[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = [node.module.split('.')[0]]
            for module in names:
                filename = module + '.py'
                if (ROOT / 'code' / filename).is_file():
                    pending.append(filename)
    source = ROOT / 'code/de_wajnryb_homology.json'
    old = json.loads(source.read_text())
    files = modules | set(old['input_sha256'])
    protected = {'code/' + name: sha256((ROOT / 'code' / name).read_bytes()).hexdigest()
                 for name in files | {'de_wajnryb_homology.json', 'de_wajnryb_homology.npz'}}
    proof = 'sections/E_wajnryb_homology_agent.tex'
    protected[proof] = sha256((ROOT / proof).read_bytes()).hexdigest()
    assert protected[proof] == '781213236c19c551250b4cfb8fecacb2e7192434af2990c0845fd2ae2dab022c'
    for name in files:
        shutil.copy2(ROOT / 'code' / name, code / name)
    with (code / 'de_wajnryb_homology.out').open('w') as stdout, (code / 'de_wajnryb_homology.err').open('w') as stderr:
        subprocess.run([sys.executable, 'de_wajnryb_homology.py'], cwd=code,
                       stdout=stdout, stderr=stderr, check=True)
    got = json.loads((code / 'de_wajnryb_homology.json').read_text())
    for obj, base in [(old, ROOT / 'code'), (got, code)]:
        for name, expected in obj['input_sha256'].items():
            assert sha256((base / name).read_bytes()).hexdigest() == expected
    old_seconds, new_seconds = old.pop('seconds'), got.pop('seconds')
    assert old == got
    a = np.load(ROOT / 'code/de_wajnryb_homology.npz')
    b = np.load(code / 'de_wajnryb_homology.npz')
    assert a.files == b.files
    for k in a.files:
        assert a[k].dtype == b[k].dtype and a[k].shape == b[k].shape and np.array_equal(a[k], b[k]), k
    assert all(sha256((ROOT / name).read_bytes()).hexdigest() == h for name, h in protected.items())
    result = {'status': 'PASS_COMPLETE_ISOLATED_E72_ROOT_REPLAY',
              'full_root_proof_and_program_read': True,
              'all_integral_and_90_induced_coordinate_identities_exact': True,
              'all_mathematical_JSON_and_NPZ_values_shapes_dtypes_exact': True,
              'all_fixed_input_hashes_validated': True,
              'protected_originals_unchanged': len(protected),
              'proof_sha256': protected[proof],
              'source_sha256': protected['code/de_wajnryb_homology.py'],
              'old_calculation_seconds': old_seconds, 'rerun_calculation_seconds': new_seconds,
              'seconds': round(time.monotonic() - started, 6), 'protected_sha256': protected}
    (out / 'replay.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'protected_sha256'}, indent=2), flush=True)


if __name__ == '__main__':
    main()
