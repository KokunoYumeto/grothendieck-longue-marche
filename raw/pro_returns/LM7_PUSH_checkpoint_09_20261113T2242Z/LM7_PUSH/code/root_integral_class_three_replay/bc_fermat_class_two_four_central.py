#!/usr/bin/env python3
"""Literal H-prime preimages of the entire 39-dimensional binary centre."""
from pathlib import Path
from unittest.mock import patch
from itertools import combinations
import json
import numpy as np
from de_ferrari_two_core import Span2
import de_ferrari_two_family_words as family
import bc_fermat_class_two_four as q
import bc_fermat_class_two as q3

HERE=Path(__file__).resolve().parent
record=json.loads((HERE/"bc_fermat_class_two_four_kernel.json").read_text())
arrays=np.load(HERE/"bc_fermat_class_two_four_kernel.npz")
with patch.object(Path,"write_text",return_value=0):data=family.load_data()
d=data["d"];basis_words=record["basis_F_prime_words_B"]
indices=[r["normal_relator_index"] for r in record["parity_basis_preimages"]]
assert indices==[96,97,98,100,103,104]
literal_relators=[]
for j,index in enumerate(indices):
    row=record["normal_relator_metadata"][index]
    assert row["kind"]=="N_commutator"
    a,b=[d["Nwords"][i] for i in row["indices"]]
    word=a+b+d["binv"](a)+d["binv"](b)
    representative=[]
    for power,g in zip(row["image_coefficients"],basis_words):representative+=g*int(power)
    word+=d["binv"](representative)
    fw=list(d["fword"](word))
    assert np.array_equal(q.literal(fw),arrays["parity_basis"][:,j])
    assert np.array_equal(q.f.integral_abel(fw),
                          arrays["original_relation_boundary_matrix"][:,index])
    assert all(sum(1 if a==i else -1 if a==-i else 0 for a in fw)==0 for i in (1,2))
    literal_relators.append({"normal_relator_index":index,
                             "literal_B_word":word,"literal_F_word":fw})

span=Span2(45);preimages=[];all_values=[]
for i,row in enumerate(literal_relators):
    a=row["literal_F_word"]
    for j,b in enumerate(q.f.NWORDS):
        word=a+b+q.f.inverse_word(a)+q.f.inverse_word(b)
        value=q.literal(word)
        assert not np.any(q.f.integral_abel(word))
        assert not np.any(value[:10])
        assert np.array_equal(value,q.commutator(arrays["parity_basis"][:,i],
                                                np.eye(55,dtype=np.int64)[j]))
        # This exact ninth power retains the binary centre and kills P3.
        assert np.array_equal(q.literal(word*9),value)
        assert not np.any(q3.literal(word*9))
        all_values.append(value[10:])
        if span.add(value[10:],None):
            preimages.append({"normal_relator_index":row["normal_relator_index"],
                              "H_basis_generator_index":j+1,
                              "literal_F_commutator_word":word,
                              "joint_preserving_power":9})
assert len(span.basis)==39
for value in arrays["commutator_central_basis"].T:span.coordinates(value)
for value in span.basis:
    check=Span2(45)
    for col in arrays["commutator_central_basis"].T:check.add(col,None)
    check.coordinates(value)
out={"source_kernel":"ker(B->D2,6) intersect F-prime",
     "intersection":"source kernel intersect H-prime",
     "actual_parity_relators":literal_relators,
     "central_basis_preimages":preimages,
     "central_image_dimension":39,
     "all_60_literal_commutators_checked":True,
     "all_integral_H_abelianizations_zero":True,
     "ninth_powers_preserve_binary_values_and_kill_P3":True,
     "joint_ternary_source_preserved":"Every displayed word lies in K6; its ninth power kills the complete exponent-three ternary K6 image."}
(HERE/"bc_fermat_class_two_four_central.json").write_text(json.dumps(out,indent=2)+"\n")
np.savez_compressed(HERE/"bc_fermat_class_two_four_central.npz",
                    central_basis=span.matrix(),all_60_commutator_values=np.stack(all_values))
print("Actual binary parity relators:",indices)
print("Central basis dimension:",len(span.basis))
print("PASS: exact H-prime preimages, all60 literal comparisons, and ninth-power CRT preservation.")
