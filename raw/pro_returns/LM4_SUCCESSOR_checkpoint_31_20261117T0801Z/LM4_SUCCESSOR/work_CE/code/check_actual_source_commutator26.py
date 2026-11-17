#!/usr/bin/env python3
"""Literal marking certificate for the actual six-source commutator.

Only free cancellation and the two cone squares are used in the raw
comparisons.  The four required commuting pairs are tied, with exact
conjugators and signs, to three actual regional node relators.  The
universal complete-cross-block calculation is done in F2 x F2, which is
the group presented by precisely those four cross commutators.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'work_CE/next_symmetric_nodes'
paths = [DATA / 'annular_neck_presentation23.json',
         DATA / 'annular_ordinary13_24.json',
         DATA / 'annular_two_operator25.json']
G, O, T = [json.loads(p.read_text()) for p in paths]

def red(w, cones=(6, 7)):
    out = []
    for z in w:
        if abs(z) in cones:
            z = abs(z)
        if out and (out[-1] == -z or (z in cones and out[-1] == z)):
            out.pop()
        else:
            out.append(z)
    return out

def inv(w):
    return [-z for z in w[::-1]]

def mul(*ws):
    return red([z for w in ws for z in w])

def con(h, w):
    return mul(h, w, inv(h))

def com(u, v):
    return mul(u, v, inv(u), inv(v))

def sub(w, mp):
    return red([z for v in w for z in (mp[abs(v)] if v > 0 else inv(mp[abs(v)]))])

checks = []
def check(name, left, right):
    left, right = red(left), red(right)
    assert left == right, (name, left, right)
    checks.append({'name': name, 'left': left, 'right': right})

eta = {int(k): v for k, v in G['eta_in_common_K'].items()}
mark = {int(k): v for k, v in O['selected_cone_old_to_new'].items()}
a, B, tau, m = [1], [2], [7], [8]
A = eta[1]
C = con(inv(A), tau)
Bplus = eta[2]
b = con(C, Bplus)
V = con(A, Bplus)
delta = lambda w: con(tau, w)
norm = lambda w: mul(w, delta(w))
check('selected plus local a', A, T['plus_local_to_global']['1'])
check('selected plus local b', b, T['plus_local_to_global']['2'])
check('selected plus local cone', C, T['plus_local_to_global']['6'])
check('V=eta(O1)', V, sub([1, 2, -1], eta))
check('V=a B^-1 a^-1', V, [1, -2, -1])
check('A=V^-1 a^-1 V', A, mul(inv(V), [-1], V))
check('V A^-1 V^-1=a', con(V, inv(A)), a)

raw = [sub(z['word'], mark) for z in G['actual_six_source_words']]
check('actual s1 is norm V freely', raw[0], norm(V))
r = com(A, con(C, A))
h = mul(A, C, b)
check('actual s4 retains exact diagonal correction', raw[3], mul(con(h, r), norm(A)))

regional = {(z['side'], z['name']): sub(z['word'], mark)
            for z in G['regional_relators']}
check('raw diagonal correction is actual plus diagonal_a', r,
      regional['plus', 'diagonal_a'])
check('actual diagonal_a conjugates to [A,delta A]',
      con(A, regional['plus', 'diagonal_a']), com(A, delta(A)))
check('inverse actual diagonal_b conjugates to [V,delta V]',
      inv(con(A, regional['plus', 'diagonal_b'])), com(V, delta(V)))
check('actual pair_ab conjugates to [A,delta V]',
      con(A, regional['plus', 'pair_ab']), com(A, delta(V)))
check('inverse cone-conjugate pair gives [V,delta A]',
      inv(delta(con(A, regional['plus', 'pair_ab']))), com(V, delta(A)))

for sign in ['m', 'm_inverse']:
    alpha = {int(k): v for k, v in T['far_orbifold_actions'][sign].items()}
    check(sign + ' fixes common a literally', alpha[1], a)
    check(sign + ' fixes selected tau literally', alpha[7], tau)
    check(sign + ' fixes norm a literally', sub(norm(a), alpha), norm(a))
check('actual inner generic [m,a]', regional['minus', 'k_fixes_a'], com(m, a))
cross = sub(G['cross_relators'][0]['word'], mark)
check('actual cross is [tau,m]', cross, com(tau, m))

# Universal calculation in the exact four-cross-commutator presentation.
# Symbols 1,2 are V,A and 3,4 are delta V,delta A.
def product_normal(w):
    left = red([z for z in w if abs(z) <= 2], ())
    right = red([(1 if z > 0 else -1) * (abs(z)-2)
                 for z in w if abs(z) > 2], ())
    return [left, right]

u_symbolic = [1, 3, -4, -2, -3, -1]
norm_conjugate_symbolic = [1, -2, -1, 3, -4, -3]
assert product_normal(u_symbolic) == product_normal(norm_conjugate_symbolic)
assert product_normal(u_symbolic) == [[1, -2, -1], [1, -2, -1]]

source_word = [6, 1, -4, -1, -6, 1, 4, -1]
assert red(source_word, ()) == source_word and len(source_word) == 8

# One fixed explicit finite source quotient detects the source word.
# D8 = UT3(F2), coordinates (u,v,z); [A,B]=(0,0,1).
def dm(q, r):
    u,v,z=q; U,V,Z=r
    return (u^U, v^V, z^Z^(u&V))
def di(q):
    u,v,z=q
    return (u,v,z^(u&v))
def deval(w, mp):
    out=(0,0,0)
    for z in w:
        q=mp.get(abs(z),(0,0,0))
        out=dm(out, q if z>0 else di(q))
    return out
finite_source_image=deval(source_word,{6:(1,0,0),4:(0,1,0)})
assert finite_source_image == (0,0,1)

Uraw = mul(raw[0], inv(raw[3]), inv(raw[0]))
result = {
 'status':'PASS',
 'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
 'selected_generators':{'a':1,'B':2,'tau':7,'m':8},
 'words':{'A':A,'V':V,'C':C,'b':b,'correction_conjugator':h,
          'diagonal_correction':r,'actual_s1':raw[0],'actual_s4':raw[3],
          'raw_U':Uraw,'proved_U':norm(a)},
 'literal_checks':checks,
 'complete_cross_block':{'generator_order':['V','A','delta V','delta A'],
                         'source_expression':u_symbolic,
                         'norm_expression':norm_conjugate_symbolic,
                         'common_product_normal_form':product_normal(u_symbolic)},
 'abstract_source_order':['s1','s2','s3','s4','v','m'],
 'nontrivial_source_relator':source_word,
 'source_relator_length':8,
 'finite_source_detector':{'group':'UT3(F2), order 8','m':[1,0,0],
                           's4':[0,1,0],'all_other_generators':[0,0,0],
                           'nontrivial_image':list(finite_source_image)},
 'scope':'Actual full one-neck source relation, discrete and full profinite; '
         'no source-centralizer equality or non-equality inferred.'
}
out=DATA/'actual_source_commutator26.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print('PASS: %d literal marked-word comparisons.' % len(checks))
print('PASS: all four cross commutations tied to three actual node relators.')
print('PASS: U=s1*s4^-1*s1^-1 equals a*tau*a*tau after those relations.')
print('PASS: both signed actual m actions fix a,tau and their norm.')
print('PASS: actual source commutator word',source_word,'has length 8.')
print('PASS: explicit order-eight source detector image',finite_source_image,'is nontrivial.')
print('Saved',out.relative_to(ROOT))
