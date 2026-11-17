#!/usr/bin/env python3
"""Compile the actual full21 semilinear Fox maps over Z[G].

G=(R_A x R_B) semidirect T, with T acting on the common R basis by
left translation of its T index in A and beta(T) in B.  The five
retained edges are preserved.  No product-tree rectangles are expanded.
"""
from pathlib import Path
from collections import defaultdict
import json, hashlib, time

ROOT = Path(__file__).resolve().parents[2]
P = ROOT/'work_CE/next_symmetric_nodes'
DATA = P/'symmetric_paired_fox_data.json'
SOURCE = P/'symmetric_full_source_data.json'
REDUCED = ROOT/'work_DE/next_marginal_source/boundary16_and_Tate_certificate.json'
data = json.loads(DATA.read_text())
source = json.loads(SOURCE.read_text())
reduced = json.loads(REDUCED.read_text())


class Trie:
    def __init__(self):
        self.nodes = [(0, 0, 0)]
        self.index = {}

    def append(self, p, x):
        assert x
        if p and self.nodes[p][1] == -x:
            return self.nodes[p][0]
        key = (p, x)
        if key not in self.index:
            self.index[key] = len(self.nodes)
            self.nodes.append((p, x, self.nodes[p][2] + 1))
        return self.index[key]

    def word(self, w):
        p = 0
        for x in w:
            p = self.append(p, x)
        return p

    def read(self, p):
        w = []
        while p:
            p, x, _ = self.nodes[p]
            w.append(x)
        return tuple(reversed(w))


T, R = Trie(), Trie()
generators = [None]
gen_index = {}
group_elements = [(0, 0, 0)]
group_index = {(0, 0, 0): 0}
retained = {j: i + 1 for i, j in enumerate(data['retained_paired_indices'])}
beta = {int(k): tuple(v) for k, v in data['retained_involution'].items()}
assert all(len(w) == 1 for w in beta.values())
beta_ids = {0: 0}


def beta_head(t):
    if t not in beta_ids:
        trail = []
        p = t
        while p not in beta_ids:
            trail.append(p)
            p = T.nodes[p][0]
        for p in reversed(trail):
            parent, x, _ = T.nodes[p]
            beta_ids[p] = T.append(beta_ids[parent],
                                   (1 if x > 0 else -1) * beta[abs(x)][0])
    return beta_ids[t]


def generator(t, slot):
    key = (t, slot)
    if key not in gen_index:
        gen_index[key] = len(generators)
        generators.append(key)
    return gen_index[key]


def group(g):
    if g not in group_index:
        group_index[g] = len(group_elements)
        group_elements.append(g)
    return group_index[g]


def right_letter(gid, letter):
    """Exact right multiplication in G by one paired F21 generator."""
    a, b, t = group_elements[gid]
    j, sign = abs(letter), 1 if letter > 0 else -1
    if j in retained:
        return group((a, b, T.append(t, sign * retained[j])))
    if j < 12:
        return group((R.append(a, sign * generator(t, j)), b, t))
    return group((a, R.append(b, sign * generator(beta_head(t), j - 10)), t))


def add(c, key, n):
    c[key] += n
    if not c[key]:
        del c[key]


def fox(word):
    """d(word)=sum prefix*e_i, with negative edge -prefix*x_i^-1*e_i."""
    state = 0
    chain = defaultdict(int)
    for letter in word:
        if letter > 0:
            add(chain, (letter, state), 1)
            state = right_letter(state, letter)
        else:
            state = right_letter(state, letter)
            add(chain, (-letter, state), -1)
    boundary = defaultdict(int)
    for (row, coefficient), n in chain.items():
        add(boundary, right_letter(coefficient, row), n)
        add(boundary, coefficient, -n)
    expected = defaultdict(int)
    add(expected, state, 1)
    add(expected, 0, -1)
    assert dict(boundary) == dict(expected), 'entire Fox boundary'
    return state, chain


def pack(chain):
    return [[row, gid, n] for (row, gid), n in sorted(chain.items())]


started = time.monotonic()
matrices = []
inputs = []
for action in data['old_actions']:
    for direction, field in [('push', 'geometric_push_paired'),
                             ('pull', 'based_pullback_paired')]:
        inputs.append(('old', action['name'], direction, action[field],
                       {'old_index': action['index']}))
for action in source['old_source_generators']:
    for direction, field in [('push', 'source_push_F21'),
                             ('pull', 'source_pullback_F21')]:
        inputs.append(('source', action['name'], direction, action[field],
                       {'far_base_word': action['far_base_word']}))
inputs.append(('involution', 'F', 'self_inverse', data['paired_involution'], {}))

for family, name, direction, images, metadata in inputs:
    columns, endpoints, literal_images = [], [], []
    for j in range(1, 22):
        w = images[str(j)]
        endpoint, chain = fox(w)
        a, b, t = group_elements[endpoint]
        if j not in retained and family != 'involution':
            assert t == 0
            assert (b == 0 if j < 12 else a == 0), (family, name, j)
        if j not in retained and family == 'involution':
            assert t == 0
            assert (a == 0 if j < 12 else b == 0)
        columns.append(pack(chain))
        endpoints.append(endpoint)
        literal_images.append(w)
    record = {'family': family, 'name': name, 'direction': direction,
              **metadata, 'literal_F21_images': literal_images,
              'generator_images_G': endpoints, 'columns': columns,
              'total_input_letters': sum(map(len, literal_images)),
              'nonzero_terms': sum(map(len, columns)),
              'all21_boundary_identities': True,
              'deleted_family_preservation': True}
    matrices.append(record)
    print('PASS', family, name, direction, 'letters', record['total_input_letters'],
          'terms', record['nonzero_terms'], flush=True)

