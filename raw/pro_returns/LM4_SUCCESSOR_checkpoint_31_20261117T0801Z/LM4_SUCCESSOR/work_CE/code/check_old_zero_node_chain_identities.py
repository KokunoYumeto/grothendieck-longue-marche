#!/usr/bin/env python3
"""Four full old-zero node-chain identities with explicit E coefficients.
The old-base and retained-fiber deck indices remain distinct even when
their columns agree. No nonzero Tate syzygy or kappa value is inferred.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/'symmetric_paired_fox_data.json',ROOT/'work_A/old_zero_node_orbit_identities.json']
raw=[p.read_bytes() for p in paths];D,W=[json.loads(r) for r in raw]
def red(w):
    r=[]
    for x in w:
        if r and r[-1]==-x:r.pop()
        else:r.append(x)
    return tuple(r)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
def mp(d):return {int(i):tuple(w) for i,w in d.items()}
def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]
beta=mp(D['retained_involution']);ret=D['retained_paired_indices'];hm={j:i+1 for i,j in enumerate(ret)}
meta={int(i):dict(r,retained_word=tuple(r['retained_word'])) for i,r in D['finite_used_common_R_basis'].items()}
idx={(r['retained_word'],r['paired_slot']):i for i,r in meta.items()}
def bid(g,i):
    if (g,i) not in idx:
        j=max(meta,default=0)+1;idx[g,i]=j;meta[j]={'retained_word':g,'paired_slot':i}
    return idx[g,i]
def rw(w):
    g=();r=[]
    for x in w:
        i=abs(x);sgn=1 if x>0 else -1
        if i in hm:g=red(g+(sgn*hm[i],))
        else:
            a=i<12;n=bid(g if a else sub(g,beta),i if a else i-10)
            r.append(sgn*(2*n-1 if a else 2*n))
    assert not g
    return red(r)
def isA(x):return abs(x)%2==1
def rid(x):return (abs(x)+1)//2
def proj(w,a):return red((1 if x>0 else -1)*rid(x) for x in w if isA(x)==a)
def chain(w):
    a=b=();out=defaultdict(int)
    for x in w:
        y=(1 if x>0 else -1)*rid(x)
        if isA(x):
            aa=red(a+(y,));av=a if y>0 else aa;bp=()
            for z in b:
                bn=red(bp+(z,));bv=bp if z>0 else bn
                add(out,(av,bv,abs(y),abs(z)),-(1 if y>0 else -1)*(1 if z>0 else -1));bp=bn
            a=aa
        else:b=red(b+(y,))
    assert not a and not b
    return dict(out)
def edge_cycle(w):
    a=b=();out=defaultdict(int)
    for x in w:
        y=(1 if x>0 else -1)*rid(x);sgn=1 if y>0 else -1
        if isA(x):
            aa=red(a+(y,));add(out,('A',a if y>0 else aa,b,abs(y)),sgn);a=aa
        else:
            bb=red(b+(y,));add(out,('B',a,b if y>0 else bb,abs(y)),sgn);b=bb
    assert not a and not b
    return dict(out)
def boundary(c):
    out=defaultdict(int)
    for (a,b,i,j),n in c.items():
        add(out,('A',a,b,i),n);add(out,('A',a,red(b+(j,)),i),-n)
        add(out,('B',red(a+(i,)),b,j),n);add(out,('B',a,b,j),-n)
    return dict(out)
def enc(c):return [{'A_vertex':a,'B_vertex':b,'A_generator':i,'B_generator':j,'coefficient':n} for (a,b,i,j),n in sorted(c.items())]
def dec(c):return {(tuple(x['A_vertex']),tuple(x['B_vertex']),x['A_generator'],x['B_generator']):x['coefficient'] for x in c}
A=mp(D['old_actions'][0]['geometric_push_paired']);fill={i:((hm[i],) if i in hm else ()) for i in range(1,22)}
nodes={(r['loop_index'],r['local_node_index']):r for r in D['node_columns']}
rows=[];started=time.monotonic()
selected=[r for r in W['rows'] if r['conjugate']]
assert {(r['loop_index'],r['local_node_index']) for r in selected}=={(6,2),(6,3),(6,4),(6,7)}
for wit in selected:
    key=(wit['loop_index'],wit['local_node_index']);node=nodes[key]
    r=tuple(node['paired_relator']);lhs=sub(r,A);h=tuple(wit['exact_conjugator'])
    deck=tuple(wit['retained_deck_part']);n=tuple(wit['kernel_part'])
    assert red(n+deck)==h and lhs==red(h+r+inv(h))
    assert not sub(n,fill)
    oldchain=chain(rw(r));assert oldchain==dec(node['fox_cells'])
    dr=red(deck+r+inv(deck));dc=chain(rw(dr));lc=chain(rw(lhs))
    assert boundary(dc)==edge_cycle(rw(dr)) and boundary(lc)==edge_cycle(rw(lhs))
    nk=rw(n);a,b=proj(nk,True),proj(nk,False)
    rhs={(red(a+u),red(b+v),i,j):coef for (u,v,i,j),coef in dc.items()}
    assert lc==rhs
    rows.append({'original_node_index':key,
        'left_Q_translate':{'old_base_operator':'old0 geometric push'},
        'right_Q_translate':{'retained_F5_word':sub(deck,fill)},
        'indices_are_distinct':True,
        'exact_conjugator_F21':h,'kernel_conjugator_F21':n,
        'E_coefficient':{'A_word':a,'B_word':b},
        'old0_column':enc(lc),'retained_deck_column':enc(dc),
        'full_chain_identity':'old0(C_nu)=(A_word,B_word)*C_(retained_deck.nu)',
        'literal_fixed_relator':wit['literal_fixed_word']})
    print('PASS full based word and chain identity',key,'E lengths',len(a),len(b),'deck',sub(deck,fill),'cells',len(lc),flush=True)
out={'scope':__doc__,'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'common_R_basis':meta,'rows':rows,'elapsed_seconds':time.monotonic()-started,
    'syzygy_scope':'These give exact Z2_common kernel relations between distinct Q-indexed common-whisker node columns. Equality of image Lbar alone does not identify this kernel with B92 equivariant-whisker Z2; an actual equivariant generator change or refinement remains pending. No F pairing of the chosen cells, H2 nonzero class, or kappa value is asserted; within the equivariant presentation a formal symmetrization is a norm.',
 'claims_excluded':['augmented-only inference','full syzygy module','source equality']}
(P/'old_zero_node_chain_identities.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all4 exact old0 node-column identities, including retained-deck splitting and independent edge boundaries; elapsed',round(out['elapsed_seconds'],3),flush=True)
