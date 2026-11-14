#!/usr/bin/env python3
"""Complete exponent-three class-three norm fibres over all E24 source points.

The input E33 data are read only.  Its exact source-kernel image lifts to
the complete new triple centre by actual commutators with H generators.
Consequently source compatibility is precisely the recorded affine
abelian condition, with every degree-two and degree-three coordinate
available.  For each of the nine admissible abelian values the two
literal B order relations form an affine system in 10+120 variables.
"""
from pathlib import Path
import hashlib,json,time
import numpy as np
import bc_fermat_class_three_burnside as q
from bc_fermat_class_two_fibres import LinearSystem

HERE=Path(__file__).resolve().parent
LOWER_ROWS=np.r_[np.arange(55),np.arange(q.DIM,q.DIM+55)]
TRIPLE_ROWS=np.r_[np.arange(55,q.DIM),np.arange(q.DIM+55,2*q.DIM)]

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    start=time.time()
    paths=[HERE/"bc_fermat_class_two_fibres.json",HERE/"bc_fermat_class_two_fibres.npz",
           HERE/"bc_fermat_class_two_kernel.json",HERE/"bc_fermat_class_two_kernel.npz"]
    hashes={p.name:sha(p) for p in paths}
    old=json.loads(paths[0].read_text())
    arrays=np.load(paths[1]);kernel=arrays["central_norm_kernel"]
    source_basis=np.load(paths[3])["basis"]
    assert kernel.shape==(45,10) and source_basis.shape==(55,51)
    old_system=LinearSystem(source_basis)
    # Exact old source preimages of each degree-two unit; linear addition
    # is realized by gh[g,h] in the exponent-three class-two quotient.
    commutator_preimages=[]
    for i,j in q.PAIRS:
        value=np.zeros(55,dtype=np.int64);value[10+q.PAIR_INDEX[i,j]]=1
        coefficients=old_system.solve(value)
        assert coefficients is not None
        commutator_preimages.append(coefficients)
    triple_preimages=[]
    for index,(i,j,k) in enumerate(q.TRIPLES):
        r=q.ZERO.copy();r[10+q.PAIR_INDEX[j,k]]=1
        actual=q.commutator(q.GENERATORS[i],r)
        expected=q.ZERO.copy();expected[55+index]=1
        assert np.array_equal(actual,expected)
        triple_preimages.append({"H_generator":i+1,"degree_two_pair":[j+1,k+1],
            "old_source_basis_coefficients":commutator_preimages[q.PAIR_INDEX[j,k]].tolist(),
            "word_operation":"[eta_i, r_jk]^4; r_jk uses successive log sums gh[g,h]"})
    # A source lift r_jk has arbitrary new triple coordinates; its bracket
    # is unchanged because this whole layer is central.
    triples_matrix=np.stack([q.norm_errors(np.eye(q.DIM,dtype=np.int64)[55+j])[TRIPLE_ROWS]
                             for j in range(120)],axis=1)
    triple_system=LinearSystem(triples_matrix)
    assert np.array_equal(triples_matrix[:120],(np.eye(120,dtype=np.int64)+q.S.triple)%3)
    assert np.array_equal(triples_matrix[120:],
        -(np.eye(120,dtype=np.int64)+q.R.triple+q.R.triple@q.R.triple)%3)
    print("New triple norm rank/nullity:",triple_system.rank,
          triple_system.kernel.shape[1],flush=True)
    targets={}
    for record in old["records"]:
        for fibre in record["abelian_fibres"]:
            if fibre["central_norm_solvable"]:
                key=tuple(fibre["target_abelianization"])
                z=np.asarray(fibre["particular_target_central"],dtype=np.int64)
                if key in targets:assert np.array_equal(targets[key],z)
                targets[key]=z
    assert len(targets)==9
    target_records=[];target_lookup={};saved={};counterexample=None
    for index,(key,z0) in enumerate(sorted(targets.items())):
        v=np.array(key,dtype=np.int64)
        origin=np.r_[v,z0,np.zeros(120,dtype=np.int64)]
        error=q.norm_errors(origin)
        assert not np.any(error[LOWER_ROWS])
        columns=[]
        for column in kernel.T:
            moved=origin.copy();moved[10:55]=(z0+column)%3
            delta=(q.norm_errors(moved)-error)%3
            assert not np.any(delta[LOWER_ROWS])
            columns.append(delta[TRIPLE_ROWS])
        z_matrix=np.stack(columns,axis=1)
        obstruction_matrix=triple_system.transform[triple_system.rank:]@z_matrix%3
        obstruction_value=triple_system.transform[triple_system.rank:]@error[TRIPLE_ROWS]%3
        obstruction_system=LinearSystem(obstruction_matrix)
        a0=obstruction_system.solve(-obstruction_value%3)
        full_matrix=np.hstack((z_matrix,triples_matrix))
        full_system=LinearSystem(full_matrix)
        solution=full_system.solve(-error[TRIPLE_ROWS]%3)
        assert (a0 is None)==(solution is None)
        record={"target_index":index,"abelianization":v.tolist(),
                "E33_particular_central":z0.tolist(),
                "old_central_parameter_obstruction_rank":obstruction_system.rank,
                "class_three_solvable":solution is not None,
                "joint_affine_norm_rank":full_system.rank,
                "joint_affine_norm_nullity":full_system.kernel.shape[1]}
        if solution is not None:
            candidate=origin.copy()
            candidate[10:55]=(z0+kernel@solution[:10])%3
            candidate[55:]=solution[10:]
            assert not np.any(q.norm_errors(candidate))
            record.update({"liftable_E33_central_parameter_count":3**(10-obstruction_system.rank),
                "class_three_fibre_over_each_liftable_E33_point":3**triple_system.kernel.shape[1],
                "total_class_three_points":3**full_system.kernel.shape[1],
                "particular_old_central_parameters":solution[:10].tolist(),
                "particular_triple_coordinates":solution[10:].tolist()})
            assert full_system.kernel.shape[1]==10-obstruction_system.rank+triple_system.kernel.shape[1]
            # Every affine direction is an actual zero norm variation.
            for delta in full_system.kernel.T:
                moved=candidate.copy()
                moved[10:55]=(moved[10:55]+kernel@delta[:10])%3
                moved[55:]=(moved[55:]+delta[10:])%3
                assert not np.any(q.norm_errors(moved))
        else:
            record.update({"liftable_E33_central_parameter_count":0,
                           "total_class_three_points":0})
        if counterexample is None and obstruction_system.rank:
            for coordinate in range(10):
                a=np.zeros(10,dtype=np.int64);a[coordinate]=1
                value=(obstruction_matrix@a+obstruction_value)%3
                if not np.any(value):continue
                bad=origin.copy();bad[10:55]=(z0+kernel@a)%3
                bad_error=q.norm_errors(bad)
                assert not np.any(bad_error[LOWER_ROWS])
                assert triple_system.solve(-bad_error[TRIPLE_ROWS]%3) is None
                row=int(np.flatnonzero(value)[0])
                functional=triple_system.transform[triple_system.rank+row]
                assert not np.any(functional@triples_matrix%3)
                assert int(functional@bad_error[TRIPLE_ROWS]%3)!=0
                counterexample={"target_index":index,"E33_coordinates":bad[:55].tolist(),
                    "old_central_parameter_unit":coordinate,
                    "triple_obstruction_value":int(functional@bad_error[TRIPLE_ROWS]%3),
                    "annihilating_functional":functional.tolist(),
                    "equation_order":"first 120: (sf)^2; last 120: (f^-1 r)^3"}
                break
        # E33's actual H generator map is already of full rank on its
        # Frattini quotient; the central lift cannot change that matrix.
        ab_map,_=q.f.generator_images(v,z0,chi=1)
        assert q.f.rank(ab_map)==10
        record["literal_H_Frattini_rank"]=10
        print("Target",index,"old central obstruction rank",obstruction_system.rank,
              "lift",solution is not None,"new affine dimension",full_system.kernel.shape[1],flush=True)
        target_lookup[key]=record
        target_records.append(record)
        saved[f"target_{index}_obstruction_matrix"]=obstruction_matrix
        saved[f"target_{index}_obstruction_value"]=obstruction_value
        saved[f"target_{index}_norm_matrix"]=full_matrix
        saved[f"target_{index}_norm_kernel"]=full_system.kernel
        if solution is not None:saved[f"target_{index}_norm_particular"]=solution
    records=[]
    for oldrecord in old["records"]:
        passing=[target_lookup[tuple(fibre["target_abelianization"])]
                 for fibre in oldrecord["abelian_fibres"] if fibre["central_norm_solvable"]]
        total=sum(r["total_class_three_points"] for r in passing)
        result={"certificate_index":oldrecord["certificate_index"],
                "ternary_parameters":oldrecord["ternary_parameters"],
                "binary_parameter":oldrecord["binary_parameter"],
                "target_indices":[r["target_index"] for r in passing],
                "class_three_lift_exists":bool(total),
                "class_three_correction_image_count":total,
                "E33_points_that_lift":sum(r["liftable_E33_central_parameter_count"] for r in passing),
                "E33_points_in_full_fibre":3**11}
        records.append(result)
    assert len(records)==432
    # The chosen nonlifting target belongs to actual source fibres; retain one.
    if counterexample is not None:
        matches=[r for r in records if counterexample["target_index"] in r["target_indices"]]
        assert matches
        counterexample["actual_source_point"]={k:matches[0][k] for k in
                     ("certificate_index","ternary_parameters","binary_parameter")}
    assert hashes=={p.name:sha(p) for p in paths}
    result={"status":"work in progress; finite norms computed",
            "quotient":"B/(gamma_4(H) H^3)",
            "source":"all 432 multiplier-one E24 points in the actual D23 common source",
            "complete_source_kernel_dimensions":[6,45,120],
            "triple_norm_rank":triple_system.rank,
            "triple_norm_nullity":triple_system.kernel.shape[1],
            "class_three_source_points_surviving":sum(r["class_three_lift_exists"] for r in records),
            "complete_fibre_counts":sorted({r["class_three_correction_image_count"] for r in records}),
            "liftable_E33_fibre_counts":sorted({r["E33_points_that_lift"] for r in records}),
            "new_obstruction_example":counterexample,
            "target_records":target_records,"source_records":records,
            "triple_word_preimages":triple_preimages,
            "protected_input_hashes":hashes,"protected_inputs_unchanged":True,
            "elapsed_seconds":round(time.time()-start,3)}
    (HERE/"bc_fermat_class_three_norms.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_three_norms.npz",triple_norm_matrix=triples_matrix,
        triple_norm_kernel=triple_system.kernel,source_degree_two_preimages=np.stack(commutator_preimages),
        **saved)
    print(json.dumps({k:v for k,v in result.items() if k not in
        ("new_obstruction_example","target_records","source_records","triple_word_preimages")},indent=2))
    print("PASS: complete finite class-three norm systems and all 432 actual source fibres.")

if __name__=="__main__":main()
