#!/usr/bin/env python3
"""Exact finite certificates for B.52; standard library only.

Permutations are functions, and mul(a,b) means a after b.  The action
on the twelve vertices is the left action of A5 on A5/<d>.
This program checks finite data; the braid rotation invariant and the
mapping-class argument are proved in B_unrefined_product.tex.
"""
from collections import deque
from itertools import permutations
import json
from pathlib import Path


def mul(a, b):
    return tuple(a[i] for i in b)


def inv(a):
    out = [0] * len(a)
    for i, x in enumerate(a):
        out[x] = i
    return tuple(out)


def power(a, n):
    ans = tuple(range(len(a)))
    for _ in range(n):
        ans = mul(ans, a)
    return ans


def conjugate(a, b):
    return mul(mul(a, b), inv(a))


def even(a):
    return sum(a[i] > a[j] for i in range(5) for j in range(i + 1, 5)) % 2 == 0


def cycle(*seq):
    ans = list(range(5))
    for x, y in zip(seq, seq[1:] + seq[:1]):
        ans[x] = y
    return tuple(ans)


def generated(gens):
    identity = tuple(range(len(gens[0])))
    seen = {identity}
    todo = deque([identity])
    while todo:
        a = todo.popleft()
        for b in gens:
            c = mul(a, b)
            if c not in seen:
                seen.add(c)
                todo.append(c)
    return seen


E = tuple(range(5))
S = list(permutations(range(5)))
G = [a for a in S if even(a)]
Gset = set(G)
t1 = cycle(0, 1, 2)
t2 = mul(cycle(0, 1), cycle(2, 3))
d = cycle(0, 1, 2, 3, 4)
gens = [t1, t2, d]
T = generated(gens[:2])
D = {power(d, r) for r in range(5)}
assert len(T) == 12 and all(a[4] == 4 for a in T)
assert generated(gens) == Gset

# A finite three-generator presentation, read from the Cayley table.
words = {E: ()}
todo = deque([E])
while todo:
    a = todo.popleft()
    for i, b in enumerate(gens, 1):
        c = mul(a, b)
        if c not in words:
            words[c] = words[a] + (i,)
            todo.append(c)
assert len(words) == 60


def evaluate(word):
    out = E
    for i in word:
        out = mul(out, gens[i - 1] if i > 0 else inv(gens[-i - 1]))
    return out


relations = []
for a in G:
    assert evaluate(words[a]) == a
    for i, b in enumerate(gens, 1):
        c = mul(a, b)
        word = words[a] + (i,) + tuple(-j for j in reversed(words[c]))
        assert evaluate(word) == E
        relations.append(word)
assert len(relations) == 180

cosets = sorted({tuple(sorted(mul(a, b) for b in D)) for a in G})
assert len(cosets) == 12
coset_of = {a: i for i, coset in enumerate(cosets) for a in coset}
p = coset_of[E]
rho = {a: tuple(coset_of[mul(a, coset[0])] for coset in cosets) for a in G}
assert len(set(rho.values())) == 60
assert {rho[a][p] for a in G} == set(range(12))
assert {a for a in G if rho[a][p] == p} == D
normalizer_G_D = [a for a in G if {conjugate(a, b) for b in D} == D]
centralizer_S_d = [a for a in S if conjugate(a, d) == d]
assert len(normalizer_G_D) == 10
assert set(centralizer_S_d) == D

# A commuting permutation of a transitive G-set is determined by its
# value at p.  That value must be fixed by D.  These are all candidates.
fixed_D = [i for i in range(12) if all(rho[a][i] == i for a in D)]
centralizers = set()
for q in fixed_D:
    c = tuple(rho[coset[0]][q] for coset in cosets)
    assert len(set(c)) == 12
    assert all(mul(c, rho[a]) == mul(rho[a], c) for a in G)
    centralizers.add(c)
assert len(centralizers) == 2
assert len([c for c in centralizers if c[p] == p]) == 1

