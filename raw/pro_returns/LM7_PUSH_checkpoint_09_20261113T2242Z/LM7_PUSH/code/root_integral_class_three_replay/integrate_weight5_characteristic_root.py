#!/usr/bin/env python3
"""Integrate the independently audited D37 target and E46 common map."""
from pathlib import Path
import ast
import json

ROOT = Path(__file__).resolve().parent.parent


def main():
    audit = json.loads((ROOT / 'code/audit_weight5_characteristic_root.json').read_text())
    assert audit['all_passed'] and audit['entire_JSON_byte_identical']
    saved = ROOT / 'research/checkpoint06_weight5_prior_passages.json'
    assert not saved.exists()
    old = {}
    source = ROOT / 'code/assemble_register.py'
    lines = source.read_text().splitlines()
    for i, line in enumerate(lines):
        text = line.strip()
        if not text.startswith("('"):
            continue
        row = ast.literal_eval(text.rstrip(','))
        if row[0] == 'D.1':
            old['D.1'] = row
            row = (row[0], row[1] + '; D.37', row[2],
                   'The actual geometric S3 action excludes dimension two. The complete chief-step lifting and obstruction comparisons are retained. Fully invariant finite five-group targets P_n of order 5^(17n+2) now carry all three compatible ordinary special outer parameters, with the exact S3 action and inner powers accounted for. Their kernels are proved fully invariant by Fox substitution. Realization or exclusion of the two-dimensional complement through every finer full finite source remains.')
            lines[i] = ' ' + repr(row) + ','
        elif row[0] == 'E.3':
            old['E.3'] = row
            row = (row[0], row[1], row[2],
                   'All864 degree-six points pass the retained full pentagons, braid and twist relations. The A6 kernel/outer tests and five-point A96 Hurwitz test retain them through exact correction and common-quotient maps. The actual SL2(F5) source maps onto the Hurwitz source, so the same corrected word retains both with every E42/E44 boundary family. The full common four-strand target is (T23 times over S_L T_L) times A96. Compatibility through every finite quotient remains.')
            lines[i] = ' ' + repr(row) + ','
    assert set(old) == {'D.1', 'E.3'}
    mainpath = ROOT / 'LM7_PUSH_paper.tex'
    maintext = mainpath.read_text()
    anchor = r'\InputIfFileExists{sections/D_order5_agent.tex}{}{}'
    assert maintext.count(anchor) == 1
    maintext = maintext.replace(anchor, anchor + '\n' +
                               r'\InputIfFileExists{sections/D_weight5_agent.tex}{}{}')
    anchor = 'This working manuscript is \\textbf{INCOMPLETE};'
    assert maintext.count(anchor) == 1
    maintext = maintext.replace(anchor,
        'Explicit fully invariant finite five-group targets carry all three compatible '
        'ordinary weight-five special parameters, including their exact geometric symmetry. ' + anchor)
    report = ROOT / 'research/report_body.md'
    text = report.read_text()
    anchor = '\nE.44 constructs the exponent-three class-three boundary quotient'
    assert text.count(anchor) == 1
    paragraph = ('\nD.37 constructs actual characteristic finite Magnus targets P_n of order '
        '5^(17n+2), metabelian of class six, with abelianization (Z/5^(n+1))^2, '
        'derived subgroup (Z/5^n)^15 and center (Z/5^n)^5. Its Fox substitution map '
        'proves full invariance of the quotient kernel at every precision. All three '
        'weight-five parameters give compatible multiplier-one special automorphisms. '
        'The actual centralizer of x is computed, including the inner powers x^(5^n t); '
        'this proves injectivity in the ordinary outer group. Both geometric generators '
        'have the exact symmetric-square action after the specified actual inner '
        'correction. At the first precision every nonzero parameter has order five. '
        'The independent replay takes2.049s and reproduces the entire JSON byte for byte '
        'at n=1,2, with the original artifacts unchanged. The all-precision proof was '
        'read independently twice. One codomain typo in the draft Fox identity was '
        'corrected before integration. The full finite-source lifting question remains.\n')
    text = text.replace(anchor, paragraph + anchor)
    oldphrase = ('The current route must account for every finite component above that shadow, '
                 'through an actual characteristic quotient, before this construction can bound '
                 'its rational leading direction.')
    newphrase = ('D.37 now supplies actual fully invariant characteristic targets P_n and the '
                 'complete three-parameter ordinary outer family. The current route must account '
                 'for every finite component above these specified shadows before it can bound '
                 'a rational leading direction.')
    assert text.count(oldphrase) == 1
    old['remaining_D_phrase'] = oldphrase
    text = text.replace(oldphrase, newphrase)
    saved.write_text(json.dumps(old, indent=2) + '\n')
    source.write_text('\n'.join(lines) + '\n')
    mainpath.write_text(maintext)
    report.write_text(text)
    print(json.dumps({'integrated': 'D.37', 'updated_task_rows': ['D.1', 'E.3'],
                      'prior_passages_saved': str(saved.relative_to(ROOT))}, indent=2))


if __name__ == '__main__':
    main()
