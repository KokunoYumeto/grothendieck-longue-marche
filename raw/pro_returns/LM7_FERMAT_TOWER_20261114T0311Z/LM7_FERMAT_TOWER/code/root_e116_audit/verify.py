#!/usr/bin/env python3
"""Rebuild the frozen E.116 computation from copied sources and compare it."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
AUTHOR = ROOT / 'research_e116'
GP = ROOT / 'research_e52/vendor/pari-2.19.0/gp'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

manifest = AUTHOR / 'ledger/e_inert_lower_manifest.json'
assert sha(manifest) == 'f3621089be7dda072f6cfa26198340316544c08fb3e3067e1189a60766e2e53f'
files = json.loads(manifest.read_text())['files']
for rel, item in files.items():
    p = AUTHOR / rel
    assert p.stat().st_size == item['bytes'] and sha(p) == item['sha256'], rel
before = {rel: sha(AUTHOR / rel) for rel in files}
fresh = OUT / 'fresh_retry'
assert not fresh.exists(), 'Use a new audit directory; do not overwrite an execution.'
(fresh / 'code').mkdir(parents=True)
for p in (AUTHOR / 'code').iterdir():
    if p.is_file():
        shutil.copy2(p, fresh / 'code' / p.name)
command = [sys.executable, 'code/e_inert_lower_factors.py', '--gp', str(GP)]
run = subprocess.run(command, cwd=fresh, capture_output=True)
(fresh / 'code/e_inert_lower_factors.out').write_bytes(run.stdout)
(fresh / 'code/e_inert_lower_factors.err').write_bytes(run.stderr)
assert run.returncode == 0, run.stderr.decode(errors='replace')
assert json.loads(run.stdout)['status'] == 'PASS'
stems = ['e_inert_lower_factors', 'e_small_inert_units', 'e53_prime_columns',
         'e53_pure9_norm_witness', 'e53_pure9_class_upper', 'e53_exact_maps',
         'e53_first_norm_explore', 'e53_s_norm_explore', 'e53_unit_saturation',
         'e53_complete_transition']
compared = {}
for stem in stems:
    for suffix in ['.out', '.json']:
        p = AUTHOR / 'code' / (stem + suffix)
        if p.exists():
            q = fresh / 'code' / p.name
            same = p.read_bytes() == q.read_bytes()
            compared[p.name] = {'author_sha256': sha(p), 'replay_sha256': sha(q),
                                'byte_identical': same}
            assert same, p.name
bins = sorted(p.name for p in (fresh / 'code').glob('*.bin')
              if p.name in ['e_small_inert_units.bin', 'e53_prime_columns.bin',
                            'e53_pure9_candidate.bin', 'e53_pure9_norm_witness.bin',
                            'e53_pure9_class_upper.bin', 'e53_exact_maps.bin'])
script = ['default(parisize,256000000);', 'default(parisizemax,1000000000);']
binary = {}
for name in bins:
    p, q = AUTHOR / 'code' / name, fresh / 'code' / name
    binary[name] = {'author_sha256': sha(p), 'replay_sha256': sha(q),
                    'raw_bytes_identical': p.read_bytes() == q.read_bytes()}
    script.append('a=read(' + json.dumps(str(p)) + ');')
    script.append('b=read(' + json.dumps(str(q)) + ');')
    script.append('if(a!=b,error(' + json.dumps('Complete GEN mismatch: ' + name) + '));')
    script.append('print(' + json.dumps('PASS complete GEN: ' + name) + ');')
script += ['print("PASS complete binary object comparison");', 'quit(0);']
gp_source = OUT / 'compare_binary.gp'
gp_source.write_text('\n'.join(script) + '\n')
gp_run = subprocess.run([str(GP), '-q', '-f', str(gp_source)], capture_output=True)
(OUT / 'compare_binary.out').write_bytes(gp_run.stdout)
(OUT / 'compare_binary.err').write_bytes(gp_run.stderr)
assert gp_run.returncode == 0 and b'PASS complete binary object comparison' in gp_run.stdout
warnings = gp_run.stderr.decode(errors='replace').splitlines()
allowed = ('  ***   Warning: new stack size = ',
           '  ***   Warning: new maximum stack size = ')
assert all(not line.strip() or line.startswith(allowed) for line in warnings), warnings
for value in binary.values():
    value['complete_GEN_identical'] = True
assert all(sha(AUTHOR / rel) == value for rel, value in before.items())
result = {'statement': 'E.116', 'status': 'PASS', 'exit_code': run.returncode,
          'manifest_sha256': sha(manifest), 'manifest_files_verified': len(files),
          'command': command, 'complete_text_outputs': compared, 'binary_outputs': binary,
          'binary_comparison_exit_code': gp_run.returncode,
          'binary_comparison_stack_warnings': warnings,
          'author_files_unchanged': True, 'ignored_fields': [],
          'proof_verification_claimed_by_this_program': False}
(OUT / 'verification.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2), flush=True)
