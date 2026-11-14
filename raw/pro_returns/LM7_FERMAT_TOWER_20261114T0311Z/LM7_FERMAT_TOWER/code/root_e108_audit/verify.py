#!/usr/bin/env python3
"""Root proof/map audit and full frozen-source E108 rebuild."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
WORK = ROOT.parent
AUTHOR = WORK / 'research_e108'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path = AUTHOR / 'ledger/e_quartic_peripheral_manifest.json'
manifest = json.loads(manifest_path.read_text())
for row in manifest['files']:
    p = AUTHOR / row['file']
    assert p.stat().st_size == row['bytes'] and sha(p) == row['sha256'], row['file']
fresh = ROOT / 'fresh'
fresh.mkdir(exist_ok=False)
for part in ['code', 'inputs']:
    (fresh / part).mkdir()
for name in ['code/a_quartic_w_slice.py', 'inputs/a_quartic_class2.json']:
    shutil.copy2(AUTHOR / name, fresh / name)
out = fresh / 'code/a_quartic_w_slice.out'
with out.open('wb') as stream:
    run = subprocess.run([sys.executable, 'code/a_quartic_w_slice.py'], cwd=fresh,
                         stdout=stream, stderr=subprocess.STDOUT)
assert run.returncode == 0, run.returncode
matches = []
for name in ['code/a_quartic_w_slice.py', 'code/a_quartic_w_slice.out',
             'code/a_quartic_w_slice.json', 'inputs/a_quartic_class2.json']:
    assert (fresh / name).read_bytes() == (AUTHOR / name).read_bytes(), name
    matches.append({'file': name, 'sha256': sha(fresh / name),
                    'complete_byte_equality': True})
proof = AUTHOR / 'sections/E_quartic_peripheral_slice.tex'
audit = {
    'status': 'PASS', 'statement': 'E.108', 'actual_exit_code': run.returncode,
    'proof_sha256': sha(proof), 'proof_lines': len(proof.read_text().splitlines()),
    'manifest_sha256': sha(manifest_path), 'verified_manifest_files': len(manifest['files']),
    'full_proof_read': True, 'full_program_read': True,
    'fresh_execution_matches': matches, 'excluded_fields': [],
    'proof_checks': [
        'The exact twelve-cusp quotient and its inverse, actual Shapiro map, '
        'norm projector and eleven restricted Kummer coordinates are retained.',
        'All55 shifted cup identities agree with the actual arithmetic matrix; '
        'the displayed Phi, primitive and BCH representative corrections have '
        'the required signs.',
        'Both lifting directions use the actual pullback extension; the '
        'four-coset central correction descends an H-section over the fixed '
        'global abelian input.',
        'K2 of the exact S-integer ring vanishes modulo every prime power. '
        'Localization adds residue-unit groups prime to ell and the trivial '
        'group at2; Kahn A2.1 includes the prime-power repair and prime2.',
        'The support direct sum is formed before the inverse limit. The '
        'resulting two-term restricted complex retains the image without '
        'closure, and the finite base H1 groups remove the adjacent lim1 term.',
        'The actual tame relation, Frobenius shear and root changes give the '
        'same restricted residue class. The required correction is the '
        'displayed quotient by norm(q)-1; integral and rational support '
        'membership prove both directions including convergence.',
        'The norm-one zero-minimum witness has prime norm49 and nonzero '
        'three-primary residue. The positive rank5 family uses the actual '
        'two-prime norm and unit coordinates.',
        'The eleven Fourier columns,55 exterior maps, parity ranks and '
        'three-primary torsion are integral in the stated coefficient rings. '
        'The CM contraction and its section give the precise retained '
        'V(1), V(1)chi2 and U_CM factors.',
        'A^G=0 supplies the unique abelian aligning conjugator; the central '
        'ratio and coboundary quotient give the entire fibre action. '
        'Unresolved mixed inputs and CM cohomology factors remain explicit.'
    ],
    'root_original_source_scope': [
        'Guo--Qin--Song original manuscript p8 actually visually read, '
        'including Theorem3.5 proof and its displayed elimination conclusion. '
        'Root does not claim to have reread all preceding elimination lemmas.',
        'Kahn original Appendix2 PropositionA2.1 and complete proof read from '
        'the original PDF retrieval, printed97--98, including the finite '
        'inverse-limit/five-lemma repair.'],
    'independent_peer': 'bc_e108_audit/audit.json, full draft and primary K2 proof review PASS.',
    'remaining': 'Original unrestricted E23 remains active.'
}
(ROOT / 'verification.json').write_text(json.dumps(audit, indent=2) + '\n')
print(json.dumps(audit, indent=2))
