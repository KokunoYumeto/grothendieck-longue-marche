#!/usr/bin/env python3
"""Integrate the same-pair finite class surjections, retaining the convergence gap."""
from pathlib import Path
import datetime,json
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
old=r'\input{sections/legendre_dyadic_multiplier_range.tex}'
new=r'\input{sections/norm_hilbert_prime_allocation_agent.tex}'
if new not in s:s=s.replace(old,old+'\n'+new)
p.write_text(s)
p=w/'notes/register_metadata.json';m=json.loads(p.read_text())
m['A.95']={
 'answers':'A5; A15; L9; L10; L14',
 'depends_on':'A.44; A.77; A.86; A.89; A.92; primary Hilbert class fields; exact private-prime ramification intersection and Frobenius coset character maps',
 'notes':'Constructs one ordinary infinitely supported completed pair and one nested3-power root tower for which lim W surjects onto every cofinal finite class target, hence has dense image in lim C^0. The compatible representatives of each fixed finite target have finite prime support. The proof does not supply convergence as targets grow, closedness of the image or membership of the particular A86 obstruction family. The auxiliary-prime theorem accommodates the B-radical and a prescribed cyclotomic Frobenius through an explicit unramified/totally ramified intersection and invariant-character calculation.',
 'uses_local_theorem':'no; explicit ordinary local construction and ideal-class/norm maps',
 'manuscript_passages':'cote149; scans54–58,79–85; L10 and L14 fixed-pair norm compatibility problem'}
p.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md';s=p.read_text();lines=s.splitlines()
extra=' A.95 constructs one fixed ordinary pair whose actual3-power tower has surjective compatible-divisor maps to every cofinal finite class target and hence dense image in the class inverse limit. Convergence of the representatives and membership of the particular A.86 family remain unresolved.'
for i,line in enumerate(lines[:50]):
 if line.startswith(('| A5 |','| A15 |','| L10 |','| L14 |')):
  cols=line.split(' | ')
  if 'A.95' not in cols[1]:cols[1]+=', A.95'
  line=' | '.join(cols)
  if extra not in line:line=line[:-2]+extra+' |'
  lines[i]=line
s='\n'.join(lines)+'\n'
heading='## One fixed norm tower with dense divisor-correction image'
if heading not in s:
 s+='\n'+heading+'\n\n'+stamp+': A.95 strengthens the norm construction for one fixed ordinary pair. The private valuation v2(B)=1 makes the odd-primary boundary radical totally ramified at2, while the Hilbert compositum for the A-root field is unramified there. Their exact intersection after the specified cyclotomic base change is the base field. A separate coset-character argument proves that prescribing the cyclotomic Frobenius does not reduce the split-prime class subgroup. These primes can therefore be allocated as fresh A-support inside the literal A.44 recursion while preserving all old local and precision conditions.\n\nAt allocation level n=v3(M), each new prime has final A-valuation M and splits completely at that level. The exact stable inertia quotient gives W_infinity,q→W_n,q as an isomorphism. Along with A.92, this makes lim W→C_n^0 surjective at every cofinal allocation level in the same final tower. Its image in lim C_n^0 is dense. The proof gives finite-support representatives separately for each finite target; it has not supplied the convergence needed to represent the particular compatible family. This is the remaining condition in A.86.5, and no full metabelian lift or A1 conclusion is inferred.\n'
p.write_text(s)
audit=stamp+' root A95 audit: read full proof and A44 invariant transfer; checked odd-primary total ramification from the private valuation at2, unramified Hilbert base change, exact boundary/cyclotomic intersection, nonempty allowed Frobenius coset, invariant character annihilator and G0 abelianization; checked fresh finite batches preserve eighth-power shapes, unit-coordinate local points, old sum-error bounds and all excluded primes. Verified fixed embedded fields and s=n stable root quotients, finite-support compatible representatives and density in the same tower. Independent local_preprint audit passed. Two missing TeX backslashes were corrected by the author before integration. No convergence or closed-image claim is made.\n'
for q in ['notes/hour6_root_audits.md','notes/root_progress.md']:
 with (w/q).open('a') as f:f.write('\n'+audit)
out='A95 integrated: one fixed pair and tower, finite-level surjections and dense correction image; convergence remains open.\n'
Path(__file__).with_name('integrate_a95_output.txt').write_text(out)
print(out,end='')
