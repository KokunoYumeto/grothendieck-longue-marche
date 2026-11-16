#!/usr/bin/env python3
"""Unique actual source-lasso corrections in C2*C2*F10.

The paired F21 involution inverts its axis and swaps ten generator pairs.
Write tau1=x_axis*tau.  For each nodal loop the exact inner discrepancy
k satisfies F*alpha*F*alpha^-1=Inn(k), and tau*k=h*tau*h^-1 is solved by
free-product normal form.  The orientation-even h is unique.  If alpha
is geometric push, alpha_g(x)=g^-1*x*g; consequently h=g_far^-1*g_source.
After the far nodal lasso is filled, h is the actual positive source loop.
No nonfixed-node h is declared trivial in the free F21.
"""
from pathlib import Path
from collections import Counter
import json, hashlib, time
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
names=['symmetric_node_words_pullback_corrected.json',
       'symmetric_corrected_words_independent.json','symmetric_paired_fox_data.json']
raw={n:(P/n).read_bytes() for n in names};nodes,checks,paired=[json.loads(raw[n]) for n in names]
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
def mp(d):return {int(i):tuple(w) for i,w in d.items()}
F=mp(paired['paired_involution']);to_pair=mp(paired['nodal_cut_basis_in_paired_basis'])
to_cut=mp(paired['paired_basis_forward_in_nodal_cut_basis'])
TAU,TAU1=101,102
def einv_letter(x):return x if x in (TAU,TAU1) else -x
def er(w):
    out=[]
    for x in w:
        assert x in (TAU,TAU1) or 2<=abs(x)<=11
        if out and out[-1]==einv_letter(x):out.pop()
        else:out.append(x)
    return tuple(out)
def ei(w):return tuple(einv_letter(x) for x in reversed(w))
def eimage(w):
    ans=[]
    for x in w:
        i=abs(x)
        if i==1:v=(TAU1,TAU)
        elif i<=11:v=(i,)
        else:v=(TAU,i-10,TAU)
        ans.extend(v if x>0 else ei(v))
    return er(ans)
def orientation(w):return sum(x in (TAU,TAU1) for x in w)%2
def sch(w):
    parity=0;out=[]
    for x in w:
        if x==TAU:parity^=1
        elif x==TAU1:
            out.append(1 if parity==0 else -1);parity^=1
        else:out.append((1 if x>0 else -1)*(abs(x)+(10 if parity else 0)))
    assert parity==0
    return red(out)
for j in range(1,22):assert sch(eimage((j,)))==(j,)
start=time.monotonic();rows=[]
for row,ck in zip(nodes['loops'],checks['node_checks']):
    assert row['index']==ck['index'];k=sub(ck['F_commutator_inner_word'],to_pair)
    assert red(sub(k,F)+k)==()
    t=er((TAU,)+eimage(k));assert er(t+t)==()
    prefix=[];core=t
    while len(core)>1 and core[0]==einv_letter(core[-1]):
        prefix.append(core[0]);core=core[1:-1]
    assert core==(TAU,),('source fixed branch did not return',row['index'],core)
    g=tuple(prefix)
    if orientation(g):g=er(g+(TAU,))
    assert orientation(g)==0 and er(g+(TAU,)+ei(g))==t
    h=sch(g);assert eimage(h)==g
    assert red(sub(h,F)+inv(h))==k
    hcut=sub(h,to_cut);assert sub(hcut,to_pair)==h
    # The discrepancy-corrected source monodromy commutes with F literally.
    A=mp(row['geometric_push_images'])
    AP={j:sub(sub(to_cut[j],A),to_pair) for j in range(1,22)}
    source={j:red(inv(h)+AP[j]+h) for j in range(1,22)}
    for j in range(1,22):assert sub(source[j],F)==sub(F[j],source)
    ab=Counter()
    for x in hcut:ab[nodes['initial_order'][abs(x)-1]]+=1 if x>0 else -1
    ab={i:n for i,n in sorted(ab.items()) if n}
    fixed=[p for p in row['expected_node_pairs'] if p[0]==p[1]]
    if fixed:
        assert len(fixed)==2 and len(ab)==2 and set(ab.values())=={1},('source orientation',row['index'],ab)
        tags=[nodes['labels'][i] for i in ab]
        assert {x['kind'] for x in tags}=={'A','B'}
        assert tags[0]['branch']==tags[1]['branch'] and tags[0]['index']==tags[1]['index']
    else:
        assert not ab,('non-source local lasso has nonzero peripheral abelianization',row['index'],ab)
    rows.append({'index':row['index'],'critical_key':row['key'],
        'has_fixed_source_nodes':bool(fixed),'physical_fixed_node_count':len(fixed),
        'k_in_paired_basis':k,'h_in_paired_basis':h,'h_in_nodal_cut_basis':hcut,
        'positive_source_peripheral_physical_abelianization':ab,
        'source_monodromy_paired':source,
        'free_product_even_conjugator':g,'free_product_core':core,
        'equations':['k=F(h)*h^-1','alpha_far=Inn(h)*alpha_source','F*alpha_source=alpha_source*F'],
        'after_critical_filling':'h is the actual positive source lasso; it is trivial if the source section extends across this critical value.'})
    print('PASS source lasso',row['index'],'fixed source nodes',len(fixed),'h length',len(h),'physical abelianization',ab,flush=True)
out={'scope':__doc__,'input_sha256':{n:hashlib.sha256(r).hexdigest() for n,r in raw.items()},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'free_product_encoding':{'tau':TAU,'tau1':TAU1,'axis':'tau1*tau','right_pair_generators':'2..11'},
 'based_loop_convention':'geometric push alpha_g(x)=g^-1*x*g; g_source=g_far*h',
 'uniqueness':'C_(C2*C2*F10)(tau)=<tau>; its intersection with the orientation kernel F21 is1',
 'loops':rows,'elapsed_seconds':time.monotonic()-start,
 'claims_excluded':['h=1 in freeF21 at non-source nodes','full source generation after old-base translates','nonlinear fixed lifting']}
(P/'symmetric_source_lasso_corrections.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS unique positive source-lasso corrections for all18 nodal values; elapsed',round(out['elapsed_seconds'],3),flush=True)
