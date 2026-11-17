#!/usr/bin/env python3
"""Actual rank-289 source homology and its eight five-point insertion maps.

This computes a quotient and its B-action only.  No surviving finite record
is asserted to lift to a profinite source element.
"""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np
import fivepoint_signed_level_data as C

def inverse(w):return tuple(-j for j in reversed(w))
def subst(w,images):return tuple(j for z in w for j in
    (images[z-1] if z>0 else inverse(images[-z-1])))

JQ=C.joint;ji=C.seen;JG=(C.X,C.Y)
assert C.complete and len(JQ)==288
def jmul(a,b):return tuple(int(C.table[x,y]) for x,y in zip(a,b))
def jinv(a):return tuple(C.inverses[x] for x in a)
jtable=np.array([[ji[jmul(a,b)] for b in JQ] for a in JQ],dtype=np.int64)
jinvtable=np.array([ji[jinv(q)] for q in JQ],dtype=np.int64)
jgens=np.array([ji[q] for q in JG],dtype=np.int64)
def jword(w):
    q=0
    for z in w:
        g=jgens[z-1] if z>0 else jinvtable[jgens[-z-1]]
        q=int(jtable[q,g])
    return q
paths={0:()};tree=set();order=[0]
for q in order:
    for j,g in enumerate(jgens):
        v=int(jtable[q,g])
        if v not in paths:
            paths[v]=paths[q]+(j+1,);tree.add((q,j));order.append(v)
chords=[(q,j) for q in range(288) for j in range(2) if (q,j) not in tree]
ci={edge:k for k,edge in enumerate(chords)}
loops=[paths[q]+(j+1,)+inverse(paths[int(jtable[q,jgens[j]])]) for q,j in chords]
assert len(loops)==289

def jchain(w):
    q=0;row=np.zeros(289,dtype=np.int64)
    for z in w:
        if z>0:
            edge=(q,z-1);q=int(jtable[q,jgens[z-1]]);sign=1
        else:
            q=int(jtable[q,jinvtable[jgens[-z-1]]]);edge=(q,-z-1);sign=-1
        if edge in ci:row[ci[edge]]+=sign
    assert q==0
    return row%3

deck={'s':((2,),(1,)),'r':((2,),(-2,-1))}
base_actions={};homology_actions={}
for name,aut in deck.items():
    perm=np.array([jword(subst(paths[q],aut)) for q in range(288)],dtype=np.int64)
    images=[jword(w) for w in aut]
    valid=all(perm[int(jtable[q,jgens[j]])]==jtable[perm[q],images[j]]
              for q in range(288) for j in range(2))
    assert valid, ('base kernel not B-stable',name)
    assert len(set(perm.tolist()))==288
    base_actions[name]=perm
    homology_actions[name]=np.array([jchain(subst(w,aut)) for w in loops],dtype=np.int64)
I289=np.eye(289,dtype=np.int64)
assert np.array_equal(homology_actions['s']@homology_actions['s']%3,I289)
assert np.array_equal(homology_actions['r']@homology_actions['r']@homology_actions['r']%3,I289)
print('PASS base288 kernel is B-normal; exact s,r actions retained on all289 free generators',flush=True)

def rref(A,p=3):
    A=(A%p).copy();r=0;piv=[]
    for c in range(A.shape[1]):
        if r==len(A):break
        nz=np.flatnonzero(A[r:,c])
        if not len(nz):continue
        j=r+int(nz[0]);A[[r,j]]=A[[j,r]]
        A[r]=A[r]*pow(int(A[r,c]),-1,p)%p
        nz=np.flatnonzero(A[:,c]);nz=nz[nz!=r]
        A[nz]=(A[nz]-A[nz,c,None]*A[r])%p
        piv.append(c);r+=1
    return A[:r],piv

R,piv=rref(C.matrix)
free=[j for j in range(C.matrix.shape[1]) if j not in piv]
P=np.zeros((C.matrix.shape[1],len(free)),dtype=np.int64)
P[free]=np.eye(len(free),dtype=np.int64)
P[piv]=-R[:,free]%3
assert P.shape==(769,102) and not np.any(C.matrix@P%3)

x12=(-5,-4,-3,-2,-1);z0=inverse(x12+(2,))
pairs=[(x12,(2,4)),((1,2),(5,)),((2,),(5,)),
       (x12+(1,),(4,5)),(x12,(2,)),((2,),x12),(z0,x12),((2,),z0)]
for pair,matrices in zip(pairs,C.pairs):
    assert tuple(C.word_eval(w,C.gens) for w in pair)==matrices

def target_chain(w):
    q=0;row=np.zeros(769,dtype=np.int64)
    for z in w:
        if z>0:
            edge=(q,z-1);q=int(C.table[q,C.ig[z-1]]);sign=1
        else:
            q=int(C.table[q,C.inverses[C.ig[-z-1]]]);edge=(q,-z-1);sign=-1
        if edge in C.chordidx:row[C.chordidx[edge]]+=sign
    assert q==0
    return row

