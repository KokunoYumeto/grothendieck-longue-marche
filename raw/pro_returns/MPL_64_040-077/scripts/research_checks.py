#!/usr/bin/env python3
"""Exact finite/symbolic checks for research notes; never edits transcription.

Run from any working directory. Requires SymPy for polynomial identities.
These computations concern explicitly stated refinements, not all manuscript
claims or any unprovided results-register proof.
"""
from pathlib import Path
from itertools import product
from datetime import datetime, timezone
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research_support"
OUT.mkdir(exist_ok=True)

def add(a, b):
    return tuple(x ^ y for x, y in zip(a, b))

def mul(a, b):
    p, q, r, s = a
    u, v, w, x = b
    return ((p*u+q*w)%2, (p*v+q*x)%2,
            (r*u+s*w)%2, (r*v+s*x)%2)

def det(a):
    p, q, r, s = a
    return (p*s-q*r)%2

def tr(a):
    return (a[0]+a[3])%2

def inv(a):
    assert det(a) == 1
    return (a[3], a[1], a[2], a[0])

def act(a, v):
    return ((a[0]*v[0]+a[1]*v[1])%2,
            (a[2]*v[0]+a[3]*v[1])%2)

Z = (0, 0, 0, 0)
I = (1, 0, 0, 1)
vectors = [(1, 0), (0, 1), (1, 1)]
matrices = list(product(range(2), repeat=4))
group = [a for a in matrices if det(a)]

def parity(a):
    p = [vectors.index(act(a, v)) for v in vectors]
    return sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))%2

Vp = {Z} | {a for a in group if parity(a)}
W = {Z} | {a for a in group if not parity(a)}
assert len(group) == 6 and len(Vp) == len(W) == 4
assert all(add(a, b) in Vp for a in Vp for b in Vp)
assert all(add(a, b) in W for a in W for b in W)
assert Vp & W == {Z}
assert {add(a, b) for a in Vp for b in W} == set(matrices)
assert all(tr(mul(a, b)) == 0 for a in Vp for b in W)
for a in Vp:
    for b in Vp:
        assert tr(mul(a, b)) == int(a != Z and b != Z and a != b)
assert all(mul(a,b) in W and mul(a,b) == mul(b,a) for a in W for b in W)
assert all(inv(a) in W for a in W if a != Z)
assert {a for a in W if all(tr(mul(a,b)) == 0 for b in W)} == {Z}
assert any(tr(mul(a,a)) == 1 for a in W)
assert {act(g,vectors[0]) for g in group} == set(vectors)
conj = lambda g,a: mul(mul(g,a), inv(g))
fixed_W = {a for a in W if all(conj(g,a) == a for g in group)}
assert fixed_W == {Z,I}
assert not any(tr(a) for a in fixed_W)
assert {a for a in matrices if tr(a) == 0} == {add(a,b) for a in Vp for b in (Z,I)}
assert {a for a in W if tr(mul(a,I)) == 0} == {Z,I}
assert {a for a in matrices if tr(mul(a,I)) == 0} != {Z,I}
tau = {}
for v in vectors:
    matches = [a for a in Vp-{Z} if act(a,v) == v]
    assert len(matches) == 1
    tau[v] = matches[0]
tau[(0,0)] = Z
for v in tau:
    for w in tau:
        assert add(tau[v],tau[w]) == tau[(v[0]^w[0],v[1]^w[1])]
for g in group:
    for v in tau:
        assert conj(g,tau[v]) == tau[act(g,v)]

z,t,u,x = sp.symbols("z t u x")
A=z*z-2*z+t
B=z*z-2*t*z+t
C=z*z-t
F=t*A*A/(B*B)
R=A/B
sigma=[(z-t)/(z-1),t/z,t*(z-1)/(z-t)]
assert sp.cancel(sigma[0].subs(z,sigma[1])-sigma[2]) == 0
for q in sigma:
    assert sp.cancel(F.subs(z,q)-F) == 0
