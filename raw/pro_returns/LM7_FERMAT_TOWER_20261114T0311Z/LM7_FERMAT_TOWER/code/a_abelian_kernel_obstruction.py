#!/usr/bin/env python3
"""E87: first-degree kernel, complete horizontal obstruction, and filled elliptic target."""
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


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def decode(A):
    return s.Matrix([[s.Rational(*x) for x in row] for row in A])


def encode(A):
    return [[str(x) for x in A.row(i)] for i in range(A.rows)]


def egcd(a,b):
    if b == 0:
        return abs(a), 1 if a >= 0 else -1, 0
    g,x,y = egcd(b,a%b)
    return g,y,x-(a//b)*y


def row_kernel(a,m):
    a = [int(x) for x in a]
    n = len(a);S = s.eye(n)
    if not any(a):
        return S
    p = next(i for i,x in enumerate(a) if x)
    a[0],a[p] = a[p],a[0];S.col_swap(0,p)
    for k in range(1,n):
        if not a[k]:
            continue
        g,x,y = egcd(a[0],a[k]);M = s.eye(n)
        M[0,0],M[k,0] = x,y
        M[0,k],M[k,k] = -a[k]//g,a[0]//g
        assert M.det() == 1
        S = S*M;a[0],a[k] = g,0
    S[:,0] *= m//math.gcd(m,a[0])
    return S


def integral3(A):
    return all(int(s.Rational(x).q)%3 for x in A)


def emul(g,h):
    x,y,c = g;X,Y,C = h
    return tuple(s.expand(v) for v in (x+X,y+Y,c+C-(x*Y-y*X)/2))


def einv(g):
    return tuple(-x for x in g)


def epower(g,n):
    return tuple(n*x for x in g)


def eT(g):
    x,y,c = g
    return (x-3*y,3*x-2*y,7*c)


def eJ(g):
    x,y,c = g
    return (x-y,-y,-c)


def main():
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-code', type=Path)
    ap.add_argument('--smith-helper', type=Path)
    args = ap.parse_args()
    code = args.source_code or here
    if not (code/'e_unramified_sections.py').is_file():
        code = here.parent.parent/'LM7_FERMAT_TOWER/code'
    helper = args.smith_helper or code/'e_cusp_local_smith.py'
    if not helper.is_file():
        helper = here.parent.parent/'research_e82/code/e_cusp_local_smith.py'
    files = {'Hall':code/'e_unramified_sections.py',
             'wild_layers':code/'e_wild_layers.json',
             'wild_degree_two_transforms':code/'e_wild_layers_r2_transforms.npz',
             'relative_kernels':code/'a_wild_kernel.json',
             'local_smith':helper}
    assert all(p.is_file() for p in files.values())
    hall = load_module('e87_Hall',files['Hall'])
    smith = load_module('e87_smith',helper)
    data = json.loads(files['wild_layers'].read_text())['layers']
    kernels = json.loads(files['relative_kernels'].read_text())['layers']
    T,J = (s.Matrix(data['1'][k]) for k in ('input_tau','input_c'))
    R = s.Matrix([[1,-1,0,0,0,-1,-1,-1,0,0],
                  [2,-1,0,0,0,0,0,0,0,-3],
                  [1,-1,0,0,0,0,0,0,-1,-1]])
    QJ = s.Matrix([[-1,0,0],[0,1,-3],[0,0,-1]])
    assert R*T == 7*R and R*J == QJ*R
    assert abs(R[:,[1,5,8]].det()) == 1
    G1 = (s.eye(10)-T)*(s.eye(10)+J)
    S1 = smith.local_smith(G1.tolist())
    assert S1['valuations'] == [0,1,1,1]
    L1,Li1 = s.Matrix(S1['left']),s.Matrix(S1['left_inverse'])
    Umap = R*Li1
    assert Umap == s.Matrix([[0,0,0,0,0,-1,1,-1,-1,0],
                            [-6,-6,6,6,0,0,2,0,-1,-3],
                            [0,0,0,0,0,0,1,0,-1,-1]])
    B1 = decode(kernels['1']['kernel_basis'])
    Amap = R*B1
    assert Amap == s.Matrix([[2,0,0,0,-1,-1,-1,0,0],
                            [5,0,0,0,0,0,0,0,-3],
                            [2,0,0,0,0,0,0,-1,-1]])
    first_inverse_checks = 0
    for trial in range(243):
        Lu,mu,eps = trial%11-5,(3*trial)%13-6,trial%3
        q1,q3,q4,k = (trial*(i+3)%17-8 for i in range(4))
        q5 = 2*q3-eps-3*k
        q6 = -q3+eps+3*k-mu
        q2 = -q3-q4+eps+3*k-Lu
        p = s.Matrix([0,trial%3,(trial//3)%3,(trial//9)%3,q1,q2,q3,q4,q5,q6])
        im = Umap*p
        assert im[0] == Lu and im[2] == mu and int(im[1])%3 == eps
        assert (2*q3-q5-eps)//3 == k
        La,pa,ma = (trial*(i+7)%19-9 for i in range(3))
        aa0,aa1,aa2,bb1,bb2,cc2 = (trial*(i+11)%23-11 for i in range(6))
        tt = s.Rational(pa+3*cc2,5)
        cc1 = 2*tt-cc2-ma
        bb0 = 2*tt-bb1-bb2-La
        acoord = s.Matrix([tt,aa0,aa1,aa2,bb0,bb1,bb2,cc1,cc2])
        assert Amap*acoord == s.Matrix([La,pa,ma])
        first_inverse_checks += 3

    # Literal rank-seven coefficient kernel, with its specified inverse.
    K = s.zeros(10,7)
    K[:,0] = s.Matrix([1,2,0,0,0,-1,0,0,-1,0])
    K[:,1] = s.Matrix([0,-3,0,0,0,3,0,0,2,1])
    K[2,2] = K[3,3] = K[4,4] = 1
    K[6,5] = K[7,6] = 1;K[5,5] = K[5,6] = -1
    Kl = s.zeros(7,10)
    for i,jj in enumerate((0,9,2,3,4,6,7)):Kl[i,jj] = 1
    assert Kl*K == s.eye(7) and R*K == s.zeros(3,7)
    assert K.rank() == 7
    TK,JK = Kl*T*K,Kl*J*K
    assert K*TK == T*K and K*JK == J*K
    GK = (s.eye(7)-TK)*(s.eye(7)+JK)
    SK = smith.local_smith(GK.tolist())
    assert SK['valuations'] == [1,1,1] and SK['free_rank'] == 4
    AK = s.zeros(7,6);AK[0,0],AK[1,0] = 9,5
    for i in range(1,6):AK[i+1,i] = 1
    AKl = s.zeros(6,7);AKl[0,1] = s.Rational(1,5)
    for i in range(1,6):AKl[i,i+1] = 1
    DK = (s.eye(7)-JK)*(TK-7*s.eye(7))
    assert DK*AK == s.zeros(7,6) and AKl*AK == s.eye(6)
    assert DK.rank() == 1 and integral3(AKl)

    # Every horizontal change has the actual central error 7[v,e_B0].
    H = hall.Hall(2)
    ids = [i for i,d in enumerate(H.degree) if d == 2]
    hrow = {i:j for j,i in enumerate(ids)}
    Br = s.zeros(45,10)
    for i in range(10):
        for j,c in H.bracket(i,5).items():Br[hrow[j],i] = 7*c
    Vdef = Br*K
    assert Vdef[0,:] == s.zeros(1,7)
    arc = np.load(files['wild_degree_two_transforms'])
    L2 = s.Matrix(arc['left'].tolist())
    vals = [x['valuation'] for x in data['2']['elementary_operations']]
    selected = [i for i,v in enumerate(vals) if v]
    mods = [3**vals[i] for i in selected]
    assert mods == [3]*11+[9]*4
    F = (L2*Vdef)[selected,:]
    F = s.Matrix([[int(F[i,j])%mods[i] for j in range(7)] for i in range(15)])
    assert all(int((F*GK)[i,j])%mods[i] == 0 for i in range(15) for j in range(7))
    Q = s.eye(7)
    for i,m in enumerate(mods):Q = hermite_normal_form(Q*row_kernel(F[i,:]*Q,m))
    assert Q == s.Matrix([[3,0,0,0,0,2,1],[0,3,0,0,0,0,0],
                          [0,0,1,0,0,0,0],[0,0,0,3,1,1,2],
                          [0,0,0,0,1,0,0],[0,0,0,0,0,1,0],
                          [0,0,0,0,0,0,1]])
    char = s.Matrix([[1,0,0,0,0,-2,-1],[0,1,0,0,0,0,0],
                     [0,0,0,1,-1,-1,-2]])
    generators = F[:,[0,1,3]]
    assert all(int((F-generators*char)[i,j])%mods[i] == 0
               for i in range(15) for j in range(7))
    scaled = s.Matrix([[int(generators[i,j])//(mods[i]//3) for j in range(3)]
                       for i in range(15)])
    minor = scaled[[3,7,14],:]
    assert int(minor.det())%3 and minor.inv_mod(3)*minor%3 == s.eye(3)
    QG = Q.inv()*GK
    assert all(x.q == 1 for x in QG)
    SQ = smith.local_smith(QG.tolist())
    assert SQ['valuations'] == [0,0,0] and SQ['free_rank'] == 4
    # Its complete finite obstruction image, including the order-nine
    # ambient coordinates that receive elements of order three.
    images = set()
    for x in product(range(3),repeat=3):
        images.add(tuple(int((generators*s.Matrix(x))[i])%mods[i] for i in range(15)))
    assert len(images) == 27
    for x in product(range(3),repeat=7):
        xx = s.Matrix(x)
        assert all(int(v)%3 == 0 for v in char*xx) == all(
            int((F*xx)[i])%mods[i] == 0 for i in range(15))

    # Exact particular corrections, from the actual rational Smith maps
    # of E75; no finite-level vanishing is substituted for integrality.
    kd = kernels['2']
    T2,J2 = (s.Matrix(data['2'][k]) for k in ('input_tau','input_c'))
    target_left = decode(kd['split_inverse'])[kd['plus_rank']:,:]
    TL = decode(kd['left_transform']);DR = decode(kd['domain_transform'])
    DD = decode(kd['diagonal']);mat = decode(kd['matrix'])
    assert TL*mat*DR == DD
    omega = (s.eye(45)-J2)*Vdef*Q
    sy = TL*target_left*omega
    rank = kd['rank'];assert rank == 23
    assert sy[rank:,:] == s.zeros(1,7)
    invdiag = s.diag(*[1/DD[i,i] for i in range(rank)])
    particular = -DR[:,:rank]*invdiag*sy[:rank,:]
    assert integral3(particular)
    assert (s.eye(45)-J2)*(T2-7*s.eye(45))*particular == -omega
    unitQ = s.Matrix([[2,-1,0,0,0,0,0,0,0,-3],
                      [1,0,0,0,0,1,1,1,0,-3],
                      [1,-2,0,0,0,0,0,0,-3,0],
                      [0,-1,0,0,0,1,1,1,-3,0]])
    F2 = s.Matrix([[unitQ[o,H.children[i][0]]*unitQ[o+1,H.children[i][1]]
                    -unitQ[o+1,H.children[i][0]]*unitQ[o,H.children[i][1]]
                    for i in ids] for o in (0,2)])
    fp = F2*particular
    assert fp[0,:] == fp[1,:] and integral3(fp/3)
    astar = -s.eye(45)[:,10]+s.eye(45)[:,11]-s.eye(45)[:,13]
    joint_zero = particular-astar*(fp[0,:]/3)
    assert F2*joint_zero == s.zeros(2,7)
    assert (s.eye(45)-J2)*(T2-7*s.eye(45))*joint_zero == -omega
    assert integral3(joint_zero)

    # The actual formal-disc involution, including its coherent square.
    z = s.symbols('z')
    phi = -z*sum(s.binomial(-s.Rational(1,3),i)*z**(3*i) for i in range(5))
    square = s.series(phi.subs(z,phi),z,0,13).removeO().expand()
    assert square == z
    disc_checks = 1
    for n in range(1,6):
        exponent = -s.Rational(1,3**(n+1))
        a = sum(s.binomial(exponent,i)*z**i for i in range(8))
        b = sum(s.binomial(-exponent,i)*z**i for i in range(8))
        assert s.series(a*b,z,0,8).removeO().expand() == 1
        disc_checks += 1

    # Literal central basis change under the involution.
    x,y,c,b1,b2 = s.symbols('x y c b1 b2')
    sharp = lambda g:(g[0],g[1],s.expand(g[2]+(b1*g[0]+b2*g[1])/2))
    old = lambda g:(g[0],g[1],s.expand(g[2]-(b1*g[0]+b2*g[1])/2))
    iota = lambda g:(-g[0],-g[1],s.expand(g[2]+b1*g[0]+b2*g[1]))
    assert sharp(old((x,y,c))) == (x,y,c)
    assert old(sharp((x,y,c))) == (x,y,c)
    assert sharp(iota(old((x,y,c)))) == (-x,-y,c)
    aa,bb,cc,dd = s.symbols('aa bb cc dd')
    AM = s.Matrix([[aa,bb],[cc,dd]]);det = AM.det();brow = s.Matrix([[b1,b2]])
    eta = (det*brow-brow*AM)/2
    old_g = lambda g:tuple(AM*s.Matrix(g[:2]))+(s.expand(det*g[2]+(eta*s.Matrix(g[:2]))[0]),)
    new_g = sharp(old_g(old((x,y,c))))
    assert new_g == (aa*x+bb*y,cc*x+dd*y,s.expand(det*c))

    U1,U2,tt,uc,ac,bb = s.symbols('U1 U2 t uc ac b')
    u = (U1,U2,uc);a = (3*tt,tt,ac)
    v = emul(emul(emul(u,eT(a)),einv(u)),epower(a,-7))
    error = -7*tt*(U1+s.Rational(21,2)*tt)
    assert tuple(s.expand(t) for t in v) == (-21*tt,0,s.expand(error))
    full = emul(v,einv(eJ(v)))
    assert full == (0,0,s.expand(2*error))
    conjugator = (bb,0,0)
    changed_u = emul(emul(conjugator,u),einv(eT(conjugator)))
    changed_a = emul(emul(conjugator,a),einv(conjugator))
    assert changed_u == (U1,U2-3*bb,s.expand(uc+(3*bb**2+3*bb*U1-2*bb*U2)/2))
    assert changed_a == (3*tt,tt,ac-bb*tt)
    elliptic_checks = 0
    for i in range(243):
        tangent = s.Rational(i%17-8,2 if i%2 else 1)
        first = i%19-9 if i%2 else -s.Rational(21,2)*tangent
        if i%2:tangent = s.Integer(0)
        second = s.Rational((7*i)%29-14,2 if i%3 else 1)
        eps = int(second.p)*pow(int(second.q),-1,3)%3
        gauge = (second-eps)/3
        assert integral3(s.Matrix([gauge]))
        uu = (first,second,s.Rational(i%13-6,2))
        ar = (3*tangent,tangent,s.Rational(i%11-5,2))
        vv = emul(emul(emul(uu,eT(ar)),einv(uu)),epower(ar,-7))
        assert emul(vv,einv(eJ(vv))) == (0,0,0)
        gg = (gauge,0,0)
        un = emul(emul(gg,uu),einv(eT(gg)))
        an = emul(emul(gg,ar),einv(gg))
        assert un[1] == eps
        assert emul(emul(einv(gg),un),eT(gg)) == uu
        assert emul(emul(einv(gg),an),gg) == ar
        elliptic_checks += 3

    result = {'statement':'E.87','status':'PASS',
        'inputs':{k:{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
                  for k,p in files.items()},
        'first_degree_map':encode(R),'first_degree_target_involution':encode(QJ),
        'first_degree_gauge_smith':smith.encode(S1),
        'first_degree_horizontal_coordinate_map':encode(Umap),
        'first_degree_relative_coordinate_map':encode(Amap),
        'first_degree_inverse_checks':first_inverse_checks,
        'first_degree_kernel_type':'Z3^10 x C3^3','first_degree_map_surjective':True,
        'coefficient_kernel_basis':encode(K),'coefficient_kernel_left_inverse':encode(Kl),
        'kernel_tau':encode(TK),'kernel_involution':encode(JK),
        'kernel_horizontal_gauge_smith':smith.encode(SK),
        'kernel_relative_basis':encode(AK),'kernel_relative_inverse':encode(AKl),
        'horizontal_defect_matrix':encode(Vdef),
        'horizontal_obstruction_in_E74_coordinates':encode(F),'E74_coordinate_moduli':mods,
        'horizontal_three_characters':encode(char),
        'horizontal_image_generators':encode(generators),
        'horizontal_image_type':'C3^3',
        'horizontal_image_inverse_selected_rows':[3,7,14],
        'horizontal_image_inverse_matrix_mod3':encode(minor.inv_mod(3)),
        'horizontal_kernel_lattice':encode(Q),'horizontal_kernel_lattice_inverse':encode(Q.inv()),
        'horizontal_liftable_gauge_smith':smith.encode(SQ),
        'horizontal_liftable_cohomology_type':'Z3^4',
        'horizontal_all_residue_tests':3**7,
        'particular_central_correction':encode(particular),
        'particular_joint_zero_correction':encode(joint_zero),
        'all_correction_denominators_prime_to3':True,
        'formal_disc_square_checks':disc_checks,
        'central_coordinate_change':'r_sharp=r+(b1*x+b2*y)/2; inverse subtracts the same term',
        'filled_target_tau':[[1,-3],[3,-2]],'filled_target_involution':[[1,-1],[0,-1]],
        'filled_target_central_actions':[7,-1],
        'filled_target_actual_obstruction':str(error),
        'filled_target_vanishing_locus':'t=0 or U1=-21*t/2',
        'filled_target_central_fibre':'Z3^2',
        'filled_target_gauge_corrections':[str(changed_u[2]-uc),str(changed_a[2]-ac)],
        'filled_target_inverse_checks':elliptic_checks,
    }
    here.joinpath('a_abelian_kernel_obstruction.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS onto first-degree map, complete descent/gauge, and',first_inverse_checks,'exact inverse checks')
    print('PASS literal rank-seven kernel, all arithmetic intertwiners, and both saturated cohomology factors')
    print('PASS complete C3^3 horizontal obstruction image and all2187 residue inputs')
    print('PASS exact Z3^4 horizontal zero locus and every integral particular correction column')
    print('PASS actual formal-disc square and central averaging coordinate morphism')
    print('PASS symbolic filled elliptic obstruction, full central gauge, and',elliptic_checks,'inverse checks')
    print('ALL PASS')


if __name__ == '__main__':
    main()
