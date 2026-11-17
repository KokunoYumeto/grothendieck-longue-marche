#!/usr/bin/env python3
"""Independent bounded old0 anti-kernel decomposition and source audit."""
from pathlib import Path
from collections import defaultdict
from math import gcd
from functools import reduce as fold
import json,hashlib,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent
paths=[ROOT/'work_A/intrinsic_old0_128_columns.json',ROOT/'work_A/intrinsic_old0_128_anti_chain_certificate.json',
       ROOT/'work_A/intrinsic_64_anti_chain_certificate.json',ROOT/'work_CE/next_symmetric_nodes/symmetric_full_source_data.json',
       ROOT/'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json']
raw=[p.read_bytes() for p in paths];C,D,K64,S,P=map(json.loads,raw);started=time.monotonic()
def red(w):
    a=[]
    for x in w:
        if a and a[-1]==-x:a.pop()
        else:a.append(int(x))
    return tuple(a)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
def cell(row):return {(tuple(x['A_vertex']),x['A_generator'],tuple(x['B_vertex']),x['B_generator']):x['coefficient'] for x in row['fox_cells']}
def flip(k):return k[2],k[3],k[0],k[1]
def determinant(matrix):
    a=[list(r) for r in matrix];n=len(a);previous=1;sign=1
    for k in range(n-1):
        p=next(i for i in range(k,n) if a[i][k])
        if p!=k:a[k],a[p]=a[p],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=pivot*a[i][j]-a[i][k]*a[k][j]
                assert value%previous==0;a[i][j]=value//previous
            a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]
cols=[cell(r) for r in C['node_columns']]
assert len(cols)==128
source0=S['old_source_generators'][0]
assert source0['name']=='old_0' and source0['h_paired']==[]
A21={int(j):tuple(w) for j,w in source0['source_push_F21'].items()}
assert A21=={int(j):tuple(w) for j,w in P['old_actions'][0]['geometric_push_paired'].items()}
for j,r in enumerate(P['node_columns']):
    assert cols[j]==cell(r)
    assert tuple(C['node_columns'][j+64]['paired_relator'])==sub(r['paired_relator'],A21)
keys=sorted({min(k,flip(k)) for c in cols for k in c if k!=flip(k)})
rows=[];seen=set();fullcount=0
for k in keys:
    row=tuple(c.get(k,0)-c.get(flip(k),0) for c in cols)
    if not any(row):continue
    fullcount+=1;g=fold(gcd,(abs(x) for x in row if x));s=1 if next(x for x in row if x)>0 else -1
    normal=tuple(s*x//g for x in row)
    if normal not in seen:rows.append(normal);seen.add(normal)
assert fullcount==8166 and rows==[tuple(r) for r in D['normalized_integer_equations']]
assert len(rows)==195
w=D['rank_witness'];ri=w['row_indices'];ci=w['column_indices']
assert len(ri)==len(ci)==116
assert determinant([[rows[i][j] for j in ci] for i in ri])==-1
K=[tuple(v) for v in D['two_saturated_kernel_basis']];free=sorted(set(range(128))-set(ci))
assert len(K)==12 and [[v[j] for j in free] for v in K]==[[int(i==j) for j in range(12)] for i in range(12)]
assert all(all(sum(x*y for x,y in zip(row,v))==0 for row in rows) for v in K)
expected=[tuple(v)+(0,)*64 for v in K64['two_saturated_kernel_basis']]
expected += [(0,)*64+tuple(v) for v in K64['two_saturated_kernel_basis']]
for label in ([6,3],[6,7]):
    j=K64['column_labels'].index(label);v=[0]*128;v[j]=-1;v[j+64]=1;expected.append(tuple(v))
change=[[v[j] for j in free] for v in expected]
assert abs(determinant(change))==1
for v,coeff in zip(expected,change):
    assert v==tuple(sum(coeff[i]*K[i][j] for i in range(12)) for j in range(128))

ret=P['retained_paired_indices'];ren={j:i+1 for i,j in enumerate(S['first_family_F13_kept_paired_indices'])}
expand={}
for j,r in D['common_R_basis'].items():
    t=tuple((1 if x>0 else -1)*ren[ret[abs(x)-1]] for x in r['retained_word'])
    expand[int(j)]=red(t+(ren[r['paired_slot']],)+inv(t))
seeds={int(j):tuple(v) for j,v in D['actual_source_seeds'].items()}
A13={int(j):tuple(v) for j,v in source0['source_push_F13'].items()}
for row in D['source_seed_indexing']:
    base=S['source_peripheral_generators'][row['source_seed_index']-1]
    assert (row['sheet'],row['critical_index'])==(base['sheet'],base['critical_index'])
    target=tuple(base['positive_source_word_F13'])
    if row['layer']:target=sub(target,A13)
    assert sub(seeds[row['index']],expand)==target

checks=[]
for i,v in enumerate(K):
    chain=defaultdict(int)
    for n,c in zip(v,cols):
        for k,a in c.items():chain[k]+=n*a
    chain={k:n for k,n in chain.items() if n}
    assert all(chain.get(k,0)==chain.get(flip(k),0) for k in set(chain)|{flip(k) for k in chain})
    psi=set()
    for (u,a,w,b),n in chain.items():
        if (u,a)!=(w,b) or not n%2:continue
        for x in (u,red(u+(a,))):
            if x in psi:psi.remove(x)
            else:psi.add(x)
    assert psi=={tuple(w) for w in D['diagonal_group_ring_supports'][i]}
    cert=next(r for r in D['source_ideal_zero_certificates'] if r['kernel_basis_index']==i)
    rebuilt=set();witness=[]
    for p in cert['pairs']:
        g=tuple(p['left_coefficient']);sw=tuple(p['source_word_in_sixteen_actual_witnesses'])
        other=red(g+sub(sw,seeds));assert other==tuple(p['other_support_word'])
        for x in (g,other):
            if x in rebuilt:rebuilt.remove(x)
            else:rebuilt.add(x)
        witness.append(sw)
    assert rebuilt==psi
    checks.append({'basis_index':i,'support_words':len(psi),'source_witnesses':witness})
used={abs(x) for r in checks for w in r['source_witnesses'] for x in w}
assert used=={3,4,11,12}
out={'input_sha256':{p.name:hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
     'full_equations':fullcount,'normalized_equations':len(rows),'exact_rank':116,'minor_det':-1,
     'integral_kernel_rank':12,'decomposition':'5 original +5 old0 translates +2 literal zero-column relations',
     'all16_source_witnesses_checked_in_actual_F13':True,'checks':checks,
     'scope':'one old0 integer-span union and F-closure only; no full E/deck/base orbit exhaustion',
     'elapsed_seconds':time.monotonic()-started}
(HERE/'intrinsic_old0_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:8166 full equations,195 normalized rows; independent116-minor determinant -1.')
print('PASS:full integral kernel is exactly5 original +5 old0 images +2 zero-column relations.')
print('PASS:all12 diagonal zero certificates; source witnesses3,4,11,12 are literal seeds and old0 source conjugates.')
print('Elapsed seconds',round(out['elapsed_seconds'],3))
