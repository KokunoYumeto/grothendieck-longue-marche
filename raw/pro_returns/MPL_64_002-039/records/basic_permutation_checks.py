#!/usr/bin/env python3
"""Exact finite certificates for research notes on cote64/003--025.

No scan processing and no transcription mutation. Standard-library integers only.
"""
from itertools import permutations, product, combinations
from collections import Counter
from pathlib import Path
import csv, json

OUT=Path(__file__).resolve().parent
E=(0,1,2,3)
G=set(permutations(range(4)))
def mul(a,b): return tuple(a[b[i]] for i in range(4))
def inv(a): return tuple(a.index(i) for i in range(4))
def powp(a,n):
    r=E
    for _ in range(n):r=mul(r,a)
    return r
def order(a):
    r=a;n=1
    while r!=E:r=mul(r,a);n+=1
    return n
def cyc(a):
    seen=set();out=[]
    for i in range(4):
        if i in seen:continue
        x=i;c=[]
        while x not in seen:seen.add(x);c.append(x+1);x=a[x]
        if len(c)>1:out.append('('+''.join(map(str,c))+')')
    return ''.join(out) or '1'
def closure(gs):
    gs=set(gs)|{inv(g) for g in gs};h={E};todo=[E]
    while todo:
        x=todo.pop()
        for g in gs:
            y=mul(x,g)
            if y not in h:h.add(y);todo.append(y)
    return frozenset(h)
def conjugate(h,g):return frozenset(mul(mul(g,x),inv(g)) for x in h)
def cent(xs):return frozenset(g for g in G if all(mul(g,x)==mul(x,g) for x in xs))
def normalizer(h):return frozenset(g for g in G if conjugate(h,g)==h)
def normal(h):return len(normalizer(h))==24
V=frozenset(g for g in G if g==E or (order(g)==2 and all(g[i]!=i for i in range(4))))
def kind(h):
    n=len(h)
    if n==1:return '1'
    if n==2:return 'C2_double' if h<=V else 'C2_transposition'
    if n==3:return 'C3'
    if n==4:
        if any(order(g)==4 for g in h):return 'C4'
        return 'V4_normal' if h==V else 'V4_nonnormal'
    return {6:'S3',8:'D8',12:'A4',24:'S4'}[n]
subgroups={frozenset({E})};todo=list(subgroups)
while todo:
    h=todo.pop()
    for g in G-h:
        k=closure(set(h)|{g})
        if k not in subgroups:subgroups.add(k);todo.append(k)
