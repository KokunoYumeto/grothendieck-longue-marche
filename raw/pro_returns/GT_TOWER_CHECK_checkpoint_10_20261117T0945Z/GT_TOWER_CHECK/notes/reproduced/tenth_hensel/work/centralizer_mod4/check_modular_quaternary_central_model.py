#!/usr/bin/env python3
"""Full canonical central kernel for B/(K' K^4), with actual K rank97.

The exterior-square coinvariants are collected over Z/4, not inferred
from their reduction mod2.  Unit row operations are represented by two
bit planes, followed by all residual even relations.
"""
from pathlib import Path
import json
import numpy as np
from flint import fmpz_mat

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
old=np.load(ROOT/'work/centralizer_code/check_modular_binary_central_obstruction.npz')
actions={'s':old['s_action'].astype(np.int64),'r':old['r_action'].astype(np.int64)}
proj2=old['wedge_projection'].astype(np.int64)
n=97;d=4656;q=15
pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
pi={a:i for i,a in enumerate(pairs)}
P0=[sum(int(a)<<i for i,a in enumerate(row)) for row in proj2]
def addpos(L,H,j,v):
    v%=4
    if not v:return L,H
    bit=1<<j;oldv=int(bool(L&bit))+2*int(bool(H&bit));new=(oldv+v)%4
    if (oldv^new)&1:L^=bit
    if (oldv^new)&2:H^=bit
    return L,H
def add(L,H,M,N):return L^M,H^N^(L&M)
def wedge4(a,b):
    L=H=0
    for i in np.flatnonzero(a%4):
        for j in np.flatnonzero(b%4):
            if i==j:continue
            ii,jj=sorted((int(i),int(j)))
            value=int(a[i])*int(b[j])*(1 if i<j else -1)
            L,H=addpos(L,H,pi[ii,jj],value)
    return L,H
piv={};even=[]
for name,A in actions.items():
    for k,(i,j) in enumerate(pairs):
        L,H=wedge4(A[i],A[j]);L,H=addpos(L,H,k,-1)
        while L:
            z=(L&-L).bit_length()-1
            if z not in piv:
                if (H>>z)&1:H^=L
                assert ((H>>z)&1)==0
                piv[z]=(L,H);break
            M,N=piv[z]
            # Subtract coefficient1 or3 at the chosen pivot.
            if not ((H>>z)&1):N^=M
            L,H=add(L,H,M,N)
        if not L:even.append(H)
    print('QUATERNARY WEDGE',name,'unit rank',len(piv),'residual even rows',len(even),flush=True)
assert len(piv)==4641
free=[i for i in range(d) if i not in piv]
assert len(free)==15
assert all(P0[j]==1<<i for i,j in enumerate(free))

def xor_project(H,coords=P0):
    out=0
    while H:
        bit=H&-H;out^=coords[bit.bit_length()-1];H^=bit
    return out
def apply(L,H,lo,hi):
    a=b=0
    while L:
        bit=L&-L;j=bit.bit_length()-1
        a,b=add(a,b,lo[j],hi[j]);L^=bit
    b^=xor_project(H,lo)
    return a,b
zero=[0]*d
B={}
for i,(L,H) in piv.items():
    a,b=apply(L,H,P0,zero);assert a==0;B[i]=b
P1=[0]*d
for i in range(d-1,-1,-1):
    if i not in piv:continue
    L,H=piv[i];P1[i]=B[i]^xor_project(L^(1<<i),P1)
for L,H in piv.values():assert apply(L,H,P0,P1)==(0,0)
even_rows=[xor_project(H) for H in even]
epiv={}
for v in even_rows:
    while v:
        i=(v&-v).bit_length()-1
        if i not in epiv:epiv[i]=v;break
        v^=epiv[i]
print('PASS exact Z4 wedge projection; independent residual even constraints',len(epiv),flush=True)
def bitvec(v):return [(v>>i)&1 for i in range(q)]
relations=[]
for A in actions.values():
    for i,row in enumerate(A):
        v=0;ids=np.flatnonzero(row%2)
        for ii,j in enumerate(ids):
            for k in ids[ii+1:]:v^=P0[pi[int(j),int(k)]]
        a=row.copy();a[i]-=1
        relations.append(a.tolist()+[2*t for t in bitvec(v)])
for i in range(q):
    a=[0]*(n+q);a[n+i]=4;relations.append(a)
for v in epiv.values():relations.append([0]*n+[2*t for t in bitvec(v)])
Z=fmpz_mat(relations);H=Z.hnf();D=Z.snf()
diag=[int(D[i,i]) for i in range(n+q)]
assert all(t>0 for t in diag)
order=1
for t in diag:order*=t
from collections import Counter
print('PASS full quaternary canonical multiplier Smith invariants',dict(Counter(diag)),'order',order,flush=True)
projection4=np.array([[((a>>i)&1)+2*((b>>i)&1) for i in range(q)] for a,b in zip(P0,P1)],dtype=np.int8)
np.savez_compressed(Path(__file__).with_suffix('.npz'),s_action=actions['s'],r_action=actions['r'],
    wedge_projection4=projection4,wedge_even_relations=np.array([bitvec(v) for v in epiv.values()],dtype=np.int8),
    central_relations=np.array(relations,dtype=np.int64),smith=np.array(diag,dtype=np.int64),
    hnf=np.array(H.tolist(),dtype=np.int64))
out={'scope':'Full integral canonical multiplier of B/(Kprime K^4).',
     'rank_K':n,'unit_wedge_relation_rank':len(piv),'residual_even_relation_rank':len(epiv),
     'full_smith_invariants':diag,'canonical_multiplier_order':order,'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
