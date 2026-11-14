#!/usr/bin/env python3
"""Exact integral Smith and polynomial norm data for the full three-adic tower."""
from pathlib import Path
from itertools import combinations
import json
import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
import bc_fermat_class_two_integral_model as q

HERE=Path(__file__).resolve().parent
rows=np.r_[np.arange(10,55),np.arange(65,110)]
abel=np.vstack((np.eye(10,dtype=np.int64)+q.S[:10,:10],
                np.eye(10,dtype=np.int64)+q.R[:10,:10]+q.R[:10,:10]@q.R[:10,:10],
                q.f.F_AB_DIV3))
AS,AU,AV=map(lambda x:x.to_Matrix(),smith_normal_decomp(
    DomainMatrix.from_Matrix(sp.Matrix(abel)).convert_to(sp.ZZ)))
arank=sum(bool(AS[i,i]) for i in range(10))
assert arank==7 and abs(AV.det())==1
assert all(int(AS[i,i])%3 for i in range(arank))
B=np.array(AV[:,arank:],dtype=np.int64)
assert not np.any(abel@B)
M=np.stack([q.norm_errors(np.eye(55,dtype=np.int64)[10+j])[rows]
            for j in range(45)],axis=1)
SM,UM,VM=map(lambda x:x.to_Matrix(),smith_normal_decomp(
    DomainMatrix.from_Matrix(sp.Matrix(M)).convert_to(sp.ZZ)))
assert SM==UM*sp.Matrix(M)*VM and abs(UM.det())==abs(VM.det())==1
diagonal=[abs(int(SM[i,i])) for i in range(45)]
rank=sum(bool(a) for a in diagonal)
assert diagonal==[1]*35+[3,3]+[0]*8
U=np.array(UM,dtype=np.int64)

def error(v):return q.norm_errors(np.r_[B@v,np.zeros(45,dtype=np.int64)])[rows]

linear=[];quadratic=[]
for i in range(3):
    e=np.eye(3,dtype=np.int64)[i]
    e1,e2=error(e),error(2*e)
    numerator=e2-2*e1;assert not np.any(numerator%2)
    square=numerator//2
    linear.append(e1-square);quadratic.append(square)
for i,j in combinations(range(3),2):
    ei,ej=np.eye(3,dtype=np.int64)[[i,j]]
    quadratic.append(error(ei+ej)-error(ei)-error(ej))
L=np.stack(linear,axis=1);Q=np.stack(quadratic,axis=1)
transformed_L=U@L;transformed_Q=U@Q
rng=np.random.default_rng(3372026)
for _ in range(30):
    a=rng.integers(-5,6,size=3)
    mon=np.r_[a*a,[a[i]*a[j] for i,j in combinations(range(3),2)]]
    assert np.array_equal(error(a),L@a+Q@mon)
free_rows=[i for i in range(rank,90) if np.any(transformed_L[i]) or np.any(transformed_Q[i])]
torsion_rows=[i for i in range(rank) if int(SM[i,i])%3==0]
result={"coordinates":"v=B*t, Z twice BCH central coordinate",
    "primitive_abelian_norm_basis":B.tolist(),
    "abelian_norm_and_F_prime_rank":arank,
    "abelian_norm_and_F_prime_smith_factors":[abs(int(AS[i,i])) for i in range(10)],
    "central_norm_smith_factors":diagonal,
    "central_norm_rational_rank":rank,
    "central_norm_integral_kernel_rank":45-rank,
    "three_torsion_rows":torsion_rows,
    "three_torsion_linear_coefficients":transformed_L[torsion_rows].tolist(),
    "three_torsion_quadratic_coefficients":transformed_Q[torsion_rows].tolist(),
    "quadratic_monomial_order":["t1^2","t2^2","t3^2","t1*t2","t1*t3","t2*t3"],
    "nonzero_rational_cokernel_rows":free_rows,
    "rational_cokernel_linear_coefficients":transformed_L[free_rows].tolist(),
    "rational_cokernel_quadratic_coefficients":transformed_Q[free_rows].tolist(),
    "polynomial_identity_verified_integrally":True}
(HERE/"bc_fermat_class_two_3adic_norms.json").write_text(json.dumps(result,indent=2)+"\n")
np.savez_compressed(HERE/"bc_fermat_class_two_3adic_norms.npz",
    abelian_norm_basis=B,central_norm=M,
    smith=np.array(SM,dtype=np.int64),smith_left=U,
    smith_right=np.array(VM,dtype=np.int64),
    error_linear=L,error_quadratic=Q,
    transformed_error_linear=transformed_L,
    transformed_error_quadratic=transformed_Q)
print(json.dumps(result,indent=2))
print("PASS: exact integral central Smith map and every polynomial obstruction coefficient.")