subs=sorted(subgroups,key=lambda h:(len(h),kind(h),sorted(h)))
ids={h:f'H{i:02}' for i,h in enumerate(subs,1)}
classes=[];unseen=set(subs)
while unseen:
    h=min(unseen,key=lambda q:(len(q),kind(q),sorted(q)))
    orbit={conjugate(h,g) for g in G};unseen-=orbit
    classes.append({'type':kind(h),'order':len(h),'subgroup_count':len(orbit),'homogeneous_cardinality':24//len(h)})
covers=[(h,k) for h in subs for k in subs if h<k and not any(h<m<k for m in subs)]
with (OUT/'s4_subgroups.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['id','type','order','index','normalizer_order','elements'])
    for h in subs:w.writerow([ids[h],kind(h),len(h),24//len(h),len(normalizer(h)),' '.join(sorted(map(cyc,h)))])
with (OUT/'s4_hasse_edges.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['lower','upper','relative_index'])
    for h,k in covers:w.writerow([ids[h],ids[k],len(k)//len(h)])

# Coxeter presentation: involutions t1,t2,t3, adjacent products order3,
# distant generators commute, and images generate S4.
involutions=[g for g in G if order(g)==2]
automorphism_triples=[]
for a,b,c in product(involutions,repeat=3):
    if order(mul(a,b))==order(mul(b,c))==3 and mul(a,c)==mul(c,a) and len(closure([a,b,c]))==24:
        automorphism_triples.append((a,b,c))
assert len(automorphism_triples)==24
assert len(cent(G))==1 and cent(V)==V

r=(1,2,3,0);s=(0,3,2,1);D=closure([r,s]);z=powp(r,2)
reflections=sorted(g for g in D if order(g)==2 and g!=z)
autD=[]
for rr,ss in product(D,repeat=2):
    if order(rr)!=4 or order(ss)!=2 or mul(mul(ss,rr),ss)!=inv(rr):continue
    if len(closure([rr,ss]))!=8:continue
    m={mul(powp(r,i),powp(s,j)):mul(powp(rr,i),powp(ss,j)) for i in range(4) for j in range(2)}
    assert len(m)==8 and all(m[mul(a,b)]==mul(m[a],m[b]) for a in D for b in D)
    autD.append(m)
reflection_actions={tuple(reflections.index(m[x]) for x in reflections) for m in autD}
assert len(autD)==len(reflection_actions)==8
assert len(cent(D)&D)==2
c=(1,0,3,2);d=(0,3,2,1)
orientation_products={'r_c_d_usual':cyc(mul(mul(r,c),d)),'d_c_r_usual':cyc(mul(mul(d,c),r)),'antipodism':cyc(z)}

# Orientation-preserving signed coordinate permutations of the cube.
verts=list(product((-1,1),repeat=3))
neg=lambda v:tuple(-x for x in v)
body=sorted({tuple(sorted([v,neg(v)])) for v in verts})
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
rotations=[(p,t) for p in permutations(range(3)) for t in product((-1,1),repeat=3) if parity(p)*t[0]*t[1]*t[2]==1]
def action(q,v):p,t=q;return tuple(t[i]*v[p[i]] for i in range(3))
def applyset(q,x):return tuple(sorted(action(q,v) for v in x))
def cubeperm(q):return tuple(body.index(applyset(q,b)) for b in body)
assert {cubeperm(q) for q in rotations}==G
edges=sorted(tuple(sorted([v,w])) for v,w in combinations(verts,2) if sum(a!=b for a,b in zip(v,w))==1)
faces=sorted(tuple(v for v in verts if v[i]==t) for i in range(3) for t in (-1,1))
opposite_edges=sorted({tuple(sorted([e,tuple(sorted(neg(v) for v in e))])) for e in edges})
opposite_faces=sorted({tuple(sorted([f,tuple(sorted(neg(v) for v in f))])) for f in faces})
face_diagonals=sorted(tuple(sorted([v,w])) for v,w in combinations(verts,2) if sum(a!=b for a,b in zip(v,w))==2)
tetrahedra=[tuple(v for v in verts if v[0]*v[1]*v[2]==t) for t in (-1,1)]
directed_edges=[(v,w) for v in verts for w in verts if sum(a!=b for a,b in zip(v,w))==1]
def nested(q,x):return tuple(sorted(applyset(q,y) for y in x))
objects=[
 ('vertices',verts,action),('edges',edges,applyset),('faces',faces,applyset),
 ('body_diagonals',body,applyset),('opposite_edge_pairs',opposite_edges,nested),
 ('opposite_face_pairs',opposite_faces,nested),
 ('directed_edges',directed_edges,lambda q,x:tuple(action(q,v) for v in x)),
 ('inscribed_tetrahedra',tetrahedra,applyset),('face_diagonals',face_diagonals,applyset),
 ('ordered_distinct_axes',list(permutations(range(3),2)),lambda q,x:tuple(q[0].index(i) for i in x))]
cube=[]
for name,xs,act in objects:
    x=xs[0];orbit={act(q,x) for q in rotations}
    h=frozenset(cubeperm(q) for q in rotations if act(q,x)==x)
    assert len(orbit)==len(xs) and len(xs)*len(h)==24
    cube.append({'object':name,'cardinality':len(xs),'stabilizer_type':kind(h),'stabilizer_order':len(h)})

# Three partitions into pairs, their product, and the four-element fibre.
parts=sorted({tuple(sorted([tuple(A),tuple(i for i in range(4) if i not in A)])) for A in combinations(range(4),2)})
embedding=[tuple(next(j for j,b in enumerate(p) if i in b) for p in parts) for i in range(4)]
parities={sum(e)%2 for e in embedding}
assert len(set(embedding))==4 and len(parities)==1

# Orientation of the two inequivalent six-point S4-covers of J.
# For three antipodal pairs, orientation = sign(on six faces)*sign(on pairs).
def sign_tuple(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
cycles=sorted(g for g in G if order(g)==4)
pairs2=sorted(combinations(range(4),2))
js=sorted(V-{E});cover_checks=[]
for g in sorted(G):
    jp=tuple(js.index(mul(mul(g,x),inv(g))) for x in js)
    cp=tuple(cycles.index(mul(mul(g,x),inv(g))) for x in cycles)
    pp=tuple(pairs2.index(tuple(sorted(g[i] for i in x))) for x in pairs2)
    oc=sign_tuple(cp)*sign_tuple(jp)
    op=sign_tuple(pp)*sign_tuple(jp)
    assert oc==1 and op==sign_tuple(g)
    cover_checks.append({'g':cyc(g),'circular_cover_orientation':oc,'two_subset_cover_orientation':op,'sign_on_I':sign_tuple(g)})

# Central D8 extension of C2^2. Section u^a v^b with u,v involutions.
u=s;v=mul(r,s)
section=lambda a,b:mul(powp(u,a),powp(v,b))
for a,b,aa,bb in product(range(2),repeat=4):
    lhs=mul(section(a,b),section(aa,bb))
    rhs=mul(powp(z,b*aa),section((a+aa)%2,(b+bb)%2))
    assert lhs==rhs

report={
 'method':'Exhaustive standard-library permutation enumeration; no OCR or manuscript edits.',
 'S4_order':len(G),'S4_automorphisms_via_Coxeter_generators':len(automorphism_triples),
 'subgroup_count':len(subs),'conjugacy_class_count':len(classes),'conjugacy_classes':classes,
 'hasse_cover_count':len(covers),'V_centralizer_order':len(cent(V)),'V_normalizer_order':len(normalizer(V)),
 'double_transposition_centralizers':[{'element':cyc(x),'order':len(cent([x])),'type':kind(cent([x]))} for x in sorted(V-{E})],
 'cyclic4_count':sum(kind(h)=='C4' for h in subs),'sylow3_count':sum(len(h)==3 for h in subs),
 'D8_order':len(D),'D8_automorphisms':len(autD),'D8_reflection_action_order':len(reflection_actions),
 'D8_inner_map_kernel_order':len(cent(D)&D),'D8_noncentral_involutions':list(map(cyc,reflections)),
 'orientation_product_convention':orientation_products,
 'cube_rotations_order':len(rotations),'cube_full_signed_permutation_order':48,'cube_homogeneous_spaces':cube,
 'four_set_to_pair_partition_product':{'partitions':parts,'image':embedding,'image_sum_mod2':list(parities),'product_size':8,'contracted_product_size':2},
 'two_six_point_covers_orientation':cover_checks,
 'D8_central_extension_cocycle':{'section':'u^a v^b; u=s, v=r*s','value':'z^(b*a_prime)','cases_checked':16,'cohomology_class':'beta cup alpha = alpha cup beta in H^2(-,F2)'},
 'literal_presentation_scan017_countermodel':'Map every generator x in S to 1 in additive Z and a to 0. Every displayed commutator relation holds, and the image is infinite cyclic. Thus the displayed relations alone do not present D8.',
}
(OUT/'basic_permutation_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['subgroup_count','conjugacy_class_count','hasse_cover_count','S4_automorphisms_via_Coxeter_generators','D8_automorphisms','orientation_product_convention','cube_homogeneous_spaces']},indent=2))
