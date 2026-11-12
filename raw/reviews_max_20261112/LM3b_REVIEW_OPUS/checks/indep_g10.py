# Reviewer's end-to-end check of the mechanism of LM3b G.10 (Willwacher's characteristic-two reconstruction)
# on actual grt_1 solutions of weights 3, 5, 8 (rational candidates read from the return's fg_candidates.json,
# where V_n has dimension 1 and the pentagon rank is 0, so the candidate IS the solution).
# Elements of free associative algebras over F_2: Python sets of words (tuples); addition = symmetric difference.
import sys, json, itertools
sys.stdout.reconfigure(encoding='utf-8')
cand = json.load(open(sys.argv[1], encoding='utf-8'))

def add(*ps):
    s = set()
    for p in ps:
        s ^= set(p)
    return s
def mul(p, q):
    out = set()
    for u in p:
        for v in q:
            out ^= {u + v}
    return out
def br(p, q): return add(mul(p, q), mul(q, p))

def is_lyndon(w): return all(w < w[i:] for i in range(1, len(w)))
def expand_word(w, gens):
    if len(w) == 1:
        return gens[w[0]]
    for i in range(1, len(w)):
        if is_lyndon(w[i:]):
            return br(expand_word(w[:i], gens), expand_word(w[i:], gens))

def psi_bar(n):
    z = cand[str(n)]
    assert len(z['kernel']) == 1
    coeffs = z['kernel'][0]
    gens = {0: {('x',)}, 1: {('y',)}}
    out = set()
    for c, w in zip(coeffs, z['words']):
        if c % 2:
            out ^= expand_word(tuple(int(ch) for ch in w), gens)
    return out

WT = {'A': 2, 'B': 1, 'C': 2}
def lyndon_weighted(n):
    letters = ['A', 'B', 'C']  # order A<B<C
    res = []
    for k in range(1, n + 1):
        for w in itertools.product(range(3), repeat=k):
            if sum(WT[letters[i]] for i in w) == n and is_lyndon(w):
                res.append(tuple(letters[i] for i in w))
    return res

def lie_ABC(w):
    gens = {'A': {('A',)}, 'B': {('B',)}, 'C': {('C',)}}
    return expand_word(w, gens)

def iota(p):
    img = {'A': {('x', 'x')}, 'B': {('y',)}, 'C': {('x', 'y'), ('y', 'x')}}
    out = set()
    for w in p:
        m = {()}
        for l in w:
            m = mul(m, img[l])
        out ^= m
    return out

def solve_P(target, n):
    basis = lyndon_weighted(n)
    cols = [iota(lie_ABC(w)) for w in basis]
    # Gaussian elimination over F_2 on sets
    keys = sorted(set().union(*cols, target))
    kidx = {k: i for i, k in enumerate(keys)}
    vec = lambda s: sum(1 << kidx[k] for k in s)
    rows = []  # (vector, combination mask)
    piv = {}
    for j, c in enumerate(cols):
        v, m = vec(c), 1 << j
        while v:
            p = v.bit_length() - 1
            if p in piv:
                v ^= piv[p][0]; m ^= piv[p][1]
            else:
                piv[p] = (v, m); break
        else:
            raise AssertionError('iota not injective on this weight')
    v, m = vec(target), 0
    while v:
        p = v.bit_length() - 1
        if p not in piv:
            return None
        v ^= piv[p][0]; m ^= piv[p][1]
    P = set()
    for j, w in enumerate(basis):
        if (m >> j) & 1:
            P ^= lie_ABC(w)
    return P

# operators on F_2<A,B,C> : functions from sets of words to sets of words
def L(r):
    rr = r
    return lambda S: mul(rr, S)
def derivation(img):
    def D(S):
        out = set()
        for w in S:
            for i, l in enumerate(w):
                for v in img[l]:
                    out ^= {w[:i] + v + w[i + 1:]}
        return out
    return D
E = derivation({'A': {('A', 'B'), ('B', 'A')}, 'B': set(), 'C': {('A', 'B'), ('B', 'A')}})
T = derivation({'A': set(), 'B': {('C', 'B'), ('B', 'C')}, 'C': {('A', 'B', 'B'), ('B', 'B', 'A')}})
d = derivation({'B': {('B', 'B'), ('C',)}, 'C': {('B', 'C'), ('C', 'B')}})
dpar = derivation({'B': {('C',)}, 'C': set()})
def opsum(*ops): return lambda S: add(*[o(S) for o in ops])

def eval_assoc(p, ops, start):
    """p: set of words in letters; ops: letter -> operator; returns sum over words of op_{w1}(...op_{wk}(start))"""
    out = set()
    for w in p:
        v = set(start)
        for l in reversed(w):
            v = ops[l](v)
        out ^= v
    return out

for n in (3, 5, 8):
    psi = psi_bar(n)
    swap = {tuple('y' if c == 'x' else 'x' for c in w) for w in psi}
    antisym = (psi == swap)   # char 2: psi(x,y) = psi(y,x)
    P = solve_P(psi, n)
    assert P is not None
    f = {w for w in P if 'A' not in w}   # P(0,B,C) on the associative expansion
    one = {()}
    rhs = add(eval_assoc(f, {'B': E, 'C': opsum(L({('C',)}), T)}, one),
              eval_assoc(f, {'B': opsum(E, L({('B',)})), 'C': T}, one))
    g3 = (rhs == P)
    recon = eval_assoc(f, {'B': d, 'C': L({('C',)})}, one)
    fixed = (recon == f)
    # f lies in Lie(C,[B,C]): check by solving in brackets of C and D=[B,C] (weights 2,3)
    print(f'weight {n}: |psi words| = {len(psi)}, antisymmetric mod 2: {antisym}, P found, f nonzero: {bool(f)}, '
          f'(G.3) P = f(E,L_C+T)(1)+f(E+L_B,T)(1): {g3}, f = f(d,L_C)(1): {fixed}')

# Negative control: weight 7 and 9, where V_n contains non-pentagon vectors. The mod-2 reductions of the integral
# candidate basis vectors and their sums: count how many satisfy (G.3). A pentagon-free check would accept all.
for n in (7, 9):
    z = cand[str(n)]
    gens = {0: {('x',)}, 1: {('y',)}}
    vecs = []
    for coeffs in z['kernel']:
        p = set()
        for c, w in zip(coeffs, z['words']):
            if c % 2:
                p ^= expand_word(tuple(int(ch) for ch in w), gens)
        vecs.append(p)
    results = []
    for mask in range(1, 1 << len(vecs)):
        psi = set()
        for j, v in enumerate(vecs):
            if (mask >> j) & 1:
                psi ^= v
        if not psi:
            results.append((mask, 'zero')); continue
        P = solve_P(psi, n)
        f = {w for w in P if 'A' not in w}
        rhs = add(eval_assoc(f, {'B': E, 'C': opsum(L({('C',)}), T)}, {()}),
                  eval_assoc(f, {'B': opsum(E, L({('B',)})), 'C': T}, {()}))
        results.append((mask, rhs == P))
    print(f'weight {n}: dim V_n = {len(vecs)}; (G.3) holds for masks:', [m for m, ok in results if ok is True],
          'fails for:', [m for m, ok in results if ok is False])
