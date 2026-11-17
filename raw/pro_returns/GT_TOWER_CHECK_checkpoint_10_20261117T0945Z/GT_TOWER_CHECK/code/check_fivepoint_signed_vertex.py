#!/usr/bin/env python3
"""Compare the actual eight-map module with the modular C3 vertex module."""
from pathlib import Path
import json
import numpy as np

HERE=Path(__file__).resolve().parent
data=np.load(HERE/'check_fivepoint_signed_module.npz')
meta=json.loads((HERE/'check_fivepoint_signed_module.json').read_text())
I=(1,0,0,1)
def mul(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%12
                 for i in range(2) for j in range(2))
def inv(a):return (a[3],-a[1]%12,-a[2]%12,a[0])
def canon(a):return min(a,tuple(-z%12 for z in a))
def bmul(a,b):return canon(mul(a,b))
def inverse(w):return tuple(-z for z in reversed(w))
def subst(w,images):return tuple(z for a in w for z in
    (images[a-1] if a>0 else inverse(images[-a-1])))
S=canon((0,1,11,0));R=canon((0,11,1,11));BI=canon(I)
B=[BI];bi={BI:0}
for q in B:
    for g in (S,R):
        v=bmul(q,g)
        if v not in bi:bi[v]=len(B);B.append(v)
assert len(B)==576
table=np.array([[bi[bmul(a,b)] for b in B] for a in B],dtype=np.int16)
invs=np.array([bi[canon(inv(a))] for a in B],dtype=np.int16)
bs,br=bi[S],bi[R]
H=[0,br,int(table[br,br])]
coset={};reps=[]
for q in range(576):
    if q in coset:continue
    i=len(reps);reps.append(q)
    for h in H:coset[int(table[q,h])]=i
assert len(reps)==192
perms=np.array([[coset[int(table[q,t])] for t in reps] for q in range(576)],dtype=np.int16)
bx=(-2,1,-2,1);by=(1,)+bx+(1,)
def b_eval(w):
    q=0;row=np.zeros(192,dtype=np.int16)
    for z in w:
        g=(bs,br)[abs(z)-1]
        if z>0:
            if z==2:row[perms[q,0]]+=1
            q=int(table[q,g])
        else:
            q=int(table[q,invs[g]])
            if z==-2:row[perms[q,0]]-=1
    return q,row%3

ktable=data['modular_table'];kgi=data['modular_generators'];kchords=data['modular_chords']
paths={0:()};order=[0]
for q in order:
    for j,g in enumerate(kgi):
        v=int(ktable[q,g])
        if v not in paths:paths[v]=paths[q]+(j+1,);order.append(v)
kloops=[paths[int(q)]+(int(j)+1,)+inverse(paths[int(ktable[q,kgi[j]])]) for q,j in kchords]
V=[]
for w in kloops:
    q,row=b_eval(subst(w,(bx,by)))
    assert q==0;V.append(row)
V=np.array(V,dtype=np.int16)
Jvertex=[]
for w in meta['Schreier_words']:
    q,row=b_eval(subst(w,(bx,by)))
    assert q==0;Jvertex.append(row)
Jvertex=np.array(Jvertex,dtype=np.int16)
assert np.array_equal(data['modular_restriction']@V%3,Jvertex)
factor=data['modular_factor']@V%3
assert np.array_equal(data['common_projection']@factor%3,Jvertex)

def rref(A):
    A=(A%3).copy();r=0;piv=[]
    for c in range(A.shape[1]):
        if r==len(A):break
        nz=np.flatnonzero(A[r:,c])
        if not len(nz):continue
        j=r+int(nz[0]);A[[r,j]]=A[[j,r]]
        A[r]=A[r]*pow(int(A[r,c]),-1,3)%3
        nz=np.flatnonzero(A[:,c]);nz=nz[nz!=r]
        A[nz]=(A[nz]-A[nz,c,None]*A[r])%3
        piv.append(c);r+=1
    return A[:r],piv
def kernel_rows(A):
    # Rows v with v A=0.
    RR,piv=rref(A.T);free=[j for j in range(A.shape[0]) if j not in piv]
    result=np.zeros((len(free),A.shape[0]),dtype=np.int16)
    for k,j in enumerate(free):
        result[k,j]=1;result[k,piv]=-RR[:,j]%3
    assert not np.any(result@A%3)
    return result

kr=len(rref(V)[0]);jr=len(rref(Jvertex)[0]);fr=len(rref(factor)[0])
assert kr==96 and jr==fr
kernel=kernel_rows(factor)
assert len(kernel)==97-jr
kernel_rref,kernel_piv=rref(kernel)
actions={}
for name,g in [('s',bs),('r',br)]:
    action=data['quotient_'+name]
    pushed=np.empty_like(factor);pushed[:,perms[g]]=factor
    assert np.array_equal(action@factor%3,pushed)
    rows=kernel_rref@action%3
    coeff=rows[:,kernel_piv]
    assert np.array_equal(coeff@kernel_rref%3,rows)
    actions[name]=coeff
print('PASS literal K-rank97-to-vertex192 map has rank',kr,flush=True)
print('PASS actual J restriction and common source97-to-vertex192 map have rank',jr,flush=True)
print('PASS exact factorization and B-equivariance checked coefficientwise',flush=True)
print('Common-source vertex kernel dimension',len(kernel),'s=',actions['s'].tolist(),'r=',actions['r'].tolist(),flush=True)

out={'scope':'Exact module comparison; no full genuine-source parity exclusion',
     'K_free_rank':97,'K_vertex_rank':kr,'J_vertex_rank':jr,
     'common_module_dimension':97,'vertex_kernel_dimension':len(kernel),
     'vertex_kernel_s':actions['s'].tolist(),'vertex_kernel_r':actions['r'].tolist(),
     'kernel_pivot_coordinates':kernel_piv,'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),
    K_vertex=V,J_vertex=Jvertex,common_vertex_factor=factor,
    common_vertex_kernel=kernel_rref,kernel_s=actions['s'],kernel_r=actions['r'],
    B_table=table,B_s=bs,B_r=br,B_matrices=np.array(B),vertex_permutations=perms,
    K_schreier_words=np.array([json.dumps(w) for w in kloops]))
print('PASS exact retained source-to-vertex morphisms saved',flush=True)
