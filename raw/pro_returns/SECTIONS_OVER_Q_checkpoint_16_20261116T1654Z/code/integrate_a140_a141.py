#!/usr/bin/env python3
"""Integrate the fully reviewed wild norm maps and proper detector."""
from pathlib import Path
import datetime,json,subprocess
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
anchor=r'\input{sections/harmonic_cyclic_finite_obstruction.tex}'
for entry in [r'\input{sections/wild_pure_tower_norm_agent.tex}',r'\input{sections/harmonic_proper_finite_obstruction.tex}']:
    assert anchor in s
    if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
    anchor=entry
p.write_text(s)
p=w/'SECTIONS_OVER_Q_references.bib';s=p.read_text()
if '@misc{LegLevrat2024,' not in s:
    fragment=(w/'notes/legendre_proper_detector.bib').read_text().replace('note = {Version','note = {Verified: Version').replace('Opened primary PDF and checked exact comparison statement.','Opened primary PDF on16November2026; root independently checked the exact natural comparison and its arithmetic Hochschild--Serre proof on PDF pages11--13.')
    s+='\n'+fragment
if 'III Theorem 3.5 reopened for A.140' not in s:
    s=s.replace('VIII1.4 reopened in the sixth hour for odd-power unit detection.','VIII1.4 reopened in the sixth hour for odd-power unit detection. III Theorem 3.5 reopened for A.140: the actual norm group of a non-Galois local extension equals that of its maximal abelian subextension; the root-stabilizer inclusion and Artin diagram were checked on printed pages108--109.')
p.write_text(s)
data={
'A.140':{
 'answers':'A5; A7; A8; A9; A12; A15; L9; L10; L14; L17; L20',
 'depends_on':'A.138 fixed-tower unit family; exact local holomorph and root stabilizer; Milne III Theorem3.5 with its actual Artin/norm diagram; compact norm fibres',
 'uses_local_theorem':'no; the proof uses local class field theory and exact pure-root field norms',
 'manuscript_passages':'cote149; scans56–58,126–127; actual norm-family compatibility under a changed radicand',
 'notes':'For every specified pure-three tower over a finite extension of Q3 without mu3 and with radicand valuation prime to3, all field and unit transition norms are surjective. The exact Galois closure has commutator equal to its translation subgroup and G-prime times the root stabilizer equals G. The Artin diagram gives a literal preimage in the non-Galois pure field. Compact fixed-valuation fibres give actual compatible local families, including completed targets. The application to a prime-to-three rational multiplier a-prime=aQ^(e3^n) retains the exact old-field embedding. This establishes the local map at3; a compatible global family remains unresolved. Full root/local saved-source audits and independent finite certificate reruns passed.'},
'A.141':{
 'answers':'A5; A7; A8; A9; A12; A15; L2; L9; L10; L14; L17; L20',
 'depends_on':'A.139 actual cyclic genus-three cover and all local sheets; proper K(pi,1) comparison; rational boundary point and Chern-class correction; explicit proper mod-two homology quotient',
 'uses_local_theorem':'no; the exclusion retains its specified ordinary finite local images and ordinary/cuspidal real image',
 'manuscript_passages':'cote149; scans56–58,126–127; finite/metabelian quotient detection of a completed tripod pair',
 'notes':'The same completed pair of A139 is detected by Qbar=(F2[tau]/tau^6) semidirect C8, of order512 and exact class6. A proper mu2 lift of the Brauer class is corrected by the rational boundary point Chern class to have zero geometric degree, without changing any point or proper-cusp evaluation. Its central extension therefore splits geometrically and descends through proper mod-two homology. The four explicit boundary words kill exactly an order8 subgroup of the order4096 detector. The resulting maps from Pi double-prime and the class6 quotient are literal. All local values remain1/2 at2 and0 elsewhere. This excludes locally matching sections; an arbitrary abstract metabelian lift having only the same two abelian coordinates is not asserted to be excluded. Full root/local source audits and independent certificate reruns passed.'}
}
p=w/'notes/register_metadata.json';meta=json.loads(p.read_text());meta.update(data);p.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
details={
'A.140':'A.140 proves surjective actual and completed local norm maps at3 throughout the specified changed pure-three tower, with compatible local families. Global compatibility remains open.',
'A.141':'A.141 detects the same completed pair through an explicit proper-curve quotient of order512 and exact class6, retaining the prescribed local images. Its proper cohomology correction and exact boundary quotient are proved.'}
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines()
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[z.strip() for z in line.strip().strip('|').split('|')]
    if len(cells)!=3:continue
    for key,record in data.items():
        if cells[0] not in {x.strip() for x in record['answers'].split(';')}:continue
        if key not in cells[1]:cells[1]+=', '+key
        if details[key] not in cells[2]:cells[2]+=' '+details[key]
    lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: exact wild norm maps and proper-curve detection'
if heading not in lines:
    lines.extend(['',heading,'',stamp+': '+details['A.140']+' '+details['A.141'],
    'The wild-place proof computes the actual root stabilizer in each local Galois closure. Its image is the whole abelianization, so local reciprocity and norm transitivity give every target as a norm from the indicated pure field. The radicand has valuation prime to three; this proves total ramification and preserves normalized valuations under every transition. Nonempty compact fixed-valuation fibres give a single compatible local family. The old-to-new radical identities specify exactly which local tower is being used.',
    'For the proper detector, a rational boundary point on the genus-three product-root cover supplies a degree-one Chern class. Subtracting its geometric parity from a proper mu2 lift leaves the Brauer class and every local point pullback unchanged, and makes the geometric central extension split. The exact central-extension argument then uses the six-dimensional proper mod-two homology. The affine boundary classes are the two alternating lamp sums and the eighth power of the cyclic generator. Killing them gives the512-element quotient, whose lower-central dimensions are5,4,3,2,1,0. Its combined mod-eight Kummer character survives. The actual local contradiction applies to sections with the specified local images; it does not classify arbitrary abstract metabelian lifts of the same two abelian coordinates.',
    'The full saved proofs have independent reviews. The root reran both exact certificates, reopened Milne’s norm limitation theorem, and checked Levrat’s natural proper comparison and Milne’s curve cohomology. Both A1 assertions remain open.',''])
p.write_text('\n'.join(lines)+'\n')
audit=stamp+' A140 and A141 full root/local audits PASS. A140: all valuation signs; exact Kummer degree and holomorph/root stabilizer; actual non-Galois norm/Artin diagram; unit norms, compact fibres and completed transitions; changed-radicand embedding. Root reran15 subgroup cases,358 commutator identities,252 valuation checks and616 exponent maps. A141: proper K(pi,1) map; rational Chern-class correction; exact central inflation through proper homology; every boundary word and arithmetic normality; exact quotient/class6; retained combined character and all ordinary/real-cusp pullbacks. Root reran4096 quotient images,12288 generator products and262144 character products. Primary sources were independently reopened and exact passages checked.\n'
for name in ['notes/hour10_root_audits.md','notes/root_progress.md']:
    with(w/name).open('a')as f:f.write('\n'+audit)
result=subprocess.run(['python',str(w/'code/build_register.py')],check=True,text=True,capture_output=True)
out='Integrated A140 and A141.\n'+result.stdout
Path(__file__).with_name('integrate_a140_a141_output.txt').write_text(out);print(out,end='')
