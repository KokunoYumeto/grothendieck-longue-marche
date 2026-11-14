#!/usr/bin/env python3
"""Actual source, framed Shapiro, and conjugator certificate for D.36.

Construct one generating surface homomorphism in each of the five colour
families, transport it back to the exact Schreier basis, and form its
twisted induced source pair.  Every based path and local conjugator is
checked literally.  The large exhaustion product is specified in the
proof by finite lexicographic lists, using the separately exact counts.
"""

from functools import reduce
from itertools import product
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('finite_count', HERE/'a_peripheral_count.py')
finite = importlib.util.module_from_spec(spec)
spec.loader.exec_module(finite)


def apply(columns, vector):
    return reduce(int.__xor__, (column for i, column in enumerate(columns) if (vector >> i) & 1), 0)


def parity(x):
    return x.bit_count() & 1


def inverse_word(word):
    return [-a for a in reversed(word)]


def main():
    raw = json.loads(HERE.joinpath('a_peripheral_a5_deleted.json').read_text())
    surf = json.loads(HERE.joinpath('a_peripheral_surface20_framed.json').read_text())
    count = json.loads(HERE.joinpath('a_peripheral_a6_boundary_framed_flip.json').read_text())
    group = json.loads(HERE.joinpath('a_peripheral_a6_outer.json').read_text())
    nielsen = json.loads(HERE.joinpath('a_peripheral_a6_nielsen.json').read_text())
    pairs = [tuple(p) for p in group['automorphism_generator_pairs']]
    maps = dict(zip(pairs, group['automorphism_maps']))
    aa, bb = group['A6_generators']
    G = finite.Group('Aut(A6)', pairs,
                     lambda x, y: (maps[x][y[0]], maps[x][y[1]]), (aa, bb))
    outer = group['outer_coordinates']
    inner = frozenset(group['inner_indices'])
    relative_classes = [frozenset(c) for c in group['relative_classes']]
    class_of = {g: i for i, c in enumerate(relative_classes) for g in c}
    class_action = group['outer_class_action']
    qsource = nielsen['profiles'][0]['proper_orbit_representatives'][0]
    assert qsource == [0, 24, 1380]
    assert len(G.generated(qsource[:2])) == 1440
    assert G.mul[G.mul[qsource[0]][qsource[1]]][qsource[2]] == G.one
    assert [outer[g] for g in qsource] == [1, 2, 3]
    qcentralizers = [sorted(G.centralizer(g)) for g in qsource]
    assert [{outer[h] for h in C} for C in qcentralizers] == [{0, 1}, {0, 2}, {0, 3}]
    qouter = {outer[g]: g for g in qsource}

    H = [tuple(p) for p in raw['A5_elements']]
    hi = {p: i for i, p in enumerate(H)}
    h_one = hi[tuple(range(5))]
    hmul = lambda a, b: hi[tuple(H[a][H[b][i]] for i in range(5))]
    hinv = [next(b for b in range(60) if hmul(a, b) == h_one) for a in range(60)]
    matrices = raw['module_action_columns']
    hsource = raw['A5_source_indices']
    vx, vy = raw['source_big_vectors']
    T = raw['cup_pattern_witness']['multiplicity_matrix_columns']
    powers = [[1, 2, 4, 8]]
    for _ in range(5):
        powers.append([apply(T, col) for col in powers[-1]])
    assert powers[-1] == [1, 2, 4, 8] and powers[1] != powers[0]
    f, g = surf['outer_module_forms']

    def epsilon(v):
        return parity(f & v) | (parity(g & v) << 1)

    def hact(h, v):
        return sum(apply(matrices[h], (v >> (4*j)) & 15) << (4*j) for j in range(4))

    def tact(t, v):
        blocks = [(v >> (4*j)) & 15 for j in range(4)]
        return sum(reduce(int.__xor__, (blocks[j] for j in range(4) if (t[j] >> i) & 1), 0)
                   << (4*i) for i in range(4))

    assert all(tact(T, hact(h, 1 << i)) == hact(h, tact(T, 1 << i))
               for h in range(60) for i in range(16))
    C = {h_one, raw['C3_generator_index'],
         hmul(raw['C3_generator_index'], raw['C3_generator_index'])}
    character_conjugators = []
    for j, k in product(range(5), repeat=2):
        witnesses = [h for h in range(60)
                     if all(epsilon(tact(powers[j], hact(h, 1 << i))) ==
                            epsilon(tact(powers[k], 1 << i)) for i in range(16))]
        assert set(witnesses) == (C if j == k else set())
        character_conjugators.append({'j': j, 'k': k, 'conjugators': witnesses})
    assert raw['source_normal_module_span_rank'] == 16
    print('PASS: source module rank16, actual order-five action, and all25 character-conjugator sets', flush=True)

    def dmul(a, b):
        return a[0] ^ hact(a[1], b[0]), hmul(a[1], b[1])

    def dinv(a):
        return hact(hinv[a[1]], a[0]), hinv[a[1]]

    dgens = {1: (vx, hsource[0]), 2: (vy, hsource[1])}
    dgens.update({-j: dinv(value) for j, value in list(dgens.items())})

    def deval(word):
        out = (0, h_one)
        for letter in word:
            out = dmul(out, dgens[letter])
        return out

    def geval(word, values):
        out = G.one
        for letter in word:
            value = values[abs(letter)]
            out = G.mul[out][value if letter > 0 else G.inv[value]]
        return out

    tree = {int(k): word for k, word in raw['tree_words'].items()}
    cosets = raw['cover_cosets']
    coset_of = {h: i for i, coset in enumerate(cosets) for h in coset}
    base = coset_of[h_one]
    edges = raw['cover_positive_edges']
    back = [[coset_of[hmul(min(cosets[v]), hinv[h])] for h in hsource[:2]] for v in range(20)]
    chord_words = {tuple(word): i+1 for i, word in enumerate(raw['schreier_words'])}
    chords = {}
    for v in range(20):
        for j in range(2):
            word = tree[v]+[j+1]+inverse_word(tree[edges[v][j]])
            if tuple(word) in chord_words:
                chords[v, j] = chord_words[tuple(word)]
    assert len(chords) == 21

    def rewrite(word):
        v, out = base, []
        for letter in word:
            j = abs(letter)-1
            dest = edges[v][j] if letter > 0 else back[v][j]
            edge = (v, j) if letter > 0 else (dest, j)
            if edge in chords:
                out.append(chords[edge] if letter > 0 else -chords[edge])
            v = dest
        assert v == base
        return out

    path_values = [deval(tree[v]) for v in range(20)]
    path_q = [geval(tree[v], {1: qsource[0], 2: qsource[1]}) for v in range(20)]
    starts = surf['boundary_start_cosets']
    profile = (12, 7, 5)
    pi = next(i for i, p in enumerate(count['profiles']) if tuple(p) == profile)
    boundary_class_rows = count['boundary_profiles_for_each_power'][pi]
    counts = count['whole_group_epimorphism_counts'][pi]
    assert len(set(counts[1:])) == 1 and counts[0] > counts[1] > 0
    assert all(n % 360 == 0 for n in counts)
    high, low = counts[0]//360, counts[1]//360
    assert [o for o in range(4) if all(class_action[o][ci] == ci for ci in profile)] == [0]
    global_cycle_classes = [class_action[epsilon(path_values[v][0]) ^ (2 if i == 0 else 0)][profile[i//4]]
                            for i, v in enumerate(starts)]
    peripheral_words = [[1], [2], [-2, -1]]
    dperipherals = [deval(word) for word in peripheral_words]
    hcentralizers = []
    for v, h in dperipherals:
        assert deval(peripheral_words[len(hcentralizers)]*5) == (0, h_one)
        ch = [k for k in range(60) if hmul(k, h) == hmul(h, k)]
        assert len(ch) == 5
        assert len({w ^ apply(matrices[h], w) for w in range(16)}) == 16
        hcentralizers.append(ch)
    print('PASS: complete base centralizer images are the three outer lines', flush=True)

    # Actual reference peripheral elements in the twisted induced group.
    reference = []
    for i, ((v, h), qi) in enumerate(zip(dperipherals, qsource)):
        array = [None]*20
        forced = [epsilon(hact(path_values[w][1], v)) ^ outer[qi] for w in range(20)]
        for cycle_number, cycle in enumerate(raw['peripheral_cycles'][i]):
            target = min(relative_classes[global_cycle_classes[4*i+cycle_number]])
            prod = G.one
            for w in cycle[:-1]:
                array[w] = next(g for g in range(G.size) if outer[g] == forced[w])
                prod = G.mul[prod][array[w]]
            array[cycle[-1]] = G.mul[G.inv[prod]][target]
        assert [outer[g] for g in array] == forced
        reference.append(array)

    identity_image = ([G.one]*20, list(range(20)))

    def image_mul(a, b):
        za, pa = a
        zb, pb = b
        return [G.mul[za[w]][zb[pa[w]]] for w in range(20)], [pb[pa[w]] for w in range(20)]

    def image_inv(a):
        z, p = a
        pinv = [p.index(w) for w in range(20)]
        return [G.inv[z[pinv[w]]] for w in range(20)], pinv

    def image_eval(word, gens):
        allgens = dict(gens)
        allgens.update({-j: image_inv(value) for j, value in gens.items()})
        out = identity_image
        for letter in word:
            out = image_mul(out, allgens[letter])
        return out

    def product_g(values):
        out = G.one
        for value in values:
            out = G.mul[out][value]
        return out

    witness_records = []
    for j in range(5):
        boundary_values = [min(relative_classes[ci]) for ci in boundary_class_rows[j]]
        chars = surf['handle_outer_characters'][j]
        generating_handle = next(i for i, (r, s) in enumerate(chars)
                                 if r and s and r != s)
        unknown_handle = next(i for i in range(5) if i != generating_handle)
        handles = [[G.one if r == 0 else next(g for g in range(G.size) if outer[g] == r),
                    G.one if s == 0 else next(g for g in range(G.size) if outer[g] == s)]
                   for r, s in chars]
        r, s = chars[generating_handle]
        handles[generating_handle] = [qouter[r], qouter[s]]
        assert len(G.generated(handles[generating_handle])) == G.size
        before = product_g(G.commutator(*handles[i]) for i in range(unknown_handle))
        after = product_g(G.commutator(*handles[i]) for i in range(unknown_handle+1, 5))
        boundary_product = product_g(G.inv[boundary_values[abs(a)-22]] for a in surf['final_boundary_word'])
        target = G.mul[G.mul[G.inv[before]][G.inv[boundary_product]]][G.inv[after]]
        r, s = chars[unknown_handle]
        handles[unknown_handle] = next([a, b] for a in range(G.size) if outer[a] == r
                                      for b in range(G.size) if outer[b] == s
                                      and G.commutator(a, b) == target)
        assert G.mul[product_g(G.commutator(*pair) for pair in handles)][boundary_product] == G.one
        final_handles = [pair[:] for pair in handles]
        values = {22+i: v for i, v in enumerate(boundary_values)}
        for step in reversed(surf['handle_extractions']):
            A, B = handles[-1]
            U, V, W = [geval(step[key], values) for key in ('U', 'V', 'W')]
            Cvalue = G.mul[G.mul[W][V]][U]
            values[step['first_variable']] = G.mul[G.mul[Cvalue][A]][G.inv[U]]
            bvalue = G.mul[G.mul[B][G.inv[U]]][G.inv[V]]
            bsigned = step['second_signed_variable']
            values[abs(bsigned)] = bvalue if bsigned > 0 else G.inv[bvalue]
            conjugator = G.mul[geval(step['cyclic_prefix'], values)][Cvalue]
            handles = [[G.conjugate(conjugator, a), G.conjugate(conjugator, b)] for a, b in handles[:-1]]
        for step in reversed(surf['face_eliminations']):
            values[step['eliminated_generator']] = geval(step['replacement'], values)
        phi = {i: values[i] for i in range(1, 22)}
        assert len(G.generated(list(phi.values()))) == G.size
        assert [outer[phi[i]] for i in range(1, 22)] == surf['source_characters_on_Schreier_basis'][j]
        assert [geval(word, phi) for word in raw['boundary_words_in_Schreier_basis']] == boundary_values
        assert [[geval(A, phi), geval(B, phi)] for A, B in surf['handle_words_in_Schreier_basis']] == final_handles

        forced_path_outer = [epsilon(tact(powers[j], v)) ^ outer[q]
                             for (v, h), q in zip(path_values, path_q)]
        gauge = [G.one if w == base else next(g for g in range(G.size) if outer[g] == forced_path_outer[w])
                 for w in range(20)]
        assert forced_path_outer[base] == 0
        source_images = {}
        for letter in (1, 2):
            array = []
            for w in range(20):
                dest = edges[w][letter-1]
                k = rewrite(tree[w]+[letter]+inverse_word(tree[dest]))
                array.append(G.mul[G.mul[G.inv[gauge[w]]][geval(k, phi)]][gauge[dest]])
            v = tact(powers[j], (vx, vy)[letter-1])
            forced = [epsilon(hact(path_values[w][1], v)) ^ letter for w in range(20)]
            assert [outer[g] for g in array] == forced
            source_images[letter] = (array, [edges[w][letter-1] for w in range(20)])
        peripheral_images = [image_eval(word, source_images)[0] for word in peripheral_words]
        literal_conjugators = []
        for i in range(3):
            u = surf['local_base_conjugator_module_vectors'][j][i]
            Hlift = [next(g for g in range(G.size)
                          if outer[g] == epsilon(hact(path_values[w][1], u))) for w in range(20)]
            permutation = image_eval(peripheral_words[i], source_images)[1]
            moved_reference = [G.mul[G.mul[Hlift[w]][reference[i][w]]][G.inv[Hlift[permutation[w]]]]
                               for w in range(20)]
            kernel_conjugator = [None]*20
            for cycle_number, cycle in enumerate(raw['peripheral_cycles'][i]):
                oldprod = product_g(moved_reference[w] for w in cycle)
                newprod = product_g(peripheral_images[i][w] for w in cycle)
                expected_class = class_action[surf['local_conjugator_outer_values'][j][4*i+cycle_number]][global_cycle_classes[4*i+cycle_number]]
                assert class_of[newprod] == class_of[oldprod] == expected_class
                a0 = next(a for a in sorted(inner) if G.conjugate(a, oldprod) == newprod)
                value = a0
                for w in cycle:
                    kernel_conjugator[w] = value
                    value = G.mul[G.mul[G.inv[peripheral_images[i][w]]][value]][moved_reference[w]]
                assert value == a0
            assert all(a in inner for a in kernel_conjugator)
            literal = [G.mul[kernel_conjugator[w]][Hlift[w]] for w in range(20)]
            assert all(G.mul[G.mul[literal[w]][reference[i][w]]][G.inv[literal[permutation[w]]]] ==
                       peripheral_images[i][w] for w in range(20))
            literal_conjugators.append(literal)
        witness_records.append({'colour': j, 'surface_generator_images': [phi[i] for i in range(1, 22)],
                                'surface_handle_images': final_handles, 'surface_boundary_images': boundary_values,
                                'path_gauge': gauge, 'source_x_images': source_images[1][0],
                                'source_y_images': source_images[2][0],
                                'source_peripheral_images': peripheral_images,
                                'actual_peripheral_conjugators_over_prescribed_base': literal_conjugators})
        print('PASS colour', j, ': actual generating surface map, induced pair, all12 cycle products and60 conjugator coordinates', flush=True)
    payload = {'status': 'PASS_ACTUAL_ORDER_FIVE_A6_SOURCE_AND_BASED_TRANSPORT',
               'base_Q_source': qsource, 'complete_Q_peripheral_centralizers': qcentralizers,
               'complete_A5_peripheral_centralizers': hcentralizers,
               'source_base_order': 60*(2**16)*1440,
               'source_outer_module_forms': [f, g],
               'multiplicity_order_five_matrix': T,
               'all_outer_character_conjugators': character_conjugators,
               'boundary_profile': profile, 'fixed_first_boundary_outer_flip': 2,
               'global_reference_cycle_classes': global_cycle_classes,
               'actual_global_reference_peripheral_components': reference,
               'epimorphism_counts': counts, 'kernel_counts': [high]+[low]*4,
               'high_count': high, 'low_count': low, 'positive_excess': high-low,
               'five_actual_source_maps': witness_records,
               'scope': 'Finite source and framed transport certificate used with the exact simple-kernel exhaustion proof in D.36.'}
    HERE.joinpath('a_peripheral_order5_certificate.json').write_text(json.dumps(payload, indent=2)+'\n')
    print('Distinct kernel counts:', [high]+[low]*4, '; excess', high-low, flush=True)
    print(payload['status'])


if __name__ == '__main__':
    main()
