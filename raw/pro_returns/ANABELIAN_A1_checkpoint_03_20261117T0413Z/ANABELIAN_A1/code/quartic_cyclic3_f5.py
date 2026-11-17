"""Exact cyclic-three pullbacks for the plane quartic w^4=x^3-x over F5.

The dual of each of the four 3-isogenies out of E:y^2=x^3-x is
used, so no claim that an ordinary isogenous elliptic curve is
isomorphic to E is needed. Cartier data are computed on the entire
genus-seven cover, with the old factor divided as a polynomial.
"""
from pathlib import Path
import json,time
from flint import fq_default_ctx,fq_default_poly_ctx
start=time.time();p=5;nfield=8;q=p**nfield
k=fq_default_ctx(p,nfield,"z");R=fq_default_poly_ctx(k);x=R.gen()
zero=k(0);one=k(1)
def enc(a):return sum(int(c)*p**j for j,c in enumerate(a.to_list()))
def ep(a):return [enc(c) for c in a.coeffs()]
def em(A):return [[enc(a) for a in row] for row in A]
def ecadd(P,Q,A):
    if P is None:return Q
    if Q is None:return P
    a,b=P;c,d=Q
    if a==c:
        if b==-d:return None
        m=(3*a*a+A)/(2*b)
    else:m=(d-b)/(c-a)
    u=m*m-a-c;v=m*(a-u)-b;return (u,v)
def velu(A,B,K):
    a,b=K;h=x-a;N=x*h*h+2*(3*a*a+A)*h+4*b*b
    g=N.derivative()*h-2*N*h.derivative();f=x**3+A*x+B
    diff=f*g*g-N**3;aa=diff[7];bb=(diff-aa*N*h**4)[6]
    assert diff==aa*N*h**4+bb*h**6
    return aa,bb,h,N,g
def image_isogeny(P,h,N,g):
    a,b=P;v=h(a)
    if v==0:return None
    return (N(a)/(v*v),b*g(a)/(v**3))
def eye(n):return [[one if i==j else zero for j in range(n)] for i in range(n)]
def mm(A,B):return [[sum((a*b for a,b in zip(row,col)),zero) for col in zip(*B)] for row in A]
def mpow(A,e):return [[a**e for a in row] for row in A]
def det(A):
    A=[row[:] for row in A];ans=one;n=len(A)
    for j in range(n):
        s=next((i for i in range(j,n) if A[i][j]!=0),None)
        if s is None:return zero
        if s!=j:A[j],A[s]=A[s],A[j];ans=-ans
        u=A[j][j];ans*=u
        for i in range(j+1,n):
            v=A[i][j]/u
            for h in range(j,n):A[i][h]-=v*A[j][h]
    return ans
def charpoly(A):
    n=len(A);B=[[(x if i==j else R(0))-A[i][j] for j in range(n)] for i in range(n)]
    prev=R(1);sgn=one
    for j in range(n-1):
        s=next(i for i in range(j,n) if B[i][j])
        if s!=j:B[j],B[s]=B[s],B[j];sgn=-sgn
        u=B[j][j]
        for i in range(j+1,n):
            for h in range(j+1,n):
                v,r=(B[i][h]*u-B[i][j]*B[j][h]).divmod(prev);assert not r;B[i][h]=v
            B[i][j]=R(0)
        prev=u
    ans=B[-1][-1]*sgn
    assert ans(one)==det([[one-A[i][j] if i==j else -A[i][j] for j in range(n)] for i in range(n)])
    return ans
