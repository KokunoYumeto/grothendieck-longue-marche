#!/usr/bin/env python3
"""Complete P8 source fibres, using all5458 binary normal relators.

The source abelian lattice, its actual word lifts, the Hall parity
condition and the full central source lattice are retained.  The finite
central modulus is4, while the abelian modulus is8.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time
import numpy as np
import sympy as sp
import bc_fermat_class_two_integral_model as q
from bc_fermat_class_two_integral_extension import hall_coordinates

HERE=Path(__file__).resolve().parent

def main():
    started=time.time()
    src=np.load(HERE/"bc_fermat_class_two_2adic_source.npz")
    K=src["integral_abelian_image"]
    generators=src["integral_K_basis_logs"]
    C=src["central_kernel_lattice"]
    data=np.load(HERE/"bc_fermat_class_two_2adic_norms.npz")
    detector=data["source_membership_detector"]
    particular3=data["ambient_particular_times3"]
    cp3=sp.Matrix(C).inv()*sp.Matrix(particular3)
    cp12=np.array(4*cp3,dtype=np.int64)
    assert np.array_equal(cp12,detector)
    source=np.load(HERE/"bc_fermat_class_two_integral_family.npz")["source_word_logs"]
    metadata=json.loads((HERE/"bc_fermat_class_two_integral_family.json").read_text())["records"]
    old=json.loads((HERE/"bc_cm_fermat_kernel_boundary.json").read_text())["records"]
    hom=np.array(json.loads((HERE/"bc_cm_fermat_kernel_words.json").read_text())[
        "homogeneous_norm_kernel_basis"],dtype=np.int64)
    rows=[0,1,3,4,5,7,8,9]
    inverse12=np.array(12*sp.Matrix(K[rows]).inv(),dtype=np.int64)
    assert np.array_equal(K[rows]@inverse12,12*np.eye(8,dtype=np.int64))
    derivative=np.load(HERE/"bc_cm_fermat_boundary.npz")["abelian_action_derivatives"]
    old4=json.loads((HERE/"bc_fermat_class_two_four_fibres.json").read_text())["records"]
    central_rows=np.r_[np.arange(10,55),np.arange(65,110)]
    abelian_rows=np.r_[np.arange(10),np.arange(55,65)]
    records=[];passing_examples=[];obstruction_counts=Counter()
    for i,(f,meta,previous) in enumerate(zip(source,metadata,old)):
        rational=[sp.Rational(x) for x in previous["rational_boundary_correction"]]
        assert all(x.q==1 for x in rational)
        vpart=f[:10]+np.array(rational,dtype=np.int64)
        fibres=[];seen=set();reductions4=set()
        for a in product(range(8),range(2),range(2)):
            v=vpart+hom@np.array(a,dtype=np.int64)
            residue=tuple(v%8);assert residue not in seen;seen.add(residue)
            reductions4.add(tuple(v%4))
            numerator=inverse12@(v-f[:10])[rows]
            assert not np.any(numerator%12)
            coefficients=numerator//12
            assert np.array_equal(K@coefficients,v-f[:10])
            correction=q.ZERO.copy()
            for exponent,generator in zip(coefficients,generators.T):
                correction=q.multiply(correction,int(exponent)*generator)
            target=q.multiply(f,correction)
            assert np.array_equal(target[:10],v)
            errors=q.norm_errors(target)
            assert not np.any(errors[abelian_rows])
            assert not np.any(errors[central_rows]%2)
            rhs=errors[central_rows]//2
            t1,t2,t3=-v[0],v[1],v[4]
            u,w=t1+t2,t2
            vv=t3-t2
            F=vv+3*(u*u+u*vv+vv*vv)
            assert F%4==0
            residue_obstruction=detector@(rhs%4)%4
            good=not np.any(residue_obstruction)
            obstruction_counts[tuple(residue_obstruction)]+=1
            central_correction=None;rank=None
            if good:
                # detector*h/4 is the exact source coefficient vector of
                # three times the ambient particular solution.
                source_numerator=detector@rhs
                assert not np.any(source_numerator%4)
                source_coeff=3*(source_numerator//4)%4
                central_correction=C@source_coeff%4
                candidate=target.copy();candidate[10:]+=2*central_correction
                residual=q.norm_errors(candidate)
                assert not np.any(residual[abelian_rows]%8)
                assert not np.any(residual[central_rows]%8)
                hall=hall_coordinates(candidate)
                assert np.array_equal(hall[:10]%8,v%8)
                action=np.eye(10,dtype=np.int64)+np.stack([
                    block@(v%2) for block in derivative],axis=1)
                rank=q.f.rank(action%2,p=2);assert rank==10
                if len(passing_examples)<12:
                    passing_examples.append({"source_index":i,"abelian_parameters":list(a),
                        "source_K_word_coefficients":coefficients.tolist(),
                        "source_central_coefficients_mod4":source_coeff.tolist(),
                        "target_Hall_coordinates":np.r_[hall[:10]%8,hall[10:]%4].tolist()})
            fibres.append({"abelian_parameters":list(a),
                "target_abelianization_mod8":[int(x) for x in residue],
                "central_norm_solvable":good,
                "obstruction_mod4":residue_obstruction.tolist(),
                "particular_Hall_central_correction_mod4":None if central_correction is None else central_correction.tolist(),
                "H_Frattini_action_rank":rank})
        assert len(seen)==32 and len(reductions4)==4
        assert reductions4=={tuple(row["target_abelianization"]) for row in old4[i]["abelian_fibres"]}
        count=sum(fiber["central_norm_solvable"] for fiber in fibres)
        records.append({**meta,"abelian_fibres":fibres,"passing_abelian_fibres":count,
            "central_correction_images_per_passing_value":2**16,
            "total_distinct_correction_images":count*2**16})
        if i%18==17:
            current=records[-18:]
            print("CM row",meta["certificate_index"],"source points",sum(
                row["passing_abelian_fibres"]>0 for row in current),
                "passing abelian counts",sorted({row["passing_abelian_fibres"] for row in current}),flush=True)
    result={"quotient":"B/(gamma3(H) H^8)",
        "actual_source_points":432,
        "source_points_with_lifts":sum(row["passing_abelian_fibres"]>0 for row in records),
        "passing_abelian_count_distribution":dict(Counter(row["passing_abelian_fibres"] for row in records)),
        "complete_obstruction_value_count":len(obstruction_counts),
        "passing_CM_row_counts":[sum(row["passing_abelian_fibres"]>0 for row in records[18*i:18*i+18]) for i in range(24)],
        "central_correction_images_per_passing_value":2**16,
        "actual_word_examples":passing_examples,"records":records,
        "elapsed_seconds":round(time.time()-started,3)}
    (HERE/"bc_fermat_class_two_2adic_fibres.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ("records","actual_word_examples")},indent=2))
    print("PASS: complete P8 source affine lattice, Hall carries, central norm and generation.")

if __name__=="__main__":main()
