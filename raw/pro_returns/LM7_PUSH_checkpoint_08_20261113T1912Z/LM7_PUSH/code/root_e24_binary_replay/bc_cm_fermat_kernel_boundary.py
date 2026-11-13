#!/usr/bin/env python3
"""Complete integral boundary image of ker(B->D6) intersect F-prime.

Use all normal generators of K6 intersect F-prime, its complete
eighteen-dimensional elementary-abelian image, all presentation
relations, and closure under the actual B action on H^ab.  Squaring
then retains the binary E24 factor without changing the Z3 image.
"""
from pathlib import Path
from unittest.mock import patch
from itertools import combinations
import json,time
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
import de_fermat_schreier as f
from de_ferrari_degree6_lift import setup
from de_ferrari_mod9_lift import Span

HERE=Path(__file__).resolve().parent
start=time.time()
with patch.object(Path,"write_text",return_value=0):
    d,H,W,N,C,Full,data,J=setup()
assert len(J.basis)==19
full_elements=[W.exp(v) for v in J.basis]
for a,b in combinations(full_elements,2):
    assert W.equal(W.comm(a,b),W.one)
words=data["old_F_prime_basis_words"]+data["F_prime_basis_words"]
assert len(words)==18
prime=Span(19)
elements=[]
for w in words:
    g=W.word(w);elements.append(g)
    assert prime.add(J.coordinates(W.log(g)),w)
assert len(prime.basis)==18
def coordinates(g):
    return prime.coordinates(J.coordinates(W.log(g))).astype(np.int64)
hb=np.stack([f.integral_abel(d["fword"](w)) for w in words],axis=1)
for g in elements:assert W.equal(W.power(g,3),W.one)
for a,b in combinations(elements,2):assert W.equal(W.comm(a,b),W.one)
print("Loaded the exact18-dimensional elementary-abelian F-prime image.",flush=True)

boundary=np.load(HERE/"bc_cm_fermat_boundary.npz")
cover=np.load(HERE/"bc_cm_fermat_factorization.npz")
integer=np.load(HERE/"bc_cm_fermat_boundary_integral.npz")
geometric_action=[np.eye(10,dtype=np.int64),cover["translation"],
                  cover["translation"]@cover["translation"]]
nw=json.loads((HERE/"bc_cm_literal_words.json").read_text())["N_B_basis_in_F"]
assert len(nw)==97
residuals=[];metadata=[]
def add(vector,kind,indices,coefficients=None):
    residuals.append(np.asarray(vector,dtype=np.int64))
    metadata.append({"kind":kind,"indices":indices,
                     "image_coefficients":None if coefficients is None else
                        np.asarray(coefficients,dtype=np.int64).tolist()})

for col,(i,j) in enumerate(combinations(range(97),2)):
    v=coordinates(W.comm(N[i],N[j]))
    add(cover["N_B_commutator_images"][:,col]-hb@v,"N_commutator",[i,j],v)
    if (col+1)%1000==0:print("Original commutator relators:",col+1,flush=True)
power_elements=[W.power(n,6) for n in N]
power_coordinates=np.stack([J.coordinates(W.log(g)) for g in power_elements],axis=1)
power_boundary=np.stack([f.integral_abel(w*6) for w in nw],axis=1)
power_kernel=np.load(HERE/"de_ferrari_mod9_module.npz")["integral_abelianization_kernel"]
assert power_kernel.shape==(97,95)
fab=np.array([[sum(1 if a==j else -1 if a==-j else 0 for a in w)
               for w in nw] for j in (1,2)],dtype=np.int64)
assert not np.any(fab@power_kernel)
for j,coefficient in enumerate(power_kernel.T):
    v=prime.coordinates(power_coordinates@coefficient%3)
    add(power_boundary@coefficient-hb@v,"F_prime_sixth_powers",[j],v)
for j,h in enumerate(hb.T):add(3*h,"basis_cube",[j])
for i,j in combinations(range(18),2):
    assert W.equal(W.comm(elements[i],elements[j]),W.one)
    add(np.zeros(10,dtype=np.int64),"basis_commutator",[i,j])
for i,g in enumerate(elements):
    for j,n in enumerate(N):
        v=coordinates(W.conj(n,g))
        exponent=sum(1 if a==1 else -1 if a==-1 else 0 for a in nw[j])%3
        add(geometric_action[exponent]@hb[:,i]-hb@v,"N_conjugation",[i,j],v)
    print("Conjugation rows completed:",i+1,flush=True)
assert len(residuals)==4656+95+18+153+18*97==6668
R=np.stack(residuals,axis=1)
L=np.array(json.loads((HERE/"bc_cm_fermat_boundary_integral.json").read_text())[
    "F_abelianization_map_divided_by_three"],dtype=np.int64)
assert not np.any(L@R)
K=hermite_normal_form(sp.Matrix(R))
S,Raction=map(sp.Matrix,(boundary["S"],boundary["R"]))
closure_dimensions=[]
while True:
    knew=hermite_normal_form(K.row_join(S*K).row_join(Raction*K))
    closure_dimensions.append(knew.cols)
    if knew==K:break
    K=knew
