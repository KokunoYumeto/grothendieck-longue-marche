#!/usr/bin/env python3
"""Exact transfer from the boundary obstruction to compact orientation.

This program uses the separate marked order1080 source and retains
the actual compact quotient, norm and invariant-coordinate maps.
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

# Compact homology is the actual quotient by the radical of the ribbon form.
pairing=json.loads((OUT/'d_class2_diagnostic.json').read_text())
Omega=[int(x,16) for x in pairing['pairing_columns_mod2']]
_,compact_rank,radical,Cindices=solver(Omega);assert compact_rank==146 and len(radical)==35
def compress(v):return sum(1<<i for i,j in enumerate(Cindices) if v>>j&1)
def embed(v):return sum(1<<j for i,j in enumerate(Cindices) if v>>i&1)
OC=[compress(Omega[j]) for j in Cindices]
osolve,ork,_,_=solver(OC);assert ork==146
projection=[embed(osolve(compress(c))) for c in Omega]
assert all(combine(projection,v)==0 for v in radical)
assert all(projection[j]==1<<j for j in Cindices)
inverse_form=[0]*rho
for j,index0 in enumerate(Cindices):inverse_form[index0]=embed(osolve(1<<j))
J=rows_to_wedges(inverse_form)
assert rank(inverse_form)==146
# Reconstruct exactly the invariant basis used in the original13-coordinate map.
fixed_candidates=[(1<<j)^combine(M[z],1<<j)^combine(M[z2],1<<j) for j in range(rho)]
_,nf,_,fi=solver(fixed_candidates);fixed=[fixed_candidates[j] for j in fi];assert nf==61
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
        assert combine(M[z],v)==u^v;paired.extend([u,v])
assert len(paired)==120
inv_basis=[wedge(paired[2*i],paired[2*i+1]) for i in range(60)]
pp=[];qq=[]
for i in range(60):
    ui,vi=paired[2*i:2*i+2]
    for j in range(i+1,60):
        uj,vj=paired[2*j:2*j+2]
        pp.append(wedge(ui,uj)^wedge(ui,vj)^wedge(vi,vj))
        qq.append(wedge(ui,vj)^wedge(vi,uj))
inv_basis+=pp+qq;assert len(inv_basis)==3600
full=json.loads((OUT/'d_cm_full_class2_search.json').read_text())
dual=[int(x,16) for x in full['coinvariant_dual_functionals']]
dcols=[sum(1<<j for j,row in enumerate(dual) if row>>i&1) for i in range(3600)]
dsolve,dr,_,_=solver(dcols);assert dr==13
representatives=[combine(inv_basis,dsolve(1<<j)) for j in range(13)]
assert all(wa(v,z)==v and wa(v,z2)==v for v in representatives)
# Exact subgroup-chain norm, with the literal direct-product markings retained.
def transversal(big,small):
    uncovered=set(big);rep=[]
    while uncovered:
        a=min(uncovered);rep.append(a);cos={gm(a,b) for b in small}
        assert cos<=set(big);uncovered-=cos
    assert len(rep)*len(small)==len(big)
    return rep
A5=[18*i for i in range(60)]
H4=[18*i for i,a in enumerate(AG) if a[1]==1]
ra0=18*ax[ra];H3=[0,ra0,gm(ra0,ra0)]
assert len(H4)==12 and set(H3)<=set(H4)
S3=[ox[(p,0)] for p in generated(tuple(range(3)),[so[0],ro[0]],pm)]
rr0=ox[(ro[0],0)];HS3=[0,rr0,gm(rr0,rr0)]
chains=[H3,transversal(H4,H3),transversal(A5,H4),HS3,transversal(S3,HS3)]
assert [len(x) for x in chains]==[3,4,5,3,2]
needed=set(g for row in chains for g in row)|{z,z2,s,r}
for g in needed:
    if g not in M:M[g]=[vc(act(c,g)) for c in cycles]
mrows={g:[sum(1<<j for j,c in enumerate(cols) if c>>i&1) for i in range(rho)] for g,cols in M.items()}
def fastwa(v,g):
    rows=wedges_to_rows(v)
    return rows_to_wedges([combine(M[g],combine(rows,row)) for row in mrows[g]])
def compact_wedge(v):return wedge_action(v,projection)
def norm(v):
    # The central C3 norm is identity on every chosen A-invariant vector.
    assert fastwa(v,z)==v
    for reps in chains:
        a=0
        for g in reps:a^=fastwa(v,g)
        v=a
    return compact_wedge(v)
for g in [s,r]:
    for j,c in enumerate(M[g]):
        ov=combine(Omega,c)
        assert sum(1<<i for i,u in enumerate(M[g]) if (u&ov).bit_count()%2)==Omega[j]
        assert combine(projection,combine(M[g],projection[j]))==combine(projection,c)
    assert compact_wedge(fastwa(J,g))==J
Ncols=[norm(v) for v in representatives]
assert all(compact_wedge(fastwa(v,g))==v for v in Ncols for g in [s,r])
_,nr,nkernel,_=solver(Ncols)
reduced=json.loads((OUT/'d_cm_reduced_invariant_equations.json').read_text())
local=reduced['same_action_obstruction_image_basis']
local_killed=all(combine(Ncols,v)==0 for v in local)
print('compact norm rank',nr,'local kernel killed',local_killed,flush=True)
Ds=[[int(v,16) for v in row] for row in reduced['full_homology_derivation_columns']]
def bivector_defect(d):
    return compact_wedge(wedge_action(J,[c^(1<<j) for j,c in enumerate(d)]))^J
blinear=[bivector_defect(d) for d in Ds]
bquad=[[0]*18 for _ in range(18)]
for i in range(18):
    for j in range(i+1,18):bquad[i][j]=bivector_defect([a^b for a,b in zip(Ds[i],Ds[j])])^blinear[i]^blinear[j]
ol=reduced['reduced_linear_obstruction_coefficients'];oq=reduced['reduced_quadratic_obstruction_coefficients']
linear_match=[combine(Ncols,c)==blinear[i] for i,c in enumerate(ol)]
quadratic_match=[combine(Ncols,oq[i][j])==bquad[i][j] for i in range(18) for j in range(i+1,18)]
summary={'scope':'Exact norm-to-compact-bivector comparison for the separate marked order1080 source.',
 'compact_rank':compact_rank,'cusp_radical_dimension':len(radical),
 'actual_deck_pairing_compact_projection_and_norm_invariance_verified':True,
 'obstruction_coordinate_dimension':13,'compact_norm_rank':nr,
 'entire_local_obstruction_image_killed':local_killed,
 'norm_kernel_equals_local_image':local_killed and nr==9,
 'all18_linear_bivector_coefficients_equal_norm':all(linear_match),
 'all153_quadratic_bivector_coefficients_equal_norm':all(quadratic_match),
 'matched_linear_coefficients':sum(linear_match),'matched_quadratic_coefficients':sum(quadratic_match),
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'compact_basis_indices':Cindices,'compact_projection_columns':[hex(x) for x in projection],
 'compact_intersection_bivector':hex(J),'actual_norm_subgroup_transversals':chains,
 'thirteen_obstruction_representatives':[hex(x) for x in representatives],
 'norm_columns':[hex(x) for x in Ncols],
 'compact_bivector_linear_coefficients':[hex(x) for x in blinear],
 'compact_bivector_quadratic_coefficients':[[hex(x) for x in row] for row in bquad]}
(OUT/'d_cm_boundary_norm.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
