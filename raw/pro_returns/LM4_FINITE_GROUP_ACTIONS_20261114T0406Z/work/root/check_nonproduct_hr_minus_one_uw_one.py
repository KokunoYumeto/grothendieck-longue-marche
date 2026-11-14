#!/usr/bin/env python3
"""Independent exact certificate for the hr=-1, u=w=1 sign stratum.

All original matrix and trace inputs are bound by complete-byte hashes.
The local quotient-ring arithmetic here is independent of the producer's
Laurent helpers. The full original-word reconstruction remains a separate
input obligation for any later numbered general theorem.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
folder = ROOT / 'work/part_a/code'
paths = {
    'pairings': folder / 'affine_nonproduct_general_rank_one_pairings_stage_output.json',
    'matrices': folder / 'affine_nonproduct_boundary_quotient_stage_output.json',
    'factors': folder / 'affine_nonproduct_source_zero_stage_output.json',
}
data = {name: json.loads(path.read_text()) for name, path in paths.items()}
r, h, t, u, v, w, z, s = sp.symbols('r h t u v w z s')
ratio = sp.symbols('d')
checks = []

def check(name, value):
    assert value, name
    checks.append({'name': name, 'passed': True})

def difference_zero(left, right):
    return sp.cancel(left-right) == 0

# Before imposing the source2 consequence, retain only hr=-1,u=w=1.
row2 = next(row for row in data['pairings']['records'] if row['index'] == 2)
source2_before = sp.Add(*(coefficient*(-ratio)**((er+eh+1)//2)*ratio**(-eh)
                         *t**et*v**ev*z**ez
                         for coefficient,(er,eh,et,eu,ev,ew,ez) in row2['exact_laurent_coefficients']
                         if (er+eh) % 2))
check('source2_before_t_relation', difference_zero(source2_before, ratio*(ratio*t-1/t)))

# Direct exponent transport of r times the odd trace, in coordinates
# d=r/h, R=r^2, followed by R=-t^-2, d=t^-2, u=w=1.
short = {}
for row in data['pairings']['records']:
    coefficients = Counter()
    for coefficient, (er, eh, et, eu, ev, ew, ez) in row['exact_laurent_coefficients']:
        if (er+eh) % 2:
            power_R = (er+eh+1)//2
            power_d = -eh
            coefficients[(et-2*power_R-2*power_d, ev, ez)] += coefficient*(-1 if power_R % 2 else 1)
    short[row['index']] = sp.Add(*(coefficient*t**et*v**ev*z**ez
                           for (et,ev,ez), coefficient in coefficients.items() if coefficient))

check('source10_normalized_odd_factor', difference_zero(short[10], -(z-t**2)*(z-1)/(t**2*z**2)))
check('source8_on_z_one', difference_zero(short[8].subs(z,1), -(v-1)*(v-t**2)/(t**2*v**2)))
check('source3_on_v_t_squared', difference_zero(short[3].subs(v,t**2), (t**2-1)**2*(t**2+1)/t**6))
f3 = t**4+t**3*v-2*t**3-t**2*v+t**2+2*t*v-t-v
f8 = -t**6-t**4*v+t**4-t**2*v+t**2+v
check('source3_linear_factor', difference_zero(short[3], (v-1)*f3/(t**3*v**2)))
check('source8_on_z_t_squared_linear_factor', difference_zero(short[8].subs(z,t**2), (v-1)*f8/(t**4*v**2)))
leading3, constant3 = sp.Poly(f3,v).all_coeffs()
leading8, constant8 = sp.Poly(f8,v).all_coeffs()
resultant = -t*(t-1)*(t+1)*(t**2+1)*(t**2-t+1)**2
check('explicit_two_by_two_resultant_identity', sp.expand(leading3*constant8-leading8*constant3-resultant) == 0)
check('explicit_bezout_identity', sp.expand(leading3*f8-leading8*f3-resultant) == 0)
quotient, remainder = sp.div(f3-(t-1)*(v-1), t**2-t+1, t)
check('primitive_sixth_root_reduction', remainder == 0)
for index in range(11):
    check('single_trace_%d_zero_on_exceptional_family' % index,
          sp.cancel(short[index].subs({v:1,z:t**2})) == 0)

# Ring Z[t,t^-1,r]/(r^2+t^-2), represented by integer dictionaries.
# A key (epsilon,n) means r^epsilon t^n with epsilon in{0,1}.
def clean(poly):
    return {key:value for key,value in poly.items() if value}

def add(*polynomials):
    answer = Counter()
    for poly in polynomials:
        answer.update(poly)
    return clean(answer)

def multiply(left, right):
    answer = Counter()
    for (a,b),c in left.items():
        for (e,f),g in right.items():
            quotient, residue = divmod(a+e,2)
            answer[(residue,b+f-2*quotient)] += c*g*(-1 if quotient % 2 else 1)
    return clean(answer)

def matrix_multiply(left, right):
    assert len(left[0]) == len(right)
    return [[add(*(multiply(left[i][k],right[k][j]) for k in range(len(right))))
             for j in range(len(right[0]))] for i in range(len(left))]

def original_matrix_polynomial(terms):
    answer = Counter()
    for coefficient,(er,es,et,eu,ev,ew,ez) in terms:
        quotient,residue = divmod(er,2)
        answer[(residue,-es+et+2*ez-2*quotient)] += coefficient*(-1 if quotient % 2 else 1)
    return clean(answer)

def expression_polynomial(text):
    original = sp.sympify(text,locals={str(x):x for x in [r,s,t,u,v,w,z]})
    substituted = sp.expand(original.subs({s:1/t,u:1,v:1,w:1,z:t**2},simultaneous=True))
    answer = Counter()
    for term in sp.Add.make_args(substituted):
        coefficient,monomial = term.as_coeff_Mul()
        powers = {} if monomial == 1 else monomial.as_powers_dict()
        assert set(powers) <= {r,t} and coefficient.is_Integer
        er,et = int(powers.get(r,0)),int(powers.get(t,0))
        quotient,residue = divmod(er,2)
        answer[(residue,et-2*quotient)] += int(coefficient)*(-1 if quotient % 2 else 1)
    return clean(answer)

q = [[expression_polynomial(text) for text in data['factors']['row_q']]]
column = [[expression_polynomial(text)] for text in data['factors']['column_a']]
matrices = {row['index']:[[original_matrix_polynomial(poly) for poly in line]
                         for line in row['boundary_quotient_matrix_6']]
            for row in data['matrices']['records']}
for index in range(11):
    scalar = matrix_multiply(matrix_multiply(q,matrices[index]),column)[0][0]
    check('matrix_derived_single_trace_%d_has_zero_odd_part' % index,
          not any(coefficient for (epsilon,n),coefficient in scalar.items() if epsilon))
word = matrix_multiply(matrix_multiply(matrix_multiply(q,matrices[2]),matrices[5]),column)[0][0]
odd = {(epsilon,n):coefficient for (epsilon,n),coefficient in word.items() if epsilon}
check('actual_word_2_5_exact_odd_part', odd == {(1,0):-1,(1,-4):1})
check('word_factorization', difference_zero(-r+r/t**4, -r*(t-1)*(t+1)*(t**2+1)/t**4))

def binding(path):
    raw = path.read_bytes()
    return {'path':str(path.relative_to(ROOT)),'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

result = {
    'status':'PASS_EXACT_LOCAL_SIGN_STRATUM_CERTIFICATE',
    'producer':binding(Path(__file__)),
    'input_bindings':[binding(path) for path in paths.values()],
    'checks':checks,'check_count':len(checks),
    'domain':'Odd-characteristic field L; r in a quadratic field extension with sign involution, r^2 in L and nonsquare; d=r/h in L*, t,u,v,w,z in L*, hr=-1, u=w=1, and <u,v,w,z> nontrivial.',
    'short_trace_coordinate_map':'r*O_i; source2 first forces d=t^-2 and r^2=-t^-2; the displayed raw-trace transport is then applied.',
    'source10_factor':str(-(z-t**2)*(z-1)/(t**2*z**2)),
    'source8_z_one_factor':str(-(v-1)*(v-t**2)/(t**2*v**2)),
    'source3_v_t_squared_factor':str((t**2-1)**2*(t**2+1)/t**6),
    'f3':str(f3),'f8':str(f8),'resultant':str(resultant),
    'bezout_coefficients':{'f8':str(leading3),'f3':str(-leading8)},
    'sixth_root_reduction_quotient':str(quotient),
    'exceptional_character_map':'(r,s,t,u,v,w,z)=(r,t^-1,t,1,1,1,t^2), r^2=-t^-2; h=r*t^2=-r^-1.',
    'ring_definition':'Z[t,t^-1,r]/(r^2+t^-2), coefficient basis1,r',
    'word_order':'q*T2*T5*a, original zero-based source indices2 and5',
    'word_odd_coefficients':[[list(key),coefficient] for key,coefficient in sorted(odd.items())],
    'word_odd_factor':'-r*(t-1)*(t+1)*(t^2+1)/t^4',
    'scope':'Independent algebraic verification from the hash-bound actual source matrices and rank-one data. The accompanying proof supplies the field-theoretic nonvanishing and the common-submodule implication. No other sign stratum or R=0 module is claimed settled.'}
output=Path(__file__).with_name('check_nonproduct_hr_minus_one_uw_one_output.json')
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks':len(checks),'output':binding(output)},indent=2))
