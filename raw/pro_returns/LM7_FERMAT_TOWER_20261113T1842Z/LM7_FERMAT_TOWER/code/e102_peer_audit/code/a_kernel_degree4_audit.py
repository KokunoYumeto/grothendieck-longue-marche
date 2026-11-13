#!/usr/bin/env python3
"""Independent E102 audit: successive mod-3 Schur blocks and exact map lifts.

This does not import or call the author's Smith implementation. The valuations
are recovered from the frozen E100 input by exhausting unit pivots at each
successive quotient precision, using reverse pivot order. Author maps are then
checked against that independently rebuilt matrix and lifted two extra digits.
"""
from pathlib import Path
import argparse, hashlib, json
import numpy as np

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def mm(a,b,m):
    bound=a.shape[1]*int(np.max(np.abs(a),initial=0))*int(np.max(np.abs(b),initial=0))
    assert bound<2**63
    return (a@b)%m

def stages(matrix,precision):
    A=matrix.copy()%(3**precision)
    rows=[]
    for v in range(precision):
        modulus=3**(precision-v);n=A.shape[0];r=0
        while r<n:
            # Reverse lexicographic unit pivot, distinct from the author's
            # smallest-valuation forward pivoting. Only mod 3 is consulted.
            nz=np.argwhere(A[r:,r:]%3)
            if len(nz)==0:break
            i,j=map(int,nz[-1]);i+=r;j+=r
            if i!=r:A[[r,i],:]=A[[i,r],:]
            if j!=r:A[:,[r,j]]=A[:,[j,r]]
            inverse=pow(int(A[r,r]),-1,modulus)
            A[r,r:]=(A[r,r:]*inverse)%modulus
            assert A[r,r]==1
            col=A[r+1:,r].copy()
            A[r+1:,r:]=(A[r+1:,r:]-col[:,None]*A[r,r:])%modulus
            assert np.all(A[r+1:,r]==0)
            # The upper unit block can be discarded. Its right-hand entries
            # are cleared by column operations that do not change the Schur
            # block because the lower-left block is already zero.
            r+=1
        residual=A[r:,r:]
        assert np.all(residual%3==0)
        rows.append({'valuation':v,'unit_rank':r,'remaining_dimension':int(n-r),
                     'Schur_modulus':modulus,
                     'divided_residual_sha256':hashlib.sha256((residual//3).tobytes()).hexdigest()})
        print('independent mod-3 layer',v,'rank',r,'remaining',n-r,flush=True)
        A=residual//3
    return rows

def inv_from_seed(A,seed,m):
    I=np.eye(A.shape[0],dtype=np.int64)
    X=seed%m
    for _ in range(5):
        if np.array_equal(mm(A%m,X,m),I):break
        X=mm(X,(2*I-mm(A%m,X,m))%m,m)
    assert np.array_equal(mm(A%m,X,m),I)
    assert np.array_equal(mm(X,A%m,m),I)
    return X

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',type=Path,default=Path('research_e100/code/a_s23_full.json'))
    ap.add_argument('--certificate',type=Path,default=Path('research_e102/code/e_kernel_degree4_smith.json'))
    ap.add_argument('--archive',type=Path,default=Path('research_e102/code/e_kernel_degree4_smith.npz'))
    a=ap.parse_args()
    cert=json.loads(a.certificate.read_text())
    assert digest(a.input)==cert['input_sha256']
    assert digest(a.archive)==cert['change_of_basis_archive_sha256']
    original=json.loads(a.input.read_text())['integral_quotient']
    indices=original['integral_layers'][3]['kernel_Hall_indices']
    n=len(indices);assert n==990
    mats={}
    for k in ('tau','c','Frob_K2'):
        X=np.zeros((n,n),dtype=np.int64)
        for i,j,x in original['actual_graded_naturality_degree_4'][k]['kernel_action_coo']:
            X[i,j]+=x
        mats[k]=X
    T,J,F=(mats[k] for k in ('tau','c','Frob_K2'))
    I=np.eye(n,dtype=np.int64)
    assert np.array_equal(J@J,I)
    assert np.array_equal(F@J,J@F)
    assert int(np.trace(J))==-18
    C=(T-I)@(I+J)
    data=stages(C,7)
    exponents=[v['valuation'] for v in data for _ in range(v['unit_rank'])]
    counts={str(v):exponents.count(v) for v in sorted(set(exponents))}
    assert counts==cert['Smith_exponent_multiplicities']
    assert sum(v['unit_rank'] for v in data)==486
    z=np.load(a.archive,allow_pickle=False)
    for k,x in [('T',T),('J',J),('F',F),('C',C),('original_Hall_indices',np.array(indices))]:
        assert np.array_equal(z[k],x),k
    assert np.array_equal(z['exponents'],exponents)
    U,Ui,V,Vi=(z[k] for k in ('U','Uinv','V','Vinv'))
    m=2187
    checks={}
    for name,L,R in [('U_Uinv',U,Ui),('Uinv_U',Ui,U),('V_Vinv',V,Vi),('Vinv_V',Vi,V)]:
        checks[name]=bool(np.array_equal(mm(L,R,m),I));assert checks[name]
    B=z['B_integer_lift'];D=z['D'];rank=486
    assert n*int(np.max(abs(U)))*int(np.max(abs(C)))<2**63
    UC=U@C
    assert n*int(np.max(abs(UC)))*int(np.max(abs(V)))<2**63
    assert np.array_equal(UC@V,B)
    assert np.array_equal(B%m,D)
    powers=np.array([3**v for v in exponents],dtype=np.int64)
    E=(B[:rank,:rank]-np.diag(powers))//powers[:,None]
    assert np.array_equal(E,z['E_top'])
    assert np.all(E%3==0)
    assert np.all(B[:rank,rank:]%powers[:,None]==0)
    assert np.all(B[rank:,:rank]%m==0)
    # Actual Z3 matrices: compute S^-1 to precision 13, retaining four
    # additional digits before the possible division by 81. Check complete
    # left/right inverses and the exact diagonal identity modulo 3^9.
    M=3**9;high=3**13;Ir=np.eye(rank,dtype=np.int64)
    S=(Ir+E)%high
    Sinv=inv_from_seed(S,Ir,high)
    W=(B[:rank,rank:]//powers[:,None])%high
    lower_num=mm(B[rank:,:rank]%high,Sinv,high)
    assert np.all(lower_num%powers[None,:]==0)
    lower=(lower_num//powers[None,:])%M
    R1=np.eye(n,dtype=np.int64);L1=R1.copy()
    R1[:rank,:rank]=Sinv%M
    R1[:rank,rank:]=-mm(Sinv,W,high)%M
    L1[rank:,:rank]=-lower%M
    R1inv=np.eye(n,dtype=np.int64);L1inv=R1inv.copy()
    R1inv[:rank,:rank]=S%M;R1inv[:rank,rank:]=W%M
    L1inv[rank:,:rank]=lower
    for name,L,R in [('L1_inverse',L1,L1inv),('R1_inverse',R1,R1inv)]:
        checks[name+'_left']=bool(np.array_equal(mm(L,R,M),I))
        checks[name+'_right']=bool(np.array_equal(mm(R,L,M),I))
        assert checks[name+'_left'] and checks[name+'_right']
    lifted=mm(mm(L1,B%M,M),R1,M)
    checks['actual_lift_diagonal_mod_3_9']=bool(np.array_equal(lifted,D))
    assert checks['actual_lift_diagonal_mod_3_9']
    Uhigh=inv_from_seed(U,Ui,M);Vhigh=inv_from_seed(V,Vi,M)
    forward=mm(L1,U%M,M);backward=mm(Uhigh,L1inv,M)
    checks['quotient_coordinate_ambient_round_trip_left']=bool(np.array_equal(mm(forward,backward,M),I))
    checks['quotient_coordinate_ambient_round_trip_right']=bool(np.array_equal(mm(backward,forward,M),I))
    assert checks['quotient_coordinate_ambient_round_trip_left'] and checks['quotient_coordinate_ambient_round_trip_right']
    result={'status':'PASS','statement':'E.102','scope':'independent successive mod-3 ranks; every saved map; actual 3-adic lift through modulus 3^9',
            'input_sha256':digest(a.input),'author_certificate_sha256':digest(a.certificate),'author_archive_sha256':digest(a.archive),
            'rank':n,'trace_J':int(np.trace(J)),'plus_rank':486,'minus_rank':504,'successive_layers':data,
            'Smith_exponent_multiplicities':counts,'finite_factors':cert['finite_factors'],'free_rank':504,
            'torsion_order_exponent':sum(exponents),'map_checks':checks,
            'exact_integer_lift_recomputed':True,'lift_precision':9,'division_guard_precision':13,
            'rank_completeness':'rank(C)<=rank(I+J)=486; 486 independently detected pivots force equality'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)
if __name__=='__main__':main()
