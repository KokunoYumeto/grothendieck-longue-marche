#!/usr/bin/env python3
"""Exact wreath and pullback certificates for the coupled D.27 family.

The 25 simple coordinate maps are checked by 300 literal distinguishing
relators.  All wreath source/peripheral maps are evaluated directly.
The central product uses the exact Clifford double cover from D.25.
An explicit nonidentity order-five special automorphism is constructed
inside the degree-four truncated associative algebra over F5, with
literal words proving its conjugators belong to the two-generator group.
"""

from itertools import product
from math import factorial
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('cycle', HERE/'a_peripheral_cycle.py')
cycle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cycle)
pmul, pinv = cycle.pmul, cycle.pinv
ONE = tuple(range(8))


def wmul(a, b):
    return (tuple(pmul(a[0][i], b[0][(i-a[1]) % 5]) for i in range(5)),
            (a[1]+b[1]) % 5)


def winv(a):
    return tuple(pinv(a[0][(i+a[1]) % 5]) for i in range(5)), -a[1] % 5


WONE = ((ONE,)*5, 0)


def wpow(a, k):
    if k < 0:
        a, k = winv(a), -k
    b = WONE
    while k:
        if k & 1:
            b = wmul(b, a)
        a = wmul(a, a)
        k >>= 1
    return b


def delta(a, k=0):
    return tuple(a if i == k else ONE for i in range(5))


def wconjugator(source, target, first):
    assert source[1] == target[1] and source[1] in (1, 4)
    h = [None]*5
    h[0] = first
    i = 0
    for _ in range(5):
        j = (i-source[1]) % 5
        value = pmul(pmul(pinv(target[0][i]), h[i]), source[0][i])
        if h[j] is not None:
            assert h[j] == value
        else:
            h[j] = value
        i = j
    result = (tuple(h), 0)
    assert wmul(wmul(result, source), winv(result)) == target
    return result


class CentralProduct:
    """(Spin(A8)^5 / even central signs) semidirect C5.

An element is (five permutations, shift, total central sign), relative
to the literal Clifford section cycle.Clifford.lift at each coordinate.
"""
    def __init__(self, cliff):
        self.cliff = cliff
        self.one = ((ONE,)*5, 0, 1)
        self.minus = ((ONE,)*5, 0, -1)

    def section_sign(self, value, perm):
        quotient = self.cliff.mul(value, self.cliff.inverse(self.cliff.lift(perm)))
        assert quotient in (self.cliff.one, self.cliff.minus)
        return 1 if quotient == self.cliff.one else -1

    def mul(self, a, b):
        p, sign = [], a[2]*b[2]
        for i in range(5):
            u, v = a[0][i], b[0][(i-a[1]) % 5]
            w = pmul(u, v)
            sign *= self.section_sign(self.cliff.mul(self.cliff.lift(u),
                                                     self.cliff.lift(v)), w)
            p.append(w)
        return tuple(p), (a[1]+b[1]) % 5, sign

    def inv(self, a):
        p, k = winv((a[0], a[1]))
        trial = (p, k, 1)
        sign = self.mul(a, trial)[2]
        result = (p, k, sign)
        assert self.mul(a, result) == self.one
        return result

    def power(self, a, n):
        if n < 0:
            a, n = self.inv(a), -n
        b = self.one
        while n:
            if n & 1:
                b = self.mul(b, a)
            a = self.mul(a, a)
            n >>= 1
        return b

    def order(self, a, bound=70):
        b = self.one
        for n in range(1, bound+1):
            b = self.mul(b, a)
            if b == self.one:
                return n
        raise AssertionError('explicit odd peripheral bound')


# The finite associative algebra F5<X,Y>/(words of length >=5).
P = 5
WEIGHT = 4


def clean(a):
    return {w: c % P for w, c in a.items() if c % P}


def padd(*values):
    out = {}
    for a in values:
        for w, c in a.items():
            out[w] = out.get(w, 0)+c
    return clean(out)


def scale(a, k):
    return clean({w: k*c for w, c in a.items()})


def mul(a, b):
    out = {}
    for u, c in a.items():
        for v, d in b.items():
            if len(u)+len(v) <= WEIGHT:
                out[u+v] = out.get(u+v, 0)+c*d
    return clean(out)


def power(a, n):
    result = {(): 1}
    for _ in range(n):
        result = mul(result, a)
    return result


