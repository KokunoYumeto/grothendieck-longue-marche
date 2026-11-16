"""Exact finite certificates for A.47's uniform component-support lemma."""
from collections import defaultdict, deque
from itertools import product, combinations
from pathlib import Path
import json
import sympy as sp


def prufer(seq, n):
    degree = [1]*n
    for a in seq:
        degree[a] += 1
    edges = []
    for a in seq:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, a))
        degree[leaf] -= 1
        degree[a] -= 1
    edges.append(tuple(i for i in range(n) if degree[i] == 1))
    return edges


def rooted_edges(edges, root=0):
    graph = defaultdict(list)
    for a, b, length in edges:
        graph[a].append((b, length))
        graph[b].append((a, length))
    parent = {root: None}
    queue = deque([root])
    order = []
    while queue:
        a = queue.popleft()
        for b, length in graph[a]:
            if b in parent:
                continue
            parent[b] = a
            queue.append(b)
            order.append((a, b, length))
    result = []
    for a, b, length in order:
        side = {b}
        todo = [b]
        while todo:
            c = todo.pop()
            for d, _ in graph[c]:
                if parent.get(d) == c:
                    side.add(d)
                    todo.append(d)
        result.append((side, length))
    return graph, result


def distance(graph, source, target):
    todo = deque([(source, 0)])
    seen = {source}
    while todo:
        a, value = todo.popleft()
        if a == target:
            return value
        for b, length in graph[a]:
            if b not in seen:
                seen.add(b)
                todo.append((b, value+length))
    raise AssertionError('disconnected tree')


tree_rows = []
for n in range(2, 7):
    checks = 0
    for seq in product(range(n), repeat=n-2):
        edges = [(a, b, i+1) for i, (a, b) in enumerate(prufer(seq, n))]
        graph, sides = rooted_edges(edges)
        for i, j in combinations(range(n), 2):
            A = sum(m*int(i in side) for side, m in sides)
            D = sum(m*int(j in side) for side, m in sides)
            B = sum(m*int(i in side)*int(j in side) for side, m in sides)
            coeff = sum(m*(int(i in side)-int(j in side))**2 for side, m in sides)
            assert coeff == A+D-2*B == distance(graph, i, j) > 0
            checks += 1
    tree_rows.append({'vertices': n, 'two_component_distance_checks': checks})
    print(tree_rows[-1], flush=True)


def add(a, b, scale=1):
    answer = dict(a)
    for w, c in b.items():
        answer[w] = sp.expand(answer.get(w, 0)+scale*c)
        if answer[w] == 0:
            del answer[w]
    return answer


def mul(a, b):
    answer = {}
    for u, c in a.items():
        for v, d in b.items():
            answer = add(answer, {u+v: c*d})
    return answer


def comm(a, b):
    return add(mul(a, b), mul(b, a), -1)


x, y = {(0,): 1}, {(1,): 1}
Z = comm(x, y)
a, b, c, d = x, y, {w: -v for w, v in x.items()}, y
omega_i, omega_j = comm(a, b), comm(c, d)
assert add(omega_i, omega_j) == {}
assert add(a, c) == {}
A, B, C, D = sp.symbols('A B C D')
Wi = add({w: A*v for w, v in omega_i.items()}, omega_j, B)
Wj = add({w: C*v for w, v in omega_i.items()}, omega_j, D)
image = add(comm(Wi, a), comm(Wj, c))
expected = {w: sp.expand((A-B-C+D)*v) for w, v in comm(Z, x).items()}
assert image == expected
assert comm(Z, x) == {(0, 1, 0): 2, (1, 0, 0): -1, (0, 0, 1): -1}
print({'free_Lie_witness': '2xyx-yxx-xxy', 'coefficient': 'A-B-C+D'}, flush=True)

component_rows = []
phi = sp.Matrix([[1, -1], [1, 1]])
assert phi.det() == 2
for n in [3, 5, 7, 9, 15, 21]:
    image_matrix = sp.Matrix.hstack(*([phi]*n))
    assert image_matrix.rank() == 2
    for i in range(n):
        assert image_matrix[:, 2*i:2*i+2].rank() == 2
    kernel = image_matrix.nullspace()
    assert len(kernel) == 2*n-2
    for vector in kernel:
        support = [i for i in range(n) if vector[2*i] != 0 or vector[2*i+1] != 0]
        assert len(support) >= 2
    component_rows.append({'n': n, 'proper_homology_dimension': 2*n,
                           'target_rank': 2, 'kernel_dimension': len(kernel),
                           'each_component_rank': 2,
                           'single_component_kernel_dimension': 0})

result = {'tree_distance_checks': tree_rows,
          'surface_relation_image': '0', 'candidate_vector_image': '0',
          'nonzero_derivative_witness': 'distance(i,j)*(2xyx-yxx-xxy)',
          'component_map_certificates': component_rows, 'status': 'PASS'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print('PASS: tree distances, surface-Lie witness and component-map kernels.', flush=True)
