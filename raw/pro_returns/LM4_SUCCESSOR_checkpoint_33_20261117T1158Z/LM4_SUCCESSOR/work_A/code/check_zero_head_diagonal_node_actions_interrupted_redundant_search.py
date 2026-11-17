#!/usr/bin/env python3
"""Bounded exact16 root-generator/fixed-node stabilizer diagnostics.

Reconstructs product-tree2-chains directly from actual F21 words, verifies
all eight starting chains, and compares full G columns. No word-depth
search, syzygy quotient, or nonmembership in the source ideal is inferred.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,json,time
ROOT=Path(__file__).resolve().parents[2]
paths=[ROOT/'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json',
       ROOT/'work_A/old_base_augmented_row_action.json',
       ROOT/'records/old0_retained_incidence18.json']
raw=[p.read_bytes() for p in paths];D,H,I=map(json.loads,raw)
started=time.monotonic()
def red(w):
    a=[]
    for x in w:
        if a and a[-1]==-x:a.pop()
        else:a.append(int(x))
    return tuple(a)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in(A[abs(x)] if x>0 else inv(A[abs(x)])))
def mp(d):return {int(k):tuple(v) for k,v in d.items()}
beta=mp(D['retained_involution']);old=tuple(D['retained_paired_indices']);oi={j:i+1 for i,j in enumerate(old)}
meta={int(k):(tuple(v['retained_word']),v['paired_slot']) for k,v in D['finite_used_common_R_basis'].items()}
def b(w):return sub(w,beta)
def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]
def rr(w):
    a=[]
    for x in w:
        if a and a[-1]==(-x[0],x[1],x[2]):a.pop()
        else:a.append(x)
    return tuple(a)
def ri(w):return tuple((-s,h,i) for s,h,i in reversed(w))
def act(t,w):return rr((s,red(t+h),i) for s,h,i in w)
def gm(a,c):
    u,v,t=a;x,y,s=c
    return rr(u+act(t,x)),rr(v+act(b(t),y)),red(t+s)
def gi(a):
    u,v,t=a;s=inv(t)
    return act(s,ri(u)),act(b(s),ri(v)),s
def kernel(w):
    head=();out=[]
    for x in w:
        j=abs(x);sg=1 if x>0 else -1
        if j in oi:head=red(head+(sg*oi[j],))
        else:
            side=0 if j<12 else 1
            out.append((side,(sg,head if not side else b(head),j if not side else j-10)))
    assert not head
    return out
def fill(w):return red((1 if x>0 else -1)*oi[abs(x)] for x in w if abs(x) in oi)
def quotient(w):
    t=fill(w);lift=tuple((1 if x>0 else -1)*old[abs(x)-1] for x in t)
    kw=kernel(red(w+inv(lift)))
    return rr(a for s,a in kw if s==0),rr(a for s,a in kw if s==1),t
def normcell(c):
    out=defaultdict(int)
    for(u,v,(g,i),(h,j)),n in c.items():
        add(out,((i,j,red(inv(b(g))+h)),(u,v,g)),n)
    return dict(out)
def edgecycle(w):
    pos=[(),()];out=defaultdict(int)
    for side,a in kernel(w):
        nxt=rr(pos[side]+(a,));start=list(pos)
        if a[0]<0:start[side]=nxt
        add(out,(side,start[0],start[1],a[1:]),a[0]);pos[side]=nxt
    assert pos==[(),()]
    return dict(out)
def boundary(c):
    out=defaultdict(int)
    for(a,d,i,j),n in c.items():
        ai=rr(a+((1,*i),));dj=rr(d+((1,*j),))
        add(out,(0,a,d,i),n);add(out,(0,a,dj,i),-n)
        add(out,(1,ai,d,j),n);add(out,(1,a,d,j),-n)
    return dict(out)
def chain(w):
    pos=[(),()];out=defaultdict(int)
    for side,a in kernel(w):
        nxt=rr(pos[side]+(a,))
        if side==0:
            av=pos[0] if a[0]>0 else nxt;bv=()
            for q in pos[1]:
                bn=rr(bv+(q,));bs=bv if q[0]>0 else bn
                add(out,(av,bs,a[1:],q[1:]),-a[0]*q[0]);bv=bn
            assert bv==pos[1]
        pos[side]=nxt
    assert pos==[(),()]
    out=dict(out);assert boundary(out)==edgecycle(w)
    return out
def rw(w):return rr((1 if x>0 else -1,*meta[abs(x)]) for x in w)
def stored(c):
    out=defaultdict(int)
    for x in c:
        add(out,(rw(x['A_vertex']),rw(x['B_vertex']),meta[x['A_generator']],meta[x['B_generator']]),x['coefficient'])
    return dict(out)
def cyc(w):
    w=red(w);p=[]
    while len(w)>1 and w[0]==-w[-1]:p.append(w[0]);w=w[1:-1]
    return tuple(p),w
def conjugacy(a,c):
    pa,ca=cyc(a);pc,cc=cyc(c)
    if len(ca)!=len(cc):return None
    for j in range(len(ca)):
        if ca[j:]+ca[:j]==cc:
            h=red(pc+inv(ca[:j])+inv(pa))
            assert red(h+a+inv(h))==c
            return h
    return None
def shifted(c,a,sign=1):
    out=defaultdict(int)
    for(row,g),n in c.items():add(out,(row,gm(a,g)),sign*n)
    return dict(out)
def monomial(c,d):
    rc={r for r,g in c};rd={r for r,g in d}
    if rc!=rd:
        return None,{'kind':'different_full_row_support','only_original':sorted(rc-rd),'only_transformed':sorted(rd-rc)}
    row=min(rc,key=lambda r:sum(1 for rr,g in d if rr==r))
    g0,n0=next((g,n) for(r,g),n in c.items() if r==row)
    trials=0
    for(r,g),n in d.items():
        if r!=row or abs(n)!=abs(n0):continue
        sg=n//n0;a=gm(g,gi(g0));trials+=1
        if shifted(c,a,sg)==d:return (sg,a),{'kind':'exact_full_G_unit','candidate_trials':trials}
    return None,{'kind':'all_possible_group_units_exhausted','fixed_pivot_row':row,'candidate_trials':trials}
def serialize(c):
    return [{'row':r,'G_coefficient':{'A_word':a[0],'B_word':a[1],'retained_word':a[2]},'integer':n}
            for(r,a),n in sorted(c.items())]

inc={tuple(x['node_index']):x for x in I['rows']}
nodes={ (x['loop_index'],x['local_node_index']):x for x in D['node_columns'] }
fixed=[k for k in nodes if inc[k]['seed_row'][0]==inc[k]['seed_row'][1]]
assert len(fixed)==8
base={}
for k in fixed:
    w=tuple(nodes[k]['paired_relator']);c=chain(w)
    assert c==stored(nodes[k]['fox_cells'])
    z=tuple(inc[k]['seed_row'][2]);assert red(b(z)+z)==()
    base[k]=(w,normcell(c))
rows=[]
for ai in range(2,6):
    op=D['old_actions'][ai];heads=H['old_generators'][ai];A=mp(op['geometric_push_paired'])
    assert mp(op['retained_push'])=={j:(j,) for j in range(1,6)}
    for k in fixed:
        i=inc[k]['seed_row'][0]
        if heads['A_heads'][str(i)] or heads['B_heads'][str(i)]:continue
        w,c=base[k];target=sub(w,A);new=normcell(chain(target))
        h=conjugacy(w,target)
        unit,reason=monomial(c,new)
        if h is not None:
            a=quotient(h);assert shifted(c,a)==new and unit is not None
        aug=defaultdict(int)
        for(r,g),n in new.items():add(aug,(r,g[2]),n)
        oldaug=defaultdict(int)
        for(r,g),n in c.items():add(oldaug,(r,g[2]),n)
        assert dict(aug)==dict(oldaug)
        if unit is not None:assert unit[1][2]==()
        rows.append({'old_name':op['name'],'old_index':ai,'node_index':k,'physical_slot':i,
                     'original_relator_F21':w,'transformed_relator_F21':target,
                     'positive_free_conjugacy':h is not None,'conjugator_F21':h,
                     'full_G_monomial_relation':unit is not None,'unit':unit,'exact_decision':reason,
                     'original_full_G_column':serialize(c),'transformed_full_G_column':serialize(new)})
assert len(rows)==16
out={'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(x).hexdigest() for p,x in zip(paths,raw)},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'original_chain_checks':8,'cases':rows,
     'free_conjugacies':sum(x['positive_free_conjugacy'] for x in rows),
     'full_G_monomial_relations':sum(x['full_G_monomial_relation'] for x in rows),
     'claims_excluded':['all stabilizer words','syzygy cohomology value','nonmembership in source ideal','global kappa'],
     'elapsed_seconds':time.monotonic()-started}
(ROOT/'work_A/zero_head_diagonal_node_actions.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:all8 initial fixed-node chains independently reconstructed and boundary checked.')
print('PASS:all16 zero-head transformed chains independently reconstructed; their augmented rows and units are identical.')
print('Positive free-word conjugacies:',out['free_conjugacies'],'of16.')
print('Exact full-G monomial relations:',out['full_G_monomial_relations'],'of16.')
for x in rows:print(x['old_name'],tuple(x['node_index']),'word_conjugate',x['positive_free_conjugacy'],'G_monomial',x['full_G_monomial_relation'],x['exact_decision']['kind'])
print('Elapsed seconds',round(out['elapsed_seconds'],3))
