#!/usr/bin/env python3
"""Exact checks of editorial calculations only; no TeX is written."""
from pathlib import Path
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
t,x,a,b,c,h,J,eps,z=s.symbols('t x a b c h J epsilon z')
F=(t+1)*(2*t-1)*(t-2)
D=t*(t-1)
Q=t*t-t+1
i=-F**2/(27*D**2)
classic=256*Q**3/D**2
sigma=(t-2)/(2*t-1)
lam=1/t
mu=1-t
checks=[]

def equal(name, left, right, note):
    difference=s.factor(s.cancel(left-right))
    assert difference==0,(name,difference)
    checks.append(dict(name=name,left=str(left),right=str(right),
                       difference=str(difference),verified=True,note=note))

equal('branch_identity',1-i,4*Q**3/(27*D**2),'B16; identity over Z[1/6].')
equal('classical_normalization',i,1-classic/1728,'B05/B16; J in the conventional Legendre normalization.')
equal('S3_generator_lambda',i.subs(t,lam),i,'B07; invariance under t -> 1/t.')
equal('S3_generator_mu',i.subs(t,mu),i,'B07; invariance under t -> 1-t.')
equal('extra_involution_square',sigma.subs(t,sigma),t,'B08.')
equal('extra_involution_commutes_lambda',sigma.subs(t,lam),lam.subs(t,sigma),'B08.')
equal('extra_involution_commutes_mu',sigma.subs(t,mu),mu.subs(t,sigma),'B08.')
equal('extra_involution_on_invariant',i.subs(t,sigma),1/i,'B17.')
equal('extra_involution_on_classical',1728*(1-1/i),1728*classic/(classic-1728),'B17.')
equal('quotient_derivative_numerator',s.diff(F,t)*D-F*s.diff(D,t),2*Q**2,'B15; scalar denominator omitted.')
r=F/D
equal('ordering_sign_lambda',r.subs(t,lam),-r,'C23; first transposition.')
equal('ordering_sign_mu',r.subs(t,mu),-r,'C23; second transposition.')
equal('ordering_sign_square',r*r,-27*i,'C23; quadratic class -3i.')

depressed=x**3+b*x+c
equal('depressed_resultant',s.resultant(depressed,s.diff(depressed,x),x),
      4*b**3+27*c**2,'B04; product of f prime over the roots of the monic cubic.')
equal('depressed_discriminant',s.discriminant(depressed,x),
      -4*b**3-27*c**2,'B04; squared Vandermonde convention.')
general=x**3+a*x**2+b*x+c
disc=s.discriminant(general,x)
root_product=s.resultant(general,3*x+a,x)
equal('root_product_general',root_product,-2*a**3+9*a*b-27*c,'B05.')
p=b-a*a/3
q=c-a*b/3+2*a**3/27
j_cubic=1728*4*p**3/(4*p**3+27*q**2)
equal('general_cubic_normalization',root_product**2/(-27*disc),
      1-j_cubic/1728,'B05.')
equal('h_family_classical',1728*h**3/(h**3-27*h**2),
      1728*h/(h-27),'B06; identities are in the rational function field.')
equal('h_solves_classical', (1728*h/(h-27)).subs(h,27*J/(J-1728)),
      J,'B06.')
equal('cube_roots_one_invariant',
      (root_product**2/(-27*disc)).subs({a:0,b:0,c:-1}),1,
      'C12; neutral equianharmonic triple x^3-1, with marked infinity.')

harmonic=s.series(i.subs(t,-1+eps),eps,0,3).removeO().expand()
assert harmonic.coeff(eps,0)==0 and harmonic.coeff(eps,1)==0
checks.append(dict(name='dual_number_harmonic',expansion=str(harmonic),
                   modulo='epsilon^2',result=0,verified=True,note='C13.'))

# Work modulo z^2-z+1 and epsilon^2 without numerical roots.
expanded=s.Poly(s.expand(Q.subs(t,z+eps)**3),eps)
for k in [0,1]:
    assert s.rem(expanded.coeff_monomial(eps**k),z*z-z+1,z)==0
checks.append(dict(name='dual_number_cyclotomic',
                   numerator='((z+epsilon)^2-(z+epsilon)+1)^3',
                   relations=['z^2-z+1=0','epsilon^2=0'],
                   result=0,verified=True,note='C13; denominator is a unit.'))
transforms=[t,1-t,1/t,1/(1-t),t/(t-1),(t-1)/t]
derivatives=[]
for tr in transforms:
    v=s.factor(s.diff(tr,t).subs(t,-1))
    assert v!=0
    derivatives.append(str(v))
checks.append(dict(name='harmonic_transforms_do_not_kill_epsilon',
                   derivatives_at_minus_one=derivatives,verified=True,
                   note='C13; all anharmonic transforms have invertible derivative at the allowed point.'))

M=s.Matrix([[1,-2],[2,-1]])
assert M.det()==3 and M*M==-3*s.eye(2)
checks.append(dict(name='sigma_matrix',determinant=3,square='-3 I',
                   verified=True,note='B08; invertibility requires 3 invertible.'))

# Explicit finite-group shape and the singular-base cover are mathematical
# arguments in the notes, not claims established by these symbolic tests.
record=dict(scope='Exact checks of stated rational/polynomial identities and first-order examples only.',
            no_transcription_changes=True,checks=checks,
            limitations=[
                'The normalizer and descent arguments are proved in prose, not by symbolic testing.',
                'DVR extension and singular normal-base examples require the hypotheses stated in C08-C10.',
                'Passing these calculations does not resolve any uncertain manuscript glyph.'
            ])
out=ROOT/'records/research/algebra_checks.json'
out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'all_verified':True,'file':str(out)}))
