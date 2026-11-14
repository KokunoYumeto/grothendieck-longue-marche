#!/usr/bin/env python3
"""Exact central image of the source kernel intersected with H-prime.

The eight actual words from E31 form an integral basis of the H-abelian
image K.  Replace every source normal relator and every s/r conjugate of
these words by its ordered K representative, and retain their commutators.
This is a complete normal presentation of R3 intersect H-prime.
"""
from pathlib import Path
from itertools import combinations
import json
import numpy as np
import sympy as sp
from de_ferrari_mod9_lift import Span
import bc_fermat_class_two as q

HERE=Path(__file__).resolve().parent
old=np.load(HERE/"bc_cm_fermat_kernel_boundary.npz")
current=np.load(HERE/"bc_fermat_class_two_kernel.npz")
words=json.loads((HERE/"bc_cm_fermat_kernel_words.json").read_text())
K=old["kernel_boundary_basis"]
R=old["original_relation_boundary_matrix"]
indices=[r["normal_relator_index"] for r in words["selected_normal_relators"]]
coefficients=np.asarray(words["exact_integer_word_combination_matrix"],dtype=np.int64)
selected=current["normal_relator_values"][indices]
zrows=[0,1,3,4,5,7,8,9]
inverse=sp.Matrix(K[zrows]).inv()
scaled=np.array(12*inverse,dtype=np.int64)
assert np.array_equal(scaled@K[zrows],12*np.eye(8,dtype=np.int64))

def coordinates(ab):
    numerator=scaled@ab[zrows]
    assert not np.any(numerator%12)
    out=numerator//12
    assert np.array_equal(K@out,ab)
    return out

generators=[]
for column in coefficients.T:
    value=q.ZERO.copy()
    for power,log in zip(column,selected):
        value=q.multiply(value,int(power)*log%3)
    generators.append(value)
generators=np.stack(generators)
assert np.array_equal(generators[:,:10].T,K%3)

def representative(powers):
    result=q.ZERO.copy()
    for power,value in zip(powers,generators):
        result=q.multiply(result,int(power)*value%3)
    return result

span=Span(45);provenance=[]
def add(value,origin):
    assert not np.any(value[:10])
    if span.add(value[10:],origin):provenance.append(origin)

for i,(ab,value) in enumerate(zip(R.T,current["normal_relator_values"])):
    c=coordinates(ab)
    residual=q.multiply(value,-representative(c)%3)
    add(residual,{"kind":"adjusted_normal_relator","normal_relator_index":i,
                  "integral_K_coordinates":c.tolist()})

integral=np.load(HERE/"bc_cm_fermat_boundary.npz")
for name,action,action_ab in (("s",q.S,integral["S"]),("r",q.R,integral["R"])):
    for i,value in enumerate(generators):
        c=coordinates(action_ab@K[:,i])
        residual=q.multiply(action@value%3,-representative(c)%3)
        add(residual,{"kind":"adjusted_basis_conjugation","letter":name,
                      "kernel_basis_index":i,"integral_K_coordinates":c.tolist()})
for i,j in combinations(range(8),2):
    add(q.commutator(generators[i],generators[j]),
        {"kind":"kernel_basis_commutator","kernel_basis_indices":[i,j]})
initial=len(span.basis)
at=0
while at<len(span.basis):
    value=span.basis[at]
    for name,action in (("s",q.S[10:,10:]),("r",q.R[10:,10:])):
        image=action@value%3
        if span.add(image,None):
            provenance.append({"kind":"central_conjugation","letter":name,"basis_index":at})
    at+=1
result={"source":"R3=ker(B->D6) intersect F-prime",
        "intersection":"R3 intersect H-prime",
        "central_image_dimension":len(span.basis),
        "initial_central_image_dimension":initial,
        "integral_abelian_basis_rank":8,
        "exact_normal_presentation":True,
        "basis_preimages":provenance}
(HERE/"bc_fermat_class_two_integral_kernel.json").write_text(json.dumps(result,indent=2)+"\n")
np.savez_compressed(HERE/"bc_fermat_class_two_integral_kernel.npz",
                    central_basis=span.matrix(),integral_kernel_basis_logs=generators.T,
                    integral_kernel_basis=K)
print(json.dumps({k:v for k,v in result.items() if k!="basis_preimages"},indent=2))
print("PASS: exact integral-abelian kernel intersection and its complete central image.")
