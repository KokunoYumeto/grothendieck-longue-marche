#!/usr/bin/env python3
"""Independent source-word map to the compact quaternion detector."""
from pathlib import Path
import json
import numpy as np

D = Path(__file__).resolve().parents[1] / 'tower_code'
cover = json.loads((D / 'translation_cover_basis.json').read_text())
cover73 = json.loads((D / 'translation_quaternion_homology.json').read_text())
cover9 = json.loads((D / 'modular_quaternion_surface.json').read_text())
H = np.load(D / 'translation_quaternion_homology.npz')
Q = np.load(D / 'modular_quaternion_compact_setup.npz')
CP = np.load(D / 'modular_quaternion_homology_compressed.npz')['central_quotient_projection'].astype(np.int64)
projection = Q['quotient_projection'].astype(np.int64)


def red(word):
    answer = []
    for x in word:
        if answer and answer[-1] == -x:
            answer.pop()
        else:
            answer.append(int(x))
    return tuple(answer)


def inverse_word(word):
    return tuple(-x for x in reversed(word))


def substitute(word, generators):
    return red(y for x in word for y in
               (generators[x - 1] if x > 0 else inverse_word(generators[-x - 1])))


def rref(matrix):
    a = np.array(matrix, dtype=np.int64) % 3
    row, pivots = 0, []
    for col in range(a.shape[1]):
        candidates = np.flatnonzero(a[row:, col])
        if not len(candidates):
            continue
        k = row + int(candidates[0])
        a[[row, k]] = a[[k, row]]
        a[row] = a[row, col] * a[row] % 3
        for j in range(len(a)):
            if j != row:
                a[j] = (a[j] - a[j, col] * a[row]) % 3
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def rank(matrix):
    return len(rref(matrix)[1])


# Independent Q8 multiplication from its defining i,j relations.
coordinates = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)]
coordinates += [(a, b, 1) for a, b, _ in coordinates]
indices = {q: i for i, q in enumerate(coordinates)}


