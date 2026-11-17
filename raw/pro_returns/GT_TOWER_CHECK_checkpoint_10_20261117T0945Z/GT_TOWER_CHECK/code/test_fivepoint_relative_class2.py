#!/usr/bin/env python3
"""Finite multiplier-one pentagon/CM test in the actual relative class-two cover.

Every f-record is an element of the ACTUAL derived subgroup of
F2/(gamma3(J2) J2^3), J2=kernel(F2->C4^2).  The source variables are
its class-two BCH coordinates.  A surviving record is not asserted
to lift to a profinite gentle element.
"""
from pathlib import Path
import json
from functools import lru_cache
from itertools import product
import numpy as np
from fivepoint_relative_tools import (abelian_schreier, fibre_action,
                                     subst, inverse, reduce_word)

HERE = Path(__file__).resolve().parent
data = np.load(HERE / 'build_fivepoint_relative_class2.npz')
description = json.loads((HERE / 'build_fivepoint_relative_class2.json').read_text())
P_f = data['projection'].astype(np.int64)
linear = data['linear'].astype(np.int64)
basis_sources = data['linear_basis_sources']
Rcentral = data['relator_central'].astype(np.int64)
central_basis = data['central_basis'].astype(np.int16)
central_pivots = data['central_pivots'].astype(int)
central_free = np.array([i for i in range(3160) if i not in set(central_pivots)], dtype=int)
assert len(central_free) == 1429
# The nonzero eliminated rows need not be inferred from the numerical P:
# recover its free columns using the original echelon algorithm.
linear_pivots = []
echelon = []
for original in linear:
    row = original.copy()
    for p,b in zip(linear_pivots,echelon):
        row = (row-int(row[p])*b)%3
    nz=np.flatnonzero(row)
    if len(nz):
        p=int(nz[0]);row=row*pow(int(row[p]),-1,3)%3
        linear_pivots.append(p);echelon.append(row)
assert len(linear_pivots)==66
linear_free=[i for i in range(129) if i not in linear_pivots]
assert np.array_equal(P_f[linear_free],np.eye(63,dtype=np.int64))


def inverse_matrix(a,p=3):
    a=np.array(a,dtype=np.int64).copy();n=len(a)
    a=np.concatenate([a,np.eye(n,dtype=np.int64)],axis=1)
    for c in range(n):
        nz=np.flatnonzero(a[c:,c]);assert len(nz)
        r=c+int(nz[0]);a[[c,r]]=a[[r,c]]
        a[c]=a[c]*pow(int(a[c,c]),-1,p)%p
        ix=np.flatnonzero(a[:,c]);ix=ix[ix!=c]
        a[ix]=(a[ix]-a[ix,c,None]*a[c])%p
    return a[:,n:]


square_inverse=inverse_matrix(linear[basis_sources][:,linear_pivots])
P=np.zeros((146,80),dtype=np.int64)
P[:129,:63]=P_f;P[129:,63:]=np.eye(17,dtype=np.int64)
shifts=np.zeros((146,3160),dtype=np.int64)
shifts[linear_pivots]=-square_inverse@Rcentral[basis_sources]%3
upper=np.triu_indices(80,1)


def central_reduce(rows):
    rows=np.array(rows,dtype=np.int16).copy()%3
    one=rows.ndim==1
    if one:rows=rows[None,:]
    for p,b in zip(central_pivots,central_basis):
        ix=np.flatnonzero(rows[:,p])
        if len(ix):rows[ix]=(rows[ix]-rows[ix,p,None]*b)%3
    assert not np.any(rows[:,central_pivots])
    result=rows[:,central_free]
    return result[0] if one else result


def log_j_word(word):
    v=np.zeros(146,dtype=np.int64)
    z=np.zeros((146,146),dtype=np.int64)
    for letter in word:
        j=abs(letter)-1;sign=1 if letter>0 else -1
        z[:,j]+=2*sign*v;z[j,:]-=2*sign*v
        v[j]+=sign
    v%=3;z%=3
    projected=P.T@z@P%3
    return v@P%3,(projected[upper]+v@shifts)%3


_,_,floops,rewrite_f=abelian_schreier(3)
_,_,bloops,rewrite_b=abelian_schreier(2)
_,_,source_loops,rewrite_source=abelian_schreier(2)
assert source_loops==bloops and len(source_loops)==17


@lru_cache(maxsize=None)
def normal_form(word):
    # Exact free-by-free collection f*b.  Base conjugation is the
    # specified actual Artin action from the six-relator presentation.
    f=();b=()
    for letter in word:
        if abs(letter)<=2:
            b=reduce_word(b+(letter,))
        else:
            action=fibre_action(b)
            j=abs(letter)-3
            image=action[j] if letter>0 else inverse(action[j])
            f=reduce_word(f+image)
    return f,b


