#!/usr/bin/env python3
"""Integrate the audited ordinary two-prime class and balanced-order comparisons."""
from pathlib import Path
import datetime,json,subprocess
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
record={
 'answers':'A5; A9; A15; L10; L14; L20',
 'depends_on':'A.155 precise balanced class quotient; A.156 principal level2 two-prime; A.165 complete seed congruences; A.166 actual/completed coherent support comparison; ideal extension and norm on literal degree-one branches',
 'uses_local_theorem':'no',
 'manuscript_passages':'cote149; scans56–58 and126–127; exact ordinary and balanced ideal-class obstruction maps',
 'notes':'The distinguished two-prime has nonzero ordinary three-primary ideal class at every level n>=3. A prime-to3 principal order would yield a completed generator with that single-prime divisor; its exact first seed has a=b=c=0, contradicting the two A165 congruences z=6 andz=3 modulo9. Actual ideal norms preserve the nonzero class at all higher levels. Thus no integral element of those fields has rational norm±2. Every completed K3 S-unit norm preimage of-2, and every coherent completed family, has stable changed-prime coordinates satisfying c59-4c11=3 modulo9. Extending the principal level2 prime gives the sharper balanced element bound3^(n-2)e_n=0. The quotient map is explicit; the nonzero ordinary class may map to zero in the balanced quotient, and e3 remains undecided. No finite coefficient precision bound is inferred from the element order.'
}
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
anchor=r'\input{sections/harmonic_affine_abelian_classification.tex}'
new=r'\input{sections/two_inert_raw_two_class_obstruction.tex}'
assert anchor in s
if new not in s:s=s.replace(anchor,anchor+'\n'+new,1)
p.write_text(s)
p=w/'notes/register_metadata.json';meta=json.loads(p.read_text());meta['A.168']=record
p.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')
detail='A.168 proves the distinguished two-prime has nonzero ordinary three-primary ideal class at every degree27 and higher level, and excludes integral norm±2 elements there. It gives the necessary valuation correction c59-4c11=3 modulo9 and improves the balanced element order bound to3^(n-2). The actual balanced quotient image e3 remains undecided.'
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines();assert lines[0]=='INCOMPLETE'
for i,line in enumerate(lines[:55]):
 if not line.startswith('| '):continue
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)==3 and cells[0] in {x.strip() for x in record['answers'].split(';')}:
  if 'A.168' not in cells[1]:cells[1]+=', A.168'
  if detail not in cells[2]:cells[2]+=' '+detail
  lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: the ordinary class is nonzero, with its balanced image still to determine'
if heading not in lines:
 lines.extend(['',heading,'',stamp+': '+detail,'',
  'The contradiction uses actual principal divisors and completed roots of prime-to3 exponents. The resulting first seed has only a unit correction; the complete local norm classification then gives two incompatible residues for that exponent. Ideal norm along the actual degree-one branch propagates the nonzero ordinary class. The stable changed-prime valuation relation follows by eliminating the unit exponent from the same two congruences. Finally, the principal level2 two-prime extends to a divisor whose residue-degree sum is3^(n-2), yielding the stated bound after the explicitly defined balanced quotient. These maps prove the relation between the ordinary class and the unresolved balanced class without identifying their vanishing conditions.', ''])
p.write_text('\n'.join(lines)+'\n')
audit=stamp+' A168 integrated after root complete-source audit and independent local complete-source/certificate audit. All actual principal-divisor roots, norm weights, ordinary class persistence, integral norm consequence, ramified valuation constraint and sharper balanced-order comparison passed. The balanced target remains explicitly unresolved.\n'
for name in ['notes/hour12_root_audits.md','notes/root_progress.md']:
 with(w/name).open('a')as f:f.write('\n'+audit)
proc=subprocess.run(['python',str(w/'code/build_register.py')],capture_output=True,text=True,check=True)
out='Integrated audited A168.\n'+proc.stdout
Path(__file__).with_name('integrate_a168_output.txt').write_text(out);print(out,end='')
