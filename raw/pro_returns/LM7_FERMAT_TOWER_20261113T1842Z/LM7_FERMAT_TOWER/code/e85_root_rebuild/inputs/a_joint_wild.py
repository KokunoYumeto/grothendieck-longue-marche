#!/usr/bin/env python3
"""E80: actual conjugate cubic maps and the descended class-three quotient.

Exact rational Hall arithmetic, a separate finite Hall model, and integer
Smith transformations.  No external binary certificate is an input.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import deque
import hashlib
import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

HERE = Path(__file__).resolve().parent
Z,t,s = sp.symbols("Z t s")


def reduce_z(expression):
    n,d = sp.fraction(sp.cancel(expression))
    return sp.rem(sp.Poly(n,Z),sp.Poly(Z**2+Z+1,Z)).as_expr() == 0


h=(t+1)/(t+Z)
hb=(t+1)/(t+Z**2)
assert reduce_z(hb+Z**2*h/(h+Z))
assert reduce_z((1-h)/(1-hb)+Z*h/hb)
assert reduce_z(h*hb-(t+1)**3/(t**3+1))
H=sp.symbols("H")
ti=(1-Z*H)/(H-1)
assert reduce_z(h.subs(t,ti)-H)
assert reduce_z(hb.subs(t,ti)+Z**2*H/(H+Z))
assert reduce_z((ti+1)**3/(ti**3+1)+Z**2*H**2/(H+Z))
assert reduce_z(h.subs(t,0)-Z**2)
yy=-1-s**3/3+s**6/9
tt=-1+s**3/3-2*s**6/9
hs=sp.series(h.subs(t,tt),s,0,7).removeO()
hbs=sp.series(hb.subs(t,tt),s,0,7).removeO()
assert reduce_z(hs.coeff(s,3)-Z/(1-Z)**3)
assert reduce_z(hbs.coeff(s,3)+Z**2/(1-Z)**3)
assert reduce_z(hs.coeff(s,3)*hbs.coeff(s,3)-sp.Rational(1,27))
assert sp.expand(-(yy+1)/s).coeff(s,2)==sp.Rational(1,3)

ONE=(Q(0),)*5
X=(Q(1),Q(0),Q(0),Q(0),Q(0))
Y=(Q(0),Q(1),Q(0),Q(0),Q(0))
C=(Q(0),Q(0),Q(1),Q(0),Q(0))


def mul(g,h):
    a,b,n,r,s=map(Q,g)
    A,B,N,R,S=map(Q,h)
    return (a+A,b+B,n+N-A*b,
            r+R+b*A*(A+1)/2-A*n,
            s+S+A*b*(b+1)/2-B*n+A*b*B)


def inv(g):
    a,b,n,r,s=map(Q,g)
    return (-a,-b,-n-a*b,
            -r-a*n-a*b*(a-1)/2,
            -s-b*n+a*b*(1-b)/2)


def power(g,n):
    if n<0:
        return power(inv(g),-n)
    out=ONE
    while n:
        if n&1:
            out=mul(out,g)
        g=mul(g,g)
        n//=2
    return out


def comm(g,h):
    return mul(mul(mul(g,h),inv(g)),inv(h))


def alpha(g,chi,k):
    a,b,n,r,s=map(Q,g)
    chi,k=Q(chi),Q(k)
    beta=(chi*chi-1)/24
    return (chi*a,chi*b,k*chi*b+chi**2*n,
            chi*k*(k-1)*b/2+(chi**2*(chi-1)/2+k*chi**2)*n+chi**3*r,
            (chi*beta-k*chi*(chi+1)/2)*b
            -k*chi**2*b*(b-1)/2+chi**2*(chi-1)*n/2+chi**3*s)


def j0(g):
    return alpha(g,-1,0)


def ell(g):
    return g[0]-g[1]


def modq(q,n=3):
    q=Q(q)
    assert q.denominator%3
    return q.numerator*pow(q.denominator,-1,n)%n


def member(g):
    a,b=g
    return ell(a)==ell(b) and modq(a[0]+b[0])==0


def pmul(g,h):
    return mul(g[0],h[0]),mul(g[1],h[1])


def pinv(g):
    return inv(g[0]),inv(g[1])


def pcomm(g,h):
    return pmul(pmul(pmul(g,h),pinv(g)),pinv(h))


def invol(g):
    return j0(g[1]),j0(g[0])


def action(g):
    return alpha(g[0],7,Q(-5,2)),alpha(g[1],7,Q(-1,2))


def action_prime(g):
    return alpha(g[0],7,Q(1,2)),alpha(g[1],7,Q(5,2))


def ppower(g,n):
    return power(g[0],n),power(g[1],n)


def rel(u,a):
    return pmul(pmul(pmul(u,action(a)),pinv(u)),ppower(a,-7))


def f(u,a,k):
    return mul(mul(mul(u,alpha(a,7,k)),inv(u)),power(a,-7))


def gauge(w,g,k):
    return mul(mul(w,g),inv(alpha(w,7,k)))


def conjugate(w,g):
    return mul(mul(w,g),inv(w))


def first_to_pair(u,up,a,ap):
    return (u,j0(up)),(a,j0(ap))


def abpair(L,p,m):
    return ((p,p-L,Q(0),Q(0),Q(0)),
            (3*m-p,3*m-p-L,Q(0),Q(0),Q(0)))


def smith(A):
    dm=DomainMatrix.from_Matrix(A).convert_to(sp.ZZ)
    D,L,R=[x.to_Matrix() for x in smith_normal_decomp(dm)]
    Li,Ri=L.inv(),R.inv()
    assert D==L*A*R and L*Li==sp.eye(L.rows) and R*Ri==sp.eye(R.rows)
    assert all(v.q==1 for v in Li) and all(v.q==1 for v in Ri)
    conv=lambda M:[[int(v) for v in M.row(i)] for i in range(M.rows)]
    return {"matrix":conv(A),"diagonal":[abs(int(D[i,i])) for i in range(min(D.shape))],
            "left":conv(L),"right":conv(R),"left_inverse":conv(Li),"right_inverse":conv(Ri)}


# The integral abelian image and both actual lower-central lattices.
E=sp.Matrix([[0,1,0],[-1,1,0],[0,-1,3],[-1,-1,3]])
CE=sp.Matrix([[0,0,-1,0],[0,0,0,-1],[-1,0,0,0],[0,-1,0,0]])
CJ=sp.Matrix([[-1,0,0],[0,1,-3],[0,0,-1]])
assert CE*E==E*CJ and CJ*CJ==sp.eye(3)
abcolumns=[tuple(E[:,i]) for i in range(3)]
wedgecols=[]
for i in range(3):
    for j in range(i):
        a,b,A,B=abcolumns[i]
        c,d,C0,D=abcolumns[j]
        wedgecols.append(sp.Matrix([a*d-b*c,A*D-B*C0]))
wedge=sp.Matrix.hstack(*wedgecols)
gamma2=smith(wedge)
assert gamma2["diagonal"]==[1,3]

g1=(inv(Y),inv(Y))
g2=(mul(X,Y),mul(inv(X),inv(Y)))
g3=(ONE,mul(power(X,3),power(Y,3)))
g4=(C,ONE)
generators=[g1,g2,g3,g4]
assert all(member(g) for g in generators)
core=pcomm(g1,g2)
central=[pcomm(g4,g1),pcomm(g4,g2),pcomm(core,g1),pcomm(core,g2)]
central_columns=[]
for g in central:
    assert g[0][:3]==g[1][:3]==(0,0,0)
    central_columns.append(sp.Matrix(list(g[0][3:])+list(g[1][3:])))
central_basis=sp.Matrix.hstack(*central_columns)
assert abs(central_basis.det())==1

central_lie=[]
for v in abcolumns:
    a,b,A,B=v
    for r,rr in [(1,-1),(0,3)]:
        central_lie.append(sp.Matrix([a*r,b*r,A*rr,B*rr]))
gamma3matrix=sp.Matrix.hstack(*central_lie)
gamma3=smith(gamma3matrix)
assert gamma3["diagonal"]==[1,1,3,3]
quotient=sp.Matrix([[-1,0,1,0],[-2,1,0,1]])
assert all(int(x)%3==0 for x in quotient*gamma3matrix)
Jcentral=-sp.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
Jtorsion=sp.Matrix([[1,0],[2,-1]])
assert all(int(x)%3==0 for x in quotient*Jcentral-Jtorsion*quotient)
assert quotient.rank()==2


# Independent finite Hall arithmetic, followed by complete generated images.
def finite_mul(g,h,mod,degree):
    a,b,n,r,s=(list(g)+[0]*5)[:5]
    A,B,N,R,S=(list(h)+[0]*5)[:5]
    half=pow(2,-1,mod)
    out=[a+A,b+B,n+N-A*b,
         r+R+b*A*(A+1)*half-A*n,
         s+S+A*b*(b+1)*half-B*n+A*b*B]
    dim={1:2,2:3,3:5}[degree]
    return tuple(v%mod for v in out[:dim])


def finite_pair_mul(g,h,mod,degree):
    return (finite_mul(g[0],h[0],mod,degree),
            finite_mul(g[1],h[1],mod,degree))


finite_records=[]
for degree,mod in [(1,27),(2,9),(3,3)]:
    dim={1:2,2:3,3:5}[degree]
    gens=[tuple(tuple(modq(q,mod) for q in a[:dim]) for a in g)
          for g in generators]
    identity=((0,)*dim,(0,)*dim)
    seen={identity}
    queue=deque([identity])
    while queue:
        g=queue.popleft()
        for v in gens:
            h=finite_pair_mul(g,v,mod,degree)
            if h not in seen:
                assert (h[0][0]-h[0][1]-h[1][0]+h[1][1])%mod==0
                assert (h[0][0]+h[1][0])%3==0
                seen.add(h)
                queue.append(h)
    expected=mod**(2*dim-1)//3
    assert len(seen)==expected
    digest=hashlib.sha256()
    for v in sorted(seen):
        digest.update(bytes(v[0]+v[1]))
    finite_records.append({"class":degree,"modulus":mod,"order":len(seen),
                           "complete_sorted_image_sha256":digest.hexdigest()})
    print("PASS complete finite image",degree,mod,len(seen),flush=True)


# Exact symbolic class-two image in descended abelian coordinates.
La,pa,ma,Lu,pu,mu=sp.symbols("L_a p_a m_a L_u p_u m_u")
A,B,Ap,Bp=pa,pa-La,pa-3*ma,pa-3*ma+La
U,V,Up,Vp=pu,pu-Lu,pu-3*mu,pu-3*mu+Lu
D2=sp.expand(3*(A*B-Ap*Bp)-sp.Rational(5,2)*B-sp.Rational(1,2)*Bp
             +U*B-V*A-Up*Bp+Vp*Ap)
mod3target=La*(pu-1)-Lu*pa
assert all(int(c)%3==0 for c in sp.Poly(2*(D2-mod3target),La,pa,ma,Lu,pu,mu).coeffs())

arithmetic_checks=normalization_checks=class2_examples=class3_examples=0
for i in range(240):
    pars=[Q(((i*(j+2)+j*j)%17)-8,2 if (i+j)%3==0 else 1)
          for j in range(6)]
    La0,pa0,ma0,Lu0,pu0,mu0=pars
    aa=abpair(La0,pa0,ma0)
    uu=abpair(Lu0,pu0,mu0)
    aa=tuple(tuple(list(g[:2])+[Q((i+2*j)%7-3),Q(i%5),Q(j-1)])
             for j,g in enumerate(aa))
    uu=tuple(tuple(list(g[:2])+[Q((2*i+j)%11-5),Q(j+2),Q(i%7)])
             for j,g in enumerate(uu))
    assert member(aa) and member(uu)
    assert invol(invol(aa))==aa
    assert invol(action(invol(aa)))==action_prime(aa)
    assert member(action(aa)) and member(invol(aa))
    assert invol(pmul(aa,uu))==pmul(invol(aa),invol(uu))
    arithmetic_checks+=5

    u,up=uu[0],j0(uu[1])
    a,ap=aa[0],j0(aa[1])
    assert ell(u)+ell(up)==ell(a)+ell(ap)==0
    assert modq(u[0]-up[0])==modq(a[0]-ap[0])==0
    w=(Q(i%7-3),Q((i*3)%11-5),Q(i%5),Q(2),Q(-1))
    gu,gup=gauge(w,u,Q(-5,2)),gauge(w,up,Q(1,2))
    ga,gap=conjugate(w,a),conjugate(w,ap)
    total=ell(gu)+ell(gup)
    assert total==-12*ell(w) and modq(total)==0
    correction=(total/12,Q(0),Q(0),Q(0),Q(0))
    nu,nup=gauge(correction,gu,Q(-5,2)),gauge(correction,gup,Q(1,2))
    na,nap=conjugate(correction,ga),conjugate(correction,gap)
    combined=mul(correction,w)
    assert ell(combined)==0
    assert (nu,nup,na,nap)==(
        gauge(combined,u,Q(-5,2)),gauge(combined,up,Q(1,2)),
        conjugate(combined,a),conjugate(combined,ap))
    assert all(member(v) for v in first_to_pair(nu,nup,na,nap))
    fixed=(combined,j0(combined))
    assert member(fixed) and invol(fixed)==fixed
    normalization_checks+=1

    # Build actual class-two sections from the six descended abelian values.
    u=(u[0],u[1],Q(i%5-2),Q(0),Q(0))
    up=(up[0],up[1],Q((i*2)%7-3),Q(0),Q(0))
    a=(a[0],a[1],Q(0),Q(0),Q(0))
    ap=(ap[0],ap[1],Q(0),Q(0),Q(0))
    defect=(f(u,a,Q(-5,2))[2]-f(up,ap,Q(1,2))[2])/7
    assert modq(defect)==modq(La0*(pu0-1)-Lu0*pa0)
    if modq(defect):
        continue
    a=(a[0],a[1],-defect/6,Q(0),Q(0))
    uj,aj=first_to_pair(u,up,a,ap)
    v=rel(uj,aj)
    assert v[0][:3]==j0(v[1])[:3]
    class2_examples+=1
    delta=mul(f(u,a,Q(-5,2)),inv(f(up,ap,Q(1,2))))
    assert delta[:3]==(0,0,0)
    if modq(delta[3]) or modq(delta[4]):
        continue
    a=(a[0],a[1],a[2],-delta[3]/336,-delta[4]/336)
    uj,aj=first_to_pair(u,up,a,ap)
    assert member(uj) and member(aj)
    v=rel(uj,aj)
    assert invol(v)==v
    class3_examples+=1

assert class2_examples and class3_examples

# A descended two-parameter family: both positive and obstructed cases.
family_records=[]
for n in range(6):
    for m in range(6):
        u=(Q(5,2),Q(0),Q(n),Q(0),Q(0))
        up=(Q(-1,2),Q(2),Q(m),Q(0),Q(0))
        a=Y
        ap=inv(Y)
        uj,aj=first_to_pair(u,up,a,ap)
        assert member(uj) and member(aj)
        delta=mul(f(u,a,Q(-5,2)),inv(f(up,ap,Q(1,2))))
        assert delta==(0,0,0,0,7*(5-n-m))
        if (n+m-2)%3==0:
            a=(0,1,0,0,Q(n+m-5,48))
            uj,aj=first_to_pair(u,up,a,ap)
            assert rel(uj,aj)==invol(rel(uj,aj))
        family_records.append({"N":n,"M":m,"error_e":7*(5-n-m),
                               "lifts":(n+m-2)%3==0})

result={
 "statement":"E.80","status":"PASS",
 "geometric_identities_checked":11,
 "actual_cover":"v^3=h*hbar=-zeta^2*h^2/(h+zeta), v=-(x+y)/z",
 "joint_image":"ell(f)=ell(g), X(f)+X(g) in3Z3",
 "abelian_lattice_matrix":[list(map(int,E.row(i))) for i in range(E.rows)],
 "abelian_involution":[list(map(int,CJ.row(i))) for i in range(CJ.rows)],
 "gamma2_coordinate_Smith":gamma2,
 "all_four_central_directions_in_gamma2":{
     "matrix":[list(map(int,central_basis.row(i))) for i in range(4)],
     "inverse":[list(map(int,central_basis.inv().row(i))) for i in range(4)],
     "determinant":int(central_basis.det())},
 "gamma3_coordinate_Smith":gamma3,
 "gamma3_quotient_map_mod3":[list(map(int,quotient.row(i))) for i in range(2)],
 "gamma3_quotient_involution_mod3":[list(map(int,Jtorsion.row(i))) for i in range(2)],
 "finite_complete_images":finite_records,
 "class_two_abelian_error":str(D2),
 "class_two_image_mod3":"L_a*(p_u-1)-L_u*p_a=0",
 "arithmetic_action_checks":arithmetic_checks,
 "actual_restriction_normalization_inverse_checks":normalization_checks,
 "descended_class_two_sections":class2_examples,
 "descended_class_three_lifts":class3_examples,
 "descended_family":family_records,
 "H1_Q3_J1":"Z3^5 x C3",
 "J2_over_J1_nonempty_fibres":"Z3^2 x C3",
 "J3_over_J2_nonempty_fibres":"Z3^4 x C9^2",
 "intrinsic_gamma3_index_in_product_central_kernel":9
}
HERE.joinpath("a_joint_wild.json").write_text(json.dumps(result,indent=2)+"\n")
print("PASS exact scheme and tangent identities")
print("PASS both integer Smith maps and inverses")
print("PASS",arithmetic_checks,"arithmetic action identities")
print("PASS",normalization_checks,"restriction normalization maps and inverse gauges")
print("PASS",class2_examples,"descended class-two sections and",
      class3_examples,"class-three lifts")
print("PASS all36 descended family cases")
print("ALL PASS")
