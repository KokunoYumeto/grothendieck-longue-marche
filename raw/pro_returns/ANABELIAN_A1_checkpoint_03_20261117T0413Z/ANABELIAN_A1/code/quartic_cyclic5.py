"""Exact cyclic-five covers of C/F_3: w^4=x^3-x, P=infinity.

Use an explicit Velu isogeny to pull back C -> E, then compute the
Cartier operator on all eleven regular differentials.  All output
field elements use base-three little-endian polynomial encoding.
Requires python-flint 0.9.0.  No point-count heuristic is used.
"""
from pathlib import Path
import json, random, time
from flint import fq_default_ctx, fq_default_poly_ctx

started=time.time()
k=fq_default_ctx(3,8,"z"); R=fq_default_poly_ctx(k); x=R.gen()
q=3**8; one=k(1); zero=k(0); f=x**3-x
rng=random.Random(202611170235)
def el(n): return k([(n//3**j)%3 for j in range(8)])
def enc(a): return sum(int(c)*3**j for j,c in enumerate(a.to_list()))
def ep(a): return [enc(c) for c in a.coeffs()]
def em(A): return [[enc(a) for a in row] for row in A]
def eccheck(P): return P is None or P[1]**2 == P[0]**3-P[0]
def ecadd(P,Q):
    if P is None:return Q
    if Q is None:return P
    a,b=P; c,d=Q
    if a==c:
        if b==-d:return None
        m=(-one)/(2*b)
    else:m=(d-b)/(c-a)
    u=m*m-a-c;v=m*(a-u)-b
    ans=(u,v);assert eccheck(ans);return ans
def ecmul(n,P):
    ans=None
    while n:
        if n&1:ans=ecadd(ans,P)
        P=ecadd(P,P);n//=2
    return ans
def ec5():
    while True:
        a=el(rng.randrange(q));b=a**3-a
        if not b.is_square():continue
        P=ecmul(16,(a,b.sqrt()))
        if P is not None:
            assert ecmul(5,P) is None;return P
def mm(A,B):
    return [[sum((a*b for a,b in zip(row,col)),zero) for col in zip(*B)] for row in A]
def eye(n):return [[one if i==j else zero for j in range(n)] for i in range(n)]
def mpow(A,e):return [[a**e for a in row] for row in A]
def det(A):
    A=[row[:] for row in A];d=one;n=len(A)
    for j in range(n):
        pivot=next((i for i in range(j,n) if not A[i][j].is_zero()),None)
        if pivot is None:return zero
        if pivot!=j:A[j],A[pivot]=A[pivot],A[j];d=-d
        v=A[j][j];d*=v
        for i in range(j+1,n):
            if not A[i][j].is_zero():
                c=A[i][j]/v
                for h in range(j,n):A[i][h]-=c*A[j][h]
    return d
def rank(A):
    A=[row[:] for row in A];r=0
    for j in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if not A[i][j].is_zero()),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r];v=A[r][j]
        for i in range(r+1,len(A)):
            if not A[i][j].is_zero():
                c=A[i][j]/v
                for h in range(j,len(A[0])):A[i][h]-=c*A[r][h]
        r+=1
    return r
def charpoly(A):
    # Fraction-free Bareiss over k[X], with an independent determinant check.
    n=len(A);B=[[(x if i==j else R(0))-R(A[i][j]) for j in range(n)] for i in range(n)]
    prev=R(1);sgn=one
    for j in range(n-1):
        pivot=next(i for i in range(j,n) if B[i][j])
        if pivot!=j:B[j],B[pivot]=B[pivot],B[j];sgn=-sgn
        v=B[j][j]
        for i in range(j+1,n):
            for h in range(j+1,n):
                num=B[i][h]*v-B[i][j]*B[j][h]
                val,rem=num.divmod(prev);assert not rem;B[i][h]=val
            B[i][j]=R(0)
        prev=v
    cp=B[-1][-1]*sgn
    assert cp(one)==det([[one-A[i][j] if i==j else -A[i][j] for j in range(n)] for i in range(n)])
    return cp
def cartier(F,hfactor,basis):
    # basis entries (s,j): hfactor[s]*x^j dx/w^s.
    n=len(basis);M=[[zero for j in range(n)] for i in range(n)]
    for j,(s,a) in enumerate(basis):
        t=(3*s)%4; power=(3*t-s)//4
        H=hfactor[s]*x**a*F**power
        C=R([H[3*b+2].pth_root() for b in range(max(0,(H.degree()-2)//3+1))])
        C,rem=C.divmod(hfactor[t]);assert not rem
        for i,(ss,b) in enumerate(basis):
            if ss==t:M[i][j]=C[b]
        assert all(C[b]==0 for b in range(C.degree()+1) if (t,b) not in basis)
    return M

# C is a smooth plane quartic w^4=x^3 z-x z^3; the partials -z^3,
# w^3, x^3 have no common projective zero.  It has unique infinity.
basebasis=[(2,0),(3,0),(3,1)]
basecartier=cartier(f,{1:R(1),2:R(1),3:R(1)},basebasis)
assert all(a.is_zero() for row in basecartier for a in row)

P=ec5();line={enc(ecmul(i,P)[0])*q+enc(ecmul(i,P)[1]) for i in range(1,5)}
while True:
    Q=ec5()
    if enc(Q[0])*q+enc(Q[1]) not in line:break
kernels=[P]+[ecadd(Q,ecmul(i,P)) for i in range(5)]
records=[]
for kernel in kernels:
    T=ecmul(2,kernel);a,b=kernel;c,d=T
    h=(x-a)*(x-c);h2=h*h
    N=x*h2
    for u,v in [kernel,T]:
        lin=x-u
        N+=h2.exact_division(lin)+h2.exact_division(lin**2)*(v*v)
    g=N.derivative()*h-2*N*h.derivative()
    diff=f*g*g-N**3
    aa=diff[13];bb=(diff-aa*N*h**4)[12]
    assert diff==aa*N*h**4+bb*h**6
    roots_s=(x**4+aa).roots();roots_r=(x**3+aa*x+bb).roots()
    assert roots_s and roots_r
    scale=min((v for v,m in roots_s),key=enc);shift=min((v for v,m in roots_r),key=enc)
    assert scale**4==-aa and shift**3+aa*shift+bb==0
    F=f*g*g*h*h/(scale**6)
    assert F.degree()==19
    assert f.is_squarefree() and g.is_squarefree() and h.is_squarefree()
    assert f.gcd(g)==1 and f.gcd(h)==1 and g.gcd(h)==1
    hf={1:R(1),2:g*h,3:g*h}
    basis=[(1,j) for j in range(4)]+[(2,0)]+[(3,j) for j in range(6)]
    M=cartier(F,hf,basis)
    Aq=eye(11)
    for j in range(8):Aq=mm(M,mpow(Aq,3**7))
    cp=charpoly(Aq);v=cp(one)
    assert all(c**3==c for c in cp.coeffs())
    B=eye(11);ranks=[]
    for j in range(12):B=mm(Aq,B);ranks.append(rank(B))
    assert all(P[0]**(3**j)!=P[0] or P[1]**(3**j)!=P[1] for j in [1,2,4])
    rec={"kernel_generator":[enc(a),enc(b)],"kernel_second":[enc(c),enc(d)],
         "source_E":"y^2=x^3-x","target_E_coefficients":[enc(aa),enc(bb)],
         "h":ep(h),"N":ep(N),"g":ep(g),"scale":enc(scale),"shift":enc(shift),
         "cover_polynomial_F":ep(F),"cover_equation":"w^4=F(x)","basis":basis,
         "map_to_C":"X=(N/h^2-shift)/scale^2, W=w/h^2",
         "Cartier_matrix":em(M),"Cartier_eighth_power":em(Aq),
         "Frobenius_characteristic_polynomial_mod_3":ep(cp),
         "det_one_minus_Frobenius_mod_3":enc(v),"p_rank":ranks[-1],
         "power_ranks":ranks,"relative_class_number_prime_to_3":not v.is_zero()}
    records.append(rec)
    print(json.dumps({"kernel":rec["kernel_generator"],"charpoly":ep(cp),"det":enc(v),"p_rank":ranks[-1]}),flush=True)
out={"field":{"p":3,"degree":8,"order":q,"modulus":list(map(int,k.modulus()))},
     "curve":"W^4=X^3 Z-X Z^3","point":[1,0,0],
     "affine_curve":"W^4=X^3-X","base_Cartier_matrix":em(basecartier),
     "ell":5,"constant_degree":8,"E5_basis":[[enc(v) for v in P],[enc(v) for v in Q]],
     "covers":records,"seconds":time.time()-started}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("completed",len(records),"covers; good:",sum(r["relative_class_number_prime_to_3"] for r in records),"seconds",out["seconds"],flush=True)
