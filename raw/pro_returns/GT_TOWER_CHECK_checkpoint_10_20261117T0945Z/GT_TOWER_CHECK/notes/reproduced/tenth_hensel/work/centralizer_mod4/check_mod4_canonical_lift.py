#!/usr/bin/env python3
"""Full canonical cusp gate for the actual coefficient-four affine lifts.

All finite s-centralizer corrections are retained, as are all affine
increments fixing the certified binary parameter and its corrected frames.
"""
from pathlib import Path
import json
import numpy as np
from sympy import Matrix
from flint import fmpz_mat

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
src=(HERE/'lift_mask31_mod4.py').read_text()
env={'__name__':'mod4_canonical_prefix','__file__':str(HERE/'mod4_canonical_prefix.py')}
exec(compile(src.split('matrices=[];rhs=[]',1)[0],str(HERE/'lift_mask31_mod4.py'),'exec'),env)
ns=env['ns'];P=env['P'];L=env['L'];mod=env['mod'];wi=env['inverse'];subst=env['subst'];chain=env['chain']
SX=env['SX'];RX=env['RX'];jp=env['jp'];jl=env['jl']
model=np.load(HERE/'check_modular_quaternary_central_model.npz')
rel=model['central_relations'].astype(np.int64)
rows=[r for r in fmpz_mat(rel.tolist()).hnf().tolist() if any(r)]
H=Matrix(rows).T;Hi=H.inv(method='DM')
def integral(v):return all(a.q==1 for a in Hi*Matrix(np.asarray(v,dtype=np.int64).tolist()))
def embedding(v):
    w=4*Hi*Matrix(np.asarray(v,dtype=np.int64).tolist())
    assert all(a.q==1 for a in w)
    return np.array([int(a)%4 for a in w],dtype=np.int64)

