#!/usr/bin/env python3
"""Freeze E109 after the received independent full audit."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT.parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
dump = lambda x: json.dumps(x, indent=2) + '\n'
ledger = ROOT / 'ledger'
peer_path = WORK / 'd_e109_audit/audit.json'
peer = json.loads(peer_path.read_text())
proof = ROOT / 'sections/E_quartic_compact_action.tex'
assert peer['status'] == 'PASS' and peer['mathematical_corrections_requested'] == []
assert peer['reviewed_current_section_sha256'] == sha(proof)
for path, digest in peer['file_sha256'].items():
    assert sha(WORK / path) == digest, path
replay = json.loads((ROOT / 'code/e_quartic_ceresa_final_replay.json').read_text())
assert replay['status'] == 'PASS' and replay['actual_exit_code'] == 0
assert replay['excluded_fields'] == []

history = ROOT / 'code/e109_metadata_before_peer'
history.mkdir(exist_ok=False)
for name in ['e_quartic_compact_action_results.json',
             'e_quartic_compact_action_source_evidence.json',
             'e_quartic_compact_action_report.md']:
    shutil.copy2(ledger / name, history / name)

p = ledger / 'e_quartic_compact_action_results.json'
rows = json.loads(p.read_text())
rows[0]['notes'] += ' Independent full proof/source audit PASS; separate independent coefficient and p19 execution PASS with exit0.'
rows[0]['where_proved'] += '; independent audit d_e109_audit/audit.json and its actual focused program.'
p.write_text(dump(rows))
p = ledger / 'e_quartic_compact_action_source_evidence.json'
d = json.loads(p.read_text())
d['independent_review'] = {
    'status': 'PASS', 'file': 'd_e109_audit/audit.json',
    'sha256': sha(peer_path), 'full_proof_read': True,
    'reviewed_proof_sha256': peer['reviewed_current_section_sha256'],
    'independent_focused_execution_exit_code': 0,
    'corrections_requested': [],
    'scope': 'The peer report separately records the exact original sources read and actual page images viewed.'
}
p.write_text(dump(d))
p = ledger / 'e_quartic_compact_action_report.md'
p.write_text(p.read_text() + '''
## Received independent audit

The full proof/source audit by d_galois is PASS with no correction requested.
The exact reviewed proof hash is retained. Its separate program imports neither
the author code nor its certificate, and verifies the coefficient maps, rank
modulo five, all twenty exterior characters, all nineteen trace-one summands
at19, the exact point orders and the group-ring commutator sign. Its actual
exit code is zero. The author owns the separate complete fresh program replay;
the peer does not claim to have performed that replay.
''')

review = {
    'statement': 'E.109', 'status': 'PASS',
    'proof_sha256': sha(proof), 'proof_lines': len(proof.read_text().splitlines()),
    'author_final_replay': 'code/e_quartic_ceresa_final_replay.json',
    'peer_audit': 'd_e109_audit/audit.json', 'peer_audit_sha256': sha(peer_path),
    'independent_program': 'd_e109_audit/code/d_e109_independent.py',
    'mathematical_corrections_requested': [],
    'source_reading_limits': 'The exact source-evidence records remain authoritative for reading scope.'
}
(ledger / 'e_quartic_compact_action_reviews.json').write_text(dump(review))

manifest_path = ledger / 'e_quartic_compact_action_manifest.json'
excluded = {manifest_path, Path(__file__).resolve(), Path(__file__).with_suffix('.out').resolve()}
owned = []
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p not in excluded and '__pycache__' not in p.parts and 'qa' not in p.parts:
        owned.append({'file': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
                      'sha256': sha(p)})
inputs = []
for path in ['research_e103/sections/E_quartic_odd_abelian.tex',
             'research_e105/sections/E_quartic_class2.tex']:
    src = WORK / path
    if not src.exists():
        # E105's authoritative section name is read from its single matching file.
        if path.startswith('research_e105/'):
            candidates = list((WORK / 'research_e105/sections').glob('*.tex'))
            assert len(candidates) == 1
            src = candidates[0]
        else:
            raise FileNotFoundError(path)
    inputs.append({'workspace_path': str(src.relative_to(WORK)), 'sha256': sha(src)})
manifest = {
    'statement': 'E.109', 'state': 'author frozen and full independent audit PASS',
    'proof_sha256': sha(proof), 'files': owned, 'exact_inputs': inputs,
    'author_rebuild': 'Complete source/stdout/JSON byte identity with no excluded fields.',
    'independent_peer': review,
    'excluded_material': [
        'Third-party PDFs and their images remain source evidence outside the deliverable.',
        'This recording helper and its still-running stdout are excluded from their own manifest; '
        'both actual files are retained for the later package manifest.',
        'The independent peer bundle is retained separately during integration.'
    ]
}
manifest_path.write_text(dump(manifest))
print(dump({'status': 'PASS', 'statement': 'E.109', 'proof_sha256': sha(proof),
            'manifest_sha256': sha(manifest_path), 'manifest_files': len(owned),
            'exact_input_files': len(inputs), 'peer_audit_sha256': sha(peer_path)}))
