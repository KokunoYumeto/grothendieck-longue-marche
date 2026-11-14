#!/usr/bin/env python3
"""Independent E96 algebra/lattice audit, using the literal E95 path columns."""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import sympy as s

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
source=BASE/"research_e95/code/a_cusp_kummer_explore.json"
paths=json.loads(source.read_text())["global_cusp_coefficients"]
layerfile=BASE/"LM7_FERMAT_TOWER/code/e_wild_layers.json"
layer=json.loads(layerfile.read_text())["layers"]["1"]
T=s.Matrix(layer["input_tau"]); C=s.Matrix(layer["input_c"])
labels=["A0","A1","A2","B0","B1","B2","C1","C2"]
coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=s.Matrix([[v,-u] for u,v in coords])
R=s.Matrix([[0,-1],[1,-1]])
j=s.Matrix.vstack(3*s.eye(2),U)
wedges=list(combinations(range(10),2))
def wedge(x,y):
    return s.Matrix([x[i]*y[j]-x[j]*y[i] for i,j in wedges])
def exterior(A):
    return s.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
                      for k,l in wedges] for i,j in wedges])
def iszero(A):
    return all(s.expand(x)==0 for x in A)
def integral3(A):
    return all(s.denom(s.cancel(x))%3 != 0 for x in A)

w=wedge(j[:,0],j[:,1]);pivot=wedges.index((2,4))
assert w[pivot]==1
keep=[i for i in range(45) if i!=pivot]
Q=(s.eye(45)-w*s.eye(45)[pivot,:])[keep,:]
section=s.eye(45)[:,keep]
assert Q*section==s.eye(44) and Q*w==s.zeros(44,1)
assert section*Q==s.eye(45)-w*s.eye(45)[pivot,:]
assert integral3(Q)
# This is the actual quotient, including its nonzero f1^f2 row.
assert Q[0,pivot]==-9

a,b,q=s.symbols("a b q")
AE=a*s.eye(2)+b*R
A=AE.row_join(s.zeros(2,8)).col_join(
    (U*(AE-q*s.eye(2))/3).row_join(q*s.eye(8)))
B=exterior(A)
assert iszero(A*j-j*AE)
assert iszero((B-q*s.eye(45))*w-
              (a*a-a*b+b*b-q)*w)
checks=0
for i in range(10):
    h=s.eye(10)[:,i]
    for d in range(2,10):
        e=s.eye(10)[:,d]
        assert iszero((B-q*s.eye(45))*wedge(h,e)
                      -q*wedge((A-s.eye(10))*h,e))
        checks+=1

hstar=(s.eye(10)+C)*s.eye(10)[:,0]/2-s.Matrix(
    [0,0,0,0,0,0,s.Rational(1,4),-s.Rational(1,4),
     s.Rational(1,4),-s.Rational(1,4)])
c3=s.Matrix([0,0,1,1,1,2,s.Rational(1,2),s.Rational(1,2),
             s.Rational(3,2),s.Rational(3,2)])
cz=s.Matrix([0,0,0,1,-1,0,s.Rational(1,2),-s.Rational(1,2),
             s.Rational(1,2),-s.Rational(1,2)])
assert integral3(hstar) and integral3(c3) and integral3(cz)
assert c3+2*cz+(T-s.eye(10))*hstar==3*s.eye(10)[:,1]
Tp=C*T*C
assert -c3+2*cz+(Tp-s.eye(10))*hstar==3*C*s.eye(10)[:,1]
cols={}
for d in labels:
    bb,rr,ss=[s.Matrix([s.Rational(x) for x in paths[d][key]])
              for key in ["rational_coboundary","Kummer3","Kummer_zeta"]]
    assert integral3(3*bb) and integral3(3*rr) and integral3(3*ss)
    assert rr[:2,:]==ss[:2,:]==s.zeros(2,1)
    cols[d]=(bb,rr,ss)

