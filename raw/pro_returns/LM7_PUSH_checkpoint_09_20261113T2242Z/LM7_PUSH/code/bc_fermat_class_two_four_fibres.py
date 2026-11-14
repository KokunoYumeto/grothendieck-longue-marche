#!/usr/bin/env python3
"""All complete exponent-four H-class-two fibres over the 432 E24 points."""
from pathlib import Path
from unittest.mock import patch
import json,time
import numpy as np
from de_ferrari_two_core import Span2,solve2
import de_ferrari_two_family_words as family
import bc_fermat_class_two_four as q

HERE=Path(__file__).resolve().parent

class LinearSystem2:
    def __init__(self,matrix):
        self.matrix=np.asarray(matrix,dtype=np.int64)%2
        a=self.matrix.copy();u=np.eye(a.shape[0],dtype=np.int64);pivots=[];rank=0
        for j in range(a.shape[1]):
            nz=np.flatnonzero(a[rank:,j])
            if not len(nz):continue
            i=rank+int(nz[0]);a[[rank,i]]=a[[i,rank]];u[[rank,i]]=u[[i,rank]]
            for i in range(a.shape[0]):
                if i!=rank and a[i,j]:a[i]^=a[rank];u[i]^=u[rank]
            pivots.append(j);rank+=1
            if rank==a.shape[0]:break
        free=[i for i in range(a.shape[1]) if i not in pivots]
        kernel=np.zeros((a.shape[1],len(free)),dtype=np.int64)
        for col,j in enumerate(free):
            kernel[j,col]=1;kernel[pivots,col]=a[:rank,j]
        assert not np.any(self.matrix@kernel%2)
        self.transform=u;self.pivots=pivots;self.rank=rank;self.kernel=kernel
    def solve(self,rhs):
        b=self.transform@rhs%2
        if np.any(b[self.rank:]):return None
        result=np.zeros(self.matrix.shape[1],dtype=np.int64)
        result[self.pivots]=b[:self.rank]
        assert np.array_equal(self.matrix@result%2,rhs%2)
        return result

