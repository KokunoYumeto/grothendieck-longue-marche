#!/usr/bin/env python3
"""Exact modular source check for the multifactor order-five search.

Construct SL2(F4)=A5 literally, choose a (3,3,5) source, and compute all
linear crossed-homomorphism constraints for its natural F4^2 module.
This tests whether two natural-module copies can occur in a two-generated
split extension before proposing any outer-action construction.
"""

from collections import deque
from functools import reduce
from itertools import product
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('finite_count', HERE/'a_peripheral_count.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def fm(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return c


def matrix_mul(a, b):
    return (fm(a[0], b[0]) ^ fm(a[1], b[2]),
            fm(a[0], b[1]) ^ fm(a[1], b[3]),
            fm(a[2], b[0]) ^ fm(a[3], b[2]),
            fm(a[2], b[1]) ^ fm(a[3], b[3]))


def rref(rows, n):
    rows = [list(row) for row in rows if any(row)]
    rank = 0
    pivots = []
    for col in range(n):
        pivot = next((j for j in range(rank, len(rows)) if rows[j][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = next(x for x in range(1, 4) if fm(x, rows[rank][col]) == 1)
        rows[rank] = [fm(x, inverse) for x in rows[rank]]
        for j in range(len(rows)):
            if j != rank and rows[j][col]:
                scalar = rows[j][col]
                rows[j] = [x ^ fm(scalar, y) for x, y in zip(rows[j], rows[rank])]
        pivots.append(col)
        rank += 1
    return rows[:rank], pivots


def main():
    elements = [a for a in product(range(4), repeat=4)
                if fm(a[0], a[3]) ^ fm(a[1], a[2]) == 1]
    H = module.Group('SL2(F4)', elements, matrix_mul, (1, 0, 0, 1))
    assert H.size == 60
    x, y = next((x, y) for x in range(60) for y in range(60)
                if H.orders[x] == H.orders[y] == 3
                and H.orders[H.mul[x][y]] == 5
                and len(H.generated([x, y])) == 60)
    zero = [[0]*4 for _ in range(2)]
    vx = [[1, 0, 0, 0], [0, 1, 0, 0]]
    vy = [[0, 0, 1, 0], [0, 0, 0, 1]]

    def act(g, v):
        a, b, c, d = H.elements[g]
        return [[fm(a, p) ^ fm(b, q) for p, q in zip(v[0], v[1])],
                [fm(c, p) ^ fm(d, q) for p, q in zip(v[0], v[1])]]

    def add(u, v):
        return [[a ^ b for a, b in zip(r, s)] for r, s in zip(u, v)]

    values = {H.one: zero}
    words = {H.one: []}
    todo = deque([H.one])
    constraints = []
    while todo:
        g = todo.popleft()
        for h, v, letter in ((x, vx, 1), (y, vy, 2)):
            k = H.mul[g][h]
            value = add(values[g], act(g, v))
            if k not in values:
                values[k] = value
                words[k] = words[g]+[letter]
                todo.append(k)
            else:
                constraints += add(value, values[k])
    reduced, pivots = rref(constraints, 4)
    dimension = 4-len(pivots)
    # Actual coboundaries at x,y, from both F4 basis vectors.
    coboundaries = []
    for v in ((1, 0), (0, 1)):
        images = []
        for h in (x, y):
            a, b, c, d = H.elements[h]
            images += [fm(a, v[0]) ^ fm(b, v[1]) ^ v[0],
                       fm(c, v[0]) ^ fm(d, v[1]) ^ v[1]]
        coboundaries.append(images)
    cob_reduced, cob_pivots = rref(coboundaries, 4)
    assert len(cob_pivots) == 2
    assert all(all(reduce(int.__xor__,
                    (fm(a, b) for a, b in zip(row, v)), 0) == 0 for row in reduced)
               for v in coboundaries)
    print('SL2(F4) source matrices:', H.elements[x], H.elements[y], 'orders3,3,5')
    print('Crossed-homomorphism constraint rank over F4:', len(pivots))
    print('Z1 dimension:', dimension, 'B1 dimension:', len(cob_pivots),
          'H1 dimension:', dimension-len(cob_pivots))
    print('Independent non-complement source directions:', len(pivots))
    payload = {'status': 'PASS_NATURAL_A5_MODULE_SOURCE_CONSTRAINTS',
               'field': 'F2[w]/(w^2+w+1), values0,1,w,w+1',
               'group_elements': H.elements, 'source': [x, y],
               'constraint_rref': reduced, 'constraint_pivots': pivots,
               'Z1_dimension': dimension, 'B1_dimension': len(cob_pivots),
               'H1_dimension': dimension-len(cob_pivots),
               'all_constraint_rows': constraints, 'coboundaries': coboundaries,
               'scope': 'Exact finite natural-module source calculation; no multifactor lift or obstruction is inferred.'}
    HERE.joinpath('a_peripheral_a5_module.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
