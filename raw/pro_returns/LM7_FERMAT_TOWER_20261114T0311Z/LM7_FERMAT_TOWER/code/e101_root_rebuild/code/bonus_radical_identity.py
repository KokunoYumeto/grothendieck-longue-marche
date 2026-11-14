"""Exact signed radical identity supporting the next upper-unit calculation."""
import json
import e_unit_norm_complete as m

F = m.Field([289, 0, 0, 17, 0, 0, 1])
b = F.elt([0, 1])
z = F.scale(F.pow(b, 3), m.Q(1, 17))
d, _ = m.records('e_unit_norm_scalar')
e1, e2 = [F.elt([m.Q(a, den) for a, den in row]) for row in d['lower_units']]
eps = F.mul(e1, e2)
c1 = F.add(F.add(b, F.one), F.scale(z, 3))
signed = F.mul(eps, F.pow(c1, 3))
assert signed == F.add(F.one, F.scale(z, 2))
target = F.mul(z, signed)
assert target == F.sub(F.pow(z, 2), F.one)
print(json.dumps({'status': 'PASS',
                  'signed_identity': '(e1*e2)*c1^3 = 1+2*zeta',
                  'norm_target_identity': '(zeta*e1*e2)*c1^3 = zeta^2-1',
                  'signed_coefficients': [str(x) for x in signed],
                  'target_coefficients': [str(x) for x in target]}, indent=2))
