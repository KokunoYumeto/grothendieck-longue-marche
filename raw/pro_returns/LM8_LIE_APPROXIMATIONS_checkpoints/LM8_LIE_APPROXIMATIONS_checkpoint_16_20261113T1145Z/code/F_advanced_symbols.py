"""Exact level-32 modular-symbol audit for the quadratic twist E_6 at p=5.

This is a finite arithmetic certificate, not by itself a Selmer vanishing
theorem.  Manin generators represent {g(0),g(infinity)}, with g in SL_2(Z).
Hecke operators are computed by actual rational paths and continued
fractions.  The character-24 twist is evaluated before reducing modulo 5.
"""
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import json
import math
import sympy as sp

HERE = Path(__file__).resolve().parent
LEVEL = 32
PRIME = 5
P1 = [(1,d) for d in range(LEVEL)] + [(c,1) for c in range(0,LEVEL,2)]
INDEX = {x:i for i,x in enumerate(P1)}
DIM = len(P1)

def canonical(c,d):
    c %= LEVEL
    d %= LEVEL
    if c % 2:
        return (1, d * pow(c,-1,LEVEL) % LEVEL)
    assert d % 2
    return (c * pow(d,-1,LEVEL) % LEVEL, 1)

def index(c,d):
    return INDEX[canonical(c,d)]

@lru_cache(None)
def symbol(r):
    """Return the integral Manin vector of {r,infinity}; None is infinity."""
    v = [0]*DIM
    if r is None:
        return tuple(v)
    r = Fraction(r)
    n,d = r.numerator,r.denominator
    cf=[]
    while d:
        q,rem = divmod(n,d)
        cf.append(q)
        n,d=d,rem
    pp,pq=0,1
    qp,qq=1,0
    for t in cf:
        a,b=t*pq+pp,t*qq+qp
        # Previous convergent pq/qq, current convergent a/b.
        det=pq*b-a*qq
        assert det in (-1,1)
        v[index(det*qq,b)]+=1
        pp,pq=pq,a
        qp,qq=qq,b
    assert Fraction(pq,qq)==r
    return tuple(v)

def rat(a,b):
    return None if b==0 else Fraction(a,b)

def lift(c,d):
    if c==1:
        return (0,-1,1,d)
    assert d==1
    return (1,0,c,1)

def hecke(ell):
    rows=[]
    for c,d in P1:
        a,b,c,d=lift(c,d)
        v=[0]*DIM
        for k in range(ell):
            # [[1,k],[0,ell]] acting on both endpoints.
            left=symbol(rat(b+k*d,ell*d))
            right=symbol(rat(a+k*c,ell*c))
            v=[u+x-y for u,x,y in zip(v,left,right)]
        left=symbol(rat(ell*b,d))
        right=symbol(rat(ell*a,c))
        v=[u+x-y for u,x,y in zip(v,left,right)]
        rows.append(v)
    return sp.Matrix(rows)

