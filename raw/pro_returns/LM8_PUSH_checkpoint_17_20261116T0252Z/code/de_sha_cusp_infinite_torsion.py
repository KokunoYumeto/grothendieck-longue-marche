#!/usr/bin/env python3
"""Exact support for D86. Structural infinite/cohomological proofs remain in TeX."""
from pathlib import Path
import json, math
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

p=5

def add(a,b):
    c=dict(a)
    for m,x in b.items():
        c[m]=(c.get(m,0)+x)%p
        if not c[m]: del c[m]
    return c

def scale(a,s): return {m:x*s%p for m,x in a.items() if x*s%p}
def mul(a,b,N):
    c={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            if i+j+k+l<N:
                m=(i+k,j+l); c[m]=(c.get(m,0)+x*y)%p
    return {m:x for m,x in c.items() if x}
def powp(a,k,N):
    b={(0,0):1}
    while k:
        if k&1:b=mul(b,a,N)
        a=mul(a,a,N); k//=2
    return b
def rank_mod(rows):
    if not rows:return 0
    a=[r[:] for r in rows]; r=0
    for c in range(len(a[0])):
        pivot=next((j for j in range(r,len(a)) if a[j][c]%p),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][c],-1,p); a[r]=[x*inv%p for x in a[r]]
        for j in range(r+1,len(a)):
            z=a[j][c]
            if z:a[j]=[(x-z*y)%p for x,y in zip(a[j],a[r])]
        r+=1
        if r==len(a):break
    return r

operator_checks=[]
for n in range(2,11):
    N=n+1
    basis=[(i,d-i) for d in range(n) for i in range(d+1)]
    target=[(i,d-i) for d in range(N) for i in range(d+1)]
    for chi in (1,6,11,16,21):
        su={(i,0):math.comb(chi,i+1)%p for i in range(min(chi,N)) if math.comb(chi,i+1)%p}
        sv={(0,j):math.comb(chi,j+1)%p for j in range(min(chi,N)) if math.comb(chi,j+1)%p}
        du={(i,0):math.comb(chi,i)%p for i in range(1,min(chi,N-1)+1) if math.comb(chi,i)%p}
        dv={(0,j):math.comb(chi,j)%p for j in range(1,min(chi,N-1)+1) if math.comb(chi,j)%p}
        for h in range(1,5):
            trans={(i,0):math.comb(h,i)%p for i in range(min(h,N-1)+1) if math.comb(h,i)%p}
            for cubic in (0,1,3):
                # Every actual beta has zero linear part. These exact models
                # include cubic and higher coefficients; the proof uses only
                # the universal leading symbol, not a fabricated Galois image.
                beta={(0,0):1}
                beta=add(beta,{(2,1):cubic,(1,2):cubic,(3,1):2,(1,3):4})
                M=mul(mul(mul(trans,su,N),sv,N),beta,N)
                columns=[]
                for i,j in basis:
                    col=add(mul(M,mul(powp(du,i,N),powp(dv,j,N),N),N),{(i,j):-1})
                    d=i+j
                    assert all(sum(k)>=d+1 for k in col)
                    assert {k:x for k,x in col.items() if sum(k)==d+1}=={(i+1,j):h}
                    columns.append([col.get(m,0) for m in target])
                rows=list(map(list,zip(*columns)))
                rank=rank_mod(rows)
                assert rank==len(basis)
                operator_checks.append({'n':n,'chi':chi,'h':h,'cubic':cubic,'rank':rank,'source_dimension':len(basis)})

