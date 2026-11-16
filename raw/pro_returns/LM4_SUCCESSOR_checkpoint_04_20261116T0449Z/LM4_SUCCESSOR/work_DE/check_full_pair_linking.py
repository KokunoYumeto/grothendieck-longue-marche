"""Exact abelian comparison of twelve-point and rigid-seven orbit monodromy.

All arithmetic is in Q(i,sqrt(3)).  Pair linking is the order of the
rational difference of two normalized point coordinates at the specified
positive meridian.  We check the rigid-seven restriction against the
independently certified braid words before comparing integral matrices.
"""
from pathlib import Path
import itertools,json,time
import sympy as s

HERE=Path(__file__).resolve().parent
NEXT=HERE/'next_B56'
u=s.Symbol('u'); I=s.I
field=s.QQ.algebraic_field(I,s.sqrt(3))
pts=[u,-u,1/u,(u+I)/(u-I),-1/u,-(u+I)/(u-I),
     (u-I)/(u+I),-(u-I)/(u+I),(u+1)/(-I*u+I),
     (u+1)/(I*u-I),(u-1)/(I*u+I),(u-1)/(-I*u-I)]
# The normalization agrees literally with the B.56 certificate:
# labels 2,4,6 become infinity,0,1.
labels=[j for j in range(1,13) if j!=2]
z={j:s.cancel((pts[j-1]-pts[3])/(pts[j-1]-pts[1])*
              (pts[5]-pts[1])/(pts[5]-pts[3])) for j in labels}
assert z[4]==0 and z[6]==1
a=(s.sqrt(3)-1)/2; b=(s.sqrt(3)+1)/2
roots=[-b+I*b,I,b+I*b,-a+I*a,-1,a+I*a,0,
       -a-I*a,-b-I*b,a-I*a,1,-I,b-I*b]
assert len(roots)==13
exceptional=s.Poly(u*(u**4-1)*(u**8+14*u**4+1),u,domain=field)
assert all(exceptional.eval(r)==0 for r in roots)
assert s.Poly(s.prod(u-r for r in roots),u,domain=field)==exceptional

def multiplicity(poly,root):
    factor=s.Poly(u-root,u,domain=field)
    result=0
    while poly.degree()>0:
        quotient,remainder=poly.div(factor)
        if not remainder.is_zero:break
        poly=quotient;result+=1
    return result

def orders(fun):
    num,den=s.fraction(s.cancel(fun))
    pn=s.Poly(num,u,domain=field);pd=s.Poly(den,u,domain=field)
    assert not pn.is_zero
    finite=[multiplicity(pn,r)-multiplicity(pd,r) for r in roots]
    infinite=pd.degree()-pn.degree()
    assert sum(finite)+infinite==0
    return finite,infinite

start=time.time()
pairs=list(itertools.combinations(labels,2))
columns=[];infinity=[];differences=[]
for pair in pairs:
    f=s.cancel(z[pair[0]]-z[pair[1]])
    col,inf=orders(f)
    columns.append(col);infinity.append(inf)
    differences.append(str(f))
M=s.Matrix(columns) # 55 pair rows,13 source columns.
assert M.shape==(55,13)
fixed=pairs.index((4,6));assert M[fixed,:]==s.zeros(1,13)
raw=json.loads((NEXT/'all13_pair_linking.json').read_text())
restrict=[]
for p in raw['pair_columns']:
    restrict.append(pairs.index(tuple(sorted(p))))
R=M[restrict,:]
certified=s.Matrix(raw['matrix_rows_basis1_to13']).T
assert R==certified
rank_full=M.rank();rank_rigid=R.rank()
print('Exact thirteen roots and exceptional polynomial: PASS')
print('All55 rational pair differences have divisor supported on the14 exceptional points: PASS')
print('Normalized fixed pair(4,6) has identically zero linking: PASS')
print('Rigid-seven restriction equals all13 independently certified braid linking rows: PASS')
print('Full twelve-point normalized pair-linking rank:',rank_full)
print('Rigid-seven pair-linking rank:',rank_rigid)
assert rank_full==rank_rigid==6

# Compute a displayed rational reconstruction M=D R.  Retain only a
# basis of the rigid-seven rows, giving a compact 55-by-6 certificate.
_,basis_rows=R.T.rref()
assert len(basis_rows)==6
RB=R[list(basis_rows),:]
solutions=[]
for i in range(M.rows):
    solution,parameters=RB.T.gauss_jordan_solve(M.row(i).T)
    assert parameters.rows==0
    solutions.append(list(solution))
D=s.Matrix(solutions)
assert D*RB==M
denominator=s.ilcm(*[v.q for v in D])
integer_D=D*denominator
assert all(v.q==1 for v in integer_D)
assert integer_D*RB==denominator*M
print('Rigid row basis (labelled pairs):',[raw['pair_columns'][i] for i in basis_rows])
print('Integral reconstruction multiplier:',denominator)
print('Exact reconstruction (integer_D)(rigid row basis)=multiplier(full matrix): PASS')

# Exhibit the complete common kernel in source abelianization.
ker=M.nullspace();assert len(ker)==7 and R.nullspace()==ker
integral_kernel=[]
for v in ker:
    d=s.ilcm(*[x.q for x in v]);w=v*d
    g=s.igcd(*[int(x) for x in w]);w=w/g
    integral_kernel.append([int(x) for x in w])
print('Common rational kernel dimension:',len(ker))
for row in integral_kernel:print('kernel vector',row)

out={
 'description':__doc__,
 'normalization_labels':[2,4,6],
 'finite_labels':labels,
 'source_roots_basis1_to13':[str(r) for r in roots],
 'pair_rows':[list(p) for p in pairs],
 'rational_differences':differences,
 'full_matrix_rows_pairs_columns_basis':[[int(x) for x in M.row(i)] for i in range(M.rows)],
 'infinity_pair_orders':infinity,
 'rigid_pair_rows':raw['pair_columns'],
 'rigid_restriction_indices':restrict,
 'rigid_basis_pairs':[raw['pair_columns'][i] for i in basis_rows],
 'rigid_basis_matrix':[[int(x) for x in RB.row(i)] for i in range(RB.rows)],
 'reconstruction_multiplier':int(denominator),
 'integer_reconstruction_matrix':[[int(x) for x in integer_D.row(i)] for i in range(integer_D.rows)],
 'common_rational_kernel_basis':integral_kernel,
 'rank_full':rank_full,'rank_rigid':rank_rigid,
 'checked_identity':'integer_reconstruction_matrix * rigid_basis_matrix = reconstruction_multiplier * full_matrix',
 'remaining_claim':'This certificate concerns abelianization only; it does not prove that K is trivial.'}
(HERE/'full_pair_linking_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL EXACT CHECKS PASS; elapsed seconds',round(time.time()-start,3))
