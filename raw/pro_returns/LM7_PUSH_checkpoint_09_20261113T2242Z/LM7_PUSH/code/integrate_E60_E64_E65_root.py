#!/usr/bin/env python3
"""One-shot integration of three completely read and replayed results."""
from pathlib import Path
from hashlib import sha256
import ast
import json
import re

ROOT = Path(__file__).resolve().parent.parent
SAVED = ROOT / 'research/checkpoint09_covers_characters_prior_passages.json'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    assert not SAVED.exists(), 'This integration has already been performed.'
    replays = {
        'E60': json.loads((ROOT / 'research/root_a6_triple_fibres_replay/result.json').read_text()),
        'E64_first': json.loads((ROOT / 'research/root_hyperelliptic_sewing_replay/result.json').read_text()),
        'E64_second': json.loads((ROOT / 'research/root_cm_norm_characters_replay/result.json').read_text()),
        'E65': json.loads((ROOT / 'research/root_E65_replay/replay_result.json').read_text()),
    }
    assert replays['E60']['status'] == 'PASS_ROOT_COMPLETE_E60_CONTINUATION_REPLAY'
    assert replays['E60']['all_original_files_unchanged']
    assert replays['E60']['complete_target_relation_count'] == 3144734
    assert replays['E64_first']['all_JSON_and_stdout_bytes_identical']
    assert replays['E64_second']['all_JSON_and_stdout_bytes_identical']
    assert replays['E65']['status'] == 'PASS_ISOLATED_E65_REPLAY'
    assert replays['E65']['all_protected_original_hashes_unchanged']
    manifests = {
        'E60': ('code/de_a6_triple_fibres_manifest.json',
                '6fb3b1ace496838ae1825f2fc09f59bdc1f9f8370d89f2c6c7a61b8663d576cb'),
        'E64': ('research/E64_authoritative_manifest.json',
                '063b0bf12da2be7c9ab085d013f69a35d7f6c2d8a8a953e2772fa534bbe07703'),
        'E65': ('research/E65_authoritative_manifest.json',
                'bd3f5301724a493f9e25924d944e36407111d33d7176f93b152a0b052d5bfbf9'),
    }
    for label, (name, expected) in manifests.items():
        assert digest(ROOT / name) == expected, label
        data = json.loads((ROOT / name).read_text())
        records = ({**data['records'], **data['documents']} if label == 'E60'
                   else data['files'] if label == 'E64'
                   else {n: {'sha256': h} for n, h in data['protected_sha256'].items()})
        for path, record in records.items():
            assert digest(ROOT / path) == record['sha256'], path
    proofs = {
        'sections/E_a6_triple_agent.tex': 'ad3b13d61b6e048c93e40ba26c5d6d706592fbddc49a01e809439e72e2541223',
        'sections/E_hyperelliptic_CM_agent.tex': '865c00864680234a840fe80193fedbd8c13f65fa3a162146f0c971178b10236c',
        'sections/E_cm_character_agent.tex': '45fb24828a71b3a2444f32b99625a594092732222065515f848bd49e022f15b9',
    }
    for name, expected in proofs.items():
        assert digest(ROOT / name) == expected
    names = ['LM7_PUSH_paper.tex', 'code/assemble_register.py', 'research/report_body.md',
             'research/root_searches_02.md', 'LM7_PUSH_references.bib']
    old = {name: (ROOT / name).read_text() for name in names}
    new = dict(old)
    anchor = r'\InputIfFileExists{sections/E_sl23_ferrari_agent.tex}{}{}'
    assert new[names[0]].count(anchor) == 1
    new[names[0]] = new[names[0]].replace(anchor, anchor+'\n'+
        r'\InputIfFileExists{sections/E_a6_triple_agent.tex}{}{}')
    anchor = r'\InputIfFileExists{sections/E_gl23_ferrari_agent.tex}{}{}'
    assert new[names[0]].count(anchor) == 1
    new[names[0]] = new[names[0]].replace(anchor, anchor+'\n'+
        r'\subsection{Hyperelliptic descent and the two complex-multiplication comparisons}'+'\n'+
        r'\InputIfFileExists{sections/E_hyperelliptic_CM_agent.tex}{}{}'+'\n'+
        r'\InputIfFileExists{sections/E_cm_character_agent.tex}{}{}')
    lines = new[names[1]].splitlines()
    hits = 0
    final = 'Arbitrary finite pentagon sources remain unresolved.'
    addition = (
        ' E.60 retains every old finite CM point and the entire E.57 boundary '
        'and congruence family through the literal 3.A6 Ferrari source. Its '
        'whole relative kernel has dimension 79 over F3; the preimage of the '
        'old perfect residual has abelianization F3^3 and derived kernel '
        'dimension 76. Exact stable commutators fill all three characters, '
        'and compactness retains every lower-central correction. The actual '
        'four-strand target has specified maximal solvable quotient '
        'S_L times ASL2(F3), of order 20736, with perfect kernel; all six '
        'target chains pass root replay. E.64 proves full hyperelliptic '
        'presentation descent, the selected completed genus-two sewing map, '
        'both exact CM subgroup inclusions and two integral norm characters. '
        'Its separate orbifold discrepancy characters remain unevaluated '
        'on full GT. E.65 constructs the actual continuous quadratic '
        'character Delta on the full gentle group, invariant under every '
        'multiplier and vanishing on Galois. E.58 has Delta equal to one. '
        'The explicit map F to F sigma-inverse to its cube proves that E.3 '
        'is precisely the image of Delta restricted to full GT. This '
        'restriction remains unassigned. '+final)
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] == 'E.3':
            assert row[2] == 'OPEN: full GT image' and row[3].endswith(final)
            old['prior_E3_coverage_row'] = row
            lines[i] = ' '+repr((row[0], row[1]+'; E.60; E.64; E.65', row[2],
                                 row[3][:-len(final)].rstrip()+addition))+','
            hits += 1
        elif row[0] == 'E.2':
            old['prior_E2_coverage_row'] = row
            lines[i] = ' '+repr((row[0], row[1]+'; E.65', row[2], row[3]))+','
    assert hits == 1
    new[names[1]] = '\n'.join(lines)+'\n'
    body = new[names[2]]
    start = body.index('1. **E.3:**')
    end = body.index('\n', start)
    old['prior_current_E3_paragraph'] = body[start:end]
    current = (
        '1. **E.3:** The full profinite GT CM image remains undecided. '
        'E.65 now gives the exact remaining quantity as the image of the '
        'continuous quadratic character Delta restricted to full GT. Its '
        'whole gentle-group extension, arbitrary-multiplier invariance, '
        'Galois vanishing and nonzero E.58 value are proved. Matching a '
        'Galois multiplier and cubing gives the exact comparison with '
        'the specified extra E.1/G6 matrix fibre. E.64 gives actual '
        'hyperelliptic descent, completed genus-two sewing, both CM '
        'braid inclusions, two integral norm characters and the separately '
        'defined orbifold discrepancies; their full-GT values remain '
        'unevaluated. E.60 retains all old CM fibres and the whole E.57 '
        'boundary/congruence system through 3.A6, with full source '
        'corrections and exact common target generation. E.59/E.62 retain '
        'all24 CM pairs through the entire common SL2(F3)/GL2(F3) '
        'class-two correction group. The 2.A6 calculation has exact '
        'kernel dimension128, residual abelianization F2^3, derived '
        'kernel dimension125, a surjective literal W commutator pairing '
        'and all128 corrections with actual Q12 identity. Its signed '
        'common-source and perfect-bridge comparisons are active. The '
        'next work is the actual signed binary pullback and simultaneous '
        'cyclic-cover maps, together with a direct pentagon evaluation '
        'of Delta. No completed finite family is asserted cofinal.')
    body = body[:start]+current+body[end:]
    body += '''

## The complete 3.A6 source, all stable corrections, and the entire target

E.60 is integrated after full root and peer proof/program reads and the isolated root continuation replay. Its actual source projects to B0=im(B -> G_A6 x Q12), whose kernel over G_A6 is the specified Q8. The entire relative kernel is F3^79. All79 coordinates remain available in the exact signed-source fibre product. The new preimage of the old perfect residual has abelianization F3^3, and its derived subgroup is perfect with kernel F3^76. The signed perfect bridge uses the actual A5^3 projections and their specified universal central cover; its two-primary and three-primary kernel maps prove the required perfection.

All60 literal queries were evaluated by the complete C normal form and independently replayed. The six stable vectors have three commutator values with determinant4 modulo3. This fills the entire new residual abelianization. The proof retains every lower-central term of N and then the compact intersection gamma5(N) intersect R_nil(H). Its correction kernel remains onto after retaining the entire old congruence system and the additional E.59/E.62 finite-two-group extension. Consequently every one of the864 old finite points and every432-point multiplier-one boundary family has the full new source fibre available, with the same actual Galois values selected in all new evaluations.

The exact four-strand target quotient has faithful degree2221. Its specified maximal solvable quotient is S_L times ASL2(F3), order20736, with derived orders20736,3456,288,9,1. Six complete literal subgroup chains have indices1,6,72,2304,20736,20736. The final derived inclusion and equal orders prove the entire specified kernel perfect. The full target has order2^406 times3^271 times5^117 times7^8 times11^3 times13^2. Its actual projection to the old signed/A6 target has solvable kernel8 times3^108. The explicit old T23 maps identify the full common target as the fibre product over the displayed solvable quotient, retaining the uniform perfect and Hurwitz factors.

Root's isolated continuation replay completed in346.65seconds. It replayed all1159255 signed-base relations, independently verified the79-word signed lower bound against the previously root-replayed79-dimensional upper bound, evaluated all60 exact queries, and recompiled/replayed all six target chains with3144734 final relations. All11 mathematical JSON outputs, all arrays in seven NPZ outputs, and four exact binary/text outputs agree. All340 frozen original files and documents are unchanged. Discovery-history scan and selected-index fields were compared with their exact replay meanings and preserved separately. Every earlier failed mixture, compile-only stop and provenance-schema stop remains in the frozen package.

## Exact hyperelliptic descent, both CM inclusions, and the remaining characters

E.64 proves the closed presentation-kernel invariance for the full profinite hyperelliptic group in every genus at least two, using the explicit identity Phi(W)=v W^lambda v-inverse. The selected genus-two stabilizer is the exact completed central quotient (B4hat times Zhat)/<(z4,-2)>, with both cut-boundary twists mapping to t and t squared=z4. The completed comparison uses the actual cut-surface and inertia maps. The source audit retains the branch-point-stabilizer capping image and the explicit based-uniqueness counterexample; neither discarded identification enters the proof.

The Mordell inclusion is u->ab, v->b-inverse c b a. The quartic inclusion has d=abc and y=b-inverse d squared b, with y squared=d to the fourth. Their full completed images are the inverse images of the specified cyclic subgroups under the Ferrari fold. Both contain the same free kernel with its actual two-generator basis. The quartic frame is uniquely determined by its conjugacy and its exact projection to the positive harmonic frame. The two normalized actions give integral norm-one characters C3 and C2, with the literal equality of the Ferrari homology matrix and the normalized rigidity shear over each coefficient ring. The positive CM signs and every central carry are retained.

The original orbifold actions have their own explicit central lifts and homology matrices. Their discrepancies D3 and D4 are defined through actual morphisms. The Galois Mordell discrepancy is the inner automorphism by u^(3 rho_K), giving its displayed homology sign. This evaluated Galois formula is not assigned to every full-GT element. The 45-word and14-word programs both pass isolated byte-for-byte root replay, including integral genus-two matrices, the independent free-by-cyclic presentation and both positive CM tables. The seven-page standalone E64 build has zero overfull boxes and no undefined citations/references; all seven pages were visually inspected by its authoring agent. The integrated manuscript has its own later build and visual gate.

## The exact quadratic character reduction of E.3

E.65 constructs the continuous character delta on the multiplier-one full gentle group from the two signed Cartan maps, using the actual finite covariance V=U^(8 rho). Its integral class-two calculation proves rho even. The modulo-four values fix the global signs, and the full pure-frame cocycles prove multiplicativity. The normalized two-by-two intertwiner for every cyclotomic multiplier proves conjugation invariance. Matching an actual Galois multiplier gives the unique continuous extension Delta to the full gentle group that vanishes on Galois; the compact quotient map proves continuity. The E.58 full gentle element has Delta equal to one.

The final comparison with the question is explicit: F maps to H=F sigma-inverse and then H cubed. Cubing preserves the quadratic value and makes rho zero modulo3, so V12 and q12(f) are identity. The resulting actual automorphism preserves N_B and its characteristic sixth-power commutator kernel, hence gives the specified G6 CM fibre. E.3 is therefore exactly the image of Delta restricted to full profinite GT. That image is not assigned by E.65 and remains Open.

Root read the complete proof and every line of the independent standard-library certificate, reopened Marin's primary Lemmas4.1--4.3, and executed the isolated replay in0.038363seconds. Every mathematical JSON field agrees and all nine protected originals are unchanged. The625 integral class-two tests, all576 Cartan-pair products, all136 normalizer character checks and all256 products in the dihedral common-abelianization fibre product supplement the exact source and continuity proof. The initial reviewed draft and the printed-source typo correction are preserved. No prounipotent comparison or unproved full-GT abelianization statement is used to assign the remaining character value.
'''
    new[names[2]] = body
    new[names[3]] += '''

157. E60 complete isolated root continuation replay PASS,346.65seconds.
     The full signed base has1159255 checked relations; all79 new
     signed words give the complete previous kernel by an invertible
     transition. All60 normal-form queries and all six target chains
     pass, with3144734 final target relations. All11 mathematical JSON,
     seven NPZ and four byte outputs agree, and all340 protected
     originals remain unchanged. Full source, bridge, compactness and
     target proof/program reads pass independently. E60 is integrated.

158. E65 isolated root replay PASS,0.038363seconds. Every mathematical
     JSON field is identical and all nine protected originals remain
     unchanged. E64's final seven-page standalone layout also passes,
     with no source edits after root's proof and both-program replays.
     E60,E64,E65 and three opened E64 references are integrated with
     complete prior active passages preserved in the named checkpoint09
     acceptance record. E3 remains Open, now with the exact restricted
     quadratic character and its actual matrix-fibre comparison.
'''
    extra = (ROOT / 'research/E64_references.bib').read_text()
    keys = re.findall(r'@\w+\{([^,]+),', extra)
    assert len(keys) == 3
    assert not set(keys) & set(re.findall(r'@\w+\{([^,]+),', new[names[4]]))
    new[names[4]] += '\n'+extra
    SAVED.write_text(json.dumps(old, indent=2)+'\n')
    for name in names:
        (ROOT / name).write_text(new[name])
    result = {'statements': ['E.60', 'E.64', 'E.65'],
              'complete_root_proof_and_program_reads': True,
              'independent_peer_proof_reads': True,
              'root_isolated_replay_statuses': {k: v['status'] for k, v in replays.items()},
              'proof_sha256': proofs,
              'manifest_sha256': {k: value for k, (name, value) in manifests.items()},
              'new_primary_bibliography_keys': keys,
              'preserved_prior_files_and_passages': str(SAVED.relative_to(ROOT)),
              'E3_status': 'Open'}
    (ROOT / 'research/checkpoint09_covers_characters_acceptance.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
