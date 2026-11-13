"""E.33: exact cyclotomic conjugation, trace maps, and free-Lie ranks.

No floating point or field tables are used. Cyclotomic fields are represented
by Q[z]/Phi_m(z). Every trace is the literal sum over automorphisms fixing
the embedded lower field. The verification checks maps, not just dimensions.
"""
from pathlib import Path
from functools import lru_cache
import json
from math import gcd
import sympy as sp

HERE = Path(__file__).resolve().parent
z = sp.Symbol('z')

@lru_cache(None)
def phi(m):
    return sp.Poly(sp.cyclotomic_poly(m, z), z, domain=sp.QQ)

def degree(m):
    return phi(m).degree()

@lru_cache(None)
def power(m, e):
    p = sp.Poly(z ** (e % m), z, domain=sp.QQ).rem(phi(m))
    return sp.ImmutableMatrix([p.nth(i) for i in range(degree(m))])

@lru_cache(None)
def aut(m, a):
    return sp.ImmutableMatrix.hstack(*(power(m, a*j) for j in range(degree(m))))

@lru_cache(None)
def embedding(m, n):
    assert n % m == 0
    return sp.ImmutableMatrix.hstack(*(power(n, (n//m)*j) for j in range(degree(m))))

@lru_cache(None)
def trace(m, n):
    """K_n -> K_m; compatible primitive roots satisfy z_m=z_n^(n/m)."""
    fixing = [a for a in range(n) if gcd(a,n)==1 and (a-1)%m==0]
    assert len(fixing) == degree(n)//degree(m)
    trace_in_n = sum((aut(n,a) for a in fixing), sp.zeros(degree(n)))
    ans, parameters = embedding(m,n).gauss_jordan_solve(trace_in_n)
    assert not parameters.rows
    assert embedding(m,n)*ans == trace_in_n
    return sp.ImmutableMatrix(ans)

@lru_cache(None)
def v_basis(m):
    """Scalar plus the anti-invariant subspace, as columns in K_m."""
    c = aut(m,-1)
    pminus = (sp.eye(degree(m))-c)/2
    columns = [power(m,0)] + pminus.columnspace()
    return sp.ImmutableMatrix.hstack(*columns)

@lru_cache(None)
def v_trace(m,n):
    rhs = trace(m,n)*v_basis(n)
    ans, parameters = v_basis(m).gauss_jordan_solve(rhs)
    assert not parameters.rows
    assert v_basis(m)*ans == rhs
    return sp.ImmutableMatrix(ans)

def witt(rank, weight):
    return int(sum(sp.mobius(d)*rank**(weight//d) for d in sp.divisors(weight))//weight)

def encode(matrix):
    return [[str(matrix[i,j]) for j in range(matrix.cols)] for i in range(matrix.rows)]

def main():
    rows=[]
    maps=[]
    equivariance_checks=0
    for m in range(1,25):
        d=degree(m)
        c=aut(m,-1)
        assert c*c == sp.eye(d)
        pm=(sp.eye(d)-c)/2
        pp=(sp.eye(d)+c)/2
        assert pm*pp == sp.zeros(d)
        assert pm*pm == pm and pp*pp == pp
        rank=1 if m<=2 else d//2+1
        b=v_basis(m)
        assert b.cols == rank and b.rank()==rank
        absolute_trace=trace(1,m)
        quotient=sp.Matrix.vstack(absolute_trace/d, pm)
        expected_kernel_dimension=0 if m<=2 else d//2-1
        assert d-quotient.rank()==expected_kernel_dimension
        for v in quotient.nullspace():
            assert c*v==v and absolute_trace*v==sp.zeros(1,1)
        rows.append({'m':m,'degree':d,'r2_plus_1':rank,
                     'unit_log_rank':expected_kernel_dimension,
                     'free_lie_ranks_1_to_8':[witt(rank,k) for k in range(1,9)]})
    for n in range(1,25):
        for m in sp.divisors(n):
            t=trace(m,n)
            assert t*embedding(m,n)==(degree(n)//degree(m))*sp.eye(degree(m))
            vt=v_trace(m,n)
            assert vt.rank()==v_basis(m).cols
            assert vt[0,0]==degree(n)//degree(m)
            assert all(vt[0,j]==0 for j in range(1,vt.cols))
            assert all(vt[i,0]==0 for i in range(1,vt.rows))
            for a in range(n):
                if gcd(a,n)==1:
                    assert t*aut(n,a)==aut(m,a)*t
                    equivariance_checks+=1
            maps.append({'from_conductor':n,'to_conductor':int(m),
                         'field_trace':encode(t),'V_trace':encode(vt)})
    towers=0
    for n in range(1,25):
        for m in sp.divisors(n):
            for k in sp.divisors(m):
                assert trace(k,m)*trace(m,n)==trace(k,n)
                assert v_trace(k,m)*v_trace(m,n)==v_trace(k,n)
                towers+=1
    out={'statement':'E.33','conductors_checked':24,
         'divisor_trace_maps':len(maps),'tower_compositions':towers,
         'galois_equivariance_checks':equivariance_checks,
         'rows':rows,'trace_maps':maps,'all_checks_passed':True}
    (HERE/'e_arithmetic_kernel.json').write_text(json.dumps(out,indent=2)+'\n')
    print('E.33 exact arithmetic-kernel maps')
    print('m degree generators unit_log_rank free_Lie_ranks_1_to_8')
    for row in rows:
        print(row['m'],row['degree'],row['r2_plus_1'],row['unit_log_rank'],
              ','.join(map(str,row['free_lie_ranks_1_to_8'])))
    print('divisor_trace_maps',len(maps))
    print('tower_compositions',towers)
    print('galois_equivariance_checks',equivariance_checks)
    print('PASS: all exact projection, norm/trace, composition and rank checks')

if __name__=='__main__':
    main()
