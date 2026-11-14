#!/usr/bin/env python3
"""Exhaust all same-lower-action s-centralizer freedom at rank two, degree9.

The centralizer is lifted through all eight actual Zassenhaus layers.
At every stage the resulting subgroup is proved elementary by its exact
Magnus depths, and its complete order follows from the central-extension
connecting map.  Actual reduced free words certify every generator.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
import json,time

OUT=Path(__file__).resolve().parent;started=time.time();DEG=9
B=json.loads((OUT/'d_cm_solvable_even_boundary.json').read_text())
T=json.loads((OUT/'d_cm_rank2_boundary_test.json').read_text())
J=json.loads((OUT/'d_cm_rank2_degree9.json').read_text())
ONE=(1,)+(0,)*DEG
def tensor(a,b,d):
    out=0
    while b:
        bit=b&-b;j=bit.bit_length()-1;b^=bit;out^=a<<(j<<d)
    return out
def pmul(a,b):
    c=[a[0]&b[0]]+[ (b[d] if a[0] else 0)^(a[d] if b[0] else 0) for d in range(1,DEG+1)]
    for d in range(2,DEG+1):
        for i in range(1,d):
            if a[i] and b[d-i]:c[d]^=tensor(a[i],b[d-i],i)
    return tuple(c)
def pinv(a):
    b=[1]+[0]*DEG
    for d in range(1,DEG+1):
        z=a[d]
        for i in range(1,d):
            if a[i] and b[d-i]:z^=tensor(a[i],b[d-i],i)
        b[d]=z
    return tuple(b)
def free_reduce(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return tuple(out)
def wi(w):return tuple(-a for a in reversed(w))
def wc(a,b):return free_reduce(a+b+wi(a)+wi(b))
def eval_free(w):
    v=[1]+[0]*DEG
    for a in w:
        i=abs(a)-1
        for d in (range(DEG,0,-1) if a>0 else range(1,DEG+1)):
            v[d]^=v[d-1]<<(i*(1<<(d-1)))
    return tuple(v)
def lyndon(w):return all(w<w[k:]+w[:k] for k in range(1,len(w)))
@lru_cache(None)
def lw(w):
    if len(w)==1:return (w[0]+1,)
    k=next(k for k in range(1,len(w)) if lyndon(w[k:]))
    return wc(lw(w[:k]),lw(w[k:]))
layers={}
for n in range(1,10):
    layer=[];power=1
    while n%power==0:
        d=n//power
        for w in product(range(2),repeat=d):
            if lyndon(w):
                ww=free_reduce(lw(w)*power);p=eval_free(ww)
                assert not any(p[1:n]) and p[n]
                layer.append((p,ww))
        power*=2
    layers[n]=layer
assert [len(layers[n]) for n in range(1,10)]==[2,3,2,6,6,11,18,36,56]
def span(cols):
    piv={};null=[]
    for j,v in enumerate(cols):
        mask=1<<j
        while v:
            p=v.bit_length()-1
            if p not in piv:piv[p]=(v,mask);break
            z,m=piv[p];v^=z;mask^=m
        if not v:null.append(mask)
    def reduce(v):
        mask=0
        for p,(z,m) in sorted(piv.items(),reverse=True):
            if (v>>p)&1:v^=z;mask^=m
        return v,mask
    return piv,reduce,null
def select(mask,gs):
    p=ONE;w=()
    while mask:
        bit=mask&-mask;j=bit.bit_length()-1;mask^=bit
        p=pmul(p,gs[j][0]);w=free_reduce(w+gs[j][1])
    return p,w
def b_inverse(w):return [0 if a==0 else 3-a for a in reversed(w)]
outputs=[];certs=[]
for record,oldcentral in zip(T['graphs'],J['certificates']):
    name=record['name'];G=[tuple(q) for q in B[name+'_quotient_states']];ix={q:i for i,q in enumerate(G)}
    if name=='sphere':
        mul=lambda a,b:tuple(a[b[i]] for i in range(3));e=(0,1,2);s=(1,0,2);r=(1,2,0)
    else:
        mul=lambda a,b:((a[0]+b[0])%2,(a[1]+b[1])%3);e=(0,0);s=(1,0);r=(0,1)
    rr=mul(r,r);ch={j:i for i,j in enumerate(B[name+'_cycle_chords'])}
    basis=B['sphere_F_basis_B_words' if name=='sphere' else 'elliptic_Bprime_basis_B_words']
    def collapse(w):
        q=e;out=[]
        for a in w:
            if a==0:q=mul(q,s)
            else:
                h=mul(q,r if a==1 else rr)
                if ix[q] in ch:out.append(ch[ix[q]]+1)
                if ix[h] in ch:out.append(-ch[ix[h]]-1)
                q=h
        return q,free_reduce(out)
    simages=[]
    for w in basis:
        q,v=collapse([0]+w+[0]);assert q==e;simages.append(v)
    sx=[eval_free(w) for w in simages]
    X=[tuple([0]+list(p[1:])) for p in sx]
    mon={():ONE}
    for n in range(1,10):
        for w in product(range(2),repeat=n):mon[w]=pmul(mon[w[:-1]],X[w[-1]])
    mcode={n:[mon[tuple((j>>k)&1 for k in range(n))] for j in range(1<<n)] for n in range(1,10)}
    def phi(p):
        out=[p[0]]+[0]*DEG
        for n in range(1,10):
            v=p[n]
            while v:
                bit=v&-v;j=bit.bit_length()-1;v^=bit
                for d in range(n,10):out[d]^=mcode[n][j][d]
        return tuple(out)
    assert all(phi(phi(eval_free((j+1,))))==eval_free((j+1,)) for j in range(2))
    centralizer=[];history=[];recipes=[]
    for n in range(1,9):
        layer=layers[n]
        scol=[p[n]^phi(p)[n] for p,w in layer]
        sp,sred,snull=span(scol)
        defects=[]
        for p,w in centralizer:
            delta=pmul(phi(p),pinv(p));assert not any(delta[1:n])
            defects.append(sred(delta[n])[0])
        dp,dred,dnull=span(defects)
        new=[];rec=[]
        for mask in dnull:
            p,w=select(mask,centralizer);delta=pmul(phi(p),pinv(p))
            rem,cmask=sred(delta[n]);assert rem==0
            z,zw=select(cmask,layer);pp=pmul(z,p);ww=free_reduce(zw+w)
            assert eval_free(ww)==pp
            assert not any(pmul(phi(pp),pinv(pp))[1:n+1])
            new.append((pp,ww));rec.append({'old_mask':hex(mask),'layer_correction':hex(cmask)})
        for mask in snull:
            p,w=select(mask,layer)
            assert not any(pmul(phi(p),pinv(p))[1:n+1])
            new.append((p,w));rec.append({'new_fixed_layer_mask':hex(mask)})
        depths=[next(d for d in range(1,10) if p[d]) for p,w in new]
        assert all(2*d>=n+1 for d in depths)
        trunc=[sum(p[d]<<((1<<d)-2) for d in range(1,n+1)) for p,w in new]
        assert len(span(trunc)[0])==len(new)
        for p,w in new:assert not any(pmul(p,p)[1:n+1])
        # The depth bound makes all products additive and all commutators
        # zero in the complete quotient, not merely on leading terms.
        history.append({'quotient':'F/D'+str(n+1),'layer_dimension':len(layer),
                        'one_minus_s_rank':len(sp),'previous_centralizer_rank':len(centralizer),
                        'connecting_rank':len(dp),'new_centralizer_rank':len(new),
                        'minimum_depth':min(depths) if depths else None,
                        'complete_centralizer_is_elementary_abelian':True})
        recipes.append(rec);centralizer=new
    extra=[]
    for p,w in centralizer:
        assert eval_free(w)==p
        delta=pmul(phi(p),pinv(p));assert not any(delta[1:9]);extra.append(delta[9])
    oldcols=[int(v,16) for v in oldcentral['correction_columns']]
    cols=oldcols+extra;sp,reduce,null=span(cols)
    target=int(oldcentral['target'],16);rem,solution=reduce(target)
    functional=None
    if rem:
        functional=1<<(rem.bit_length()-1)
        for p,(v,m) in sorted(sp.items()):
            if (functional&v).bit_count()%2:functional^=1<<p
        assert (functional&target).bit_count()%2==1
        assert all((functional&v).bit_count()%2==0 for v in cols)
    result={'graph':name,'complete_lower_s_centralizer_rank':len(centralizer),
            'all_lower_centralizer_generators_checked_by_actual_words':True,
            'central_correction_rank':len(span(oldcols)[0]),
            'full_same_action_correction_rank':len(sp),
            'same_lower_action_has_a_degree9_lift':not bool(rem),
            'annihilator_checked_on_all_central_and_centralizer_columns':bool(rem),
            'lower_centralizer_history':history}
    outputs.append(result)
    certs.append({'name':name,'s_free_generator_images':simages,'centralizer_recipes':recipes,
                  'centralizer_free_words':[list(w) for p,w in centralizer],
                  'centralizer_polynomials':[[hex(v) for v in p] for p,w in centralizer],
                  'centralizer_degree9_defects':[hex(v) for v in extra],
                  'full_remainder':hex(rem),'solution_mask':None if rem else hex(solution),
                  'annihilating_functional':None if functional is None else hex(functional)})
summary={'results':outputs,
         'scope':'Exhaustive lower s-centralizer freedom for the recorded rank-two action moduloD9, with conjugators in the same even-abelianization coset. Coprime order3 centralizers add no obstruction beyond the central correction columns. Full D39 homology compatibility remains a separate constraint when a lift survives.',
         'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_rank2_centralizers.json').write_text(json.dumps({'summary':summary,'certificates':certs},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
