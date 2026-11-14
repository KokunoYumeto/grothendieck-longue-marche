#!/usr/bin/env python3
"""Exact deleted-permutation module and twenty-sheeted cup-form test.

All groups, module actions, source maps, Schreier words, and mod-two
Heisenberg evaluations are retained.  This is a bounded source test for
the next order-five peripheral construction, not a lifting conclusion.
"""

from collections import deque
from functools import reduce
from itertools import permutations, product
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('finite_count', HERE/'a_peripheral_count.py')
finite = importlib.util.module_from_spec(spec)
spec.loader.exec_module(finite)


def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            k = row.bit_length()-1
            if k in pivots:
                row ^= pivots[k]
            else:
                pivots[k] = row
                break
    return len(pivots)


def rref(rows, width):
    rows = [r for r in rows if r]
    pivots, at = [], 0
    for col in range(width):
        j = next((j for j in range(at, len(rows)) if (rows[j] >> col) & 1), None)
        if j is None:
            continue
        rows[at], rows[j] = rows[j], rows[at]
        for k in range(len(rows)):
            if k != at and ((rows[k] >> col) & 1):
                rows[k] ^= rows[at]
        pivots.append(col)
        at += 1
    return rows[:at], pivots


def parity(x):
    return x.bit_count() & 1


def apply(columns, vector):
    out = 0
    for k, column in enumerate(columns):
        if (vector >> k) & 1:
            out ^= column
    return out


def inverse_word(word):
    return [-a for a in reversed(word)]