assert sp.expand(t*A*A-B*B-(t-1)*C*C) == 0
assert sp.expand(A*A-B*B-4*(t-1)*z*(z-1)*(z-t)) == 0
assert sp.factor(sp.resultant(A,B,z)) == 4*t*(t-1)**2
assert sp.cancel(sp.diff(F,z)+4*t*(t-1)*A*C/B**3) == 0
Rvalues=[sp.cancel(R.subs(z,0)),sp.cancel(R.subs(z,1)),sp.limit(R,z,sp.oo),sp.cancel(R.subs(z,t))]
assert Rvalues == [1,-1,1,-1]
assert all(sp.cancel(F.subs(z,k)-t) == 0 for k in (0,1,t))
assert sp.limit(F,z,sp.oo) == t
assert sp.simplify(B.subs(z,t+sp.sqrt(t*(1-t)))+2*t*(t-1)) == 0
assert sp.simplify(B.subs(z,t+sp.sqrt(t*(t-1)))) == 0
iterate = sp.factor(F.subs(z,F,simultaneous=True)-t)
num,den = sp.fraction(iterate)
expected_num=16*t*(t-1)*z*(z-1)*(z-t)*A*A*B*B*C*C
assert sp.expand(num-expected_num) == 0
assert sp.degree(num,z) == 15 and sp.degree(den,z) == 16
assert sp.gcd(num.subs(t,2),den.subs(t,2)) == 1
# At t=2 all six critical points are distinct and disjoint from {0,1,2,infty}.
for a,b in ((A,B),(A,C),(B,C)):
    assert sp.resultant(a.subs(t,2),b.subs(t,2),z) != 0
for a in (A,B,C):
    assert sp.discriminant(a.subs(t,2),z) != 0
    assert all(a.subs({t:2,z:k}) != 0 for k in (0,1,2))

norms={}
for n in range(2,9):
    # Multiplication by y on k(x)[y]/(y^n-x/u), basis 1,y,...,y^(n-1).
    matrix=sp.zeros(n)
    for j in range(n-1):
        matrix[j+1,j]=1
    matrix[0,n-1]=x/u
    norm=sp.factor(matrix.det())
    assert sp.cancel(norm-(-1)**(n-1)*x/u) == 0
    norms[str(n)]=str(norm)

result={
    "run_utc":datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    "model":"GPT-6 Astra Pro; effort setting not exposed; run MPL_64_040-077/root",
    "scope":"exact finite enumeration and symbolic polynomial identities; no scan OCR and no transcription edits",
    "M2F2":{
        "GL2_count":len(group), "Vp":sorted(Vp), "W":sorted(W),
        "fixed_vectors_in_W":sorted(fixed_W),
        "verified":"all five assertions on scans042–043 under natural conjugation action; W is F4; self-orthogonal line is relative to W, not all End(V)"
    },
    "rational_map":{
        "A":str(A),"B":str(B),"C":str(C),"F":str(F),
        "hypotheses":"base ring with 2, t, and t-1 invertible",
        "invariant_under_all_three_involutions":True,
        "resultant_A_B":str(sp.factor(sp.resultant(A,B,z))),
        "R_at_0_1_infty_t":[str(v) for v in Rvalues],
        "derivative":str(sp.factor(sp.diff(F,z))),
        "wrong_radical_residue":str(-2*t*(t-1)),
        "iterate_minus_t_numerator":str(sp.factor(num)),
        "iterate_minus_t_denominator":str(sp.factor(den)),
        "t_equals_2_second_iterate_fibre_degree":16,
        "t_equals_2_second_iterate_reduced_support_degree":10,
        "verified":"normalization c_t=t and f_t branch data; source sign slips and n>=2 fibre multiplicities are separate from the correct map"
    },
    "raw_norm_y_for_y_power_n_equals_x_over_u":norms,
    "general_norm_formula":"N(y)=(-1)^(n-1)x/u follows from the constant coefficient of Y^n-x/u; the finite calculations are examples, not the proof for all n"
}
(OUT/"root_checks.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(result,ensure_ascii=False,indent=2))
