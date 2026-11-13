#!/usr/bin/env python3
from pathlib import Path
from itertools import product
from collections import Counter
import json
import hashlib
import numpy as np

HERE=Path(__file__).resolve().parent
d=json.loads((HERE/'a_toric_wild.json').read_text())
labels=['A0','A1','A2','B0','B1','B2','C1','C2']
blocks=np.array([[[int(x)for x in row]for row in d['polynomial_blocks'][k]]for k in labels],dtype=np.int64)

def solve3(A,b):
    m,n=A.shape
    E=np.column_stack((A%3,b%3)).copy();piv=[];r=0
    for c in range(n):
        possible=np.flatnonzero(E[r:,c])
        if not len(possible):continue
        q=r+int(possible[0]);E[[r,q]]=E[[q,r]]
        E[r]=E[r]*int(E[r,c])%3
        for i in range(m):
            if i!=r and E[i,c]:E[i]=(E[i]-int(E[i,c])*E[r])%3
        piv.append(c);r+=1
        if r==m:break
    ok=not np.any(E[r:,-1])
    x=np.zeros(n,dtype=np.int64)
    if ok:
        for i,c in enumerate(piv):x[c]=E[i,-1]
    return ok,r,x,E,piv

def kernel3(A):
    ok,r,x,E,piv=solve3(A,np.zeros(A.shape[0],dtype=np.int64));assert ok
    free=[i for i in range(A.shape[1])if i not in piv]
    N=np.zeros((A.shape[1],len(free)),dtype=np.int64)
    for j,c in enumerate(free):
        N[c,j]=1
        for i,q in enumerate(piv):N[q,j]=-E[i,c]%3
    assert not np.any(A@N%3)
    return N

eligible=[];ranks=Counter();counts=Counter()
nonunit_counts=Counter();nonunit_ranks=Counter();nonunit_bad=[];nonunit_good=[]
for a in product(range(3),repeat=8):
    BB=np.tensordot(np.array(a,dtype=np.int64),blocks,axes=1)%3
    ok,rank,x,_,_=solve3(BB[:,1:],-BB[:,0])
    counts[ok]+=1;ranks[(ok,rank)]+=1
    if ok:eligible.append(list(a))
    ok3,rk3,_,_,_=solve3(BB[11:,1:],-BB[11:,0])
    nonunit_counts[ok3]+=1;nonunit_ranks[(ok3,rk3)]+=1
    if not ok3:nonunit_bad.append(list(a))
    else:nonunit_good.append(list(a))
print('mod3 consistency counts',counts)
print('ranks',ranks)
print('eligible',eligible)
print('relative multiples of3',nonunit_counts,nonunit_ranks)

# Exact closed form for all nonunit relative vectors A=3a.
# The sole horizontal scalar is p_6+p_8 modulo three.
C=blocks[:,11:,0].T%3;D=blocks[:,11:,6].T%3
ell=np.array([0,0,0,0,0,1,0,1,0],dtype=np.int64)
assert np.array_equal(blocks[:,11:,1:].transpose(1,0,2)%3,D[:,:,None]*ell[None,None,:]%3)
nonunit_matrices=[(C+k*D)%3 for k in range(3)]
nonunit_kernels=[kernel3(A)for A in nonunit_matrices]
assert all(N.shape==(8,5)for N in nonunit_kernels)
common=kernel3(np.vstack((C,D)))
assert common.shape==(8,3)
for k in range(3):
    for l in range(k+1,3):
        assert kernel3(np.vstack((nonunit_matrices[k],nonunit_matrices[l]))).shape==(8,3)
for a in product(range(3),repeat=8):
    aa=np.array(a,dtype=np.int64)
    yes=any(not np.any(M@aa%3)for M in nonunit_matrices)
    assert yes==(list(a)in nonunit_good)
assert len(nonunit_good)==3*3**5-2*3**3==675

