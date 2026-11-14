#!/usr/bin/env python3
"""Exploratory four rational class-three norm obstructions over the E37 tower.

The source-central lattice is already complete.  Here the four common
dual invariants give the exact rational obstruction; their polynomial
coefficients and actual changes of row basis are retained.  No unknown
integral divisibility condition is silently discarded.
"""
from pathlib import Path
from itertools import product
from functools import reduce
from math import gcd
import json,time
import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import bc_fermat_class_three_integral as q
from bc_fermat_class_two_fibres import LinearSystem
from bc_fermat_class_three_norm_smith_probe import finite_rref

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();data=np.load(HERE/"bc_fermat_class_three_integral.npz")
    S=data["S"][55:,55:];R=data["R"][55:,55:]
    A=np.vstack((S.T-np.eye(330,dtype=np.int64),R.T-np.eye(330,dtype=np.int64)))
    print("Computing exact common dual invariants",flush=True)
    null=DomainMatrix.from_Matrix(sp.Matrix(A.tolist())).convert_to(sp.QQ).nullspace().to_Matrix()
    assert null.rows==4 and null.cols==330
    rows=[]
    for i in range(4):
        row=null[i,:];den=sp.ilcm(*[x.q for x in row]);values=[int(x*den) for x in row]
        common=reduce(gcd,(abs(x) for x in values if x));rows.append([x//common for x in values])
    invariant=np.array(rows,dtype=np.int64)
    saturations=0
    while finite_rref(invariant.T,3)[0]<4:
        system=LinearSystem(invariant.T%3)
        relation=system.kernel[:,0];j=int(np.flatnonzero(relation)[0])
        numerator=relation@invariant
        assert not np.any(numerator%3)
        invariant[j]=numerator//3;saturations+=1
    assert not np.any(A@invariant.T)
    assert np.array_equal(invariant@S,invariant) and np.array_equal(invariant@R,invariant)
    assert not np.any(np.hstack((3*invariant,2*invariant))@data["triple_norm"])
    print("Four saturated invariant rows; saturation steps",saturations,flush=True)
    old=np.load(HERE/"bc_fermat_class_two_3adic_norms.npz");B=old["abelian_norm_basis"]
    def obstruction(t,Z):
        g=np.r_[B@np.asarray(t,dtype=np.int64),Z,np.zeros(330,dtype=np.int64)]
        err=q.norm_errors(g)
        return 3*invariant@err[55:385]+2*invariant@err[440:770]
    zeroZ=np.zeros(45,dtype=np.int64);zeroT=np.zeros(3,dtype=np.int64)
    grids=sorted([a for a in product(range(4),repeat=3) if sum(a)<=3],key=lambda a:(sum(a),a))
    evaluation=sp.Matrix([[sp.prod(int(t[i])**a[i] for i in range(3)) for a in grids] for t in grids])
    values=np.stack([obstruction(t,zeroZ) for t in grids])
    coefficients=evaluation.inv()*sp.Matrix(values.tolist())
    assert all(x.q==1 for x in coefficients)
    constant_coefficients=np.array(coefficients,dtype=np.int64).T
    C0=np.stack([obstruction(zeroT,e) for e in np.eye(45,dtype=np.int64)],axis=1)
    C=[]
    for i in range(3):
        t=np.eye(3,dtype=np.int64)[i];base=obstruction(t,zeroZ)
        C.append(np.stack([obstruction(t,e)-base for e in np.eye(45,dtype=np.int64)],axis=1)-C0)
    rng=np.random.default_rng(2026111345)
    for _ in range(12):
        t=rng.integers(-3,4,size=3);Z=rng.integers(-3,4,size=45)
        mon=np.array([np.prod(t**np.array(a)) for a in grids],dtype=np.int64)
        expected=constant_coefficients@mon+(C0+sum(t[i]*C[i] for i in range(3)))@Z
        assert np.array_equal(expected,obstruction(t,Z))
    print("Exact degree-three and mixed coefficients reconstructed",flush=True)
    t1,t2,t3=sp.symbols("t1 t2 t3");symbols=(t1,t2,t3)
    t=sp.Matrix(symbols);mon2=sp.Matrix([t1*t1,t2*t2,t3*t3,t1*t2,t1*t3,t2*t3])
    E=sp.Matrix(old["transformed_error_linear"])*t+sp.Matrix(old["transformed_error_quadratic"])*mon2
    Q=t1*t1+t2*t2+t3*t3+t1*t2+t1*t3-t2*t3
    F=t3-t2+3*Q
    G=t2+t3-3*t1*t1-4*t2*t2-2*t3*t3-3*t1*t2-5*t1*t3+5*t2*t3-(t3-t2)*Q
    Y=[]
    for i in range(35):Y.append(-E[i]/int(old["smith"][i,i]))
    Y +=[-G,t1-t3]
    Zbase=sp.Matrix(old["smith_right"][:,:37])*sp.Matrix(Y)
    Cz=sp.Matrix(C0)+sum((symbols[i]*sp.Matrix(C[i]) for i in range(3)),sp.zeros(4,45))
    f0=sp.Matrix(constant_coefficients)*sp.Matrix([sp.prod(symbols[i]**a[i] for i in range(3)) for a in grids])
    base=(f0+Cz*Zbase).applyfunc(sp.expand)
    free=(Cz*sp.Matrix(old["smith_right"][:,37:])).applyfunc(sp.expand)
    # Retain a primitive 3-adic row lattice of the actual polynomial equations.
    mon4=sorted([a for a in product(range(5),repeat=3) if sum(a)<=4],key=lambda a:(sum(a),a))
    mon1=[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
    coefficient_rows=[]
    for i in range(4):
        row=[sp.Poly(base[i],symbols).coeff_monomial(a) for a in mon4]
        for j in range(8):row +=[sp.Poly(free[i,j],symbols).coeff_monomial(a) for a in mon1]
        assert all(x.q==1 for x in row)
        coefficient_rows.append([int(x) for x in row])
    polynomials=np.array(coefficient_rows,dtype=np.int64)
    transform=sp.eye(4)
    for i in range(4):
        common=reduce(gcd,(abs(int(x)) for x in polynomials[i] if x))
        polynomials[i]//=common;transform[i,:]=transform[i,:]/common
    polynomial_saturations=0
    while finite_rref(polynomials.T,3)[0]<4:
        relation=LinearSystem(polynomials.T%3).kernel[:,0];j=int(np.flatnonzero(relation)[0])
        numerator=relation@polynomials;assert not np.any(numerator%3)
        polynomials[j]=numerator//3
        transform[j,:]=(sp.Matrix(1,4,relation.tolist())*transform)/3
        polynomial_saturations+=1
        assert polynomial_saturations<30
    newbase=(transform*base).applyfunc(sp.expand)
    newfree=(transform*free).applyfunc(sp.expand)
    assert all(x.q==1 for expression in list(newbase)+list(newfree)
               for x in sp.Poly(expression,symbols).coeffs())
    finite_data=json.loads((HERE/"bc_fermat_class_three_tower_comparison.json").read_text())
    comparisons=[]
    for r in finite_data["target_records"]:
        vals=dict(zip(symbols,r["t_residue"]))
        matrix=np.array(newfree.subs(vals),dtype=np.int64)%3
        value=np.array(newbase.subs(vals),dtype=np.int64).ravel()%3
        system=LinearSystem(matrix)
        rhs=system.solve(-value%3)
        oldA=np.array(r["E37_free_parameter_equations"],dtype=np.int64)
        oldb=np.array(r["E37_free_parameter_rhs"],dtype=np.int64)
        rowrank=finite_rref(np.vstack((matrix,oldA)),3)[0]
        combined=LinearSystem(np.vstack((matrix,oldA)))
        consistent=combined.solve(np.r_[-value,oldb]%3) is not None
        comparisons.append({"target_index":r["target_index"],"t_residue":r["t_residue"],
            "new_polynomial_matrix_rank_mod3":system.rank,"combined_with_E44_rank":rowrank,
            "combined_affine_consistent":consistent,"polynomial_affine_solvable":rhs is not None})
        print("Residue",r["target_index"],"matrix rank",system.rank,
              "combined E44 rank",rowrank,"consistent",consistent,flush=True)
    result={"status":"exploratory rational obstruction only; integral Smith tests remain separate",
        "common_dual_invariant_rank":4,"invariant_lattice_saturation_steps":saturations,
        "polynomial_row_saturation_steps":polynomial_saturations,
        "variables":["t1","t2","t3"],"E37_relation":str(F),
        "new_constant_polynomials":[str(x) for x in newbase],
        "new_free_Smith_coefficient_matrix":[[str(newfree[i,j]) for j in range(8)] for i in range(4)],
        "rational_row_change":[[str(transform[i,j]) for j in range(4)] for i in range(4)],
        "comparisons_with_E44":comparisons,
        "elapsed_seconds":round(time.time()-start,3)}
    (HERE/"bc_fermat_class_three_rational_obstruction.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_three_rational_obstruction.npz",
        common_dual_invariants=invariant,raw_constant_coefficients=constant_coefficients,
        raw_Z_coefficients=np.stack([C0]+C),primitive_polynomial_coefficients=polynomials,
        constant_monomials=np.array(mon4),free_monomials=np.array(mon1))
    print(json.dumps(result,indent=2))
    print("PASS: exact rational norm obstruction polynomials; full integral tests not yet concluded.")

if __name__=="__main__":main()
