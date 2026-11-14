#!/usr/bin/env python3
"""Exact original-matrix certificate for both crossed hr=-1 sign branches."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
names={
 'pairings':'work/part_a/code/affine_nonproduct_general_rank_one_pairings_stage_output.json',
 'matrices':'work/part_a/code/affine_nonproduct_boundary_quotient_stage_output.json',
 'factors':'work/part_a/code/affine_nonproduct_source_zero_stage_output.json'}
data={name:json.loads((ROOT/path).read_text()) for name,path in names.items()}
r,s,t,u,v,w,z,d=sp.symbols('r s t u v w z d')
checks=[]
def check(name,value):
    assert value,name
    checks.append({'name':name,'passed':True})
def equal(left,right):return sp.cancel(left-right)==0
def clean(poly):return {e:c for e,c in poly.items() if c}
def add(*polys):
    result=Counter()
    for poly in polys:result.update(poly)
    return clean(result)
def multiply(left,right):
    result=Counter()
    for (a,ad,at,av,az),c in left.items():
        for (b,bd,bt,bv,bz),f in right.items():
            q,e=divmod(a+b,2)
            result[(e,ad+bd+q,at+bt,av+bv,az+bz)]+=c*f*(-1 if q%2 else 1)
    return clean(result)
def matrix_multiply(left,right):
    return [[add(*(multiply(left[i][k],right[k][j]) for k in range(len(right))))
             for j in range(len(right[0]))] for i in range(len(left))]
def original_terms(terms,uf,wf):
    result=Counter()
    for c,(er,es,et,eu,ev,ew,ez) in terms:
        q,e=divmod(er,2)
        result[(e,q+(uf+wf-1)*es-uf*eu-wf*ew,et-es,ev-es,ez-es)]+=c*(-1 if q%2 else 1)
    return clean(result)
def expression_terms(text):
    expression=sp.expand(sp.sympify(text,locals={str(a):a for a in (r,s,t,u,v,w,z)}))
    terms=[]
    for term in sp.Add.make_args(expression):
        c,monomial=term.as_coeff_Mul()
        powers={} if monomial==1 else monomial.as_powers_dict()
        assert set(powers)<={r,s,t,u,v,w,z} and c.is_Integer
        terms.append([int(c),[int(powers.get(a,0)) for a in (r,s,t,u,v,w,z)]])
    return terms

branches={}
for uf,wf in [(1,0),(0,1)]:
    short={}
    for row in data['pairings']['records']:
        result=Counter()
        for c,(er,eh,et,eu,ev,ew,ez) in row['exact_laurent_coefficients']:
            if (er+eh)%2:
                p=(er+eh+1)//2
                result[(p-eh-uf*eu-wf*ew,et,ev,ez)]+=c*(-1 if p%2 else 1)
        coefficients=clean(result)
        short[row['index']]=sp.Add(*(c*d**ed*t**et*v**ev*z**ez
                                    for (ed,et,ev,ez),c in coefficients.items()))
        q=[[original_terms(expression_terms(x),uf,wf) for x in data['factors']['row_q']]]
        a=[[original_terms(expression_terms(x),uf,wf)] for x in data['factors']['column_a']]
        matrix_record=next(x for x in data['matrices']['records'] if x['index']==row['index'])
        T=[[original_terms(poly,uf,wf) for poly in line]
           for line in matrix_record['boundary_quotient_matrix_6']]
        scalar=matrix_multiply(matrix_multiply(q,T),a)[0][0]
        matrix_r_odd={(ed+1,et,ev,ez):-c for (e,ed,et,ev,ez),c in scalar.items() if e}
        check('branch_%d_%d_original_matrix_trace_%d'%(uf,wf,row['index']),matrix_r_odd==coefficients)
    branches[(uf,wf)]=short

A=branches[(1,0)]
check('A_source1',equal(A[1],-(d-1)*(d+1)*(t-1)*(d*t+1)/t))
check('A_source2_t_one',equal(A[2].subs(t,1),-d*(d-1)*(d*v-d-1)/v))
check('A_source2_t_minus_inverse_d',equal(A[2].subs(t,-1/d),(d-1)*((2*d+1)*v-d-1)/v))
A1={i:sp.factor(f.subs({t:1,v:(d+1)/d},simultaneous=True)) for i,f in A.items()}
check('A1_source10',equal(A1[10],-(z-1)*(d*z-1)/z**2))
check('A1_source8_z_one',equal(A1[8].subs(z,1),-d**2/(d+1)**2))
check('A1_source5_z_inverse_d',equal(A1[5].subs(z,1/d),(1-d)*(d+2)))
check('A1_source3_d_minus_two',equal(A1[3].subs(d,-2),4))
A2={i:sp.factor(f.subs({t:-1/d,v:(d+1)/(2*d+1)},simultaneous=True)) for i,f in A.items()}
check('A2_source1_zero',A2[1]==0)
check('A2_source2_zero',A2[2]==0)
polynomials={i:sp.fraction(A2[i])[0] for i in [3,5,7,8,10]}
check('A2_source3_quartic',equal(polynomials[3],-6*d**4-9*d**3+5*d**2+11*d+4))
F=polynomials[3]
pair_certificates=[]
constants=[]
for i in [8,5,7]:
    f,g=polynomials[10],polynomials[i]
    m,n=sp.degree(f,z),sp.degree(g,z)
    columns=[sp.Poly(f*z**j,z) for j in range(n)]+[sp.Poly(g*z**j,z) for j in range(m)]
    matrix=sp.Matrix([[col.nth(j) for col in columns] for j in range(m+n)])
    determinant=sp.expand(matrix.det(method='domain-ge'))
    resultant=sp.resultant(f,g,z)
    sign=1 if sp.expand(determinant-resultant)==0 else -1
    check('A2_sylvester_determinant_%d'%i,sp.expand(determinant-sign*resultant)==0)
    cofactors=matrix.adjugate()[:,0]
    first=sp.expand(sign*sum(cofactors[j]*z**j for j in range(n)))
    second=sp.expand(sign*sum(cofactors[n+j]*z**j for j in range(m)))
    check('A2_integral_resultant_combination_%d'%i,sp.expand(first*f+second*g-resultant)==0)
    x,y,h=sp.gcdex(F,resultant,d)
    denominator=sp.ilcm(*[c.q for e in [x,y,h] for c in sp.Poly(e,d).all_coeffs()])
    X,Y,N=sp.expand(denominator*x),sp.expand(denominator*y),int(denominator*h)
    check('A2_integer_bezout_%d'%i,sp.expand(X*F+Y*resultant)==N)
    check('A2_integer_coefficients_%d'%i,all(c.is_Integer for e in [first,second,X,Y] for c in sp.Poly(e,d,z).coeffs()))
    constants.append(N)
    pair_certificates.append({'index':i,'polynomial':str(g),
        'sylvester_columns':[str(x.as_expr()) for x in columns],
        'resultant':str(sp.factor(resultant)),
        'resultant_coefficient_source10':str(first),'resultant_coefficient_other_source':str(second),
        'coefficient_F3':str(X),'coefficient_resultant':str(Y),'constant':N})
g=constants[0]
coefficients=[1]
for N in constants[1:]:
    a,b,h=sp.gcdex(g,N)
    coefficients=[int(a)*x for x in coefficients]+[int(b)]
    g=int(h)
check('A2_final_integer_combination_is_four',g==4 and sum(a*b for a,b in zip(coefficients,constants))==4)

B=branches[(0,1)]
check('B_source1',equal(B[1],(d-1)*(d+1)*(v-1)*(z-1)*(d*z+1)/(v*z)))
check('B_source10_z_minus_inverse_d',equal(B[10].subs(z,-1/d),-2*d*(d+1)))
check('B_source2_z_one',equal(B[2].subs(z,1),d*(d*t**2-1)/t))
check('B_source5_z_one',equal(B[5].subs(z,1),2*(d-1)*(d+1)*(t-1)*(v-1)/(t*v)))
check('B_source7_z_v_one_d_inverse_t_squared',equal(B[7].subs({z:1,v:1,d:t**-2},simultaneous=True),(t-1)**3*(t+1)*(t**2+1)/t**5))
check('B_source5_v_one',equal(B[5].subs(v,1),(z-1)*(d*z-1)/z**2))
check('B_source10_z_inverse_d',equal(B[10].subs(z,1/d),-2*(d-1)**2*(d+1)))

def binding(name):
    raw=(ROOT/name).read_bytes()
    return {'path':name,'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
result={'status':'PASS_EXACT_CROSSED_SIGN_STRATUM_CERTIFICATE',
 'producer':binding(str(Path(__file__).relative_to(ROOT))),
 'input_bindings':[binding(name) for name in names.values()],
 'domain':'Odd-characteristic quadratic finite-field sign extension K/L, hr=-1, d=r/h, r^2=-d nonsquare in L, and either (u,w)=(1/d,1) or (1,1/d). The d=1 overlap is covered by the separately accepted u=w=1 proof.',
 'coordinate_map':'On branch (uf,wf), r^2=-d, s=d^(uf+wf-1)/(t*v*z), u=d^-uf, w=d^-wf. Matrix monomial exponent map is recorded in original_terms; trace odd-part map is independently computed from r,h exponents.',
 'quotient_ring':'Z[d,d^-1,t,t^-1,v,v^-1,z,z^-1,r]/(r^2+d), with basis 1,r.',
 'checks':checks,'check_count':len(checks),
 'A2_substitution':{'t':'-1/d','v':'(d+1)/(2*d+1)'},
 'A2_source_polynomials':{str(i):str(f) for i,f in polynomials.items()},
 'A2_source_denominators':{str(i):str(sp.fraction(A2[i])[1]) for i in polynomials},
 'integral_resultant_and_bezout_certificates':pair_certificates,
 'final_integer_combination':{'coefficients':coefficients,'constants':constants,'result':g},
 'scope':'Complete exact coefficient verification from the bound original six-dimensional matrices and independent odd-trace transport. The accompanying proof supplies exhaustive branch coverage and all denominator/nonvanishing arguments; original group-word reconstruction is a later audit.'}
output=Path(__file__).with_name('check_nonproduct_hr_minus_one_crossed_output.json')
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks':len(checks),
                  'output':binding(str(output.relative_to(ROOT)))},indent=2))
