#!/usr/bin/env python3
"""Record completed manual root reviews and their separate exact replays."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()

configs = [
 ('E.116', 'research_e116', 'root_e116_audit', 'sections/E_inert_lower_factors.tex',
  '0adab8885890ea4ed51bdd7b035dd795ad466e4aa8954277e288067eeb2b8051', [
   'The exact two-prime ramification, nonzero zeta norm character, both ambiguous-class formulas, quadratic norm/extension inverses, and all-level ordinary pure-unit norms.',
   'The chosen Smith right inverses, norm-coherent prime generators, unique surviving root chains, restricted topology, actual total-norm cube, and both directions of the E.46/E.55 comparison.',
   'Every labeled local character at53, the complete outside-S Hilbert90 maps, the conjugation sign, completion/preimage directions, and the fixed-group descent of the full S-unit norm image.',
   'The precise flag-one upper presentation, independently proved lower bound, all actual ideal relations, full complex S-class action, ordinary-unit saturation, and every norm-fibre inverse.',
   'The complete main driver, four supporting Python programs and five successful GP programs, as well as the retained unsuccessful default-flag-zero program.'
  ]),
 ('D.61', 'D61_EXPERIMENTS', 'root_d61_audit', 'sections/D_remaining_projective_rows.tex',
  'bbdd706f893f43b67ed05e208a4398cc41f659ad5447a100d5934b8228db806e', [
   'The actual stabilizer modules, finite affine inclusions/retractions, induced integral projective lattices, prescribed reduction lifts, zero small-image maps and cusp annihilation.',
   'The Fitting-summand argument for the actual complementary diagonal, the exact row replacement, both projector identities, and its continuous peripheral realization with retained source conjugators.',
   'The orientation-to-norm comparison, both injective maps on the selected blocks, central correction image, exact source quotient and every displayed comparison kernel.',
   'The actual intermediate-cover transfer, integral projective norm inverse, Kurosh target homomorphism, cone and cusp terms, coset-sum formula, and all26 surviving self classes.',
   'All four complete mathematical programs, including the invariant Hermitian-to-wedge maps on every column and the full induced-module divided norms.'
  ])
]

for statement, author, audit, relative, expected, scopes in configs:
    base, out = ROOT / author, ROOT / audit
    proof, replay_file = base / relative, out / 'verification.json'
    assert sha(proof) == expected
    replay = json.loads(replay_file.read_text())
    assert replay['status'] == 'PASS' and replay['author_files_unchanged']
    record = {
      'statement': statement, 'status': 'PASS', 'reviewer': '/root',
      'reviewed_at_utc': now, 'proof_sha256': sha(proof),
      'proof_lines_read': len(proof.read_text().splitlines()),
      'full_proof_read': True, 'full_mathematical_program_sources_read': True,
      'mathematical_review': scopes, 'mathematical_corrections_to_frozen_proof': [],
      'root_fresh_program_replay': True,
      'execution_evidence': {'path': audit + '/verification.json', 'sha256': sha(replay_file)},
      'method': 'Complete written-proof and source-code inspection. The executed finite comparisons are separate evidence and do not certify the infinite proofs by enumeration.'
    }
    if statement == 'E.116':
        assert replay['exit_code'] == 0 and replay['manifest_files_verified'] == 84
        assert not replay['ignored_fields']
        assert len(replay['complete_text_outputs']) == 15
        assert len(replay['binary_outputs']) == 6
        assert all(x['complete_GEN_identical'] for x in replay['binary_outputs'].values())
        record['execution_evidence']['scope'] = 'All84 manifest files; all15 complete text outputs byte-identical; six PARI binary files differ as raw serialization, while every complete decoded GEN is identical. No mathematical fields were excluded.'
        record['source_review'] = {
          'new_local_primary_reading': 'Official PARI documentation of bnfcertify flag1 and the actual class-generation phase of bnfcertify0 were read in full at the retained excerpt scope.',
          'reused_verified_sources': 'Milne CFT exact local Artin, cyclic Hasse norm and S-unit Herbrand results, and both Lemmermeyer ambiguous-class formulas, are used in their stated forms. Their complete author primary-source reading scopes are retained; this root audit does not claim a fresh root opening of those PDFs.',
          'original_arguments_reviewed': 'The outside-S Hilbert90 sequence, its conjugation twist, the lower class bound and every completion comparison are proved in the section and were reviewed in full.'
        }
        peer = base / 'ledger/e_inert_lower_peer_audit.md'
        record['received_independent_review'] = {
          'path': str(peer.relative_to(ROOT)), 'sha256': sha(peer),
          'scope': 'The complete draft was read by a_structure with focused independent derivations of E116.19–21 and the following class/action deduction. No peer GP replay is claimed.'
        }
        record['retained_failed_attempts'] = [
          'The author default-flag-zero degree-nine run timed out with actual exit124 and is not used as proof.',
          'The first root audit guard rejected two ordinary PARI stack-size warnings after the arithmetic comparisons. Its actual exit1, source, empty stdout and observed traceback were retained. The corrected guard accepts only those named warnings; the subsequent complete fresh replay exited0.'
        ]
    else:
        assert replay['author_manifest_files_verified'] == 27
        assert replay['immutable_inputs_verified'] == 2 and len(replay['programs']) == 4
        assert all(x['actual_exit_code'] == 0 for x in replay['programs'])
        record['execution_evidence']['scope'] = 'All27 owned manifest files and two frozen inputs checked; all four complete copied-source/input program replays passed. Whole JSON and stdout agree, with only the explicitly named elapsed_seconds values excluded and every original timing retained.'
        pdf = ROOT / 'LM7_FERMAT_TOWER/sources/originals/HerfortRibes1985_GDZ.pdf'
        assert sha(pdf) == '67f1f99f001a6b198a3e5cef50849fbedd244e0469aa7172986d8c777ce126d8'
        record['source_review'] = {
          'new_original_reading': 'Herfort–Ribes1985, printed pages156–159: the exact pro-C conventions and Kurosh statement, Lemma1, Propositions1–2, TheoremA-prime and its complete three-step proof. All four original page images were actually viewed and read.',
          'source_pdf_sha256': sha(pdf),
          'reused_verified_internal_dependencies': 'The actual marked-source maps, odd-kernel comparison and orientation identity of D.55–D.60 retain their earlier complete root audits.',
          'application': 'The actual finite torsion words in the intermediate open subgroup lie in conjugates of its finite Kurosh factors, so the constructed class-two target kills the cone terms.'
        }
        record['additional_peer_claimed'] = False
    (out / 'audit.json').write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n')
    paragraphs = [
      '# ' + statement + ' complete root proof and computation audit',
      'Status: PASS for the frozen proof and the precisely scoped source and replay evidence.',
      'The complete final proof and all mathematical program sources were read. The proof SHA256 is `' + sha(proof) + '`.',
      '\n'.join('- ' + item for item in scopes),
      record['execution_evidence']['scope'],
      'No mathematical correction to the frozen proof was required. The finite executions and the all-level proof review are recorded separately in audit.json.',
      'The source-reading scope, primary evidence and any earlier failed attempts are recorded explicitly in audit.json. This review does not close the original remaining D.13, D.19 or E.23 tasks beyond the stated theorem.'
    ]
    (out / 'audit.md').write_text('\n\n'.join(paragraphs) + '\n')
    print(json.dumps({'statement': statement, 'status': 'PASS', 'audit_sha256': sha(out / 'audit.json')}, ensure_ascii=False), flush=True)
