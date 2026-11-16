#!/usr/bin/env python3
"""Idempotently integrate the audited all-finite-exponent harmonic theorem."""
from pathlib import Path
import json
import subprocess

work=Path(__file__).resolve().parents[1]
paper=work/'SECTIONS_OVER_Q_paper.tex'
text=paper.read_text()
anchor=r'\input{sections/dyadic_common_field_tower.tex}'
new=r'\input{sections/harmonic_all_exponents_initialization.tex}'
assert anchor in text
if new not in text:
    paper.write_text(text.replace(anchor,anchor+'\n'+new,1))

meta_path=work/'notes/register_metadata.json'
metadata=json.loads(meta_path.read_text())
metadata['A.127']={
    'answers':'A9; A12; A15; L14; L20',
    'depends_on':'A.85; A.112; A.123; A.126 including exact odd-factor CRT; Kedlaya4.1.2/4.1.4 signed cyclotomic norm map',
    'uses_local_theorem':'no',
    'manuscript_passages':'cote149; scans56–58,126–127; harmonic finite initialization through every Kummer exponent divisible by four',
    'notes':'Proves every harmonic common character has zero normalized local evaluation for every exponent divisible by four. The full dyadic induction retains all mixed relation vectors, the exact signed cyclotomic norm kernel and the forced even first weight at the remaining depth. The odd-factor root map gives the same actual character field; all odd places and real points are included. A85 gives a new coefficient preserving each finite prescribed old-point collection. Root and Legendre independently passed the full proof and the finite certificate passed. Cross-exponent coefficient compatibility and infinitely prescribed local data are not asserted.'
}
meta_path.write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')

report=work/'SECTIONS_OVER_Q_report.md'
lines=report.read_text().splitlines()
items={'A9','A12','A15','L14','L20'}
addition=('A.127 proves full finite harmonic initialization at every exponent '
          'divisible by four, retaining every common character and each finite '
          'collection of local old points. Compatible choices across exponents '
          'and infinitely prescribed local points remain unresolved.')
changed=0
for j,line in enumerate(lines[:55]):
    if not line.startswith('| '):
        continue
    parts=line.split('|')
    if len(parts)!=5 or parts[1].strip() not in items:
        continue
    if 'A.127' not in parts[2]:
        parts[2]=parts[2].rstrip()+', A.127 '
        parts[3]=parts[3].rstrip()+' '+addition+' '
        lines[j]='|'.join(parts)
        changed+=1
entry=('A.127 integration audit: harmonic finite initialization now holds at '
       'every exponent divisible by four. The exact odd-factor field equality '
       'reduces to a dyadic induction. At each growth step the signed '
       'cyclotomic norm map controls the unit depth; the remaining mixed '
       'relation forces its first weight even and excludes a negative '
       'normalized power. Positive new characters and prior characters are '
       'killed by the resulting actual power of the normalized entry. '
       'Deep fibres reduce through a literal root specialization and norm '
       'product. Odd and real cases retain every actual field factor. '
       'Root and Legendre independently passed the full proof. The certificate '
       'checks26 power images,1022 signed kernels,180208 mixed-relation '
       'parity implications,4537 actual odd-factor CRT lifts and4881 root '
       'equations, with132928 character consequences on1340 actual local '
       'points at exponents8 through128. The finite coefficient choices '
       'are not asserted to be compatible across exponents.')
if not any(line.startswith('A.127 integration audit:') for line in lines):
    lines.extend(['',entry,''])
report.write_text('\n'.join(lines))
print('A.127 input, metadata and parsed first-table rows integrated.',flush=True)
print('Outcome rows newly changed:',changed,flush=True)
subprocess.run(['python',str(work/'code/build_register.py')],check=True)

