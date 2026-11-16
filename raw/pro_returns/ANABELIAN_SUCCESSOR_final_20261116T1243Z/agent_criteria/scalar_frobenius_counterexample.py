"""Exact ordinary-new rational witness with scalar Jacobian Frobenius.

C:y^2+y=x^5 over F16 has Frobenius -4 on J. A pointed constant C13
cover over F4096 is checked twice: Cartier--Mumford, and an explicit
Kummer function recovered by linear algebra, followed by all4353 point
characters. Neither check assumes the other one's parity conclusion.
"""
import sys,json,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'code'))
from finite_jacobian import BinaryField,PolynomialRing,Jacobian
from verify_mixed_certificates import independent_double,poly_linear_product,irreducible
import sympy as sp
start=time.time();modulus=4105
assert irreducible(modulus)
F=BinaryField(modulus);R=PolynomialRing(F)
h=(1,);f=(0,0,0,0,0,1);J=Jacobian(F,h,f)
D=((483,3377,1),(2626,3144));assert J.valid(D)
ell=13;q=4096;d=12
assert D!=J.zero and J.scale(D,ell)==J.zero
frobenius16=tuple(tuple(F.power(a,16) for a in p) for p in D)
assert frobenius16==J.scale(D,-4)
assert pow(-4,3,ell)==1 and all(pow(-4,j,ell)!=1 for j in (1,2))
ds=[J.zero]
for i in range(1,ell):ds.append(J.add(ds[-1],D))
assert len(set(ds))==ell and J.add(ds[-1],D)==J.zero
cs=[0]*ell;cases={}
for i in range(1,ell):
 out,c,case=independent_double(J,ds[i]);assert out==ds[2*i%ell]
 cs[i]=c;cases[case]=cases.get(case,0)+1
As=[]
for i in range(1,ell):
 a=1;j=i
 for _ in range(d):a=F.mul(F.mul(a,a),cs[j]);j=2*j%ell
 assert j==i;As.append(a)
assert all(a not in(0,1) for a in As)
assert set(As)=={72,73}
assert all(F.mul(a,a)^a^1==0 for a in As)
cartier_poly=poly_linear_product(F,As)
assert all(a in (0,1) for a in cartier_poly)
assert [i for i,a in enumerate(cartier_poly) if a]==[0,2,6,10,12]
q16_coefficients=[]
for i in range(1,ell):
 a=1;j=i
 for _ in range(4):a=F.mul(F.mul(a,a),cs[j]);j=2*j%ell
 q16_coefficients.append(a)
assert all(F.power(a,273)==b for a,b in zip(q16_coefficients,As))

# Recover F=A+B*y with div(F)=13 D_eff -26 infinity.
# Hensel-lift y modulo u^13 and solve A+B*y=0 there, A monic degree13.
u,v=D;M=(1,)
for _ in range(ell):M=R.mul(M,u)
ylift=v
for _ in range(4):ylift=R.mod(R.add(R.sq(ylift),f),M)
assert not R.mod(R.add(R.add(R.sq(ylift),ylift),f),M)
cols=[]
for i in range(13):cols.append((0,)*i+(1,))
for i in range(11):cols.append(R.mod((0,)*i+ylift,M))
rhs=(0,)*13+(1,)
mat=[[c[j] if j<len(c) else 0 for c in cols]+[rhs[j] if j<len(rhs) else 0] for j in range(26)]
rank=0;pivots=[]
for col in range(24):
 piv=next((r for r in range(rank,26) if mat[r][col]),None)
 assert piv is not None
 mat[rank],mat[piv]=mat[piv],mat[rank]
 inv=F.inv(mat[rank][col]);mat[rank]=[F.mul(x,inv) for x in mat[rank]]
 for row in range(26):
  if row==rank or not mat[row][col]:continue
  factor=mat[row][col]
  mat[row]=[a^F.mul(factor,b) for a,b in zip(mat[row],mat[rank])]
 pivots.append(col);rank+=1
assert rank==24
assert all(not any(row) for row in mat[rank:])
sol=[mat[i][-1] for i in range(24)]
A=tuple(sol[:13])+(1,);B=tuple(sol[13:])
assert not R.mod(R.add(A,R.mul(B,ylift)),M)
norm=R.add(R.add(R.sq(A),R.mul(A,B)),R.mul(R.sq(B),f))
assert norm==M

# At a zero of F, its leading unit is B(x)^(-1) up to a13th power;
# at infinity the monic A term gives leading unit1.
counts=[0]*ell;counts[0]=1;zero_points=[]
for name,_ in J.points()[1:]:
 x,y=name;value=R.eval(A,x)^F.mul(R.eval(B,x),y)
 if value:e=F.log[value]%ell
 else:
  b=R.eval(B,x);assert b
  e=(-F.log[b])%ell;zero_points.append([x,y,e])
 counts[e]+=1
assert sum(counts)==4353
T,z=sp.symbols('T z');phi=sum(z**i for i in range(ell))
S=sum(n*z**i for i,n in enumerate(counts))
L=1+S*T+q*T*T
relative=sp.Poly(sp.resultant(phi,L,z),T)
relative_h=int(relative.eval(1));assert relative_h%2==1
pmod=[int(relative.nth(i))%2 for i in range(relative.degree()+1)]
while pmod and pmod[-1]==0:pmod.pop()
assert pmod==cartier_poly
# Independent ordinary-new check: every S at primitive13th roots is nonzero mod2.
smod=sp.Poly(S,z,modulus=2);phimod=sp.Poly(phi,z,modulus=2)
assert sp.gcd(smod,phimod).degree()==0
small=[]
for mm in (19,283):
 FF=BinaryField(mm);JJ=Jacobian(FF,h,f)
 small.append({'q':FF.q,'N':len(JJ.points())})
assert small==[{'q':16,'N':33},{'q':256,'N':193}]
# These counts give (X+4)^4. Semisimplicity makes Frobenius [-4].
assert sp.expand((z+4)**4)==z**4+16*z**3+96*z*z+256*z+256
out={'curve':'y^2+y=x^5','base_scalar_field':16,'Jacobian_Frobenius_scalar':-4,
 'small_point_counts':small,'witness_field':q,'extension_degree_from_F16':3,
 'first_constant_deck_extension_degree':3,'prime':ell,'field_modulus':modulus,
 'field_modulus_irreducible':True,'field_generator':F.generator,'torsion_divisor':D,
 'exact_order_verified':True,'Frobenius16_divisor_equals_minus4':True,
 'all_multiples':ds,'doubling_coefficients':cs,'doubling_cases':cases,
 'q_Frobenius_scalars':As,'nonzero_scalar_values':[72,73],
 'base_F16_Cartier_coefficients':q16_coefficients,
 'Kummer15_Frobenius_norm_check':True,
 'relative_zeta_mod2_exponents':[0,2,6,10,12],'new_geometric_2_rank':12,
 'Kummer_A':A,'Kummer_B':B,'norm_identity':'A^2+A*B+B^2*x^5=u^13',
 'Kummer_zero_points_and_local_character_exponents':zero_points,
 'point_character_counts':counts,'twisted_L_coefficients':{'constant':1,'T_cyclotomic_counts':counts,'T2':q},
 'relative_zeta_polynomial_coefficients_ascending':[int(relative.nth(i)) for i in range(relative.degree()+1)],
 'relative_class_number':relative_h,'relative_class_number_is_odd':True,
 'all_Cartier_and_Kummer_checks_agree':True,'seconds':time.time()-start}
print(json.dumps(out,indent=2))
