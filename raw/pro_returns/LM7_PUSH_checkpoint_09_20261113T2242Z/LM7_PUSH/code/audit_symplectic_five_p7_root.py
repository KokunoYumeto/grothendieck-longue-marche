#!/usr/bin/env python3
"""Complete, isolated E51 replay from the frozen authoritative manifest.

Every declared input hash is checked in its own location.  All numerical
and word data are compared, allowing only elapsed-time metadata to vary.
Noncanonical permutation generating lists are compared by both inclusions.
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
    manifest_path = ROOT / 'research/E51_authoritative_manifest.json'
    manifest = json.loads(manifest_path.read_text())
    protected = {}
    for key in ('files', 'read_only_external_input_hashes',
                'local_python_import_hashes'):
        for name, expected in manifest[key].items():
            assert digest(ROOT / name) == expected, ('frozen input', name)
            assert name not in protected or protected[name] == expected
            protected[name] = expected
    protected['research/E51_authoritative_manifest.json'] = digest(manifest_path)
    protected['code/audit_symplectic_five_p5_root.py'] = digest(
        HERE / 'audit_symplectic_five_p5_root.py')
    steps = [Path(name).stem for name in manifest['replay_order']]
    outputs = {stem: [] for stem in steps}
    generated = set()
    for name in manifest['files']:
        path = Path(name)
        if path.parts[0] != 'code' or path.suffix not in ('.json', '.npz'):
            continue
        matches = [stem for stem in steps
                   if path.stem == stem or path.stem.startswith(stem + '_')]
        assert matches, name
        owner = max(matches, key=len)
        outputs[owner].append(path.name)
        generated.add(path.name)
    replay = HERE / 'root_symplectic_five_p7_replay'
    replay.mkdir(exist_ok=False)
    copied = []
    for name in protected:
        path = Path(name)
        if path.parts[0] != 'code' or path.name in generated:
            continue
        if path.suffix not in ('.py', '.json', '.npz', '.bin', '.input'):
            continue
        shutil.copy2(ROOT / name, replay / path.name)
        copied.append(path.name)
    rows = []
    for stem in steps:
        tick = time.time()
        with (replay / (stem + '_root_check.out')).open('x') as log:
            run = subprocess.run([sys.executable, '-u', str(replay / (stem + '.py'))],
                                 cwd=replay, stdout=log, stderr=subprocess.STDOUT)
        assert run.returncode == 0, (stem, run.returncode)
        comparisons = []
        for name in sorted(outputs[stem]):
            old, new = HERE / name, replay / name
            assert new.is_file(), ('missing output', name)
            if old.suffix == '.json':
                a, b = json.loads(old.read_text()), json.loads(new.read_text())
                provenance = set()
                for directory, data in ((HERE, a), (replay, b)):
                    for source, expected in data.get('input_sha256', {}).items():
                        assert digest(directory / source) == expected, (name, source)
                        provenance.add(source)
                assert mathematical(a) == mathematical(b), ('JSON mismatch', name)
                comparisons.append({'file': name, 'mathematical_records_equal': True,
                                    'declared_hashes_verified': sorted(provenance)})
            else:
                comparisons.append({'file': name,
                                    'arrays': compare_arrays(old, new)})
        row = {'program': stem + '.py', 'exit_code': 0,
               'all_comparisons_passed': True, 'outputs': comparisons,
               'seconds': round(time.time() - tick, 3)}
        rows.append(row)
        print(json.dumps({k: v for k, v in row.items() if k != 'outputs'}), flush=True)
    assert all(digest(ROOT / name) == expected for name, expected in protected.items())
    out = {'all_passed': True, 'steps': rows,
           'original_artifacts_unchanged': True, 'copied_input_files': sorted(copied),
           'protected_sha256': protected, 'seconds': round(time.time() - start, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
    print('ROOT_PRIME_SEVEN_SYMPLECTIC_COMPLETE_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
