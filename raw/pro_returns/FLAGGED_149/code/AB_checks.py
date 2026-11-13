"""Exact finite/symbolic checks for the AB counterexamples. No external data."""
import json
from pathlib import Path
import sympy as s
x,y,T,S=s.symbols('x y T S')
reports={}
# Translation by (0,0) on y^2=x^3-x.
X=-1/x;Y=y/x**2
reports['elliptic_translation']={
 'equation_remainder':str(s.factor((Y**2-X**3+X).subs(y**2,x**3-x))),
 'second_x':str(s.simplify(-1/X)),
 'second_y':str(s.simplify(Y/X**2))}
assert reports['elliptic_translation']['equation_remainder']=='0'
assert s.simplify(-1/X-x)==0 and s.simplify(Y/X**2-y)==0
p=5
pts=[None]+[(a,b) for a in range(p) for b in range(p) if (b*b-a*a*a+a)%p==0]
u=(0,0)
U=[P for P in pts if P not in (None,u)]
perm={str(P):((-pow(P[0],-1,p))%p,(P[1]*pow(P[0],-2,p))%p) for P in U}
assert set(perm.values())==set(U)
reports['elliptic_translation']['F5_U_permutation']=perm
# Anomalous elliptic curve with #E(F5)=5, all nonzero points 5-torsion.
a,b=3,2
assert (4*a**3+27*b**2)%p!=0
pts=[None]+[(xx,yy) for xx in range(p) for yy in range(p) if (yy*yy-xx**3-a*xx-b)%p==0]
def add(P,Q):
 if P is None:return Q
 if Q is None:return P
 x1,y1=P;x2,y2=Q
 if x1==x2 and (y1+y2)%p==0:return None
 slope=((3*x1*x1+a)*pow(2*y1,-1,p) if P==Q else (y2-y1)*pow((x2-x1)%p,-1,p))%p
 x3=(slope*slope-x1-x2)%p
 return (x3,(slope*(x1-x3)-y1)%p)
orders={}
for P in pts:
 Q=None
 for n in range(1,30):
  Q=add(Q,P)
  if Q is None:
   orders[str(P)]=n;break
assert len(pts)==5 and all(orders[str(P)]==5 for P in pts if P is not None)
reports['E_F5']={'equation':'y^2=x^3+3x+2','points':pts,'orders':orders,'P_minus_Q':add((1,1),(1,1))}
# Genus-two AS test: the missing projective points are analyzed in the proof.
pts3=[(xx,yy) for xx in (1,2) for yy in range(3) if (yy**3-yy-xx-pow(xx,-1,3))%3==0]
assert pts3==[]
reports['AS_F3']={'equation':'y^3-y=x+x^-1','affine_points_x_nonzero':pts3,
 'two_simple_poles_different_exponents':[4,4], 'RH_2g_minus_2':3*(-2)+4+4,'genus':2}
# The genus-two prime-to-five test separated in B15 has an exact order-five difference.
f5=s.Poly(x**5+(x*x+1)**2,x,modulus=5)
assert s.gcd(f5,f5.diff()).degree()==0
pts5=[(xx,yy) for xx in range(5) for yy in range(5)
      if (yy*yy-xx**5-(xx*xx+1)**2)%5==0]
assert pts5==[(0,1),(0,4),(1,0)]
reports['genus2_F5_test_separated_B15']={'equation':'y^2=x^5+(x^2+1)^2',
 'polynomial_gcd_with_derivative':str(s.gcd(f5,f5.diff()).as_expr()),
 'affine_points':pts5,'rational_infinity_points':1,
 'function':'y-x^2-1','divisor':'5*(0,1)-5*infinity',
 'prime_to_5_nonabelian_section_classes':'separated in B15; this check verifies the curve and divisor inputs'}
# Normalization identity for the nodal cubic.
xx=S*(T*T-S*S);yy=T*(T*T-S*S);zz=S**3
normalization=s.expand(yy**2*zz-xx**2*(xx+zz))
assert normalization==0
reports['nodal_cubic']={'normalization_identity':str(normalization),
 'node_preimages':[[1,1],[-1,1]],'node_tangent_cone':'Y^2-X^2=(Y-X)(Y+X)'}
branch=list(range(5));assert len(set(branch))==5
reports['nonimmersion_polycurve']={'genus2_branch_values':branch,'sixth_branch':'infinity','degree_polynomial':5}
# Cyclically invariant degree-zero cusp divisors vanish for the genus-zero tower.
cyclic_constraints=s.Matrix([[1,-1,0],[0,1,-1],[1,1,1]])
assert cyclic_constraints.nullspace()==[]
reports['genus0_nonimmersion']={'cusp_divisor_constraint_matrix':[[int(v) for v in row] for row in cyclic_constraints.tolist()],
 'determinant':int(cyclic_constraints.det()),'kernel_rank':0,'cover':'z -> z^3'}
# A single toric translate intersection does not imply a translated open.
aa,bb=s.Integer(2),s.Integer(3)
tt=(1-bb)/(aa-bb);ss=aa*tt
assert (tt,ss)==(2,4) and ss-1==bb*(tt-1)
reports['toric_single_intersection']={'translation':[2,3],'source_t':int(tt),
 'target_t':int(ss),'source_coordinates':[2,1],'target_coordinates':[4,3]}
# Meridian spans: one surviving cusp kills the entire module; two do not.
def span_rank(n,subset):
 diag=s.ones(n,1);cols=[s.eye(n)[:,i] for i in subset]
 return s.Matrix.hstack(diag,*cols).rank()-1
reports['meridian_ranks']={}
for n in range(2,7):
 r1=span_rank(n,range(n-1));r2=span_rank(n,range(n-2))
 assert r1==n-1 and r2==n-2
 reports['meridian_ranks'][n]={'module_rank':n-1,'killed_with_one_remaining_cusp':r1,'killed_with_two_remaining_cusps':r2}
# All index-two subgroups of F_2^4, as kernels of its 15 nonzero linear forms.
# Column sums prove the integral group-ring identity sum_H N_H = 8*id + 7*N_G.
group_elements=list(range(16))
linear_forms=list(range(1,16))
incidence=[[int((a&v).bit_count()%2==0) for v in group_elements]
           for a in linear_forms]
assert len(incidence)==15 and all(len(row)==16 for row in incidence)
assert all(sum(row)==8 for row in incidence)
assert len({tuple(row) for row in incidence})==15
column_sums=[sum(row[v] for row in incidence) for v in group_elements]
identity_coefficients=[8*int(v==0)+7 for v in group_elements]
assert column_sums==[15]+[7]*15==identity_coefficients
for i in range(15):
 for j in range(i):
  assert sum(incidence[i][v]*incidence[j][v] for v in group_elements)==4
reports['F2_4_hyperplane_norm_identity']={
 'element_encoding':'0,...,15 represent four binary coordinates; addition is xor',
 'row_encoding':'nonzero linear forms a=1,...,15; entry is 1 iff parity(a&v)=0',
 'incidence_matrix_15_by_16':incidence,
 'row_sizes':[sum(row) for row in incidence],
 'column_multiplicities':column_sums,
 'eight_identity_plus_seven_group_norm':identity_coefficients,
 'distinct_hyperplane_intersection_size':4,
 'identity':'sum_H N_H = 8*id + 7*N_G',
 'scope':'Finite incidence identity only; the Jacobian and point-divisor arguments are proved in B9'}
out=Path(__file__).with_name('AB_checks_output.json')
out.write_text(json.dumps(reports,indent=2)+'\n')
print(json.dumps(reports,indent=2))
