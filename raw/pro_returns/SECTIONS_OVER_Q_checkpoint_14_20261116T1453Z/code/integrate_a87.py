#!/usr/bin/env python3
"""Record the reviewed dyadic inertia and recognition theorem."""
from pathlib import Path
import json
w=Path(__file__).resolve().parents[1]
p=w/'notes/register_metadata.json'
m=json.loads(p.read_text())
m['A.87']={
 'answers':'A1; A7; L15; L19',
 'depends_on':'A.16; A.34; A.37; A.63; A.78; A.82; A.84; Freitas-Kraus arXiv1607.01218v5 Table5, section14.3 and Theorem7; exact local model maps',
 'notes':'All dyadic contact-two Legendre curves have inertia SL2(F3) and minimal discriminant valuation8. Contact-four curves have inertia of order at most2 through explicit good quadratic twists. Every odd global Weil multiplier is a square. This extends the logarithmic criteria to lambda=4u with u=1 or3 mod8 under arbitrary labeled integral comparison, and recognizes lambda36 by coefficient5 and7 equations. No assertion about the coefficient-two multiplier.',
 'uses_local_theorem':'no for the stated Selmer result; extension to arbitrary sections uses R1',
 'manuscript_passages':'cote149; scans48,54–58,66; A7 and L15 recognition problem'}
p.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md'
s=p.read_text()
lines=s.splitlines()
for i,line in enumerate(lines):
 if line.startswith(('| A7 |','| L15 |')) and 'A.87' not in line:
  columns=line.split(' | ')
  columns[1]+=', A.87'
  lines[i]=' | '.join(columns[:-1])+' | '+columns[-1]
  lines[i]=lines[i][:-2]+' A.87 proves square odd Weil multipliers from dyadic contact-two inertia, extends the unrestricted criteria and recognizes36. |'
s='\n'.join(lines)+'\n'
heading='## Dyadic recognition update at05:23 UTC'
if heading not in s:
 s+='\n'+heading+'\n\nA.87 is independently audited by the root and local agent. Its three exact contact-two integral models have invariant valuations(4,6,8) and normalized discriminant1mod8. Faithful inertia reduction modulo3 and the checked Freitas–Kraus tables give order24; explicit good quadratic twists give order at most2 at contact four. Theorem7 of the opened primary source then forces every odd global multiplier to be a square. The exact coefficient5 and7 equations recognize36. The squareclass argument also extends A.79 and A.82 to all lambda=4u, u=1 or3mod8, under arbitrary labeled integral comparison. No coefficient-two multiplier claim is made.\n'
p.write_text(s)
audit='05:23 UTC root audit A87: read every displayed model, inertia-kernel argument and squareclass branch. Opened arXiv1607.01218v5 Theorem7 (printed15), Table5 C3iii (printed30), and section14.3 (printed47). The relevant necessary discriminant congruences are both minus1mod4, while the three actual models give1mod8. The actual fixed multiplier is preserved under geometric local representative changes. Verified the coefficient5 and7 logarithm divisions and the exact constant256. Local independent audit also passed.\n'
with (w/'notes/hour5_root_audits.md').open('a') as f:f.write(audit)
with (w/'notes/root_progress.md').open('a') as f:f.write('\n'+audit)
output='A87 metadata, outcome scope and root primary-source audit recorded.\n'
Path(__file__).with_name('integrate_a87_output.txt').write_text(output)
print(output,end='')
