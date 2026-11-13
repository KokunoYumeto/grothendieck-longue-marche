#!/usr/bin/env python3
"""Evaluate the actual arithmetic base pentagon and every supplied direction.

The source file is a_ihara_pentagon_inputs.json. Its actual free words
are used, and their supplied Magnus coefficients are independently
checked. All candidate differences begin in degree5, so the complete
degree<=7 pentagon residual is affine in these changes and in the true
kernel corrections of degrees6,7. The nonlinear transport by the base
word is retained by the evaluator, not replaced by the leading Lie map.
"""
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
import argparse,hashlib,io,json,time
import numpy as np
from de_fermat_pentagon_magnus import PentagonMagnus,summary,encode
with redirect_stdout(io.StringIO()):import de_fermat_schreier as sf

parser=argparse.ArgumentParser()
parser.add_argument('--prefix',default='de_fermat_pentagon_arithmetic')
args=parser.parse_args()
here=Path(__file__).resolve().parent;source=here/'a_ihara_pentagon_inputs.json'
data=json.loads(source.read_text());start=time.time();E=PentagonMagnus(prime=3,weight=7)
def decode(q):return {tuple(w):int(c) for w,c in q}
base=E.source.word(data['base_word']);assert base==decode(data['base_magnus'])
fa,fz=sf.literal(data['base_word'])
assert np.array_equal(fa,data['base_fa']) and np.array_equal(fz,data['base_fz'])
source_words=[w for degree in range(8) for w in product(range(2),repeat=degree)]
source_index={w:i for i,w in enumerate(source_words)}
target_words=[w for degree in range(1,9) for w in product(range(3),repeat=degree)]
target_index={w:i for i,w in enumerate(target_words)};nt=len(target_words)
def sv(q):
    a=np.zeros(len(source_words),dtype=np.int64)
    for w,c in q.items():a[source_index[w]]=c
    return a
def tv(q):
    a=np.zeros(3*nt,dtype=np.int64)
    for i,poly in enumerate(q):
        for w,c in poly.items():a[i*nt+target_index[w]]=c
    return a
def rref(A):
    A=np.asarray(A,dtype=np.int64).copy()%3;row=0;piv=[]
    for col in range(A.shape[1]):
        choices=np.flatnonzero(A[row:,col])
        if not len(choices):continue
        k=row+int(choices[0]);A[[row,k]]=A[[k,row]]
        A[row]=A[row]*pow(int(A[row,col]),-1,3)%3
        multipliers=A[:,col].copy();multipliers[row]=0
        A=(A-multipliers[:,None]*A[row][None,:])%3
        piv.append(col);row+=1
        if row==A.shape[0]:break
    return A,piv
def solve(A,b):
    A=np.asarray(A,dtype=np.int64)%3;b=np.asarray(b,dtype=np.int64)%3
    n=A.shape[1];R,piv=rref(np.column_stack((A,b)))
    if n in piv:return None
    x=np.zeros(n,dtype=np.int64);x[piv]=R[:len(piv),n]
    free=[j for j in range(n) if j not in piv];K=np.zeros((n,len(free)),dtype=np.int64)
    for j,k in enumerate(free):K[k,j]=1;K[piv,j]=-R[:len(piv),k]%3
    assert not np.any((A@x-b)%3) and not np.any(A@K%3)
    return x,K

candidate=[];differences=[]
for row in data['candidate_records']:
    q=E.source.word(row['literal_word']);assert q==decode(row['magnus'])
    candidate.append(q);delta=E.source.add(q,base,-1)
    assert all(len(w)>=5 for w in delta)
    differences.append(sv(delta))
DV=np.stack(differences,axis=1);_,selected=rref(DV);basis=DV[:,selected]
assert len(selected)==6
coordinates=[]
for col in DV.T:
    solution=solve(basis,col);assert solution is not None and solution[1].shape[1]==0
    coordinates.append(solution[0])
coordinates=np.array(coordinates,dtype=np.int64).T
print(json.dumps({'actual_base_word_length':len(data['base_word']),
                  'all_literal_source_Magnus_expansions_checked':len(candidate)+1,
                  'candidate_direction_dimension':len(selected),
                  'selected_record_indices':selected}),flush=True)

residual=E.from_series(base);base_factors=E.last_factors
base_vector=tv(residual)
print(json.dumps({'base_pentagon':summary(residual),
                  'elapsed_after_base':round(time.time()-start,3)}),flush=True)
columns=[];direction_records=[]
for j,index in enumerate(selected):
    direction=E.variation_from_degree_five(candidate[index],base,base_factors)
    columns.append(tv(direction));direction_records.append({'type':'candidate','record_index':index})
    print(json.dumps({'candidate_column':j,'record_index':index,
                      'residual_difference':summary(direction)}),flush=True)

