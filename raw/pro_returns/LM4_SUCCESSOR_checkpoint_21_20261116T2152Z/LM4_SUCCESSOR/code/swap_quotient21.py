#!/usr/bin/env python3
"""Exact rational identities for the actual free-swap quotient, hour21."""
from pathlib import Path
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
v, q, s, t, u, r, a, b = S.symbols('v q s t u r a b')
checks = {}
forms = {}

def eq(name, lhs, rhs):
    residual = S.factor(S.cancel(lhs-rhs))
    checks[name] = str(residual)
    assert residual == 0, (name, residual)

f = (v-q)/(v-1)
g = q/v
eq('f_order_two', f.subs(v, f), v)
eq('g_order_two', g.subs(v, g), v)
eq('f_g_commute', f.subs(v, g), g.subs(v, f))
Fs = (4*q-(1+q)*s)/(q+1-s)
eq('descended_sum', f + q/f, Fs.subs(s, v+q/v))
eq('descended_order_two', Fs.subs(s, Fs), s)
forms['fixed_sum_numerator'] = str(S.factor(S.together(Fs-s)))
T = (s-2)/(s-2*q)
Sinv = 2*(q*t-1)/(t-1)
eq('t_inverse', T.subs(s, Sinv), t)
eq('s_inverse', Sinv.subs(t, T), s)
eq('reflection', T.subs(s, Fs), -T)
eq('branch_discriminant', (s*s-4*q).subs(s, Sinv),
   4*(q-1)*(q*t*t-1)/(t-1)**2)
tu = (q+u*u-2*u)/(u*u+(1-2*u)*q)
tr = tu.subs(u, r)
eq('A_line_t', T.subs(s, u+q/u), tu)
eq('B_line_t', T.subs(s, Fs.subs(s, u+q/u)), -tu)
forms['B_sum'] = str(S.factor(Fs.subs(s, u+q/u)))
for name, expr in [('tu_minus_one',tu-1), ('tu_plus_one',tu+1),
                   ('branch_collision',q*tu**2-1),
                   ('same_sign_collision',tu-tr),
                   ('opposite_sign_collision',tu+tr)]:
    forms[name] = str(S.factor(expr))
eq('branch_collision_factor', q*(q+u*u-2*u)**2-(u*u+(1-2*u)*q)**2,
   (q-1)*(q-u*u)**2)
eq('same_sign_collision_factor',
   (q+u*u-2*u)*(r*r+(1-2*r)*q)
   -(q+r*r-2*r)*(u*u+(1-2*u)*q),
   2*(u-r)*(q-1)*(q-u*r))
sa = 2*(a*b-1)/(b*b-1)
qa = (a*a-1)/(b*b-1)
eq('reflection_chart_t', T.subs({s:sa,q:qa}, simultaneous=True), -b/a)
eq('cover_equation', ((q-1)/(q*t*t-1)).subs({q:qa,t:-b/a}, simultaneous=True), a*a)
h = (v*v-q)**2/(4*v*(v-1)*(v-q))
eq('Legendre_invariant_f', h.subs(v,f), h)
eq('Legendre_invariant_g', h.subs(v,g), h)
eq('Legendre_invariant_sum', h,
   ((s*s-4*q)/(4*(s-q-1))).subs(s,v+q/v))
eq('Legendre_invariant_t',
   ((s*s-4*q)/(4*(s-q-1))).subs(s,Sinv),
   (q*t*t-1)/(t*t-1))

Pq = S.Rational(399,40000)
eq('actual_base_sum', S.Rational(399,200)+S.Rational(1,200), 2)
eq('actual_base_product', S.Rational(399,200)*S.Rational(1,200), Pq)
eq('actual_base_t', T.subs({s:2,q:Pq}), 0)
forms['source_zero_for_u'] = str(u*(2-u))
forms['source_infinity_for_u'] = str(u*u/(2*u-1))
forms['cover_equation'] = 'a^2=(q-1)/(q*t^2-1), b=-t*a'
forms['Legendre_invariant'] = str(h)

out={'status':'PASS','checks':checks,'formulas':forms,
     'scope':'Rational identities only. No critical-filling or fixed-lifting conclusion.'}
target=ROOT/'records/swap_quotient21.json'
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
