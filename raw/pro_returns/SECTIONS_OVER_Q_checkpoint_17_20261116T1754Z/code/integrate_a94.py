#!/usr/bin/env python3
"""Record the independently reviewed dyadic multiplier theorem."""
from pathlib import Path
import datetime,json
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
old=r'\input{sections/completed_old_section_obstruction.tex}'
new=r'\input{sections/legendre_dyadic_multiplier_range.tex}'
if new not in s:s=s.replace(old,old+'\n'+new)
p.write_text(s)
p=w/'notes/register_metadata.json';m=json.loads(p.read_text())
m['A.94']={
 'answers':'A7; L15; L16; L19',
 'depends_on':'A.14; A.16; A.34; A.37; A.39; A.82; A.87; A.91; Freitas-Kraus arXiv1607.01218v5 Theorems6–9, Proposition6, Tables3 and5, Sections14.2–14.3',
 'notes':'For labeled integral realization, dyadic contact1 and3 force the exact ordinary dyadic valuation pair and inertia orders8 and24. At contacts1,2,3 every odd fixed global Weil multiplier is square. At contact4 only the additional coefficient7 square restriction is proved, using the actual common good reduction and nonscalar Jordan Frobenius centralizer. No coefficient2 multiplier assertion is made. All local model maps, common twists, conductor64 exclusion and source hypotheses are explicit.',
 'uses_local_theorem':'no in the stated Selmer realization range; arbitrary-section passage elsewhere uses the stipulated local classification',
 'manuscript_passages':'cote149; scans54–58; L15 exact integral congruence recognition comparison'}
p.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md';s=p.read_text();lines=s.splitlines()
extra=' A.94 fixes the exact dyadic valuation pair at contacts1 and3 and proves that all odd global Weil multipliers are square at contacts1,2,3. At contact4 it adds the coefficient7 square restriction, with no coefficient2 claim.'
for i,line in enumerate(lines[:50]):
 if line.startswith(('| A7 |','| L15 |')):
  cols=line.split(' | ')
  if 'A.94' not in cols[1]:cols[1]+=', A.94'
  line=' | '.join(cols)
  if extra not in line:line=line[:-2]+extra+' |'
  lines[i]=line
s='\n'.join(lines)+'\n'
heading='## Dyadic multiplier range and the contact-four restriction'
if heading not in s:
 s+='\n'+heading+'\n\n'+stamp+': A.94 proves exact dyadic labels and contact orders at contacts1 and3. Explicit minimal Weierstrass models, the cubic-resolvent partition action and the opened inertia lists give orders8 and24. At contact1 the proof checks the conductor64 alternative by its actual two-twist and excludes it through the normalized c4 residue; this places both curves in the same case of the Freitas–Kraus quaternionic criterion. Every odd multiplier is consequently square at contacts1,2,3. At contact4, equal local twists and Weil-paired good specialization give the same curve over F2, with Frobenius trace−1 and discriminant−7. The nonscalar Jordan centralizer at coefficient7 has square determinants, giving precisely that additional restriction. Coefficient2 and the remaining contact-four or cuspidal potentially multiplicative cases retain their stated scope.\n'
p.write_text(s)
audit=stamp+' root A94 audit: independently read the four model rows and changes of variables, c4-minimality obstruction, pair-partition Q8 kernel, inertia exclusions, exact parity-to-label transfer, conductor64/two-twist contradiction and same-case hypotheses. Opened Freitas–Kraus v5 Theorems6–9, Proposition6/Table5, Sections14.2–14.3 and the conductor reduction in the proof of Theorem9. Checked contact4 infinity uses G_(1/u), equal twisting characters, Weil-paired specialization, four F2 points, discriminant−7 and square determinant centralizer. No extra Δ2 or all-coefficient contact4 assertion. Independent local_preprint audit passed.\n'
for q in ['notes/hour6_root_audits.md','notes/root_progress.md']:
 with (w/q).open('a') as f:f.write('\n'+audit)
out='A94 integrated; odd multipliers square at contacts1–3 and coefficient7 at contact4, with exact local maps.\n'
Path(__file__).with_name('integrate_a94_output.txt').write_text(out)
print(out,end='')
