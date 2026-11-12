#!/usr/bin/env python3
"""Exact finite and graded checks for Parts C, E, H.

The degree-three deck calculation is rational, NOT a p-quotient certificate.
The double-cover calculation is cellular homology over F_3, using signed
lifted edge paths (equivalently, evaluated Fox derivatives).
"""
import json
from pathlib import Path
import sympy as sp
from ab_lie import special, pointpush, column_matrix

def lie_character(n, trace_power):
    return sum(int(sp.mobius(d))*trace_power(d)**(n//d)
               for d in sp.divisors(n))//n

def deck_table():
    ans=[]
    for r,order in [(3,2),(5,4)]:
        for n in range(2,5):
            dim=r*lie_character(n,lambda d:r)-lie_character(n+1,lambda d:r)
            # Each nonidentity deck element fixes exactly two punctures.
            tr=lie_character(n,lambda d:r if d%2==0 else 1)-lie_character(n+1,lambda d:r if d%2==0 else 1)
            fixed=(dim+(order-1)*tr)//order
            geo=sum(lie_character(n,lambda d,k=k:k) for k in range(2,r))
            ans.append(dict(rank=r,degree=n,deck_order=order,ambient=dim,
                            nonidentity_trace=tr,fixed=fixed,geometric=geo))
    # Independent matrix check in the index-two case.
    perm=(0,2,1)
    def action(D):
        return tuple({tuple(perm[j] for j in w):c for w,c in D[perm[i]].items()}
                     for i in range(3))
    basis=special(3,3)
    M=column_matrix(basis,3,3)
    AM=column_matrix([action(D) for D in basis],3,3)
    rows=list(M.T.rref()[1]); A=M[rows,:].inv()*AM[rows,:]
    assert M*A==AM and A*A==sp.eye(6)
    P=column_matrix(pointpush(3),3,3)
    fixed_basis=(A-sp.eye(6)).nullspace()
    F=M*sp.Matrix.hstack(*fixed_basis)
    assert A.trace()==2 and F.cols==4 and P.rank()==2
    assert F.row_join(P).rank()==5
    return ans,dict(degree=3,ambient=6,deck_fixed=4,geometric=2,
                    sum_rank=5,missing_dimension=1,
                    deck_matrix=[[str(x) for x in row] for row in A.tolist()])

def rref_mod(A,p=3):
    A=[[int(v)%p for v in row] for row in A]
    rows=len(A);cols=len(A[0]) if rows else 0;piv=[];i=0
    for j in range(cols):
        hit=next((k for k in range(i,rows) if A[k][j]),None)
        if hit is None: continue
        A[i],A[hit]=A[hit],A[i]
        inv=pow(A[i][j],-1,p);A[i]=[(v*inv)%p for v in A[i]]
        for k in range(rows):
            if k!=i and A[k][j]:
                c=A[k][j];A[k]=[(v-c*w)%p for v,w in zip(A[k],A[i])]
        piv.append(j);i+=1
        if i==rows:break
    return A,piv

def rank(A,p=3):return len(rref_mod(A,p)[1])

def nullspace(A,p=3):
    R,piv=rref_mod(A,p);cols=len(A[0]);out=[]
    for j in range(cols):
        if j in piv:continue
        v=[0]*cols;v[j]=1
        for i,k in enumerate(piv):v[k]=-R[i][j]%p
        out.append(v)
    return sp.Matrix.hstack(*(sp.Matrix(v) for v in out))

def inverse(word):return tuple(-x for x in reversed(word))

def homology_cover():
    p=3;q=(1,0,1,0,0,0)
    def path(word,start):
        v=start;chain=[0]*12
        for t in word:
            i=abs(t)-1
            if t>0:
                chain[2*i+v]+=1;v^=q[i]
            else:
                v^=q[i];chain[2*i+v]-=1
        return sp.Matrix([a%p for a in chain]),v
    d1=sp.zeros(2,12)
    for i in range(6):
        for v in range(2):
            d1[v,2*i+v]-=1;d1[v^q[i],2*i+v]+=1
    rel=tuple(x for i in (1,3,5) for x in (i,i+1,-i,-i-1))
    d2=sp.Matrix.hstack(*(path(rel,v)[0] for v in range(2)))
    c=(1,2,-1,-2)
    images=[c+(i,)+inverse(c) if i<=2 else (i,) for i in range(1,7)]
    T=sp.Matrix.hstack(*(path(images[i],v)[0] for i in range(6) for v in range(2)))
    mod=lambda M:M.applyfunc(lambda x:int(x)%p)
    assert mod(d1*d2)==sp.zeros(2,2)
    assert mod(d1*T)==mod(d1)
    assert mod(T*d2)==mod(d2)
    Z=nullspace(d1.tolist(),p)
    B_rank=rank(d2.tolist(),p)
    sep_rank=rank(d2.row_join((T-sp.eye(12))*Z).tolist(),p)-B_rank
    square_rank=rank(d2.row_join((T-sp.eye(12))**2*Z).tolist(),p)-B_rank
    assert rank(d1.tolist(),p)==1 and B_rank==1 and Z.cols-B_rank==10
    assert sep_rank==1 and square_rank==0
    assert mod(T**3)==sp.eye(12)
    return dict(base_genus=3,cover_degree=2,cover_genus=5,
                monodromy_q=list(q),coefficient_prime=p,
                C0=2,C1=12,C2=2,d1_rank=1,d2_rank=1,H1_dimension=10,
                separating_twist_rank_T_minus_I=sep_rank,
                square_rank_on_H1=square_rank,order=3,
                T_chain_matrix=[[int(x)%p for x in row] for row in T.tolist()])

def coherence():
    # C2-valued compatibility signs for two forgetting arrows, modulo
    # the central modification at the target. Relabelling forces s1=s2.
    pairs=[(a,b) for a in range(2) for b in range(2)]
    reps={min(x,tuple((v+1)%2 for v in x)) for x in pairs}
    equiv=[x for x in pairs if x[0]==x[1]]
    eqreps={min(x,tuple((v+1)%2 for v in x)) for x in equiv}
    assert len(reps)==2 and len(eqreps)==1
    return dict(two_unrelated_arrows_modifications_orbits=len(reps),
                coherent_relabelling_orbits=len(eqreps))

if __name__=='__main__':
    table,matrix=deck_table()
    out={'deck_characters':table,'index2_matrix_check':matrix,
         'genus3_double_cover':homology_cover(),'central_coherence':coherence(),
         'scope':'No nilpotent pro-2 group enumeration or p-quotient algorithm is claimed.'}
    dest=Path(__file__).with_name('ceh_checks.json')
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
