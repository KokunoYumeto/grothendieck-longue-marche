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
frozen=json.loads((OUT/'d_cm_projective_repair.json').read_text())
old=frozen['certificate'];aa=[a%4 for a in old['A_mod16_cycle_coordinates']]
bb=[a%4 for a in old['beta_mod16_cycle_coordinates']]
assert len(aa)==rho and len(bb)==rho
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

# A literal telescoping of (1-z)u into the two cusp correction columns.
bc=0;ac=0;suffix=u
for token in reversed(zroot):
    if token==0:
        bc^=suffix;suffix=wa(suffix,s)
    else:
        assert token==1
        ac^=suffix;bc^=suffix^wa(suffix,r);suffix=wa(suffix,r)
assert suffix==wa(u,z)
correction=bc^wa(bc,s)^wa(ac^wa(ac,r),s)
assert correction==moving
assert bc^wa(bc,z)^wa(bc,z2)==0
assert ac^wa(ac,z)^wa(ac,z2)==0
for v in [bc,ac]:
    av=wedge_action(v,inverse_cols)
    assert all(not(av>>offset[i]&((1<<(nf-i-1))-1)) for i in range(nf))
def central_word(v):
    word=[]
    while v:
        bit=v&-v;i,j=pairs[bit.bit_length()-1]
        word.extend(basis_words[i]);word.extend(basis_words[j])
        word.extend(inverse(basis_words[i]));word.extend(inverse(basis_words[j]))
        v^=bit
    return word
Ac=central_word(ac)+Aw;Bc=central_word(bc)+Bw
q,new_ab,new_error=evaluate(cusp_word(Ac,Bc))
assert q==0 and new_ab==[0]*rho and new_error==invariant
ss=Bc+[0]+inverse(Bc);rrw=Ac+[1]+inverse(Ac)
assert evaluate(ss*2)==(0,[0]*rho,0)
assert evaluate(rrw*3)==(0,[0]*rho,0)
assert evaluate(Ac)[1]==aa and evaluate(Bc)[1]==bb

# Central corrections preserve every actual Frattini matrix column.
ma=sum(1<<j for j,a in enumerate(aa) if a%2)
mb=sum(1<<j for j,a in enumerate(bb) if a%2)
ew=combine(cycles,ma^mb)
et=[act(ew,g) for g in range(size)]
new_columns=[vc(c^combine(et,c)) for c in cycles]
assert [hex(c) for c in new_columns]==old['new_full_kernel_columns']
assert rank(new_columns)==rho
central_residual=120*61+120*119//2
invariant_dimension=60**2
moving_dimension=central_residual-invariant_dimension
assert central_residual==14460 and invariant_dimension==3600 and moving_dimension==10860
summary={
 'scope':'Separate marked order-1080 verification; actual arithmetic G3 is proved symbolically.',
 'base_order':size,'homology_rank':rho,'moving_homology_rank':120,
 'A_module_fixed_rank':61,'A_module_nontrivial_two_blocks':60,
 'exact_class2_residual_dimension':central_residual,
 'invariant_class2_residual_dimension':invariant_dimension,
 'added_moving_central_kernel_dimension':moving_dimension,
 'old_D50_full_homology_matrix_unchanged':True,
 'old_D50_mod16_conjugators_retained_mod4':True,
 'generation_rank':rank(new_columns),
 'all181_free_generator_words_checked':True,
 'both_exact_torsion_relations_checked':True,
 'full_corrected_cusp_word_checked_mod_invariant_kernel':True,
 'corrected_A_B_word_length':len(Ac),'corrected_beta_B_word_length':len(Bc),
 'corrected_cusp_B_word_length':len(cusp_word(Ac,Bc)),
 'remaining_invariant_error_nonzero':bool(invariant),
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,
 'central_cusp_error':hex(error),'moving_error':hex(moving),'invariant_error':hex(invariant),
 'A_central_correction':hex(ac),'beta_central_correction':hex(bc),
 'z_base_word':zroot,'z_order_three_lift_word':zword,
 'free_generator_B_words':basis_words,
 'fixed_A_module_basis':[hex(v) for v in fixed],
 'nontrivial_A_two_block_basis':[hex(v) for v in paired],
 'A_mod4_abelian_coordinates':aa,'beta_mod4_abelian_coordinates':bb,
 'old_new_Frattini_columns':[hex(c) for c in new_columns]}
(OUT/'d_cm_class2_moving.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)

