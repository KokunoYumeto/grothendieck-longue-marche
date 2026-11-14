#!/usr/bin/env python3
"""E.118: exact eigenunit maps and independent finite-field arithmetic.

Full reconstruction: python e_quartic_five_numerical_verify.py --gp /path/to/gp
The GP stage has no binary inputs. The Python stage independently checks
the polynomial identities, the whole residual group, point count, torsion
basis, Miller pairing, Kummer residues and the exact local order.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
from math import isqrt
import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
import sympy as s

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--gp')
args = parser.parse_args()
stem = 'e_quartic_five_numerical'
if args.gp:
    gp = str(Path(args.gp).resolve())
    with tempfile.TemporaryDirectory(prefix='e118_actual_') as td:
        td = Path(td)
        shutil.copy2(HERE / (stem + '.gp'), td / (stem + '.gp'))
        run = subprocess.run([gp, '-q', '-f', stem + '.gp'], cwd=td, capture_output=True)
        (HERE / (stem + '.out')).write_bytes(run.stdout)
        (HERE / (stem + '.err')).write_bytes(run.stderr)
        assert run.returncode == 0, run.stderr.decode(errors='replace')
        allowed = ('  ***   Warning: new stack size = ',
                   '  ***   Warning: new maximum stack size = ')
        assert all(not line.strip() or line.startswith(allowed)
                   for line in run.stderr.decode().splitlines())
rows = [json.loads(line) for line in (HERE / (stem + '.out')).read_text().splitlines()]
assert rows[-1] == {'type': 'completion', 'status': 'PASS'}
assert [r['type'] for r in rows] == ['eigenunit', 'division_field', 'numerical_prime', 'completion']
unit, division, finite, _ = rows
x = s.symbols('x')
P = s.Poly(x**8 + 2*x**4 + 5, x, domain=s.QQ)
assert P.is_irreducible

def poly(coefficients):
    return s.Poly(sum(s.Rational(v) * x**j for j, v in enumerate(coefficients)), x, domain=s.QQ)

def rem(a):
    return s.rem(a, P)

def mul(a, b):
    return rem(a*b)

def power(a, n):
    r = s.Poly(1, x, domain=s.QQ)
    while n:
        if n & 1:
            r = mul(r, a)
        a = mul(a, a)
        n //= 2
    return r

def evaluate_poly(a, b):
    r = s.Poly(0, x, domain=s.QQ)
    for coefficient in a.all_coeffs():
        r = rem(r*b + s.Poly(coefficient, x, domain=s.QQ))
    return r

u, w, ui = [poly(unit[k]) for k in ['unit_coefficients', 'correction_coefficients', 'inverse_coefficients']]
ii = s.Poly((x**4+1)/2, x, domain=s.QQ)
assert power(ii, 2) == s.Poly(-1, x, domain=s.QQ)
tau = rem(ii*s.Poly(x, x, domain=s.QQ))
assert evaluate_poly(u, tau) == mul(power(u, 3), power(w, 5))
assert mul(u, ui) == s.Poly(1, x, domain=s.QQ)
for element, key in [(u, 'unit_minpoly'), (w, 'correction_minpoly')]:
    f = s.Poly(s.sympify(unit[key].replace('^', '**')), x, domain=s.QQ)
    assert f.LC() == 1 and abs(f.TC()) == 1
    assert all(c.q == 1 for c in f.all_coeffs())
    assert evaluate_poly(f, element).is_zero

def mm(A, B):
    return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2)) % 5
                 for i in range(2) for j in range(2))

I = (1,0,0,1)
Ta, Tb, C = (2,0,0,1), (1,0,0,3), (0,1,1,0)
group, todo = {I}, [I]
for A in todo:
    for B in [Ta, Tb, C]:
        M = mm(A, B)
        if M not in group:
            group.add(M)
            todo.append(M)
assert len(group) == division['all_embeddings_count'] == 32
assert all(mm(A, B) in group for A in group for B in group)
assert mm(Ta,Tb) == mm(Tb,Ta)
assert mm(mm(mm(Ta,Ta),Ta),Ta) == I and mm(mm(mm(Tb,Tb),Tb),Tb) == I
assert mm(C,C) == I and mm(mm(C,Ta),C) == mm(mm(Tb,Tb),Tb)

# For k=(kappa_u,kappa_cu), H=diag(1,-1)k. These are the
# literal transformations of k(g^-1 h g) obtained from the unit characters
# and the cyclotomic action, for tau_a, tau_b and c respectively.
S = (1,0,0,4)
kum = [(3,0,0,1), (1,0,0,2), (0,4,4,0)]
assert all(mm(mm(A,S),K) == S for A,K in zip([Ta,Tb,C],kum))
assert (32*3) % 5 == 1

p = finite['p']
assert p == 3121 and all(p%d for d in range(2,isqrt(p)+1))
assert p % 40 == 1 and (p-1)%5 == 0 and (p-1)%25 != 0
ip, ap, bp = finite['i_a_b']
assert ip*ip % p == p-1
assert pow(ap,4,p) == (-1-2*ip)%p and pow(bp,4,p) == (-1+2*ip)%p
assert pow(finite['fifth_root_of_two'],5,p) == 2
assert pow(finite['primitive_eighth_root'],4,p) == p-1

def finite_poly(coefficients, a):
    z = 0
    for c in reversed(coefficients):
        c = Fraction(c)
        z = (z*a + c.numerator*pow(c.denominator,-1,p)) % p
    return z

values = [finite_poly(unit['unit_coefficients'],v) for v in [bp,ap]]
assert values == finite['unit_values'] == [1362,1576]
residues = [pow(v,(p-1)//5,p) for v in values]
assert residues == finite['fifth_residues'] == [2163,2119]
assert residues[0] != 1

def add(Pt, Qt):
    if Pt is None:
        return Qt
    if Qt is None:
        return Pt
    X,Y = Pt
    U,V = Qt
    if X == U and (Y+V)%p == 0:
        return None
    slope = ((3*X*X+1)*pow(2*Y,-1,p) if Pt == Qt
             else (V-Y)*pow(U-X,-1,p)) % p
    nx = (slope*slope-X-U)%p
    return nx, (slope*(X-nx)-Y)%p

def times(Pt,n):
    r = None
    while n:
        if n & 1:
            r = add(r,Pt)
        Pt = add(Pt,Pt)
        n //= 2
    return r

PP, PM = [tuple(v) for v in finite['points']]
assert all((Y*Y-X**3-X)%p == 0 for X,Y in [PP,PM])
assert times(PP,5) is None and times(PM,5) is None
assert times(PP,2) == ((-PP[0])%p,ip*PP[1]%p)
assert times(PM,2) == ((-PM[0])%p,(-ip*PM[1])%p)
span = {add(times(PP,a),times(PM,b)) for a,b in product(range(5),repeat=2)}
assert len(span) == 25
card = 1
quadratic_counts = [0,0,0]
for a in range(p):
    v = (a**3+a)%p
    character = pow(v,(p-1)//2,p)
    if v == 0:
        card += 1
        quadratic_counts[0] += 1
    elif character == 1:
        card += 2
        quadratic_counts[1] += 1
    else:
        assert character == p-1
        quadratic_counts[2] += 1
assert card == finite['elliptic_order'] == 3200 and card//25 % 5

def line_ratio(R,S,X):
    """Miller line through R,S divided by the vertical line through R+S."""
    assert R is not None and S is not None and X is not None
    A,B = R
    D,E = S
    xx,yy = X
    T = add(R,S)
    if A == D and (B+E)%p == 0:
        return (xx-A)%p
    slope = ((3*A*A+1)*pow(2*B,-1,p) if R == S
             else (E-B)*pow(D-A,-1,p)) % p
    numerator = (yy-B-slope*(xx-A))%p
    denominator = 1 if T is None else (xx-T[0])%p
    assert numerator and denominator
    return numerator*pow(denominator,-1,p)%p

def miller(Pt,X,n):
    f,T = 1,Pt
    for bit in bin(n)[3:]:
        f = f*f*line_ratio(T,T,X)%p
        T = add(T,T)
        if bit == '1':
            f = f*line_ratio(T,Pt,X)%p
            T = add(T,Pt)
    assert T is None
    return f

eta = (-miller(PP,PM,5)*pow(miller(PM,PP,5),-1,p))%p
assert eta == finite['Weil_pairing'] == 190 and eta != 1 and pow(eta,5,p) == 1
logs = [next(j for j in range(5) if pow(eta,j,p) == z) for z in residues]
assert logs == finite['Kummer_logarithms'] == [3,4]
assert [logs[0],(-logs[1])%5] == finite['global_cocycle_coordinates'] == [3,1]

result = {
 'statement': 'E.118', 'status': 'PASS',
 'source_field_polynomial': str(P.as_expr()),
 'eigenunit': unit, 'division_field': division, 'numerical_prime': finite,
 'exact_rational_polynomial_identities_verified': True,
 'residual_group_order': len(group), 'closure_products_checked': len(group)**2,
 'actual_invariant_tensor_generator_checks': 3,
 'independent_primality_trial_division_limit': isqrt(p),
 'independent_complete_point_count': card,
 'quadratic_value_counts_zero_square_nonsquare': quadratic_counts,
 'independent_five_torsion_span_size': len(span),
 'independent_Miller_Weil_pairing': eta,
 'local_five_primary_group': [5,5],
 'nonzero_unramified_compact_class_order': 5,
 'mixed_criterion_at_3121': {'toric_inertia_valuation': 0,
                            'compact_coefficient_valuation': 0,
                            'local_Kummer_exponent': 1,
                            'integrality_inequality_satisfied': False},
 'sources_sha256': {n: hashlib.sha256((HERE/n).read_bytes()).hexdigest()
                    for n in [stem+'.gp', stem+'.out']},
 'scope': 'Exact field and unit maps, actual mod-five Kummer descent data, and a numerical mixed nonlifting witness. The infinite integral cohomology lift and class-two obstruction comparison use the complete E.112 and E.115 proofs; no uncomputed Frobenius matrix modulo25 is assigned.'
}
text = json.dumps(result,indent=2)+'\n'
(HERE/'e_quartic_five_numerical_verify.json').write_text(text)
print(text,end='')