def integer_vector(v):
    den=sp.ilcm(*[x.q for x in v])
    out=[int(den*x) for x in v]
    g=math.gcd(*out)
    return [x//g for x in out]

def mod_rank(rows,p):
    a=[[int(x)%p for x in row] for row in rows]
    r=0
    for j in range(len(a[0]) if a else 0):
        i=next((i for i in range(r,len(a)) if a[i][j]),None)
        if i is None:
            continue
        a[r],a[i]=a[i],a[r]
        k=pow(a[r][j],-1,p)
        a[r]=[(k*x)%p for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][j]:
                k=a[i][j]
                a[i]=[(x-k*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):
            break
    return r

def main():
    relations=[]
    for c,d in P1:
        r=[0]*DIM
        r[index(c,d)]+=1
        r[index(-d,c)]+=1
        relations.append(r)
        r=[0]*DIM
        for x,y in [(c,d),(d,-c-d),(-c-d,c)]:
            r[index(x,y)]+=1
        relations.append(r)
    R=sp.Matrix(relations)
    basis=R.nullspace()
    assert len(basis)==9
    T3,T5=hecke(3),hecke(5)
    # A Hecke action descends exactly if it carries every relation to zero
    # against every functional on the relative Manin quotient.
    B=sp.Matrix.hstack(*basis)
    assert R*T3*B==sp.zeros(R.rows,B.cols)
    assert R*T5*B==sp.zeros(R.rows,B.cols)
    equations=R.col_join(T3)
    cusp=equations.nullspace()
    assert len(cusp)==2
    Phi=sp.Matrix.hstack(*[sp.Matrix(integer_vector(v)) for v in cusp])
    assert T3*Phi==sp.zeros(DIM,2)
    assert T5*Phi==-2*Phi
    assert mod_rank(equations.tolist(),PRIME)==DIM-2
    assert mod_rank(Phi.T.tolist(),PRIME)==2
    # The full primitive level-32 period lattice has no new 5-index:
    # both the defining quotient and the displayed dual basis have rank two
    # modulo 5 as well as over Q.
    def value(r):
        return sp.Matrix(1,DIM,symbol(r))*Phi
    E1_values={a:[int(x) for x in value(Fraction(a,5))] for a in range(5)}
    E1_moments={j:[sum((a**j)*E1_values[a][i] for a in range(1,5))
                   for i in range(2)] for j in range(4)}
    chi={v:int(sp.kronecker_symbol(24,v)) for v in range(24)}
    def twisted(r):
        out=sp.zeros(1,2)
        for v in range(24):
            if chi[v]:
                out += chi[v]*value(Fraction(r)+Fraction(v,24))
        return [int(x) for x in out]
    values={a:twisted(Fraction(a,5)) for a in range(5)}
    moments={j:[sum((a**j)*values[a][i] for a in range(1,5))
                for i in range(2)] for j in range(4)}
    # The conjugation action on period functionals is read from rational
    # paths; checking against all Manin generators gives an exact involution.
    conjrows=[]
    for c,d in P1:
        a,b,c,d=lift(c,d)
        left=value(rat(-b,d))
        right=value(rat(-a,c))
        conjrows.append(list(left-right))
    CPhi=sp.Matrix(conjrows)
    C=(Phi.T*Phi).inv()*Phi.T*CPhi
    assert Phi*C==CPhi and C*C==sp.eye(2)
    reduction_counts={}
    for curve_d in [1,6]:
        count=1+sum(1 for x in range(7) for y in range(7)
                    if (y*y-x*x*x+curve_d*curve_d*x)%7==0)
        assert count==8
        reduction_counts[curve_d]=count
    assert not any((a*a+2)%5==0 for a in range(5))
    out={
        'level':LEVEL,'prime':PRIME,'manin_generators':P1,
        'relation_rank':int(R.rank()),'relative_dimension':len(basis),
        'cusp_hecke_kernel_dimension':len(cusp),
        'integral_period_dual_basis_columns':[[int(x) for x in row] for row in Phi.tolist()],
        'T3_eigenvalue':0,'T5_eigenvalue':-2,
        'relations_and_hecke_verified_exactly':True,
        'rank_mod_5':mod_rank(equations.tolist(),PRIME),
        'basis_rank_mod_5':mod_rank(Phi.T.tolist(),PRIME),
        'complex_conjugation_matrix':[[str(x) for x in row] for row in C.tolist()],
        'twist_character_modulus':24,'twist_character':chi,
        'E1_raw_symbols':E1_values,'E1_raw_Bernoulli_moments':E1_moments,
        'E1_moments_mod_5':{j:[v%5 for v in vec] for j,vec in E1_moments.items()},
        'F7_point_counts':reduction_counts,
        'residual_Frobenius7_polynomial':'t^2+2, irreducible over F5',
        'raw_twisted_symbols_Gauss_multiple':values,
        'raw_Bernoulli_moments':moments,
        'moments_mod_5':{j:[v%5 for v in vec] for j,vec in moments.items()},
        'normalization':'Raw twisted symbols are tau(chi_24) times E6 symbols, expressed in a level-32 period basis. tau(chi_24)^2=24 is a 5-adic unit. No Selmer theorem is inferred by this program.',
    }
    (HERE/'F_advanced_symbols.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['manin_generators','integral_period_dual_basis_columns']},indent=2))

if __name__=='__main__':
    main()
