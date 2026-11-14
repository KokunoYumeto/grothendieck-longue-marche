#!/usr/bin/env python3
"""Exact rational class-three equations on the actual E37 conic chart.

Put U=t1+t2, u=t2, t3=u+3e.  The E37 equation is
e+U^2+3Ue+9e^2=0, with U=c_source+3w.  The substitution and all row
divisions below are exact polynomial morphisms, and are saved.
This program does not discard the separate two integral Smith tests.
"""
from pathlib import Path
from functools import reduce
from math import gcd
import json,time
import numpy as np
import sympy as sp
from bc_fermat_class_two_fibres import LinearSystem
from bc_fermat_class_three_norm_smith_probe import finite_rref

HERE=Path(__file__).resolve().parent

def coefficient_matrix(rows,variables):
    monos=sorted(set().union(*(set(sp.Poly(x,variables).monoms()) for x in rows)),
                 key=lambda a:(sum(a),a))
    columns=[]
    for j in range(rows.cols):
        columns.extend([(j,m) for m in monos])
    matrix=sp.Matrix([[sp.Poly(rows[i,j],variables).coeff_monomial(m)
                       for j,m in columns] for i in range(rows.rows)])
    return matrix,columns

def main():
    start=time.time();old=json.loads((HERE/"bc_fermat_class_three_rational_obstruction.json").read_text())
    t1,t2,t3=sp.symbols("t1 t2 t3");U,u,e=sp.symbols("U u e")
    variables=(U,u,e);Phi=e+U**2+3*U*e+9*e**2
    oldrows=sp.Matrix([[sp.sympify(old["new_constant_polynomials"][i])]+
                      [sp.sympify(s) for s in old["new_free_Smith_coefficient_matrix"][i]]
                      for i in range(4)])
    rows=oldrows.subs({t1:U-u,t2:u,t3:u+3*e},simultaneous=True).applyfunc(sp.expand)
    transformation=sp.eye(4);divisors=[]
    for i in range(4):
        coefficients=[int(c) for x in rows.row(i) for c in sp.Poly(x,variables).coeffs()]
        common=reduce(gcd,(abs(c) for c in coefficients if c))
        rows[i,:]=rows[i,:]/common;transformation[i,:]=transformation[i,:]/common
        divisors.append(common)
    coeff,_=coefficient_matrix(rows,variables)
    reduced,change=coeff.lll_transform()
    assert reduced==change*coeff and abs(int(change.det()))==1
    rows=(change*rows).applyfunc(sp.expand);transformation=change*transformation
    # Saturation on the conic, with the precise polynomial multiples retained.
    corrections=[]
    for iteration in range(20):
        reduced_rows=rows.subs(e,-U**2).applyfunc(sp.expand)
        cm,_=coefficient_matrix(reduced_rows,(U,u))
        matrix=np.array(cm,dtype=np.int64)%3
        rank=finite_rref(matrix.T,3)[0]
        if rank==4:break
        relation=LinearSystem(matrix.T).kernel[:,0]
        j=int(np.flatnonzero(relation)[0])
        combination=(sp.Matrix(1,4,relation.tolist())*rows)
        new=[];quotients=[]
        for expression in combination:
            quotient,remainder=sp.div(expression,e+U**2,e)
            assert all(int(c)%3==0 for c in sp.Poly(remainder,U,u).coeffs())
            value=sp.expand(-U*e*quotient-3*e**2*quotient+remainder/3)
            assert sp.expand(expression-3*value-Phi*quotient)==0
            new.append(value);quotients.append(str(quotient))
        rows[j,:]=sp.Matrix(1,9,new)
        transformation[j,:]=(sp.Matrix(1,4,relation.tolist())*transformation)/3
        corrections.append({"replaced_row":j,"relation":relation.tolist(),
                            "Phi_multiple_quotients":quotients})
    else:raise AssertionError("curve saturation did not terminate within the retained bound")
    assert all(c.q==1 for x in rows for c in sp.Poly(x,variables).coeffs())
    assert all(sp.diff(rows[i,j],u)==0 for i in range(4) for j in range(1,9))
    finite=json.loads((HERE/"bc_fermat_class_three_tower_comparison.json").read_text())
    records=[]
    for r in finite["target_records"]:
        a,b,c=r["t_residue"];source=(a+b)%3
        values={U:source,u:b,e:(-source*source)%3}
        A=np.array(rows[:,1:].subs(values),dtype=np.int64)%3
        constant=np.array(rows[:,0].subs(values),dtype=np.int64).ravel()%3
        system=LinearSystem(A)
        oldA=np.array(r["E37_free_parameter_equations"],dtype=np.int64)
        oldb=np.array(r["E37_free_parameter_rhs"],dtype=np.int64)
        joint=LinearSystem(np.vstack((A,oldA)))
        joint_sol=joint.solve(np.r_[-constant,oldb]%3)
        rec={"target_index":r["target_index"],"source_residue":source,"u_residue":b,
            "rational_equation_matrix_rank_mod3":system.rank,
            "rational_equation_pivot_columns":system.pivots,
            "joint_rank_with_E44":joint.rank,"joint_affine_solvable":joint_sol is not None,
            "matrix_mod3":A.tolist(),"constant_mod3":constant.tolist()}
        records.append(rec)
        print("Chart",source,b,"rational rank",system.rank,"joint E44",joint.rank,
              "solvable",joint_sol is not None,flush=True)
    out={"status":"exploratory rational chart; two integral tests remain separate",
        "old_to_new_chart":{"t1":"U-u","t2":"u","t3":"u+3e",
                            "U":"c_source+3w","equation":str(Phi)},
        "row_content_divisors_after_exact_substitution":divisors,
        "constant_row_change":[[str(transformation[i,j]) for j in range(4)] for i in range(4)],
        "conic_saturation_corrections":corrections,
        "constant_polynomials":[str(x) for x in rows[:,0]],
        "free_Smith_coefficient_matrix":[[str(rows[i,j]) for j in range(1,9)] for i in range(4)],
        "finite_charts":records,"elapsed_seconds":round(time.time()-start,3)}
    (HERE/"bc_fermat_class_three_curve_obstruction.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
    print("PASS: exact conic substitution, rational equations and every retained residue chart.")

if __name__=="__main__":main()
