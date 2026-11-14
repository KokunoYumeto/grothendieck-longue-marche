"""Data-only independent checks of the literal Tor symbol and its maps.

No author Python module is imported or executed. Sympy performs rational
polynomial and matrix arithmetic on the frozen certificate inputs.
"""
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sympy as sp

BASE = Path(__file__).resolve().parent
SOURCE = BASE.parent / 'research_e120'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def matrix(data):
    return sp.Matrix([[sp.Rational(x) for x in row] for row in data])


def encode(mat):
    return [[str(x) for x in mat.row(i)] for i in range(mat.rows)]


def main():
    manifest_bytes = (SOURCE / 'ledger/a_elliptic_tor_symbol_manifest.json').read_bytes()
    assert sha(manifest_bytes) == '14116ce60b91b8968fa659dc022e3f4cbe02d13c9b50ef583d427207452c9001'
    expected = {
        'a_elliptic_tor_symbol.json': '953c43452a4646746d54508a7ad72a2e3d345014ffe07d045c77c0a8a08f49d9',
        'a_handle_comparison.json': '23e7c60d37bb7b388ae7551bff9b2998fd6f0e9463415ed37d863c84d9049903',
        'a_handle_torsion_gauge.json': '76ce3a134bbf7b55ffed9d999557a16db3bd1cf5c5dc93923bbfdbaa65a2d3ff',
    }
    loaded = {}
    for name, digest in expected.items():
        raw = (SOURCE / 'code' / name).read_bytes()
        assert sha(raw) == digest
        loaded[name] = json.loads(raw)
    tor = loaded['a_elliptic_tor_symbol.json']
    handles = loaded['a_handle_comparison.json']
    gauge = loaded['a_handle_torsion_gauge.json']

    # Work in Q[z]/(z^2+z+1) by polynomial remainders and Euclidean inverses.
    z, s = sp.symbols('z s')
    cyclo = z*z + z + 1

    def reduce(expr):
        numerator, denominator = sp.cancel(expr).as_numer_denom()
        return sp.rem(sp.rem(numerator, cyclo, z) * sp.invert(denominator, cyclo, z), cyclo, z).expand()

    def leading(expr):
        poly = sp.Poly(sp.expand(expr), s)
        for degree in range(4):
            coefficient = reduce(poly.nth(degree))
            if coefficient != 0:
                return degree, coefficient
        raise AssertionError('Unexpected vanishing through degree three')

    labels = ['C0', 'A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'C1', 'C2']
    derived_frames = []
    numerator_degree = denominator_degree = 0
    for label in labels:
        root = reduce(z ** int(label[1]))
        cubic_root_expansion = -root * (1 + s**3 / 3)
        X, Y, Z = {'A': (s, cubic_root_expansion, 1),
                   'B': (cubic_root_expansion, s, 1),
                   'C': (1, cubic_root_expansion, s)}[label[0]]
        # The expansion lies on X^3+Y^3+Z^3 through degree three.
        equation = sp.Poly(sp.expand(X**3 + Y**3 + Z**3), s)
        assert all(reduce(equation.nth(i)) == 0 for i in range(4))
        rn, an = leading(Y + Z)
        rd, ad = leading(3 * (X + Y))
        coefficient = reduce(an / ad)
        order = rn - rd
        boundary = reduce(z**order)
        assert boundary == 1
        numerator_degree += rn
        denominator_degree += rd
        derived_frames.append({'cusp': label, 'order': order,
                               'leading': [str(coefficient.coeff(z, 0)), str(coefficient.coeff(z, 1))],
                               'symbol_tame_boundary': ['1', '0']})
    assert numerator_degree == denominator_degree == 3
    assert derived_frames == tor['all9_frames_and_tame_boundaries']

    T = matrix(handles['actual_V_actions']['tau'])
    C = matrix(handles['actual_V_actions']['c'])
    AE, CE = T[:2, :2], C[:2, :2]
    H = matrix(handles['residual_handle_actions']['tau'])
    HC = matrix(handles['residual_handle_actions']['c'])
    R = sp.Matrix([[0, -1], [1, -1]])
    S = sp.Matrix([[0, -1], [1, 0]])
    p = sp.eye(10)[:2, :]
    j = matrix(handles['V_basis_with_j'])[:, :2]
    U = j[2:, :]
    ell = sp.Matrix([[0, 1, 3, 0, 0, 0, 0, 0, 0, 0]])
    t = sp.zeros(1, 10)
    t[0, 2] = 1
    u = sp.Matrix([[0, 1]])
    assert ell == matrix(tor['unit_character'])
    assert ell - 3*t == u*p
    assert p*j == 3*sp.eye(2) and ell*j == sp.zeros(1, 2)
    assert ell*T == 7*ell and ell*C == -ell and t*C == -t
    assert T*j == j*AE and C*j == j*CE

    # Generic CM calculation using an independently constructed block inverse.
    a, b = sp.symbols('a b')
    A = sp.Matrix([[1+3*a, -3*b], [3*b, 1+3*a-3*b]])
    q = sp.expand(A.det())
    lower = U*(A-q*sp.eye(2))/3
    generic_inverse = sp.zeros(10)
    generic_inverse[:2, :2] = A.inv()
    generic_inverse[2:, :2] = -lower*A.inv()/q
    generic_inverse[2:, 2:] = sp.eye(8)/q
    dt_generic = q*q*t*generic_inverse-t
    beta_generic = (q-1)*ell/3
    proper_generic = (q*q*u*A.inv()-u)/3
    assert all(sp.cancel(v) == 0 for v in beta_generic-dt_generic-proper_generic*p)
    assert all(sp.denom(sp.cancel(v)) == 1 for v in lower)

    F4 = sp.diag(-2, -2, *([4]*8))
    F4[2:, :2] = -2*U
    action_inputs = [('tau', T, 7), ('tau_prime', C*T*C, 7), ('Frob_K_2', F4, 4)]
    computed_regulators = []
    K = R*S.inv()
    for (name, M, chi), record in zip(action_inputs, tor['actual_elements']):
        beta = sp.Rational(chi-1, 3)*ell
        dt = chi**2*t*M.inv()-t
        proper = (chi**2*u*M[:2, :2].inv()-u)/3
        assert beta-dt == proper*p
        assert record['element'] == name
        assert matrix(record['actual_V_matrix']) == M
        assert matrix(record['raw_cross_beta']) == beta
        assert matrix(record['peripheral_boundary_dt']) == dt
        assert matrix(record['proper_regulator']) == proper
        assert matrix(record['residual_handle_coordinates_at_Weil_unit_1']) == K*proper.T
        computed_regulators.append(encode(proper))
    assert computed_regulators == [[['-7', '2']], [['7', '-5']], [['0', '-3']]]

    assert K.det() == 1 and K == sp.Matrix([[1, 0], [1, 1]])
    assert H*K == K*49*AE.inv().T
    assert HC*K == -K*CE.inv().T
    assert HC == R*CE*R.inv()
    hp = sp.Matrix([0, 1])
    k = sp.Matrix([-7, -5])
    assert (H-sp.eye(2))*hp == 3*k and HC*hp == hp
    assert (HC-sp.eye(2)).nullspace() == [hp]
    forward = sp.Matrix([[5, -7], [2, -3]])
    backward = sp.Matrix([[3, -7], [2, -5]])
    assert forward*backward == backward*forward == sp.eye(2)
    assert forward*k == sp.Matrix([0, 1])
    assert forward*(H-sp.eye(2))*hp == sp.Matrix([0, 3])
    assert matrix(tor['residual_cohomology']['coordinates_free_and_mod3']) == forward
    assert matrix(tor['residual_cohomology']['inverse']) == backward
    w = sp.Symbol('w')
    carry = -w/(1+3*w)
    assert all(sp.cancel(v) == 0 for v in k/(1+3*w)-k-(H-sp.eye(2))*(carry*hp))
    assert HC*(carry*hp) == carry*hp
    finite_carries = 0
    for n in range(1, 7):
        m = 3**n
        for r in range(3**(n-1)):
            omega = 1+3*r
            inverse_omega = pow(omega, -1, m)
            c = (-r*inverse_omega) % m
            assert all(int(x) % m == 0 for x in (inverse_omega-1)*k-(H-sp.eye(2))*(c*hp))
            finite_carries += 1
    assert finite_carries == tor['Weil_marking']['finite_carry_tests'] == 364
    assert (-8*sp.eye(2)-sp.eye(2)) == -9*sp.eye(2)
    assert all(int(x) % 9 == 0 for x in 3*(-3*hp))
    assert any(int(x) % 9 for x in -3*hp)

    # Recompute the full weight obstruction from actual matrices, without
    # solving a 450-variable intertwiner system or importing the old checker.
    pairs = list(combinations(range(10), 2))

    def exterior(M):
        row_pairs = list(combinations(range(M.rows), 2))
        col_pairs = list(combinations(range(M.cols), 2))
        return sp.Matrix([[M[i,a]*M[j,b]-M[i,b]*M[j,a]
                           for a,b in col_pairs] for i,j in row_pairs])

    LT, LC = exterior(T), exterior(C)
    W = matrix(gauge['actual_rational_weight_basis'])
    assert W.det() == 9
    assert T*W == W*sp.diag(AE, 7*sp.eye(8))
    x = sp.Symbol('x')
    char_T = T.charpoly(x).as_expr()
    char_LT = LT.charpoly(x).as_expr()
    assert sp.expand(char_T-(x*x+x+7)*(x-7)**8) == 0
    assert sp.expand(char_LT-(x-7)*(x*x+7*x+343)**8*(x-49)**28) == 0
    assert sp.gcd(char_T, char_LT) == x-7
    eigen7 = (LT-7*sp.eye(45)).nullspace()
    assert len(eigen7) == 1
    wedge_j = sp.Matrix([j[a,0]*j[b,1]-j[a,1]*j[b,0] for a,b in pairs])
    assert wedge_j != sp.zeros(45,1)
    assert LT*wedge_j == 7*wedge_j
    assert wedge_j == matrix(gauge['determinant_line'])
    D = [matrix(v).row_join(sp.zeros(45,8)) for v in handles['residual_handle_basis']]
    primitive = D[1]/3
    assert LT*primitive*T.inv()-primitive == -7*D[0]-5*D[1]
    assert LC*primitive*C.inv() == primitive
    assert pairs[19] == (2,5) and wedge_j[19] == 0
    assert primitive[19,0] == -sp.Rational(2,3)
    assert matrix(gauge['rational_c_fixed_primitive']) == primitive

    fillings = tor['conjugate_three_puncture_maps']
    selectors, probes = [], []
    for index, columns in enumerate(([0,1,2,3], [0,1,2,4])):
        Q = sp.eye(10)[columns, :]
        ext = exterior(Q)
        induced = Q*T*Q.T
        assert Q*T == induced*Q
        images = [ext*d*Q.T for d in D]
        assert all(M[:5, :] == sp.zeros(5,4) and M[:,2:] == sp.zeros(6,2) for M in images)
        probe = sp.Matrix.hstack(*[M[5,:2].T for M in images])
        assert probe.det() == 1
        assert probe*H == 49*AE.inv().T*probe
        assert matrix(fillings['abelian_filling_matrices'][index]) == Q
        assert matrix(fillings['exterior_filling_matrices'][index]) == ext
        assert matrix(fillings['residual_to_handle_commutator_maps'][index]) == probe
        assert matrix(fillings['inverse_maps'][index])*probe == sp.eye(2)
        selectors.append(Q)
        probes.append(probe)
    Q1,Q2 = selectors
    J21,J12 = Q2*C*Q1.T, Q1*C*Q2.T
    assert Q2*C == J21*Q1 and Q1*C == J12*Q2
    assert J21*J12 == J12*J21 == sp.eye(4)
    assert matrix(fillings['c_from_first_to_second']) == J21
    assert matrix(fillings['c_from_second_to_first']) == J12
    assert probes[1]*HC == CE.inv().T*probes[0]
    assert probes[0]*HC == CE.inv().T*probes[1]

    for name,digest in expected.items():
        assert sha((SOURCE/'code'/name).read_bytes()) == digest
    result = {
        'status': 'PASS', 'author_code_imported_or_executed': False,
        'frozen_manifest_sha256': sha(manifest_bytes), 'input_sha256': expected,
        'independently_derived_cusp_frames_and_boundaries': derived_frames,
        'symbolic_CM_cup_and_peripheral_cochain_identity': True,
        'proper_regulators_tau_tau_prime_Frob4': computed_regulators,
        'dual_Weil_R_and_Q_K_twist_squares': True,
        'full_Weil_unit_symbolic_coboundary_and_finite_tests': finite_carries,
        'exact_cohomology_coordinates_and_inverse': True,
        'nonzero_local_order': 3,
        'full_IA_weight_gcd': str(sp.gcd(char_T,char_LT)),
        'full_IA_common_eigenspace_dimension': len(eigen7),
        'immutable_nonintegral_primitive_entry': str(primitive[19,0]),
        'three_puncture_maps_and_integral_inverses': 2,
        'original_arithmetic_handle_coefficient_assigned': False,
        'checked_utc': datetime.now(timezone.utc).isoformat(),
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
