#!/usr/bin/env python3
"""Integrate the audited affine-cover classification and exact downstairs orbits."""
from pathlib import Path
import datetime,json,subprocess
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
ident='A.167'
record={
 'answers':'A5; A10; A15; L7; L10; L14',
 'depends_on':'A.76 full completed Kummer localization injection; A.157 literal degree8 cover and boundary words; A.160 full Prym Sha and finite boundary support; A.163 proper-abelian classification; A.164 boundary separation; actual toric module sequence and continuous cohomology; cyclotomic deck centralizer',
 'uses_local_theorem':'no; the exact domain is locally actual point/cusp-matching quotient sections',
 'manuscript_passages':'cote149; scans54–58 and126–127; exact packets and completed tangents in an actual all-coefficient metabelian quotient',
 'notes':'For H the degree8 geometric cover subgroup, the arithmetic normal kernel Kaff is its closed commutator. The quotient Pi/Kaff is literally Zhat[C8] semidirect Zhat with x=(e0,2),y=(0,1). The exact toric sequence has M=Zhat(1)^4/diagonal and proper quotient TJ. Vanishing local/global Tate invariants makes H1(M) inject into H1(Hab). A163 fixes a boundary point; the actual split quotient M/inertia(P)=Zhat(1)^2 and A76 completed Kummer injection force a unique global tangent class. Selected-cover classes are exactly four copies of completed Q×. Downstairs the only additional geometric conjugators have deck coordinate0 or4, by the actual cyclotomic centralizer. The rational deck involution fixes each boundary and sends its parameter to its negative. Thus the exact downstairs class set is four disjoint copies of completed Q×/{±1}. All four rational tangent constants are computed. The conclusion for a full metabelian section concerns its image in this quotient, with no full-source cuspidality claim.'
}
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
anchor=r'\input{sections/two_inert_infinite_support_identity.tex}'
new=r'\input{sections/harmonic_affine_abelian_classification.tex}'
assert anchor in s
assert 'A.167.17' in (w/'sections/harmonic_affine_abelian_classification.tex').read_text()
if new not in s:s=s.replace(anchor,anchor+'\n'+new,1)
p.write_text(s)
p=w/'notes/register_metadata.json';meta=json.loads(p.read_text());meta[ident]=record
p.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')
detail='A.167 classifies the locally matching affine-cover abelian quotient in the specified combined mod8 class: a selected sheet has one of four boundary labels and one unique completed tangent. Under the actual full downstairs geometric conjugacy, the exact class set is four disjoint copies of completed Q×/{±1}. The map from the full metabelian quotient is explicit and its larger kernel remains outside this conclusion.'
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines();assert lines[0]=='INCOMPLETE'
for i,line in enumerate(lines[:55]):
 if not line.startswith('| '):continue
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)==3 and cells[0] in {x.strip() for x in record['answers'].split(';')}:
  if ident not in cells[1]:cells[1]+=', '+ident
  if detail not in cells[2]:cells[2]+=' '+detail
  lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: the full affine-cover tangent and downstairs conjugacy'
if heading not in lines:
 lines.extend(['',heading,'',stamp+': '+detail,'',
  'The geometric quotient is the actual semidirect product Zhat[C8] by Zhat, with the second factor shifting the eight lamp coordinates modulo8. The literal boundary words give a primitive toric submodule with one sum relation. Compactification and Abel–Jacobi give its exact quotient TJ. The finite rational/local torsion argument proves zero Tate invariants, so the lift of a proper boundary class to H1 of the toric module is unique. Its quotient by that boundary inertia is a split pair of full completed multiplicative Kummer modules. The global class is locally zero there at every finite prime, and A76 injectivity therefore puts it on the single global inertia line.',
  'The actual full cusp section is recovered from that completed tangent cocycle. The four downstairs tangent constants are8a,-8a,64a²,-a²/4 with the exact fourth/eighth powers and formal units checked. For geometric conjugacy downstairs, both selected-cover sections have the same finite arithmetic projection. The conjugator deck coordinate must therefore be fixed by the full cyclotomic action on C8, giving exactly0 and4. The nontrivial rational deck map is W to-W; it fixes each boundary and negates the chosen parameter. This proves the exact four disjoint tangent quotients and resolves the previously uncomputed larger deck-conjugacy relation for this affine quotient.',
  'The result retains the specified quotient, combined class and local-matching hypotheses. Both general A1 assertions, and the full metabelian source classification beyond this actual quotient map, remain open.', ''])
p.write_text('\n'.join(lines)+'\n')
audit=stamp+' A167 integrated after complete root, local and birational saved-source audits and independent certificate reruns. Root derived the extra downstairs centralizer comparison; Legendre and local independently verified it, and the final saved proof plus fixed-deck certificate were reread/rerun. The quotient map, primitive toric sequence, continuous Kummer domain, exact tangent constants and conjugacy scope are retained.\n'
for name in ['notes/hour12_root_audits.md','notes/root_progress.md']:
 with(w/name).open('a')as f:f.write('\n'+audit)
proc=subprocess.run(['python',str(w/'code/build_register.py')],capture_output=True,text=True,check=True)
out='Integrated audited A167, including the proved downstairs tangent orbits.\n'+proc.stdout
Path(__file__).with_name('integrate_a167_output.txt').write_text(out);print(out,end='')
