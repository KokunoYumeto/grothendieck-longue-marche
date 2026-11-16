#!/usr/bin/env python3
"""Integrate the audited finite geometric obstruction and its exact quotient maps."""
from pathlib import Path
import datetime
import json
import re

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
new=r'\input{sections/completed_old_section_obstruction.tex}'
old=r'\input{sections/norm_split_generation_agent.tex}'
if new not in s:s=s.replace(old,old+'\n'+new)
p.write_text(s)

p=w/'notes/register_metadata.json';m=json.loads(p.read_text())
m['A.93']={
 'answers':'A5; A9; A12; A15; L10; L14; L20',
 'depends_on':'A.69; A.88; A.90; actual degree64 Kummer cover; Milne LEC Remark3.3(c), Theorems14.14,21.3,21.5; cross-cocycle inflation; global Brauer reciprocity',
 'notes':'The constructed four-puncture completed data admit no full Selmer section. The exact finite quotient has order2^135, is metabelian and has nilpotency class at most11; it excludes quotient sections with the specified modulo4 coordinates and ordinary local images, including the real point. The same obstruction applies to locally matching full metabelian and class11 sections. The third inertia coordinate is retained, so this particular quotient does not factor through the tripod. No failure of lifting an existing full tripod section is asserted.',
 'uses_local_theorem':'no; ordinary local images are stipulated for quotient sections, and the full-section assertion is in the Selmer range',
 'manuscript_passages':'cote149; scans54–58,79–85,120–130; exact completed-coordinate and puncture comparison maps'}
p.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')

p=w/'SECTIONS_OVER_Q_references.bib';s=p.read_text()
source=(w/'notes/local_agent_references.bib').read_text()
pattern=r'(?ms)^@misc\{AgentMilneLEC,.*?^\}'
entry=re.search(pattern,source).group(0)
entry=entry.replace('used in the geometric localization calculation.','used in the geometric localization calculation. Root also opened Proposition 14.12 and Theorem 14.14, which give directly the higher-cohomology vanishing and the group/etale comparison for smooth affine curves over algebraically closed fields.')
s=re.sub(pattern,lambda _:entry,s)
p.write_text(s)

p=w/'sections/completed_old_section_obstruction.tex';s=p.read_text()
needle='The two arithmetic Hochschild--Serre spectral\nsequences and this comparison give (A.93.7).'
replacement=('The geometric comparison is also stated directly in\n'
             '\\cite[Proposition 14.12 and Theorem 14.14]{AgentMilneLEC}.\n'
             +needle)
if replacement not in s:s=s.replace(needle,replacement)
p.write_text(s)

p=w/'SECTIONS_OVER_Q_report.md';s=p.read_text();lines=s.splitlines()
scope={
 'A5':' A.93 proves that the A.90 four-puncture completed tuple has no full Selmer section; its locally matching obstruction already occurs in a metabelian quotient of order2^135 and factors through nilpotency class11.',
 'A9':' A.93 detects that completed tuple in an explicit finite geometric quotient and excludes its realization by a full Selmer section on the old four-punctured line. It supplies no counterexample starting from an existing full tripod section.',
 'A12':' A.93 computes a finite fundamental-group obstruction to the constructed old tuple, with the exact comparison to the tripod retained.',
 'A15':' A.93 gives the literal cross-cocycle, finite inflation and local evaluation maps detecting the completed obstruction.',
 'L10':' A.93 detects the four-puncture example in an explicit metabelian quotient of class at most11. Its retained third inertia prevents this quotient from factoring through the tripod.',
 'L14':' A.93 realizes this Jacobian obstruction as a literal finite geometric quotient class on the degree64 cover subgroup.',
 'L20':' A.93 proves that this particular completed tuple has no full Selmer realization on the old four-punctured line; the assertion about lifting an existing full section remains open.'}
for i,line in enumerate(lines[:50]):
 for key,extra in scope.items():
  if line.startswith('| '+key+' |'):
   cols=line.split(' | ')
   if 'A.93' not in cols[1]:cols[1]+=', A.93'
   line=' | '.join(cols)
   if extra not in line:line=line[:-2]+extra+' |'
   lines[i]=line
s='\n'.join(lines)+'\n'
heading='## Finite geometric detection of the completed obstruction'
if heading not in s:
 s+='\n'+heading+'\n\n'+stamp+': A.93 constructs the actual quotient Π/K of the geometric group of the old four-punctured line, where H is the kernel of its three modulo4 Kummer characters and K is the closed subgroup H²[H,H]. Its order is2^135. The normalized Brauer class on the degree64 cover is represented by the literal cross-cocycle cη((h1,g1),(h2,g2))=η(g1)(g1h2), which descends to (H/K)⋊G_Q. The modulo4 coordinate condition lifts a section into that cover subgroup. The local fixed-sheet maps then turn its global pullback into the invariant sum1/2, a contradiction. Real ordinary and tangential pullbacks are checked using the class on the proper curve.\n\nThe quotient is metabelian and receives Π/Γ12 because its commutator is a module over F2[(Z/4)^3] with augmentation ideal satisfying I^10=0. Thus the obstruction is visible by nilpotency class11. This result excludes full Selmer sections with the A.90 coordinates and excludes locally matching quotient sections in the stated scope. The map from the old curve to the tripod kills the third puncture inertia, which Π/K retains. No tripod counterexample or main A1 classification follows. The affine-curve comparison was checked directly in Milne LEC Proposition14.12 and Theorem14.14, together with the finite-cover comparison, and all finite certificates and independent proof audits are retained.\n'
p.write_text(s)

audit=stamp+' root A93 review: checked exact cover subgroup and arithmetic action; Schreier rank129 and order2^135; characteristic K and metabelian projection; augmentation I^10 and Γ12; proper μ2 lift and affine group comparison; explicit continuous cross-cocycle, edge and inflation; global mod4 conjugation into cover; finite-place fixed sheets and real ordinary/tangential transfer; global reciprocity; exclusion of all finite cusp labels from completed coordinates; exact third-inertia obstruction to factorization through tripod. Root reopened Milne LEC source and read the named statements, including the direct Theorem14.14. All passed; no local theorem invoked.\n'
for q in ['notes/hour6_root_audits.md','notes/root_progress.md']:
 with (w/q).open('a') as f:f.write('\n'+audit)
out='A93 integrated with finite quotient, metabelian and class11 comparison maps; both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a93_output.txt').write_text(out)
print(out,end='')
