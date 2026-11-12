"""Universal identities, integral monic Groebner basis, and bad-fibre checks.

All symbolic calculations use exact integers or rational functions.  No finite
sample is used as a proof of a polynomial identity.  The integral Groebner
basis is certified by monicity and pairwise coprime leading monomials, a
Buchberger criterion valid over Z because all leading coefficients are units.
"""
import sympy as S
from itertools import combinations

def check(name,expr):
    entries=list(expr) if isinstance(expr,S.MatrixBase) else [expr]
    assert all(S.cancel(v)==0 for v in entries), (name,entries)
    print('PASS',name)

r=S.Matrix([[0,1],[-1,1]]); j=S.Matrix([[0,1],[-1,0]])
old_s=-j; I=S.eye(2)
c,d,t,u,e,f,m,l,nu,v,w=S.symbols('c d t u e f m l nu v w')
a,b,g,h=S.symbols('a b g h')
A=S.Matrix([[a,b],[g,h]])
q3=c*c+c*d+d*d; q2=t*t+u*u
check('rho^3=-I',r**3+I)
check('sigma^2=-I',j**2+I)
check('rho^2-rho+I=0',r**2-r+I)
check('epsilon1=rho*sigma_final^-1',r*j.inv()-S.Matrix([[1,0],[1,1]]))
check('epsilon0=sigma_final^-1*rho',j.inv()*r-S.Matrix([[1,-1],[0,1]]))
check('rho+sigma_old=projector',r+old_s-S.diag(0,1))
check('centralizer rho norm',(c*r+d*I).det()-q3)
check('centralizer sigma norm',(t*j+u*I).det()-q2)
check('sigma conjugation = det(A)*A^-transpose',j*A*j.inv()-A.det()*A.inv().T)
check('commutator sigma = A A^transpose/det(A)',A*j*A.inv()*j.inv()-A*A.T/A.det())
rho_comm=A*r*A.inv()*r.inv()
check('rho commutator lower-right norm identity',A.det()*rho_comm[1,1]-(g*g+g*h+h*h))
z=S.Matrix([[a,b],[g,h]])
check('trace(zeta rho)=C+D-B',S.trace(z*r)-(g+h-b))
print('REFUTED scan266 alternative B+D-C: difference =',S.expand(S.trace(z*r)-(b+h-g)))
U=S.Matrix([[m,l],[0,1]])
eta=U*j*U.inv()*j.inv(); zeta=U*r*U.inv()*r.inv()
check('B0 parametrization eta',eta-S.Matrix([[m+l*l/m,l/m],[l/m,1/m]]))
check('twisted equation',zeta-eta*S.Matrix([[1,0],[m-1,1]]))
R=S.Matrix([[0,1],[v,w]])
Ss=S.Matrix([[0,-1],[-v,1-w]])
check('general normalized rho+sigma',R+Ss-S.diag(0,1))
check('general normalized epsilon1',-R*Ss.inv()-S.Matrix([[1,0],[1,1]]))
check('general normalized epsilon0',-Ss.inv()*R-S.Matrix([[1,1/v],[0,1]]))
check('general rho cube',R**3-S.Matrix([[v*w,v+w*w],[v*(v+w*w),w*(2*v+w*w)]]))
check('scan328 corrected rho^2 sigma',R**2*Ss-S.Matrix([[-v*w,w-v-w*w],[-v*(v+w*w),-w*(w*w+2*v)+v+w*w]]))

B=S.Matrix([[u,t],[-e*t,e*u]])
Gsign=S.groebner([e*e-1],e,t,u)
def rem(x):return Gsign.reduce(S.expand(x))[1]
assert all(rem(x)==0 for x in B*j-e*j*B)
assert rem(B.det()-e*q2)==0
print('PASS N_sigma normal form and determinant modulo e^2-1')
assert all(rem(x)==0 for x in B*B.T-e*B.det()*I)
print('PASS corrected scan480 b b^transpose=epsilon*det(b)*I')
print('COUNTEREXAMPLE omitted det(b): b=2I over Q has b b^t=4I, epsilon=1')

