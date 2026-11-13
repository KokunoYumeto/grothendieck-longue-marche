#!/usr/bin/env python3
"""Exact finite checks for G2, G5, Z142a, Z142e and Z142f.

Run: python code/G_checks.py. Requires Python 3 and SymPy.
These checks support the specified examples; no general theorem is inferred
from a finite enumeration.
"""
import itertools
import json
from pathlib import Path
import sympy as s

x,t,b=s.symbols('x t b')
h=x**3-3*x+t
f=h**2
fixed_values=(0,3,-3,4,-4)
discs={str(c):s.factor(s.discriminant(h-c,x)) for c in fixed_values}
assert s.expand(h-(t-2)-(x-1)**2*(x+2))==0
assert s.expand(h-(t+2)-(x+1)**2*(x-2))==0
assert s.expand(s.diff(f,x)-6*h*(x*x-1))==0
assert s.expand((t+2)**2-(t-2)**2)==8*t
discriminant_bounds={}
for c in fixed_values:
    D=discs[str(c)]
    assert s.expand(D-27*(4-(t-c)**2))==0
    if c==0:
        bound=27*(4-s.Rational(1,100))
        assert bound>0
        discriminant_bounds[str(c)]={'lower_bound':str(bound)}
    else:
        distance=min(abs(s.Rational(c)),abs(s.Rational(1,10)-c))
        assert distance>2
        bound=27*(4-distance**2)
        assert bound<0
        discriminant_bounds[str(c)]={'upper_bound':str(bound)}
    for branch in (t-2,t+2):
        a=s.Rational(branch.subs(t,0))-c
        z=s.Rational(branch.subs(t,s.Rational(1,10)))-c
        assert a*z>0
for c,d in itertools.combinations(fixed_values,2):
    assert s.gcd(h-c,h-d)==1
source_punctures=5*3+2*2+1
assert source_punctures==20
assert 2-source_punctures==3*(2-8)
assert 2-6==2*(2-4)
square_preimages={0,s.Integer(3),s.Integer(-3),s.Integer(4),s.Integer(-4)}
assert set().union(*(set(s.solve(x*x-c,x)) for c in (0,9,16)))==square_preimages
critical_value_polynomial=s.factor(b*(b-(t-2)**2)*(b-(t+2)**2))
value_disc=s.factor(s.discriminant(critical_value_polynomial,b))
assert value_disc==64*t**2*(t-2)**4*(t+2)**4
assert s.factor(critical_value_polynomial.subs(t,0))==b*(b-4)**2

A=s.diag(-1,-1)
assert A*A == s.eye(2)
assert A != s.eye(2)
assert A.applyfunc(lambda a: a%2) == s.eye(2)
assert A.applyfunc(lambda a: a%3) != s.eye(2)

perms=list(itertools.permutations(range(3)))
assert len(perms)==6
for p,q in itertools.product(perms,repeat=2):
    assert tuple(p[q[i]] for i in range(3)) in perms

# A free orientation-preserving involution on a genus-2 surface would have
# quotient Euler characteristic -1 = 2-2h. This gives h=3/2, not an integer.
quotient_genus=s.Rational(3,2)
assert quotient_genus.q!=1

finite_preimages={str(a):[str(v) for v in s.solve(x*x-a,x)] for a in (0,1,-1)}
assert set(s.solve(x*x-1,x))=={-s.Integer(1),s.Integer(1)}
assert set(s.solve(x*x+1,x))=={-s.I,s.I}
assert s.solve(s.diff(x*x,x),x)==[0]

out={
 'scope':'Exact example checks, not a proof by finite approximation',
 'G2':{'matrix':str(A),'order':2,'mod_2_identity':True,'mod_3_identity':False},
 'G5':{'source_genus':2,'free_involution_quotient_euler_characteristic':-1,
       'required_quotient_genus':str(quotient_genus),'integral_genus':False},
 'Z142a':{'three_puncture_permutations':[list(p) for p in perms],
           'oriented_unlabelled_self_Hom_size':6},
 'Z142e':{'cubic':str(h),'degree_six_composite':str(f),
          'finite_cover_degrees':[3,2],
          'factorization':'X_t -> Y1_t -> Y2 -> Y3 -> Y; finite etale, inclusion, finite etale, inclusion',
          'intermediate_puncture_counts':[20,8,6,4,3],
          'cubic_fibre_discriminants':{k:str(v) for k,v in discs.items()},
          'discriminant_bounds':discriminant_bounds,
          'critical_value_polynomial':str(critical_value_polynomial),
          'critical_value_discriminant':str(value_disc),
          'at_t_zero':str(s.factor(critical_value_polynomial.subs(t,0))),
          't_interval':'0 <= t <= 1/10',
          'finite_critical_values_at_zero':2,
          'finite_critical_values_for_positive_t_in_interval':3,
          'deleted_source_points':source_punctures},
 'Z142f':{'map':'x^2','finite_preimages':finite_preimages,
          'additional_source_puncture_after_target_filling':'0',
          'finite_critical_point':'0','its_image_inside_final_target':'0'},
 'all_assertions_passed':True,
 'sympy_version':s.__version__
}
text=json.dumps(out,indent=2,ensure_ascii=False)+'\n'
Path(__file__).with_name('G_checks_output.json').write_text(text)
print(text)
