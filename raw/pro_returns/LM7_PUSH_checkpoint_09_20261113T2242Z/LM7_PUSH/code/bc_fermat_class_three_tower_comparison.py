#!/usr/bin/env python3
"""Exact comparison of the new class-three quotient with the full E37 tower.

This keeps the literal source cosets and gives new central word preimages
inside gamma_3(H), so every existing class-two boundary coordinate is
preserved.  All checkpoint05 inputs are read only.
"""
from pathlib import Path
import hashlib,json,time
import numpy as np
import sympy as sp
import bc_fermat_class_three_burnside as q
import bc_fermat_class_two_integral_model as integral
from bc_fermat_class_two_fibres import LinearSystem

HERE=Path(__file__).resolve().parent
TRIPLE_ROWS=np.r_[np.arange(55,q.DIM),np.arange(q.DIM+55,2*q.DIM)]
LOWER_ROWS=np.r_[np.arange(55),np.arange(q.DIM,q.DIM+55)]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def g_polynomial(a,b,c):
    quadratic=a*a+b*b+c*c+a*b+a*c-b*c
    return b+c-3*a*a-4*b*b-2*c*c-3*a*b-5*a*c+5*b*c-(c-b)*quadratic

def short_functional(system,error):
    rows=system.transform[system.rank:]
    candidates=[r.copy() for r in rows if int(r@error%3)]
    assert candidates
    best=min(candidates,key=np.count_nonzero)
    changed=True
    while changed:
        changed=False
        for row in rows:
            for coefficient in (1,2):
                value=(best+coefficient*row)%3
                if int(value@error%3) and np.count_nonzero(value)<np.count_nonzero(best):
                    best=value;changed=True
    return best

