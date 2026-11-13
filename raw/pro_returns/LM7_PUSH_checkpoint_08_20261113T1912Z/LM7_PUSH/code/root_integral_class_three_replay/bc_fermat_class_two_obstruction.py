#!/usr/bin/env python3
"""An exact small obstruction and right inverse for the central norm equations."""
from pathlib import Path
from itertools import combinations,product
import json
import numpy as np
import bc_fermat_class_two as q
from bc_fermat_class_two_fibres import LinearSystem

HERE=Path(__file__).resolve().parent
arrays=np.load(HERE/"bc_fermat_class_two_fibres.npz")
M=arrays["central_norm_matrix"]
system=LinearSystem(M)
rows=np.r_[np.arange(10,55),np.arange(65,110)]
# Every F-prime abelian norm solution has the displayed coordinates v(a,b,c).
V=np.array([
 [0,0,1],[0,1,0],[1,0,0],[0,1,0],[1,0,2],
 [2,0,1],[2,0,0],[1,0,2],[0,0,1],[0,0,2]],dtype=np.int64)
assert not np.any(arrays["abelian_norm_matrix"]@V%3)
assert not np.any(q.f.F_AB_DIV3@V%3)
assert 10-LinearSystem(np.vstack((arrays["abelian_norm_matrix"],
                                 q.f.F_AB_DIV3))).rank==3

def error(parameters):
    return q.norm_errors(np.r_[V@np.asarray(parameters)%3,np.zeros(45,dtype=np.int64)])[rows]

linear=[];quadratic=[]
for i in range(3):
    e=np.eye(3,dtype=np.int64)[i]
    e1,e2=error(e),error(2*e)
    square=2*(e1+e2)%3
    linear.append((e1-square)%3);quadratic.append(square)
for i,j in combinations(range(3),2):
    ei,ej=np.eye(3,dtype=np.int64)[[i,j]]
    quadratic.append((error(ei+ej)-error(ei)-error(ej))%3)
L=np.stack(linear,axis=1);Q=np.stack(quadratic,axis=1)
test=LinearSystem(np.column_stack((M,L,Q)).T)
rhs=np.r_[np.zeros(45,dtype=np.int64),[1,2,2],np.zeros(6,dtype=np.int64)]
witness=test.solve(rhs)
assert witness is not None
assert not np.any(witness@M%3)
assert np.array_equal(witness@L%3,np.array([1,2,2]))
assert not np.any(witness@Q%3)
particulars=[]
for a,b,c in product(range(3),repeat=3):
    e=error([a,b,c])
    assert int(witness@e%3)==(a-b-c)%3
    z=system.solve(-e%3)
    assert (z is not None)==((a-b-c)%3==0)
    if z is not None:
        assert not np.any(q.norm_errors(np.r_[V@np.array([a,b,c])%3,z]))
        particulars.append({"a_b_c":[a,b,c],"central_solution":z.tolist()})
support=[{"norm_equation":1 if i<45 else 2,
          "wedge_indices":[int(q.PAIR_I[i%45])+1,int(q.PAIR_J[i%45])+1],
          "coefficient":int(witness[i])}
         for i in np.flatnonzero(witness)]
family=json.loads((HERE/"bc_fermat_class_two_fibres.json").read_text())["records"]
bad=V[:,0]
examples=[]
for record in family:
    for fibre in record["abelian_fibres"]:
        if fibre["target_abelianization"]==bad.tolist():
            examples.append({"certificate_index":record["certificate_index"],
                             "ternary_parameters":record["ternary_parameters"],
                             "binary_parameter":record["binary_parameter"],
                             "abelian_parameters":fibre["abelian_parameters"]})
assert examples
out={"abelian_norm_parameter_matrix_columns_a_b_c":V.tolist(),
     "exact_extra_condition":"a-b-c=0, equivalently v_3-v_2-v_1=0 in F3",
     "central_obstruction_functional_support":support,
     "central_norm_rank":system.rank,"central_kernel_dimension":system.kernel.shape[1],
     "all_27_abelian_norm_vectors_tested":True,
     "all_9_admissible_vectors_have_explicit_particulars":particulars,
     "one_nonlifting_abelian_vector":bad.tolist(),
     "first_actual_E24_origin_with_that_abelian_solution":examples[0]}
(HERE/"bc_fermat_class_two_obstruction.json").write_text(json.dumps(out,indent=2)+"\n")
np.savez_compressed(HERE/"bc_fermat_class_two_obstruction.npz",
                    parameter_matrix=V,obstruction_functional=witness,
                    central_error_linear=L,central_error_quadratic=Q)
print("Exact extra condition: v3-v2-v1=0 modulo three.")
print("Obstruction functional support:",json.dumps(support))
print("First actual retained origin carrying the excluded abelian solution:",examples[0])
print("PASS: explicit necessity, all27 cases, and sufficiency with45-coordinate lifts.")
