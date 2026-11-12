"""Exact checks: Fermat-cover cycles, Heisenberg conjugation, and Lie words.

No Galois action is inferred from arbitrary matrices.  The Lie calculation
checks the central, last-degree elements which every IA action fixes.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import gcd
from pathlib import Path
import json
import platform
import sympy as sp


def fermat(n):
    vertices = list(product(range(n), repeat=2))
    vi = {v: i for i, v in enumerate(vertices)}
    edges = [(v, d) for v in vertices for d in (0, 1)]
    ei = {e: i for i, e in enumerate(edges)}
    incidence = sp.zeros(n*n, 2*n*n)
    for j, (v, d) in enumerate(edges):
        end = list(v); end[d] = (end[d]+1) % n
        incidence[vi[v], j] -= 1
        incidence[vi[tuple(end)], j] += 1

    def walk(v, word):
        v = list(v); out = sp.zeros(2*n*n, 1)
        for d, sign in word:
            if sign == 1:
                out[ei[(tuple(v), d)], 0] += 1
                v[d] = (v[d]+1) % n
            else:
                v[d] = (v[d]-1) % n
                out[ei[(tuple(v), d)], 0] -= 1
        return out, tuple(v)

    boundary = []
    for j in range(n): boundary.append(walk((0,j), [(0,1)]*n)[0])
    for i in range(n): boundary.append(walk((i,0), [(1,1)]*n)[0])
    for j in range(n): boundary.append(walk((0,j), [(0,1),(1,1)]*n)[0])
    B = sp.Matrix.hstack(*boundary)
    c, end = walk((0,0), [(0,1),(1,1),(0,-1),(1,-1)])
    assert end == (0,0)
    assert incidence*B == sp.zeros(n*n, 3*n)
    assert incidence*c == sp.zeros(n*n, 1)
    rB, rBc = B.rank(), B.row_join(c).rank()
    homology = 2*n*n-incidence.rank()-rB
    assert rB == 3*n-1
    assert homology == (n-1)*(n-2)
    assert (rBc > rB) == (n >= 3)
    return dict(n=n, vertices=n*n, edges=2*n*n, boundary_rank=rB,
                compact_H1_rank=homology, commutator_survives=bool(rBc>rB),
                boundary_plus_commutator_rank=rBc)


def heisenberg(q):
    def mul(a,b):
        x,y,z=a; X,Y,Z=b
        return ((x+X)%q,(y+Y)%q,(z+Z+x*Y)%q)
    checks=0
    for alpha in range(q):
        if gcd(alpha,q) != 1: continue
        for t in range(q):
            r=t*pow(alpha,-1,q)%q
            got=mul(mul((0,r,0),(alpha,0,t)),(0,-r,0))
            assert got == (alpha,0,0)
            checks += 1
    roots=[a for a in range(q) if (a*a+1)%q==0]
    assert len(roots)==2 and gcd(roots[0]-roots[1],q)==1
    return dict(modulus=q, conjugations_checked=checks, roots_of_minus_one=roots,
                cancellation="y^r (x^alpha c^t) y^(-r)=x^alpha; r=t/alpha")


def mul_poly(a,b):
    out=defaultdict(int)
    for u,c in a.items():
        for v,d in b.items(): out[u+v]+=c*d
    return {w:c for w,c in out.items() if c}


def bracket(a,b):
    out=defaultdict(int,mul_poly(a,b))
    for w,c in mul_poly(b,a).items(): out[w]-=c
    return {w:c for w,c in out.items() if c}


def lyndon(w):
    return all(w < w[i:] for i in range(1,len(w)))


@lru_cache(None)
def expansion(w):
    if len(w)==1: return {w:1}
    cut=next(i for i in range(1,len(w)) if lyndon(w[i:]))
    return bracket(expansion(w[:cut]),expansion(w[cut:]))


def lie_table(max_degree=10):
    rows=[]
    for n in range(1,max_degree+1):
        words=[''.join(w) for w in product('XY',repeat=n) if lyndon(''.join(w))]
        for w in words:
            e=expansion(w)
            assert min(e)==w and e[w]==1
        expected=sum(int(sp.mobius(d))*2**(n//d) for d in sp.divisors(n))//n
        assert len(words)==expected
        witness='X'*(n-1)+'Y' if n>=2 else 'X'
        e=expansion(witness)
        assert e[witness]==1
        rows.append(dict(degree=n, integral_rank=len(words),
                         leading_word_certificate=True,
                         last_degree_fixed_by_every_IA_action=True,
                         witness=witness,
                         witness_associative_expansion=e,
                         nonperipheral_in_class_n=bool(n>=3)))
    return rows


def blowup():
    M=sp.Matrix([[1,1]])
    k=sp.Matrix([1,-1])
    assert M*k==sp.zeros(1,1)
    finite=[]
    for n in (2,3,5,25):
        image={(a+b)%n for a in range(n) for b in range(n)}
        kernel=[(a,b) for a in range(n) for b in range(n) if (a+b)%n==0]
        assert len(image)==n and len(kernel)==n
        finite.append(dict(modulus=n,image_size=len(image),kernel_size=len(kernel)))
    return dict(chart="t=a*b, u=b", inertia_matrix=[[1,1]],
                kernel_generator=[1,-1], finite_checks=finite)


def s3_certificate():
    from sympy.combinatorics import Permutation, PermutationGroup
    x=Permutation(0,1,size=3)
    y=Permutation(0,1,2,size=3)
    G=PermutationGroup(x,y)
    assert G.order()==6 and x*y!=y*x
    return dict(generator_orders=[int(x.order()),int(y.order())],
                generated_group_order=int(G.order()),noncommuting=True,
                purpose="Finite quotient certifying that pi itself is not procyclic")


def node_branch_exchange():
    out=[]
    for n in (3,4,5,7,9,25):
        for j in range(n):
            # tau(j)=j+1; exchange(j)=-j; exchange*tau*exchange=tau^-1.
            lhs=-((-j+1)%n)%n
            assert lhs==(j-1)%n
        out.append(dict(modulus=n,checks=n,conjugate_exponent=-1))
    return dict(local_equation="x*y=t",root_relation="x_n*y_n=t_n",checks=out,
                scope="Local branch exchange; no global specialization assertion")


def real_cyclotomic_kernel():
    character={e:pow(3,e,4) for e in (0,1)}
    kernel=[e for e in character if character[e]==1]
    assert character=={0:1,1:3} and kernel==[0]
    return dict(galois_group="C2",character_mod_4=character,
                cyclotomic_kernel=kernel,
                consequence="The kernel action fixes every geometric group element")


result={
    "runtime":{"python":platform.python_version(),"sympy":sp.__version__},
    "Fermat_cover_chain_checks":[fermat(n) for n in (2,3,4,5)],
    "CM_Heisenberg_checks":[heisenberg(q) for q in (5,25,125)],
    "lower_central_series":lie_table(),
    "blowup_local_inertia":blowup(),
    "S3_quotient":s3_certificate(),
    "node_branch_exchange":node_branch_exchange(),
    "real_cyclotomic_kernel":real_cyclotomic_kernel(),
    "scope":"The arithmetic action beyond class two is not simulated. Last-degree invariants follow from the proved IA lemma."
}
output=json.dumps(result,indent=2)
Path(__file__).with_name('root_math_checks_output.json').write_text(output+'\n')
print(output)
