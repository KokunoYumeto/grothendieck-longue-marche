#!/usr/bin/env python3
"""Integrate the scalar norm restriction and the explicit tripod support image."""
from pathlib import Path
import datetime
import json
import subprocess

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
s=p.read_text()
anchor=r'\input{sections/harmonic_escaping_support.tex}'
assert anchor in s
for source in ['scalar_cyclotomic_precision_agent.tex','tripod_escaping_support.tex']:
    entry='\\input{sections/'+source+'}'
    if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
    anchor=entry
p.write_text(s)
p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta['A.135']={
 'answers':'A5; A9; A15; L10; L14; L20',
 'depends_on':'A.130 scalar construction; exact rational and completed field norms; three-adic unit power map',
 'uses_local_theorem':'no; explicit valuations, field norms and local multiplicative powers',
 'manuscript_passages':'cote149; scans56–58,126–127; simultaneous auxiliary-prime and local-three prescriptions',
 'notes':'The actual norm of a single-prime scalar class with exponent3^r and trivial localization above3 forces the distinguished split rational prime to be1mod3^(r+1). This identifies a constraint in the proved Schmidt–Wingberg building classes beyond the chosen splitting field. The several-prime version is an exact product condition; actual split primes61,67 cancel modulo9 while each has depth one. It asserts no global scalar class with those exact divisors. Root and local_preprint full audits passed; root reran all finite unit maps and2184 norm-exponent tests.'
}
meta['A.136']={
 'answers':'A5; A8; A9; A12; A15; L2; L9; L14; L17; L20',
 'depends_on':'A.80; A.83; A.85; A.107 actual harmonic cover; A.132; A.133 with both fibres2,−1 removed',
 'uses_local_theorem':'no; exact completed Kummer maps and finite Kummer covers',
 'manuscript_passages':'cote149; scans56–58,126–127; fixed ordinary tripod coordinates and a new rational puncture',
 'notes':'Maps the fully specified harmonic escaping-support construction to the actual tripod by t=4T(1−T), A=−4A0A1 and B=4Ah², with exact finite-cover coordinates(X0X1,Xh²). Both completed coordinates have infinite support, initial mod-four pair(3/4,1/4), and fixed real centre3/4. At new puncture−8 every finite common field is Q(sqrt−6) and every finite prescribed-point initialization succeeds, while the literal factorization t+8=−4(T−2)(T+1) gives valuation one at infinitely many forced primes, excluding a global new squareclass. No full section is inferred or excluded merely from that missing coordinate. Root full audit and exact certificate passed.'
}
p.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')

p=w/'SECTIONS_OVER_Q_report.md'
lines=p.read_text().splitlines()
details={
 'A.135': ('A.135 proves that the single-prime scalar repair classes with zero local data at3 force their prime to be1mod3^(r+1), even when the specified splitting field omits that layer; its actual several-prime norm condition permits the displayed61/67 cancellation.', {'A5','A9','A15','L10','L14','L20'}),
 'A.136': ('A.136 carries the escaping-support construction onto the tripod through t=4T(1−T): both ordinary completed coordinates have infinite support, all finite initialization tests at−8 vanish, and infinitely many valuations v_p(t_p+8)=1 exclude a new global squareclass.', {'A5','A8','A9','A12','A15','L2','L9','L14','L17','L20'})
}
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[z.strip() for z in line.strip().strip('|').split('|')]
    if len(cells)!=3:continue
    for identifier,(detail,items) in details.items():
        if cells[0] not in items:continue
        if identifier not in cells[1]:cells[1]+=', '+identifier
        if detail not in cells[2]:cells[2]+=' '+detail
    lines[i]='| '+' | '.join(cells)+' |'
heading='## The actual tripod image and the scalar cyclotomic restriction'
if heading not in lines:
    lines.extend(['',heading,'',stamp+': '+details['A.136'][0],
    'A133 was strengthened to exclude both points2 and−1, the complete fibre over−8. Its good-prime count removes two unramified fibres, and the unchanged bound was checked again. The actual finite-cover maps and their coefficient transitions prove the completed tripod identities. The new-boundary common field is exactly Q(sqrt−6), so all its characters are individual norm characters; the constant-algebra identity gives every finite initialization. The infinite forced valuation formula is retained explicitly. This establishes failure of fixed-centre puncture matching on an actual ordinary tripod pair, without drawing a fundamental-group conclusion from missing Kummer data alone.',
    details['A.135'][0]+' The proof uses the global norm valuation at every rational prime, the actual product of local norms above3, an explicit Bezout extraction of the distinguished prime and the exact three-adic unit power image. This constraint applies to the single-prime scalar building classes; its multi-prime comparison is stated only as the proved necessary norm condition.',''])
p.write_text('\n'.join(lines)+'\n')
audit=('A135 root and local_preprint full audits passed, with root independent execution of the retained unit-power and2184 norm-exponent certificate. A136 root audit passed the complete polynomial fibre map, finite-cover coordinate maps, coefficient transitions, both infinite supports, all-place ordinary avoidance, the exact new boundary common field and its individual norm identity. Root independently reran its19 symbolic identities,64 coefficient/common-field instances and10 forced-prime valuations. Root also reran the strengthened A133 certificate with both removed fibres and the revised bound b≤6D; all passed.')
for name in ['notes/hour9_root_audits.md','notes/root_progress.md']:
    p=w/name
    s=p.read_text() if p.exists() else '# Ninth-hour root audits\n'
    if audit not in s:p.write_text(s+'\n'+stamp+' '+audit+'\n')
result=subprocess.run(['python',str(w/'code/build_register.py')],check=True,text=True,capture_output=True)
out='Integrated A135 and A136; the numerical slot A134 remains reserved for the current explicit Brauer construction.\n'+result.stdout+'Both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a135_a136_output.txt').write_text(out)
print(out,end='')
