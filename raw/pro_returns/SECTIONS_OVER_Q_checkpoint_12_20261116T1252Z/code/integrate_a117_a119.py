#!/usr/bin/env python3
"""Integrate audited support approximation and the free-three graph obstruction."""
from pathlib import Path
import datetime
import json

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
source=p.read_text()
anchor=r'\input{sections/harmonic_eighth_dyadic.tex}'
one=r'\input{sections/norm_prior_field_approximation_agent.tex}'
two=r'\input{sections/norm_free_three_graph_obstruction_agent.tex}'
assert anchor in source
if one not in source:
    source=source.replace(anchor,anchor+'\n'+one)
anchor118=r'\input{sections/odd_quartic_subset_norm.tex}'
if two not in source:
    anchor=anchor118 if anchor118 in source else one
    source=source.replace(anchor,anchor+'\n'+two)
p.write_text(source)
p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta['A.117']={
 'answers':'A5; A9; A15; L10; L14; L20',
 'depends_on':'A.44; A.101; A.105; A.115; exact finite relative modules; Milne ADT I4.10(b),I4.15 and torus duality p66',
 'uses_local_theorem':'no',
 'manuscript_passages':'cote149; scans56–58,126–127; finite relative norm repair retaining the prior radical fields',
 'notes':'At every finite three-power precision, proves finite-group H1 restriction injectivity at3 for the actual prior simultaneous radical field, by the full local radical kernel and deeper-holomorph vanishing. Poitou–Tate gives arbitrary finite old local classes with3 left unspecified and new Kummer ramification only at primes splitting that field. Relative torus Sha vanishing makes all local torus prescriptions actual global lower-norm-one elements. The allowed local3 classes are an affine fibre; divisors and nonlinear graph conditions retain their separate exact maps.'
}
meta['A.119']={
 'answers':'A5; A9; A15; L10; L14; L20',
 'depends_on':'A.106; A.113; A.115; A.117; the diagonal boundary cocycle and the actual rank-two quotient; local/global Tate duality',
 'uses_local_theorem':'no',
 'manuscript_passages':'cote149; scans56–58,126–127; obstruction to the stronger global graph repair prescription',
 'notes':'Explicit degree9 relative norm-one local data at q321193 are globally realizable with new Kummer ramification splitting the full prior field and3 left unspecified. Nevertheless no global class with these data has scalar-shifted graph values at every new ramified prime. The global pairing with the boundary class iκ(−2) forces the rank-two quadratic value at3 to zero; a second reciprocity sum contradicts the single prescribed nonzero value. This is a counterexample to unrestricted local plans, with no assertion that the actual canonical chain has that discrepancy.'
}
p.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md'
report=p.read_text()
detail=('A.117 proves actual relative norm-one approximation with new Kummer ramification restricted '
        'to primes splitting all specified prior fields, while leaving3 unspecified. A.119 proves that '
        'its affine restriction at3 can obstruct every scalar-shifted graph repair for explicitly '
        'realizable degree9 local data; the actual chain discrepancy remains to be treated.')
lines=report.splitlines()
for index,line in enumerate(lines[:55]):
    if not any(line.startswith('| '+item+' |') for item in ['A5','A9','A15','L10','L14','L20']):
        continue
    parts=line.split(' | ')
    for label in ['A.117','A.119']:
        if label not in parts[1]:
            parts[1]+=', '+label
    line=' | '.join(parts)
    if detail not in line:
        line=line[:-2]+' '+detail+' |'
    lines[index]=line
report='\n'.join(lines)+'\n'
heading='## Prior-field approximation and the actual restriction at three'
if heading not in report:
    report+='\n'+heading+'\n\n'+stamp+': A.117 proves the exact constrained-support finite approximation theorem for both relative torsion modules and their Cartier duals at every three-power precision. The proof computes the deeper holomorph cohomology, proves that the entire prior three-primary radical kernel occurs in the decomposition group at3, and uses the resulting restriction injection in the explicit Poitou–Tate annihilator. The relative S3 full-decomposition argument proves the required torus Hasse norm principle, so the resulting class is represented by an actual global relative norm-one element. Only finite Kummer ramification, rather than an unexamined integral divisor, is controlled.\n\nA.119 identifies a genuine constraint on the previously free coefficient place. In the degree9 relative module, the boundary cocycle iκ(−2) maps through the actual rank-two quotient. Its local image at3 is a nonzero isotropic line whose orthogonal is itself. Global reciprocity with that boundary cocycle forces every allowed correction into that orthogonal, and hence forces its lowest quadratic value at3 to vanish. At q=321193 the explicit vectors t=Z³ and c=Z⁴ have that quadratic value nonzero; every scalar-shifted graph at the other newly ramified split primes has value zero. A second reciprocity sum proves nonexistence of the requested graph repair. A.117 nevertheless realizes the finite old prescription by an actual relative norm-one element. Thus A.115 remains an onto statement on the full local cohomology space, while A.119 computes the obstruction on the smaller affine fibre imposed by the prior splitting conditions. The current next step uses the actual chain discrepancy and its available local choices, rather than an unrestricted local repair theorem.\n'
p.write_text(report)
audits=[
 'A117 complete root and local_preprint audit passed: all-precision relative modules and both involution signs, full local prior radical kernel, actual finite-group restriction, exact Poitou–Tate annihilator and stabilization, relative S3 Sha comparison and actual torus Kummer lifting. Root reopened Milne I4.10(b),I4.15 and the torus-duality paragraph on printed p66. Root reran the retained certificate:26 exact finite cohomology cases,59040 quotient generator checks,120 norm-socle identities.',
 'A119 complete root and local_preprint audit passed: actual rank-two quotient and terminal-module isomorphism, diagonal boundary cocycle, exact Kummer connecting class, nonzero isotropic local line, both global reciprocity pairings, scalar-shift radical, actual finite norm-one realization and literal prior-field inclusions. Wording identifies the cubic splitting field and the unramified procyclic H2 map. Root reran54 arithmetic maps,6561 scalar-shift graphs,48 isotropic-plane checks and all displayed splitting/unit data.'
]
for name in ['notes/hour8_root_audits.md','notes/root_progress.md']:
    p=w/name
    text=p.read_text() if p.exists() else ''
    for audit in audits:
        if audit not in text:
            text+='\n'+stamp+' '+audit+'\n'
    p.write_text(text)
output='Integrated A117 and A119: constrained-support actual relative approximation and the explicit scalar-shifted graph obstruction with3 left unspecified. Both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a117_a119_output.txt').write_text(output)
print(output,end='')
