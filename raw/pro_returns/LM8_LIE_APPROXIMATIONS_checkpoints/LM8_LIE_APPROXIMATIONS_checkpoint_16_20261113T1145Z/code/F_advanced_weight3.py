"""Exact polynomial modular symbols for eta(4z)^6, level 16, weight 3.

The character is epsilon(d)=(-4/d). Manin [P,g] means
g(P tensor {0,infinity}), with g.P(X,Y)=P(g^{-1}(X,Y)).
Hecke action on degree-one polynomials uses the integral adjugate.
"""
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import json
import sympy as sp
from F_advanced_symbols import integer_vector, mod_rank

HERE=Path(__file__).resolve().parent
N=16
P1=[(1,d) for d in range(N)]+[(c,1) for c in range(0,N,2)]
INDEX={x:i for i,x in enumerate(P1)}
D=2*len(P1)

def eps(u):
    assert u%2
    return 1 if u%4==1 else -1

def mm(g,h):
    a,b,c,d=g; A,B,C,D=h
    return (a*A+b*C,a*B+b*D,c*A+d*C,c*B+d*D)

def adj(g):
    a,b,c,d=g
    return (d,-b,-c,a)

def rowmul(v,g):
    a,b,c,d=g; x,y=v
    return (x*a+y*c,x*b+y*d)

def canonical(c,d):
    c%=N; d%=N
    if c%2:
        return INDEX[(1,d*pow(c,-1,N)%N)],eps(c)
    assert d%2
    return INDEX[(c*pow(d,-1,N)%N,1)],eps(d)

def manin(v,c,d):
    i,e=canonical(c,d)
    out=[0]*D
    out[2*i]=int(e*v[0]);out[2*i+1]=int(e*v[1])
    return out

def lift(c,d):
    if c==1:return (0,-1,1,d)
    assert d==1
    return (1,0,c,1)

def rat(a,b):
    return None if b==0 else Fraction(a,b)

@lru_cache(None)
def edge_matrices(r):
    if r is None:return ()
    r=Fraction(r);n,d=r.numerator,r.denominator;cf=[]
    while d:
        q,t=divmod(n,d);cf.append(q);n,d=d,t
    pp,pq,qp,qq=0,1,1,0
    ans=[]
    for t in cf:
        a,b=t*pq+pp,t*qq+qp;det=pq*b-a*qq
        assert det in (-1,1)
        ans.append((det*pq,a,det*qq,b))
        pp,pq,qp,qq=pq,a,qq,b
    assert Fraction(pq,qq)==r
    return tuple(ans)

def symbol(v,r):
    """Polynomial v[0]X+v[1]Y times {r,infinity}."""
    out=[0]*D
    for g in edge_matrices(r):
        # Global v = g.Q, hence Q = g^{-1}.v = v composed with g.
        term=manin(rowmul(v,g),g[2],g[3])
        out=[a+b for a,b in zip(out,term)]
    return out

def hecke(ell):
    rows=[]
    delta=[((1,j,0,ell),1) for j in range(ell)]
    delta.append(((ell,0,0,1),eps(ell)))
    for c,d in P1:
        g=lift(c,d);a,b,c,d=g
        for v in [(1,0),(0,1)]:
            globalpoly=rowmul(v,adj(g))
            out=[0]*D
            for h,e in delta:
                hg=mm(h,g);A,B,C,Dd=hg
                hp=rowmul(globalpoly,adj(h))
                l=symbol(hp,rat(B,Dd));r=symbol(hp,rat(A,C))
                out=[u+e*(x-y) for u,x,y in zip(out,l,r)]
            rows.append(out)
    return sp.Matrix(rows)

