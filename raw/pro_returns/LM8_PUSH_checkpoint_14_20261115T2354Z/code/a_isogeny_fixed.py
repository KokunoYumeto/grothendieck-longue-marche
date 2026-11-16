"""Exact finite certificates for A.40's unbounded rooted-tree lemma.

The proof in A.40, not this finite enumeration, covers every tree and weight.
Ranks modulo 1000003 only certify rational injectivity in the tested degrees.
"""
from collections import defaultdict, deque
from itertools import product
from pathlib import Path
import json
import math


def add(a, b, c=1):
    ans = dict(a)
    for w, v in b.items():
        ans[w] = ans.get(w, 0)+c*v
        if not ans[w]:
            del ans[w]
    return ans


def mul(a, b):
    ans = defaultdict(int)
    for u, x in a.items():
        for v, y in b.items():
            ans[u+v] += x*y
    return {w: c for w, c in ans.items() if c}


def bracket(a, b):
    return add(mul(a, b), mul(b, a), -1)


def deriv(poly, data):
    ans = defaultdict(int)
    for w, c in poly.items():
        for j, x in enumerate(w):
            for v, d in data[x].items():
                ans[w[:j]+v+w[j+1:]] += c*d
    return {w: c for w, c in ans.items() if c}


def rank_mod(cols, prime=1000003):
    pivots = {}
    for raw in cols:
        v = {w: c % prime for w, c in raw.items() if c % prime}
        while v:
            key = max(v)
            if key not in pivots:
                inv = pow(v[key], -1, prime)
                pivots[key] = {w: c*inv % prime for w, c in v.items()}
                break
            fac = v[key]
            for w, c in pivots[key].items():
                val = (v.get(w, 0)-fac*c) % prime
                if val:
                    v[w] = val
                elif w in v:
                    del v[w]
    return len(pivots)


def prufer_edges(seq, n):
    degree = [1]*n
    for a in seq:
        degree[a] += 1
    edges = []
    for a in seq:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, a))
        degree[leaf] -= 1
        degree[a] -= 1
    left = [i for i in range(n) if degree[i] == 1]
    edges.append(tuple(left))
    return edges


def rooted_sides(edges, root=0):
    graph = defaultdict(list)
    for u, v, length in edges:
        graph[u].append((v, length))
        graph[v].append((u, length))
    parent = {root: None}
    queue = deque([root])
    oriented = []
    while queue:
        u = queue.popleft()
        for v, length in graph[u]:
            if v in parent:
                continue
            parent[v] = u
            oriented.append((u, v, length))
            queue.append(v)
    sides = []
    for u, v, length in oriented:
        side = {v}
        stack = [v]
        while stack:
            node = stack.pop()
            for w, _ in graph[node]:
                if parent.get(w) == node:
                    side.add(w)
                    stack.append(w)
        sides.append((side, length))
    return sides


# All labelled trees through six vertices, with the genus vertex a leaf.
# Every other vertex is permitted to carry a cusp; no stability hypothesis
# is needed for the coefficient identity itself.
tree_checks = []
for n in range(3, 7):
    count = 0
    genus = n-1
    for seq in product(range(n), repeat=n-2):
        bare = prufer_edges(seq, n)
        if sum(genus in e for e in bare) != 1:
            continue
        edges = [(u, v, i+1) for i, (u, v) in enumerate(bare)]
        sides = rooted_sides(edges)
        q = 1
        r = sum(length*int(genus in side)*int(q not in side)
                for side, length in sides)
        assert r > 0
        for cusp in range(n-1):
            if cusp == q:
                continue
            cj = sum(length*int(cusp in side)*
                     (int(genus in side)-int(q in side))
                     for side, length in sides)
            positive_expression = sum(length*(
                int(genus in side)*int(q not in side)*int(cusp not in side)
                + int(genus not in side)*int(q in side)*int(cusp in side))
                for side, length in sides)
            assert r-cj == positive_expression > 0
        count += 1
    tree_checks.append({'vertices': n, 'labelled_genus_leaf_trees': count})
    print(tree_checks[-1], flush=True)


# A stable marked tree with several positive and negative c_j values.
# The genus vertex 5 is the only positive-genus component; cusp Z is
# on that component, deliberately allowing c_Z=r (the stronger case).
edges = [(0, 1, 2), (1, 4, 3), (4, 5, 2), (1, 2, 3), (2, 3, 4)]
marks = {'P': 0, 'S': 0, 'R': 4, 'U': 2, 'Q': 3, 'T': 3, 'Z': 5}
retained = [name for name in marks if name != 'Q']
sides = rooted_sides(edges)
genus = 5
letter_count = 1+len(retained)
letters = [{(i,): 1} for i in range(letter_count)]
omega = letters[0]
index = {name: i+1 for i, name in enumerate(retained)}


