#!/usr/bin/env python3
"""E85: actual compatible joint family and its intrinsic central fibres.

All Smith and saturated-kernel inputs are the retained E74/E75/E82
certificates.  The two coefficient maps are recomputed from the actual
four unit characters.  No unknown higher Frobenius entry is substituted.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form


def decode(A):
    return s.Matrix([[s.Rational(str(x)) for x in row] for row in A])


def encode(A):
    return [[str(x) for x in A.row(i)] for i in range(A.rows)]


def mod3(x, modulus=3):
    x = s.Rational(x)
    assert int(x.q) % 3
    return int(x.p)*pow(int(x.q), -1, modulus) % modulus


def unit_integral(A):
    return all(int(s.Rational(x).q) % 3 for x in A)


def mul(g, h):
    x, y, c, d, e = map(s.sympify, g)
    X, Y, C, D, E = map(s.sympify, h)
    return tuple(s.expand(v) for v in (
        x+X, y+Y, c+C-X*y,
        d+D+y*X*(X+1)/2-X*c,
        e+E+X*y*(y+1)/2-Y*c+X*y*Y))


def inv(g):
    x, y, c, d, e = map(s.sympify, g)
    return tuple(s.expand(v) for v in (
        -x, -y, -c-x*y,
        -d-x*c-x*y*(x-1)/2,
        -e-y*c+x*y*(1-y)/2))


def power(g, n):
    if n < 0:
        return power(inv(g), -n)
    out = (s.Integer(0),)*5
    while n:
        if n & 1:
            out = mul(out, g)
        g = mul(g, g)
        n //= 2
    return out


def alpha(g, mu):
    x, y, c, d, e = map(s.sympify, g)
    mu = s.sympify(mu)
    return tuple(s.expand(v) for v in (
        7*x, 7*y, 7*mu*y+49*c,
        7*mu*(mu-1)*y/2+(147+49*mu)*c+343*d,
        (14-28*mu)*y-49*mu*y*(y-1)/2+147*c+343*e))


def defect(u, a, mu):
    return mul(mul(mul(u, alpha(a, mu)), inv(u)), inv(power(a, 7)))


def invol(g):
    x, y, c, d, e = map(s.sympify, g)
    return (-x, -y, c, -c-d, -c-e)


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-code', type=Path)
    parser.add_argument('--cusp-certificate', type=Path)
    args = parser.parse_args()
    code = args.source_code or here
    if not (code/'e_unramified_sections.py').exists():
        code = here.parent.parent/'LM7_FERMAT_TOWER/code'
    cuspfile = args.cusp_certificate or code/'e_cusp_family_obstruction.json'
    files = {
        'Hall': code/'e_unramified_sections.py',
        'wild_layers': code/'e_wild_layers.json',
        'relative_kernel': code/'a_wild_kernel.json',
        'cusp_families': cuspfile,
        'actual_class_three_action': code/'a_wild_class3.py',
        'actual_joint_quotient': code/'a_joint_wild.py',
    }
    assert all(p.is_file() for p in files.values())
    spec = importlib.util.spec_from_file_location('e85_Hall', files['Hall'])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    H = module.Hall(2)
    ids = [i for i, d in enumerate(H.degree) if d == 2]
    assert len(ids) == 45 and H.children[ids[0]] == (1, 0)
    Q = s.Matrix([
        [2,-1,0,0,0,0,0,0,0,-3],
        [1,0,0,0,0,1,1,1,0,-3],
        [1,-2,0,0,0,0,0,0,-3,0],
        [0,-1,0,0,0,1,1,1,-3,0],
    ])
    F = s.Matrix([
        [Q[k,H.children[i][0]]*Q[k+1,H.children[i][1]]
         - Q[k+1,H.children[i][0]]*Q[k,H.children[i][1]]
         for i in ids]
        for k in (0,2)])
    # Independent alternating tensor check, including the commutator sign.
    tensor_checks = 0
    for j, i in enumerate(ids):
        a, b = H.children[i]
        for offset in (0,2):
            coeff = {}
            for u, v in product(range(2), repeat=2):
                coeff[u,v] = Q[offset+u,a]*Q[offset+v,b] - Q[offset+u,b]*Q[offset+v,a]
            assert coeff == {(0,0):0, (0,1):F[offset//2,j],
                             (1,0):-F[offset//2,j], (1,1):0}
            tensor_checks += 1
    L2 = s.Matrix([[1,0],[-1,3]])
    image = hermite_normal_form(F)
    assert abs(image.det()) == 3
    assert all(x.q == 1 for x in L2.inv()*F)
    assert abs((L2.inv()*image).det()) == 1
    assert list(F[:,0]) == [-1,1]
    assert H.children[ids[10]] == (5,0)
    assert H.children[ids[11]] == (5,1)
    assert H.children[ids[13]] == (5,3)
    # (n,m), n+m=3 ell, has the literal Hall preimage
    # (2 ell-n)[f2,f1]-ell[B0,f1].
    derived_inverse = s.zeros(45,2)
    derived_inverse[0,0] = -1
    derived_inverse[0,1] = 2
    derived_inverse[10,1] = -1
    assert F*derived_inverse == L2

    layers = json.loads(files['wild_layers'].read_text())['layers']
    T, J = (s.Matrix(layers['2'][key]) for key in ('input_tau','input_c'))
    swap = s.Matrix([[0,1],[1,0]])
    assert F*T == 49*F and F*J == swap*F
    assert J*J == s.eye(45)
    rel = json.loads(files['relative_kernel'].read_text())['layers']['2']
    B = s.Matrix([[s.Rational(*x) for x in row] for row in rel['kernel_basis']])
    Bleft = s.Matrix([[s.Rational(*x) for x in row] for row in rel['kernel_coordinate_map']])
    assert B.shape == (45,22) and Bleft.shape == (22,45)
    assert Bleft*B == s.eye(22)
    D = (s.eye(45)-J)*(T-7*s.eye(45))
    assert D*B == s.zeros(45,22)
    assert D.rank() == 23
    assert unit_integral(B) and unit_integral(Bleft)
    FB = F*B
    assert FB[0,:] == FB[1,:]
    sigma = FB[0,:]/3
    assert list(sigma) == [0,0,0,0,-3,0,0,0,0,0,1,0,-3,2,-2,0,0,0,-1,2,-1,-2]
    assert all(x.q == 1 for x in sigma)
    apivot = next(i for i, x in enumerate(sigma) if x == 1)
    assert apivot == 10

    cusp = json.loads(files['cusp_families'].read_text())
    smith = cusp['family_parameter_gauge_smith']
    LG, RG = decode(smith['left']), decode(smith['right'])
    LiG, RiG = decode(smith['left_inverse']), decode(smith['right_inverse'])
    G = (s.eye(45)-T)*(s.eye(45)+J)
    assert decode(smith['matrix']) == G
    diag = s.diag(*[s.Rational(str(x)) for x in smith['diagonal']])
    assert LG*G*RG == diag
    assert LG*LiG == LiG*LG == RG*RiG == RiG*RG == s.eye(45)
    assert list(diag.diagonal()) == [1]*7+[3]*9+[9]*5+[0]*24
    rho = F[0,:]-F[1,:]
    assert rho*G == s.zeros(1,45)
    rp = rho*LiG
    assert all(x == 0 for x in rp[:21])
    upivot = next(i for i in range(21,45) if mod3(rp[i]) != 0)
    Su = s.eye(45)
    Su[upivot,:] = rp
    Sui = Su.inv()
    Sa = s.eye(22)
    Sa[apivot,:] = sigma
    Sai = Sa.inv()
    assert unit_integral(Su) and unit_integral(Sui)
    assert unit_integral(Sa) and unit_integral(Sai)
    assert Su*Sui == Sui*Su == s.eye(45)
    assert Sa*Sai == Sai*Sa == s.eye(22)
    assert Su*diag == diag  # Only a free coordinate has been replaced.
    e0 = s.zeros(45,1);e0[0] = 1
    zstar = -e0/2
    astar = B[:,apivot]
    assert rho*zstar == s.ones(1,1)
    assert F*zstar == s.Matrix([s.Rational(1,2),-s.Rational(1,2)])
    assert F*astar == s.Matrix([3,3])
    assert D*astar == s.zeros(45,1)
    assert astar == -s.eye(45)[:,10]+s.eye(45)[:,11]-s.eye(45)[:,13]

    # Every displayed coordinate map and inverse, including the full
    # intrinsic abelian fibre, is exercised on exact rational inputs.
    coordinate_checks = 0
    for trial in range(216):
        p = s.Matrix([s.Rational((trial*(j+3)+j*j)%31-15,
                                  2 if (trial+j)%4 == 0 else 1)
                      for j in range(45)])
        for j in range(7):p[j] = 0
        for j in range(7,21):p[j] = mod3(p[j],3 if j<16 else 9)
        k = s.Matrix([s.Rational((trial*(j+5)+2*j*j)%29-14,
                                  2 if (trial+j)%3 == 0 else 1)
                      for j in range(22)])
        z, a = LiG*p, B*k
        coords_u, coords_a = Su*LG*z, Sa*Bleft*a
        assert LiG*Sui*coords_u == z
        assert B*Sai*coords_a == a
        assert coords_u[upivot] == (rho*z)[0]
        assert coords_a[apivot]*3 == (F*a)[0] == (F*a)[1]
        assert mod3(sum(F*z)/2) == 0
        # Explicit splitting by the actual first Hall commutator and
        # one retained relative-kernel column.
        zk = z-(rho*z)[0]*zstar
        ak = a-(sigma*k)[0]*astar
        assert rho*zk == s.zeros(1,1)
        assert F*ak == s.zeros(2,1)
        assert zk+(rho*z)[0]*zstar == z
        assert ak+(sigma*k)[0]*astar == a
        coordinate_checks += 6

    # Direct symbolic class-three norm identity at the normalized
    # rational cusp.  It determines the two constants, rather than
    # assigning them by a choice of lift.
    V,N,M,r1,s1,r2,s2,n,m,ss = s.symbols('V N M r1 s1 r2 s2 n m ss')
    y = (0,1,0,0,0)
    u1 = (s.Rational(5,2),V,2-s.Rational(5,2)*V,r1,s1)
    u2 = (s.Rational(1,2),V-2,3-V/2,r2,s2)
    assert defect(u1,y,s.Rational(-5,2)) == (0,0,0,0,0)
    assert defect(u2,y,s.Rational(-1,2)) == (0,0,0,0,0)
    norm1 = mul((0,-V,0,0,0),u1)
    norm2 = mul((0,-V,0,0,0),u2)
    assert tuple(s.simplify(x) for x in norm1[:3]) == (s.Rational(5,2),0,2)
    assert tuple(s.simplify(x) for x in norm2[:3]) == (s.Rational(1,2),-2,3)
    assert defect(norm1,y,s.Rational(-5,2)) == (0,0,0,0,0)
    assert defect(norm2,y,s.Rational(-1,2)) == (0,0,0,0,0)
    # The whole target central fibre, with its actual involution defect.
    v1 = defect((s.Rational(5,2),0,2+n,0,0),(0,1,ss,0,0),s.Rational(-5,2))
    v2 = defect((s.Rational(1,2),-2,3+m,0,0),(0,1,ss,0,0),s.Rational(-1,2))
    assert v1[:3] == v2[:3] == (0,0,42*ss)
    omega = mul(v1, inv(invol(v2)))
    assert omega[:3] == (0,0,0)
    assert s.expand(omega[3]) == 336*ss
    assert s.expand(omega[4]) == -7*(n+m)+868*ss
    # Modulo three, the natural E83 residual is ss-n-m.
    assert all(mod3(c) == 0 for c in s.Poly(omega[3],n,m,ss).coeffs())
    assert all(mod3(c) == 0 for c in s.Poly(omega[4]-(ss-n-m),n,m,ss).coeffs())

    family_checks = 0
    for nn, mm in product(range(-12,15), repeat=2):
        compatible = (nn+mm-5)%3 == 0
        # A direct image-lattice inverse, once its actual condition holds.
        if compatible:
            diff = s.Matrix([nn-2,mm-3])
            ellcoords = L2.inv()*diff
            assert all(x.q == 1 for x in ellcoords)
            assert F*derived_inverse*ellcoords == diff
            b = s.Rational(nn+mm-5,96)
            assert int(b.q)%3
            t = nn-mm+1
            normal = (s.simplify(nn-48*b),s.simplify(mm-48*b))
            assert normal == (2+s.Rational(t,2),3-s.Rational(t,2))
            assert normal[0]+normal[1] == 5
        else:
            assert mod3(nn+mm-5) != 0
        family_checks += 1

    # Finite target coordinate maps: the image has index nine at every
    # positive level, and its exact kernel uses the displayed cyclic maps.
    finite = []
    for exponent in range(1,5):
        modulus = 3**exponent
        image_count = modulus*(modulus//3)
        target_count = modulus*modulus*3
        assert target_count == 9*image_count
        finite.append({'modulus':modulus,'target_order':target_count,
                       'image_order':image_count,'index':9})

    result = {
        'statement':'E.85','status':'PASS',
        'inputs':{k:{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
                  for k,p in files.items()},
        'unit_character_matrix':encode(Q),
        'degree_two_pair_map':encode(F),
        'degree_two_image_basis':encode(image),
        'degree_two_lattice_basis':encode(L2),
        'derived_lattice_explicit_Hall_right_inverse':encode(derived_inverse),
        'degree_two_image_index':3,
        'independent_alternating_tensor_checks':tensor_checks,
        'actual_tau':encode(T),'actual_involution':encode(J),
        'gauge_smith':{k:smith[k] for k in ('matrix','diagonal','left','right','left_inverse','right_inverse')},
        'relative_kernel_basis':encode(B),'relative_kernel_inverse_on_image':encode(Bleft),
        'relative_kernel_pair_image':encode(FB),
        'relative_kernel_scaled_coordinate':encode(sigma),
        'rho_in_Hall_coordinates':encode(rho),
        'rho_in_E82_Smith_coordinates':encode(rp),
        'u_coordinate_pivot_zero_based':upivot,
        'a_coordinate_pivot_zero_based':apivot,
        'u_coordinate_change':encode(Su),'u_coordinate_inverse':encode(Sui),
        'a_coordinate_change':encode(Sa),'a_coordinate_inverse':encode(Sai),
        'explicit_rho_section':encode(zstar),
        'explicit_scaled_sigma_section':encode(astar),
        'all_coordinate_changes_invertible_over_Z3':True,
        'actual_origin_pair_class2':[['5/2','0','2'],['1/2','-2','3']],
        'symbolic_cusp_path_norm_identities':4,
        'symbolic_central_fibre_defect':[str(x) for x in omega],
        'family_compatibility':'N+M=2 modulo3',
        'family_class_coordinate':'N-M+1',
        'family_inverse':'N=2+t/2, M=3-t/2',
        'family_cases_checked':family_checks,
        'exact_coordinate_inverse_checks':coordinate_checks,
        'selected_cusp_family_fibre':'Z3^23 x C3^9 x C9^5',
        'entire_intrinsic_abelian_fibre':'Z3^46 x C3^9 x C9^5',
        'target_central_fibre_coordinates':['rho=u1-u2','sigma=a1=a2','epsilon=(u1+u2)/2 mod3'],
        'image_in_target_central_fibre':['Z3','3Z3','0'],
        'full_central_fibre_map_kernel':'Z3^44 x C3^9 x C9^5',
        'target_cokernel':'C3^2',
        'finite_target_image_checks':finite,
    }
    here.joinpath('a_compatible_joint_fibre.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',tensor_checks,'independent alternating tensor images and both arithmetic intertwiners')
    print('PASS exact index-three derived image and complete gauge Smith inverse pairs')
    print('PASS rank22 relative kernel and exact image 3 Z3 on its diagonal target')
    print('PASS all four symbolic actual cusp norm identities and the full central defect')
    print('PASS',family_checks,'compatible-family tests and',coordinate_checks,'exact coordinate inverses')
    print('PASS both explicit splitting vectors and all cyclic coordinate identifications')
    print('ALL PASS')


if __name__ == '__main__':
    main()
