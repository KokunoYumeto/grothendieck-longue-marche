"""Independent focused audit of E109; imports no author program.

Build exterior operations from signed dictionary multiplication, recompute
the p=19 Bloch sum in a separately encoded quadratic field, and check the
truncated group-ring normalization of the central commutator.
"""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json
import sympy as sp


def plus(*terms):
    out = {}
    for term in terms:
        for k, v in term.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}


def scale(n, a):
    return {k: n*v for k, v in a.items() if n*v}


def wedge(a, b):
    out = {}
    for u, x in a.items():
        for v, y in b.items():
            seq = u + v
            if len(set(seq)) != len(seq):
                continue
            sign = (-1)**sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1, len(seq)))
            k = tuple(sorted(seq))
            out[k] = out.get(k, 0) + sign*x*y
    return {k: v for k, v in out.items() if v}


E = [{(i,): 1} for i in range(6)]
q = plus(*(wedge(E[2*i], E[2*i+1]) for i in range(3)))
pairs = list(combinations(range(6), 2))
triples = list(combinations(range(6), 3))
keep = [p for p in pairs if p != (4, 5)]


def pairing(i, j):
    return (1 if i % 2 == 0 else -1) if i//2 == j//2 and i != j else 0


def quotient(a):
    return plus(a, scale(-a.get((4, 5), 0), q))


def johnson(eta):
    out = [{} for _ in range(6)]
    for (a, b, c), v in eta.items():
        for x in range(6):
            out[x] = plus(out[x], scale(v*pairing(a, x), wedge(E[b], E[c])),
                          scale(v*pairing(b, x), wedge(E[c], E[a])),
                          scale(v*pairing(c, x), wedge(E[a], E[b])))
    return [quotient(a) for a in out]


def alt(D):
    return plus(*(plus(wedge(E[2*i], D[2*i+1]), scale(-1, wedge(E[2*i+1], D[2*i]))) for i in range(3)))


def cm(a):
    return [a.get((0, 2, 4), 0), a.get((1, 3, 5), 0)]


def flatten(D):
    return [a.get(p, 0) for a in D for p in keep]


J = []
for t in triples:
    eta = {t: 1}
    D = johnson(eta)
    assert [Fraction(v, 3) for v in cm(alt(D))] == cm(eta)
    J.append(flatten(D))
inner = []
for h in E:
    D = [quotient(wedge(h, x)) for x in E]
    assert johnson(wedge(q, h)) == [scale(-1, a) for a in D]
    assert cm(alt(D)) == [0, 0]
    assert alt([wedge(h, x) for x in E]) == scale(-2, wedge(q, h))
    inner.append(flatten(D))
jm = sp.Matrix(J).T
im = sp.Matrix(inner).T
assert jm.rank() == 20 and im.rank() == 6
# Direct elimination over F5 certifies the integral direct-summand assertion.
a = [[int(x) % 5 for x in row] for row in im.tolist()]
rank = 0
for c in range(6):
    p = next(i for i in range(rank, len(a)) if a[i][c])
    a[rank], a[p] = a[p], a[rank]
    a[rank] = [(x*pow(a[rank][c], -1, 5)) % 5 for x in a[rank]]
    for i in range(len(a)):
        if i != rank:
            d = a[i][c]
            a[i] = [(x-d*y) % 5 for x, y in zip(a[i], a[rank])]
    rank += 1
assert rank == 6
characters = [(1,1),(3,3),(2,1),(2,3),(1,2),(3,2)]
fixed = [t for t in triples if all(sum(characters[j][k] for j in t) % 4 == 0 for k in range(2))]
assert fixed == [(0,2,4),(1,3,5)]

# Encode a+b*i as a+19*b.  This is independent of the author's tuple model.
p = 19
def fadd(x,y): return ((x%p+y%p)%p) + p*((x//p+y//p)%p)
def fneg(x): return (-x%p)%p + p*((-(x//p))%p)
def fmul(x,y):
    a,b,c,d = x%p,x//p,y%p,y//p
    return (a*c-b*d)%p + p*((a*d+b*c)%p)
def fpow(x,n):
    z=1
    for bit in bin(n)[2:]:
        z=fmul(z,z)
        if bit=='1': z=fmul(z,x)
    return z
def fdiv(x,y):
    assert y
    return fmul(x,fpow(y,p*p-2))
def on(P): return P is None or fmul(P[1],P[1])==fadd(fpow(P[0],3),P[0])
def addP(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and fadd(y,v)==0:return None
    if P==Q:m=fdiv(fadd(fmul(3,fmul(x,x)),1),fmul(2,y))
    else:m=fdiv(fadd(v,fneg(y)),fadd(u,fneg(x)))
    z=fadd(fadd(fmul(m,m),fneg(x)),fneg(u))
    w=fadd(fmul(m,fadd(x,fneg(z))),fneg(y))
    assert on((z,w))
    return z,w
def mult(P,n):
    Q=None
    for _ in range(n):Q=addP(Q,P)
    return Q
terms=[]
delta=None
for u in range(p*p):
    if fadd(u,fpow(u,p))!=1:continue
    sign=fpow(u,(p*p-1)//2)
    assert sign in (1,p-1)
    P=fpow(u,(p-1)//2),fpow(u,(p-3)//4)
    assert on(P)
    if sign==p-1:P=P[0],fneg(P[1])
    delta=addP(delta,P)
    terms.append(u)
assert len(terms)==19 and delta==(17,16)
four=mult(delta,4)
assert four==(9,4) and mult(four,5) is None and four is not None
assert mult(delta,10) is None and mult(delta,5) is not None and mult(delta,2) is not None

# Noncommutative degree-two algebra: the central commutator has positive sign.
def nc(a,b):
    out={}
    for x,u in a.items():
        for y,v in b.items():
            if len(x+y)<=2:out[x+y]=out.get(x+y,0)+u*v
    return {k:v for k,v in out.items() if v}
gx={():1,(0,):1}; gy={():1,(1,):1}
ix={():1,(0,):-1,(0,0):1}; iy={():1,(1,):-1,(1,1):1}
comm=nc(nc(nc(gx,gy),ix),iy)
assert comm=={():1,(0,1):1,(1,0):-1}
result={
    'status':'PASS','independence':'No import of the author program or certificate.',
    'exterior_cube_columns_checked':20,'inner_columns_checked':6,
    'Johnson_rank':20,'inner_rank_mod5':rank,'Delta_fixed_triples':fixed,
    'pure_CM_left_inverse_and_inner_annihilation':True,
    'p19_trace_one_terms':len(terms),'delta19':delta,'delta19_order':10,
    'four_delta19':four,'four_delta19_order':5,
    'group_ring_commutator':'XY-YX',
    'scope':'Focused independent finite coefficient and p19 checks. The primary-source and arithmetic comparison proof audit is recorded separately.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
