"""Independently rerun all three frozen E95 programs and compare complete bytes."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
AUTHOR = ROOT / 'research_e95'
SOURCE = ROOT / 'LM7_FERMAT_TOWER/code'
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path = AUTHOR / 'ledger/e_toric_wild_manifest.json'
manifest = json.loads(manifest_path.read_text())
for name, row in manifest['files'].items():
    assert digest(AUTHOR / name) == row['sha256'], name
inputs = {}
for name in ['a_cusp_kummer', 'a_toric_wild']:
    result = json.loads((AUTHOR / 'code' / (name + '.json')).read_text())
    for name, checksum in result['input_hashes'].items():
        assert digest(SOURCE / name) == checksum, name
        inputs[name] = checksum
(HERE / 'code').mkdir(exist_ok=True)
stages = []
for name in ['a_cusp_kummer', 'a_toric_wild', 'a_toric_residues']:
    original = AUTHOR / 'code' / (name + '.py')
    copied = HERE / 'code' / original.name
    assert not copied.exists(), 'Fresh reconstruction already exists: ' + name
    shutil.copyfile(original, copied)
    command = [sys.executable, str(copied)]
    if name != 'a_toric_residues':
        command += ['--source-code', str(SOURCE)]
    with copied.with_suffix('.out').open('w') as output:
        proc = subprocess.run(command, cwd=HERE, stdout=output,
                              stderr=subprocess.STDOUT, check=False)
    stages.append({'program': copied.name, 'returncode': proc.returncode,
                   'sha256': digest(copied)})
    (HERE / 'run_status.json').write_text(json.dumps(stages, indent=2) + '\n')
    assert proc.returncode == 0, stages[-1]
    print('PASS fresh execution: ' + name, flush=True)
comparisons = []
for name in ['a_cusp_kummer', 'a_toric_wild', 'a_toric_residues']:
    for suffix in ['.json', '.out']:
        a = AUTHOR / 'code' / (name + suffix)
        b = HERE / 'code' / a.name
        same = a.read_bytes() == b.read_bytes()
        comparisons.append({'file': a.name, 'author_sha256': digest(a),
                            'root_sha256': digest(b), 'byte_equal': same})
        assert same, a.name
for name, checksum in inputs.items():
    assert digest(SOURCE / name) == checksum, 'Changed dependency: ' + name
record = {'status': 'PASS', 'frozen_manifest_sha256': digest(manifest_path),
          'section_sha256': digest(AUTHOR / 'sections/E_toric_wild_obstruction.tex'),
          'complete_byte_comparisons': comparisons, 'exclusions': [],
          'read_only_input_sha256': inputs, 'stages': stages,
          'all_dependencies_unchanged_after_execution': True}
(HERE / 'comparison.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2), flush=True)
