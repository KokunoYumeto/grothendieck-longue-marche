"""Fresh copied-source E96 reconstruction and complete byte comparison."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = ROOT / 'research_e96'
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = json.loads((SOURCE / 'ledger/e_zero_free_elliptic_manifest.json').read_text())
for row in manifest['files']:
    assert digest(SOURCE / row['path']) == row['sha256'], row['path']
for folder in ['code', 'inputs']:
    (HERE / folder).mkdir(exist_ok=True)
for name in ['e_global_zero_free_elliptic.py']:
    dst = HERE / 'code' / name
    assert not dst.exists(), 'This fresh reconstruction already exists.'
    shutil.copyfile(SOURCE / 'code' / name, dst)
for src in sorted((SOURCE / 'inputs').iterdir()):
    assert src.is_file()
    shutil.copyfile(src, HERE / 'inputs' / src.name)
program = HERE / 'code/e_global_zero_free_elliptic.py'
with program.with_suffix('.out').open('w') as output:
    proc = subprocess.run([sys.executable, str(program)], stdout=output,
                          stderr=subprocess.STDOUT, cwd=HERE, check=False)
assert proc.returncode == 0, proc.returncode
comparisons = []
for ext in ['.json', '.out']:
    original = SOURCE / 'code' / ('e_global_zero_free_elliptic' + ext)
    rebuilt = program.with_suffix(ext)
    same = original.read_bytes() == rebuilt.read_bytes()
    comparisons.append({'file': original.name, 'source_sha256': digest(original),
                        'rebuild_sha256': digest(rebuilt), 'byte_equal': same})
    assert same, original.name
# E95's final coefficient export and the immutable early export used by E96
# have additional metadata differences. Compare each full mathematical field.
final_paths = json.loads((ROOT / 'research_e95/code/a_cusp_kummer.json').read_text())
old_paths = json.loads((HERE / 'inputs/a_cusp_kummer_explore.json').read_text())
fields = ['global_cusp_coefficients', 'c_equivariant_cusp_tau_Kummer']
for field in fields:
    assert final_paths[field] == old_paths[field], field
record = {'status': 'PASS', 'source_program_sha256': digest(program),
          'frozen_manifest_sha256': digest(SOURCE / 'ledger/e_zero_free_elliptic_manifest.json'),
          'returncode': proc.returncode, 'complete_byte_comparisons': comparisons,
          'comparison_exclusions': [],
          'final_E95_export_sha256': digest(ROOT / 'research_e95/code/a_cusp_kummer.json'),
          'final_E95_mathematical_fields_equal_to_exact_input': fields,
          'inputs': {p.name: digest(p) for p in sorted((HERE / 'inputs').iterdir())}}
(HERE / 'comparison.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2), flush=True)
