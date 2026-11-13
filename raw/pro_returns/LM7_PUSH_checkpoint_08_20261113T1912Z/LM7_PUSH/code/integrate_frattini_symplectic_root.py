#!/usr/bin/env python3
"""Integrate audited D39 and E49 with exact source-scope reporting."""
from pathlib import Path
import ast
import json

ROOT = Path(__file__).resolve().parent.parent


def main():
    a = json.loads((ROOT / 'code/audit_coprime_frattini_root.json').read_text())
    b = json.loads((ROOT / 'code/bc_symplectic_five_p3_audit.json').read_text())
    c = json.loads((ROOT / 'code/e_symplectic_five_allunits_root.json').read_text())
    assert a['all_passed'] and a['original_artifacts_unchanged']
    assert b['protected_originals_unchanged'] and b['all24_changed_quadruples_simultaneously_inner_conjugate']
    assert c['all96_periodic_delta_conjugators_verified'] and c['original_artifacts_unchanged']
    saved = ROOT / 'research/checkpoint06_frattini_symplectic_prior_passages.json'
    assert not saved.exists()
    previous = {}
    program = ROOT / 'code/assemble_register.py'
    lines = program.read_text().splitlines()
    for i, line in enumerate(lines):
        text = line.strip()
        if not text.startswith("('"):
            continue
        row = ast.literal_eval(text.rstrip(','))
        if row[0] == 'D.1':
            previous[row[0]] = row
            row = (row[0], row[1] + '; D.39', row[2],
                row[3] + (' Every generating lift at the first universal coprime elementary-p '
                'cover factors through an automorphism of that same cover; its complete '
                'fixed-conjugator fibre and ordinary centralizer union are parameterized and counted.'))
            lines[i] = ' ' + repr(row) + ','
        elif row[0] in ('E.2', 'E.3'):
            previous[row[0]] = row
            row = (row[0], row[1] + '; E.49', row[2],
                row[3] + (' The full five-strand Sp4(F3) test also retains all864 points. '
                'Its complete source factors through G6, its first B4 target is the actual '
                'E18 group, and three explicit simultaneous conjugators prove full B5 '
                'generation for every retained word.'))
            lines[i] = ' ' + repr(row) + ','
    assert set(previous) == {'D.1', 'E.2', 'E.3'}
    mainpath = ROOT / 'LM7_PUSH_paper.tex'
    maintext = mainpath.read_text()
    for old, new in [('D_weight5_constraints_agent', 'D_frattini_agent'),
                     ('E_integral_class_three_agent', 'E_symplectic_five_root')]:
        anchor = r'\InputIfFileExists{sections/' + old + '.tex}{}{}'
        assert maintext.count(anchor) == 1
        maintext = maintext.replace(anchor, anchor + '\n' +
                    r'\InputIfFileExists{sections/' + new + '.tex}{}{}')
    anchor = 'This working manuscript is \\textbf{INCOMPLETE};'
    assert maintext.count(anchor) == 1
    maintext = maintext.replace(anchor,
        'Every generating peripheral lift in a universal coprime Frattini cover is '
        'parameterized, with its full ordinary centralizer union. The five-strand '
        '$\\operatorname{Sp}_4(\\mathbb F_3)$ test retains every candidate through '
        'its actual $G_6$ source quotient. ' + anchor)
    report = ROOT / 'research/report_body.md'
    text = report.read_text()
    anchor = '\nE.44 constructs the exponent-three class-three boundary quotient'
    assert text.count(anchor) == 1
    paragraph = ('\nD.39 determines every generating peripheral lift in the universal '
        'coprime Frattini cover E=Fhat/(K^p[K,K]). The literal Cayley chains give '
        'its source, boundary module and an explicit splitting. Every fixed boundary '
        'map extends to an invertible semilinear module map; the norm identity supplies '
        'the actual kernel conjugators. Every generating source lift kills the same '
        'Frattini kernel and therefore is an automorphism of this fixed E. The entire '
        'fixed-conjugator fibre is M/M^D times Hom_D(C,B) times Aut_D(C); its count '
        'is p^(|D|-1)|Hom_D(C,B)||Aut_D(C)|. The complete ordinary union multiplies '
        'this by the product of the three centralizer-to-inertia indices. All28 '
        'matrix/group cases and the exhaustive small-group fibre counts pass independent '
        'replay in3.482s, with byte-identical JSONs and unchanged originals. Both root '
        'and geometry independently read the full proof. Thus all D.37 parameters '
        'have this entire nonempty first coprime-cover fibre.\n')
    text = text.replace(anchor, paragraph + anchor)
    anchor = '\n## Geometric and germ results'
    assert text.count(anchor) == 1
    paragraph = ('\nE.49 gives the complete five-strand symplectic test at three. '
        'The four literal chain transvections generate Sp4(F3), of order51840. '
        'An independent enumeration of all target matrices supplies word preimages '
        'and verifies the symplectic-basis count. All3840 induced source coordinates '
        'and104 compression intertwiners are reconstructed. The complete source has '
        'order46656, certified independently by81 N-elements and576 disjoint cosets '
        'with1152 closure edges; its actual map factors through G6. A complete1944-edge '
        'comparison proves that the B4 restriction is the actual E18 target of order648. '
        'All24 origins, all37 correction/basis words and the exact864-point source '
        'factorization are checked. The changed four-generator tuples are simultaneously '
        'conjugate by exactly three displayed matrices, with literal braid words, so '
        'each generates the full five-strand target. All pentagons, braid relations '
        'and full twists hold. The saved periodic conjugators extend to all unit '
        'exponents modulo ten through an exact exponent-three normalizer; the epsilon '
        'comparison uses lambda=1 modulo eight. This proves the whole stated range '
        'lambda=1 modulo72. The independent matrix/source audit takes2.915s and leaves '
        'all originals unchanged. Every later retained word has the same eight '
        'evaluations through G6, and the common B4 target is the graph of the actual '
        'E18 comparison. The prime-five symplectic source is a separate active '
        'calculation, with its new solvable layers retained.\n')
    text = text.replace(anchor, paragraph + anchor)
    old = ('The prime-three five-strand symplectic test is also undergoing independent audit.')
    assert text.count(old) == 1
    previous['former_symplectic_frontier'] = old
    text = text.replace(old, 'E.49 proves the full prime-three five-strand symplectic '
        'comparison; its prime-five source and common-quotient comparison are now active.')
    saved.write_text(json.dumps(previous, indent=2) + '\n')
    program.write_text('\n'.join(lines) + '\n')
    mainpath.write_text(maintext)
    report.write_text(text)
    print(json.dumps({'integrated': ['D.39', 'E.49'],
                      'preserved_passages': str(saved.relative_to(ROOT)),
                      'E48_status': 'Separate ongoing full A6 calculation; not integrated.'}, indent=2))


if __name__ == '__main__':
    main()
