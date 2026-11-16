"""Exact arithmetic certificate for the balanced CM Selmer argument.
No class-number database or supplied program is used.
"""
from fractions import Fraction
from math import factorial
import json
from pathlib import Path
import sympy as s
x=s.symbols('x')
f=s.cyclotomic_poly(20,x)
a=x**3-x+1
disc=int(s.discriminant(f,x)); norm=int(s.resultant(f,a,x))
assert disc==4000000 and norm==5
# pi > 3.14159, so this rational expression is a strict upper bound.
pi_lower=Fraction(314159,100000)
bound=Fraction(factorial(8),8**8)*(Fraction(4)/pi_lower)**4*2000
assert bound<13
factor_data={}
for p in (2,3,5,7,11):
 fac=s.factor_list(f,modulus=p)[1]
 degrees=[(int(s.degree(g,x)),int(e)) for g,e in fac]
 norms=[p**d for d,e in degrees]
 factor_data[str(p)]={'degrees_multiplicities':degrees,'residue_norms':norms}
 if p!=5:assert min(norms)>12
assert factor_data['5']['degrees_multiplicities']==[(1,4),(1,4)]
# The primes above 5 are conjugate and the norm-5 element generates one.
# These are therefore the only prime ideals needed by Minkowski.
result={'cyclotomic_polynomial':str(f),'discriminant':disc,
 'norm_element':str(a),'norm':norm,
 'minkowski_upper_bound_numerator':bound.numerator,
 'minkowski_upper_bound_denominator':bound.denominator,
 'minkowski_upper_bound_decimal':float(bound),'bound_less_than_13':True,
 'factorizations':factor_data,'class_number_one_conclusion':True,
 'S_primes':{'above_2':1,'above_5':2},
 'Gal_L_over_Qi_order':4,
 'twist_exponents_mod4':[1,2,3],
 'scope':'exact algebraic number field certificate; Selmer proof is in E.3'}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
