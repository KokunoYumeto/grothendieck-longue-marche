#!/usr/bin/env python3
"""Integrate fully read and independently replayed D49, retaining old text."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent


def main():
    proof = 'sections/D_v4_refinement_agent.tex'
    path = ROOT / proof
    digest = sha256(path.read_bytes()).hexdigest()
    audit = json.loads((ROOT / 'code/audit_v4_refinement_root.json').read_text())
    assert audit['all_passed'] and audit['original_artifacts_unchanged']
    assert audit['proof_sha256'] == digest
    old = {'D49_audited_source': path.read_text()}
    saved = ROOT / 'research/checkpoint08_v4_refinement_prior_passages.json'
    assert not saved.exists()
    program = ROOT / 'code/assemble_register.py'
    lines = program.read_text().splitlines()
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] != 'D.1':
            continue
        old['D.1_coverage'] = row
        assert 'D.49' not in row[1].split('; ')
        state = row[3] + (
            ' D.49 gives the complete V4-outer chief fibre after an explicit '
            'elementary-two refinement, with all actual conjugators and the '
            'entire ordinary union. Its two-character invariant retains every '
            'cover power and path term. The full preceding relative pro-two '
            'source and its specified pro-five action are retained. The remaining '
            'general finite-source lifting problem is still active.')
        lines[i] = ' ' + repr((row[0], row[1] + '; D.49', row[2], state)) + ','
    mainpath = ROOT / 'LM7_PUSH_paper.tex'
    maintext = mainpath.read_text()
    anchor = r'\InputIfFileExists{sections/D_return_tower_agent.tex}{}{}'
    added = r'\InputIfFileExists{' + proof + r'}{}{}'
    assert maintext.count(anchor) == 1 and added not in maintext
    maintext = maintext.replace(anchor, anchor + '\n' + added)

    report = ROOT / 'research/report_body.md'
    body = report.read_text()
    anchor = '\nE.44 constructs the exponent-three class-three boundary quotient'
    assert body.count(anchor) == 1
    paragraph = r'''
D.49 proves the full chief fibre for outer group V4 after an explicit induced elementary-two refinement of the actual finite base. Its central Heisenberg extension defines the two-character surface invariant. Literal boundary pushes and paired pushes give its complete phase image; exact source character orbits determine the entire comparison. Every intermediate cover retains both the dyadic power term and the path term. Actual induced extension maps, all powered boundary-root intersections, the same finite-base-map subtraction and normalizer inversion prove equality of the proper generating fibres. The theorem retains every prescribed conjugator and the full ordinary centralizer union. Its whole-source application retains the entire relative pro-two quotient over the prescribed five-group source and that original maximal pro-five action.

The two D.49 programs independently replay in %.3f seconds. Both complete JSON files and both output logs are byte-identical to their protected originals. They check all 4,116 onto source characters in the two stated genera, every displayed source word and inverse, all 373 nested dihedral-cover cases, and all 18,688 prescribed-conjugator detector cases. The exact D.36 defects are 0,1,1,1,1, including the complete ordinary conjugator union; all four obstructed powers fail the displayed Heisenberg refinements. All 64 D.31 choices agree with the actual Heisenberg relation, and its four ordinary sources each retain 360 proper A6 lifts. The full proof passes two readers. Two earlier source versions are preserved: the induced elementary-two kernel has its explicit permutation action, and each fine cycle origin is now explicitly chosen above its coarse origin. These corrections changed no computation or asserted map.
''' % audit['seconds']
    body = body.replace(anchor, '\n' + paragraph.strip() + '\n' + anchor)
    prefix = '1. **D.1--D.2:**'
    begin = body.index(prefix)
    end = body.index('\n', begin)
    old['D_remaining'] = body[begin:end]
    current = body[begin:end].replace(
        'The full noncyclic outer union and general repeated-prime source refinements remain active.',
        'D.49 proves the full V4 outer union after its actual elementary-two refinement and retains the entire preceding relative pro-two source. Arbitrary finite-source refinements remain active; the general finite scalar-cover detector argument is under independent proof review.')
    assert current != body[begin:end]
    body = body[:begin] + current + body[end:]
    saved.write_text(json.dumps(old, indent=2) + '\n')
    program.write_text('\n'.join(lines) + '\n')
    mainpath.write_text(maintext)
    report.write_text(body)
    acceptance = {'accepted_statement': 'D.49', 'proof': proof,
                  'proof_sha256': digest, 'complete_root_proof_and_code_read': True,
                  'complete_independent_proof_read': True,
                  'root_isolated_replay_seconds': audit['seconds'],
                  'all_JSON_and_output_bytes_equal': True,
                  'preserved_passages': str(saved.relative_to(ROOT)),
                  'remaining_global_tasks': ['D.1', 'D.2', 'E.2', 'E.3']}
    (ROOT / 'research/checkpoint08_v4_refinement_acceptance.json').write_text(
        json.dumps(acceptance, indent=2) + '\n')
    with (ROOT / 'research/root_searches_02.md').open('a') as log:
        log.write('''

126. Root completed the D49 proof and both new program reads. The final
     explicit fine-cycle origin choice is checked against the actual j_C
     injection. Both isolated programs reproduce every JSON byte and every
     log byte, with all protected originals unchanged. A second complete
     proof reader passes the full refinement and whole-source application.
     D49 is integrated, while D1 and D2 remain unresolved.

127. Public searches for prosolvable/prosoluble peripheral automorphism
     lifting and pro-p-to-prosolvable Grothendieck--Teichmuller comparison
     found no theorem resolving the exact remaining map. Primary papers
     on prosoluble free products, unrestricted outer automorphisms, and
     prosolvable surface rigidity appeared; their search abstracts do not
     prove the required peripheral lifting assertion. None is used as a
     theorem in the manuscript from this search. The direct finite
     scalar-cover proof continues independently.
''')
    print(json.dumps(acceptance, indent=2))


if __name__ == '__main__':
    main()
