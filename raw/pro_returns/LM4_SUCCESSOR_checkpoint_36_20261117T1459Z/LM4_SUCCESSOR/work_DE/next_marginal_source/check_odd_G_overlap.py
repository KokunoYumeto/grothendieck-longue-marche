#!/usr/bin/env python3
"""One actual cross-sheet overlap: L_ret and alpha_b^{-1}(L_ret).

All128 columns are reconstructed from literal paired F21 relators. The
whole G coefficient normalization is exact. Augmented collisions alone
are not promoted to relations: a full word/G-chain witness is required.
No further word or orbit depth is tested.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent
P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/'symmetric_paired_fox_data.json',P/'symmetric_retained_deck_module.json']
raw=[p.read_bytes() for p in paths];D,G=map(json.loads,raw)
start=time.monotonic()
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
def rr(w):
    out=[]
    for a in w:
        if out and out[-1]==(-a[0],a[1],a[2]):out.pop()
        else:out.append(a)
    return tuple(out)
def ri(w):return tuple((-s,h,j) for s,h,j in reversed(w))
old=D['retained_paired_indices'];hm={j:i+1 for i,j in enumerate(old)}
beta=mp(D['retained_involution']);F=mp(D['paired_involution'])
def bt(w):return sub(w,beta)
meta={int(k):(tuple(v['retained_word']),v['paired_slot']) for k,v in D['finite_used_common_R_basis'].items()}
lookup={v:k for k,v in meta.items()}
def rid(a):
    k=(a[1],a[2])
    if k not in lookup:
        n=max(meta,default=0)+1;meta[n]=k;lookup[k]=n
    return a[0]*lookup[k]
def encode_r(w):return tuple(rid(a) for a in w)
def decode_r(w,md=meta):return rr((1 if x>0 else -1,*md[abs(x)]) for x in w)
def act(t,w):return rr((s,red(t+h),j) for s,h,j in w)
def gm(a,c):
    u,v,t=a;x,y,s=c
    return rr(u+act(t,x)),rr(v+act(bt(t),y)),red(t+s)
def gi(a):
    u,v,t=a;s=inv(t)
    return act(s,ri(u)),act(bt(s),ri(v)),s
def gf(a):return a[1],a[0],bt(a[2])
def kw(w):
    head=();out=[]
    for x in w:
        j=abs(x);sign=1 if x>0 else -1
        if j in hm:head=red(head+(sign*hm[j],))
        else:
            side=0 if j<12 else 1
            out.append((side,(sign,head if side==0 else bt(head),j if side==0 else j-10)))
    assert not head
    return out
def qword(w):
    t=red((1 if x>0 else -1)*hm[abs(x)] for x in w if abs(x) in hm)
    lift=tuple((1 if x>0 else -1)*old[abs(x)-1] for x in t)
    n=kw(red(tuple(w)+inv(lift)))
    return rr(a for side,a in n if side==0),rr(a for side,a in n if side==1),t
def chain(w):
    a=b=();out=defaultdict(int)
    for side,x in kw(w):
        if side==0:
            an=rr(a+(x,));av=a if x[0]>0 else an;bp=()
            for y in b:
                bn=rr(bp+(y,));bv=bp if y[0]>0 else bn
                add(out,(av,bv,x[1:],y[1:]),-x[0]*y[0]);bp=bn
            a=an
        else:b=rr(b+(x,))
    assert not a and not b
    return dict(out)
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
def normalize(c):
    out=defaultdict(int)
    for (u,v,(g,i),(h,j)),n in c.items():add(out,((i,j,red(inv(bt(g))+h)),(u,v,g)),n)
    return dict(out)
def augment(c):
    out=defaultdict(int)
    for (row,a),n in c.items():add(out,(row,a[2]),n)
    return dict(out)
def shift(c,a,sign=1):
    out=defaultdict(int)
    for (r,g),n in c.items():add(out,(r,gm(a,g)),sign*n)
    return dict(out)
def fc(c):
    out=defaultdict(int)
    for ((i,j,z),a),n in c.items():add(out,((j,i,inv(bt(z))),gm(gf(a),((),(),z))),-n)
    return dict(out)
def peel(w):
    i=0
    while len(w)-2*i>1 and w[i]==-w[-1-i]:i+=1
    return w[:i],w[i:len(w)-i] if i else w
def conjugator(u,v):
    a,c=peel(u);b,d=peel(v)
    if len(c)!=len(d):return None
    for j in range(len(c)):
        if c[j:]+c[:j]==d:
            h=red(b+inv(c[:j])+inv(a));assert red(h+u+inv(h))==v
            return h
    return None
def encg(a):return {'A_word':encode_r(a[0]),'B_word':encode_r(a[1]),'retained_word':a[2]}
def enc(c):
    return [{'row':{'A_slot':r[0],'B_slot':r[1],'relative_retained_word':r[2]},
             'G_coefficient':encg(a),'coefficient':n} for (r,a),n in sorted(c.items())]

A=mp(D['old_actions'][1]['based_pullback_paired'])
Ai=mp(D['old_actions'][1]['geometric_push_paired'])
for j in range(1,22):assert sub(A[j],Ai)==sub(Ai[j],A)==(j,)
keys=[(x['loop_index'],x['local_node_index']) for x in D['node_columns']]
words=[];cols=[];augs=[]
for layer in (0,1):
    for i,node in enumerate(D['node_columns']):
        r=tuple(node['paired_relator']);w=r if not layer else sub(r,A)
        c=chain(w);assert boundary(c)==edges(w)
        if not layer:
            dc={(decode_r(x['A_vertex']),decode_r(x['B_vertex']),meta[x['A_generator']],meta[x['B_generator']]):x['coefficient'] for x in node['fox_cells']}
            assert c==dc
        norm=normalize(c)
        assert normalize(chain(sub(w,F)))==fc(norm)
        aug=augment(norm);assert len(aug)==1
        (row,t),sign=next(iter(aug.items()));assert sign in(-1,1)
        words.append(w);cols.append(norm);augs.append((row,t,sign))
    print('PASS full layer',layer,'all64 actual word boundaries/G columns/F images',flush=True)
row0={r:i for i,(r,t,s) in enumerate(augs[:64])};assert len(row0)==64
collisions=[];all_exact=True
for j,(r,t,s) in enumerate(augs[64:]):
    assert r[:2]==augs[j][0][:2]
    if r not in row0:continue
    i=row0[r];assert i==j
    h=conjugator(words[i],words[64+j])
    rec={'node':keys[i],'raw_column':i,'exact_word_conjugacy':h is not None,
         'seed_augmented_row':r,'seed_retained_unit':augs[i][1],
         'translated_retained_unit':t}
    if h is not None:
        a=qword(h);assert shift(cols[i],a)==cols[64+j]
        assert gm(a,gi(a))==gm(gi(a),a)==((),(),())
        rec.update({'conjugator_F21':h,'G_unit':encg(a),'full_chain_relation':True})
    else:all_exact=False
    collisions.append(rec)
    print('COLLISION',keys[i],'word-conjugate',h is not None,flush=True)
collisionids={x['raw_column'] for x in collisions}
keep=list(range(64))+[64+i for i in range(64) if i not in collisionids]
selected=[augs[i][0] for i in keep]
assert len(set(selected))==len(keep)
rp={r:i for i,r in enumerate(selected)};minor=defaultdict(int)
for jj,j in enumerate(keep):
    for (r,a),n in cols[j].items():
        if r in rp:add(minor,(rp[r],jj,a[2]),n)
assert dict(minor)=={(i,i,augs[j][1]):augs[j][2] for i,j in enumerate(keep)}
rels={tuple(x['node_index']):x for x in G['all64_G_relations']}
mateclosed=all(tuple(rels[tuple(x['node'])]['mate_index']) in {tuple(c['node']) for c in collisions} for x in collisions)
if all_exact:assert mateclosed
encoded=[{'layer':i//64,'node':keys[i%64],'paired_relator':words[i],
          'terms':enc(c),'augmented_row':augs[i][0],'augmented_unit':augs[i][1],
          'augmented_sign':augs[i][2]} for i,c in enumerate(cols)]
out={'scope':__doc__,'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'operator':'actual old1 based pullback alpha_b^-1','columns':encoded,
     'common_R_basis':{i:{'retained_word':h,'paired_slot':j} for i,(h,j) in meta.items()},
     'collision_count':len(collisions),'collisions':collisions,'all_collisions_have_full_G_unit_witness':all_exact,
     'remaining_augmented_unit_columns':len(keep),'intersection_F_mate_closed_if_unit_relations':mateclosed,
     'candidate_intersection_rank_if_all_exact':len(collisions) if all_exact else None,
     'claims_excluded':['higher orbit depth','global overlap vanishing','I=R'],
     'elapsed_seconds':time.monotonic()-start}
(HERE/'odd_G_overlap.json').write_text(json.dumps(out,indent=2)+'\n')
print('RESULT collisions',len(collisions),'all exact',all_exact,'independent kept columns',len(keep),'F closed',mateclosed,flush=True)
print('Elapsed seconds',round(out['elapsed_seconds'],3),flush=True)
