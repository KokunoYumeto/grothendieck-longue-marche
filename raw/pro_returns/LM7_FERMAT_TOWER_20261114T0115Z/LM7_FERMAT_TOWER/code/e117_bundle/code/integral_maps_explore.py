from pathlib import Path
from itertools import combinations
import json
import sympy as s
src=json.loads(Path('research_e109/code/e_quartic_ceresa_shadow.json').read_text())['coefficient_maps']
pairs=list(combinations(range(6),2)); triples=list(combinations(range(6),3))
def ext(M,k):
 inds=list(combinations(range(M.rows),k)); js=list(combinations(range(M.cols),k))
 return s.Matrix([[s.det(M.extract(a,b)) for b in js] for a in inds])
P=s.Matrix(src['proper_central_quotient']);q=s.Matrix(src['polarization']);F=s.Matrix(src['Johnson_map']);inner=s.Matrix(src['inner_map'])
keep=list(range(14)); old=s.eye(15)[:,keep]; assert P*old==s.eye(14)
eps=s.zeros(1,15);eps[0,0]=1; assert (eps*q)[0]==1
sec=(s.eye(15)-q*eps)*old
assert P*sec==s.eye(14) and eps*sec==s.zeros(1,14)
rows=list(F.T.rref()[1]); left=s.zeros(20,84); inv=F[rows,:].inv()
for k,j in enumerate(rows): left[:,j]=inv[:,k]
assert left*F==s.eye(20)
select=s.zeros(2,84);select[0,14+pairs.index((2,4))]=1;select[1,pairs.index((3,5))]=-1
assert select*F==s.Matrix(src['pure_CM_projection']);assert select*inner==s.zeros(2,6)
B2=s.Matrix([[1,-s.I/2],[-s.I,s.Rational(1,2)]]);assert B2.det()==1
B=s.diag(B2,B2,B2);B2ext=ext(B,2);BZ=P*B2ext*sec
assert s.simplify(B2ext*q-q)==s.zeros(15,1)
# D_eig = BZ^-1 D_real B, with column-first vectorization.
HC=s.kronecker_product(B.T,BZ.inv())
MC=s.Matrix([[1,s.I/8],[-s.I,-s.Rational(1,8)]])
real=(MC*select*HC).applyfunc(s.simplify)
assert all(v.is_Rational for v in real)
Msec=(ext(B,3)*s.Matrix(src['pure_CM_section'])*MC.inv()).applyfunc(s.simplify)
assert all(v.is_Integer for v in Msec)
assert real*F*Msec==s.eye(2)
assert real*inner==s.zeros(2,6)
assert all(int(s.denom(v)) & (int(s.denom(v))-1)==0 for v in real)
print('Z section and integer Johnson inverse PASS')
print('Integral CM selector denominator powers:',sorted(set(int(s.denom(v)) for v in real)))
print('M basis:',Msec.tolist())
print('selector nonzero entries:',[(i,j,str(real[i,j])) for i in range(2) for j in range(84) if real[i,j]])
# Exact symbolic normalizer equivariance on a common two-dimensional block.
a,b=s.symbols('a b',nonzero=True)
for G2,chi in [(s.diag(a,b),a*b),(s.Matrix([[0,b],[a,0]]),-a*b)]:
 G=s.diag(G2,G2,G2);GZ=P*ext(G,2)*old;GD=s.kronecker_product(G.inv().T,GZ)
 GM=s.diag(a**3/chi,b**3/chi) if G2[0,1]==0 else s.Matrix([[0,b**3/chi],[a**3/chi,0]])
 assert (select*GD-GM*select).applyfunc(s.simplify)==s.zeros(2,84)
print('full CM normalizer and coefficient-conjugation equivariance PASS')
out={'status':'PASS','q':q.tolist(),'proper_quotient':P.tolist(),'selected_polarization_row':eps.tolist(),'selected_polarization_section':sec.tolist(),'Johnson_rows':rows,'Johnson_integer_left_inverse':left.tolist(),'CM_eigen_selector':select.tolist(),'CM_real_basis':Msec.tolist(),'CM_real_selector':[[str(v) for v in row] for row in real.tolist()],'normalizer_equivariance':True}
Path('research_e117/code/integral_maps_explore.json').write_text(json.dumps(out,indent=2,default=lambda z:int(z) if z.is_Integer else str(z))+'\n')
