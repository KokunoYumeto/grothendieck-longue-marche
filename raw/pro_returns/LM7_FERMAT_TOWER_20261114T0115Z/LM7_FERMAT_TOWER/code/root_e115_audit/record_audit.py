#!/usr/bin/env python3
"""Record the completed manual E.115 review and its separate executed replay."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
AUTHOR = ROOT / 'research_e115'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

proof = AUTHOR / 'sections/E_quartic_mixed_five.tex'
program = AUTHOR / 'code/a_quartic_mixed_five.py'
manifest = AUTHOR / 'ledger/e_quartic_mixed_five_manifest.json'
execution = OUT / 'verification.json'
peer = ROOT / 'bc_e115_audit/audit.json'
source = AUTHOR / 'sources/sga1_recomposed.pdf'
assert sha(proof) == 'eb61b16748ffff2ced871ac1c2619018f86e1ebc02474a25e19579f9923ae01a'
assert sha(program) == '0bd93f98e369144110bb9044e172642af951cc4af08538aa82549702040a9b1b'
assert sha(manifest) == 'bcdacee1fb1b149fe250d98f5fdf472c6e9b4dd5538587cc31d6d493eeb43d44'
replay = json.loads(execution.read_text())
assert replay['status'] == 'PASS' and replay['exit_code'] == 0
assert replay['manifest_files_verified'] == 24 and not replay['ignored_fields']
assert all(item['byte_identical'] for item in replay['complete_output_comparison'].values())
assert sha(source) == '8e64218d356456c534eebf996940f0f957e43b54f1a080241debe12cbaf60d3c'

review = [
 'The smooth model, unit-tangent Puiseux fibre, prime-to-residue specialization, based inertia action, centre-free normality argument, exact arithmetic quotient and its written inverse.',
 'All finite-S and unrestricted coefficient comparisons, the nine Tate injectivity maps, ordinary S-unit norm matrix, compact primitive, actual affine Johnson comparison, integral filling map and full BCH gauge.',
 'The localization sign from the actual tame relation; the finite and continuous cohomology comparison; the restricted correction criterion and its scalar valuation form with the actual Kummer boundary.',
 'The finite translation image from the actual residual scalar and the Sah identity; the cyclotomic and Kummer field intersections through their conjugation modules; the complete Chebotarev mixed nonlifting argument.',
 'The complete finite program, frozen inputs, all universal tensor and inverse identities, and the stated limits of its finite output.'
]
data = {
 'statement': 'E.115', 'status': 'PASS', 'reviewer': '/root',
 'reviewed_at_utc': datetime.now(timezone.utc).isoformat(),
 'proof_sha256': sha(proof), 'proof_lines_read': len(proof.read_text().splitlines()),
 'full_proof_read': True, 'full_mathematical_program_sources_read': True,
 'program_sha256': sha(program), 'manifest_sha256': sha(manifest),
 'mathematical_review': review,
 'mathematical_corrections_to_frozen_proof': [],
 'prefreeze_clarification': 'The ordinary S-unit norm was written as its literal two-by-four matrix before the supplied final proof was frozen.',
 'method': 'Complete written-proof and program-source inspection. The fresh execution certificate is separate evidence and does not certify the infinite statements by enumeration.',
 'root_fresh_program_replay': True,
 'execution_evidence': {'path': 'root_e115_audit/verification.json', 'sha256': sha(execution),
  'scope': 'All24 manifest files checked; complete JSON, stdout and stderr agree byte-for-byte; no exclusions; all four frozen inputs and author files remain unchanged.'},
 'source_review': {
  'new_original_reading': 'SGA1, Expose XIII, printed pages288–292 (PDF pages304–308): Proposition2.9, the complete specialization construction2.10, Lemma2.11 with proof, and Corollary2.12 with its complete proof.',
  'source_pdf_sha256': sha(source),
  'based_refinement': 'The unit-tangent based-fibre refinement is proved in E.115 and was reviewed separately from the cited specialization statement.',
  'reused_verified_sources': 'Milne Arithmetic Duality Theorems and Jannsen are reused from the full E.112 primary-source audits. The Chebotarev source use was checked against the author evidence; this audit does not claim a fresh root reading of those other original PDFs.'
 },
 'received_independent_review': {'path': 'bc_e115_audit/audit.json', 'sha256': sha(peer),
  'written_report_sha256': sha(ROOT / 'bc_e115_audit/audit.md'),
  'scope': 'Complete text read with independent derivations focused on the actual descent, mixed localizer and convergence, finite translation image, field intersections and Chebotarev family. No peer fresh program execution is claimed.'},
 'retained_failed_attempt': 'The initial SymPy polynomial-generator failure is retained with its actual empty stdout and traceback. It supplies no evidence for the final arithmetic claims.'
}
(OUT / 'audit.json').write_text(json.dumps(data, indent=2) + '\n')
paragraphs = [
 '# E.115 complete root audit',
 'Status: PASS for the frozen proof and the explicitly described program, source and replay scopes.',
 'The final proof was read in full. Its SHA256 is `' + sha(proof) + '`. The complete mathematical program was also read. The manual review checked the following arguments:',
 '\n'.join('- ' + item for item in review),
 'The ordinary S-unit norm formula was clarified before the final freeze by displaying its literal two-by-four matrix. No further mathematical correction was required in the frozen proof.',
 'The executed fresh replay verified all24 author-manifest files and reproduced the complete JSON, stdout and stderr byte-for-byte, without ignored fields. All four frozen inputs and the author files remained unchanged. The replay has actual exit status0. Its finite checks do not replace the proofs of descent, cohomology, restricted support or Chebotarev existence.',
 'The original SGA1 Expose XIII printed pages288–292 (PDF pages304–308) were actually viewed and read, including Proposition2.9, all of2.10, Lemma2.11 and the complete proof of Corollary2.12. The E.115 unit-tangent based-fibre refinement was checked as an additional argument. Other primary-source claims reuse the precisely scoped E.112 and author records; no new root reading of their PDFs is asserted here.',
 'The independently written bc_fermat audit was read. It supports the precise descent, mixed localizer, scalar convergence and Chebotarev scopes recorded in audit.json. It contains no fresh execution claim.',
 'The failed initial polynomial-generator attempt, including its actual empty stdout and traceback, remains preserved and is not used as positive evidence.',
 'This audit settles the stated E.115 result. It does not change the scope of the original outstanding E.23 task or assign numerical higher Frobenius phases that were not computed.'
]
(OUT / 'audit.md').write_text('\n\n'.join(paragraphs) + '\n')
print(json.dumps({'status': 'PASS', 'audit_sha256': sha(OUT / 'audit.json'),
                  'proof_sha256': sha(proof), 'replay_exit_code': replay['exit_code']}, indent=2))
