"""Fresh two-stage E97 reconstruction from copied frozen source and exact comparison."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = ROOT / 'research_e97'
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path = SOURCE / 'ledger/e_unit_norm_coset_manifest.json'
manifest = json.loads(manifest_path.read_text())
for row in manifest['files']:
    assert digest(SOURCE / row['path']) == row['sha256'], row['path']
code = HERE / 'code'
code.mkdir(exist_ok=True)
for name in ['e_unit_norm_coset.py', 'e_unit_norm_coset.gp']:
    dst = code / name
    assert not dst.exists(), 'This fresh reconstruction already exists.'
    shutil.copyfile(SOURCE / 'code' / name, dst)
lower = ROOT / 'research_e86/code/e_stable_lower_genus.gp'
assert digest(lower) == '734133c36ba69a5f7c8bbf7459c5d792d2be15331fd8033c11b746385b4455bd'
shutil.copyfile(lower, code / lower.name)
gp = ROOT / 'research_e52/vendor/pari-2.19.0/gp'
program = code / 'e_unit_norm_coset.py'
with program.with_suffix('.out').open('w') as output:
    proc = subprocess.run([sys.executable, str(program), '--gp', str(gp)],
                          stdout=output, stderr=subprocess.STDOUT, cwd=HERE,
                          check=False)
assert proc.returncode == 0, proc.returncode
# These aliases retain the literal stdout of each named GP stage.
for src, dst in [('e_unit_norm_coset_gp.out', 'e_unit_norm_coset.out.gp-stage'),
                 ('e_unit_norm_coset_lower.out', 'e_stable_lower_genus.out')]:
    shutil.copyfile(code / src, code / dst)
comparisons = []
for name in ['e_unit_norm_coset.json', 'e_unit_norm_coset.out',
             'e_unit_norm_coset_gp.out', 'e_unit_norm_coset_lower.out']:
    original = SOURCE / 'code' / name
    rebuilt = code / name
    same = original.read_bytes() == rebuilt.read_bytes()
    comparisons.append({'file': name, 'source_sha256': digest(original),
                        'rebuild_sha256': digest(rebuilt), 'byte_equal': same})
    assert same, name
record = {'status': 'PASS', 'returncode': proc.returncode,
          'frozen_manifest_sha256': digest(manifest_path),
          'lower_input_sha256': digest(lower),
          'complete_byte_comparisons': comparisons, 'comparison_exclusions': [],
          'binary_files_retained': [
              {'file': n, 'source_sha256': digest(SOURCE / 'code' / n),
               'rebuild_sha256': digest(code / n),
               'byte_equal': (SOURCE / 'code' / n).read_bytes() == (code / n).read_bytes()}
              for n in ['e_unit_norm_coset.bin', 'e_unit_norm_coset_lower.bin']]}
(HERE / 'comparison.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2), flush=True)
