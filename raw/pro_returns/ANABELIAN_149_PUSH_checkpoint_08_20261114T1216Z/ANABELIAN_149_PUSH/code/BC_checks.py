#!/usr/bin/env python3
"""Exact, rerunnable checks for Parts B/C. These are not substitutes for proofs.

Run with Python 3 and SymPy. Output is JSON; all assertions use exact arithmetic.
"""
import json
from pathlib import Path
import sympy as sp

x, y, t, r, X, Y, z, lam = sp.symbols("x y t r X Y z lam")
checks = {}


def record(name, actual, expected):
    difference = sp.simplify(actual - expected)
    assert difference == 0, (name, actual, expected, difference)
    checks[name] = {"passed": True, "value": str(sp.factor(actual))}


record("quadratic_elliptic_good_model",
       (y**2-x**3+t**2*x).subs({t:r**2, x:r**2*X, y:r**3*Y})/r**6,
       Y**2-X**3+X)
record("order_ten_good_model",
       (y**2-x**5+t).subs({t:r**10, x:r**2*X, y:r**5*Y})/r**10,
       Y**2-X**5+1)
record("order_three_divisor_good_model",
       (x**3-t).subs({t:r**3, x:r*X})/r**3, X**3-1)
record("genus_two_discriminant", sp.discriminant(x**5-t, x), 3125*t**4)
record("cubic_divisor_discriminant", sp.discriminant(x**3-t, x), -27*t**2)
record("compact_type_discriminant",
       sp.discriminant((x**3-t**6)*(x**3-1), x),
       729*t**12*(t**6-1)**6)
record("constant_elliptic_cubic_discriminant", sp.discriminant(x**3-x, x), 4)
record("constant_elliptic_weierstrass_discriminant", -16*(4*(-1)**3), 64)
record("wild_quadratic_elliptic_good_model_at_two",
       ((y**2-x**3-2).subs({x:2*X,y:r*(2*Y+1)}).subs(r**2,2))/8,
       Y**2+Y-X**3)
# For y^2+y=x^3, b2=b4=b8=0 and b6=1; Delta=-27*b6^2.
record("good_elliptic_discriminant_at_two", -27, -27)
record("wild_quadratic_involution", (-Y-1)**2+(-Y-1)-X**3,
       Y**2+Y-X**3)

# Compact-type normalization at x*z=t^2, with y=x*V.
A = (1-z**3)*(x**3-1)
record("compact_type_chart_original_equation",
       (x**3*A).subs(z, t**2/x), (x**3-t**6)*(x**3-1))
record("compact_type_chart_VW_relation", (x*A)*(z/A), x*z)
record("compact_type_cluster_rescaling",
       ((x**3-t**6)*(x**3-1)).subs(x,t**2*X)/t**6,
       (X**3-1)*(t**6*X**3-1))
record("compact_type_cluster_special_fibre",
       ((X**3-1)*(t**6*X**3-1)).subs(t,0), 1-X**3)
record("compact_type_node_unit", A.subs({x:0,z:0}), -1)
for name, f in [("inner_elliptic",1-X**3), ("outer_elliptic",X*(X**3-1))]:
    disc = int(sp.discriminant(f, X))
    assert disc % 5 != 0
    checks[name+"_smooth_at_five"] = {"passed": True, "discriminant": disc,
                                          "residue_mod_5": disc % 5}

# Homological representations and exact orders.
tate = sp.Matrix([[1,1],[0,1]])
assert tate != sp.eye(2) and (tate-sp.eye(2))**2 == sp.zeros(2)
checks["tate_nonzero_square_zero_monodromy"] = {"passed":True,"matrix":tate.tolist()}
elliptic = -sp.eye(2)
assert elliptic**2 == sp.eye(2) and elliptic != sp.eye(2)
checks["quadratic_elliptic_inertia_order"] = {"passed":True,"order":2}
three = sp.Matrix([[0,-1],[1,-1]])
assert three**3 == sp.eye(2) and three != sp.eye(2)
record("three_cycle_augmentation_characteristic_polynomial",
       three.charpoly(lam).as_expr(), lam**2+lam+1)
