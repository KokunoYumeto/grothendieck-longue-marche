"""Freeze the E104 proof, exact program/output and concrete coverage metadata."""
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
enc = lambda obj: json.dumps(obj, indent=2, ensure_ascii=False) + '\n'
ledger = BASE / 'ledger'
ledger.mkdir(exist_ok=True)
stem = 'e_two_prime_full_family'
proof = BASE / 'sections/E_two_prime_full_family.tex'
fresh = json.loads((ROOT / 'root_e104_audit/comparison.json').read_text())
assert fresh['status'] == 'PASS' and sha(proof) == fresh['section_sha256']
assert all(x['complete_bytes_equal'] and not x['excluded_fields'] for x in fresh['complete_comparisons'])
detail = ('The complete full and intrinsic-metabelian cubic geometric pro-three section spaces '
          'over every two-prime arithmetic source {3,ell} with ell congruent to 2 or 5 modulo9, '
          'or v3(ell-1)=1 and 3 not a cube modulo ell. The actual original-root source maps, '
          'all ramified cusp coordinates, the entire unramified stratum, every full-to-metabelian '
          'fibre, and the quotient boundary topology are explicit.')
rows = [{'id': 'E.104', 'statement': detail, 'status': 'Proved',
         'where_proved': 'sections/E_two_prime_full_family.tex; code/e_two_prime_full_family.py/.out/.json; ledger/root_e104_audit.json',
         'depends_on': ['E.34', 'E.37', 'E.41', 'E.55', 'E.56', 'E.61', 'E.66', 'E.78', 'E.98', 'E.100', 'E.102'],
         'manuscript_passages': ['section51.16; folios733v–736v; scans172–178; formulas371–379; Part E(c),(d), follow-up4'],
         'depends_on_doubtful_reading': False,
         'notes': ('The exact prime-family source maps are proved using the actual inertia bundles and their inverse coset-tree maps. '
                   'The retained calculation checks all173 applicable primes through2000, all18338 exponent round trips, '
                   '11418 original-root transports and Hall/Chen ranks through degree20. These finite checks support the formulas; '
                   'the complete proof establishes all primes in the two stated families. Unrestricted global sources and other geometric prime components remain E.23.')}]
(ledger / (stem + '_results.json')).write_text(enc(rows))
(ledger / (stem + '_coverage_notes.json')).write_text(enc([{
    'tasks': ['E.c', 'E.d', 'E.follow-up-4'], 'statement_ids': ['E.104'],
    'outcome': detail, 'remaining_question': 'E.23 retains the requested unrestricted arithmetic source and other geometric prime components.'}]))
(ledger / (stem + '_report.md')).write_text(
    '# E.104 complete sections for two infinite two-prime families\n\n' + detail + '\n\n'
    'The inert family has exactly three rational-cusp ramified labels and zero Frobenius residue, '
    'with the actual original operator T transporting its anti-involution coordinates. '
    'The split family has all nine cusps and three residues, with an actual H^J\\H coordinate. '
    'The exponent ambiguity, normalization and inverse maps are written explicitly. '
    'The unramified source is transported back to the original free basis before applying the E100 nonlinear fibre maps.\n\n'
    'The fresh copied-source/input run is byte-identical for the complete stdout and JSON, with no excluded fields. '
    'It checks104 inert and69 split primes through2000,18338 exponent maps,11418 original-root transports, '
    'all27 inert descent labels and the degree1–20 Hall/Chen ranks. The source maps and complete local classifications '
    'prove the infinite-family assertion. A separate full peer review is pending at this freeze.\n')
(ledger / (stem + '_source_evidence.json')).write_text(enc({
    'primary_source': {'bib_key': 'E_WingbergRiemann',
                       'url': 'https://www.mathi.uni-heidelberg.de/~wingberg/agwingberg/paperwingberg/Riemann-kpi1.pdf',
                       'actually_read': 'Continuous bundle definition; Lemma1.1 and proof; Theorem2.4 and complete proof; remark after Proposition2.1.',
                       'routing': 'Previously opened primary source; its exact verified bibliography entry is already retained.'},
    'actual_internal_maps': ['E55 inertia-bundle isomorphism', 'E56 split-source marked Frobenius normalization',
                             'E61 and E66 full good-place cusp classification', 'E98 split packets',
                             'E100 integral Hall coordinates and actual nonlinear fibres', 'E102 first integral Smith factor'],
    'immutable_runtime_input': {'path': 'code/a_s23_full.json', 'sha256': fresh['input_sha256']},
    'finite_verification_scope': '173 primes through2000; all-prime theorem is proved with the stated source isomorphisms.'}))
manifest = {'status': 'frozen for full peer audit; root complete proof/source read and fresh rebuild PASS',
            'statement': 'E.104',
            'files': [{'path': str(p.relative_to(BASE)), 'sha256': sha(p), 'bytes': p.stat().st_size}
                      for folder in ['sections', 'code', 'ledger'] for p in sorted((BASE / folder).iterdir())
                      if p.is_file() and not p.name.endswith('_manifest.json')],
            'runtime_input': {'path': 'code/a_s23_full.json', 'sha256': fresh['input_sha256']},
            'command': 'python code/e_two_prime_full_family.py --input code/a_s23_full.json',
            'comparison_exclusions': [], 'root_fresh_record': 'root_e104_audit/comparison.json',
            'external_source_reused': 'E_WingbergRiemann'}
(ledger / (stem + '_manifest.json')).write_text(enc(manifest))
print(enc({'status': 'PASS', 'statement': 'E.104', 'section_sha256': sha(proof),
           'frozen_manifest_sha256': sha(ledger / (stem + '_manifest.json')),
           'full_peer_audit': 'pending'}))
