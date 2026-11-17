#!/usr/bin/env python3
"""Two prescribed S3 detectors; no group enumeration or census."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
identity = (1, 2, 3)
c = (2, 1, 3)             # (1 2)
t = (2, 3, 1)             # (1 2 3)

def mul(p, q):
    """Functional composition: q first, then p."""
    return tuple(p[x - 1] for x in q)

def inv(p):
    out = [0] * len(p)
    for i, x in enumerate(p, 1):
        out[x - 1] = i
    return tuple(out)

def comm(p, q):
    return mul(mul(mul(p, q), inv(p)), inv(q))

assert mul(c, c) == identity
assert mul(mul(t, t), t) == identity
assert t != identity
assert mul(mul(c, t), c) == inv(t)

# D_minus: R_minus via geometric base winding to <t>,
#          R_plus via orientation to <c>.
# D_plus:  the reflected assignments. Each kills K at both vertices.
maps = {
    'D_minus': {'c_minus': identity, 'k_minus': t,
                'c_plus': c, 'k_plus': identity},
    'D_plus': {'c_minus': c, 'k_minus': identity,
               'c_plus': identity, 'k_plus': t},
}
rows = {}
for name, d in maps.items():
    rows[name] = {
        'assigned_images': d,
        'r_minus=[c_plus,k_minus]': comm(d['c_plus'], d['k_minus']),
        'r_plus=[c_minus,k_plus]': comm(d['c_minus'], d['k_plus']),
    }
assert rows['D_minus']['r_minus=[c_plus,k_minus]'] == t
assert rows['D_minus']['r_plus=[c_minus,k_plus]'] == identity
assert rows['D_plus']['r_minus=[c_plus,k_minus]'] == identity
assert rows['D_plus']['r_plus=[c_minus,k_plus]'] == t

result = {
    'status': 'PASS',
    'permutation_convention': 'one-line images, functional composition q then p',
    'c': c, 't': t, 'identity': identity,
    'maps': rows,
    'geometric_input': 'Each vertex has its actual integer base winding and its orientation character; K is fiberwise and even.',
    'conclusion': 'Each cross relator survives a finite quotient killing the other; the same holds modulo the other closed normal closure in the full completion.',
    'scope': 'Exactly two prescribed maps to S3; no claim about the quotient after both relators or its centralizer.',
}
target = ROOT / 'work_A/B114_cross_relators23.json'
target.write_text(json.dumps(result, indent=2) + '\n')
print('PASS c^2=1, t^3=1, ctc=t^-1, [c,t]=t != 1')
print('PASS D_minus: (r_minus,r_plus)=(t,1)')
print('PASS D_plus:  (r_minus,r_plus)=(1,t)')
print('PASS two independent finite detectors; no census')