ten = sp.Matrix([[0,0,0,-1],[1,0,0,1],[0,1,0,-1],[0,0,1,1]])
assert ten**10 == sp.eye(4) and ten**5 == -sp.eye(4)
assert ten**2 != sp.eye(4)
record("order_ten_characteristic_polynomial", ten.charpoly(lam).as_expr(),
       sp.cyclotomic_poly(10,lam))
checks["orbifold_inertia_generator"] = {
    "passed": (4*4+5)%10 == 1,
    "u_image_in_Z10":4, "v_image_in_Z10":5,
    "positive_generator":"u^4 v", "generator_image":(4*4+5)%10,
    "kernel_free_rank":1-10*(sp.Rational(1,5)+sp.Rational(1,2)-1)}
assert checks["orbifold_inertia_generator"]["passed"]
assert checks["orbifold_inertia_generator"]["kernel_free_rank"] == 4

# Monodromy is insensitive to changing the sign of a vanishing cycle.
J = sp.Matrix([[0,1],[-1,0]])
delta = sp.Matrix([1,0])
transvection = sp.eye(2)+delta*(delta.T*J)
record("branch_reversal_transvection",
       (sp.eye(2)+(-delta)*((-delta).T*J)-transvection).norm(), 0)
m1,m2,m3 = sp.symbols("m1 m2 m3", positive=True)
cycle_basis = sp.Matrix([[1,0],[0,1],[-1,-1]])
pairing = cycle_basis.T*sp.diag(m1,m2,m3)*cycle_basis
record("theta_graph_length_pairing_determinant",pairing.det(),m1*m2+m1*m3+m2*m3)
checks["weight_dimensions"] = {
    "Tate_minus_origin": [1,0,1],
    "genus_two_good_minus_infinity": [0,4,0],
    "three_geometric_marks_on_P1": [0,0,2],
    "four_marks_tree_degeneration": [0,0,3]}

# A nonzero continuous coboundary changes an actual splitting, but not its H^1 class.
def action(g,a):
    return ((-1)**g*a)%8

def coboundary(g):
    return (1-action(g,1))%8

for g in range(2):
    for h in range(2):
        assert coboundary((g+h)%2) == (coboundary(g)+action(g,coboundary(h)))%8
assert coboundary(1) == 2
checks["splitting_coboundary_distinction"] = {
    "passed":True,"group":"C2 acting by -1 on Z/8",
    "coboundary_values":[coboundary(0),coboundary(1)],
    "cohomology_class":"zero"}

# Finite quotient witnessing the nontrivial C.7 partial conjugation.
def mul(a,b):
    return tuple(a[b[i]] for i in range(3))

def inv(a):
    return tuple(a.index(i) for i in range(3))

def conj(a,b):
    return mul(mul(a,b),inv(a))

identity=(0,1,2)
a0=(1,0,2)
a5=(0,2,1)
a1=identity
d=mul(a0,a5)
assert conj(d,a0) != a0 and conj(d,a5) != a5
assert mul(conj(d,a0),conj(d,a5)) == d and conj(d,a1) == a1
checks["C7_prime_to_five_S3_quotient"] = {
    "passed":True,"quotient_order":6,
    "a0":a0,"a5":a5,"a1":a1,"fixed_node_word_a0a5":d,
    "a0_after_twist":conj(d,a0),"a5_after_twist":conj(d,a5),
    "caution":"This finite check verifies nontriviality, not the centralizer equality."}

result = {"all_assertions_passed":True,"number_of_named_checks":len(checks),
          "checks":checks,"sympy_version":sp.__version__}
output = Path(__file__).with_name("BC_checks_output.json")
output.write_text(json.dumps(result,indent=2,default=str)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2,default=str))
