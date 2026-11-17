#!/usr/bin/env python3
"""Independent full-support check of the16 specified diagonal cases.

Uses canonical retained-head/slot letters and integrates product chains
at B steps, opposite to the construction producer. No producer import.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent
paths=[ROOT/'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json',
       ROOT/'work_A/zero_head_diagonal_node_actions.json',
       ROOT/'records/old0_retained_incidence18.json']
raw=[p.read_bytes() for p in paths];D,C,I=map(json.loads,raw)
started=time.monotonic()
def red(w):
    a=[]
    for x in w:
        if a and a[-1]==-x:a.pop()
        else:a.append(x)
    return tuple(a)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
def mp(d):return {int(k):tuple(v) for k,v in d.items()}
def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]
beta=mp(D['retained_involution']);old=D['retained_paired_indices'];oi={j:i+1 for i,j in enumerate(old)}
meta={int(k):(tuple(v['retained_word']),v['paired_slot']) for k,v in D['finite_used_common_R_basis'].items()}
def rr(w):
    a=[]
    for x in w:
        if a and a[-1]==(-x[0],x[1],x[2]):a.pop()
        else:a.append(x)
    return tuple(a)
def rw(w):return rr((1 if x>0 else -1,*meta[abs(x)]) for x in w)
def fill(w):return red((1 if x>0 else -1)*oi[abs(x)] for x in w if abs(x) in oi)
def kw(w):
    h=();a=[]
    for x in w:
        j=abs(x);s=1 if x>0 else -1
        if j in oi:h=red(h+(s*oi[j],))
        else:
            side=0 if j<12 else 1
            a.append((side,(s,h if not side else sub(h,beta),j if not side else j-10)))
    assert not h
    return a
def boundary(c):
    out=defaultdict(int)
    for (a,b,i,j),n in c.items():
        add(out,(0,a,b,i),n);add(out,(0,a,rr(b+((1,*j),)),i),-n)
        add(out,(1,rr(a+((1,*i),)),b,j),n);add(out,(1,a,b,j),-n)
    return dict(out)
def edges(w):
    pos=[(),()];out=defaultdict(int)
    for side,x in kw(w):
        nxt=rr(pos[side]+(x,));at=list(pos)
        if x[0]<0:at[side]=nxt
        add(out,(side,at[0],at[1],x[1:]),x[0]);pos[side]=nxt
    assert pos==[(),()]
    return dict(out)
def chainB(w):
    pos=[(),()];out=defaultdict(int)
    for side,x in kw(w):
        nxt=rr(pos[side]+(x,))
        if side==1:
            bv=pos[1] if x[0]>0 else nxt;ap=()
            for y in pos[0]:
                an=rr(ap+(y,));av=ap if y[0]>0 else an
                add(out,(av,bv,y[1:],x[1:]),y[0]*x[0]);ap=an
            assert ap==pos[0]
        pos[side]=nxt
    assert pos==[(),()]
    out=dict(out);assert boundary(out)==edges(w)
    return out
def normalize(c):
    out=defaultdict(int)
    for (u,v,(g,i),(h,j)),n in c.items():
        add(out,((i,j,red(inv(sub(g,beta))+h)),(u,v,g)),n)
    return dict(out)
def aug(c):
    out=defaultdict(int)
    for (r,a),n in c.items():add(out,(r,a[2]),n)
    return dict(out)
def peel(w):
    p=[];w=tuple(w)
    while len(w)>1 and w[0]==-w[-1]:p.append(w[0]);w=w[1:-1]
    return tuple(p),w
def conjugate(u,v):
    _,a=peel(u);_,b=peel(v)
    if len(a)!=len(b):return False
    return any(a[j:]+a[:j]==b for j in range(len(a)))

nodes={(x['loop_index'],x['local_node_index']):x for x in D['node_columns']}
inc={tuple(x['node_index']):x for x in I['rows']}
fixed=[k for k in nodes if inc[k]['seed_row'][0]==inc[k]['seed_row'][1]]
assert len(fixed)==8
base={}
for key in fixed:
    node=nodes[key];r=tuple(node['paired_relator']);c=chainB(r)
    stored={(rw(x['A_vertex']),rw(x['B_vertex']),meta[x['A_generator']],meta[x['B_generator']]):x['coefficient'] for x in node['fox_cells']}
    assert c==stored;base[key]=(r,normalize(c))
expected=[]
for ai in range(2,6):
    A=mp(D['old_actions'][ai]['geometric_push_paired'])
    assert all(fill(A[j])==(oi[j],) for j in old)
    for key in fixed:
        slot=inc[key]['seed_row'][0]
        p,a=peel(A[slot]);q,b=peel(A[slot+10]);assert a==(slot,) and b==(slot+10,)
        if not fill(p) and not fill(q):expected.append((ai,key))
actual={(x['old_index'],tuple(x['node_index'])):x for x in C['cases']}
assert set(expected)==set(actual) and len(expected)==16
checked=[]
for ai,key in expected:
    record=actual[ai,key];A=mp(D['old_actions'][ai]['geometric_push_paired'])
    r,c=base[key];w=sub(r,A)
    assert r==tuple(record['original_relator_F21']) and w==tuple(record['transformed_relator_F21'])
    d=normalize(chainB(w));assert aug(c)==aug(d)
    assert len(c)==record['original_chain_terms'] and len(d)==record['transformed_chain_terms']
    rc={r for r,g in c};rd={r for r,g in d}
    assert rc!=rd
    removed=sorted(rc-rd);added=sorted(rd-rc)
    decision=record['exact_decision'];assert decision['kind']=='different_full_row_support'
    decode=lambda rows:[(x[0],x[1],tuple(x[2])) for x in rows]
    assert removed==decode(decision['only_original']) and added==decode(decision['only_transformed'])
    assert hashlib.sha256(repr(sorted(c.items())).encode()).hexdigest()==record['original_full_G_column_sha256']
    assert hashlib.sha256(repr(sorted(d.items())).encode()).hexdigest()==record['transformed_full_G_column_sha256']
    assert not conjugate(r,w) and not record['positive_free_conjugacy'] and not record['full_G_monomial_relation']
    checked.append({'old_index':ai,'node':key,'original_terms':len(c),'transformed_terms':len(d),
                    'only_original_rows':removed,'only_transformed_rows':added})
    print('PASS actual case',ai,key,'full G support differences',len(removed),len(added),flush=True)
out={'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'method':'canonical retained-head/slot words;product chains integrated at B steps',
     'initial_full_chain_checks':8,'transformed_full_chain_checks':16,'cases':checked,
     'scope':'refutes only the specified all-collision G-unit shortcut;no full-span dependence,kappa value,source nonmembership,or compact conclusion',
     'elapsed_seconds':time.monotonic()-started}
(HERE/'zero_head_diagnostics_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all16 actual cases,full coefficient hashes and exact support differences independently reconstructed.')
print('Elapsed seconds',round(out['elapsed_seconds'],3),flush=True)
