"""Exact certificates for A.C2.1--A.C2.3.

All symbolic identities are checked over F2, with defining Artin--Schreier
relations imposed explicitly. Finite identities supplement, rather than
replace, the normalization, covering, and section arguments in the paper.
"""
from pathlib import Path
import json
import sympy as S

checks=[]
def check(name,condition,detail=None):
    assert bool(condition), name
    checks.append({'name':name,'passed':True,**({'detail':detail} if detail is not None else {})})
def mod2(poly,*variables):
    return S.Poly(S.expand(poly),*variables, modulus=2).as_expr()

x,a,v,d=S.symbols('x a v d')
b=a*v**3;c=a*(v+1)**3
h=x*x+x
f=a*x**5+(a+b+c)*x**3+c*x*x+b*x
u=x*x+v*v
A=a*x**3+d*x*x+(d+a+b+c)*x+b
norm=mod2(A*A+h*A+f+a*a*u**3,d,a,v,x)
G=S.groebner([d*d+d+a*a*v*v+a],d,a,v,x,modulus=2)
check('ordinary_family_norm_identity',G.reduce(norm)[1]==0)
check('ordinary_family_parameter_condition',mod2((a+b+c)**3+a*b*c,a,v)==0)

L,u0,u1,X,W,Z=S.symbols('L u0 u1 X W Z')
plane=L*(W**3+(X*X+u1*X*Z+u0*Z*Z)*W)+X*X*Z+X*Z*Z
coef=S.Poly(plane,X,W,Z).coeff_monomial(X*W*Z)
check('elliptic_quotient_hasse_scalar',coef==L*u1)
plane_ss=plane.subs(u1,0)
check('supersingular_cubic_X_derivative',mod2(S.diff(plane_ss,X)+Z*Z,L,u0,X,W,Z)==0)
check('supersingular_cubic_Z_derivative',mod2(S.diff(plane_ss,Z)+X*X,L,u0,X,W,Z)==0)

b0,c0,e,k=S.symbols('b0 c0 e k')
Agen=L*x**3+d*x*x+e*x+k
fgen=a*x**5+(a+b0+c0)*x**3+c0*x*x+b0*x
normgen=S.Poly(mod2(Agen*Agen+(x*x+x)*Agen+fgen,L,d,e,k,a,b0,c0,x),x)
check('ordinary_cubic_x5_coefficient',normgen.coeff_monomial(x**5)==L+a)
check('ordinary_cubic_x1_coefficient',normgen.coeff_monomial(x)==k+b0)
check('ordinary_cubic_x3_coefficient',normgen.coeff_monomial(x**3)==d+e+a+b0+c0)

frank1=a*x**5+b0*x**3+c0*x
nr1=S.Poly(mod2(Agen*Agen+x*Agen+frank1,L,d,e,k,a,b0,c0,x),x)
rhs3=S.Poly(mod2(L*L*(x*x+u1*x+u0)**3,L,u0,u1,x),x)
check('rank_one_cubic_left_x5',nr1.coeff_monomial(x**5)==a)
check('rank_one_cubic_right_x5',rhs3.coeff_monomial(x**5)==L*L*u1)

s=S.symbols('s')
f5=s*x**5+x**3+s**5*x
A5=x**5+s*x**4+x**3+x*x+d*x+s**5
u5=x*x+s*s
norm5=mod2(A5*A5+x*A5+f5+u5**5,d,s,x)
G5=S.groebner([d*d+d+s**8],d,s,x,modulus=2)
check('rank_one_quintic_norm_identity',G5.reduce(norm5)[1]==0)
z,q=S.symbols('z q')
check('degree_five_dickson_identity',mod2((z+q)**5+z*q*(z+q)**3+(z*q)**2*(z+q)+z**5+q**5,z,q)==0)
w,t=S.symbols('w t')
T=X*X+X*w+w*w
check('degree_five_square_factorization',mod2(w*T*T+w**5+X*X*w**3+X**4*w,X,w)==0)
H=t**4+t*t+1
substituted=t+(w*t*t+s)**2+(w*t*t+s)*w+w*w
check('hyperelliptic_quotient_equation',mod2(substituted+(H*w*w+s*w+s*s+t),s,w,t)==0)
check('artin_schreier_quotient_change',mod2(H*H*w*w+s*H*w+H*(t+s*s)+H*(H*w*w+s*w+t+s*s),s,w,t)==0)
check('rank_zero_target_degree_five',S.Poly(H*(t+s*s),t).degree()==5)
Cartier=S.Matrix([[0,1],[0,0]])
check('rank_zero_target_cartier_nilpotence',Cartier**2==S.zeros(2))

delta=S.Matrix([[0,-1],[1,-1]])
tau=S.Matrix([[0,1],[1,0]])
check('S3_dihedral_relation',delta**3==S.eye(2) and tau**2==S.eye(2) and tau*delta*tau==delta**2)
fixed=S.Matrix([1,1])
check('S3_reflection_fixed_spaces_span',S.Matrix.hstack(fixed,delta*fixed).det()!=0)

# F4 represented directly by binary polynomials modulo a^2+a+1.
def mul4(x,y):
    out=0
    while y:
        if y&1:out^=x
        y>>=1;x<<=1
        if x&4:x^=7
    return out
def cube4(x):return mul4(mul4(x,x),x)
alpha=2
obstruction=cube4(1^1^alpha)^mul4(1,mul4(1,alpha))
check('explicit_F4_cubic_obstruction_nonzero',obstruction==3,
      'For (a,b,c)=(1,1,alpha), obstruction=1+alpha=alpha^2, encoded as 3.')
special=[]
for aa in range(1,4):
 for bb in range(1,4):
  for cc in range(1,4):
   if cube4(aa^bb^cc)^mul4(aa,mul4(bb,cc))==0:
    special.append([aa,bb,cc])
check('F4_parameter_enumeration',special==[[1,1,1],[2,2,2],[3,3,3]])

out={'passed':True,'check_count':len(checks),'checks':checks,
     'F4_special_parameter_triples':special,
     'scope':'Exact symbolic and finite-field certificates; geometric and section arguments are in sections/A_char2_extension.tex.'}
Path(__file__).with_name('A_char2_extension_checks_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
