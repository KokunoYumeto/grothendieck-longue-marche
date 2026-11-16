#!/usr/bin/env python3
"""Record the exact contact-four inertia comparison."""
from pathlib import Path
import json
w=Path(__file__).resolve().parents[1]
p=w/'notes/register_metadata.json'
m=json.loads(p.read_text())
m['A.91']={
 'answers':'A1; A7; L15; L19',
 'depends_on':'A.16; A.37; A.63; A.64; A.78; A.79; A.82; A.87; exact good quadratic twists and scalar inertia characters',
 'notes':'Every dyadic contact-four realization has exactly the realized local valuation pair, at all three labels, from the full scalar inertia and ordered squareclasses. The k4 H proviso in the earlier criteria is removed. Every parameter plus or minus16p^n and all six explicitly transported S3 transforms is recognized with arbitrary labeled integral comparison.',
 'uses_local_theorem':'no for the stated Selmer result; extension to arbitrary sections uses R1',
 'manuscript_passages':'cote149; scans48,54–58,66; A7 and L15 recognition problem'}
p.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')
p=w/'SECTIONS_OVER_Q_report.md'
s=p.read_text(); lines=s.splitlines()
for i,line in enumerate(lines[:50]):
 if line.startswith(('| A7 |','| L15 |')):
  columns=line.split(' | ')
  if 'A.91' not in columns[1]:columns[1]+=', A.91'
  lines[i]=' | '.join(columns)
s='\n'.join(lines)+'\n'
heading='## Contact-four recognition update at05:33 UTC'
if heading not in s:
 s+='\n'+heading+'\n\nA.91 proves the exact dyadic valuation pair at every contact-four label with arbitrary labeled integral comparison. The good quadratic twists have scalar inertia characters chi(-1),1,chi(-v); their precise ordered squareclasses exclude both alternate labels. This removes the full-H proviso at dyadic valuation four from A.79 and A.82 and recognizes every plus or minus16p^n, with all six explicitly transported transforms. Root and local-agent audits passed.\n'
p.write_text(s)
audit='05:33 UTC root audit A91: all three scalar inertia rows and every alternate-label squareclass comparison checked. The nontrivial ramified character chi(-1) is distinguished by an explicit valuation in Q2(i); the other exclusions use exactly specified squareclasses. The rational-line Tate argument retains its coefficient-prime and full scalar scope. The two actual S3 curve maps, quadratic descent characters and cancellation via A16 checked. Local independent audit also passed.\n'
with (w/'notes/hour5_root_audits.md').open('a') as f:f.write(audit)
with (w/'notes/root_progress.md').open('a') as f:f.write('\n'+audit)
out='A91 integrated; general recognition and A1 remain open.\n'
Path(__file__).with_name('integrate_a91_output.txt').write_text(out)
print(out,end='')
