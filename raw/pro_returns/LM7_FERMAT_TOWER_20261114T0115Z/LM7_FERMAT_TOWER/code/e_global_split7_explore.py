"""Exact finite coefficients for the actual global S={3,7} class-two source."""
from pathlib import Path
from itertools import combinations, product
from collections import Counter
import importlib.util
import argparse
import hashlib
import json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--source-code',type=Path,default=HERE if (HERE/'e_wild_layers.json').exists() else HERE.parents[1]/'LM7_FERMAT_TOWER/code')
BASE=ap.parse_args().source_code.resolve()
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
smith=load('split7_smith',BASE/'e_cusp_local_smith.py')
read=lambda name:json.loads((BASE/name).read_text())
mat=lambda x:s.Matrix([[s.Rational(a)for a in row]for row in x])
enc=lambda x:[[str(a)for a in row]for row in x.tolist()]
col=lambda x:s.Matrix([s.Rational(a)for a in x])
def mod3q(a,q):
    a=s.Rational(a);assert int(a.q)%3
    return int(a.p)*pow(int(a.q),-1,q)%q
def integral(M):return all(int(s.Rational(a).q)%3 for a in M)

layers=read('e_wild_layers.json')['layers']
paths=read('a_cusp_kummer.json')
first=read('a_abelian_kernel_obstruction.json')
T=s.Matrix(layers['1']['input_tau']);J=s.Matrix(layers['1']['input_c'])
labels=['A0','A1','A2','B0','B1','B2','C1','C2']
coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
pairs=list(combinations(range(10),2));E=s.eye(10)
wedge=lambda a,b:s.Matrix([a[i]*b[j]-a[j]*b[i]for i,j in pairs])
ext=lambda A:s.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]for k,l in pairs]for i,j in pairs])
U=s.Matrix([[v,-u]for u,v in coords]);j=s.Matrix.vstack(3*s.eye(2),U)
w=wedge(j[:,0],j[:,1]);pivot=pairs.index((2,4));assert w[pivot]==1
keep=[i for i in range(45)if i!=pivot];mrows=[i for i in range(45)if i!=0]
Q=s.Matrix([[int(i==k)-w[i]*int(k==pivot)for k in range(45)]for i in keep])
S=s.eye(45)[:,keep];assert Q*S==s.eye(44) and Q*w==s.zeros(44,1)
B=ext(T);D=(B/7-s.eye(45)).extract(mrows,keep)
assert integral(D)
ds=smith.local_smith(D.tolist())
L,Li,R,Ri,DD=(mat(ds[k])for k in ['left','left_inverse','right','right_inverse','diagonal_matrix'])
assert L*D*R==DD and L*Li==Li*L==R*Ri==Ri*R==s.eye(44)
assert sum(ds['valuations'])==42
Di=R*s.diag(*[s.Rational(1,3**v)for v in ds['valuations']])*L
assert D*Di==Di*D==s.eye(44)
chosen=[i for i,v in enumerate(ds['valuations'])if v]
moduli=[3**ds['valuations'][i]for i in chosen]
print('local differential Smith',dict(Counter(ds['valuations'])),flush=True)
gauge=first['first_degree_gauge_smith']
L1,Li1,R1,Ri1,D1=(mat(gauge[k])for k in ['left','left_inverse','right','right_inverse','diagonal_matrix'])
G=(s.eye(10)-T)*(s.eye(10)+J)
assert L1*G*R1==D1
representative=Li1[:,1:]
coeff=[];full_blocks=[];kcols=[]
for d,label in enumerate(labels):
    kd=col(paths['c_equivariant_cusp_tau_Kummer'][label]);kcols.append(kd)
    F=s.Matrix.hstack(*(wedge(E[:,i],E[:,d+2]).extract(mrows,[0])for i in range(10)))
    full=(L*F)[chosen,:]
    assert all(mod3q(a,moduli[r])==0 for r in range(len(chosen))for a in (full*G).row(r))
    block=(-full*kd).row_join(full*representative)
    reduced=s.Matrix([[mod3q(a,moduli[r])for a in block.row(r)]for r in range(len(chosen))])
    assert all((3*reduced[r,c])%moduli[r]==0 for r in range(len(chosen))for c in range(1,4))
    coeff.append(reduced);full_blocks.append(F)
    point=s.Matrix(coords[d]);assert all(int(x)%3==0 for x in 2*(kd[:2,:]-s.Matrix([[0,-1],[1,-1]])*point))
