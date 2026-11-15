"""Exact certificates for A.39, not a replacement for its all-weight proof.

Handle letters have weight one and the selected cusp t has weight two.
Modular ranks give rational rank lower bounds; explicit kernel vectors give
the matching lower bound on the rational kernel. No integral saturation is
inferred from these modular calculations.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
import sympy as s


def add(a, b, c=1):
    ans = dict(a)
    for w, v in b.items():
        ans[w] = ans.get(w, 0) + c*v
        if not ans[w]:
            del ans[w]
    return ans


def scale(a, c):
    return {w: c*v for w, v in a.items() if c*v}


def mul(a, b):
    ans = defaultdict(int)
    for u, x in a.items():
        for v, y in b.items():
            ans[u+v] += x*y
    return {w: c for w, c in ans.items() if c}


def bracket(a, b):
    return add(mul(a, b), mul(b, a), -1)


def deriv(poly, d):
    ans = defaultdict(int)
    for w, c in poly.items():
        for i, a in enumerate(w):
            for v, b in d[a].items():
                ans[w[:i]+v+w[i+1:]] += c*b
    return {w: c for w, c in ans.items() if c}


@lru_cache(None)
def lyndon(w):
    return all(w < w[i:]+w[:i] for i in range(1, len(w)))


@lru_cache(None)
def basis(w):
    if len(w) == 1:
        return {w: 1}
    for i in range(1, len(w)):
        if lyndon(w[i:]):
            return bracket(basis(w[:i]), basis(w[i:]))
    raise AssertionError(w)


@lru_cache(None)
def words_of_weight(n):
    if n == 0:
        return ((),)
    return tuple((i,)+w for i, wt in enumerate([1, 1, 1, 1, 2])
                 if wt <= n for w in words_of_weight(n-wt))


def rank_mod(cols, prime=1000003):
    pivots = {}
    for raw in cols:
        v = {k: c % prime for k, c in raw.items() if c % prime}
        while v:
            k = max(v)
            if k not in pivots:
                inv = pow(v[k], -1, prime)
                pivots[k] = {j: c*inv % prime for j, c in v.items()}
                break
            fac = v[k]
            for j, c in pivots[k].items():
                val = (v.get(j, 0)-fac*c) % prime
                if val:
                    v[j] = val
                elif j in v:
                    del v[j]
    return len(pivots)


# The uniform rational function has divisor 4(Q_+ - Q_-).
x, z, a, c, u = s.symbols('x z a c u')
d = a+2*c*c
aa = x**3-4*c*x
sextic = (x*x-4*c)*(x**4-4*c*x*x+d)
assert s.expand(sextic-aa*aa-d*(x*x-4*c)) == 0
assert s.rem((z-aa)**2*(z+aa)-d*(z-aa)*(x*x-4*c),
             z*z-sextic, z).expand() == 0
assert s.rem((z-aa)**2*(z+aa)**2-d*d*(x*x-4*c)**2,
             z*z-sextic, z).expand() == 0
# At the two infinities z=+/-x^3(1-4c/x^2+O(x^-4));
# z-A=d(x^2-4c)/(z+A), giving f~d^2/(4x^4) and 4x^4.
infinity_orders = {'Q_plus': 4, 'Q_minus': -4}
assert all(a0+2*c2 != 0 for a0, c2 in [(0, s.I), (0, -s.I),
                                                     (6, 1), (6, -1),
                                                     (-6, 1), (-6, -1)])

letters = [{(i,): 1} for i in range(5)]
omega1 = bracket(letters[0], letters[1])
omega2 = bracket(letters[2], letters[3])
omega = add(omega1, omega2)
t = letters[4]

# Finite verification of the triangular Omega-bimodule normal basis.
# Use lexicographic MINIMUM, so the leading word is (a1,b1)=(0,1).
@lru_cache(None)
def omega_power(n):
    return {(): 1} if n == 0 else mul(omega_power(n-1), omega)


normal_counts = []
for n in range(8):
    descriptors = set()
    for word in product(range(4), repeat=n):
        core = word
        left = right = 0
        while core[:2] == (0, 1):
            left += 1
            core = core[2:]
        if not core:
            descriptor = ('power', left)
            poly = omega_power(left)
        else:
            while core[-2:] == (0, 1):
                right += 1
                core = core[:-2]
            assert core and core[:2] != (0, 1) and core[-2:] != (0, 1)
            descriptor = ('core', left, core, right)
            poly = mul(mul(omega_power(left), {core: 1}), omega_power(right))
        assert descriptor not in descriptors
        descriptors.add(descriptor)
        assert min(poly) == word and poly[word] == 1
    assert len(descriptors) == 4**n
    normal_counts.append({'handle_degree': n, 'triangular_basis_size': 4**n})

rows = []
for geometric_case in ['smooth_genus_two', 'two_elliptic_components']:
    for lam in [0, 1, -2]:
        derivation = {4: {}}
        for i in range(4):
            inner = add(scale(omega, 2), t, lam)
            if geometric_case == 'two_elliptic_components':
                inner = add(inner, omega1 if i < 2 else omega2,
                            3 if i < 2 else 5)
            derivation[i] = bracket(inner, letters[i])
        assert deriv(t, derivation) == {}
        assert deriv(omega, derivation) == scale(bracket(t, omega), lam)
        if geometric_case == 'two_elliptic_components':
            for oi in [omega1, omega2]:
                assert deriv(oi, derivation) == bracket(add(scale(omega, 2), t, lam), oi)
        for wt in range(1, 6):
            domain = [w for w in words_of_weight(wt) if lyndon(w)]
            cols = [deriv(basis(w), derivation) for w in domain]
            rk = rank_mod(cols)
            expected = (2 if wt == 2 else 1 if wt == 4 else 0) if lam == 0 else int(wt == 2)
            actual = len(domain)-rk
            assert actual == expected, (geometric_case, lam, wt, actual, expected)
            if lam == 0:
                explicit = [t, omega] if wt == 2 else [bracket(t, omega)] if wt == 4 else []
            else:
                explicit = [t] if wt == 2 else []
            assert rank_mod(explicit) == expected
            assert all(not deriv(v, derivation) for v in explicit)
            row = dict(geometric_case=geometric_case, packet_scalar=lam,
                       weight=wt, domain_dimension=len(domain),
                       kernel_dimension=actual, expected=expected)
            rows.append(row)
            print(row, flush=True)

answer = {
    'uniform_cusp_function': '(z-(x^3-4cx))^2/(x^2-4c)',
    'cusp_function_orders': infinity_orders,
    'hyperelliptic_norm': '(a+2c^2)^2',
    'smooth_triangular_basis_certificate': normal_counts,
    'weighted_rank_checks': rows,
    'rank_prime': 1000003,
    'all_weight_proof': 'A.39 first-core prefix operators; count t or omega_i',
    'scope': 'finite checks support, but do not replace, the unbounded proof',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(answer, indent=2)+'\n')
print('PASS: cusp unit identities, triangular basis, and weighted kernels in both geometric cases.')
