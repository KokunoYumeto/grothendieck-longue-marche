#!/usr/bin/env python3
"""Exact degree-three arithmetic lattice calculation.

M3=ker(V tensor Sym^2(V) -> Sym^3(V)).  For each multidegree mu,
use basis e_i X^(mu-e_i) - e_j X^(mu-e_j), j=min(support(mu)), i>j.
This is the integral metabelian Hall basis in degree three; in that
low degree it is the whole free Lie algebra. All arithmetic is integer.
Smith elimination is certified modulo 3^10 with no surviving zero pivot.
"""
import json
from itertools import combinations_with_replacement
from pathlib import Path
import hashlib
import numpy as np

OUT=Path(__file__).resolve().parent
base=json.loads((OUT/'a_k_lattice.out').read_text())
Vgs=[np.array(g,dtype=np.int64) for g in base['V_generator_matrices']]
multidegrees=list(combinations_with_replacement(range(10),3))
basis=[(mu,i) for mu in multidegrees for i in sorted(set(mu))[1:]]
assert len(basis)==330
index={x:j for j,x in enumerate(basis)}
pairs=list(combinations_with_replacement(range(10),2))

def remove_one(mu,i):
    z=list(mu);z.remove(i);return tuple(z)

def action(G):
    cols=[[(a,int(G[a,i])) for a in range(10) if G[a,i]] for i in range(10)]
    sym={}
    for p,q in pairs:
        D={}
        for a,x in cols[p]:
            for b,y in cols[q]:
                ab=tuple(sorted((a,b)))
                D[ab]=D.get(ab,0)+x*y
        sym[(p,q)]=[(ab,v) for ab,v in D.items() if v]
    H=np.zeros((330,330),dtype=np.int64)
    for col,(mu,i) in enumerate(basis):
        j=mu[0]; expanded={}
        for v,sgn in ((i,1),(j,-1)):
            mon=remove_one(mu,v)
            for a,x in cols[v]:
                for ab,y in sym[mon]:
                    key=(a,ab);expanded[key]=expanded.get(key,0)+sgn*x*y
        sums={}
        for (a,ab),value in expanded.items():
            if not value:continue
            nu=tuple(sorted((a,)+ab))
            sums[nu]=sums.get(nu,0)+value
            if a!=nu[0]: H[index[(nu,a)],col]+=value
        assert all(value==0 for value in sums.values()), 'Multiplication kernel not preserved.'
    return H

Hs=[action(G) for G in Vgs]
Ha,Hb,Hc=Hs
I=np.eye(330,dtype=np.int64)
assert np.array_equal(Hc@Hc,I)
assert np.array_equal(Hc@Ha@Hc,Hb)
assert np.array_equal(Ha@Hb,Hb@Ha)
assert int(np.trace(Hc))==-2

# The pivot columns of 1+c are a Z3-basis of the c-invariants.
P=I+Hc
B=P.copy()%3
pivots=[]; rr=0
for col in range(330):
    choices=np.flatnonzero(B[rr:,col])
    if not len(choices):continue
    row=rr+int(choices[0]);B[[rr,row],:]=B[[row,rr],:]
    B[rr,:]=B[rr,:]*pow(int(B[rr,col]),-1,3)%3
    factors=B[:,col].copy();factors[rr]=0
    B=(B-factors[:,None]*B[rr,:][None,:])%3
    pivots.append(col);rr+=1
assert len(pivots)==164
S=P[:,pivots]
assert np.array_equal(Hc@S,S)
d=(Ha-I)@S


def smith_3adic(M,precision=10):
    mod=3**precision
    B=M.copy()%mod
    rows,cols=B.shape
    vals=[];operations=[]
    for k in range(cols):
        block=B[k:,k:]
        val=np.full(block.shape,precision,dtype=np.int64)
        z=block.copy();nonzero=z!=0
        val[nonzero]=0
        active=nonzero & (z%3==0)
        for e in range(1,precision):
            if not np.any(active):break
            val[active]+=1;z[active]//=3
            active=active & (z%3==0)
        where=np.unravel_index(np.argmin(val),val.shape)
        v=int(val[where]);assert v<precision, 'Increase precision.'
        r,c=k+int(where[0]),k+int(where[1]);p=3**v
        B[[k,r],:]=B[[r,k],:];B[:,[k,c]]=B[:,[c,k]]
        unit=int(B[k,k])//p
        B[k,:]=B[k,:]*pow(unit,-1,mod)%mod
        assert int(B[k,k])==p
        factors=B[k+1:,k]//p
        assert np.all(B[k+1:,k]%p==0)
        B[k+1:,:]=(B[k+1:,:]-factors[:,None]*B[k,:][None,:])%mod
        assert np.all(B[k+1:,k]==0)
        factors=B[k,k+1:]//p
        assert np.all(B[k,k+1:]%p==0)
        B[:,k+1:]=(B[:,k+1:]-B[:,k][:,None]*factors[None,:])%mod
        assert np.all(B[k,k+1:]==0)
        vals.append(v);operations.append([r,c,unit,v])
    diag=np.zeros_like(B)
    for i,v in enumerate(vals):diag[i,i]=3**v
    assert np.array_equal(B,diag)
    return vals,operations

vals,operations=smith_3adic(d)
assert vals==sorted(vals)
hist={str(v):vals.count(v) for v in sorted(set(vals))}
matrices={'basis':[[list(mu),i] for mu,i in basis],
          'M3_Galois_matrices':[H.tolist() for H in Hs],
          'c_fixed_basis_columns':pivots,
          'c_fixed_basis_matrix':S.tolist(),
          'finite_S_differential':d.tolist(),
          'smith_pivot_operations':operations}
raw=json.dumps(matrices,separators=(',',':')).encode()
path=OUT/'a_degree3_matrices.json';path.write_bytes(raw)
summary={'rank_M3':330,'c_plus_rank':164,'c_minus_rank':166,
         'all_action_relations_checked':True,'multiplication_kernel_preserved':True,
         'finite_S_differential_shape':list(d.shape),'smith_precision':10,
         'Smith_valuation_histogram':hist,'Smith_valuations':vals,
         'H1_free_rank':166,
         'H1_torsion_multiplicities':{str(3**v):vals.count(v) for v in sorted(set(vals)) if v},
         'H1_torsion_order_exponent_3':sum(vals),
         'matrix_file':path.name,'matrix_file_bytes':len(raw),
         'matrix_file_sha256':hashlib.sha256(raw).hexdigest()}
print(json.dumps(summary,indent=2))
