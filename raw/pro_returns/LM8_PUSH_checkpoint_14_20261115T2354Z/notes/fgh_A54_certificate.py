#!/usr/bin/env python3
"""Exact certificate for the A.54 Heisenberg-five candidate.

The proof is in fgh_A54_draft.tex.  Finite calculations here check its
actual quotient, Fourier identities, signatures, character sums, and
global quadratic-field witnesses.  They do not assert a Galois image
from an ambient representation.
"""
from pathlib import Path
import json
import sympy as s

x, z, t = s.symbols('x z t')
I = s.I
Phi = s.cyclotomic_poly(20, z)
Phi5 = s.cyclotomic_poly(5, z)
def red(a, phi=Phi):
    return s.Poly(s.rem(s.expand(a), phi, z), z, domain=s.QQ).as_expr()
def matred(A):
    return A.applyfunc(lambda a: red(a, Phi5))
def evaluate(a, r, root):
    p = s.Poly(a, z, domain=s.QQ)
    return sum(int(c.p)*pow(int(c.q), -1, r)*pow(root, int(e[0]), r)
               for e, c in p.terms()) % r

psi = 5*x**12-62*x**10-105*x**8+300*x**6-125*x**4+50*x**2+1
lambda_H = (1-2*I)/5
lam = (1+2*I)/5
alpha = 2-I
Xalpha = x*(3+4*I)*(x**2-1-2*I)**2/(25*(x**2-lambda_H)**2)
h = x**2-lambda_H
constant = -35-120*I
assert s.cancel(psi-constant*(Xalpha**2-lam)*h**5, extension=I) == 0
assert s.expand(5*alpha**4-constant) == 0
quotient = dict(alpha=str(alpha), lambda_H=str(lambda_H),
                lambda_target=str(lam), x_alpha=str(Xalpha),
                constant=str(constant), exact_identity=True)
print('PASS actual degree-five quotient identity', flush=True)

# Positive Fourier convention: U e_j=e_(j+1), V e_j=z^j e_j.
sqrt5 = 1+2*z+2*z**4
assert red(sqrt5**2-5, Phi5) == 0
U = s.zeros(5)
for j in range(5): U[(j+1)%5, j] = 1
V = s.diag(*[z**j for j in range(5)])
A = s.Matrix(5, 5, lambda j,k: red(z**(j*k)*sqrt5/5, Phi5))
A2 = matred(A*A)
A4 = matred(A2*A2)
assert A4 == s.eye(5)
assert matred(A*U-V*A) == s.zeros(5)
assert matred(A*V-U.T*A) == s.zeros(5)
assert A2 == s.Matrix(5,5,lambda j,k:int(j == (-k)%5))
trA, trA2 = red(s.trace(A),Phi5), s.trace(A2)
assert trA == 1 and trA2 == 1
# Together with A^4=1 these traces and dimension5 give (2,1,1,1).
fourier_multiplicities = [2,1,1,1]
solutions=[]
for a in range(6):
 for b in range(6):
  for c in range(3):
   if (a+b+2*c == 5 and 2*a+b+2*c == 5
       and 3*(a+b)+4*c == 11): solutions.append([a,b,c,c])
assert solutions == [[0,1,2,2]]
print('PASS Fourier and actual quotient-genus multiplicity equations', flush=True)

primitive = [k for k in range(1,20) if s.gcd(k,20)==1]
hodge = {k:-1+sum((k*m)%20 for m in (5,10,4,1))//20 for k in primitive}
assert [hodge[k] for k in primitive] == [0,1,1,1,1,1,1,2]
cmtype={1,2}
stabilizer=[a for a in (1,2,3,4) if {(a*b)%5 for b in cmtype}==cmtype]
assert stabilizer == [1]
print('PASS primitive20 signature and primitive quartic CM type', flush=True)

def trace_character(q, degree):
    g=int(s.primitive_root(q)); ir=pow(g,(q-1)//4,q)
    lr=(1+2*ir)*pow(5,-1,q)%q
    logs={pow(g,j,q):j%20 for j in range(q-1)}
    ns=next(a for a in range(2,q) if pow(a,(q-1)//2,q)==q-1)
    counts=[0]*20
    if degree==1:
        for a in range(q):
            ff=pow(a,5,q)*pow(a-1,10,q)*pow(a-lr,4,q)%q
            if ff: counts[logs[ff]]+=1
    else:
        for a in range(q):
            for b in range(q):
                b2=ns*b*b%q
                n0=(a*a-b2)%q
                n1=((a-1)**2-b2)%q
                nl=((a-lr)**2-b2)%q
                ff=pow(n0,5,q)*pow(n1,10,q)*pow(nl,4,q)%q
                if ff: counts[logs[ff]]+=1
    aq=red(-sum(n*z**j for j,n in enumerate(counts)))
    return aq, dict(q=q,degree=degree,primitive_root=g,i=ir,
        lambda_residue=lr,quadratic_nonsquare=ns,character_counts=counts)

rows=[]
polynomials={}
for q in (41,61):
    aq,m1=trace_character(q,1)
    a2,m2=trace_character(q,2)
    dq=red((aq*aq-a2)/2)
    disc=red(aq*aq-4*dq)
    assert all(c.q==1 for c in s.Poly(dq,z).all_coeffs())
    polynomials[q]=(aq,dq,disc)
    root=pow(m1['primitive_root'],(q-1)//20,q)
    other_root=pow(root,3,q)
    ar=evaluate(aq,q,other_root)
    dr=evaluate(dq,q,other_root)
    assert ar != 0 and dr == 0 and dq != 0
    row=dict(q=q,trace=str(aq),trace_square_Frob=str(a2),
        determinant=str(dq),discriminant=str(disc),count_data=[m1,m2],
        persistence=dict(residue_characteristic=q,zeta20_residue=other_root,
                         trace_residue=ar,determinant_residue=dr))
    rows.append(row)
    print(json.dumps({k:v for k,v in row.items() if k!='count_data'},sort_keys=True),flush=True)

disc41,disc61 = polynomials[41][2],polynomials[61][2]
witnesses=[]
for label,poly,r,root,want in [
    ('Delta41 nonsquare',disc41,61,33,-1),
    ('Delta61 nonsquare',disc61,41,39,-1),
    ('Delta41 at comparison prime',disc41,41,39,1),
    ('Delta41 Delta61 nonsquare',red(disc41*disc61),41,39,-1),
]:
    assert evaluate(Phi,r,root)==0
    value=evaluate(poly,r,root)
    assert value != 0
    symbol=int(s.legendre_symbol(value,r))
    assert symbol==want
    witnesses.append(dict(label=label,r=r,zeta20_residue=root,
                          residue=value,legendre_symbol=symbol))
    print('PASS',label,witnesses[-1],flush=True)

data=dict(scope='A.54 exact finite certificate; see full proof for geometry and endomorphism argument',
    heisenberg=dict(order=125,proper_genus=51,cusps=25),quotient=quotient,
    fourier=dict(multiplicities=fourier_multiplicities,
                 residual_T_multiplicities=solutions[0]),
    primitive20_hodge_dimensions=hodge,quartic_CM_type=[1,2],
    quartic_CM_type_stabilizer=stabilizer,cyclotomic_polynomial=str(Phi),
    frobenius=rows,squareclass_witnesses=witnesses)
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS A.54 exact quotient, signatures, character sums, and persistent-field witnesses.',flush=True)
