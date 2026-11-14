#!/usr/bin/env python3
"""Literal genus-one sewing word, its braid carries and folded/affine images.

This is an exploratory E.3 comparison.  The sewing identity uses the extra
Nakamura--Schneps relation IV; it is not imposed as a full-GT axiom here.
Inputs are the immutable literal E.1 source words, not just their CM labels.
All written files have this program's new prefix.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib
import json

HERE = Path(__file__).resolve().parent
INPUT = HERE / 'bc_cm_literal_words.json'


def red(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def inverse_word(w):
    return tuple(-x for x in reversed(w))


def substitute(w, images):
    return red(t for x in w for t in
               (images[x-1] if x > 0 else inverse_word(images[-x-1])))


def compose(a, b):
    return tuple(substitute(w, a) for w in b)


IDENTITY_AUTO = tuple((i,) for i in range(1, 5))
ARTIN = {}
for i in range(1, 4):
    a = list(IDENTITY_AUTO)
    a[i-1], a[i] = (i, i+1, -i), (i,)
    ARTIN[i] = tuple(a)
    a = list(IDENTITY_AUTO)
    a[i-1], a[i] = (i+1,), (-(i+1), i, i+1)
    ARTIN[-i] = tuple(a)


def artin_word(w):
    a = IDENTITY_AUTO
    for i in w:
        a = compose(a, ARTIN[i])
    return a


def braid_power(w, n):
    return w*n if n >= 0 else inverse_word(w)*(-n)


def braid_pure(i, j):
    h = tuple(range(j-1, i, -1))
    return h + (i, i) + inverse_word(h)


def comm_word(a, b):
    return a + b + inverse_word(a) + inverse_word(b)


def fp_reduce(w):
    """C2*Z normal form: letters are ('s',1) and ('x',nonzero integer)."""
    out = []
    for kind, n in w:
        if kind == 's':
            n %= 2
        if not n:
            continue
        if out and out[-1][0] == kind:
            n += out.pop()[1]
            if kind == 's':
                n %= 2
            if n:
                out.append((kind, n))
        else:
            out.append((kind, n))
    return out


def involution_conjugator(f):
    """Return the unique beta in F with s*f=beta*s*beta^-1.

    Here y=s*x*s.  Cyclic reduction supplies a conjugator in C2*Z;
    right multiplication by s chooses its unique representative in F.
    The final literal F-word identity is checked independently.
    """
    w = [('s', 1)]
    for x in f:
        if abs(x) == 1:
            w.append(('x', 1 if x > 0 else -1))
        else:
            w.extend([('s', 1), ('x', 1 if x > 0 else -1), ('s', 1)])
    w = fp_reduce(w)
    h = []
    while len(w) > 1:
        assert w[0][0] == w[-1][0]
        if w[0][0] == 's':
            assert w[0] == w[-1] == ('s', 1)
            h.append(w[0])
            w = w[1:-1]
        else:
            assert w[0][1] == -w[-1][1]
            h.append(w[0])
            w = w[1:-1]
    assert w == [('s', 1)]
    if sum(k == 's' for k, _ in h) % 2:
        h.append(('s', 1))
    state = 0
    beta = []
    for kind, n in h:
        if kind == 's':
            state ^= 1
        else:
            beta.extend(((1 if state == 0 else 2) * (1 if n > 0 else -1),) * abs(n))
    assert state == 0
    beta = red(beta)
    swap = lambda w: tuple((3-abs(x)) * (1 if x > 0 else -1) for x in w)
    assert red(swap(beta) + inverse_word(beta)) == red(f)
    exponents = [sum((1 if x > 0 else -1) for x in beta if abs(x) == i)
                 for i in (1, 2)]
    assert exponents[0] == exponents[1]
    return beta, -exponents[0]


class Affine:
    """Actual integral Ferrari homology map, reduced modulo m."""
    def __init__(self, m):
        self.m = m
        self.one = (1, 0, 0, 1, 0, 0)
        self.a = (1, 1, 0, 1, 0, 0)
        self.b = (1, 0, -1 % m, 1, 0, 0)
        self.c = (1, 1, 0, 1, 1, 0)

    def mul(self, a, b):
        return tuple(x % self.m for x in
                     (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                      a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3],
                      a[4]+a[0]*b[4]+a[1]*b[5],
                      a[5]+a[2]*b[4]+a[3]*b[5]))

    def inv(self, a):
        return tuple(x % self.m for x in
                     (a[3], -a[1], -a[2], a[0],
                      -a[3]*a[4]+a[1]*a[5], a[2]*a[4]-a[0]*a[5]))

    def power(self, a, n):
        if n < 0:
            return self.power(self.inv(a), -n)
        out = self.one
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out

    def prod(self, *terms):
        out = self.one
        for t in terms:
            out = self.mul(out, t)
        return out

    def eval(self, w, x, y):
        choices = {1: x, -1: self.inv(x), 2: y, -2: self.inv(y)}
        return self.prod(*(choices[k] for k in w))

    def sewing(self, f, rho):
        a, b, c = self.a, self.b, self.c
        e1 = self.power(self.prod(a, b, a), 4)
        e3 = self.power(self.prod(c, b, c), 4)
        e2 = self.prod(c, b, a, self.inv(b), self.inv(c))
        full = self.prod(self.eval(f, e3, a), self.power(c, -8*rho),
                         self.eval(f, self.power(b, 2), self.power(c, 2)),
                         self.eval(f, e2, e3), self.eval(f, e1, e2),
                         self.eval(f, self.power(a, 2), self.power(b, 2)),
                         self.power(a, 8*rho), self.eval(f, c, e1))
        v = self.eval(f, self.power(b, 2), self.power(c, 2))[4:]
        formula = (1, 0, 0, 1, (v[0]-8*rho*v[1]-8*rho) % self.m, v[1])
        assert full == formula
        return full, v


def main():
    literal = json.loads(INPUT.read_text())
    a, b, c = (1,), (2,), (3,)
    x12, x13, x23, x24, x34 = (braid_pure(i, j) for i, j in
                               ((1, 2), (1, 3), (2, 3), (2, 4), (3, 4)))
    x45, x51 = (a+b+a)*2, (c+b+c)*2
    e2 = c+b+a+inverse_word(b)+inverse_word(c)
    z4 = (a+b+c)*4
    comparisons = [
        ('Artin braid 12', a+b+a, b+a+b),
        ('Artin braid 23', b+c+b, c+b+c),
        ('Artin far commutation', a+c, c+a),
        ('e2 square', e2*2, braid_pure(1, 4)),
        ('pure equality 1', x23+x24, x51+inverse_word(x34)),
        ('pure equality 2', x13+x23, x45+inverse_word(x12)),
        ('pure equality 3', x12+x13, x45+inverse_word(x23)),
        ('pure equality 4', x24+x34, x51+inverse_word(x23)),
    ]
    A3_pairs = ((a, x51, x34), (e2, x51, x23),
                (e2, x45, x23), (c, x45, x12))
    for i, (u, v, z) in enumerate(A3_pairs):
        comparisons.append((f'A3 relation {i}', u+v+u+v, v+u+v+u))
        comparisons.append((f'A3 central carry {i}', (u+v)*2, z+z4))
    comparison_rows = []
    for label, left, right in comparisons:
        value = artin_word(left)
        assert value == artin_word(right), label
        comparison_rows.append({'identity': label, 'left_word': left,
                                'right_word': right, 'artin_images': value})

    models = {m: Affine(m) for m in (3, 4, 12)}
    for model in models.values():
        a, b, c = model.a, model.b, model.c
        assert model.prod(a, b, a) == model.prod(b, a, b)
        assert model.prod(b, c, b) == model.prod(c, b, c)
        assert model.prod(a, c) == model.prod(c, a)
        assert model.power(model.prod(a, b, a), 4) == model.one
        assert model.power(model.prod(c, b, c), 4) == model.one
        assert model.power(model.prod(a, b, c), 4) == model.one
        assert model.prod(c, b, a, model.inv(b), model.inv(c))[:4] == b[:4]
        # This actual translation simultaneously conjugates the two
        # linear folded arguments to (b^2,c^2), over every modulus.
        t = model.one[:4] + (0, -1 % model.m)
        assert model.prod(t, model.power(b, 2), model.inv(t)) == model.power(b, 2)
        assert model.prod(t, model.power(a, 2), model.inv(t)) == model.power(c, 2)

    # Complete structural check, not a check of selected CM words.
    # beta belongs to the actual SL2(F3) image of F.  Its two equal
    # integral exponents are -rho, so the character sending x,y to 1
    # has value -2rho=rho mod3.
    model = models[3]
    S = (0, 1, 2, 0, 0, 0)
    R = (0, 2, 1, 2, 0, 0)
    x, y = model.power(model.a, 2), model.power(model.b, 2)
    character = {model.one: 0}
    queue = [model.one]
    for beta in queue:
        for generator in (x, y):
            nxt = model.mul(beta, generator)
            value = (character[beta]+1) % 3
            if nxt not in character:
                character[nxt] = value
                queue.append(nxt)
            else:
                assert character[nxt] == value
    assert len(character) == 24
    expected_good = {model.mul(model.power(x, k), model.power(S, j))
                     for k in range(3) for j in range(4)}
    assert len(expected_good) == 12
    structural = []
    for beta, rho in sorted(character.items()):
        f = model.prod(S, beta, model.inv(S), model.inv(beta))
        cube = model.power(model.mul(model.inv(f), R), 3)
        good = cube == model.one
        assert good == (beta in expected_good)
        assert cube in (model.one, (2, 0, 0, 2, 0, 0))
        if good:
            assert f == (1, -8*rho % 3, -8*rho % 3, (1+64*rho*rho) % 3, 0, 0)
        structural.append({'beta': beta[:4], 'rho': rho,
                           'f_commutator': f[:4], 'r_image_cube': cube[:4],
                           'cubic_relation': good})
    model4 = models[4]
    xy4 = (model4.power(model4.a, 2), model4.power(model4.b, 2))
    four = {model4.prod(model4.power(xy4[0], i), model4.power(xy4[1], j))
            for i in range(2) for j in range(2)}
    assert len(four) == 4
    assert all(model4.mul(g, h) == model4.mul(h, g) for g, h in product(four, repeat=2))

    rows = []
    for index, rec in enumerate(literal['CM_words_in_F']):
        f = tuple(rec['word'])
        beta, rho = involution_conjugator(f)
        values = {}
        for m, model in models.items():
            value, v = model.sewing(f, rho)
            qf = model.eval(f, model.power(model.a, 2), model.power(model.b, 2))
            assert value == (1, 0, 0, 1, (-qf[1]-8*rho*qf[0]) % m, (qf[0]-1) % m)
            assert qf == (1, -8*rho % m, -8*rho % m, (1+64*rho*rho) % m, 0, 0)
            values[str(m)] = {'value': value, 'translation_before_twist': v}
        rows.append({'index': index, 'extra_CM_coset': rec['extra_CM_coset'],
                     'beta_word': beta, 'rho_NS_from_exact_beta': rho,
                     'affine_sewing': values})

    # A literal beta correction in N_B' keeps its G6 value and its
    # abelian rho_NS.  The initial search for a change in this sewing
    # projection found none; the complete structural check explains it.
    model = models[12]
    Ns = [tuple(w) for w in literal['N_B_basis_in_F']]
    seed = rows[0]
    beta0 = tuple(seed['beta_word'])
    swap = lambda w: tuple((3-abs(x)) * (1 if x > 0 else -1) for x in w)
    base = seed['affine_sewing']['12']['value']
    contrast = None
    for i in range(len(Ns)):
        for j in range(i+1, len(Ns)):
            n = comm_word(Ns[i], Ns[j])
            beta = red(n+beta0)
            f = red(swap(beta)+inverse_word(beta))
            bb, rho = involution_conjugator(f)
            assert bb == beta and rho == seed['rho_NS_from_exact_beta']
            value, _ = model.sewing(f, rho)
            if value != tuple(base):
                contrast = {'base_index': 0, 'N_basis_indices_zero_based': [i, j],
                            'n_word_in_F': n, 'beta_word_in_F': beta,
                            'f_word_in_F': f, 'rho_NS': rho,
                            'sewing_before': base, 'sewing_after': value}
                break
        if contrast is not None:
            break

    counts = {str(m): {str(extra): dict(Counter(
        str(tuple(row['affine_sewing'][str(m)]['value'][4:]))
        for row in rows if row['extra_CM_coset'] == extra))
                       for extra in (False, True)} for m in models}
    out = {
        'status': 'PASS_LITERAL_SEWING_COMPARISONS',
        'scope': 'Exact braid-word and Ferrari-homology computations. The extra '
                 'NS sewing identity is not assumed for full GT.',
        'input_file': INPUT.name, 'input_sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        'Artin_convention': 'sigma_i(z_i)=z_i*z_(i+1)*z_i^-1; sigma_i(z_(i+1))=z_i',
        'braid_identities': comparison_rows,
        'rho_convention': 'h=beta^-1; f=h(y,x)^-1*h(x,y); h_ab=(rho,rho)',
        'central_carries_in_four_IV_substitutions': [2, -2, 2, -2],
        'central_carry_sum': 0,
        'affine_target': '(Z/m)^2 semidirect SL2(Z/m), a=(U,0),b=(L,0),c=(U,e1)',
        'affine_sewing_formula': '(v_x-8*rho*v_y-8*rho,v_y), v=trans f(b^2,c^2)',
        'translation_conjugator': [0, -1],
        'matrix_sewing_formula': '(-q(f)[0,1]-8*rho*q(f)[0,0], q(f)[0,0]-1)',
        'folded_sewing_is_identity': True,
        'complete_mod3_frame_classification': structural,
        'good_mod3_frames': 12,
        'good_mod3_frame_set': 'x^k*S^j, 0<=k<3, 0<=j<4, with rho=k',
        'mod4_F_image': sorted(t[:4] for t in four),
        'universal_gentle_mod12_matrix': '[[1,-8rho],[-8rho,1+64rho^2]]',
        'initial_word_value_counts_by_CM_coset': counts,
        'same_G6_beta_correction_contrast': contrast,
        'records': rows,
    }
    HERE.joinpath('bc_genus_one_sewing.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ('records', 'braid_identities', 'same_G6_beta_correction_contrast',
                                   'complete_mod3_frame_classification')}, indent=2))
    print('same-G6 contrast:', None if contrast is None else
          {k: v for k, v in contrast.items() if 'word' not in k})
    print('PASS:', len(comparison_rows), 'literal braid identities;', len(rows), 'framed CM words.')


if __name__ == '__main__':
    main()
