#!/usr/bin/env python3
"""Check the genuine quaternion quotient image and its explicit Belyi model.

No review code is imported.  Q8 is represented by i^a j^b, 0<=a<4,
0<=b<2, with j^2=i^2 and ji=i^-1j.  The mathematical Galois realization
uses cyclotomic surjectivity modulo four; finite and symbolic identities
needed by that argument are checked here.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp


def mul(u, v):
    a, b = u % 4, u // 4
    c, d = v % 4, v // 4
    return (a + (-1)**b*c + 2*b*d) % 4 + 4*((b+d) % 2)


def power(u, n):
    ans = 0
    for _ in range(n):
        ans = mul(ans, u)
    return ans


def inverse(u):
    return next(v for v in range(8) if mul(u, v) == mul(v, u) == 0)


def conjugate(u, v):
    return mul(mul(u, v), inverse(u))


def generated(u, v):
    ans = {0}
    while True:
        nxt = ans | {mul(a, b) for a in ans for b in (u, v)}
        if nxt == ans:
            return ans
        ans = nxt


assert all(mul(mul(a, b), c) == mul(a, mul(b, c))
           for a, b, c in product(range(8), repeat=3))
center = [a for a in range(8) if all(mul(a,b) == mul(b,a) for b in range(8))]
commutators = sorted({mul(mul(mul(a,b),inverse(a)),inverse(b))
                     for a,b in product(range(8),repeat=2)})
assert center == commutators == [0, 2]

pairs = [(u,v) for u,v in product(range(8),repeat=2) if len(generated(u,v))==8]
automorphisms = []
for u,v in pairs:
    phi = [mul(power(u,a),power(v,b)) for b in range(2) for a in range(4)]
    assert len(set(phi)) == 8
    assert all(phi[mul(a,b)] == mul(phi[a],phi[b]) for a,b in product(range(8),repeat=2))
    automorphisms.append(phi)
assert len(pairs) == len({tuple(phi) for phi in automorphisms}) == 24

i, j, k = 1, 4, 5
gt_maps = {}
for lam in [1,3]:
    for f in commutators:
        u, v = power(i,lam), conjugate(inverse(f),power(j,lam))
        assert (u,v) == (power(i,lam),power(j,lam))
        phi = [mul(power(u,a),power(v,b)) for b in range(2) for a in range(4)]
        assert phi in automorphisms
        gt_maps[lam] = phi
assert gt_maps[1] == list(range(8))
assert gt_maps[3] == [conjugate(k,q) for q in range(8)]
assert gt_maps[1] != gt_maps[3]

x,y = sp.symbols('x y')
I = sp.I
curve = x**5-x
t = (x*x+1)**2/(4*x*x)
ident = (x,y)
a = (-x,I*y)
b = (1/x,I*y/x**3)
h = (x,-y)


def compose(f,g):
    return tuple(sp.cancel(z.subs({x:g[0],y:g[1]},simultaneous=True)) for z in f)


def equal(f,g):
    return all(sp.cancel(u-v)==0 for u,v in zip(f,g))


def curve_preserved(f):
    return sp.cancel((f[1]**2-(f[0]**5-f[0])).subs(y**2,curve)) == 0


assert curve_preserved(a) and curve_preserved(b)
assert equal(compose(a,a),h) and equal(compose(b,b),h)
assert equal(compose(a,b),compose(h,compose(b,a)))
assert equal(compose(h,h),ident)
deck=[]
for bb in range(2):
    for aa in range(4):
        f=ident
        for _ in range(aa):f=compose(a,f)
        if bb:f=compose(f,b)
        deck.append(f)
assert all(not equal(deck[u],deck[v]) for u in range(8) for v in range(u))
assert all(equal(compose(deck[u],deck[v]),deck[mul(u,v)]) for u,v in product(range(8),repeat=2))
assert all(curve_preserved(f) for f in deck)
assert all(sp.cancel(t.subs(x,f[0])-t)==0 for f in deck)
assert sp.cancel(t-1-(x*x-1)**2/(4*x*x))==0
assert sp.gcd(curve,sp.diff(curve,x))==1
# Coefficient conjugation sends both order-four generators to their inverses.
conj_a=tuple(sp.expand(z).subs(I,-I) for z in a)
conj_b=tuple(sp.expand(z).subs(I,-I) for z in b)
assert equal(conj_a,deck[inverse(i)])
assert equal(conj_b,deck[inverse(j)])
fixed_deck=[q for q,f in enumerate(deck)
            if equal(tuple(sp.expand(z).subs(I,-I) for z in f),f)]
assert set(fixed_deck)=={power(k,n) for n in range(4)}
assert len(fixed_deck)==4

result={
    'group_order':8,
    'associativity_triples_checked':512,
    'center':center,
    'commutator_subgroup':commutators,
    'generating_pairs':pairs,
    'automorphism_count':24,
    'automorphisms':automorphisms,
    'single_automorphism_orbit_on_generating_pairs':True,
    'characteristic_quotient_reason':'Every epimorphism to Q8 has the same kernel, since every generating pair is an automorphic image of (i,j).',
    'gt_images_by_multiplier_mod4':gt_maps,
    'gt_image_order':2,
    'outer_image_order':1,
    'galois_realization_reason':'Cyclotomic character modulo four is onto; the GT restriction depends only on that residue.',
    'curve':'y^2=x^5-x',
    'belyi_map':'t=(x^2+1)^2/(4*x^2)',
    'cover_degree':8,
    'genus':2,
    'branch_values':['0','1','infinity'],
    'ramification_profiles':[[4,4],[4,4],[4,4]],
    'deck_transformations':[[sp.sstr(z) for z in f] for f in deck],
    'deck_composition_identities_checked':64,
    'coefficient_conjugation_inverts_both_generators':True,
    'geometric_deck_group_order':8,
    'deck_marking_field':'Q(i)',
    'rational_deck_group_order':4,
    'rational_deck_group_indices':fixed_deck,
    'scope':'One explicit genuine nonabelian GT quotient image. No enumeration of all nonabelian quotients is asserted.'
}
path=Path(__file__).with_name('quaternion_shadow_results.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['group_order','automorphism_count',
    'single_automorphism_orbit_on_generating_pairs','gt_image_order','outer_image_order',
    'cover_degree','genus','ramification_profiles','deck_composition_identities_checked']},indent=2))
print('All quaternion group, GT restriction, and symbolic Belyi-cover checks passed.')
