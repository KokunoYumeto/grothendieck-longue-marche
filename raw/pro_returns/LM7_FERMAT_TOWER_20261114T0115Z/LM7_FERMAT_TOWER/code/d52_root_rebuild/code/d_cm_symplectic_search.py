#!/usr/bin/env python3
"""Actual cusp-fixed homology corrections for the separate order1080 model."""
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

pairing=json.loads((OUT/'d_class2_diagnostic.json').read_text())
oc=[int(x,16) for x in pairing['pairing_columns_mod2']]
rho=len(cycles);offset=[i*(2*rho-i-1)//2 for i in range(rho)]
def upper_from_columns(cols):
    out=0
    for i in range(rho):
        row=sum(1<<(j-i-1) for j in range(i+1,rho) if cols[j]>>i&1)
        out|=row<<offset[i]
    return out
derivations=[];linear_cols=[]
for w in W:
    trans=[act(w,g) for g in range(size)]
    dc=[vc(combine(trans,c)) for c in cycles]
    derivations.append(dc)
    od=[combine(oc,c) for c in dc]
    linear=[od[j]^sum(1<<i for i,c in enumerate(dc) if (c&oc[j]).bit_count()%2)
            for j in range(rho)]
    linear_cols.append(upper_from_columns(linear))
_,linear_rank,null,_=solver(linear_cols)
def d_from_mask(mask):
    cols=[0]*rho
    while mask:
        bit=mask&-mask;d=derivations[bit.bit_length()-1]
        cols=[a^b for a,b in zip(cols,d)];mask^=bit
    return cols
def quadratic_zero(dc):
    for c in dc:
        if combine(oc,combine(dc,c)):return False
    return True
records=[];solutions=[]
for j,mask in enumerate(null):
    dc=d_from_mask(mask);ok=quadratic_zero(dc)
    records.append({'null_basis_index':j,'quadratic_zero':ok,'derivation_rank':rank(dc)})
    if ok and any(dc):solutions.append(mask)
rng=random.Random(20261114)
tried=0
while not solutions and tried<2000:
    tried+=1
    mask=combine(null,rng.getrandbits(len(null)));dc=d_from_mask(mask)
    if any(dc) and quadratic_zero(dc):solutions.append(mask)
summary={
 'scope':'The separate marked order1080 model only; no actual G3 inference.',
 'actual_cusp_fixed_derivation_parameters':len(W),
 'linearized_pairing_constraint_rank':linear_rank,
 'linearized_pairing_kernel_dimension':len(null),
 'basis_solutions':sum(x['quadratic_zero'] and x['derivation_rank']>0 for x in records),
 'random_trials':tried,'nonidentity_symplectic_solution_found':bool(solutions)}
cert={'summary':summary,'linearized_null_basis':[hex(x) for x in null],
      'basis_records':records}
if solutions:
    mask=solutions[0];dc=d_from_mask(mask);tc=[c^(1<<j) for j,c in enumerate(dc)]
    assert rank(tc)==rho
    for j,c in enumerate(tc):
        v=combine(oc,c)
        assert sum(1<<i for i,u in enumerate(tc) if (u&v).bit_count()%2)==oc[j]
    w=combine(W,mask)
    b=combine(W,bsolve(act(w^act(w,r),s)));a=w^b
    assert cusp(a,b)==0 and group_check(a,b)
    summary['solution_derivation_rank']=rank(dc)
    summary['solution_auto_rank']=rank(tc)
    cert['solution']={'parameter_mask':hex(mask),'A_cycle_coordinates':hex(vc(a)),
      'beta_cycle_coordinates':hex(vc(b)),'homology_columns':[hex(x) for x in tc]}
summary['elapsed_seconds']=round(time.time()-started,3)
(OUT/'d_cm_symplectic_search.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)

