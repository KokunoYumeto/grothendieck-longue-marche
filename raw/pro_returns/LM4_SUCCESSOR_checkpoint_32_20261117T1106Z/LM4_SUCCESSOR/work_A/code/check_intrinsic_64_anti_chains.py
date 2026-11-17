#!/usr/bin/env python3
"""Exact integral, 2-saturated anti-invariant test on the64 actual seed columns.

This is the integer span (and its F-closure), not the complete E/deck/base
orbit module. All nonzero diagonal classes require actual source witnesses.
"""
from pathlib import Path
from collections import Counter
from functools import reduce
from math import gcd,lcm
import hashlib,json,sys,time
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
names=['symmetric_paired_fox_data.json','symmetric_source_node_alignment.json']
raw={n:(P/n).read_bytes() for n in names}
D,S=[json.loads(raw[n]) for n in names]
sys.path.insert(0,str(ROOT/'work_DE/next_marginal_source'))
from weighted_stallings import WeightedFold

def red(w):
    r=[]
    for a in w:
        if r and r[-1]==-a:r.pop()
        else:r.append(a)
    return tuple(r)
def inv(w):return tuple(-a for a in reversed(w))
def sub(w,A):return red(b for a in w for b in (A[a] if a>0 else inv(A[-a])))
def cells(row):
    d=Counter()
    for x in row['fox_cells']:
        key=(tuple(x['A_vertex']),x['A_generator'],tuple(x['B_vertex']),x['B_generator'])
        d[key]+=int(x['coefficient'])
    return {k:v for k,v in d.items() if v}
def flip(k):return (k[2],k[3],k[0],k[1])
def diagonal(d):
    out=set()
    for (u,i,w,j),c in d.items():
        if u!=w or i!=j or not c%2:continue
        for a in [u,red(u+(i,))]:
            if a in out:out.remove(a)
            else:out.add(a)
    return out
def combine(v,cols):
    out=Counter()
    for c,d in zip(v,cols):
        if c:
            for k,a in d.items():out[k]+=c*a
    return {k:v for k,v in out.items() if v}
def binary_dependence(columns):
    echelon={}
    for j,v in enumerate(columns):
        x=sum((a%2)<<i for i,a in enumerate(v));mask=1<<j
        while x:
            p=x.bit_length()-1
            if p not in echelon:echelon[p]=(x,mask);break
            y,m=echelon[p];x^=y;mask^=m
        if not x:return mask
    return None
def bit_rank(vs):
    echelon={}
    for x in vs:
        while x:
            p=x.bit_length()-1
            if p not in echelon:echelon[p]=x;break
            x^=echelon[p]
    return len(echelon)

start=time.monotonic();cols=[cells(x) for x in D['node_columns']]
assert len(cols)==64
for row,c in zip(D['node_columns'],cols):
    fc={(tuple(x['A_vertex']),x['A_generator'],tuple(x['B_vertex']),x['B_generator']):int(x['coefficient'])
        for x in row['F_fox_cells']}
    assert fc=={flip(k):-a for k,a in c.items()}
