#!/usr/bin/env python3
"""Extract one literal free-two witness from the single complete edge target."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'work_A/D_source_full_retained_class2_26.json'
d=json.loads(p.read_text())
vertices={q['id']:(q['color_F11'],tuple(q['retained_bits_f_g_x'])) for q in d['vertices']}
chosen=(8,52)
assert chosen not in {tuple(q) for q in d['complete_allowed_pairs']}
assert vertices[8]==(2,(0,0,0)) and vertices[52]==(8,(0,0,1))
def red(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return out
def project(w):
    t=[0,0,0];out=[]
    for a in w:
        if abs(a) in (5,10,11):t[(5,10,11).index(abs(a))]^=1
        elif abs(a)==2 and t==[0,0,0]:out.append(1 if a>0 else -1)
        elif abs(a)==8 and t==[0,0,1]:out.append(2 if a>0 else -2)
    assert t==[0,0,0]
    return red(out)
rows=[]
for row in d['results']:
    if row['word']!='D_s':continue
    w=project(row['defect_F11'])
    assert w
    rows.append({'operator':row['operator'],'free_two_defect':w})
    print(row['operator'],'literal free-two defect',w)

# Independent finite Heisenberg check, multiplying coordinates directly.
def heisenberg(w):
    v=(0,0,0)
    for a in w:
        z=(1,0,0) if abs(a)==1 else (0,1,0)
        # Both generator matrices are involutions over F2.
        v=((v[0]+z[0])%2,(v[1]+z[1])%2,(v[2]+z[2]+v[0]*z[1])%2)
    return v
for row in rows:
    row['UT3_F2_image']=heisenberg(row['free_two_defect'])
    assert row['UT3_F2_image']==(0,0,1)
print('Both defects detected by the single UT3(F2) target; all512 allowed pairs omit the selected pair.')
out={'status':'PASS_LITERAL_FREE_PAIR_AND_FINITE_WITNESS',
     'input':str(p.relative_to(ROOT)),'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'selected_vertices':{str(i):vertices[i] for i in chosen},'results':rows,
     'literal_section':['B','x bar_d x^-1'],
     'scope':'A restriction of the actual finite-retained-cover fiber map, not a source-equivariant quotient. Complete node-orbit omission kills N. The same continuous construction on the actual closed family kernel detects both defects.'}
(ROOT/'work_A/D_source_free_pair26.json').write_text(json.dumps(out,indent=2)+'\n')
