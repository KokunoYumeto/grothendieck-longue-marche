#!/usr/bin/env python3
"""Exact class-two pairing obstruction for the separate D50 finite certificate.

The actual arithmetic G3 action is not evaluated by this diagnostic.
The frozen D50 JSON is read only; all graph and pairing maps are rebuilt.
"""
from array import array
from collections import deque
from pathlib import Path
import json,random,time

OUT=Path(__file__).resolve().parent;started=time.time()
def pm(a,b):return tuple(a[b[i]] for i in range(len(a)))
def generated(ident,gens,mul):
    out=[ident];seen={ident}
    for a in out:
        for b in gens:
            c=mul(a,b)
            if c not in seen:seen.add(c);out.append(c)
    return out
ia=tuple(range(5));sa=(0,3,4,1,2);ra=(4,1,2,0,3)
AG=generated(ia,[sa,ra],pm);assert len(AG)==60
ax={a:i for i,a in enumerate(AG)}
at=[[ax[pm(a,b)] for b in AG] for a in AG]
io=(tuple(range(3)),0);so=((1,0,2),0);ro=((1,2,0),1)
def om(a,b):return pm(a[0],b[0]),(a[1]+b[1])%3
OG=generated(io,[so,ro],om);assert len(OG)==18
ox={a:i for i,a in enumerate(OG)}
ot=[[ox[om(a,b)] for b in OG] for a in OG]
size=1080;ident=0
def gm(a,b):return 18*at[a//18][b//18]+ot[a%18][b%18]
s=18*ax[sa]+ox[so];r=18*ax[ra]+ox[ro]
z=ox[(tuple(range(3)),1)];z2=gm(z,z);t=gm(s,r)
assert len(generated(0,[s,r],gm))==size
assert gm(s,s)==0 and gm(gm(r,r),r)==0 and gm(z,z2)==0
left=[array('H',(gm(g,h) for h in range(size))) for g in range(size)]
rs=[gm(g,s) for g in range(size)];rr=[gm(g,r) for g in range(size)]
def act(v,g):
    out=0;perm=left[g]
    while v:
        b=v&-v;e=b.bit_length()-1;out^=1<<perm[e];v^=b
    return out
def order(g):
    a=g;n=1
    while a:a=gm(a,g);n+=1
    return n
assert order(t)==30 and gm(t,t)!=0
assert all(gm(z,g)==gm(g,z) for g in range(size))
v2=[(0,min(g,rs[g])) for g in range(size)]
v3=[(1,min(g,rr[g],rr[rr[g]])) for g in range(size)]
adj={v:[] for v in set(v2+v3)}
for e in range(size):
    adj[v2[e]].append((v3[e],e));adj[v3[e]].append((v2[e],e))
paths={v2[0]:0};queue=deque([v2[0]]);tree=set()
while queue:
    v=queue.popleft()
    for u,e in adj[v]:
        if u not in paths:paths[u]=paths[v]^(1<<e);tree.add(e);queue.append(u)
ch=[e for e in range(size) if e not in tree]
cycles=[paths[v2[e]]^paths[v3[e]]^(1<<e) for e in ch]
assert len(cycles)==181
ch_ix={e:i for i,e in enumerate(ch)}
def vc(v):
    out=0
    for j,e in enumerate(ch):
        if v>>e&1:out|=1<<j
    return out
assert all(vc(c)==1<<j for j,c in enumerate(cycles))
def combine(cols,v):
    out=0
    while v:
        b=v&-v;out^=cols[b.bit_length()-1];v^=b
    return out
def solver(cols):
    basis={};null=[];indices=[]
    for j,col in enumerate(cols):
        v=col;wit=1<<j
        while v:
            p=v.bit_length()-1
            if p not in basis:basis[p]=(v,wit);indices.append(j);break
            q,w=basis[p];v^=q;wit^=w
        if not v:null.append(wit)
    def solve(v):
        out=0
        for p in sorted(basis,reverse=True):
            if v>>p&1:q,w=basis[p];v^=q;out^=w
        assert not v
        return out
    return solve,len(basis),null,indices
def rank(cols):return solver(cols)[1]
w_candidates=[act(c,z)^act(c,z2) for c in cycles]
_,nw,_,indices=solver(w_candidates);assert nw==120
W=[w_candidates[j] for j in indices]
wsolve,_,_,_=solver(W)
assert all(wsolve(w)==1<<j for j,w in enumerate(W))
assert all(w^act(w,z)^act(w,z2)==0 for w in W)
Wt=[w^act(w,t) for w in W]
bsolve,brank,_,_=solver(Wt);assert brank==nw
Pr=(1<<0)^(1<<r);Pt=act(Pr,s)
def cusp(a,b):
    return b^act(b,s)^act(a^act(a,r),s)
def group_check(a,b):
    # beta=(1,b), A=(1,a); the model is the actual edge-cocycle extension.
    ss=(s,b^act(b,s))
    rr0=(r,a^Pr^act(a,r))
    def mm(g,h):return gm(g[0],h[0]),g[1]^act(h[1],g[0])
    assert mm(ss,ss)==(0,0)
    assert mm(mm(rr0,rr0),rr0)==(0,0)
    assert mm(ss,rr0)==(t,Pt)
    return True
def edge_map(c,translates):
    return c^combine(translates,c)
def fitting(cols):
    n=len(cols);power=cols[:];last=n
    for k in range(1,n+2):
        solve,rk,ker,ind=solver(power)
        if rk==last:
            image=[power[j] for j in ind]
            ds=image+ker;dsolve,dr,_,_=solver(ds)
            assert dr==n
            def projection(v):return combine(ker,dsolve(v)>>len(image))
            return k,rk,ker,projection
        last=rk;power=[combine(cols,c) for c in power]
    raise AssertionError('Fitting rank did not stabilize')

# Reconstruct literal marked B words for every free graph generator.
# Alphabet: 0=s, 1=r, 2=r^{-1}; s is its own inverse.
def inverse(word):return [0 if a==0 else 3-a for a in reversed(word)]
def qword(word):
    q=0
    for a in word:q=gm(q,s if a==0 else (r if a==1 else gm(r,r)))
    return q
gwords={0:[]};queue=deque([0])
while queue:
    q=queue.popleft()
    for a,g in [(0,s),(1,r)]:
        h=gm(q,g)
        if h not in gwords:gwords[h]=gwords[q]+[a];queue.append(h)
assert len(gwords)==size
treepaths={v2[0]:[]};queue=deque([v2[0]])
while queue:
    v=queue.popleft()
    for u,e in adj[v]:
        if u not in treepaths:
            treepaths[u]=treepaths[v]+[(e,1 if v[0]==0 else -1)]
            queue.append(u)
IC=[];basis_words=[]
for j,e in enumerate(ch):
    path=treepaths[v2[e]]+[(e,1)]+[(k,-a) for k,a in reversed(treepaths[v3[e]])]
    assert all(a==(1 if i%2==0 else -1) for i,(k,a) in enumerate(path))
    assert path[0][0] in [0,s] and path[-1][0] in [0,s]
    word=[] if path[0][0]==0 else [0]
    for (q,a),(h,b) in zip(path,path[1:]):
        if q==h:continue
        if a==1:
            if rr[q]==h:word.append(1)
            else:assert rr[rr[q]]==h;word.append(2)
        else:assert rs[q]==h;word.append(0)
    if path[-1][0]==s:word.append(0)
    assert qword(word)==0
    c={}
    for k,a in path:c[k]=c.get(k,0)+a
    c={k:a for k,a in c.items() if a}
    assert sum(1<<k for k,a in c.items() if a%2)==cycles[j]
    IC.append(c);basis_words.append(word)

rho=len(ch);offset=[i*(2*rho-i-1)//2 for i in range(rho)]
pairs=[(i,j) for i in range(rho) for j in range(i+1,rho)]
assert len(pairs)==rho*(rho-1)//2
def evaluate(word):
    """Actual collapsed path in the class-two exponent-four free kernel."""
    q=0;ab=[0]*rho;odd=0;central=0
    def append_edge(edge,sign):
        nonlocal odd,central
        if edge in ch_ix:
            j=ch_ix[edge]
            central^=(odd>>(j+1))<<offset[j]
            ab[j]=(ab[j]+sign)%4
            odd^=1<<j
    for token in word:
        if token==0:q=rs[q]
        else:
            h=rr[q] if token==1 else rr[rr[q]]
            append_edge(q,1);append_edge(h,-1);q=h
    return q,ab,central
for j,word in enumerate(basis_words):
    q,ab,c=evaluate(word)
    assert q==0 and ab==[int(i==j) for i in range(rho)] and c==0

M={g:[vc(act(c,g)) for c in cycles] for g in [s,r,z,z2]}
def wedges_to_rows(v):
    rows=[0]*rho
    while v:
        bit=v&-v;i,j=pairs[bit.bit_length()-1]
        rows[i]^=1<<j;rows[j]^=1<<i;v^=bit
    return rows
def rows_to_wedges(rows):
    out=0
    for i,row in enumerate(rows):
        assert not(row>>i&1)
        out|=(row>>(i+1))<<offset[i]
    return out
def wedge_action(v,cols):
    rows=wedges_to_rows(v)
    mrows=[sum(1<<j for j,c in enumerate(cols) if c>>i&1) for i in range(rho)]
    return rows_to_wedges([combine(cols,combine(rows,row)) for row in mrows])
def wa(v,g):return wedge_action(v,M[g])
def wedge(u,v):
    rows=[]
    for i in range(rho):
        rows.append((v if u>>i&1 else 0)^(u if v>>i&1 else 0))
    return rows_to_wedges(rows)

# The integral ribbon-graph pairing is one half of the sum of the
# oriented trivalent-vertex determinants.  Bivalent vertices contribute0.
edge_entries=[[] for g in range(size)]
for j,c in enumerate(IC):
    for g,a in c.items():edge_entries[g].append((j,a))
reps=sorted({min(g,rr[g],rr[rr[g]]) for g in range(size)})
assert len(reps)==size//3
twice=[[0]*rho for j in range(rho)]
for g in reps:
    for i,a in edge_entries[g]:
        for j,b in edge_entries[rr[g]]:
            twice[i][j]+=a*b;twice[j][i]-=a*b
assert all(a%2==0 for row in twice for a in row)
omega=[[a//2 for a in row] for row in twice]
assert all(omega[i][j]==-omega[j][i] for i in range(rho) for j in range(rho))
cols=[sum(1<<i for i in range(rho) if omega[i][j]%2) for j in range(rho)]
assert rank(cols)==146
frozen=json.loads((OUT/'d_cm_projective_repair.json').read_text())
tcols=[int(x,16) for x in frozen['certificate']['new_full_kernel_columns']]
dcols=[]
for j,col in enumerate(tcols):
    transformed=combine(cols,col)
    defects=sum(1<<i for i,u in enumerate(tcols) if (u&transformed).bit_count()%2)
    dcols.append(defects^cols[j])
bad=[(i,j) for i in range(rho) for j in range(i+1,rho) if dcols[j]>>i&1]
assert rank(dcols)==72 and bad[0]==(0,6)
summary={
 'scope':'The separate fixed order-1080 D50 finite certificate only.',
 'base_order':size,'homology_rank':rho,'cusp_count':size//order(t),
 'ribbon_pairing_rank_mod2':rank(cols),'compact_homology_rank':146,
 'fixed_repaired_action_pairing_defect_rank':rank(dcols),
 'first_nonzero_defect_position':list(bad[0]),
 'nonzero_upper_triangular_defect_positions':len(bad),
 'all181_actual_free_generator_words_checked':True,
 'elapsed_seconds':round(time.time()-started,3)}
data={'summary':summary,'pairing_columns_mod2':[hex(x) for x in cols],
      'defect_columns_mod2':[hex(x) for x in dcols],
      'pairing_integer_matrix':omega}
(OUT/'d_class2_diagnostic.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)

