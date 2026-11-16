#!/usr/bin/env python3
"""Integrate the audited every-depth relative quadratic theorem."""
from pathlib import Path
import datetime
import json

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
source=p.read_text()
anchor=r'\input{sections/cubic_belyi_fibre.tex}'
entry=r'\input{sections/relative_norm_forms_all_depths.tex}'
assert anchor in source
if entry not in source:
    p.write_text(source.replace(anchor,anchor+'\n'+entry))
p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta['A.115']={
    'answers':'A5; A9; A15; L10; L14; L20',
    'depends_on':'A.105; A.113; exact unit-orbit and duality maps; Milne ADT I Corollary2.3 and Theorem2.8',
    'uses_local_theorem':'no; continuous local finite-module cohomology and actual relative torus norm',
    'manuscript_passages':'cote149; scans56–58,126–127; relative norm repair in the lifting attempt',
    'notes':'For every relative depth n, computes all equivariant alternating forms on the actual three-torsion module, with dimension n, basis, ranks, radicals and projective rank counts. The proof identifies invariant endomorphisms with the dual of the literal block-norm module and computes its unit-group coinvariants by valuation orbits. Simultaneous local quadratic values are onto on actual relative norm-one elements at3, with all mixed terms retained. The global auxiliary-ramification construction remains open.'
}
p.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md'
report=p.read_text()
lines=report.splitlines()
detail=('A.115 extends the relative calculation to every depth: all n independent quadratic '
        'values at degree3^n can be prescribed simultaneously by an actual relative norm-one element at3.')
for i,line in enumerate(lines[:55]):
    for item in ['A5','A9','A15','L10','L14','L20']:
        if line.startswith('| '+item+' |'):
            parts=line.split(' | ')
            if 'A.115' not in parts[1]:
                parts[1]+=', A.115'
            line=' | '.join(parts)
            if detail not in line:
                line=line[:-2]+' '+detail+' |'
            lines[i]=line
report='\n'.join(lines)+'\n'
heading='## Relative quadratic compatibility at every depth'
if heading not in report:
    report+='\n'+heading+'\n\n'+stamp+': A.115 removes the depth restriction from A.113. For N=3^n and d=N/3, the dual of the translation centralizer A/(Z^(2d)) is the actual kernel of the block norm A→F3[C_d]. Its unit-group coinvariants split into n literal valuation-orbit kernels, each of dimension one. This proves that the explicit n operators z^(d−3^j) are every equivariant alternating form, with ranks2·3^j and projective multiplicities3^j. The nested radical correction and local Tate duality prescribe their values simultaneously at3 at every depth. The proof keeps the complete cup-product cross term at each step, and the relative local norm identifies the cohomology source with actual torus points. Exact finite certificates check polynomial spaces through n=7 and all literal module maps, forms, radicals and projective ranks through n=4. The global multiplier with constrained new ramification remains unconstructed.\n'
p.write_text(report)
audit=('A.115 root proof and audit: exact relative norm module; full local splitting group; '
       'block determinant and centralizer-to-form isomorphism; coefficient-pairing duality; '
       'all valuation-orbit kernels and coinvariants; explicit invariant basis, ranks and radicals; '
       'all local H0/H2 maps; the full finite triangular induction including mixed terms; '
       'actual local relative torus Kummer isomorphism. Birational agent independently audited '
       'the general orbit proof and local induction. Exact certificates were executed and passed.')
for name in ['notes/hour8_root_audits.md','notes/root_progress.md']:
    p=w/name
    old=p.read_text() if p.exists() else ''
    if audit not in old:
        p.write_text(old+'\n'+stamp+' '+audit+'\n')
output=('Integrated A115: all relative alternating forms and simultaneous local-three values '
        'at every depth. The global repair step and both A1 assertions remain open.\n')
Path(__file__).with_name('integrate_a115_output.txt').write_text(output)
print(output,end='')
