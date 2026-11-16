#!/usr/bin/env python3
"""Integrate the audited relative forms at every three-power precision."""
from pathlib import Path
import datetime
import json
import subprocess

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
source=w/'sections/relative_precision_forms_agent.tex'
assert r'\!left(' not in source.read_text(), 'Correct the reviewed display typo first.'
p=w/'SECTIONS_OVER_Q_paper.tex'
s=p.read_text()
new=r'\input{sections/relative_precision_forms_agent.tex}'
anchor=r'\input{sections/harmonic_all_exponents_initialization.tex}'
assert anchor in s
if new not in s:s=s.replace(anchor,anchor+'\n'+new,1)
p.write_text(s)

p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta['A.129']={
    'answers':'A5; A9; A15; L10; L14; L20',
    'depends_on':'A.106 exact local splitting and primitive unit; A.115 all mod-three relative forms; integral cyclotomic substitution and Smith normal form',
    'uses_local_theorem':'no; actual finite torsion modules and continuous cup maps',
    'manuscript_passages':'cote149; scans56–58,126–127; higher-precision relative norm repair',
    'notes':'Computes every equivariant bilinear form C_r tensor C_r to mu_(3^r), with the actual block pairing character and semi-invariant substitution equation. The Smith calculation forces exactly n elementary divisors of valuation one; all forms factor through the displayed mod-three source reduction and coefficient inclusion. Every form is alternating and all coefficient/source transition maps are computed. An actual relative norm-one point over Q_321193 at precision nine has all these quadratic values zero and noncyclic local image. Root and local_preprint independent proofs audits passed; root reran all exact Smith, action and transition checks. No higher-power cyclic repair or compatible infinite norm family is inferred.'
}
p.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')

p=w/'SECTIONS_OVER_Q_report.md'
lines=p.read_text().splitlines()
items={'A5','A9','A15','L10','L14','L20'}
detail=('A.129 computes all relative bilinear forms at every three-power precision. '
        'They factor through the exact mod-three reduction and inclusion maps; '
        'an actual precision-nine local class has every such value zero and noncyclic image. '
        'The higher-power norm conditions at allocated primes remain unresolved.')
changed=0
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[cell.strip() for cell in line.strip().strip('|').split('|')]
    if len(cells)!=3 or cells[0] not in items:continue
    if 'A.129' not in cells[1]:cells[1]+=', A.129'
    if detail not in cells[2]:cells[2]+=' '+detail
    lines[i]='| '+' | '.join(cells)+' |'
    changed+=1
heading='## Higher-precision relative forms and their exact transitions'
if heading not in lines:
    lines.extend(['',heading,'',stamp+': '+detail,
        'The integral substitution operator is sigma_2+2 on Z_3[x]/Phi_(3^n). Its determinant has valuation n and its mod-three nullity is n, so each nonunit Smith entry has valuation one. The explicit pairing character supplies all equivariant bilinear forms, and the argument and value transitions give the cochain-level cup comparison. The local counterexample is an actual product-one triple (q,q^(-1)g^3,g^(-3)) with q=321193 and g=5. Its tame vector has order nine and its unramified vector lies outside that cyclic subgroup. This records the precise limitation of the bilinear tests.',''])
p.write_text('\n'.join(lines)+'\n')
audit=('A129 full source audit passed root and local_preprint: actual torsion kernel and cyclic ideal basis, arithmetic block-pairing character, conjugation orientation of the semi-invariant equation, one-cycle characteristic polynomial, exact Smith valuations, all source and coefficient maps, continuous cup naturality, and actual precision-nine product-one example. Root executed the retained certificate:30 exact Smith-kernel counts,60 action comparisons,48 precision transitions; all passed. The source display typo in A129.5 was corrected before integration.')
for name in ['notes/hour9_root_audits.md','notes/root_progress.md']:
    p=w/name
    s=p.read_text() if p.exists() else '# Ninth-hour root audits\n'
    if audit not in s:p.write_text(s+'\n'+stamp+' '+audit+'\n')
result=subprocess.run(['python',str(w/'code/build_register.py')],check=True,text=True,capture_output=True)
out=f'Integrated A129; updated {changed} outcome rows.\n'+result.stdout+'Both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a129_output.txt').write_text(out)
print(out,end='')