# Exact finite-shell functions for the chi-weighted permutation action.
shell_checks=[]
for r in range(1,6):
    q=5**r
    def val(x):
        if not x:return r
        j=0
        while x%5==0:x//=5;j+=1
        return j
    fs=[]
    for n in range(r):
        f=[pow((x//5**n)%5,-1,5) if val(x)==n else 0 for x in range(q)]
        assert all(f[(2*x)%q]==3*f[x]%5 for x in range(q))
        fs.append(f)
    # The weighted zero orbit contributes no invariant, each nonzero shell one.
    seen=set(); orbit_lengths=[]
    for x in range(q):
        if x in seen:continue
        orb=[]; y=x
        while y not in seen: seen.add(y);orb.append(y);y=2*y%q
        orbit_lengths.append(len(orb))
    assert len(orbit_lengths)==r+1
    assert sum(pow(2,l,5)==1 for l in orbit_lengths)==r
    # On first-u coefficient modules, multiply by v: the functional on v^j
    # is the finite difference of the shell function of order j+1.
    if r<=3:
        N=q-1
        psis=[]
        for f in fs:
            psi=[sum((-1)**(j+1-k)*math.comb(j+1,k)*f[k] for k in range(j+2))%5 for j in range(N)]
            for j in range(N):
                # chi*S_chi(v)*v'^j at chi=2: (4+2v)(2v+v²)^j.
                ans=0
                for k in range(j+1):
                    coef=math.comb(j,k)*pow(2,j-k,5)
                    d=j+k
                    if d<N:ans+=4*coef*psi[d]
                    if d+1<N:ans+=2*coef*psi[d+1]
                assert ans%5==psi[j]
            psis.append(psi)
        assert rank_mod(psis)==r
    shell_checks.append({'level':r,'group_order':q,'weighted_invariant_dimension':r,'orbit_lengths':sorted(orbit_lengths)})

# Integral finite-boundary equivariance, including the diagonal half gauge.
t=sp.symbols('t')
Phi=sum(t**i for i in range(5))
def arem(f):return sp.Poly(sp.expand(f),t,domain=ZZ).rem(sp.Poly(Phi,t,domain=ZZ)).as_expr()
def rvec(f):
    pol=sp.Poly(sp.expand(f),t,domain=ZZ); out=[0]*5
    for (i,),a in pol.terms():out[i%5]+=int(a)
    return sp.Matrix(out)
def avec(f):
    pp=sp.Poly(arem(f),t);return sp.Matrix([int(pp.nth(i)) for i in range(4)])
basisA=[t**j for j in range(4)]
emb=sp.Matrix.hstack(*[rvec((t-1)**2*f) for f in basisA])
embdiag=sp.Matrix.hstack(*[rvec(t**2*(t-1)**2*f) for f in basisA])
assert emb.rank()==embdiag.rank()==4
boundary=[]
for chi in (2,3,4,6,7,11,16):
    S=sum(t**j for j in range(chi))
    M=sp.Matrix.hstack(*[avec(S*S*f.subs(t,t**chi)) for f in basisA])
    e=((1-chi)*3)%5
    Md=sp.Matrix.hstack(*[avec(S*S*t**e*f.subs(t,t**chi)) for f in basisA])
    perm=sp.zeros(5)
    for j in range(5):perm[(chi*j)%5,j]=1
    assert emb*M==perm*emb
    assert embdiag*Md==perm*embdiag
    if chi%5==1:assert M==sp.eye(4) and Md==sp.eye(4)
    boundary.append({'chi':chi,'axis_equivariance':True,'diagonal_half_gauge_equivariance':True})
M2=sp.Matrix.hstack(*[avec((1+t)**2*f.subs(t,t**2)) for f in basisA])
snf=smith_normal_form(M2-sp.eye(4),domain=ZZ)
diag=[abs(int(snf[i,i])) for i in range(4)]
assert sum(x==0 for x in diag)==1 and all(x==0 or x%5 for x in diag)

S=5+10*sp.Symbol('u')+10*sp.Symbol('u')**2+5*sp.Symbol('u')**3+sp.Symbol('u')**4
assert 26**4-1==456975
v5=0;tmp=26**4-1
while tmp%5==0:tmp//=5;v5+=1
assert v5==2
result={'status':'PASS','candidate':'D.86, unregistered',
 'bounded_primitive_operator_checks':operator_checks,
 'operator_check_count':len(operator_checks),
 'weighted_shell_checks':shell_checks,
 'first_u_functional_equivariance_levels':[1,2,3],
 'integral_boundary_checks':boundary,
 'boundary_coinvariant_Smith_diagonal':diag,
 'Eisenstein_polynomial_coefficients':[5,10,10,5,1],
 'cusp_example':{'parameter':26,'factorization':{'2':1,'13':1},'v5_26fourth_minus1':v5,'local_logarithm_depth':1},
 'scope':'Finite exact support for the actual formulas and uniform leading-symbol proof. No finite model is asserted to realize arbitrary Ihara coefficients, and no infinite Sha conclusion follows from the sample alone.'}
if __name__=='__main__':
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
