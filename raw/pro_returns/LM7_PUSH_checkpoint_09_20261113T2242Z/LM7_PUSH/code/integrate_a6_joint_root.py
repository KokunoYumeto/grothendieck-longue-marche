#!/usr/bin/env python3
"""Accept E54 after every complete chain, quotient and word-map audit."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    proof = 'sections/E_a6_joint_agent.tex'
    expected = 'bb32bbc41188d8b0a1da3b65d4680b2e44f64245d89c0ff09a4bf14ef0fcd998'
    assert digest(ROOT / proof) == expected
    audits = {}
    for kind in ('chains', 'quotients'):
        audits[kind] = json.loads((ROOT / 'code' / ('audit_a6_joint_' + kind + '_root.json')).read_text())
        assert audits[kind]['all_passed'] and audits[kind]['original_artifacts_unchanged']
        assert audits[kind]['protected_sha256'][proof] == expected
    assert len(audits['chains']['steps']) == 8 and len(audits['quotients']['steps']) == 20
    morphisms = json.loads((ROOT / 'code/audit_a6_common_generator_morphisms_root.json').read_text())
    assert morphisms['all_passed']
    old = {'E54_audited_source': (ROOT / proof).read_text()}
    saved = ROOT / 'research/checkpoint08_a6_joint_prior_passages.json'
    assert not saved.exists()
    program = ROOT / 'code/assemble_register.py'
    lines = program.read_text().splitlines()
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] not in ('E.2', 'E.3'):
            continue
        old[row[0] + '_coverage'] = row
        assert 'E.54' not in row[1].split('; ')
        state = row[3].replace(
            'The full A6 comparison is under independent replay; compatibility at an arbitrary finite source remains unresolved.',
            'E.54 proves the complete joint A6 and signed source, its exact common '
            'quotient of order1166400000, perfect common residual and full retained '
            'boundary fibres. All864 finite points and all432 multiplier-one full '
            'boundary families survive. The joint four-strand target has the same '
            'specified solvable quotient of order96. Its eight complete chain and '
            'twenty quotient audits pass. The simultaneous A6 and uniform fibre '
            'comparison is under final review; arbitrary finite sources remain unresolved.')
        assert state != row[3]
        lines[i] = ' ' + repr((row[0], row[1] + '; E.54', row[2], state)) + ','
    mainpath = ROOT / 'LM7_PUSH_paper.tex'
    maintext = mainpath.read_text()
    anchor = r'\InputIfFileExists{sections/E_symplectic_integral_common_root.tex}{}{}'
    added = r'\InputIfFileExists{' + proof + r'}{}{}'
    assert maintext.count(anchor) == 1 and added not in maintext
    maintext = maintext.replace(anchor, anchor + '\n' + added)

    bibpath = ROOT / 'LM7_PUSH_references.bib'
    bib = bibpath.read_text()
    entry = (ROOT / 'research/DE_Steinberg.bib').read_text()
    old['Steinberg_original_bibliography_fragment'] = entry
    assert 'DE_Steinberg1967' not in bib
    anchor = 'note = {'
    assert entry.count(anchor) == 1
    entry = entry.replace(anchor, 'note = {verified: original Yale notes PDF opened; ')
    bib += '\n' + entry.strip() + '\n'

    report = ROOT / 'research/report_body.md'
    body = report.read_text()
    anchor = '\nE.55 retains the full 432-point multiplier-one family'
    assert body.count(anchor) == 1
    paragraph = r'''
E.54 determines the complete actual common quotient of the full A6 and signed Ferrari sources. Its order is 1,166,400,000; its three A5 epikernels are the specified indices4,12,18 and its abelian coordinates are the actual exponent sums modulo30. The full signed kernel has rank42, with the two omitted old binary directions identified by the literal projective modulo-four map. The actual common perfect residual is proved using the complete central pullback to SL2(F5)^3: all720615 defining relations and all ten original normal-form links are evaluated, and the complete thirteen-column relation rank includes all thirty central sign freedoms. The exact universal-cover input is Steinberg's Section7 Theorem10 and Corollary2(b), opened in the original Yale notes with the stated finite-field restrictions checked.

The actual closed subgroup gamma5(N) intersected with the lower-central residual of H reaches the full prescribed common kernel. Its correction retains all864 finite old points and every full432-point multiplier-one boundary fibre, with the same Galois value in both sources and with complete generation of the actual joint source. The joint four-strand target retains exactly the old solvable quotient S_L of order96. Five full target chains have indices1,2,6,96,96; equal final orders and747 literal normal conjugations prove the perfect kernel of the specified old quotient map.

Root replayed all eight new complete stabilizer chains in174.520 seconds and all twenty remaining program/comparison steps in%.3f seconds. Every protected original remains unchanged. The first chain driver stopped before any chain ran because it selected a preparation log; the exact failure is preserved and the corrected selection checks every complete record. The first quotient driver stopped on two noncanonical SymPy derived-generator lists. All source generators and point maps were literally equal. The resolution supplies explicit signed words expressing every generator of either list in the other, and independently replays both identity morphisms on the same labelled ambient points. The two original failed files/directories remain unchanged, and the last eight programs execute in a fresh continuation directory. These exact failures and resolutions are recorded in research/E54_root_chain_initial_log_failure.json and research/E54_root_derived_generator_replay_failure.json. The complete proof passes root and an independent reader.
''' % audits['quotients']['seconds']
    body = body.replace(anchor, '\n' + paragraph.strip() + '\n' + anchor)
    prefix = '2. **E.2--E.3:**'
    begin = body.index(prefix)
    end = body.index('\n', begin)
    old['E_remaining'] = body[begin:end]
    current = body[begin:end].replace(
        'The complete joint A6/$G_L$ certificates are replaying independently; the simultaneous A6 and uniform comparison and arbitrary finite sources remain active.',
        'E.54 now proves the complete joint A6/$G_L$ comparison, with all complete certificates independently replayed. The simultaneous A6 and uniform comparison is under final review; arbitrary finite sources remain active.')
    assert current != body[begin:end]
    body = body[:begin] + current + body[end:]
    body += ('\n\nCheckpoint 08 fifth compilation completes 420 pages. Its one '
             '14.47926pt overflow is the D.49.5 group-law display. The entire build '
             'is preserved under build/checkpoint08_fifth_complete. The source now '
             'places its exact definition and group law on two display lines; '
             'research/checkpoint08_fifth_display_repair.json retains both passages.\n')
    saved.write_text(json.dumps(old, indent=2) + '\n')
    program.write_text('\n'.join(lines) + '\n')
    mainpath.write_text(maintext)
    bibpath.write_text(bib)
    report.write_text(body)
    acceptance = {'accepted_statement': 'E.54', 'proof': proof, 'proof_sha256': expected,
                  'complete_root_proof_and_new_code_read': True,
                  'complete_independent_proof_read': True,
                  'root_complete_chain_count': 8,
                  'root_chain_seconds': audits['chains']['seconds'],
                  'root_quotient_step_count': 20,
                  'root_completed_quotient_step_seconds': audits['quotients']['seconds'],
                  'two_noncanonical_arrays_compared_by_exact_identity_word_maps': True,
                  'all_other_arrays_literal': True,
                  'all417_original_artifacts_unchanged': True,
                  'preserved_passages': str(saved.relative_to(ROOT)),
                  'remaining_global_tasks': ['D.1', 'D.2', 'E.2', 'E.3']}
    (ROOT / 'research/checkpoint08_a6_joint_acceptance.json').write_text(
        json.dumps(acceptance, indent=2) + '\n')
    with (ROOT / 'research/root_searches_02.md').open('a') as log:
        log.write('''

128. E54 full root proof and all new Python/C++ collector reads PASS.
     All8 complete chains PASS174.520s; all20 remaining program/comparison
     steps PASS. The initial preparation-log selection failure and strict
     derived-generator-list comparison failure are preserved. The latter
     is resolved by explicit mutual signed-word identity maps on the same
     ambient permutation points; every other array remains literal. The
     continuation retains the failed directory unchanged. All417 frozen
     originals are unchanged. E54 is accepted and integrated; the verified
     Steinberg bibliographic entry is merged with its exact original
     fragment preserved.

129. E57 complete root proof read passes the exact residual ranks9/6,
     power120 congruence correction, direct I fibre product preserving the
     whole E55 word, common sources and target generation. One sentence
     making the onto abelian/derived-coordinate comparison explicit was
     requested before its final manifest. Its independent peer read and
     isolated certificate replay remain to be completed.

130. The general finite character-count argument is now being checked
     for arbitrary normal kernels. Its central scalar detectors allow
     the joint-image argument to use [E,A]=A. The finite lower-central
     residual and actual nilpotent detector quotients are the active
     next step toward the full D1/D2 source comparison. No global task
     status is changed before that complete proof and audit.
''')
    print(json.dumps(acceptance, indent=2))


if __name__ == '__main__':
    main()
