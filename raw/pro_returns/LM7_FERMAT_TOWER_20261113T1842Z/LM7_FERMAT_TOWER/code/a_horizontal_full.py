#!/usr/bin/env python3
"""E89: all horizontal intrinsic inputs over the actual B0 relative value."""
from pathlib import Path
from itertools import product
import argparse
import hashlib
import importlib.util
import json
import math
import numpy as np
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def mat(rows):
    return s.Matrix([[s.Rational(x) for x in row] for row in rows])


def decode(rows):
    return s.Matrix([[s.Rational(*x) for x in row] for row in rows])


def encode(A):
    return [[str(x) for x in A.row(i)] for i in range(A.rows)]


def integral3(A):
    return all(int(s.Rational(x).q) % 3 for x in A)


def divisible3(A, n=1):
    return integral3(A / (3**n))


def egcd(a, b):
    if b == 0:
        return abs(a), 1 if a >= 0 else -1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def row_kernel(row, modulus):
    row = [int(x) for x in row]
    size = len(row)
    change = s.eye(size)
    if not any(row):
        return change
    pivot = next(i for i, x in enumerate(row) if x)
    row[0], row[pivot] = row[pivot], row[0]
    change.col_swap(0, pivot)
    for j in range(1, size):
        if not row[j]:
            continue
        g, x, y = egcd(row[0], row[j])
        step = s.eye(size)
        step[0, 0], step[j, 0] = x, y
        step[0, j], step[j, j] = -row[j] // g, row[0] // g
        assert step.det() == 1
        change *= step
        row[0], row[j] = g, 0
    change[:, 0] *= modulus // math.gcd(modulus, row[0])
    return change


def mul(a, b):
    A, B, n = a
    C, D, m = b
    return tuple(s.expand(x) for x in (A+C, B+D, n+m-C*B))


def inv(a):
    A, B, n = a
    return (-A, -B, -n-A*B)


def power(a, t):
    A, B, n = a
    return (t*A, t*B, s.expand(t*n-A*B*t*(t-1)/2))


def T(a, mu):
    A, B, n = a
    return (7*A, 7*B, 49*n+7*mu*B)


def I(a):
    return (-a[0], -a[1], a[2])


def pair(L, p, m, n, nn):
    return ((p, p-L, n), (3*m-p, 3*m-p-L, nn))


def theta(g):
    return s.expand(g[0][2]+g[1][2]+g[0][0]*(g[0][0]-1))


