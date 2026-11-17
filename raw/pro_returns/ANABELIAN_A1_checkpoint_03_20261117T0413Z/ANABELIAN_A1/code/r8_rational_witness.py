"""Search and certify a rational prime-cyclic witness on the R8 curve.
Exact Cartier--Mumford test; no enumeration of the huge constant field.
"""
from pathlib import Path
from functools import lru_cache
import json, sys, time
from flint import fq_default_ctx, fq_default_poly_ctx
root=Path(__file__).resolve().parent
ell=int(sys.argv[1]) if len(sys.argv)>1 else 191
m=1
while pow((-2**19)%ell,m,ell)!=1:m+=1
degree=38*m
start=time.monotonic()
k=fq_default_ctx(2,degree,"z",fq_type="FQ_NMOD")
R=fq_default_poly_ctx(k);x=R.gen()
print("Field degree",degree,"modulus",k.modulus(),"seconds",time.monotonic()-start,flush=True)
M=R([int(i in (38,14,10,9,8,5,2,1,0)) for i in range(39)])
roots=M.roots();assert len(roots)==38
t=roots[0][0];den=t**3+1
A=(x*x+t*t*x+t)/den
B=(t*x*x+x+t*t)/den
f=A**3
shift=R.zero()
for j in (3,2,1):
    a=f[2*j].sqrt()
    r=R([k.zero()] * j+[a])
    shift+=r; f+=r*r+r
assert f.degree()==5 and all(f[j]==0 for j in (2,4))
lead=f[5]
# u=lead*x, original y=lead^3*Y+shift(lead*x).
ff=f.compose(lead*x)/lead**6
hh=R([lead**-3])
assert ff[5]==1
Ac=A.compose(lead*x); Bc=B.compose(lead*x)
Sc=shift.compose(lead*x)
one=R.one();zero=R.zero()
O=(one,zero)
def monic(a):return a/a[a.degree()]
def check(D):
    a,b=D
    assert a.degree()<=2 and a[a.degree()]==1 and b.degree()<a.degree()
    assert (b*b+hh*b+ff)%a==zero
def add(D,E):
    a1,b1=D;a2,b2=E
    d1,e1,e2=a1.xgcd(a2)
    d,c1,c2=d1.xgcd(b1+b2+hh)
    s1,s2,s3=c1*e1,c1*e2,c2
    a=(a1*a2)//(d*d)
    numerator=s1*a1*b2+s2*a2*b1+s3*(b1*b2+ff)
    assert numerator%d==zero
    b=(numerator//d)%a
    while a.degree()>2:
        numerator=ff+b*b+hh*b
        assert numerator%a==zero
        anew=monic(numerator//a)
        b=(b+hh)%anew;a=anew
    result=(a,b);check(result)
    return result
def mul(D,n):
    result=O
    while n:
        if n&1:result=add(result,D)
        D=add(D,D);n>>=1
    return result
def eadd(P,Q):
    if P is None:return Q
    if Q is None:return P
    X,Y=P;Z,W=Q
    if X==Z:
        if Y!=W:return None
        return X**4,Y**4+1
    slope=(Y+W)/(X+Z)
    v=slope*slope+X+Z
    w=slope*(X+v)+Y+1
    assert w*w+w==v**3
    return v,w
def emul(P,n):
    Q=None
    while n:
        if n&1:Q=eadd(P,Q)
        P=eadd(P,P);n>>=1
    return Q
# F over this field is scalar (-2)^(degree/2) on E.
scalar=(-2)**(degree//2)
N=abs(scalar-1)
assert N%ell==0 and (N//ell)%ell!=0
def torsion():
    while True:
        X=k.random_element()
        rr=R([X**3,1,1]).roots()
        if not rr:continue
        P=emul((X,rr[0][0]),N//ell)
        if P is not None:
            assert emul(P,ell) is None
            return P
def pullback(P,which):
    X,Y=P
    if which==1:
        a=monic(Ac-X)
        b=((R([Y])+Sc)/lead**3)%a
    else:
        a=monic(Bc-X)
        b=((R([Y])+Sc+((lead*x)**3+1)/den)/lead**3)%a
    result=a,b;check(result)
    assert mul(result,ell)==O
    return result
def encode(a):return sum(int(v)<<i for i,v in enumerate(a.to_list()))
def epoly(f):return [encode(a) for a in f]
def ediv(D):return {"u":epoly(D[0]),"v":epoly(D[1])}
attempts=[]
for attempt in range(1,31):
    P,Q=torsion(),torsion()
    D=add(pullback(P,1),pullback(Q,2))
    if D==O:continue
    assert mul(D,ell)==O
    divisors=[O,D]
    for i in range(2,ell):divisors.append(add(divisors[-1],D))
    assert add(divisors[-1],D)==O
    assert all(a.degree()==2 for a,b in divisors[1:])
    cs=[k.zero()]*ell
    for i in range(1,ell):
        a,b=divisors[i]
        numerator=ff+b*b+hh*b
        assert numerator%a==zero
        correction=(numerator//a)/hh[0]
        v=(b+a*(correction%a))%(a*a)
        assert (v*v+hh*v+ff)%(a*a)==zero
        target=divisors[2*i%ell][0]
        assert target==monic((v*v+hh*v+ff)//(a*a))
        assert (v+hh)%target==divisors[2*i%ell][1]
        cs[i]=v[3]*target[1]
        assert cs[i]!=0
    vals=[]
    for i in range(1,ell):
        a=k.one();j=i
        for s in range(degree):
            a=a*a*cs[j];j=2*j%ell
        assert j==i
        vals.append(a)
    failures=[i+1 for i,v in enumerate(vals) if v==1]
    print("Attempt",attempt,"failed characters",len(failures),"seconds",time.monotonic()-start,flush=True)
    attempts.append({"attempt":attempt,"failed_characters":failures})
    if not failures:
        data={"ell":ell,"base_field_degree":38,"constant_extension_degree":m,
              "field_degree":degree,"field_modulus_coefficients":list(map(int,k.modulus())),
              "encoding":"integer bits are coefficients in z; ascending polynomial arrays",
              "t":encode(t),"reduced_shift":epoly(shift),
              "coordinate_scale":encode(lead),"h":epoly(hh),"f":epoly(ff),
              "elliptic_points":[[encode(a) for a in P],[encode(a) for a in Q]],
              "torsion_divisor":ediv(D),"divisors":[ediv(E) for E in divisors[1:]],
              "cartier_scalars":[encode(c) for c in cs[1:]],
              "linear_frobenius_multipliers":[encode(a) for a in vals],
              "attempts":attempts,"seconds":time.monotonic()-start,
              "result":"all nontrivial multipliers differ from one; odd relative class number"}
        (root/f"r8_rational_witness_{ell}.json").write_text(json.dumps(data,indent=2)+"\n")
        print("CERTIFIED RATIONAL WITNESS",ell,"extension",m,flush=True)
        break
else:
    (root/f"r8_rational_witness_{ell}_attempts.json").write_text(json.dumps(attempts,indent=2)+"\n")
    print("No witness in attempted classes; no nonexistence assertion.",flush=True)

