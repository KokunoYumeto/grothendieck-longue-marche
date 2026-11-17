#!/usr/bin/env python3
"""Exact small printed source table for proposed B131; no new target."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'work_CE/next_symmetric_nodes/annular_two_operator25.json'
d=json.loads(p.read_text())
def red(w):
    o=[]
    for a in w:
        if o and o[-1]==-a:o.pop()
        else:o.append(a)
    return o
def inv(w):return [-a for a in w[::-1]]
def sub(w,mp):return red(a for i in w for a in (mp[abs(i)] if i>0 else inv(mp[abs(i)])))
def project(w):
    t=0;o=[]
    for a in w:
        if abs(a) in (5,10,11):t^=1<<(5,10,11).index(abs(a))
        elif abs(a)==2 and t==0:o.append(1 if a>0 else -1)
        elif abs(a)==8 and t==4:o.append(2 if a>0 else -2)
    assert t==0
    return red(o)
raw=[r['fiber11'] for r in d['actual_six_source_normal_forms'][:4]]
table={'identity':[project(w) for w in raw]}
for name in ('m','m_inverse'):
    mp={int(k):v for k,v in d['source_ordinary_actions'][name].items()}
    table[name]=[project(sub(w,mp)) for w in raw]
assert table=={'identity':[[-1],[],[-2],[]],'m':[[],[],[-2],[]],'m_inverse':[[],[],[-2],[]]}
for k,v in table.items():print(k,v)
out={'status':'PASS_ALL_TWELVE_PRINTED_IMAGES','input':str(p.relative_to(ROOT)),
     'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'table':table,
     'scope':'Exact same two selected retained-residue coordinates as the reviewed B131 proof. No new quotient, period, group target or source orbit.'}
(ROOT/'work_A/B131_printed_images26.json').write_text(json.dumps(out,indent=2)+'\n')
