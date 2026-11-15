#!/usr/bin/env python3
"""Exact F_2 homology of finite stable-graph-type rank posets.

These are explicit quotient targets of the actual rank-selected multicurve
posets. Their homology is not asserted to equal the homology of those posets.
"""
from pathlib import Path
from itertools import combinations
import json

P=Path(__file__).resolve().parent

def rank_mod2(columns):
    piv={}
    for x in columns:
        while x:
            j=x.bit_length()-1
            if j not in piv:
                piv[j]=x
                break
            x^=piv[j]
    return len(piv)

def calculate(g,n,k):
    a=json.loads((P/f'a_graphs_{g}_{n}.json').read_text())
    d=3*g-3+n
    vertices=[i for i,G in enumerate(a['graphs']) if len(G[2])>=d-k]
    below=[set(v) for v in a['contractions']]
    chains=[[(i,) for i in vertices]]
    while chains[-1]:
        nex=[]
        for c in chains[-1]:
            nex.extend(c+(j,) for j in vertices if j>c[-1] and c[-1] in below[j])
        if not nex:break
        chains.append(nex)
    ranks=[0]
    for j in range(1,len(chains)):
        ix={c:i for i,c in enumerate(chains[j-1])}
        columns=[sum(1<<ix[c[:i]+c[i+1:]] for i in range(len(c))) for c in chains[j]]
        ranks.append(rank_mod2(columns))
    ranks.append(0)
    betti=[len(c)-ranks[i]-ranks[i+1] for i,c in enumerate(chains)]
    out={'type':[g,n],'k':k,'cells':list(map(len,chains)),'F2_betti':betti}
    print(json.dumps(out))
    return out

rows=[]
for g,n in [(2,1),(2,2),(3,0)]:
    if (P/f'a_graphs_{g}_{n}.json').exists():
        for k in range(1,min(4,3*g-3+n)):
            rows.append(calculate(g,n,k))
(P/'d_rank_quotients.json').write_text(json.dumps(rows,indent=2)+'\n')
print('These quotient computations do not certify connectivity of the infinite multicurve posets.')