def exp(a):
    return padd(*(scale(power(a, n), pow(factorial(n), -1, P))
                  for n in range(WEIGHT+1)))


def log(a):
    b = padd(a, {(): -1})
    return padd(*(scale(power(b, n), (-1)**(n+1)*pow(n, -1, P))
                  for n in range(1, WEIGHT+1)))


def inverse(a):
    return exp(scale(log(a), -1))


def bracket(a, b):
    return padd(mul(a, b), scale(mul(b, a), -1))


def group_commutator(a, b):
    return mul(mul(mul(a, b), inverse(a)), inverse(b))


def word_inverse(w):
    return [-i for i in reversed(w)]


def word_commutator(a, b):
    return a+b+word_inverse(a)+word_inverse(b)


def polynomial_word(word, x, y):
    values = {1: x, 2: y, -1: inverse(x), -2: inverse(y)}
    answer = {(): 1}
    for i in word:
        answer = mul(answer, values[i])
    return answer


def serialize_poly(a):
    return {''.join('X' if i == 0 else 'Y' for i in w): c
            for w, c in sorted(a.items(), key=lambda z: (len(z[0]), z[0]))}


def finite_beta():
    X, Y = {(0,): 1}, {(1,): 1}
    x, y = exp(X), exp(Y)
    z = mul(inverse(y), inverse(x))
    h = bracket(X, Y)
    f = padd(bracket(X, h), bracket(Y, h))
    g = bracket(Y, h)
    delta_y = bracket(f, Y)
    assert delta_y and delta_y == bracket(g, padd(X, Y))

    def beta(value):
        images = [X, padd(Y, delta_y)]
        out = {}
        for word, c in value.items():
            term = {(): c}
            for i in word:
                term = mul(term, images[i])
            out = padd(out, term)
        return out

    F, H = exp(f), exp(g)
    assert beta(x) == x
    assert beta(y) == mul(mul(F, y), inverse(F))
    assert beta(z) == mul(mul(H, z), inverse(H))
    assert beta(y) != y
    q = y
    for _ in range(5):
        q = beta(q)
    assert q == y

    cword = word_commutator([1], [2])
    uword = word_commutator([1], cword)
    vword = word_commutator([2], cword)
    dwords = [word_commutator([1], uword),
              word_commutator([2], uword), word_commutator([2], vword)]
    ds = [log(polynomial_word(w, x, y)) for w in dwords]
    assert all(all(len(w) == 4 for w in d) for d in ds)
    records = []
    for target, start in ((f, uword+vword), (g, vword)):
        initial = polynomial_word(start, x, y)
        error = padd(log(initial), scale(target, -1))
        correction = next(coeff for coeff in product(range(5), repeat=3)
                          if padd(*(scale(d, k) for d, k in zip(ds, coeff))) == error)
        word = start[:]
        for dword, k in zip(dwords, correction):
            word += word_inverse(dword)*k
        assert polynomial_word(word, x, y) == exp(target)
        records.append({'literal_word': word, 'central_correction': correction})
    return {'field': 5, 'truncation': 4,
            'group': 'subgroup generated by exp(X), exp(Y) in 1+augmentation ideal',
            'ambient_group_order': 5**30,
            'X_fixed': True, 'beta_order': 5, 'beta_nonidentity': True,
            'f_Lie': serialize_poly(f), 'g_Lie': serialize_poly(g),
            'delta_y': serialize_poly(delta_y),
            'normalized_y_conjugator_word': word_inverse(records[0]['literal_word']),
            'left_z_conjugator_word': records[1]['literal_word'],
            'conjugator_word_certificates': records,
            'beta_y': serialize_poly(beta(y)), 'beta_z': serialize_poly(beta(z)),
            'pro_cyclic_projection': 'coefficient of X in degree one; x maps to 1, y to 0'}


