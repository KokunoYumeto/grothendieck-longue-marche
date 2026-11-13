#!/usr/bin/env python3
"""Two exact mod-three tests on the saturated rational central norm image.

The complete Smith diagonal is 1^264,3,3,0^64.  We construct its
saturated image by actual divisions with retained column preimages;
the resulting two functionals characterize the integral image on
that rational subspace.  This is separate from solving the tests on
the nonlinear E37 parameter graph.
"""
from pathlib import Path
import json,time
import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from bc_fermat_class_two_fibres import LinearSystem
from bc_fermat_class_three_norm_smith_probe import finite_rref

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();data=np.load(HERE/"bc_fermat_class_three_integral.npz")
    M=data["triple_norm"]
    rank,pivots,_=finite_rref(M,5);assert rank==266
    N=M[:,pivots].copy();numerator=np.eye(330,dtype=np.int64)[:,pivots]
    denominator=1;steps=[]
    while finite_rref(N,3)[0]<266:
        relation=LinearSystem(N%3).kernel[:,0];j=int(np.flatnonzero(relation)[0])
        value=N@relation;assert not np.any(value%3)
        old_numerator=numerator.copy();numerator*=3
        numerator[:,j]=old_numerator@relation
        denominator*=3;N[:,j]=value//3
        assert np.array_equal(M@numerator,denominator*N)
        steps.append({"replaced_column":j,"relation":relation.tolist()})
        assert len(steps)<15
    assert finite_rref(N,3)[0]==266
    _,rows,_=finite_rref(N.T,3);assert len(rows)==266
    minor=N[rows]%3;minor_system=LinearSystem(minor);assert minor_system.rank==266
    inverse=minor_system.transform%3
    assert np.array_equal(inverse@minor%3,np.eye(266,dtype=np.int64))
    left=np.zeros((266,660),dtype=np.int64);left[:,rows]=inverse
    assert np.array_equal(left@N%3,np.eye(266,dtype=np.int64))
    coordinates=left@M%3
    dual=LinearSystem(coordinates.T)
    assert dual.rank==264 and dual.kernel.shape==(266,2)
    tests=dual.kernel.T@left%3
    assert not np.any(tests@M%3)
    assert finite_rref(tests@N,3)[0]==2
    print("Saturated norm image rank266; two exact integral tests; saturation steps",len(steps),flush=True)
    print("Computing the exact 64-dimensional rational kernel",flush=True)
    null=DomainMatrix.from_Matrix(sp.Matrix(M.tolist())).convert_to(sp.QQ).nullspace().to_Matrix()
    assert null.shape==(64,330)
    columns=[]
    for i in range(64):
        row=null[i,:];den=sp.ilcm(*[a.q for a in row]);values=[int(a*den) for a in row]
        common=sp.igcd(*values);columns.append([a//int(common) for a in values])
    K=np.array(columns,dtype=np.int64).T;kernel_steps=[]
    while finite_rref(K,3)[0]<64:
        relation=LinearSystem(K%3).kernel[:,0];j=int(np.flatnonzero(relation)[0])
        value=K@relation;assert not np.any(value%3)
        K[:,j]=value//3;kernel_steps.append({"replaced_column":j,"relation":relation.tolist()})
        assert len(kernel_steps)<70
    assert not np.any(M@K)
    assert finite_rref(K,3)[0]==64
    projection=data["projection_exp3_central"]@K%3
    projection_rank=finite_rref(projection,3)[0]
    finite=np.load(HERE/"bc_fermat_class_three_norms.npz")["triple_norm_matrix"]
    assert not np.any(finite@projection%3)
    result={"status":"exact linear integral tests; parameter-graph solvability remains under investigation",
        "rational_image_rank":266,"saturated_image_division_steps":len(steps),
        "saturated_image_preimage_denominator":denominator,
        "image_Smith_index_at_three":9,"number_of_independent_integral_tests":2,
        "criterion":"On the rational norm image, E lies in M Z3^330 iff tests*E=0 mod3",
        "central_kernel_rank":64,"kernel_saturation_steps":len(kernel_steps),
        "central_kernel_image_rank_in_E44":projection_rank,
        "source_image_saturation_steps":steps,"kernel_saturation_operations":kernel_steps,
        "elapsed_seconds":round(time.time()-start,3)}
    (HERE/"bc_fermat_class_three_integral_tests.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_three_integral_tests.npz",
        saturated_image=N,saturated_image_preimage_numerator=numerator,
        saturated_image_preimage_denominator=np.array(denominator),integral_tests=tests,
        exact_integral_kernel=K,exact_kernel_projection_to_E44=projection)
    print(json.dumps({k:v for k,v in result.items() if k not in
        ("source_image_saturation_steps","kernel_saturation_operations")},indent=2))
    print("PASS: exact saturated image, two integral tests, and complete central kernel.")

if __name__=="__main__":main()
