#!/usr/bin/env python3
"""Complete three-adic class-two norm fibres and a literal nonlifting point.

All polynomial identities are checked over Z.  The actual source affine
lattice is retained, and the finite-to-integral comparison includes both
Smith3 central coordinates instead of assuming compatible lifting.
"""
from pathlib import Path
from collections import Counter
from itertools import combinations
import json
import numpy as np
import sympy as sp
from de_ferrari_mod9_lift import Span
import bc_fermat_class_two as finite

HERE=Path(__file__).resolve().parent
data=np.load(HERE/"bc_fermat_class_two_3adic_norms.npz")
B=data["abelian_norm_basis"];M=data["central_norm"]
U=data["smith_left"];V=data["smith_right"];SM=data["smith"]
L=data["transformed_error_linear"];Q=data["transformed_error_quadratic"]
t1,t2,t3=sp.symbols("t1 t2 t3")
t=sp.Matrix([t1,t2,t3])
mon=sp.Matrix([t1*t1,t2*t2,t3*t3,t1*t2,t1*t3,t2*t3])
quadratic=t1*t1+t2*t2+t3*t3+t1*t2+t1*t3-t2*t3
difference=t3-t2
F=difference+3*quadratic
G=sp.expand(t2+t3-3*t1*t1-4*t2*t2-2*t3*t3
            -3*t1*t2-5*t1*t3+5*t2*t3-difference*quadratic)
errors=sp.Matrix(L)*t+sp.Matrix(Q)*mon
assert sp.expand(errors[35]-(1+difference)*F-3*G)==0
assert sp.expand(errors[36]-3*(-t1+t3))==0
assert errors[63]==2*F
for i in range(37,90):
    quotient,remainder=sp.div(errors[i],F,t3,t2,t1)
    assert remainder==0
    assert not quotient.free_symbols
assert int(SM[35,35])==int(SM[36,36])==3
assert all(int(coefficient)%3==0
           for coefficient in sp.Poly(sp.diff(F,t3)-1,t1,t2,t3).coeffs())

def f(a,b,c):return c-b+3*(a*a+b*b+c*c+a*b+a*c-b*c)
def g(a,b,c):
    qq=a*a+b*b+c*c+a*b+a*c-b*c
    return b+c-3*a*a-4*b*b-2*c*c-3*a*b-5*a*c+5*b*c-(c-b)*qq
