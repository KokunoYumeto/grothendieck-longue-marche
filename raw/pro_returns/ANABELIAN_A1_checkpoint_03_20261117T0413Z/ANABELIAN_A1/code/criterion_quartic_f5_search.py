"""Exact dual-isogeny witnesses for W^4=X^3-X in characteristic five.
Usage: python criterion_quartic_f5_search.py [odd_prime_ell]
All finite data and complete Cartier matrices are saved, whether the
selected elliptic-pullback family succeeds or fails.
"""
from pathlib import Path
import json, random, sys, time
from flint import fq_default_ctx, fq_default_poly_ctx

START=time.monotonic();ROOT=Path(__file__).resolve().parent
ell=int(sys.argv[1]) if len(sys.argv)>1 else 7
assert ell>2 and ell!=5 and all(ell%d for d in range(2,int(ell**.5)+1))
p=5;trace=-2

def mm_mod(A,B):
    return [[sum(A[i][h]*B[h][j] for h in range(2))%ell for j in range(2)] for i in range(2)]
companion=[[0,-p%ell],[1,trace%ell]];I2=[[1,0],[0,1]]
prod=I2;degree=0
while True:
    prod=mm_mod(prod,companion);degree+=1
    if prod==I2:break
assert degree<ell**4
q=p**degree
s0,s1=2,trace
for j in range(2,degree+1):s0,s1=s1,trace*s1-p*s0
N=q+1-s1
val=0;cofactor=N
while cofactor%ell==0:cofactor//=ell;val+=1
assert val==2,(ell,degree,val)
k=fq_default_ctx(p,degree,"z",fq_type="FQ_NMOD")
R=fq_default_poly_ctx(k);x=R.gen();one=k.one();zero=k.zero()
random_source=random.Random(20261117+ell)
print(json.dumps({"ell":ell,"field_degree":degree,"field_modulus":list(map(int,k.modulus())),"E_order":N,"ell_valuation":val}),flush=True)

