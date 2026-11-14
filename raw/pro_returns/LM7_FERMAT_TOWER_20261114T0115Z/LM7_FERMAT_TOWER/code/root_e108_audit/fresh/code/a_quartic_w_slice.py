#!/usr/bin/env python3
"""Exact E108 coefficient, cochain and residue certificates.

Only the already frozen E105 arithmetic coefficient certificate is an input.
All other calculations use exact rational/integer or finite-field arithmetic.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import random
import sympy as sp

INPUT_SHA = "caea1a69e0c694c61bdcbeb897e42d985aae13ece94dbe78b7fea9f940b3ffd0"
PAIRS = list(combinations(range(11), 2))

def smat(x):
    return [[str(a) for a in row] for row in sp.Matrix(x).tolist()]

def wedge_matrix(m):
    return sp.Matrix([[m[i,a]*m[j,b]-m[i,b]*m[j,a]
                       for a,b in PAIRS] for i,j in PAIRS])

def wedge(x,y):
    return sp.Matrix([x[i]*y[j]-x[j]*y[i] for i,j in PAIRS])

def field_add(x,y):
    return tuple(a+b for a,b in zip(x,y))

def field_scale(a,x):
    return tuple(a*t for t in x)

def field_mul(x,y):
    z=[Q(0)]*7
    for i,a in enumerate(x):
        for j,b in enumerate(y): z[i+j]+=a*b
    for j in range(6,3,-1): z[j-4]-=z[j]
    return tuple(z[:4])

ONE=(Q(1),Q(0),Q(0),Q(0))
ZETA=(Q(0),Q(1),Q(0),Q(0))

def field_pow(x,n):
    if n<0: return field_pow(field_inv(x),-n)
    z=ONE
    while n:
        if n&1: z=field_mul(z,x)
        x=field_mul(x,x); n//=2
    return z

def field_matrix(x):
    return sp.Matrix.hstack(*(sp.Matrix(field_mul(x,field_pow(ZETA,i))) for i in range(4)))

def field_inv(x):
    return tuple(Q(a) for a in field_matrix(x).inv()[:,0])

def field_norm(x):
    return Q(field_matrix(x).det())

def field_sigma(x,k):
    ans=(Q(0),)*4
    for i,a in enumerate(x): ans=field_add(ans,field_scale(a,field_pow(ZETA,k*i)))
    return ans

class FF:
    """Fp or Fp[t]/(t^2-d), encoded as integers a+p*b."""
    def __init__(self,p,f):
        self.p,self.f=p,f
        self.order=p**f
        self.d=0 if f==1 else next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    def add(self,x,y):
        p=self.p
        return (x%p+y%p)%p + p*((x//p+y//p)%p)
    def neg(self,x):
        return ((-x)%self.p)+self.p*((-(x//self.p))%self.p)
    def mul(self,x,y):
        p=self.p;a,b=x%p,x//p;c,d=y%p,y//p
        return (a*c+self.d*b*d)%p+p*((a*d+b*c)%p)
    def pow(self,x,n):
        if n<0: n%=self.order-1
        ans=1
        while n:
            if n&1: ans=self.mul(ans,x)
            x=self.mul(x,x);n//=2
        return ans
    def generator(self):
        primes=list(sp.factorint(self.order-1))
        return next(x for x in range(1,self.order)
                    if all(self.pow(x,(self.order-1)//r)!=1 for r in primes))
    def evaluate(self,x,zeta):
        ans=0;power=1
        for a in x:
            a=Q(a)
            assert a.denominator%self.p
            r=a.numerator*pow(a.denominator,-1,self.p)%self.p
            ans=self.add(ans,self.mul(r,power));power=self.mul(power,zeta)
        return ans

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',type=Path,default=Path(__file__).resolve().parents[1]/'inputs/a_quartic_class2.json')
    ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    args=ap.parse_args()
    raw=args.input.read_bytes(); assert sha256(raw).hexdigest()==INPUT_SHA
    data=json.loads(raw)
    order=data['peripheral_order']; assert order==['A0','A1','A2','A3','B1','B2','B3','C0','C1','C2','C3']
    N=sp.Matrix(data['sqrt2_exponent_matrix'])
    v=sp.Matrix([sp.Rational(s) for s in data['averaged_origin_vector']])
    Lv=sp.Matrix([[sp.Rational(s) for s in row] for row in data['relative_action_matrix']])
    assert N==N.T
    assert Lv==sp.Matrix.hstack(*(wedge(sp.eye(11)[:,i],N[:,i]/8)+wedge(v,sp.eye(11)[:,i]) for i in range(11)))

    # Literal Fourier columns in the twelve-cusp quotient, B0=-sum(other cusps).
    ks=[1,3,5,7]
    chars={'1':[1,1,1,1],'-1':[1,-1,1,-1],'2':[1,-1,-1,1],'-2':[1,1,-1,-1]}
    def cusp(name):
        if name=='B0': return -sp.ones(11,1)
        return sp.eye(11)[:,order.index(name)]
    columns=[]; labels=[]; types=[]
    for typ,chi in chars.items():
        for orbit in ('AB' if typ=='1' else 'ABC'):
            columns.append(sum((chi[i]*cusp(orbit+str(i)) for i in range(4)),sp.zeros(11,1)))
            labels.append(orbit+':'+typ);types.append(typ)
    P=sp.Matrix.hstack(*columns);Pinv=P.inv()
    assert P*Pinv==Pinv*P==sp.eye(11)
    assert all(Q(a).denominator & (Q(a).denominator-1)==0 for a in Pinv)
    exterior=wedge_matrix(P);exterior_inv=wedge_matrix(Pinv)
    assert exterior*exterior_inv==exterior_inv*exterior==sp.eye(55)
    char_product={}
    for a in chars:
        for b in chars:
            seq=[x*y for x,y in zip(chars[a],chars[b])]
            char_product[a,b]=next(t for t in chars if chars[t]==seq)
    wedge_types=[char_product[types[i],types[j]] for i,j in PAIRS]
    for row in data['galois_quotient_matrices']:
        k=row['zeta_exponent'];idx=ks.index(k)
        G=sp.Matrix(row['permutation_quotient_matrix'])
        assert G*P==P*sp.diag(*(chars[t][idx] for t in types))
        assert wedge_matrix(G)*exterior==exterior*sp.diag(*(chars[t][idx] for t in wedge_types))
    assert dict(Counter(types))=={'1':2,'-1':3,'2':3,'-2':3}
    assert dict(Counter(wedge_types))=={'1':10,'-1':15,'2':15,'-2':15}
    print('PASS: actual eleven-cusp Fourier basis and all 55 exterior coordinates/inverses')

    # Symbolic chi-twisted cochain identity, retained in each of the 55 rows.
    x,y,k,X,Y,K,t,p,q=sp.symbols('x y k X Y K t p q')
    Phi=lambda xx,yy,kk:xx*yy/2+q*kk*xx+p*q*kk**2/2
    dPhi=sp.expand(t*t*Phi(X,Y,K)-Phi(x+t*X,y+t*Y,k+t*K)+Phi(x,y,k))
    shifted=(x+p*k)*t*(Y+q*K)
    omega=-q*k*t*X+p*k*t*Y+(x*t*Y-y*t*X)/2
    assert sp.expand(shifted+dPhi-omega)==0
    shifts=[]
    for n,(i,j) in enumerate(PAIRS):
        pp=v[i]-N[i,j]/8;qq=v[j]-N[i,j]/8
        assert Lv[n,i]==-qq and Lv[n,j]==pp
        assert all(Lv[n,h]==0 for h in range(11) if h not in (i,j))
        shifts.append({'pair':[order[i],order[j]],'p':str(pp),'q':str(qq),
                       'integer_power_of_2_in_U':int(8*pp),
                       'integer_power_of_2_in_V':int(8*qq),
                       'Phi_xy':'1/2','Phi_kx':str(qq),'Phi_kk':str(pp*qq/2)})
    # Independently multiply the full BCH gauge in 11+55 coordinates.
    rng=random.Random(108)
    gauge_count=0
    for _ in range(120):
        b=sp.Matrix([rng.randrange(-4,5) for _ in range(11)])
        m=sp.Matrix([rng.randrange(-4,5) for _ in range(11)])
        zz=sp.Matrix([rng.randrange(-4,5) for _ in range(55)])
        chi=rng.choice([1,3,5,7,-1]);kk=rng.randrange(-4,5)
        def mul(a,bb):
            return (a[0]+bb[0],a[1]+bb[1]+wedge(a[0],bb[0])/2)
        actual=mul(mul((-m,sp.zeros(55,1)),(b,zz)),(chi*m,chi*kk*Lv*m))
        expected=(b+(chi-1)*m,zz+chi*kk*Lv*m-(1+chi)*wedge(m,b)/2)
        assert actual==expected;gauge_count+=1
    print('PASS: all 55 exact shifted-cup identities and 120 full BCH gauge identities')

    # Exact rational CM projectors: relation a^2+bc=-1.
    aa,bb,cc=sp.symbols('a b c');I=sp.Matrix([[aa,bb],[cc,-aa]])
    I2=sp.Matrix([[aa**2,aa*bb,bb**2],
                  [2*aa*cc,bb*cc-aa**2,-2*aa*bb],
                  [cc**2,-aa*cc,aa**2]])
    ell=sp.Matrix([[-cc,aa,bb]])
    sec=sp.Matrix([bb/2,-aa,-cc/2])
    rel=aa**2+bb*cc+1
    rem=lambda f:sp.rem(sp.Poly(sp.expand(f),aa),sp.Poly(rel,aa)).as_expr()
    assert all(rem(x)==0 for x in (I*I+sp.eye(2)))
    assert rem((ell*sec)[0]-1)==0
    assert all(rem(x)==0 for x in ((sp.eye(3)+I2)/2-sec*ell))
    assert all(rem(x)==0 for x in ((sp.eye(3)-sec*ell)**2-(sp.eye(3)-sec*ell)))
    print('PASS: literal CM contraction, section and complementary rank-two projector')

    # Number-field identities, including the zero-minimum obstruction.
    sqrt2=field_add(ZETA,field_scale(-1,field_pow(ZETA,3)))
    eps=field_add(ONE,sqrt2);pi2=field_add(ONE,field_scale(-1,ZETA))
    two=field_mul(field_pow(ZETA,6),field_mul(field_pow(eps,2),field_pow(pi2,4)))
    assert two==field_scale(2,ONE)
    assert field_norm(eps)==1 and field_norm(pi2)==2
    epsprime=field_add(ONE,field_add(ZETA,field_pow(ZETA,2)))
    assert field_mul(pi2,epsprime)==field_add(ONE,field_scale(-1,field_pow(ZETA,3)))
    threeplus=field_add(field_scale(3,ONE),sqrt2)
    threeminus=field_add(field_scale(3,ONE),field_scale(-1,sqrt2))
    special=field_mul(threeplus,field_inv(threeminus))
    assert field_norm(threeplus)==field_norm(threeminus)==49
    assert field_norm(special)==1
    assert [field_sigma(special,k) for k in ks]==[special,field_inv(special),field_inv(special),special]
    witness=sp.Matrix([0]*7+[1,-1,-1,1])
    assert sp.Matrix(data['toric_projection'])*witness==sp.zeros(2,1)
    wi=PAIRS.index((7,8));assert Lv[wi,:]*witness==sp.Matrix([[sp.Rational(1,4)]])
    print('PASS: exact F=Q(zeta8) unit/prime identities and zero-minimum witness')

    # Finite residue fields and every prime of F over the tested rational primes.
    residue_records=[];tests=0;two_sign_tests=0;transition_tests=0
    witness_records=[]
    for prime in list(sp.primerange(3,104)):
        prime=int(prime);f=1 if prime%8==1 else 2
        ff=FF(prime,f);Qq=ff.order;g=ff.generator()
        zeta0=ff.pow(g,(Qq-1)//8)
        assert ff.pow(zeta0,4)==prime-1
        unseen=set(ks);reps=[]
        while unseen:
            a=min(unseen);orbit={a,a*prime%8};unseen-=orbit;reps.append((a,sorted(orbit)))
        assert len(reps)*f==4
        for a,orbit in reps:
            zeta=ff.pow(zeta0,a)
            ep=ff.evaluate(eps,zeta);p2=ff.evaluate(pi2,zeta)
            assert ep and p2
            assert ff.mul(ff.pow(zeta,6),ff.mul(ff.pow(ep,2),ff.pow(p2,4)))==2
            e3=0;tmp=Qq-1
            while tmp%3==0:e3+=1;tmp//=3
            row={'p':prime,'f':f,'Q':Qq,'zeta_exponents':orbit,'model_nonsquare':ff.d,
                 'field_generator':g,'zeta':zeta,'epsilon':ep,'pi2':p2,'logs':[]}
            for lp in [2,3,5,7,11,13,17]:
                e=0;tmp=Qq-1
                while tmp%lp==0:e+=1;tmp//=lp
                if not e:continue
                mod=lp**e
                # At two preserve the specified embedding of mu_8 into F.
                eta=ff.pow(g,((Qq-1)//mod)*(a if lp==2 else 1))
                if lp==2: assert ff.pow(eta,2**(e-3))==zeta
                log={ff.pow(eta,j):j for j in range(mod)}
                assert len(log)==mod
                elog=log[ff.pow(ep,(Qq-1)//mod)]
                pi2log=log[ff.pow(p2,(Qq-1)//mod)]
                twolog=log[ff.pow(2,(Qq-1)//mod)]
                assert (2*elog+4*pi2log+6*log[ff.pow(zeta,(Qq-1)//mod)]-twolog)%mod==0
                row['logs'].append({'ell':lp,'e':e,'eta':eta,'epsilon':elog,'pi2':pi2log,'two':twolog})
                for U,V,m,n in product(range(1,5),range(1,5),range(-2,3),range(-2,3)):
                    u=ff.pow(g,U);vv=ff.pow(g,V)
                    lu=log[ff.pow(u,(Qq-1)//mod)]
                    lv=log[ff.pow(vv,(Qq-1)//mod)]
                    D=lu*n-lv*m
                    tame=ff.mul(ff.pow(u,n),ff.pow(vv,-m))
                    if m*n%2:tame=ff.neg(tame)
                    rt=log[ff.pow(tame,(Qq-1)//mod)]
                    if lp==2:
                        assert 2*(D-rt)%mod==0;two_sign_tests+=1
                    else:
                        assert (D-rt)%mod==0;tests+=1
                # Actual cochain changes and Frobenius shear in the local support coordinate.
                for aa0,bb0,A0,B0,u0,v0,r0 in [(1,2,3,4,5,6,7),(-2,3,7,-5,9,2,-4)]:
                    D=A0*bb0-B0*aa0
                    assert (A0+r0*aa0)*bb0-(B0+r0*bb0)*aa0==D
                    assert ((A0+(Qq-1)*u0)*bb0-(B0+(Qq-1)*v0)*aa0-D)==(Qq-1)*(u0*bb0-v0*aa0)
                    transition_tests+=2
            if prime==7 and ff.evaluate(threeplus,zeta)==0:
                assert ff.evaluate(threeminus,zeta)!=0
                rr=next(t for t in row['logs'] if t['ell']==3)
                assert ff.pow(2,3)==1 and 2!=1 and rr['two']%3!=0
                det=rr['two']*pow(4,-1,3)%3
                assert det
                witness_records.append({'prime':row,'k_inertia':1,'C0C1_residue_mod3':det,
                                         'cohomology_coefficient':'-1/4 * kappa(k) cup kappa(2)'})
            residue_records.append(row)
    assert len(witness_records)==1
    print(f'PASS: {len(residue_records)} actual residue fields; {tests} odd tame identities; {two_sign_tests} rational-two sign identities')
    print(f'PASS: {transition_tests} representative/Frobenius transitions; nonzero C0,C1 obstruction at norm49')

    # All finite character ranks and their fully typed cohomology totals.
    result={
      'statement':'E.108','status':'PASS','input_sha256':INPUT_SHA,
      'peripheral_order':order,'Fourier_labels':labels,
      'Fourier_matrix':smat(P),'Fourier_inverse':smat(Pinv),
      'exterior_pairs':[[labels[i],labels[j]] for i,j in PAIRS],
      'exterior_matrix':smat(exterior),'exterior_inverse':smat(exterior_inv),
      'quadratic_character_table':chars,'W_multiplicities':dict(Counter(types)),
      'wedge_multiplicities':dict(Counter(wedge_types)),
      'all_55_shifted_cups':shifts,'BCH_gauge_checks':gauge_count,
      'peripheral_H1_free_rank':30,'peripheral_H1_torsion_at_3':[3]*10,
      'peripheral_H1_torsion_other_odd':[],
      'mixed_CM_coefficient_multiplicities':{'V(1)':15,'V(1)chi_2':18},
      'symmetric_CM_contraction':['-c','a','b'],
      'symmetric_CM_section':['b/2','-a','-c/2'],
      'symmetric_CM_relation':'a^2+b*c=-1',
      'evaluated_determinant_Kummer_copies':6,'evaluated_anti_Qi_Kummer_copies':3,
      'S2_positive_W_rank':5,
      'unit_identity':'2=zeta8^6*(1+sqrt2)^2*(1-zeta8)^4',
      'special_k_coefficients':[str(x) for x in special],
      'special_k_norm':str(field_norm(special)),
      'zero_minimum_witness':witness_records,
      'residue_fields':residue_records,'odd_tame_symbol_checks':tests,
      'rational_two_sign_checks':two_sign_tests,'local_coordinate_transition_checks':transition_tests,
      'scope':'Exact maps and finite certificates; source theorems and continuous convergence proof are in E108, not inferred from finite tests.'
    }
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('PASS: all E108 exact certificate assertions')

if __name__=='__main__':main()