# For theta=c_s, every pair (theta,sigma) satisfies
# sigma rho(theta(a)) sigma^{-1} = rho(a).  Build both transporters
# using v with theta(D)=vDv^{-1}.
pairs = set()
for s in S:
    theta_D = {conjugate(s, b) for b in D}
    v_candidates = [v for v in G if {conjugate(v, b) for b in D} == theta_D]
    sigmas = set()
    for v in v_candidates:
        tau = tuple(coset_of[mul(conjugate(s, coset[0]), v)] for coset in cosets)
        sigma = inv(tau)
        assert all(mul(mul(sigma, rho[conjugate(s, a)]), inv(sigma)) == rho[a] for a in G)
        sigmas.add(sigma)
    assert len(sigmas) == 2
    for sigma in sigmas:
        pairs.add((s, sigma))
assert len(pairs) == 240

# Right action of the discrete normalizer A5 on the descriptions:
# (s,sigma).a = (a^{-1}s, sigma rho(a)).
unseen = set(pairs)
orbits = []
while unseen:
    s, sigma = min(unseen)
    orbit = {(mul(inv(a), s), mul(sigma, rho[a])) for a in G}
    assert len(orbit) == 60 and orbit <= pairs
    unseen -= orbit
    normalized = [(ss, sig) for ss, sig in orbit if sig[p] == p]
    assert len(normalized) == 5
    residues = set()
    for ss, sig in normalized:
        dd = conjugate(ss, d)
        r = next(r for r in range(1, 5) if power(d, r) == dd)
        residues.add(r)
    assert len(residues) == 1
    orbits.append({'size': 60, 'normalized_descriptions': 5, 'rotation_multiplier': residues.pop()})
assert sorted(o['rotation_multiplier'] for o in orbits) == [1, 2, 3, 4]

representatives = []
for r in range(1, 5):
    s = tuple((r * i) % 5 for i in range(5))
    assert conjugate(s, d) == power(d, r)
    sigma = tuple(coset_of[conjugate(inv(s), coset[0])] for coset in cosets)
    assert (s, sigma) in pairs and sigma[p] == p
    representatives.append({'r': r, 's_on_five_letters': s, 'sigma_on_cosets': sigma})

result = {
    'convention': 'zero-based permutations; mul(a,b)=a after b; left cosets gD',
    'a5_order': 60, 'T_order': 12, 'D_order': 5,
    'generators_on_five_letters': {'t1': t1, 't2': t2, 'd': d},
    'base_puncture': p,
    'generators_on_twelve_cosets': {name: rho[a] for name, a in zip(['t1', 't2', 'd'], gens)},
    'normalizer_A5_D_order': 10, 'centralizer_S12_A5_order': 2,
    'centralizer_S5_d_order': 5,
    'compatible_description_count': 240,
    'description_orbits': sorted(orbits, key=lambda o: o['rotation_multiplier']),
    'representatives': representatives,
    'canonical_words': [{'permutation': a, 'word': words[a]} for a in G],
    'relators': relations,
}
outdir = Path(__file__).resolve().parent
(outdir / 'marked_a5_certificate.json').write_text(json.dumps(result, indent=2) + '\n')
(outdir / 'marked_a5_relators.txt').write_text(
    'A5=<t1,t2,d | R>; signed 1,2,3 denote these generators and inverses.\n'
    + '\n'.join(' '.join(map(str, word)) for word in relations) + '\n')
print('A5 order: 60; T=<t1,t2> order: 12; D=<d> order: 5')
print('The three generators generate A5: PASS')
print('Cayley-table presentation: 60 canonical words; 180 verified relators')
print('Faithful transitive twelve-point coset action; base stabilizer D: PASS')
print('N_A5(D) order: 10; C_S12(A5) order: 2; C_S5(d) order: 5')
print('Compatible (automorphism, permutation) descriptions: 240')
print('Normalizer orbits: four, each of size 60')
print('Each orbit has five descriptions fixing the named puncture')
print('Their distinct rotation multipliers modulo 5: 1, 2, 3, 4')
print('Four explicit representatives and all relators saved in JSON/text')
print('ALL CHECKS PASS')