def dec(n):return k([(n//p**i)%p for i in range(degree)])
def enc(a):return sum(int(c)*p**i for i,c in enumerate(a.to_list()))
def ep(F):return [enc(a) for a in F]
def em(A):return [[enc(a) for a in row] for row in A]
def on_curve(P,A,B):return P is None or P[1]**2==P[0]**3+A*P[0]+B
def add(P,Q,A):
    if P is None:return Q
    if Q is None:return P
    a,b=P;c,d=Q
    if a==c and b+d==0:return None
    slope=(d-b)/(c-a) if a!=c else (3*a*a+A)/(2*b)
    X=slope*slope-a-c;Y=-b+slope*(a-X)
    return X,Y
def mul(n,P,A):
    Q=None
    while n:
        if n&1:Q=add(Q,P,A)
        P=add(P,P,A);n>>=1
    return Q
def torsion():
    while True:
        X=dec(random_source.randrange(q));rhs=X**3-X
        if not rhs.is_square():continue
        P=mul(cofactor,(X,rhs.sqrt()),-one)
        if P is not None:
            assert on_curve(P,-one,zero) and mul(ell,P,-one) is None
            return P

P=torsion();Pline={tuple(map(enc,mul(i,P,-one))) for i in range(1,ell)}
while True:
    Q=torsion()
    if tuple(map(enc,Q)) not in Pline:break
generators=[P]+[add(Q,mul(i,P,-one),-one) for i in range(ell)]

def velu(A,B,K):
    pairs=[mul(i,K,A) for i in range(1,(ell+1)//2)]
    assert all(on_curve(T,A,B) for T in pairs)
    h=R.one()
    for a,b in pairs:h*=x-a
    N=x*h*h
    for a,b in pairs:
        N+=2*(3*a*a+A)*(h*h).exact_division(x-a)+4*b*b*(h*h).exact_division((x-a)**2)
    g=N.derivative()*h-2*N*h.derivative()
    delta=(x**3+A*x+B)*g*g-N**3
    m=(ell-1)//2
    AA=delta[6*m+1];BB=(delta-AA*N*h**4)[6*m]
    assert delta==AA*N*h**4+BB*h**6
    assert N.gcd(h)==1
    return AA,BB,h,N,g
def image(P,h,N,g):
    a,b=P;v=h(a)
    if v==0:return None
    return N(a)/(v*v),b*g(a)/(v**3)
def eye(n):return [[one if i==j else zero for j in range(n)] for i in range(n)]
def mm(A,B):return [[sum((A[i][h]*B[h][j] for h in range(len(B))),zero) for j in range(len(B[0]))] for i in range(len(A))]
def characteristic(A):
    n=len(A)
    if not n:return R.one()
    B=[row[1:] for row in A[1:]];cp=characteristic(B);ans=(x-A[0][0])*cp
    if n==1:return ans
    row=A[0][1:];col=[A[i][0] for i in range(1,n)];moments=[]
    for j in range(n-1):
        moments.append(sum((a*b for a,b in zip(row,col)),zero))
        col=[sum((a*b for a,b in zip(r,col)),zero) for r in B]
    for j in range(n-1):
        value=sum((cp[n-1-h]*moments[j-h] for h in range(j+1)),zero)
        ans-=R([zero]*(n-2-j)+[value])
    return ans
def cartier(F,factors,basis):
    M=[[zero for _ in basis] for _ in basis]
    for j,(s,a) in enumerate(basis):
        H=factors[s]*x**a*F**s
        coeffs=[H[b].pth_root() for b in range(p-1,H.degree()+1,p)]
        C,rem=divmod(R(coeffs),factors[s]);assert rem==0
        for i,(ss,b) in enumerate(basis):
            if ss==s:M[i][j]=C[b]
        assert C==sum((R([M[i][j]])*x**b for i,(ss,b) in enumerate(basis) if ss==s),R.zero())
    return M
def linear_power(M):
    A=eye(len(M))
    for j in range(degree):
        conjugated=[[a**(p**((-j)%degree)) for a in row] for row in M]
        A=mm(A,conjugated)
    return A

basebasis=[(2,0),(3,0),(3,1)]
baseM=cartier(x**3-x,{s:R.one() for s in (1,2,3)},basebasis)
baseA=linear_power(baseM);basecp=characteristic(baseA)
records=[]
for index,K in enumerate(generators):
    A1,B1,h1,N1,g1=velu(-one,zero,K)
    independent=Q if tuple(map(enc,K)) in Pline else P
    K2=image(independent,h1,N1,g1);assert K2 is not None
    assert on_curve(K2,A1,B1) and mul(ell,K2,A1) is None
    A2,B2,h,N,g=velu(A1,B1,K2)
    assert A2==-one*k(ell)**4 and B2==0
    cubic=x**3+A1*x+B1
    F=cubic*g*g*h*h/(k(ell)**6)
    assert F.degree()==4*ell-1
    assert all(a.is_squarefree() for a in (cubic,g,h))
    assert cubic.gcd(g)==cubic.gcd(h)==g.gcd(h)==1
    assert F==(N**3*h*h-k(ell)**4*N*h**6)/(k(ell)**6)
    basis=[(1,j) for j in range(ell-1)]+[(2,0)]+[(3,j) for j in range(ell+1)]
    M=cartier(F,{1:R.one(),2:g*h,3:g*h},basis)
    A=linear_power(M);cp=characteristic(A);new,rem=divmod(cp,basecp);assert rem==0
    assert all(a**p==a for a in cp)
    value=new(one);prank=len(basis)-next(i for i,a in enumerate(cp) if a!=0)
    record={"index":index,"initial_kernel":[enc(a) for a in K],
            "isogenous_E_coefficients":[enc(A1),enc(B1)],"dual_kernel":[enc(a) for a in K2],
            "forward_h":ep(h1),"forward_N":ep(N1),"forward_g":ep(g1),
            "h":ep(h),"N":ep(N),"g":ep(g),"F":ep(F),"basis":basis,
            "cover_equation":"w^4=F(x)","map_to_C":f"X=N/({ell}^2*h^2), W=w/h^2",
            "Cartier_matrix":em(M),"Cartier_linear_power":em(A),
            "full_characteristic_polynomial_mod_5":ep(cp),"new_characteristic_polynomial_mod_5":ep(new),
            "relative_class_number_mod_5":enc(value),"p_rank":prank,
            "relative_class_number_prime_to_5":value!=0}
    records.append(record)
    print(json.dumps({"ell":ell,"index":index,"new_charpoly":ep(new),"det":enc(value),"p_rank":prank,"seconds":time.monotonic()-START}),flush=True)
    out={"field":{"p":p,"degree":degree,"order":q,"modulus":list(map(int,k.modulus()))},
         "curve":"W^4=X^3 Z-X Z^3","affine_curve":"W^4=X^3-X","point":[1,0,0],
         "ell":ell,"constant_degree":degree,"E_order":N if isinstance(N,int) else q+1-s1,
         "E_basis":[[enc(a) for a in P],[enc(a) for a in Q]],
         "base_Cartier_matrix":em(baseM),"base_Cartier_linear_power":em(baseA),
         "base_characteristic_polynomial_mod_5":ep(basecp),"covers":records,
         "seconds":time.monotonic()-START}
    (ROOT/f"criterion_quartic_f5_ell{ell}.json").write_text(json.dumps(out,indent=2)+"\n")
print("COMPLETED",len(records),"COVERS; GOOD",sum(r["relative_class_number_prime_to_5"] for r in records),flush=True)
