#!/usr/bin/env python3
"""Exact modular-source conventions and the unique coprime cusp gauge.

The symbolic calculations take place in literal free products, and the
finite normalization test uses the actual quotient of C2*C3 with pure
kernel F5^2 and its specified S3 action. No general torsion-conjugacy
assertion is inferred from finite order equations.
"""
from collections import deque
from itertools import permutations, product
from pathlib import Path
import json
import numpy as np

from a_peripheral_count import Group, perm_mul

HERE = Path(__file__).resolve().parent
ORDERS = {1: 2, 2: 3, 3: 2}


def normal(word):
    stack = []
    for letter in word:
        factor, exponent = abs(letter), 1 if letter > 0 else -1
        if stack and stack[-1][0] == factor:
            exponent += stack.pop()[1]
        exponent %= ORDERS[factor]
        if exponent:
            stack.append((factor, exponent))
    return tuple(stack)


def literal(value):
    return [factor for factor, exponent in value for _ in range(exponent)]


def mul(*words):
    return literal(normal([a for w in words for a in w]))


def inv(word):
    return mul([-a for a in reversed(word)])


def power(word, a):
    if a < 0:
        return power(inv(word), -a)
    return mul(*([word]*a))


def conj(a, b):
    return mul(a, b, inv(a))


def source_words():
    s, r, S = [1], [2], [3]
    tau = mul(s, r)
    x, y = power(tau, -2), conj(s, power(tau, -2))
    z = inv(mul(x, y))
    assert conj(r, x) == y
    assert conj(r, y) == z
    assert conj(r, z) == x
    assert conj(s, x) == y and conj(s, y) == x
    assert conj(s, z) == conj(inv(x), z)
    pants3 = inv(mul(s, inv(r)))
    assert pants3 == mul(r, s) == conj(s, tau)
    assert mul(inv(r), s) == inv(tau)
    f, R = mul(s, S), mul(S, tau)
    assert R == mul(inv(f), r)
    assert mul(conj(s, f), f) == []
    three_cycle = mul(conj(power(r, 2), f), conj(r, f), f)
    assert three_cycle == inv(power(R, 3))
    gauges = []
    for a in range(-3, 4):
        xa = power(x, a)
        Snew = conj(xa, S)
        fnew = mul(s, Snew)
        assert fnew == mul(power(y, a), f, power(x, -a))
        assert mul(Snew, tau) == conj(xa, R)
        gauges.append({'integer_exponent': a,
                       'literal_new_conjugator': fnew})

    Q = Group('S3', list(permutations(range(3))), perm_mul, (0, 1, 2))
    qs, qr = Q.index[(1, 0, 2)], Q.index[(1, 2, 0)]

    def quotient(word):
        v = Q.one
        for a in word:
            g = qs if abs(a) == 1 else qr
            v = Q.mul[v][g if a > 0 else Q.inv[g]]
        return v

    reps = [[], s, r, power(r, 2), mul(s, r), mul(s, power(r, 2))]
    trans = {quotient(t): t for t in reps}
    assert len(trans) == 6
    rows, targets = [], set()
    for t in reps:
        for a in (1, 2):
            endpoint = quotient(t+[a])
            word = mul(t, [a], inv(trans[endpoint]))
            assert quotient(word) == Q.one
            rows.append({'coset_path': t, 'letter': a,
                         'Schreier_word': word})
            targets.add(tuple(word))
    basis_words = {1: x, -1: inv(x), 2: y, -2: inv(y)}
    found = {(): []}
    todo = deque([()])
    while not targets <= set(found):
        value = todo.popleft()
        expression = found[value]
        assert len(expression) < 8
        for a in (1, 2, -1, -2):
            new = tuple(mul(list(value), basis_words[a]))
            if new not in found:
                found[new] = expression+[a]
                todo.append(new)
    for row in rows:
        expression = found[tuple(row['Schreier_word'])]
        assert mul(*[basis_words[a] for a in expression]) == row['Schreier_word']
        row['word_in_x_y'] = expression
    return {'s': s, 'r': r, 'tau': tau,
            'earlier_inverse_cusp': inv(tau),
            'pants_generators': [s, inv(r)], 'third_pants_boundary': pants3,
            'pure_basis': {'x': x, 'y': y, 'z': z},
            'all_six_coset_schreier_rows': rows,
            'graph_edges_vertices_rank': [6, 5, 2],
            'generic_involution_symbol': S,
            'generic_f': f, 'generic_R': R,
            'literal_three_cycle_equals_inverse_R_cube': three_cycle,
            'integer_cusp_gauges': gauges}


