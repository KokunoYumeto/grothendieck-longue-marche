#!/usr/bin/env python3
"""Exact integral source lattice and central kernel for the binary tower."""
from pathlib import Path
from unittest.mock import patch
from itertools import combinations
import json,time
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
import de_ferrari_two_family_words as family
import bc_fermat_class_two_integral_model as q
from bc_fermat_class_two_integral_extension import FExtension,hall_coordinates

HERE=Path(__file__).resolve().parent

def main():
    started=time.time()
    old=json.loads((HERE/"bc_fermat_class_two_four_kernel.json").read_text())
    finite=np.load(HERE/"bc_fermat_class_two_four_kernel.npz")
    Rabel=finite["original_relation_boundary_matrix"]
    K=hermite_normal_form(sp.Matrix(Rabel))
    assert np.array_equal(np.array(K,dtype=np.int64),
                         np.load(HERE/"bc_cm_fermat_kernel_boundary.npz")["kernel_boundary_basis"])
    zrows=[0,1,3,4,5,7,8,9]
    selected=[];current=np.zeros((10,0),dtype=np.int64);rows=[];inverse=None;den=1
    for j,v in enumerate(Rabel.T):
        if not np.any(v):continue
        member=False
        if current.shape[1]:
            numerator=inverse@v[rows]
            if not np.any(numerator%den):
                coefficients=numerator//den
                member=np.array_equal(current@coefficients,v)
        if member:continue
        selected.append(j)
        current=np.array(hermite_normal_form(sp.Matrix(Rabel[:,selected])),dtype=np.int64)
        rows=list(sp.Matrix(current.T).rref()[1])
        rational=sp.Matrix(current[rows]).inv()
        den=int(sp.ilcm(1,*[a.q for a in rational]))
        inverse=np.array(den*rational,dtype=np.int64)
        if np.array_equal(current,np.array(K,dtype=np.int64)):break
    assert np.array_equal(current,np.array(K,dtype=np.int64))
    A=sp.Matrix(Rabel[np.ix_(zrows,selected)])
    SD,SU,SV=map(lambda x:x.to_Matrix(),smith_normal_decomp(
        DomainMatrix.from_Matrix(A).convert_to(sp.ZZ)))
    assert SD==SU*A*SV
    coefficients=SV[:,:8]*sp.diag(*[1/SD[i,i] for i in range(8)])*SU*K[zrows,:]
    assert all(a.q==1 for a in coefficients)
    assert sp.Matrix(Rabel[:,selected])*coefficients==K
    coeff=np.array(coefficients,dtype=np.int64)
    print("Actual selected integral source relators:",selected,flush=True)
    print("Largest lattice-word coefficient:",int(np.abs(coeff).max()),flush=True)

    with patch.object(Path,"write_text",return_value=0):data=family.load_data()
    d=data["d"];ext=FExtension()
    nwords=json.loads((HERE/"bc_cm_literal_words.json").read_text())["N_B_basis_in_F"]
    ns=[ext.word(w) for w in nwords]
    basis=[q.literal(d["fword"](w)) for w in old["basis_F_prime_words_B"]]
    powers=[ext.power(n,6) for n in ns]
    power_kernel=np.load(HERE/"de_ferrari_mod9_module.npz")["integral_abelianization_kernel"]
    sixth=[]
    for column in power_kernel.T:
        value=q.ZERO.copy()
        for a,g in zip(column,powers):
            assert g[0]==(0,0)
            if a:value=q.multiply(value,int(a)*g[1])
        sixth.append(value)
    values=[]
    for index,row in enumerate(old["normal_relator_metadata"]):
        i=row["indices"];kind=row["kind"]
        if kind=="N_commutator":deck,value=ext.comm(ns[i[0]],ns[i[1]]);assert deck==(0,0)
        elif kind=="F_prime_sixth_powers":value=sixth[i[0]].copy()
        elif kind=="basis_square":value=2*basis[i[0]]
        elif kind=="basis_commutator":
            value=np.r_[np.zeros(10,dtype=np.int64),2*q.wedge(basis[i[0]][:10],basis[i[1]][:10])]
        elif kind=="N_conjugation":deck,value=ext.conj(ns[i[1]],((0,0),basis[i[0]]));assert deck==(0,0)
        else:raise ValueError(kind)
        if row["image_coefficients"] is not None:
            rep=q.ZERO.copy()
            for a,g in zip(row["image_coefficients"],basis):
                if a:rep=q.multiply(rep,int(a)*g)
            value=q.multiply(value,-rep)
        assert np.array_equal(value[:10],Rabel[:,index])
        hall=hall_coordinates(value)
        reduced=np.r_[hall[:10]%4,hall[10:]%2]
        assert np.array_equal(reduced,finite["normal_relator_values"][index])
        values.append(value)
    values=np.stack(values)
    generators=[]
    for column in coeff.T:
        value=q.ZERO.copy()
        for a,g in zip(column,values[selected]):
            if a:value=q.multiply(value,int(a)*g)
        generators.append(value)
    generators=np.stack(generators,axis=1)
    assert np.array_equal(generators[:10],np.array(K,dtype=np.int64))
    inv=sp.Matrix(K[zrows,:]).inv();scale=int(sp.ilcm(1,*[a.q for a in inv]))
    invscaled=np.array(scale*inv,dtype=np.int64)
    def coordinates(ab):
        numerator=invscaled@ab[zrows];assert not np.any(numerator%scale)
        c=numerator//scale
        assert np.array_equal(np.array(K,dtype=np.int64)@c,ab)
        return c
    def representative(c):
        value=q.ZERO.copy()
        for a,g in zip(c,generators.T):
            if a:value=q.multiply(value,int(a)*g)
        return value
    central=[]
    for value in values:
        residual=q.multiply(value,-representative(coordinates(value[:10])))
        assert not np.any(residual[:10]) and not np.any(residual[10:]%2)
        central.append(residual[10:]//2)
    for name,action in (("s",q.S),("r",q.R)):
        for value in generators.T:
            image=action@value
            residual=q.multiply(image,-representative(coordinates(image[:10])))
            assert not np.any(residual[:10]) and not np.any(residual[10:]%2)
            central.append(residual[10:]//2)
    for i,j in combinations(range(8),2):
        central.append(q.wedge(generators[:10,i],generators[:10,j]))
    raw=np.stack(central,axis=1)
    print("Exact central relation matrix:",raw.shape,"largest entry",int(np.abs(raw).max()),flush=True)
    # A full-rank minor supplies a proved determinant multiple for
    # the modular HNF algorithm, avoiding coefficient growth on5502 columns.
    pivots={};minor=[]
    for j,column in enumerate(raw.T):
        v=column.copy()%5
        for p,row in sorted(pivots.items()):
            if v[p]:v=(v-int(v[p])*row)%5
        nz=np.flatnonzero(v)
        if len(nz):
            p=int(nz[0]);v=v*pow(int(v[p]),-1,5)%5
            pivots[p]=v;minor.append(j)
            if len(minor)==45:break
    assert len(minor)==45
    determinant=abs(sp.Matrix(raw[:,minor]).det())
    assert determinant
    print("Modular HNF determinant-bound digits:",len(str(determinant)),flush=True)
    lattice=hermite_normal_form(sp.Matrix(raw),D=determinant)
    a,b=map(sp.Matrix,(q.S[10:,10:],q.R[10:,10:]))
    while True:
        new=hermite_normal_form(lattice.row_join(a*lattice).row_join(b*lattice),
                               D=abs(lattice.det()))
        if new==lattice:break
        lattice=new
    assert lattice.shape==(45,45)
    smith=smith_normal_form(lattice,domain=ZZ)
    factors=[abs(int(smith[i,i])) for i in range(45)]
    def v2(n):
        k=0
        while n%2==0:n//=2;k+=1
        return k
    exponents=[v2(n) for n in factors]
    result={"actual_integral_abelian_image":np.array(K,dtype=np.int64).tolist(),
        "selected_normal_relators":selected,
        "exact_K_basis_word_coefficients":coeff.tolist(),
        "central_kernel_smith_factors":factors,
        "central_kernel_two_adic_exponents":exponents,
        "complete_central_kernel_rank":45,
        "all5458_integral_and_mod4_comparisons_verified":True,
        "elapsed_seconds":round(time.time()-started,3)}
    (HERE/"bc_fermat_class_two_2adic_source.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_two_2adic_source.npz",
        integral_relator_logs=values,integral_K_basis_logs=generators,
        integral_abelian_image=np.array(K,dtype=np.int64),
        central_relation_matrix=raw,central_kernel_lattice=np.array(lattice,dtype=np.int64))
    print(json.dumps(result,indent=2))
    print("PASS: complete integral binary source image and the exact H-prime central lattice.")

if __name__=="__main__":main()
