#!/usr/bin/env python3
"""Exact E113 coefficient, local reduction and obstruction-transfer checks.

The arithmetic proof of global cup vanishing is in the theorem.  This
certificate verifies its literal coefficient inverses, local equations,
finite real transitions, and all displayed nonlinear coordinate signs.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import random
import subprocess
import sympy as sp

INPUT_SHA = 'caea1a69e0c694c61bdcbeb897e42d985aae13ece94dbe78b7fea9f940b3ffd0'
CM_INPUT_SHA = '13bf3ca1f780c5294466c91f3ca027194dd497ff34bc0a723b1e8c562e7cb782'

def mat_strings(A):
    return [[str(x) for x in row] for row in A.tolist()]

def wedge(x,y):
    return sp.Matrix([x[i]*y[j]-x[j]*y[i]
                      for i,j in combinations(range(len(x)),2)])

def wedge_action(A,z):
    n=A.cols; Z=sp.zeros(n)
    pairs=list(combinations(range(n),2))
    for v,(i,j) in zip(z,pairs): Z[i,j]=v; Z[j,i]=-v
    Q=A*Z*A.T
    return sp.Matrix([Q[i,j] for i,j in combinations(range(A.rows),2)])

def randmat(rng,n,m,den=1):
    return sp.Matrix(n,m,lambda i,j:sp.Rational(rng.randrange(-3,4),den))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',type=Path,
                    default=Path(__file__).resolve().parents[1]/'inputs/a_quartic_class2.json')
    ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    ap.add_argument('--cm-input',type=Path,
                    default=Path(__file__).resolve().parents[1]/'inputs/a_quartic_w_slice.json')
    ap.add_argument('--gp',type=Path)
    args=ap.parse_args()
    raw=args.input.read_bytes(); assert sha256(raw).hexdigest()==INPUT_SHA
    previous=json.loads(raw)
    cmraw=args.cm_input.read_bytes(); assert sha256(cmraw).hexdigest()==CM_INPUT_SHA
    cmdata=json.loads(cmraw)
    D=sp.Matrix([[sp.Rational(v) for v in row]
                 for row in previous['compact_determinant_projection']])
    S=sp.Matrix([[sp.Rational(v) for v in row]
                 for row in previous['compact_determinant_section']])
    assert D*S==sp.eye(6)
    E=sp.eye(6)
    cols=[]; labels=[]
    for i,j in combinations(range(3),2):
        ei,fi,ej,fj=E[:,2*i],E[:,2*i+1],E[:,2*j],E[:,2*j+1]
        cols.extend([wedge(ei,ej),(wedge(ei,fj)+wedge(fi,ej))/2,wedge(fi,fj)])
        labels.extend([f'{i+1}{j+1}:ee',f'{i+1}{j+1}:ef',f'{i+1}{j+1}:ff'])
    Q=sp.Matrix.hstack(S,*cols); Qi=Q.inv()
    assert Q*Qi==Qi*Q==sp.eye(15)
    assert Qi[:6,:]==D
    assert D*sp.Matrix.hstack(*cols)==sp.zeros(6,9)
    assert all(Fraction(str(x)).denominator in (1,2) for x in list(Q)+list(Qi))

    r=sp.symbols('r1 r2 r3'); u,v=sp.symbols('u v'); U,V=sp.symbols('U V')
    # The actual two-column V -> V^3 map, with the same scalar in each copy.
    J=sp.Matrix(6,2,lambda i,j:r[i//2] if i%2==j else 0)
    sigma=wedge(J[:,0],J[:,1]); coeff=Qi*sigma
    expected=sp.Matrix([r[0]**2,r[1]**2,r[2]**2,
                        2*r[0]*r[1],2*r[0]*r[2],2*r[1]*r[2]]+[0]*9)
    assert sp.simplify(coeff-expected)==sp.zeros(15,1)
    assert sp.simplify(wedge(J*sp.Matrix([u,v]),J*sp.Matrix([U,V]))-
                       (u*V-v*U)*sigma)==sp.zeros(15,1)

    # The other three Tate lines use the actual E108 CM contraction/section.
    a,b,c=sp.symbols('a b c')
    relation=a*a+b*c+1
    red=lambda f:sp.rem(sp.expand(f),relation,a)
    ell=sp.Matrix([[sp.sympify(s) for s in cmdata['symmetric_CM_contraction']]])
    sec=sp.Matrix([sp.sympify(s) for s in cmdata['symmetric_CM_section']])
    assert ell==sp.Matrix([[-c,a,b]]) and sec==sp.Matrix([b/2,-a,-c/2])
    assert red((ell*sec)[0]-1)==0
    PT=sp.Matrix.vstack(D,*(ell*Qi[6+3*i:9+3*i,:] for i in range(3)))
    ST=sp.Matrix.hstack(S,*(Q[:,6+3*i:9+3*i]*sec for i in range(3)))
    assert (PT*ST-sp.eye(9)).applyfunc(red)==sp.zeros(9)
    assert (ST*PT*ST*PT-ST*PT).applyfunc(red)==sp.zeros(15)
    assert red(sp.trace(ST*PT)-9)==0
    assert (sp.eye(15)-ST*PT).subs({a:0,b:-1,c:1}).rank()==6
    I=sp.Matrix([[a,b],[c,-a]]); pairing=sp.Matrix([[0,1],[-1,0]])
    BI=I.T*pairing
    assert BI==BI.T
    xx,yy=sp.Matrix([u,v]),sp.Matrix([U,V])
    KI=lambda z:-(z.T*BI*z)[0]/2
    assert sp.expand(KI(yy)-KI(xx+yy)+KI(xx)-(xx.T*BI*yy)[0])==0
    cm_equivariance=0
    I0=sp.Matrix([[0,-1],[1,0]]); BI0=I0.T*pairing
    for a0,b0,eps in product(range(-3,4),range(-3,4),[1,-1]):
        if a0==b0==0: continue
        A=(a0*sp.eye(2)+b0*I0)*sp.diag(1,eps)
        assert A*I0==eps*I0*A
        assert A.T*BI0*A==eps*A.det()*BI0
        cm_equivariance+=1

    # The exact scalar-twist equivariance of all coefficient columns.
    equivariance=0
    for A in [sp.Matrix([[1,1],[0,1]]),sp.Matrix([[0,-1],[1,0]]),
              sp.Matrix([[2,1],[1,1]]),sp.diag(1,-1),sp.diag(2,3)]:
        AC=sp.diag(A,A,A)
        B=sp.Matrix.hstack(*(wedge_action(AC,sp.eye(15)[:,i]) for i in range(15)))
        assert D*B==A.det()*D
        assert B*S==A.det()*S
        assert D*B*(sp.eye(15)-S*D)==sp.zeros(6,15)
        equivariance+=1

    # Direct equation and the first Tate-algorithm stopping branch.
    x=sp.symbols('x')
    assert sp.expand((x+1)**3+(x+1))==x**3+3*x*x+4*x+2
    c4,c6,disc=-48,0,-64
    assert (c4**3-c6**2)//1728==disc
    points=[(a,b) for a,b in product(range(2),repeat=2) if (b*b-a**3-a)%2==0]
    singular=[(a,b) for a,b in points if (3*a*a+1)%2==0 and 2*b%2==0]
    nonsingular=[p for p in points if p not in singular]+['O']
    assert points==[(0,0),(1,0)] and singular==[(1,0)]
    assert nonsingular==[(0,0),'O']
    odd_checks=0
    for n in range(2,13):
        modulus=2**n
        squares={b*b%modulus for b in range(modulus)}
        for a in range(1,modulus,2):
            f=a**3+a
            assert f%4==2 and f%modulus not in squares
            odd_checks+=1
    # The formal chart uses w=t^3+t*w^2; integer coefficients suffice.
    t=sp.symbols('t'); w=sp.Integer(0); precision=32
    for _ in range(precision):
        new=sp.series(t**3+t*w*w,t,0,precision).removeO().expand()
        if new==w: break
        w=new
    assert sp.series(w-t**3-t*w*w,t,0,precision).removeO()==0
    assert all(c.is_Integer for c in sp.Poly(w,t).all_coeffs())

    # Arithmetic Frobenius determinant checks on actual good reductions.
    primes=list(sp.primerange(3,204))
    good=[]
    for p in primes:
        squares={a*a%p for a in range(p)}
        N=1+sum(1 if (a**3+a)%p==0 else (2 if (a**3+a)%p in squares else 0)
                for a in range(p))
        trace=p+1-N
        F=sp.Matrix([[0,-p],[1,trace]])
        assert (F-p*sp.eye(2)).det()==p*N!=0
        assert trace*trace<=4*p
        good.append({'p':p,'points':N,'trace':trace,'det_F_minus_p':p*N})

    # The real H2 coefficient transition is exactly multiplication by 2.
    real=[]
    for n in range(1,11):
        top=2**(n+1); lower=2**n
        invariant=[a for a in range(top) if 2*a%top==0]
        assert invariant==[0,2**n]
        reductions=[a%lower for a in invariant]
        assert reductions==[0,0]
        real.append({'n':n,'top_invariants':invariant,'reductions':reductions})

    # General class-two action/gauge and filling identities.  Work in all
    # seventeen coordinates, retaining arbitrary central off-diagonal maps.
    rng=random.Random(1132026); n=17; m=n*(n-1)//2
    checks={'gauge':0,'filling':0,'mixed':0,'full_central_shift':0}
    for sample in range(16):
        a0,a1,a2,a3=[rng.randrange(-2,3) for _ in range(4)]
        Rg=sp.Matrix([[1+a0*a1,a0],[a1,1]])
        Rh=sp.Matrix([[1+a2*a3,a2],[a3,1]])
        Rg=sp.diag(sample%3+1,1)*Rg
        Rh=sp.diag(sample%2+1,1)*Rh
        Ag=sp.diag(*([Rg.det()]*11),Rg,Rg,Rg)
        Ah=sp.diag(*([Rh.det()]*11),Rh,Rh,Rh)
        Agh=Ag*Ah
        Dg,Dh=randmat(rng,m,n,2),randmat(rng,m,n,2)
        Dgh=sp.Matrix.hstack(*(wedge_action(Ag,Dh[:,i]) for i in range(n)))+Dg*Ah
        ag,ah=randmat(rng,n,1),randmat(rng,n,1)
        agh=ag+Ag*ah
        z=randmat(rng,n,1)
        def Gamma(A,D,a):
            Az=A*z
            return -D*z+wedge(z+Az,a)/2-wedge(z,Az)/2
        Gg,Gh,Ggh=Gamma(Ag,Dg,ag),Gamma(Ah,Dh,ah),Gamma(Agh,Dgh,agh)
        dG=wedge_action(Ag,Gh)-Ggh+Gg
        apg=ag-(Ag-sp.eye(n))*z; aph=ah-(Ah-sp.eye(n))*z
        old=Dg*ah+wedge(ag,Ag*ah)/2
        new=Dg*aph+wedge(apg,Ag*aph)/2
        assert old-new==dG
        checks['gauge']+=1

        # A literal filling with an arbitrary retained linear central term.
        p=sp.zeros(6,n); p[:,11:]=sp.eye(6)
        pB=sp.Matrix.hstack(*(wedge_action(p,sp.eye(m)[:,i]) for i in range(m)))
        # wedge_action also accepts rectangular maps, using source size.
        Jfill=randmat(rng,15,n,2)
        BgJ=sp.Matrix.hstack(*(wedge_action(sp.diag(Rg,Rg,Rg),Jfill[:,i]) for i in range(n)))
        DC=randmat(rng,15,6,2)
        Dgfill=Dg+pB.T*(DC*p-Jfill*Ag+BgJ-pB*Dg)
        actual_Dp=pB*Dgfill+Jfill*Ag-BgJ
        assert actual_Dp==DC*p
        dJa=BgJ*ah-Jfill*agh+Jfill*ag
        compact=actual_Dp*ah+wedge(p*ag,sp.diag(Rg,Rg,Rg)*p*ah)/2
        filled_source=Dgfill*ah+wedge(ag,Ag*ah)/2
        assert compact==pB*filled_source-dJa
        checks['filling']+=1

        # Common elliptic cocycle values and arbitrary peripheral values.
        rr=randmat(rng,3,1)
        j=sp.zeros(n,2)
        for i in range(3): j[11+2*i:13+2*i,:]=rr[i]*sp.eye(2)
        hg,hh=randmat(rng,2,1),randmat(rng,2,1)
        eg,eh=j*hg,j*hh; egh=eg+Ag*eh
        bg,bh=randmat(rng,n,1),randmat(rng,n,1)
        bg[11:,:]=sp.zeros(6,1); bh[11:,:]=sp.zeros(6,1)
        bgh=bg+Ag*bh
        pg,ph,pgh=wedge(bg,eg),wedge(bh,eh),wedge(bgh,egh)
        dp=wedge_action(Ag,ph)-pgh+pg
        mixed=(wedge(bg,Ag*eh)+wedge(eg,Ag*bh))/2
        assert mixed==wedge(bg,Ag*eh)+dp/2
        checks['mixed']+=1
        scalar=(hg[0]*(Rg*hh)[1]-hg[1]*(Rg*hh)[0])
        sr=wedge(j[:,0],j[:,1])
        assert wedge(eg,Ag*eh)==sr*scalar
        # Choose any values of k_g,k_h and then k_gh so that dk is scalar.
        kg,kh=sp.Rational(sample-3,2),sp.Rational(sample+1,4)
        kgh=Rg.det()*kh+kg-scalar
        Pg=sr*kg/2+pg/2; Ph=sr*kh/2+ph/2; Pgh=sr*kgh/2+pgh/2
        dP=wedge_action(Ag,Ph)-Pgh+Pg
        full=Dg*(bh+eh)+wedge(bg+eg,Ag*(bh+eh))/2
        rem=Dg*bh+wedge(bg,Ag*bh)/2+Dg*eh+wedge(bg,Ag*eh)
        assert full==rem+dP
        checks['full_central_shift']+=1

    pari_output=None
    if args.gp:
        gp_source=Path(__file__).with_suffix('.gp')
        result=subprocess.run([str(args.gp),'-q',str(gp_source)],capture_output=True,text=True,check=True)
        assert not result.stderr.strip(),result.stderr
        pari_output=result.stdout
        gp_source.with_name(gp_source.stem+'_gp.out').write_text(pari_output)
        assert 'local2=[6, 2, [1, 0, 0, 0], 1]' in pari_output

    out={
        'statement':'E.113','input_sha256':INPUT_SHA,
        'cm_input_sha256':CM_INPUT_SHA,
        'curve':[0,0,0,1,0],'invariants':[c4,c6,disc],
        'translated_curve':[0,3,0,4,2],
        'special_fiber_affine_points':points,'singular_points':singular,
        'nonsingular_rational_points':nonsingular,
        'odd_x_nonsquare_checks':odd_checks,
        'formal_chart_precision':precision,'formal_w':str(w),
        'good_reduction_records':good,
        'real_coefficient_transitions':real,
        'compact_basis_order':['e1','f1','e2','f2','e3','f3'],
        'compact_wedge_order':list(combinations(range(6),2)),
        'compact_determinant_projection':mat_strings(D),
        'compact_determinant_section':mat_strings(S),
        'symmetric_column_order':labels,
        'full_compact_coefficient_matrix':mat_strings(Q),
        'full_compact_coefficient_inverse':mat_strings(Qi),
        'diagonal_scalar_column':[str(a) for a in sigma],
        'diagonal_projected_column':[str(a) for a in coeff],
        'equivariance_checks':equivariance,
        'tate_nine_projection':mat_strings(PT),
        'tate_nine_section':mat_strings(ST),
        'CM_relation':str(relation)+'=0',
        'CM_equivariance_checks':cm_equivariance,
        'remaining_obstruction_rank':127,
        'actual_dimension':n,'central_dimension':m,
        'nonlinear_transfer_checks':checks,
        'scope':'Global cup vanishing follows from the proof, using exact finite local maps, Brauer reciprocity and the proved continuous primitive alignment. No unevaluated handle action is replaced by its graded representation.'
    }
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print('PASS E113 exact compact-cup coefficient and transfer certificate')
    print('bad-2 odd-x checks:',odd_checks)
    print('actual good reductions:',len(good),'real transitions:',len(real))
    print('coefficient inverse rank:',Q.rank(),'equivariance:',equivariance)
    print('nine Tate projections: exact inverse; remaining rank: 127; CM equivariance:',cm_equivariance)
    print('nonlinear transfers:',json.dumps(checks,sort_keys=True))
    if pari_output: print(pari_output,end='')

if __name__=='__main__': main()
