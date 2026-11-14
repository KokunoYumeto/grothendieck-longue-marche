#!/usr/bin/env python3
"""Independent exhaustive checks of the actual E121 finite maps.

The matrices are entered from the separately derived full field diagram.
This program imports neither the author's checker nor its output.  The
arithmetic realization of its coordinates is audited separately.
"""
from collections import Counter
from itertools import product
from math import comb
from pathlib import Path
import json


class FiniteAbelian:
    def __init__(self, name, moduli):
        self.name, self.moduli = name, tuple(moduli)
        self.elements = tuple(product(*(range(m) for m in self.moduli)))
        self.zero = tuple(0 for _ in self.moduli)

    def reduce(self, x):
        return tuple(a % m for a, m in zip(x, self.moduli))

    def add(self, x, y):
        return self.reduce(tuple(a + b for a, b in zip(x, y)))

    def scale(self, n, x):
        return self.reduce(tuple(n * a for a in x))


def hom(source, target, matrix):
    assert len(matrix) == len(target.moduli)
    assert all(len(row) == len(source.moduli) for row in matrix)
    for row, n in zip(matrix, target.moduli):
        assert all(a * m % n == 0 for a, m in zip(row, source.moduli))
    return lambda x: target.reduce(tuple(sum(a * b for a, b in zip(row, x))
                                         for row in matrix))


def subgroup(group, generators):
    known, queue = {group.zero}, [group.zero]
    while queue:
        x = queue.pop()
        for y in generators:
            z = group.add(x, y)
            if z not in known:
                known.add(z)
                queue.append(z)
    return known


def log3(n):
    k = 0
    while n > 1:
        assert n % 3 == 0
        n //= 3
        k += 1
    return k


