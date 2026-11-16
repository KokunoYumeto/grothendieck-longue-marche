"""Finite exact certificates accompanying the all-weight proof of A.41.

This script does not prove the unbounded theorem by testing finitely many
weights. Prefix ranks are computed over Q. Tensor-intersection ranks use a
nonzero modular minor plus the explicit common subspace, which certifies
the displayed rational dimensions exactly.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import product, combinations
from pathlib import Path
import json


def add(a, b, scale=1):
    ans = dict(a)
    for w, c in b.items():
        ans[w] = ans.get(w, 0) + scale*c
        if not ans[w]:
            del ans[w]
    return ans


def mul(a, b):
    ans = defaultdict(int)
    for w, c in a.items():
        for v, d in b.items():
            ans[w+v] += c*d
    return {w: c for w, c in ans.items() if c}


def comm(a, b):
    return add(mul(a, b), mul(b, a), -1)


def deriv(a, data):
    ans = defaultdict(int)
    for w, c in a.items():
        for i, letter in enumerate(w):
            for v, d in data[letter].items():
                ans[w[:i]+v+w[i+1:]] += c*d
    return {w: c for w, c in ans.items() if c}


def rank_q(columns):
    pivots = {}
    for col in columns:
        v = {w: Fraction(c) for w, c in col.items() if c}
        while v:
            key = max(v)
            if key not in pivots:
                c = v[key]
                pivots[key] = {w: d/c for w, d in v.items()}
                break
            v = add(v, pivots[key], -v[key])
    return len(pivots)


def rank_mod(columns, prime=1000003):
    pivots = {}
    for col in columns:
        v = {w: c % prime for w, c in col.items() if c % prime}
        while v:
            key = max(v)
            if key not in pivots:
                scale = pow(v[key], -1, prime)
                pivots[key] = {w: c*scale % prime for w, c in v.items()}
                break
            factor = v[key]
            for w, c in pivots[key].items():
                d = (v.get(w, 0)-factor*c) % prime
                if d:
                    v[w] = d
                elif w in v:
                    del v[w]
    return len(pivots)


def prufer(seq, n):
    degrees = [1]*n
    for a in seq:
        degrees[a] += 1
    edges = []
    for a in seq:
        leaf = next(i for i in range(n) if degrees[i] == 1)
        edges.append((leaf, a))
        degrees[leaf] -= 1
        degrees[a] -= 1
    left = [i for i in range(n) if degrees[i] == 1]
    edges.append(tuple(left))
    return edges


def root_tree(edges, root=0):
    graph = defaultdict(list)
    for a, b, length in edges:
        graph[a].append((b, length))
        graph[b].append((a, length))
    parents = {root: None}
    heights = {root: 0}
    queue = deque([root])
    ordered = []
    while queue:
        a = queue.popleft()
        for b, length in graph[a]:
            if b in parents:
                continue
            parents[b] = a
            heights[b] = heights[a] + length
            ordered.append((a, b, length))
            queue.append(b)
    sides = []
    for a, b, length in ordered:
        descendants = {b}
        todo = [b]
        while todo:
            c = todo.pop()
            for d, _ in graph[c]:
                if parents.get(d) == c:
                    descendants.add(d)
                    todo.append(d)
        sides.append((descendants, length))
    return parents, heights, sides


# The distance identity for every labelled tree through six vertices,
# every possible genus vertex, and Q either at the root or at vertex 1.
tree_rows = []
for n in range(2, 7):
    count = 0
    for seq in product(range(n), repeat=n-2):
        edges = [(a, b, i+1) for i, (a, b) in enumerate(prufer(seq, n))]
        parents, heights, sides = root_tree(edges)
        for q in (0, 1):
            q_path = {q}
            node = q
            while parents[node] is not None:
                node = parents[node]
                q_path.add(node)
            for genus_vertex in range(n):
                branch = genus_vertex
                while branch not in q_path:
                    branch = parents[branch]
                r = sum(length*int(genus_vertex in side)*int(q not in side)
                        for side, length in sides)
                assert r == heights[genus_vertex]-heights[branch]
                assert (r > 0) == (genus_vertex not in q_path)
                count += 1
    tree_rows.append({'vertices': n, 'distance_identities': count})
    print(tree_rows[-1], flush=True)


# A compact-type tree with two positive-genus components. P and Q are
# rational vertices; R is a cusp on the first genus component.
edges = [(0, 1, 2), (0, 2, 3), (1, 3, 5)]
genera = [2, 3]
marks = {'P': 0, 'Q': 1, 'R': 2}
retained = ['P', 'R']
_, _, sides = root_tree(edges)
letters = [{(i,): 1} for i in range(4)]  # Omega_1, Omega_2, P, R
Ws = [{} for _ in range(4)]
locations = genera + [marks[j] for j in retained]
for side, length in sides:
    q_in = int(marks['Q'] in side)
    delta = {(i,): int(v in side)-q_in for i, v in enumerate(locations)}
    delta = {w: c for w, c in delta.items() if c}
    for i, v in enumerate(locations):
        if v in side:
            Ws[i] = add(Ws[i], delta, length)
assert Ws == [
    {(0,): 3, (3,): 3},
    {(0,): -2, (1,): 5, (2,): -2, (3,): -2},
    {},
    {(0,): 3, (3,): 3},
]
r_values = [Ws[i][(i,)] for i in range(2)]
assert r_values == [3, 5]

slot_checks = 0
for core_type in range(2):
    omega = letters[core_type]
    r = r_values[core_type]
    c = [Ws[j].get((core_type,), 0) for j in range(4)]
    top = {j: ({w: c[j]*v for w, v in comm(omega, letters[j]).items()}
               if j != core_type else {}) for j in range(4)}
    for degree in range(5):
        for word in product(range(4), repeat=degree):
            actual = add(deriv({word: 1}, top), mul({word: 1}, omega), r)
            other = [j for j in word if j != core_type]
            exponents = [0]*(len(other)+1)
            slot = 0
            for j in word:
                if j == core_type:
                    exponents[slot] += 1
                else:
                    slot += 1
            coeffs = ([c[other[0]]] +
                      [c[other[h+1]]-c[other[h]] for h in range(len(other)-1)] +
                      [r-c[other[-1]]]) if other else [r]
            assert sum(coeffs) == r
            expected = {}
            for h, coefficient in enumerate(coeffs):
                if not coefficient:
                    continue
                powers = list(exponents)
                powers[h] += 1
                out = (core_type,)*powers[0]
                for j, letter in enumerate(other):
                    out += (letter,) + (core_type,)*powers[j+1]
                expected[out] = expected.get(out, 0)+coefficient
            assert actual == {w: a for w, a in expected.items() if a}
            slot_checks += 1

prefix_rows = []
for lam in [-5, -1, 0, 1, 5]:
    shifted = [add(W, letters[2], lam) for W in Ws]
    data = {i: comm(shifted[i], letters[i]) for i in range(4)}
    for core_type in range(2):
        for degree in range(4):
            columns = [add(deriv({w: 1}, data), mul({w: 1}, shifted[core_type]))
                       for w in product(range(4), repeat=degree)]
            rank = rank_q(columns)
            assert rank == 4**degree
            prefix_rows.append({'packet_scalar': lam, 'core_type': core_type+1,
                                'boundary_degree': degree, 'dimension': len(columns),
                                'rational_rank': rank})
print({'slot_checks': slot_checks, 'prefix_full_rank_checks': len(prefix_rows)}, flush=True)


# A symplectic shear on three orthogonal planes. Coordinates of Lambda^2 V
# are indexed by pairs, with a separate first coordinate for one cusp T.
pairs = list(combinations(range(6), 2))
index = {pair: i+1 for i, pair in enumerate(pairs)}

def wedge(a, b):
    result = defaultdict(int)
    for i, c in a.items():
        for j, d in b.items():
            if i == j:
                continue
            pair = tuple(sorted((i, j)))
            result[(index[pair],)] += c*d*(1 if i < j else -1)
    return {w: c for w, c in result.items() if c}

basis = [{i: 1} for i in range(6)]
image = [dict(v) for v in basis]
for i in range(3):
    for j in range(3):
        if i != j:
            image[2*i+1][2*j] = 1
omega = [wedge(basis[2*i], basis[2*i+1]) for i in range(3)]
gomega = [wedge(image[2*i], image[2*i+1]) for i in range(3)]
omega_sum = {}
gomega_sum = {}
for a, b in zip(omega, gomega):
    omega_sum = add(omega_sum, a)
    gomega_sum = add(gomega_sum, b)
assert omega_sum == gomega_sum  # exact preservation of total symplectic bivector
assert rank_q(omega+gomega) == 5  # dim U intersection gU = 1
cusp = {(0,): 1}
Acols, Bcols = [cusp]+omega, [cusp]+gomega

def tensor_columns(columns, degree):
    result = []
    for choices in product(columns, repeat=degree):
        out = {(): 1}
        for col in choices:
            out = mul(out, col)
        result.append(out)
    return result

intersection_rows = []
for degree in range(1, 4):
    left = tensor_columns(Acols, degree)
    right = tensor_columns(Bcols, degree)
    rank = rank_mod(left+right)
    intersection_dim = 2*4**degree-rank
    assert intersection_dim == 2**degree
    # The 2^degree independent tensors in cusp,total-Omega are genuinely
    # common over Q; this modular maximal-rank bound proves equality over Q.
    common = tensor_columns([cusp, omega_sum], degree)
    assert rank_mod(common) == 2**degree
    intersection_rows.append({'tensor_degree': degree, 'union_rank_mod_1000003': rank,
                              'certified_rational_intersection_dimension': intersection_dim,
                              'expected_common_tensor_dimension': 2**degree})
print({'tensor_intersections': intersection_rows}, flush=True)

result = {
    'tree_distance_checks': tree_rows,
    'explicit_tree_edges': edges,
    'genus_vertices': genera,
    'cusps': marks,
    'W_rows': [{str(w[0]): c for w, c in row.items()} for row in Ws],
    'positive_self_coefficients': r_values,
    'slot_formula_checks': slot_checks,
    'prefix_checks': prefix_rows,
    'symplectic_plane_intersection_dimension': 1,
    'tensor_intersection_checks': intersection_rows,
    'status': 'PASS',
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print('PASS: all finite exact certificates; the text proves all weights.', flush=True)
