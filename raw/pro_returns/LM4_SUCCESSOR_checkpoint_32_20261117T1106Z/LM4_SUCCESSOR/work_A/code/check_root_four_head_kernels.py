#!/usr/bin/env python3
"""Exact eight head maps on the four-root free subgroup; no column claim."""
from pathlib import Path
import hashlib,itertools,json
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'work_A/old_base_augmented_row_action.json';raw=p.read_bytes();d=json.loads(raw)
def red(w):
    a=[]
    for x in w:
        if a and a[-1]==-x:a.pop()
        else:a.append(x)
    return a
def inv(w):return[-x for x in w[::-1]]
rows=[]
for i in(2,3,5,6,7,8,10,11):
    heads=[a['A_heads'][str(i)] for a in d['old_generators'][2:]]
    nz=[j for j,h in enumerate(heads) if h];assert len(nz)==2
    a,b=[heads[j] for j in nz]
    comm=red(a+b+inv(a)+inv(b));assert comm
    aa=[sum((1 if x>0 else -1) for x in a if abs(x)==j) for j in range(1,6)]
    bb=[sum((1 if x>0 else -1) for x in b if abs(x)==j) for j in range(1,6)]
    minors=[(j+1,k+1,aa[j]*bb[k]-aa[k]*bb[j]) for j,k in itertools.combinations(range(5),2)]
    unit=next(x for x in minors if abs(x[2])==1)
    rows.append({'slot':i,'zero_root_generators':[j+2 for j,h in enumerate(heads) if not h],
                 'nonzero_root_generators':[j+2 for j in nz],
                 'nonzero_heads':[a,b],'commutator':comm,'abelian_unit_minor':unit})
out={'input_sha256':hashlib.sha256(raw).hexdigest(),
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'rows':rows,'scope':'four-root free subgroup only; no full-column or whole-kernel assertion'}
(ROOT/'work_A/root_four_head_kernel_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:all8 head maps have exactly2 zero and2 noncommuting nonzero root-generator images.')
print('PASS:each nonzero pair has an integral abelian unit minor; all full words retained.')
print('Scope:four-root free subgroup only; no full-column action is inferred.')
