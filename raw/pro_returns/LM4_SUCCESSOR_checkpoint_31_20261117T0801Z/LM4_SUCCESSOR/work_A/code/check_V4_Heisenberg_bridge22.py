"""Exact rational P4 cup-lift / universal relative-class-two pentagon test.

This is a bounded representation calculation, not a finite-group census.
The P4 action presentation is the already audited Cohen/Artin convention
used in work_CE/code/check_heisenberg_parity.py. All arithmetic is exact.
No full GT or full-generation claim is made by this producer.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import gcd, lcm
from functools import reduce
from pathlib import Path
import json
import sympy as S

OUT = Path(__file__).resolve().parents[1] / "V4_Heisenberg_bridge22.json"
KEYS = [(1,2),(1,3),(2,3),(1,4),(2,4),(3,4)]

def sign(bit): return 1 if bit == 0 else -1

def one(n): return ((Q(0),)*n, (Q(0),)*(n*(n-1)//2), 0)

def make_ops(weights):
    n=len(weights); pairs=list(combinations(range(n),2))
    def act(v,h,central=False):
        ww=[weights[i]^weights[j] for i,j in pairs] if central else weights
        return tuple(sign((w&h).bit_count()%2)*a for w,a in zip(ww,v))
    def mul(g,h):
        a,c,e=g; b,d,f=h
        b=act(b,e); d=act(d,e,True)
        return (tuple(x+y for x,y in zip(a,b)),
                tuple(x+y+(a[i]*b[j]-a[j]*b[i])/2
                      for x,y,(i,j) in zip(c,d,pairs)), e^f)
    def inv(g):
        a,c,e=g
        return tuple(-v for v in act(a,e)),tuple(-v for v in act(c,e,True)),e
    def conj(g,h): return mul(mul(g,h),inv(g))
    def comm(g,h): return mul(conj(g,h),inv(h))
    def word(w,gens):
        z=one(n)
        for j in w:z=mul(z,gens[j-1] if j>0 else inv(gens[-j-1]))
        return z
    return mul,inv,conj,comm,word

mul,inv,conj,comm,word=make_ops([1,2])

def defects(q):
    out=[]
    for j in (3,4):
        for r in range(1,j):
            for s in range(r+1,j):
                g=q[r,s]
                for i in range(1,j):
                    v=q[i,j]
                    if i<r or s<i: rhs=v
                    elif s==i: rhs=conj(q[r,j],v)
                    elif r==i: rhs=conj(mul(q[r,j],q[s,j]),v)
                    else: rhs=conj(comm(q[r,j],q[s,j]),v)
                    lhs=conj(inv(g),v)
                    assert lhs[2]==rhs[2]
                    out.append(tuple(x-y for x,y in zip(lhs[0]+lhs[1],rhs[0]+rhs[1])))
    return out

def character_matrix(eps):
    cols=[]
    for j in range(6):
        q={k:((Q(int(i==j)),Q(0)),(Q(0),),eps[i]) for i,k in enumerate(KEYS)}
        cols.append([d[0] for d in defects(q)])
    return S.Matrix.hstack(*map(S.Matrix,cols))

def primitive(v):
    den=reduce(lcm,[int(x.q) for x in v],1)
    vv=[int(x*den) for x in v]
    dd=reduce(gcd,[abs(x) for x in vv],0)
    vv=[x//dd for x in vv]
    if next(x for x in vv if x)<0:vv=[-x for x in vv]
    return vv

chars=[]; matrices={}
for eps in product(range(2),repeat=6):
    M=character_matrix(eps); matrices[eps]=M
    ns=M.nullspace()
    if any(eps) and len(ns)==2:
        cob=S.Matrix([1-sign(x) for x in eps])
        v=next(v for v in ns if S.Matrix.hstack(cob,v).rank()==2)
        chars.append((eps,primitive(v)))
assert len(chars)==15
print("Nontrivial rank-one-character H1 lines:",len(chars),flush=True)

# Universal relative class-two quotient of free F(x,y) above C2^2.
# H1 of its index-four free kernel has 2 trivial and 3 sign characters.
WEIGHTS=[0,0,1,2,3]
UM,UI,UC,UCOM,UWORD=make_ops(WEIGHTS)
ux=((Q(1),Q(0),Q(0),Q(1),Q(0)),(Q(0),)*10,1)
uy=((Q(0),Q(1),Q(1),Q(0),Q(1)),(Q(0),)*10,2)
SCHREIER=[[1,1],[2,1,-2,-1],[2,2],[1,2,1,-2],[1,2,2,-1]]
UB=[UWORD(w,[ux,uy]) for w in SCHREIER]
assert all(g[2]==0 for g in UB)
P=S.Matrix.hstack(*[S.Matrix(g[0]) for g in UB]); Pinv=P.inv()
assert P.det()!=0
ZUB=S.Matrix.hstack(*[S.Matrix(g[1]) for g in UB])
UPAIRS=list(combinations(range(5),2))
variables=S.symbols("lC lD lE " + " ".join("z"+str(i)+str(j) for i,j in UPAIRS))
print("Universal rank-five Schreier determinant:",P.det(),flush=True)
TEST_WORDS=[[1,2,-1,-2], [1,2,-1,-2]*2,
            [1,1,2,2,-1,-1,-2,-2],
            [1,1,2,-1,-2,-1], [2,1,2,-1,-2,-2]]
TEST_U=[UWORD(w,[ux,uy]) for w in TEST_WORDS]
assert all(v[2]==0 and v[0][0]==v[0][1]==0 for v in TEST_U)
TEST_COORDS=[dict(zip(variables,v[0][2:]+v[1])) for v in TEST_U]

def evaluate_u(g,h):
    """Return X,Y,Z logs, each linear in the thirteen actual u coordinates."""
    bb=[word(w,[g,h]) for w in SCHREIER]
    assert all(x[2]==0 for x in bb)
    lin=S.Matrix.hstack(*[S.Matrix(x[0]) for x in bb])*Pinv
    bracket=S.Matrix([[lin[0,i]*lin[1,j]-lin[1,i]*lin[0,j] for i,j in UPAIRS]])
    cen=S.Matrix([[x[1][0] for x in bb]])*Pinv-bracket*ZUB*Pinv
    image=S.Matrix.vstack(lin,cen)
    result=image[:,2:5]*S.Matrix(variables[:3])
    result[2]+=(bracket*S.Matrix(variables[3:]))[0]
    return result

dihedral=evaluate_u(((Q(0),Q(0)),(Q(0),),1),
                    ((Q(-1),Q(0)),(Q(0),),1))
ordinary=evaluate_u(((Q(1),Q(0)),(Q(0),),0),
                    ((Q(0),Q(1)),(Q(0),),0))
assert dihedral==S.Matrix([-variables[2],0,0])
assert ordinary==S.Matrix([0,0,variables[3]])
print("Calibrated dihedral k=-lE; ordinary c2=z01",flush=True)

def pentagon(q):
    a,b,c,d,e,f=[q[k] for k in KEYS]
    args=[(a,mul(c,e)),(mul(b,c),f),(c,f),(mul(a,b),mul(e,f)),(a,c)]
    us=[evaluate_u(*v) for v in args]
    # u1 u2 = u3 u4 u5 in the retained P4 convention.
    order=[us[0],us[1],-us[4],-us[3],-us[2]]
    z=S.zeros(3,1)
    for u in order:
        z[2]+=u[2]+(z[0]*u[1]-z[1]*u[0])/2
        z[0]+=u[0];z[1]+=u[1]
    return [S.expand(v) for v in z],args

def rat(x):
    x=S.Rational(x)
    return Q(int(x.p),int(x.q))

lifted=[]; obstructed=[]; polynomials=[]; exact_word_checks=0
for (ep,a),(eq,b) in combinations(chars,2):
    hh=[ep[i]+2*eq[i] for i in range(6)]
    q0={k:((Q(a[i]),Q(b[i])),(Q(0),),hh[i]) for i,k in enumerate(KEYS)}
    ds=defects(q0)
    assert all(d[0]==d[1]==0 for d in ds)
    rhs=-S.Matrix([d[2] for d in ds])
    ec=tuple(x^y for x,y in zip(ep,eq)); M=matrices[ec]
    # The same character matrix governs the central coordinate.
    try: sol,params=M.gauss_jordan_solve(rhs)
    except ValueError:
        left=M.T.nullspace()
        left_den=reduce(lcm,[int(x.q) for v in left for x in v],1)
        assert left_den & (left_den-1)==0
        ob=[(v.T*rhs)[0] for v in left]
        den=reduce(lcm,[int(x.q) for x in ob],1)
        gg=reduce(gcd,[abs(int(x*den)) for x in ob],0)
        assert gg==1 and den==1
        obstructed.append({"lambda":ep,"nu":eq,"left_kernel_obstruction_gcd":gg,
                           "common_denominator":den,"left_basis_denominator":left_den})
        continue
    zz=sol.subs({v:0 for v in params})
    zs=[zz]+[zz+v for v in M.nullspace()]
    record={"lambda":ep,"nu":eq,"a":a,"b":b,"central":[str(v) for v in zz],"polynomials":[]}
    for z in zs:
        q={k:((Q(a[i]),Q(b[i])),(rat(z[i]),),hh[i]) for i,k in enumerate(KEYS)}
        assert all(all(v==0 for v in d) for d in defects(q))
        pp,args=pentagon(q)
        for g,h in args:
            symbolic=evaluate_u(g,h)
            for ww,co in zip(TEST_WORDS,TEST_COORDS):
                actual=word(ww,[g,h]); assert actual[2]==0
                evaluated=[S.expand(v.subs(co)) for v in symbolic]
                assert evaluated==list(actual[0]+actual[1]),(ww,actual,evaluated)
                exact_word_checks+=1
        record["polynomials"].append([str(v) for v in pp])
        for v in pp:
            if v!=0: polynomials.append(v)
    lifted.append(record)

polynomials=list(dict.fromkeys(polynomials))
print("Independent character pairs:",len(lifted)+len(obstructed),flush=True)
print("Actual rational Heisenberg lifts:",len(lifted),"; cup-obstructed:",len(obstructed),flush=True)
print("Distinct nonzero universal pentagon polynomials:",len(polynomials),flush=True)
for v in polynomials:print(" ",v,flush=True)

# Linearize quadratic monomials to identify exact row-space consequences;
# no replacement of the actual nonlinear equations by an equivalence is made.
monomials=sorted(set(m for f in polynomials for m,c in S.Poly(f,variables).terms()))
rows=S.Matrix([[S.Poly(f,variables).coeff_monomial(m) for m in monomials] for f in polynomials]) if polynomials else S.zeros(0,0)
target=variables[2]**2-variables[2]-6*variables[3] # z01 is the ordinary c2 coordinate.
tm=S.Poly(target,variables)
all_monomials=sorted(set(monomials)|set(m for m,c in tm.terms()))
rr=S.Matrix([[S.Poly(f,variables).coeff_monomial(m) for m in all_monomials] for f in polynomials]) if polynomials else S.zeros(0,len(all_monomials))
tr=S.Matrix([[tm.coeff_monomial(m) for m in all_monomials]])
in_span=rr.rank()==rr.col_join(tr).rank()
print("Exact polynomial coefficient rank:",rr.rank(),flush=True)
print("Target lE^2-lE-6*z01 in exact linear span:",in_span,flush=True)
assert all(S.diff(f,variables[3])==0 for f in polynomials)
word_values=[S.expand(f.subs(TEST_COORDS[1])) for f in polynomials]
target_word=S.expand(target.subs(TEST_COORDS[1]))
print("Exact actual-word substitution checks:",exact_word_checks,flush=True)
print("All pentagon polynomials omit ordinary z01:",True,flush=True)
print("Actual u=[x,y]^2 gives pentagon polynomial values:",word_values,flush=True)
print("Same word's target value:",target_word,flush=True)
assert all(v==0 for v in word_values) and target_word==8

data={"scope":"rational actual P4 representations; necessary universal pentagon equations only",
      "character_lines":[{"epsilon":e,"basis":v} for e,v in chars],
      "schreier_basis":SCHREIER,"universal_first_matrix":str(P),"universal_det":str(P.det()),
      "variables":[str(v) for v in variables],"lifts":lifted,"cup_obstructed_pairs":obstructed,
      "nonzero_polynomials":[str(v) for v in polynomials],"coefficient_rank":rr.rank(),
      "target":str(target),"target_in_span":in_span,"exact_word_checks":exact_word_checks,
      "test_words":TEST_WORDS,"commutator_squared_coordinates":{str(k):str(v) for k,v in TEST_COORDS[1].items()},
      "commutator_squared_polynomial_values":[str(v) for v in word_values],
      "commutator_squared_target":str(target_word)}
OUT.write_text(json.dumps(data,indent=2)+"\n")
print("SAVED",OUT,flush=True)
