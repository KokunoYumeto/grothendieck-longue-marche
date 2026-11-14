#!/usr/bin/env python3
"""Exploratory exact Smith factors and actual source-central lattice.

This uses the new integral class-three matrices and never changes an
accepted certificate.  The diagonal Smith computation is kept separate
from any later row-coordinate optimization or full lifting claim.
"""
from pathlib import Path
from collections import Counter
import json,time
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

HERE=Path(__file__).resolve().parent

def finite_rref(a,p):
    a=np.asarray(a,dtype=np.int64).copy()%p;pivots=[];r=0
    for j in range(a.shape[1]):
        nz=np.flatnonzero(a[r:,j])
        if not len(nz):continue
        i=r+int(nz[0]);a[[r,i]]=a[[i,r]]
        a[r]=a[r]*pow(int(a[r,j]),-1,p)%p
        coefficients=a[:,j].copy();coefficients[r]=0
        a=(a-coefficients[:,None]*a[r][None,:])%p
        pivots.append(j);r+=1
        if r==a.shape[0]:break
    return r,pivots,a

def main():
    start=time.time();data=np.load(HERE/"bc_fermat_class_three_integral.npz")
    M=data["triple_norm"];S=data["S"][55:,55:];R=data["R"][55:,55:]
    traceS=int(np.trace(S));traceR=int(np.trace(R))
    print("Central norm",M.shape,"traces S,R",traceS,traceR,flush=True)
    ranks={p:finite_rref(M,p)[0] for p in (2,3,5,7,11)}
    print("Finite-field ranks:",ranks,flush=True)
    oldC=np.load(HERE/"bc_fermat_class_two_integral_kernel.npz")["central_basis"]
    B=data["bracket"].reshape(330,10,45)
    source=np.hstack([B[:,i,:]@oldC for i in range(10)])%3
    source_rank,pivots,_=finite_rref(source,3)
    assert source_rank==330
    print("Actual gamma3 source bracket rank",source_rank,"of330",flush=True)
    print("Beginning exact integer Smith diagonal",flush=True)
    smith=smith_normal_form(sp.Matrix(M.tolist()),domain=sp.ZZ)
    diagonal=[abs(int(smith[i,i])) for i in range(330)]
    rank=sum(bool(v) for v in diagonal)
    assert ranks[5]<=rank and ranks[7]<=rank
    print("Smith factors",dict(Counter(diagonal)),flush=True)
    result={"status":"exploratory exact central operator; no full lifting conclusion",
        "central_norm_shape":list(M.shape),"trace_S":traceS,"trace_R":traceR,
        "finite_field_ranks":ranks,"integer_Smith_factors":diagonal,
        "Smith_factor_histogram":dict(Counter(diagonal)),"rational_rank":rank,
        "rational_central_kernel_rank":330-rank,
        "actual_source_gamma3_image_rank_mod3":330,
        "actual_source_basis_words":[{"H_generator":j//45+1,
            "integral_adjusted_relator_basis_index":j%45,
            "word":"[eta_i,u_l^4]"} for j in pivots],
        "elapsed_seconds":round(time.time()-start,3)}
    (HERE/"bc_fermat_class_three_norm_smith_probe.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_three_norm_smith_probe.npz",
        central_source_brackets_mod3=source,central_source_pivot_columns=np.array(pivots),
        smith_diagonal=np.array(diagonal,dtype=np.int64))
    print(json.dumps({k:v for k,v in result.items() if k not in
        ("integer_Smith_factors","actual_source_basis_words")},indent=2))
    print("PASS: exact central Smith factors and full actual source-central lattice.")

if __name__=="__main__":main()
