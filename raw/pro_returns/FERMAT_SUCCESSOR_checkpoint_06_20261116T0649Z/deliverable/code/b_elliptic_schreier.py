#!/usr/bin/env python3
"""Exact Schreier data for the multiplication-three elliptic cover.

F=<a,b>, N=ker(F -> (Z/3)^2).  The underlying once-punctured
elliptic curve is not the tripod.  All words below are exact free
group words.  Only class-two logarithms use division, by the unit2.
"""
from pathlib import Path
import json
from itertools import product
import numpy as np
import sympy as sp

cosets=list(product(range(3),repeat=2))
def transversal(c):return [1]*c[0]+[2]*c[1]
def inv(word):return [-x for x in word[::-1]]
def reduce(word):
    out=[]
    for x in word:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return out
def step(c,x):
    s=1 if x>0 else -1
    return tuple((c[i]+(s if i==abs(x)-1 else 0))%3 for i in range(2))

edges={}
words=[]
for c in cosets:
    for x in [1,2]:
        w=reduce(transversal(c)+[x]+inv(transversal(step(c,x))))
        if w:
            edges[(c,x)]=len(words)+1
            words.append(w)
        else:edges[(c,x)]=0
assert len(words)==10

def rewrite(word):
    c=(0,0);result=[]
    for x in word:
        if x>0:
            g=edges[(c,x)];c=step(c,x)
        else:
            c=step(c,x);g=-edges[(c,-x)]
        if g:result.append(g)
    assert c==(0,0)
    return reduce(result)

for i,w in enumerate(words):assert rewrite(w)==[i+1]
def abelian(word):
    v=np.zeros(10,dtype=np.int64)
    for x in word:v[abs(x)-1]+=1 if x>0 else -1
    return v

pairs=[(i,j) for i in range(10) for j in range(i)]
def wedge(x,y):return np.array([int(x[i])*int(y[j])-int(x[j])*int(y[i]) for i,j in pairs],dtype=np.int64)
def class_two(word):
    """Return (linear, twice central BCH coordinates)."""
    v=np.zeros(10,dtype=np.int64)
    z2=np.zeros(45,dtype=np.int64)
    for letter in word:
        e=np.zeros(10,dtype=np.int64);e[abs(letter)-1]=1 if letter>0 else -1
        z2+=wedge(v,e);v+=e
    return v,z2

commutator=[1,2,-1,-2]
peripheral={c:abelian(rewrite(transversal(c)+commutator+inv(transversal(c)))) for c in cosets}
assert not np.any(sum(peripheral.values()))
transfer=[]
for x in [1,2]:
    t=np.zeros(10,dtype=np.int64)
    for c in cosets:
        g=edges[(c,x)]
        if g:t[g-1]+=1
    transfer.append(t)
ut,vt=transfer
ordered_cusps=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)

