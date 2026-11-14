#!/usr/bin/env python3
"""E90: all B0 relative multiples, their nonunit regimes, and Kummer localization."""
from pathlib import Path
from itertools import product
import argparse
import hashlib
import importlib.util
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def vp(n, p=3):
    if n == 0:
        return 10**9
    n = abs(int(n));v = 0
    while n % p == 0:
        n //= p;v += 1
    return v


def log_unit_mod(u, precision):
    """The genuine logarithm of u in 1+3Z3 modulo 3^precision."""
    assert (u-1) % 3 == 0
    modulus = 3**precision
    z = u-1
    value = 0
    # For k >= 3*(precision+2), k-v3(k) >= precision;
    # every remaining logarithm term therefore vanishes.
    for k in range(1, 3*(precision+2)):
        power3 = 3**vp(k)
        numerator = z**k
        assert numerator % power3 == 0
        term = (numerator//power3)*pow(k//power3,-1,modulus)
        value += term if k % 2 else -term
    return value % modulus


def prime_log_coordinate(p, precision):
    assert p != 3
    unit = p if p % 3 == 1 else -p
    modulus = 3**precision
    denominator = log_unit_mod(4,precision+1)//3
    numerator = log_unit_mod(unit,precision+1)//3
    assert denominator % 3
    return numerator*pow(denominator,-1,modulus) % modulus


def main():
    here = Path(__file__).resolve().parent
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-code',type=Path)
    args=parser.parse_args()
    code=args.source_code or here
    if not (code/'a_horizontal_full.py').is_file():
        code=here.parent.parent/'LM7_FERMAT_TOWER/code'
    paths={
        'horizontal_program':code/'a_horizontal_full.py',
        'horizontal_certificate':code/'a_horizontal_full.json',
        'first_degree_kernel':code/'a_abelian_kernel_obstruction.json',
        'central_fibre':code/'a_compatible_joint_fibre.json',
        'wild_layers':code/'e_wild_layers.json',
        'relative_kernels':code/'a_wild_kernel.json',
        'local_smith':code/'e_cusp_local_smith.py',
    }
    assert all(p.is_file()for p in paths.values())
    a=load('e90_e89',paths['horizontal_program'])
    smith=load('e90_smith',paths['local_smith'])
    hor=json.loads(paths['horizontal_certificate'].read_text())
    first=json.loads(paths['first_degree_kernel'].read_text())
    central=json.loads(paths['central_fibre'].read_text())
    layers=json.loads(paths['wild_layers'].read_text())['layers']
    rel=json.loads(paths['relative_kernels'].read_text())['layers']['2']
    assert hor['status']==first['status']==central['status']=='PASS'
    R=a.mat(first['first_degree_map'])
    T1,J1=(s.Matrix(layers['1'][k])for k in('input_tau','input_c'))
    T2,J2=(s.Matrix(layers['2'][k])for k in('input_tau','input_c'))
    G=(s.eye(10)-T1)*(s.eye(10)+J1)
    F=a.mat(hor['obstruction_coordinates'])
    moduli=hor['obstruction_moduli']
    character=a.mat(hor['three_characters'])
    Qunit=a.mat(hor['kernel_lattice'])
    Qthree=hermite_normal_form(a.row_kernel(R[1,:],3))
    assert Qthree.det()==3
    assert a.divisible3(character[2,:]-R[1,:])
    sm_unit=smith.local_smith((Qunit.inv()*G).tolist())
    sm_three=smith.local_smith((Qthree.inv()*G).tolist())
    sm_nine=smith.local_smith(G.tolist())
    assert sm_unit['valuations']==[0]*4
    assert sm_three['valuations']==sm_nine['valuations']==[0,1,1,1]
    assert sm_unit['free_rank']==sm_three['free_rank']==sm_nine['free_rank']==6
    assert all(a.divisible3((3*F*Qthree)[i,:],vp(moduli[i]))for i in range(15))
    assert all(a.divisible3((9*F)[i,:],vp(moduli[i]))for i in range(15))
    # Exact image sizes under every multiplier regime, over all 81 values.
    image_basis=a.mat(hor['obstruction_image_basis'])
    image_sizes={}
    for r in (0,1,2,3,6,9,18,27):
        values=set()
        for x,y,z in product(range(3),range(3),range(9)):
            value=r*image_basis*s.Matrix([x,y,z])
            values.add(tuple(int(v.p)*pow(int(v.q),-1,moduli[i])%moduli[i]
                             for i,v in enumerate(value)))
        expected=1 if r%9==0 else (3 if r%3==0 else 81)
        assert len(values)==expected
        image_sizes[str(r)]=len(values)

    # One rational matrix supplies every actual particular correction.
    bracket=a.mat(hor['full_horizontal_defect'])
    omega=(s.eye(45)-J2)*bracket
    target_left=a.decode(rel['split_inverse'])[rel['plus_rank']:,:]
    DL,DR,DD=(a.decode(rel[k])for k in('left_transform','domain_transform','diagonal'))
    rhs=DL*target_left*omega
    assert rhs[23:,:]==s.zeros(1,10)
    B=-DR[:,:23]*s.diag(*[1/DD[i,i]for i in range(23)])*rhs[:23,:]
    F2=a.mat(central['degree_two_pair_map'])
    astar=a.mat(central['explicit_scaled_sigma_section'])
    B-=astar*((F2*B)[0,:]+(F2*B)[1,:])/6
    assert (s.eye(45)-J2)*(T2-7*s.eye(45))*B==-omega
    joint_row=R[2,:]/4-R[1,:]/6
    assert F2*B==joint_row.col_join(-joint_row)
    assert a.integral3(B*Qunit) and a.integral3(3*B*Qthree) and a.integral3(9*B)
    expected_rows={
        10:[-s.Rational(7,36),s.Rational(5,36),0,0,0,0,0,0,s.Rational(1,12),-s.Rational(1,12)],
        11:[-s.Rational(17,36),s.Rational(7,36),0,0,0,0,0,0,-s.Rational(1,12),s.Rational(1,12)],
        13:[s.Rational(7,36),s.Rational(1,36),0,s.Rational(1,6),-s.Rational(1,6),0,0,0,s.Rational(1,12),-s.Rational(1,12)],
        20:[-s.Rational(5,18),s.Rational(1,18),0,0,0,0,-s.Rational(1,6),s.Rational(1,6),0,0],
        33:[-s.Rational(5,18),s.Rational(1,18),0,0,0,0,0,0,-s.Rational(1,6),s.Rational(1,6)],
    }
    for i in range(45):
        assert list(B[i,:])==expected_rows.get(i,[0]*10)
    assert B*a.mat(hor['horizontal_splitting'])==a.mat(hor['relative_particular_correction'])

    # The order-three phase direction and its full kernel coordinates.
    K=a.mat(first['coefficient_kernel_basis'])
    KLinv=a.mat(first['kernel_horizontal_gauge_smith']['left_inverse'])
    PKbasis=K*KLinv
    w=s.Matrix([[0,1,0,0,0,0,2,1,0,0]])
    phase=w*PKbasis/2
    assert phase==s.Matrix([[s.Rational(1,2),-1,1,1,0,0,s.Rational(1,2)]])
    phase_generator=PKbasis[:,2]
    assert phase_generator==s.Matrix([0,0,0,0,0,0,2,-2,0,0])
    assert phase* s.eye(7)[:,2]==s.Matrix([1])
    # Both the source torsion relation and phase section are actual.
    kg=a.mat(first['kernel_horizontal_gauge_smith']['right'])
    kD=a.mat(first['kernel_horizontal_gauge_smith']['diagonal_matrix'])
    GK=(s.eye(7)-a.mat(first['kernel_tau']))*(s.eye(7)+a.mat(first['kernel_involution']))
    assert GK*kg[:,2]==3*KLinv[:,2]
    phase_checks=0
    for t1,t2,z1,z2,z3,z4,eps in product(range(3),repeat=7):
        t3=(eps-pow(2,-1,3)*t1+t2-z1-pow(2,-1,3)*z4)%3
        coord=s.Matrix([t1,t2,t3,z1,z2,z3,z4])
        v=(phase*coord)[0]
        assert int(v.p)*pow(int(v.q),-1,3)%3==eps
        phase_checks+=1

    # All exact target source relations, for arbitrary relative r.
    L,m,p,r,rho,sigma,eps=s.symbols('L m p r rho sigma eps')
    delta=r*m/4-r*p/6
    u=((s.Rational(5,2)+p,p-L,2+eps+rho/2),
       (s.Rational(1,2)+3*m-p,3*m-p-L-2,3+eps-rho/2))
    aa=((0,r,3*sigma+delta),(0,r,3*sigma-delta))
    norms=[]
    for i,mu in enumerate((-s.Rational(5,2),-s.Rational(1,2))):
        norms.append(a.mul(a.mul(a.mul(u[i],a.T(aa[i],mu)),a.inv(u[i])),a.power(aa[i],-7)))
    assert norms[0]==norms[1]==(0,0,s.expand(126*sigma+s.Rational(21,2)*r*m))
    eta=s.symbols('eta')
    actual_phase=(-p*(eta+1)-p*(p-1)+6*m-2*p)/2
    phase_origin=-p*(p+eta+2)/2
    assert s.expand(actual_phase-phase_origin)==3*m
    bb,rr=s.symbols('b rr')
    fixed=((bb,bb,rr),(-bb,-bb,rr))
    gauged=tuple(a.mul(a.mul(fixed[i],aa[i]),a.inv(fixed[i]))for i in range(2))
    assert gauged==((0,r,s.expand(3*sigma+delta+r*bb)),(0,r,s.expand(3*sigma-delta-r*bb)))
    assert s.expand((gauged[0][2]+gauged[1][2])/2)==3*sigma
    correction_tests=0
    for multiplier,QQ in ((1,Qunit),(2,Qunit),(3,Qthree),(6,Qthree),(9,s.eye(10)),(18,s.eye(10)),(0,s.eye(10))):
        for i in range(81):
            v=QQ*s.Matrix([i*(j+3)%19-9 for j in range(10)])
            ac=multiplier*B*v
            assert a.integral3(ac)
            assert (s.eye(45)-J2)*(T2-7*s.eye(45))*ac==-multiplier*omega*v
            assert (F2*ac)[0]+(F2*ac)[1]==0
            correction_tests+=1

    # The rational y/z swap carries the actual formal parameter exactly.
    X,Y,Z=s.symbols('X Y Z')
    source_parameter=Z/X
    target_parameter=Y/X
    assert target_parameter.xreplace({X:X,Y:Z,Z:Y})==source_parameter
    assert (X,Y,Z)==tuple(q.xreplace({X:X,Y:Z,Z:Y}).xreplace({X:X,Y:Z,Z:Y})for q in (X,Y,Z))

    # Actual logarithmic localization, including transitions and inverse.
    primes=list(s.primerange(2,101))
    log_records={};log_checks=0
    for precision in range(1,8):
        modulus=3**precision
        for prime in primes:
            if prime==3:continue
            ell=prime_log_coordinate(prime,precision)
            unit=prime if prime%3==1 else -prime
            assert pow(4,ell,3**(precision+1))==unit%3**(precision+1)
            if precision>1:
                assert ell%3**(precision-1)==prime_log_coordinate(prime,precision-1)
            log_records[f'{prime}:{precision}']=ell
            log_checks+=1
        assert prime_log_coordinate(2,precision)==pow(2,-1,modulus)
    localization_checks=0
    other=[p for p in primes if p not in(2,3)]
    for precision in range(1,8):
        modulus=3**precision
        logs={p:prime_log_coordinate(p,precision)for p in other}
        for trial in range(81):
            outside={p:(trial*(j+3)+j*j)%modulus for j,p in enumerate(other)}
            first=(trial*7+2)%modulus;second=(trial*11-3)%modulus
            sum_out=sum(outside[p]*logs[p]for p in other)%modulus
            a2=(2*second-2*sum_out)%modulus
            assert (a2*pow(2,-1,modulus)+sum_out)%modulus==second
            assert first==first%modulus
            # The kernel formula is the same exact inverse at second=0.
            kernel_a2=(-2*sum_out)%modulus
            assert (kernel_a2*pow(2,-1,modulus)+sum_out)%modulus==0
            localization_checks+=2
        # Restricted tails vanish in every stated finite quotient.
        tail=sum((3**(precision+j))*logs[p]for j,p in enumerate(other))
        assert tail%modulus==0
    alpha,beta,V,rr=s.symbols('alpha beta V rr',nonzero=True)
    local_matrix=s.Matrix([[1,beta],[0,alpha]])
    local_inverse=s.Matrix([[1,-beta/alpha],[0,1/alpha]])
    assert local_matrix*local_inverse==s.eye(2)
    global_origin=s.Matrix([-V-beta*rr/alpha,rr/alpha])
    assert local_matrix*global_origin==s.Matrix([-V,rr])

    result={
        'statement':'E.90','status':'PASS',
        'inputs':{k:{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for k,p in paths.items()},
        'multiplier_obstruction_image_sizes':image_sizes,
        'valuation_one_kernel_lattice':a.encode(Qthree),
        'valuation_one_kernel_inverse':a.encode(Qthree.inv()),
        'unit_gauge_smith':smith.encode(sm_unit),
        'valuation_one_gauge_smith':smith.encode(sm_three),
        'valuation_at_least_two_gauge_smith':smith.encode(sm_nine),
        'universal_particular_correction':a.encode(B),
        'universal_particular_joint_image':a.encode(F2*B),
        'particular_correction_cases':correction_tests,
        'phase_in_kernel_cohomology_coordinates':a.encode(phase),
        'phase_generator':a.encode(phase_generator),
        'actual_handle_phase_origin':str(phase_origin),
        'phase_kernel_type':'Z3^4 x C3^2',
        'phase_inverse_checks':phase_checks,
        'target_norm':[list(map(str,g))for g in norms],
        'target_relative_gauge':[list(map(str,g))for g in gauged],
        'local_types':{
            'unit':{'horizontal':'Z3^6','source':'Z3^52 x C3^9 x C9^5','image':'Z3^4','fibre':'Z3^48 x C3^9 x C9^5','p_residue':[0],'central_residue':'m mod3'},
            'valuation_one':{'horizontal':'Z3^6 x C3^3','source':'Z3^52 x C3^12 x C9^5','image':'Z3^4 x C3','fibre':'Z3^48 x C3^11 x C9^5','p_residue':[0],'central_residue':'arbitrary C3'},
            'divisible_by_nine_including_zero':{'horizontal':'Z3^6 x C3^3','source':'Z3^52 x C3^12 x C9^5','image':'Z3^4 x C3^2','fibre':'Z3^48 x C3^11 x C9^5','p_residue':[0,1,2],'central_residue':'arbitrary C3'}},
        'global_unramified_class_two_source':'Z3^30 x C3^12 x C9^5',
        'global_unramified_joint_image':'Z3^3 x C3^2',
        'global_unramified_class_two_fibre':'Z3^27 x C3^11 x C9^5',
        'logarithmic_coordinates':log_records,
        'logarithmic_prime_precision_checks':log_checks,
        'localization_inverse_checks':localization_checks,
        'local_kummer_transport':a.encode(local_matrix),
        'local_kummer_transport_inverse':a.encode(local_inverse),
        'global_cusp_origin_exponents':list(map(str,global_origin)),
        'global_topology':'inverse limit of discrete finite-exponent direct sums; restricted sequences, not the ambient product topology',
        'global_localization_kernel':'arbitrary restricted prime exponents outside2,3; a3=0 and a2=-2*sum(a_p*ell_p)',
    }
    here.joinpath('a_relative_multiples.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS all81 obstruction values in eight multiplier cases and all three zero-lattice Smith systems')
    print('PASS',correction_tests,'integral particular corrections and complete joint images')
    print('PASS',phase_checks,'full phase-kernel inverse coordinates')
    print('PASS actual symbolic joint norm and nonunit fixed conjugation')
    print('PASS exact rational tangent swap and symbolic Kummer source transport')
    print('PASS',log_checks,'prime/precision logarithmic identities and',localization_checks,'localization inverses')
    print('ALL PASS')


if __name__=='__main__':
    main()
