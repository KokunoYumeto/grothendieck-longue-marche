"""Exact rigid restrictions of the common-base cyclic source.

Exploration only: finite images, not a completed-kernel identification.
Projectivized homology of the double cover branched at the retained six
finite points gives a quotient of the seven-point sphere target.
"""
from pathlib import Path
import json,itertools,time
import numpy as np
import sympy as sp
from sympy.combinatorics import Permutation, PermutationGroup

HERE=Path(__file__).resolve().parent
DATA=json.loads((HERE.parent/'next_B59_image/common_base_braid_words.json').read_text())
INITIAL=DATA['initial_order_labels']
SETS={'plus':[1,2,4,5,6,10,11], 'minus':[2,3,4,7,10,11,12]}
labels=json.loads((HERE.parent/'rigid7_subsets.json').read_text())
D=labels['D_permutation'];allsets={tuple(x) for x in labels['rigid7']}
def dimage(S):return tuple(sorted(D[i-1]+1 for i in S))
orbits=[];left=set(allsets)
while left:
    s=min(left);orb={s};t=dimage(s)
    while t!=s:orb.add(t);t=dimage(t)
    orbits.append(sorted(orb));left-=orb
assert sorted(map(len,orbits))==[1,1,5,5]
assert [1,2,3,4,6,9,12] in labels['rigid7']
assert [1,3,5,7,8,10,11] in labels['rigid7']
for S in SETS.values():assert len(next(o for o in orbits if tuple(S) in o))==5
assert next(o for o in orbits if tuple(SETS['plus']) in o)!=next(o for o in orbits if tuple(SETS['minus']) in o)
print('chosen D orbit sizes on all twelve rigid sets:',sorted(map(len,orbits)),flush=True)
print('two selected NON-D-stable representatives cover the two size-five orbits',flush=True)

def project(word,subset):
    keep=set(subset)-{2};order=INITIAL[:];out=[]
    for a in word:
        k=abs(a)-1
        if order[k] in keep and order[k+1] in keep:
            j=sum(x in keep for x in order[:k])+1
            out.append(j if a>0 else -j)
        order[k],order[k+1]=order[k+1],order[k]
    assert order==INITIAL
    return out

n=6;d=4;p=3
eps=np.array([1,-1,1,-1,1,-1],dtype=np.int64)
inc=np.vstack([np.eye(d,dtype=np.int64),-eps[:d],np.zeros(d,dtype=np.int64)])
J=np.array([[0 if i==j else ((-1)**(j-i+1) if i<j else -(-1)**(i-j+1)) for j in range(d)] for i in range(d)],dtype=np.int64)
assert sp.Matrix(J).det()==1
gens={};integral_gens={}
for j in range(1,n):
    B=np.eye(n,dtype=np.int64);B[j-1:j+1,j-1:j+1]=[[2,-1],[1,0]]
    Y=B@inc;M=Y[:d]-Y[-1]
    assert np.array_equal(M.T@J@M,J)
    integral_gens[j]=M
    gens[j]=M%p
    gens[-j]=np.asarray(sp.Matrix(M).inv()).astype(np.int64)%p

def evalword(word):
    M=np.eye(d,dtype=np.int64)
    for a in word:M=M@gens[a]%p
    return M
assert np.array_equal(evalword(list(range(1,n))*n),np.eye(d,dtype=np.int64))
spherical=evalword(list(range(1,n))+list(range(n-1,0,-1)))
assert np.array_equal(spherical,2*np.eye(d,dtype=np.int64))
for j in range(1,n-1):
    assert np.array_equal(gens[j]@gens[j+1]@gens[j]%p,gens[j+1]@gens[j]@gens[j+1]%p)
for j in range(1,n):
    for k in range(j+2,n):assert np.array_equal(gens[j]@gens[k]%p,gens[k]@gens[j]%p)

def normal(v):
    v=[int(x)%3 for x in v]
    z=next(x for x in v if x)
    return tuple(int(x*z%3) for x in v)
points=sorted({normal(v) for v in itertools.product(range(3),repeat=4) if any(v)})
assert len(points)==40
point_index={x:i for i,x in enumerate(points)}
def perm(M):return Permutation([point_index[normal(M@np.array(x))] for x in points])

records={};pgens={}
for name,S in SETS.items():
    records[name]={};pgens[name]=[]
    for i,w in sorted(DATA['C5'].items(),key=lambda x:int(x[0])):
        v=project(w,S);M=evalword(v);P=perm(M)
        records[name][i]={'braid':v,'matrix':M.tolist(),'permutation':P.array_form}
        pgens[name].append(P)
    G=PermutationGroup(pgens[name]);order=G.order()
    print(name,'projective image order',order,'source braid lengths',[len(x['braid']) for x in records[name].values()],flush=True)
    print(name,'derived subgroup order',G.derived_subgroup().order(),flush=True)
joint=[]
for a,b in zip(pgens['plus'],pgens['minus']):joint.append(Permutation(a.array_form+[x+40 for x in b.array_form]))
G=PermutationGroup(joint)
print('joint rigid image order',G.order(),flush=True)
print('joint derived order',G.derived_subgroup().order(),flush=True)
(HERE/'rigid_restrictions.json').write_text(json.dumps({'subsets':SETS,'D_orbits':orbits,'initial_order':INITIAL,'projective_points':points,'families':records,'joint_order':int(G.order()),'joint_derived_order':int(G.derived_subgroup().order())},indent=2)+'\n')
print('PASS exact braid deletion; integral symplectic form; full twist killed; spherical relation is-I; finite joint images computed')
