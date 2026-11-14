#!/usr/bin/env python3
"""Verify the D40 generation certificates using only the Python standard library."""
from pathlib import Path
from itertools import product, permutations
from math import factorial, prod
import hashlib, json, time

OUT = Path(__file__).resolve().parent
started = time.time()
C = json.loads((OUT/'d_cm_perfect_completion.json').read_text())

def eye(n):
    return tuple(int(i == j) for i in range(n) for j in range(n))

def mul(a,b,q,n):
    ans = []
    for i in range(n):
        for j in range(n):
            ans.append(sum(a[n*i+k]*b[n*k+j] for k in range(n)) % q)
    return tuple(ans)

def power(a,k,q,n):
    ans = eye(n)
    for _ in range(k):
        ans = mul(ans,a,q,n)
    return ans

def determinant(a,q,n):
    ans = 0
    for p in permutations(range(n)):
        inversions = sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        ans += (-1)**inversions*prod(a[n*i+p[i]] for i in range(n))
    return ans % q

def elementary(i,j,a,q,n):
    m = list(eye(n))
    m[n*i+j] = a % q
    return tuple(m)

verified = []
commutator_checks = 0
diagonal_checks = 0
for name, cover in C['central_covers'].items():
    q, n = cover['original']['q'], cover['original']['n']
    identity = eye(n)
    for i,j,k in permutations(range(n),3):
        for a,b in product(range(q),repeat=2):
            u, v = elementary(i,j,a,q,n), elementary(j,k,b,q,n)
            ui, vi = elementary(i,j,-a,q,n), elementary(j,k,-b,q,n)
            comm = mul(mul(mul(u,v,q,n),ui,q,n),vi,q,n)
            assert comm == elementary(i,k,a*b,q,n)
            commutator_checks += 1
    for i in range(n):
        for j in range(i+1,n):
            for a in range(1,q):
                wa = mul(mul(elementary(i,j,a,q,n),
                             elementary(j,i,-pow(a,-1,q),q,n),q,n),
                         elementary(i,j,a,q,n),q,n)
                wm = mul(mul(elementary(i,j,-1,q,n),
                             elementary(j,i,1,q,n),q,n),
                         elementary(i,j,-1,q,n),q,n)
                diagonal = list(identity)
                diagonal[n*i+i] = a
                diagonal[n*j+j] = pow(a,-1,q)
                assert mul(wa,wm,q,n) == tuple(diagonal)
                diagonal_checks += 1
    for variant in ['original','twisted']:
        cert = cover[variant]
        s,r = tuple(cert['s']),tuple(cert['r'])
        assert determinant(s,q,n) == determinant(r,q,n) == 1
        assert power(s,2,q,n) == power(r,3,q,n) == identity
        r2 = mul(r,r,q,n)
        matrices = []
        for word, stored in zip(cert['strong_generator_words'],
                                cert['strong_generator_matrices']):
            a = identity
            for letter in word:
                assert letter in (0,1,2)
                a = mul(a,(s,r,r2)[letter],q,n)
            assert a == tuple(stored)
            matrices.append(a)
        vectors = [v for v in product(range(q),repeat=n) if any(v)]
        index = {v:i for i,v in enumerate(vectors)}
        perms = []
        for a in matrices:
            p = []
            for v in vectors:
                p.append(index[tuple(sum(a[n*i+j]*v[j] for j in range(n)) % q
                                     for i in range(n))])
            assert len(set(p)) == len(vectors)
            perms.append(p)
        base = cert['base']
        lengths = []
        for level,b in enumerate(base):
            generators = [g for g in perms
                          if all(g[c] == c for c in base[:level])]
            visited = {b}
            queue = [b]
            for point in queue:
                for g in generators:
                    nxt = g[point]
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            assert queue == cert['orbits'][level]
            lengths.append(len(queue))
        goal = q**(n*(n-1)//2)*prod(q**i-1 for i in range(2,n+1))
        assert lengths == cert['orbit_lengths']
        assert prod(lengths) == goal == cert['order']
        verified.append({'group':name,'variant':variant,
                         'orbit_lengths':lengths,'order':goal,
                         'word_count':len(matrices),
                         'total_word_length':sum(map(len,cert['strong_generator_words']))})
    z = tuple(cover['central_element'])
    assert power(z,cover['central_order'],q,n) == identity and z != identity
    s0,r0 = tuple(cover['original']['s']),tuple(cover['original']['r'])
    s1,r1 = tuple(cover['twisted']['s']),tuple(cover['twisted']['r'])
    if cover['central_order'] == 2:
        assert s1 == mul(z,s0,q,n) and r1 == r0
    else:
        assert r1 == mul(z,r0,q,n) and s1 == s0

permutation_checks = []
for name, cert in C['summary']['symmetric_quotients'].items():
    s,r = bytes(cert['s']),bytes(cert['r'])
    n = len(s)
    identity = bytes(range(n))
    def compose(a,b):
        return bytes(a[i] for i in b)
    assert compose(s,s) == compose(compose(r,r),r) == identity
    seen = {identity}
    queue = [identity]
    for a in queue:
        for b in (s,r):
            c = compose(a,b)
            if c not in seen:
                seen.add(c)
                queue.append(c)
    assert len(seen) == factorial(n) == cert['order']
    digest = hashlib.sha256(b''.join(queue)).hexdigest()
    assert digest == cert['enumeration_sha256']
    permutation_checks.append({'group':name,'enumerated_order':len(seen),
                               'sha256':digest})
    del seen, queue

answer = {
    'status':'PASS',
    'uses_sympy':False,
    'matrix_word_and_orbit_certificates':verified,
    'elementary_perfectness_commutator_checks':commutator_checks,
    'elementary_diagonal_identity_checks':diagonal_checks,
    'independent_complete_permutation_enumerations':permutation_checks,
    'scope':'Every finite generation claim in D40 is independently checked from explicit words and orbit lower bounds or full enumeration. The infinite-source comparisons are proved in the accompanying theorem.',
    'elapsed_seconds':round(time.time()-started,3),
}
(OUT/'d_cm_perfect_verify.json').write_text(json.dumps(answer,indent=2)+'\n')
print(json.dumps(answer,indent=2),flush=True)
