#!/usr/bin/env python3
"""Independent A.46 audit from the original W_D,W_F cocycles."""
import sympy as s
q,m,n,t,al,be,ga,j,u,v=s.symbols('q m n t alpha beta gamma j u v')
b2=lambda z:z*(z-1)/2
eps=lambda z:(z-1)/2
eta=lambda z:(z*z-1)/24
def WD(g,h):
    a,b,c,k=g; A,B,C,K=h
    return -(a+eps(k))*k*k*C-b2(a)*k*B
def WF(g,h):
    a,b,c,k=g; A,B,C,K=h
    return (b+eps(k))*k*k*(A*B-C)+b2(b)*k*A-eta(k)*k*B
F=(al,be,ga,q)
T=(m,n,t,1)
FT=(al+q*m,be+q*n,ga+q*q*t+al*q*n,q)
Fi=(-al/q,-be/q,(al*be-ga)/(q*q),1/q)
Tj=(j*m,j*n,j*t+j*(j-1)*m*n/2,1)
def residue(W):
    return s.factor((W(F,T)+W(FT,Fi)-W(F,Fi)
                     -s.summation(W(Tj,T),(j,1,q-1)))/q)
BD=(q-1)*((2*q-1)*m*m-3*m)/12
BF=(q-1)*((2*q-1)*n*n-3*n)/12
ZD=m*ga-q*(al+eps(q))*t-n*b2(al)+be/q*b2(q*m)+eps(q)*m*t+n*BD
ZF=n*(ga-al*be)+q*(be+eps(q))*(m*n-t)+m*b2(be)-eta(q)*n-al/q*b2(q*n)-eps(q)*(m*n*n-n*t)-m*BF
for label,W,Z in (('D',WD,ZD),('F',WF,ZF)):
    err=s.factor(residue(W)-Z)
    print('strict residue',label,'difference =',err)
    assert err==0
checks=(
 ('m-positive D',ZD.subs({n:0,be:(q-1)*v,t:m*v}),
  m*(ga-q*al*v)+(q*q-1)*b2(m)*v),
 ('m-positive F',ZF.subs({n:0,be:(q-1)*v,t:m*v}),
  -(q*q-1)*m*b2(v+1)),
 ('n-positive D',ZD.subs({m:0,al:(q-1)*u,t:-n*u}),
  (q*q-1)*n*b2(u+1)),
 ('n-positive F',ZF.subs({m:0,al:(q-1)*u,t:-n*u}),
  n*(ga+be*u-eta(q))-(q*q-1)*b2(n)*u),
)
for label,left,right in checks:
    err=s.factor(left-right)
    print(label,'difference =',err)
    assert err==0
print('All six independent rational-polynomial identities verified.')
print('Integrality at2 is separately supplied by the integer-valued binomial formulas.')

# Independent verification of the new negative-valuation calculation A.58.
C = ga+be*u-b2(be)
RD = m*m/6-m*(u+1)/2+u*u/2+u+s.Rational(3,8)
RF = -m*m/6-m*u/2+u/2+s.Rational(5,24)
negative_substitution = {n:m, al:be+(q-1)*(u+s.Rational(1,2)),
                         t:b2(m)-m*u}
for label, Z, R in (('D',ZD,RD), ('F',ZF,RF)):
    err=s.factor(Z.subs(negative_substitution)-m*(C+(q*q-1)*R))
    print('A58 negative valuation',label,'difference =',err)
    assert err==0
    integral_R=s.Poly(s.expand(24*R),m,u)
    assert all(v.is_Integer for v in integral_R.all_coeffs()) if integral_R.is_univariate else all(v.is_Integer for v in integral_R.coeffs())
    print('A58 24R_'+label+' =',s.expand(24*R))
print('All eight independent identities and both 24R integrality checks passed.')
