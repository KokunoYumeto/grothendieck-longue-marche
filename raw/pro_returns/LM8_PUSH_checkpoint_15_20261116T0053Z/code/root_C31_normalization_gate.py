#!/usr/bin/env python3
"""Exact retained-frame calculation for the C31 normalization ambiguity.

The first finite pure abelianization has exponent12 but inertia order24.
Normalization therefore changes some retained values. This program checks
that it changes BOTH descended frames by the same cusp inner factor, which
can be removed before the second, order12-invisible normalization.
"""
from pathlib import Path
import hashlib,json,math,re
CODE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
seedp=CODE/'pbc_hopf_joint_seed.json';seed=json.loads(seedp.read_text())
n=len(seed['s']);one=list(range(1,n+1))
def mul(a,b):return [b[i-1] for i in a]
def inv(a):
    b=[0]*len(a)
    for i,v in enumerate(a,1):b[v-1]=i
    return b
def power(a,k):
    if k<0:return power(inv(a),-k)
    z=list(range(1,len(a)+1))
    while k:
        if k&1:z=mul(z,a)
        a=mul(a,a);k//=2
    return z
def product(*a):
    z=list(range(1,len(a[0])+1))
    for x in a:z=mul(z,x)
    return z
def order(a):
    seen=set();z=1
    for i in range(1,len(a)+1):
        if i in seen:continue
        j=i;k=0
        while j not in seen:seen.add(j);k+=1;j=a[j-1]
        z=math.lcm(z,k)
    return z
s,r=seed['s'],seed['r'];tau=mul(s,r);z=inv(r)
beta,A,f=seed['beta'],seed['A'],seed['f'];u=mul(inv(A),beta)
assert power(s,2)==power(r,3)==one
assert product(beta,s,inv(beta))==mul(s,inv(f))
assert product(A,r,inv(A))==mul(f,r)
assert order(tau)==24
x1=power(mul(r,s),2);y1=power(tau,2);assert order(x1)==order(y1)==12
triple=[s,tau,z];pairs=[(i,j) for i in range(3) for j in range(3) if i!=j]
def values(v,u):return [v,u,inv(v),mul(u,inv(v)),inv(u),mul(v,inv(u))]
target=values(beta,u);branches=[]
for a in (0,12):
    actual=[product(power(triple[j],-a),w,power(triple[i],a)) for (i,j),w in zip(pairs,target)]
    common=power(tau,-a);v=mul(common,beta)
    assert actual==values(v,u)
    # u is the product of the (tau,z) and (s,tau) evaluations.
    assert mul(actual[3],actual[0])==u
    Bnew=actual[0];Anew=mul(Bnew,inv(u))
    assert Bnew==mul(common,beta) and Anew==mul(common,A)
    assert mul(common,tau)==mul(tau,common)
    assert product(inv(common),Bnew)==beta and product(inv(common),Anew)==A
    branches.append(dict(normalizing_exponent_mod24=a,common_cusp_power_mod24=(-a)%24,
                         beta_frame=Bnew,r_frame=Anew,u_value=u,
                         both_frames_have_same_left_factor=True,
                         all_six_values_match_exact_gauge=True,
                         removing_inner_factor_restores_C27_frames=True))
def mm(a,b,m):return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%m for i in range(2) for j in range(2))
def mi(a,m):return (a[3],-a[1]%m,-a[2]%m,a[0])
def mp(a,k,m):
    if k<0:return mp(mi(a,m),-k,m)
    q=(1,0,0,1)
    while k:
        if k&1:q=mm(q,a,m)
        a=mm(a,a,m);k//=2
    return q
signed=[]
for m in (3,4):
    S=(0,1,m-1,0);T=(1,m-1,0,1);Z=mi(mm(S,T,m),m)
    assert all(mp(v,12,m)==(1,0,0,1) for v in (S,T,Z))
    signed.append(dict(modulus=m,all_three_inertia_twelfth_powers_identity=True))
gp=CODE/'pbc_iterated_joint.g';text=gp.read_text();big=[]
for key in ('PBC_ind_s','PBC_ind_r'):
    match=re.search(key+r':=PermList\((\[[^;]+\])\);;',text);assert match
    big.append(json.loads(match.group(1)))
s2,r2=big;assert len(s2)==len(r2)==2592
assert power(s2,2)==power(r2,3)==list(range(1,2593))
x2=power(mul(r2,s2),2);y2=power(mul(s2,r2),2)
assert order(x2)==order(y2)==24
out=dict(status='PASS',seed_sha256=sha(seedp),iterated_finite_program_sha256=sha(gp),checker_sha256=sha(__file__),
         first_source_degree=2592,first_inertia_orders=[24,24],
         first_pure_abelianization='C12^2, independently retained GAP calculation in pbc_hopf_iterated_joint.out',
         next_source_degree=n,next_cusp_order=24,next_inertia_orders=[12,12],
         normalization_branches=branches,signed_first_level=signed,
         scope='Exact normalization/frame comparison only. Full existence still requires the original central lifting obstruction to vanish.')
(CODE.parent/'notes/root_C31_normalization_gate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='normalization_branches'},indent=2))
print('BOTH_NORMALIZATION_BRANCHES_RESTORE_EXACT_C27_FRAMES')
