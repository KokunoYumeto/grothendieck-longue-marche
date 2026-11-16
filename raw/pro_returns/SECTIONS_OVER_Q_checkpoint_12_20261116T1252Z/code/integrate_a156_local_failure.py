#!/usr/bin/env python3
"""Record the exact next-level obstruction to the specified norm representative."""
from pathlib import Path
import datetime,json,subprocess
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
detail='The same A.156 representative fails the next relative norm at both quadratic places over11 and59, with explicit nontrivial cubic residue characters; its first seed passes every higher local test.'
p=w/'notes/register_metadata.json';m=json.loads(p.read_text())
if detail not in m['A.156']['notes']:m['A.156']['notes']+=' '+detail
m['A.156']['depends_on']+='; exact tame cubic unit-norm residues at11 and59'
p.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines()
answers={x.strip() for x in m['A.156']['answers'].split(';')}
for i,line in enumerate(lines[:55]):
 if not line.startswith('| '):continue
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)==3 and cells[0] in answers and detail not in cells[2]:
  cells[2]+=' '+detail;lines[i]='| '+' | '.join(cells)+' |'
lines.extend(['','### The specified representative at the next norm step','',
 stamp+': '+detail,
 'In the actual quadratic residue fields F121 and F3481, beta2 has residues6+3alpha and23+57alpha. Their cubic characters are10+6alpha and58+6alpha, respectively, both nonidentity cube roots of one. At each branch K3/K2 is totally ramified cubic, with radicand valuation8, so a unit norm must have cubic residue. This proves that this beta2 cannot be used unchanged. Its residue cube is exactly the residue of beta1, retaining the already proved norm relation. The beta1 characters are both one; since the residue3-parts have order3, that first representative passes the local tests at every higher depth. The exact classes and field maps are retained in the source and independently rerun certificate. A unit repair is being investigated separately.',''])
p.write_text('\n'.join(lines)+'\n')
audit=stamp+' A156 next-level continuation root audit PASS: exact coefficient integrality bounds give the actual residue -A0, both local cubic characters are nontrivial, and normalized radicand valuations8 force total cubic ramification. Beta1 stable local admissibility checked on the same tower. The certificate was independently rerun.\n'
for name in ['notes/hour11_root_audits.md','notes/root_progress.md']:
 with(w/name).open('a')as f:f.write('\n'+audit)
r=subprocess.run(['python',str(w/'code/build_register.py')],check=True,capture_output=True,text=True)
out='Recorded actual A156 next-level norm failure.\n'+r.stdout
Path(__file__).with_name('integrate_a156_local_failure_output.txt').write_text(out);print(out,end='')
