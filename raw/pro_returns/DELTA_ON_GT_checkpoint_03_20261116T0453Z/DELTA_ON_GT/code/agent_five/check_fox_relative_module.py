"""Exact characteristic-three Fox module over the genuine L quotient of order216.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026.
Run: python -I -B check_fox_relative_module.py
"""
from pathlib import Path
import json,numpy as np

I=(1,0,0,0,1,0,0,0,1)
def mm(a,b):return tuple(sum(a[3*i+k]*b[3*k+j]for k in range(3))%3 for i in range(3)for j in range(3))
gg=((1,1,0,0,1,0,0,0,1),(1,0,0,2,1,0,0,0,1),(1,1,1,0,1,0,0,0,1))
Q=[I];qi={I:0};pos=0
while pos<len(Q):
    a=Q[pos];pos+=1
    for b in gg:
        z=mm(a,b)
        if z not in qi:qi[z]=len(Q);Q.append(z)
assert len(Q)==216
n=len(Q);dim=3*n
mult=np.array([[qi[mm(a,b)]for b in Q]for a in Q],dtype=np.int16)
invs=np.array([next(j for j in range(n)if mult[i,j]==0)for i in range(n)],dtype=np.int16)
gens=[qi[g]for g in gg]
relators=((1,2,1,-2,-1,-2),(2,3,2,-3,-2,-3),(1,3,-1,-3),(1,2,3)*4)
rows=[]
for word in relators:
    row=np.zeros(dim,dtype=np.int16);q=0
    for x in word:
        j=abs(x)-1
        if x>0:
            row[j*n+q]+=1;q=int(mult[q,gens[j]])
        else:
            q=int(mult[q,invs[gens[j]]]);row[j*n+q]-=1
    assert q==0
    row%=3
    for h in range(n):
        translated=np.zeros(dim,dtype=np.int16)
        for j in range(3):translated[j*n+mult[h]]=row[j*n:(j+1)*n]
        rows.append(translated)
R=np.array(rows,dtype=np.int16)
assert R.shape==(864,648)
pivots=[];rank=0
for col in range(dim):
    candidates=np.flatnonzero(R[rank:,col])
    if not len(candidates):continue
    k=rank+int(candidates[0]);R[[rank,k]]=R[[k,rank]]
    if R[rank,col]==2:R[rank]=(2*R[rank])%3
    indices=np.flatnonzero(R[:,col]);indices=indices[indices!=rank]
    R[indices]=(R[indices]-R[indices,col,None]*R[rank])%3
    pivots.append(col);rank+=1
free=[j for j in range(dim)if j not in set(pivots)]
d=len(free)
T=np.zeros((dim,d),dtype=np.int16)
T[free]=np.eye(d,dtype=np.int16)
for i,j in enumerate(pivots):T[j]=(-R[i,free])%3
assert not np.any(np.array(rows,dtype=np.int16)@T%3)
boundary=np.zeros((dim,n),dtype=np.int16)
for j in range(3):
    for q in range(n):
        boundary[j*n+q,q]-=1
        boundary[j*n+q,mult[q,gens[j]]]+=1
