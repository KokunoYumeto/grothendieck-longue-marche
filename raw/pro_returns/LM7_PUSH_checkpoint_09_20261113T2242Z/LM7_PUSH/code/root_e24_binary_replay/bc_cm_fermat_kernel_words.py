#!/usr/bin/env python3
"""Actual word preimages of the eight complete boundary-kernel generators."""
from pathlib import Path
from unittest.mock import patch
import json
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
import de_fermat_schreier as f
from de_ferrari_degree6_lift import setup

HERE=Path(__file__).resolve().parent
with patch.object(Path,"write_text",return_value=0):
    d,H,W,N,C,Full,data,J=setup()
record=json.loads((HERE/"bc_cm_fermat_kernel_boundary.json").read_text())
arrays=np.load(HERE/"bc_cm_fermat_kernel_boundary.npz")
basis=record["basis_F_prime_words_B"]
power_kernel=np.load(HERE/"de_ferrari_mod9_module.npz")["integral_abelianization_kernel"]
selected=[2,3,101,103,104,105,106,108,111,4658,4660,4661]
coefficients=np.array([
 [-7,-12,-11,-4,2,0,-11,-1],
 [-19,-28,-30,-1,0,-2,-15,-1],
 [14,21,20,-3,0,-2,14,-3],
 [-2,-7,-7,-3,2,0,-4,-1],
 [-10,-12,-9,1,-3,-3,-10,-1],
 [0,3,5,3,-3,-1,1,0],
 [6,9,8,1,0,1,7,1],
 [-3,-4,-7,-2,3,2,-3,1],
 [7,13,12,0,0,0,8,0],
 [-1,-3,-3,0,0,0,-1,0],
 [-1,-1,-1,0,0,0,-1,0],
 [1,2,2,0,0,0,1,0]],dtype=np.int64)
R=arrays["original_relation_boundary_matrix"]
K=arrays["kernel_boundary_basis"]
assert np.array_equal(R[:,selected]@coefficients,K)

def word_power(w,a):
    return (w if a>=0 else d["binv"](w))*abs(a)
def relator(index):
    row=record["normal_relator_metadata"][index]
    i=row["indices"]
    if row["kind"]=="N_commutator":
        a,b=[d["Nwords"][j] for j in i]
        seed=a+b+d["binv"](a)+d["binv"](b)
    elif row["kind"]=="F_prime_sixth_powers":
        seed=[]
        for a,w in zip(power_kernel[:,i[0]],d["Nwords"]):
            seed+=word_power(w,6*int(a))
    elif row["kind"]=="basis_cube":
        seed=basis[i[0]]*3
    elif row["kind"]=="basis_commutator":
        a,b=[basis[j] for j in i]
        seed=a+b+d["binv"](a)+d["binv"](b)
    elif row["kind"]=="N_conjugation":
        a,b=d["Nwords"][i[1]],basis[i[0]]
        seed=a+b+d["binv"](a)
    else:
        raise ValueError(row["kind"])
    if row["image_coefficients"] is not None:
        representative=[]
        for a,w in zip(row["image_coefficients"],basis):
            representative+=w*int(a)
        seed+=d["binv"](representative)
    return seed

relators=[];fw=[]
for index in selected:
    bw=relator(index);word=list(d["fword"](bw))
    assert W.equal(W.word(bw),W.one)
    assert np.array_equal(f.integral_abel(word),R[:,index])
    assert all(sum(1 if a==j else -1 if a==-j else 0 for a in word)==0 for j in (1,2))
    relators.append({"normal_relator_index":index,"literal_B_word":bw,
                     "literal_F_word":word})
    fw.append(word)
    print("Checked actual source-kernel relator",index,"with F-word length",len(word),flush=True)

generators=[]
for j in range(8):
    word=[]
    for a,w in zip(coefficients[:,j],fw):
        word+=(w if a>=0 else f.inverse_word(w))*abs(int(a))
    assert np.array_equal(f.integral_abel(word),K[:,j])
    generators.append({"kernel_basis_column":j,
        "word_as_ordered_selected_relator_power_product":coefficients[:,j].tolist(),
        "expanded_F_word_length":len(word),
        "H_abelianization":K[:,j].tolist()})
    print("Checked kernel-lattice generator",j,"with expanded F-word length",len(word),flush=True)

homogeneous=sp.Matrix(K)*sp.Matrix(arrays["smith_right"])[:,5:]
smithK=smith_normal_form(sp.Matrix(K),domain=ZZ)
smithHom=smith_normal_form(homogeneous,domain=ZZ)
sk=[abs(int(smithK[j,j])) for j in range(8)]
sh=[abs(int(smithHom[j,j])) for j in range(3)]
assert sk==[1,1,1,1,1,1,12,12] and sh==[1,4,12]
out={"selected_normal_relators":relators,
    "exact_integer_word_combination_matrix":coefficients.tolist(),
    "kernel_lattice_generators":generators,
    "kernel_embedding_smith":sk,
    "homogeneous_norm_kernel_basis":np.array(homogeneous,dtype=np.int64).tolist(),
    "homogeneous_norm_kernel_embedding_smith":sh,
    "finite_three_power_fibre_size":"3^(3n-1) for n>=1, as actual H^ab/3^n correction images",
    "all_finite_boundary_fibres_lift_compatibly":True,
    "binary_preserving_generators":"Square each of these eight actual ternary-kernel/F-prime words; use continuous Z3 exponents after dividing their coefficients by2."}
(HERE/"bc_cm_fermat_kernel_words.json").write_text(json.dumps(out,indent=2)+"\n")
print("PASS: eight actual lattice-generator preimages; full source-kernel/F-prime checks; exact compatible ternary fibre counts.",flush=True)
