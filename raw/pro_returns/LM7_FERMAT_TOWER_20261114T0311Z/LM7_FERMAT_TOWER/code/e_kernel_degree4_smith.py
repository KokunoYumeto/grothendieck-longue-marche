#!/usr/bin/env python3
"""E102: exact integral three-primary Smith maps for the degree-four N'' layer.

The input is the frozen E100 actual arithmetic-action certificate. All
calculations use integers. Modular change-of-basis matrices and both their
inverses are retained, together with their exact integer-lift product.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import numpy as np

EXPECTED_INPUT='9ed2ac3d9f612b757882d1c696e43c3a65c80f6dba8235d8d4f6883e36c480d1'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mm(A,B,modulus):
    assert A.shape[1]*int(np.max(np.abs(A)))*int(np.max(np.abs(B))) < 2**63
    return (A@B)%modulus


def smith(A,modulus,precision):
    n=A.shape[0]
    A=A.copy()%modulus
    U=np.eye(n,dtype=np.int64);Ui=U.copy();V=U.copy();Vi=U.copy()
    vals=np.full(modulus,precision,dtype=np.int8)
    for a in range(1,modulus):
        b=a;v=0
        while b%3==0:
            b//=3;v+=1
        vals[a]=v
    operations=[];exponents=[]
    for k in range(n):
        view=vals[A[k:,k:]]
        pos=int(view.argmin());i,j=divmod(pos,n-k);v=int(view[i,j])
        if v==precision:
            break
        i+=k;j+=k
        if i!=k:
            A[[k,i],:]=A[[i,k],:];U[[k,i],:]=U[[i,k],:]
            Ui[:,[k,i]]=Ui[:,[i,k]]
        if j!=k:
            A[:,[k,j]]=A[:,[j,k]];V[:,[k,j]]=V[:,[j,k]]
            Vi[[k,j],:]=Vi[[j,k],:]
        power=3**v
        unit=int(A[k,k])//power;unit_inverse=pow(unit,-1,modulus)
        A[k,:]=(A[k,:]*unit_inverse)%modulus
        U[k,:]=(U[k,:]*unit_inverse)%modulus
        Ui[:,k]=(Ui[:,k]*unit)%modulus
        assert A[k,k]==power
        assert np.all(A[k+1:,k]%power==0)
        row_coeff=A[k+1:,k]//power
        if row_coeff.size:
            A[k+1:,k:]=(A[k+1:,k:]-row_coeff[:,None]*A[k,k:])%modulus
            U[k+1:,:]=(U[k+1:,:]-row_coeff[:,None]*U[k,:])%modulus
            Ui[:,k]=(Ui[:,k]+Ui[:,k+1:]@row_coeff)%modulus
        assert np.all(A[k+1:,k]==0)
        assert np.all(A[k,k+1:]%power==0)
        col_coeff=A[k,k+1:]//power
        if col_coeff.size:
            A[k:,k+1:]=(A[k:,k+1:]-A[k:,k,None]*col_coeff[None,:])%modulus
            V[:,k+1:]=(V[:,k+1:]-V[:,k,None]*col_coeff[None,:])%modulus
            Vi[k,:]=(Vi[k,:]+col_coeff@Vi[k+1:,:])%modulus
        assert np.all(A[k,k+1:]==0)
        operations.append({'index':k,'row_swap':i,'column_swap':j,
                           'exponent':v,'unit':unit,'unit_inverse':unit_inverse,
                           'row_coefficients':row_coeff.tolist(),
                           'column_coefficients':col_coeff.tolist()})
        exponents.append(v)
        if (k+1)%100==0:
            print('exact Smith pivots',k+1,'current exponent',v,flush=True)
    assert exponents==sorted(exponents)
    D=np.zeros_like(A)
    for k,v in enumerate(exponents):D[k,k]=3**v
    assert np.array_equal(A,D)
    return D,U,Ui,V,Vi,exponents,operations


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',type=Path,default=Path(__file__).with_name('a_s23_full.json'))
    args=ap.parse_args()
    assert sha(args.input)==EXPECTED_INPUT
    raw=json.loads(args.input.read_text())['integral_quotient']
    layer=raw['integral_layers'][3]
    n=layer['kernel_rank'];assert n==990
    matrices={}
    for key in ['tau','c','Frob_K2']:
        A=np.zeros((n,n),dtype=np.int64)
        for i,j,a in raw['actual_graded_naturality_degree_4'][key]['kernel_action_coo']:
            A[i,j]+=a
        matrices[key]=A
    T,J,F=(matrices[k] for k in ['tau','c','Frob_K2'])
    I=np.eye(n,dtype=np.int64)
    assert np.array_equal(J@J,I)
    assert np.array_equal(F@J,J@F)
    plus=(n+int(np.trace(J)))//2
    minus=n-plus
    assert (plus,minus)==(486,504)
    C=(T-I)@(I+J)
    precision=7;modulus=3**precision
    D,U,Ui,V,Vi,exponents,operations=smith(C,modulus,precision)
    print('verifying all exact modular change-of-basis maps',flush=True)
    checks={
        'U_times_Uinv':np.array_equal(mm(U,Ui,modulus),I),
        'Uinv_times_U':np.array_equal(mm(Ui,U,modulus),I),
        'V_times_Vinv':np.array_equal(mm(V,Vi,modulus),I),
        'Vinv_times_V':np.array_equal(mm(Vi,V,modulus),I),
        'U_C_V_equals_D':np.array_equal(mm(mm(U,C%modulus,modulus),V,modulus),D)
    }
    assert all(checks.values()),checks
    rank=len(exponents)
    assert rank==plus
    # Rank(C)<=rank(I+J)=486 over Q, since J^2=I. The 486
    # nonzero modular pivots give the reverse inequality over Q_3.
    # Thus the lower Schur block is exactly zero over Q_3; no
    # unknown higher-valuation Smith factor is omitted.
    first_bound=n*int(np.max(np.abs(U)))*int(np.max(np.abs(C)))
    assert first_bound<2**63
    UC=U@C
    second_bound=n*int(np.max(np.abs(UC)))*int(np.max(np.abs(V)))
    assert second_bound<2**63
    B=UC@V
    assert np.array_equal(B%modulus,D)
    powers=np.array([3**v for v in exponents],dtype=np.int64)
    exact_top=B[:rank,:rank]
    E=(exact_top-np.diag(powers))//powers[:,None]
    assert np.array_equal(exact_top,np.diag(powers)+powers[:,None]*E)
    assert np.all(E%3==0)
    assert np.all(B[:rank,rank:]%powers[:,None]==0)
    assert np.all(B[rank:,:rank]%modulus==0)
    archive=Path(__file__).with_suffix('.npz')
    np.savez_compressed(archive,T=T,J=J,F=F,C=C,D=D,U=U,Uinv=Ui,V=V,Vinv=Vi,
                        B_integer_lift=B,E_top=E,exponents=np.array(exponents,dtype=np.int8),
                        original_Hall_indices=np.array(layer['kernel_Hall_indices'],dtype=np.int64))
    finite=Counter(v for v in exponents if v)
    result={
        'status':'PASS','statement':'E.102','input_sha256':EXPECTED_INPUT,
        'precision_exponent':precision,'modulus':modulus,'rank_K4':n,
        'rank_J_fixed':plus,'rank_J_negative':minus,
        'exact_rank_C':rank,'free_rank':n-rank,
        'Smith_exponent_multiplicities':{str(v):exponents.count(v) for v in sorted(set(exponents))},
        'finite_factors':{str(3**v):finite[v] for v in sorted(finite)},
        'torsion_order_exponent':sum(exponents),'all_nonzero_pivots_detected':True,
        'exact_rank_upper_bound':'C=(T-I)(I+J), J^2=I, trace(J)=-18; rank(I+J)=486',
        'modular_inverse_checks':checks,
        'integer_lift_B_equals_U_C_V':True,
        'integer_lift_bounds':[first_bound,second_bound],
        'largest_absolute_input_entry':int(np.max(np.abs(C))),
        'largest_absolute_B_entry':int(np.max(np.abs(B))),
        'top_residual_E_divisible_by_3':True,
        'change_of_basis_archive':archive.name,'change_of_basis_archive_sha256':sha(archive),
        'operations':operations,
        'actual_Z3_lifts':{
            'S':'I+E_top; inverse is convergent sum (-E_top)^j',
            'R1':'[[S^-1,-S^-1*D_rank^-1*B12],[0,I]]',
            'L1':'[[I,0],[-B21*S^-1*D_rank^-1,I]]',
            'identity':'L1*(U*C*V)*R1=diag(D_rank,0)',
            'quotient_map':'x -> (L1*U)*x, reduced in the finite diagonal coordinates',
            'inverse_map':'choose diagonal representatives and apply U^-1*L1^-1',
            'Schur_zero_reason':'The exact rank is the size of the invertible top block,486'
        }
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    summary={k:v for k,v in result.items() if k!='operations'}
    print(json.dumps(summary,indent=2),flush=True)


if __name__=='__main__':main()
