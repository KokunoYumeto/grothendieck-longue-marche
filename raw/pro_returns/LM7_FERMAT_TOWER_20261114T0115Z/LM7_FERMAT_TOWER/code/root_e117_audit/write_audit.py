#!/usr/bin/env python3
"""Record the completed root proof, source, and frozen replay audit of E.117."""
from pathlib import Path
import hashlib
import json

here = Path(__file__).resolve().parent
work = here.parent
author = work / 'research_e117'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
replay = json.loads((here / 'verification.json').read_text())
assert replay['status'] == 'PASS'
assert replay['excluded_fields'] == []
proof = author / 'sections/E_quartic_three.tex'
assert sha(proof) == 'de1d67c7ae1e6e52850e57f51c6fa10a904e14eb1d8092471ee2a0002073da59'
peer = json.loads((author / 'ledger/e_quartic_three_peer.json').read_text())
for row in peer['external_records']:
    assert sha(work / row['path']) == row['sha256']
assert sha(author / peer['exact_diff']) == peer['exact_diff_sha256']
warning = (here / 'compare_binary.err').read_text()
assert warning.strip() == '***   Warning: new stack size = 128000000 (122.070 Mbytes).'

checks = [
    'Full proof, both core program sources, all dependency and source ledgers read; the sole post-review amendment explicitly defines H=C=T_3 J_C and changes no formula.',
    'Literal degree-sixteen third-division fields, actual residual basis and tangent-function Weil pairing, complete default-flag-zero class certification, and the two full decomposition groups checked.',
    'Finite-S H0/H2 vanishing for all five descended lattices, cyclic finite H1, compatible inverse-limit cocycles, and the Tate twist in the Brauer augmentation comparison checked.',
    'Actual unit-tangent specialization and centre-free rank-seventeen source pullback checked with explicit inverse maps; the three-adic source is constructed over its stated arithmetic group.',
    'Integral Phi/2 and Psi/2 inverse symplectic maps, inverse coordinate scaling, the primitive epsilon_1 selector, saturated Johnson and inner images, and the pure-CM projector with quarter denominators checked.',
    'Integral Ceresa-to-action comparison, the complete inner correction, the retained filling cochain J, and all compact/affine cochain transports checked.',
    'Finite-support direct limits followed by derived inverse limits, the exact unclosed support denominator, the literal mixed localizer, integral valuation/decay tests, and bounded-denominator rational inverse checked.',
    'Finite-S section coordinates Z_3^13 times (Z_3^78 plus C_3^10), full central free rank 66, all restricted Tate/CM factors, and the absence of a lower stabilizer checked.',
    'Actual S-unit norm matrix and its kernel, local CM residue projector and charts, uniformly convergent inverse cocycles, and the full-translation Chebotarev argument for unbounded local orders checked.'
]
fresh_sources = []
for stem, locations in [
    ('hain_matsumoto2005', 'Printed page 4, Theorem 3 and factor-two explanation; printed pages 28-29, Section 8, Theorem 8.1 and complete specialization proof of Theorem 3. Text extraction lines 145-210 and 1495-1625 were actually read.'),
    ('bisogno_li_litt_srinivasan2023', 'Printed pages 12-14, all of Lemmas 2.20-2.22 and Proposition 2.23 with its full proof, including the group-ring comparison g to g-1 and factor two. Text extraction lines 608-725 were actually read.')
]:
    pdf = work / 'source_route_raw' / (stem + '.pdf')
    txt = pdf.with_suffix('.txt')
    fresh_sources.append({'pdf':str(pdf.relative_to(work)), 'pdf_sha256':sha(pdf), 'text':str(txt.relative_to(work)), 'text_sha256':sha(txt), 'actual_read':locations, 'new_page_image_inspection_claim':False})
result = {
    'statement':'E.117', 'status':'PASS', 'proof_sha256':sha(proof),
    'manifest_sha256':replay['manifest_sha256'], 'manifest_files_verified':replay['manifest_files_verified'],
    'full_proof_and_core_source_read':True, 'mathematical_checks':checks,
    'fresh_replay_record':'verification.json', 'fresh_replay_sha256':sha(here/'verification.json'),
    'whole_text_outputs_equal':True, 'excluded_fields':[], 'complete_deserialized_binary_equal':True,
    'binary_stderr':'The sole stderr line is the recorded requested-stack-size warning; exact text checked by this writer.',
    'fresh_original_text_readings':fresh_sources,
    'reused_original_readings':[
        'SGA1 Expose XIII printed 288-292 / PDF 304-308: full original text and all five images actually reviewed in the retained root E115 audit.',
        'Milne ADT and Jannsen finite/continuous-cochain comparison: retained earlier E112 source audits and exact author source ledger; no new reading of those passages is claimed here.',
        'PARI full certification semantics and Milne Chebotarev: retained original-source records; actual arithmetic and field-intersection argument checked independently in this proof.'
    ],
    'peer_audit':{'scope':peer['scope'], 'audited_proof_sha256':peer['audited_proof_sha256'], 'frozen_proof_sha256':peer['frozen_proof_sha256'], 'records':peer['external_records'], 'fresh_program_execution_claim':False, 'full_unrestricted_support_audit_claim':False},
    'corrections_requested_and_resolved':['Explicitly define H=C=T_3 J_C before the integral-polarization comparison.'],
    'remaining_claim_boundary':'E117 proves the specified intrinsic class-two three-primary quartic stage. Original E23 and the full higher intrinsic quotients remain active. No unevaluated Frobenius value is assigned.'
}
(here/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
text = '# Root audit of E.117\n\n**PASS for the frozen statement.**\n\n'
text += 'Proof SHA256: `'+sha(proof)+'`. Frozen manifest SHA256: `'+replay['manifest_sha256']+'` (95 files verified).\n\n'
text += '## Proof and source inspection\n\n'+'\n\n'.join(checks)+'\n\n'
text += 'The two freshly reread original sources are recorded in audit.json with their exact PDF and text hashes and passage ranges. Those reads were text reads; no new page-image inspection is claimed. The earlier SGA1, Milne, Jannsen, Chebotarev, and PARI readings retain their original recorded scopes.\n\n'
text += '## Reproducibility\n\nThe copied source and all three immutable inputs were executed afresh. All five compared source/text output files agree byte for byte, with zero excluded fields. The serialized binary bytes differ, and the entire deserialized PARI GEN, including every nested BNF component, is equal. The sole comparison stderr line reports the explicitly requested stack size. All 95 author-manifest files remained unchanged. The complete executed verifier and actual stdout/stderr are retained.\n\n'
text += '## Independent focused review\n\nThe separate BC audit covers the actual residual fields, finite-S cohomology, integral selector, coordinate counts, and tangent-pairing sign. It makes no fresh arithmetic-replay or full unrestricted-support claim. Its two records and the sole later definition amendment were opened and their hashes checked.\n\n'
text += '## Scope\n\n'+result['remaining_claim_boundary']+'\n'
(here/'audit.md').write_text(text)
print(json.dumps({'status':'PASS','audit_json_sha256':sha(here/'audit.json'),'audit_md_sha256':sha(here/'audit.md'),'proof_sha256':sha(proof),'manifest_files_verified':95},indent=2))
