#!/usr/bin/env python3
"""Exact finite support for the unregistered D94 all-depth proof."""
from pathlib import Path
import json
import hashlib
import numpy as np

def local_smith(A, precision=10):
    modulus=5**precision
    A=np.array(A,dtype=np.int64)%modulus
    n=A.shape[0]
    vals=[]
    for k in range(n):
        B=A[k:,k:]
        nz=B!=0
        if not nz.any():break
        valuation=0
        while True:
            loc=np.argwhere(nz & ((B//(5**valuation))%5!=0))
            if len(loc):break
            valuation+=1
            assert valuation<precision
        i,j=map(int,loc[0]);i+=k;j+=k
        A[[k,i],:]=A[[i,k],:]
        A[:,[k,j]]=A[:,[j,k]]
        power=5**valuation
        inv=pow(int(A[k,k])//power,-1,modulus)
        A[k,k:]=(A[k,k:]*inv)%modulus
        assert A[k,k]==power
        for i in range(k+1,n):
            q=int(A[i,k])//power
            assert int(A[i,k])%power==0
            if q:A[i,k:]=(A[i,k:]-q*A[k,k:])%modulus
            assert A[i,k]==0
        # Actual column subtraction affects only this pivot row now.
        assert all(int(x)%power==0 for x in A[k,k+1:])
        A[k,k+1:]=0
        vals.append(valuation)
    return vals,n-len(vals)

def run():
    rows=[]
    for r,N in [(1,1),(1,2),(2,2),(1,3),(2,3),(3,3)]:
        n=5**N;a=5**r
        A=np.zeros((n,n),dtype=np.int64)
        for j in range(n):
            for shift in (0,a):
                for b,c in enumerate((1,3,3,1)):
                    A[(2*j+shift+b)%n,j]+=c
            A[j,j]-=1
        vals,zero=local_smith(A)
        # Rational rank is proved separately by the actual Fourier cycles.
        assert zero==N-r
        predicted=list(range(N-r+1,N))+[N+1]
        tors=[v for v in vals if v]
        assert tors==predicted,(r,N,tors,predicted)
        rows.append({'r':r,'N':N,'dimension':n,'precision':10,
                     'rational_free_rank':N-r,'zero_pivots':zero,
                     'nonzero_pivots':len(vals),'five_torsion_valuations':tors,
                     'exactness':'all rationally nonzero pivots found below precision; remaining pivots have the proved rational nullity'})
    diagram_rows=[]
    for r,N in [(1,1),(1,2),(2,2),(1,3),(2,3),(3,3)]:
        n=5**N;a=5**r;h=N-r
        T=np.zeros((n,n),dtype=np.int64)
        Pi=np.zeros((n,n),dtype=np.int64)
        for j in range(n):T[(j+1)%n,j]=1;Pi[(2*j)%n,j]=1
        Ta=np.zeros((a,a),dtype=np.int64)
        Pia=np.zeros((a,a),dtype=np.int64)
        for j in range(a):Ta[(j+1)%a,j]=1;Pia[(2*j)%a,j]=1
        Ia=np.eye(a,dtype=np.int64);In=np.eye(n,dtype=np.int64)
        A=(In+np.linalg.matrix_power(T,a))@Pi
        C=np.linalg.matrix_power(In+T,3)@Pi
        B=(In+np.linalg.matrix_power(T,a))@np.linalg.matrix_power(In+T,3)@Pi
        Ar=2*Pia;Br=2*np.linalg.matrix_power(Ia+Ta,3)@Pia
        F=np.zeros((n,a),dtype=np.int64)
        for j in range(a):
            for z in range(n//a):F[j+a*z,j]=1
        qr=np.linalg.matrix_power(T,a)-In
        u3=np.linalg.matrix_power(T-In,3)
        assert np.array_equal(A@F,F@Ar)
        assert np.array_equal(B@F,F@Br)
        assert np.array_equal(u3@B,A@u3)
        assert np.array_equal(qr@B,C@qr)
        assert np.array_equal(qr@A,Pi@qr)
        assert np.array_equal(F@np.ones(a,dtype=np.int64),np.ones(n,dtype=np.int64))
        av,az=local_smith(A-In);cv,cz=local_smith(C-In)
        assert az==h and [x for x in av if x]==list(range(h+1,h+r+1))
        assert cz==N and not any(cv)
        diagram_rows.append({'r':r,'N':N,'norm_A_intertwiner':True,'norm_B_intertwiner':True,
          'u_cubed_intertwiner':True,'actual_qr_target_intertwiner':True,
          'qr_ordinary_permutation_intertwiner':True,'norm_generator_maps_literally':True,
          'A_free_rank':az,'A_torsion_valuations':[x for x in av if x],
          'target_free_rank':cz,'target_torsion_valuations':[x for x in cv if x]})
    arithmetic=[]
    for r in range(1,6):
        for h in range(0,6):
            c=5**(h+1)-1
            tmod=pow(c,5**r,25)
            assert tmod==24 and (1-tmod)%25==2
            z=c**4-1;v=0
            while z%5==0:z//=5;v+=1
            assert v==h+1
            arithmetic.append({'r':r,'N':r+h,'c':c,'t_mod25':tmod,
                'one_minus_t_mod25':(1-tmod)%25,'unit_log_numerator_valuation':v})
    return {'status':'PASS_FINITE_SUPPORT_FOR_UNREGISTERED_D94',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'smith_rows':rows,'literal_norm_and_natural_map_rows':diagram_rows,
            'ordinary_point_residue_rows':arithmetic,
            'scope':'The all-depth homology and norm-extension proof is in the draft; no extrapolation from these finite rows.'}

if __name__=='__main__':
    result=run();data=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(data)
    print(data,end='')
