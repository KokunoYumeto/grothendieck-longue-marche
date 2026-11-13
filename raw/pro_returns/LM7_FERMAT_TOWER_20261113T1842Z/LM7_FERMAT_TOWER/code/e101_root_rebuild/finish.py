"""Complete E101 copied rebuild, exact stdout/JSON and full PARI object comparison."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = ROOT / 'research_e101'
GP = ROOT / 'research_e52/vendor/pari-2.19.0/gp'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path = SOURCE / 'ledger/e_unit_norm_complete_manifest.json'
manifest = json.loads(manifest_path.read_text())
for row in manifest['files']:
    p = SOURCE / row['path']
    assert sha(p) == row['sha256'] and p.stat().st_size == row['bytes'], row['path']
code = HERE / 'code'
inputs = HERE / 'inputs'
program = code / 'e_unit_norm_complete.py'
for name in ['e_unit_norm_scalar.gp','e_unit_norm_coordinates.gp','e_unit_norm_complete.py']:
    assert sha(code/name)==sha(SOURCE/'code'/name)
for p in inputs.glob('*.gp'):
    assert sha(p)==sha(SOURCE/'inputs'/p.name)
comparisons = []
for p in sorted(code.glob('*.out')) + [program.with_suffix('.json')]:
    original = SOURCE / 'code' / p.name
    assert p.read_bytes() == original.read_bytes(), ('complete byte comparison', p.name)
    comparisons.append({'file': p.name, 'sha256': sha(p), 'bytes': p.stat().st_size,
                        'complete_byte_equality': True, 'excluded_fields': []})

# Binary serialization is recorded separately. Every complete PARI object
# is compared by PARI itself, including all actual field, basis and Artin data.
bins = sorted(code.glob('*.bin'))
assert len(bins) == 5
lines = ['default(parisize,256000000);', 'default(parisizemax,2000000000);']
for p in bins:
    original = SOURCE / 'code' / p.name
    a = json.dumps(str(original))
    b = json.dumps(str(p))
    label = json.dumps(p.name)
    lines += [f'a=read({a});b=read({b});',
              f'if(a!=b,error("complete binary object mismatch: ",{label}));',
              f'print({label}," COMPLETE_OBJECT_EQUAL ",a==b," COMPONENTS ",#a);']
lines += ['print("PASS: every complete PARI object agrees; no component excluded.");', 'quit;']
gp_source = HERE / 'compare_bins.gp'
gp_source.write_text('\n'.join(lines) + '\n')
with (HERE / 'compare_bins.out').open('w') as out:
    r = subprocess.run([str(GP), '-q', str(gp_source)], cwd=HERE,
                       stdout=out, stderr=subprocess.STDOUT, check=False)
text = (HERE / 'compare_bins.out').read_text()
warnings = [line.strip() for line in text.splitlines() if '***' in line]
assert warnings == ['***   Warning: new stack size = 256000000 (244.141 Mbytes).',
                    '***   Warning: new maximum stack size = 2000003072 (1907.352 Mbytes).'], warnings
assert r.returncode == 0 and text.count('COMPLETE_OBJECT_EQUAL 1') == 5, text
binary = [{'file': p.name, 'source_sha256': sha(SOURCE / 'code' / p.name),
           'fresh_sha256': sha(p), 'complete_PARI_object_equality': True,
           'excluded_components': []} for p in bins]
for row in manifest['files']:
    assert sha(SOURCE / row['path']) == row['sha256'], row['path']
result = {'status': 'PASS', 'section_sha256': sha(SOURCE / 'sections/E_first_unit_norms.tex'),
          'frozen_manifest_sha256': sha(manifest_path), 'complete_byte_comparisons': comparisons,
          'complete_binary_object_comparisons': binary,
          'binary_comparison_program': 'compare_bins.gp', 'binary_comparison_output': 'compare_bins.out',
          'source_read_scope': 'Complete written proof, all three owned arithmetic programs and all three dependency GP programs read.'}
(HERE / 'comparison.json').write_text(json.dumps(result, indent=2) + '\n')
print('PASS complete E101 fresh output and every complete PARI binary object, with no exclusions.', flush=True)