def main():
    H = finite.Group('A5', [p for p in permutations(range(5)) if finite.parity(p) == 0],
                     finite.perm_mul, tuple(range(5)))
    x = H.index[(1, 2, 3, 4, 0)]
    y = next(y for y in range(H.size)
             if H.orders[y] == H.orders[H.mul[x][y]] == 5
             and len(H.generated([x, y])) == 60)
    z = H.inv[H.mul[x][y]]
    c = H.index[(1, 2, 0, 3, 4)]
    C = H.generated([c])
    assert len(C) == 3

    def module_action(g, v):
        full = v | (parity(v) << 4)
        moved = sum(((full >> i) & 1) << H.elements[g][i] for i in range(5))
        assert parity(moved) == 0
        return moved & 15

    matrices = [[module_action(g, 1 << i) for i in range(4)] for g in range(60)]
    assert all(apply(matrices[H.mul[g][h]], v) ==
               apply(matrices[g], apply(matrices[h], v))
               for g, h, v in product(range(60), range(60), range(16)))
    orbit_span_ranks = [rank(module_action(g, v) for g in range(60)) for v in range(1, 16)]
    assert orbit_span_ranks == [4]*15

    # Literal endomorphisms commuting with the two generating matrices.
    endomorphisms = []
    for cols in product(range(16), repeat=4):
        if all(apply(cols, module_action(g, 1 << j)) ==
               module_action(g, cols[j]) for g in (x, y) for j in range(4)):
            endomorphisms.append(cols)
    assert endomorphisms == [(0, 0, 0, 0), (1, 2, 4, 8)]

    def act_rows(g, rows):
        return [reduce(int.__xor__,
                    (rows[k] for k in range(4) if (matrices[g][k] >> i) & 1), 0)
                for i in range(4)]

    values = {H.one: [0]*4}
    source_tree_words = {H.one: []}
    todo = deque([H.one])
    constraints = []
    source_relators = []
    gen_values = [[1 << i for i in range(4)], [1 << (i+4) for i in range(4)]]
    while todo:
        g = todo.popleft()
        for letter, (h, v) in enumerate(zip((x, y), gen_values), start=1):
            k = H.mul[g][h]
            new = [a ^ b for a, b in zip(values[g], act_rows(g, v))]
            if k not in values:
                values[k] = new
                source_tree_words[k] = source_tree_words[g]+[letter]
                todo.append(k)
            else:
                constraints += [a ^ b for a, b in zip(new, values[k])]
                source_relators.append(source_tree_words[g]+[letter]+inverse_word(source_tree_words[k]))
    reduced, pivots = rref(constraints, 8)
    coboundaries = [module_action(x, v) ^ v |
                   ((module_action(y, v) ^ v) << 4) for v in (1, 2, 4, 8)]
    assert rank(coboundaries) == 4
    assert all(parity(row & vector) == 0 for row in reduced for vector in coboundaries)
    print('Deleted module: simple, End=F2; crossed constraint rank', len(pivots), flush=True)
    print('Z1,B1,H1 dimensions:', 8-len(pivots), 4, 4-len(pivots), flush=True)
    assert len(pivots) == 4

    # The standard unit vectors in these pivot positions form an actual
    # basis of M^2/Z1(H,M), hence define four source-module coordinates.
    quotient_basis = [1 << p for p in pivots]
    vx = sum((v & 15) << (4*j) for j, v in enumerate(quotient_basis))
    vy = sum((v >> 4) << (4*j) for j, v in enumerate(quotient_basis))

    def big_action(g, v):
        return sum(module_action(g, (v >> (4*j)) & 15) << (4*j) for j in range(4))

    def mul(a, b):
        return a[0] ^ big_action(a[1], b[0]), H.mul[a[1]][b[1]]

    def inv(a):
        return big_action(H.inv[a[1]], a[0]), H.inv[a[1]]

    generators = {1: (vx, x), 2: (vy, y)}
    generators.update({-j: inv(a) for j, a in list(generators.items())})

    def evaluate(word):
        out = (0, H.one)
        for letter in word:
            out = mul(out, generators[letter])
        return out

    for word in ([1], [2], [-2, -1]):
        assert evaluate(word*5) == (0, H.one)
    relation_values = [evaluate(word) for word in source_relators]
    assert all(h == H.one for v, h in relation_values)
    normal_module_span_rank = rank(big_action(h, v) for v, k in relation_values for h in range(60))
    assert normal_module_span_rank == 16
    print('Actual source-kernel relators span all16 module coordinates under A5', flush=True)
    assert all(rank([module_action(g, 1 << j) ^ (1 << j) for j in range(4)]) == 4
               for g in (x, y, z))

    # Actual right-coset rose and a signed-edge spanning tree.
    cosets = sorted({frozenset(H.mul[h][g] for h in C) for g in range(60)}, key=min)
    which = {g: i for i, coset in enumerate(cosets) for g in coset}
    base = which[H.one]
    reps = [min(coset) for coset in cosets]
    edges = [[which[H.mul[g][h]] for h in (x, y)] for g in reps]
    back_edges = [[which[H.mul[g][H.inv[h]]] for h in (x, y)] for g in reps]
    tree_words = {base: []}
    tree_edges = set()
    todo = deque([base])
    while todo:
        v = todo.popleft()
        for letter in (1, 2, -1, -2):
            j = abs(letter)-1
            dest = edges[v][j] if letter > 0 else back_edges[v][j]
            if dest not in tree_words:
                tree_words[dest] = tree_words[v]+[letter]
                tree_edges.add((v, j) if letter > 0 else (dest, j))
                todo.append(dest)
    assert len(tree_words) == 20 and len(tree_edges) == 19
    chords = [(v, j) for v in range(20) for j in range(2) if (v, j) not in tree_edges]
    chord_index = {edge: i+1 for i, edge in enumerate(chords)}
    assert len(chords) == 21

    def rewrite(word, start=base):
        v, out = start, []
        for letter in word:
            j = abs(letter)-1
            dest = edges[v][j] if letter > 0 else back_edges[v][j]
            edge = (v, j) if letter > 0 else (dest, j)
            if edge in chord_index:
                out.append(chord_index[edge] if letter > 0 else -chord_index[edge])
            v = dest
        return v, out

    schreier_words = [tree_words[v]+[j+1]+inverse_word(tree_words[edges[v][j]])
                     for v, j in chords]
    assert all(rewrite(word) == (base, [i+1]) for i, word in enumerate(schreier_words))
    schreier_values = [evaluate(word) for word in schreier_words]
    assert all(g in C for v, g in schreier_values)
    boundaries, boundary_words, cycles = [], [], []
    for letter_word, h in (([1], x), ([2], y), ([-2, -1], z)):
        remaining, cs = set(range(20)), []
        while remaining:
            first = min(remaining)
            cyc, v = [], first
            while v in remaining:
                remaining.remove(v)
                cyc.append(v)
                v = which[H.mul[reps[v]][h]]
            assert v == first and len(cyc) == 5
            cs.append(cyc)
            word = tree_words[first]+letter_word*5+inverse_word(tree_words[first])
            end, based = rewrite(word)
            assert end == base and evaluate(word) == (0, H.one)
            boundaries.append(based)
            boundary_words.append(word)
        cycles.append(cs)
    assert list(map(len, cycles)) == [4, 4, 4]
    genus = (20+2-len(boundaries))//2
    assert genus == 5

    invariant_forms = [f for f in range(16)
                       if all(parity(f & module_action(c, v)) == parity(f & v)
                              for v in range(16))]
    form_basis = []
    for f in invariant_forms:
        if rank(form_basis+[f]) > len(form_basis):
            form_basis.append(f)
    assert len(form_basis) == 2
    big_forms = [f << (4*j) for f in form_basis for j in range(4)]
    character_rows = [[parity(f & v) for v, g in schreier_values] for f in big_forms]
    assert rank([sum(a << j for j, a in enumerate(row)) for row in character_rows]) == 8

    def heisenberg_boundary(chi, psi, word):
        a = b = central = 0
        for letter in word:
            u, v = chi[abs(letter)-1], psi[abs(letter)-1]
            central ^= (u & v if letter < 0 else 0) ^ (a & v)
            a ^= u
            b ^= v
        assert a == b == 0
        return central

    cup = [[sum(heisenberg_boundary(a, b, word) for word in boundaries) % 2
            for b in character_rows] for a in character_rows]
    assert all(cup[i][i] == 0 for i in range(8))
    assert all(cup[i][j] == cup[j][i] for i, j in product(range(8), repeat=2))
    cup_rows = [sum(value << j for j, value in enumerate(row)) for row in cup]
    print('Cover degree20, genus5, boundaries4+4+4; invariant character dimension8', flush=True)
    print('Actual mod-two cup-form rank:', rank(cup_rows), flush=True)
    print('Cup matrix:', cup, flush=True)

    # Companion of Phi_5, acting on the four module copies.  Search all
    # conjugates and all nonzero first character vectors, then solve the
    # five linear equations in the second vector exactly.
    companion = (2, 4, 8, 15)
    assert all(apply(companion, apply(companion, apply(companion,
               apply(companion, apply(companion, v))))) == v for v in range(16))

    def mat_comp(a, b):
        return tuple(apply(a, col) for col in b)

    def mat_inv(a):
        return tuple(next(v for v in range(16) if apply(a, v) == 1 << i) for i in range(4))

    def dual(a, f):
        return sum(parity(f & a[j]) << j for j in range(4))

    def dual_big(a, f):
        return dual(a, f & 15) | (dual(a, f >> 4) << 4)

    def cup_value(f, g):
        return parity(reduce(int.__xor__,
                      (cup_rows[i] for i in range(8) if (f >> i) & 1), 0) & g)

    def solve(rows, rhs, width):
        augmented = [row | (b << width) for row, b in zip(rows, rhs)]
        reduced_rows, ps = rref(augmented, width)
        if any(row == 1 << width for row in reduced_rows):
            return None
        # rref omits a pivot in the augmented column; test leftover rows.
        if rank(augmented) > rank(rows):
            return None
        return sum(((row >> width) & 1) << p for row, p in zip(reduced_rows, ps))

    witness = None
    tried = set()
    for change in permutations(range(1, 16), 4):
        if rank(change) != 4:
            continue
        T = mat_comp(mat_inv(change), mat_comp(companion, change))
        if T in tried:
            continue
        tried.add(T)
        powers = [(1, 2, 4, 8)]
        for j in range(4):
            powers.append(mat_comp(powers[-1], T))
        for f in range(1, 256):
            linear_rows = []
            for power in powers:
                first = dual_big(power, f)
                linear_rows.append(sum(cup_value(first, dual_big(power, 1 << k)) << k
                                       for k in range(8)))
            for wanted in ((1, 0, 0, 0, 0), (0, 1, 1, 1, 1)):
                g = solve(linear_rows, wanted, 8)
                if g is not None:
                    assert g not in (0, f)
                    actual = [cup_value(dual_big(power, f), dual_big(power, g)) for power in powers]
                    assert actual == list(wanted)
                    witness = {'multiplicity_matrix_columns': T, 'first_form_coordinates': f,
                               'second_form_coordinates': g, 'cup_sequence': actual,
                               'change_of_basis_columns': change}
                    break
            if witness is not None:
                break
        if witness is not None:
            break
        if rank(cup_rows) == 0:
            break
    print('Order-five cup-pattern witness:', witness, flush=True)

    payload = {
        'status': 'PASS_DELETED_A5_MODULE_AND_EXACT_CUP_TEST',
        'scope': 'Exact source module and surface-cover cup test only; no A6 chief lifting conclusion.',
        'A5_elements': H.elements, 'A5_source_indices': [x, y, z],
        'A5_source_permutations': [H.elements[g] for g in (x, y, z)],
        'C3_generator_index': c, 'module_basis': ['e0+e4', 'e1+e4', 'e2+e4', 'e3+e4'],
        'module_action_columns': matrices, 'nonzero_vector_orbit_span_ranks': orbit_span_ranks,
        'module_endomorphisms': endomorphisms,
        'crossed_constraint_rows': constraints, 'crossed_constraint_rref': reduced,
        'crossed_constraint_pivots': pivots, 'coboundaries': coboundaries,
        'Z1_dimension': 4, 'B1_dimension': 4, 'H1_dimension': 0,
        'source_quotient_basis': quotient_basis,
        'source_big_vectors': [vx, vy], 'source_group_order': 60*(2**16),
        'source_kernel_relators': source_relators,
        'source_kernel_relator_values': relation_values,
        'source_normal_module_span_rank': normal_module_span_rank,
        'cover_cosets': [sorted(coset) for coset in cosets],
        'cover_positive_edges': edges, 'tree_words': tree_words,
        'schreier_words': schreier_words, 'schreier_values': schreier_values,
        'peripheral_cycles': cycles, 'boundary_words_in_F2': boundary_words,
        'boundary_words_in_Schreier_basis': boundaries, 'genus': genus,
        'C3_invariant_dual_basis': form_basis, 'character_rows': character_rows,
        'cup_matrix': cup, 'cup_rank': rank(cup_rows),
        'order_five_matrices_tested': len(tried), 'cup_pattern_witness': witness}
    HERE.joinpath('a_peripheral_a5_deleted.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