def main():
    S=(0,-1,1,0);R=(0,-1,1,-1);R2=mm(R,R)
    relations=[]
    for c,d in P1:
        for v in [(1,0),(0,1)]:
            def action(h):
                # [P,g].h=[h^{-1}.P,gh]; h^{-1}.P(z)=P(hz).
                cd=rowmul((c,d),h)
                return manin(rowmul(v,h),*cd)
            base=manin(v,c,d)
            relations.append([a+b for a,b in zip(base,action(S))])
            relations.append([a+b+c for a,b,c in zip(base,action(R),action(R2))])
    Rel=sp.Matrix(relations)
    basis=Rel.nullspace()
    B=sp.Matrix.hstack(*basis)
    T3,T5=hecke(3),hecke(5)
    assert Rel*T3*B==sp.zeros(Rel.rows,B.cols)
    assert Rel*T5*B==sp.zeros(Rel.rows,B.cols)
    Eq=Rel.col_join(T3)
    cusp=Eq.nullspace()
    print('DIMENSIONS',D,Rel.rank(),len(basis),len(cusp),flush=True)
    assert len(cusp)==2
    Phi=sp.Matrix.hstack(*[sp.Matrix(integer_vector(v)) for v in cusp])
    assert T5*Phi==-6*Phi
    assert mod_rank(Eq.tolist(),5)==D-2
    assert mod_rank(Phi.T.tolist(),5)==2
    def value(poly,r):
        return [int(x) for x in sp.Matrix(1,D,symbol(poly,r))*Phi]
    values_Y={a:value((0,1),Fraction(a,5)) for a in range(5)}
    values_X={a:value((1,0),Fraction(a,5)) for a in range(5)}
    I1={a:value((5,-a),Fraction(a,5)) for a in range(1,5)}
    I0={a:value((1,-a),Fraction(a,1)) for a in range(1,5)}
    assert len(set(tuple(v) for v in I0.values()))==1
    # T_5 = U_5 + epsilon(5)*5^(k-1)*V_5, where V_5 f(z)=f(5z).
    # Substitution w=5z in the polynomial integral leaves the factor
    # 5^(k-2)=5.  This also checks the distribution normalization directly.
    I2={a+5*b:value((25,-a-5*b),Fraction(a+5*b,25))
        for a in range(1,5) for b in range(5)}
    distribution_checks={}
    for a in range(1,5):
        lhs=[sum(I2[a+5*b][i] for b in range(5)) for i in range(2)]
        rhs=[-6*I1[a][i]-5*I0[a][i] for i in range(2)]
        assert lhs==rhs
        distribution_checks[a]={'sum_I2':lhs,'a5_I1_minus_5_I0':rhs}
    # alpha is the unit root of t^2+6t+25, hence alpha=4 mod5.
    alpha=4
    measure={a:[(pow(alpha,-1,5)*I1[a][i]-5*pow(alpha,-2,5)*I0[a][i])%5
                for i in range(2)] for a in range(1,5)}
    moments={j:[sum(pow(a,j,5)*measure[a][i] for a in range(1,5))%5
                for i in range(2)] for j in range(4)}
    out={
        'level':N,'weight':3,'character':'epsilon(d)=(-4/d)',
        'Manin_dimension_before_relations':D,'relation_rank':int(Rel.rank()),
        'relative_dimension':len(basis),'cusp_hecke_kernel_dimension':len(cusp),
        'rank_mod_5':mod_rank(Eq.tolist(),5),'basis_rank_mod_5':mod_rank(Phi.T.tolist(),5),
        'T3_eigenvalue':0,'T5_eigenvalue':-6,
        'Manin_generators':P1,
        'integral_period_dual_basis_columns':[[int(x) for x in row] for row in Phi.tolist()],
        'Y_path_values_at_a_over_5':values_Y,'X_path_values_at_a_over_5':values_X,
        'I1_polynomial_5X_minus_aY':I1,'I0_polynomial_X_minus_aY':I0,
        'I2_polynomial_25X_minus_aY':I2,
        'exact_distribution_checks':distribution_checks,
        'measure_formula':'mu_n(a)=alpha^(-n)*I_n(a)-5*alpha^(-n-1)*I_(n-1)(a)',
        'ordinary_measure_residue_classes_mod_5':measure,
        'measure_Bernoulli_moments_mod_5':moments,
        'target_Kato_trivial_branch':'measure omega^{-2}, j=2, because the bounded measure interpolates the top critical value r=k-1=2',
        'relation_and_Hecke_checks':True,
        'scope':'Exact finite modular-symbol calculation only; representation identification and Selmer deduction require the separate proof.'
    }
    (HERE/'F_advanced_weight3.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['Manin_generators','integral_period_dual_basis_columns']},indent=2))

if __name__=='__main__':main()
