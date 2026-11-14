"""Independent resultant and matrix checks for the integral theta bridge."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import sympy as sp

BASE = Path(__file__).resolve().parent
SOURCE = BASE.parent/'research_e120'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def matrix(data):
    return sp.Matrix([[sp.Rational(v) for v in row] for row in data])


def main():
    target = SOURCE/'code/a_theta_principal_distribution.json'
    raw = target.read_bytes()
    assert sha(raw) == '5dc3b5bb733c2f2de1eecd2d6bdebf5300c443cc63cd359e22d7cb468c2a2588'
    record = json.loads(raw)
    units_path = SOURCE/'code/a_cusp_unit_symbols.json'
    units_raw = units_path.read_bytes()
    assert sha(units_raw) == 'f09f07ea6268f753f3315f4b98f8adcece35ea4dd9d3965036992fcdb7dd2e09'
    units = json.loads(units_raw)
    z,X = sp.symbols('z X')
    modulus = z*z+z+1

    def reduce(expr):
        num,den = sp.cancel(expr).as_numer_denom()
        return sp.rem(sp.rem(num,modulus,z)*sp.invert(den,modulus,z),modulus,z).expand()

    def field(pair):
        return sp.Rational(pair[0])+sp.Rational(pair[1])*z

    def encoded(expr):
        expr = reduce(expr)
        return [str(expr.coeff(z,0)),str(expr.coeff(z,1))]

    D, pi, lam = 1+2*z,1+3*z,1-z
    B = -sp.Rational(27,4)
    c = reduce(-27/pi)
    assert reduce(D*D) == -3
    theta_lead = reduce(-D/(9*pi))
    assert encoded(theta_lead) == record['theta_O_leading']
    assert reduce(1/(pi*theta_lead)) == 3*D
    outputs = []
    line_count = 0
    for unit, stated in zip(units['normalized_units'], record['norm_records']):
        product = reduce(field(unit['constant'])**6)
        for factor,saved in zip(unit['linear_factors'],stated['all_line_norms']):
            aa,bb,cc = map(field,factor['line'])
            linear = (aa+bb)/2-cc*X/3
            y_coeff = (aa-bb)/9
            two_sign_product = sp.expand(linear**2-y_coeff**2*(X**3+B))
            resultant = reduce(sp.resultant(X**3+c,two_sign_product,X))
            assert resultant != 0
            assert encoded(resultant) == saved['norm_nonzero_kernel']
            product = reduce(product*resultant**factor['power'])
            line_count += 1
        r = unit['divisor']
        scalar = reduce(product*pi**(-r[0]))
        tame = reduce(theta_lead**r[0])
        expected = reduce((3*D)**r[0])
        for label,exponent in zip(units['cusp_order'][1:],r[1:]):
            theta_value = 3*D if label.startswith('C') else -lam
            tame = reduce(tame*theta_value**exponent)
            expected = reduce(expected*theta_value**(-exponent))
        assert reduce(tame*product) == 1
        assert scalar == expected
        assert encoded(product) == stated['product_f_on_nonzero_pi_kernel']
        assert encoded(scalar) == stated['Norm_pi_f_over_f']
        outputs.append({'unit':unit['index'],'constant':encoded(scalar),
                        'full_tame_product':['1','0']})
    assert len(outputs) == 8
    assert [x['constant'] for x in outputs] == [
        ['729','0'],['1/729','0'],['729','0'],
        ['-9','-9'],['-9','-9'],['-9','-9'],['-27','0'],['-27','0']]

    maps = record['proper_regulator']
    A = sp.Matrix([[1,-3],[3,-2]])
    pullback = matrix(maps['pi_pullback'])
    transfer = matrix(maps['pi_transfer'])
    operator = matrix(maps['seven_transfer_minus_identity'])
    assert pullback == A.T and transfer == 7*A.inv().T
    assert pullback*transfer == transfer*pullback == 7*sp.eye(2)
    assert operator == 7*transfer-sp.eye(2)
    assert operator.det() == 351
    assert sp.gcd_list(list(operator)) == 3
    # The integral Smith factors are 3 and 117; 13 is a unit at three.
    assert operator.det()/3 == 117 == 9*13
    assert matrix(maps['inverse'])*operator == operator*matrix(maps['inverse']) == sp.eye(2)
    smith = maps['smith']
    L,Li = matrix(smith['left']),matrix(smith['left_inverse'])
    R,Ri = matrix(smith['right']),matrix(smith['right_inverse'])
    assert L*operator*R == sp.diag(3,9)
    assert L*Li == Li*L == R*Ri == Ri*R == sp.eye(2)
    assert all(sp.denom(v)%3 for M in (L,Li,R,Ri) for v in M)
    result = {
        'status':'PASS','author_code_imported_or_executed':False,
        'full_certificate_sha256':sha(raw),'unit_data_sha256':sha(units_raw),
        'independent_method':'polynomial resultants for the six nonzero pi-kernel points; exact rational matrix products and determinantal divisors',
        'literal_line_resultants_checked':line_count,'eight_norms_and_tame_products':outputs,
        'actual_pullback_transfer_compositions':7,
        'operator_determinant':351,'integral_Smith_factors':[3,117],
        'three_local_Smith_factors':[3,9],
        'complete_Smith_maps_and_inverse_pairs_checked':True,
        'original_arithmetic_handle_coefficient_assigned':False,
        'checked_utc':datetime.now(timezone.utc).isoformat()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
