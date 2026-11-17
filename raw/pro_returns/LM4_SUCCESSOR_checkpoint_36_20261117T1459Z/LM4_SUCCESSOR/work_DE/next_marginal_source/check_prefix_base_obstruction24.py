#!/usr/bin/env python3
"""Independent whole-regional semidirect quotient and prefix obstruction.

No producer imports and no finite-group enumeration.  The only permutation
cases are the three transpositions specified by the uniform proof.
"""
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
SOURCE=ROOT/'work_CE/next_symmetric_nodes/annular_neck_presentation23.json'
D=json.loads(SOURCE.read_text())
IDP=(0,1,2)
ONE=(frozenset(),IDP)
C=(0,2,1)
K=(1,0,2)
def pc(p,q): return tuple(p[q[i]] for i in range(3))
def pi(p): return tuple(p.index(i) for i in range(3))
def act(p,v): return frozenset((family,p[point]) for family,point in v)
def mul(x,y): return (x[0]^act(x[1],y[0]),pc(x[1],y[1]))
def inverse(x):
    p=pi(x[1]); return (act(p,x[0]),p)
def word(w,images):
    z=ONE
    for a in w: z=mul(z,images[a] if a>0 else inverse(images[-a]))
    return z
def record(x):
    return {'lamps':[[family,point+1] for family,point in sorted(x[0])],
            'permutation_images':[i+1 for i in x[1]]}
def red(w):
    s=[]
    for x in w:
        if s and s[-1]==-x:s.pop()
        else:s.append(x)
    return tuple(s)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(x for a in w for x in (A[a] if a>0 else inv(A[-a])))

# Actual global labels: a,B=bar b,d,e,f,Cminus,Cplus,kminus,kplus.
# Only the certified minus vertex is used.  B is the b-family lamp at2.
images={1:(frozenset({('a',2)}),IDP),2:(frozenset({('b',1)}),IDP),
        3:(frozenset({('d',2)}),IDP),4:(frozenset({('e',2)}),IDP),
        5:(frozenset(),pc(C,K)),6:(frozenset(),C),8:(frozenset(),K)}
actual=D['local_Y_h_maps']['minus']
local={int(i):word(w,images) for i,w in actual.items()}
for label,j in [('a',1),('b',2),('d',5),('e',6)]:
    assert local[j]==(frozenset({(label,2)}),IDP)
assert local[3]==(frozenset(),C)
assert local[4]==images[5] and local[7]==(frozenset(),C)
assert mul(local[3],local[7])==ONE # z=C h
rels=[(r['name'],tuple(r['word'])) for r in D['regional_relators'] if r['side']=='minus']
assert len(rels)==16
rels.append(('cone_square',(6,6)))
results=[]
for name,w in rels:
    value=word(w,images); assert value==ONE,(name,record(value))
    results.append({'name':name,'actual_stored_word':w,'value':record(value)})

# These are the actual geometric characters, not inferred from the target:
# only C is odd for the ordinary two-cover, and only k winds the q0 base.
epsilon={j:int(j==6) for j in images}
base={j:int(j==8) for j in images}
def parity(p):return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
for j,x in images.items():assert parity(x[1])==(epsilon[j]+base[j])%2
for name,w in rels:
    assert sum(epsilon[abs(j)] for j in w)%2==0
    assert sum((1 if j>0 else -1)*base[abs(j)] for j in w)==0

# Reconstruct the actual triangular prefix automorphism in the full K basis.
OinK={1:(1,2,-1),2:(1,),3:(5,3,4,-3,-5),4:(3,),5:(-3,5,3)}
KinO={1:(2,),2:(-2,1,2),3:(4,),4:(-5,-4,3,4,5),5:(4,5,-4)}
prefix={j:tuple(range(1,j+1)) for j in range(1,6)}
prefix_inverse={1:(1,),**{j:(-(j-1),j) for j in range(2,6)}}
for j in range(1,6):
    assert sub(prefix[j],prefix_inverse)==sub(prefix_inverse[j],prefix)==(j,)
    assert sub(OinK[j],KinO)==sub(KinO[j],OinK)==(j,)
theta={j:sub(sub(KinO[j],prefix),OinK) for j in range(1,6)}
theta_inverse={j:sub(sub(KinO[j],prefix_inverse),OinK) for j in range(1,6)}
for j in range(1,6):assert sub(theta[j],theta_inverse)==sub(theta_inverse[j],theta)==(j,)
assert theta[1]==(1,2)
v=word(theta[1],images)
assert v==(frozenset({('a',2),('b',1)}),IDP)
transpositions=[]
for i,j in [(0,1),(0,2),(1,2)]:
    p=list(IDP);p[i],p[j]=p[j],p[i];p=tuple(p)
    moved=act(p,v[0]);assert moved!=v[0]
    transpositions.append({'permutation_images':[k+1 for k in p],
       'conjugated_lamps':record((moved,IDP))['lamps'],
       'nonzero_commutator_lamps':record((moved^v[0],IDP))['lamps']})

out={'status':'PASS_ALL_17_ACTUAL_REGIONAL_RELATIONS_AND_LITERAL_PREFIX',
 'actual_input':str(SOURCE.relative_to(ROOT)),
 'actual_input_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
 'group':'(F_2)^(4x3) semidirect S3, S3 acts on positions within each named family',
 'global_generator_images':{str(j):record(x) for j,x in images.items()},
 'all_regional_checks':results,'theta_K_images':theta,'theta_K_inverse_images':theta_inverse,
 'theta_a_literal_word':theta[1],'theta_a_image':record(v),
 'three_transposition_cases':transpositions,
 'symbolic_all_translation_identity':'(m,p)(v,1)(m,p)^-1=(p.v,1); m cancels for every lamp vector.',
 'stronger_exact_stabilizer':'If p fixes the a-family lamp at3 and b-family lamp at2, p fixes2 and3 separately, hence p=1. Therefore the target centralizer of theta(a) is the full lamp subgroup.',
 'actual_geometric_characters':{'ordinary_orientation':epsilon,'base_q0_winding':base,
    'identity':'permutation_sign = ordinary_orientation + base_q0_winding modulo2',
    'consequence':'Every ordinary element of odd base winding maps to a transposition and cannot centralize theta(a).'},
 'scope':'Rules out any regional extension of the literal prefix map sending k to an ordinary element of odd q0 winding, including every genuine alternative degree+1 or-1 base section. Arbitrary retained-fiber and graph-kernel corrections do not evade this character obstruction. This does not rule out a new regional presentation with transformed relations or identify the actual post-cross-quotient centralizer.'}
(HERE/'prefix_base_obstruction_independent24.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all17 actual regional relations, including cone square.')
print('PASS literal theta(a)=aB and both directions of all5 prefix K images.')
print('PASS all3 transposition supports; symbolic cancellation covers every lamp correction.')
print('Target centralizer of theta(a) is exactly the lamp subgroup; no target enumeration.')
print('PASS actual parity=ordinary orientation+base winding; every ordinary odd-degree base section excluded.')