digits=np.array(list(product(range(3),repeat=8)),dtype=np.int64)
nextblocks=np.tensordot(digits,blocks,axes=(1,0))
all_lifts=[];total=0;witness_checks=0
for a0 in eligible:
    aa=np.array(a0,dtype=np.int64)
    if not np.any(aa):
        goodset={tuple(a)for a in nonunit_good}
        indices=[k for k,a in enumerate(digits)if tuple(a)in goodset]
        total+=len(indices)
        all_lifts.append({'first_digit':a0,'next_digits':indices,'horizontal_torsion_rank':3})
        continue
    BB=np.tensordot(aa,blocks,axes=1)
    ok,r,x0,_,_=solve3(BB[:,1:],-BB[:,0]);assert ok
    N=kernel3(BB[:,1:]);D0=BB[11:,1:]%3
    Z=kernel3(D0.T).T
    tmp=BB[11:,1:]@x0+BB[11:,0];assert not np.any(tmp%3)
    t0=tmp//3
    tmp=BB[11:,1:]@N;assert not np.any(tmp%3)
    Q=tmp//3
    Ac=(np.einsum('am,kmn,nr->kar',Z,nextblocks[:,11:,1:],N)+(Z@Q)[None,:,:])%3
    bc=(np.einsum('am,kmn,n->ka',Z,nextblocks[:,11:,1:],x0)
        +np.einsum('am,km->ka',Z,nextblocks[:,11:,0])+(Z@t0)[None,:])%3
    indices=[];witnesses=[]
    for k in range(len(digits)):
        yes,rr,xx,_,_=solve3(Ac[k],-bc[k])
        if yes:
            indices.append(k)
            if len(witnesses)<2 or k==len(digits)-1:
                p0=x0+N@xx
                defect=t0+Q@xx+nextblocks[k,11:,1:]@p0+nextblocks[k,11:,0]
                okp,_,p1,_,_=solve3(D0,-defect);assert okp
                pp=p0+3*p1
                full=np.tensordot(aa+3*digits[k],blocks,axes=1)
                check=full[:,1:]@pp+full[:,0]
                assert not np.any(check[:11]%3) and not np.any(check[11:]%9)
                witnesses.append({'next_digit_index':k,'horizontal':pp.tolist()})
                witness_checks+=1
    Ft=BB[:,1:4].copy();assert not np.any(Ft[11:]%3)
    Ft[11:]//=3
    torsrank=3-solve3(Ft,np.zeros(15,dtype=np.int64))[1]
    all_lifts.append({'first_digit':a0,'next_digits':indices,'horizontal_torsion_rank':torsrank,'witnesses':witnesses,
        'first_digit_horizontal_solution':x0.tolist(),
        'first_digit_horizontal_kernel':N.tolist(),
        'four_integer_rows':BB[11:,:].tolist(),
        'mod3_four_row_matrix':D0.tolist(),'left_kernel':Z.tolist(),
        'divided_defect':t0.tolist(),'divided_kernel_matrix':Q.tolist()})
    total+=len(indices)
    print('first digit',a0,'admissible next digits',len(indices),'horizontal torsion',torsrank,flush=True)
print('complete mod9 relative image size',total,'out of',9**8)
print('lift witnesses',witness_checks)
summary=Counter((len(x['next_digits']),x['horizontal_torsion_rank'])for x in all_lifts)
assert summary==Counter({(243,0):54,(486,3):6,(675,3):1})
assert total==16713
print('PASS all relative residues modulo9; all finite horizontal kernels and closed nonunit formula')
out={'status':'PASS','counts':{str(k):v for k,v in counts.items()},
     'ranks':{str(k):v for k,v in ranks.items()},'eligible':eligible,
     'nonunit_counts':{str(k):v for k,v in nonunit_counts.items()},
     'nonunit_ranks':{str(k):v for k,v in nonunit_ranks.items()},'nonunit_bad':nonunit_bad,
     'all_mod9_relative_lifts':all_lifts,'mod9_relative_image_size':total,'witness_checks':witness_checks,
     'nonunit_horizontal_linear_form':ell.tolist(),
     'nonunit_constant_matrix':C.tolist(),'nonunit_linear_matrix':D.tolist(),
     'nonunit_three_matrices':[M.tolist()for M in nonunit_matrices],
     'nonunit_three_kernel_bases':[M.tolist()for M in nonunit_kernels],
     'nonunit_common_kernel':common.tolist(),
     'relative_image_summary':[
       {'first_digit_count':v,'second_digit_count':k[0],'horizontal_C3_rank':k[1]}
       for k,v in sorted(summary.items())],
     'input_hash':hashlib.sha256((HERE/'a_toric_wild.json').read_bytes()).hexdigest()}
(HERE/'a_toric_residues.json').write_text(json.dumps(out,indent=2)+'\n')