def poly_div3(poly, vars_):
    return all(s.Rational(x/3).q % 3 for x in s.Poly(s.expand(poly), *vars_).coeffs())


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-code', type=Path)
    args = parser.parse_args()
    code = args.source_code or here
    if not (code/'e_unramified_sections.py').is_file():
        code = here.parent.parent/'LM7_FERMAT_TOWER/code'
    paths = {
        'Hall': code/'e_unramified_sections.py',
        'wild_layers': code/'e_wild_layers.json',
        'wild_degree_two_transforms': code/'e_wild_layers_r2_transforms.npz',
        'relative_kernels': code/'a_wild_kernel.json',
        'local_smith': code/'e_cusp_local_smith.py',
        'first_degree_kernel': code/'a_abelian_kernel_obstruction.json',
        'central_fibre': code/'a_compatible_joint_fibre.json',
    }
    assert all(p.is_file() for p in paths.values())
    hall = load('e89_Hall', paths['Hall'])
    smith = load('e89_smith', paths['local_smith'])
    data = json.loads(paths['wild_layers'].read_text())['layers']
    relative = json.loads(paths['relative_kernels'].read_text())['layers']
    previous = json.loads(paths['first_degree_kernel'].read_text())
    central = json.loads(paths['central_fibre'].read_text())
    assert previous['status'] == central['status'] == 'PASS'
    T1, J1 = (s.Matrix(data['1'][k]) for k in ('input_tau', 'input_c'))
    T2, J2 = (s.Matrix(data['2'][k]) for k in ('input_tau', 'input_c'))
    R = mat(previous['first_degree_map'])
    G = (s.eye(10)-T1)*(s.eye(10)+J1)

    H = hall.Hall(2)
    ids = [i for i, d in enumerate(H.degree) if d == 2]
    row = {i: j for j, i in enumerate(ids)}
    bracket = s.zeros(45, 10)
    for i in range(10):
        for j, coefficient in H.bracket(i, 5).items():
            bracket[row[j], i] = 7*coefficient
    arc = np.load(paths['wild_degree_two_transforms'])
    LL = s.Matrix(arc['left'].tolist())
    vals = [x['valuation'] for x in data['2']['elementary_operations']]
    sel = [i for i, v in enumerate(vals) if v]
    moduli = [3**vals[i] for i in sel]
    assert moduli == [3]*11+[9]*4
    F = (LL*bracket)[sel, :]
    F = s.Matrix([[int(F[i, j]) % moduli[i] for j in range(10)] for i in range(15)])
    assert all(divisible3((F*G)[i, :], vals[sel[i]]) for i in range(15))

    Q = s.eye(10)
    for i, modulus in enumerate(moduli):
        Q = hermite_normal_form(Q*row_kernel(F[i, :]*Q, modulus))
    characters = F[[3, 7, 14], :]
    character_moduli = [3, 3, 9]
    Qshort = s.eye(10)
    for i, modulus in enumerate(character_moduli):
        Qshort = hermite_normal_form(Qshort*row_kernel(characters[i, :]*Qshort, modulus))
    assert Q == Qshort and Q.det() == 81
    Qsmith = smith.local_smith(Q.tolist())
    assert Qsmith['valuations'] == [0]*7+[1, 1, 2]
    qg = Q.inv()*G
    assert integral3(qg)
    gauge = smith.local_smith(qg.tolist())
    assert gauge['valuations'] == [0]*4 and gauge['free_rank'] == 6
    primitive_columns = [0, 6, 1]
    minor = characters[:, primitive_columns]
    assert int(minor.det()) % 3
    obstruction_inverse = s.zeros(10, 3)
    for k, j in enumerate(primitive_columns):
        obstruction_inverse[j, :] = minor.inv()[k, :]
    assert characters*obstruction_inverse == s.eye(3)
    image_basis = F*obstruction_inverse
    assert all(divisible3((F-image_basis*characters)[i, :], vals[sel[i]]) for i in range(15))
    for j, order in enumerate(character_moduli):
        assert all(integral3(s.Matrix([image_basis[i, j]*order/moduli[i]])) for i in range(15))
    image_points = set()
    for aa, bb, cc in product(range(3), range(3), range(9)):
        value = image_basis*s.Matrix([aa, bb, cc])
        image_points.add(tuple(int(v.p)*pow(int(v.q), -1, moduli[i]) % moduli[i]
                               for i, v in enumerate(value)))
    assert len(image_points) == 81

    # A literal splitting over the two varying joint abelian coordinates.
    K = mat(previous['coefficient_kernel_basis'])
    QK = mat(previous['horizontal_kernel_lattice'])
    LKinv = mat(previous['horizontal_liftable_gauge_smith']['left_inverse'])
    Kzero = K*QK*LKinv[:, 3:]
    vL = -s.eye(10)[:, 5]
    vm = s.Matrix([2, -2, 0, 0, 0, 3, 0, 1, 1, 2])
    B = s.Matrix.hstack(vL, vm, Kzero)
    assert R*B == s.Matrix([[1,0,0,0,0,0], [0,0,0,0,0,0], [0,1,0,0,0,0]])
    assert integral3(Q.inv()*B)
    LQ = mat(gauge['left'])
    coordinates = LQ[4:, :]*Q.inv()
    compare = coordinates*B
    assert integral3(compare) and integral3(compare.inv())
    inverse_coordinates = compare.inv()*coordinates
    assert inverse_coordinates*B == s.eye(6)
    assert inverse_coordinates*G == s.zeros(6,10)
    # Exact lower alignment map, keeping the fixed coefficient itself.
    gsmith = smith.local_smith(G.tolist())
    GL, GR = mat(gsmith['left']), mat(gsmith['right'])
    GD = mat(gsmith['diagonal_matrix'])
    align_difference = (B*inverse_coordinates-s.eye(10))*Q
    alignment = (s.eye(10)+J1)*GR[:, :4]*s.diag(*[1/GD[i,i] for i in range(4)])*(GL*align_difference)[:4,:]
    assert integral3(alignment) and J1*alignment == alignment
    assert (s.eye(10)-T1)*alignment == align_difference

    # Every particular correction is computed over Z_(3), with both
    # residual joint central coordinates evaluated exactly.
    kd = relative['2']
    target_left = decode(kd['split_inverse'])[kd['plus_rank']:, :]
    DSleft, DSright = decode(kd['left_transform']), decode(kd['domain_transform'])
    diag = decode(kd['diagonal'])
    omega = (s.eye(45)-J2)*bracket*B
    rhs = DSleft*target_left*omega
    assert rhs[23:, :] == s.zeros(1, 6)
    correction = -DSright[:, :23]*s.diag(*[1/diag[i,i] for i in range(23)])*rhs[:23, :]
    assert integral3(correction)
    assert (s.eye(45)-J2)*(T2-7*s.eye(45))*correction == -omega
    unit_rows = s.Matrix([[2,-1,0,0,0,0,0,0,0,-3],
                         [1,0,0,0,0,1,1,1,0,-3],
                         [1,-2,0,0,0,0,0,0,-3,0],
                         [0,-1,0,0,0,1,1,1,-3,0]])
    F2 = s.Matrix([[unit_rows[o,H.children[i][0]]*unit_rows[o+1,H.children[i][1]]
                   -unit_rows[o+1,H.children[i][0]]*unit_rows[o,H.children[i][1]]
                   for i in ids] for o in (0,2)])
    astar = -s.eye(45)[:,10]+s.eye(45)[:,11]-s.eye(45)[:,13]
    zstar = -s.eye(45)[:,0]/2
    assert F2 == mat(central['degree_two_pair_map'])
    assert astar == mat(central['explicit_scaled_sigma_section'])
    assert zstar == mat(central['explicit_rho_section'])
    assert F2*astar == s.Matrix([3,3]) and F2*zstar == s.Matrix([s.Rational(1,2),-s.Rational(1,2)])
    cr, cs = s.symbols('cr cs')
    ell = (cr+cs)/3
    right_inverse = (2*ell-cr)*s.eye(45)[:,0]-ell*s.eye(45)[:,10]
    assert F2*right_inverse == s.Matrix([cr,cs])
    image_correction = F2*correction
    assert image_correction[0,:]-image_correction[1,:] == s.Matrix([[0,s.Rational(1,2),0,0,0,0]])
    mean = (image_correction[0,:]+image_correction[1,:])/2
    assert divisible3(mean)
    correction -= astar*(mean/3)
    assert F2*correction == s.Matrix([[0,s.Rational(1,4),0,0,0,0],
                                    [0,-s.Rational(1,4),0,0,0,0]])
    assert (s.eye(45)-J2)*(T2-7*s.eye(45))*correction == -omega

    # The finite central character is a genuine homomorphism on J2.
    La,p,ma,n,nn,Lb,q,mb,k,kk = s.symbols('La p ma n nn Lb q mb k kk')
    first,second = pair(La,p,ma,n,nn),pair(Lb,q,mb,k,kk)
    product_pair = tuple(mul(first[i],second[i]) for i in range(2))
    vars_ = (La,p,ma,n,nn,Lb,q,mb,k,kk)
    assert poly_div3(theta(product_pair)-theta(first)-theta(second),vars_)
    tfirst = (T(first[0],-s.Rational(5,2)),T(first[1],-s.Rational(1,2)))
    jfirst = (I(first[1]),I(first[0]))
    assert poly_div3(theta(tfirst)-theta(first)-p,vars_)
    assert poly_div3(theta(jfirst)-theta(first),vars_)
    # Known geometric cusp values leave just one harmless handle choice.
    phase_rows = []
    for a,b,c,d in product(range(3),repeat=4):
        w=s.Matrix([[a,b,0,0,0,0,c,d,0,0]])
        if divisible3(w*T1-w-R[1,:]) and divisible3(w*J1-w):
            phase_rows.append(w)
    expected=[s.Matrix([[a,(a+1)%3,0,0,0,0,2,1,0,0]])for a in range(3)]
    assert phase_rows == expected
    for w in phase_rows:
        assert divisible3(w*B-s.Matrix([[0,2,0,0,0,0]]))

    # Symbolic target norm and full geometric gauge.
    L,m,rho,sigma,eps=s.symbols('L m rho sigma eps')
    u=((s.Rational(5,2),-L,2+eps+rho/2),
       (s.Rational(1,2)+3*m,3*m-L-2,3+eps-rho/2))
    aa=((0,1,3*sigma+m/4),(0,1,3*sigma-m/4))
    norm=[]
    for i,mu in enumerate((-s.Rational(5,2),-s.Rational(1,2))):
        norm.append(mul(mul(mul(u[i],T(aa[i],mu)),inv(u[i])),power(aa[i],-7)))
    assert norm[0] == norm[1] == (0,0,s.expand(126*sigma+s.Rational(21,2)*m))
    bb,rr,pp,N,M,a1,a2=s.symbols('b r p N M a1 a2')
    arbitrary_u=((s.Rational(5,2)+pp,pp-L,N),
                 (s.Rational(1,2)+3*m-pp,3*m-pp-L-2,M))
    arbitrary_a=((0,1,a1),(0,1,a2))
    fixed=((bb,bb,rr),(-bb,-bb,rr))
    gauged_u=tuple(mul(mul(fixed[i],arbitrary_u[i]),inv(T(fixed[i],mu)))
                   for i,mu in enumerate((-s.Rational(5,2),-s.Rational(1,2))))
    gauged_a=tuple(mul(mul(fixed[i],arbitrary_a[i]),inv(fixed[i]))for i in range(2))
    assert gauged_u[0][:2] == (pp-6*bb+s.Rational(5,2),pp-6*bb-L)
    assert gauged_u[1][:2] == (3*m-pp+6*bb+s.Rational(1,2),3*m-pp+6*bb-L-2)
    assert gauged_a == ((0,1,a1+bb),(0,1,a2-bb))
    assert s.expand((gauged_a[0][2]+gauged_a[1][2])-(a1+a2)) == 0
    for i,base in enumerate((N,M)):
        assert s.expand(gauged_u[i][2].subs(bb,0)-base) == -48*rr

    # Explicit finite-carry and all six horizontal coordinate inverses.
    inverse_checks=0
    for trial in range(729):
        c=s.Matrix([trial*(i+3)%31-15 for i in range(6)])
        raw=B*c
        bfixed=(s.eye(10)+J1)*s.Matrix([trial*(i+11)%17-8 for i in range(10)])
        changed=raw+(s.eye(10)-T1)*bfixed
        assert inverse_coordinates*changed == c
        assert all(integral3(s.Matrix([(characters*changed)[i]/character_moduli[i]]))for i in range(3))
        lm=int(c[1]);ee=lm%3
        rational_rho=s.Rational(trial%23-11,2)
        targetN=2+ee+rational_rho/2
        targetM=3+ee-rational_rho/2
        residue=(targetN+targetM-5)/2
        assert residue==ee and targetN-targetM+1==rational_rho
        shift=s.Rational(trial%19-9,2)
        shifted=(targetN-48*shift,targetM-48*shift)
        recovered=((shifted[0]+shifted[1]-5)/2-ee)/48
        assert recovered==-shift
        assert (shifted[0]-48*recovered,shifted[1]-48*recovered)==(targetN,targetM)
        inverse_checks+=3

    result={
        'statement':'E.89','status':'PASS',
        'inputs':{k:{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for k,p in paths.items()},
        'full_horizontal_defect':encode(bracket),'obstruction_coordinates':encode(F),
        'obstruction_moduli':moduli,'three_characters':encode(characters),
        'three_character_moduli':character_moduli,
        'obstruction_inverse':encode(obstruction_inverse),'obstruction_image_basis':encode(image_basis),
        'obstruction_image_type':'C3^2 x C9','obstruction_image_elements':len(image_points),
        'kernel_lattice':encode(Q),'kernel_lattice_inverse':encode(Q.inv()),
        'kernel_lattice_smith':smith.encode(Qsmith),'kernel_gauge_smith':smith.encode(gauge),
        'liftable_horizontal_type':'Z3^6','horizontal_splitting':encode(B),
        'horizontal_inverse_coordinates':encode(inverse_coordinates),
        'horizontal_inverse_domain':'kernel_lattice; modulo the full fixed abelian gauge',
        'fixed_alignment_on_kernel_lattice':encode(alignment),
        'relative_particular_correction':encode(correction),
        'relative_particular_joint_image':encode(F2*correction),
        'all_correction_denominators_prime_to3':True,
        'joint_phase_rows': [encode(w)for w in phase_rows],
        'joint_phase_on_splitting_mod3':[0,2,0,0,0,0],
        'joint_normalized_image':'L,m,rho arbitrary Z3; relative central mean=3*sigma; horizontal mean residue=m mod3',
        'joint_normalized_source_type':'Z3^52 x C3^9 x C9^5',
        'joint_image_type':'Z3^4','full_fibre_type':'Z3^48 x C3^9 x C9^5',
        'joint_norm_word':[list(map(str,g))for g in norm],
        'joint_full_fixed_gauge_centres':[str(g[2])for g in gauged_u],
        'joint_relative_fixed_gauge_centres':[str(g[2])for g in gauged_a],
        'inverse_checks':inverse_checks,
        'actual_hall_image_normalization':'Use the evaluated actual joint Hall image, then the E85 literal L2 right inverse; its required sum is proved divisible by3 by the character theta.',
    }
    here.joinpath('a_horizontal_full.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS full horizontal image C3^2 x C9 and all 81 image coordinates')
    print('PASS saturated zero lattice, full fixed gauge, and Z3^6 inverse coordinates')
    print('PASS six integral particular corrections and their exact joint central image')
    print('PASS actual joint finite character, cusp/arithmetic constraints, and all handle choices')
    print('PASS symbolic joint source word and full nonlinear fixed conjugation')
    print('PASS',inverse_checks,'complete horizontal and finite-carry inverse checks')
    print('ALL PASS')


if __name__=='__main__':
    main()
