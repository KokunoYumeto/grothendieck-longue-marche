#!/usr/bin/env python3
"""Complete integral central right inverse and exact E44 fibre projection.

All 3-adic divisions are performed using saved integral matrices and a
specified unit minor.  Finite evaluations retain enough extra precision
for division by three.  No formal Lie lattice is substituted for the
actual Hall group lattice.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time
import numpy as np
import sympy as sp
import bc_fermat_class_three_integral as q
import bc_fermat_class_three_burnside as finite
from bc_fermat_class_two_fibres import LinearSystem
from bc_fermat_class_three_norm_smith_probe import finite_rref

HERE=Path(__file__).resolve().parent
OLD=np.load(HERE/'bc_fermat_class_two_3adic_norms.npz')
CURVE=json.loads((HERE/'bc_fermat_class_three_curve_obstruction.json').read_text())
GRAPH=json.loads((HERE/'bc_fermat_class_three_graph_tests.json').read_text())
U,u,e=sp.symbols('U u e')
MATRIX=sp.Matrix([[sp.sympify(v) for v in row] for row in CURVE['free_Smith_coefficient_matrix']])
PHI=U**2+3*U*e+e+9*e**2
CONSTANT=sp.Matrix([sp.rem(sp.sympify(v),PHI,U) for v in CURVE['constant_polynomials']])
AM=sp.lambdify((U,u,e),MATRIX,'numpy');AC=sp.lambdify((U,u,e),CONSTANT,'numpy')
PIVOTS=[0,1,2,4];FREE=[3,5,6,7]
RECORDS={(r['source_residue'],r['u_residue']):r for r in GRAPH['records']}

def inverse_mod(a,modulus):
    a=np.asarray(a,dtype=np.int64).copy()%modulus
    inv=np.eye(a.shape[0],dtype=np.int64)
    for j in range(a.shape[0]):
        nz=np.flatnonzero(a[j:,j]%3);assert len(nz)
        k=j+int(nz[0]);a[[j,k]]=a[[k,j]];inv[[j,k]]=inv[[k,j]]
        scale=pow(int(a[j,j]),-1,modulus)
        a[j]=a[j]*scale%modulus;inv[j]=inv[j]*scale%modulus
        coefficient=a[:,j].copy();coefficient[j]=0
        a=(a-coefficient[:,None]*a[j][None,:])%modulus
        inv=(inv-coefficient[:,None]*inv[j][None,:])%modulus
    assert np.array_equal(a,np.eye(a.shape[0],dtype=np.int64))
    return inv

def conic_root(Uvalue,modulus):
    root=(-Uvalue*Uvalue)%3;power=3
    while power<modulus:
        next_power=3*power
        candidates=[root+k*power for k in range(3)]
        candidates=[v for v in candidates if (v+Uvalue*Uvalue+3*Uvalue*v+9*v*v)%next_power==0]
        assert len(candidates)==1;root=candidates[0];power=next_power
    assert power==modulus
    return root

def base_point(source,parameters,modulus):
    """Six parameters are (u,w,b2,b3,h0,h1), all in Z3."""
    uvalue,w,b2,b3,h0,h1=[int(a)%modulus for a in parameters]
    Uvalue=(source+3*w)%modulus;root=conic_root(Uvalue,modulus)
    r=RECORDS[(source,uvalue%3)];rhs=np.array(r['integral_test_rhs'],dtype=np.int64)
    b0=(2*(int(rhs[0])-b2-b3))%3
    b1=(int(rhs[1])-(source+2)*b0+source*(b2+b3))%3
    b=np.array([b0+3*h0,b1+3*h1,b2,b3],dtype=np.int64)%modulus
    A=np.asarray(AM(Uvalue,uvalue,root),dtype=np.int64)%modulus
    h=np.asarray(AC(Uvalue,uvalue,root),dtype=np.int64).ravel()%modulus
    a=np.zeros(8,dtype=np.int64);a[FREE]=b
    a[PIVOTS]=inverse_mod(A[:,PIVOTS],modulus)@(-h-A[:,FREE]@b)%modulus
    assert not np.any((A@a+h)%modulus)
    assert not np.any((np.array(r['integral_test_matrix_on_four_free_variables'])@b-rhs)%3)
    t=np.array([Uvalue-uvalue,uvalue,uvalue+3*root],dtype=np.int64)%modulus
    t1,t2,t3=[int(x) for x in t]
    mon=np.array([t1*t1,t2*t2,t3*t3,t1*t2,t1*t3,t2*t3],dtype=np.int64)
    transformed=(OLD['transformed_error_linear']@t+OLD['transformed_error_quadratic']@mon)
    Y=np.zeros(45,dtype=np.int64)
    for i in range(35):
        assert abs(int(OLD['smith'][i,i]))==1
        Y[i]=-transformed[i]//int(OLD['smith'][i,i])
    Q=t1*t1+t2*t2+t3*t3+t1*t2+t1*t3-t2*t3
    G=t2+t3-3*t1*t1-4*t2*t2-2*t3*t3-3*t1*t2-5*t1*t3+5*t2*t3-(t3-t2)*Q
    Y[35]=-G;Y[36]=t1-t3;Y[37:]=a
    v=OLD['abelian_norm_basis']@t%modulus
    Z=OLD['smith_right']@(Y%modulus)%modulus
    assert (t3-t2+3*Q)%modulus==0
    return v,Z,{'U':Uvalue,'u':uvalue,'e':root,'t':t.tolist(),'free_Smith':a.tolist()}

def main():
    start=time.time();data=np.load(HERE/'bc_fermat_class_three_integral_tests.npz')
    reduction_quotients=[]
    for original,reduced in zip(CURVE['constant_polynomials'],CONSTANT):
        quotient,remainder=sp.div(sp.sympify(original),PHI,U)
        assert sp.expand(remainder-reduced)==0
        assert sp.expand(sp.sympify(original)-reduced-PHI*quotient)==0
        reduction_quotients.append(str(quotient))
    assert sp.expand(MATRIX[:,PIVOTS].det()+16*(1-3*U-3*e)+480*PHI)==0
    full=np.load(HERE/'bc_fermat_class_three_integral.npz')
    M=full['triple_norm'];N=data['saturated_image'];numerator=data['saturated_image_preimage_numerator']
    assert int(data['saturated_image_preimage_denominator'])==9 and not np.any(numerator%3)
    P=numerator//3;assert np.array_equal(M@P,3*N)
    assert finite_rref(P,3)[0]==2
    _,rows,_=finite_rref(N.T,3);minor=N[rows]
    inverse3=inverse_mod(minor,3)
    inverse9=inverse_mod(minor,9)
    assert np.array_equal(inverse9%3,inverse3)
    K=data['exact_integral_kernel'];projection=data['exact_kernel_projection_to_E44']
    finite_data=np.load(HERE/'bc_fermat_class_three_norms.npz');KF=finite_data['triple_norm_kernel']
    system=LinearSystem(projection)
    excluded=next(KF[:,j] for j in range(KF.shape[1]) if system.solve(KF[:,j]) is None)
    equations=np.vstack((projection.T,excluded[None,:]));rhs=np.r_[np.zeros(K.shape[1],dtype=np.int64),1]
    functional=LinearSystem(equations).solve(rhs);assert functional is not None
    assert not np.any(functional@projection%3) and int(functional@excluded%3)==1
    assert not np.any(finite_data['triple_norm_matrix']@excluded%3)
    ordinary=np.zeros(330,dtype=np.int64)
    for coefficient,(i,j,k) in zip(excluded,finite.TRIPLES):
        if coefficient:ordinary+=int(coefficient)*q.BRACKET_BY_GENERATOR[:,i,q.PAIRS.index((j,k))]
    assert np.array_equal(q.PROJECTION@ordinary%3,excluded)
    nonlift=np.r_[np.zeros(55,dtype=np.int64),12*ordinary]
    assert np.array_equal(q.projection_exp3(nonlift),np.r_[np.zeros(55,dtype=np.int64),excluded])
    assert not np.any(finite.norm_errors(q.projection_exp3(nonlift)))
    # The exact central right inverse is P*(N_rows)^(-1)*b_rows/3.
    # For its reduction modulo m, lower coordinates need precision 9*m.
    rng=np.random.default_rng(2026111348);sample_records=[]
    cache={9:inverse9,27:inverse_mod(minor,27)}
    for source in range(3):
        for ubar in range(3):
            for sample in range(3):
                parameters=rng.integers(0,9,size=6,dtype=np.int64)
                parameters[0]=ubar+3*(int(parameters[0])%3)
                modulus=3 if sample<2 else 9;precision=9*modulus
                v,Z,chart=base_point(source,parameters,precision)
                g=q.canonical(v,Z);errors=q.norm_errors(g)
                assert not np.any(errors[np.r_[np.arange(55),np.arange(385,440)]]%precision)
                E=np.r_[errors[55:385],errors[440:770]]%precision
                assert not np.any(E%3)
                b=-(E//3)*pow(4,-1,3*modulus)%(3*modulus)
                z=cache[3*modulus]@b[rows]%(3*modulus)
                assert np.array_equal(N@z%(3*modulus),b)
                pc=P@z%(3*modulus);assert not np.any(pc%3)
                c=(pc//3)%modulus
                assert np.array_equal(M@c%modulus,b%modulus)
                g[55:]+=12*c;new_errors=q.norm_errors(g)
                assert not np.any(new_errors[55:385]%(3*modulus))
                assert not np.any(new_errors[440:770]%(3*modulus))
                finite_g=q.projection_exp3(g)
                assert not np.any(finite.norm_errors(finite_g))
                for _ in range(2):
                    alpha=rng.integers(0,3,size=64,dtype=np.int64)
                    shifted=g.copy();shifted[55:]+=12*K@alpha
                    assert np.array_equal(q.norm_errors(shifted),new_errors)
                    assert np.array_equal(q.projection_exp3(shifted)[55:],
                                          (finite_g[55:]+projection@alpha)%3)
                sample_records.append({'source_residue':source,'u_residue':ubar,
                    'parameters':parameters.tolist(),'central_precision':modulus,
                    'class_two_precision':precision,'chart':chart,
                    'central_particular_mod3':(c%3).tolist(),
                    'finite_class_three_image':finite_g.tolist()})
    sources=json.loads((HERE/'bc_fermat_class_three_tower_comparison.json').read_text())['source_records']
    print('Exact right inverse and all27 extra-precision evaluations pass',flush=True)
    result={'status':'complete integral class-three fibres and exact finite E44 projection',
            'source_points_surviving':len(sources),'rational_base_parameters':6,
            'central_kernel_rank':64,'complete_correction_image_parameter_space':'Z3^70',
            'central_particular_formula':'P*(N_rows)^(-1)*b_rows/3, with M*P=3*N',
            'reduced_rational_constant_polynomials':[str(x)for x in CONSTANT],
            'constant_reduction_Phi_quotients':reduction_quotients,
            'pivot_minor_identity':'det(A_P)=-16*(30*Phi+1-3U-3e)',
            'fixed_E37_point_finite_central_image_dimension':21,
            'E44_central_fibre_dimension':22,
            'fixed_E37_point_fraction_of_E44_central_fibre_lifting':'1/3',
            'excluded_central_vector':excluded.tolist(),
            'triple_support_labels':'zero based; label i denotes eta_(i+1)',
            'excluded_central_vector_support':[[list(t),int(a)] for t,a in zip(finite.TRIPLES,excluded) if a],
            'nonlifting_functional_support':[[list(t),int(a)] for t,a in zip(finite.TRIPLES,functional) if a],
            'nonlifting_functional_value':1,
            'sample_records':sample_records,'elapsed_seconds':round(time.time()-start,3)}
    (HERE/'bc_fermat_class_three_fibres.json').write_text(json.dumps(result,indent=2)+'\n')
    np.savez_compressed(HERE/'bc_fermat_class_three_fibres.npz',
        right_inverse_numerator=P,saturated_image_minor_rows=np.array(rows),
        minor_inverse_mod9=inverse9,excluded_finite_central=excluded,
        excluded_ordinary_Lie_preimage=ordinary,nonlifting_functional=functional,
        nonlifting_actual_Hall_log=nonlift)
    print(json.dumps({k:v for k,v in result.items() if k not in
        ('sample_records','excluded_central_vector')},indent=2))
    print('PASS: complete central right inverse, Z3^70 fibre, and exact codimension-one finite central obstruction.')

if __name__=='__main__':main()
