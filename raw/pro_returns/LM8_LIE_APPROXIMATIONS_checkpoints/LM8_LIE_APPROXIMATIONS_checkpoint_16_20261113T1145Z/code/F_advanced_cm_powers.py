"""Exact polynomial Manin symbols for powers of the Q(i) CM character.

Power m has weight m+1 and polynomial degree m-1.  This executable
constructs the character space, isolates T3=0 and the exact CM T5
eigenvalue, and computes ordinary top-critical branch moments.
Odd powers are also twisted by the primitive quadratic character24.
Twisted integral paths are multiplied by 24^(m-1), a 5-adic unit.
Every output has a finite computation scope; arithmetic deductions are
separate statements in F_advanced.tex.
"""
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from math import comb
import argparse
import json
import sympy as sp
from F_advanced_symbols import integer_vector,mod_rank
from F_advanced_weight3 import edge_matrices,mm,adj,rat,rowmul

HERE=Path(__file__).resolve().parent

def main(m):
    w=m-1
    N=32 if m%2 else (16 if m%4==2 else 4)
    P1=[(1,d) for d in range(N)]+[(c,1) for c in range(0,N,2)]
    INDEX={x:i for i,x in enumerate(P1)}
    D=(w+1)*len(P1)
    eps=lambda u: (1 if u%4==1 else -1)**w
    def canonical(c,d):
        c%=N;d%=N
        if c%2:return INDEX[(1,d*pow(c,-1,N)%N)],eps(c)
        return INDEX[(c*pow(d,-1,N)%N,1)],eps(d)
    @lru_cache(None)
    def compose(v,g):
        a,b,c,d=g
        ans=[0]*(w+1)
        for i,coeff in enumerate(v):
            if not coeff:continue
            for j in range(w-i+1):
                for k in range(i+1):
                    ans[j+k]+=coeff*comb(w-i,j)*a**(w-i-j)*b**j*comb(i,k)*c**(i-k)*d**k
        return tuple(ans)
    def monomial(i):return tuple(int(i==j) for j in range(w+1))
    def manin(v,c,d):
        ix,e=canonical(c,d)
        out=[0]*D
        for i,x in enumerate(v):out[(w+1)*ix+i]=e*x
        return out
    @lru_cache(None)
    def symbol(v,r):
        out=[0]*D
        for g in edge_matrices(r):
            term=manin(compose(v,g),g[2],g[3])
            out=[a+b for a,b in zip(out,term)]
        return tuple(out)
    def lift(c,d):return (0,-1,1,d) if c==1 else (1,0,c,1)
    def hecke(ell):
        rows=[]
        deltas=[((1,j,0,ell),1) for j in range(ell)]+[((ell,0,0,1),eps(ell))]
        for c,d in P1:
            g=lift(c,d)
            for i in range(w+1):
                gp=compose(monomial(i),adj(g));out=[0]*D
                for h,e in deltas:
                    A,B,C,Dd=mm(h,g)
                    hp=compose(gp,adj(h))
                    left=symbol(hp,rat(B,Dd));right=symbol(hp,rat(A,C))
                    out=[a+e*(b-c) for a,b,c in zip(out,left,right)]
                rows.append(out)
        return sp.Matrix(rows)
    S=(0,-1,1,0);R=(0,-1,1,-1);R2=mm(R,R)
    relations=[]
    for c,d in P1:
        for i in range(w+1):
            v=monomial(i);base=manin(v,c,d)
            def action(h):return manin(compose(v,h),*rowmul((c,d),h))
            relations.append([a+b for a,b in zip(base,action(S))])
            relations.append([a+b+c for a,b,c in zip(base,action(R),action(R2))])
    Rel=sp.Matrix(relations)
    B=sp.Matrix.hstack(*Rel.nullspace())
    print('CMPOWER',m,'generators',D,'relation_rank',D-B.cols,flush=True)
    T3,T5=hecke(3),hecke(5)
    assert Rel*T3*B==sp.zeros(Rel.rows,B.cols)
    assert Rel*T5*B==sp.zeros(Rel.rows,B.cols)
    traces=[2,-2]
    for i in range(2,m+1):traces.append(-2*traces[-1]-5*traces[-2])
    a5=traces[m]
    Eq=Rel.col_join(T3).col_join(T5-a5*sp.eye(D))
    cusp=Eq.nullspace()
    print('CMPOWER',m,'CM_quotient_dimension',len(cusp),'a5',a5,flush=True)
    assert len(cusp)==2
    Phi=sp.Matrix.hstack(*[sp.Matrix(integer_vector(v)) for v in cusp])
    # Saturate the rank-two lattice at5 by elementary exact divisions.
    saturation_steps=[]
    while mod_rank(Phi.T.tolist(),5)<2:
        if all(int(x)%5==0 for x in Phi[:,0]):
            Phi[:,0]=Phi[:,0]/5;saturation_steps.append(['divide',0]);continue
        if all(int(x)%5==0 for x in Phi[:,1]):
            Phi[:,1]=Phi[:,1]/5;saturation_steps.append(['divide',1]);continue
        c=next(c for c in range(5) if all((int(Phi[i,1])+c*int(Phi[i,0]))%5==0 for i in range(D)))
        Phi[:,1]=(Phi[:,1]+c*Phi[:,0])/5;saturation_steps.append(['combine_divide',c])
    assert Eq*Phi==sp.zeros(Eq.rows,2)
    assert all(x.q==1 for x in Phi)
    phi=[[int(x) for x in row] for row in Phi.tolist()]
    def value(poly,r):
        v=symbol(poly,r)
        return [sum(v[a]*phi[a][i] for a in range(D)) for i in range(2)]
    # The homological conjugation involution acts by z -> -conj(z)
    # and P(X,Y) -> P(-X,Y).  Top-critical integrals consequently
    # satisfy C I_n(a)=(-1)^w I_n(-a).  This certifies that each
    # character specialization is in one period line, not a sum of
    # uncontrolled plus/minus periods.
    conjrows=[]
    Cgeom=(-1,0,0,1)
    for c,d in P1:
        g=lift(c,d);a,b,c,d=g
        for i in range(w+1):
            gp=compose(compose(monomial(i),adj(g)),Cgeom)
            left=value(gp,rat(-b,d));right=value(gp,rat(-a,c))
            conjrows.append([x-y for x,y in zip(left,right)])
    CPhi=sp.Matrix(conjrows)
    C=(Phi.T*Phi).inv()*Phi.T*CPhi
    assert Phi*C==CPhi and C*C==sp.eye(2)
    assert all(x.q%5 for x in C)
    def c_mod(modulus):
        return [[int(C[i,j].p)*pow(int(C[i,j].q),-1,modulus)%modulus
                 for j in range(2)] for i in range(2)]
    chi={v:int(sp.kronecker_symbol(24,v)) for v in range(24)}
    def linear_power(a,b):return tuple(comb(w,i)*a**(w-i)*b**i for i in range(w+1))
    def I(d,n,a):
        q=5**n
        if d==1:return value(linear_power(q,-a),Fraction(a,q))
        assert d==6 and m%2
        # 24^w*tau(chi24)*I_n(f twist chi24).
        vals=[(e,value(linear_power(24*q,-24*a-q*v),Fraction(a,q)+Fraction(v,24)))
              for v,e in chi.items() if e]
        return [sum(e*z[i] for e,z in vals) for i in range(2)]
    def unit_root(h):
        alpha=a5%5
        modulus=5
        for _ in range(1,h):
            alpha=next(alpha+modulus*b for b in range(5)
                       if ((alpha+modulus*b)**2-a5*(alpha+modulus*b)+5**m)%(5*modulus)==0)
            modulus*=5
        assert (alpha*alpha-a5*alpha+5**m)%modulus==0
        return alpha
    curves={}
    for d in ([1,6] if m%2 else [1]):
        I1={a:I(d,1,a) for a in range(1,5)}
        I0={a:I(d,0,a) for a in range(1,5)}
        I2={a:I(d,2,a) for a in range(1,25) if a%5}
        checks={}
        for a in range(1,5):
            lhs=[sum(I2[a+5*b][i] for b in range(5)) for i in range(2)]
            rhs=[a5*I1[a][i]-5**w*I0[a][i] for i in range(2)]
            assert lhs==rhs
            checks[a]=lhs
        alpha=a5%5
        measure={a:[(pow(alpha,-1,5)*I1[a][i]-5**w*pow(alpha,-2,5)*I0[a][i])%5
                    for i in range(2)] for a in range(1,5)}
        moments={j:[sum(pow(a,j,5)*measure[a][i] for a in range(1,5))%5
                    for i in range(2)] for j in range(4)}
        curves[d]={'I1':I1,'I0':I0,'I2':I2,'exact_distribution_rhs':checks,
                   'measure_residue_classes_mod5':measure,'branch_constant_terms_mod5':moments,
                   'target_untwisted_Kato_branch_j':(-m)%4}
        # Desired negative Tate twists through lower-central degree eight.
        # The bounded top-critical measure evaluates the Kato L-function
        # at chi^(-t) when its integrand is chi^(-m-t).
        t_values=list(range((6-m)//2+1))
        specializations={}
        for h in [2,3]:
            modulus=5**h
            alpha=unit_root(h)
            units=[a for a in range(1,modulus) if a%5]
            Ih=I2 if h==2 else {a:I(d,h,a) for a in units}
            parent=I1 if h==2 else I2
            masses={a:[(pow(alpha,-h,modulus)*Ih[a][i]
                        -5**w*pow(alpha,-h-1,modulus)*parent[a%(modulus//5)][i])%modulus
                       for i in range(2)] for a in units}
            vals={t:[sum(pow(a,-m-t,modulus)*masses[a][i] for a in units)%modulus
                     for i in range(2)] for t in t_values}
            Cmod=c_mod(modulus)
            for t,vec in vals.items():
                sign=(-1)**(w+m+t)
                assert [sum(vec[i]*Cmod[i][j] for i in range(2))%modulus for j in range(2)]==[(sign*x)%modulus for x in vec]
            specializations[h]={'modulus':modulus,'alpha':alpha,'raw_Ih':Ih,
                                'measure_masses_modulus':masses,'Tate_twist_t_values':vals,
                                'homological_period_eigenvalue_by_t':{t:(-1)**(w+m+t) for t in t_values},
                                'single_period_line_checks':True}
            print('CMPOWER',m,'curve',d,'precision',h,'specializations',vals,flush=True)
            if all(any(vec) for vec in vals.values()):break
        curves[d]['negative_Tate_specializations']=specializations
        print('CMPOWER',m,'curve',d,'moments',moments,flush=True)
    out={'CM_power':m,'weight':m+1,'level':N,'nebentypus':'epsilon_-4' if w%2 else 'trivial',
         'dimension_before_relations':D,'relation_rank':D-B.cols,'relative_dimension':B.cols,
         'equation_rank':D-2,'equation_rank_mod5':mod_rank(Eq.tolist(),5),
         'period_basis_rank_mod5':mod_rank(Phi.T.tolist(),5),'p_saturation_steps':saturation_steps,
         'a3':0,'a5':a5,'Manin_generators':P1,'integral_period_dual_basis_columns':phi,
         'homological_complex_conjugation_matrix':[[str(x) for x in row] for row in C.tolist()],
         'curves':curves,'exact_Hecke_descent_and_distribution_checks':True,
         'scope':'Exact finite Manin/Hecke and top-critical ordinary measure calculation. CM form identification and arithmetic deduction are separate.'}
    (HERE/f'F_advanced_cm_power_{m}.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('m',type=int)
    args=p.parse_args();assert 1<=args.m<=6
    main(args.m)
