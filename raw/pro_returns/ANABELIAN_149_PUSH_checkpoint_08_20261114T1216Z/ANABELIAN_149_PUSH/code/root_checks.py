#!/usr/bin/env python3
"""Exact finite checks supporting D, E and the local-germ lead.

No finite computation below asserts an infinite-level theorem. The proofs
and the scope of each check are in the paper. Run with Python 3 and SymPy.
"""
import itertools
import json
from pathlib import Path
import sympy as sp

out = {}

# The local P2 example has the map (a,b) -> a-b. Its diagonal is
# exactly the kernel at every finite level, not only in a chosen sample.
local = []
for n in range(2, 31):
    kernel = [(a, b) for a in range(n) for b in range(n)
              if (a-b) % n == 0]
    assert kernel == [(a, a) for a in range(n)]
    # The local character (a,b)->a cannot descend through a-b: (1,1)
    # is killed by the latter and not the former.
    assert (1-1) % n == 0 and 1 % n != 0
    local.append({"n": n, "kernel_order": len(kernel),
                  "nonextending_character_witness": [1, 1]})
out["local_normal_crossings"] = local

# Finite concrete version of the closed-subgroup/sub-germ construction.
# G=Z/12 x Z/6, H=< (2,1) > (order 6); test every subgroup V of H.
G = {(a, b) for a in range(12) for b in range(6)}
H = {(2*j % 12, j % 6) for j in range(6)}
def add(x,y): return ((x[0]+y[0]) % 12, (x[1]+y[1]) % 6)
germ_cases = []
for step in (1,2,3,6):
    V = {(2*j % 12, j % 6) for j in range(0,6,step)}
    N = {(0,0)}
    U = {add(v,n) for v in V for n in N}
    assert H & U == V
    # The H orbit of U in G/U is H/V.
    cosets = {frozenset(add(h,u) for u in U) for h in H}
    assert len(cosets) == len(H)//len(V)
    germ_cases.append({"V_order":len(V), "orbit_size":len(cosets)})
out["finite_germ_orbits"] = germ_cases

t,z,c = sp.symbols("t z c")
h = z**3 - 3*z + t
f = sp.expand(h**2)
assert sp.expand(sp.diff(f,z)-6*(z-1)*(z+1)*(t+z**3-3*z)) == 0
assert sp.expand(h-(t-2)) == sp.expand((z-1)**2*(z+2))
assert sp.expand(h-(t+2)) == sp.expand((z+1)**2*(z-2))
disc = sp.factor(sp.discriminant(h-c,z))
assert sp.expand(disc - 27*(4-(t-c)**2)) == 0
assert sp.expand((t+2)**2-(t-2)**2) == 8*t
critical_values = {
    "t=0": sorted({sp.Rational(0), (-2)**2, 2**2}),
    "t=1/10": sorted({sp.Rational(0), (sp.Rational(1,10)-2)**2,
                       (sp.Rational(1,10)+2)**2})}
assert len(critical_values["t=0"]) == 2
assert len(critical_values["t=1/10"]) == 3
out["moving_critical_values"] = {
    "derivative": str(sp.factor(sp.diff(f,z))),
    "discriminant": str(disc),
    "values": {k:list(map(str,v)) for k,v in critical_values.items()},
    "source_punctures": 5*3+4+1,
    "types_in_diagram": [[0,20],[0,8],[0,6],[0,4],[0,3]],
    "degrees": [3,1,2,1]}
assert out["moving_critical_values"]["source_punctures"] == 20

# Degree and Euler-characteristic obstruction to unrestricted specialization.
obstructions = []
for p in (2,3,5,7,11,13):
    g_target, g_source = 2, p+1
    d = sp.Rational(2*g_source-2, 2*g_target-2)
    assert d == p
    obstructions.append({"p":p,"target_genus":g_target,
                         "source_genus":g_source,"forced_degree":int(d)})
out["specialization_degree_obstruction"] = obstructions

# Artin-Schreier pole check. For a nonconstant polynomial h of degree d,
# the leading pole of h^p-h has degree p*d. Enumerate coefficients for
# p=2,3,5 and d<=4, with nonzero leading coefficient.
AS = []
x = sp.symbols("x")
for p in (2,3,5):
    checked = 0
    for degree in range(1,5):
        for coeffs in itertools.product(range(p), repeat=degree+1):
            if coeffs[-1] == 0: continue
            poly = sp.Poly(sum(coeffs[i]*x**i for i in range(degree+1)), x,
                           modulus=p)
            AS_poly = poly**p-poly
            assert AS_poly.degree() == p*degree
            assert AS_poly.degree() != 1
            checked += 1
    AS.append({"p":p,"polynomials_checked":checked,
               "all_nonzero_leading_poles_divisible_by_p":True})
out["artin_schreier_poles"] = AS

# Tangential Kummer specialization is multiplicative and need not be
# an evaluation preserving addition at a zero or pole.
def tangential_value(expr, tangent=sp.Rational(2)):
    expr=sp.cancel(expr)
    num, den=sp.fraction(expr)
    pn,pd=sp.Poly(num,t),sp.Poly(den,t)
    mn=min(mon[0] for mon,_ in pn.terms())
    md=min(mon[0] for mon,_ in pd.terms())
    m=mn-md
    leading=sp.limit(expr/t**m,t,0)
    return sp.simplify(tangent**m*leading)
vals = [tangential_value(q) for q in (t,t-1,t+1,t**-2*(3+t))]
assert vals == [2,-1,1,sp.Rational(3,4)]
assert vals[1] != vals[0]-1
for a,b in [(t,t-1), (t**2+2*t,t**-3*(t+1))]:
    assert tangential_value(a*b) == tangential_value(a)*tangential_value(b)
out["tangential_kummer"] = {"tangent":2,
    "functions":["t","t-1","t+1","t^-2(3+t)"],
    "values":list(map(str,vals)),"not_additive":True}

# Complexity identity for a composable word: cover d multiplies c;
# filling r lowers c by r. The test diagram gives 18=6*1+12.
complexities = [2*g-2+n for g,n in out["moving_critical_values"]["types_in_diagram"]]
degrees = out["moving_critical_values"]["degrees"]
defects = [complexities[i]-degrees[i]*complexities[i+1] for i in range(4)]
assert defects == [0,2,0,1]
total = sum(defects[i]*sp.prod(degrees[:i]) for i in range(4))
assert total == complexities[0]-sp.prod(degrees)*complexities[-1] == 12
out["diagram_complexity"] = {"complexities":complexities,"defects":defects,
                            "composite_degree":6,"composite_defect":int(total)}
out["status"] = "All asserted exact checks passed; infinite statements require the written proofs."
dest = Path(__file__).with_name("root_checks_output.json")
dest.write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps({"status":"passed","output":str(dest),
                  "AS_cases":sum(v["polynomials_checked"] for v in AS)},indent=2))
