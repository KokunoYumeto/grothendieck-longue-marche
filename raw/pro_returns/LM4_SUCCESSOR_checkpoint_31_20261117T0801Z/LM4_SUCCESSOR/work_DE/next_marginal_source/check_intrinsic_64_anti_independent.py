#!/usr/bin/env python3
"""Independent exact five-chain and actual-source audit of the bounded64 span.

Reconstructs full symmetry equations, checks the supplied rank minor by
fraction-free elimination, proves the five integer vectors span using
their free-coordinate identity block, and expands every source word
into the actual F13 marking from the nineteen-source package.
"""
from pathlib import Path
from collections import defaultdict
from math import gcd
from functools import reduce as fold
import json,hashlib,time

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent
paths=[ROOT/'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json',
       ROOT/'work_A/intrinsic_64_anti_chain_certificate.json',
       ROOT/'work_CE/next_symmetric_nodes/symmetric_full_source_data.json']
raw=[p.read_bytes() for p in paths];P,D,S=map(json.loads,raw)
start=time.monotonic()
def red(w):
    ans=[]
    for x in w:
        if ans and ans[-1]==-x:ans.pop()
        else:ans.append(int(x))
    return tuple(ans)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
def flip(k):return k[2],k[3],k[0],k[1]
def cells(r):
    out={}
    for x in r['fox_cells']:
        k=tuple(x['A_vertex']),x['A_generator'],tuple(x['B_vertex']),x['B_generator']
        assert k not in out
        out[k]=x['coefficient']
    return out
cols=[cells(r) for r in P['node_columns']]
keys=sorted({min(k,flip(k)) for c in cols for k in c if k!=flip(k)})
normal=[];seen=set();fullrows=[]
for k in keys:
    r=tuple(c.get(k,0)-c.get(flip(k),0) for c in cols)
    if not any(r):continue
    fullrows.append(r);g=fold(gcd,(abs(x) for x in r if x))
    sign=1 if next(x for x in r if x)>0 else -1
    r=tuple(sign*x//g for x in r)
    if r not in seen:normal.append(r);seen.add(r)
assert normal==[tuple(r) for r in D['normalized_integer_equations']]
assert len(fullrows)==1951 and len(normal)==84

def bareiss(matrix):
    a=[list(r) for r in matrix];n=len(a);old=1;sign=1
    for k in range(n-1):
        pivot=next(i for i in range(k,n) if a[i][k])
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=p*a[i][j]-a[i][k]*a[k][j]
                assert z%old==0
                a[i][j]=z//old
            a[i][k]=0
        old=p
    return sign*a[-1][-1]
wit=D['rank_witness'];ri=wit['row_indices'];ci=wit['column_indices']
assert len(ri)==len(ci)==59
det=bareiss([[normal[i][j] for j in ci] for i in ri])
assert det==-1==wit['minor_determinant']
K=[tuple(v) for v in D['two_saturated_kernel_basis']]
assert len(K)==5 and all(len(v)==64 for v in K)
for v in K:
    assert all(sum(x*y for x,y in zip(r,v))==0 for r in fullrows)
free=sorted(set(range(64))-set(ci))
assert [[v[j] for j in free] for v in K]==[[int(i==j) for j in range(5)] for i in range(5)]
# Any integer kernel vector is the sum of its five free coordinates times
# these vectors: the remainder has zero free coordinates and the59x59
# nonsingular minor kills every remaining coordinate. Thus full saturation
# is proved, not merely saturation at2.

ret=P['retained_paired_indices'];kept=S['first_family_F13_kept_paired_indices']
ren={j:i+1 for i,j in enumerate(kept)}
Rimages={}
for j,r in D['common_R_basis'].items():
    t=tuple((1 if x>0 else -1)*ren[ret[abs(x)-1]] for x in r['retained_word'])
    Rimages[int(j)]=red(t+(ren[r['paired_slot']],)+inv(t))
seed={int(j):tuple(w) for j,w in D['actual_source_seeds'].items()}
actual={(r['sheet'],r['critical_index']):r for r in S['source_peripheral_generators']}
for r in D['source_seed_indexing']:
    original=actual[r['sheet'],r['critical_index']]
    assert sub(seed[r['index']],Rimages)==tuple(original['positive_source_word_F13'])

checks=[]
for i,v in enumerate(K):
    chain=defaultdict(int)
    for coefficient,c in zip(v,cols):
        for k,n in c.items():chain[k]+=coefficient*n
    chain={k:n for k,n in chain.items() if n}
    assert all(chain.get(k,0)==chain.get(flip(k),0) for k in set(chain)|{flip(k) for k in chain})
    psi=set()
    for (u,a,w,b),n in chain.items():
        if (u,a)!=(w,b) or not n%2:continue
        for g in (u,red(u+(a,))):
            if g in psi:psi.remove(g)
            else:psi.add(g)
    assert psi=={tuple(w) for w in D['diagonal_group_ring_supports'][i]}
    cert=next(r for r in D['source_ideal_zero_certificates'] if r['kernel_basis_index']==i)
    rebuilt=set();witnesses=[]
    for pair in cert['pairs']:
        g=tuple(pair['left_coefficient']);sw=tuple(pair['source_word_in_eight_actual_seeds'])
        iw=sub(sw,seed);other=red(g+iw)
        assert other==tuple(pair['other_support_word'])
        for word in (g,other):
            if word in rebuilt:rebuilt.remove(word)
            else:rebuilt.add(word)
        witnesses.append({'left_R_word':g,'source_basis_F19_word':[(1 if x>0 else -1)*(11+abs(x)) for x in sw],
                          'I_word_F13':sub(iw,Rimages)})
    assert rebuilt==psi
    checks.append({'basis_index':i,'nonzero_column_coefficients':[(D['column_labels'][j],n) for j,n in enumerate(v) if n],
                   'diagonal_R_support':sorted(psi),'source_witnesses':witnesses})
assert sum(bool(r['source_witnesses']) for r in checks)==2
out={'input_sha256':{p.name:hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
     'full_equations':len(fullrows),'normalized_equations':len(normal),'rank':59,
     'rank_minor_det':det,'integer_kernel_rank':5,'full_integer_saturation':'free-coordinate identity block plus nonsingular59-minor',
     'checks':checks,'all_eight_seed_images_match_actual_F13':True,
     'scope':'entire integer span of64 seed columns and its F-closure only; all diagonal values in J_I; no full E/deck/base closure claim',
     'elapsed_seconds':time.monotonic()-start}
(HERE/'intrinsic_64_anti_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: rebuilt1951 full equations,84 normalized equations; independent Bareiss59-minor determinant -1.')
print('PASS: five displayed vectors form the FULL saturated integral anti-chain kernel.')
print('PASS: all five complete chains and diagonal supports; two nonzero diagonals are actual source seeds3 and4.')
print('PASS: all8 R seed words expand to the audited actual F13 source words; full translated module remains open.')
print('Elapsed seconds',round(out['elapsed_seconds'],3))
