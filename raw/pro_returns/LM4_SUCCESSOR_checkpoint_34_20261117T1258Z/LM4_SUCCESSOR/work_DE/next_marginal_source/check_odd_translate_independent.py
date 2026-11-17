#!/usr/bin/env python3
"""Independent actual odd-translate cone/source audit, both directions.

The eight integral chains are checked by full product-tree boundaries;
the sixteen cone tests and actual F13 source words are evaluated directly.
No producer is imported and no overlap/global claim is made.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent
P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/x for x in ['symmetric_paired_fox_data.json','symmetric_F_node_matching.json',
                     'symmetric_full_source_data.json','symmetric_odd_old_translate.json']]
raw=[x.read_bytes() for x in paths];D,M,S,O=map(json.loads,raw)
started=time.monotonic()
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(int(x))
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
def mp(d):return {int(k):tuple(v) for k,v in d.items()}
def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]
F=mp(D['paired_involution']);beta=mp(D['retained_involution'])
old=D['retained_paired_indices'];hm={j:i+1 for i,j in enumerate(old)}
meta={int(k):(tuple(v['retained_word']),v['paired_slot']) for k,v in O['common_R_basis'].items()}
def rr(w):
    out=[]
    for a in w:
        if out and out[-1]==(-a[0],a[1],a[2]):out.pop()
        else:out.append(a)
    return tuple(out)
def ri(w):return tuple((-s,h,j) for s,h,j in reversed(w))
def rw(w):return rr((1 if x>0 else -1,*meta[abs(x)]) for x in w)
def schreier(w):
    h=();out=[]
    for x in w:
        j=abs(x);sgn=1 if x>0 else -1
        if j in hm:h=red(h+(sgn*hm[j],))
        else:
            side=0 if j<12 else 1
            out.append((side,(sgn,h if side==0 else sub(h,beta),j if side==0 else j-10)))
    assert not h
    return out
def edges(w):
    pos=[(),()];out=defaultdict(int)
    for side,a in schreier(w):
        nxt=rr(pos[side]+(a,));at=list(pos)
        if a[0]<0:at[side]=nxt
        add(out,(side,at[0],at[1],a[1:]),a[0]);pos[side]=nxt
    assert pos==[(),()]
    return dict(out)
def cells(rows):
    out=defaultdict(int)
    for x in rows:add(out,(rw(x['A_vertex']),rw(x['B_vertex']),meta[x['A_generator']],meta[x['B_generator']]),x['coefficient'])
    return dict(out)
def boundary(c):
    out=defaultdict(int)
    for (a,b,i,j),n in c.items():
        add(out,(0,a,b,i),n);add(out,(0,a,rr(b+((1,*j),)),i),-n)
        add(out,(1,rr(a+((1,*i),)),b,j),n);add(out,(1,a,b,j),-n)
    return dict(out)
def diag(c):
    out=defaultdict(int)
    for (a,b,i,j),n in c.items():
        if a==b and i==j:
            add(out,rr(a+((1,*i),)),n);add(out,a,-n)
    return {w:n%2 for w,n in out.items() if n%2}

TAU,TAU1=101,102
def il(x):return x if x in (TAU,TAU1) else -x
def er(w):
    out=[]
    for x in w:
        if out and out[-1]==il(x):out.pop()
        else:out.append(x)
    return tuple(out)
def ei(w):return tuple(il(x) for x in reversed(w))
def emb(w):
    out=[]
    for x in w:
        i=abs(x);p=(TAU1,TAU) if i==1 else (i,) if i<=11 else (TAU,i-10,TAU)
        out.extend(p if x>0 else ei(p))
    return er(out)
def even_to_fiber(w):
    par=0;out=[]
    for x in w:
        if x==TAU:par^=1
        elif x==TAU1:out.append(1 if par==0 else -1);par^=1
        else:out.append((1 if x>0 else -1)*(abs(x)+(10 if par else 0)))
    assert par==0
    return red(out)
for j in range(1,22):assert er((TAU,)+emb((j,))+(TAU,))==emb(F[j])

nodes={(r['loop_index'],r['local_node_index']):r for r in D['node_columns']}
matches={tuple(r['node_index']):r for r in M['rows']}
As={'positive_push':mp(D['old_actions'][1]['geometric_push_paired']),
    'canonical_second_sheet_pullback':mp(D['old_actions'][1]['based_pullback_paired'])}
for j in range(1,22):
    assert sub(As['positive_push'][j],As['canonical_second_sheet_pullback'])==(j,)
    assert sub(As['canonical_second_sheet_pullback'][j],As['positive_push'])==(j,)
kept=S['first_family_F13_kept_paired_indices'];unfill={i+1:(j,) for i,j in enumerate(kept)}
branch=next(x for x in S['old_source_generators'] if x['name']=='branch_square')
branchmaps={0:None,1:mp(branch['source_push_F13']),-1:mp(branch['source_pullback_F13'])}
seeds={x['critical_index']:x for x in S['source_peripheral_generators'] if x['sheet']==1}
checked=[];ks={}
for row in O['rows']:
    direction=row['direction'];A=As[direction];key=tuple(row['node_index']);match=matches[key]
    g=tuple(row['translated_matching_conjugator_F21'])
    k=red(g+inv(sub(match['conjugator_F21'],A)))
    if direction in ks:assert ks[direction]==k
    else:
        ks[direction]=k
        for j in range(1,22):assert sub(A[j],F)==red(k+sub(F[j],A)+inv(k))
    assert not red(sub(g,F)+g)
    t=red((1 if x>0 else -1)*hm[abs(x)] for x in g if abs(x) in hm)
    assert t==tuple(row['retained_cocycle'])
    ew=er((TAU,)+emb(g));assert er(ew+ew)==()
    prefix=[];core=ew
    while len(core)>1 and core[0]==il(core[-1]):prefix.append(core[0]);core=core[1:-1]
    assert core==tuple(row['cone_core']) and core in ((TAU,),(TAU1,))
    neutral=core==(TAU,)
    assert neutral==row['neutral']==(key[1]==0)
    if not neutral:
        assert tuple(prefix)==tuple(row['free_product_prefix'])
        checked.append({'direction':direction,'node':key,'cone':core,'neutral':False})
        continue
    if sum(x in (TAU,TAU1) for x in prefix)%2:prefix=list(er(tuple(prefix)+(TAU,)))
    h=even_to_fiber(prefix)
    assert h==tuple(row['free_product_half_h_F21'])
    assert red(sub(h,F)+inv(h))==g and inv(h)==tuple(row['coefficient_half_word_F21'])
    r=tuple(nodes[key]['paired_relator'])
    if match['A_first_orientation_signs'][0]<0:r=inv(r)
    translated=sub(r,A)
    assert translated==tuple(row['translated_A_first_relator'])
    assert sub(translated,F)==red(g+inv(translated)+inv(g))
    anti=red(inv(h)+translated+h)
    assert anti==tuple(row['actual_integral_anti_word']) and sub(anti,F)==inv(anti)
    c=cells(row['actual_integral_anti_chain']);assert boundary(c)==edges(anti)
    assert c=={(v,u,j,i):n for (u,v,i,j),n in c.items()}
    psi=diag(c);assert len(psi)==2
    assert psi=={rw(x['word']):x['coefficient_F2'] for x in row['Tate_diagonal']}
    expected_branch=1 if direction=='positive_push' else 0
    witnesses=row['actual_source_zero_witnesses'];assert witnesses
    for w in witnesses:
        assert w['sheet']==1 and w['critical_index']==key[0]
        assert w['source_branch_square_power']==expected_branch
        source13=tuple(seeds[key[0]]['positive_source_word_F13'])
        if expected_branch:source13=sub(source13,branchmaps[expected_branch])
        source21=sub(source13,unfill);kw=schreier(source21)
        assert not rr(a for side,a in kw if side==1)
        rho=rr(a for side,a in kw if side==0)
        assert rho==rw(w['R_word'])
        if w['power']<0:rho=ri(rho)
        a=rw(w['left_coefficient_R'])
        assert set(psi)=={a,rr(a+rho)}
    checked.append({'direction':direction,'node':key,'cone':core,'neutral':True,
                    'anti_word_length':len(anti),'chain_terms':len(c),
                    'source_branch_square_power':expected_branch,'exact_source_witnesses':len(witnesses)})
assert len(checked)==16 and sum(x['neutral'] for x in checked)==8
assert ks['canonical_second_sheet_pullback']==sub(inv(ks['positive_push']),As['canonical_second_sheet_pullback'])
out={'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'checks':checked,'both_actual_directions':True,'full_basis_discrepancy_checks':42,
     'scope':'individual odd translates only; no intersections, higher orbit sum, full kappa, or source equality',
     'elapsed_seconds':time.monotonic()-started}
(HERE/'odd_translate_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:both actual odd directions and42 full-basis F-discrepancy equations.')
print('PASS:all16 cone normal forms;four neutral andfour opposite-cone cells in each direction.')
print('PASS:eight full integral anti-chain boundaries,negative swaps,and exact two-term diagonals.')
print('PASS:canonical pullback gives actual second-sheet source words;positive push gives their actual branch-square source images.')
print('Scope:individual translates only;no overlap or global orbit conclusion.')
print('Elapsed seconds',round(out['elapsed_seconds'],3))