def main():
    started=time.time()
    kernel=np.load(HERE/"bc_fermat_class_two_four_kernel.npz")
    generators=kernel["parity_basis"];central=kernel["central_basis"]
    commcentral=kernel["commutator_central_basis"]
    assert generators.shape==(55,6) and central.shape==(55,45)
    assert commcentral.shape==(45,39)
    parity=Span2(10)
    for g in generators.T:assert parity.add(g[:10]%2,None)
    high=LinearSystem2(central[:10])
    integral=np.load(HERE/"bc_cm_fermat_boundary_integral.npz")
    D=integral["D"];E=integral["E"];primitive=integral["primitive_kernel"].reshape(6)
    metadata=json.loads((HERE/"bc_cm_fermat_boundary_integral.json").read_text())
    P3=np.array(metadata["odd_denominator_norm_correction_three_times_P"],dtype=np.int64)
    zrows=metadata["kernel_basis_inverse_coordinate_rows"]
    assert P3.shape==(6,8)
    assert np.array_equal(E@D@P3%4,3*E@np.array(
        metadata["primitive_F_prime_kernel_basis"],dtype=np.int64)%4)
    def lift_abelian(v):
        coefficients=parity.coordinates(v%2)
        out=q.ZERO.copy()
        for a,g in zip(coefficients,generators.T):
            if a:out=q.multiply(out,g)
        difference=(v-out[:10])%4;assert not np.any(difference%2)
        c=high.solve(difference//2)
        assert c is not None
        out=q.multiply(out,q.central_element(central@c%2))
        assert np.array_equal(out[:10],v%4)
        return out
    # The whole abelian correction image is exactly D mod4.
    assert high.rank==6
    for column in D.T:lift_abelian(column%4)
    central_rows=np.r_[np.arange(10,55),np.arange(65,110)]
    normcentral=np.stack([q.norm_errors(np.r_[np.zeros(10,dtype=np.int64),column])[central_rows]
                          for column in commcentral.T],axis=1)
    system=LinearSystem2(normcentral)
    print("Central correction dimension, norm rank and nullity:",39,system.rank,
          system.kernel.shape[1],flush=True)
    old=json.loads((HERE/"bc_cm_fermat_odd_boundary.json").read_text())["records"]
    derivative=np.load(HERE/"bc_cm_fermat_boundary.npz")["abelian_action_derivatives"]
    with patch.object(Path,"write_text",return_value=0):data=family.load_data()
    records=[];logs=[];cache={}
    for index in range(24):
        local=[]
        for row in family.family_words(data,index,lam=1):
            value=q.literal(row["literal_F_word"]);logs.append(value)
            original=np.asarray(old[len(records)]["integral_H_abelianization"],dtype=np.int64)
            assert np.array_equal(value[:10],original%4)
            particular=-3*(P3@original[zrows])%4
            assert not np.any((E@(value[:10]+D@particular))%4)
            fibres=[]
            for parameter in range(4):
                a=(particular+parameter*primitive)%4
                correction=lift_abelian(D@a%4)
                target=q.multiply(value,correction)
                errors=q.norm_errors(target)
                assert not np.any(errors[np.r_[np.arange(10),np.arange(55,65)]])
                coefficients=system.solve(errors[central_rows]%2)
                good=coefficients is not None
                central_correction=None;action_rank=None
                if good:
                    central_correction=commcentral@coefficients%2
                    candidate=q.multiply(target,np.r_[np.zeros(10,dtype=np.int64),central_correction])
                    assert not np.any(q.norm_errors(candidate))
                    action=np.eye(10,dtype=np.int64)+np.stack([a@candidate[:10] for a in derivative],axis=1)
                    action_rank=q.f.rank(action%2,p=2)
                    assert action_rank==10
                fibres.append({"abelian_parameter":parameter,
                    "target_abelianization":target[:10].tolist(),
                    "central_norm_solvable":good,
                    "particular_central_correction":None if central_correction is None else central_correction.tolist(),
                    "H_Frattini_action_rank":action_rank})
            count=sum(f["central_norm_solvable"] for f in fibres)
            result={"certificate_index":index,"ternary_parameters":row["ternary_parameters"],
                "binary_parameter":row["binary_parameter"],"abelian_fibres":fibres,
                "passing_abelian_fibres":count,
                "central_fibre_dimension":system.kernel.shape[1],
                "total_distinct_correction_images":count*2**system.kernel.shape[1]}
            records.append(result);local.append(result)
        print("CM row",index,":",sum(r["passing_abelian_fibres"]>0 for r in local),
              "of18 source points; abelian fibre counts",
              sorted({r["passing_abelian_fibres"] for r in local}),flush=True)
    output={"quotient":"B/(gamma_3(H) H^4)",
        "complete_source_kernel_order_exponent_two":51,
        "complete_source_kernel_abelian_type":"(Z/4)^6",
        "complete_source_kernel_commutator_central_dimension":39,
        "central_norm_rank":system.rank,
        "central_norm_kernel_dimension":system.kernel.shape[1],
        "source_points_with_a_lift":sum(r["passing_abelian_fibres"]>0 for r in records),
        "records":records,"elapsed_seconds":round(time.time()-started,3)}
    (HERE/"bc_fermat_class_two_four_fibres.json").write_text(json.dumps(output,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_two_four_fibres.npz",
                        source_word_values=np.stack(logs),central_norm_matrix=normcentral,
                        central_norm_kernel=system.kernel,
                        central_correction_space=commcentral)
    print("PASS: all complete exponent-four correction fibres and exact generation ranks.")
    print("Elapsed seconds:",round(time.time()-started,3),flush=True)

if __name__=="__main__":main()
