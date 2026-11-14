#!/usr/bin/env python3
"""E96: exact closed obstruction coordinates on the b=0 global cubic slice.

This program verifies rational identities, their integral quotient map,
all finite mod-three inertia solutions, and actual marked norm-seven cases.
Formal matrix inputs are explicitly distinguished from actual Frobenius data.
"""
from pathlib import Path
from itertools import combinations, product
import hashlib
import json
import random
import sympy as s

HERE = Path(__file__).resolve().parent
INPUTS = HERE.parent / 'inputs'
LABELS = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'C1', 'C2']
COORDS = [(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
PAIRS = list(combinations(range(10), 2))

def read(name):
    candidates = [INPUTS/name, HERE/name]
    p = next(p for p in candidates if p.exists())
    return json.loads(p.read_text()), hashlib.sha256(p.read_bytes()).hexdigest()

paths, path_hash = read('a_cusp_kummer_explore.json')
old, old_hash = read('e_intrinsic_class2.json')
wild, wild_hash = read('e_wild_layers.json')
col = lambda x: s.Matrix([s.Rational(a) for a in x])
E = s.eye(10)
T = s.Matrix(wild['layers']['1']['input_tau'])
J = s.Matrix(wild['layers']['1']['input_c'])
R = s.Matrix([[0,-1],[1,-1]])
U = s.Matrix([[v,-u] for u,v in COORDS])
j = s.Matrix.vstack(3*s.eye(2),U)
W = E[:,2:]

def wedge(a,b):
    return s.Matrix([a[i]*b[k]-a[k]*b[i] for i,k in PAIRS])

def ext(A):
    return s.Matrix([[A[i,k]*A[jj,l]-A[i,l]*A[jj,k]
                      for k,l in PAIRS] for i,jj in PAIRS])

def val3(x):
    x=s.Rational(x)
    if not x: return 10**9
    a,b=abs(int(x.p)),int(x.q); v=0
    while a%3==0: a//=3; v+=1
    while b%3==0: b//=3; v-=1
    return v

def integral3(A): return all(val3(x)>=0 for x in A)
def dump(A): return [[str(x) for x in row] for row in A.tolist()]

w = wedge(j[:,0],j[:,1])
pivot=PAIRS.index((2,4))
assert list(w)==old['primitive_Tate_line'] and w[pivot]==1
assert PAIRS==[tuple(x) for x in old['wedge_basis']]
keep=[i for i in range(45) if i!=pivot]
Q=s.Matrix([[int(i==k)-w[i]*int(k==pivot) for k in range(45)] for i in keep])
section=s.eye(45)[:,keep]
assert Q*section==s.eye(44) and Q*w==s.zeros(44,1)
assert section*Q==s.eye(45)-w*s.eye(45)[pivot,:]
M0rows=[i for i in range(45) if PAIRS[i]!=(0,1)]

bd={d:col(paths['global_cusp_coefficients'][d]['rational_coboundary']) for d in LABELS}
rd={d:col(paths['global_cusp_coefficients'][d]['Kummer3']) for d in LABELS}
sd={d:col(paths['global_cusp_coefficients'][d]['Kummer_zeta']) for d in LABELS}
qcarry=col([0,0,0,0,0,0,'1/4','-1/4','1/4','-1/4'])
hstar=(s.eye(10)+J)*E[:,0]/2-qcarry
c3=col([0,0,1,1,1,2,'1/2','1/2','3/2','3/2'])
cz=col([0,0,0,1,-1,0,'1/2','-1/2','1/2','-1/2'])
assert integral3(hstar) and integral3(c3) and integral3(cz)
assert (T-s.eye(10))*hstar+c3+2*cz==3*E[:,1]
assert (J*T*J-s.eye(10))*hstar-c3+2*cz==3*J*E[:,1]
for d,(u,vv) in zip(LABELS,COORDS):
    assert all(integral3(3*x) for x in (bd[d],rd[d],sd[d]))
    assert rd[d][:2,:]==sd[d][:2,:]==s.zeros(2,1)
    assert integral3(3*bd[d][:2,:]-s.Matrix([u,vv]))
    assert all(val3(x)>=1 for x in 3*bd[d][:2,:]-s.Matrix([u,vv]))
    assert (T-s.eye(10))*bd[d]+rd[d]+2*sd[d]==col(paths['c_equivariant_cusp_tau_Kummer'][d])

Lb=s.Matrix.hstack(*(wedge(bd[d],E[:,i+2]) for i,d in enumerate(LABELS)))
Lr=s.Matrix.hstack(*(wedge(rd[d],E[:,i+2]) for i,d in enumerate(LABELS)))
Ls=s.Matrix.hstack(*(wedge(sd[d],E[:,i+2]) for i,d in enumerate(LABELS)))

def numerator(eps,n,t,y,v):
    """Exactly Q times 3(q-1)X, where q-1=3n."""
    vv=W*v; yy=W*y
    return Q*(3*eps*n*wedge(hstar,vv)-9*n*Lb*v+3*wedge(yy,vv)
              +eps*t*wedge(c3,vv)+eps*n*wedge(cz,vv)-3*t*Lr*v-3*n*Ls*v)

eps,n,t=s.symbols('epsilon n kappa3')
y=s.symbols('y_A0 y_A1 y_A2 y_B0 y_B1 y_B2 y_C1 y_C2')
v=s.symbols('v_A0 v_A1 v_A2 v_B0 v_B1 v_B2 v_C1 v_C2')
variables=(eps,n,t)+y+v
Npoly=numerator(eps,n,t,s.Matrix(y),s.Matrix(v))
polynomial_rows=[]
term_count=0
for i,x in enumerate(Npoly):
    poly=s.Poly(s.expand(x),*variables)
    terms=[]
    for powers,coefficient in poly.terms():
        assert val3(coefficient)>=0
        assert sum(powers[k] for k in (0,)+tuple(range(3,19)))<=2
        terms.append({'powers':list(powers),'coefficient':str(coefficient)})
    term_count+=len(terms)
    polynomial_rows.append({'quotient_wedge':list(PAIRS[keep[i]]),'terms':terms})
print('PASS exact primitive quotient Q and integral section; no deletion-only quotient.',flush=True)
print('PASS all44 polynomial rows integral over Z_(3); total terms',term_count,flush=True)

# Exact finite matrix comparison. The extra values of t,y,v below are formal
# algebraic test inputs, not assigned values of new arithmetic Frobenii.
rng=random.Random(20261113)
matrix_records=[]; comparison_count=0
for a,b in [(-2,0),(1,3),(-2,-3),(4,3),(1,-3),(-2,3)]:
    q=a*a-a*b+b*b; k=q-1; nn=s.Rational(k,3)
    AE=a*s.eye(2)+b*R
    A=AE.row_join(s.zeros(2,8)).col_join(((U*(AE-q*s.eye(2)))/3).row_join(q*s.eye(8)))
    B=ext(A); delta=B/q-s.eye(45)
    assert B*w==q*w and integral3(A)
    Dmatrix=delta.extract(M0rows,keep)
    Dinv=Dmatrix.inv()
    for z in range(12):
        ee=z%3; tt=rng.randrange(-20,21)
        yy=s.Matrix([rng.randrange(-20,21) for _ in range(8)])
        vv=s.Matrix([rng.randrange(-5,6) for _ in range(8)])
        vf=W*vv
        u=W*yy+ee*(c3*tt+cz*k/3)/3
        af=(A-s.eye(10))*(ee*hstar/3)+u
        kd={d:(A-s.eye(10))*bd[d]+tt*rd[d]+s.Rational(k,3)*sd[d] for d in LABELS}
        rhs=wedge(af,vf)-sum((vv[i]*wedge(kd[d],E[:,i+2]) for i,d in enumerate(LABELS)),s.zeros(45,1))
        X=ee*wedge(hstar,vf)/3-Lb*vv+(wedge(u,vf)-tt*Lr*vv-s.Rational(k,3)*Ls*vv)/k
        assert delta*X==rhs and rhs[PAIRS.index((0,1))]==0
        N=numerator(ee,nn,tt,yy,vv)
        assert integral3(N) and N==3*k*Q*X
        original=-Dinv*rhs.extract(M0rows,[0])
        closed=-N/(3*k)
        assert original==closed
        assert integral3(original)==all(val3(x)>=val3(3*k) for x in N)
        comparison_count+=1
    matrix_records.append({'primary':[a,b],'norm':q,'formal_inputs':12,'denominator_3_valuation':val3(3*k)})
print('PASS',comparison_count,'complete44-coordinate comparisons with original exact inverse.',flush=True)

# Every mod-three solution of the two mixed rows at each cusp. theta is
# the reduction of9 times the discarded pivot coefficient of X.
solutions={}; enumerated=0
for ee in range(3):
    sol=[]
    for vv in product(range(3),repeat=8):
        for theta in range(3):
            enumerated+=1
            if all(((ee-u)*vv[i]+theta*u)%3==0 and
                   (qv*(vv[i]-theta))%3==0 for i,(u,qv) in enumerate(COORDS)):
                sol.append({'v':list(vv),'theta':theta})
    expected=[{'v':[r]*8,'theta':r} for r in range(3)] if ee==0 else [
        {'v':[r if i==(0 if ee==1 else 3) else 0 for i in range(8)],'theta':0}
        for r in range(3)]
    assert sorted(sol,key=lambda x:x['v'])==sorted(expected,key=lambda x:x['v'])
    solutions[str(ee)]=sol
print('PASS all',enumerated,'finite inertia inputs; exactly three solutions per elliptic residue.',flush=True)

# Actual marked prime of norm7: kappa3(tau)=1, A=T, q=7.
# Pure toric kappa(7)e_A0 has alpha(F) proportional to e_A0, so its
# coefficient along that line can be set to zero in the wedge equation.
vv=s.Matrix([1,0,0,0,0,0,0,0])
obstructed=-numerator(0,2,1,s.zeros(8,1),vv)/18
assert not integral3(obstructed)
badrows=[{'quotient_wedge':list(PAIRS[keep[i]]),'coefficient':str(x),'valuation':val3(x)}
         for i,x in enumerate(obstructed) if val3(x)<0]
print('PASS actual pure-toric kappa(7)e_A0 is obstructed; nonintegral coordinates',len(badrows),flush=True)

# Actual rational tangential sections at A0 and B0, twisted by kappa(7).
positive=[]
for d,ee in [('A0',1),('B0',2)]:
    i=LABELS.index(d); vv=s.eye(8)[:,i]
    kd=col(paths['c_equivariant_cusp_tau_Kummer'][d])
    betaF=kd-ee*E[:,1]
    assert betaF[:2,:]==s.zeros(2,1)
    value=-numerator(ee,2,1,betaF[2:,:],vv)/18
    assert value==s.zeros(44,1)
    positive.append({'cusp':d,'elliptic_residue':ee,'all44_correction_coordinates_zero':True})
print('PASS actual A0 and B0 tangential norm-seven twists have zero correction.',flush=True)

out={'status':'PASS','statement':'E.96','basis':'ascending exterior pairs of (f1,f2,A0,A1,A2,B0,B1,B2,C1,C2)',
     'input_sha256':{'a_cusp_kummer_explore.json':path_hash,'e_intrinsic_class2.json':old_hash,'e_wild_layers.json':wild_hash},
     'pivot':{'index':pivot,'pair':list(PAIRS[pivot]),'coefficient_in_w':1},
     'primitive_w':[str(x) for x in w],'quotient_map':dump(Q),'quotient_section':dump(section),
     'hstar':[str(x) for x in hstar],'cT3':[str(x) for x in c3],'cTz':[str(x) for x in cz],
     'path_matrices':{'Lb':dump(Lb),'Lr':dump(Lr),'Ls':dump(Ls)},
     'polynomial_variables':[str(x) for x in variables],'polynomial_numerator_rows':polynomial_rows,
     'correction_formula':'-N/(3(q-1)); n=(q-1)/3',
     'integrality_exponent':'v3(q-1)+1','restricted_convergence_exponent':'v3(q-1)+1+m',
     'exact_matrix_comparisons':comparison_count,'matrix_records':matrix_records,
     'finite_inertia_cases':enumerated,'finite_inertia_solutions':solutions,
     'actual_norm7_pure_toric_counterexample':{'abelian_class':'kappa(7)e_A0','nonintegral_rows':badrows},
     'actual_norm7_cusp_twists':positive,
     'scope':'The rational identities and finite calculations are exact. Arithmetic path formulas are those of E95; global completeness and restricted support transfer are proved using E37 in the accompanying E96 proof. Formal matrix samples are not labelled arithmetic Frobenius evaluations.'}
HERE.joinpath('e_global_zero_free_elliptic.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS complete E96 exact certificate.',flush=True)
