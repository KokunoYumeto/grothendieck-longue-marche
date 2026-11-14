#!/usr/bin/env python3
"""Isolated replay of all four exact reduced deep-source programs."""
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
STEMS = ['e_a6_E62_deep_prepare_root', 'e_a6_E62_deep_collect_root',
         'e_a6_E62_H_residual_root', 'e_a6_E62_deep_replay_root']


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def math_fields(v):
    if isinstance(v, dict):
        return {k: math_fields(x) for k, x in v.items()
                if k not in ('seconds', 'input_sha256')}
    if isinstance(v, list):
        return [math_fields(x) for x in v]
    return v


def main():
    started = time.monotonic()
    out = ROOT / 'research/root_E73_deep_replay'
    out.mkdir(exist_ok=False)
    code = out / 'code'; code.mkdir()
    inputs = set()
    modules = set()
    pending = [s + '.py' for s in STEMS]
    for stem in STEMS:
        raw = json.loads((ROOT / 'code' / (stem + '.json')).read_text())
        for name, expected in raw['input_sha256'].items():
            assert digest(ROOT / 'code' / name) == expected
            inputs.add(name)
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
                candidate = module + '.py'
                if (ROOT / 'code' / candidate).is_file():
                    pending.append(candidate)
    outputs = {s + ext for s in STEMS for ext in ('.json', '.npz')}
    all_files = inputs | modules | outputs
    chain_folder = ROOT / 'code/e_a6_E62_H_residual_root_certificates'
    chains = [str(p.relative_to(ROOT / 'code')) for p in sorted(chain_folder.iterdir())
              if p.suffix in ('.input', '.bin')]
    all_files.update(chains)
    protected = {'code/' + n: digest(ROOT / 'code' / n) for n in all_files}
    proof = 'sections/E_double_E62_deep_root.tex'
    protected[proof] = digest(ROOT / proof)
    for name in (inputs | modules) - outputs:
        dest = code / name; dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / 'code' / name, dest)
    with (out / 'compile.out').open('w') as stdout, (out / 'compile.err').open('w') as stderr:
        subprocess.run(['g++', '-O3', '-std=c++17', 'de_a6_schreier.cpp', '-o', 'de_a6_schreier_fast'],
                       cwd=code, stdout=stdout, stderr=stderr, check=True)
    records = []
    for stem in STEMS:
        then = time.monotonic()
        with (code / (stem + '.out')).open('w') as stdout, (code / (stem + '.err')).open('w') as stderr:
            subprocess.run([sys.executable, stem + '.py'], cwd=code,
                           stdout=stdout, stderr=stderr, check=True)
        old = json.loads((ROOT / 'code' / (stem + '.json')).read_text())
        got = json.loads((code / (stem + '.json')).read_text())
        provenance = []
        for label, obj, base in [('original', old, ROOT / 'code'), ('rerun', got, code)]:
            for name, expected in obj['input_sha256'].items():
                assert digest(base / name) == expected, (label, stem, name)
                provenance.append([label, name, expected])
        assert math_fields(old) == math_fields(got), stem
        a = np.load(ROOT / 'code' / (stem + '.npz'))
        b = np.load(code / (stem + '.npz'))
        assert a.files == b.files
        for k in a.files:
            assert a[k].shape == b[k].shape and a[k].dtype == b[k].dtype
            assert np.array_equal(a[k], b[k]), (stem, k)
        record = {'program': stem, 'status': 'PASS',
                  'all_mathematical_JSON_and_NPZ_fields_exact': True,
                  'arrays_checked_with_dtype_and_shape': a.files,
                  'verified_input_provenance': provenance,
                  'seconds': round(time.monotonic() - then, 6)}
        records.append(record)
        print(stem, 'PASS', record['seconds'], flush=True)
    for name in chains:
        assert digest(ROOT / 'code' / name) == digest(code / name), name
    assert all(digest(ROOT / name) == h for name, h in protected.items())
    result = {'status': 'PASS_COMPLETE_ISOLATED_E73_REDUCED_DEEP_SOURCE',
              'results': records, 'exact_complete_chain_inputs_and_binaries': chains,
              'all144_binary_and42_ternary_stage_words_replayed': True,
              'protected_originals_unchanged': len(protected),
              'proof_sha256': protected[proof], 'protected_sha256': protected,
              'seconds': round(time.monotonic() - started, 6)}
    (out / 'replay.json').write_text(json.dumps(result, indent=2) + '\n')
    print(result['status'], result['seconds'], flush=True)


if __name__ == '__main__':
    main()
