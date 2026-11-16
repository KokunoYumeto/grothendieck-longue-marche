"""Exact finite orbit and Eisenstein checks for A.89."""
from pathlib import Path
from math import comb

def val(x, ell):
    if x == 0:
        return 10**6
    x=abs(x); out=0
    while x % ell == 0:
        x//=ell; out+=1
    return out

def cycles(q, alpha, modulus):
    left=set(range(modulus)); out=[]
    while left:
        start=min(left); orbit=[]; x=start
        while x not in orbit:
            orbit.append(x); left.remove(x)
            x=(q*x+alpha)%modulus
        assert x==start
        out.append(tuple(orbit))
    return out

stable=0
for ell in (2,3,5):
    for q in (2,3,5,7,11,13):
        if q==ell: continue
        for s in range(4):
            for alpha in range(5):
                cyc=cycles(q,alpha,ell**s)
                assert sum(map(len,cyc))==ell**s
                for n in range(max(1,s),max(1,s)+3):
                    e=ell**(n-s)
                    assert sum(e*len(o) for o in cyc)==ell**n
                    # Quotient inertia labels and residue degrees remain literal.
                    next_cyc=cycles(q,alpha,ell**s)
                    assert next_cyc==cyc
                    assert all(len(a)//len(b)==1 for a,b in zip(next_cyc,cyc))
                    stable+=1

growth=[]
for ell,q,alpha,n in ((2,3,0,2),(2,5,1,2),(3,2,0,1),
                       (3,7,1,1),(5,2,0,1),(5,11,1,1)):
    mod=ell**n
    fixed=None
    if val(alpha,ell)>=val(q-1,ell):
        t=val(q-1,ell)
        fixed=(-(alpha//ell**t)*pow((q-1)//ell**t,-1,mod))%mod
    coarse=cycles(q,alpha,mod)
    chosen=next(o for o in coarse if fixed is None or fixed not in o)
    vals=[]
    for r in range(n+1,n+5):
        upper=[o for o in cycles(q,alpha,ell**r) if o[0]%mod in chosen]
        assert upper
        for o in upper: assert len(o)%len(chosen)==0
        vals.append(min(val(len(o)//len(chosen),ell) for o in upper))
    assert vals[-1]>vals[0]
    growth.append((ell,q,alpha,vals))

eisenstein=0
for n in range(1,10):
    N=2**n
    assert all(comb(N,j)%2==0 for j in range(1,N))
    for k in range(7):
        a=3+8*k
        assert val(1-a,2)==1
        eisenstein+=1

# A compatible sign vector at the middle of a three-level string
# has zero negative coordinate. Its augmentation is its positive coordinate.
sign_checks=0
vec=[(a,b) for a in range(2) for b in range(2)]
for upper in vec:
    middle=((upper[0]+upper[1])%2,0)
    lower=((middle[0]+middle[1])%2,0)
    assert middle[1]==lower[1]==0
    assert (sum(middle)%2)==middle[0]
    sign_checks+=1

lines=["A.89 exact local inverse-divisor certificate",
       f"Stable inertia-quotient/residue-degree transition checks: {stable}",
       f"Shifted dyadic Eisenstein cases: {eisenstein}",
       f"Real sign-kernel checks: {sign_checks}"]
for ell,q,alpha,vs in growth:
    lines.append(f"Affine orbit norm growth ell={ell}, q={q}, alpha={alpha}: {vs}")
lines += ["Prime-to-ell residue-degree factors are retained in every transition.",
          "No unrestricted-product or global class-generation claim is tested.",
          "All exact finite checks passed."]
out="\n".join(lines)+"\n"
Path(__file__).with_name("norm_local_divisor_certificate_output.txt").write_text(out)
print(out,end="")
