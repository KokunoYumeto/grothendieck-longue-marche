#!/usr/bin/env python3
"""Independent exact rank audit for all7560 remaining F9 characters.

No producer or producer helper is imported. The inputs are the frozen,
already independently verified F24 universal Laurent rows and actions.
Polynomial evaluation uses a multiplicative logarithm table; ranks and
source closure use a separate scalar incremental elimination over F3.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from hashlib import sha256
import json
import numpy as np

FOLDER = Path(__file__).resolve().parent
INPUT_NAMES = ['affine_rank_one_certificate_stage_output.json',
               'affine_obstruction_stage_output.json']

def checksum(path):
    return sha256(path.read_bytes()).hexdigest()

def field_product(x,y):
    a,b = divmod(x,3)
    c,d = divmod(y,3)
    # x=b+a*i, y=d+c*i, i^2=-1.
    return (b*d-a*c)%3 + 3*((b*c+a*d)%3)

EXP = [1]
for _ in range(7):
    EXP.append(field_product(EXP[-1],4))
assert len(set(EXP)) == 8 and set(EXP) == set(range(1,9))
assert field_product(EXP[-1],4) == 1
LOG = [0]*9
for i,x in enumerate(EXP):LOG[x]=i
for x in range(1,9):
    for y in range(1,9):
        assert EXP[(LOG[x]+LOG[y])%8] == field_product(x,y)
for x in range(9):
    cube=field_product(field_product(x,x),x)
    ix=field_product(3,x)
    ix3=field_product(field_product(ix,ix),ix)
    trace_ix=((ix%3+ix3%3)%3)+3*((ix//3+ix3//3)%3)
    assert trace_ix == x//3

EXP_ARRAY = np.array(EXP,dtype=np.uint8)

def evaluate_polynomials(polynomials,characters):
    """Evaluate each finite Laurent polynomial on nonzero F9 coordinates."""
    logs=np.array([[LOG[int(x)] for x in row] for row in characters],dtype=np.int16)
    monomials={}
    answer=np.zeros((len(characters),len(polynomials)),dtype=np.uint8)
    for index,poly in enumerate(polynomials):
        real=np.zeros(len(characters),dtype=np.int32)
        imag=np.zeros(len(characters),dtype=np.int32)
        for coefficient,exponent in poly:
            key=tuple(e%8 for e in exponent)
            if key not in monomials:
                exponent_vector=np.array(key,dtype=np.int16)
                monomials[key]=EXP_ARRAY[(logs@exponent_vector)%8]
            v=monomials[key]
            real+=(coefficient%3)*(v%3)
            imag+=(coefficient%3)*(v//3)
        answer[:,index]=(real%3)+3*(imag%3)
    return answer,len(monomials)

def add_to_basis(basis,row):
    """Scalar forward-echelon elimination, retaining one vector per pivot."""
    v=[int(x)%3 for x in row]
    for pivot in sorted(basis):
        a=v[pivot]
        if a:
            w=basis[pivot]
            for j in range(pivot,14):v[j]=(v[j]-a*w[j])%3
    nonzero=next((j for j,a in enumerate(v) if a),None)
    if nonzero is None:return False
    if v[nonzero]==2:v=[(2*x)%3 for x in v]
    assert nonzero not in basis and v[nonzero]==1
    basis[nonzero]=v
    return True

def basis_of(rows):
    basis={}
    for row in rows:add_to_basis(basis,row)
    return basis

def row_action(row,matrix):
    return [sum(row[k]*int(matrix[k,j]) for k in range(14))%3 for j in range(14)]

def main():
    inputs={name:checksum(FOLDER/name) for name in INPUT_NAMES}
    rows_data=json.loads((FOLDER/INPUT_NAMES[0]).read_text())
    action_data=json.loads((FOLDER/INPUT_NAMES[1]).read_text())
    characters=[list(retained+deleted)
                for retained in product(range(1,9),repeat=3)
                if not set(retained).issubset({1,2})
                for deleted in product((1,2),repeat=4) if deleted!=(1,1,1,1)]
    assert len(characters)==len({tuple(c) for c in characters})==7560
    assert 7560==(8**3-2**3)*(2**4-1)
    chars=np.array(characters,dtype=np.uint8)
    assert len(rows_data['source_rows'])==64
    polys=[p for row in rows_data['source_rows'] for p in row]
    values,monomial_count=evaluate_polynomials(polys,chars)
    values=values.reshape(7560,64,7)
    equations=np.concatenate((values//3,values%3),axis=2)
    principal=np.concatenate(((chars%3+2)%3,chars//3),axis=1)
    assert np.all(np.any(principal!=0,axis=1))
    assert np.all((equations.astype(np.int32)*principal[:,None,:]).sum(axis=2)%3==0)
    rank_counts=Counter()
    initial_ranks=[]
    deficient=[]
    for i in range(7560):
        rank=len(basis_of(equations[i]))
        assert rank<=13
        rank_counts[rank]+=1
        initial_ranks.append(rank)
        if rank<13:deficient.append(i)
    assert dict(rank_counts)=={13:7156,12:396,11:8},dict(rank_counts)
    assert len(deficient)==404
    print(json.dumps({'phase':'independent_initial_rows','rank_counts':dict(sorted(rank_counts.items()))}),flush=True)

    remaining_chars=chars[deficient]
    old=sorted((r for r in action_data['records'] if r['index']<11),key=lambda r:r['index'])
    seeds=sorted((r for r in action_data['records'] if r['index']>=11),key=lambda r:r['index'])
    assert [r['index'] for r in old]==list(range(11)) and len(seeds)==8
    action_polys=[p for r in old for row in r['action_matrix'] for p in row]
    old_values,action_monomials=evaluate_polynomials(action_polys,remaining_chars)
    old_values=old_values.reshape(404,11,7,7)
    actions=np.zeros((404,11,14,14),dtype=np.uint8)
    actions[:,:,:7,:7]=old_values%3
    # Apply the minus to the imaginary coordinate itself, before reduction.
    actions[:,:,:7,7:]=(-(old_values//3).astype(np.int16))%3
    actions[:,:,7:,:7]=old_values//3
    actions[:,:,7:,7:]=old_values%3
    seed_polys=[p for r in seeds for p in r['u_derivation_row']]
    seed_values,seed_monomials=evaluate_polynomials(seed_polys,remaining_chars)
    seed_values=seed_values.reshape(404,8,7)
    seed_equations=np.concatenate((seed_values//3,seed_values%3),axis=2)
    principal_remaining=principal[deficient]
    assert np.all(np.einsum('nijk,nk->nij',actions.astype(np.int32),principal_remaining.astype(np.int32))%3==principal_remaining[:,None,:])
    assert np.all(np.einsum('nrk,nk->nr',seed_equations.astype(np.int32),principal_remaining.astype(np.int32))%3==0)

    layer_counts=[Counter() for _ in range(4)]
    closures=[]
    for index in range(404):
        basis=basis_of(seed_equations[index])
        ranks=[len(basis)]
        layer_counts[0][len(basis)]+=1
        for layer in range(1,4):
            original=[basis[p][:] for p in sorted(basis)]
            for row in original:
                for matrix in actions[index]:add_to_basis(basis,row_action(row,matrix))
            ranks.append(len(basis))
            layer_counts[layer][len(basis)]+=1
            assert len(basis)<=13
        assert ranks[2]==ranks[3]==13
        for row in basis.values():
            assert sum(row[j]*int(principal_remaining[index,j]) for j in range(14))%3==0
        # Rank13 plus this nonzero common principal vector determines the
        # entire kernel. Still independently check stability under all11
        # actual source actions by reducing every image to zero.
        for row in list(basis.values()):
            for matrix in actions[index]:
                assert not add_to_basis(basis,row_action(row,matrix))
        closures.append({'character_index':deficient[index],
                         'character':characters[deficient[index]],'ranks':ranks,
                         'pivot_columns':sorted(basis),
                         'basis_sha256':sha256(json.dumps(basis,sort_keys=True).encode()).hexdigest()})
    rounds=[dict(sorted(c.items())) for c in layer_counts]
    assert rounds==[{5:80,6:284,7:2,8:38},{12:50,13:354},{13:404},{13:404}],rounds
    result={'status':'PASS_INDEPENDENT_EXHAUSTIVE_F9',
            'producer_sha256':checksum(Path(__file__)),
            'inputs':inputs,'characters':7560,
            'field':'F3[i]/(i^2+1); code a+3b=a+b*i; primitive element1+i',
            'coefficient_comparison':'Tr(i*z)=Im(z), checked for all9 field elements; inverse multiplication by-i',
            'initial_rank_counts':dict(sorted(rank_counts.items())),
            'initial_ranks':initial_ranks,'deficient_characters':404,
            'source_closure_rank_counts':rounds,
            'final_rank':13,'source_closure_stability_checked':True,
            'universal_principal_upper_bound_checked':True,
            'monomial_counts':[monomial_count,action_monomials,seed_monomials],
            'closures':closures,
            'independence':'No producer imports. Multiplicative-log Laurent evaluation and scalar incremental F3 echelon elimination independently verify the frozen actual F24 rows/actions.'}
    target=FOLDER/'affine_f9_independent_audit_output.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'characters':7560,
                      'initial_rank_counts':result['initial_rank_counts'],
                      'source_closure_rank_counts':rounds,
                      'output_sha256':checksum(target)},indent=2))

if __name__=='__main__':main()
