#!/usr/bin/env python3
"""Exact finite checks for research notes only; no scan/OCR/transcription code.

Standard-library Python. Statements are conditional on the interpretation of
the relevant manuscript objects described in finite_research.md.
"""
from itertools import combinations, permutations, product
from collections import Counter, deque
import json


def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def order(p):
    e = tuple(range(len(p)))
    q = e
    for n in range(1, 10000):
        q = compose(p, q)
        if q == e:
            return n
    raise AssertionError("order bound exceeded")


def cycle_type(p):
    left, sizes = set(range(len(p))), []
    while left:
        a = x = min(left)
        n = 0
        while x in left:
            left.remove(x)
            n += 1
            x = p[x]
        assert x == a
        sizes.append(n)
    return tuple(sorted(sizes))


def norm(v, q):
    a = next(x for x in v if x % q)
    return tuple(x * pow(a, -1, q) % q for x in v)


def mul2(A, x, q=3):
    a,b,c,d = A
    return ((a*x[0]+b*x[1]) % q, (c*x[0]+d*x[1]) % q)


out = {}

# Scan 159: a counterexample to c alone, preserving the four-element-block
# hypothesis. E_i = {3i,3i+1,3i+2}; orient each pair of classes i -> j for i<j.
classes = [frozenset(range(3*i, 3*i+3)) for i in range(4)]
cross_pairs = {frozenset((a,b)) for i in range(4) for j in range(i+1,4)
               for a in classes[i] for b in classes[j]}
bad_blocks = {classes[i] | {b} for i in range(4) for j in range(i+1,4) for b in classes[j]}
assert len(bad_blocks) == 18 and all(len(D) == 4 for D in bad_blocks)
assert all(sum(pair <= D for D in bad_blocks) == 1 for pair in cross_pairs)
assert any(any(len(D & E) != 1 for E in classes) for D in bad_blocks)
out['159_c_alone_counterexample'] = {
    'classes': [sorted(E) for E in classes],
    'blocks': sorted(sorted(D) for D in bad_blocks),
    'number_of_blocks': len(bad_blocks), 'cross_pairs_each_covered_once': len(cross_pairs),
    'all_block_sizes': sorted({len(D) for D in bad_blocks})}

# The affine plane and its dual incidence configuration.
points = tuple(product(range(3), repeat=2))
directions = tuple(sorted({norm(x,3) for x in points if x != (0,0)}))
line_families = []
for d in directions:
    fam = {frozenset(((x[0]+t*d[0])%3,(x[1]+t*d[1])%3) for t in range(3)) for x in points}
    assert len(fam) == 3
    line_families.append(tuple(sorted(fam, key=lambda a: sorted(a))))
lines = tuple(L for fam in line_families for L in fam)
pencils = tuple(frozenset(i for i,L in enumerate(lines) if x in L) for x in points)
assert len(lines) == 12 and len(pencils) == 9
assert all(len(D) == 4 for D in pencils)
assert all(len(D & Dp) == 1 for D,Dp in combinations(pencils,2))
assert all(sum(a in D for D in pencils)==3 for a in range(12))
assert all(len(D & set(range(3*i,3*i+3))) == 1 for D in pencils for i in range(4))
completed = pencils + tuple(frozenset(range(3*i,3*i+3)) | {12} for i in range(4))
assert all(len(D & Dp)==1 for D,Dp in combinations(completed,2))
assert all(sum({a,b} <= D for D in completed)==1 for a,b in combinations(range(13),2))
out['159_affine_and_completed_incidence'] = {
    'points':9,'affine_lines':12,'pencils':9,'line_classes':4,
    'pencil_size':4,'pencils_per_line':3,
    'completed_points':13,'completed_lines':13,
    'unique_join_and_meet_verified':True}

# Exact cover enumerates all labelled Steiner triple systems on nine points.
pair_index = {p:i for i,p in enumerate(combinations(range(9),2))}
triples = tuple(combinations(range(9),3))
masks = tuple(sum(1 << pair_index[p] for p in combinations(T,2)) for T in triples)
by_pair = {i:[] for i in range(36)}
for k,m in enumerate(masks):
    for i in range(36):
        if m >> i & 1: by_pair[i].append(k)
