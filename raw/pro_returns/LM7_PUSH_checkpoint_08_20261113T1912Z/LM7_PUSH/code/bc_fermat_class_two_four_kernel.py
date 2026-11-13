#!/usr/bin/env python3
"""Complete binary source-kernel image in B/(gamma_3(H)H^4).

The seven-dimensional elementary-abelian binary F-prime source image
gives 5458 actual normal relators.  All are evaluated with the Hall
collector retaining squares; the target subgroup is then closed under
the actual B action using its parity and central Frattini coordinates.
"""
from pathlib import Path
from unittest.mock import patch
from itertools import combinations
import json,time
import numpy as np
from de_ferrari_two_model import FerrariTwo
from de_ferrari_two_core import InducedTwo,Span2,chunk_trie,solve2
import de_ferrari_two_family_words as family
import de_fermat_schreier as f
import bc_fermat_class_two_four as q

HERE=Path(__file__).resolve().parent

class Subgroup:
    def __init__(self):
        self.parity=Span2(10);self.central=Span2(55)
        self.generators=[];self.parity_origins=[];self.central_origins=[]
    def add_central(self,value,origin):
        c=q.central_vector(value)
        if self.central.add(c,origin):
            self.central_origins.append(origin)
            return True
        return False
    def add(self,value,origin):
        residue,coordinates=self.parity.reduce(value[:10]%2)
        if np.any(residue):
            i=len(self.generators)
            assert self.parity.add(value[:10]%2,origin)
            self.generators.append(value.copy());self.parity_origins.append(origin)
            self.add_central(q.power(value,2),{"kind":"parity_basis_square","basis_index":i})
            for j,other in enumerate(self.generators[:-1]):
                self.add_central(q.commutator(value,other),
                    {"kind":"parity_basis_commutator","basis_indices":[i,j]})
            return True
        rep=q.ZERO.copy()
        coefficients=coordinates[:len(self.generators)]
        for power,g in zip(coefficients,self.generators):
            if power:rep=q.multiply(rep,g)
        return self.add_central(q.multiply(value,q.inverse(rep)),
            {"kind":"parity_reduction","source":origin,
             "parity_basis_coefficients":coefficients.tolist()})
    def contains(self,value):
        residue,coordinates=self.parity.reduce(value[:10]%2)
        if np.any(residue):return False
        rep=q.ZERO.copy()
        for power,g in zip(coordinates[:len(self.generators)],self.generators):
            if power:rep=q.multiply(rep,g)
        return not np.any(self.central.reduce(q.central_vector(
            q.multiply(value,q.inverse(rep))))[0])
    def close(self):
        a=b=0
        while a<len(self.generators) or b<len(self.central.basis):
            if a<len(self.generators):
                value=self.generators[a].copy()
                for name,action in (("s",q.S),("r",q.R)):
                    self.add(action(value),{"kind":"parity_basis_conjugation",
                                            "letter":name,"basis_index":a})
                a+=1
            else:
                value=q.central_element(self.central.basis[b])
                for name,action in (("s",q.S),("r",q.R)):
                    self.add_central(action(value),{"kind":"central_basis_conjugation",
                                                    "letter":name,"basis_index":b})
                b+=1