bt=ns['btable'];bgs=(ns['bxq'],ns['byq']);binv=ns['binverses'];bstate=ns['bforder'];tree=ns['bftree']
ci={a:i for i,a in enumerate((q,k) for q in bstate for k,g in enumerate(bgs) if (q,k) not in tree)}
kloops=ns['bfloops'];assert len(kloops)==97
pairs=[(i,j) for i in range(97) for j in range(i+1,97)];pi={a:i for i,a in enumerate(pairs)}
proj=model['wedge_projection4']
lo=[sum(int(v%2)<<i for i,v in enumerate(row)) for row in proj]
hi=[sum(int(v//2)<<i for i,v in enumerate(row)) for row in proj]
def add(a,b,c,d):return a^c,b^d^(a&c)
def rewrite(w):
    q=0;out=[]
    for a in w:
        j=abs(a)-1
        if a>0:e=(q,j);q=int(bt[q,bgs[j]]);sign=1
        else:q=int(bt[q,binv[bgs[j]]]);e=(q,j);sign=-1
        if e in ci:out.append(sign*(ci[e]+1))
    assert q==0
    return out
def central(word):
    a=[0]*97;c=d=0
    for letter in rewrite(word):
        i=abs(letter)-1;sign=1 if letter>0 else -1
        for j in range(i+1,97):
            scalar=(-sign*a[j])%4
            if scalar:
                k=pi[i,j];u,v=lo[k],hi[k]
                if scalar==2:u,v=0,u
                elif scalar==3:v^=u
                c,d=add(c,d,u,v)
        a[i]+=sign
    assert not any(t%4 for t in a)
    return np.array([t//4 for t in a]+[((c>>i)&1)+2*((d>>i)&1) for i in range(15)],dtype=np.int64)
def sourceword(v,b=0):
    raw=np.asarray(v,dtype=np.int64)@L%4
    return tuple(z for i in range(289) for _ in range(int(raw[i])) for z in jl[i])+jp[b]
def defect(beta,A,extra=()):
    bw=sourceword(beta,252)+extra;aw=sourceword(A,0)
    return central(bw+subst(wi(bw)+aw+subst(wi(aw),RX),SX))

def unit_reduce(A,p=4):
    A=np.asarray(A,dtype=np.int64).copy()%p;row=0;piv=[]
    for col in range(A.shape[1]):
        if row==len(A):break
        nz=np.flatnonzero(A[row:,col]%2)
        if not len(nz):continue
        j=row+int(nz[0]);A[[row,j]]=A[[j,row]]
        A[row]=A[row]*pow(int(A[row,col]),-1,p)%p
        nz=np.flatnonzero(A[:,col]);nz=nz[nz!=row]
        A[nz]=(A[nz]-A[nz,col,None]*A[row])%p
        piv.append(col);row+=1
    return A,piv
def solve2(A,b):
    A=np.asarray(A,dtype=np.int64).copy()%2;b=np.asarray(b,dtype=np.int64).copy()%2
    if b.ndim==1:b=b[:,None]
    oa=A.copy();ob=b.copy();row=0;piv=[]
    for col in range(A.shape[1]):
        if row==len(A):break
        nz=np.flatnonzero(A[row:,col])
        if not len(nz):continue
        j=row+int(nz[0]);A[[row,j]]=A[[j,row]];b[[row,j]]=b[[j,row]]
        nz=np.flatnonzero(A[:,col]);nz=nz[nz!=row];A[nz]^=A[row];b[nz]^=b[row]
        piv.append(col);row+=1
    good=not np.any(b[row:]);point=np.zeros((A.shape[1],b.shape[1]),dtype=np.int64);point[piv]=b[:row]
    free=[i for i in range(A.shape[1]) if i not in piv];basis=np.zeros((len(free),A.shape[1]),dtype=np.int64)
    for k,j in enumerate(free):basis[k,j]=1;basis[k,piv]=A[:row,j]
    assert not np.any(oa@basis.T%2)
    if good:assert not np.any((oa@point-ob)%2)
    return good,point[:,0],basis,piv

S=model['s_action'].astype(np.int64)
assert np.array_equal(S%4,mod['quotient_s']%4)
R,piv=unit_reduce((S-np.eye(97,dtype=np.int64)).T)
free=[i for i in range(97) if i not in piv];rank=len(piv)
assert rank==45 and len(free)==52
tail=R[rank:,free];assert not np.any(tail%2)
_,_,null,rpiv=solve2(tail//2,np.zeros(len(tail),dtype=np.int64))
assert len(rpiv)==7 and len(null)==45
fv=[v for v in null]
for j in rpiv:
    v=np.zeros(52,dtype=np.int64);v[j]=2;fv.append(v)
fixed=[]
for v in fv:
    a=np.zeros(97,dtype=np.int64);a[free]=v;a[piv]=-R[:rank,free]@v%4
    assert not np.any(a@(S-np.eye(97,dtype=np.int64))%4)
    fixed.append(a)
fixed=np.array(fixed,dtype=np.int64)
kappas=[]
for v in fixed:
    w=tuple(t for i in range(97) for _ in range(int(v[i])) for t in kloops[i])
    k=central(w+wi(subst(w,SX)))
    assert integral(2*k);kappas.append(k)
kappas=np.array(kappas,dtype=np.int64)
reduced=fmpz_mat(np.vstack((rel,kappas)).tolist()).snf()
diagonal=[int(reduced[i,i]) for i in range(112)]
from collections import Counter
print('PASS full s-centralizer C4^45 x C2^7; reduced canonical Smith',dict(Counter(diagonal)),flush=True)

aff=np.load(HERE/'lift_mask31_mod4.npz')
base=aff['solution4'].astype(np.int64);directions=aff['lift_kernel2'].astype(np.int64)
assert directions.shape==(97,291)
d0=defect(base[97:194],base[194:]);e0=embedding(d0)
ds=[]
for i,v in enumerate(directions):
    current=(base+2*v)%4
    delta=defect(current[97:194],current[194:])-d0
    assert integral(2*delta)
    ds.append(delta)
    if i%16==15:print('CUSP affine directions collected',i+1,flush=True)
ds=np.array(ds,dtype=np.int64)
# All increments lie in the image of K^2, an abelian subgroup in the
# class-two canonical model.  Thus the central defect changes linearly.
for ids in ((0,1),(3,14,59),(0,16,32,48,64,80,96),tuple(range(97))):
    current=(base+2*directions[list(ids)].sum(axis=0))%4
    predicted=d0+ds[list(ids)].sum(axis=0)
    assert integral(defect(current[97:194],current[194:])-predicted)
all_dirs=np.vstack((ds,kappas))
images=np.array([embedding(v) for v in all_dirs],dtype=np.int64)
assert not np.any(images%2)
possible_even=not np.any(e0%2)
good=False;coeff=np.zeros(len(all_dirs),dtype=np.int64)
if possible_even:good,coeff,remaining,_=solve2((images//2).T,e0//2)
print('FULL canonical lift within fixed binary record:',good,'constant has even coordinates:',possible_even,flush=True)
save={'base_solution4':base,'affine_directions2':directions,'defect0':d0,
      'defect_directions':ds,'s_centralizer_generators4':fixed,'kappas4':kappas,
      'full_hnf':np.array(rows,dtype=np.int64),'reduced_smith':np.array(diagonal),
      'defect_embedding4':e0,'direction_embeddings4':images,'correction_coefficients':coeff}
out={'scope':'Full integral canonical cusp gate on all coefficient-four lifts with the chosen corrected binary frames.',
     's_centralizer_invariants':[4]*45+[2]*7,'reduced_canonical_smith':diagonal,
     'affine_lift_dimension':97,'full_canonical_lift_exists':bool(good),
     'constant_embedding_even':bool(possible_even)}
if good:
    answer=(base+2*coeff[:97]@directions)%4
    h=coeff[97:]@fixed%4;hw=sourceword(h)
    corrected=defect(answer[97:194],answer[194:],hw)
    assert integral(corrected)
    hnf_coordinates=Hi*Matrix(corrected.tolist())
    assert all(a.q==1 for a in hnf_coordinates)
    assert not np.any((aff['matrix4']@answer-aff['rhs4'])%4)
    save.update(solution4=answer,f4=answer[:97],beta4=answer[97:194],A4=answer[194:],
                s_correction4=h,corrected_defect=corrected,
                corrected_integral_hnf_coordinates=np.array([int(a) for a in hnf_coordinates],dtype=np.int64))
    out['selected_affine_support']=np.flatnonzero(coeff[:97]).tolist()
    out['selected_centralizer_support']=np.flatnonzero(coeff[97:]).tolist()
    out['full_integral_defect_verified_zero']=True
out['all_assertions_passed']=True
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),**save)
