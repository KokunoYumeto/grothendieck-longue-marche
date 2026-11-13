#!/usr/bin/env python3
"""Solve the two integral central tests on the exact rational E37 chart.

The norm errors are reconstructed as exact integer polynomials.  Their two
Smith functionals are divided by three after substituting the actual E37
chart and checking coefficientwise divisibility there.  They are then
evaluated on every retained residue chart.  This is
separate from, and does not change, the accepted E44 certificates.
"""
from pathlib import Path
from itertools import product
import json,time
import numpy as np
import sympy as sp
import bc_fermat_class_three_integral as q
from bc_fermat_class_two_fibres import LinearSystem
from bc_fermat_class_three_norm_smith_probe import finite_rref

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();old=np.load(HERE/'bc_fermat_class_two_3adic_norms.npz')
    tests=np.load(HERE/'bc_fermat_class_three_integral_tests.npz')['integral_tests']
    B=old['abelian_norm_basis'];zero=np.zeros(45,dtype=np.int64)
    def error(t,Z):
        g=q.canonical(B@np.asarray(t,dtype=np.int64),Z)
        errors=q.norm_errors(g)
        return np.r_[errors[55:385],errors[440:770]]
    grids=sorted([a for a in product(range(4),repeat=3) if sum(a)<=3],key=lambda a:(sum(a),a))
    evaluation=sp.Matrix([[sp.prod(int(t[i])**a[i] for i in range(3)) for a in grids] for t in grids])
    values=np.stack([error(t,zero) for t in grids])
    coefficients=evaluation.inv()*sp.Matrix(values.tolist())
    assert all(a.q==1 for a in coefficients)
    constant=np.array(coefficients,dtype=np.int64).T
    tzero=np.zeros(3,dtype=np.int64)
    base=error(tzero,zero)
    C0=np.stack([error(tzero,z)-base for z in np.eye(45,dtype=np.int64)],axis=1)
    mixed=[C0]
    for i in range(3):
        t=np.eye(3,dtype=np.int64)[i];base=error(t,zero)
        mixed.append(np.stack([error(t,z)-base for z in np.eye(45,dtype=np.int64)],axis=1)-C0)
    mixed=np.stack(mixed);assert not np.any(mixed%3);mixed//=3
    rng=np.random.default_rng(2026111347)
    for _ in range(20):
        t=rng.integers(-3,4,size=3);Z=rng.integers(-3,4,size=45)
        mon=np.array([np.prod(t**np.array(a)) for a in grids],dtype=np.int64)
        expected=constant@mon+3*(mixed[0]+sum(t[i]*mixed[i+1] for i in range(3)))@Z
        assert np.array_equal(expected,error(t,Z))
    test_constant=tests@constant
    test_mixed=np.stack([tests@v%3 for v in mixed])
    t1,t2,t3=sp.symbols('t1 t2 t3');symbols=(t1,t2,t3)
    t=sp.Matrix(symbols);mon2=sp.Matrix([t1*t1,t2*t2,t3*t3,t1*t2,t1*t3,t2*t3])
    E=sp.Matrix(old['transformed_error_linear'])*t+sp.Matrix(old['transformed_error_quadratic'])*mon2
    Q=t1*t1+t2*t2+t3*t3+t1*t2+t1*t3-t2*t3
    G=t2+t3-3*t1*t1-4*t2*t2-2*t3*t3-3*t1*t2-5*t1*t3+5*t2*t3-(t3-t2)*Q
    Y=[-E[i]/int(old['smith'][i,i]) for i in range(35)]+[-G,t1-t3]
    Zbase=sp.Matrix(old['smith_right'][:,:37])*sp.Matrix(Y)
    Cm=sp.Matrix(test_mixed[0])+sum((symbols[i]*sp.Matrix(test_mixed[i+1]) for i in range(3)),sp.zeros(2,45))
    constant_test=(sp.Matrix(test_constant)*sp.Matrix([sp.prod(symbols[i]**a[i] for i in range(3)) for a in grids])/3+Cm*Zbase).applyfunc(sp.expand)
    free_test=(Cm*sp.Matrix(old['smith_right'][:,37:])).applyfunc(sp.expand)
    chart=json.loads((HERE/'bc_fermat_class_three_curve_obstruction.json').read_text())
    finite=json.loads((HERE/'bc_fermat_class_three_tower_comparison.json').read_text())
    U,u,e=sp.symbols('U u e')
    substitution={t1:U-u,t2:u,t3:u+3*e}
    constant_test=constant_test.subs(substitution,simultaneous=True).applyfunc(sp.expand)
    free_test=free_test.subs(substitution,simultaneous=True).applyfunc(sp.expand)
    assert all(a.q==1 for expression in list(constant_test)+list(free_test)
               for a in sp.Poly(expression,U,u,e).coeffs())
    chart_matrix=sp.Matrix([[sp.sympify(v) for v in row] for row in chart['free_Smith_coefficient_matrix']])
    chart_constant=sp.Matrix([sp.sympify(v) for v in chart['constant_polynomials']])
    pivots=[0,1,2,4];free=[3,5,6,7]
    determinant=sp.factor(chart_matrix[:,pivots].det())
    records=[]
    for f in finite['target_records']:
        a,b,d=f['t_residue'];c=(a+b)%3
        values={U:c,u:b,e:(-c*c)%3};tvalues=dict(zip(symbols,(a,b,d)))
        A=np.array(chart_matrix.subs(values),dtype=np.int64)%3
        h=np.array(chart_constant.subs(values),dtype=np.int64).ravel()%3
        P=LinearSystem(A[:,pivots]);assert P.rank==4
        origin=np.zeros(8,dtype=np.int64);origin[pivots]=P.solve(-h%3)
        kernel=np.zeros((8,4),dtype=np.int64);kernel[free]=np.eye(4,dtype=np.int64)
        kernel[pivots]=np.column_stack([P.solve(-A[:,j]%3) for j in free])
        C=np.array(free_test.subs(values),dtype=np.int64)%3
        k=np.array(constant_test.subs(values),dtype=np.int64).ravel()%3
        small=C@kernel%3;rhs=-(k+C@origin)%3;system=LinearSystem(small)
        assert system.rank==2 and system.solve(rhs) is not None
        oldA=np.array(f['E37_free_parameter_equations'],dtype=np.int64)
        oldb=np.array(f['E37_free_parameter_rhs'],dtype=np.int64)
        augmented=np.column_stack((np.vstack((A,C)),np.r_[h,k]))%3
        augmented_old=np.column_stack((np.vstack((A,oldA)),np.r_[h,-oldb]))%3
        assert finite_rref(augmented,3)[0]==6
        assert finite_rref(augmented_old,3)[0]==6
        assert finite_rref(np.vstack((augmented,augmented_old)),3)[0]==6
        rec={'target_index':f['target_index'],'source_residue':c,'u_residue':b,
             'rational_pivot_columns':pivots,'rational_free_columns':free,
             'rational_origin_mod3':origin.tolist(),'rational_kernel_mod3':kernel.tolist(),
             'integral_test_matrix_on_four_free_variables':small.tolist(),
             'integral_test_rhs':rhs.tolist(),'integral_test_rank':system.rank,
             'integral_test_pivots':system.pivots,
             'equivalence_to_E44_after_rational_equations':True}
        records.append(rec)
        print('Chart',c,b,'integral tests',small.tolist(),'rhs',rhs.tolist(),flush=True)
    result={'status':'complete four rational equations and two integral tests on every E37 source chart',
            'weighted_central_error_coefficientwise_divisible_by_three_on_actual_E37_chart':True,
            'rational_common_minor_columns':pivots,'rational_common_minor_determinant':str(determinant),
            'rational_free_columns':free,'integral_tests_depend_only_on_parameters_mod3':True,
            'all_nine_source_residue_charts_solvable':True,
            'free_residue_dimension_after_two_integral_tests':2,
            'complete_base_locus_is_nine_residue_disks_over_each_base_parameter_pair':True,
            'records':records,'elapsed_seconds':round(time.time()-start,3)}
    (HERE/'bc_fermat_class_three_graph_tests.json').write_text(json.dumps(result,indent=2)+'\n')
    np.savez_compressed(HERE/'bc_fermat_class_three_graph_tests.npz',
        central_error_constant=constant,central_error_mixed_div3=mixed,
        constant_monomials=np.array(grids),integral_test_constant_before_division=test_constant,
        integral_test_mixed_mod3=test_mixed)
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
    print('PASS: every exact rational chart has a nonempty integral lifting locus of codimension two modulo three.')

if __name__=='__main__':main()