kernel_words=[[1,2,-1,-2]*3]
k7=data['kernel_corrections']['7'];K7=np.array(k7['leading_kernel_basis'],dtype=np.int64)
assert K7.shape[1]==4
assert not np.any(np.array(k7['Fermat_group_images'],dtype=np.int64)@K7%3)
for col in K7.T:
    w=[]
    for c,v in zip(col,k7['literal_words']):w+=v*int(c)
    kernel_words.append(list(sf.free_reduce(w)))
for j,w in enumerate(kernel_words):
    aa,zz=sf.literal(w);assert not np.any(aa) and not np.any(zz)
    new=E.source.mul(E.source.word(w),base)
    delta=E.source.add(new,base,-1)
    assert min(map(len,delta))==6+(j>0)
    direction=E.variation_from_degree_five(new,base,base_factors)
    columns.append(tv(direction));direction_records.append({'type':'kernel','kernel_index':j})
    print(json.dumps({'kernel_column':j,'literal_word_length':len(w),
                      'residual_difference':summary(direction)}),flush=True)

M=np.stack(columns,axis=1)%3
# Independent full nonlinear substitution of one nonzero candidate checks
# the affine transport formula rather than merely its leading component.
actual=E.from_series(candidate[selected[0]])
assert np.array_equal((tv(actual)-base_vector)%3,M[:,0])
print('Full nonlinear candidate substitution agrees with the affine transport formula.',flush=True)

branch_results=[];branches=sorted({r['branch'] for r in data['candidate_records']})
for branch in branches:
    indices=[i for i,r in enumerate(data['candidate_records']) if r['branch']==branch]
    indices.sort(key=lambda i:data['candidate_records'][i]['basis_index'])
    assert data['candidate_records'][indices[0]]['basis_index']==0
    offset=coordinates[:,indices[0]]
    B=(coordinates[:,indices[1:]]-offset[:,None])%3
    equations=np.column_stack((M[:,:6]@B%3,M[:,6:]))
    rhs=-(base_vector+M[:,:6]@offset)%3
    sol=solve(equations,rhs)
    out={'branch':branch,'input_record_indices':indices,
         'old_parameter_dimension':len(indices)-1,
         'true_kernel_parameter_dimension':5,
         'equation_rank':len(rref(equations)[1]),
         'augmented_rank':len(rref(np.column_stack((equations,rhs)))[1]),
         'solution_exists':sol is not None}
    if sol is not None:
        x,K=sol;out['particular_parameters']=x.tolist();out['homogeneous_parameters']=K.tolist()
        out['candidate_coordinate_solution']=(offset+B@x[:len(indices)-1])%3
        out['candidate_coordinate_solution']=out['candidate_coordinate_solution'].tolist()
        out['candidate_coordinate_kernel']=(B@K[:len(indices)-1])%3
        out['candidate_coordinate_kernel']=out['candidate_coordinate_kernel'].tolist()
    branch_results.append(out)
    print(json.dumps({k:v for k,v in out.items() if k not in ('homogeneous_parameters','candidate_coordinate_kernel')}),flush=True)

np.savez_compressed(here/(args.prefix+'_certificate.npz'),
                    base_residual=base_vector.astype(np.uint8),direction_residuals=M.astype(np.uint8),
                    source_candidate_basis=basis.astype(np.uint8),candidate_coordinates=coordinates.astype(np.uint8))
result={'prime':3,'source_group_Magnus_degree':7,'target_automorphism_Magnus_degree':8,
        'source_input_filename':source.name,'source_input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'base_pentagon':summary(residual),'base_pentagon_residual':encode(residual),
        'candidate_direction_dimension':6,'selected_candidate_record_indices':selected,
        'candidate_coordinates':coordinates.tolist(),'direction_records':direction_records,
        'true_kernel_literal_words':kernel_words,'branch_results':branch_results,
        'full_nonlinear_candidate_checked_against_affine_formula':True,
        'all_literal_words_checked_in_Fermat_group':True,
        'matrix_row_order':'Three generator blocks X,Y,Z; within each block all words of lengths1 through8 over X<Y<Z, lexicographic within each length.',
        'elapsed_seconds':round(time.time()-start,3),
        'scope':'Complete actual degree<=7 pentagon equations on the supplied branch families and five explicitly verified kernel directions. Completeness of that finite-quotient kernel filtration is the separate arithmetic calculation.'}
(here/(args.prefix+'.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('base_pentagon_residual','candidate_coordinates','true_kernel_literal_words','branch_results','direction_records')},indent=2),flush=True)
