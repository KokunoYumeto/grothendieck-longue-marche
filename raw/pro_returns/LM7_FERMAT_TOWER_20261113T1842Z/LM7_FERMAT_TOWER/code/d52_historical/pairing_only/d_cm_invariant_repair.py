#!/usr/bin/env python3
"""Exact marked finite verification of D51's class-two moving lift.

The actual arithmetic G3 application is proved symbolically in the text.
This program retains the exact separate order-1080 D50 certificate as an
immutable input, lifts its recorded conjugators to the actual class-two
exponent-four quotient, and solves the moving central cusp equation.
Its corrected B words are checked directly in the faithful graph model.
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

# Exact A-module decomposition: fixed61 plus60 irreducible two-blocks.
fixed_candidates=[(1<<j)^combine(M[z],1<<j)^combine(M[z2],1<<j) for j in range(rho)]
_,nf,_,fi=solver(fixed_candidates);fixed=[fixed_candidates[j] for j in fi]
assert nf==61
wbasis=[vc(w) for w in W];paired=[];independent={}
def add_independent(v):
    while v:
        p=v.bit_length()-1
        if p not in independent:independent[p]=v;return True
        v^=independent[p]
    return False
for u in wbasis:
    if add_independent(u):
        v=combine(M[z],u);assert add_independent(v)
        assert combine(M[z],v)==u^v
        paired.extend([u,v])
assert len(paired)==120
adapted=fixed+paired;change,arank,_,_=solver(adapted);assert arank==rho
inverse_cols=[change(1<<j) for j in range(rho)]
assert all(combine(M[z],u)==u for u in fixed)
assert len(paired)//2==60

# Keep the exact D50 homology action and its selected mod16 conjugators.
search=json.loads((OUT/'d_cm_symplectic_search.json').read_text())
selected=search['solution']
amask=int(selected['A_cycle_coordinates'],16)
bmask=int(selected['beta_cycle_coordinates'],16)
aa=[(amask>>j)&1 for j in range(rho)]
bb=[(bmask>>j)&1 for j in range(rho)]
def edge_vector(co):
    out=[0]*size
    for a,c in zip(co,IC):
        for e,b in c.items():out[e]=(out[e]+a*b)%4
    return out
def iact(co,g):
    v=edge_vector(co);out=[0]*size
    for e,a in enumerate(v):out[left[g][e]]=a
    return [out[e] for e in ch]
def collected_word(co):
    out=[]
    for a,w in zip(co,basis_words):
        if a==3:out.extend(inverse(w))
        elif a:out.extend(w*a)
    return out
# Lift these same mod2 conjugators to the integral moving summand modulo4.
def project_moving(co):
    zc=iact(co,z);z2c=iact(co,z2)
    return [(a-3*(a+b+c))%4 for a,b,c in zip(co,zc,z2c)]
aa=project_moving(aa);bb=project_moving(bb)
def ab_cusp(a,b):
    sb=iact(b,s);ra=iact(a,r);sda=iact([(u-v)%4 for u,v in zip(a,ra)],s)
    return [(u-v+w)%4 for u,v,w in zip(b,sb,sda)]
err=ab_cusp(aa,bb);assert all(v%2==0 for v in err)
cuspcols=[w^act(w,s) for w in W]+[act(w^act(w,r),s) for w in W]
csolve,crank,_,_=solver(cuspcols);assert crank==120
rhs=combine(cycles,sum(1<<j for j,a in enumerate(err) if a==2))
co=csolve(rhs)
bc0=vc(combine(W,co&((1<<120)-1)));ac0=vc(combine(W,co>>120))
aa=[(a+2*((ac0>>j)&1))%4 for j,a in enumerate(aa)]
bb=[(a+2*((bc0>>j)&1))%4 for j,a in enumerate(bb)]
assert not any(ab_cusp(aa,bb))
assert project_moving(aa)==aa and project_moving(bb)==bb
zroot=gwords[z];zword=zroot*4
assert qword(zword)==z
assert evaluate(zword*3)==(0,[0]*rho,0)
def moving_lift(co):
    zv=iact(co,z)
    u=[(2*a-b)%4 for a,b in zip(co,zv)]
    zu=iact(u,z)
    assert [(a-b)%4 for a,b in zip(u,zu)]==co
    d=collected_word(u)
    word=d+zword+inverse(d)+inverse(zword)
    q,a,c=evaluate(word)
    assert q==0 and a==co
    return word
Aw=moving_lift(aa);Bw=moving_lift(bb)
def cusp_word(Aw,Bw):return Bw+[0]+inverse(Bw)+Aw+[1]+inverse(Aw)+[2,0]
q,ab,error=evaluate(cusp_word(Aw,Bw))
assert q==0 and ab==[0]*rho
adapted_error=wedge_action(error,inverse_cols)
assert all(not(adapted_error>>offset[i]&((1<<(nf-i-1))-1)) for i in range(nf))
invariant=error^wa(error,z)^wa(error,z2)
moving=error^invariant
assert wa(invariant,z)==invariant
assert moving^wa(moving,z)^wa(moving,z2)==0
u=wa(moving,z)
assert u^wa(u,z)==moving

# The full invariant central module has an explicit Hermitian two-block basis.
blocks=60;smallpairs=[(i,j) for i in range(blocks) for j in range(i+1,blocks)]
smalloff=[i*(2*blocks-i-1)//2 for i in range(blocks)]
npairs=len(smallpairs);dim0=blocks+2*npairs
def eo(v):
    return (sum(1<<i for i in range(blocks) if v>>(2*i)&1),
            sum(1<<i for i in range(blocks) if v>>(2*i+1)&1))
def inv_wedge_projection(a,b):
    ae,ao=a;be,bo=b
    diag=(ae&bo)^(ao&be);pp=0;qq=0
    for i in range(blocks):
        prow=(be if ae>>i&1 else 0)^(ae if be>>i&1 else 0)
        qrow=(be if ao>>i&1 else 0)^(ae if bo>>i&1 else 0)
        pp|=(prow>>(i+1))<<smalloff[i]
        qq|=(qrow>>(i+1))<<smalloff[i]
    return diag|(pp<<blocks)|(qq<<(blocks+npairs))
def invariant_action(g):
    cols=[]
    for v in paired:
        nv=change(combine(M[g],v));assert not(nv&((1<<nf)-1))
        cols.append(eo(nv>>nf))
    dd=[inv_wedge_projection(cols[2*i],cols[2*i+1]) for i in range(blocks)]
    pp=[];qq=[]
    for i,j in smallpairs:
        ui,vi=cols[2*i:2*i+2];uj,vj=cols[2*j:2*j+2]
        pp.append(inv_wedge_projection(ui,uj)^inv_wedge_projection(ui,vj)^inv_wedge_projection(vi,vj))
        qq.append(inv_wedge_projection(ui,vj)^inv_wedge_projection(vi,uj))
    return dd+pp+qq
S0=invariant_action(s);R0=invariant_action(r)
assert len(S0)==dim0 and len(R0)==dim0
inv_basis=[wedge(paired[2*i],paired[2*i+1]) for i in range(blocks)]
pp=[];qq=[]
for i,j in smallpairs:
    ui,vi=paired[2*i:2*i+2];uj,vj=paired[2*j:2*j+2]
    pp.append(wedge(ui,uj)^wedge(ui,vj)^wedge(vi,vj))
    qq.append(wedge(ui,vj)^wedge(vi,uj))
inv_basis+=pp+qq
def inv_coordinates(v):
    a=wedge_action(v,inverse_cols)
    def coefficient(i,j):return (a>>(offset[i]+j-i-1))&1
    d=sum(1<<i for i in range(blocks) if coefficient(nf+2*i,nf+2*i+1))
    p=sum(1<<k for k,(i,j) in enumerate(smallpairs) if coefficient(nf+2*i,nf+2*j))
    q=sum(1<<k for k,(i,j) in enumerate(smallpairs) if coefficient(nf+2*i+1,nf+2*j))
    result=d|(p<<blocks)|(q<<(blocks+npairs))
    assert combine(inv_basis,result)==v
    return result
target=inv_coordinates(invariant)
# Check the action with actual wedge maps on a deterministic spanning selection.
for j in range(0,dim0,53):
    assert combine(inv_basis,S0[j])==wa(inv_basis[j],s)
    assert combine(inv_basis,R0[j])==wa(inv_basis[j],r)
augmentation=[c^(1<<j) for j,c in enumerate(S0)]+[c^(1<<j) for j,c in enumerate(R0)]
asolve,augmentation_rank,anull,_=solver(augmentation)
try:
    correction0=asolve(target);solvable=True
except AssertionError:
    correction0=None;solvable=False

# First kill the moving central error by the exact odd-word telescoping.
bc=0;ac=0;suffix=u
for token in reversed(zroot):
    if token==0:
        bc^=suffix;suffix=wa(suffix,s)
    else:
        assert token==1
        ac^=suffix;bc^=suffix^wa(suffix,r);suffix=wa(suffix,r)
assert bc^wa(bc,s)^wa(ac^wa(ac,r),s)==moving
summary={
 'scope':'The separate order1080 marked source only.',
 'moving_homology_parameters':120,
 'new_nonidentity_symplectic_derivation_rank':search['summary']['solution_derivation_rank'],
 'invariant_central_dimension':dim0,
 'invariant_augmentation_rank':augmentation_rank,
 'invariant_coinvariant_dimension':dim0-augmentation_rank,
 'exact_invariant_cusp_equation_solvable':solvable,
 'new_mod2_action_retained_at_mod4':True}
cert={'summary':summary,'new_A_mod4':aa,'new_beta_mod4':bb,
 'full_cusp_error':hex(error),'moving_error':hex(moving),'invariant_error':hex(invariant),
 'invariant_target_coordinates':hex(target),
 'invariant_action_s':[hex(c) for c in S0],'invariant_action_r':[hex(c) for c in R0]}
if solvable:
    b0=correction0&((1<<dim0)-1);d0=correction0>>dim0
    b0^=d0^combine(R0,d0)
    bfull=combine(inv_basis,b0);afull=combine(inv_basis,d0)
    assert bfull^wa(bfull,s)^wa(afull^wa(afull,r),s)==invariant
    bc^=bfull;ac^=afull
    assert bc^wa(bc,s)^wa(ac^wa(ac,r),s)==error
    def central_word(v):
        word=[]
        while v:
            bit=v&-v;i,j=pairs[bit.bit_length()-1]
            word.extend(basis_words[i]);word.extend(basis_words[j])
            word.extend(inverse(basis_words[i]));word.extend(inverse(basis_words[j]))
            v^=bit
        return word
    Ac=central_word(ac)+Aw;Bc=central_word(bc)+Bw
    assert evaluate(cusp_word(Ac,Bc))==(0,[0]*rho,0)
    assert evaluate((Bc+[0]+inverse(Bc))*2)==(0,[0]*rho,0)
    assert evaluate((Ac+[1]+inverse(Ac))*3)==(0,[0]*rho,0)
    assert evaluate(Ac)[1]==aa and evaluate(Bc)[1]==bb
    ma=sum(1<<j for j,a in enumerate(aa) if a%2)
    mb=sum(1<<j for j,a in enumerate(bb) if a%2)
    ew=combine(cycles,ma^mb);et=[act(ew,g) for g in range(size)]
    tc=[vc(c^combine(et,c)) for c in cycles]
    assert [hex(c) for c in tc]==selected['homology_columns']
    assert rank(tc)==rho
    summary.update({'full_corrected_cusp_word_verified':True,'full_two_torsion_relations_verified':True,
       'corrected_cusp_word_length':len(cusp_word(Ac,Bc)),'generation_rank':rank(tc)})
    cert.update({'A_central_correction':hex(ac),'beta_central_correction':hex(bc),
                 'invariant_correction_coordinates':hex(correction0)})
summary['elapsed_seconds']=round(time.time()-started,3)
(OUT/'d_cm_invariant_repair.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)

