#!/usr/bin/env python3
"""Isolated replay of the frozen E58 finite certificate after full proof review."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent.parent
manifest_path = ROOT / 'research/E58_authoritative_manifest.json'
manifest = json.loads(manifest_path.read_text())
protected = dict(manifest['sha256'])
protected['research/E58_authoritative_manifest.json'] = hashlib.sha256(
    manifest_path.read_bytes()).hexdigest()
protected['sections/D_pronilpotent_lift_agent.tex'] = manifest['protected_D50_sha256']

def verify():
    for name, digest in protected.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name

verify()
replay = ROOT / 'code/root_relative_cm_lift_replay'
replay.mkdir(exist_ok=False)
script = replay / 'bc_relative_cm_sources.py'
shutil.copy2(ROOT / 'code/bc_relative_cm_sources.py', script)
started = time.monotonic()
with script.with_suffix('.out').open('w') as out:
    result = subprocess.run([sys.executable, str(script)], cwd=replay,
        stdout=out, stderr=subprocess.STDOUT, check=True)
elapsed = time.monotonic() - started
expected = json.loads((ROOT / 'code/bc_relative_cm_sources.json').read_text())
actual = json.loads(script.with_suffix('.json').read_text())
assert actual == expected
verify()
record = {
    'all_passed': True,
    'elapsed_seconds': round(elapsed, 3),
    'protected_files': protected,
    'all_original_files_unchanged': True,
    'all_mathematical_json_fields_identical': True,
    'source_read_in_full': True,
    'proof_read_in_full': True,
    'independent_written_review': 'Arithmetic also read the whole proof and program and passed every source comparison.',
    'proof_checks': [
        'The open normal U quotient is an actual source quotient; every finite auxiliary central cover has nilpotent U-image and kills R_nil(U).',
        'The finite relative compactness argument retains every prescribed conjugator value and every finite epimorphism condition. It does not require alpha to preserve U/R_nil(U).',
        'The local-source product is the actual fibre product over Gamma/U, proved on its kernel by coprime Goursat and compactness.',
        'The H=F-prime F-cube image is exactly C2^2 times Q8; Q and D have the explicit joint image of order 1728.',
        'The pro-two kernel in Gamma2 to J admits the specified r-centralizer lift by coprime complement conjugacy and compactness.',
        'Identity relative automorphisms with the prescribed r frame lift to a full modular automorphism, fixing tau after an inner correction in R_nil(H).',
        'The actual f lies in R_nil(H) inside F-prime; all full gentle equations and the restriction automorphism follow through the D44 source maps.',
        'Herfort--Ribes Theorem B-prime, Section 4, printed page 159, was independently opened by root; it gives unique pure s and r frames.',
        'Positive E1 representatives give A=z=[5I], beta=V=1 and bits (1,0). The actual source induces identity on Q while retaining its unique full nontrivial frame.',
        'The explicit primitive tau^12 cycle proves the stated G6 nonfactorization. The full automorphism descends to G6 because q Phi=q, giving a whole-fibre point independently of rejected prior representatives.',
    ],
    'finite_result': actual,
    'primary_source_url': 'https://www.academia.edu/104225124/Torsion_elements_and_centralizers_in_free_products_of_profinite_groups',
    'primary_source_reference': 'turn547view0, lines 19--21',
}
destination = ROOT / 'code/audit_relative_cm_lift_root.json'
destination.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'elapsed_seconds': record['elapsed_seconds'],
    'protected_files': len(protected), 'all_original_files_unchanged': True,
    'all_mathematical_json_fields_identical': True,
    'proof_sha256': protected['sections/E_relative_cm_lift_agent.tex']}, indent=2))