def multiply(q, r):
    a, b, c = coordinates[q]
    x, y, z = coordinates[r]
    return indices[((a + x) % 2, (b + y) % 2,
                    (c + z + b * x + (a + x) // 2 + (b + y) // 2) % 2)]


inverses = [next(j for j in range(8) if multiply(i, j) == 0) for i in range(8)]


def quotient_word(word, generator_images):
    q = 0
    for x in word:
        image = generator_images[abs(x) - 1]
        q = multiply(q, image if x > 0 else inverses[image])
    return q


def schreier(generator_images):
    n = len(generator_images)
    sections, queue, tree = {0: ()}, [0], set()
    for q in queue:
        for x in list(range(1, n + 1)) + list(range(-1, -n - 1, -1)):
            image = generator_images[abs(x) - 1]
            destination = multiply(q, image if x > 0 else inverses[image])
            if destination not in sections:
                sections[destination] = sections[q] + (x,)
                queue.append(destination)
                tree.add((q, x) if x > 0 else (destination, -x))
    chords = [(q, j) for q in range(8) for j in range(1, n + 1)
              if (q, j) not in tree]
    chord_index = {x: i + 1 for i, x in enumerate(chords)}

    def rewrite(word):
        q, output = 0, []
        for x in word:
            image = generator_images[abs(x) - 1]
            if x > 0:
                edge = q, x
                q = multiply(q, image)
            else:
                q = multiply(q, inverses[image])
                edge = q, -x
            if edge in chord_index:
                output.append(chord_index[edge] if x > 0 else -chord_index[edge])
        assert q == 0
        return red(output)

    basis = [red(sections[q] + (j,) + inverse_word(sections[multiply(q, generator_images[j - 1])]))
             for q, j in chords]
    return sections, basis, rewrite


sections9, basis9, rewrite9 = schreier([1, 2])
assert [list(w) for w in basis9] == cover9['schreier_basis']
standard_basis = [tuple(w) for w in cover['standard_basis_E']]
q_images = [quotient_word(w, [1, 2]) for w in standard_basis]
sections73, basis73, rewrite73 = schreier(q_images)
assert [list(w) for w in basis73] == cover73['schreier_basis_K3']
print('PASS: independently reconstructed both literal Schreier bases (ranks9 and73)')

pairs9 = [(i, j) for i in range(9) for j in range(i + 1, 9)]


def word_coordinates(word):
    abelian, central = np.zeros(9, dtype=np.int64), np.zeros(15, dtype=np.int64)
    for x in word:
        unit = np.zeros(9, dtype=np.int64)
        unit[abs(x) - 1] = 1 if x > 0 else -1
        wedge = np.array([abelian[i] * unit[j] - abelian[j] * unit[i]
                          for i, j in pairs9], dtype=np.int64)
        central = (central + 2 * wedge @ CP) % 3
        abelian = (abelian + unit) % 3
    return projection @ np.concatenate((abelian, central)) % 3


images = np.stack([word_coordinates(rewrite9(substitute(w, standard_basis)))
                   for w in basis73], axis=1)
assert images.shape == (14, 73) and rank(images) == 12
bracket = Q['bracket_matrix'].astype(np.int64)
pairs6 = [(i, j) for i in range(6) for j in range(i + 1, 6)]
for x in images.T:
    for y in images.T:
        assert not np.any(bracket @ np.array([x[i] * y[j] - x[j] * y[i]
                                             for i, j in pairs6]) % 3)
print('PASS: actual source-word homomorphism T→F3^12; every pair of generator images commutes')

peripheral = []
for word in cover['peripheral_words']:
    assert quotient_word(word, q_images) == 4
    for q in range(4):
        lifted = sections73[q] + tuple(word) + tuple(word) + inverse_word(sections73[q])
        homology = np.zeros(73, dtype=np.int64)
        for x in rewrite73(lifted):
            homology[abs(x) - 1] += 1 if x > 0 else -1
        peripheral.append(homology % 3)
peripheral = np.array(peripheral)
assert peripheral.shape == (36, 73) and rank(peripheral) == 35
assert not np.any(images @ peripheral.T % 3)
print('PASS: all36 actual peripheral lifts map to zero; their homology span has rank35')

central_deck = H['deck_matrices'][4].astype(np.int64)
assert np.array_equal(images @ central_deck % 3, -images % 3)
faithful_projector = 2 * (np.eye(73, dtype=np.int64) - central_deck) % 3
assert rank(faithful_projector) == 36
assert np.array_equal(images @ faithful_projector % 3, images)
C = H['quaternion_component_basis'].astype(np.int64)
CB = H['multiplicity_basis'].astype(np.int64)
assert rank(images @ C % 3) == 12 and rank(images @ CB % 3) == 6
print('PASS: the exact map kills the complete +1 central-deck summand and factors through dimension36')

K1, K2 = H['H73'].astype(np.int64) - np.eye(73, dtype=np.int64)
faithful_kernel = np.hstack((K1 @ K1 @ C, K1 @ K2 @ C, K2 @ K2 @ C)) % 3
assert rank(faithful_kernel) == 24
assert not np.any(images @ faithful_kernel % 3)
assert rank(images @ C % 3) + rank(faithful_kernel) == 36
print('PASS: full faithful kernel is exactly m_H^2 C_minus, dimension24')

H1, H2 = H['H18'].astype(np.int64)
I18 = np.eye(18, dtype=np.int64)
N1, N2 = (H1 - I18) % 3, (H2 - I18) % 3
augmentation_square = np.hstack((N1 @ N1, N1 @ N2, N2 @ N2)) % 3
multiplicity_map = images @ CB % 3
assert rank(augmentation_square) == 12
assert not np.any(multiplicity_map @ augmentation_square % 3)
assert rank(multiplicity_map) + rank(augmentation_square) == 18
print('PASS: multiplicity quotient has exact kernel m_H^2 M, dimension12; quotient dimension6')

np.savez_compressed(Path(__file__).with_suffix('.npz'),source_to_target=images,
                    peripheral_rows=peripheral,faithful_projector=faithful_projector,
                    faithful_kernel_generators=faithful_kernel,
                    multiplicity_map=multiplicity_map,
                    multiplicity_kernel_generators=augmentation_square)
Path(__file__).with_suffix('.json').write_text(json.dumps({
    'scope':'Actual source-word map to compact detector; exact faithful and augmentation-square factorization',
    'T_image_dimension':12,'peripheral_count':36,'peripheral_rank':35,
    'faithful_dimension':36,'multiplicity_quotient_dimension':6,
    'multiplicity_kernel_dimension':12,'multiplicity_kernel':'m_H^2 M'},indent=2)+'\n')
print('PASS. Signed ordinary periods remain joined separately as in the stated source quotient.')
