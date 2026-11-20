"""Exact finite checks for scan016's contracted-product assertions and qualifications."""
from itertools import permutations,product
from fractions import Fraction
from pathlib import Path
import json

o=Path(__file__).resolve().parents[1]
S3=list(permutations(range(3)));one=(0,1,2)
def mul(p,q):return tuple(p[q[i]] for i in range(3))
def inv(p):return tuple(p.index(i) for i in range(3))
def sign(p):return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2

def balanced(group,identity,multiply,inverse,E,rho):
    pairs=list(product(group,E));todo=set(pairs);classes=[];which={}
    while todo:
        p,e=min(todo);orb={(multiply(p,g),rho(inverse(g),e)) for g in group}
        assert orb<=set(pairs)
        idx=len(classes)
        for a in orb:which[a]=idx
        todo-=orb;classes.append(sorted(orb))
    for p,e in pairs:
        for g in group:assert which[multiply(p,g),e]==which[p,rho(g,e)]
    return classes,which

def run_case(name,G,identity,multiply,inverse,E,rho):
    classes,which=balanced(G,identity,multiply,inverse,E,rho)
    phi={p:tuple(which[p,e] for e in E) for p in G}
    B=list(permutations(range(len(classes))))
    kernel={g for g in G if all(rho(g,e)==e for e in E)}
    for p in G:assert sorted(phi[p])==list(range(len(classes)))
    for p,g in product(G,G):assert phi[multiply(p,g)]==tuple(phi[p][rho(g,e)] for e in E)
    stab_sizes=[]
    for b in B:
        stabilizer={g for g in G if tuple(b[rho(g,e)] for e in E)==b}
        assert stabilizer==kernel
        stab_sizes.append(len(stabilizer))
    fibers=[sum(phi[p]==b for p in G) for b in set(phi.values())]
    assert all(k==len(kernel) for k in fibers)
    assert (len(set(phi.values()))==len(G))==(len(kernel)==1)
    return {'case':name,'group_order':len(G),'E_size':len(E),'F_size':len(classes),'Bij_size':len(B),'kernel_size':len(kernel),'image_orbit_size':len(set(phi.values())),'fiber_sizes':fibers,'stabilizer_sizes':stab_sizes,'equivariance_checks':len(G)**2,'balanced_relation_checks':len(G)**2*len(E)},which

cases=[]
a,_=run_case('S3 natural faithful action',S3,one,mul,inv,list(range(3)),lambda g,e:g[e]);cases.append(a)
a,src=run_case('S3 sign action',S3,one,mul,inv,[0,1],lambda g,e:sign(g)^e);cases.append(a)
a,_=run_case('S3 action on empty set',S3,one,mul,inv,[],lambda g,e:e);cases.append(a)
a,_=run_case('Trivial group action on empty set',[one],one,mul,inv,[],lambda g,e:e);cases.append(a)
H=[0,1];hmul=lambda a,b:a^b
target,tgt=balanced(H,0,hmul,lambda g:g,[0,1],hmul)
induced={}
for (p,e),c in src.items():induced.setdefault(c,set()).add(tgt[sign(p),e])
assert all(len(v)==1 for v in induced.values())
assert len({next(iter(v)) for v in induced.values()})==2
assert all(sign(mul(p,q))==hmul(sign(p),sign(q)) for p,q in product(S3,S3))

rectangle=[(-2,-1),(2,-1),(2,1),(-2,1)]
rhombus=[(-2,0),(0,1),(2,0),(0,-1)]
square=[(-1,-1),(1,-1),(1,1),(-1,1)]
diamond=[(0,-1),(1,0),(0,1),(-1,0)]
def edges(v):return [(v[(i+1)%len(v)][0]-p[0],v[(i+1)%len(v)][1]-p[1]) for i,p in enumerate(v)]
def lengths(v):return [x*x+y*y for x,y in edges(v)]
def dots(v):
    e=edges(v);return [e[i][0]*e[(i+1)%len(e)][0]+e[i][1]*e[(i+1)%len(e)][1] for i in range(len(e))]
def reflect(p,s,t):return (s*p[0],t*p[1])
rect_orbit={reflect(rectangle[0],s,t) for s,t in product([-1,1],repeat=2)}
assert rect_orbit==set(rectangle)
assert lengths(rectangle)==[16,4,16,4] and dots(rectangle)==[0]*4
assert lengths(rhombus)==[5]*4 and len(set(dots(rhombus)))==2
edge_orbit={frozenset((reflect(rhombus[0],s,t),reflect(rhombus[1],s,t))) for s,t in product([-1,1],repeat=2)}
assert edge_orbit=={frozenset((p,rhombus[(i+1)%4])) for i,p in enumerate(rhombus)}
def rotate_scale(p):return (Fraction(p[0]-p[1],2),Fraction(p[0]+p[1],2))
assert [rotate_scale(p) for p in square]==diamond
assert any(y==0 and x!=0 for x,y in edges(square))
assert all(y!=0 for x,y in edges(diamond))

cert={'passed':True,'cases':cases,'noninjective_group_map_functoriality':{'source':'S3 sign action','target':'C2 regular action','group_homomorphism_checks':36,'source_classes':len(induced),'target_classes':len(target),'induced_map_well_defined':True,'induced_map_bijective':True},'geometry':{'rectangle':rectangle,'rectangle_squared_edge_lengths':lengths(rectangle),'rectangle_consecutive_dots':dots(rectangle),'rectangle_vertex_orbit_size':len(rect_orbit),'rhombus':rhombus,'rhombus_squared_edge_lengths':lengths(rhombus),'rhombus_consecutive_dots':dots(rhombus),'rhombus_edge_orbit_size':len(edge_orbit),'square':square,'diamond':diamond,'similarity_matrix':[['1/2','-1/2'],['1/2','1/2']],'no_homothety_reason':'A horizontal boundary edge of the square must remain horizontal under a nonzero scalar affine map; the diamond has no horizontal boundary edge.'}}
(o/'decisions/scan016_finite_certificate.json').write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(cert,ensure_ascii=False))
