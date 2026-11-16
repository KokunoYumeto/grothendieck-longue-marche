#!/usr/bin/env python3
"""Integrate the audited complete first-seed lattice and literal generators."""
from pathlib import Path
import datetime,json,subprocess
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
ident='A.165'
record={
 'answers':'A5; A9; A15; L10; L14; L20',
 'depends_on':'A.159 complete relative S-unit norm kernel; A.162 stable tame norm maps and wild/local tower; literal first-field prime generators; rank12 residue saturation of the final printed S-unit generators; exact order9 character; direct relative norms and integral coefficient tables',
 'uses_local_theorem':'no',
 'manuscript_passages':'cote149; scans56–58 and126–127; every first completed S-unit seed and its actual finite/all-height local norm maps',
 'notes':'The first completed norm fibre over-2 is uniquely beta1 U^z h2^a h11^b h59^c for Z3^4. Its complete global S-unit K2 norm image is a=0,b=z,c=z modulo3. An S-unit preimage passes every local K3/K2 norm test exactly for a=0,b=z+3,c=4z+6 modulo9, giving nine residue classes. The all-height compatible local locus strengthens the first condition to a=0 in Z3. Exact primitive norm direction eta is defined in the completion and has Norm eta=U h11 h59, with stable characters(0,2). Three literal integral principal generators, the four A159 units, and five other specified S-units have a directly evaluated rank12 residue matrix. All27 new integer coefficients are printed in558 two-block rows and reconstructed independently by root, with exact relative and rational norms. No global K3 S-unit preimage or infinite global family is asserted.'
}
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
anchor=r'\input{sections/harmonic_jacobian_boundary_torsion.tex}'
new=r'\input{sections/two_inert_complete_seed_lattice.tex}'
assert anchor in s
if new not in s:s=s.replace(anchor,anchor+'\n'+new,1)
p.write_text(s)
p=w/'notes/register_metadata.json';meta=json.loads(p.read_text());meta[ident]=record
p.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')
detail='A.165 determines the entire first completed S-unit norm fibre and its exact K2 norm image. Nine modulo9 first-seed classes admit a preimage passing every next local norm test; compatibility at all higher local levels additionally forces the h2 exponent to be exactly0 in Z3. Global K3 S-unit solvability remains open.'
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines();assert lines[0]=='INCOMPLETE'
for i,line in enumerate(lines[:55]):
 if not line.startswith('| '):continue
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)==3 and cells[0] in {x.strip() for x in record['answers'].split(';')}:
  if ident not in cells[1]:cells[1]+=', '+ident
  if detail not in cells[2]:cells[2]+=' '+detail
  lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: every first seed and the exact next local tests'
if heading not in lines:
 lines.extend(['',heading,'',stamp+': '+detail,'',
  'The first field has class number1 and its completed unit group has the certified generator U. Literal principal generators give the complete four-parameter first norm fibre. In the second field, the final printed four units and eight S-units are evaluated directly at twelve residue maps; the resulting matrix has rank12 modulo3. The three newly printed principal elements have norms-121,-649,-3481 and their exact prime divisors. An independent root program reads their558 coefficient-block rows first, reconstructs all27 integer coordinates, and verifies each relative and rational norm without a computer-algebra norm routine.',
  'The primitive completed norm direction eta has norm U*h11*h59. A ninth-power detector identifies the required unit correction and its stable local characters(0,2). The actual preimage formula then gives the nine congruence classes. The A159 relative norm-one S-unit kernel has zero repair characters at11 and59, so these tests hold across each entire first fibre. At2 the P6 valuation cannot be changed within that fibre. Its successive unramified norm divisibility gives the exact all-height condition a=0. This result controls every first seed with the stated fixed support and retains the completed/local/global scopes explicitly.',
  'The next undecided computation is the balanced degree27 class or an exact global S-unit norm preimage. The unrestricted completed infinite fibre has the same fixed-support obstruction by A166. Both principal A1 assertions remain open.', ''])
p.write_text('\n'.join(lines)+'\n')
audit=stamp+' A165 integrated after root complete-source audit, root reruns of the first-image/short-principal/direct-saturation certificates, and independent Legendre/birational audits. Root reconstructed all558 printed rows and27 coefficients directly, checked integral coordinates and exact relative/rational norms. The first tame equations now show the literal2z-2b and2z-2c characters. The K3 local congruence a=0 mod9 and all-height condition a=0 inZ3 are kept separate. A166 also received a complete saved-source audit and certificate rerun from local.\n'
for name in ['notes/hour12_root_audits.md','notes/root_progress.md']:
 with(w/name).open('a')as f:f.write('\n'+audit)
proc=subprocess.run(['python',str(w/'code/build_register.py')],capture_output=True,text=True,check=True)
out='Integrated audited A165 and its complete literal coefficient supplement.\n'+proc.stdout
Path(__file__).with_name('integrate_a165_output.txt').write_text(out);print(out,end='')
