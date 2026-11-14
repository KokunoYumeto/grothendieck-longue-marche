"""Fresh root replay of the frozen E122 arithmetic witness subset."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'research_e122'
MANIFEST = AUTHOR / 'ledger/e122_witness_subset_manifest.json'
MANIFEST_SHA = '4a1053db7d0cd6e5ff89e5f29ff4d77d1b188d5d610640bc2e323ce29fa1b28f'
GP = HERE.parent / 'research_e52/vendor/pari-2.19.0/Olinux-x86_64/gp-dyn'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert sha(MANIFEST) == MANIFEST_SHA
    manifest = json.loads(MANIFEST.read_text())

    def check_frozen():
        assert sha(MANIFEST) == MANIFEST_SHA
        for name, record in manifest['files'].items():
            p = AUTHOR / name
            assert sha(p) == record['sha256'], name
            assert p.stat().st_size == record['bytes'], name

    check_frozen()
    frozen = HERE / 'witness_author_freeze'
    fresh = HERE / 'witness_fresh'
    assert not frozen.exists() and not fresh.exists()
    for name in manifest['files']:
        dest = frozen / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(AUTHOR / name, dest)
    (frozen / 'ledger').mkdir()
    shutil.copy2(MANIFEST, frozen / 'ledger' / MANIFEST.name)
    sources = [
        'code/e53_higher_local.gp',
        'code/e53_upper_witness_verify.gp',
        'code/e53_literal_unit_ring.py',
    ]
    inputs = [name for name in manifest['files'] if name.startswith('inputs/')]
    assert len(inputs) == 3
    for name in sources + inputs:
        dest = fresh / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(frozen / name, dest)
    assert not list((fresh / 'code').glob('*.bin'))
    assert not list((fresh / 'code').glob('*.out'))

    stages = []
    for name in sources:
        source = fresh / name
        command = ([str(GP), '-fq', source.name] if source.suffix == '.gp'
                   else [sys.executable, source.name])
        output = source.with_suffix('.out')
        error = source.with_suffix('.err')
        with output.open('wb') as out, error.open('wb') as err:
            run = subprocess.run(command, cwd=fresh / 'code', stdout=out, stderr=err)
        assert run.returncode == 0, (name, run.returncode, error.read_text())
        stderr_lines = error.read_text().splitlines()
        bad = [line for line in stderr_lines if line.strip() and not (
            line.strip().startswith('***   Warning: new stack size = ') or
            line.strip().startswith('***   Warning: new maximum stack size = '))]
        assert not bad, (name, bad)
        expected = frozen / Path(name).with_suffix('.out')
        assert output.read_bytes() == expected.read_bytes(), name
        if source.suffix == '.gp':
            records = [json.loads(line) for line in output.read_text().splitlines()
                       if line.startswith('{')]
            assert records[-1]['status'] == 'PASS'
        else:
            assert json.loads(output.read_text())['status'] == 'PASS'
        stages.append({
            'source': name, 'source_sha256': sha(source),
            'command': command, 'exit_code': run.returncode,
            'stdout_sha256': sha(output), 'stdout_bytes': output.stat().st_size,
            'stderr_sha256': sha(error), 'stderr_bytes': error.stat().st_size,
            'whole_stdout_byte_identical': True,
        })
        print('PASS fresh stage: ' + name, flush=True)

    result_path = fresh / 'code/e53_literal_unit_ring.json'
    assert result_path.read_bytes() == (frozen / 'code/e53_literal_unit_ring.json').read_bytes()
    result = json.loads(result_path.read_text())
    check_frozen()
    report = {
        'status': 'PASS_ROOT_E122_FROZEN_WITNESS_REPLAY',
        'manifest_sha256': MANIFEST_SHA,
        'frozen_files_before_and_after': len(manifest['files']),
        'stages': stages,
        'cube_identities': len(result['independent_exact_relative_cube_identities']),
        'complete_lower_basis_norm_identities': len(result['independent_exact_relative_norm_identities']),
        'three_new_root_indices': result['three_new_root_indices'],
        'five_character_determinant': result['five_character_determinant'],
        'norm_lattice_index': result['norm_lattice_index'],
        'whole_python_certificate_byte_identical': True,
        'excluded_fields': [],
        'scope': ('Fresh local norm calculation, fresh literal unit/divisor/positive-character '
                  'calculation, and independent rational relative-ring cube/norm arithmetic. '
                  'No upper NF/BNF or root-search output was loaded. The frozen E119 lower '
                  'certificate is an input. The final all-level proof is reviewed separately.'),
    }
    (HERE / 'witness_replay.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
