#!/usr/bin/env python3
"""Exact F2 module exploration for the actual top elementary2^72 kernel.

All matrices come from the original pc conjugation words.  This script makes
no homological lifting claim; it saves complete rank data when finished.
"""
from pathlib import Path
import hashlib,itertools,json,time
CODE=Path(__file__).resolve().parent
src=CODE/'pbc_iterated_shortcut_v2_original_source.json'
s=json.loads(src.read_text());C={(i,j):w for i,j,w in s['conjugates']}
assert hashlib.sha256(src.read_bytes()).hexdigest()=='95fb384593bfaf97d468bbc51f11cd797484a08cb3ec3b954961085b520ffc88'
d=72;low=104;pairs=list(itertools.combinations(range(d),2));width=len(pairs)
def insert(B,v):
    while v:
        p=v.bit_length()-1
        if p not in B:B[p]=v;return True
        v^=B[p]
    return False
def wedge_index(a,b):
    if a>b:a,b=b,a
    assert a<b
    return a*(2*d-a-1)//2+b-a-1
matrices={}
ordinary={};ordinary_selected=[]
for g in range(1,105):
    rows=[];rank={}
    for i in range(105,177):
        w=C[i,g];v=0
        for k,a in zip(w[::2],w[1::2]):
            assert 105<=k<=176
            if a%2:v^=1<<(k-105)
        rows.append(v);insert(rank,v)
        if g>=87 and insert(ordinary,v^(1<<(i-105))):ordinary_selected.append([g,i])
    assert len(rank)==d
    matrices[g]=rows
assert len(ordinary)==72
print('NORMAL_THREE_SUBGROUP_COINVARIANTS',d-len(ordinary),flush=True)
B={};selected=[];stats=[];start=time.time();digest=hashlib.sha256()
order=[1,2]+list(range(87,105))+list(range(3,87))
for g in order:
    support=[[i for i in range(d) if v>>i&1] for v in matrices[g]]
    before=len(B)
    for q,(i,j) in enumerate(pairs):
        v=1<<q
        for a in support[i]:
            for b in support[j]:
                if a!=b:v^=1<<wedge_index(a,b)
        digest.update(v.to_bytes((width+7)//8,'little'))
        if insert(B,v):selected.append([g,105+i,105+j])
    stats.append(dict(generator=g,rank=len(B),new_rank=len(B)-before,seconds=time.time()-start))
    print(json.dumps(stats[-1]),flush=True)
out=dict(status='PASS',source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),
         checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         module_dimension=d,normal_three_coinvariant_dimension=0,
         normal_three_independent_row_labels=ordinary_selected,
         all_action_matrices_hex={str(g):[hex(v) for v in rows] for g,rows in matrices.items()},
         wedge_dimension=width,wedge_rank=len(B),wedge_coinvariant_dimension=width-len(B),
         wedge_rows_checked=104*width,all_rows_sha256=digest.hexdigest(),
         independent_original_wedge_row_labels=selected,per_generator=stats,
         scope='Exact actual module ranks only; no target identity or full C31 conclusion.')
(CODE/'pbc_two_top_module.json').write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE_WEDGE_COINVARIANTS',width-len(B),'seconds',time.time()-start,flush=True)
