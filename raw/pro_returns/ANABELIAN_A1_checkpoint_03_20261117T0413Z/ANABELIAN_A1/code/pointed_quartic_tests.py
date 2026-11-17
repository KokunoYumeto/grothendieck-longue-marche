"""Exact small-field tests on two pointed smooth plane quartics."""
from pathlib import Path
from collections import Counter
import json
import sympy as sp
from flint import fq_default_ctx
out=[]
def enc(a,p):
    return sum(int(v)*p**i for i,v in enumerate(a.to_list()))
for p,az,P in [(3,1,[1,1,1]),(5,-1,[1,0,1])]:
    counts=[];fields=[]
    for n in (1,2,3):
        k=fq_default_ctx(p,n,"z")
        els=[k([(a//p**i)%p for i in range(n)]) for a in range(p**n)]
        v4=Counter(enc(a**4,p) for a in els)
        values={enc(a,p):a for a in els}
        affine=sum(c*v4.get(enc(-az-values[v],p),0) for v,c in v4.items())
        infinity=v4.get(enc(k(-1),p),0)
        counts.append(affine+infinity)
        fields.append({"degree":n,"modulus":list(map(int,k.modulus())),
                       "affine":affine,"infinity":infinity,"count":affine+infinity})
    s1,s2,s3=[p**(i+1)+1-counts[i] for i in range(3)]
    a1=-s1;a2=(s1*s1-s2)//2;a3=(-s1**3+3*s1*s2-2*s3)//6
    coeff=[1,a1,a2,a3,p*a2,p*p*a1,p**3]
    X=sp.symbols("X");H=sum(c*X**(6-i) for i,c in enumerate(coeff))
    h=int(H.subs(X,1))
    rec={"p":p,"curve":f"X^4+Y^4+({az})Z^4=0","point":P,
         "smoothness":"partial derivatives 4X^3,4Y^3,4aZ^3 have no common projective zero",
         "point_counts":fields,"Frobenius_polynomial":str(H),"factorization":str(sp.factor(H)),
         "jacobian_order":h,"jacobian_factorization":sp.factorint(h),
         "odd_prime_base_field_tests":"none, since Jacobian order is a power of 2"}
    assert h & (h-1)==0
    print(json.dumps(rec,indent=2),flush=True);out.append(rec)
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")

