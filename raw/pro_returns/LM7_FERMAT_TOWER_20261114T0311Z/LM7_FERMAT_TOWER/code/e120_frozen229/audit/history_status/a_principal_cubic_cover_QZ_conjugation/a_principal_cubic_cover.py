#!/usr/bin/env python3
"""Actual framed cubic cover, norm-seven lift, and next augmentation map."""
from pathlib import Path
from hashlib import sha256
from itertools import combinations,product
from math import gcd
import json
import sympy as s
from a_e120_exact import QZ

base=Path(__file__).resolve().parent
names=['a_elliptic_tor_symbol.json','a_handle_comparison.json',
       'a_theta_principal_distribution.json','a_e120_exact.py']
hashes={n:sha256((base/n).read_bytes()).hexdigest() for n in names}
tor=json.loads((base/names[0]).read_text())
handle=json.loads((base/names[1]).read_text())
distribution=json.loads((base/names[2]).read_text())
assert tor['status']==handle['status']==distribution['status']=='PASS'
u,w,v=s.symbols('u w v')
G=w**3-27*u**3-18*u*w*v-9*v**3
xx=-3*u**3-u*w*v
yy=3*u**3+u*w*v+v**3
zz=-u*w*v-v**3
quot,rem=s.div(s.expand(xx**3+yy**3+zz**3),G,w)
assert rem==0
assert s.expand(yy+zz)==3*u**3 and s.expand(xx+yy)==v**3
g1=9*u*u+2*w;g2=w*w-6*u;g3=2*u*w+3
assert s.expand(8*u*g1+12*u*u*g2+10*g3-3*g3*g3)==3
r=s.symbols('r')
truncated=3+2*r+r**3/s.Integer(27)
assert s.series(truncated**3-27-18*truncated*r-9*r**3,r,0,4).removeO()==0
parameter=s.series((truncated*r+r**3)/(3+truncated*r),r,0,4)
assert parameter.removeO().coeff(r,1)==1

zeta=QZ(0,1);one=QZ(1);D=one+2*zeta;lam=one-zeta
pi=one+3*zeta
theta_lead=-D/(9*pi)
theta_A0=-lam
ratio_lead=theta_lead/theta_A0
gamma=9*zeta**2
assert ratio_lead==zeta/(9*pi)
assert gamma**3==QZ(729)
assert gamma*ratio_lead==one/pi
gamma_bar=9*zeta
assert gamma.conj()==gamma_bar
assert gamma_bar*ratio_lead.conj()==one/pi.conj()

# Actual Tate isogeny, including its nonunit factor and the original c.
AE=s.Matrix([[1,-3],[3,-2]])
CE=s.Matrix([[1,-1],[0,-1]])
qT=s.diag(1,3)
Atilde=qT.inv()*AE*qT
Ctilde=qT.inv()*CE*qT
assert all(x.q==1 for x in Atilde) and all(x.q==1 for x in Ctilde)
assert qT*Atilde==AE*qT and qT*Ctilde==CE*qT
assert Atilde==s.Matrix([[1,-9],[1,-2]])
assert Ctilde==s.Matrix([[1,-3],[0,-1]])

def mod7(x,z):
    return (int(x.a.numerator)*pow(int(x.a.denominator),-1,7)+
            int(x.b.numerator)*pow(int(x.b.denominator),-1,7)*z)%7
assert mod7(gamma,2)==1 and mod7(gamma_bar,4)==1
def norm_point(P):
    j=next(i for i,a in enumerate(P) if a%7)
    c=pow(P[j],-1,7)
    return tuple(a*c%7 for a in P)
cover7=set();base7=set();pointmap={}
for P in product(range(7),repeat=3):
    if P==(0,0,0):continue
    a,b,c=P
    if (a**3+b**3+c**3)%7==0:base7.add(norm_point(P))
    if (b**3-27*a**3-18*a*b*c-9*c**3)%7==0:
        P=norm_point(P);a,b,c=P
        Q=norm_point((-3*a**3-a*b*c,3*a**3+a*b*c+c**3,-a*b*c-c**3))
        cover7.add(P);pointmap[P]=Q