def target_j_word(word):
    f,b=normal_form(tuple(word))
    fq,fw=rewrite_f(f);bq,bw=rewrite_b(b)
    assert fq==0 and bq==0
    return fw+tuple((129+abs(i))*(1 if i>0 else -1) for i in bw)


a,b,x,y,z=(1,),(2,),(3,),(4,),(5,)
x12=(-5,-4,-3,-2,-1)
z0=inverse(x12+b)
pairwords=[(x12,b+y),(a+b,z),(b,z),(x12+a,y+z),(x12,b),
           (b,x12),(z0,x12),(b,z0)]
mapped_linear=[];mapped_central=[]
for k,pair in enumerate(pairwords):
    lin=[];cent=[];lengths=[]
    for w in source_loops:
        target=target_j_word(subst(w,pair))
        lengths.append(len(target))
        v,c=log_j_word(target)
        lin.append(v);cent.append(c)
    mapped_linear.append(lin);mapped_central.append(cent)
    print('PASS actual insertion',k+1,'on all17 source loops; lengths sum/max',sum(lengths),max(lengths),flush=True)
mapped_linear=np.array(mapped_linear,dtype=np.int16)
mapped_central=np.array(mapped_central,dtype=np.int16)
assert mapped_linear.shape==(8,17,80)

# Actual abelianization of the source quotient is C12^2; f is in its
# derived subgroup exactly when these two residual C3 coordinates vanish.
source_abel=np.array([[sum(1 if j==i else -1 if j==-i else 0 for j in w)//4
                       for i in (1,2)] for w in source_loops],dtype=np.int16)%3
linear_equations=np.concatenate([
    source_abel.T,
    (mapped_linear[4]+mapped_linear[5]).T%3,
    (mapped_linear[6]+mapped_linear[7]+mapped_linear[4]).T%3,
    (mapped_linear[0]+mapped_linear[1]-mapped_linear[4]-mapped_linear[3]-mapped_linear[2]).T%3])


def nullspace(a):
    a=np.array(a,dtype=np.int16).copy()%3;r=0;pivots=[]
    for c in range(a.shape[1]):
        nz=np.flatnonzero(a[r:,c])
        if not len(nz):continue
        j=r+int(nz[0]);a[[r,j]]=a[[j,r]]
        a[r]=a[r]*pow(int(a[r,c]),-1,3)%3
        ix=np.flatnonzero(a[:,c]);ix=ix[ix!=r]
        a[ix]=(a[ix]-a[ix,c,None]*a[r])%3
        pivots.append(c);r+=1
        if r==len(a):break
    free=[i for i in range(a.shape[1]) if i not in pivots]
    out=np.zeros((len(free),a.shape[1]),dtype=np.int16)
    out[:,free]=np.eye(len(free),dtype=np.int16)
    out[:,pivots]=-a[:r,free].T%3
    assert not np.any(a@out.T%3)
    return out,r


source_linear_basis,linear_rank=nullspace(linear_equations)
print('RESULT first-degree f equations rank/dimension:',linear_rank,len(source_linear_basis),flush=True)

source_upper=np.triu_indices(17,1)
bracket_maps=[]
for k in range(8):
    M=mapped_linear[k].astype(np.int64)
    rows=[]
    for i,j in zip(*source_upper):
        mat=(np.outer(M[i],M[j])-np.outer(M[j],M[i]))%3
        rows.append(mat[upper])
    bracket_maps.append(rows)
print('Reducing 1224 exact insertion and bracket vectors through the central relation space',flush=True)
all_central=central_reduce(np.concatenate([mapped_central.reshape(-1,3160),
                                         np.array(bracket_maps,dtype=np.int16).reshape(-1,3160)]))
mapped_central_q=all_central[:136].reshape(8,17,1429)
bracket_maps_q=all_central[136:].reshape(8,136,1429)
print('PASS all eight actual class-two Lie maps to the1429-dimensional central quotient',flush=True)

np.savez_compressed(HERE/'test_fivepoint_relative_class2_maps.npz',
                    source_abel=source_abel,source_linear_basis=source_linear_basis,
                    mapped_linear=mapped_linear,mapped_central=mapped_central_q,
                    bracket_maps=bracket_maps_q,
                    central_shifts=shifts,linear_projection=P)
output={'source':'F2/(gamma3(J2)J2^3), J2=ker(F2->C4^2)',
        'source_loop_words':source_loops,'target_pair_words':pairwords,
        'source_abelianization_order':144,'first_degree_rank':linear_rank,
        'first_degree_solution_dimension':len(source_linear_basis),
        'target_kernel_dimensions':[80,1429],
        'scope':'Actual insertion maps and first-degree equations only; full central consistency census continues separately.'}
(HERE/'test_fivepoint_relative_class2_maps.json').write_text(json.dumps(output,indent=2)+'\n')
