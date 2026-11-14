"""Exact staged source involution and original-basepoint path certificate."""

from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json
import sympy as S

import cross_divisor_monodromy_f20 as gr

z, s = S.symbols("z s")
Phi = S.Poly(z**4+z**3+z**2+z+1, z)
checks = []


def residue(expression):
    n, _ = S.fraction(S.cancel(S.together(expression)))
    return S.rem(S.Poly(S.expand(n), z), Phi).as_expr()


def identity(name, expression):
    value = residue(expression)
    assert value == 0, (name, value)
    checks.append({"name": name, "type": "rational_identity", "residue": "0"})


h = z*z/s
a = (z-s)/(z+s)
identity("source involution squares to identity", h.subs(s,h)-s)
identity("positive new track becomes negative", a.subs(s,h)+a)
identity("common retained square unchanged", a.subs(s,h)**2-a*a)
permutation = []
for j in range(5):
    jj = (2-j) % 5
    u, up = z**j, z**jj
    v = ((u-s)/(u+s))**2
    vp = ((up-s)/(up+s))**2
    identity(f"old label {j} becomes {jj}", v.subs(s,h)-vp)
    permutation.append(jj)
    if j == 1:
        continue
    outer = u*(2*z-u)
    inner = z*u*u/(2*u-z)
    outer_p = up*(2*z-up)
    inner_p = z*up*up/(2*up-z)
    identity(f"positive collision {j} becomes negative {jj}", z**4/outer-inner_p)
    identity(f"negative collision {j} becomes positive {jj}", z**4/inner-outer_p)

nf, C = gr.nf, gr.C
source0 = C(0,nf.THETA**2-2)*nf.ZETA
source1 = nf.ZETA**2*gr.cinv(source0)
vertices = [source0, source0+C(0,6), source1+C(0,6), source1]
old_punctures = [C(0)] + [sign*root for sign in (1,-1) for root in nf.ROOTS]
collision_squares = []
for j in (0,2,3,4):
    u = nf.ROOTS[j]
    collision_squares += [(j,1,u*(2*nf.ZETA-u)),
                          (j,-1,nf.ZETA*u*u*gr.cinv(2*u-nf.ZETA))]
for endpoint, point in enumerate((source0, source1)):
    x = point.re
    assert x.sign() != 0
    for j, puncture in enumerate(old_punctures):
        value = x-puncture.re
        assert value.sign() != 0
        checks.append({"name": f"vertical line {endpoint}: old puncture {j}",
                       "type": "nonzero_real_part_gap", "value": value.encoded()})
    for j, eps, value in collision_squares:
        polynomial = 4*x**4-4*value.re*x*x-value.im*value.im
        assert polynomial.sign() != 0
        checks.append({"name": f"vertical line {endpoint}: collision square {j},{eps}",
                       "type": "nonzero_vertical_line_quadratic_test", "value": polynomial.encoded()})
    height = point.im+6-2
    assert height.sign() > 0
    checks.append({"name": f"middle segment endpoint {endpoint} above radius two",
                   "type": "positive_height_margin", "value": height.encoded()})
for j, eps, value in collision_squares:
    margin = 16-(value*value.conjugate()).re
    assert margin.sign() > 0
    checks.append({"name": f"collision roots {j},{eps} inside radius two",
                   "type": "positive_fourth_power_radius_margin", "value": margin.encoded()})

producer = Path(__file__).resolve()
output = producer.with_name("source_sign_symmetry_stage_output.json")
record = {"status": "PASS_EXACT_STAGE_PENDING_GROUP_AUDIT",
          "producer_sha256": hashlib.sha256(producer.read_bytes()).hexdigest(),
          "old_label_permutation": permutation,
          "source_basepoint": source0.encoded(), "image_basepoint": source1.encoded(),
          "based_transport_vertices": [point.encoded() for point in vertices],
          "check_count": len(checks), "checks": checks}
output.write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({"status": record["status"], "checks": len(checks),
                  "output": output.name,
                  "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest()},indent=2))
