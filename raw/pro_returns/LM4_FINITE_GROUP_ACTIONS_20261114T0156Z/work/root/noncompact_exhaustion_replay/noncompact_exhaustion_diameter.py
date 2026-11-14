"""Exact checks for the recorded radial exhaustion-diameter witness.

The universal lower bound is the exact polynomial identity
(5(1+s)-2)^2-8(1+s)^2=1+14s+17s^2 for s>=0.
Grid checks supplement, and do not replace, the written inverse/operator
identities for F_(R,t)(x,y)=(x+tR beta(y-R),y).
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json


def beta(u):
    return max(F(0), 1-4*abs(u))


def forward(xy, R, t):
    x,y = xy
    return x+t*R*beta(y-R), y


def inverse(xy, R, t):
    x,y = xy
    return x-t*R*beta(y-R), y


def translation(xy, q):
    return xy[0]+q, xy[1]


def convolution(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def main():
    counts={}
    def check(value,kind):
        assert value,kind
        counts[kind]=counts.get(kind,0)+1
    a=convolution([3,5],[3,5])
    b=convolution([1,1],[1,1])
    polynomial=[x-8*y for x,y in zip(a,b)]
    check(polynomial==[1,14,17],"exact_universal_squared_bound")
    check(all(x>0 for x in polynomial),"strict_positive_coefficients_for_s_nonnegative")
    values=[]
    for m in [1,2,4,8,32,128]:
        R=F(m+1)
        check(R-F(1,4)>m,"support_escapes_core")
        check(beta(F(0))==1,"peak_value")
        check(forward((F(0),R),R,F(1))==(R,R),"exact_displaced_peak")
        for t in [F(0),F(1,3),F(2,3),F(1)]:
            for x in [F(-2),F(0),F(3,2)]:
                for y in [-R,R-F(1,3),R-F(1,4),R-F(1,8),R,
                          R+F(1,8),R+F(1,4),R+F(1,3)]:
                    p=(x,y)
                    check(inverse(forward(p,R,t),R,t)==p,"inverse_after_forward")
                    check(forward(inverse(p,R,t),R,t)==p,"forward_after_inverse")
                    for q in [-3,-1,1,4]:
                        check(forward(translation(p,q),R,t)==translation(forward(p,R,t),q),
                              "commutes_with_original_integer_translation")
                for y in [F(-m),F(0),F(m)]:
                    check(forward((x,y),R,t)==(x,y),"fixed_quotient_core_samples")
        values.append({"m":m,"R":int(R),"support_interval":[str(R-F(1,4)),str(R+F(1,4))],
                       "uniform_original_disk_displacement_lower_bound":"strictly greater than2/5"})
    out={"status":"PASS","scope":"Exact algebraic lower-bound identity plus rational sample checks for the written universal inverse, original-label commutation and support equations.",
         "universal_bound":{"R":"1+s, s>=0","positive_left_side":"5R-2=3+5s",
                            "squared_difference_coefficients":[1,14,17],
                            "consequence":"R/(1+sqrt(2)*R)>2/5 for every real R>=1"},
         "examples":values,"checks":counts,"total_checks":sum(counts.values()),
         "producer_sha256":sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name("noncompact_exhaustion_diameter_output.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))


if __name__=="__main__":
    main()
