"""Direct tuple substitution for the coordinate example on 151_scan003.

This is a check of that example only, not a proof of its proposed abstract
axiomatization. Inputs were transcribed from visually inspected crops.
Composition is read right to left. No image recognition is involved.
"""
from pathlib import Path
import json
from datetime import datetime, timezone

W = Path(__file__).resolve().parents[1]
maps = {
    'p0': lambda t: (t[0],),
    'p1': lambda t: (t[1],),
    'd0': lambda t: (t[0], t[0]),
    'd1': lambda t: (t[1], t[0], t[0]),
    'd2': lambda t: (t[0], t[1], t[0]),
    'd3': lambda t: (t[0], t[0], t[1]),
    'p12': lambda t: (t[0], t[1]),
    'p23': lambda t: (t[1], t[2]),
    'p31': lambda t: (t[2], t[0]),
    'rho': lambda t: (t[1], t[2], t[0]),
    'rho2': lambda t: (t[2], t[0], t[1]),
    's': lambda t: (t[1], t[0]),
    's1': lambda t: (t[0], t[2], t[1]),
    's2': lambda t: (t[2], t[1], t[0]),
    's3': lambda t: (t[1], t[0], t[2]),
    'id': lambda t: t,
}

def evaluate(expression, arguments):
    result = tuple(arguments)
    for name in reversed(expression.split()):
        result = maps[name](result)
    return result

specs = [
    ('p1=p0 sigma', 'xy', ['p1', 'p0 s'], True),
    ('p0=p1 sigma', 'xy', ['p0', 'p1 s'], True),
    ('p23 cyclic', 'xyz', ['p23', 'p12 rho'], True),
    ('p31 cyclic', 'xyz', ['p31', 'p23 rho', 'p12 rho2'], True),
    ('p12 cyclic', 'xyz', ['p12', 'p31 rho', 'p23 rho2'], True),
    ('sigma p12', 'xyz', ['s p12', 'p12 s3'], True),
    ('sigma p23', 'xyz', ['s p23', 'p23 s1'], True),
    ('sigma p31', 'xyz', ['s p31', 'p31 s2'], True),
    ('delta1 cyclic', 'xy', ['d1', 'rho d2', 'rho2 d3'], True),
    ('delta2 cyclic', 'xy', ['d2', 'rho d3', 'rho2 d1'], True),
    ('delta3 cyclic', 'xy', ['d3', 'rho d1', 'rho2 d2'], True),
    ('p0 delta0', 'x', ['p0 d0', 'id'], True),
    ('sigma delta0', 'x', ['s d0', 'd0'], True),
    ('delta0 p0 chain', 'xy', ['d0 p0', 'p12 d3', 'p23 d1', 'p31 d2'], True),
    ('three-value box: delta0 p0', 'xy', ['d0 p0', 'p12 rho d1'], True),
    ('three-value box: id E1', 'xy', ['id', 'p12 rho2 d1'], True),
    ('three-value box: sigma', 'xy', ['s', 'p12 d1'], True),
    ('literal marginal sigma3 delta1=delta1', 'xy', ['s3 d1', 'd1'], False),
    ('refinement: sigma3 delta1=delta2', 'xy', ['s3 d1', 'd2'], True),
    ('refinement: sigma1 delta1=delta1', 'xy', ['s1 d1', 'd1'], True),
    ('bottom boxed diagonal identity', 'x', ['rho d1 d0', 's1 d1 d0', 'd1 d0'], True),
    ('bottom underbrace p31', 'xyz', ['p12 rho2', 'p31'], True),
    ('literal bottom overbrace p12', 'xyz', ['p12 rho2 s2', 'p12'], False),
    ('refinement: first-and-third projection', 'xyz', ['p12 rho2 s2', 's p31'], True),
    ('bottom full equality after p0', 'xyz', ['p0 p12', 'p0 p12 rho2 s2'], True),
    ('005 last formula with sigma1', 'xyz', ['p0 p12 s1', 'p0 p12'], True),
    ('005 rejected alternative sigma3 in last formula', 'xyz', ['p0 p12 s3', 'p0 p12'], False),
    ('005 involution caption', 'xy', ['s s', 'id'], True),
    ('005 idempotent caption', 'xy', ['d0 p0 d0 p0', 'd0 p0'], True),
]
rows = []
for label, arguments, expressions, expected in specs:
    values = [evaluate(expr, arguments) for expr in expressions]
    equal = len(set(values)) == 1
    assert equal == expected, (label, values)
    rows.append({'claim': label, 'arguments': list(arguments), 'expressions': expressions,
                 'values': values, 'equal': equal})

report = {
    'time_utc': datetime.now(timezone.utc).isoformat(),
    'scope': 'The explicit coordinate realization, with p0 the first coordinate, p1 the second, delta0 duplication, sigma the two-coordinate swap, and sigma_i the swap of the other two coordinates. No abstract presentation theorem is checked.',
    'rows': rows,
}
(W / 'records' / '151_coordinate_computation.json').write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(f'{len(rows)} tuple checks completed; {sum(not r["equal"] for r in rows)} literal equalities fail in the coordinate model.')
