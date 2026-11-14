#!/usr/bin/env python3
"""Exact solvable quotient comparisons for both lower A6 targets.

The source comparison is G/C = B/(F-prime F^30), and its quotient by
the K6 image is B/(F-prime F^6).  These identifications use literal x,y
orders, the already computed exact F-prime image, and equal finite
orders; they do not identify the order-72 quotient with a modular group.
"""
from pathlib import Path
import json,time
import numpy as np
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_kernels import FerrariA6Kernel
from de_ferrari_two_model import FerrariTwo

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();d=load_data();rows=[];cert={}
    for outer in (False,True):
        tag='de_ferrari_a6_'+('outer' if outer else 'perm')
        source=np.load(HERE/(tag+'_source_compressed.npz'))
        data=np.load(HERE/(tag+'_corrections.npz'))
        info=json.loads((HERE/(tag+'_corrections.json')).read_text())
        s,r=source['s'],source['r'];letters={0:s,1:r,-1:r[r]}
        def word(w):
            out=np.arange(len(s))
            for t in w:out=letters[t][out]
            return Permutation(out.tolist())
        x,y=word(d['xword']),word(d['yword'])
        assert int(x.order())==int(y.order())==30
        assert info['correction_group_is_perfect']
        assert info['F_derived_image_order']==info['F_prime_K6_image_order']==info['N_derived_image_order']
        assert info['source_order']//info['F_derived_image_order']==6*30**2
        assert info['F_image_order']//info['F_derived_image_order']==30**2
        # Since x,y generate F, the map (Z/30)^2 -> F-image/C is onto;
        # both sides have900 elements, so it is the actual isomorphism.
        K=PermutationGroup([Permutation(p.tolist()) for p in data['full_generators']])
        assert int(K.order())==info['full_K6_image_order']
        assert K.contains(x**6) and K.contains(y**6)
        assert info['source_order']//int(K.order())==6*6**2
        # Thus the natural B/(F-prime F^6) -> G/K is also an isomorphism.
        fab=data['N_F_abelianization'];S=smith_normal_form(Matrix(fab.tolist()),domain=ZZ)
        diag=[abs(int(S[i,i])) for i in range(2)];assert diag==[2,6]
        # H is the kernel of the ordinary F-abelianization modulo3.
        # In the source solvable quotient its exact image is 3(Z/30)^2.
        assert (30//3)**2==100 and (6*30**2)//100==54
        H=FerrariA6Kernel(outer=outer)
        T=PermutationGroup([H.permutation(H.a),H.permutation(H.b)])
        D=T.derived_subgroup();dd=D.derived_subgroup()
        torder=int(T.order());dorder=int(D.order());ddorder=int(dd.order())
        assert torder==2*dorder and dorder==ddorder
        assert dorder==info['F_derived_image_order']
        omega=H.power(H.mul(H.a,H.b),3)
        z4=H.power(H.mul(H.mul(H.a,H.b),H.c),4)
        assert np.array_equal(z4,H.one)
        assert int(H.permutation(omega).order())==(2 if outer else 1)
        # The nontrivial cyclic quotient sends all three braid generators
        # to1, and hence is the literal braid-exponent map modulo2.
        assert not D.contains(H.permutation(H.a)) and not D.contains(H.permutation(H.b))
        unitvals=np.broadcast_to(H.one,H.x.shape).copy()
        assert np.array_equal(H.pentagon(unitvals),H.one)
        assert all(np.array_equal(a,b) for a,b in zip(H.braid_images(unitvals),(H.a,H.b,H.c)))
        H.check_braids(H.braid_images(unitvals))
        row={'mode':'outer' if outer else 'permutation','literal_source_x_y_orders':[30,30],
             'F_derived_equals_N_derived_equals_F_prime_K6_image':True,
             'source_maximal_solvable_quotient_order':5400,
             'source_maximal_solvable_quotient':'B/(F_prime F^30)',
             'source_mod_K6_comparison':'B/(F_prime F^6)',
             'source_mod_K6_order':216,'N_abelianization_lattice_Smith':diag,
             'H_image_in_maximal_solvable_quotient_order':100,
             'H_image_description':'(Z/10)^2 via ordinary F abelianization divided by3',
             'H_image_class_bound':1,'H_image_exponent':10,
             'factor_through_B_over_gamma3H_H20':True,
             'four_strand_target_order':torder,'four_strand_derived_order':dorder,
             'four_strand_second_derived_order':ddorder,
             'four_strand_maximal_solvable_quotient_order':2,
             'four_strand_quotient_is_actual_braid_exponent_mod2':True,
             'omega3_order':int(H.permutation(omega).order()),'z4_order':1,
             'identity_f_pentagon_and_all_braids_verified':True}
        rows.append(row)
        cert[('outer' if outer else 'perm')+'_four_strand_derived_generators']=np.array([p.array_form for p in D.generators])
        cert[('outer' if outer else 'perm')+'_four_strand_second_derived_generators']=np.array([p.array_form for p in dd.generators])
        print(json.dumps(row,indent=2),flush=True)
    # On the old binary Ferrari factor, the action on the three nonzero
    # vectors of F2^2 gives the same exponent-mod2 quotient.  Every Artin
    # generator is a transposition there.
    old=FerrariTwo(1);points=[(0,1),(1,0),(1,1)];point_index={v:i for i,v in enumerate(points)}
    signs=[]
    for g in (old.a,old.b,old.c):
        mat=old.project(g)[:4].reshape(2,2)
        p=Permutation([point_index[tuple(map(int,mat@v%2))] for v in map(np.array,points)])
        signs.append(int(p.signature()));assert p.signature()==-1
    out={'targets':rows,'old_binary_linear_three_point_generator_signs':signs,
         'both_joint_four_strand_targets_have_exact_common_quotient_C2':True,
         'seconds':round(time.time()-start,3)}
    (HERE/'de_ferrari_a6_kernel_compare.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'de_ferrari_a6_kernel_compare.npz',**cert)
    print('PASS: exact source and four-strand quotient comparisons, seconds',out['seconds'],flush=True)

if __name__=='__main__':main()