print('PASS all exact coefficient, gauge and finite carry identities',flush=True)
for d in range(8):
    assert full_blocks[d]*(kcols[d]-kcols[d])==s.zeros(44,1)
origin=-sum((full_blocks[d]*(-kcols[d])for d in range(8)),s.zeros(44,1))
assert integral(Di*origin)
print('PASS all eight nonzero cusp origins and the actual O inertia direction',flush=True)

blocks=np.array([[[int(x)for x in row]for row in block.tolist()]for block in coeff],dtype=np.int64)
def solve3(A,b):
    m,n=A.shape;M=np.column_stack((A%3,b%3)).copy();piv=[];r=0
    for c in range(n):
        candidates=np.flatnonzero(M[r:,c])
        if not len(candidates):continue
        k=r+int(candidates[0]);M[[r,k]]=M[[k,r]];M[r]=M[r]*int(M[r,c])%3
        for i in range(m):
            if i!=r and M[i,c]:M[i]=(M[i]-int(M[i,c])*M[r])%3
        piv.append(c);r+=1
        if r==m:break
    yes=not np.any(M[r:,-1]);x=np.zeros(n,dtype=np.int64)
    if yes:
        for i,c in enumerate(piv):x[c]=M[i,-1]
    return yes,r,x,M,piv
def kernel3(A):
    yes,r,x,M,piv=solve3(A,np.zeros(A.shape[0],dtype=np.int64));assert yes
    free=[i for i in range(A.shape[1])if i not in piv]
    N=np.zeros((A.shape[1],len(free)),dtype=np.int64)
    for k,c in enumerate(free):
        N[c,k]=1
        for i,p in enumerate(piv):N[p,k]=-M[i,c]%3
    assert not np.any(A@N%3)
    return N
eligible=[];ranks=Counter()
for a in product(range(3),repeat=8):
    block=np.tensordot(np.array(a,dtype=np.int64),blocks,axes=1)
    yes,rank,x,M,piv=solve3(block[:,1:],-block[:,0]);ranks[(yes,rank)]+=1
    if yes:eligible.append(list(a))
print('mod3 first digit systems',dict(ranks),'eligible',len(eligible),flush=True)
print('first digit vectors',eligible,flush=True)

solutions={}
for b,eps in product(range(3),repeat=2):
    pt=((eps-b)%3,-b%3);rows=[]
    for vv in product(range(3),repeat=8):
        for theta in range(3):
            if all(((pt[0]-u)*vv[i]+theta*u)%3==0 and ((pt[1]-z)*vv[i]+theta*z)%3==0
                   for i,(u,z)in enumerate(coords)):
                rows.append({'v':list(vv),'theta':theta})
    assert len(rows)==3
    expected=([{'v':[r]*8,'theta':r}for r in range(3)] if pt==(0,0) else
              [{'v':[r if coords[i]==pt else 0 for i in range(8)],'theta':0}for r in range(3)])
    assert sorted(rows,key=lambda x:x['v'])==sorted(expected,key=lambda x:x['v'])
    solutions[str((b,eps))]={'proper_point':list(pt),'solutions':rows}
print('PASS all177147 mixed-row candidates on all nine compact residue strata',flush=True)
result={'status':'PASS','smith':smith.encode(ds),'local_matrix':enc(D),'local_inverse':enc(Di),
        'quotient_map':enc(Q),'quotient_section':enc(S),'primitive_w':list(w),
        'horizontal_representative':enc(representative),'moduli':moduli,
        'coefficient_blocks':{d:enc(coeff[i])for i,d in enumerate(labels)},
        'all_first_digit_counts':{str(k):v for k,v in ranks.items()},'eligible_first_digits':eligible,
        'mod3_compact_strata':solutions,'O_particular_correction':enc(-Di*origin),
        'inputs':{name:hashlib.sha256((BASE/name).read_bytes()).hexdigest()for name in
          ['e_wild_layers.json','a_cusp_kummer.json','a_abelian_kernel_obstruction.json','e_cusp_local_smith.py']}}
HERE.joinpath('e_global_split7_explore.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
