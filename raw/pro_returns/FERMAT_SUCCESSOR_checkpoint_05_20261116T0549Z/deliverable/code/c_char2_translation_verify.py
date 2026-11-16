#!/usr/bin/env python3
"""Independent exhaustive verification of the characteristic-two affine test.

This does not reuse the sequential affine-lattice solver. It enumerates
every sigma solution by ternary digit lifting, then tests every one
against both actual translation equations for all three comparisons.
"""
from itertools import product
from collections import Counter
import json
import time
import numpy as np

started=time.monotonic()
data=np.load('deliverable/code/b_char2_translation_affine_matrices.npz')
A=np.array(data['affine_matrix'],dtype=np.int64)
moduli=np.array(data['affine_row_moduli'],dtype=np.int64)
targets=np.array(data['affine_targets'],dtype=np.int64)
domain=np.array(data['domain_moduli'],dtype=np.int64)
assert A.shape==(594,13) and targets.shape==(3,594)
assert np.array_equal(targets[0,:198],targets[1,:198])
assert np.array_equal(targets[0,:198],targets[2,:198])
assert not np.any(A*domain[None,:]%moduli[:,None])

def valuation(x):
    if not x:return 100
    answer=0
    while x%3==0:x//=3;answer+=1
    return answer

def pivot_columns(matrix):
    B=matrix.copy()%3
    row=0;columns=[]
    for col in range(B.shape[1]):
        choices=np.flatnonzero(B[row:,col])
        if not len(choices):continue
        k=row+int(choices[0]);B[[row,k]]=B[[k,row]]
        B[row]=B[row]*int(B[row,col])%3
        for i in range(len(B)):
            if i!=row:B[i]=(B[i]-B[i,col]*B[row])%3
        columns.append(col);row+=1
        if row==len(B):break
    return columns

def inverse3(B):
    n=len(B)
    C=np.hstack((B.copy()%3,np.eye(n,dtype=np.int64)))
    for j in range(n):
        k=j+int(np.flatnonzero(C[j:,j])[0])
        C[[j,k]]=C[[k,j]]
        C[j]=C[j]*int(C[j,j])%3
        for i in range(n):
            if i!=j:C[i]=(C[i]-C[i,j]*C[j])%3
    assert np.array_equal(C[:,:n],np.eye(n,dtype=np.int64))
    return C[:,n:]

# Normalize each scalar congruence by its exact common power of three.
sigma=A[:198].copy()
rhs=targets[0,:198].copy()
sigma_mod=moduli[:198].copy()
for i in range(198):
    v=min([valuation(int(sigma_mod[i]))]+[valuation(int(x)) for x in sigma[i]])
    divisor=3**v
    assert rhs[i]%divisor==0
    sigma[i]//=divisor;rhs[i]//=divisor;sigma_mod[i]//=divisor
keep=sigma_mod>1
sigma=sigma[keep];rhs=rhs[keep];sigma_mod=sigma_mod[keep]
domain_exponents=np.array([valuation(int(m)) for m in domain])
row_exponents=np.array([valuation(int(m)) for m in sigma_mod])

solutions=np.zeros((1,13),dtype=np.int64)
stages=[]
for digit in range(int(max(domain_exponents))):
    active=np.flatnonzero(domain_exponents>digit)
    rows=np.flatnonzero(row_exponents>digit)
    C=sigma[np.ix_(rows,active)]%3
    independent_rows=pivot_columns(C.T)
    rank=len(independent_rows)
    selected=C[independent_rows,:]
    pivots=pivot_columns(selected)
    assert len(pivots)==rank
    free=[i for i in range(len(active)) if i not in pivots]
    inv=inverse3(selected[:,pivots]) if rank else np.zeros((0,0),dtype=np.int64)
    kernel=np.zeros((len(free),len(active)),dtype=np.int64)
    for i,j in enumerate(free):
        kernel[i,j]=1
        if rank:kernel[i,pivots]=(-inv@selected[:,j])%3
    powers=3**digit
    residual=solutions@sigma[rows,:].T-rhs[rows]
    assert not np.any(residual%powers)
    residual=(residual//powers)%3
    correction=np.zeros((len(solutions),len(active)),dtype=np.int64)
    if rank:correction[:,pivots]=(-residual[:,independent_rows]@inv.T)%3
    compatible=~np.any((residual+correction@C.T)%3,axis=1)
    parents=solutions[compatible]
    correction=correction[compatible]
    blocks=[]
    for coefficients in product(range(3),repeat=len(free)):
        shift=np.array(coefficients,dtype=np.int64)@kernel if free else np.zeros(len(active),dtype=np.int64)
        digits=(correction+shift)%3
        children=parents.copy()
        children[:,active]+=powers*digits
        blocks.append(children)
    solutions=np.vstack(blocks)
    assert not np.any(solutions>=domain[None,:])
    stage={'digit':digit+1,'active_variables':len(active),'constraint_rank':rank,
           'free_digits':len(free),'partial_solutions':len(solutions)}
    stages.append(stage)
    print('Digit stage:',stage,flush=True)

assert len(solutions)==3**10
assert len({tuple(row) for row in solutions})==len(solutions)
for start in range(0,len(solutions),2048):
    X=solutions[start:start+2048]
    assert not np.any((X@A[:198,:].T-targets[0,:198])%moduli[:198])
print('Exhaustively enumerated all sigma/Frobenius-two solutions:',len(solutions),flush=True)

records=[]
for comparison in range(3):
    matches=[]
    for start in range(0,len(solutions),2048):
        X=solutions[start:start+2048]
        condition=(X@A[198:,:].T-targets[comparison,198:])%moduli[198:]
        matches.append(X[~np.any(condition,axis=1)])
    surviving=np.vstack(matches)
    assert len(surviving)==9
    orders=[]
    for x in surviving:
        k=next(k for k in range(5) if not np.any(3**k*x%domain))
        orders.append(3**k)
        assert not np.any((A@x-targets[comparison])%moduli)
    assert set(orders)=={27}
    record={'comparison':comparison,'survivors':len(surviving),
            'order_histogram':dict(sorted(Counter(orders).items())),
            'solutions':sorted([[int(x) for x in row] for row in surviving])}
    records.append(record)
    print('Comparison',comparison,': nine survivors, all exact order27',flush=True)

original=json.load(open('deliverable/code/b_char2_translation_affine.json'))
for left,right in zip(records,original['comparisons']):
    assert left['solutions']==right['all_solution_smith_coordinates']
result={'status':'independent exhaustive ternary-digit verification passed',
        'method':'enumerate all 59049 sigma/Frobenius-two solutions; test every translation equation',
        'domain_moduli':[int(x) for x in domain],
        'digit_stages':stages,'sigma_solutions_enumerated':len(solutions),
        'comparisons':records,'elapsed_seconds':time.monotonic()-started,
        'conclusion':'Every surviving class for every equivariant Kummer comparison has exact order27.'}
with open('deliverable/code/c_char2_translation_verify.json','w') as f:
    json.dump(result,f,indent=2);f.write('\n')
np.savez_compressed('deliverable/code/c_char2_translation_verified_solutions.npz',
                    sigma_solutions=solutions.astype(np.uint8))
print('All27 solutions agree with the separate affine-lattice solver.',flush=True)
print('Elapsed seconds:',round(result['elapsed_seconds'],3),flush=True)
