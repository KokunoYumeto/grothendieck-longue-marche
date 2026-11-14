#!/usr/bin/env python3
"""Actual zero-H-abelian words giving a basis of the two-adic source centre."""
from pathlib import Path
from collections import deque
from itertools import combinations
import json
import numpy as np
import sympy as sp
from de_ferrari_two_core import Span2
import bc_fermat_class_two_integral_model as q

HERE=Path(__file__).resolve().parent

def main():
    data=np.load(HERE/"bc_fermat_class_two_2adic_source.npz")
    raw=data["central_relation_matrix"];C=data["central_kernel_lattice"]
    generators=data["integral_K_basis_logs"];relators=data["integral_relator_logs"]
    K=data["integral_abelian_image"];rows=[0,1,3,4,5,7,8,9]
    Kinv12=np.array(12*sp.Matrix(K[rows]).inv(),dtype=np.int64)
    Cinv4=np.array(4*sp.Matrix(C).inv(),dtype=np.int64)
    def kcoords(v):
        a=Kinv12@v[rows];assert not np.any(a%12)
        a=a//12;assert np.array_equal(K@a,v)
        return a
    def representative(a):
        out=q.ZERO.copy()
        for exponent,g in zip(a,generators.T):out=q.multiply(out,int(exponent)*g)
        return out
    def raw_word(j):
        if j<5458:
            value=relators[j];coeff=kcoords(value[:10])
            value=q.multiply(value,-representative(coeff))
            meta={"kind":"adjusted_source_relator","relator_index":j,
                  "inverse_ordered_K_word_coefficients":coeff.tolist()}
        elif j<5474:
            action_index,gindex=divmod(j-5458,8)
            value=(q.S if action_index==0 else q.R)@generators[:,gindex]
            coeff=kcoords(value[:10]);value=q.multiply(value,-representative(coeff))
            meta={"kind":"adjusted_conjugate_K_word","conjugator":"s" if action_index==0 else "r",
                  "K_word_index":gindex,"inverse_ordered_K_word_coefficients":coeff.tolist()}
        else:
            i,k=list(combinations(range(8),2))[j-5474]
            value=np.r_[np.zeros(10,dtype=np.int64),2*q.wedge(generators[:10,i],generators[:10,k])]
            meta={"kind":"K_word_commutator","indices":[i,k]}
        assert not np.any(value[:10])
        assert np.array_equal(value[10:],2*raw[:,j])
        return value,meta
    span=Span2(45);selected=[];columns=[]
    queue=deque([(np.eye(45,dtype=np.int64),[])])
    seen=set()
    while queue and len(span.basis)<45:
        action,word=queue.popleft();key=action.tobytes()
        if key in seen:continue
        seen.add(key)
        values=action@raw;numerators=Cinv4@values
        assert not np.any(numerators%4)
        coordinates=numerators//4
        for j,column in enumerate(coordinates.T):
            if span.add(column%2,None):
                value,meta=raw_word(j)
                assert np.array_equal(action@value[10:],2*values[:,j])
                columns.append(values[:,j]);selected.append({"raw_relation_index":j,
                    "outer_conjugator_word":word,**meta})
                if len(span.basis)==45:break
        queue.append((q.S[10:,10:]@action,["s"]+word))
        queue.append((q.R[10:,10:]@action,["r"]+word))
    assert len(span.basis)==45
    W=np.stack(columns,axis=1)
    comparison=sp.Matrix(C).inv()*sp.Matrix(W)
    assert all(x.q==1 for x in comparison)
    determinant=int(comparison.det());assert determinant%2
    out={"basis_word_count":45,"all_words_have_zero_integral_H_abelianization":True,
         "outer_action_matrices_examined":len(seen),
         "central_word_basis_index_in_integral_C":abs(determinant),
         "central_word_basis_index_is_a_two_adic_unit":True,
         "word_preimages":selected,
         "actual_common_source_rule":"Take the supported two-primary powers of these actual binary-kernel words. Their ternary source image has exponent3, so this clears the ternary source exactly and retains their two-adic central images."}
    (HERE/"bc_fermat_class_two_2adic_words.json").write_text(json.dumps(out,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_two_2adic_words.npz",central_word_matrix=W,
                        comparison_to_integral_lattice=np.array(comparison,dtype=np.int64))
    print(json.dumps({k:v for k,v in out.items() if k!="word_preimages"},indent=2))
    print("PASS: forty-five actual word preimages form the full two-adic central source basis.")

if __name__=="__main__":main()
