#!/usr/bin/env python3
"""Exact finite-cover certificates for D.32, through degree six.

For each cycle type of x and every permutation y, enumerate transitive
Schreier graphs.  This includes every connected degree <=6 covering up to
relabeling (and deliberately retains residual duplicates).  Boundary
cycles and their homology are computed from walks, not from a prescribed
homology matrix.  Arithmetic is exact over finite fields.
"""
from collections import Counter, deque
from itertools import permutations, product
import json
from pathlib import Path


def partitions(n, lower=1):
    if n == 0:
        yield ()
    for k in range(lower, n + 1):
        for rest in partitions(n-k, k):
            yield (k,) + rest


def from_partition(parts):
    ans = list(range(sum(parts)))
    start = 0
    for length in parts:
        for j in range(length):
            ans[start+j] = start+(j+1) % length
        start += length
    return tuple(ans)


def inverse(a):
    b = [0]*len(a)
    for i, j in enumerate(a):
        b[j] = i
    return tuple(b)


def cycles(a):
    todo = set(range(len(a)))
    out = []
    while todo:
        start = min(todo)
        cyc = []
        v = start
        while v not in cyc:
            cyc.append(v)
            todo.remove(v)
            v = a[v]
        assert v == start
        out.append(cyc)
    return out


def graph_basis(x, y):
    n = len(x)
    adjacency = [[] for _ in range(n)]
    for a, perm in enumerate((x, y)):
        for v, w in enumerate(perm):
            edge = a*n+v
            adjacency[v].append((w, edge))
            adjacency[w].append((v, edge))
    reached = {0}
    queue = deque([0])
    tree = set()
    while queue:
        v = queue.popleft()
        for w, edge in adjacency[v]:
            if w not in reached:
                reached.add(w)
                tree.add(edge)
                queue.append(w)
    if len(reached) != n:
        return None
    non_tree = [e for e in range(2*n) if e not in tree]
    assert len(tree) == n-1 and len(non_tree) == n+1
    return non_tree


def boundary_data(x, y, non_tree):
    n = len(x)
    ix, iy = inverse(x), inverse(y)
    # Words act on the right, so xy sends v to y[x[v]].
    z = tuple(ix[iy[v]] for v in range(n))
    permutations_by_cusp = (x, y, z)
    records = []
    for cusp, perm in enumerate(permutations_by_cusp):
        for cyc in cycles(perm):
            vector = [0]*(2*n)
            v = cyc[0]
            for _ in cyc:
                if cusp == 0:
                    vector[v] += 1
                    v = x[v]
                elif cusp == 1:
                    vector[n+v] += 1
                    v = y[v]
                else:
                    w = iy[v]
                    vector[n+w] -= 1
                    v = w
                    w = ix[v]
                    vector[w] -= 1
                    v = w
            assert v == cyc[0]
            records.append({"cusp": cusp+1, "cycle": cyc,
                            "degree": len(cyc),
                            "edge_vector": vector,
                            "homology": [vector[e] for e in non_tree]})
    assert all(sum(b["edge_vector"][i] for b in records) == 0
               for i in range(2*n))
    return records


def rref(matrix, p):
    a = [[v % p for v in row] for row in matrix]
    if not a:
        return a, []
    row = 0
    pivots = []
    for column in range(len(a[0])):
        pivot = next((j for j in range(row, len(a)) if a[j][column]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][column], -1, p)
        a[row] = [v*inv % p for v in a[row]]
        for j in range(len(a)):
            if j != row:
                scale = a[j][column]
                a[j] = [(v-scale*w) % p for v, w in zip(a[j], a[row])]
        pivots.append(column)
        row += 1
        if row == len(a):
            break
    return a, pivots


def dual_characters(rows, p):
    r = len(rows[0])
    result = []
    for target in range(len(rows)):
        aug = [list(v)+[int(j == target)] for j, v in enumerate(rows)]
        reduced, pivots = rref(aug, p)
        assert len(pivots) == len(rows) and all(k < r for k in pivots)
        character = [0]*r
        for j, column in enumerate(pivots):
            character[column] = reduced[j][-1]
        values = [sum(a*b for a, b in zip(v, character)) % p for v in rows]
        assert values == [int(j == target) for j in range(len(rows))]
        result.append(character)
    return result


def main():
    counts = Counter()
    histograms = Counter()
    examples = {}
    prime_list = (2, 3, 5)
    for n in range(1, 7):
        for parts in partitions(n):
            x = from_partition(parts)
            for y in permutations(range(n)):
                non_tree = graph_basis(x, y)
                if non_tree is None:
                    continue
                counts[f"degree_{n}_transitive_pairs"] += 1
                boundaries = boundary_data(x, y, non_tree)
                b = len(boundaries)
                assert (n+2-b) % 2 == 0 and n+2-b >= 0
                genus = (n+2-b)//2
                for p in prime_list:
                    rank = len(rref([v["homology"] for v in boundaries], p)[1])
                    assert rank == b-1
                    counts["boundary_relation_field_checks"] += 1
                    if n % p:
                        continue
                    selections = [[j for j, v in enumerate(boundaries)
                                   if v["cusp"] == cusp and v["degree"] % p]
                                  for cusp in (1, 2, 3)]
                    if not all(selections):
                        continue
                    assert b >= 4
                    counts[f"p_{p}_admissible_cover_pairs"] += 1
                    histograms[f"degree={n},p={p},boundaries={b}"] += 1
                    for selected in product(*selections):
                        rows = []
                        scalars = []
                        for j in selected:
                            degree = boundaries[j]["degree"]
                            scalar = pow(degree, -1, p)
                            assert degree*pow(degree, -1, p*p) % (p*p) == 1
                            scalars.append(scalar)
                            rows.append([scalar*v % p for v in boundaries[j]["homology"]])
                        assert len(rref(rows, p)[1]) == 3
                        duals = dual_characters(rows, p)
                        counts[f"p_{p}_selected_triple_checks"] += 1
                        key = str(p)
                        if key not in examples:
                            examples[key] = {
                                "degree": n, "prime": p, "x": x, "y": y,
                                "genus": genus, "non_tree_edges": non_tree,
                                "boundary_count": b, "boundaries": boundaries,
                                "selected": selected, "restriction_scalars": scalars,
                                "selected_full_Zp_homology_rows": rows,
                                "dual_characters": duals,
                                "evaluation_matrix": [[sum(a*b for a, b in zip(v, c)) % p
                                                       for c in duals] for v in rows]
                            }
    assert set(examples) == {"2", "3", "5"}
    result = {
        "claim": "D.32", "status": "passed",
        "coverage": "Every connected covering through degree six is represented; x runs through cycle types and y through all permutations, retaining residual relabeling duplicates.",
        "counts": dict(sorted(counts.items())),
        "admissible_cover_histogram": dict(sorted(histograms.items())),
        "explicit_dual_character_examples": examples,
        "logical_limit": "These exact finite checks validate the covering and homology maps; the arbitrary-degree and closed-subgroup proof is in d32.tex."
    }
    destination = Path(__file__).with_name("three_cusp_rank_d32_output.json")
    destination.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "passed", "counts": result["counts"],
                      "output": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
