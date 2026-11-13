#!/usr/bin/env python3
"""Isolated replay of the exact E48 quotient maps and all complete fibres.

The preceding independent full-chain audit is required.  These programs
reconstruct the actual quotient actions, both module layers, and every
old-word/correction comparison.  Legacy dependency main programs are not run.
"""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import time
from audit_symplectic_five_p5_root import digest, mathematical, compare_arrays

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def main():
    start = time.time()
    preceding = json.loads((HERE / 'audit_a6_full_chains_root.json').read_text())
    assert preceding['all_passed'] and preceding['original_artifacts_unchanged']
    manifest = json.loads((HERE / 'de_a6_e48_manifest.json').read_text())
    protected = {name: row['sha256'] for name, row in manifest['records'].items()}
    protected.update({name: row['sha256'] for name, row in manifest['documents'].items()})
    protected['code/de_a6_e48_manifest.json'] = digest(HERE / 'de_a6_e48_manifest.json')
    protected['code/audit_a6_full_chains_root.json'] = digest(HERE / 'audit_a6_full_chains_root.json')
    for name, expected in protected.items():
        assert digest(ROOT / name) == expected, ('frozen file', name)
    replay = HERE / 'root_a6_full_quotient_replay'
    replay.mkdir(exist_ok=False)
    for name in manifest['records']:
        path = Path(name)
        assert path.parts[0] == 'code' and len(path.parts) == 2
        shutil.copy2(ROOT / name, replay / path.name)
    for stem in ('de_a6_subgroup_checks', 'de_a6_quotient',
                 'de_a6_module', 'de_a6_binary_module'):
        with (replay / (stem + '_compile_root.out')).open('x') as log:
            p = subprocess.run(['g++', '-std=c++17', '-O3', stem + '.cpp', '-o', stem],
                               cwd=replay, stdout=log, stderr=subprocess.STDOUT)
        assert p.returncode == 0, stem
    rows = []

    def execute(label, command, outputs):
        tick = time.time()
        for name in outputs:
            path = replay / name
            if path.exists():
                path.unlink()
        with (replay / (label + '_quotient_root_check.out')).open('x') as log:
            p = subprocess.run(command, cwd=replay, stdout=log, stderr=subprocess.STDOUT)
        assert p.returncode == 0, (label, p.returncode)
        comparisons = []
        for name in outputs:
            old, new = HERE / name, replay / name
            assert new.is_file(), ('missing regenerated output', name)
            if old.suffix == '.json':
                a, b = json.loads(old.read_text()), json.loads(new.read_text())
                provenance = set()
                for directory, record in ((HERE, a), (replay, b)):
                    for source, expected in record.get('input_sha256', {}).items():
                        assert digest(directory / source) == expected, (name, source)
                        provenance.add(source)
                assert mathematical(a) == mathematical(b), ('JSON', name)
                comparisons.append({'file': name, 'mathematical_records_equal': True,
                                    'declared_hashes_verified': sorted(provenance)})
            elif old.suffix == '.npz':
                comparisons.append({'file': name, 'arrays': compare_arrays(old, new)})
            else:
                assert old.read_bytes() == new.read_bytes(), ('literal generated input', name)
                comparisons.append({'file': name, 'literally_equal': True})
        row = {'program': label, 'exit_code': 0, 'all_comparisons_passed': True,
               'outputs': comparisons, 'seconds': round(time.time() - tick, 3)}
        rows.append(row)
        Path(__file__).with_suffix('.partial.json').write_text(
            json.dumps({'completed_steps': rows}, indent=2) + '\n')
        print(json.dumps({k: v for k, v in row.items() if k != 'outputs'}), flush=True)

    cpp_steps = [
        ('residual_normal', ['de_a6_subgroup_checks', 'de_a6_schreier_residual.bin',
                            'de_a6_schreier_full_ordered.input', 'de_a6_schreier_residual_normal.json', 'normal'],
         ['de_a6_schreier_residual_normal.json']),
        ('source_mod_N', ['de_a6_quotient', 'de_a6_schreier_N.bin',
                          'de_a6_schreier_full_ordered.input', 'de_a6_source_mod_N.json', '72'],
         ['de_a6_source_mod_N.json']),
        ('ternary_module', ['de_a6_module', 'de_a6_schreier_Fprimecompact.bin',
                            'de_a6_schreier_Fprimeprime.bin', 'de_a6_schreier_full_ordered.input',
                            'de_a6_module_basis.input', 'de_a6_module.json'],
         ['de_a6_module.json']),
        ('residual_quotient', ['de_a6_quotient', 'de_a6_schreier_residual.bin',
                              'de_a6_schreier_Fprimeprime_all.input', 'de_a6_residual_quotient.json', '64'],
         ['de_a6_residual_quotient.json']),
    ]
    for label, command, outputs in cpp_steps:
        command[0] = str(replay / command[0])
        execute(label, command, outputs)
    execute('binary_module_prepare', [sys.executable, 'de_a6_residual_module_prepare.py'],
            ['de_a6_binary_module_basis.input', 'de_a6_binary_module_V.input',
             'de_a6_binary_module_basis.json', 'de_a6_binary_module_basis.npz'])
    execute('binary_module', [str(replay / 'de_a6_binary_module'), 'de_a6_schreier_residual.bin',
                             'de_a6_schreier_Fprimeprime.bin', 'de_a6_binary_module_basis.input',
                             'de_a6_schreier_full_ordered.input', 'de_a6_schreier_Fprime_compact.input',
                             'de_a6_binary_module_V.input', 'de_a6_binary_module.json'],
            ['de_a6_binary_module.json'])
    for program in manifest['program_replay_order']:
        stem = Path(program).stem
        outputs = [stem + '.json']
        if (HERE / (stem + '.npz')).is_file():
            outputs.append(stem + '.npz')
        execute(stem, [sys.executable, '-u', program], outputs)
    assert all(digest(ROOT / name) == expected for name, expected in protected.items())
    out = {'all_passed': True, 'preceding_complete_chain_audit': 'audit_a6_full_chains_root.json',
           'steps': rows, 'original_artifacts_unchanged': True, 'protected_sha256': protected,
           'seconds': round(time.time() - start, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
    print('ROOT_A6_FULL_QUOTIENTS_AND_ALL_FIBRES_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