def cartier(F,hfactor,basis):
    n=len(basis);M=[[zero for j in range(n)] for i in range(n)]
    for j,(s,a) in enumerate(basis):
        t=s;power=s
        H=hfactor[s]*x**a*F**power
        C=R([H[p*b+p-1].pth_root() for b in range(max(0,(H.degree()-(p-1))//p+1))])
        C,rem=C.divmod(hfactor[t]);assert not rem
        for i,(ss,b) in enumerate(basis):
            if ss==t:M[i][j]=C[b]
        assert all(C[b]==0 for b in range(C.degree()+1) if (t,b) not in basis)
    return M
def linear_power(M):
    A=eye(len(M))
    for j in range(nfield):A=mm(M,mpow(A,p**(nfield-1)))
    return A
A=-one;B=zero;f=x**3-x
torsion_x=[a for a,m in (3*x**4+6*A*x*x-A*A).roots()]
assert len(torsion_x)==4
torsion=[(a,(a**3-a).sqrt()) for a in sorted(torsion_x,key=enc)]
for T in torsion:assert ecadd(ecadd(T,T,A),T,A) is None
basebasis=[(2,0),(3,0),(3,1)]
baseM=cartier(f,{1:R(1),2:R(1),3:R(1)},basebasis)
baseq=linear_power(baseM);basecp=charpoly(baseq)
assert basecp==(x-1)**3
recs=[]
for K in torsion:
    A1,B1,h1,N1,g1=velu(A,B,K)
    other=next(T for T in torsion if T[0]!=K[0]);K2=image_isogeny(other,h1,N1,g1)
    assert K2[1]**2==K2[0]**3+A1*K2[0]+B1
    assert ecadd(ecadd(K2,K2,A1),K2,A1) is None
    A2,B2,h2,N2,g2=velu(A1,B1,K2)
    assert A2==A*3**4 and B2==B*3**6
    F=(x**3+A1*x+B1)*g2*g2*h2*h2/(k(3)**6)
    assert F.degree()==11
    assert all(H.is_squarefree() for H in [x**3+A1*x+B1,g2,h2])
    assert (x**3+A1*x+B1).gcd(g2)==1 and (x**3+A1*x+B1).gcd(h2)==1 and g2.gcd(h2)==1
    basis=[(1,j) for j in range(2)]+[(2,0)]+[(3,j) for j in range(4)]
    M=cartier(F,{1:R(1),2:g2*h2,3:g2*h2},basis);Mq=linear_power(M)
    cp=charpoly(Mq);new,rem=cp.divmod(basecp);assert not rem
    assert all(c**p==c for c in new.coeffs())
    value=new(one)
    rec={"initial_kernel":[enc(a) for a in K],"isogenous_E_coefficients":[enc(A1),enc(B1)],
         "dual_kernel":[enc(a) for a in K2],"forward_h":ep(h1),"forward_N":ep(N1),"forward_g":ep(g1),
         "h":ep(h2),"N":ep(N2),"g":ep(g2),"F":ep(F),"cover_equation":"w^4=F(x)",
         "map_to_C":"X=N/(9*h^2), W=w/h^2","basis":basis,"Cartier_matrix":em(M),
         "Cartier_eighth_power":em(Mq),"Frobenius_characteristic_polynomial_mod_5":ep(cp),
         "new_Frobenius_characteristic_polynomial_mod_5":ep(new),
         "relative_class_number_mod_5":enc(value),"relative_class_number_prime_to_5":value!=0}
    recs.append(rec);print(json.dumps({"kernel":rec["initial_kernel"],"new_charpoly":ep(new),"det":enc(value)}),flush=True)
out={"field":{"p":p,"degree":nfield,"order":q,"modulus":list(map(int,k.modulus()))},
     "curve":"W^4=X^3 Z-X Z^3","affine_curve":"W^4=X^3-X","point":[1,0,0],
     "ell":3,"constant_degree":8,"base_Cartier_matrix":em(baseM),"base_Cartier_eighth_power":em(baseq),
     "base_Frobenius_characteristic_polynomial_mod_5":ep(basecp),"covers":recs,"seconds":time.time()-start}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("complete",len(recs),"covers, good",sum(z["relative_class_number_prime_to_5"] for z in recs),"seconds",out["seconds"])