def main():
    started=time.time()
    with patch.object(Path,"write_text",return_value=0):
        data=family.load_data()
    d=data["d"];model=FerrariTwo(6);W=InducedTwo(model,d,4)
    ns=[W.word(w) for w in d["Nwords"]]
    W.chunks=chunk_trie(d,ns,W)
    source=json.loads((HERE/"de_ferrari_two_degree6_module.json").read_text())
    source_arrays=np.load(HERE/"de_ferrari_two_degree6_module.npz")
    CM=source_arrays["F_prime_basis"];basis_words=source["F_prime_basis_words"]
    C=Span2(CM.shape[0])
    for column,word in zip(CM.T,basis_words):assert C.add(column,word)
    assert len(C.basis)==7
    old_elements=[W.element(column) for column in CM.T]
    for i,g in enumerate(old_elements):
        assert W.equal(W.power(g,2),W.one)
        assert W.equal(W.word(basis_words[i]),g)
        for j,h in enumerate(old_elements):
            assert np.array_equal(W.vector(W.mul(g,h)),(CM[:,i]+CM[:,j])%2)
    ext=q.FExtension()
    nwords=json.loads((HERE/"bc_cm_literal_words.json").read_text())["N_B_basis_in_F"]
    target_ns=[ext.word(w) for w in nwords]
    basis_fwords=[d["fword"](w) for w in basis_words]
    basis=[q.literal(w) for w in basis_fwords]
    hab=np.stack([f.integral_abel(w) for w in basis_fwords],axis=1)
    target_powers=[ext.power(n,6) for n in target_ns]
    power_vectors=np.column_stack([W.vector(W.power(n,6)) for n in ns])
    power_hab=np.stack([f.integral_abel(w*6) for w in nwords],axis=1)
    power_kernel=np.load(HERE/"de_ferrari_mod9_module.npz")["integral_abelianization_kernel"]
    cover=np.load(HERE/"bc_cm_fermat_factorization.npz")
    translation=cover["translation"]
    actions=[np.eye(10,dtype=np.int64),translation,translation@translation]
    subgroup=Subgroup();metadata=[];values=[];integral_values=[]

    def add(seed,ab,kind,indices,coefficients=None):
        representative=q.ZERO.copy()
        if coefficients is not None:
            for coefficient,g in zip(coefficients,basis):
                if coefficient:representative=q.multiply(representative,g)
            seed=q.multiply(seed,q.inverse(representative))
            ab=ab-hab@coefficients
        assert np.array_equal(seed[:10],ab%4)
        index=len(values);values.append(seed);integral_values.append(ab)
        metadata.append({"kind":kind,"indices":indices,
                         "image_coefficients":None if coefficients is None else coefficients.tolist()})
        subgroup.add(seed,{"kind":"normal_relator","normal_relator_index":index})

    for col,(i,j) in enumerate(combinations(range(97),2)):
        coefficients=C.coordinates(W.vector(W.comm(ns[i],ns[j])))
        deck,value=ext.comm(target_ns[i],target_ns[j]);assert deck==(0,0)
        add(value,cover["N_B_commutator_images"][:,col],"N_commutator",[i,j],coefficients)
        if (col+1)%1000==0:print("Binary normal commutator relators:",col+1,flush=True)
    for j,column in enumerate(power_kernel.T):
        coefficients=C.coordinates(power_vectors@column%2)
        value=q.ZERO.copy()
        for a,g in zip(column,target_powers):
            assert g[0]==(0,0)
            if a:value=q.multiply(value,q.power(g[1],int(a)))
        add(value,power_hab@column,"F_prime_sixth_powers",[j],coefficients)
    for i,g in enumerate(basis):add(q.power(g,2),2*hab[:,i],"basis_square",[i])
    for i,j in combinations(range(7),2):
        add(q.commutator(basis[i],basis[j]),np.zeros(10,dtype=np.int64),
            "basis_commutator",[i,j])
    for i,g in enumerate(old_elements):
        for j,n in enumerate(ns):
            coefficients=C.coordinates(W.vector(W.conj(n,g)))
            deck,value=ext.conj(target_ns[j],((0,0),basis[i]));assert deck==(0,0)
            exponent=sum(1 if a==1 else -1 if a==-1 else 0 for a in nwords[j])%3
            add(value,actions[exponent]@hab[:,i],"N_conjugation",[i,j],coefficients)
        print("Binary basis conjugation rows:",i+1,flush=True)
    assert len(values)==5458
    initial=[len(subgroup.generators),len(subgroup.central.basis)]
    subgroup.close()
    for value in values:assert subgroup.contains(value)
    for action in (q.S,q.R):
        for value in subgroup.generators:assert subgroup.contains(action(value))
        for value in subgroup.central.basis:
            assert subgroup.contains(action(q.central_element(value)))
    central=subgroup.central.matrix()
    high=Span2(10)
    for value in central[:10].T:high.add(value,None)
    h=len(high.basis);u=len(subgroup.generators);c=len(subgroup.central.basis)
    zero=np.zeros(10,dtype=np.int64)
    solved=solve2(central[:10],zero);assert solved is not None
    commutator_central=central[10:]@solved[1]%2
    assert f.rank(commutator_central,p=2)==c-h
    output={"quotient":"B/(gamma_3(H)H^4)",
        "source_kernel":"ker(B->D2,6) intersect F-prime",
        "complete_normal_relators_evaluated":len(values),
        "initial_parity_and_Frattini_dimensions":initial,
        "parity_image_dimension":u,"central_Frattini_intersection_dimension":c,
        "abelian_high_bit_dimension":h,
        "commutator_central_intersection_dimension":c-h,
        "total_kernel_image_order_exponent_two":u+c,
        "abelian_image_order_exponent_two":u+h,
        "basis_F_prime_words_B":basis_words,
        "normal_relator_metadata":metadata,
        "parity_basis_preimages":subgroup.parity_origins,
        "central_basis_preimages":subgroup.central_origins,
        "binary_source_basis_elementary_abelian_verified":True,
        "all_H_abelian_projections_verified_integrally":True,
        "joint_ternary_comparison":"Cube each binary-kernel element and use its third power again; ninth powers retain the exponent-four target and kill the exponent-three ternary K6 image.",
        "elapsed_seconds":round(time.time()-started,3)}
    (HERE/"bc_fermat_class_two_four_kernel.json").write_text(json.dumps(output,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_two_four_kernel.npz",
        parity_basis=np.stack(subgroup.generators,axis=1),central_basis=central,
        commutator_central_basis=commutator_central,
        normal_relator_values=np.stack(values),
        original_relation_boundary_matrix=np.stack(integral_values,axis=1),
        old_prime_basis_values=np.stack(basis))
    print(json.dumps({k:v for k,v in output.items() if "preimages" not in k and
                     k not in ("normal_relator_metadata","basis_F_prime_words_B")},indent=2))
    print("PASS: complete binary source-kernel image with every Hall square retained.")

if __name__=="__main__":main()