def hensel(a,b,n):
    c=b%3;power=3
    for _ in range(1,n):
        assert f(a,b,c)%power==0
        # The derivative in c is1 modulo three.
        c+=power*((-f(a,b,c)//power)%3)
        power*=3
    assert f(a,b,c)%power==0
    return c%power

# Exact source affine lattice: K has the two divisibility conditions mod3.
K=np.load(HERE/"bc_cm_fermat_kernel_boundary.npz")["kernel_boundary_basis"]
lambda1=np.array([1,0,0,-1,-1,0,0,0,-11,0],dtype=np.int64)
lambda2=np.array([0,1,0,-11,0,0,0,-1,-1,0],dtype=np.int64)
assert not np.any(lambda1@K%3) and not np.any(lambda2@K%3)
assert np.array_equal(lambda1@B%3,np.array([1,2,2]))
assert np.array_equal(lambda2@B%3,np.array([1,2,2]))
hom=np.array(json.loads((HERE/"bc_cm_fermat_kernel_words.json").read_text())[
    "homogeneous_norm_kernel_basis"],dtype=np.int64)
source_t=np.vstack((-hom[0],hom[1],hom[4]))
assert np.array_equal(B@source_t,hom)
assert abs(int(sp.Matrix(source_t).det()))==48
origins=json.loads((HERE/"bc_cm_fermat_odd_boundary.json").read_text())["records"]
source_rows=[]
for row in origins:
    v=np.array(row["integral_H_abelianization"],dtype=np.int64)
    c=int(lambda1@v%3)
    assert c==int(lambda2@v%3)
    source_rows.append({"certificate_index":row["certificate_index"],
                        "ternary_parameters":row["ternary_parameters"],
                        "binary_parameter":row["binary_parameter"],
                        "affine_source_residue":c})
assert len(source_rows)==432

finite_counts=[]
for n in range(1,5):
    modulus=3**n;counts=[0,0,0]
    for a in range(modulus):
        for b in range(modulus):
            c=hensel(a,b,n)
            counts[(a-b-c)%3]+=1
            # The exact divisibility equations on the smooth hypersurface.
            assert (2*b+4*c-6*a*a-8*b*b-2*c*c-6*a*b-12*a*c+10*b*c)%3==0
    assert counts==[3**(2*n-1)]*3
    finite_counts.append({"n":n,"abelian_solutions_per_source":counts[0],
        "finite_central_solutions_per_abelian_value":3**(8*n+2),
        "finite_norm_images_per_source":3**(10*n+1),
        "infinite_lift_central_images_per_abelian_value":3**(8*n),
        "infinite_lift_images_per_source":3**(10*n-1),
        "finite_fraction_lifting_to_next_and_every_level":"1/9"})

# An individual level3 norm solution, over the first actual E24 origin.
assert source_rows[0]["affine_source_residue"]==0
y=np.zeros(45,dtype=np.int64);y[36]=1
Z=V@y
target=np.r_[np.zeros(10,dtype=np.int64),2*Z%3] # BCH central coordinate Z/2.
assert not np.any(finite.norm_errors(target))
logs=np.load(HERE/"bc_fermat_class_two_fibres.npz")["source_word_logs"]
correction=finite.multiply(-logs[0]%3,target)
kernel=np.load(HERE/"bc_fermat_class_two_kernel.npz")["basis"]
span=Span(55)
for column in kernel.T:assert span.add(column,None)
coefficients=span.coordinates(correction)
representative=finite.ZERO.copy()
for a,column in zip(coefficients,kernel.T):
    representative=finite.multiply(representative,int(a)*column%3)
commutator_corrections=[]
for i,j in combinations(range(len(coefficients)),2):
    a=(-2*int(coefficients[i])*int(coefficients[j]))%3
    if a:
        representative=finite.multiply(representative,
            a*finite.commutator(kernel[:,i],kernel[:,j])%3)
        commutator_corrections.append([i,j,a])
assert np.array_equal(representative,correction)
assert np.array_equal(finite.multiply(logs[0],representative),target)
# At level9, any lift has t1=t2=t3=0 mod3.  Its second divided
# Smith equation forces y36=t1-t3=0 mod3, contradicting y36=1.
assert g(0,0,0)==0
support=[{"wedge_indices":[int(finite.PAIR_I[i])+1,int(finite.PAIR_J[i])+1],
          "BCH_coefficient_mod3":int(target[10+i])}
         for i in np.flatnonzero(target[10:])]
out={"primitive_abelian_norm_basis":B.tolist(),
     "complete_integral_obstruction":str(F),
     "quadratic_Q":str(quadratic),
     "divided_first_Smith_polynomial_G":str(G),
     "source_affine_condition":"t1-t2-t3=c_source mod3",
     "source_homogeneous_t_basis":source_t.tolist(),
     "source_homogeneous_basis_determinant":48,
     "source_residue_distribution":dict(Counter(r["affine_source_residue"] for r in source_rows)),
     "source_rows":source_rows,
     "infinite_abelian_parametrization":"t2=u, t1=c_source-u+3w; t3 is the unique Z3 root of F=0 congruent to u mod3",
     "infinite_central_parametrization":"y_i=-(U*e(t))_i/Smith_i for i<37; y37,...,y44 arbitrary; Z=V*y",
     "extra_finite_lifting_conditions":"y35=-G(t), y36=t1-t3 mod3^n",
     "complete_inverse_limit_fibre":"Z3^10 with the displayed actual coordinate map",
     "finite_counts":finite_counts,
     "nonlifting_point":{"source_origin":source_rows[0],
         "target_abelianization_mod3":[0]*10,
         "target_doubled_log_Smith_torsion_coordinates":[0,1],
         "target_BCH_central_support":support,
         "complete_source_kernel_basis_power_coefficients":coefficients.tolist(),
         "BCH_collecting_commutator_powers":commutator_corrections,
         "actual_word_rule":"Replace each complete ternary-kernel basis relator by its fourth power to preserve its mod3 value and kill binary source coordinates; take the ordered powers and the listed commutator corrections.",
         "exact_P9_obstruction":"Any lift has t1=t3=0 mod3, so its Smith row36 forces y36=t1-t3=0 mod3, contrary to1."},
     "all_polynomial_and_affine_lattice_identities_verified":True}
(HERE/"bc_fermat_class_two_3adic_tower.json").write_text(json.dumps(out,indent=2)+"\n")
np.savez_compressed(HERE/"bc_fermat_class_two_3adic_tower.npz",
                    source_t_lattice=source_t,source_residues=np.array([
                        r["affine_source_residue"] for r in source_rows]),
                    nonlifting_target=target,nonlifting_correction=correction,
                    nonlifting_word_coefficients=coefficients)
print("Integral obstruction:",sp.factor(F))
print("Divided first torsion row G:",G)
print("Actual source residue distribution:",dict(Counter(r["affine_source_residue"] for r in source_rows)))
print("Finite and infinite-image counts:",json.dumps(finite_counts))
print("Individual nonlifting target central support:",support)
print("PASS: full source lattices, complete3-adic fibres, exact finite lifting criterion, and actual P3-to-P9 counterexample.")
