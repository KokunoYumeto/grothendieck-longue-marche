"""Independent literal B130 check; imports no CE producer.

Reads the older complete 9-generator presentation, changes only its plus
cone to the selected-gap cone, and reconstructs the proof's raw words.
The universal four-cross block is evaluated in F2 x F2, separately from
the cone-free reduction.  No finite target is used to prove group equality.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / 'work_CE/next_symmetric_nodes/annular_neck_presentation23.json'
OUTPUT = Path(__file__).with_suffix('.json')
D = json.loads(INPUT.read_text())
checks = []

def red(w, cones=(6, 7)):
    s = []
    for a in w:
        a = abs(a) if abs(a) in cones else a
        if s and (a == -s[-1] or (a in cones and a == s[-1])):
            s.pop()
        else:
            s.append(a)
    return s

def mul(*ws):
    return red([a for w in ws for a in w])

def inv(w):
    return red([-a for a in reversed(w)])

def conj(a, b):
    return mul(a, b, inv(a))

def comm(a, b):
    return mul(a, b, inv(a), inv(b))

def sub(w, images):
    return mul(*(images[abs(a)] if a > 0 else inv(images[abs(a)]) for a in w))

def eq(name, a, b):
    assert red(a) == red(b), (name, red(a), red(b))
    checks.append(name)

a, B, tau, m = [1], [2], [7], [8]
eta = {int(k): v for k, v in D['eta_in_common_K'].items()}
A = eta[1]
V = conj(A, eta[2])
C = conj(inv(A), tau)
b = conj(C, eta[2])
gauge = {i: [i] for i in range(1, 10)}
gauge[7] = C
delta = lambda w: conj(tau, w)
norm = lambda w: mul(w, delta(w))

eq('actual mirror V', V, [1, -2, -1])
eq('actual mirror A', A, conj(inv(V), inv(a)))
eq('actual VA^-1V^-1=a', conj(V, inv(A)), a)
r = comm(A, conj(C, A))
rb = comm(b, conj(C, b))
rab = comm(A, b)
plus = {z['name']: sub(z['word'], gauge) for z in D['regional_relators'] if z['side'] == 'plus'}
eq('actual plus diagonal-a', plus['diagonal_a'], r)
eq('actual plus diagonal-b', plus['diagonal_b'], rb)
eq('actual plus pair-ab', plus['pair_ab'], rab)
eq('cross A/deltaA', conj(A, r), comm(A, delta(A)))
eq('cross V/deltaV', inv(conj(A, rb)), comm(V, delta(V)))
eq('cross A/deltaV', conj(A, rab), comm(A, delta(V)))
eq('cross V/deltaA', inv(delta(conj(A, rab))), comm(V, delta(A)))

raw = [sub(z['word'], gauge) for z in D['actual_six_source_words']]
s1 = conj(A, mul(C, b, C, b))
s4 = conj(A, mul(C, b, r, inv(b), C, A, C, A, C))
q = mul(A, C, b)
eq('actual raw s1', raw[0], s1)
eq('actual raw s4', raw[3], s4)
eq('s1 exact norm', s1, norm(V))
eq('s4 exact node correction', s4, mul(conj(q, r), norm(A)))

minus = {z['name']: z['word'] for z in D['regional_relators'] if z['side'] == 'minus'}
eq('actual inner [m,a]', minus['k_fixes_a'], comm(m, a))
cross = {z['name']: sub(z['word'], gauge) for z in D['cross_relators']}
eq('actual selected cross [tau,m]', cross['opposite_cone_inner_loop'], comm(tau, m))

# Independent normal form in the universal cross group F(V,A) x F(dV,dA).
def free_red(w):
    return red(w, cones=())

def product_normal(w):
    return [free_red([a for a in w if abs(a) <= 2]),
            free_red([(1 if a > 0 else -1) * (abs(a) - 2)
                      for a in w if abs(a) > 2])]

source_expr = [1, 3, -4, -2, -3, -1]
norm_expr = [1, -2, -1, 3, -4, -3]
assert product_normal(source_expr) == product_normal(norm_expr) == [[1, -2, -1], [1, -2, -1]]
checks.append('universal complete four-cross norm product')

source_word = [6, 1, -4, -1, -6, 1, 4, -1]
assert free_red(source_word) == source_word and source_word[0] != -source_word[-1]
def heis(x, y):
    u,v,z = x; a,b,c = y
    return ((u+a)%2, (v+b)%2, (z+c+u*b)%2)
def heis_inv(x):
    u,v,z = x
    return (u,v,(z+u*v)%2)
values = {i:(0,0,0) for i in range(1,7)}
values[6] = (1,0,0); values[4] = (0,1,0)
v = (0,0,0)
for x in source_word:
    z = values[abs(x)]
    v = heis(v, z if x>0 else heis_inv(z))
assert v == (0,0,1)
checks.append('nontrivial exact order-eight source detector')

out = {'status':'PASS','input':str(INPUT.relative_to(ROOT)),
       'input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),
       'literal_checks':checks,'count':len(checks),
       'selected_words':{'A':A,'V':V,'C':C,'b':b,'s1':s1,'s4':s4,'node_r':r},
       'universal_product_normal_form':product_normal(source_expr),
       'source_word':source_word,'finite_detector':list(v),
       'scope':'Independent raw marking and algebra replay; the full all-quotient and compact separation proofs are reviewed separately.'}
OUTPUT.write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS {len(checks)} independent exact checks from the complete actual 9-generator presentation.')
print('Raw source correction retained; four-cross norm implication and order-eight source witness PASS.')
