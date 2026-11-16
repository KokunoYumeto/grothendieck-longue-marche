"""Exact actual elliptic-quotient data for the genus-two wreath intermediate."""
from pathlib import Path
import sympy as S,json
s,J=S.symbols('s J');M=s**4+2*s*s+2

def red(f):
 n,d=S.cancel(f).as_numer_denom()
 return S.rem(n*S.invert(d,M,s),M,s)
i=-1-s*s;q=3+2*s+2*s*s;yQ=-2*s*q
assert red(i*i+1)==0
assert red(yQ*yQ-(q**3-6*q*q+q))==0
slope=red((3*q*q-12*q+1)/(2*yQ));x2=red(slope*slope+6-2*q);y2=red(-yQ+slope*(q-x2))
assert x2==1 and red(y2-2*i)==0
A=red(3*q-6);B=red(3*q*q-12*q+1);C=red(q**3-6*q*q+q)
X=S.symbols('X');weier=X**3+B*X**2+red(A*C)*X+red(C*C)
assert red(S.discriminant(weier,X)-32*C*C)==0
I=red(B*B-3*A*C);j=red(8*I**3/(C*C))
pol=S.Poly(S.resultant(M,J-j,s),J).monic()
expected=J**4+247168*J**3+33016848384*J**2+1269854633984*J+12786860032000
assert pol.as_expr()==expected
assert len(S.factor_list(pol.as_expr())[1])==1 and S.factor_list(pol.as_expr())[1][0][1]==1
assert pol.is_irreducible
sturm=pol.sturm();real_count=pol.count_roots(-S.oo,S.oo);assert real_count==0
rows=[]
for p,root,expected_trace,expected_coeff in [(29,4,-4,[15,25,24]),(37,17,-4,[17,21,33])]:
 assert (root**4+2*root*root+2)%p==0
 qp=int(q.subs(s,root))%p
 Ap=(3*qp-6)%p;Bp=(3*qp*qp-12*qp+1)%p;Cp=(qp**3-6*qp*qp+qp)%p
 coeff=[Bp,Ap*Cp%p,Cp*Cp%p];assert coeff==expected_coeff
 aa,bb,cc=coeff;disc=(aa*aa*bb*bb-4*bb**3-4*aa**3*cc-27*cc*cc+18*aa*bb*cc)%p;assert disc
 residues=[];count=1
 for x in range(p):
  val=(x**3+aa*x*x+bb*x+cc)%p
  chi=0 if not val else (1 if pow(val,(p-1)//2,p)==1 else -1)
  residues.append(chi);count+=1+chi
 trace=p+1-count;assert trace==expected_trace and trace%p
 d=trace*trace-4*p;sf=-1
 for l,e in S.factorint(-d).items():
  if e%2:sf*=int(l)
 rows.append({'prime':p,'s_residue':root,'q_residue':qp,'weierstrass_coefficients':coeff,'polynomial_discriminant_nonzero':disc,'quadratic_character_values':residues,'point_count':count,'trace':trace,'frobenius_discriminant':d,'quadratic_field_squarefree_radicand':sf,'ordinary':True})
assert [r['quadratic_field_squarefree_radicand'] for r in rows]==[-1,-33]
# Exact third-multiple/cusp coordinates and Prym image, retained without a reduction claim.
l=red((2*i-yQ)/(1-q));x3=red(l*l+6-1-q);y3=red(-yQ+l*(q-x3));t3=red(x3-q)
assert red(y3*y3-(x3**3-6*x3*x3+x3))==0 and t3==-4*s
xF=red(C/t3);FF=lambda x:red(x**3+B*x*x+A*C*x+C*C)
assert FF(xF)!=0
xF2=red((3*xF*xF+2*B*xF+A*C)**2/(4*FF(xF))-B-2*xF)
assert FF(xF2)!=0
result={'status':'PASS','base_field_polynomial':str(M),'i':str(i),'q':str(q),'Q_y':str(yQ),'double_Q':['1',str(2*i)],'genus_two_equation':'v^2=(u^2+q)^3-6*(u^2+q)^2+(u^2+q)','prym_quartic':'V^2=t*(t^3+A*t^2+B*t+C)','prym_weierstrass':str(weier),'prym_j':str(j),'j_minimal_polynomial':str(expected),'minimal_polynomial_irreducible_over_Q':True,'exact_sturm_sequence':[str(x.as_expr()) for x in sturm],'real_roots_by_exact_sturm':int(real_count),'ordinary_reductions':rows,'third_Q':[str(x3),str(y3)],'ordinary_cusp_u_squared':str(t3),'prym_ordinary_cusp_x':str(xF),'prym_cusp_not_order_2_or_4':True,'scope':'Exact algebraic quotient, j/Sturm and ordinary finite-field certificates. No stable marked-model or fixed-subgroup conclusion is inferred from these finite calculations.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