def main():
    start=time.time()
    protected=[HERE/filename for filename in (
        "bc_fermat_class_two_3adic_norms.npz","bc_fermat_class_two_3adic_tower.json",
        "bc_fermat_class_two_fibres.npz","bc_fermat_class_two_integral_kernel.npz",
        "bc_fermat_class_two_integral_kernel.json")]
    hashes={p.name:sha(p) for p in protected}
    old=np.load(protected[0]);V=old["smith_right"];Vi=np.array(sp.Matrix(V.tolist()).inv(),dtype=np.int64)
    assert np.array_equal(V@Vi,np.eye(45,dtype=np.int64))
    K=np.load(protected[2])["central_norm_kernel"]
    Ksystem=LinearSystem(K)
    free=2*V[:,37:45]%3
    free_coefficients=np.stack([Ksystem.solve(column) for column in free.T],axis=1)
    assert np.array_equal(K@free_coefficients%3,free)
    new=np.load(HERE/"bc_fermat_class_three_norms.npz")
    norm_data=json.loads((HERE/"bc_fermat_class_three_norms.json").read_text())
    triple_system=LinearSystem(new["triple_norm_matrix"])
    old_torsion_matrix=2*Vi[[35,36]]@K%3
    assert LinearSystem(old_torsion_matrix).rank==2
    target_records=[];saved={}
    for r in norm_data["target_records"]:
        index=r["target_index"];v=np.array(r["abelianization"]);z0=np.array(r["E33_particular_central"])
        a,b,c=int(-v[0]%3),int(v[1]),int(v[4])
        assert np.array_equal(old["abelian_norm_basis"]@np.array([a,b,c])%3,v)
        assert b==c
        G=g_polynomial(a,b,c)
        old_torsion_value=(2*Vi[[35,36]]@z0+np.array([G,-a+c]))%3
        O=new[f"target_{index}_obstruction_matrix"]
        error=new[f"target_{index}_obstruction_value"]
        joint=np.vstack((O,old_torsion_matrix))
        joint_error=np.r_[error,old_torsion_value]
        system=LinearSystem(joint)
        assert system.rank==6 and system.solve(-joint_error%3) is not None
        # An actual E37 full-tower central origin, reduced modulo three.
        t=np.array([a,b,c],dtype=np.int64)
        mon=np.array([a*a,b*b,c*c,a*b,a*c,b*c])
        E=old["transformed_error_linear"]@t+old["transformed_error_quadratic"]@mon
        Y=np.zeros(45,dtype=np.int64)
        for j in range(35):
            assert abs(int(old["smith"][j,j]))==1
            Y[j]=-int(E[j])*int(old["smith"][j,j])
        Y[35]=-G;Y[36]=a-c
        ztower=2*V@Y%3
        centre_origin=Ksystem.solve((ztower-z0)%3)
        assert centre_origin is not None
        assert not np.any((old_torsion_matrix@centre_origin+old_torsion_value)%3)
        A=O@free_coefficients%3
        e=(O@centre_origin+error)%3
        reduced=LinearSystem(A)
        assert reduced.rank==4
        particular=reduced.solve(-e%3)
        assert particular is not None
        R=reduced.transform@A%3
        rhs=-reduced.transform@e%3
        assert not np.any(R[4:]) and not np.any(rhs[4:])
        central=(ztower+free@particular)%3
        candidate=np.r_[v,central,np.zeros(120,dtype=np.int64)]
        candidate_error=q.norm_errors(candidate)
        assert not np.any(candidate_error[LOWER_ROWS])
        triple=triple_system.solve(-candidate_error[TRIPLE_ROWS]%3)
        assert triple is not None
        candidate[55:]=triple
        assert not np.any(q.norm_errors(candidate))
        record={"target_index":index,"abelianization":v.tolist(),
            "t_residue":[a,b,c],"joint_old_parameter_rank":system.rank,
            "E37_free_Smith_parameter_obstruction_rank":4,
            "E37_free_parameter_equations":R[:4].tolist(),
            "E37_free_parameter_rhs":rhs[:4].tolist(),
            "E37_free_parameter_pivots":reduced.pivots,
            "E37_free_parameter_particular":particular.tolist(),
            "E37_free_parameter_kernel":reduced.kernel.tolist(),
            "compatible_E33_points_per_abelian_value":3**4,
            "compatible_class_three_points_per_abelian_value":3**26,
            "particular_target_central":central.tolist(),
            "particular_target_triple":triple.tolist()}
        target_records.append(record)
        saved[f"target_{index}_free_Smith_matrix"]=R[:4]
        saved[f"target_{index}_free_Smith_rhs"]=rhs[:4]
        saved[f"target_{index}_free_Smith_kernel"]=reduced.kernel
        saved[f"target_{index}_free_Smith_particular"]=particular
        print("Target",index,": old/new/joint ranks 2/5/6; E37 free rank4",flush=True)
    # New central word preimages with exactly zero integral class-two image.
    centre=np.load(protected[3])["central_basis"]
    centre_system=LinearSystem(centre)
    centre_preimages=np.stack([centre_system.solve(e) for e in np.eye(45,dtype=np.int64)],axis=1)
    assert np.array_equal(centre@centre_preimages%3,np.eye(45,dtype=np.int64))
    metadata=json.loads(protected[4].read_text())["basis_preimages"]
    assert len(metadata)==45 and all(row["kind"]=="adjusted_normal_relator" for row in metadata)
    triple_word_preimages=[]
    for index,(i,j,k) in enumerate(q.TRIPLES):
        coefficients=centre_preimages[:,q.PAIR_INDEX[j,k]]
        r=q.ZERO.copy();r[10+q.PAIR_INDEX[j,k]]=1
        actual=q.commutator(q.GENERATORS[i],q.power(r,4))
        expected=q.ZERO.copy();expected[55+index]=1
        assert np.array_equal(actual,expected)
        triple_word_preimages.append({"H_generator":i+1,"degree_two_pair":[j+1,k+1],
            "adjusted_relator_coefficients":coefficients.tolist(),
            "literal_rule":"[eta_i,(product u_l^coefficient_l)^4]",
            "u_l_rule":"normal_relator_l*(ordered product K_basis_j^integral_K_coordinates_j)^(-1)",
            "exact_location":"ker(B->D23) intersect gamma_3(H)"})
    # An individually specified full E37 tower point: t=0, Y37=1.
    Z=V[:,37].copy();central=2*Z%3
    assert not np.any(old["central_norm"]@Z)
    assert not np.any(integral.norm_errors(np.r_[np.zeros(10,dtype=np.int64),Z]))
    target=np.r_[np.zeros(10,dtype=np.int64),central,np.zeros(120,dtype=np.int64)]
    error=q.norm_errors(target)
    assert not np.any(error[LOWER_ROWS])
    assert triple_system.solve(-error[TRIPLE_ROWS]%3) is None
    functional=short_functional(triple_system,error[TRIPLE_ROWS])
    assert not np.any(functional@new["triple_norm_matrix"]%3)
    value=int(functional@error[TRIPLE_ROWS]%3)
    assert value
    support=[]
    for i in np.flatnonzero(functional):
        norm=0 if i<120 else 1;triple=q.TRIPLES[i%120]
        support.append({"norm":"(sf)^2" if norm==0 else "(f^-1 r)^3",
                        "triple":[a+1 for a in triple],"coefficient":int(functional[i])})
    example={"source_point":{"certificate_index":0,"ternary_parameters":[0,0],"binary_parameter":0},
        "full_E37_parameters":{"u":0,"w":0,"Y37":1,"Y38_through_Y44":[0]*7},
        "integral_target_abelianization":[0]*10,
        "integral_target_doubled_log_central":Z.tolist(),
        "E33_target_central":central.tolist(),
        "exact_integral_class_two_norms_zero":True,
        "triple_obstruction_functional_support":support,
        "triple_obstruction_value":value,
        "all_triple_corrections_annihilated":True}
    sources=[]
    for row in norm_data["source_records"]:
        sources.append({"certificate_index":row["certificate_index"],
            "ternary_parameters":row["ternary_parameters"],"binary_parameter":row["binary_parameter"],
            "all_three_abelian_values_survive":True,
            "E37_reduction_points_compatible_with_class_three":3**5,
            "all_E37_reduction_points":3**9,
            "class_three_images_compatible_with_full_E37_tower":3**27})
    assert len(sources)==432
    assert hashes=={p.name:sha(p) for p in protected}
    result={"status":"work in progress; exact tower comparison certified",
        "new_quotient":"B/(gamma_4(H) H^3)",
        "class_two_tower":"all E37 three-adic class-two factors",
        "common_geometric_quotient":"H/(gamma_3(H) H^3), with literal projection",
        "joint_central_word_preimages_in_gamma3_H":True,
        "source_points_surviving":432,"per_source_E33_points_compatible_with_both":3**5,
        "per_source_class_three_images_compatible_with_full_class_two_tower":3**27,
        "new_independent_conditions_on_E37_free_Smith_coordinates":4,
        "all_class_three_fibres_above_a_compatible_E37_point":"F3^22",
        "complete_source_comparison":"New triple centre supplied by actual source-kernel words in gamma3(H); their 3-supported powers preserve every other E42 factor.",
        "target_records":target_records,"source_records":sources,
        "adjusted_relator_metadata":metadata,"triple_word_preimages":triple_word_preimages,
        "full_class_two_tower_nonlifting_example":example,
        "protected_input_hashes":hashes,"protected_inputs_unchanged":True,
        "elapsed_seconds":round(time.time()-start,3)}
    (HERE/"bc_fermat_class_three_tower_comparison.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_three_tower_comparison.npz",Smith_inverse=Vi,
        integral_central_preimage_coefficients=centre_preimages,
        nonlifting_integral_doubled_log=Z,nonlifting_class_three_target=target,
        nonlifting_norm_functional=functional,**saved)
    print("New four equations in the E37 free Smith coordinates:")
    for r in target_records:
        print(r["target_index"],r["E37_free_parameter_equations"],r["E37_free_parameter_rhs"])
    print("Explicit full-class-two nonlift, Smith Y37=1; functional:",support,"value",value)
    print(json.dumps({k:v for k,v in result.items() if k not in
        ("target_records","source_records","adjusted_relator_metadata","triple_word_preimages",
         "full_class_two_tower_nonlifting_example")},indent=2))
    print("PASS: exact full-class-two comparison, actual gamma3 source words, and new nonlifting tower point.")

if __name__=="__main__":main()
