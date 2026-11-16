"""Exact finite and rational data for the common-involution Birman note.

This certifies only the displayed permutations and rational maps.  The
continuous/completed group comparison is proved in the accompanying note.
"""
from pathlib import Path
import json
import sympy as S

HERE = Path(__file__).resolve().parent
source = json.loads((HERE.parent / 'rigid7_subsets.json').read_text())
I = tuple(range(12))
T = {tuple(g) for g in source['T_permutations']}
d = tuple(source['D_permutation'])

def transpositions(pairs):
    g = list(I)
    for a, b in pairs:
        g[a-1], g[b-1] = b-1, a-1
    return tuple(g)

r = transpositions([(1,3),(2,5),(6,8),(12,10),(9,11),(4,7)])
s = transpositions([(1,2),(3,5),(4,6),(7,8),(9,10),(11,12)])

def mul(a,b):
    return tuple(a[b[i]] for i in I)

def group(gens):
    seen, todo = {I}, [I]
    while todo:
        a = todo.pop()
        for g in gens:
            b = mul(g,a)
            if b not in seen:
                seen.add(b); todo.append(b)
    return seen

def order(a):
    p = I
    for k in range(1,121):
        p = mul(a,p)
        if p == I:
            return k
    raise AssertionError('unexpected order')

J, A = group([d,r]), group([d,r,s])
assert r in T and s in T and mul(r,s) == mul(s,r)
assert len(J) == 10 and len(A) == 60 and T <= A
assert order(mul(s,d)) == 3 and order(mul(mul(r,s),d)) == 5
print('Actual s,r belong to T, commute, and <d,r,s> has order60: PASS')
print('Exact deck-ambiguity obstruction: order(sd)=3; order(rsd)=5: PASS')

pairs = [(1,3),(2,5),(6,8),(12,10),(9,11),(4,7)]
pair_sets = [set(p) for p in pairs]
pair_action = [pair_sets.index({s[a-1]+1 for a in p}) for p in pairs]
assert pair_action == [1,0,5,4,3,2]
print('On ordinary quotient labels s swaps U,V and reverses the four others: PASS')

# Every centralizer permutation of a transitive permutation group is
# determined by the image of one point.  Check all twelve possibilities.
central = []
for dest in I:
    p = [None]*12
    valid = True
    for a in A:
        x, y = a[0], a[dest]
        if p[x] not in (None,y):
            valid = False; break
        p[x] = y
    if valid and None not in p and len(set(p)) == 12:
        p = tuple(p)
        if all(mul(p,a) == mul(a,p) for a in A):
            central.append(p)
assert len(central) == 2 and I in central
antipodal = next(g for g in central if g != I)
assert antipodal[0] == 2 and antipodal[2] == 0
assert [g for g in central if g[0] == 0] == [I]
print('C_S12(A5) has order2; its nonidentity swaps original labels1,3: PASS')

# J is regular on the ten nonpole labels.  Its commuting permutations
# fixing both poles are determined by the image of original label2.
nonpoles = sorted(set(I)-{0,2})
right_J = []
for dest in nonpoles:
    p = [None]*12; p[0] = 0; p[2] = 2
    for a in J:
        p[a[1]] = a[dest]
    assert None not in p and len(set(p)) == 12
    p = tuple(p)
    assert all(mul(p,a) == mul(a,p) for a in J)
    right_J.append(p)
stabilizer = [p for p in right_J if {p[1],p[4]} == {1,4}]
assert len(right_J) == 10 and len(stabilizer) == 2
assert next(g for g in stabilizer if g != I)[1] == 4
print('The G permutation quotient is regular D5; stabilizer of V has order2: PASS')
print('Its nonpure element swaps original labels2,5; no purity assumption is inserted: PASS')

u,w = S.symbols('u w')
W = 4*(u+1)**2/(u-1)**2
Q = 4*w*(w*w+40*w+80)**2/(w-4)**5
assert S.cancel(Q.subs(w,W)-(u**5+1)**2/u**5) == 0
assert S.cancel(Q-4-16*(5*w*w+40*w+16)**2/(w-4)**5) == 0
assert S.cancel(5*W**2+40*W+16-256*(u**4+u**3+u**2+u+1)/(u-1)**4) == 0
phi = (1+S.sqrt(5))/2
assert S.simplify(W.subs(u,-phi**2)) == S.Rational(4,5)
assert S.simplify(Q.subs(w,S.Rational(4,5))) == -121
print('Based orbifold maps, two filled cusp polynomial, and w*=4/5,q*=-121: PASS')

out = {
    'r':r, 's':s, 'd':d,
    'orders':{'sd':order(mul(s,d)), 'rsd':order(mul(mul(r,s),d))},
    'ordinary_pairs':pairs, 's_pair_action_zero_based':pair_action,
    'centralizer_A5':central, 'right_J_pole_fixing':right_J,
    'V_stabilizer':stabilizer,
    'W_u':str(W), 'Q_w':str(Q), 'common_w':'4/5', 'common_q':'-121',
    'scope':'Finite permutation and exact rational data only; no proof of K=1.'
}
(HERE/'Birman_cocycle_data.json').write_text(json.dumps(out,indent=2)+'\n')
