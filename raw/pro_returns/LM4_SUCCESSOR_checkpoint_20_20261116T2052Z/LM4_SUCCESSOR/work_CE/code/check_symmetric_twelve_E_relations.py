#!/usr/bin/env python3
"""Twelve exact relations in the original 64 seed + 64 F-image domain.

Columns 0..63 are the raw stored Fox columns, in node_columns order;
columns 64..127 are their actual F images.  Coefficients are on the left
in Z[E], E=R_A x R_B.  This certifies independence and the semilinear F
action on the twelve relations, but does not by itself prove spanning.
"""
from pathlib import Path
from collections import defaultdict
import json, hashlib, time

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / 'work_CE/next_symmetric_nodes'
paths = [P / 'symmetric_paired_fox_data.json', P / 'symmetric_F_node_matching.json',
         P / 'symmetric_F_cycles_and_fixed_chains.json']
raw = [p.read_bytes() for p in paths]
paired, match, halves = [json.loads(r) for r in raw]

def red(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)

def inv(w):
    return tuple(-x for x in reversed(w))

def mul(a, b):
    return red(a[0] + b[0]), red(a[1] + b[1])

def fi(a):
    return a[1], a[0]

def add(d, k, n):
    d[k] += n
    if not d[k]:
        del d[k]

def cell_decode(rows):
    return {(tuple(r['A_vertex']), tuple(r['B_vertex']), r['A_generator'], r['B_generator']):
            r['coefficient'] for r in rows}

def Fchain(c):
    return {(v, u, j, i): -n for (u, v, i, j), n in c.items()}

def shift(c, a):
    return {(red(a[0] + u), red(a[1] + v), i, j): n for (u, v, i, j), n in c.items()}

def vector_add(v, col, a, n):
    add(v, (col, a[0], a[1]), n)

def vector_shift(v, a, n=1):
    out = defaultdict(int)
    for (j, u, w), z in v.items():
        b = mul(a, (u, w))
        vector_add(out, j, b, n*z)
    return dict(out)

def vector_F(v):
    out = defaultdict(int)
    for (j, u, w), z in v.items():
        vector_add(out, j+64 if j < 64 else j-64, (w, u), z)
    return dict(out)

def vector_boundary(v):
    out = defaultdict(int)
    for (j, u, w), n in v.items():
        for cell, z in shift(columns[j], (u, w)).items():
            add(out, cell, n*z)
    return dict(out)

def vector_encode(v):
    return [{'column': j, 'A_word': u, 'B_word': w, 'coefficient': n}
            for (j, u, w), n in sorted(v.items())]

def diagonal(c):
    out = defaultdict(int)
    for (u, v, i, j), n in c.items():
        if u == v and i == j:
            add(out, red(u+(i,)), n)
            add(out, u, -n)
    return {w: n % 2 for w, n in out.items() if n % 2}

start = time.monotonic()
nodes = paired['node_columns']
keys = [(r['loop_index'], r['local_node_index']) for r in nodes]
positions = {k: j for j, k in enumerate(keys)}
base = [cell_decode(r['fox_cells']) for r in nodes]
columns = base + [Fchain(c) for c in base]
lookup = {tuple(r['node_index']): r for r in match['rows']}
fixed_lookup = {tuple(r['node_index']): r for r in halves['fixed_cell_anti_chains']}
relations = {}
rows = []
for k, row in lookup.items():
    if not row['pure_E_coefficient']:
        continue
    mu = tuple(row['physical_F_mate_index'])
    i, j = positions[k], positions[mu]
    eps, eps_mu = row['A_first_orientation_signs']
    delta = eps * eps_mu
    a = (tuple(row['E_coefficient']['A_word']), tuple(row['E_coefficient']['B_word']))
    v = defaultdict(int)
    vector_add(v, 64+i, ((), ()), 1)
    vector_add(v, j, a, delta)
    v = dict(v)
    assert not vector_boundary(v), ('nonzero relation', k)
    relations[k] = v
    rows.append({'node_index': k, 'mate_index': mu, 'seed_column': i, 'F_column': 64+i,
                 'raw_orientation_delta': delta, 'A_first_signs': [eps, eps_mu],
                 'coefficient_a': {'A_word': a[0], 'B_word': a[1]},
                 'relation': vector_encode(v),
                 'semilinear_F_multiplier': {'coefficient': delta, 'A_word': a[1], 'B_word': a[0]}})