# Test both peripheral orientations.  The compatible one must recover
# the integral Fermat gluing basis without dividing a nonmultiple of3.
compatible=[]
for orientation in [1,-1]:
    E=np.column_stack([orientation*peripheral[c] for c in ordered_cusps])
    raw=np.column_stack((ut,vt))-E@U
    if not np.any(raw%3):
        basis=np.column_stack((raw//3,E))
        det=int(sp.Matrix(basis).det())
        compatible.append((orientation,det,basis))
print('Schreier generators:',words,flush=True)
print('Transfer vectors:',ut.tolist(),vt.tolist(),flush=True)
print('Compatible boundary orientations/determinants:',[(a,b) for a,b,_ in compatible],flush=True)
assert len(compatible)==1
orientation,det,basis=compatible[0]
assert abs(det)==1
binv=np.array(sp.Matrix(basis).inv(),dtype=np.int64)
assert np.array_equal(binv@ut,np.concatenate(([3,0],U[:,0])))
assert np.array_equal(binv@vt,np.concatenate(([0,3],U[:,1])))

actions=[];quadratic=[];all_images=[]
for x in [1,2]:
    images=[rewrite([x]+w+[-x]) for w in words]
    all_images.append(images)
    lin=np.column_stack([abelian(w) for w in images])
    quad=np.column_stack([class_two(w)[1] for w in images])
    actions.append(binv@lin@basis)
    quadratic.append(quad)
    assert np.array_equal(lin@ut,ut) and np.array_equal(lin@vt,vt)
    for c in cosets:
        # Conjugation acts on the peripheral orbit by the deck translation.
        assert np.array_equal(lin@peripheral[c],peripheral[step(c,x)])
print('Both exact deck actions preserve transfer and permute all nine peripheral classes: PASS',flush=True)
reference=[]
for shift in [(1,0),(0,1)]:
    torus=np.zeros((8,8),dtype=np.int64)
    for j,c in enumerate(ordered_cusps):
        target=tuple((c[k]+shift[k])%3 for k in range(2))
        if target==(0,0):torus[:,j]=-1
        else:torus[ordered_cusps.index(target),j]=1
    reference.append(np.block([[np.eye(2,dtype=np.int64),np.zeros((2,8),dtype=np.int64)],[(U-torus@U)//3,torus]]))
reference=np.stack(reference)
assert np.array_equal(np.stack(actions),reference)
print('The integral abelianization matches the original B24/B38 V matrices exactly: PASS',flush=True)

# A boundary-preserving punctured-torus lift of the CM matrix R.
# First a->b,b->b^-1 a^-1 has peripheral conjugator (ab)^-1;
# conjugating by ab gives the following exact based representative.
sigma_words={1:[1,2,-1],2:[-2,-1]}
def substitute(word,images):
    return reduce([a for x in word for a in (images[x] if x>0 else inv(images[-x]))])
assert substitute(commutator,sigma_words)==commutator
for x in [1,2]:
    third=[x]
    for _ in range(3):third=substitute(third,sigma_words)
    assert third==reduce(commutator+[x]+inv(commutator))
sigma_images=[rewrite(substitute(w,sigma_words)) for w in words]
sigma_linear=np.column_stack([abelian(w) for w in sigma_images])
sigma_quadratic=np.column_stack([class_two(w)[1] for w in sigma_images])
sigma_V=binv@sigma_linear@basis
R=np.array([[0,-1],[1,-1]],dtype=np.int64)
assert np.array_equal(sigma_linear@np.column_stack(transfer),np.column_stack(transfer)@R)
for c in cosets:
    target=tuple(R@np.array(c,dtype=np.int64)%3)
    assert np.array_equal(sigma_linear@peripheral[c],peripheral[target])
glob=np.load('deliverable/code/b_global_action_ambiguity_matrices.npz')
matches=[g for g in glob['projective_automorphisms'] if np.array_equal(g,sigma_V)]
assert len(matches)==1
assert np.array_equal(sigma_V[:2,:2],R)
assert np.array_equal(sigma_V[2:,2:]@(-np.ones(8,dtype=np.int64)),-np.ones(8,dtype=np.int64))
print('Exact boundary-fixing CM automorphism matches the actual R3 Fermat automorphism: PASS',flush=True)
actions.append(sigma_V);quadratic.append(sigma_quadratic);all_images.append(sigma_images)

# The elliptic involution has compact matrix -I.  Its peripheral
# correction is again conjugation by ab.
neg_words={1:[1,2,-1,-2,-1],2:[1,-2,-1]}
assert substitute(commutator,neg_words)==commutator
for x in [1,2]:
    assert substitute(substitute([x],neg_words),neg_words)==reduce(commutator+[x]+inv(commutator))
neg_images=[rewrite(substitute(w,neg_words)) for w in words]
neg_linear=np.column_stack([abelian(w) for w in neg_images])
neg_quadratic=np.column_stack([class_two(w)[1] for w in neg_images])
neg_V=binv@neg_linear@basis
assert np.array_equal(neg_V[:2,:2],-np.eye(2,dtype=np.int64))
assert sum(np.array_equal(g,neg_V) for g in glob['projective_automorphisms'])==1
assert np.array_equal(neg_V[2:,2:]@(-np.ones(8,dtype=np.int64)),-np.ones(8,dtype=np.int64))
actions.append(neg_V);quadratic.append(neg_quadratic);all_images.append(neg_images)
print('Exact boundary-fixing elliptic involution also matches its Fermat V action: PASS',flush=True)

result={'Schreier_generators':words,'boundary_orientation':orientation,
        'basis_determinant':det,'transfer_u':ut.tolist(),'transfer_v':vt.tolist(),
        'sigma_base_words':sigma_words,'involution_base_words':neg_words,
        'images_of_Schreier_generators':all_images,
        'status':'exact index-nine Schreier words, translations, boundary-fixing CM, and B24 abelian comparison certified'}
Path('deliverable/code/b_elliptic_schreier.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed('deliverable/code/b_elliptic_schreier_matrices.npz',
                    original_basis_in_Schreier=basis,Schreier_basis_in_original=binv,
                    translation_V=np.stack(actions),quadratic_Schreier_twice=np.stack(quadratic),
                    transfer_Schreier=np.column_stack(transfer),
                    peripheral_Schreier=np.stack([orientation*peripheral[c] for c in cosets]))
