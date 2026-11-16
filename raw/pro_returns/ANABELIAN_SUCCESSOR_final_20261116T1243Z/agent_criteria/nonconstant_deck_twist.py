"""Exact same-field separation of constant and nonconstant deck criteria.

The nonconstant cover is defined by twisting the pointed cyclic-seven Lang
cover of class203 by the lifted hyperelliptic involution.  The proof of this
descent and of the relative numerator is in AC.18--AC.19.  This file verifies
the finite curve and character data and the resulting integral polynomial.
"""
import sys,json
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'code'))
from finite_jacobian import BinaryField,PolynomialRing,Jacobian,genus2_characters

F=BinaryField(7); R=PolynomialRing(F); alpha=2
h=(2,1,1); f=(1,1,0,2,0,1)
ft=R.add(f,R.scale(R.sq(h),alpha))
assert ft==(0,1,2,2,2,1)
J=Jacobian(F,h,f); Jt=Jacobian(F,h,ft)
assert len(J.enumerate())==28 and len(Jt.enumerate())==8
assert len(J.points())==7 and len(Jt.points())==3
rows=genus2_characters(J)
w=next(r for r in rows if r['point']=='infinity' and r['ell']==7)
assert w['point_counts']==[1,1,0,2,2,0,1]
assert w['relative_class_number']==9409
assert genus2_characters(Jt)==[]

# Coefficients of the original and twisted curves after extension to F16.
E=BinaryField(19); RE=PolynomialRing(E); a=E.embed_f4(); b=a^1
hh=(a,1,1)
ff=RE.mul(hh,RE.add(RE.mul((0,1),hh),RE.scale((1,1),b)))
fft=RE.add(ff,RE.scale(RE.sq(hh),a))
assert len(Jacobian(E,hh,ff).points())==15
assert len(Jacobian(E,hh,fft).points())==15

t,T,z=s.symbols('t T z')
minimal=t**3+t**2-2*t-1
S=3-t-2*t*t
phi=s.Poly(sum(z**i for i in range(7)),z)
Scycl=1+z+z**6+2*z**3+2*z**4
assert s.rem(s.Poly(S.subs(t,z+z**6)-Scycl,z),phi)==0
Lp=1+S*T+4*T*T
pair=s.expand(Lp*Lp.subs(T,-T))
relative=s.expand(s.resultant(minimal,pair,t))
expected=1+10*T**2+65*T**4+279*T**6+1040*T**8+2560*T**10+4096*T**12
assert relative==expected
nplus=int(s.resultant(minimal,5+S,t))
nminus=int(s.resultant(minimal,5-S,t))
assert (nplus,nminus)==(97,83)
assert relative.subs(T,1)==8051 and 8051%2==1
assert s.Poly(relative,T,modulus=2).as_expr()==T**6+T**4+1

result={
 'field':{'q':4,'modulus':7,'alpha':2},
 'original':{'h':h,'f':f,'points4':7,'points16':15,'J_order4':28},
 'twist':{'h':h,'f':ft,'twisting_AS_constant':alpha,
          'points4':3,'points16':15,'J_order4':8,
          'Frobenius_polynomial_ascending':[16,-8,1,-2,1]},
 'original_pointed_seven_cover':w,
 'descent':{'geometric_group':'C7','arithmetic_Frobenius_on_deck':'inversion',
            'rational_lift':'the point fixed by the lifted hyperelliptic involution above infinity'},
 'real_cyclotomic_minimal':str(minimal),
 'original_character_linear_coefficient':str(S),
 'paired_twisted_factor':str(pair),
 'relative_numerator_ascending':[int(relative.coeff(T,i)) for i in range(13)],
 'relative_class_number':8051,
 'norm_plus':nplus,'norm_minus':nminus,
 'constant_odd_group_witness_over_F4':'impossible: J(F4) has order8 and every nontrivial odd group has a prime cyclic quotient',
 'scope':'strict improvement at fixed field F4; no claim of strictness after allowing every extension'
}
print(json.dumps(result,indent=2))
