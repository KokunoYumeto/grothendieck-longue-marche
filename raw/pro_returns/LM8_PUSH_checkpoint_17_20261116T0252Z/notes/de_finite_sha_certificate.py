#!/usr/bin/env python3
"""Exact finite action checks supporting the unregistered D.78 draft.

This verifies coefficient identities, not the arithmetic coinduction or
Poitou--Tate arguments.  All reductions use the actual Fox multiplier
S_chi(t1) S_chi(t2) beta and semilinear substitutions through degree three.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp

P = 5
MON = [(i, d-i) for d in range(4) for i in range(d+1)]
IX = {ij: n for n, ij in enumerate(MON)}
DIM = len(MON)

def choose(a, j):
    x = F(1)
    for k in range(j):
        x *= F(a-k, k+1)
    return x

def red(a):
    a = F(a)
    assert a.denominator % P
    return a.numerator * pow(a.denominator, -1, P) % P

def add(*polys):
    out = {}
    for poly in polys:
        for ij, a in poly.items():
            out[ij] = out.get(ij, F(0)) + a
    return {ij: a for ij, a in out.items() if a}

def mul(f, g):
    out = {}
    for (i,j), a in f.items():
        for (k,l), b in g.items():
            if i+j+k+l <= 3:
                ij = (i+k,j+l)
                out[ij] = out.get(ij, F(0)) + a*b
    return {ij: a for ij, a in out.items() if a}

def power(f, n):
    out = {(0,0): F(1)}
    for _ in range(n):
        out = mul(out, f)
    return out

def tx(a, axis):
    return {((j,0) if axis == 0 else (0,j)): choose(a,j)
            for j in range(4) if choose(a,j)}

def s_chi(q, axis):
    return {((j,0) if axis == 0 else (0,j)): choose(q,j+1)
            for j in range(4) if choose(q,j+1)}

def beta(q, c):
    # log(beta) = r X Y + h X Y(X+Y) + O(4), h=c/48.
    # X=log(1+u), Y=log(1+v); no quadratic exponential term below 4.
    r, h = F(q*q-1,24), F(c,48)
    return {(0,0): F(1), (1,1): r,
            (2,1): h-r/2, (1,2): h-r/2}

def action(q, a, b, c):
    multiplier = mul(mul(tx(a,0),tx(b,1)),
                     mul(mul(s_chi(q,0),s_chi(q,1)), beta(q,c)))
    pu = add(tx(q,0), {(0,0): F(-1)})
    pv = add(tx(q,1), {(0,0): F(-1)})
    cols = []
    for i,j in MON:
        f = mul(multiplier, mul(power(pu,i), power(pv,j)))
        cols.append([red(f.get(ij,0)) for ij in MON])
    return [[cols[j][i] for j in range(DIM)] for i in range(DIM)]

def rt_times(R, x):
    return [sum(R[j][i]*x[j] for j in range(len(x))) % P
            for i in range(len(x))]

def eps(i,j,a=1):
    v = [0]*DIM
    v[IX[i,j]] = a % P
    return v

cases = []
for q in range(1,5):
    for a in range(5):
        for b in range(5):
            for c in range(5):
                R = action(q,a,b,c)
                if q != 1:
                    m = eps(0,0,c*pow((pow(q,-1,5)-1)%5,-1,5))
                    kind = "constant"
                elif a:
                    m = eps(1,0,-c*pow(a,-1,5))
                    kind = "first_linear"
                elif b:
                    m = eps(0,1,-c*pow(b,-1,5))
                    kind = "second_linear"
                else:
                    m = eps(2,1,-48)
                    kind = "fixed_cubic"
                z = eps(0,0,c)
                # Cartier action is q R^{-T}; avoid an unnecessary inversion.
                lhs = [(q*x)%5 for x in m]
                rhs = rt_times(R, [(m[i]+z[i])%5 for i in range(DIM)])
                assert lhs == rhs, (q,a,b,c,kind,lhs,rhs)
                cases.append(kind)

def umul(f,g):
    out = [F(0)]*4
    for i,a in enumerate(f):
        for j,b in enumerate(g):
            if i+j < 4:
                out[i+j] += a*b
    return out

def upower(f,n):
    out = [F(1),F(0),F(0),F(0)]
    for _ in range(n):
        out = umul(out,f)
    return out

alpha, bet = 2, 4
u = [choose(bet,j) for j in range(4)]
v = [choose(-alpha,j) for j in range(4)]
u[0] = v[0] = F(0)

def restrict(poly):
    out = [F(0)]*4
    for (i,j), a in poly.items():
        f = umul(upower(u,i),upower(v,j))
        out = [out[k]+a*f[k] for k in range(4)]
    return out

def line_action(q,c):
    multiplier = restrict(mul(mul(s_chi(q,0),s_chi(q,1)),beta(q,c)))
    pz = [choose(q,j) if j else F(0) for j in range(4)]
    cols = [umul(multiplier,upower(pz,j)) for j in range(4)]
    return sp.Matrix(4,4,lambda i,j: sp.Rational(cols[j][i]))

Rk = line_action(2,0)
Rdelta = line_action(1,1)
Kdual = 2*Rk.inv().T
Ddual = Rdelta.inv().T
K5 = [[red(Kdual[i,j]) for j in range(4)] for i in range(4)]
D5 = [[red(Ddual[i,j]) for j in range(4)] for i in range(4)]

def matvec(A,x):
    return [sum(a*b for a,b in zip(row,x))%5 for row in A]

def defect(A,x):
    return [(a-b)%5 for a,b in zip(matvec(A,x),x)]

vectors4 = [[a,b,c,d] for a in range(5) for b in range(5)
            for c in range(5) for d in range(5)]
joint_fixed = [x for x in vectors4 if defect(K5,x)==[0]*4
               and defect(D5,x)==[0]*4]
assert joint_fixed == [[0]*4]
quotient_fixed = [x for x in vectors4 if x[0]==0
                  and defect(K5,x)[1:]==[0]*3
                  and defect(D5,x)[1:]==[0]*3]
assert len(quotient_fixed)==5
primitive = [x for x in vectors4 if defect(K5,x)==[0]*4
             and defect(D5,x)==[1,0,0,0]]
assert len(primitive)==1

Rz = Rk[1:4,1:4]
Qdual = 2*Rz.inv().T
det = sp.factor((Qdual-sp.eye(3)).det())

def val5(x):
    x = F(x)
    n,d = abs(x.numerator),x.denominator
    assert n
    e = 0
    while n%5==0:
        n//=5; e+=1
    while d%5==0:
        d//=5; e-=1
    return e

assert val5(det)==1
diag = [Qdual[i,i] for i in range(3)]
assert diag==[sp.Rational(1,4),sp.Rational(1,8),sp.Rational(1,16)]
assert all(val5(diag[i]-diag[j])==0 for i in range(3) for j in range(i))

# Pull back the four local line functionals to the actual ten-dimensional M.
restr_cols = [restrict({ij:F(1)}) for ij in MON]
local_pullback = [sum(red(restr_cols[j][i])*primitive[0][i]
                      for i in range(4))%5 for j in range(DIM)]
Rdelta2 = action(1,0,0,1)
assert rt_times(Rdelta2, [(local_pullback[i]+eps(0,0)[i])%5
                        for i in range(DIM)]) == local_pullback

counts = {k:cases.count(k) for k in sorted(set(cases))}
assert counts=={"constant":375,"first_linear":100,
                "second_linear":20,"fixed_cubic":5}

result = {
    "status":"PASS",
    "scope":"Exact coefficient identities; arithmetic hypotheses are proved in D.78, not inferred from this finite test.",
    "monomial_order":MON,
    "finite_cartier_module_dimension":DIM,
    "universal_primitive_cases":len(cases),
    "primitive_case_counts":counts,
    "cartier_action_convention":"chi times inverse transpose of actual Fox-semilinear action",
    "local_logarithm_residues":{"alpha":2,"beta":4,"alpha_minus_beta":3},
    "local_cubic_numerator_mod5":bet*(-alpha)*(bet-alpha)%5,
    "local_cubic_coefficient_mod5":red(F(bet*(-alpha)*(bet-alpha),48)),
    "local_multiplier_two_matrix":[[str(Rk[i,j]) for j in range(4)] for i in range(4)],
    "local_delta_matrix":[[str(Rdelta[i,j]) for j in range(4)] for i in range(4)],
    "local_joint_fixed_vectors_mod5":len(joint_fixed),
    "quotient_fixed_vectors_mod5":len(quotient_fixed),
    "local_normalized_primitive_mod5":primitive[0],
    "local_primitive_pullback_to_actual_M":local_pullback,
    "quotient_cartier_eigenvalues":[str(x) for x in diag],
    "quotient_cartier_minus_one_determinant":str(det),
    "determinant_five_valuation":val5(det),
    "all_pairwise_eigenvalue_differences_units":True,
    "no_arbitrary_local_denominator_used":True,
}

if __name__ == "__main__":
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
