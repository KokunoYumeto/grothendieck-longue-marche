#!/usr/bin/env python3
"""Independent reconstruction of the two specified whole-G modules.

No DE producer is imported.  Product-tree chains are integrated at B
steps, independently of the producer's A-step integration.  All words,
boundaries, F images, normalized terms and augmented unit rows are checked.
This does not test any further old-base word or any whole preceding sum.
"""
from pathlib import Path
from collections import defaultdict
import hashlib, json, time

ROOT = Path(__file__).resolve().parents[2]
paths = [ROOT/'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json',
         ROOT/'work_DE/next_marginal_source/odd_G_overlap.json']
raw = [p.read_bytes() for p in paths]
D, cert = map(json.loads, raw)
start = time.monotonic()

def reduce_word(w):
    s = []
    for x in w:
        if s and s[-1] == -x: s.pop()
        else: s.append(int(x))
    return tuple(s)

def inverse(w): return tuple(-x for x in reversed(w))

def apply(w, action):
    return reduce_word(y for x in w for y in
                       (action[abs(x)] if x > 0 else inverse(action[abs(x)])))

def mapping(d): return {int(k): tuple(v) for k, v in d.items()}

def add(d, k, n):
    d[k] += n
    if not d[k]: del d[k]

# A residual generator is represented by its literal retained word and
# physical paired slot; no numerical Schreier-ID alignment is assumed.
def cancel(w):
    s = []
    for x in w:
        if s and s[-1] == (-x[0], x[1], x[2]): s.pop()
        else: s.append(x)
    return tuple(s)

retained = D['retained_paired_indices']
head_id = {j: i+1 for i, j in enumerate(retained)}
beta = mapping(D['retained_involution'])
F = mapping(D['paired_involution'])
A = mapping(D['old_actions'][1]['based_pullback_paired'])
Ainv = mapping(D['old_actions'][1]['geometric_push_paired'])

def split_word(w):
    t = (); out = []
    for x in w:
        j, sign = abs(x), 1 if x > 0 else -1
        if j in head_id:
            t = reduce_word(t+(sign*head_id[j],))
        elif j < 12: out.append((0, (sign, t, j)))
        else: out.append((1, (sign, apply(t, beta), j-10)))
    assert not t
    return out

def integrate_at_B_steps(w):
    a = (); b = (); c = defaultdict(int); edges = defaultdict(int)
    for side, x in split_word(w):
        if side == 0:
            an = cancel(a+(x,))
            add(edges, (0, a if x[0] > 0 else an, b, x[1:]), x[0])
            a = an
        else:
            bn = cancel(b+(x,)); bv = b if x[0] > 0 else bn
            add(edges, (1, a, bv, x[1:]), x[0])
            u = ()
            for y in a:
                un = cancel(u+(y,)); av = u if y[0] > 0 else un
                add(c, (av, bv, y[1:], x[1:]), y[0]*x[0])
                u = un
            b = bn
    assert not a and not b
    boundary = defaultdict(int)
    for (u, v, i, j), n in c.items():
        add(boundary, (0, u, v, i), n)
        add(boundary, (0, u, cancel(v+((1, *j),)), i), -n)
        add(boundary, (1, cancel(u+((1, *i),)), v, j), n)
        add(boundary, (1, u, v, j), -n)
    assert dict(boundary) == dict(edges)
    return dict(c)

def normalize(c):
    out = defaultdict(int)
    for (u, v, (g, i), (h, j)), n in c.items():
        z = reduce_word(inverse(apply(g, beta))+h)
        add(out, ((i, j, z), (u, v, g)), n)
    return dict(out)

meta = {int(k): (tuple(v['retained_word']), v['paired_slot'])
        for k, v in cert['common_R_basis'].items()}

def decode_R(w):
    return cancel((1 if x > 0 else -1, *meta[abs(x)]) for x in w)

def decode_terms(terms):
    out = defaultdict(int)
    for x in terms:
        r, a = x['row'], x['G_coefficient']
        key = ((r['A_slot'], r['B_slot'], tuple(r['relative_retained_word'])),
               (decode_R(a['A_word']), decode_R(a['B_word']), tuple(a['retained_word'])))
        add(out, key, x['coefficient'])
    return dict(out)

for j in range(1, 22):
    assert apply(A[j], Ainv) == apply(Ainv[j], A) == (j,)
    assert apply(F[j], F) == (j,)

assert len(cert['columns']) == 128
rows = []; units = []; parity_changes = []; allterms = 0
for index, rec in enumerate(cert['columns']):
    layer, number = divmod(index, 64)
    node = D['node_columns'][number]
    assert rec['layer'] == layer
    assert tuple(rec['node']) == (node['loop_index'], node['local_node_index'])
    baseword = tuple(node['paired_relator'])
    word = baseword if layer == 0 else apply(baseword, A)
    assert word == tuple(rec['paired_relator'])
    c = integrate_at_B_steps(word)
    Fc = integrate_at_B_steps(apply(word, F))
    assert Fc == {(v, u, j, i): -n for (u, v, i, j), n in c.items()}
    norm = normalize(c)
    assert norm == decode_terms(rec['terms'])
    aug = defaultdict(int)
    for (row, coefficient), n in norm.items(): add(aug, (row, coefficient[2]), n)
    assert len(aug) == 1
    (row, t), sign = next(iter(aug.items()))
    assert sign in (-1, 1)
    assert row == (rec['augmented_row'][0], rec['augmented_row'][1], tuple(rec['augmented_row'][2]))
    assert t == tuple(rec['augmented_unit']) and sign == rec['augmented_sign']
    rows.append(row); units.append((t, sign)); allterms += len(c)
    if layer:
        old = rows[number]
        assert row[:2] == old[:2]
        parity = tuple((sum(abs(x) == j for x in row[2])+sum(abs(x) == j for x in old[2])) % 2
                       for j in range(1, 6))
        assert parity == (1, 0, 0, 0, 0)
        parity_changes.append(parity)
    if number == 63: print('PASS independent B-step reconstruction of layer', layer, flush=True)

assert len(set(rows)) == 128
assert cert['collision_count'] == 0 and cert['remaining_augmented_unit_columns'] == 128
out = {'scope': __doc__, 'input_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(b).hexdigest()
                                        for p, b in zip(paths, raw)},
       'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'columns_checked': 128, 'actual_boundaries_checked': 256,
       'full_F_chain_identities': 128, 'full_G_term_count': allterms,
       'distinct_augmented_rows': len(set(rows)), 'cross_sheet_collisions': 0,
       'all64_relative_retained_parity_changes': [1, 0, 0, 0, 0],
       'whole_coefficient_consequence': 'B94 separated filtration gives intersection zero and free-G rank128 direct sum',
       'excluded': ['further old-base translates', 'whole previous sum overlaps', 'global kappa vanishing', 'I=R'],
       'elapsed_seconds': time.monotonic()-start}
target = ROOT/'work_CE/next_symmetric_nodes/cross_sheet_overlap_independent_review.json'
target.write_text(json.dumps(out, indent=2)+'\n')
print('PASS all128 literal chains, boundaries, F images, G coefficients and distinct unit rows;',
      'seconds', round(out['elapsed_seconds'], 3), flush=True)
