#!/usr/bin/env python3
"""Integrate the audited all-place harmonic quartic initialization result."""
from pathlib import Path
import datetime
import json

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
source=p.read_text()
anchor=r'\input{sections/norm_torus_cyclic_obstruction.tex}'
assert anchor in source
for filename in ['harmonic_dyadic_norm.tex','harmonic_local_initialization.tex']:
    entry='\\input{sections/'+filename+'}'
    if entry not in source: source=source.replace(anchor,anchor+'\n'+entry)
    anchor=entry
p.write_text(source)

p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta.update({
 'A.111':{
  'answers':'A9; A12; A15; L14; L20',
  'depends_on':'A.108; explicit harmonic D4 transformations; dyadic fourth powers and unramified quadratic norms',
  'uses_local_theorem':'no',
  'manuscript_passages':'cote149; scans56–58,126–127; prime2 in the harmonic puncture comparison',
  'notes':'Every harmonic negative-triple quaternion evaluates to zero at every ordinary dyadic point. The proof gives exact cover and symbol maps, all valuation cases, the quartic norm identity and the final unramified quadratic norm group. No vanishing of H1(Q2,J4) is inferred.'
 },
 'A.112':{
  'answers':'A9; A12; A15; L14; L20',
  'depends_on':'A.85; A.96; A.108; A.111; explicit odd-place torsion translations and norm maps',
  'uses_local_theorem':'no',
  'manuscript_passages':'cote149; scans56–58,126–127; full finite-character harmonic initialization',
  'notes':'Proves zero localized Jacobian class at every odd and real place and zero evaluation at every place. All quartic common characters then give an actual new rational coefficient preserving any finite prescribed old-point set. Gives a nonzero elliptic H1 class at3 killed by the exact injective Jacobian morphism. No infinite prescribed local tuple, higher-exponent initialization or global Brauer vanishing is asserted.'
 }
})
meta['A.108']['notes']+=' A.112 gives an explicit nonzero local source class killed by this cohomology map.'
meta['A.107']['notes']=meta['A.107']['notes'].replace('No obstructed harmonic arithmetic tuple has been found.','A.111–A.112 prove that the harmonic quartic joint characters have zero evaluation at every place; higher-exponent and full completed initialization remain under investigation.')
p.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')

p=w/'SECTIONS_OVER_Q_report.md'
report=p.read_text()
lines=report.splitlines()
for i,line in enumerate(lines[:55]):
    for item in ['A9','A12','A15','L14','L20']:
        if line.startswith('| '+item+' |'):
            parts=line.split(' | ')
            if 'A.111–A.112' not in parts[1]:parts[1]+=', A.111–A.112'
            detail='Every harmonic quartic common character has zero local evaluation, and one new coefficient can be initialized while preserving any finite set of old local points. Higher exponents and full compatible lifting remain open.'
            line=' | '.join(parts)
            if detail not in line:line=line[:-2]+' '+detail+' |'
            lines[i]=line
report='\n'.join(lines)+'\n'
heading='## Harmonic quartic initialization resolved'
if heading not in report:
    report+='\n'+heading+'\n\n'+stamp+': A.111 proves the unbounded dyadic evaluation theorem through explicit D4 coordinate maps, exact fourth-power discs, a quartic norm identity and the remaining unramified quadratic norm group. A.112 proves odd-place vanishing of the actual Jacobian class: good reduction gives surjective unramified elliptic norm, while odd valuation reduces every local point modulo twice the group to explicitly named rational two-torsion. Their Jacobian cocycles have the primitives in A.108. The real component calculation completes the local comparison. Thus every harmonic negative-triple character has zero evaluation at every place. The full common-character formula of A.96 and the sufficient direction of A.85 now construct a new rational quartic coefficient preserving any prescribed finite set of old local points. This closes the quartic character test for this harmonic cover; it supplies no compatible all-exponent or infinite prescribed-point extension.\n\nThe exact source example d138, R24/23, Q=(162,1080) has no Q3-point on its source norm quartic, proved by all valuation cases and the residue18 modulo27. Its nonzero elliptic H1 class maps to zero under the actual harmonic Jacobian pullback. The morphism of Jacobians is injective, with its kernel computed through the inertia-generated cover; the cohomology map has the displayed nonzero kernel. No vanishing of the global Brauer class, or of its H1 localization at2, is inferred. The new certificates retain14,018 dyadic symbol evaluations,4,278 odd-place translation cases,14 finite-field norm maps with2,464 points, and the complete modulo27 check.\n'
p.write_text(report)

audit=stamp+' root audits A111–A112: checked every exact D4 cover and quaternion map; dyadic disc reduction, all shallow and deep valuations, both root signs and unramified norm case; finite-field1+Frobenius norm and formal correction; all odd-valuation torsion translations including p3; real components; proper-curve evaluation continuation; all common quartic characters and actual A85 forgetful map; c=R case; and every valuation of the explicit nonsoluble source quartic. Both sources also independently audited by the other mathematical agent. Certificates are retained with actual outputs.\n'
for name in ['notes/hour7_root_audits.md','notes/root_progress.md']:
    with(w/name).open('a')as out:out.write('\n'+audit)
output='Integrated A111–A112: harmonic quartic finite initialization proved; both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a111_a112_output.txt').write_text(output)
print(output,end='')
