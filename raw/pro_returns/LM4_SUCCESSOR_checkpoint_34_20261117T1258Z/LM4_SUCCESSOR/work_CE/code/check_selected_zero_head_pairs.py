#!/usr/bin/env python3
"""Two selected actual zero-head pairs, reconstructed independently at B steps.

The shared primitives are copied from the previously audited independent
cross-sheet verifier. Only zeta at nodes(8,0),(8,1) is tested. Domain-based
rank-two directness does not determine an overlap of whole64-column blocks.
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


heads_path=ROOT/'work_A/old_base_augmented_row_action.json'
heads=json.loads(heads_path.read_text())['old_generators'][2]
A=mapping(D['old_actions'][2]['geometric_push_paired'])
assert mapping(D['old_actions'][2]['retained_push'])=={i:(i,) for i in range(1,6)}
records=[]
for key in [(8,0),(8,1)]:
    node=next(n for n in D['node_columns'] if (n['loop_index'],n['local_node_index'])==key)
    word=tuple(node['paired_relator']);target=apply(word,A)
    c=normalize(integrate_at_B_steps(word));d=normalize(integrate_at_B_steps(target))
    augc=defaultdict(int);augd=defaultdict(int)
    for (row,g),n in c.items():add(augc,(row,g[2]),n)
    for (row,g),n in d.items():add(augd,(row,g[2]),n)
    assert dict(augc)==dict(augd) and len(augc)==1
    (row,t),sign=next(iter(augc.items()));slot=row[0]
    assert row[1]==slot and heads['A_heads'][str(slot)]==heads['B_heads'][str(slot)]==[]
    original_rows={r for r,g in c};new_rows={r for r,g in d}-original_rows
    assert new_rows
    private=min(new_rows,key=lambda r:(sum(q==r for q,g in d),r))
    polynomial=[{'coefficient':n,'A_word':u,'B_word':v,'retained_word':t}
                for (r,(u,v,t)),n in sorted(d.items()) if r==private]
    assert polynomial and all(x['coefficient'] for x in polynomial)
    records.append({'old_index':2,'old_name':'zeta','node_index':key,
        'original_terms':len(c),'transformed_terms':len(d),'identical_augmented_row':row,
        'private_row':private,'collected_nonzero_private_coefficient':polynomial,
        'private_row_absent_original':True,'two_column_consequence':'free Omega rank2 by the proved domain property',
        'excluded':'No whole64-column intersection conclusion'})
    print('PASS zeta',key,'terms',len(c),len(d),'private row',private,'coefficient terms',len(polynomial),flush=True)
out={'scope':__doc__,'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(x).hexdigest() for p,x in zip(paths,raw)},
     'head_sha256':hashlib.sha256(heads_path.read_bytes()).hexdigest(),
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':records,
     'elapsed_seconds':time.monotonic()-start}
(ROOT/'work_CE/next_symmetric_nodes/selected_zero_head_pair_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS two independently reconstructed private-row certificates; seconds',round(out['elapsed_seconds'],3),flush=True)
