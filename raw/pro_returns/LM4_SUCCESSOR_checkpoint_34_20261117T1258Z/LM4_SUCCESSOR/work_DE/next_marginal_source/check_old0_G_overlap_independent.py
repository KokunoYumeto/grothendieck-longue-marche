#!/usr/bin/env python3
"""Independent exact two-summand retained-deck overlap.

All128 two-chains are checked from their actual F21 word boundaries.
The four coincident incidence rows are then eliminated using literal
free-word conjugators, not an augmented-equality assumption. All124
surviving columns have distinct augmentation units. No iteration occurs.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/'symmetric_paired_fox_data.json',ROOT/'work_A/intrinsic_old0_128_columns.json',
       ROOT/'work_A/old_zero_node_orbit_identities.json',
       P/'symmetric_retained_deck_module.json',P/'symmetric_full_source_data.json',
       ROOT/'records/old0_retained_incidence18.json']
raw=[p.read_bytes() for p in paths]
D,C,W,G,S,incidence=map(json.loads,raw)
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
beta=mp(D['retained_involution'])
old=D['retained_paired_indices'];oldidx={j:i+1 for i,j in enumerate(old)}
meta={int(k):(tuple(v['retained_word']),v['paired_slot']) for k,v in C['common_R_basis'].items()}
def rr(w):
    out=[]
    for a in w:
        if out and out[-1]==(-a[0],a[1],a[2]):out.pop()
        else:out.append(a)
    return tuple(out)
def ri(w):return tuple((-s,h,j) for s,h,j in reversed(w))
def rw(w,md=meta):return rr((1 if x>0 else -1,*md[abs(x)]) for x in w)
def act(t,w):return rr((s,red(t+h),j) for s,h,j in w)
def b(t):return sub(t,beta)
def gm(a,c):
    u,v,t=a;x,y,s=c
    return rr(u+act(t,x)),rr(v+act(b(t),y)),red(t+s)
def gf(a):return a[1],a[0],b(a[2])
def gi(a):
    u,v,t=a;s=inv(t)
    return act(s,ri(u)),act(b(s),ri(v)),s
ONE=((),(),())

# Literal Reidemeister--Schreier rewriting in canonical peripheral names.
def kernel_word(w):
    head=();out=[]
    for x in w:
        j=abs(x);sgn=1 if x>0 else -1
        if j in oldidx:head=red(head+(sgn*oldidx[j],))
        else:
            side=0 if j<12 else 1
            out.append((side,(sgn,head if side==0 else b(head),j if side==0 else j-10)))
    assert not head
    return out
def filled(w):return red((1 if x>0 else -1)*oldidx[abs(x)] for x in w if abs(x) in oldidx)
def liftold(t):return tuple((1 if x>0 else -1)*old[abs(x)-1] for x in t)
def project_kernel(w,side):return rr(a for s,a in kernel_word(w) if s==side)
def quotient(w):
    t=filled(w);n=red(tuple(w)+inv(liftold(t)))
    return project_kernel(n,0),project_kernel(n,1),t
def cellchain(rows):
    out=defaultdict(int)
    for x in rows:
        add(out,(rw(x['A_vertex']),rw(x['B_vertex']),meta[x['A_generator']],meta[x['B_generator']]),x['coefficient'])
    return dict(out)
def boundary(c):
    out=defaultdict(int)
    for (a,d,i,j),n in c.items():
        ai=rr(a+((1,*i),));dj=rr(d+((1,*j),))
        add(out,(0,a,d,i),n);add(out,(0,a,dj,i),-n)
        add(out,(1,ai,d,j),n);add(out,(1,a,d,j),-n)
    return dict(out)
def edgecycle(w):
    pos=[(),()];out=defaultdict(int)
    for side,a in kernel_word(w):
        nxt=rr(pos[side]+(a,));start=list(pos)
        if a[0]<0:start[side]=nxt
        add(out,(side,start[0],start[1],a[1:]),a[0]);pos[side]=nxt
    assert pos==[(),()]
    return dict(out)
def normalize(c):
    out=defaultdict(int)
    for (u,v,(g,i),(h,j)),n in c.items():
        add(out,((i,j,red(inv(b(g))+h)),(u,v,g)),n)
    return dict(out)
def augment(c):
    out=defaultdict(int)
    for (row,a),n in c.items():add(out,(row,a[2]),n)
    return dict(out)
def shift(c,a,sgn=1):
    out=defaultdict(int)
    for (row,d),n in c.items():add(out,(row,gm(a,d)),sgn*n)
    return dict(out)
def Fc(c):
    out=defaultdict(int)
    for ((i,j,z),a),n in c.items():
        add(out,((j,i,inv(b(z))),gm(gf(a),((),(),z))),-n)
    return dict(out)

A=mp(D['old_actions'][0]['geometric_push_paired'])
Ai=mp(D['old_actions'][0]['based_pullback_paired'])
F=mp(D['paired_involution'])
source0=next(x for x in S['old_source_generators'] if x['name']=='old_0')
assert not source0['h_paired'] and A==mp(source0['source_push_F21'])
for j in range(1,22):
    assert sub(A[j],Ai)==sub(Ai[j],A)==(j,)
    assert sub(A[j],F)==sub(F[j],A)

keys=[(x['loop_index'],x['local_node_index']) for x in D['node_columns']]
cols=[];augs=[]
assert len(C['node_columns'])==128
for i,col in enumerate(C['node_columns']):
    layer,j=divmod(i,64);original=tuple(D['node_columns'][j]['paired_relator'])
    word=original if not layer else sub(original,A)
    assert word==tuple(col['paired_relator'])
    chain=cellchain(col['fox_cells'])
    assert boundary(chain)==edgecycle(word)
    assert cellchain(col['F_fox_cells'])=={(v,u,bh,ah):-n for (u,v,ah,bh),n in chain.items()}
    norm=normalize(chain);cols.append(norm)
    aug=augment(norm);assert len(aug)==1
    (row,t),sign=next(iter(aug.items()));assert sign in(-1,1)
    augs.append((row,t,sign))

collisions=[];rows0={r:i for i,(r,t,s) in enumerate(augs[:64])}
assert len(rows0)==64
for j,(r,t,s) in enumerate(augs[64:]):
    if r in rows0:
        k=rows0[r];assert k==j
        collisions.append(keys[j])
assert set(collisions)=={(6,2),(6,3),(6,4),(6,7)}
declinc={tuple(x['node_index']):x for x in incidence['rows']}
for j,k in enumerate(keys):
    decl=declinc[k];r,t,s=augs[j];r2,t2,s2=augs[j+64]
    assert decl['same_retained_deck_incidence_orbit']==(r==r2)
    assert r==(decl['seed_row'][0],decl['seed_row'][1],tuple(decl['seed_row'][2]))
    assert r2==(decl['old0_row'][0],decl['old0_row'][1],tuple(decl['old0_row'][2]))

wordwitness={(x['loop_index'],x['local_node_index']):x for x in W['rows']}
relations=[]
for key in collisions:
    i=keys.index(key);wit=wordwitness[key];h=tuple(wit['exact_conjugator'])
    r=tuple(D['node_columns'][i]['paired_relator'])
    assert sub(r,A)==red(h+r+inv(h))
    a=quotient(h)
    assert cols[i+64]==shift(cols[i],a)
    assert gm(a,gi(a))==gm(gi(a),a)==ONE
    assert a[2]==tuple(declinc[key]['required_retained_deck_translate'])
    relations.append({'node':key,'raw_column':i,'conjugator_F21':h,
                      'retained_unit_head':a[2],'A_coefficient_length':len(a[0]),
                      'B_coefficient_length':len(a[1]),'literal_full_G_relation_checked':True})

keep=list(range(64))+[64+j for j,k in enumerate(keys) if k not in collisions]
assert len(keep)==124
selected=[augs[j][0] for j in keep]
assert len(set(selected))==124
rowindex={r:i for i,r in enumerate(selected)}
matrix=defaultdict(int)
for jj,j in enumerate(keep):
    for (r,a),n in cols[j].items():
        if r in rowindex:add(matrix,(rowindex[r],jj,a[2]),n)
assert dict(matrix)=={(i,i,augs[j][1]):augs[j][2] for i,j in enumerate(keep)}

# Exact F action on the four original basis elements of the intersection.
gmeta={int(k):(tuple(v['retained_word']),v['paired_slot']) for k,v in G['common_R_basis'].items()}
frels={tuple(x['node_index']):x for x in G['all64_G_relations']}
frows=[]
for key in collisions:
    r=frels[key];mate=tuple(r['mate_index']);assert mate in collisions and mate!=key
    a0=r['G_coefficient'];a=(rw(a0['A_word'],gmeta),rw(a0['B_word'],gmeta),tuple(a0['retained_word']))
    assert Fc(cols[keys.index(key)])==shift(cols[keys.index(mate)],a,-r['delta'])
    frows.append({'node':key,'mate':mate,'delta':r['delta'],'full_F_identity':True})
assert {frozenset((tuple(x['node']),tuple(x['mate']))) for x in frows}=={
    frozenset(((6,2),(6,4))),frozenset(((6,3),(6,7)))}

out={'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'source_old0_is_actual':True,'source_old0_commutes_with_F_on_all21':True,
     'full_chain_boundaries':128,'collisions':relations,'surviving_columns':124,
     'selected_augmentation_minor':'diagonal124x124 with genuine signed retained units',
     'intersection_F_action':frows,
     'claims_excluded':['old0 invariance','higher old0 iterates','other old-base translates','global kappa vanishing'],
     'elapsed_seconds':time.monotonic()-started}
(HERE/'old0_G_overlap_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:actual old0 source action,42 inverse substitutions,21 literal F commutations.')
print('PASS:all128 actual F21 word boundaries and full negative-swap chains.')
print('PASS:exactly four augmented collisions, all resolved by literal F21 conjugators and full G chain identities.')
print('PASS:remaining124 columns have a diagonal124x124 augmented-unit minor.')
print('PASS:the rank4 intersection basis has two exchanged F orbits; no iteration or invariance inferred.')
print('Elapsed seconds',round(out['elapsed_seconds'],3))
