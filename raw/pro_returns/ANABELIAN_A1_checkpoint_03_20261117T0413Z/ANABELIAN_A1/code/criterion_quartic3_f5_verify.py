"""Independent exact verification of the four F5 quartic cubic pullbacks.
No producer code is imported.  Characteristic polynomials use recursive
adjugates, and the eighth Cartier iterate is a direct conjugate product.
"""
from pathlib import Path
from hashlib import sha256
import json
from flint import fq_default_ctx, fq_default_poly_ctx, fmpz_mod_poly_ctx

ROOT = Path(__file__).resolve().parent
raw = (ROOT/"quartic_cyclic3_f5.json").read_bytes()
data = json.loads(raw)
assert data["field"]["p"] == 5 and data["field"]["degree"] == 8
P = fmpz_mod_poly_ctx(5)
mod = P(data["field"]["modulus"])
z = P.gen()
assert z.pow_mod(5**8, mod) == z
assert (z.pow_mod(5**4, mod)-z).gcd(mod) == 1
k = fq_default_ctx(modulus=mod, var="z", fq_type="FQ_NMOD")
R = fq_default_poly_ctx(k)
x, one, zero = R.gen(), k.one(), k.zero()

def dec(n):
    assert isinstance(n, int) and 0 <= n < 5**8
    return k([(n//5**j) % 5 for j in range(8)])

def enc(a):
    return sum(int(c)*5**j for j,c in enumerate(a.to_list()))

def pol(values):
    return R([dec(a) for a in values])

def mat(values):
    return [[dec(a) for a in row] for row in values]

def eye(n):
    return [[one if i == j else zero for j in range(n)] for i in range(n)]

def mm(A, B):
    return [[sum((A[i][h]*B[h][j] for h in range(len(B))), zero)
             for j in range(len(B[0]))] for i in range(len(A))]

def charpoly(A):
    n = len(A)
    if not n:
        return R.one()
    B = [row[1:] for row in A[1:]]
    cp = charpoly(B)
    ans = (x-A[0][0])*cp
    if n == 1:
        return ans
    row, col = A[0][1:], [A[i][0] for i in range(1,n)]
    moments = []
    for j in range(n-1):
        moments.append(sum((a*b for a,b in zip(row,col)), zero))
        col = [sum((a*b for a,b in zip(r,col)), zero) for r in B]
    for j in range(n-1):
        value = sum((cp[n-1-h]*moments[j-h] for h in range(j+1)),zero)
        ans -= R([zero]*(n-2-j)+[value])
    return ans

def ecadd(P,Q,A):
    if P is None:return Q
    if Q is None:return P
    a,b=P;c,d=Q
    if a==c and b+d==0:return None
    slope=(d-b)/(c-a) if a!=c else (3*a*a+A)/(2*b)
    X=slope*slope-a-c;Y=-b+slope*(a-X)
    return X,Y

def check_isogeny(A,B,point,h,N,g):
    a,b=point
    assert b*b==a**3+A*a+B
    assert ecadd(ecadd(point,point,A),point,A) is None
    assert h==x-a
    assert N==x*h*h+2*(3*a*a+A)*h+4*b*b
    assert g==N.derivative()*h-2*N*h.derivative()
    assert N.gcd(h)==1
    diff=(x**3+A*x+B)*g*g-N**3
    AA=diff[7]
    BB=(diff-AA*N*h**4)[6]
    assert diff==AA*N*h**4+BB*h**6
    return AA,BB

def cartier(F,factors,basis):
    M=[[zero for _ in basis] for _ in basis]
    for j,(s,a) in enumerate(basis):
        target=next(t for t in (1,2,3) if (5*t-s)%4==0)
        power=(5*target-s)//4
        H=factors[s]*x**a*F**power
        coeffs=[H[b]**(5**7) for b in range(4,H.degree()+1,5)]
        C,rem=divmod(R(coeffs),factors[target])
        assert rem==0
        rebuilt=R.zero()
        for i,(ss,b) in enumerate(basis):
            if ss==target:
                M[i][j]=C[b];rebuilt+=R([C[b]])*x**b
        assert rebuilt==C
    return M

def eighth(M):
    A=eye(len(M))
    for j in range(8):
        A=mm(A,[[a**(5**((-j)%8)) for a in row] for row in M])
    return A

def elementary_count(n,modulus):
    p=5;q=p**n
    def digits(a):return [(a//p**i)%p for i in range(n)]
    def add(a,b):return sum(((u+v)%p)*p**i for i,(u,v) in enumerate(zip(digits(a),digits(b))))
    def neg(a):return sum((-u%p)*p**i for i,u in enumerate(digits(a)))
    def mul(a,b):
        A=digits(a);B=digits(b);C=[0]*(2*n-1)
        for i,u in enumerate(A):
            for j,v in enumerate(B):C[i+j]=(C[i+j]+u*v)%p
        for j in range(2*n-2,n-1,-1):
            c=C[j]
            for i in range(n):C[j-n+i]=(C[j-n+i]-c*modulus[i])%p
        return sum(C[i]*p**i for i in range(n))
    fourth=[0]*q
    for w in range(q):
        v=mul(w,w);fourth[mul(v,v)]+=1
    return 1+sum(fourth[add(mul(mul(a,a),a),neg(a))] for a in range(q))

counts=[elementary_count(n,m) for n,m in [(1,[0,1]),(2,[2,0,1]),(3,[1,1,0,1])]]
assert counts==[8,44,104]
traces=[5**n+1-counts[n-1] for n in (1,2,3)]
c1=-traces[0]
c2=-(traces[1]+c1*traces[0])//2
c3=-(traces[2]+c1*traces[1]+c2*traces[0])//3
assert (c1,c2,c3)==(2,11,12)
# H=(X^2+2X+5)^2(X^2-2X+5).
weil=[125,50,55,12,11,2,1]
base_basis=[(2,0),(3,0),(3,1)]
baseM=cartier(x**3-x,{i:R.one() for i in (1,2,3)},base_basis)
assert baseM==mat(data["base_Cartier_matrix"])
baseA=eighth(baseM)
assert baseA==eye(3)==mat(data["base_Cartier_eighth_power"])
basecp=charpoly(baseA)
assert basecp==pol(data["base_Frobenius_characteristic_polynomial_mod_5"])
assert basecp==(x-1)**3

records=[]
initial_points=[tuple(map(dec,r["initial_kernel"])) for r in data["covers"]]
assert len({enc(P[0]) for P in initial_points})==4
for rec,point in zip(data["covers"],initial_points):
    h1,N1,g1=[pol(rec[name]) for name in ("forward_h","forward_N","forward_g")]
    A1,B1=check_isogeny(-one,zero,point,h1,N1,g1)
    assert [enc(A1),enc(B1)]==rec["isogenous_E_coefficients"]
    dual=tuple(map(dec,rec["dual_kernel"]))
    images=[]
    for Q in initial_points:
        if Q[0]==point[0]:continue
        a,b=Q;v=h1(a)
        image=(N1(a)/(v*v),b*g1(a)/(v**3))
        images.append(image)
    assert dual in images
    h,N,g=[pol(rec[name]) for name in ("h","N","g")]
    A2,B2=check_isogeny(A1,B1,dual,h,N,g)
    assert A2==-one*k(3)**4 and B2==0
    cubic=x**3+A1*x+B1
    F=pol(rec["F"])
    assert F==cubic*g*g*h*h/(k(3)**6)
    assert F==(N**3*h*h-k(3)**4*N*h**6)/(k(3)**6)
    assert (cubic.degree(),g.degree(),h.degree(),F.degree())==(3,3,1,11)
    assert all(a.is_squarefree() for a in (cubic,g,h))
    assert cubic.gcd(g)==cubic.gcd(h)==g.gcd(h)==1
    basis=[tuple(v) for v in rec["basis"]]
    expected=[]
    for s in (1,2,3):
        dh=0 if s==1 else 4
        j=0
        while 11*s-4*dh-4*j-5>=0:
            expected.append((s,j));j+=1
    assert basis==expected and len(basis)==7
    M=cartier(F,{1:R.one(),2:g*h,3:g*h},basis)
    assert M==mat(rec["Cartier_matrix"])
    A=eighth(M)
    assert A==eye(7)==mat(rec["Cartier_eighth_power"])
    cp=charpoly(A)
    assert cp==pol(rec["Frobenius_characteristic_polynomial_mod_5"])
    new,rem=divmod(cp,basecp)
    assert rem==0 and new==(x-1)**4
    assert new==pol(rec["new_Frobenius_characteristic_polynomial_mod_5"])
    assert new(one)==0 and rec["relative_class_number_prime_to_5"] is False
    records.append({"initial_kernel":rec["initial_kernel"],
                    "checked_Cartier_entries":49,
                    "Cartier_eighth_power_is_identity":True,
                    "new_characteristic_polynomial":[enc(a) for a in new],
                    "all_new_geometric_p_torsion_is_rational":True,
                    "failure_persists_under_all_constant_extensions":True})

out={"source_sha256":sha256(raw).hexdigest(),"field_modulus_irreducible":True,
     "base_counts_degrees1_2_3":counts,"base_Frobenius_polynomial":weil,
     "base_Frobenius_polynomial_factored":"(X^2+2X+5)^2(X^2-2X+5)",
     "every_constant_degree3_character_requires_field_degree_multiple_of":8,
     "verified_covers":records,
     "scope":"the four elliptic-isogeny pullbacks fail; no claim that every cubic cover of the quartic fails"}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
