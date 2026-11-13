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

# Quotient the complete pair space by its exact same-action kernel.
S=[wsolve(w^act(w,s)) for w in W]
R=[wsolve(w^act(w,r)) for w in W]
_,sr,sk,_=solver(S);_,rrank,rk,_=solver(R)
K=sk+rk;assert len(K)==102 and rank(K)==102
_,nr,_,inds=solver(K+[1<<j for j in range(120)])
comp=[1<<(j-102) for j in inds if j>=102]
assert len(comp)==18 and nr==120
input_data=json.loads((OUT/'d_cm_full_class2_search.json').read_text())
linear=input_data['linear_obstruction_coefficients'];quadratic=input_data['quadratic_obstruction_coefficients']
def obstruction(mask):
    active=[i for i in range(120) if mask>>i&1];ans=0
    for k,i in enumerate(active):
        ans^=linear[i]
        for j in active[k+1:]:ans^=quadratic[min(i,j)][max(i,j)]
    return ans
Kobs=[obstruction(k) for k in K];ksolve,kr,_,ki=solver(Kobs);assert kr==4
# A canonical representative for the quotient of the13 obstruction coordinates.
obsbasis={}
for col in Kobs:
    v=col
    while v:
        p=v.bit_length()-1
        if p not in obsbasis:obsbasis[p]=v;break
        v^=obsbasis[p]
def ored(v):
    for p in sorted(obsbasis,reverse=True):
        if v>>p&1:v^=obsbasis[p]
    return v
lin=[ored(obstruction(c)) for c in comp]
qua=[[0]*18 for _ in range(18)]
for i in range(18):
    for j in range(i+1,18):qua[i][j]=ored(obstruction(comp[i]^comp[j]))^lin[i]^lin[j]
# Compute every actual matrix coefficient of T^t Omega T-Omega.
oc=[int(x,16) for x in json.loads((OUT/'d_class2_diagnostic.json').read_text())['pairing_columns_mod2']]
rho=181;offset=[i*(2*rho-i-1)//2 for i in range(rho)]
def mat_upper(cols):
    out=0
    for j,col in enumerate(cols):
        for i in range(j):
            if col>>i&1:out^=1<<(offset[i]+j-i-1)
    return out
def defect(dc):
    tc=[v^(1<<j) for j,v in enumerate(dc)]
    out=[]
    for j,c in enumerate(tc):
        v=combine(oc,c);out.append(sum(1<<i for i,u in enumerate(tc) if (u&v).bit_count()%2)^oc[j])
    return mat_upper(out)
Ds=[]
for mask in comp:
    w=combine(W,mask);tr=[act(w,g) for g in range(size)]
    Ds.append([vc(combine(tr,c)) for c in cycles])
plin=[defect(d) for d in Ds]
pquad=[[0]*18 for _ in range(18)]
for i in range(18):
    for j in range(i+1,18):pquad[i][j]=defect([a^b for a,b in zip(Ds[i],Ds[j])])^plin[i]^plin[j]
o_cols=lin+[qua[i][j] for i in range(18) for j in range(i+1,18)]
p_cols=plin+[pquad[i][j] for i in range(18) for j in range(i+1,18)]
_,orank,okernel,oi=solver(o_cols);_,prank,pkernel,pi=solver(p_cols)
same_equations=all(combine(p_cols,k)==0 for k in okernel) and all(combine(o_cols,k)==0 for k in pkernel)
print('reduced obstruction rank',orank,'pairing coefficient rank',prank,'same equations',same_equations,flush=True)
def poly(m):
    ans=0;active=[i for i in range(18) if m>>i&1]
    for k,i in enumerate(active):
        ans^=lin[i]
        for j in active[k+1:]:ans^=qua[i][j]
    return ans
solutions=[m for m in range(1<<18) if poly(m)==0]
print('complete solution count',len(solutions),flush=True)
rank_counts={};matrices=[];corrected_parameter_masks=[]
for m in solutions:
    representative=combine(comp,m)
    correction=ksolve(obstruction(representative))
    repaired=representative^combine(K,correction)
    assert obstruction(repaired)==0
    corrected_parameter_masks.append(repaired)
    d=[0]*rho
    for i in range(18):
        if m>>i&1:d=[a^b for a,b in zip(d,Ds[i])]
    T=[v^(1<<j) for j,v in enumerate(d)]
    assert rank(T)==181 and defect(d)==0
    dr=rank(d);rank_counts[dr]=rank_counts.get(dr,0)+1
    matrices.append(T)
# Verify that the completed solution set is an actual group on homology.
flatDs=[sum(c<<(rho*j) for j,c in enumerate(d)) for d in Ds]
dsolve,dr,_,_=solver(flatDs);assert dr==18
solution_set=set(solutions)
def product_mask(a,b):
    TA=matrices[a];TB=matrices[b]
    D=[combine(TA,c)^(1<<j) for j,c in enumerate(TB)]
    return dsolve(sum(c<<(rho*j) for j,c in enumerate(D)))
# Choose generators by exact subgroup closure and check inverses through finiteness.
lookup={m:i for i,m in enumerate(solutions)};generated_masks={0};gens=[]
for mask in solutions:
    if mask in generated_masks:continue
    gens.append(mask);todo=list(generated_masks);at0=0
    while at0<len(todo):
        v=todo[at0];at0+=1
        for g in gens:
            p=product_mask(lookup[v],lookup[g]);assert p in solution_set
            if p not in generated_masks:generated_masks.add(p);todo.append(p)
assert generated_masks==solution_set
summary={'scope':'Complete separate order1080 finite homology classification; no arithmetic transfer.',
 'pair_parameter_dimension':120,'same_action_kernel_dimension':102,'actual_homology_parameter_dimension':18,
 'same_action_obstruction_image_rank':kr,'reduced_obstruction_coefficient_rank':orank,
 'pairing_defect_coefficient_rank':prank,'reduced_obstruction_exactly_pairing_equations':same_equations,
 'complete_solution_count':len(solutions),'all_solutions_invertible':True,
 'homology_deviation_rank_counts':rank_counts,'group_generators':[hex(g) for g in gens],
 'exact_group_generation_verified':True,'all864_repaired_full_parameter_equations_verified':True,'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'homology_complement_parameter_masks':[hex(x) for x in comp],
 'same_action_obstruction_image_basis':[obsbasis[p] for p in sorted(obsbasis)],
 'reduced_linear_obstruction_coefficients':lin,'reduced_quadratic_obstruction_coefficients':qua,
 'pairing_linear_coefficients':[hex(x) for x in plin],
 'pairing_quadratic_coefficients':[[hex(x) for x in row] for row in pquad],
 'exact_homology_solution_parameters':[hex(x) for x in solutions],
 'all_corrected_full_pair_parameter_masks':[hex(x) for x in corrected_parameter_masks],
 'full_homology_derivation_columns':[[hex(x) for x in d] for d in Ds]}
(OUT/'d_cm_reduced_invariant_equations.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