def boundary(side):
    # t_Q=-Omega-sum of retained t_j, before extracting coefficients.
    qin = int(marks['Q'] in side)
    ans = {(0,): int(genus in side)-qin}
    for name in retained:
        ans[(index[name],)] = int(marks[name] in side)-qin
    return {w: c for w, c in ans.items() if c}


W = {}
Wj = {name: {} for name in retained}
for side, length in sides:
    delta = boundary(side)
    if genus in side:
        W = add(W, delta, length)
    for name in retained:
        if marks[name] in side:
            Wj[name] = add(Wj[name], delta, length)
r = W.get((0,), 0)
cvalues = {name: Wj[name].get((0,), 0) for name in retained}
assert r == 5
assert cvalues == {'P': 0, 'S': 0, 'R': 3, 'U': -3, 'T': -7, 'Z': 5}
print({'r': r, 'c_j': cvalues}, flush=True)

# Check the top-count slot-polynomial formula on all words up to length 4.
Dtop = {0: {}}
for name in retained:
    i = index[name]
    Dtop[i] = {w: cvalues[name]*v for w, v in bracket(omega, letters[i]).items()}
slot_checks = 0
for n in range(5):
    for word in product(range(letter_count), repeat=n):
        actual = add(deriv({word: 1}, Dtop), mul({word: 1}, omega), r)
        cusps = [x for x in word if x != 0]
        exponent = [0]*(len(cusps)+1)
        pos = 0
        for x in word:
            if x == 0:
                exponent[pos] += 1
            else:
                pos += 1
        cs = [cvalues[retained[i-1]] for i in cusps]
        coeffs = ([cs[0]]+[cs[i+1]-cs[i] for i in range(len(cs)-1)]+[r-cs[-1]]) if cs else [r]
        assert sum(coeffs) == r
        expected = {}
        for slot, coeff in enumerate(coeffs):
            if not coeff:
                continue
            exp = list(exponent)
            exp[slot] += 1
            out = (0,)*exp[0]
            for i, cusp in enumerate(cusps):
                out += (cusp,)+(0,)*exp[i+1]
            expected[out] = expected.get(out, 0)+coeff
        expected = {w: c for w, c in expected.items() if c}
        assert actual == expected
        slot_checks += 1

rank_checks = []
for lam in [0, 1, -2, 5, -5]:
    Wpacket = add(W, letters[index['P']], lam)
    data = {0: bracket(Wpacket, omega)}
    for name in retained:
        data[index[name]] = bracket(add(Wj[name], letters[index['P']], lam),
                                    letters[index[name]])
    for n in range(4):
        cols = [add(deriv({w: 1}, data), mul({w: 1}, Wpacket))
                for w in product(range(letter_count), repeat=n)]
        rk = rank_mod(cols)
        assert rk == letter_count**n
        row = {'packet_scalar': lam, 'boundary_degree': n,
               'domain_dimension': len(cols), 'rank': rk}
        rank_checks.append(row)
        print(row, flush=True)

# The supersingular Hasse coefficient certificate, illustrating all odd
# inert primes below 100; parity proves the general assertion in the text.
hasse_checks = []
for p in range(3, 100):
    if any(p % d == 0 for d in range(2, math.isqrt(p)+1)):
        continue
    m = (p-1)//2
    coefficient = 0 if m % 2 else math.comb(m, m//2)*((-1)**(m-m//2)) % p
    assert (coefficient == 0) == (p % 4 == 3)
    hasse_checks.append({'prime': p, 'hasse_coefficient': coefficient})

answer = {
    'tree_coefficient_checks': tree_checks,
    'explicit_tree_edges': edges,
    'explicit_cusps': marks,
    'eliminated_cusp': 'Q',
    'r': r,
    'omega_coefficients_c_j': cvalues,
    'slot_formula_word_checks': slot_checks,
    'prefix_ranks': rank_checks,
    'rank_prime': 1000003,
    'hasse_coefficients': hasse_checks,
    'unbounded_proof': 'A.40 slot multiplier is nonzero because its coefficients sum to r',
    'limitation': 'No finite enumeration is used to infer the all-tree or all-weight theorem.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(answer, indent=2)+'\n')
print('PASS: exact tree coefficients, slot formula, packet prefix ranks, and Hasse coefficients.')
