"""Exact least-prime-five witness at infinity for y²+y=x⁵+x over F4.

The polynomial basis of F256 is F2[t]/(t^8+t^4+t^3+t+1), modulus283.
The Kummer function F=y+a*x²+b*x+c satisfies F(F+1)=(x+r)^5.
At its unique zero R and the pole infinity the leading local unit is1;
the unramified character there is consequently zero. All other local
characters are computed by F(Q)^51 in mu5. The proof that no degree3
witness exists over any extension is in the accompanying section.
"""
import sys,json
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'code'))
from finite_jacobian import BinaryField,PolynomialRing
F=BinaryField(283); R=PolynomialRing(F)
r,a,b,c=18,254,79,44
u=(c,b,a)
norm=R.add(R.add(R.sq(u),u),(0,1,0,0,0,1))
target=(F.power(r,5),F.power(r,4),0,0,r,1)
assert norm==target
assert F.power(r,16)^r^1==0
assert b==1^F.power(r,4) and a==F.power(b,2)
assert F.mul(c,c)^c==F.power(r,5)
yR=R.eval(u,r)
assert yR==42 and F.mul(yR,yR)^yR==F.power(r,5)^r

allr=[v for v in range(256) if F.power(v,16)^v^1==0]
assert len(allr)==16
assert all(F.trace(F.power(v,5))==0 for v in allr)
zeta=12;mu={F.power(zeta,i):i for i in range(5)}
assert len(mu)==5 and F.power(zeta,5)==1
counts=[1,0,0,0,0]  # infinity, whose pointed character is0
points=[]
for x in range(256):
 for y in F.artin.get(F.power(x,5)^x,[]):
  value=y^R.eval(u,x)
  exponent=0 if value==0 else mu[F.power(value,51)]
  counts[exponent]+=1
  points.append([x,y,exponent])
assert len(points)+1==193 and counts==[13,45,45,45,45]
assert [q[:2] for q in points if (q[1]^R.eval(u,q[0]))==0]==[[18,42]]

z,T=s.symbols('z T');phi=sum(z**i for i in range(5))
S=sum(n*z**i for i,n in enumerate(counts))
assert s.rem(S,phi,z)==-32
L=1-32*T+256*T*T
relative=int(s.resultant(phi,257+S,z))
assert s.expand(L-(1-16*T)**2)==0
assert relative==225**4==2562890625 and relative%2==1
assert sum(1 for q in points if q[2]==0)+1==13
# Point counting of the cover itself: five rational points above each
# zero-character point, none over nonzero-character points.
ND=5*counts[0]
assert ND==65==257-2*6*16

# The F4 quadratic twist becomes explicitly isomorphic over F256.
alpha=F.embed_f4()
twist_shift=F.artin[alpha][0]
assert F.mul(twist_shift,twist_shift)^twist_shift==alpha
result={
 'base_curve':'y^2+y=x^5+x over F4, P=infinity',
 'extension':{'q':256,'degree_over_F4':4,'binary_modulus':283},
 'Kummer_function':{'formula':'y+a*x^2+b*x+c','r':r,'a':a,'b':b,'c':c,
                    'zero_point':[r,yR]},
 'norm_polynomial_ascending':norm,
 'theta5_parameter_roots':allr,
 'all_root_r5_traces':[(v,F.trace(F.power(v,5))) for v in allr],
 'mu5_generator':zeta,'mu5_powers':[F.power(zeta,i) for i in range(5)],
 'point_character_table_affine':points,
 'point_counts':{'base':193,'cover':ND},
 'character_occupancies':counts,
 'nontrivial_L_polynomials':'1-32*T+256*T^2=(1-16*T)^2 for all four characters',
 'relative_class_number':relative,'factorization':{'3':8,'5':8},
 'Fermat_model':'u^5+z^5=1, z^5=F, u=(x+r)/z',
 'quadratic_twist':{'F4_alpha_in_F256':alpha,'shift_satisfying_d2_plus_d_alpha':twist_shift,
                    'Kummer_function':'y+shift+a*x^2+b*x+c'},
 'least_prime':5,
 'least_prime_proof':'no theta3 point because no function has sole pole of order3 at infinity; exact cubic criterion AC.22 with kappa=0 excludes all extensions'
}
print(json.dumps(result,indent=2))
