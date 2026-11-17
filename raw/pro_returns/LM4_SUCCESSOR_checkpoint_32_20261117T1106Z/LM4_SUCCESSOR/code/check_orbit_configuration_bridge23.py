"""Check the obstruction to a literal orbit-configuration shortcut for Z.

This rejects only the proposed identification in the actual (v,w)
coordinates. It makes no claim about arbitrary changes of model.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
u, x = s.symbols('u x')
phi = u**4 + u**3 + u**2 + u + 1
M1 = s.Matrix([[0, u], [1, 0]])
M2 = s.Matrix([[1-u, u], [1, 0]])
translation = s.Matrix([[1, 1-u], [0, 1]])
assert M1 * M1 == u * s.eye(2)
assert M2 * M1 == u * translation
assert s.cancel((1-u) + u/(u/x) - (x+1-u)) == 0

v, w = s.Integer(10), 11-u
q = s.expand(v*w)
factors = {'v': v, 'w': w, 'v-1': v-1, 'w-1': w-1, 'v-w': v-w}
for j in range(5):
    root = u**j
    factors[f'q-u^{j}'] = q-root
    factors[f'v-u^{j}'] = v-root
    factors[f'w-u^{j}'] = w-root
    if j:
        factors[f'q+(u^{j}-1)v-u^{j}'] = q+(root-1)*v-root
        factors[f'q+(u^{j}-1)w-u^{j}'] = q+(root-1)*w-root
remainders = {name: s.rem(s.expand(value), phi, u) for name, value in factors.items()}
assert all(value != 0 for value in remainders.values())
assert s.expand(w-(v+1-u)) == 0

out = {
    'status': 'PASS',
    'completed_at': datetime.now(timezone.utc).isoformat(),
    'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'coefficient_field': 'Q(u), u a primitive fifth root; minimal polynomial u^4+u^3+u^2+u+1',
    'two_deleted_graph_maps': ['g1(x)=u/x', 'g2(x)=1-u+u/x'],
    'composition': 'g2*g1(x)=x+1-u, an infinite-order nonidentity translation',
    'point': {'v': str(v), 'w': str(w), 'q': str(q)},
    'all_actual_deleted_factors_nonzero': {name: str(value) for name, value in remainders.items()},
    'point_in_actual_Z': True,
    'point_excluded_by_orbit_relation_of_generated_maps': True,
    'scope': 'The actual finite forbidden-map family is not the orbit relation of a Mobius group in these coordinates. No arbitrary topological or birational replacement is refuted.',
}
(ROOT / 'records/orbit_configuration_bridge23.json').write_text(json.dumps(out, indent=2)+'\n')
print('PASS the two actual deleted graph maps compose to a nonidentity translation.')
print('PASS the exact point (10,11-u) satisfies every actual Z nonvanishing condition.')
print('PASS that point belongs to the generated orbit relation; the literal shortcut fails.')
print('No claim about an arbitrary alternative configuration model or either main decision.')
