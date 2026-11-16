#!/usr/bin/env python3
"""Idempotently integrate the independently audited A.121 common-field theorem."""
from pathlib import Path
import json
import subprocess

work=Path(__file__).resolve().parents[1]
paper=work/'SECTIONS_OVER_Q_paper.tex'
text=paper.read_text()
anchor=r'\input{sections/cubic_source_quartic_initialization.tex}'
new=r'\input{sections/eighth_common_field.tex}'
assert anchor in text
if new not in text:
    paper.write_text(text.replace(anchor,anchor+'\n'+new,1))

meta_path=work/'notes/register_metadata.json'
metadata=json.loads(meta_path.read_text())
metadata['A.121']={
    'answers':'A9; A12; A15; L14; L20',
    'depends_on':'A.57 actual radical splitting group; A.80; A.96; exact Z/4 stabilizer and annihilator maps',
    'uses_local_theorem':'no',
    'manuscript_passages':'cote149; scans56–58,126–127; complete higher-exponent puncture-fibre character calculation',
    'notes':'Computes the entire common abelian field of every rational eighth-root fibre. Gives the exact no-i and middle stabilizer-coset cases and every positive/negative fourth-power relation generator when mu8 is already in B4. Direct field-factor inclusions, the harmonic pure-chi16 example, and a necessary positive sqrt5 direction are explicit. Root and Legendre independently passed the complete proof; the finite certificate checks796 tuples and67056 literal root equations. The field theorem alone does not assert local constancy or full compatible initialization.'
}
meta_path.write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')

report=work/'SECTIONS_OVER_Q_report.md'
lines=report.read_text().splitlines()
items={'A9','A12','A15','L14','L20'}
addition=('A.121 computes every common character of an eighth-root fibre, '
          'with the exact middle stabilizer case and all positive and negative '
          'fourth-power relation generators. Its local evaluations are being '
          'analyzed through the stated norm maps.')
changed=0
for j,line in enumerate(lines[:55]):
    if not line.startswith('| '):
        continue
    parts=line.split('|')
    if len(parts)!=5 or parts[1].strip() not in items:
        continue
    if 'A.121' not in parts[2]:
        parts[2]=parts[2].rstrip()+', A.121 '
        parts[3]=parts[3].rstrip()+' '+addition+' '
        lines[j]='|'.join(parts)
        changed+=1
entry=('A.121 integration audit: the complete octic common field is now proved '
       'from actual root stabilizers. If i is absent from the individual quadratic '
       'field, A80 gives that field exactly. If i is present but sqrt2 is absent '
       'from B4, the actual u=5 mod8 stabilizers generate the full fixing subgroup. '
       'When mu8 is in B4, the Z/4 relation module gives all positive quadratic '
       'and negative order-four character fields, with explicit inclusions into '
       'every fibre factor. Root and Legendre passed independent full audits. '
       'The retained exact certificate passes796 field tuples,1140 relation '
       'vectors,384 coset products,6120 literal lifts and67056 root equations. '
       'No local nonvanishing or completed initialization is inferred from '
       'this finite field calculation.')
if not any(line.startswith('A.121 integration audit:') for line in lines):
    lines.extend(['',entry,''])
report.write_text('\n'.join(lines))
print('A.121 input, metadata and parsed first-table rows integrated.')
print('Outcome rows newly changed:',changed)
subprocess.run(['python',str(work/'code/build_register.py')],check=True)

