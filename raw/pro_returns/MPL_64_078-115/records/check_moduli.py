#!/usr/bin/env python3
"""Independent exact checks for research notes M05--M09; never reads or edits images."""
import itertools, json
from collections import Counter
from pathlib import Path
import sympy as s

perms=list(itertools.permutations(range(3)))
identity=(0,1,2)
def parity(p):
    return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)) % 2
G=[(p,a) for p in perms for a in range(4) if parity(p)==a%2]
one=(identity,0)
def mul(x,y):
    p,a=x; q,b=y
    return tuple(p[q[i]] for i in range(3)),(a+b)%4
def inv(x):
    return next(y for y in G if mul(x,y)==one and mul(y,x)==one)
def order(x):
    y=one
    for n in range(1,13):
        y=mul(y,x)
        if y==one:return n
    raise AssertionError(x)
comms={mul(mul(mul(x,y),inv(x)),inv(y)) for x in G for y in G}
derived={one}
while True:
    new=derived|{mul(x,y) for x in derived for y in comms}
    if new==derived:break
    derived=new
central=[x for x in G if all(mul(x,y)==mul(y,x) for y in G)]
kernel=[x for x in G if x[1]==0]
assert len(G)==12 and len(derived)==3 and set(kernel)==derived
assert {x[1] for x in G}==set(range(4))
assert len(central)==2
assert all(order(x)==4 for x in G if parity(x[0])==1)

z=s.symbols('lambda')
orbit=[z,1-z,1/z,1/(1-z),z/(z-1),(z-1)/z]
j=256*(z*z-z+1)**3/(z*z*(1-z)**2)
assert all(s.cancel(j.subs(z,t)-j)==0 for t in orbit)
j1728=s.factor(j-1728)
fix=s.factor(s.together(z-1/(1-z)))
equianharmonic_mod3=s.Poly(z*z-z+1,z,modulus=3)
assert s.Poly((z+1)**2,z,modulus=3)==equianharmonic_mod3
harmonic=s.Poly((z+1)*(z-2)*(2*z-1),z,modulus=3)
def rational_mod3(value):
    num,den=s.fraction(s.cancel(value))
    return (int(num)*pow(int(den),-1,3))%3
assert all(rational_mod3(t.subs(z,-1))==2 for t in orbit)
result={
  'group_order':len(G), 'element_order_counts':dict(sorted(Counter(order(x) for x in G).items())),
  'centre_order':len(central), 'derived_subgroup_order':len(derived),
  'abelianization':'C4 via the second projection; its kernel is the derived subgroup',
  'odd_permutation_lifts':'all have order 4; the central extension by C2 is nonsplit',
  'lambda_orbit':[str(x) for x in orbit], 'j':str(j),
  'all_six_j_invariance_checks':True, 'j_minus_1728':str(j1728),
  'order_three_fixed_equation':'lambda^2-lambda+1=0',
  'fixed_equation_mod3':'(lambda+1)^2',
  'harmonic_numerator_mod3':str(harmonic.as_expr()),
  'char3_all_six_transformations_fix_lambda_minus_one':True,
  'scope':'finite algebraic group and rational functions only; no assertion about profinite GT or congruence kernels'
}
target=Path(__file__).with_name('moduli_check_results.json')
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
