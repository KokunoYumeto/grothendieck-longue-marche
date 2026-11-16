#!/usr/bin/env python3
"""Exact checks for D.39--D.41. No numerical p-adic approximations."""
from pathlib import Path
import json
import sympy as s

t, w, X, Y, Z = s.symbols("t w X Y Z")

def S(a, z):
    if a == 0:
        return s.Integer(0)
    if a > 0:
        return sum(z**j for j in range(a))
    return -sum(z**(-j) for j in range(1, -a+1))

def clean(expr):
    return s.cancel(s.expand(expr))

C = s.Matrix([1-w, t-1])

def fox(a, b, lam):
    return s.Matrix([S(a, t), t**a*S(b, w)]) + lam*C

def mul(g, h):
    a, b, lam = g
    c, d, eta = h
    return (a+c, b+d,
            clean(lam+t**a*w**b*eta-t**a*S(b,w)*S(c,t)))

def inv(g):
    a,b,lam = g
    return (-a,-b,clean(-t**(-a)*w**(-b)*(lam+S(a,t)*S(b,w))))

def powint(g, n):
    if n < 0:
        return powint(inv(g), -n)
    result = (0,0,s.Integer(0))
    for _ in range(n):
        result = mul(result,g)
    return result

def action(g,q,B):
    a,b,lam = g
    beta = 1+(t-1)*(w-1)*B
    U = S(q,t)*S(q,w)*beta
    phi = lam.subs({t:t**q,w:w**q}, simultaneous=True)
    return (q*a,q*b,clean(U*phi+t**(q*a)*(w**(q*b)-1)*B))

checks = 0
samples = [
    ((1,0,t+w), (0,1,t*w)),
    ((-1,2,t**2-w), (2,-1,w**2+t)),
    ((2,1,1-t*w), (1,2,t-w)),
    ((0,-2,t+w**-1), (-1,0,1)),
]
for g,h in samples:
    a,b,lam=g
    c,d,eta=h
    product=mul(g,h)
    difference=fox(*product)-fox(*g)-t**a*w**b*fox(*h)
    assert all(clean(v)==0 for v in difference)
    assert mul(g,inv(g))==(0,0,0)
    checks += 2

# Direct Fox evaluation of the action for arbitrary inner conjugator B.
for q in (2,3):
    B=1+t+2*w
    U=S(q,t)*S(q,w)*(1+(t-1)*(w-1)*B)
    gx=s.Matrix([S(q,t),0])
    gy=s.Matrix([0,S(q,w)])+(w**q-1)*B*C
    for g,_ in samples[:2]:
        a,b,lam=g
        acted_vector=(U*lam.subs({t:t**q,w:w**q},simultaneous=True)*C
                      +S(a,t**q)*gx+t**(q*a)*S(b,w**q)*gy)
        assert all(clean(v)==0 for v in fox(*action(g,q,B))-acted_vector)
        checks += 1

# The explicit tame relator, with arbitrary (not necessarily arithmetic) B.
relator_checks=[]
for q,(a,b,alpha,beta) in [(2,(1,-1,1,1)),(3,(0,1,1,0))]:
    c=t+2*w
    d=t*w-1
    B=1+t-w
    F=(a,b,d)
    I=(alpha,beta,c)
    actual=mul(mul(mul(F,action(I,q,B)),inv(F)),powint(I,-q))
    mu=t**alpha*w**beta
    nu=t**a*w**b
    U=S(q,t)*S(q,w)*(1+(t-1)*(w-1)*B)
    P=-sum(t**(k*alpha)*S(k*beta,w)*S(alpha,t) for k in range(q))
    K=t**(q*alpha)*S(q*beta,w)*S(a,t)-t**a*S(b,w)*S(q*alpha,t)
    predicted=clean(
        nu*U*c.subs({t:t**q,w:w**q},simultaneous=True)
        -S(q,mu)*c+(1-mu**q)*d
        +nu*t**(q*alpha)*(w**(q*beta)-1)*B+K-P)
    assert actual[0:2]==(0,0)
    assert clean(actual[2]-predicted)==0
    checks += 1
    relator_checks.append({"q":q,"abelian_coordinates":[a,b,alpha,beta]})

# The additive beta identity in every displayed weight.
for m in range(2,17):
    D=lambda A,B:(A+B)**m-A**m-B**m
    assert s.expand(D(X,Y)+D(X+Y,Z)-D(Y,Z)-D(X,Y+Z))==0
    checks += 1

# Reflection checked as an exact Taylor identity, not a decimal approximation.
reflection=[]
for q in (2,7,11):
    target=sum(s.bernoulli(m)*(1-q**m)*X**m/(m*s.factorial(m))
               for m in range(2,13,2))
    ratio=s.series(q*s.sinh(X/2)/s.sinh(q*X/2),X,0,13).removeO()
    actual=s.series(s.log(ratio),X,0,13).removeO()
    assert s.expand(actual-target)==0
    checks += 1
    reflection.append({"q":q,"through_degree":12})

q,k=s.symbols("q k")
L2=(q*q-1)*((X+Y)**2-X**2-Y**2)/48
L3=k*((X+Y)**3-X**3-Y**3)/288
L4=-(q**4-1)*((X+Y)**4-X**4-Y**4)/5760
assert s.expand(L2).coeff(X,1).coeff(Y,1)==(q*q-1)/24
assert s.expand(L3).coeff(X,2).coeff(Y,1)==k/96
assert s.expand(L4).coeff(X,3).coeff(Y,1)==-(q**4-1)/1440
checks+=3

out={
    "status":"all exact checks passed",
    "total_checks":checks,
    "normal_form":"C^lambda x^a y^b",
    "multiplication":"lambda + t1^a t2^b eta - t1^a S_b(t2) S_c(t1)",
    "tame_relator_checks":relator_checks,
    "beta_identity_weights":list(range(2,17)),
    "Bernoulli_reflection_checks":reflection,
    "low_coefficient_comparison":"r=(q^2-1)/24, h=kappa3([g,c])/96, c=-(q^4-1)/1440",
    "odd_generator_residual_classes":{"n=1 mod4":"5","n=3 mod4":"phi^3"},
    "scope":"Exact algebraic certificates; the infinite identities and arithmetic applicability are proved in the text."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
