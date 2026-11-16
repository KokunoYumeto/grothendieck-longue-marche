#!/usr/bin/env python3
"""Integrate the audited relative pairing and simultaneous local-map theorem."""
from pathlib import Path
import datetime
import json
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
source=p.read_text()
anchor=r'\input{sections/harmonic_local_initialization.tex}'
entry=r'\input{sections/relative_norm_forms_agent.tex}'
assert anchor in source
if entry not in source:source=source.replace(anchor,anchor+'\n'+entry)
p.write_text(source)
p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta['A.113']={
 'answers':'A5; A9; A15; L10; L14; L20',
 'depends_on':'A.105; A.109–A.110; exact block norm module; Milne ADT I2.3,I2.8',
 'uses_local_theorem':'no',
 'manuscript_passages':'cote149; scans56–58,126–127; relative norm repair preserving the preceding level',
 'notes':'For degrees9 and27 computes every equivariant alternating form on the actual relative norm-one three-torsion module, with bases, ranks and radicals. Proves the simultaneous local quadratic map at3 is onto on actual relative norm-one elements. The triangular correction retains all cross terms and uses exact subquotient H1 maps. No extrapolation to higher degrees or global cyclic repair is asserted.'
}
p.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md'
report=p.read_text()
lines=report.splitlines()
for i,line in enumerate(lines[:55]):
    for item in ['A5','A9','A15','L10','L14','L20']:
        if line.startswith('| '+item+' |'):
            parts=line.split(' | ')
            if 'A.113' not in parts[1]:parts[1]+=', A.113'
            line=' | '.join(parts)
            detail='At relative degrees9 and27, all equivariant alternating forms are computed and their quadratic values can be prescribed simultaneously by actual local relative norm-one elements at3.'
            if detail not in line:line=line[:-2]+' '+detail+' |'
            lines[i]=line
report='\n'.join(lines)+'\n'
heading='## Simultaneous relative correction at three'
if heading not in report:
    report+='\n'+heading+'\n\n'+stamp+': A.113 computes the entire spaces Hom_G(wedge²M_rel,mu3) for degrees9 and27: their dimensions are2 and3, with the explicit operator bases1,z² and1,z6,z8. Their projective ranks are6 with multiplicity3 and2 with multiplicity1, and18 with multiplicity9,6 with multiplicity3 and2 with multiplicity1. The proof uses the actual block norm map and translation centralizer, including the exact action z↦z+z². The nested radical correction computes each restricted radical, proves the required H2 vanishings, and completes the square to retain every mixed term. It proves simultaneous surjectivity of the local Brauer-value map on actual relative norm-one elements at3. This settles the displayed finite-depth local compatibility calculation; constructing a global multiplier with the required auxiliary ramification remains unresolved.\n'
p.write_text(report)
audit=stamp+' root A113 audit: checked the geometric block norm and twisted module, determinant form and all translation/unit actions, complete polynomial centralizer and inversion subring, both finite coefficient systems, exact ranks and radicals, submodule H2 and quotient H0 vanishings, every restricted radical, the linear section and cross-term completion of squares, and the actual local relative norm-one Kummer surjection. Independently audited by local_preprint. All finite certificates have actual retained outputs.\n'
for name in ['notes/hour7_root_audits.md','notes/root_progress.md']:
    with(w/name).open('a')as out:out.write('\n'+audit)
output='Integrated A113: complete relative pairing spaces and simultaneous local-three map at degrees9 and27. Global norm-chain repair and both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a113_output.txt').write_text(output)
print(output,end='')
