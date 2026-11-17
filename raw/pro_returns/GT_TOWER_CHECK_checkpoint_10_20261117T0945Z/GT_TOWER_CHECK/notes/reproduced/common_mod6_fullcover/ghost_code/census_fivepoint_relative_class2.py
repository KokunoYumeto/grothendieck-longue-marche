#!/usr/bin/env python3
"""Complete finite class-two pentagon/gentle census and capped CM defect.

Records are literal elements of the derived image of the free source.
The program does not claim that a surviving record is the image of an
actual profinite gentle automorphism.
"""
from pathlib import Path
from itertools import product
from collections import deque
import json
import numpy as np
from fivepoint_relative_tools import inverse, subst

HERE=Path(__file__).resolve().parent
target=np.load(HERE/'build_fivepoint_relative_class2.npz')
maps=np.load(HERE/'test_fivepoint_relative_class2_maps.npz')
description=json.loads((HERE/'test_fivepoint_relative_class2_maps.json').read_text())
loops=[tuple(w) for w in description['source_loop_words']]
M=maps['mapped_linear'].astype(np.int64)
N=maps['mapped_central'].astype(np.int64)
B=maps['bracket_maps'].astype(np.int64)
U=maps['source_linear_basis'].astype(np.int64)
assert U.shape==(4,17)
upper=np.triu_indices(80,1)
source_upper=np.triu_indices(17,1)
central_basis=target['central_basis'].astype(np.int16)
central_pivots=target['central_pivots'].astype(int)
central_free=np.array([i for i in range(3160) if i not in set(central_pivots)],dtype=int)


def central_reduce(rows):
    rows=np.array(rows,dtype=np.int16).copy()%3
    for p,b in zip(central_pivots,central_basis):
        ix=np.flatnonzero(rows[:,p])
        if len(ix):rows[ix]=(rows[ix]-rows[ix,p,None]*b)%3
    assert not np.any(rows[:,central_pivots])
    return rows[:,central_free]


patterns=[((4,1),(5,1)),((6,1),(7,1),(4,1)),
          ((0,1),(1,1),(4,-1),(3,-1),(2,-1))]
coefficient_cases=np.array(list(product(range(3),repeat=4)),dtype=np.int64)
u_cases=coefficient_cases@U%3
quadratics=[]
for u in u_cases:
    values=np.einsum('i,kij->kj',u,M)%3
    case=[]
    for pattern in patterns:
        acc=np.zeros(80,dtype=np.int64)
        q=np.zeros((80,80),dtype=np.int64)
        for i,sign in pattern:
            v=sign*values[i]
            q+=2*(np.outer(acc,v)-np.outer(v,acc))
            acc+=v
        assert not np.any(acc%3)
        case.append(q[upper]%3)
    quadratics.append(case)
quadratics=central_reduce(np.array(quadratics).reshape(-1,3160)).reshape(81,3,1429)
linear_w=np.concatenate([sum(sign*B[i] for i,sign in p).T%3 for p in patterns])
linear_u=np.concatenate([sum(sign*N[i] for i,sign in p).T%3 for p in patterns])
rhs=(-linear_u@u_cases.T-quadratics.reshape(81,-1).T)%3
assert linear_w.shape==(4287,136) and rhs.shape==(4287,81)
aug=np.concatenate([linear_w,rhs],axis=1).astype(np.int16)
r=0;pivots=[]
for col in range(136):
    nz=np.flatnonzero(aug[r:,col])
    if not len(nz):continue
    row=r+int(nz[0]);aug[[r,row]]=aug[[row,r]]
    aug[r]=aug[r]*pow(int(aug[r,col]),-1,3)%3
    ix=np.flatnonzero(aug[:,col]);ix=ix[ix!=r]
    if len(ix):aug[ix]=(aug[ix]-aug[ix,col,None]*aug[r])%3
    pivots.append(col);r+=1
    if r%32==0:print('Reduced central-variable pivots',r,flush=True)
consistent=np.all(aug[r:,136:]==0,axis=0)
free=[i for i in range(136) if i not in pivots]
kernel=np.zeros((len(free),136),dtype=np.int64)
kernel[:,free]=np.eye(len(free),dtype=np.int64)
kernel[:,pivots]=-aug[:r,free].T%3
assert not np.any(linear_w@kernel.T%3)
particular=np.zeros((81,136),dtype=np.int64)
particular[:,pivots]=aug[:r,136:].T
for i in np.flatnonzero(consistent):
    assert np.array_equal(linear_w@particular[i]%3,rhs[:,i])
print('RESULT central-equation rank/kernel dimension:',r,len(free),flush=True)
print('RESULT consistent first-degree cases:',int(consistent.sum()),'of81',flush=True)

# Rebuild the actual capped216 group, rather than infer a target from an
# abstract Heisenberg presentation.
cap=np.load(HERE/'check_main_mixed_capping.npz')
edges=cap['capped_edges'].astype(int)
words=[None]*216;words[0]=();queue=deque([0])
while queue:
    i=queue.popleft()
    for k in range(2):
        j=int(edges[i,k])
        if words[j] is None:words[j]=words[i]+(k+1,);queue.append(j)
