#!/usr/bin/env python3
"""Exhaust the central degree9 corrections of the two recorded rank2 images."""
from pathlib import Path
from collections import deque
from functools import lru_cache
from itertools import product
import json,time

OUT=Path(__file__).resolve().parent;started=time.time()
B=json.loads((OUT/'d_cm_solvable_even_boundary.json').read_text())
D=json.loads((OUT/'d_cm_rank2_boundary_test.json').read_text())
def tensor(a,b,d):
    out=0
    while b:
        bit=b&-b;j=bit.bit_length()-1;b^=bit;out^=a<<(j<<d)
    return out
def lyndon(w):return all(w<w[k:]+w[:k] for k in range(1,len(w)))
@lru_cache(None)
def leading(w):
    if len(w)==1:return 1<<w[0]
    k=next(k for k in range(1,len(w)) if lyndon(w[k:]))
    a,b=leading(w[:k]),leading(w[k:])
    return tensor(a,b,k)^tensor(b,a,len(w)-k)
words=[w for w in product(range(2),repeat=9) if lyndon(w)]
L=[leading(w) for w in words];assert len(L)==56
def span(cols):
    piv={}
    for j,v0 in enumerate(cols):
        v=v0;mask=1<<j
        while v:
            p=v.bit_length()-1
            if p not in piv:piv[p]=(v,mask);break
            w,m=piv[p];v^=w;mask^=m
    def reduce(v):
        mask=0
        for p,(w,m) in sorted(piv.items(),reverse=True):
            if (v>>p)&1:v^=w;mask^=m
        return v,mask
    return piv,reduce
LP,LR=span(L);assert len(LP)==56
def inverse_word(w):return [0 if a==0 else 3-a for a in reversed(w)]
def substitution(M,n=9):
    cols=[1]
    for k in range(n):
        nxt=[]
        for a in range(2):
            for v in cols:nxt.append(tensor(v,M[a],k))
        cols=nxt
    assert len(cols)==1<<n
    def apply(v):
        out=0
        while v:
            bit=v&-v;j=bit.bit_length()-1;v^=bit;out^=cols[j]
        return out
    return apply
results=[];certs=[]
for record in D['graphs']:
    name=record['name'];G=[tuple(q) for q in B[name+'_quotient_states']];ix={q:i for i,q in enumerate(G)}
    if name=='sphere':
        mul=lambda a,b:tuple(a[b[i]] for i in range(3));e=(0,1,2);s=(1,0,2);r=(1,2,0)
    else:
        mul=lambda a,b:((a[0]+b[0])%2,(a[1]+b[1])%3);e=(0,0);s=(1,0);r=(0,1)
    rr=mul(r,r);ch={j:i for i,j in enumerate(B[name+'_cycle_chords'])}
    basis=B['sphere_F_basis_B_words' if name=='sphere' else 'elliptic_Bprime_basis_B_words']
    def ab(w):
        q=e;v=0
        for a in w:
            if a==0:q=mul(q,s)
            else:
                h=mul(q,r if a==1 else rr)
                if ix[q] in ch:v^=1<<ch[ix[q]]
                if ix[h] in ch:v^=1<<ch[ix[h]]
                q=h
        assert q==e
        return v
    Ms=[ab([0]+w+[0]) for w in basis]
    Mr=[ab([1]+w+[2]) for w in basis]
    acts=substitution(Ms);actr=substitution(Mr)
    assert all(acts(acts(v))==v and actr(actr(actr(v)))==v for v in L)
    cols=[v^acts(v) for v in L]+[acts(v^actr(v)) for v in L]
    piv,reduce=span(cols)
    target=int(record['relative_cusp_defect_polynomials'][ix[e]][9],16)
    assert LR(target)[0]==0
    remainder,solution=reduce(target)
    functional=None
    if remainder:
        j=remainder.bit_length()-1;functional=1<<j
        for p,(v,mask) in sorted(piv.items()):
            if (functional&v).bit_count()%2:functional^=1<<p
        assert (functional&target).bit_count()%2==1
        assert all((functional&v).bit_count()%2==0 for v in cols)
    beta_mask=solution&((1<<56)-1);A_mask=solution>>56
    result={'graph':name,'central_layer_dimension':56,'correction_columns':112,
            'full_central_correction_rank':len(piv),'target_is_degree9_Lie_element':True,
            'recorded_conjugator_pair_has_a_central_lift':not bool(remainder),
            'obstruction_nonzero':bool(remainder),
            'annihilating_functional_checked_on_all_columns':bool(remainder),
            'identity_cusp_target':hex(target),
            'reduced_obstruction':hex(remainder)}
    results.append(result)
    certs.append({'name':name,'s_H1_columns':Ms,'r_H1_columns':Mr,
                  'target':hex(target),'correction_columns':[hex(v) for v in cols],
                  'annihilating_functional':None if functional is None else hex(functional),
                  'beta_correction_mask':None if remainder else hex(beta_mask),
                  'A_correction_mask':None if remainder else hex(A_mask)})
summary={'results':results,
         'scope':'Exhaustive corrections in D9/D10 with the recorded conjugator images fixed moduloD9. Lower centralizer changes and full D39 homology compatibility are not inferred from this central test.',
         'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_rank2_degree9.json').write_text(json.dumps({'summary':summary,'Lyndon_words':[list(w) for w in words],
    'Lie_basis_polynomials':[hex(v) for v in L],'certificates':certs},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
