#!/usr/bin/env python3
"""Exact image of the full integral class-three family in E44.

Two additional equations on the finite E37 coordinates characterize the
image.  The missing central direction over a fixed exact lower point is
supplied by an actual change of a higher lower-central parameter.  The
derivative calculation is integral and retains its exact right inverse.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time
import numpy as np
import sympy as sp
import bc_fermat_class_three_integral as q
import bc_fermat_class_three_burnside as finite
from bc_fermat_class_three_fibres import inverse_mod,base_point
from bc_fermat_class_two_fibres import LinearSystem
from bc_fermat_class_three_norm_smith_probe import finite_rref

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();fib=np.load(HERE/'bc_fermat_class_three_fibres.npz')
    data=np.load(HERE/'bc_fermat_class_three_integral_tests.npz')
    ints=np.load(HERE/'bc_fermat_class_three_integral.npz')
    graph=np.load(HERE/'bc_fermat_class_three_graph_tests.npz')
    old=np.load(HERE/'bc_fermat_class_two_3adic_norms.npz')
    records=json.loads((HERE/'bc_fermat_class_three_graph_tests.json').read_text())['records']
    oldrecords=json.loads((HERE/'bc_fermat_class_three_tower_comparison.json').read_text())['target_records']
    curves=json.loads((HERE/'bc_fermat_class_three_curve_obstruction.json').read_text())['finite_charts']
    N=data['saturated_image'];P=fib['right_inverse_numerator'];rows=fib['saturated_image_minor_rows']
    inverse=inverse_mod(N[rows],3);projection=ints['projection_exp3_central']
    kernel=data['exact_kernel_projection_to_E44'];functional=fib['nonlifting_functional']
    finite_data=np.load(HERE/'bc_fermat_class_three_norms.npz')
    out_records=[];derivatives=[];finite_points=[]
    for r,o,curve in zip(records,oldrecords,curves):
        c,u=r['source_residue'],r['u_residue'];t=np.array([(c-u)%3,u,u])
        Cm=graph['central_error_mixed_div3'][0]+sum(t[i]*graph['central_error_mixed_div3'][i+1]for i in range(3))
        direction=old['smith_right'][:,37:]@np.array(r['rational_kernel_mod3'])
        # Adding three times a rational free-coordinate direction preserves
        # both integral residue tests and every class-two mod-three value.
        derivative=-P@inverse@(Cm@direction)[rows]%3
        finite_derivative=projection@derivative%3
        assert not np.any(finite_data['triple_norm_matrix']@finite_derivative%3)
        character=functional@finite_derivative%3
        assert character.tolist()==[2,0,1,1]
        assert finite_rref(np.column_stack((kernel,finite_derivative)),3)[0]==22
        derivatives.append(finite_derivative)
        A=np.array(curve['matrix_mod3']);h=np.array(curve['constant_mod3'])
        new=np.array([[2,2,1,2,2,0,0,1],
                      [c+2,2,2*c+2,2,2,2*c+2,2*c,c+2]],dtype=np.int64)%3
        rhs=-np.array([2*c+2*u*u+u,
                      (c+2)*u*u+(2*c+1)*u+c*c+2*c],dtype=np.int64)%3
        assert np.array_equal(new,A[[0,2]]) and np.array_equal(rhs,-h[[0,2]]%3)
        oldA=np.array(o['E37_free_parameter_equations']);oldb=np.array(o['E37_free_parameter_rhs'])
        joint=LinearSystem(np.vstack((oldA,new)));assert joint.rank==6
        joint_solution=joint.solve(np.r_[oldb,rhs]);assert joint_solution is not None
        origin=np.array(r['rational_origin_mod3']);K=np.array(r['rational_kernel_mod3'])
        test=np.array(r['integral_test_matrix_on_four_free_variables']);test_rhs=np.array(r['integral_test_rhs'])
        admissible=[]
        for b2,b3 in product(range(3),repeat=2):
            b0=2*(int(test_rhs[0])-b2-b3)%3
            b1=(int(test_rhs[1])-(c+2)*b0+c*(b2+b3))%3
            b=np.array([b0,b1,b2,b3]);a=(origin+K@b)%3
            assert not np.any((test@b-test_rhs)%3)
            assert not np.any((oldA@a-oldb)%3) and not np.any((new@a-rhs)%3)
            admissible.append(a.tolist())
            v,Z,_=base_point(c,[u,0,b2,b3,0,0],27)
            finite_points.append(np.r_[v%3,2*Z%3])
        assert len({tuple(a)for a in admissible})==9
        out_records.append({'source_residue':c,'u_residue':u,
            'additional_equation_matrix':new.tolist(),'additional_equation_rhs':rhs.tolist(),
            'admissible_free_Smith_residues':admissible,
            'higher_parameter_central_character':character.tolist(),
            'full_central_image_dimension':22})
    for source in range(3):
        assert sum(r['source_residue']==source for r in out_records)==3
    # An E44 point compatible with the full E37 zero-abelian tower, but
    # outside the exact finite image of the full class-three group.
    Z=old['smith_right'][:,41].copy()
    base=q.canonical(np.zeros(10,dtype=np.int64),Z)
    finite_base=q.projection_exp3(base)
    assert not np.any(finite_base[55:])
    errors=finite.norm_errors(finite_base)
    central_error=np.r_[errors[55:175],errors[230:350]]
    central=LinearSystem(finite_data['triple_norm_matrix']).solve(-central_error%3)
    assert central is not None
    target=finite_base.copy();target[55:]=(target[55:]+central)%3
    assert not np.any(finite.norm_errors(target))
    a=np.zeros(8,dtype=np.int64);a[4]=1
    zero=next(r for r in out_records if r['source_residue']==r['u_residue']==0)
    assert not np.any(np.array(oldrecords[0]['E37_free_parameter_equations'])@a%3)
    obstruction=np.array(zero['additional_equation_matrix'])@a%3
    assert obstruction.tolist()==[2,2]
    source_data=json.loads((HERE/'bc_fermat_class_two_3adic_tower.json').read_text())
    source_records=source_data['source_rows'];assert len(source_records)==432
    CM=Counter(r['certificate_index']for r in source_records)
    assert len(CM)==24 and set(CM.values())=={18}
    result={'status':'complete exact finite image of the integral class-three family',
            'source_points':432,'CM_rows':24,'points_per_CM_row':18,
            'admissible_P3_images_per_source':3**3,
            'complete_E44_images_per_source':3**25,
            'all_E44_images_per_source':3**28,
            'E44_images_compatible_with_full_E37_per_source':3**27,
            'additional_equations_after_E44_and_full_E37':2,
            'every_finite_central_solution_over_an_admitted_P3_point_lifts':True,
            'mechanism':'h0 changes by one; its extra central character is two on every chart',
            'records':out_records,
            'new_nonlifting_point':{'source':{'certificate_index':0,'ternary_parameters':[0,0],'binary_parameter':0},
                'E37_parameters':'u=w=0, Y41=1, all other free Y=0',
                'integral_doubled_log':Z.tolist(),'finite_E44_value':target.tolist(),
                'finite_E44_norm_zero':True,'additional_equation_values':obstruction.tolist(),
                'fails_even_after_changing_all_higher_class_two_digits':True},
            'elapsed_seconds':round(time.time()-start,3)}
    (HERE/'bc_fermat_class_three_finite_image.json').write_text(json.dumps(result,indent=2)+'\n')
    np.savez_compressed(HERE/'bc_fermat_class_three_finite_image.npz',
        higher_parameter_central_derivatives=np.stack(derivatives),
        admissible_class_two_reductions=np.stack(finite_points),
        new_nonlifting_doubled_log=Z,new_nonlifting_finite_E44=target,
        new_nonlifting_central_correction=central)
    print(json.dumps({k:v for k,v in result.items()if k not in ('records','new_nonlifting_point')},indent=2))
    print('New nonlift: u=w=0,Y41=1; finite E44 norms vanish, additional equations give',obstruction.tolist())
    print('PASS: all432 fibres, complete finite image, higher-parameter central surjectivity, and explicit E44 nonlift.')

if __name__=='__main__':main()
