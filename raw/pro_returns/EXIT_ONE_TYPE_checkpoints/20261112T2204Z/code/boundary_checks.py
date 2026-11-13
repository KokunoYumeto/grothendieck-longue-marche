"""Exact finite checks for EXIT_ONE_TYPE Part 4.
Run: python code/boundary_checks.py
No random choices and no floating-point rank computations.
"""
from itertools import combinations, product, permutations
from collections import Counter
from math import factorial
import json
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def split_complex(n):
    # Root at leaf n. Each split is uniquely the side not containing n.
    ground = frozenset(range(1, n))
    vertices = [frozenset(s) for r in range(2, n-1)
                for s in combinations(sorted(ground), r)]
    def compatible(a, b):
        return a <= b or b <= a or a.isdisjoint(b)
    faces = [[(i,) for i in range(len(vertices))]]
    for size in range(2, n-2):
        layer = [c for c in combinations(range(len(vertices)), size)
                 if all(compatible(vertices[a], vertices[b])
                        for a,b in combinations(c, 2))]
        faces.append(layer)
    return vertices, faces


def boundary_homology(n):
    vertices, faces = split_complex(n)
    nv = len(vertices)
    edges = faces[1] if len(faces)>1 else []
    triangles = faces[2] if len(faces)>2 else []
    parent=list(range(nv))
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    tree=set()
    for i,(a,b) in enumerate(edges):
        a,b=find(a),find(b)
        if a!=b:
            parent[a]=b;tree.add(i)
    components=len({find(a) for a in range(nv)}) if nv else 0
    non_tree=[i for i in range(len(edges)) if i not in tree]
    row={i:j for j,i in enumerate(non_tree)}
    edge_index={e:i for i,e in enumerate(edges)}
    A=Matrix.zeros(len(non_tree), len(triangles))
    for j,t in enumerate(triangles):
        for k in range(3):
            e=t[:k]+t[k+1:]
            eidx=edge_index[e]
            if eidx in row:A[row[eidx],j]+=(-1)**k
    if A.rows and A.cols:
        S=smith_normal_form(A,domain=ZZ)
        diagonal=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0]
    else:diagonal=[]
    rank=len(diagonal)
    return {'n':n,'f_vector':[len(f) for f in faces],
            'connected_components':components,
            'H1_free_rank':len(non_tree)-rank,
            'H1_torsion':[d for d in diagonal if d>1],
            'H2_free_rank':len(triangles)-rank,
            'cycle_boundary_smith_diagonal_counts':dict(Counter(diagonal)),
            'expected_top_betti':factorial(n-2)}


def segal_counterexample():
    perm={1:2,2:1,3:4,4:3}
    def act(chain):return tuple(tuple(sorted(perm[x] for x in s)) for s in chain)
    def orbit(chain):return tuple(sorted({chain,act(chain)}))
    middle=(1,2)
    upper=[(1,2,3),(1,2,4)]
    lower=[(1,),(2,)]
    triples={orbit((a,middle,c)) for a,c in product(upper,lower)}
    left={orbit((a,middle)) for a in upper}
    right={orbit((middle,c)) for c in lower}
    composites={orbit((t[0][0],t[0][2])) for t in triples}
    assert len(triples)==2 and len(left)==len(right)==1 and len(composites)==2
    return {'group':'C2 acting as (12)(34)',
            'triple_flag_orbits':sorted(triples),
            'composable_pair_component_count':len(left)*len(right),
            'triple_flag_component_count':len(triples),
            'distinct_composite_component_count':len(composites),
            'Segal_map_is_bijective':False}

def loop_graph_category():
    # Half-edges 0,1 form the loop; 2 is the labelled leg and must be fixed.
    involution=(1,0,2)
    automorphisms=[p for p in permutations(range(3))
                   if p[2]==2 and all(p[involution[i]]==involution[p[i]] for i in range(3))]
    assert len(automorphisms)==2
    # Normalized bar boundary [a|b] -> [b] - [a+b mod 2] + [a].
    nonzero=lambda x: 1 if x%2 else 0
    d2=nonzero(1)-nonzero(1+1)+nonzero(1)
    assert d2==2
    return {'automorphisms':automorphisms,'group':'C2',
            'normalized_bar_boundary_d2':[[d2]],'H1':'Z/2',
            'coarse_dual_complex':'point','coarse_H1':'0'}


def lens_bundle(degree):
    # A degree-d plane curve has self-intersection d^2; here d=1 or 2.
    euler=degree**2
    S=smith_normal_form(Matrix([[euler]]),domain=ZZ)
    d=abs(int(S[0,0]))
    return {'pair':'P2, '+('line' if degree==1 else 'smooth conic'),
            'normal_Chern_number':euler,'boundary_smith_diagonal':d,
            'pi1_link':'0' if d==1 else f'Z/{d}'}


result={'segal_counterexample':segal_counterexample(),
        'genus_zero_boundary_complexes':[boundary_homology(n) for n in (4,5,6)],
        'one_loop_graph_automorphism_category':loop_graph_category(),
        'same_dual_complex_different_links':[lens_bundle(d) for d in (1,2)]}
assert result['genus_zero_boundary_complexes'][1]['H1_free_rank']==6
assert result['genus_zero_boundary_complexes'][2]['H2_free_rank']==24
assert result['genus_zero_boundary_complexes'][2]['H1_torsion']==[]
print(json.dumps(result,indent=2))