def group_type(group, elements=None, denominator=None):
    elements = group.elements if elements is None else tuple(elements)
    denominator = {group.zero} if denominator is None else denominator
    assert group.zero in elements and group.zero in denominator
    exponent = max(log3(m) for m in group.moduli)
    killed = [sum(group.scale(3 ** k, x) in denominator for x in elements)
              // len(denominator) for k in range(exponent + 1)]
    assert killed[0] == 1
    ranks = [log3(killed[k]) - log3(killed[k - 1])
             for k in range(1, len(killed))] + [0]
    assert all(ranks[i] >= ranks[i + 1] for i in range(len(ranks) - 1))
    return [3 ** k for k in range(exponent, 0, -1)
            for _ in range(ranks[k - 1] - ranks[k])]


B = FiniteAbelian('A(B2)', [9, 3, 3, 3])
L = FiniteAbelian('A(L2)', [9, 9])
B1 = FiniteAbelian('A(B1)', [3, 3])
L1 = FiniteAbelian('A(L1)', [3, 3])
QL = FiniteAbelian('Q(L2)', [9, 3])
Bg = FiniteAbelian('A(B2)_g', [9, 3, 3])
Bh = FiniteAbelian('A(B2)_h', [9, 3])
C3 = FiniteAbelian('C3', [3])

matrices = {
    'g': [[1,0,0,0],[2,0,1,2],[2,2,2,2],[0,0,0,1]],
    'h': [[4,3,6,0],[2,2,2,0],[0,1,0,0],[1,0,0,1]],
    'sigma_L': [[1,3],[0,1]],
    'Nh': [[1,0,6,6],[0,3,6,3]],
    'jh': [[0,3],[2,0],[2,0],[0,1]],
    'NB': [[0,0,0,2],[1,0,0,2]],
    'jB': [[6,3],[0,0],[0,0],[0,0]],
    'NL': [[0,2],[2,0]],
    'jL': [[0,6],[6,0]],
    'Nh1': [[0,0],[1,2]],
    'jh1': [[1,0],[1,0]],
    'pL': [[6,1],[2,1]],
    'pi_g': [[5,3,6,6],[1,1,2,1],[0,0,0,2]],
    'pi_h': [[1,0,6,6],[0,1,2,1]],
    'Nh_projected': [[6,3,6,3],[2,0,0,0]],
    'jh_projected': [[3,0],[2,1],[2,1],[1,0]],
    'NL_projected': [[2,0],[2,1]],
    'jL_projected': [[6,0],[0,0]],
    'Artin_horizontal': [[0,1]],
    'Artin_compositum': [[1,1,2,1]],
}
g, h = (hom(B, B, matrices[n]) for n in ['g', 'h'])
sigma = hom(L, L, matrices['sigma_L'])
Nh, jh = hom(B, L, matrices['Nh']), hom(L, B, matrices['jh'])
NB, jB = hom(B, B1, matrices['NB']), hom(B1, B, matrices['jB'])
NL, jL = hom(L, L1, matrices['NL']), hom(L1, L, matrices['jL'])
Nh1, jh1 = hom(B1, L1, matrices['Nh1']), hom(L1, B1, matrices['jh1'])
pL = hom(L, QL, matrices['pL'])
pi_g, pi_h = hom(B, Bg, matrices['pi_g']), hom(B, Bh, matrices['pi_h'])
Nhq = hom(B, QL, matrices['Nh_projected'])
jhq = hom(QL, B, matrices['jh_projected'])
NLq = hom(QL, L1, matrices['NL_projected'])
jLq = hom(L1, QL, matrices['jL_projected'])
art = hom(L, C3, matrices['Artin_horizontal'])
psi = hom(B, C3, matrices['Artin_compositum'])

dif = lambda group, x, y: group.add(x, group.scale(-1, y))
gminus = {dif(B, g(x), x) for x in B.elements}
hminus = {dif(B, h(x), x) for x in B.elements}
sigminus = {dif(L, sigma(x), x) for x in L.elements}
assert gminus == {(0,0,0,0),(0,1,1,0),(0,2,2,0)}
assert len(hminus) == 9
assert sigminus == {(0,0),(3,0),(6,0)}
assert group_type(B, denominator=gminus) == [9,3,3]
assert group_type(B, denominator=hminus) == [9,3]
joint = subgroup(B, gminus | hminus)
assert group_type(B, denominator=joint) == [3,3]

checks = Counter()
for x in B.elements:
    assert g(g(g(x))) == x and h(h(h(x))) == x
    assert g(h(x)) == h(g(x))
    assert dif(B, g(dif(B, g(x), x)), dif(B, g(x), x)) == B.zero
    assert jh(Nh(x)) == B.add(x, B.add(h(x), h(h(x))))
    assert jB(NB(x)) == B.scale(3, x)
    assert Nh(h(x)) == Nh(x) and sigma(Nh(x)) == Nh(x)
    assert pL(Nh(x)) == Nhq(x)
    assert NL(Nh(x)) == Nh1(NB(x))
    assert psi(g(x)) == psi(x) == psi(h(x))
    checks['B2_elements'] += 1
for x in L.elements:
    assert sigma(sigma(sigma(x))) == x
    assert L.add(x, L.add(sigma(x), sigma(sigma(x)))) == L.scale(3, x)
    assert Nh(jh(x)) == L.scale(3, x)
    assert jL(NL(x)) == L.scale(3, x)
    assert h(jh(x)) == jh(x) == jh(sigma(x))
    assert jh(x) == jhq(pL(x))
    assert NL(x) == NLq(pL(x))
    assert NB(jh(x)) == jh1(NL(x))
    checks['L2_elements'] += 1
for x in B1.elements:
    assert NB(jB(x)) == B1.zero
    assert Nh(jB(x)) == jL(Nh1(x))
    checks['B1_elements'] += 1
for x in L1.elements:
    assert NL(jL(x)) == L1.zero
    assert jh(jL(x)) == jB(jh1(x))
    assert pL(jL(x)) == jLq(x)
    checks['L1_elements'] += 1

maps = [('Nh',B,L,Nh),('jh',L,B,jh),('NB',B,B1,NB),('jB',B1,B,jB),
        ('NL',L,L1,NL),('jL',L1,L,jL),('pL',L,QL,pL),
        ('pi_g',B,Bg,pi_g),('pi_h',B,Bh,pi_h)]
statistics = {}
for name, source, target, f in maps:
    fibres = Counter(f(x) for x in source.elements)
    kernel = [x for x in source.elements if f(x) == target.zero]
    assert set(fibres.values()) == {len(kernel)}
    statistics[name] = {'source_order':len(source.elements),
                        'image_order':len(fibres),'kernel_order':len(kernel),
                        'image_type':group_type(target, fibres),
                        'kernel_type':group_type(source, kernel)}
assert statistics['Nh']['kernel_type'] == [3,3]
assert statistics['jh']['kernel_type'] == [3,3]
assert statistics['NB']['kernel_type'] == [3,3,3]
assert statistics['NL']['kernel_type'] == [3,3]
assert statistics['jB']['kernel_type'] == [3]
assert statistics['jL']['kernel_type'] == []
assert {x for x in B.elements if Nh(x) == L.zero} == hminus
assert {x for x in B.elements if pi_g(x) == Bg.zero} == gminus
assert {x for x in B.elements if pi_h(x) == Bh.zero} == hminus
assert {x for x in L.elements if pL(x) == QL.zero} == sigminus
assert {Nh(x) for x in B.elements} == {x for x in L.elements if art(x) == (0,)}
assert {x for x in B1.elements if jB(x) == B.zero} == {(0,0),(1,1),(2,2)}

# Positive connecting class: its nonzero class in B_h maps to sigma(a)-a.
delta = (3,0,0,0)
assert delta not in hminus
assert pi_h(delta) == (3,0)
assert Nh(delta) == dif(L, sigma((0,1)), (0,1)) == (3,0)
assert Nh((0,1,0,0)) == (0,3)
for k in range(3):
    shear = hom(L, L, [[1,3*k],[0,1]])
    for x in L.elements:
        assert pL(shear(x)) == pL(x)
        assert jh(shear(x)) == jh(x) and NL(shear(x)) == NL(x)
        assert shear(sigma(x)) == sigma(shear(x))
    assert all(shear(Nh(x)) == Nh(x) for x in B.elements)
    assert all(shear(jL(x)) == jL(x) for x in L1.elements)

# Invariant ideal quotient coordinates for all three actual unit defects.
fixed_h = {x for x in B.elements if h(x) == x}
fixed_sigma = {x for x in L.elements if sigma(x) == x}
jBimage, jLimage, jhimage = ({f(x) for x in source.elements}
                           for source, f in [(B1,jB),(L1,jL),(L,jh)])
assert group_type(B, denominator=jBimage) == [3,3,3,3]
assert group_type(L, fixed_sigma, jLimage) == [3]
assert group_type(B, fixed_h, jhimage) == [3]
assert fixed_h == {(3*r,t,t,s) for r,t,s in product(range(3),repeat=3)}
assert {x for x in fixed_h if (x[0]//3-x[3])%3 == 0} == jhimage
assert {x for x in fixed_sigma if x[0]%3 == 0} == jLimage

# The actual degree-81 group of the compositum over Q(zeta_3).
field_group = set(product(range(9), repeat=2))
mul = lambda x,y: ((x[0]+pow(4,x[1],9)*y[0])%9,(x[1]+y[1])%9)
def generated(gens):
    known, queue = {(0,0)}, [(0,0)]
    while queue:
        x = queue.pop()
        for y in gens:
            z = mul(x,y)
            if z not in known:
                known.add(z); queue.append(z)
    return known
HB2 = generated([(6,3)])
Hconj = generated([(3,3)])
HB1 = generated(list(HB2 | Hconj))
assert len(HB2) == len(Hconj) == 3 and HB2 & Hconj == {(0,0)}
assert HB1 == {(3*r,3*s) for r,s in product(range(3),repeat=2)}
assert generated([(1,0),(0,1)]) == field_group
overF = {(a,3*b) for a,b in product(range(9),range(3))}
assert len(overF) == 27
assert {(a,b) for a,b in overF if (a+b)%9 == 0} == HB2
assert [(b//3)%3 for a,b in sorted(HB2)] == [0,2,1]
assert mul(mul((8,1),(8,1)),(8,1)) == (6,3)

# Coefficients in T^9=-sum_{1<=i<9} binom(9,i)T^i.
nilpotence_coefficients = [-comb(9,i) for i in range(1,9)]
assert all(c%3 == 0 for c in nilpotence_coefficients)
assert [comb(3,i) for i in range(1,4)] == [3,3,1]

result = {
    'status':'PASS_INDEPENDENT_FULL_FINITE_MAPS',
    'scope':'Exhaustive finite maps and defining polynomial identities; arithmetic realization and full proof audited separately.',
    'matrices':matrices,'map_statistics':statistics,'element_checks':dict(checks),
    'connecting_class':{'in_B_coordinates':delta,'in_B_h':pi_h(delta),
                        'image_in_L':Nh(delta)},
    'unit_field_norm_defect_types':{'B2/B1':[3,3,3,3],
                                  'L2/L1':[3],'B2/L2':[3]},
    'normal_closure_fixed_subgroups':{'B2':sorted(HB2),
                                    'conjugate_B2':sorted(Hconj),
                                    'B1':sorted(HB1)},
    'nilpotence_relation_coefficients':nilpotence_coefficients,
    'general_nilpotence_bound':'For a+b=9e, a+floor(b/9)=floor((9a+b)/9)>=e; hence (3,T)^(9e) annihilates A with 3^e A=0.'
}
encoded = json.dumps(result,indent=2,sort_keys=True)+'\n'
Path(__file__).with_suffix('.json').write_text(encoded)
print(encoded,end='')