def main():
    data = json.loads(HERE.joinpath('a_peripheral_cycle_a8.json').read_text())
    recs = [data['records'][i] for i in data['selected_record_indices']]
    a = tuple(recs[0]['a'])
    bs = [tuple(r['b']) for r in recs]
    cs = [tuple(r['c']) for r in recs]
    cliff = cycle.Clifford(8)
    central = CentralProduct(cliff)
    x = (delta(a), 1)
    ys = [(delta(b), 0) for b in bs]
    zs = [winv(wmul(x, y)) for y in ys]
    assert wpow(x, 5) == ((a,)*5, 0)
    for j, y in enumerate(ys):
        for k in range(5):
            assert wmul(wmul(wpow(x, k), y), wpow(x, -k)) == (delta(bs[j], k), 0)
        assert wpow(zs[j], 5)[0][0] == cs[j]
    print('PASS: x^5 and all25 literal Schreier conjugates')

    relators = {(r['source_component'], r['target_component']): r['source_relator']
                for r in data['selected_pair_inequivalence_certificates']}
    coords = [(j, k) for j in range(5) for k in range(5)]
    maps = [[a]+[bs[j] if h == k else ONE for h in range(5)] for j, k in coords]
    witnesses = []
    for i, (j, k) in enumerate(coords):
        for l in range(i+1, len(coords)):
            r, s = coords[l]
            if k != s:
                word = [s+2]
            else:
                word = [(1 if abs(v) == 1 else k+2)*(1 if v > 0 else -1)
                        for v in relators[(j, r)]]
            assert cycle.eval_word(word, maps[i], ONE) == ONE
            target = cycle.eval_word(word, maps[l], ONE)
            assert target != ONE
            witnesses.append({'source': coords[i], 'target': coords[l],
                              'source_relator': word, 'target_value': target})
    assert len(witnesses) == 300
    print('PASS: all300 coordinate-kernel inequivalence witnesses')

    sign_a = central.section_sign(cliff.odd_lift(a, 7), a)
    X = (x[0], 1, sign_a)
    Y = [(y[0], 0, central.section_sign(cliff.odd_lift(b, 7), b))
         for y, b in zip(ys, bs)]
    Z = [central.inv(central.mul(X, y)) for y in Y]
    orders = [(central.order(X), central.order(y), central.order(z)) for y, z in zip(Y, Z)]
    assert orders == [(35, 7, 70)]+[(35, 7, 35)]*4
    conjugators = []
    products = []
    for j in range(5):
        hb0 = tuple(recs[0]['conjugator_a_to_b'])
        hbj = tuple(recs[j]['conjugator_a_to_b'])
        hy = (delta(pmul(hbj, pinv(hb0))), 0)
        assert wmul(wmul(hy, ys[0]), winv(hy)) == ys[j]
        hc0 = tuple(recs[0]['conjugator_a_to_c'])
        hcj = tuple(recs[j]['conjugator_a_to_c'])
        hz = wconjugator(zs[0], zs[j], pmul(hcj, pinv(hc0)))
        lifted_hy = (hy[0], 0, 1)
        lifted_hz = (hz[0], 0, 1)
        eligible_y = central.mul(central.mul(lifted_hy, Y[0]), central.inv(lifted_hy))
        eligible_z = central.mul(central.mul(lifted_hz, Z[0]), central.inv(lifted_hz))
        assert eligible_y == Y[j]
        expected_z = Z[j] if j == 0 else central.mul(central.minus, Z[j])
        assert eligible_z == expected_z
        result = central.mul(central.mul(X, eligible_y), eligible_z)
        assert result == (central.one if j == 0 else central.minus)
        products.append(result[2])
        conjugators.append({'target_row': j, 'y_base_conjugator': hy[0],
                            'z_base_conjugator': hz[0]})
    print('PASS: central-product peripheral orders', orders)
    print('PASS: complete allowed peripheral products', products)

    beta = finite_beta()
    print('PASS: explicit nonidentity order-five normalized peripheral beta')
    payload = {'status': 'PASS_COUPLED_WREATH_AND_PRO_FIVE_PULLBACK',
               'simple_group_order': 20160, 'rows': 5, 'columns': 5,
               'perfect_kernel_order': 20160**25,
               'base_quotient_order': 5*20160**25,
               'extension_order': 10*20160**25,
               'source_x': x, 'source_y_rows': ys, 'source_z_rows': zs,
               'schreier_basis': ['x^5']+[f'x^{k} y x^-{k}' for k in range(5)],
               'coordinate_maps_on_schreier_basis': maps,
               'all300_pair_inequivalence_witnesses': witnesses,
               'peripheral_orders_in_central_product_rows': orders,
               'all_peripheral_base_conjugators': conjugators,
               'allowed_peripheral_products_by_row_rotation': products,
               'actual_finite_pro_five_example': beta,
               'scope': 'All evaluated maps are literal. Full generation follows from the certified simple-group subdirect argument; the pullback theorem is proved in D.27.'}
    HERE.joinpath('a_peripheral_coupled.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
