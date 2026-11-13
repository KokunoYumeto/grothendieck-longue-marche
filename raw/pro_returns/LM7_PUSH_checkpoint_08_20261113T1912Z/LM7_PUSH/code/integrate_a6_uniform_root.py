#!/usr/bin/env python3
"""Accept E57 after complete proof review and all four isolated replays."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    proof = 'sections/E_a6_uniform_agent.tex'
    expected = 'cf54237143936a0825f2a9f97a6096366599a6139dc2bdcc1366acfd4bf017f5'
    assert digest(ROOT / proof) == expected
    audit = json.loads((ROOT / 'code/audit_a6_uniform_root.json').read_text())
    assert audit['all_passed'] and audit['original_artifacts_unchanged']
    assert audit['proof_sha256'] == expected and len(audit['steps']) == 4
    assert audit['steps'][2]['complete_final_Schreier_relations'] == 219684
    old = {'E57_audited_source': (ROOT / proof).read_text()}
    saved = ROOT / 'research/checkpoint08_a6_uniform_prior_passages.json'
    assert not saved.exists()
    program = ROOT / 'code/assemble_register.py'
    lines = program.read_text().splitlines()
    changed = []
    prior = ('The simultaneous A6 and uniform fibre comparison is under final review; '
             'arbitrary finite sources remain unresolved.')
    replacement = ('E.57 retains every whole E.55 word, for all432 multiplier-one '
                   'points and every full admitted boundary parameter, through '
                   'the full A6 source and the entire congruence system. The '
                   'actual common quotient remains the signed level-five '
                   'quotient, and the exact residual correction, common source '
                   'fibres and full target products are proved. All four new '
                   'certificate steps, including219684 complete target relations, '
                   'pass isolated replay. Arbitrary finite sources remain unresolved.')
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] not in ('E.2', 'E.3'):
            continue
        old[row[0] + '_coverage'] = row
        assert 'E.57' not in row[1].split('; ') and row[3].count(prior) == 1
        lines[i] = ' ' + repr((row[0], row[1] + '; E.57', row[2],
                              row[3].replace(prior, replacement))) + ','
        changed.append(row[0])
    assert changed == ['E.2', 'E.3']

    mainpath = ROOT / 'LM7_PUSH_paper.tex'
    maintext = mainpath.read_text()
    anchor = r'\InputIfFileExists{sections/E_symplectic_integral_targets_agent.tex}{}{}'
    added = r'\InputIfFileExists{' + proof + r'}{}{}'
    assert maintext.count(anchor) == 1 and added not in maintext
    maintext = maintext.replace(anchor, anchor + '\n' + added)

    report = ROOT / 'research/report_body.md'
    body = report.read_text()
    anchor = '\n## Typesetting verification'
    assert body.count(anchor) == 1
    paragraph = '''
E.57 proves that each complete E.55 word, for all432 multiplier-one points and every admitted full boundary parameter, extends through the full A6 source while retaining its entire signed and integral symplectic values. The actual closed residual image is the displayed fibre product over SL2(F5), and its correcting subgroup reaches the whole required A6 kernel while killing both old maps. The uniform residual correction remains exactly the level-five congruence subgroup times all higher prime factors and the full rank-three additive module. The proofs give the actual finite common quotients Q_m*, the inverse-limit quotient, both complete word fibres, and the full four- and five-strand target products. All are comparisons of the specified source maps.

The complete E.57 proof passes root and an independent reader at SHA256 cf54237143936a0825f2a9f97a6096366599a6139dc2bdcc1366acfd4bf017f5. Root read all three new Python programs and replayed all four certificate steps in10.229 seconds. The536-point target chain checks all219684 final Schreier relations. Every mathematical JSON record and every literal NPZ array agrees; provenance hashes are verified against each replay's own inputs. All450 manifest files and the further protected audit inputs remain unchanged. The two preliminary encoding and polynomial-expansion failures remain preserved with their exact sources and outputs.
'''
    body = body.replace(anchor, '\n' + paragraph.strip() + '\n' + anchor)
    prefix = '2. **E.2--E.3:**'
    begin = body.index(prefix)
    end = body.index('\n', begin)
    old['E_remaining'] = body[begin:end]
    prior = ('The simultaneous A6 and uniform comparison is under final review; '
             'arbitrary finite sources remain active.')
    replacement = ('E.57 now retains every complete E.55 word through the full A6 '
                   'source, with the exact common congruence quotient and all '
                   'joint targets. Its full proof and all four new certificate '
                   'steps pass independent review. The explicit central-three '
                   'A6 cover is the next finite comparison; arbitrary finite '
                   'sources remain active.')
    assert body[begin:end].count(prior) == 1
    body = body[:begin] + body[begin:end].replace(prior, replacement) + body[end:]

    saved.write_text(json.dumps(old, indent=2) + '\n')
    program.write_text('\n'.join(lines) + '\n')
    mainpath.write_text(maintext)
    report.write_text(body)
    acceptance = {'accepted_statement': 'E.57', 'proof': proof,
                  'proof_sha256': expected, 'complete_root_proof_and_code_read': True,
                  'complete_independent_proof_read': True,
                  'root_certificate_steps': 4,
                  'complete_final_target_relations': 219684,
                  'all_mathematical_JSON_and_literal_arrays_equal': True,
                  'root_seconds': audit['seconds'],
                  'preserved_passages': str(saved.relative_to(ROOT)),
                  'remaining_global_tasks': ['D.1', 'D.2', 'E.2', 'E.3']}
    (ROOT / 'research/checkpoint08_a6_uniform_acceptance.json').write_text(
        json.dumps(acceptance, indent=2) + '\n')
    with (ROOT / 'research/root_searches_02.md').open('a') as log:
        log.write('''

131. E57 is accepted after the complete root and geometry proof reads,
     all three new Python reads, and all four isolated certificate
     replays. Mathematical JSON and every NPZ array agree literally;
     the complete536-point chain checks219684 final relations. The
     exact full-word correction, common quotient and target products
     are retained. The frozen source SHA is cf54237143936a0825f2a9f97a
     6096366599a6139dc2bdcc1366acfd4bf017f5. Root runtime10.229s.

132. D50's final residual comparison and actual aligned row breaks
     were read and accepted by root and geometry, SHA b27a2116165d03c9
     75e4022125e92fcbf3e599f25d217b350f32a8ec26ef3ff9. Its independent
     finite scalar-cover program is fully read and replayed literally:
     420 Q8 phase cases,848 noncentral-kernel cases,1088 proper-subgroup
     counts,136 ordinary Mobius counts,3672 boundary transports,
     331776 pair-group products, and the nonfaithful32-point pullback.
     All original hashes are unchanged; root runtime0.239s. The four
     normalized free-Lie source witnesses also pass isolated literal
     replay, with exact rescalings2,3/2,-1,3 and common denominator2;
     root runtime0.387s. D51/D52 are being written before global
     task statuses are changed.

133. Turaev, Sections of fiber bundles over surfaces, arXiv0904.2692,
     was reopened at the primary PDF. Lemma2.1 constructs the scalar
     cocycle; Section2.3 constructs the relative boundary class; the
     positive-genus restriction is explicit in Section2.4. Theorem1.2
     supplies the comparison count in its stated scope. D50 proves
     its required pants count directly, including every proper J,
     without extending that theorem past its boundary hypotheses.
     Searches for a ready-made full peripheral pronilpotent lifting
     result supplied no exact theorem used here. Reopened Marin and
     Nakamura--Tsunogai--Yasuda sources retain their already recorded
     GT/Galois scopes; no CM transfer is inferred from the reread.
''')
    print(json.dumps(acceptance, indent=2))


if __name__ == '__main__':
    main()