# A completely separate producer supplied all64 reduced cycles.  Translate
# its explicit R dictionary, then compare every coefficient after dropping
# precisely the five retained rows of the full21 Fox cycle.
DE_gens = {}
for k, v in reduced['common_R_basis'].items():
    DE_gens[int(k)] = generator(T.word(v['retained_word']), v['paired_slot'])


def convert_R(w):
    return R.word((1 if x > 0 else -1) * DE_gens[abs(x)] for x in w)


reduced_by_node = {tuple(c['node_index']): c for c in reduced['columns']}
node_cycles = []
for node in data['node_columns']:
    index = (node['loop_index'], node['local_node_index'])
    endpoint, chain = fox(node['paired_relator'])
    assert endpoint == 0, index
    collapsed = {key: n for key, n in chain.items() if key[0] not in retained}
    expected = defaultdict(int)
    for term in reduced_by_node[index]['boundary_terms']:
        g = term['G_coefficient']
        gid = group((convert_R(g['A_word']), convert_R(g['B_word']),
                     T.word(g['retained_word'])))
        row = term['slot'] + (0 if term['side'] == 'A' else 10)
        add(expected, (row, gid), term['coefficient'])
    assert collapsed == dict(expected), ('full21-to16 comparison', index)
    node_cycles.append({'node_index': list(index),
                        'literal_F21_word': node['paired_relator'],
                        'full21_cycle': pack(chain),
                        'collapsed16_cycle': pack(collapsed),
                        'G_endpoint': 0, 'full_boundary_zero': True,
                        'independent16_entire_cycle_equal': True})

assert len(matrices) == 35 and len(node_cycles) == 64
counts = {'old_signed_matrices': 12, 'source_signed_matrices': 22,
          'involution_matrix': 1, 'all_columns': len(matrices) * 21,
          'input_letters': sum(m['total_input_letters'] for m in matrices),
          'matrix_terms': sum(m['nonzero_terms'] for m in matrices),
          'node_full21_terms': sum(len(c['full21_cycle']) for c in node_cycles),
          'node_collapsed16_terms': sum(len(c['collapsed16_cycle']) for c in node_cycles)}
assert counts['node_collapsed16_terms'] == 2096
out = {'scope': __doc__, 'status': 'complete_actual_full21_semilinear_Fox_maps',
       'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'input_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in (DATA, SOURCE, REDUCED)},
       'coefficient_group': '(R_A x R_B) semidirect T; (u,v,t)(x,y,s)=(u*tau_t(x),v*tau_beta(t)(y),t*s)',
       'retained_paired_indices': data['retained_paired_indices'],
       'deleted_A_slots': data['deleted_right_slots'],
       'retained_involution': data['retained_involution'],
       'retained_word_DAG': T.nodes, 'common_R_generators': generators,
       'R_word_DAG': R.nodes, 'group_elements': group_elements,
       'DAG_convention': 'node0 is empty. Each node is(parent,signed_letter,length), the freely reduced parent followed by its letter. R generators are(retained_DAG_id,paired_slot). G ids are canonical triples(A_R_DAG_id,B_R_DAG_id,T_DAG_id).',
       'Fox_convention': 'Each matrix column j is the full left Fox chain of the literal image of x_j. Sparse term(row,G_id,n) means n*g*e_row. Boundary(e_row)=q(x_row)-1.',
       'semilinear_convention': 'For a chosen action alpha, alpha_*(sum c_j*e_j)=sum alpha_G(c_j)*M_alpha[:,j]. alpha_G is the automorphism specified by the21 stored generator_images_G and literal images. The matrices are NOT ordinary linear maps over a fixed coefficient ring action.',
       'geometric_composition': 'Positive based push alpha_g(x)=g^-1*x*g. Chronological base words compose push operators in reverse order; pull is the actual inverse push.',
       'forest_projection': 'Delete the five retained rows. This collapses the right T-coset forest on chains and induces H1 isomorphism; it is not asserted to be a G-homotopy equivalence.',
       'matrices': matrices, 'node_cycles': node_cycles, 'counts': counts,
       'claims_excluded': ['full orbit rank or syzygy decision', 'kappa vanishing',
                           'ordinary rather than semilinear matrix composition',
                           'coefficient division ring or rank monotonicity'],
       'elapsed_seconds': time.monotonic() - started}
(P/'actual_full21_Fox.json').write_text(json.dumps(out, separators=(',', ':')) + '\n')
print('PASS all64 full21 cycles equal independently computed16 cycles after forest projection', flush=True)
print('COUNTS', counts, flush=True)
print('DAGS', len(T.nodes), len(generators)-1, len(R.nodes), len(group_elements), flush=True)
print('DONE elapsed', round(out['elapsed_seconds'], 3), flush=True)
