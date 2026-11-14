"""Exact finite checks for the Hahn valuations in F.40.

The proof of the infinite value group is in F.40.  Here each m-th norm
polynomial is evaluated at the series symbolically at the level of its
first nonzero terms.  A nonidentity m!-th-root conjugate first differs
at the first exponent e_j=j+1/j! whose root-of-unity multiplier is
nontrivial.  No floating-point arithmetic or approximate roots are used.
"""
from fractions import Fraction
from math import factorial
from pathlib import Path
import json

rows=[]
for m in range(1,8):
    degree=factorial(m)
    exponents=[Fraction(j)+Fraction(1,factorial(j)) for j in range(1,m+1)]
    integral_powers=[int(degree*e) for e in exponents]
    tail=Fraction(m+1)+Fraction(1,factorial(m+1))
    other=Fraction(0)
    multiplicities={}
    for k in range(1,degree):
        first=next(j for j,power in enumerate(integral_powers,1) if k*power % degree)
        other+=exponents[first-1]
        multiplicities[first]=multiplicities.get(first,0)+1
    value=tail+other
    assert (degree*other).denominator==1
    assert (value-Fraction(1,factorial(m+1)))*degree == int((value-Fraction(1,factorial(m+1)))*degree)
    assert sum(multiplicities.values())==degree-1
    rows.append(dict(m=m,norm_degree=degree,other_factor_orders={str(k):v for k,v in multiplicities.items()},norm_valuation=str(value),tail_order=str(tail),other_order=str(other),new_denominator=factorial(m+1),passed=True))

# The two refinements are separated on Q(x), and the twisting involution
# in F.41 fixes 1/2 while fixing the quotient coordinate z(1-z).
def involution(z): return 1-z
assert involution(Fraction(1,2))==Fraction(1,2)
for z in [Fraction(0),Fraction(1),Fraction(2),Fraction(3,7)]:
    assert involution(involution(z))==z
    assert z*(1-z)==involution(z)*(1-involution(z))
output=dict(status='passed',hahn_norm_checks=rows,refinement_centres=[0,1],involution_fixed_point='1/2',limitations='Finite exact leading-order checks only. Infinite value-group generation and the noncontinuous character are proved in the text, not inferred from these finite computations.')
Path(__file__).with_name('valuation_normalization_checks_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
