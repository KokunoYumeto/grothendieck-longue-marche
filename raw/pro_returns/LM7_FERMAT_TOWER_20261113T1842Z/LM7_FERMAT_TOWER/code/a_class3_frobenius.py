#!/usr/bin/env python3
"""Exact integral Magnus checks for the genuine class-three h quotient."""
from fractions import Fraction as Q
from pathlib import Path
from math import comb
import json

DEG=3
def add(*ps):
    out={}
    for p in ps:
        for w,a in p.items():out[w]=out.get(w,Q(0))+a
    return {w:a for w,a in out.items() if a}
def scale(p,a):return {w:a*b for w,b in p.items() if a*b}
def mul(p,q):
    out={}
    for w,a in p.items():
        for v,b in q.items():
            if len(w+v)<=DEG:out[w+v]=out.get(w+v,Q(0))+a*b
    return {w:a for w,a in out.items() if a}
one={():Q(1)}
x={():Q(1),(0,):Q(1)}
y={():Q(1),(1,):Q(1)}
def power(p,a):
    assert p.get((),Q(0))==1
    u=add(p,scale(one,-1));term=one;out=one;coef=Q(1)
    for k in range(1,DEG+1):
        term=mul(term,u);coef*=Q(a-(k-1),k)
        out=add(out,scale(term,coef))
    return out
def inv(p):return power(p,Q(-1))
def prod(*ps):
    out=one
    for p in ps:out=mul(out,p)
    return out
def comm(p,q):return prod(p,q,inv(p),inv(q))
c=comm(x,y);d=comm(x,c);e=comm(y,c)
z=inv(mul(x,y))
def evaluate(poly,X,Y):
    vx=add(X,scale(one,-1));vy=add(Y,scale(one,-1));out={}
    for w,a in poly.items():
        term=one
        for letter in w:term=mul(term,vx if letter==0 else vy)
        out=add(out,scale(term,a))
    return out
def normal(a,b,cc,dd,ee):
    return prod(power(x,a),power(y,b),power(c,cc),power(d,dd),power(e,ee))
def c2(lam):return (lam*lam-1)/24
def action(lam,k):
    f=power(c,c2(lam))
    return power(x,lam),prod(power(x,k),inv(f),power(y,lam),f,power(x,-k))

# The degree-two hexagon fixes both the denominator and the sign.
hexagons=[]
for lam in [Q(-5),Q(-2),Q(1),Q(2),Q(4),Q(7),Q(10),Q(1,4),Q(4,7)]:
    m=(lam-1)/2;coef=c2(lam)
    fxy=power(comm(x,y),coef)
    fzx=power(comm(z,x),coef)
    fyz=power(comm(y,z),coef)
    word=prod(fxy,power(x,m),fzx,power(z,m),fyz,power(y,m))
    degree2={w:a for w,a in word.items() if len(w)<=2}
    assert degree2==one
    assert word==one
    assert all(a.denominator%3 for p in [fxy,word] for a in p.values())
    hexagons.append({'lambda':str(lam),'c':str(coef),
                     'remaining_degree3':{''.join(map(str,w)):str(a) for w,a in word.items() if len(w)==3}})

lam=Q(4);k=Q(1)
X,Y=action(lam,k)
assert X==power(x,4)
assert Y==normal(0,4,4,0,Q(-15,2))
C=evaluate(c,X,Y);D=evaluate(d,X,Y);E=evaluate(e,X,Y)
assert C==normal(0,0,16,40,24)
assert D==power(d,64) and E==power(e,64)

# Both actual tangential root conventions are related by the specified
# inner transport, with its sign checked on the two free generators.
Xold,Yold=action(Q(4),Q(-5))
B=lambda p:prod(power(x,-2),p,power(x,2))
Binv=lambda p:prod(power(x,2),p,power(x,-2))
assert B(evaluate(Binv(x),Xold,Yold))==X
assert B(evaluate(Binv(y),Xold,Yold))==Y

general=[]
for lam in [Q(-5),Q(-2),Q(1),Q(2),Q(4),Q(7),Q(1,4),Q(4,7)]:
    for k in [Q(-5),Q(-2),Q(0),Q(1),Q(2),Q(1,2)]:
        X,Y=action(lam,k)
        expectedY=normal(0,lam,k*lam,lam*k*(k-1)/2,
                          lam*c2(lam)-k*lam*(lam+1)/2)
        assert Y==expectedY
        assert evaluate(c,X,Y)==normal(0,0,lam**2,
                    lam**2*(lam-1)/2+k*lam**2,lam**2*(lam-1)/2)
        assert evaluate(d,X,Y)==power(d,lam**3)
        assert evaluate(e,X,Y)==power(e,lam**3)
        assert all(a.denominator%3 for p in [X,Y] for a in p.values())
        general.append([str(lam),str(k)])

composition_checks=0
params=[(Q(4),Q(1)),(Q(7),Q(2)),(Q(1),Q(3)),(Q(1,4),Q(-1,4)),(Q(4,7),Q(2,7))]
for lam,k in params:
    X,Y=action(lam,k)
    for mu,l in params:
        X2,Y2=action(mu,l)
        Xt,Yt=action(lam*mu,k+lam*l)
        assert evaluate(X2,X,Y)==Xt and evaluate(Y2,X,Y)==Yt
        composition_checks+=1

out={'status':'PASS','statement':'E.54','hexagon_sign_checks':hexagons,
     'Frobenius4_Hall_images':{'x':['4','0','0','0','0'],
        'y':['0','4','4','0','-15/2'],'c':['0','0','16','40','24'],
        'd':['0','0','0','64','0'],'e':['0','0','0','0','64']},
     'Hall_order':'x^a y^b c^n d^r e^s; c=[x,y],d=[x,c],e=[y,c]',
     'general_exact_action_checks':general,
     'affine_composition_checks':composition_checks,
     'root_change_inner_transport':'Ad(x^-2) action(4,-5) Ad(x^2) = action(4,1)'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: positive hexagon coefficient c=(chi^2-1)/24 checked in integral Magnus degree3.')
print('Hexagon remaining degree3 terms:',[r['remaining_degree3'] for r in hexagons])
print('PASS: actual Frobenius4 images x^4, y^4 c^4 e^(-15/2), c^16 d^40 e^24, d^64, e^64.')
print('PASS:',len(general),'general Hall-action checks and',composition_checks,'affine composition checks.')
print('PASS: exact Ad(x^-2) root-normalization transport from k=-5 to k=1.')