all_sts = set()
full = (1 << 36)-1
def exact_cover(covered, chosen):
    if covered == full:
        all_sts.add(tuple(sorted(chosen)))
        return
    remaining = [i for i in range(36) if not (covered >> i & 1)]
    options = min(([k for k in by_pair[i] if not masks[k] & covered] for i in remaining), key=len)
    for k in options:
        exact_cover(covered | masks[k], chosen+(k,))
exact_cover(0, ())
triple_id = {T:i for i,T in enumerate(triples)}
pidx = {x:i for i,x in enumerate(points)}
affine_sts = tuple(sorted(triple_id[tuple(sorted(pidx[x] for x in L))] for L in lines))
orbit = {affine_sts}
queue = deque([affine_sts])
adjacent = [tuple(i+1 if j==i else i if j==i+1 else j for j in range(9)) for i in range(8)]
while queue:
    system = queue.popleft()
    for g in adjacent:
        image = tuple(sorted(triple_id[tuple(sorted(g[x] for x in triples[t]))] for t in system))
        if image not in orbit: orbit.add(image);queue.append(image)
assert all_sts == orbit and len(orbit)==840
out['159_steiner_completion'] = {'labelled_STS9':len(all_sts),
    'affine_plane_orbit_under_S9':len(orbit),
    'one_isomorphism_class':True,'automorphism_order':362880//len(orbit)}

# AGL(2,3) and its direction quotient; inspect lifts of double transpositions.
gl = tuple(A for A in product(range(3),repeat=4) if (A[0]*A[3]-A[1]*A[2])%3)
assert len(gl)==48
agl = []
dir_actions = set()
kernel = []
double_lift_orders = Counter()
direction_to_id = {d:i for i,d in enumerate(directions)}
for A in gl:
    dp = tuple(direction_to_id[norm(mul2(A,d),3)] for d in directions)
    dir_actions.add(dp)
    for t in points:
        p = tuple(pidx[((mul2(A,x)[0]+t[0])%3,(mul2(A,x)[1]+t[1])%3)] for x in points)
        agl.append(p)
        if dp == tuple(range(4)): kernel.append(p)
        if cycle_type(dp)==(2,2): double_lift_orders[order(p)] += 1
assert len(set(agl))==432 and len(dir_actions)==24 and len(kernel)==18
assert double_lift_orders == {4:54}
# Equal-parity S3 x S3 is (C3 x C3) semidirect simultaneous inversion.
s3 = tuple(permutations(range(3)))
equal_parity = [(a,b) for a in s3 for b in s3 if sign(a)==sign(b)]
assert len(equal_parity)==18
out['160_quadritriade_extension'] = {
    'GL2_F3':48,'AGL2_F3':432,'direction_image':24,'kernel':18,
    'equal_parity_subgroup_order':len(equal_parity),
    'double_transposition_lift_orders':dict(double_lift_orders),
    'extension_splits':False,
    'nonsplitting_certificate':'Every lift of each of the three order-two double transpositions has order four.'}

# Monomial F3 matrices acting on body diagonals of a cube.
body = tuple(sorted({norm(v,3) for v in product((1,2),repeat=3)}))
body_id = {v:i for i,v in enumerate(body)}
full_actions, positive_actions = [],[]
for p in permutations(range(3)):
    for s in product((1,2),repeat=3):
        det = sign(p) * s[0]*s[1]*s[2] % 3
        perm = tuple(body_id[norm(tuple(s[i]*v[p[i]]%3 for i in range(3)),3)] for v in body)
        full_actions.append(perm)
        if det==1: positive_actions.append(perm)
assert len(full_actions)==48 and len(positive_actions)==24
assert len(set(positive_actions))==24 and len(set(full_actions))==24
out['160_cube_line_stabilizer'] = {'full_monomial_group':48,
    'determinant_one_subgroup':24,'positive_action_on_four_body_diagonals_is_S4':True,
    'kernel_of_full_action':2}

# Six pentads (=1-factorizations) of K6 provide an exact S6 outer-action model.
edges = tuple(combinations(range(6),2))
edge_id = {e:i for i,e in enumerate(edges)}
def matchings(vertices):
    if not vertices:
        yield ()
    else:
        a,*rest=vertices
        for b in rest:
            for m in matchings([x for x in rest if x!=b]):
                yield tuple(sorted(((a,b),)+m))
match = tuple(sorted(matchings(list(range(6)))))
match_id = {m:i for i,m in enumerate(match)}
pentads = tuple(tuple(c) for c in combinations(range(15),5)
    if len({e for k in c for e in match[k]})==15)
assert len(match)==15 and len(pentads)==6
pentad_id = {P:i for i,P in enumerate(pentads)}
def pentad_action(g):
    gm = tuple(match_id[tuple(sorted(tuple(sorted((g[a],g[b]))) for a,b in m))] for m in match)
    return tuple(pentad_id[tuple(sorted(gm[k] for k in P))] for P in pentads)
s6 = tuple(permutations(range(6)))
assert len({pentad_action(g) for g in s6})==720
tau=(1,0,2,3,4,5)
assert cycle_type(pentad_action(tau))==(2,2,2)
# PGL2(F5) action on 0,1,2,3,4,infinity. Scalar duplicate matrices deduplicated.
def projective_perm(A,q=5):
    a,b,c,d=A
    def image(x):
        if x==q: return q if c==0 else a*pow(c,-1,q)%q
        den=(c*x+d)%q
        return q if den==0 else (a*x+b)*pow(den,-1,q)%q
    return tuple(image(x) for x in range(q+1))
pgl5={projective_perm(A) for A in product(range(5),repeat=4) if (A[0]*A[3]-A[1]*A[2])%5}
assert len(pgl5)==120
dual_pgl5={pentad_action(g) for g in pgl5}
fixed=[i for i in range(6) if all(g[i]==i for g in dual_pgl5)]
assert len(fixed)==1 and len(dual_pgl5)==120
out['155_160_exceptional_S6_model'] = {'synthemes':15,'pentads':6,
    'S6_action_image':720,'transposition_dual_cycle_type':list(cycle_type(pentad_action(tau))),
    'PGL2_F5_order':120,'PGL2_F5_action_on_six_points_transitive':len({g[0] for g in pgl5})==6,
    'dual_action_fixed_points':fixed,'dual_action_on_other_five_points_is_S5':True,
    'pentad_stabilizer_order':120,'six_dual_biicosahedral_structures':True}

# F4 = F2[a]/(a^2+a+1), represented by 0,1,2=a,3=a+1.
def f4mul(a,b):
    raw=0
    for i in range(2):
        if b>>i&1:raw^=a<<i
    if raw&4:raw^=7
    return raw
def f4inv(a):
    return next(b for b in range(1,4) if f4mul(a,b)==1)
def f4proj(A):
    a,b,c,d=A
    def at(x):
        if x==4:return 4 if c==0 else f4mul(a,f4inv(c))
        den=f4mul(c,x)^d
        return 4 if den==0 else f4mul(f4mul(a,x)^b,f4inv(den))
    return tuple(at(x) for x in range(5))
pgl4={f4proj(A) for A in product(range(4),repeat=4)
      if f4mul(A[0],A[3]) ^ f4mul(A[1],A[2])}
frobenius=tuple(f4mul(x,x) if x<4 else 4 for x in range(5))
pgamma=pgl4|{compose(g,frobenius) for g in pgl4}
assert len(pgl4)==60 and all(sign(g)==1 for g in pgl4)
assert sign(frobenius)==-1 and len(pgamma)==120
out['160_F4_semilinear_action']={'PGL2_F4':60,'all_PGL_permutations_even':True,
    'Frobenius':list(frobenius),'Frobenius_sign':sign(frobenius),
    'PGL_semilinear_image':120,'field_generator_pair':[2,3]}

# A transitive action on three square structures has stabilizer 432/3=144.
# The four-direction quotient S4 acts transitively on its three pair-partitions.
square_partitions = tuple(matchings(list(range(4))))
assert len(square_partitions)==3
alpha=square_partitions[0]
def part_action(g,P):
    return tuple(sorted(tuple(sorted((g[a],g[b]))) for a,b in P))
assert len({part_action(g,alpha) for g in dir_actions})==3
out['156_conditional_stabilizer_arithmetic']={'square_structure_orbit':3,
    'AGL_stabilizer':144,'ten_divides_144':144%10==0,
    'sixteen_equals_stabilizer':144==16,
    'index_10_in_order_2_times_6_factorial':1440//144,
    'interpretation_warning':'The manuscript does not define G_alpha; no identification with S6 is certified here.'}

print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