T=np.hstack([np.array([target_chain(subst(w,pair)) for w in loops],dtype=np.int64)@P%3
             for pair in pairs])
R0,piv0=rref(T)
print('Actual eight-map homology image rank',len(R0),'of289, target dimension816',flush=True)
individual_ranks=[len(rref(T[:,102*i:102*(i+1)])[0]) for i in range(8)]
print('Individual insertion ranks',individual_ranks,flush=True)
S=homology_actions['s'];R3=homology_actions['r']
deck_matrices=[I289,S,R3,R3@R3%3,S@R3%3,S@R3@R3%3]
Tcore=np.hstack([a@T%3 for a in deck_matrices])
Rc,pivc=rref(Tcore)
print('Six-deck common homology image rank',len(Rc),'of289, target dimension4896',flush=True)

# A direct quotient coordinate projection obtained from independent columns.
columns=pivc;basis=Tcore[:,columns]
assert len(columns)==len(Rc)
Q=basis
# Q has full column rank; compute a left inverse by pivot rows of Q^t.
_,rows=rref(Q.T)
square=Q[rows]
aug=np.hstack((square,np.eye(len(rows),dtype=np.int64)))
red,pp=rref(aug)
assert pp[:len(rows)]==list(range(len(rows)))
left=np.zeros((len(rows),289),dtype=np.int64)
left[:,rows]=red[:,len(rows):]
assert np.array_equal(left@Q%3,np.eye(len(rows),dtype=np.int64))
assert np.array_equal(Q@(left@Tcore%3)%3,Tcore)
quotient_actions={}
for name,a in homology_actions.items():
    aq=left@a@Q%3
    assert np.array_equal(a@Q%3,Q@aq%3),('kernel not B-stable',name)
    quotient_actions[name]=aq
print('PASS exact B-action descends to retained common homology quotient',flush=True)

# Compare with the literal rank97 free modular kernel K.  The fifth
# insertion has generators U^2,L^2 and signed image96 omitting -I.
kgens=C.pairs[4]
KQ=[C.I];ki={C.I:0};kpaths={0:()};ktree=set()
for q in KQ:
    qi=ki[q]
    for j,g in enumerate(kgens):
        v=C.mul(q,g)
        if v not in ki:
            vi=len(KQ);ki[v]=vi;KQ.append(v)
            kpaths[vi]=kpaths[qi]+(j+1,);ktree.add((qi,j))
assert len(KQ)==96
ktable=np.array([[ki[C.mul(a,b)] for b in KQ] for a in KQ],dtype=np.int64)
kinv=np.array([ki[C.inv(q)] for q in KQ],dtype=np.int64)
kgi=np.array([ki[g] for g in kgens],dtype=np.int64)
kchords=[(q,j) for q in range(96) for j in range(2) if (q,j) not in ktree]
kci={edge:i for i,edge in enumerate(kchords)}
assert len(kchords)==97
def kchain(w):
    q=0;row=np.zeros(97,dtype=np.int64)
    for z in w:
        if z>0:
            edge=(q,z-1);q=int(ktable[q,kgi[z-1]]);sign=1
        else:
            q=int(ktable[q,kinv[kgi[-z-1]]]);edge=(q,-z-1);sign=-1
        if edge in kci:row[kci[edge]]+=sign
    assert q==0
    return row%3
modular=np.array([kchain(w) for w in loops],dtype=np.int64)
modular_rank=len(rref(modular)[0])
assert modular_rank==96
assert len(rref(np.hstack((T,modular)))[0])==len(R0)
modular_factor=left@modular%3
assert np.array_equal(Q@modular_factor%3,modular)
print('PASS common quotient maps onto the exact modular restriction image of rank96; kernel dimension1',flush=True)

output={
 'scope':'Actual source homology quotient and B action; no profinite lifting conclusion',
 'base_order':288,'source_rank':289,'target_h1_dimension':102,
 'eight_map_rank':len(R0),'six_deck_core_rank':len(Rc),
 'individual_insertion_ranks':individual_ranks,
 'modular_restriction_rank':modular_rank,'extra_module_dimension':len(Rc)-modular_rank,
 'base_B_normal':True,'pairwords':pairs,'Schreier_words':loops,
 'core_projection_columns':columns,'projection_pivot_rows':rows,
 'original_builder_sha256':sha256(Path(C.__file__).read_bytes()).hexdigest(),
 'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),
    target_relation_matrix=C.matrix,target_h1_projection=P,eight_map=T,
    six_deck_map=Tcore,common_projection=Q,
    source_s=S,source_r=R3,quotient_s=quotient_actions['s'],quotient_r=quotient_actions['r'],
    base_s=base_actions['s'],base_r=base_actions['r'],source_table=jtable,
    source_generators=jgens,source_chords=np.array(chords),
    projection_left_inverse=left,core_factor=left@Tcore%3,
    modular_restriction=modular,modular_factor=modular_factor,
    modular_table=ktable,modular_generators=kgi,modular_chords=np.array(kchords))
print('PASS complete actual maps and source/quotient B matrices saved',flush=True)
