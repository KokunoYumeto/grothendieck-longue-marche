#!/usr/bin/env python3
"""Integrate independently audited D38 and E47, retaining preceding passages."""
from pathlib import Path
import ast
import json

ROOT = Path(__file__).resolve().parent.parent


def main():
    for name in ('audit_weight5_constraints_root', 'audit_integral_class_three_root'):
        audit = json.loads((ROOT / 'code' / (name + '.json')).read_text())
        assert audit['all_passed'] and audit['original_artifacts_unchanged']
    previous = {}
    saved = ROOT / 'research/checkpoint06_integral_class3_prior_passages.json'
    assert not saved.exists()
    program = ROOT / 'code/assemble_register.py'
    lines = program.read_text().splitlines()
    for i, line in enumerate(lines):
        text = line.strip()
        if not text.startswith("('"):
            continue
        row = ast.literal_eval(text.rstrip(','))
        if row[0] not in ('D.1', 'D.2', 'E.2', 'E.3'):
            continue
        previous[row[0]] = row
        refs = row[1] + ('; D.38' if row[0].startswith('D') else '; E.47')
        if row[0] == 'D.1':
            description = ('The actual geometric S3 action excludes dimension two. Fully invariant '
                'finite five-group targets carry all three ordinary special outer parameters. '
                'Every first-precision parameter is class-preserving with an exact elementwise '
                'conjugator. All A6 chief steps over an odd-order base have the proved equal '
                'positive generating-lift count, including coupled odd pullbacks. The ordinary '
                'even-base A6^20 obstruction and all earlier lifting comparisons remain retained. '
                'Realization or exclusion of the two-dimensional complement through every finer '
                'full finite source remains.')
        elif row[0] == 'D.2':
            description = row[3] + (' The exact odd-base A6 chief comparison now fixes every '
                'prescribed peripheral conjugator and counts every generating lift at that stage.')
        elif row[0] == 'E.2':
            description = ('All24 CM fibres survive every proved refinement through E47. The full '
                'three-adic class-three boundary correction-image fibre is Z3^70 over every '
                'one of the432 multiplier-one sources. Four rational equations and two '
                'integral residue tests give its exact class-two projection. Its complete '
                'exponent-three image has3^25 points per source, with a specified finite '
                'nonlift surviving every change of higher class-two digits. The defined '
                'binary, prime-supported, SL2(F5) and Hurwitz common families are retained. '
                'Full profinite survival remains.')
        else:
            description = ('All864 degree-six points pass the retained pentagons, braid and '
                'twist relations. The actual SL2(F5) source maps onto the five-point Hurwitz '
                'source; the same word retains both through E47\'s complete integral '
                'class-three families at multiplier one. Their full common four-strand '
                'target is (T23 times over S_L T_L) times A96. The A6 kernel/outer tests '
                'also retain all864 points in their stated common sources. Compatibility '
                'through every finite quotient remains.')
        lines[i] = ' ' + repr((row[0], refs, row[2], description)) + ','
    assert set(previous) == {'D.1', 'D.2', 'E.2', 'E.3'}
    mainpath = ROOT / 'LM7_PUSH_paper.tex'
    maintext = mainpath.read_text()
    for old, new in [('D_weight5_agent', 'D_weight5_constraints_agent'),
                     ('E_hurwitz_five_root', 'E_integral_class_three_agent')]:
        anchor = r'\InputIfFileExists{sections/' + old + '.tex}{}{}'
        assert maintext.count(anchor) == 1
        maintext = maintext.replace(anchor, anchor + '\n' +
                    r'\InputIfFileExists{sections/' + new + '.tex}{}{}')
    anchor = 'This working manuscript is \\textbf{INCOMPLETE};'
    assert maintext.count(anchor) == 1
    maintext = maintext.replace(anchor,
        'The complete integral three-adic class-three boundary fibre is '
        '$\\mathbb Z_3^{70}$; its exact exponent-three image has $3^{25}$ points '
        'per retained source and excludes a specified finite shadow. ' + anchor)
    report = ROOT / 'research/report_body.md'
    text = report.read_text()
    anchor = '\nE.44 constructs the exponent-three class-three boundary quotient'
    assert text.count(anchor) == 1
    paragraph = ('\nD.38 gives exact elementwise conjugators for every first-precision '
        'weight-five parameter, including the restricted fifth powers needed in1200 of3125 '
        'executed cases. The nonzero ordinary outer classes remain those proved in D.37. '
        'For every A6 chief extension over a finite odd-order base, the actual outer cocycle '
        'is removed by the displayed averaging gauge. The cover, root-class and minimal '
        'normalizer maps then give the exact equal positive generating-lift count with '
        'all prescribed conjugators, all unit multipliers and coupled odd pullbacks. '
        'The literal odd S6 conjugation realizes the required target power classes; '
        'all16 units modulo60 are checked on all360 elements. Both independent replays '
        'pass in4.444s with byte-identical JSONs and unchanged originals. The precise '
        'comparison with D.33–D.36 is retained in the proof.\n')
    text = text.replace(anchor, paragraph + anchor)
    anchor = '\n## Geometric and germ results'
    assert text.count(anchor) == 1
    paragraph = ('\nE.47 determines the complete integral class-three pro-three boundary '
        'correction-image fibre over every retained multiplier-one point. Its actual '
        'Hall lattice has385 coordinates with the central divisibility by three retained. '
        'The660-by330 central norm matrix has Smith factors1^264,3,3,0^64. Four exact '
        'rational conditions and two integral residue conditions give the entire projection '
        'to E.37. A common unit minor solves the four rational coordinates; all nine residue '
        'charts have the same invertible two-column minor. The explicit central right '
        'inverse and saturated rank64 kernel give the full Z3^70 parametrization. Actual '
        'profinite word fibres are separately identified as cosets of the specified joint '
        'kernel. Over a fixed exact E.37 point, the finite central image has dimension21. '
        'One actual change of a higher lower-coordinate digit supplies its complementary '
        'direction, giving all22 finite central directions when higher digits may vary. '
        'Two additional finite lower equations give the exact total3^25 images per source. '
        'The explicit Y41=1 example satisfies both E.44 norms and the whole class-two '
        'tower, but fails these new equations with values(2,2), even after every higher '
        'digit changes. Every one of the432 source points remains nonempty, with the '
        'specified simultaneous E.41–E.43 and E.46 maps. The isolated eight-program replay '
        'passes in55.690s; all mathematical JSONs and every NPZ array agree, and the '
        'original31 program/output artifacts are unchanged. The failed pre-chart '
        'coefficientwise division attempt and the corrected scaled-log sentence are '
        'both preserved in the audit notes.\n')
    text = text.replace(anchor, paragraph + anchor)
    old = ('The full integral three-adic class-three tower and the full inner/free A6 '
           'source remain active calculations beyond E.44 and E.45 until their unfinished '
           'comparisons are certified.')
    assert text.count(old) == 1
    previous['former_frontier_sentence'] = old
    text = text.replace(old, 'E.47 below certifies the complete integral three-adic '
        'class-three tower. The full inner/free A6 source remains under investigation '
        'with its additional derived and solvable source layers retained.')
    old = next(line for line in text.splitlines() if line.startswith('2. **E.2--E.3:**'))
    previous['remaining_E_paragraph'] = old
    new = ('2. **E.2--E.3:** continue the finer quotient calculations on the entire '
        'CM-coordinate fibres. All24 fibres remain nonempty through E.47. The full '
        'integral class-three boundary calculation gives Z3^70 correction-image fibres '
        'and an exact finite3^25 image, with an explicit finite shadow excluded even '
        'after changing every higher class-two digit. The defined binary, full pro-p, '
        'SL2(F5) and five-point Hurwitz common families coexist through the displayed '
        'maps. The full inner/free A6 source has additional three-primary layers in '
        'its successive derived quotients; their actions and exact comparison with '
        'all old parameters remain active work. The prime-three five-strand symplectic '
        'test is also undergoing independent audit. Nonemptiness at every finite '
        'quotient, or a finite quotient excluding all twelve extra CM fibres, remains '
        'to be proved.')
    text = text.replace(old, new)
    saved.write_text(json.dumps(previous, indent=2) + '\n')
    program.write_text('\n'.join(lines) + '\n')
    mainpath.write_text(maintext)
    report.write_text(text)
    print(json.dumps({'integrated': ['D.38', 'E.47'],
                      'updated_task_rows': ['D.1', 'D.2', 'E.2', 'E.3'],
                      'preserved_passages': str(saved.relative_to(ROOT))}, indent=2))


if __name__ == '__main__':
    main()
