"""Finite algebraic checks for the marked four-puncture counterexample.

This checks its moduli and good-model data; the full inertia assertion is
proved in N4.tex and is not inferred from a finite quotient calculation.
"""
from pathlib import Path
import json
import sympy as sp

t=sp.symbols('t')
j=256*(1-t+t*t)**3/(t*t*(1-t)**2)
transforms=[t,1-t,1/t,1/(1-t),t/(t-1),(t-1)/t]
assert len({str(sp.cancel(a)) for a in transforms})==6
invariance=[sp.cancel(j.subs(t,a)-j)==0 for a in transforms]
assert all(invariance)
num,den=map(sp.Poly,sp.fraction(sp.cancel(j)))
assert sp.gcd(num,den).degree()==0
assert max(num.degree(),den.degree())==6
finite_sections=[sp.Integer(0),sp.Integer(1),t,sp.Integer(2)]
specialized=[a.subs(t,3) for a in finite_sections]
assert len(set(specialized))==4
diffs={f'{a}-{b}':str(sp.expand(a-b)) for ix,a in enumerate(finite_sections)
       for b in finite_sections[ix+1:]}
values_at_three={k:str(sp.sympify(v).subs(t,3)) for k,v in diffs.items()}
assert all(sp.sympify(v)!=0 for v in values_at_three.values())
out={
 'field':'Q(t)', 'curve':'P1 - {0,1,t,infinity}', 'marking':['2'],
 'moduli_invariant':str(j), 'cross_ratio_transforms':list(map(str,transforms)),
 'invariance_checks':invariance, 'numerator_degree':num.degree(),
 'denominator_degree':den.degree(), 'gcd_degree':sp.gcd(num,den).degree(),
 'field_degree_over_Qj':6,
 'finite_sections_at_t3':list(map(str,specialized)),
 'pairwise_differences_at_t3':values_at_three,
 'ramification_polynomial':'z^n - (t-3)',
 'uniformizer_valuation':1,
 'ramification_argument':'Eisenstein at t-3 for every n>=2; inertia nontrivial',
 'scope':'Algebraic data certificate; the profinite-action claim is proved in N4.tex'
}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
