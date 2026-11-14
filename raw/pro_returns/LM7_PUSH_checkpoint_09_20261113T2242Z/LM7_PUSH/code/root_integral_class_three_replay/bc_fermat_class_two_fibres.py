#!/usr/bin/env python3
"""Complete H-class-two norm fibres over all 432 retained E24 words."""
from pathlib import Path
from unittest.mock import patch
from itertools import product
import json,time
import numpy as np
from de_ferrari_mod9_lift import Span
import de_ferrari_two_family_words as family
import bc_fermat_class_two as q

HERE=Path(__file__).resolve().parent

class LinearSystem:
    def __init__(self,matrix):
        self.matrix=np.asarray(matrix,dtype=np.int64)%3
        a=self.matrix.copy();u=np.eye(a.shape[0],dtype=np.int64);pivots=[]
        rank=0
        for j in range(a.shape[1]):
            nz=np.flatnonzero(a[rank:,j])
            if not len(nz):continue
            k=rank+int(nz[0])
            a[[rank,k]]=a[[k,rank]];u[[rank,k]]=u[[k,rank]]
            scale=int(a[rank,j])
            a[rank]=scale*a[rank]%3;u[rank]=scale*u[rank]%3
            for i in range(a.shape[0]):
                if i!=rank and a[i,j]:
                    c=int(a[i,j]);a[i]=(a[i]-c*a[rank])%3;u[i]=(u[i]-c*u[rank])%3
            pivots.append(j);rank+=1
            if rank==a.shape[0]:break
        free=[j for j in range(a.shape[1]) if j not in pivots]
        kernel=np.zeros((a.shape[1],len(free)),dtype=np.int64)
        for col,j in enumerate(free):
            kernel[j,col]=1
            kernel[pivots,col]=-a[:rank,j]%3
        assert not np.any(self.matrix@kernel%3)
        assert np.array_equal(u@self.matrix%3,a)
        self.transform=u;self.pivots=pivots;self.rank=rank;self.kernel=kernel
    def solve(self,rhs):
        b=self.transform@rhs%3
        if np.any(b[self.rank:]):return None
        solution=np.zeros(self.matrix.shape[1],dtype=np.int64)
        solution[self.pivots]=b[:self.rank]
        assert np.array_equal(self.matrix@solution%3,np.asarray(rhs)%3)
        return solution

def main():
    started=time.time()
    kernel=np.load(HERE/"bc_fermat_class_two_kernel.npz")["basis"]
    assert kernel.shape==(55,51)
    abspan=Span(10)
    for column in kernel[:10].T:abspan.add(column,None)
    ab=abspan.matrix()
    assert ab.shape==(10,6)
    abnorm=np.vstack((np.eye(10,dtype=np.int64)+q.S[:10,:10],
                      np.eye(10,dtype=np.int64)+q.R[:10,:10]+q.R[:10,:10]@q.R[:10,:10]))%3
    ab_system=LinearSystem(abnorm@ab%3)
    assert ab_system.rank==4 and ab_system.kernel.shape==(6,2)
    central_rows=np.r_[np.arange(10,55),np.arange(65,110)]
    central_matrix=np.stack([q.norm_errors(np.eye(55,dtype=np.int64)[10+j])[central_rows]
                             for j in range(45)],axis=1)
    central_system=LinearSystem(central_matrix)
    assert central_system.kernel.shape[0]==45
    print("Exact central norm rank and nullity:",central_system.rank,
          central_system.kernel.shape[1],flush=True)
    with patch.object(Path,"write_text",return_value=0):
        data=family.load_data()
    old=json.loads((HERE/"bc_cm_fermat_odd_boundary.json").read_text())["records"]
    records=[];logs=[];cached={}
    for index in range(24):
        local=[]
        for row in family.family_words(data,index,lam=1):
            value=q.literal(row["literal_F_word"])
            oldrow=old[len(records)]
            assert row["certificate_index"]==oldrow["certificate_index"]
            assert row["ternary_parameters"]==oldrow["ternary_parameters"]
            assert row["binary_parameter"]==oldrow["binary_parameter"]
            assert np.array_equal(value[:10],
                    np.asarray(oldrow["integral_H_abelianization"],dtype=np.int64)%3)
            logs.append(value)
            particular=ab_system.solve(-abnorm@value[:10]%3)
            assert particular is not None
            fibres=[]
            for parameters in product(range(3),repeat=2):
                a=(particular+ab_system.kernel@np.array(parameters,dtype=np.int64))%3
                v=(value[:10]+ab@a)%3
                key=tuple(v.tolist())
                if key not in cached:
                    target=np.r_[v,np.zeros(45,dtype=np.int64)]
                    errors=q.norm_errors(target)
                    assert not np.any(errors[np.r_[np.arange(10),np.arange(55,65)]])
                    z=central_system.solve(-errors[central_rows]%3)
                    if z is not None:
                        candidate=np.r_[v,z]
                        assert not np.any(q.norm_errors(candidate))
                    cached[key]=z
                z=cached[key]
                fibres.append({"abelian_parameters":list(parameters),
                               "target_abelianization":v.tolist(),
                               "central_norm_solvable":z is not None,
                               "particular_target_central":None if z is None else z.tolist()})
            passing=sum(x["central_norm_solvable"] for x in fibres)
            result={"certificate_index":index,"ternary_parameters":row["ternary_parameters"],
                    "binary_parameter":row["binary_parameter"],"abelian_fibres":fibres,
                    "passing_abelian_fibres":passing,
                    "central_fibre_dimension":central_system.kernel.shape[1],
                    "total_distinct_correction_images":passing*3**central_system.kernel.shape[1]}
            records.append(result);local.append(result)
        print("CM row",index,":",sum(r["passing_abelian_fibres"]>0 for r in local),
              "of18 source points; abelian fibre counts",
              sorted({r["passing_abelian_fibres"] for r in local}),flush=True)
    assert len(records)==432
    result={"quotient":"B/(gamma_3(H) H^3)",
        "source_family":"All432 multiplier-one E24 points, literal F-word reconstruction",
        "complete_source_kernel_image_dimension":51,
        "complete_source_kernel_abelian_dimension":6,
        "complete_source_kernel_central_dimension":45,
        "abelian_norm_rank_on_kernel_image":ab_system.rank,
        "abelian_norm_kernel_dimension":ab_system.kernel.shape[1],
        "central_norm_rank":central_system.rank,
        "central_norm_kernel_dimension":central_system.kernel.shape[1],
        "distinct_target_abelian_vectors_tested":len(cached),
        "source_points_with_a_lift":sum(r["passing_abelian_fibres"]>0 for r in records),
        "all_finite_norm_solutions_generate_joint_source":True,
        "records":records,"elapsed_seconds":round(time.time()-started,3)}
    (HERE/"bc_fermat_class_two_fibres.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_two_fibres.npz",
                        source_word_logs=np.stack(logs),abelian_kernel_image=ab,
                        abelian_norm_matrix=abnorm,abelian_norm_kernel=ab_system.kernel,
                        central_norm_matrix=central_matrix,
                        central_norm_kernel=central_system.kernel)
    print("PASS: complete class-two correction fibres over all432 literal source points.")
    print("Elapsed seconds:",round(time.time()-started,3),flush=True)

if __name__=="__main__":main()
