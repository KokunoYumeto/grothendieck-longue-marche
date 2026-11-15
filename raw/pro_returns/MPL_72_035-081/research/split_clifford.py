#!/usr/bin/env python3
"""Exact integral matrix checks for the split B12 construction; no source edits."""
from pathlib import Path
import json
import sympy as s

OUT = Path(__file__).resolve().parent
I = s.eye(2)
D = s.diag(1, -1)
Y = s.Matrix([[0, 1], [0, 0]])
Z = s.Matrix([[0, 0], [1, 0]])
zero = s.zeros(2)
checks = {}
for name, value in {
    "x_square": D*D-I, "y_square": Y*Y, "z_square": Z*Z,
    "xy_anticommutator": D*Y+Y*D, "xz_anticommutator": D*Z+Z*D,
    "yz_anticommutator": Y*Z+Z*Y-I,
}.items():
    checks[name] = value == zero
x,y,z = s.symbols("x y z")
checks["generic_square"] = s.simplify((x*D+y*Y+z*Z)**2-(x*x+y*z)*I) == zero
basis = [I,D*Y,D*Z,Y*Z]
flatten = lambda m: s.Matrix(list(m))
P = s.Matrix.hstack(*(flatten(m) for m in basis))
checks["even_basis_is_integral_basis"] = abs(P.det()) == 1
table=[]
for u in range(4):
    for v in range(4):
        coefficients = P.inv()*flatten(basis[u]*basis[v])
        rebuilt = sum((coefficients[k]*basis[k] for k in range(4)), s.zeros(2))
        assert rebuilt == basis[u]*basis[v]
        table.append({"left":u,"right":v,"coefficients":list(map(int,coefficients))})
a,b,c,d = s.symbols("a b c d")
checks["coefficient_inverse"] = d*basis[0]+b*basis[1]-c*basis[2]+(a-d)*basis[3] == s.Matrix([[a,b],[c,d]])
units=[]
for i in range(2):
    for j in range(2):
        m=s.zeros(2);m[i,j]=1;units.append(m)
actions=[]
for A in units:
    for B in units:
        action=s.Matrix.hstack(*(flatten(A*T*B) for T in units))
        actions.append(flatten(action))
action_basis=s.Matrix.hstack(*actions)
checks["azumaya_action_integral_basis"] = abs(action_basis.det()) == 1
checks["sixteen_products"] = len(table)==16
assert all(checks.values()), checks
result={"status":"PASS","coefficient_ring":"Z, then arbitrary base change","checks":checks,
        "even_basis_determinant":int(P.det()),"azumaya_action_determinant":int(action_basis.det()),
        "multiplication_table":table,"matrix_unit_actions":16}
(OUT/"split_clifford_results.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"status":"PASS","checks":len(checks),"products":16,"matrix_unit_actions":16}))
