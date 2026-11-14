#!/usr/bin/env python3
"""One-shot integration after the complete isolated E63 replay passes."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent
SAVED = ROOT / 'research/checkpoint09_double_cover_prior_passages.json'
MANIFEST_HASH = '2544ec463ef4885ea61d76fa476c43cc60fdf2be367b6d2af4d2fd49d108d7a8'
PROOF_HASH = 'b76b93d7468e5f16826f17c73b2cd92539a5d6ad05700e1d666e203bc3933441'


def main():
    assert not SAVED.exists(), 'This integration has already run.'
    manifest_path = ROOT / 'code/de_a6_double_source_manifest.json'
    assert sha256(manifest_path.read_bytes()).hexdigest() == MANIFEST_HASH
    manifest = json.loads(manifest_path.read_text())
    for name, record in {**manifest['records'], **manifest['documents']}.items():
        assert sha256((ROOT / name).read_bytes()).hexdigest() == record['sha256'], name
    assert sha256((ROOT / 'sections/E_a6_double_agent.tex').read_bytes()).hexdigest() == PROOF_HASH
    replay_path = ROOT / 'research/root_e63_complete_replay/replay.json'
    replay = json.loads(replay_path.read_text())
    assert replay['status'] == 'PASS_COMPLETE_ISOLATED_E63_REPLAY'
    assert replay['mode'] == 'complete' and replay['complete_new_relations_repeated']
    assert replay['all_originals_unchanged']
    assert replay['every_omitted_input_hash_independently_verified']
    assert replay['manifest_sha256'] == MANIFEST_HASH
    assert replay['protected_original_count'] == 665
    assert all(row['status'] == 'PASS' for row in replay['steps'])
    names = ['LM7_PUSH_paper.tex', 'code/assemble_register.py',
             'research/report_body.md', 'research/root_searches_02.md']
    old = {name: (ROOT / name).read_text() for name in names}
    new = dict(old)
    anchor = r'\InputIfFileExists{sections/E_gl23_ferrari_agent.tex}{}{}'
    assert new[names[0]].count(anchor) == 1
    new[names[0]] = new[names[0]].replace(anchor, anchor + '\n' +
        r'\InputIfFileExists{sections/E_a6_double_agent.tex}{}{}')
    ending = 'Arbitrary finite pentagon sources remain unresolved.'
    addition = (
        ' E.63 proves the complete 2.A6 source and its exact signed common '
        'quotient of order 9331200000. The entire 125-dimensional relative '
        'binary kernel survives while preserving the signed, triple-cover, '
        'uniform congruence and nilpotent boundary system of E.60. Its '
        'perfect common residual has relative kernel dimension 122, and '
        'stable actual commutators fill all three remaining characters. '
        'Every specified finite point and full boundary family extends '
        'with the same Galois values. The double/triple joint target is '
        'the exact fibre product over the old signed-A6 target, with '
        'order 2^557*3^271*5^117*7^8*11^3*13^2 and a perfect kernel over '
        'the specified order-20736 solvable quotient. All four new complete '
        'source presentations and independent literal replays pass root '
        'isolated replay. The additional E.59/E.62 source overlap is being '
        'computed through its actual enlarged source. ' + ending)
    lines = new[names[1]].splitlines()
    hits = 0
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] == 'E.3':
            assert row[2] == 'OPEN: full GT image' and row[3].endswith(ending)
            old['prior_E3_coverage_row'] = row
            lines[i] = ' ' + repr((row[0], row[1] + '; E.63', row[2],
                                  row[3][:-len(ending)].rstrip() + addition)) + ','
            hits += 1
    assert hits == 1
    new[names[1]] = '\n'.join(lines) + '\n'
    prior = ('The 2.A6 target has a completely replayed perfect kernel and the '
             'specified solvable quotient of order 96. Its signed source has '
             'exact relative kernel dimension 125 and an identified candidate '
             'common quotient whose remaining source factorization is being checked.')
    assert new[names[2]].count(prior) == 1
    new[names[2]] = new[names[2]].replace(prior,
        'E.63 proves both source factorizations through the actual signed '
        'common quotient of order9331200000 and its exact fibre product. '
        'All125 relative binary corrections retain the full specified E.60 '
        'system, and the double/triple target product has the stated '
        'order20736 solvable quotient with perfect kernel.')
    seconds = replay['seconds']
    provenance_count = replay['verified_input_hash_count']
    new[names[2]] += f'''

## The complete central double cover and its actual signed source

E.63 uses the literal map SL2(F9)→A6, all212 free epikernels and the full lifted Nielsen action. The six-evaluation source X2 has relative kernel F2^128 over the retained A6 source. All865049 source relations were evaluated, with every independent kernel word and source conjugate checked again in the full model. The full preimage E2 of the old perfect residual has abelianization F2^3; its derived group D2 is perfect and has relative kernel dimension125.

The exact signed bridge is determined by a complete43-column presentation of E2×_(A5^3)SL2(F5)^3. All720615 final relations and ten original-generator links give rank37, so the full pullback abelianization is F2^6. The three Schur signs inject into it. Its derived group projects isomorphically onto D2, providing the actual surjection D2→SL2(F5)^3. The central sign map has rank three on the125-dimensional kernel, leaving dimension122. The universal central-cover property then proves the perfection of D2×_(SL2(F5)^3)C_L, through an explicit commutator equality for its entire kernel.

The900-point signed quotient is constructed from an explicit SL2(F5) matrix pair, all six induced cosets and the two ordinary exponent coordinates modulo30. Its pure image is SL2(F5)^3×(Z/30)^2 and its whole order is9331200000. The complete G_L and X2 factorization calculations evaluate25965 and865049 relations, respectively. The independent actual X2/G_L joint calculation evaluates1154659 relations and has kernel rank167 inside the full128+42 coordinate product. Its maximum common quotient therefore equals the constructed signed quotient through the two specified maps. The relative kernel over the entire old J source has dimension125. Every transporter, free-character twist and all six induced signs are retained.

The deep-source proof does not rely on the chosen basis representatives lying in N_B-prime. It uses six actual N_B module words, corrected to the literal Q12 identity without changing their complete double-cover values. Their three specified commutators fill the whole E2 abelianization. Together with the perfect bridge they prove the exact image at every lower-central depth and, by nested compact fibres, on I=gamma5(Nhat_B) intersect R_nil(H). The actual old uniform/triple image on the signed kernel has no C2 quotient, so Goursat retains all125 corrections while fixing that entire old system. Every old finite point and multiplier-one full boundary family extends with the same actual Galois values; both corrected source generation and the full word-kernel fibres are proved.

The target calculation retains all three exact maps T2→T0←T3. The double relative kernel is elementary binary of dimension151. The triple relative kernel maps onto ASL2(F3), with kernel3^105 and abelianization of odd order. These maps prove the actual joint fibre product, of order2^557·3^271·5^117·7^8·11^3·13^2. Its kernel over Sigma=S_L×ASL2(F3) is perfect, proved through both actual projections. The T23, uniform and Hurwitz target maps remain simultaneous. The E.59/E.62 source comparison is a further named calculation and is not inferred from this target result.

Root and arithmetic read the complete source proof and both target fragments. Root read every new mathematical program, generated collector and independent replay. The complete isolated root replay passes in{seconds}seconds, repeating all four new full presentation calculations and all independent word and matrix checks. Every mathematical JSON field and NPZ array agrees, all665 protected originals are unchanged, and{provenance_count} input hashes are validated against their exact original or regenerated file bytes before provenance fields are omitted from mathematical equality. The earlier selected-row and partial signed probes, interrupted candidate session, initial source typography, and first successful replay wrapper are preserved with their exact scope. The strengthened wrapper changes only explicit provenance validation.
'''
    new[names[3]] += f'''

170. E63 full source proof, both root target fragments and every new
     mathematical program/collector/replay pass root and arithmetic read.
     Complete isolated root replay PASS{seconds}seconds: all four new full
     presentation calculations, all literal words and all mathematical
     JSON/NPZ values agree;665 original files are unchanged and
     {provenance_count} exact routed input hashes are explicitly validated.
     The signed common quotient is the actual9331200000-element group;
     the full relative correction kernel is125-dimensional, with the
     perfect122-dimensional bridge and all three stable characters retained.
     The exact source and target scopes are integrated as E63. E3 is open.

171. Root's enlarged A6/A5/E62 actual base is a15774-point permutation
     action. All1279851 final Schreier relations pass;407
     strong words and13526 DAG nodes are retained. The subsequent full
     signed/binary collector and independent literal replay determine
     the exact additional common source. Earlier finite probes retain
     only their literal N-word values, with no unsupported N-prime claim.
'''
    SAVED.write_text(json.dumps(old, indent=2) + '\n')
    for name in names:
        (ROOT / name).write_text(new[name])
    acceptance = {
        'statement': 'E.63', 'full_root_and_peer_proof_reads': True,
        'full_root_program_and_collector_reads': True,
        'complete_isolated_root_replay': str(replay_path.relative_to(ROOT)),
        'manifest_sha256': MANIFEST_HASH, 'source_proof_sha256': PROOF_HASH,
        'protected_original_count': 665, 'verified_input_hash_count': provenance_count,
        'preserved_prior_passages': str(SAVED.relative_to(ROOT)), 'E3_status': 'Open',
    }
    (ROOT / 'research/checkpoint09_double_cover_acceptance.json').write_text(
        json.dumps(acceptance, indent=2) + '\n')
    print(json.dumps(acceptance, indent=2), flush=True)


if __name__ == '__main__':
    main()
