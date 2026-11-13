#!/usr/bin/env python3
"""Integrate audited D36/E44--E46 scope in the active task ledger.

This edits reporting metadata, not mathematical certificate inputs.
The exact preceding task rows are retained before replacement.
"""
from pathlib import Path
import ast,json

ROOT=Path(__file__).resolve().parent.parent
states={
'D.1': ('D.36','The actual geometric S3 action excludes dimension two. The complete A5 chief-step lifting theorem and the cyclic/two-group outer-image lifts are proved. An ordinary split A6^20 chief extension obstructs every nonidentity power of a specified order-five base automorphism after the full centralizer union. Its exact pro-five product comparison also retains an admitted component above the same five-group shadow. Realization or exclusion of the two-dimensional complement in the full source remains.'),
'D.2': ('D.36','The extra weight-nine vector, gamma line and complete finite pentagon comparison are verified. Elementary abelian and central obstructions, the complete A5 chief-step count, and the ordinary order-five A6^20 obstruction retain their actual source maps and every centralizer choice. The latter also retains an admitted component above the prescribed five-group shadow. A cofinal equivariant lift or exclusion of the extra gentle direction remains.'),
'E.2': ('E.44; E.45; E.46','All24 CM fibres survive every proved refinement through E46. The exponent-three class-three boundary test adds four congruences beyond the full three-adic class-two tower and excludes one specified full-tower point, while retaining all432 multiplier-one sources. The compatible boundary fibre is Z3^10 times F3^22. Both A6 kernel/outer tests and the five-point A96 Hurwitz test retain all864 finite points, with exact boundary gluing maps. Full profinite survival remains.'),
'E.3': ('E.44; E.45; E.46','All864 degree-six points pass the retained full pentagons, braid and twist relations. Both A6 kernel/outer tests and the five-point A96 Hurwitz quotient retain them through complete perfect-correction and common-quotient maps. The fifth-point rotation has the required conjugacy in A96 itself, and the actual common four-strand image is T23 times A96. Every compatible E42/E44 multiplier-one boundary family also survives the stated Hurwitz comparison. Compatibility through every finite quotient remains.')}

def main():
    path=ROOT/'code/assemble_register.py';lines=path.read_text().splitlines();prior=[];changed=[]
    for i,line in enumerate(lines):
        stripped=line.strip()
        if not stripped.startswith("('"):continue
        value=ast.literal_eval(stripped.rstrip(','))
        if value[0] not in states:continue
        prior.append(value);suffix,description=states[value[0]]
        refs=value[1].split('; ')
        refs.extend(r for r in suffix.split('; ') if r not in refs)
        updated=(value[0],'; '.join(refs),value[2],description)
        lines[i]=' '+repr(updated)+',';changed.append(value[0])
    assert sorted(changed)==sorted(states)
    saved=ROOT/'research/checkpoint06_prior_coverage_rows.json'
    assert not saved.exists()
    saved.write_text(json.dumps(prior,indent=2)+'\n')
    path.write_text('\n'.join(lines)+'\n')
    main=ROOT/'LM7_PUSH_paper.tex';text=main.read_text()
    old='This working manuscript is \\textbf{INCOMPLETE};'
    new=('An ordinary order-five peripheral shadow has no generating lift across a specified split '
         '$A_6^{20}$ chief extension, for any of its four nonidentity powers, with the admitted '
         'pro-five comparison retained. The exponent-three class-three boundary quotient imposes '
         'four new congruences on the complete three-adic class-two tower and excludes an explicit '
         'tower point, while retaining every CM fibre. The complete $A_6$ kernel and outer-coordinate '
         'tests retain all $864$ points. A five-point Hurwitz quotient has pure and full image '
         '$A_{96}$; its complete source and explicit exponent-ten boundary comparison retain '
         'all those points and the order-five rotation conjugacy. '
         'This working manuscript is \\textbf{INCOMPLETE};')
    assert text.count(old)==1
    main.write_text(text.replace(old,new))
    print(json.dumps({'task_rows_updated':changed,'new_included_statements':['D.36','E.44','E.45','E.46'],
                      'preceding_rows_preserved':str(saved.relative_to(ROOT))},indent=2))

if __name__=='__main__':main()