assert len(cover7)==len(base7)==9
assert all(Q in base7 for Q in pointmap.values())
assert sorted(list(pointmap.values()).count(Q) for Q in set(pointmap.values()))==[3,3,3]

def parseq(text):
    # The exact frame coefficients are stored as two rational coefficients.
    return QZ(text)

# The exact affine-cover subgroup K=ker(l mod3) has rank28.
Vrank=10;Krank=28
pairsN=list(combinations(range(10),2));rowN={p:i for i,p in enumerate(pairsN)}
pairsK=list(combinations(range(28),2));rowK={p:i for i,p in enumerate(pairsK)}
nonb=[0]+list(range(2,10))
namesK=['B=b^3']+[f'b^{j} g{i} b^-{j}' for j in range(3) for i in nonb]
L=s.zeros(10,28);L[1,0]=3
eta=s.zeros(45,28)
for j in range(3):
    for k,i in enumerate(nonb):
        col=1+9*j+k;L[i,col]=1
        lo,hi=sorted((1,i));eta[rowN[lo,hi],col]=j*(1 if 1<i else -1)

W=s.zeros(45,378)
for col,(i,j) in enumerate(pairsK):
    for row,(a,b0) in enumerate(pairsN):
        W[row,col]=L[a,i]*L[b0,j]-L[b0,i]*L[a,j]
chosenK={1:0,**{i:1+k for k,i in enumerate(nonb)}}
selected=[]
for a,b0 in pairsN:
    selected.append(rowK[tuple(sorted((chosenK[a],chosenK[b0])))])
image=W[:,selected]
assert all(image[i,j]==0 for i in range(45) for j in range(45) if i!=j)
diagonal=[int(image[i,i]) for i in range(45)]
assert sorted(abs(x) for x in diagonal)==[1]*36+[3]*9
coeff=image.inv()*W
assert all(x.q==1 for x in coeff)
kernel=[]
for col in range(378):
    if col in selected:continue
    vec={col:1}
    for row,sel in enumerate(selected):
        if coeff[row,col]:vec[sel]=vec.get(sel,0)-int(coeff[row,col])
    assert all(sum(int(W[row,k])*z for k,z in vec.items())==0 for row in range(45))
    kernel.append({'free_column':col,'sparse_entries':[[k,z] for k,z in sorted(vec.items()) if z]})
assert len(kernel)==333

# The actual deck action of b on K/ gamma3 K, including the wrap-around.
perm=[0]+[1+9*((j+1)%3)+k for j in range(3) for k in range(9)]
Pdeck=s.zeros(28)
for i,j in enumerate(perm):Pdeck[j,i]=1
deck_correction=s.zeros(378,28)
for k in range(9):deck_correction[rowK[0,1+k],1+18+k]=1
assert Pdeck**3==s.eye(28) and L*Pdeck==L
def extperm(vector):
    out=s.zeros(378,1)
    for row,(i,j) in enumerate(pairsK):
        a,b0=perm[i],perm[j]
        if a>b0:a,b0=b0,a;sign=-1
        else:sign=1
        out[rowK[a,b0],0]+=sign*vector[row]
    return out
def extembed(vector):
    out=s.zeros(378,1)
    for row,(a,b0) in enumerate(pairsN):
        if vector[row]:
            assert a>=2 and b0>=2
            aa,bb=chosenK[a],chosenK[b0]
            assert aa<bb
            out[rowK[aa,bb]]=vector[row]
    return out

cover_residuals=[];flat_rows=[]
for h in handle['residual_handle_basis']:
    Dmap=s.Matrix(h).applyfunc(s.sympify)
    assert Dmap.shape==(45,10)
    assert Dmap[:,2:10]==s.zeros(45,8)
    da=extembed(Dmap[:,0]);db=extembed(Dmap[:,1])
    lifted=s.zeros(378,28)
    lifted[:,0]=db+extperm(db)+extperm(extperm(db))
    for j in range(3):
        cur=da
        for _ in range(j):cur=extperm(cur)
        lifted[:,1+9*j]=cur
    assert W*lifted==Dmap*L
    assert lifted*Pdeck==s.Matrix.hstack(*(extperm(lifted[:,j]) for j in range(28)))
    cover_residuals.append(lifted)