# Exact coefficient checks of the universal numerator. q-1=3ell is
# substituted only for the integral lattice check, not in the identity.
eps,gamma,ell=s.symbols("eps gamma ell")
beta=s.symbols("beta0:8")
betavec=s.Matrix([0,0,*beta])
k=q-1
coefficient_checks=0
denominator_checks=0
numeric_inverse_checks=0
for index,d in enumerate(labels):
    v=s.eye(10)[:,index+2]
    bb,rr,ss=cols[d]
    h=eps*hstar/3
    u=betavec+eps*(c3*gamma+cz*k/3)/3
    X=wedge(h,v)-wedge(bb,v)+(wedge(u,v)-gamma*wedge(rr,v)
                             -k*wedge(ss,v)/3)/k
    NN=eps*k*wedge(hstar,v)-3*k*wedge(bb,v)+3*wedge(betavec,v)
    NN+=eps*gamma*wedge(c3,v)+eps*k*wedge(cz,v)/3
    NN-=3*gamma*wedge(rr,v)+k*wedge(ss,v)
    assert iszero(3*k*X-NN)
    coeffsymbols=(eps,gamma,*beta,ell)
    for x in Q*NN:
        p=s.Poly(s.expand(x.subs(q,1+3*ell)),*coeffsymbols)
        assert integral3(p.coeffs())
        denominator_checks+=1
    alpha=(A-s.eye(10))*h+u
    kd=(A-s.eye(10))*bb+rr*gamma+ss*k/3
    D=wedge(alpha,v)-wedge(kd,v)
    # Universal equality is justified by the eighty basis identities above.
    direct=(B-q*s.eye(45))*NN-3*k*q*D
    assert iszero(direct)
    coefficient_checks+=1

# Explicit quotient inverse at a genuine Frobenius q=7, psi=1+3zeta:
# it uses M/L as domain and M0 (not M/L) as range.
Av=A.subs({a:1,b:3,q:7})
Bv=exterior(Av)
M0rows=[i for i,p in enumerate(wedges) if p!=(0,1)]
dmat=((Bv/7-s.eye(45))*section)[M0rows,:]
assert dmat.det()!=0
for index,d in enumerate(labels):
    v=s.eye(10)[:,index+2];bb,rr,ss=cols[d]
    h=hstar/3;u=s.zeros(10,1)+(c3+2*cz)/3
    X=wedge(h,v)-wedge(bb,v)+(wedge(u,v)-wedge(rr,v)
                             -2*wedge(ss,v))/6
    alpha=(Av-s.eye(10))*h+u
    kd=(Av-s.eye(10))*bb+rr+2*ss
    D=wedge(alpha,v)-wedge(kd,v)
    assert D[wedges.index((0,1))]==0
    assert dmat*(Q*X)==D[M0rows,:]
    numeric_inverse_checks+=1

out={
    "status":"PASS",
    "universal_mixed_wedge_identities":checks,
    "universal_cusp_numerator_identities":coefficient_checks,
    "integral_quotient_coefficient_checks":denominator_checks,
    "actual_Frobenius_quotient_inverse_checks":numeric_inverse_checks,
    "quotient_pivot":[2,4],
    "primitive_w":[int(x) for x in w],
    "actual_quotient_matrix":[[int(x) for x in row] for row in Q.tolist()],
    "hstar":[str(x) for x in hstar],
    "cT3":[str(x) for x in c3],
    "cTz":[str(x) for x in cz],
    "input_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
    "layer_input_sha256":hashlib.sha256(layerfile.read_bytes()).hexdigest(),
    "denominator":"3(q-1), with q=1 modulo3",
    "criterion":"N is in 3^(v3(q-1)+1) Z3^44; convergence requires the same exponent plus each fixed m outside a finite set",
    "scope":"Algebra and actual integral quotient lattice for the E95 transported marking. No theorem E96 is published by this independent audit."
}
(HERE/"bc_class2_reduction.json").write_text(json.dumps(out,indent=2)+"\n")
print("PASS: eighty universal mixed-wedge identities and all eight exact numerator identities.")
print("PASS: all352 coefficient-lattice checks and all eight actual Frobenius quotient checks.")
print("PASS: the primitive quotient Q includes the -9 pivot correction in its first row.")
print("PASS: denominator 3(q-1), with the stated restricted-convergence exponents.")
