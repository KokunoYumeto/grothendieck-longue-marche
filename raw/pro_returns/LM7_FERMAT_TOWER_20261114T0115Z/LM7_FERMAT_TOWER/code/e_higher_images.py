#!/usr/bin/env python3
"""E.44: exact degree-three local obstruction module at the K-prime 2.

The local central correction is (Frob_4-4)z=-epsilon.
The split-lattice identity proves exponent at most3^5, so the
retained modular transformations modulo3^6 give exact Smith data.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json
import numpy as np
import e_unramified_sections as u

MOD=3**6
h=u.Hall(3)
inputs=u.arithmetic_inputs()
F,basis=h.action(inputs['Frob_K2'],3)
B,_=h.action(inputs['B'],3)
C,_=h.action(inputs['C'],3)
D,_=h.action(inputs['split_Frob_K2'],3)
assert len(basis)==330
assert u.compose(B,C)==u.identity(330,27)
assert u.compose(F,B)==u.compose(B,D)
eigenvalues=[D[j][j] for j in range(330)]
assert Counter(eigenvalues)==Counter({64:168,-32:128,16:32,-8:2})
assert sum(u.vp3(abs(x-4)) for x in eigenvalues)==458
assert all(Fraction(9,x-4).denominator%3 for x in eigenvalues)
P=u.plus(F,u.identity(330),-4)
A=np.zeros((330,330),dtype=np.int64)
for j,column in enumerate(P):
    for i,a in column.items():
        A[i,j]=a


def smith_mod(matrix,modulus):
    a=matrix.copy()%modulus
    m,n=a.shape
    left=np.eye(m,dtype=np.int64)
    right=np.eye(n,dtype=np.int64)
    valuations=[]
    operations=[]
    for k in range(min(m,n)):
        sub=a[k:,k:]
        if not np.any(sub):
            break
        chosen=None
        for v in range(6):
            p=3**v
            candidates=np.argwhere((sub%p==0)&(sub%(3*p)!=0))
            if len(candidates):
                chosen=candidates[0]+k
                break
        assert chosen is not None
        i,j=map(int,chosen)
        a[[i,k]]=a[[k,i]]
        left[[i,k]]=left[[k,i]]
        a[:,[j,k]]=a[:,[k,j]]
        right[:,[j,k]]=right[:,[k,j]]
        p=3**v
        inv=pow(int(a[k,k])//p,-1,modulus)
        a[k]=(a[k]*inv)%modulus
        left[k]=(left[k]*inv)%modulus
        assert int(a[k,k])==p
        factors=a[:,k]//p
        factors[k]=0
        assert np.all(a[:,k]%p==0)
        a=(a-factors[:,None]*a[k][None,:])%modulus
        left=(left-factors[:,None]*left[k][None,:])%modulus
        factors2=a[k,:]//p
        factors2[k]=0
        assert np.all(a[k,:]%p==0)
        a=(a-a[:,k][:,None]*factors2[None,:])%modulus
        right=(right-right[:,k][:,None]*factors2[None,:])%modulus
        valuations.append(v)
        operations.append({'pivot':k,'row_swap':i,'column_swap':j,
                           'row_unit':inv,'valuation':v,
                           'row_eliminations':factors.tolist(),
                           'column_eliminations':factors2.tolist()})
    diag=np.zeros_like(a)
    for k,v in enumerate(valuations):
        diag[k,k]=3**v
    assert np.array_equal(a,diag)
    assert np.array_equal(((left@(matrix%modulus))%modulus@right)%modulus,diag)
    assert all(op['row_unit']%3 for op in operations)
    return valuations,left,right,operations


print('Constructed the actual integral Lie3(Frob_K2)-4 matrix of rank330.',flush=True)
vals,left,right,operations=smith_mod(A,MOD)
assert len(vals)==330
assert sum(vals)==458
assert max(vals)<=5
counts={str(v):vals.count(v) for v in sorted(set(vals))}
print('Exact Smith valuation counts:',counts,flush=True)
print('Independent determinant valuation:',sum(vals),'=458.',flush=True)

# An exact rational inverse certificate from the actual split-lattice map.
# The denominator bound follows from 9/(eigenvalue-4) being 3-integral.
# This checks local correction examples without asserting that an arbitrary
# lattice vector is the obstruction of a globally realizable lower section.
examples=[]
for k in [0,1,2,100,329]:
    v={i:Fraction(a,27*(eigenvalues[i]-4)) for i,a in C[k].items()}
    correction={}
    for i,a in v.items():
        u.add_scaled(correction,B[i],-a)
    check={}
    for i,a in correction.items():
        u.add_scaled(check,P[i],a)
    assert check=={k:Fraction(-1)}
    minimum=min((u.vp3(abs(a.numerator))-u.vp3(a.denominator)
                 for a in correction.values()),default=0)
    examples.append({'error_basis_index':k,
                     'negative_inverse_error':[[i,str(a)] for i,a in sorted(correction.items())],
                     'minimum_3_valuation':minimum,
                     'integral':minimum>=0})
print('Verified exact inverse corrections for five basis errors.',flush=True)

# Rational Q2 refinement.  The actual Frobenius is integrally conjugate
# to elliptic sqrt(-2)*CE and toric 2P.  The divided gluing block requires
# one more digit, hence the square root is computed modulo3^7.
s=1
for k in range(1,7):
    candidates=[s+t*3**k for t in range(3)
                if ((s+t*3**k)**2+2)%3**(k+1)==0]
    assert len(candidates)==1
    s=candidates[0]
assert s%3==1 and (s*s+2)%2187==0
cusps=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=[(v,-u0) for u0,v in cusps]
cc=inputs['c']
E=[[s*cc[j].get(i,0) for j in range(2)] for i in range(2)]
T=[[-2*cc[j+2].get(i+2,0) for j in range(8)] for i in range(8)]
V2=[[0]*10 for _ in range(10)]
for i in range(2):
    V2[i][:2]=E[i]
for i in range(8):
    V2[i+2][2:]=T[i]
    for j in range(2):
        numerator=(sum(U[i][k]*E[k][j] for k in range(2))-
                   sum(T[i][k]*U[k][j] for k in range(8)))
        assert numerator%3==0
        V2[i+2][j]=numerator//3
V2=u.dense_to_columns(V2)
Fq,_=h.action(V2,3)


def reduce_columns(M):
    return [{i:a%MOD for i,a in col.items() if a%MOD} for col in M]


assert reduce_columns(u.compose(Fq,Fq))==reduce_columns(F)
Pq=u.plus(Fq,u.identity(330),-2)
Aq=np.zeros((330,330),dtype=np.int64)
for j,col in enumerate(Pq):
    for i,a in col.items():
        Aq[i,j]=a%MOD
qvals,ql,qr,qops=smith_mod(Aq,MOD)
assert len(qvals)==330 and max(qvals)<=5
qcounts={str(v):qvals.count(v) for v in sorted(set(qvals))}
eigenletters=[s,-s]+[2]*5+[-2]*3
qdetval=0
for node in basis:
    eigen=1
    for a,k in zip(eigenletters,h.letters[node]):
        eigen*=a**k
    qdetval+=u.vp3(abs(eigen-2))
assert qdetval==sum(qvals)
print('Rational Q2 Smith valuation counts:',qcounts,flush=True)
print('Rational Q2 independent determinant valuation:',qdetval,flush=True)

result={'status':'PASS','prime_of_K':'(2)','residue_cardinality':4,
        'degree':3,'rank':330,'matrix_coo':u.coo(P),'modulus':MOD,
        'torsion_bound_exponent':5,'Smith_valuation_counts':counts,
        'determinant_3_valuation':458,
        'split_eigenvalue_multiplicities':dict(Counter(eigenvalues)),
        'left_transform_mod729':left.tolist(),
        'right_transform_mod729':right.tolist(),
        'elementary_operations':operations,
        'correction_examples':examples,
        'rational_Q2':{'sqrt_minus2_mod2187':s,
                       'V_Frobenius_mod729_coo':u.coo(reduce_columns(V2)),
                       'Lie3_Frobenius_mod729_coo':u.coo(reduce_columns(Fq)),
                       'matrix_mod729':Aq.tolist(),
                       'Smith_valuation_counts':qcounts,
                       'determinant_3_valuation':qdetval,
                       'left_transform_mod729':ql.tolist(),
                       'right_transform_mod729':qr.tolist(),
                       'elementary_operations':qops,
                       'verified_square_equals_K_Frobenius':True,
                       'torsion_bound_exponent':5},
        'example_scope':'Linear lattice corrections only; no claim that arbitrary basis errors arise from a global lower section.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print('PASS: retained invertible transformations and proven bound certify the exact local obstruction group.',flush=True)
