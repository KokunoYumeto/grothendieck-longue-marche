"""Exact local U7/Q7 counterexample to bad-prime cusp recognition.

This verifies the Hensel data and finite Kummer obstruction in A.55.
The resulting section is an actual local point section; no global lift
to the full fundamental group is claimed.
"""
import json
import sympy as s

z=s.symbols("z")
F=s.Poly(s.expand(((4+7*z)**7+129)/49),z,domain=s.ZZ)
assert s.Poly(F,z,modulus=7)==s.Poly(z+1,z,modulus=7)
assert int(F.diff().eval(6))%7==1

# Hensel lift z through six base-seven digits, using only integer arithmetic.
root=6
modulus=7
digits=[root]
for _ in range(5):
    candidates=[root+modulus*d for d in range(7)
                if int(F.eval(root+modulus*d))%(7*modulus)==0]
    assert len(candidates)==1
    root=candidates[0]
    modulus*=7
    digits.append(root)
y=4+7*root
assert (y**7+129)%(49*modulus)==0

cubes=sorted({pow(a,3,7) for a in range(1,7)})
assert cubes==[1,6]
t=-128
u=129
assert t+u==1
assert t%7 not in cubes and u%7 not in cubes
ratio=(u*pow(t,-1,7))%7
assert ratio==2 and ratio not in cubes
discrete_log={pow(3,e,7):e%3 for e in range(6)}
pair=(discrete_log[t%7],discrete_log[u%7])
assert pair==(2,1)
cusp_lines={"0":{(e,0) for e in range(3)},
            "1":{(0,e) for e in range(3)},
            "infinity":{(e,e) for e in range(3)}}
assert all(pair not in line for line in cusp_lines.values())

print(json.dumps({
    "curve":"X^7+Y^7+Z^7=0 over Q7",
    "local_point":"[2:y:1], y^7=-129, y congruent46 modulo49",
    "hensel_polynomial":str(F.as_expr()),
    "hensel_reduction_mod7":"z+1", "hensel_derivative_mod7":1,
    "successive_z_lifts":digits,
    "final_y_residue":y,"verified_y_equation_modulus":49*modulus,
    "tripod_coordinates":[t,u],"unit_residues_mod7":[t%7,u%7],
    "cubes_in_F7_units":cubes,"ratio_residue_mod7":ratio,
    "Kummer_pair_in_F3_squared":pair,
    "cusp_lines_in_F3_squared":{k:sorted(v) for k,v in cusp_lines.items()},
    "status":"PASS",
    "scope":"full local point section; intrinsically ramified at7; noncuspidal in pro3; no global full-section lift asserted"
},indent=2))
