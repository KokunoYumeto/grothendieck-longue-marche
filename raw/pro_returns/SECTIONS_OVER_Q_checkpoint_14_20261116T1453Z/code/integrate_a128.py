#!/usr/bin/env python3
"""Integrate the audited arbitrary-twist local constancy and global obstruction."""
from pathlib import Path
import datetime,json,subprocess

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
s=p.read_text()
anchor=r'\input{sections/harmonic_all_exponents_initialization.tex}'
entry=r'\input{sections/arbitrary_twist_local_constancy.tex}'
assert anchor in s
if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
p.write_text(s)
p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta['A.128']={
 'answers':'A8; A9; A12; A15; L14; L17; L20',
 'depends_on':'A.85; A.96; A.111; A.118; A.120; A.126; A.127; CT–Skorobogatov Corollary3.7.3, Proposition9.5.2 and Proposition12.3.1(iii); exact signed cyclotomic reciprocity',
 'uses_local_theorem':'no; explicit Kummer covers, local points and Brauer evaluations',
 'manuscript_passages':'cote149; scans56–58,126–127; rational puncture initialization on the harmonic and cubic Belyi source',
 'notes':'Proves local constancy for every common boundary character at every exponent divisible by four: all odd places and the real place for arbitrary finite puncture sets, and the dyadic place for both exact harmonic and cubic source sets with arbitrary coefficients. Gives proper Brauer classes, their canonical global evaluation element in Gal(B_N/K), and the exact equivalence with finite all-place initialization. Any rational point of the proper old curve forces the element to be trivial. Explicit coefficient, affine, inverse-root and exponent maps yield compatible obstruction restrictions for completed old tuples; no sufficiency for completed new coefficients is asserted. Root and local_preprint audits passed; root independently reran the exact certificate.'
}
p.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
p=w/'SECTIONS_OVER_Q_report.md'
lines=p.read_text().splitlines()
items={'A8','A9','A12','A15','L14','L17','L20'}
detail=('A.128 proves arbitrary-twist local constancy at every exponent divisible by four on the harmonic and cubic sources, and at all odd/real places for arbitrary finite punctures. Its actual proper Brauer classes define the complete finite global initialization obstruction, with compatible restriction maps for completed old tuples. A rational point of the proper old curve makes that sum zero; the arbitrary-twist sum and compatible new coefficients remain open.')
changed=0
for i,line in enumerate(lines[:55]):
 if not line.startswith('| '):continue
 cells=[z.strip() for z in line.strip().strip('|').split('|')]
 if len(cells)!=3 or cells[0] not in items:continue
 if 'A.128' not in cells[1]:cells[1]+=', A.128'
 if detail not in cells[2]:cells[2]+=' '+detail
 lines[i]='| '+' | '.join(cells)+' |'
 changed+=1
heading='## Arbitrary twists and the actual global puncture obstruction'
if heading not in lines:
 lines.extend(['',heading,'',stamp+': '+detail,
 'The local square correction preserves every original global relation character. The odd-place proof treats arbitrary reduction and every dyadic exponent by residue characters and exact cancellation of the higher cyclotomic term. The dyadic proof transports all characters through actual affine and inverse-root maps, and its remaining mixed relation has an even distinguished weight. Residues at the new fibre vanish in each actual factor, and the order bound kills the pole residue at infinity. The resulting proper Brauer classes have constant local evaluations and a finite global sum. The individual square-root characters are global constant algebras, so the obstruction lies in Gal(B_N/K). Exact exponent maps give compatible restriction identities. Finite-place solubility also forces a valid real sign interval by a displayed rational quaternion reciprocity argument.',''])
p.write_text('\n'.join(lines)+'\n')
audit=('A128 full saved-source audits passed root and local_preprint. Root checked every odd residue case, local square corrections, actual affine/inverse-root and coefficient maps, the dyadic induction, residue extension to the proper curve, finite-support global pairing, kernel Gal(B_N/K), exponent restrictions and the real-sign reciprocity. Root reopened CT–Skorobogatov Cor3.7.3, Prop9.5.2 including its real remark, and Prop12.3.1(iii). Root reran the certificate:91 symbolic identities;9484 odd equations,282786 literal radicand computations,606450 finite states,40408 mixed-character values and3006 Frobenius-order checks;312 dyadic depth cases,1632 sign implications,12 power images and8 signed norm kernels. All passed. The proper-rational-point corollary was added with its actual evaluation map.')
for name in ['notes/hour9_root_audits.md','notes/root_progress.md']:
 p=w/name
 s=p.read_text() if p.exists() else '# Ninth-hour root audits\n'
 if audit not in s:p.write_text(s+'\n'+stamp+' '+audit+'\n')
result=subprocess.run(['python',str(w/'code/build_register.py')],check=True,text=True,capture_output=True)
out=f'Integrated A128 in numerical order; updated {changed} outcome rows.\n'+result.stdout+'Both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a128_output.txt').write_text(out)
print(out,end='')