assert K.cols==8
assert sp.Matrix(L)*K==sp.zeros(2,8)
zrows=[0,1,3,4,5,7,8,9]
relative=K.extract(zrows,list(range(8)))
assert relative.det()!=0
index=abs(int(relative.det()))
E=sp.Matrix(integer["E"])
norm=E*K
SN,U,V=map(lambda a:a.to_Matrix(),
          smith_normal_decomp(DomainMatrix.from_Matrix(norm).convert_to(sp.ZZ)))
assert SN==U*norm*V and abs(U.det())==abs(V.det())==1
diagonal=[abs(int(SN[j,j])) for j in range(8)]
rank=sum(bool(x) for x in diagonal)
assert rank==5
print("Complete integral kernel-boundary index in ker(Fab):",index,sp.factorint(index),flush=True)
print("Complete norm Smith factors:",diagonal,flush=True)

def integral_at_three(a):return int(sp.denom(a))%3!=0
def reduction_three(a):return int(sp.numer(a))*pow(int(sp.denom(a)),-1,3)%3
def rank_mod3(a):
    a=np.asarray(a,dtype=np.int64).copy()%3;r=0
    for j in range(a.shape[1]):
        ids=np.flatnonzero(a[r:,j])
        if not len(ids):continue
        k=r+int(ids[0]);a[[r,k]]=a[[k,r]]
        a[r]=a[r]*pow(int(a[r,j]),-1,3)%3
        for i in range(a.shape[0]):
            if i!=r:a[i]=(a[i]-a[i,j]*a[r])%3
        r+=1
        if r==a.shape[0]:break
    return r

families=json.loads((HERE/"bc_cm_fermat_odd_boundary.json").read_text())["records"]
derivatives=[sp.Matrix(a) for a in boundary["abelian_action_derivatives"]]
records=[]
for row in families:
    z=sp.Matrix(row["integral_H_abelianization"]);rhs=-E*z;urhs=U*rhs
    assert urhs[rank:,:]==sp.zeros(20-rank,1)
    y=sp.Matrix([urhs[j]/SN[j,j] if j<rank else 0 for j in range(8)])
    good=all(integral_at_three(a) for a in y)
    correction=None;action_rank=None
    if good:
        coefficients=V*y;correction=K*coefficients
        assert E*correction==rhs
        target=z+correction
        reduced=sp.Matrix([reduction_three(a) for a in target])
        action=sp.eye(10)+sp.Matrix.hstack(*(a*reduced for a in derivatives))
        action_rank=rank_mod3(np.array(action,dtype=np.int64))
        assert action_rank==10
    records.append({"certificate_index":row["certificate_index"],
        "ternary_parameters":row["ternary_parameters"],
        "binary_parameter":row["binary_parameter"],
        "complete_kernel_norm_solvable_over_Z3":good,
        "corrected_H_action_rank_mod3":action_rank,
        "rational_boundary_correction":None if correction is None else [str(a) for a in correction]})
counts=[]
for i in range(24):
    group=[r for r in records if r["certificate_index"]==i]
    n=sum(r["complete_kernel_norm_solvable_over_Z3"] for r in group);counts.append(n)
    print("CM row",i,": complete-kernel generating three-adic lifts",n,"of18",flush=True)

result={"normal_presentation":"K6 intersect F-prime -> exact18-dimensional elementary-abelian D6 image",
    "number_of_normal_relators":len(residuals),
    "basis_F_prime_words_B":words,
    "basis_H_abelianizations":hb.tolist(),
    "normal_relator_metadata":metadata,
    "literal_boundary_actions_closed":["s","r"],
    "kernel_boundary_basis":np.array(K,dtype=np.int64).tolist(),
    "kernel_boundary_index_in_ker_F_abelianization":index,
    "kernel_boundary_index_factorization":{str(p):int(e) for p,e in sp.factorint(index).items()},
    "norm_smith_factors":diagonal,
    "records":records,"passing_counts_by_CM_row":counts,
    "total_passing":sum(counts),
    "binary_comparison":"Square each ternary-kernel relator to kill the binary exponent2 K6 image; multiplication by2 preserves the Z3 boundary image.",
    "elapsed_seconds":round(time.time()-start,3)}
(HERE/"bc_cm_fermat_kernel_boundary.json").write_text(json.dumps(result,indent=2)+"\n")
np.savez_compressed(HERE/"bc_cm_fermat_kernel_boundary.npz",
    original_relation_boundary_matrix=R,kernel_boundary_basis=np.array(K,dtype=np.int64),
    norm=np.array(norm,dtype=np.int64),smith=np.array(SN,dtype=np.int64),
    smith_left=np.array(U,dtype=np.int64),smith_right=np.array(V,dtype=np.int64))
print("PASS: complete ternary-kernel boundary image and all432 joint-family tests.",flush=True)
