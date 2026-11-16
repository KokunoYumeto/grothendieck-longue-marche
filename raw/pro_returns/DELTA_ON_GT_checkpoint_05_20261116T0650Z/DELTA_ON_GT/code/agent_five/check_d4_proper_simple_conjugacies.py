"""Exact conjugacies of all active proper normal images to one simple group.

No inference from order or perfectness alone is used.  A reference image
is proved simple by every conjugacy-class normal closure; all other
images are conjugated explicitly into that image, with equal order6048.
"""
import json
import numpy as np
from check_ferrari_d4_fox import ROOT, ADD, MUL, NEG, INV, mm as nmm

A=ADD.tolist();M=MUL.tolist();N=NEG.tolist();IV=INV.tolist()
I=(1,0,0,0,1,0,0,0,1)
def mm(a,b):
    return tuple(A[A[M[a[3*i]][b[j]]][M[a[3*i+1]][b[3+j]]]][M[a[3*i+2]][b[6+j]]]
                 for i in range(3) for j in range(3))
def mi(a):
    r=[list(a[3*i:3*i+3])+[int(i==j) for j in range(3)] for i in range(3)]
    for j in range(3):
        k=next(k for k in range(j,3) if r[k][j]);r[j],r[k]=r[k],r[j]
        r[j]=[M[IV[r[j][j]]][v] for v in r[j]]
        for k in range(3):
            if k!=j:
                f=r[k][j];r[k]=[A[x][N[M[f][y]]] for x,y in zip(r[k],r[j])]
    return tuple(v for row in r for v in row[3:])
def closure(gs):
    G=[I];seen={I}
    for h in G:
        for g in gs:
            z=mm(h,g)
            if z not in seen:seen.add(z);G.append(z)
        assert len(G)<=6048
    return G,seen

CONJ=np.array([a%3+3*(-(a//3)%3) for a in range(9)],dtype=np.int16)
def star(g):return CONJ[g].T
HB=[]
for j in range(3):
    h=np.zeros((3,3),dtype=np.int16);h[j,j]=1;HB.append(h)
for j,k in ((0,1),(0,2),(1,2)):
    for value in (1,3):
        h=np.zeros((3,3),dtype=np.int16);h[j,k]=value;h[k,j]=CONJ[value];HB.append(h)

def nullspace3(B):
    B=np.array(B,dtype=np.int16)%3;r=0;piv=[]
    for j in range(B.shape[1]):
        p=np.flatnonzero(B[r:,j])
        if not len(p):continue
        k=r+int(p[0]);B[[r,k]]=B[[k,r]];B[r]=B[r]*int(B[r,j])%3
        for k in range(len(B)):
            if k!=r:B[k]=(B[k]-B[k,j]*B[r])%3
        piv.append(j);r+=1
        if r==len(B):break
    free=[j for j in range(B.shape[1]) if j not in piv];out=[]
    for j in free:
        v=np.zeros(B.shape[1],dtype=np.int16);v[j]=1
        for k,p in enumerate(piv):v[p]=-B[k,j]%3
        out.append(v)
    return out

def invariant_form(gs):
    equations=[]
    for g in gs:
        g=np.array(g,dtype=np.int16).reshape(3,3)
        cols=[]
        for h in HB:
            z=ADD[nmm(star(g),nmm(h,g)),NEG[h]]
            cols.append(np.concatenate((z.ravel()%3,z.ravel()//3)))
        equations.extend(np.stack(cols,axis=1))
    ns=nullspace3(equations);assert len(ns)==1
    H=np.zeros((3,3),dtype=np.int16)
    for c,h in zip(ns[0],HB):H=ADD[H,MUL[c,h]]
    assert np.array_equal(H,star(H))
    mi(tuple(map(int,H.ravel()))) # nondegeneracy
    return H

def orthonormal_basis(H):
    vs=[]
    for index in range(729):
        v=np.array([(index//9**j)%9 for j in range(3)],dtype=np.int16)
        for u in vs:
            scalar=int(nmm(CONJ[u][None,:],nmm(H,v[:,None]))[0,0])
            v=ADD[v,NEG[MUL[scalar,u]]]
        norm=int(nmm(CONJ[v][None,:],nmm(H,v[:,None]))[0,0])
        assert norm in (0,1,2)
        if not norm:continue
        if norm==2:v=MUL[4,v] # norm(1+i)=2
        vs.append(v)
        if len(vs)==3:break
    assert len(vs)==3
    Q=np.stack(vs,axis=1)
    assert np.array_equal(nmm(star(Q),nmm(H,Q)),np.eye(3,dtype=np.int16))
    return Q

data=json.loads((ROOT/'d4_proper_seed_generators.json').read_text())
groups={k:[tuple(g) for g in v['normal_generators']] for k,v in data.items()}
enumerated=json.loads((ROOT/'d4_proper_seed_classification.json').read_text())
orders={str(v['representative']):v['normal_image_order'] for v in enumerated}
assert set(orders)==set(groups) and all(v==6048 for v in orders.values())
ref=groups['81'];Href=invariant_form(ref);Qref=orthonormal_basis(Href)
qr=tuple(map(int,Qref.ravel()));qri=mi(qr)
reference_generators=[mm(mm(qri,g),qr) for g in ref]
G,seen=closure(reference_generators);assert len(G)==6048
gis=[(g,mi(g)) for g in reference_generators]
unseen=set(G);classes=[]
while unseen:
    first=min(unseen);cl=[first];cs={first}
    for h in cl:
        for g,gi in gis:
            z=mm(mm(g,h),gi)
            if z not in cs:cs.add(z);cl.append(z)
    unseen.difference_update(cs)
    if first==I:nc=1
    else:
        gs=[];ss={I}
        for h in cl:
            if h not in ss:gs.append(h);ng,ss=closure(gs)
            if len(ss)==6048:break
        nc=len(ss);assert nc==6048
    classes.append({'size':len(cl),'normal_closure_order':nc})
assert len(classes)==14 and sum(c['size'] for c in classes)==6048
assert sum(c['size']==1 for c in classes)==1
reports=[]
for rep,gs in groups.items():
    H=invariant_form(gs);Q=orthonormal_basis(H);q=tuple(map(int,Q.ravel()));qi=mi(q)
    images=[mm(mm(qi,g),q) for g in gs]
    assert all(g in seen for g in images)
    # Equal order was proved by the independent complete enumeration.
    report={'representative':int(rep),'invariant_Hermitian_form':H.tolist(),
       'orthonormal_basis':Q.tolist(),'all_conjugated_generators_in_reference_simple_group':True,
       'normal_image_order':orders[rep],'simple':True}
    reports.append(report)
out={'reference_order':6048,'reference_conjugacy_classes':classes,
 'all40_nontrivial_primitive_proper_images_conjugate_to_reference':True,
 'conjugacies':reports,
 'scope':'These are centreless nonabelian simple images. Perfectness or order alone was not used to infer simplicity or a perfect simultaneous source image.'}
(ROOT/'d4_proper_simple_conjugacies.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
