#!/usr/bin/env python3
"""Integrate the exact, independently replayed E73 source comparison once."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent
SAVED = ROOT / 'research/checkpoint09_double_E62_deep_prior_passages.json'


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def main():
    assert not SAVED.exists(), 'Integration already performed.'
    replay = json.loads((ROOT / 'research/root_E73_deep_replay/replay.json').read_text())
    assert replay['status'] == 'PASS_COMPLETE_ISOLATED_E73_REDUCED_DEEP_SOURCE'
    assert replay['protected_originals_unchanged'] == 73
    assert replay['all144_binary_and42_ternary_stage_words_replayed']
    assert len(replay['exact_complete_chain_inputs_and_binaries']) == 12
    for name, h in replay['protected_sha256'].items():
        assert digest(ROOT / name) == h, name
    proof = 'sections/E_double_E62_deep_root.tex'
    assert digest(ROOT / proof) == '344ae0bdc91c85ab2d1fa60b5d646186763d63bf66aa1d9175a70a171f4653ac'
    peer = 'research/BC_E73_deep_independent_audit.md'
    assert digest(ROOT / peer) == '1852107aacef37a9fd26bec6278d83eea0f739dbf218738ed8559f6c7368d455'
    kernel = json.loads((ROOT / 'code/e_a6_double_E62_kernel_root.json').read_text())
    independent = json.loads((ROOT / 'code/e_a6_double_E62_kernel_replay_root.json').read_text())
    literal = json.loads((ROOT / 'code/e_a6_E62_deep_replay_root.json').read_text())
    assert kernel['status'] == 'PASS_COMPLETE_JOINT_KERNEL'
    assert kernel['all_Schreier_relators_evaluated']
    assert kernel['lifted_relators_evaluated'] == kernel['complete_base_relator_count'] == 1279851
    assert kernel['kernel_dimension'] == 163
    assert independent['status'] == 'PASS_INDEPENDENT_COMPLETE_DOUBLE_SIGNED_E62_SOURCE'
    assert independent['kernel_over_entire_old_J_and_E62_dimension'] == 122
    assert independent['actual_J2_E62_maximum_common_quotient_order'] == '95551488'
    for name, h in independent['input_sha256'].items():
        assert digest(ROOT / 'code' / name) == h, name
    assert literal['E62_image_of_I_intersect_kernel_J2_order'] == 64
    names = ['LM7_PUSH_paper.tex', 'code/assemble_register.py',
             'research/report_body.md', 'research/root_searches_02.md']
    old = {name: (ROOT / name).read_text() for name in names}
    new = dict(old)
    anchor = r'\InputIfFileExists{sections/E_wajnryb_homology_agent.tex}{}{}'
    assert new[names[0]].count(anchor) == 1
    new[names[0]] = new[names[0]].replace(
        anchor, anchor + '\n' + r'\InputIfFileExists{' + proof + '}{}{}')
    ending = 'Arbitrary finite pentagon sources remain unresolved.'
    addition = (
        ' E.73 computes the actual double-cover/E.62 common quotient, of '
        'order 2^17 times 3^6, retaining the complete signed source. '
        'Its old-J/E.62 identity kernel is exactly the 122-dimensional '
        'kernel of the perfect bridge. On N-prime, descent by the actual '
        'C_J2-times-identity subgroup identifies the reduced source with '
        'V6 times the entire E.62 class-two two-group, through six explicit '
        'parity masks. On I=gamma5(Nhat) intersect R_nil(H), the exact '
        'image is V6 times the 2^15-element intersection of that two-group '
        'with the whole H-image nilpotent residual. Nested compact source '
        'fibres and the matching full-H upper bound prove both inclusions. '
        'Every fixed J2 value has precisely a coset of the 64-element '
        'E.62 kernel, with the entire common word-kernel fibre. Additional '
        'prescribed pentagon targets in these cosets remain to be evaluated. ' + ending)
    lines = new[names[1]].splitlines()
    found = 0
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] == 'E.3':
            assert row[2] == 'OPEN: full GT image' and row[3].endswith(ending)
            old['prior_E3_coverage_row'] = row
            lines[i] = ' ' + repr((row[0], row[1] + '; E.73', row[2],
                row[3][:-len(ending)].rstrip() + addition)) + ','
            found += 1
    assert found == 1
    new[names[1]] = '\n'.join(lines) + '\n'
    pending = 'Preservation of the E.59/E.62 binary values requires its actual common-source comparison.'
    assert new[names[2]].count(pending) == 1
    new[names[2]] = new[names[2]].replace(pending,
        'E.73 now determines that actual common source and its entire deep '
        'correction image. Its reduced I image has order 3^6 times 2^15, '
        'and the E.62 values over a fixed J2 value form a coset of a '
        '64-element subgroup. Evaluating the prescribed pentagon targets '
        'against these actual cosets is the next source comparison.')
    new[names[2]] += f'''

## The exact double-cover and E.62 image on the deep source

E.73 retains the entire 15774-point A6/A5/E.62 common source. All 1279851 final Schreier relations are evaluated in both lifted models. The relative binary kernel has dimension 163 inside the actual 128+42-dimensional coordinate product. Its projections have dimensions 125 and 41. The independent full replay checks all 407 base words, all 163 kernel words and all 326 original-generator conjugates. The actual maximum J2/E.62 common quotient has order 95551488. The full identity kernel over old J and E.62 is the same 122-dimensional kernel of the perfect bridge, with zero image in E2's three-dimensional abelianization.

The descent is on the exact N_B-prime domain. Goursat's quotient is a quotient of the E.62 two-group, so the perfect subgroup C_J2 has trivial image in it. Thus C_J2 times the identity lies in the actual common source. The retained old-J comparison and the 122-dimensional kernel equality identify the kernel of the map to (P-prime/C) times C62 with precisely this subgroup. The reduced image is the graph of the explicit six-mask homomorphism from the entire ordered E.62 two-group to W, together with the independent rank-six ternary factor. All 576 ordered basis products and all 4656 original N commutators verify this map with the actual central carries.

Successive commutators with N retain the complete binary order 2^24 through gamma5(N). Commutators with the ten literal H generators give binary orders 2^18, 2^15 and 2^15, while the ternary rank stays six. Each finite image has actual source words. Perfection retains C_J2 times the identity in every full image. Nested compact fibres provide preimages in I=gamma5(Nhat) intersect R_nil(H). Independently, six complete Schreier certificates compute the whole H lower-central residual, its intersection with C62 and their actual product. The intersection has order 2^15 and contains the stable lower image, proving equality and the full upper bound. The reduced I image has order 23887872. Its projection to the entire E.63 I image leaves precisely the 64-element E.62 kernel, with exact value cosets and complete word fibres.

Root and geometry read the full proof and all four reduced-source programs. Root's isolated replay passes in {replay['seconds']} seconds: all four mathematical outputs and every NPZ value, shape and dtype agree; all six complete H-certificate inputs and binaries are byte-identical and independently replayed; all 73 protected originals are unchanged. The independent literal replay checks 144 binary and 42 ternary stage words through 1105 original B-word ancestors. The earlier complete enlarged-source collector takes 972.033 seconds and its independent full-model replay 13.279641 seconds. All routed input provenance hashes are checked against the exact bytes before provenance fields are omitted from output equality.

The first collector used a shared DAG for an additional projection-only calculation, appending three unrelated nodes after the exported source grades. Its complete successful mathematical output and code are preserved; the corrected version separates that projection DAG and asserts equal source-grade lengths. A first literal replay lacked a named commutator method in the retained SolvableB interface and failed before certification. Its code and failure are preserved; a local subclass supplies the literal operation without modifying the accepted implementation. Earlier proof typography is also preserved. Every passage changed by this integration is retained in checkpoint09_double_E62_deep_prior_passages.json. E.3 remains Open while the prescribed target evaluation and full pentagon comparison continue.
'''
    new[names[3]] += f'''

176. E73 complete root and geometry proof/four-program reads PASS.
     Root isolated replay PASS {replay['seconds']} seconds, all 73 originals
     unchanged, every mathematical output and array exact, all six full
     H-certificate inputs/binaries byte-identical and independently replayed.
     The enlarged source evaluates all 1279851 relations and has binary
     relative rank 163. Its old-J/E62 identity kernel is the retained
     122-dimensional bridge kernel. The exact N-prime descent gives the
     graph of six explicit masks over C62, with independent V6. The full
     I image is V6 times the order-2^15 H-residual intersection, proved
     by nested compact fibres and a matching full-H upper comparison.
     Each fixed J2 value has an entire 64-element E62 coset. Individual
     prescribed pentagon targets remain to be evaluated in these cosets.
'''
    SAVED.write_text(json.dumps(old, indent=2) + '\n')
    for name in names:
        (ROOT / name).write_text(new[name])
    accepted = {'statement': 'E.73', 'full_root_proof_and_program_reads': True,
                'peer_audit_sha256': digest(ROOT / peer),
                'proof_sha256': digest(ROOT / proof),
                'isolated_replay_seconds': replay['seconds'],
                'protected_originals_unchanged': 73,
                'complete_H_certificates_replayed': 6,
                'preserved_prior_passages': str(SAVED.relative_to(ROOT)),
                'E3_status': 'Open'}
    (ROOT / 'research/checkpoint09_double_E62_deep_acceptance.json').write_text(
        json.dumps(accepted, indent=2) + '\n')
    print(json.dumps(accepted, indent=2))


if __name__ == '__main__':
    main()
