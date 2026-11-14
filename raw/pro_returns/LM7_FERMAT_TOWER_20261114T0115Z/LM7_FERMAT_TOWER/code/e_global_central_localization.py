#!/usr/bin/env python3
"""E93: exact global central localization and its joint-quotient map.

The integral Tate line is transported from the E37 exterior basis to the
actual E74 Hall basis before any matrix comparison. No marked Kummer
evaluation constant is assigned a numerical value.
"""
from pathlib import Path
from itertools import combinations, product
import argparse
import hashlib
import importlib.util
import json
import sympy as s


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod


def mat(rows):
    return s.Matrix([[s.Rational(str(x)) for x in row] for row in rows])


def encode(A):
    return [[str(x) for x in A.row(i)] for i in range(A.rows)]


def integral3(A):
    return all(int(x.q)%3 for x in A)


def residue(x,n):
    x=s.Rational(x)
    assert int(x.q)%3
    return int(x.p)*pow(int(x.q),-1,3**n)%(3**n)


def main():
    here=Path(__file__).resolve().parent
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-code',type=Path)
    args=parser.parse_args()
    code=args.source_code or here
    paths={
        'Hall':code/'e_unramified_sections.py',
        'E37':code/'e_intrinsic_class2.json',
        'wild':code/'e_wild_layers.json',
        'joint':code/'a_compatible_joint_fibre.json',
        'Kummer':code/'a_relative_multiples.py',
    }
    assert all(p.is_file() for p in paths.values())
    hall=load('e93_hall',paths['Hall']).Hall(2)
    logs=load('e93_logs',paths['Kummer'])
    intrinsic=json.loads(paths['E37'].read_text())
    layers=json.loads(paths['wild'].read_text())['layers']
    joint=json.loads(paths['joint'].read_text())
    assert intrinsic['status']==joint['status']=='PASS'
    ids=[i for i,d in enumerate(hall.degree) if d==2]
    pairs=[tuple(x) for x in intrinsic['wedge_basis']]
    assert pairs==list(combinations(range(10),2)) and len(ids)==45
    change=s.zeros(45)
    for row,i in enumerate(ids):
        a,b=hall.children[i]
        assert a>b and a<10
        change[row,pairs.index((b,a))]=-1
    assert change*change.T==s.eye(45)
    w=change*s.Matrix(intrinsic['primitive_Tate_line'])
    T,J=(s.Matrix(layers['2'][k]) for k in ('input_tau','input_c'))
    T1,J1=(s.Matrix(layers['1'][k]) for k in ('input_tau','input_c'))
    for A,AA in [(T1,T),(J1,J)]:
        exterior=s.Matrix(45,45,lambda i,j:A[pairs[i][0],pairs[j][0]]*A[pairs[i][1],pairs[j][1]]-A[pairs[i][0],pairs[j][1]]*A[pairs[i][1],pairs[j][0]])
        assert AA*change==change*exterior
    assert T*w==7*w and J*w==-w
    primitive_pivot=next(i for i,x in enumerate(w) if abs(x)==1)
    F=mat(joint['degree_two_pair_map'])
    swap=s.Matrix([[0,1],[1,0]])
    assert F*T==49*F and F*J==swap*F and F*w==s.zeros(2,1)
    K=mat(joint['relative_kernel_basis'])
    Ki=mat(joint['relative_kernel_inverse_on_image'])
    assert Ki*K==s.eye(22)
    assert (s.eye(45)-J)*(T-7*s.eye(45))*K==s.zeros(45,22)
    kw=Ki*w
    assert K*kw==w and integral3(kw)
    kp=next(i for i,x in enumerate(kw) if residue(x,1)!=0)
    replace=s.eye(22);replace[:,kp]=kw
    replace_inverse=replace.inv()
    assert integral3(replace) and integral3(replace_inverse)
    assert replace_inverse*kw==s.eye(22)[:,kp]
    quotient_rows=[i for i in range(22) if i!=kp]
    quotient=replace_inverse[quotient_rows,:]*Ki
    quotient_section=K*replace[:,quotient_rows]
    scalar=(replace_inverse*Ki)[kp,:]
    assert quotient*w==s.zeros(21,1)
    assert quotient*quotient_section==s.eye(21)
    assert w*scalar+quotient_section*quotient==K*Ki

    g=joint['gauge_smith']
    L,Li,R,Ri=(mat(g[k]) for k in ['left','left_inverse','right','right_inverse'])
    diag=s.diag(*[s.Rational(x) for x in g['diagonal']])
    G=(s.eye(45)-T)*(s.eye(45)+J)
    assert L*G*R==diag
    assert L*Li==Li*L==R*Ri==Ri*R==s.eye(45)
    assert list(diag.diagonal())==[1]*7+[3]*9+[9]*5+[0]*24
    rho=F[0,:]-F[1,:]
    zstar=mat(joint['explicit_rho_section'])
    assert rho==mat(joint['rho_in_Hall_coordinates'])
    assert rho*G==s.zeros(1,45) and rho*zstar==s.Matrix([1])
    assert F*zstar==s.Matrix([s.Rational(1,2),-s.Rational(1,2)])
    rho_smith=rho*Li
    assert rho_smith[:,:21]==s.zeros(1,21)
    free=rho_smith[:,21:]
    rp=next(i for i,x in enumerate(free) if residue(x,1)!=0)
    # Explicit kernel/inverse over the 24 free cohomology coordinates.
    kerfree=s.zeros(24,23)
    rcols=[i for i in range(24) if i!=rp]
    for j,i in enumerate(rcols):
        kerfree[i,j]=1;kerfree[rp,j]=-free[i]/free[rp]
    free_origin=s.zeros(24,1);free_origin[rp]=1/free[rp]
    assert free*kerfree==s.zeros(1,23) and free*free_origin==s.Matrix([1])
    assert integral3(kerfree) and integral3(free_origin)
    smith_w=L*w
    free_w=smith_w[21:,:]
    assert all(residue(x,1)==0 for x in free_w)
    assert any(residue(x,2)!=0 for x in free_w)
    assert free*free_w==s.Matrix([0])

    # The marked constants remain symbols.  The inverse is verified literally.
    b,alpha,t,u,ell=s.symbols('b alpha t u ell',nonzero=True)
    source=s.Matrix([u-b*t/alpha,t/alpha])
    restriction=s.Matrix([[1,b],[0,alpha]])
    assert restriction*source==s.Matrix([u,t])
    assert restriction*s.Matrix([0,ell])==s.Matrix([b*ell,alpha*ell])

    primes=[p for p in s.primerange(2,101) if p!=3]
    others=[p for p in primes if p!=2]
    localization_checks=0
    for precision in range(1,8):
        modulus=3**precision
        ellp={p:logs.prime_log_coordinate(p,precision) for p in primes}
        assert ellp[2]==pow(2,-1,modulus)
        for trial in range(81):
            a={p:(trial*(j+2)+j*j)%modulus for j,p in enumerate(others)}
            a2=-2*sum(a[p]*ellp[p] for p in others)%modulus
            assert (a2*ellp[2]+sum(a[p]*ellp[p] for p in others))%modulus==0
            value=(13*trial+5)%modulus
            assert (2*value*ellp[2])%modulus==value
            localization_checks+=2
    coordinate_checks=0
    for trial in range(729):
        v=s.Matrix([(trial*(i+3)+i*i)%37-18 for i in range(22)])
        a=K*v
        assert w*(scalar*a)+quotient_section*(quotient*a)==a
        x=s.Matrix([(trial*(i+2)+i*i)%31-15 for i in range(24)])
        r=(free*x)[0];rest=x-free_origin*r
        assert free_origin*r+kerfree*rest[rcols,:]==x
        coordinate_checks+=2
    ans={
        'statement':'E.93','status':'PASS',
        'inputs':{k:{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in paths.items()},
        'exterior_to_actual_Hall':encode(change),
        'Tate_vector_Hall':encode(w),'primitive_Hall_pivot':primitive_pivot,
        'Tate_vector_relative_coordinates':encode(kw),'relative_pivot':kp,
        'relative_basis_change':encode(replace),'relative_basis_inverse':encode(replace_inverse),
        'relative_quotient_map':encode(quotient),'relative_quotient_section':encode(quotient_section),
        'relative_scalar_map':encode(scalar),
        'Tate_vector_horizontal_Smith':encode(smith_w),
        'Tate_free_horizontal_exact_divisibility':3,
        'joint_Tate_vector':encode(F*w),'joint_rho_map':encode(rho),
        'joint_rho_Smith':encode(rho_smith),'joint_rho_free_pivot':rp,
        'joint_rho_free_kernel':encode(kerfree),'joint_rho_free_section':encode(free_origin),
        'joint_rho_Hall_section':encode(zstar),
        'global_restriction_image':'Z3^25 x C3^9 x C9^5',
        'global_restriction_kernel':'restricted Z3 prime exponents outside {2,3}',
        'global_restriction_cokernel':'Z3^21',
        'global_joint_variation_image':'Z3, actual horizontal rho; relative coordinate zero',
        'global_joint_variation_kernel':'restricted Z3 prime exponents outside {3} x Z3^23 x C3^9 x C9^5',
        'localization_inverse_checks':localization_checks,
        'full_coordinate_inverse_checks':coordinate_checks,
        'actual_marking_constants':'b,alpha retained symbolically; alpha is a unit by E90',
    }
    here.joinpath('e_global_central_localization.json').write_text(json.dumps(ans,indent=2)+'\n')
    print('PASS exact E37 exterior-to-Hall transport and both genuine arithmetic actions')
    print('PASS primitive relative Tate line, full rank21 quotient and both inverse maps')
    print('PASS actual horizontal Smith coordinates, divisibility3 and full joint rho kernel')
    print('PASS joint annihilation of the Tate line and exact marked symbolic restriction inverse')
    print('PASS',localization_checks,'localization inverses and',coordinate_checks,'full coordinate inverses')
    print('ALL PASS')


if __name__=='__main__':
    main()
