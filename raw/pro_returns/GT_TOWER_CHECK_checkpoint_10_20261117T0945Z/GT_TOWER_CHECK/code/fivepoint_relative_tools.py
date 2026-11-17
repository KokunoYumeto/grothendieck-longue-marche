"""Exact source words for the pending relative five-point detector.

Gamma_0,5 is the actual P4/center with generators
a=A13,b=A23,x=A14,y=A24,z=A34.  Word products run left to right.
This module performs no output-file writes when imported.
"""
from collections import deque
from itertools import product
import numpy as np


def inverse(w):
    return tuple(-i for i in reversed(w))


def reduce_word(w):
    result = []
    for i in w:
        if result and result[-1] == -i:
            result.pop()
        else:
            result.append(int(i))
    return tuple(result)


def subst(w, images):
    return reduce_word(j for i in w for j in
                       (images[i - 1] if i > 0 else inverse(images[-i - 1])))


def small_comm(u, v):
    return (-v, -u, v, u)


relations = []
for left, right in [
    ((1, 3, -1), (-5, 3, 5)),
    ((1, 4, -1), small_comm(3, 5) + (4,) + inverse(small_comm(3, 5))),
    ((1, 5, -1), small_comm(3, 5) + (5,)),
    ((2, 3, -2), (3,)),
    ((2, 4, -2), (-5, 4, 5)),
    ((2, 5, -2), small_comm(4, 5) + (5,)),
]:
    relations.append(reduce_word(left + inverse(right)))


# The literal conjugation actions of a and b on F(x,y,z).
fa = ((-3, 1, 3), small_comm(1, 3) + (2,) + inverse(small_comm(1, 3)),
      small_comm(1, 3) + (3,))
fb = ((1,), (-3, 2, 3), small_comm(2, 3) + (3,))


def inverse_pair_twist(g, h, remaining=None):
    # a acts on x,z by conjugation with (xz)^-1, and its y-conjugator
    # is a(z)z^-1.  The inverse acts on x,z by conjugation with xz.
    pair = (g, h)
    images = [(1,), (2,), (3,)]
    images[g - 1] = reduce_word(pair + (g,) + inverse(pair))
    images[h - 1] = reduce_word(pair + (h,) + inverse(pair))
    if remaining is not None:
        c = reduce_word(images[h - 1] + (-h,))
        images[remaining - 1] = reduce_word(c + (remaining,) + inverse(c))
    return tuple(images)


fai = inverse_pair_twist(1, 3, remaining=2)
fbi = inverse_pair_twist(2, 3)
for f, fi in ((fa, fai), (fb, fbi)):
    assert tuple(subst(w, f) for w in fi) == ((1,), (2,), (3,))
    assert tuple(subst(w, fi) for w in f) == ((1,), (2,), (3,))


def fibre_action(base_word):
    images = ((1,), (2,), (3,))
    # phi_(ab) = phi_a o phi_b, hence substitute the preceding image
    # into the next elementary images.
    for i in base_word:
        f = {1: fa, 2: fb, -1: fai, -2: fbi}[i]
        images = tuple(subst(w, images) for w in f)
    return images


def abelian_schreier(rank, modulus=4):
    states = list(product(range(modulus), repeat=rank))
    index = {v: i for i, v in enumerate(states)}
    transitions = np.empty((len(states), rank), dtype=np.int32)
    for q, v in enumerate(states):
        for j in range(rank):
            w = list(v)
            w[j] = (w[j] + 1) % modulus
            transitions[q, j] = index[tuple(w)]
    paths = {0: ()}
    tree = set()
    queue = deque([0])
    while queue:
        q = queue.popleft()
        for j in range(rank):
            v = int(transitions[q, j])
            if v not in paths:
                paths[v] = paths[q] + (j + 1,)
                tree.add((q, j))
                queue.append(v)
    chords = [(q, j) for q in range(len(states)) for j in range(rank)
              if (q, j) not in tree]
    chord_index = {e: i for i, e in enumerate(chords)}
    loops = [reduce_word(paths[q] + (j + 1,) +
                         inverse(paths[int(transitions[q, j])]))
             for q, j in chords]

    def rewrite(word, start=0):
        q = start
        output = []
        for i in word:
            if i > 0:
                edge = (q, i - 1)
                q = int(transitions[q, i - 1])
                sign = 1
            else:
                v = list(states[q])
                v[-i - 1] = (v[-i - 1] - 1) % modulus
                q = index[tuple(v)]
                edge = (q, -i - 1)
                sign = -1
            if edge in chord_index:
                output.append(sign * (chord_index[edge] + 1))
        return q, reduce_word(output)

    for i, w in enumerate(loops):
        assert rewrite(w) == (0, (i + 1,))
    return states, transitions, loops, rewrite