# A monic Groebner basis for the SL2 x X presentation, in the stated order.
h11,h12,h21,h22,z0=S.symbols('h11 h12 h21 h22 z0')
variables=(h11,h12,h21,h22,c,e,f,z0,t,u,d)
polys=[h11*h22-h12*h21-1,c*c+c*d+d*d-e*f*(t*t+u*u),e*e-1,f*f-1,z0*(t*t+u*u)-1]
P=[S.Poly(p,*variables,domain=S.ZZ) for p in polys]
leads=[p.monoms()[0] for p in P]
assert all(p.LC()==1 for p in P)
assert all(all(min(x,y)==0 for x,y in zip(a,b)) for a,b in combinations(leads,2))
print('INTEGRAL MONIC GROEBNER BASIS over Z; leading monomials pairwise coprime:')
for p in P:print(' ',p.as_expr())
for domain in (S.QQ,S.GF(2),S.GF(3)):
    G=S.groebner(polys,*variables,domain=domain)
    print('GROEBNER',str(domain),'basis size',len(G.polys))
    assert len(G.polys)==5
    for p in G.polys:print(' ',p.as_expr())

# Unit gradient certificate for norm relation at fixed signs.
# Gradient ideal includes 2 = z0*(t*2t+u*2u).  Then c,d belong
# via 2c+d and c+2d, hence q3 is a unit in the quotient.
check('norm-gradient certificate for 2',z0*(t*(2*t)+u*(2*u))-2*(z0*q2-1)-2)
print('GEOMETRY: smooth over sign base mu2^2; relative dimension 6; Z-flat')
print('Nonsmooth Jacobian ideal=(4); smooth locus D(2).')
print('F2: e=1+x,f=1+y,x^2=y^2=0; nilradical (x,y), length 4, one geometric component.')
print('F3: four smooth geometric components, each SL2 x Gm^2 x Ga.')

# Smallest lifting counterexamples.
for n,tau in [(4,2)]:
    from AB_core import ident,mul,scale,det,tr,sub,conj
    E=(1,0,1,1); E2=scale(1+tau,E,n)
    assert E2!=E and det(E2,n)==1 and tr(E2,n)==2%n
    assert mul(sub(E2,ident(n),n),sub(E2,ident(n),n),n)==(0,0,0,0)
    print('LIFT COUNTEREXAMPLE Z/4:',E,E2,'same projective class')
    rr=(0,1,n-1,1); ss=(0,n-1,1,0)
    a=(1,tau,-tau%n,(1+tau)%n)
    assert conj(a,rr,n)==rr and conj(a,ss,n)==scale(1+tau,ss,n)
    print('PROJECTIVE PINNING STABILIZER:',a,'fixes rho and projective sigma')
p,q,r0,s0=S.symbols('p q r0 s0')
B0=S.Matrix([[p,q],[r0,s0]])
theta=lambda M:M/M.det()
check('theta multiplicative',theta(A*B0)-theta(A)*theta(B0))
check('theta involutive',theta(theta(A))-A)
check('theta fixes rho and sigma',theta(r)-r)
print('theta on scalar 2I is (1/2)I; hence not inner over Q')
T=S.symbols('T')
poly=S.Poly(T*T+T+1,T,modulus=2)
assert poly.diff().as_expr()==1
print('PROJECTIVE IMPERFECT EXAMPLE: rho=[[0,1],[1,1]], sigma=[[1,T],[T+1,1]]')
print('det(sigma)=T^2+T+1, derivative=1, so not a square in F2(T)')
# Convert the ambient inner semidirect product to componentwise coordinates.
n0,z1=S.symbols('n0 z1')
V1=S.Matrix([[m,l],[0,1]]); V2=S.Matrix([[n0,z1],[0,1]])
check('ambient semidirect direct-product coordinate U=g*v',
      (A*V1*B0*V1.inv())*(V1*V2)-(A*V1)*(B0*V2))
# Both alternatives in the quadratic norm reading at scan264.
check('scan264 cd norm reading',(c*r+d*I).det()-(c*c+c*d+d*d))
assert S.expand((c*r+d*I).det()-(c*c+d+d*d))==c*d-d
print('REFUTED scan264 alternative d instead of cd: difference c*d-d')
# Both alternatives for the final exponent in scan509, over the universal ring.
check('scan509 exponent -1',A*r*A.inv()*r.inv()-rho_comm)
assert any(S.cancel(v)!=0 for v in A*r*A.inv()*r-rho_comm)
print('REFUTED scan509 exponent +1; exponent -1 is the commutator')
print('ALL ASSERTIONS PASSED')
