#!/usr/bin/env python3
"""Exact computable formulas accompanying the global contraction in C87."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

checks: list[dict[str, object]]=[]


def check(name: str, condition: object) -> None:
    result=bool(condition)
    checks.append({"name":name,"passed":result})
    if not result:
        raise AssertionError(name)


def eq(name: str,lhs: object,rhs: object=0) -> None:
    check(name,sp.simplify(lhs-rhs)==0)


x,y,k,l=sp.symbols("x y k l",real=True)
twist=x+k*(y+1)/2
eq("canonical lower twist boundary",twist.subs(y,-1),x)
eq("exact upper integer shift",twist.subs(y,1)-x,k)
eq("original twist deck label",twist.subs(x,x+1)-twist,1)
eq("composition adds the measured shift",
   twist.subs(x,x+l*(y+1)/2),x+(k+l)*(y+1)/2)
eq("negative shift is the inverse twist",
   twist.subs(x,x-k*(y+1)/2),x)
eq("zero shift original spanning-arc lower label",
   twist.subs({x:0,y:-1,k:0}),0)
eq("zero shift original spanning-arc upper label",
   twist.subs({x:0,y:1,k:0}),0)

alpha,a,b,ha,hb=sp.symbols("alpha a b ha hb",real=True)
eq("relative interval correction difference",
   ((1-alpha)*b+alpha*hb)-((1-alpha)*a+alpha*ha),
   (1-alpha)*(b-a)+alpha*(hb-ha))
eq("relative correction unaltered side",
   ((1-alpha)*a+alpha*ha).subs(alpha,0),a)
eq("relative correction central final value",
   ((1-alpha)*a+alpha*ha).subs(alpha,1),ha)
eq("relative correction lower endpoint",
   ((1-alpha)*a+alpha*ha).subs({a:-1,ha:-1}),-1)
eq("relative correction upper endpoint",
   ((1-alpha)*a+alpha*ha).subs({a:1,ha:1}),1)
for aa in [sp.Rational(0),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),sp.Rational(1)]:
    for d1,d2 in [(sp.Rational(1,3),sp.Rational(1,7)),(sp.Rational(2),sp.Rational(5,3))]:
        check(f"strict interval correction {aa},{d1},{d2}",
              (1-aa)*d1+aa*d2>0)

w=sp.symbols("w",positive=True)
D=sp.diag(1,w)
Di=sp.diag(1,1/w)
check("scaling inverse first identity",D*Di==sp.eye(2))
check("scaling inverse second identity",Di*D==sp.eye(2))
z=sp.Matrix([x,y])
unit=sp.Matrix([1,0])
check("original unit translation under scaling",D*(Di*z+unit)==z+unit)
X,Y=sp.symbols("X Y",real=True)
check("exact vertical output scaling",D*sp.Matrix([X,Y])==sp.Matrix([X,w*Y]))

t,e=sp.symbols("t e",nonnegative=True)
ratio=(1+t/w)/(1+t)
eq("weighted ratio upper-scale margin",
   (1-ratio).subs(w,1+e),t*e/((1+e)*(1+t)))
eq("weighted ratio lower-scale margin",
   (1/w-ratio).subs(w,1/(1+e)),e/(1+t))

rho=sp.symbols("rho",nonnegative=True)
norm=sp.symbols("norm",positive=True)
den=1-rho+rho*norm
target_radius=rho*norm/den
eq("original disk radial scaling formula",
   (rho/(1-rho))/(1+rho*norm/(1-rho)),rho/den)
eq("original disk normalizer inverse scalar",
   (rho/den)/(1-target_radius+rho/den),rho)
eq("boundary normalizer radius",target_radius.subs(rho,1),1)
eq("origin normalizer radius",target_radius.subs(rho,0),0)
eq("identity normalizer",(rho/den).subs(norm,1),rho)
eq("boundary direction coefficient",(rho/den).subs(rho,1),1/norm)

Lmax=sp.symbols("Lmax",positive=True)
support=1+2*Lmax
W=3+2*Lmax
eq("continuous support height strict margin",W-support,2)
eq("rescaled support stays in unit annulus",support/W,1-2/W)
check("strict rescaled support inequality",sp.simplify(1-support/W).is_positive)
eq("unscaling recovers the original support",W*(support/W),support)

s=sp.symbols("s",positive=True)
eq("cutoff stage middle parameter",(1/(2*s)).subs(s,sp.Rational(1,2)),1)
eq("annulus contraction middle parameter",(2*s-1).subs(s,sp.Rational(1,2)),0)
eq("annulus contraction final parameter",(2*s-1).subs(s,1),1)
check("cutoff stage initial interface",sp.limit(1/(2*s),s,0,dir="+")==sp.oo)

result={
    "claim":"C.87",
    "arithmetic":"Exact symbolic expressions and rational inequalities only",
    "scope":(
        "Twist, deck labels, relative correction, normalizer inverse, weighted "
        "scaling, closed-disk formula, support bounds and homotopy faces. "
        "The full annulus identity-component contraction is the checked "
        "source theorem; the exact topology and global parameter comparison "
        "are proved in the manuscript."
    ),
    "checks":checks,
    "number_of_checks":len(checks),
    "all_passed":all(row["passed"] for row in checks),
}
out=Path(__file__).with_name("c87_global_contraction_output.json")
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(f"C87: {len(checks)} exact checks; all passed.")
print(out)
