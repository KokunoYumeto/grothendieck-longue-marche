#!/usr/bin/env python3
"""Exact marked finite test of D50's projective Fitting repair.

The actual arithmetic application has G=G3 and is proved in the text.
This runnable certificate uses the explicit marked source
B -> A5 x (S3 x C3), of order1080, and verifies the same repair on
its full181-dimensional kernel.  It does not replace the arithmetic
parameter by a guessed finite vector.
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

rng=random.Random(20261113);trial_records=[];chosen=None
for trial in range(1,65):
    w=combine(W,rng.getrandbits(nw))
    translates=[act(w,g) for g in range(size)]
    LW=[wsolve(edge_map(v,translates)) for v in W]
    k,rk,Pcoords,projection=fitting(LW)
    trial_records.append({'trial':trial,'W_map_rank':rank(LW),
                          'Fitting_invertible_dimension':rk,
                          'Fitting_nilpotent_dimension':nw-rk,'stabilization_power':k})
    if rk==nw:continue
    P=[combine(W,c) for c in Pcoords];d=len(P)
    # The explicit regular-module Fitting projection is determined by its
    # value p on edge1.  On the nilpotent summand, L+I is invertible.
    plus_cols=[combine(LW,c)^c for c in Pcoords]
    plussolve,prank,_,_=solver(plus_cols);assert prank==d
    pcoords=combine(Pcoords,plussolve(projection(wsolve(w))))
    p=combine(W,pcoords)
    pe=[act(p,g) for g in range(size)]
    if w==p:continue
    def project_edge(v):return combine(pe,v)
    assert project_edge(p)==p
    assert rank(pe)==d
    assert edge_map(p,translates)==p^project_edge(w)
    for j,v in enumerate(W):
        assert project_edge(v)==combine(W,projection(1<<j))
    for c in cycles:
        wpart=act(c,z)^act(c,z2)
        assert project_edge(c)==combine(W,projection(wsolve(wpart)))
    # Verify both original and repaired cusp/peripheral identities.
    b=combine(W,bsolve(act(w^act(w,r),s)));a=w^b
    assert cusp(a,b)==0 and group_check(a,b)
    delta_t=act(p^act(p,r),s)
    norm=0;g=0
    for j in range(order(t)):norm^=act(delta_t,g);g=gm(g,t)
    assert g==0 and norm==0
    repair_cols=[v^act(v,t) for v in P]
    repair_solve,repair_rank,_,_=solver(repair_cols)
    repair_b=combine(P,repair_solve(delta_t))
    assert repair_b^act(repair_b,t)==delta_t
    anew=a^p^repair_b;bnew=b^repair_b
    assert cusp(anew,bnew)==0 and group_check(anew,bnew)
    assert anew^bnew==w^p
    # The entire181-dimensional actual kernel map, not just W.
    LV=[vc(edge_map(c,translates)) for c in cycles]
    new_trans=[x^y for x,y in zip(translates,pe)]
    LVnew=[vc(edge_map(c,new_trans)) for c in cycles]
    assert rank(LV)<181 and rank(LVnew)==181
    assert all((edge_map(c,new_trans)^edge_map(c,translates))==project_edge(c)
               for c in cycles)
    assert any(LVnew[j]!=(1<<j) for j in range(181))
    # The regular-module projection is explicitly idempotent and G-linear.
    assert all(project_edge(v)==v for v in pe)
    assert all(pe[left[g][j]]==act(pe[j],g) for g in [s,r] for j in range(size))
    chosen={'trial':trial,'Fitting_nilpotent_dimension':d,
      'Fitting_stabilization_power':k,'regular_projection_rank':rank(pe),
      'old_full_kernel_rank':rank(LV),'new_full_kernel_rank':rank(LVnew),
      'repair_cyclic_equation_rank':repair_rank,
      'w_edge_chain':hex(w),'projection_of_edge1':hex(p),
      'A_cycle_coordinates':hex(vc(a)),'beta_cycle_coordinates':hex(vc(b)),
      'repair_b_cycle_coordinates':hex(vc(repair_b)),
      'new_A_cycle_coordinates':hex(vc(anew)),'new_beta_cycle_coordinates':hex(vc(bnew)),
      'old_full_kernel_columns':[hex(c) for c in LV],
      'new_full_kernel_columns':[hex(c) for c in LVnew],
      'nilpotent_basis_cycle_coordinates':[hex(vc(c)) for c in P],
      'regular_module_projection_columns':[hex(c) for c in pe],
      'cyclic_norm_of_cusp_error_is_zero':True,
      'full_group_cusp_and_two_torsion_relations_before_and_after':True,
      'all181_cycle_comparisons':True,'regular_projection_G_linear_and_idempotent':True}
    break
assert chosen is not None
# A compatible integral lift through exponents2,4,8,16.  The actual
# odd-deck averaging idempotent is used modulo16, so these are lifts in
# the moving direct summand, not arbitrary parity representatives.
ipaths={v2[0]:{}};queue=deque([v2[0]]);itree=set()
while queue:
    v=queue.popleft()
    for u,e in adj[v]:
        if u not in ipaths:
            c=ipaths[v].copy();c[e]=c.get(e,0)+(1 if v[0]==0 else -1)
            if not c[e]:del c[e]
            ipaths[u]=c;itree.add(e);queue.append(u)
assert [e for e in range(size) if e not in itree]==ch
IC=[]
for j,e in enumerate(ch):
    c=ipaths[v2[e]].copy()
    for k,a0 in ipaths[v3[e]].items():
        c[k]=c.get(k,0)-a0
        if not c[k]:del c[k]
    c[e]=c.get(e,0)+1
    if not c[e]:del c[e]
    assert sum(1<<k for k,a0 in c.items() if a0%2)==cycles[j]
    IC.append(c)
def av(v,g):
    out=[0]*size
    for j,a0 in enumerate(v):out[left[g][j]]=a0
    return out
def ivec(coords,mod=16):
    out=[0]*size
    while coords:
        bit=coords&-coords
        for j,a0 in IC[bit.bit_length()-1].items():out[j]=(out[j]+a0)%mod
        coords^=bit
    return out
def move(v,mod=16):
    zv=av(v,z);z2v=av(v,z2);q=pow(3,-1,mod)
    return [(a0-q*(a0+b0+c0))%mod for a0,b0,c0 in zip(v,zv,z2v)]
IW=[move(ivec(1<<j)) for j in indices]
assert all(sum(1<<j for j,a0 in enumerate(v) if a0%2)==w0 for v,w0 in zip(IW,W))
cusp_cols=[v^act(v,s) for v in W]+[act(v^act(v,r),s) for v in W]
cusp_solve,cusp_rank,_,_=solver(cusp_cols);assert cusp_rank==nw
aa=move(ivec(vc(anew)));bb=move(ivec(vc(bnew)))
def idefect(a0,b0,mod):
    sb=av(b0,s);ra=av(a0,r);da=[(u-v)%mod for u,v in zip(a0,ra)];sda=av(da,s)
    return [(u-v+w0)%mod for u,v,w0 in zip(b0,sb,sda)]
def add_cycles(v,mask,scale,mod=16):
    while mask:
        bit=mask&-mask
        for j,a0 in enumerate(IW[bit.bit_length()-1]):v[j]=(v[j]+scale*a0)%mod
        mask^=bit
def group_check_mod(a0,b0,mod):
    pr=[0]*size;pr[0]=1;pr[r]=-1
    ssv=[(u-v)%mod for u,v in zip(b0,av(b0,s))]
    rrv=[(u+v-w0)%mod for u,v,w0 in zip(a0,pr,av(a0,r))]
    assert all((u+v)%mod==0 for u,v in zip(ssv,av(ssv,s)))
    r2v=av(rrv,r);r3v=av(r2v,r)
    assert all((u+v+w0)%mod==0 for u,v,w0 in zip(rrv,r2v,r3v))
    pt=av(pr,s)
    assert all((u+v-w0)%mod==0 for u,v,w0 in zip(ssv,av(rrv,s),pt))
    return True
lift_steps=[]
for level in [2,4,8,16]:
    previous=level//2
    error=idefect(aa,bb,level);correction=0
    if level>2:
        assert all(e%previous==0 for e in error)
        rhs=sum(1<<j for j,e in enumerate(error) if (e//previous)%2)
        correction=cusp_solve(rhs)
        add_cycles(bb,correction&((1<<nw)-1),previous)
        add_cycles(aa,correction>>nw,previous)
    assert not any(idefect(aa,bb,level))
    assert group_check_mod(aa,bb,level)
    assert move(aa,level)==[x%level for x in aa]
    assert move(bb,level)==[x%level for x in bb]
    assert sum(1<<j for j,x in enumerate(aa) if x%2)==anew
    assert sum(1<<j for j,x in enumerate(bb) if x%2)==bnew
    lift_steps.append({'kernel_exponent':level,'cusp_and_torsion_checks':True,
                       'same_original_mod2_conjugators':True,
                       'both_conjugators_in_actual_moving_summand':True,
                       'correction_mask':hex(correction)})
chosen['integral_lift_steps']=lift_steps
chosen['A_mod16_cycle_coordinates']=[aa[e] for e in ch]
chosen['beta_mod16_cycle_coordinates']=[bb[e] for e in ch]
summary={'marked_finite_base':'A5 x (S3 x C3)','base_order':size,
 'base_s_A5_one_line':list(sa),'base_r_A5_one_line':list(ra),
 'central_odd_A_order':3,'cusp_order':order(t),
 'actual_mod2_homology_kernel_dimension':181,'moving_A_dimension':nw,
 'moving_A_cusp_correction_rank':nw,'selected_trial':chosen['trial'],
 'projective_Fitting_summand_dimension':chosen['Fitting_nilpotent_dimension'],
 'old_full_kernel_rank':chosen['old_full_kernel_rank'],
 'repaired_full_kernel_rank':chosen['new_full_kernel_rank'],
 'regular_module_retraction_G_linear_and_idempotent':True,
 'all181_actual_cycle_maps_checked':True,
 'peripheral_and_cusp_identities_checked_before_and_after':True,
 'repaired_action_is_nonidentity':True,
 'compatible_integral_kernel_exponents':[2,4,8,16],
 'all_integral_cusp_and_torsion_checks':True,
 'scope':'Exact marked finite verification of the projective repair used in D50. The actual G3 arithmetic application and its compatible source maps are proved in the theorem; no arithmetic parameter vector is claimed to have been evaluated here.',
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'trials':trial_records,'certificate':chosen,
 'base_right_s':rs,'base_right_r':rr,'cycle_chords':ch,
 'moving_basis_edge_chains':[hex(c) for c in W]}
(OUT/'d_cm_projective_repair.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