boundary%=3
assert not np.any(np.array(rows,dtype=np.int16)@boundary%3)
assert np.array_equal(T@boundary[free]%3,boundary)
actions=np.stack([T[np.array([j//n*n+int(mult[h,j%n])for j in free])].T for h in range(n)])
assert np.array_equal(actions[0],np.eye(d,dtype=np.int16))
for g in gens:
    for h in gens:assert np.array_equal(actions[g]@actions[h]%3,actions[mult[g,h]])
zero=np.zeros(d,dtype=np.int16)
lifts=[(T[j*n].copy(),gens[j])for j in range(3)]
def am(a,b):return ((a[0]+actions[a[1]]@b[0])%3,int(mult[a[1],b[1]]))
def ai(a):
    q=int(invs[a[1]])
    return ((-actions[q]@a[0])%3,q)
def aw(word):
    a=(zero.copy(),0)
    for x in word:a=am(a,lifts[x-1]if x>0 else ai(lifts[-x-1]))
    return a
for word in relators:
    v,q=aw(word);assert q==0 and not np.any(v)
Xwords=((1,1),(2,2),(3,3),(1,2,1)*2,(3,2,3)*2)
XX=[aw(w)for w in Xwords]

def basis(rows0):
    piv={}
    for vv in rows0:
        v=np.array(vv,dtype=np.int16)%3
        for j,w in sorted(piv.items()):
            if v[j]:v=(v-v[j]*w)%3
        nz=np.flatnonzero(v)
        if len(nz):
            j=int(nz[0]);v=(v*(1 if v[j]==1 else 2))%3;piv[j]=v
    return [piv[j]for j in sorted(piv)]
def span_contains(B,v):return len(basis(B+[v]))==len(B)
def base_group(gens0):
    H=[0];seen={0};pos=0
    while pos<len(H):
        h=H[pos];pos+=1
        for g in gens0:
            z=int(mult[h,g])
            if z not in seen:seen.add(z);H.append(z)
    return H
def base_comm(g,h):return int(mult[mult[mult[g,h],invs[g]],invs[h]])
def base_derived(H,gens0):
    cg=list({base_comm(g,h)for g in H for h in gens0})
    return base_group(cg)
def subgroup_data(ag):
    sec={0:zero.copy()};todo=[0]
    while todo:
        h=todo.pop()
        for v,g in ag:
            z=int(mult[h,g])
            if z not in sec:sec[z]=(sec[h]+actions[h]@v)%3;todo.append(z)
    loops=[]
    for h in sec:
        for v,g in ag:loops.append((sec[h]+actions[h]@v-sec[int(mult[h,g])])%3)
    U=basis(loops)
    assert all(span_contains(U,actions[g]@v%3)for v in U for _,g in ag)
    return list(sec),sec,U
def module_comm(B,H):
    return basis([(actions[h]@v-v)%3 for h in H for v in B])

reports=[]
for ii,jj in ((0,1),(2,3),(3,4)):
    ag=[XX[ii],XX[jj]]
    H,sec,U=subgroup_data(ag)
    HD=base_derived(H,[x[1]for x in ag]);HDD=base_derived(HD,HD)
    U1=module_comm(U,H)
    U2=module_comm(U1,HD)
    full_kernel_second_base_action_rank=len(basis([(actions[h]@v-v)%3 for h in HDD for v in U]))
    bad=[]
    for h in HDD:
        for v in U2:
            if np.any((actions[h]@v-v)%3):
                bad.append({'base_element':h,'base_matrix':Q[h],
                            'vector':v.tolist(),'commutator':((actions[h]@v-v)%3).tolist()})
                break
        if bad:break
    reports.append({'pair':[ii+1,jj+1],'base_orders':[len(H),len(HD),len(HDD)],
                    'relative_kernel_dimension':len(U),'U1_dimension':len(U1),'U2_dimension':len(U2),
                    'actual_pair_image_order':len(H)*3**len(U),
                    'second_base_derived_action_rank_on_entire_pair_kernel':full_kernel_second_base_action_rank,
                    'second_derived_abelian_certified':len(HDD)<=2 and full_kernel_second_base_action_rank==0,
                    'second_derived_provably_nonnilpotent':bool(bad),
                    'witness':bad[:1]})

out=Path(__file__).with_name('fox_relative_module.npz')
np.savez_compressed(out,quotient_map=T,actions=actions,Q=np.array(Q,dtype=np.int8),
                    mult=mult,inverses=invs,gens=np.array(gens),free=np.array(free))
print(json.dumps({'base_order':n,'Fox_matrix_shape':[864,648],'Fox_relation_rank':rank,
                  'Fox_quotient_dimension':d,'kernel_homology_dimension':d-(n-1),
                  'all_presentation_relators_vanish_in_affine_extension':True,
                  'Fox_boundary_compatibility_verified':True,
                  'pair_reports':reports,
                  'criterion':'U1=[U,H] lies in P prime; U2=[U1,H prime] lies in P second derived. If a base element in H second derived acts nontrivially on U2, the second derived group has nontrivial coprime action and cannot be nilpotent.',
                  'scope':'An actual finite quotient of L via the Fox relation module. No finite parameter or automorphism is declared a GT lift.'},indent=2))