keys=sorted({min(k,flip(k)) for c in cols for k in c if k!=flip(k)})
rawrows=[];rows={}
for key in keys:
    row=tuple(c.get(key,0)-c.get(flip(key),0) for c in cols)
    if not any(row):continue
    g=reduce(gcd,(abs(a) for a in row if a))
    s=1 if next(a for a in row if a)>0 else -1
    normal=tuple(s*a//g for a in row)
    rows.setdefault(normal,len(rows));rawrows.append((key,row,normal))
Arows=list(rows);A=sp.Matrix(Arows) if Arows else sp.zeros(0,64)
print('Actual64 columns; full off-diagonal equations',len(rawrows),
      'normalized distinct equations',len(Arows),flush=True)
qbasis=A.nullspace();K=[];scales=[]
for b in qbasis:
    den=lcm(*(int(x.q) for x in b));v=[int(den*x) for x in b]
    assert all(sum(a*x for a,x in zip(row,v))==0 for row in Arows)
    K.append(v);scales.append(den)
rank=64-len(K)
_,pivot_columns=A.rref()
_,pivot_rows=A.T.rref()
assert len(pivot_columns)==len(pivot_rows)==rank
minor=A.extract(list(pivot_rows),list(pivot_columns))
minor_det=int(minor.det()) if rank else 1
assert minor_det
print('Exact rational rank',rank,'nullity',len(K),'denominator scales',scales,flush=True)
print('Nonzero rank-witness minor determinant',minor_det,flush=True)
initial=[list(v) for v in K];steps=[]
while (mask:=binary_dependence(K)) is not None:
    j=(mask&-mask).bit_length()-1
    num=[sum(K[k][i] for k in range(len(K)) if mask>>k&1) for i in range(64)]
    assert all(a%2==0 for a in num)
    new=[a//2 for a in num]
    assert all(sum(a*x for a,x in zip(row,new))==0 for row in Arows)
    steps.append({'dependence_mask':mask,'replaced_basis_index':j,'new_vector':new})
    K[j]=new
assert binary_dependence(K) is None
assert sp.Matrix.hstack(*(sp.Matrix(v) for v in K)).rank()==len(K) if K else True
print('Integral kernel 2-saturation steps',len(steps),flush=True)

chains=[];diags=[]
for v in K:
    c=combine(v,cols)
    assert all(c.get(k,0)==c.get(flip(k),0) for k in set(c)|{flip(k) for k in c})
    chains.append(c);diags.append(diagonal(c))
words=sorted(set().union(*diags)) if diags else []
wpos={w:i for i,w in enumerate(words)}
diag_masks=[sum(1<<wpos[w] for w in d) for d in diags]
diag_rank=bit_rank(diag_masks)
print('Full diagonal image rank over F2',diag_rank,'support words',len(words),flush=True)

# Preserve the common free R labels: source data may only append new ones.
for k,v in D['finite_used_common_R_basis'].items():assert S['common_R_basis'][k]==v
seeds={i+1:tuple(row['actual_source_word_R']) for i,row in enumerate(S['source_rows'])}
fold=WeightedFold(list(seeds.values()),allow_relations=True)
zero_certificates=[];unresolved=[]
for j,psi in enumerate(diags):
    remaining=set(psi);pairs=[];unmatched=[]
    while remaining:
        g=min(remaining);remaining.remove(g);mate=None
        for h in sorted(remaining):
            witness=fold.rewrite(red(inv(g)+h))
            if witness is not None:
                assert sub(witness,seeds)==red(inv(g)+h)
                mate=(h,witness);break
        if mate is None:unmatched.append(g)
        else:
            h,witness=mate;remaining.remove(h)
            pairs.append({'left_coefficient':g,'source_word_in_eight_actual_seeds':witness,
                          'other_support_word':h})
    if not unmatched:
        rebuilt=set()
        for r in pairs:
            g=tuple(r['left_coefficient']);i=sub(r['source_word_in_eight_actual_seeds'],seeds)
            for w in (g,red(g+i)):
                if w in rebuilt:rebuilt.remove(w)
                else:rebuilt.add(w)
        assert rebuilt==psi
        zero_certificates.append({'kernel_basis_index':j,'pairs':pairs})
    else:unresolved.append({'kernel_basis_index':j,'unmatched_support_words':unmatched,
                            'scope':'Only failure of this eight-seed finite subgroup pairing; no full-I nonmembership claim.'})
print('Source-ideal zero certificates',len(zero_certificates),'unresolved finite-seed pairings',len(unresolved),flush=True)
out={'scope':__doc__,'input_sha256':{n:hashlib.sha256(r).hexdigest() for n,r in raw.items()},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'sympy_version':sp.__version__,
     'column_labels':[[r['loop_index'],r['local_node_index']] for r in D['node_columns']],
     'full_off_diagonal_row_count':len(rawrows),
     'normalized_integer_equations':Arows,'rational_rank':rank,
     'rank_witness':{'row_indices':list(pivot_rows),'column_indices':list(pivot_columns),
                     'minor_determinant':minor_det,
                     'upper_bound':'The displayed independent nullspace basis has dimension64-rank.'},
     'initial_integer_kernel_basis':initial,'initial_denominator_scales':scales,
     'two_saturation_steps':steps,'two_saturated_kernel_basis':K,
     'integral_anti_invariance_directly_verified':True,
     'diagonal_group_ring_supports':[sorted(x) for x in diags],
     'diagonal_image_rank_F2':diag_rank,
     'common_R_basis':S['common_R_basis'],
     'actual_source_seeds':seeds,'source_seed_indexing':[
       {'index':i+1,'sheet':r['sheet'],'critical_index':r['critical_index']} for i,r in enumerate(S['source_rows'])],
     'source_ideal_zero_certificates':zero_certificates,
     'unresolved_finite_seed_pairings':unresolved,
     'elapsed_seconds':time.monotonic()-start,
     'claims_excluded':['full translated module exhausted','kappa vanishes globally','finite-seed nonmembership in full source','nonlinear fixed lifting']}
(ROOT/'work_A/intrinsic_64_anti_chain_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact bounded integral anti-chain test; elapsed',round(out['elapsed_seconds'],6),flush=True)