for row in range(378):
    for col in range(28):
        pair=[int(D[row,col]) for D in cover_residuals]
        if any(pair):flat_rows.append({'central_row':row,'source_column':col,'values':pair})
best=None
for i in range(len(flat_rows)):
    for j in range(i):
        a,b0=flat_rows[i]['values'];c,d=flat_rows[j]['values']
        det=a*d-b0*c
        if det%3:
            best=(i,j,det);break
    if best:break
assert best
i,j,det=best
minor=s.Matrix([flat_rows[i]['values'],flat_rows[j]['values']])
assert minor.det()==det and all(int(x.q)%3 for x in minor.inv())

def matrix(M):return [[str(x) for x in M.row(i)] for i in range(M.rows)]
def sparse(M):
    return [[i,j,str(M[i,j])] for i in range(M.rows) for j in range(M.cols) if M[i,j]]
out={'status':'PASS','scope':'actual cubic-cover source and framed isogeny; homology zero map and surviving augmentation map; no intrinsic arithmetic coefficient assigned',
     'input_sha256':hashes,'cover_equation':str(G),
     'actual_plane_map':[str(xx),str(yy),str(zz)],
     'curve_equation_quotient':str(quot),
     'smoothness_identity':'8u*g1+12u^2*g2+10g3-3g3^2=3',
     'positive_O_point':[1,3,0],'local_parameter':'r=v/u','s_expansion':str(parameter),
     'framed_pi_lift':{'formula':'u -> 9*zeta^2*u^7*theta(Q)/theta(Q-A0)',
                       'gamma':str(gamma),'gamma_cubed':'729','gamma_conjugate':str(gamma_bar),
                       'ratio_leading':str(ratio_lead),'source_leading':str(gamma*ratio_lead),
                       'unit_tangent_transport':'formal path with coefficient pi; its actual Kummer cocycle is retained'},
     'Tate_map':matrix(qT),'Tate_pi':matrix(Atilde),'Tate_c':matrix(Ctilde),
     'reduction_at_pi':{'zeta':2,'gamma':1,'cover_points':[list(P) for P in sorted(cover7)],
                        'base_points':[list(P) for P in sorted(base7)],
                        'point_map':[[list(P),list(pointmap[P])] for P in sorted(pointmap)],
                        'proper_Frobenius':'the framed lift reduces to the seventh-power proper morphism'},
     'source_generators':namesK,'abelian_map':matrix(L),'class2_linear_correction':sparse(eta),
     'central_map_shape':[45,378],'central_map_sparse':sparse(W),
     'central_image_diagonal':diagonal,'central_image_selected_columns':selected,
     'central_image_cokernel_orders':[3]*9,'central_kernel_rank':333,'central_kernel':kernel,
     'deck_permutation':perm,'deck_class2_correction':sparse(deck_correction),
     'H1_residual_map':'zero: all original peripheral generators lie in K and both D images lie in [K,K]',
     'next_augmentation_residual_rows':flat_rows,
     'next_augmentation_unit_minor':{'rows':[flat_rows[i],flat_rows[j]],'determinant':det,
                                       'inverse':matrix(minor.inv())},
     'unresolved':'The framed isogeny and these exact source maps do not yet evaluate the arithmetic action on the next augmentation extension.'}
(base/'a_principal_cubic_cover.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: actual smooth cubic cover, degree-three source map and tangent-normalized pi lift')
print('PASS: both Tate squares, nine actual points and three rational fibres at7')
print('PASS: rank28 Schreier source, rank45 central image, C3^9 cokernel and333 kernel columns')
print('PASS: both residual directions vanish on cover H1 and survive primitively in the next augmentation layer')
print('Residual unit-minor determinant:',det)
