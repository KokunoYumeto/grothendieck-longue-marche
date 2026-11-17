#!/usr/bin/env python3
"""Construct the exact surface intersection constraints on the odd CM fiber.

The modular level-12 kernel is a genus-25 surface with 48 cusps.
Its rank-97 homology has a rank-50 alternating intersection form.
We compute the map forced by each affine finite f-coordinate and
write its isometry equations as explicit quadratic polynomials.
"""
import extract_cm_shadow_spaces as E
T=E.T
import numpy as np
from pathlib import Path
from collections import deque
import json

which2=T.bcases[2][0];which3=T.bcases[3][0]
edges=[(which2[q],288+which3[q]) for q in T.BQ]
adj=[[] for _ in range(480)]
for k,(u,v) in enumerate(edges):
    adj[u].append((v,k,1));adj[v].append((u,k,-1))
parent={0:None};order=[0];tree=set()
for u in order:
    for v,k,sign in adj[u]:
        if v not in parent:parent[v]=(u,k,sign);order.append(v);tree.add(k)
chords=[j for j in range(576) if j not in tree]
assert len(chords)==97 and len(parent)==480
def root_path(v):
    c=np.zeros(576,dtype=np.int16)
    while v:
        u,k,s=parent[v];c[k]=s;v=u
    return c
cycles=[]
for k in chords:
    u,v=edges[k];c=root_path(u)-root_path(v);c[k]+=1;cycles.append(c)
C=np.array(cycles,dtype=np.int16)
assert np.array_equal(C[:,chords],np.eye(97,dtype=np.int16))
omega2=np.zeros((97,97),dtype=np.int32)
for rep in T.bcases[3][1]:
    q=T.bi[rep];r=int(T.btable[q,T.br])
    a=C[:,q];b=C[:,r]
    omega2+=np.outer(a,b)-np.outer(b,a)
assert not np.any(omega2%2)
omega=omega2//2
for p in (2,3):
    basis,_=T.row_space_projection(omega,p)
    assert len(basis)==50
print("PASS integral modular ribbon intersection form: rank 50, genus 25, 48 cusps",flush=True)

def halfchain(w):
    q=0;v=np.zeros(576,dtype=np.int16)
    for j in w:
        g=T.bgs[abs(j)-1]
        h=int(T.btable[q,g if j>0 else T.binverses[g]])
        sign=-1 if abs(j)==1 else 1
        v[q]+=sign;v[h]-=sign;q=h
    return q,v
bfwords=[T.subst(w,(T.bx,T.by)) for w in T.bfloops]
def actual_cycle(w):
    q,v=halfchain(w);assert q==0 and not np.any(v%2)
    v=v//2
    assert np.array_equal(v[chords]@C,v)
    return v[chords]
K=np.array([actual_cycle(w) for w in bfwords],dtype=np.int16)
L=np.array([actual_cycle(T.subst(w,(T.bx,T.by))) for w in T.jloops],dtype=np.int16)
for p in (2,3):
    basis,_=T.row_space_projection(K,p);assert len(basis)==97
source_form=K@omega@K.T
selector=np.array([[int(T.btable[T.binverses[q],k]) for k in chords]
                   for q in range(576)],dtype=np.int16)
def effect(v):
    """Change in the 97 target homology rows for f in the level kernel."""
    full=v@C
    rows=[]
    for w in bfwords:
        q=0;out=np.zeros(97,dtype=np.int64)
        for j in w:
            if abs(j)==1:
                h=int(T.btable[q,T.bs])
                out+=full[selector[h]];q=h
            elif j==2:
                out-=full[selector[q]];q=int(T.btable[q,T.br])
            else:
                q=int(T.btable[q,T.binverses[T.br]])
                out+=full[selector[q]]
        assert q==0;rows.append(out)
    return np.array(rows,dtype=np.int64)

saved=np.load(Path(E.__file__).with_suffix(".npz"))
metadata={};arrays={"intersection":omega,"source_basis":K,"source_form":source_form,
                    "J_loop_map":L}
for p in (2,3):
    sol=saved[f"particular{p}"];N=saved[f"nullspace{p}"]
    v0=sol@L%p
    space=N@L%p
    V,_=T.row_space_projection(space,p)
    dim=len(V)
    M0=(K+effect(v0))%p
    Ms=np.array([effect(v)%p for v in V],dtype=np.int64)
    polys=[(M0@omega@M0.T-source_form)%p]
    monomials=[()]
    for j in range(dim):
        polys.append((Ms[j]@omega@M0.T+M0@omega@Ms[j].T)%p);monomials.append((j,))
    for i in range(dim):
        polys.append(Ms[i]@omega@Ms[i].T%p);monomials.append((i,i))
        for j in range(i+1,dim):
            polys.append((Ms[i]@omega@Ms[j].T+Ms[j]@omega@Ms[i].T)%p)
            monomials.append((i,j))
    positions=[(i,j) for i in range(97) for j in range(i+1,97)]
    coeff=np.array([[A[i,j] for A in polys] for i,j in positions],dtype=np.int16)
    # Over F2, x_i^2=x_i; combine before analyzing the exact finite equations.
    if p==2:
        for k,mono in enumerate(monomials):
            if len(mono)==2 and mono[0]==mono[1]:
                coeff[:,1+mono[0]]=(coeff[:,1+mono[0]]+coeff[:,k])%p
                coeff[:,k]=0
    basis,_=T.row_space_projection(coeff,p)
    constant_only=any(row[0]!=0 and not np.any(row[1:]) for row in basis)
    print("Field",p,"actual modular f-image dimension",dim,
          "quadratic monomials",len(monomials),"equation rank",len(basis),
          "constant obstruction",constant_only,flush=True)
    metadata[str(p)]={"image_dimension":dim,"monomials":monomials,
                       "equation_rank":len(basis),"constant_obstruction":constant_only}
    arrays[f"particular_image{p}"]=v0;arrays[f"image_basis{p}"]=V
    arrays[f"matrix_constant{p}"]=M0;arrays[f"matrix_coefficients{p}"]=Ms
    arrays[f"equations{p}"]=basis
np.savez_compressed(Path(__file__).with_suffix(".npz"),**arrays)
Path(__file__).with_suffix(".json").write_text(json.dumps(metadata,indent=2)+"\n")