def finite_gauge():
    p = 5
    Q = Group('S3', list(permutations(range(3))), perm_mul, (0, 1, 2))
    qs, qr = Q.index[(1, 0, 2)], Q.index[(1, 2, 0)]
    sm = np.array([[0, 1], [1, 0]], dtype=np.int64)
    rm = np.array([[0, -1], [1, -1]], dtype=np.int64) % p
    matrices = {Q.one: np.eye(2, dtype=np.int64)}
    todo = deque([Q.one])
    while todo:
        a = todo.popleft()
        for b, B in ((qs, sm), (qr, rm)):
            c, C = Q.mul[a][b], matrices[a] @ B % p
            if c in matrices:
                assert np.array_equal(matrices[c], C)
            else:
                matrices[c] = C
                todo.append(c)
    assert len(matrices) == 6
    E = Group(
        'F5^2 semidirect S3',
        [(v, d) for v in product(range(p), repeat=2) for d in range(Q.size)],
        lambda a, b: (
            tuple(map(int, (np.array(a[0])+matrices[a[1]] @ np.array(b[0])) % p)),
            Q.mul[a[1]][b[1]]),
        ((0, 0), Q.one))
    s, r = E.index[((0, 0), qs)], E.index[((1, 0), qr)]
    tau = E.mul[s][r]
    x = E.power(tau, -2)
    y = E.conjugate(s, x)
    assert E.elements[x] == ((1, 0), Q.one)
    assert E.elements[y] == ((0, 1), Q.one)
    assert E.orders[s] == 2 and E.orders[r] == 3
    assert len(E.generated([s, r])) == 150
    kernel = [a for a in range(E.size) if E.elements[a][1] == Q.one]
    centralizer = set(kernel) & E.centralizer(tau)
    assert centralizer == {E.power(x, a) for a in range(p)}
    records = []
    for v in kernel:
        old_s, old_r = E.conjugate(v, s), E.conjugate(v, r)
        old_tau = E.conjugate(v, tau)
        for k in range(p):
            c = E.mul[v][E.power(x, k)]
            assert E.conjugate(c, tau) == old_tau
            S = E.conjugate(E.inv[c], old_s)
            R = E.conjugate(E.inv[c], old_r)
            assert E.mul[S][R] == tau
            f = E.mul[s][S]
            a, b = E.elements[f][0]
            assert (a+b) % p == 0
            gauge = E.power(x, a)
            final_s, final_r = E.conjugate(gauge, S), E.conjugate(gauge, R)
            final_f = E.mul[s][final_s]
            assert final_s == s and final_r == r and final_f == E.one
            records.append({'kernel_inner': list(E.elements[v][0]),
                            'centralizer_parameter': k,
                            'tau_normalizing_conjugator': list(E.elements[c][0]),
                            'pre_gauge_f': list(E.elements[f][0]),
                            'unique_gauge': a,
                            'final_f': list(E.elements[final_f][0])})
    assert len(records) == 125
    return {'prime': p, 'order': E.size,
            'S3_elements': [list(a) for a in Q.elements],
            'S3_matrices': [matrices[a].tolist() for a in range(Q.size)],
            'actual_generators': {
                's': [list(E.elements[s][0]), E.elements[s][1]],
                'r': [list(E.elements[r][0]), E.elements[r][1]]},
            'tau_order': E.orders[tau], 'pure_basis': [list(E.elements[x][0]),
                                                     list(E.elements[y][0])],
            'all_kernel_cusp_centralizer_elements': [
                list(E.elements[a][0]) for a in sorted(centralizer)],
            'complete_normalization_cases': records}


def main():
    words = source_words()
    gauge = finite_gauge()
    payload = {
        'status': 'PASS_MODULAR_SOURCE_AND_EXACT_COPRIME_GAUGE',
        'literal_source_maps': words,
        'finite_actual_modular_quotient': gauge,
        'scope': ('The word identities certify the precise conventions and '
                  'both cycle comparisons. The 125 finite cases check the '
                  'unique cusp normalization on one actual coprime modular '
                  'quotient. The general lifting assertion uses D42/D43 '
                  'and the proved residual/abelianization maps.')}
    HERE.joinpath('a_modular_coprime.json').write_text(json.dumps(payload, indent=2)+'\n')
    print('PASS all12 Schreier generator expressions in the exact pure basis x,y')
    print('PASS literal s swap, r cycle, pants/cusp convention conversion, and both gentle cycle identities')
    print('PASS seven signed integer gauge identities in the actual free-product words')
    print('PASS actual modular quotient of order150, pure F5^2, all125 kernel-normalization choices')
    print(payload['status'])


if __name__ == '__main__':
    main()