table=np.empty((216,216),dtype=int)
for j,w in enumerate(words):
    col=np.arange(216)
    for k in w:col=edges[col,k-1]
    table[:,j]=col
invs=np.array([np.flatnonzero(table[i]==0)[0] for i in range(216)],dtype=int)
D,V=map(int,edges[0])


def mul(*args):
    x=0
    for y in args:x=int(table[x,y])
    return x


def power(x,n):
    if n<0:return power(int(invs[x]),-n)
    ans=0
    for _ in range(n):ans=mul(ans,x)
    return ans


def eval_word(w,gens):
    return mul(*(gens[i-1] if i>0 else int(invs[gens[-i-1]]) for i in w))


def subgroup(gens):
    seen={0};todo=[0]
    for x in todo:
        for g in gens:
            y=mul(x,g)
            if y not in seen:seen.add(y);todo.append(y)
    return seen


pure=subgroup([power(D,2),V]);assert len(pure)==108
comm=lambda x,y:mul(x,y,invs[x],invs[y])
heis=subgroup({comm(x,y) for x in pure for y in pure})
assert len(heis)==27
HX,HY=next((x,y) for x in sorted(heis) for y in sorted(heis) if comm(x,y)!=0)
HZ=comm(HX,HY)
log={}
for i,j,k in product(range(3),repeat=3):
    element=mul(power(HX,i),power(HY,j),power(HZ,k))
    assert element not in log
    log[element]=np.array([i,j,(k+2*i*j)%3],dtype=np.int64)
assert set(log)==heis
for x,y in product(heis,repeat=2):
    a,b=log[x],log[y]
    expected=(a+b)%3
    expected[2]=(expected[2]+2*(a[0]*b[1]-a[1]*b[0]))%3
    assert np.array_equal(log[mul(x,y)],expected)
assert power(V,4)==0 and power(D,4) in heis
assert all(mul(power(D,4),g)==mul(g,power(D,4)) for g in range(216))

qmaps=[];qbrackets=[]
for gens in ((D,power(V,2)),(power(D,2),V)):
    rows=np.array([log[eval_word(w,gens)] for w in loops],dtype=np.int64)
    qmaps.append(rows)
    qbrackets.append(np.array([rows[i,0]*rows[j,1]-rows[i,1]*rows[j,0]
                              for i,j in zip(*source_upper)],dtype=np.int64)%3)
qmaps=np.array(qmaps);qbrackets=np.array(qbrackets)
c2=[]
for word in loops:
    parity=0;c=0
    for letter in word:
        if abs(letter)==1:parity^=1
        elif parity==0:c+=1 if letter>0 else -1
    assert parity==0
    c2.append(c%3)
c2=np.array(c2,dtype=np.int64)
cm_w=(qbrackets[0]-qbrackets[1])%3
cm_kernel=kernel@cm_w%3
cm_kernel_nonzero=bool(np.any(cm_kernel))
case_records=[]
for index in np.flatnonzero(consistent):
    u=u_cases[index];w=particular[index]
    A=u@qmaps[0]%3;B0=u@qmaps[1]%3
    A[2]=(A[2]+w@qbrackets[0])%3
    B0[2]=(B0[2]+w@qbrackets[1])%3
    coefficient=int(u@c2%3)
    defect=(A-B0-coefficient*log[power(D,4)])%3
    defect[2]=(defect[2]-2*(A[0]*B0[1]-A[1]*B0[0]))%3
    case_records.append({'case_index':int(index),'parameters':coefficient_cases[index].tolist(),
                         'c2':coefficient,'particular_defect':defect.tolist(),
                         'all_central_residues_available':cm_kernel_nonzero,
                         'u':u.tolist(),'w_particular':w.tolist()})
print('RESULT CM variation on the full central solution kernel:',
      sorted(set(map(int,cm_kernel))),flush=True)
print('RESULT particular capped CM defects:',
      sorted({tuple(r['particular_defect']) for r in case_records}),flush=True)
print('PASS all target multiplication laws, exact derived-source constraints, and every81-case consistency test',flush=True)
np.savez_compressed(HERE/'census_fivepoint_relative_class2.npz',
                    linear_w=linear_w,linear_u=linear_u,rhs=rhs,
                    central_kernel=kernel,particular=particular,consistent=consistent,
                    u_cases=u_cases,qmaps=qmaps,qbrackets=qbrackets,c2=c2,
                    cm_w=cm_w,cm_kernel=cm_kernel)
output={'source':'Actual derived image in F2/(gamma3(J2)J2^3), with J2=ker(F2->C4^2)',
        'target':'Gamma_0,5/(gamma3(J)J^3), J=ker(Gamma_0,5->C4^5)',
        'first_degree_cases':81,'consistent_cases':int(consistent.sum()),
        'central_equation_rank':r,'central_solution_dimension':len(free),
        'capped_group_order':216,'capped_heisenberg_generators':[HX,HY,HZ],
        'cm_nonzero_on_homogeneous_solutions':cm_kernel_nonzero,
        'case_records':case_records,
        'scope':'Complete finite derived-word record census under the displayed gentle and pentagon equations. No surviving record is asserted to lift to an actual profinite gentle element.'}
(HERE/'census_fivepoint_relative_class2.json').write_text(json.dumps(output,indent=2)+'\n')