assert len(relations) == 12

# The twelve f_nu coordinates are distinct, with coefficient 1 in their
# own relation and 0 in every other relation: this proves independence
# over the entire noncommutative ring Z[E], not only after augmentation.
private_F_columns = [64+positions[k] for k in relations]
assert len(set(private_F_columns)) == 12
for k, v in relations.items():
    for j in private_F_columns:
        terms = {(a, b): n for (col, a, b), n in v.items() if col == j}
        assert terms == ({((), ()): 1} if j == 64+positions[k] else {})

fixed = []
for row in rows:
    k, mu = tuple(row['node_index']), tuple(row['mate_index'])
    a = (tuple(row['coefficient_a']['A_word']), tuple(row['coefficient_a']['B_word']))
    delta = row['raw_orientation_delta']
    assert vector_F(relations[k]) == vector_shift(relations[mu], fi(a), delta), ('F relation', k)
    if k != mu:
        continue
    assert delta == 1 and a[1] == inv(a[0])
    r = a[0]
    # t=(r^-1,1); e=t*a=(1,r^-1).  Thus K=t*R is F-fixed,
    # and K=(1+F)(e*e_nu) in the original induced domain.
    t = (inv(r), ())
    e = ((), inv(r))
    K = vector_shift(relations[k], t)
    assert vector_F(K) == K
    p = {(positions[k], e[0], e[1]): 1}
    norm_p = defaultdict(int, p)
    for q, n in vector_F(p).items():
        add(norm_p, q, n)
    assert dict(norm_p) == K
    anti = vector_boundary(p)
    assert Fchain(anti) == {q: -n for q, n in anti.items()}
    stored = cell_decode(fixed_lookup[k]['actual_anti_chain'])
    assert anti == stored
    fixed.append({'node_index': k, 'fixed_kernel_generator': vector_encode(K),
                  'primitive_in_induced_domain': vector_encode(p),
                  'norm_equation': '(1+F)p=K',
                  'Tate_diagonal': [{'word': w, 'coefficient_F2': n} for w, n in sorted(diagonal(anti).items())],
                  'source_left_ideal_zero_witnesses': fixed_lookup[k]['source_left_ideal_zero_witnesses']})
assert len(fixed) == 4
orbits = []
seen = set()
for row in rows:
    k, mu = tuple(row['node_index']), tuple(row['mate_index'])
    if k in seen:
        continue
    seen.update((k, mu))
    orbits.append({'nodes': [k] if k == mu else [k, mu],
                   'type': 'fixed signed-coefficient summand' if k == mu else 'exchanged induced summand'})
assert sum(len(x['nodes']) == 2 for x in orbits) == 4

out = {'scope': __doc__, 'input_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(r).hexdigest()
           for p, r in zip(paths, raw)},
       'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'column_order': [{'column': j, 'kind': 'seed' if j < 64 else 'F(seed)',
                         'node_index': keys[j % 64]} for j in range(128)],
       'common_R_basis': match['common_R_basis'], 'relations': rows, 'F_orbits': orbits,
       'fixed_generators_and_connecting_classes': fixed,
       'independence_certificate': {'private_unit_F_columns': private_F_columns,
                                    'argument': 'Distinct private F-column with coefficient1 in each relation.'},
       'conditional_scope': 'If these12 generate the full128-column kernel, its H^2 image consists exactly of the four displayed source-generated ideals. Spanning is not asserted here.',
       'excluded_claims': ['full kernel spanning without the separate elimination certificate',
                           'full old-base/deck orbit exhaustion', 'I=R'],
       'elapsed_seconds': time.monotonic()-start}
(P / 'symmetric_twelve_E_relations.json').write_text(json.dumps(out, indent=2)+'\n')
for row in rows:
    print('PASS original-domain relation', row['node_index'], 'mate', row['mate_index'],
          'delta', row['raw_orientation_delta'], 'F-column', row['F_column'])
print('PASS12 E-independent exact relations, four exchanged F-orbits, four fixed generators and actual source connecting classes; elapsed', round(out['elapsed_seconds'], 3))
