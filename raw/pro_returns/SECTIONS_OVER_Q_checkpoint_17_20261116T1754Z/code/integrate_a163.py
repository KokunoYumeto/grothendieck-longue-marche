#!/usr/bin/env python3
"""Integrate the audited all-coefficient proper-abelian classification."""
from pathlib import Path
import datetime,json,subprocess
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
ident='A.163'
record={
 'answers':'A5; A10; A15; L7; L10; L14',
 'depends_on':'A.143 exact rank-two descent; A.150 three quotient maps; A.154 two-primary Prym Sha; A.157 actual finite-cover quotient; A.160 full Prym Sha and finite boundary centres; Stoll Proposition3.6 and Theorem6.4; continuous Kummer comparison; rational V4 divisor push/pull isogenies',
 'uses_local_theorem':'no; sections of the specified quotient must locally match actual point or cusp sections',
 'manuscript_passages':'cote149; scans54–58 and126–127; actual global cusp image in a specified arithmetic quotient',
 'notes':'The chosen fixed sheet identifies E_D/Nall with TJ_D semidirect G_Q via the proper Abel–Jacobi map with origin P0. The section gives a full inverse Selmer class whose finite local values lie in the four rational boundary images. Stoll Proposition3.6 forces one global boundary Kummer class without a Sha hypothesis for J_D. Continuous-cohomology injectivity gives geometric conjugacy to an actual cusp image in E_U/Nall. No four-image distinctness after larger downstairs conjugacy is asserted. The old elliptic factor has full Sel2 order16 and zero two-primary Sha by an exact Selmer-kernel argument. Literal rational V4 push/pull maps have both compositions [2], proving rank J_D(Q)=2 and a finite two-primary Sha group killed by4. No odd-primary Sha assertion for this rank-two Jacobian is used.'
}
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
anchor=r'\input{sections/two_inert_changed_seed_repair_agent.tex}'
new=r'\input{sections/harmonic_proper_abelian_classification.tex}'
assert anchor in s
if new not in s:s=s.replace(anchor,anchor+'\n'+new,1)
p.write_text(s)
p=w/'notes/register_metadata.json';meta=json.loads(p.read_text());meta[ident]=record
p.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_references.bib';s=p.read_text()
old='Corollaries 6.2, 6.3 and 8.8, Theorem 8.2, Proposition 8.5, and Theorem 8.6 checked with the 2017 errata.'
new='Propositions 3.6 and 3.7, Theorem 6.4 with its geometric-cover comparison, Corollaries 6.2, 6.3 and 8.8, Theorem 8.2, Proposition 8.5, and Theorem 8.6 checked with the 2017 errata. Proposition 3.6 has no Tate--Shafarevich finiteness hypothesis.'
if old in s:s=s.replace(old,new,1)
else:assert new in s
p.write_text(s)
detail='A.163 proves that every locally matching section of the specified all-coefficient proper-abelian cover quotient in the combined mod8 class is globally a rational cusp image. The actual Jacobian comparison and Stoll finite support determine one boundary class; separate exact arithmetic gives rank2 and finite two-primary Sha killed by4 for the genus-three Jacobian.'
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines();assert lines[0]=='INCOMPLETE'
for i,line in enumerate(lines[:55]):
 if not line.startswith('| '):continue
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)==3 and cells[0] in {x.strip() for x in record['answers'].split(';')}:
  if ident not in cells[1]:cells[1]+=', '+ident
  if detail not in cells[2]:cells[2]+=' '+detail
  lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: a single global boundary class in the all-coefficient quotient'
if heading not in lines:
 lines.extend(['',heading,'',stamp+': '+detail,'',
  'The proof uses the actual proper geometric-abelian extension of D and the closed geometric commutator quotient. Abel–Jacobi identifies it with the full Tate-module extension of its Jacobian. The finite local centres lie in the four rational boundary points by A160, so Stoll Proposition3.6 identifies the full inverse Selmer class with one boundary point. Compatible finite zero-cochains lift that equality to continuous cohomology and hence to geometric conjugacy of sections. A rational tangential section supplies the actual cusp image downstairs. The result retains the locally matching quotient premise and does not construct a full lift of an arbitrary quotient section.',
  'The separate arithmetic assertion proves the old elliptic two-Selmer group has order16 and zero two-primary Sha. Its local Selmer-kernel argument uses the actual dual isogenies. The three quotient involutions of D give rational divisor pushforward and pullback maps between the Jacobian and E times the Prym Weil restriction; both composites are multiplication by2. The resulting Jacobian has rational rank2 and finite two-primary Sha of exponent at most4. The all-coefficient finite-support classification does not require an odd-primary Sha claim for this Jacobian. Both principal A1 assertions remain open.', ''])
p.write_text('\n'.join(lines)+'\n')
note=stamp+' A163 integrated: root read the complete source and independently reran its exact certificate; birational full source audit passed. Primary Stoll3.6/3.7 and Theorem6.4, including the pullback-of-isogenies proof, were reopened. The closed commutator, actual rational V4 maps, local Selmer kernel and all-coefficient/full-quotient scopes are explicit.\n'
for name in ['notes/hour12_root_audits.md','notes/root_progress.md']:
 with(w/name).open('a')as f:f.write('\n'+note)
proc=subprocess.run(['python',str(w/'code/build_register.py')],capture_output=True,text=True,check=True)
out='Integrated audited A163.\n'+proc.stdout
Path(__file__).with_name('integrate_a163_output.txt').write_text(out);print(out,end='')
