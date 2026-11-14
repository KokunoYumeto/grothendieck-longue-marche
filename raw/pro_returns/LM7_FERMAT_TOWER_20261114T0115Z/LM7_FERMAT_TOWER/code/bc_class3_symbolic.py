"""Independent symbolic audit of every E54.11--12 coefficient."""
from pathlib import Path
import json
import sympy as s

a,b,n,A,B,N,r,t=s.symbols("a b n A B N r t")
zero=(s.Integer(0),)*5

def mul(g,h):
    x,y,c,d,e=g
    X,Y,C,D,E=h
    return tuple(s.expand(z) for z in (
        x+X,y+Y,c+C-X*y,
        d+D+y*X*(X+1)/2-X*c,
        e+E+X*y*(y+1)/2-Y*c+X*y*Y))

def inv(g):
    x,y,c,d,e=g
    return (-x,-y,-c-x*y,
            -d-x*c-x*y*(x-1)/2,
            -e-y*c+x*y*(1-y)/2)

def pow4(g):
    return mul(mul(g,g),mul(g,g))

def alpha(g):
    x,y,c,d,e=g
    return (4*x,4*y,4*y+16*c,40*c+64*d,
            24*c+64*e-8*y*(y-1)-s.Rational(15,2)*y)

g=(a,b,n,r,t)
assert mul(g,inv(g))==zero and mul(inv(g),g)==zero
inertia=(a,b,n,s.Integer(0),s.Integer(0))
frob=(A,B,N,s.Integer(0),s.Integer(0))
error=mul(mul(mul(frob,alpha(inertia)),inv(frob)),inv(pow4(inertia)))
L=4*A*b-4*B*a+6*a*b+4*b+12*n
R=(2*A*A*b-4*A*B*a+16*A*a*b+2*A*b+16*A*n
   -8*B*a*a+2*B*a-4*N*a+17*a*a*b+13*a*b+54*a*n+40*n)
S=(16*A*b*b-4*A*b-4*B*B*a+4*B*a+8*B*b+32*B*n-8*N*b
   +14*a*b*b-6*a*b+16*b*b+108*b*n+b+48*n)/2
assert tuple(s.expand(z) for z in error)==(0,0,s.expand(L),s.expand(R),s.expand(S))
changed=mul(mul(mul(frob,alpha((a,b,n,r,t))),inv(frob)),inv(pow4((a,b,n,r,t))))
assert s.expand(changed[3]-error[3])==60*r
assert s.expand(changed[4]-error[4])==60*t
example=[s.expand(z.subs({a:0,b:1,n:0,A:-1,B:0})) for z in map(s.sympify,error)]
assert example==[0,0,0,0,s.Rational(5,2)-4*N]
out={"statement":"E.54","status":"PASS",
     "identities":["both Hall inverses","full symbolic L,R,S",
                   "central changes exactly60r,60t",
                   "entire example family error5/2-4N"],
     "polynomials":{"L":str(s.expand(L)),"R":str(s.expand(R)),"S":str(s.expand(S))}}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("PASS both exact Hall inverses")
print("PASS every coefficient of the full symbolic local defect L,R,S")
print("PASS exact central correction60(r,t) and the entire example family")
print("E54 independent symbolic audit PASS")
