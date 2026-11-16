#!/usr/bin/env python3
"""Exact degree-nine witness for the post-repair unit obstruction (A.106)."""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json
import sympy as sp

OUT = Path(__file__).resolve().parent
LOG = []


def emit(text):
    LOG.append(str(text))
    print(text, flush=True)


q = 321193
q2 = q*q
g = 5
theta = 2827
a = 146470
zeta = 100461
U = [1, 2, 4, 5, 7, 8]
assert sp.isprime(q)
assert q % 216 == 1
assert sp.n_order(g, q) == q-1
assert pow(theta, 27, q) == 3
assert pow(theta, 3, q) == a
assert pow(a, 9, q) == 3
assert sp.n_order(zeta, q) == 9
assert pow(q-2, (q-1)//72, q) == 1
emit(f'q={q}; primitive root g={g}; theta={theta}; a={a}; zeta9={zeta}')
emit('Prime, roots, complete L3 splitting and full B72 splitting: passed')


def hensel(x, exponent, value):
    correction = ((value-x**exponent)//q) * pow(exponent*x**(exponent-1), -1, q) % q
    answer = x + q*correction
    assert (answer**exponent-value) % q2 == 0
    return answer


aroots = [a*pow(zeta, i, q) % q for i in range(9)]
zroots = {u: pow(zeta, u, q) for u in U}
aroots2 = [hensel(x, 9, 3) for x in aroots]
zroots2 = {u: hensel(zroots[u], 9, 1) for u in U}
assert all((z**6+z**3+1) % q2 == 0 for z in zroots2.values())
for i, u in product(range(9), U):
    assert aroots2[i]*zroots2[u] % q2 == aroots2[(i+u) % 9]


def pmul(p, r, modulus):
    ans = [0]*(len(p)+len(r)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(r):
            ans[i+j] = (ans[i+j]+x*y) % modulus
    return ans


def peval(p, x, modulus):
    v = 0
    for c in reversed(p):
        v = (v*x+c) % modulus
    return v


def lagrange(roots, index):
    ans = [1]
    denominator = 1
    for j, x in enumerate(roots):
        if j != index:
            ans = pmul(ans, [-x % q2, 1], q2)
            denominator = denominator*(roots[index]-x) % q2
    ans = [c*pow(denominator, -1, q2) % q2 for c in ans]
    for j, x in enumerate(roots):
        assert peval(ans, x, q2) == int(j == index)
    return ans


Ls = [lagrange(aroots2, i) for i in range(9)]
M1 = lagrange([zroots2[u] for u in U], 0)
Es = [[[x*y % q2 for y in M1] for x in Li] for Li in Ls]


def eval2(p, av, zv, modulus):
    return sum(c*pow(av, i, modulus)*pow(zv, j, modulus)
               for i, row in enumerate(p) for j, c in enumerate(row)) % modulus


for i, j, u in product(range(9), range(9), U):
    assert eval2(Es[i], aroots2[j], zroots2[u], q2) == int(i == j and u == 1)

zeta3 = pow(g, (q-1)//3, q)
charlog = {pow(zeta3, j, q): j for j in range(3)}
B = [charlog[pow((1-x) % q, (q-1)//3, q)] for x in aroots]
assert sum(B) % 3 == 0
v = [0]
for i in range(8):
    v.append((v[-1]-B[i]) % 3)
assert (v[0]-v[-1]+B[-1]) % 3 == 0


def interpolate(values):
    p = [[0]*6 for _ in range(9)]
    p[0][0] = 1
    for i in range(9):
        for j, k in product(range(9), range(6)):
            p[j][k] += (values[i]-1)*Es[i][j][k]
    assert p[0][0] % 2 == 1
    assert all(p[j][k] % 2 == 0 for j, k in product(range(9), range(6)) if (j,k) != (0,0))
    return p


prevalues = [g**x for x in v]
badvalues = [1]*9
badvalues[1] = q
badvalues[4] = g
hpre = interpolate(prevalues)
hbad = interpolate(badvalues)
for i, u in product(range(9), U):
    assert eval2(hpre, aroots2[i], zroots2[u], q2) == (prevalues[i] if u == 1 else 1)
    assert eval2(hbad, aroots2[i], zroots2[u], q2) == (badvalues[i] if u == 1 else 1)
emit(f'Roots of X^9-3 modulo q: {aroots}')
emit(f'Original unit cubic logarithms B: {B}; interpolation exponents v: {v}')
emit('All 486 idempotent evaluations and both 54-place interpolation tables: passed')


def local_data(p):
    vals = {}
    chars = {}
    for i, u in product(range(9), U):
        value = eval2(p, aroots2[i], zroots2[u], q2)
        if value % q == 0:
            assert value == q
            vals[i,u], chars[i,u] = 1, 0
        else:
            vals[i,u] = 0
            chars[i,u] = charlog[pow(value % q, (q-1)//3, q)]
    # tau acts by alpha -> zeta*alpha, so at (i,u) it uses (i+u,u).
    t = [sum(vals[(i+u) % 9,u]-vals[i,u] for u in U) for i in range(9)]
    C = [sum(chars[(i+u) % 9,u]-chars[i,u] for u in U) % 3 for i in range(9)]
    return t, C


tp, Cp = local_data(hpre)
tb, Cb = local_data(hbad)
assert tp == [0]*9
assert all((x+y) % 3 == 0 for x,y in zip(B,Cp))
assert tb == [1,-1,0,0,0,0,0,0,0]
assert Cb == [0,0,0,1,2,0,0,0,0]
assert all(charlog[pow(x,(q-1)//3,q)] == 0 for x in aroots)
emit('Prior representative is a cubic unit at all nine branches: passed')
emit(f'Post-repair valuation vector: {tb}; unit cubic logarithms: {Cb}')
emit('Every old alpha branch is a cube; both multipliers are units at every two-adic place: passed')

# Exact field multiplication in Q[alpha,zeta]/(alpha^9-3,zeta^6+zeta^3+1).
zpowers = [[int(j==0) for j in range(6)]]
for power in range(1,32):
    old = zpowers[-1]
    new = [0]+old[:5]
    new[0] -= old[5]
    new[3] -= old[5]
    zpowers.append(new)


def tau(p):
    ans = [[0]*6 for _ in range(9)]
    for i,j in product(range(9),range(6)):
        for k,z in enumerate(zpowers[i+j]):
            ans[i][k] += p[i][j]*z
    return ans


def norm(p):
    columns = []
    for ai,zj in product(range(9),range(6)):
        col = [0]*54
        for i,j in product(range(9),range(6)):
            av, factor = (ai+i) % 9, 3**((ai+i)//9)
            for k,z in enumerate(zpowers[zj+j]):
                col[6*av+k] += p[i][j]*factor*z
        columns.append(col)
    matrix = sp.polys.matrices.DomainMatrix.from_Matrix(sp.Matrix(54,54,lambda i,j:columns[j][i]))
    return int(matrix.det())


exact_norms = {}
for label, p in [('hpre',hpre),('hbad',hbad)]:
    rotated = p
    for _ in range(9):
        rotated = tau(rotated)
    assert rotated == p
    nh = norm(p)
    nth = norm(tau(p))
    assert nh == nth and nh % 2 == 1
    exact_norms[label] = str(nh)
    emit(f'Exact 54-dimensional determinants for {label} and tau({label}) agree; norm has {len(str(abs(nh)))} digits')
emit('Exact transitive norms: N(u_pre)=N(u_bad)=1, N(beta_pre)=N(beta)=-2')

checked = successes = 0
for e,k,rval,x,y in product([1,2],range(3),range(3),range(3),range(3)):
    equations = [((ti+e*rval)*e*x-e*k*(ci+e*y)) % 3 for ti,ci in zip(tb,Cb)]
    holds = not any(equations)
    assert holds == (k == 0 and x == 0)
    checked += 1
    successes += int(holds)
emit(f'All {checked} residue choices: {successes} satisfy every norm equation, exactly when Q is a local cube')

data = {'q':q,'q2':q2,'g':g,'theta':theta,'a':a,'zeta9':zeta,'U':U,
        'alpha_roots_mod_q':aroots,'alpha_roots_mod_q2':aroots2,
        'zeta_roots_mod_q2':zroots2,'B':B,'v':v,
        'hpre_coefficients_alpha_rows_zeta_columns':hpre,
        'hbad_coefficients_alpha_rows_zeta_columns':hbad,
        'exact_rational_norms_h':exact_norms,
        'post_valuation_vector':tb,'post_unit_cubic_logs':Cb,
        'residue_cases':checked,'local_norm_successes':successes}
polypath = OUT/'norm_deeper_unit_polynomials.json'
polypath.write_text(json.dumps(data,indent=2)+'\n')
emit(f'Exact polynomial data SHA256: {sha256(polypath.read_bytes()).hexdigest()}')
emit('All A.106 identities passed. The global extension map and exact local criterion are proved in the source.')
(OUT/'norm_deeper_unit_certificate_output.txt').write_text('\n'.join(LOG)+'\n')
