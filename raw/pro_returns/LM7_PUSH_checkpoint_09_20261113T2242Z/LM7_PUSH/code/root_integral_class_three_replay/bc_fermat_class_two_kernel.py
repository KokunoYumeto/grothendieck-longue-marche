#!/usr/bin/env python3
"""Complete source-kernel image in the exponent-three H-class-two quotient.

The input has all 6668 actual normal relators of ker(B->D6) intersect F'.
Every multiplication, conjugation and cube below is evaluated in the
literal quotient from bc_fermat_class_two.py.  The resulting Lie subgroup
is closed under the two actual B actions and all Lie brackets.
"""
from pathlib import Path
from unittest.mock import patch
from itertools import combinations
import json,time
import numpy as np
import de_ferrari_two_family_words as family
from de_ferrari_mod9_lift import Span
import bc_fermat_class_two as q

HERE=Path(__file__).resolve().parent

def main():
    started=time.time()
    with patch.object(Path,"write_text",return_value=0):
        data=family.load_data()
    d=data["d"];ext=q.FExtension()
    old=json.loads((HERE/"bc_cm_fermat_kernel_boundary.json").read_text())
    oldmatrix=np.load(HERE/"bc_cm_fermat_kernel_boundary.npz")["original_relation_boundary_matrix"]
    nwords=json.loads((HERE/"bc_cm_literal_words.json").read_text())["N_B_basis_in_F"]
    ns=[ext.word(w) for w in nwords]
    basis=[q.literal(d["fword"](w)) for w in old["basis_F_prime_words_B"]]
    assert len(ns)==97 and len(basis)==18
    powers=[ext.power(n,6) for n in ns]
    assert all(g[0]==(0,0) for g in powers)
    power_kernel=np.load(HERE/"de_ferrari_mod9_module.npz")["integral_abelianization_kernel"]
    six_values=[]
    for column in power_kernel.T:
        h=q.ZERO.copy()
        for a,g in zip(column,powers):
            h=q.multiply(h,int(a)*g[1]%3)
        six_values.append(h)
    span=Span(55)
    provenance=[]
    def add(value,source):
        if span.add(value,source):
            provenance.append(source)
            return True
        return False
    relator_values=[]
    for index,row in enumerate(old["normal_relator_metadata"]):
        i=row["indices"]
        kind=row["kind"]
        if kind=="N_commutator":
            deck,h=ext.comm(ns[i[0]],ns[i[1]])
            assert deck==(0,0)
        elif kind=="F_prime_sixth_powers":
            h=six_values[i[0]].copy()
        elif kind=="basis_cube":
            h=q.multiply(q.multiply(basis[i[0]],basis[i[0]]),basis[i[0]])
        elif kind=="basis_commutator":
            h=q.commutator(basis[i[0]],basis[i[1]])
        elif kind=="N_conjugation":
            deck,h=ext.conj(ns[i[1]],((0,0),basis[i[0]]))
            assert deck==(0,0)
        else:
            raise ValueError(kind)
        if row["image_coefficients"] is not None:
            representative=q.ZERO.copy()
            for a,g in zip(row["image_coefficients"],basis):
                representative=q.multiply(representative,int(a)*g%3)
            h=q.multiply(h,-representative%3)
        assert np.array_equal(h[:10],oldmatrix[:,index]%3)
        relator_values.append(h)
        add(h,{"kind":"normal_relator","normal_relator_index":index})
    initial_dimension=len(span.basis)
    at=0
    while at<len(span.basis):
        value=span.basis[at].copy()
        for name,action in (("s",q.S),("r",q.R)):
            add(action@value%3,{"kind":"conjugation","letter":name,"basis_index":at})
        for j in range(at):
            add(q.commutator(value,span.basis[j]),
                {"kind":"commutator","basis_indices":[at,j]})
        at+=1
    matrix=span.matrix()
    ab_rank=q.f.rank(matrix[:10])
    dim=len(span.basis)
    assert ab_rank==q.f.rank(np.load(HERE/"bc_cm_fermat_kernel_boundary.npz")[
        "kernel_boundary_basis"]%3)
    for action in (q.S,q.R):
        for value in span.basis:span.coordinates(action@value%3)
    for i,j in combinations(range(dim),2):
        span.coordinates(q.commutator(span.basis[i],span.basis[j]))
    output={
        "quotient":"B/(gamma_3(H) H^3)",
        "source_kernel":"ker(B->D6) intersect F-prime",
        "complete_normal_relators_evaluated":len(relator_values),
        "initial_log_span_dimension":initial_dimension,
        "complete_image_log_dimension":dim,
        "abelian_image_dimension":ab_rank,
        "central_image_dimension":dim-ab_rank,
        "basis_preimages":provenance,
        "all_6668_abelian_projections_match_integral_certificate":True,
        "closed_under_actual_s_r_and_all_brackets":True,
        "binary_factor_comparison":"Squaring clears the exponent-two binary K6 image and is an automorphism of every cyclic subgroup of this exponent-three target.",
        "elapsed_seconds":round(time.time()-started,3)}
    (HERE/"bc_fermat_class_two_kernel.json").write_text(json.dumps(output,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_two_kernel.npz",
                        basis=matrix,normal_relator_values=np.stack(relator_values),
                        old_prime_basis_values=np.stack(basis),N_values=np.stack([g[1] for g in ns]),
                        N_decks=np.array([g[0] for g in ns]))
    print(json.dumps({k:v for k,v in output.items() if k!="basis_preimages"},indent=2))
    print("PASS: complete actual source-kernel image, with normal-relator word preimages.")

if __name__=="__main__":main()
