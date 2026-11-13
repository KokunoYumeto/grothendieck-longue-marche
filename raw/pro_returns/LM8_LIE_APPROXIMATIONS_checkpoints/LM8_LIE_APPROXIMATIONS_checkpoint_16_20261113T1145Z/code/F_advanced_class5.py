"""Exact truncated group/Lie computations for the integral class-five attack.

The first executable calculation derives the low GT hexagon coefficients.
Further certificates distinguish full and metabelian degree-five quotients.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial
from functools import lru_cache
from pathlib import Path
import json

N = 5
ONE = {(): Q(1)}
X = {(0,): Q(1)}
Y = {(1,): Q(1)}


def add(*args):
    result = {}
    for a in args:
        for w, c in a.items():
            result[w] = result.get(w, Q(0)) + c
    return {w: c for w, c in result.items() if c}


def scale(a, t):
    return {w: t*c for w, c in a.items() if t*c}


def mul(a, b, n=N):
    result = {}
    for u, cu in a.items():
        for v, cv in b.items():
            if len(u) + len(v) <= n:
                result[u+v] = result.get(u+v, Q(0)) + cu*cv
    return {w: c for w, c in result.items() if c}


def prod(*args):
    result = ONE
    for a in args:
        result = mul(result, a)
    return result


def bracket(a, b):
    return add(mul(a, b), scale(mul(b, a), -1))


def truncate(a, n):
    return {w: c for w, c in a.items() if len(w) <= n}


def hom(a, n):
    return {w: c for w, c in a.items() if len(w) == n}


def exp(a):
    assert not a.get((), 0)
    out, term = ONE, ONE
    for k in range(1, N+1):
        term = mul(term, a)
        out = add(out, scale(term, Q(1, factorial(k))))
    return out


def power(a, exponent):
    assert a.get((), 0) == 1
    t = add(a, scale(ONE, -1))
    out, term, coefficient = ONE, ONE, Q(1)
    for k in range(1, N+1):
        term = mul(term, t)
        coefficient *= Q(exponent-k+1, k)
        out = add(out, scale(term, coefficient))
    return out


def log(a):
    assert a.get((), 0) == 1
    t = add(a, scale(ONE, -1))
    out, term = {}, ONE
    for k in range(1, N+1):
        term = mul(term, t)
        out = add(out, scale(term, Q((-1)**(k+1), k)))
    return out


def subst(a, x, y):
    cache = {(): ONE}
    def word(w):
        if w not in cache:
            cache[w] = mul(word(w[:-1]), (x, y)[w[-1]])
        return cache[w]
    return add(*(scale(word(w), c) for w, c in a.items()))


def comm(a, b):
    return prod(a, b, power(a, -1), power(b, -1))


def coordinates(a, basis):
    words = sorted(set(a).union(*(set(x) for x in basis)))
    matrix = [[b.get(w, Q(0)) for b in basis]+[a.get(w, Q(0))]
              for w in words]
    pivots = []
    k = 0
    for j in range(len(basis)):
        pivot = next((i for i in range(k, len(matrix)) if matrix[i][j]), None)
        if pivot is None:
            continue
        matrix[k], matrix[pivot] = matrix[pivot], matrix[k]
        scalar = matrix[k][j]
        matrix[k] = [x/scalar for x in matrix[k]]
        for i in range(len(matrix)):
            if i != k and matrix[i][j]:
                scalar = matrix[i][j]
                matrix[i] = [x-scalar*y for x,y in zip(matrix[i],matrix[k])]
        pivots.append((j, k))
        k += 1
    assert len(pivots) == len(basis)
    assert not any(not any(row[:-1]) and row[-1] for row in matrix)
    result = [Q(0)]*len(basis)
    for j, i in pivots:
        result[j] = matrix[i][-1]
    assert add(a,scale(add(*(scale(b,c) for b,c in zip(basis,result))),-1)) == {}
    return result


C = bracket(X, Y)
U, V = bracket(X, C), bracket(Y, C)
E = [bracket(X, U), bracket(Y, U), bracket(Y, V)]
L5 = [bracket(X,E[0]), bracket(Y,E[0]), bracket(Y,E[1]),
      bracket(Y,E[2]), bracket(C,U), bracket(C,V)]
assert len(coordinates(L5[0],L5)) == 6


def gt_low(q, a=Q(0), c=None):
    x, y = exp(X), exp(Y)
    z = power(mul(x,y), -1)
    Z = log(z)
    m, r = Q(q-1,2), Q(q*q-1,24)
    def f(c, d):
        return exp(add(scale(C,r),scale(add(U,V),a),
                       scale(add(E[0],E[2]),c),scale(E[1],d)))
    def defect(c,d):
        F = f(c,d)
        value = prod(power(x,m),subst(F,Z,X),power(z,m),
                     subst(F,Y,Z),power(y,m),F)
        return truncate(add(value,scale(ONE,-1)),4)
    if c is None:
        raise ValueError("The hexagon alone leaves the degree-four depth-one coefficient free")
    constant = defect(c,Q(0))
    columns = [add(defect(c,Q(1)),scale(constant,-1))]
    d, = coordinates(scale(constant,-1),columns)
    assert defect(c,d) == {}
    F = f(c,d)
    assert truncate(add(mul(F,subst(F,Y,X)),scale(ONE,-1)),4) == {}
    return dict(q=q,m=m,r=r,a=a,c=c,d=d,F=truncate(F,4))


class Auto:
    """IA automorphism on a free group, acting on its Magnus variables."""
    def __init__(self, images):
        self.images = images
        self.cache = {():ONE}
    def word(self,w):
        if w not in self.cache:
            self.cache[w] = mul(self.word(w[:-1]), self.images[w[-1]])
        return self.cache[w]
    def apply(self,p):
        return add(*(scale(self.word(w),c) for w,c in p.items()))
    def delta(self,p):
        return add(self.apply(p),scale(p,-1))
    def log(self,p):
        out,term={},p
        for k in range(1,N+1):
            term=self.delta(term)
            if not term:
                break
            out=add(out,scale(term,Q((-1)**(k+1),k)))
        return out
    def inverse(self):
        result=[]
        for j in range(len(self.images)):
            g={(j,):Q(1)}
            out,term=g,g
            for k in range(1,N+1):
                term=self.delta(term)
                if not term:
                    break
                out=add(out,scale(term,(-1)**k))
            result.append(out)
        return Auto(result)


def amul(*autos):
    # g -> (p -> g^-1 p g) reverses composition.
    result=[{(j,):Q(1)} for j in range(len(autos[0].images))]
    for a in autos:
        result=[a.apply(p) for p in result]
    return Auto(result)


def inner_auto(g):
    return Auto([add(prod(power(g,-1),add(ONE,{(j,):Q(1)}),g),
                     scale(ONE,-1)) for j in range(3)])


def pb4():
    u,v,w=[add(ONE,{(j,):Q(1)}) for j in range(3)]
    iu,iv,iw=[power(g,-1) for g in (u,v,w)]
    h=comm(u,w)
    A=Auto([add(prod(u,v,u,iv,iu),scale(ONE,-1)),
            add(prod(u,v,iu),scale(ONE,-1)),
            add(w,scale(ONE,-1))])
    B=Auto([add(u,scale(ONE,-1)),
            add(prod(v,w,v,iw,iv),scale(ONE,-1)),
            add(prod(v,w,iv),scale(ONE,-1))])
    C=Auto([add(prod(u,w,u,iw,iu),scale(ONE,-1)),
            add(prod(h,v,power(h,-1)),scale(ONE,-1)),
            add(prod(u,w,iu),scale(ONE,-1))])
    U,V,W=[inner_auto(g) for g in (u,v,w)]
    central=amul(A,C,B)
    for g in (A,B,C):
        assert amul(central,g).images == amul(g,central).images
    assert amul(A.inverse(),U,A).images == amul(U,V,U,V.inverse(),U.inverse()).images
    assert amul(A.inverse(),V,A).images == amul(U,V,U.inverse()).images
    assert amul(A.inverse(),W,A).images == W.images
    assert amul(B.inverse(),U,B).images == U.images
    assert amul(B.inverse(),V,B).images == amul(V,W,V,W.inverse(),V.inverse()).images
    assert amul(B.inverse(),W,B).images == amul(V,W,V.inverse()).images
    assert amul(C.inverse(),U,C).images == amul(U,W,U,W.inverse(),U.inverse()).images
    hh=amul(U,W,U.inverse(),W.inverse())
    assert amul(C.inverse(),V,C).images == amul(hh,V,hh.inverse()).images
    assert amul(C.inverse(),W,C).images == amul(U,W,U.inverse()).images
    return A,B,C,U,V,W


def eval_log_operator(F,A,B,p):
    result={}
    for word,c in F.items():
        value=p
        for letter in word:
            value=(A,B)[letter].log(value)
            if not value:
                break
        result=add(result,scale(value,c))
    return result


def eval_group_operator(F,A,B,p):
    out,term=p,p
    for k in range(1,3):
        term=eval_log_operator(F,A,B,term)
        out=add(out,scale(term,Q(1,factorial(k))))
    return out


def pentagon_low(q, a=Q(0)):
    A,B,C,UU,VV,W=pb4()
    pairs=[(B,W),(amul(A,C),amul(VV,W)),(A,B),
           (A,amul(B,VV)),(amul(C,B),W)]
    r=Q(q*q-1,24)
    def defect(c,d):
        F=add(scale(C_free,r),scale(add(U_free,V_free),a),
              scale(add(E[0],E[2]),c),scale(E[1],d))
        out={}
        for j in range(3):
            left=right={(j,):Q(1)}
            for k in range(3):
                left=eval_group_operator(F,*pairs[k],left)
            for k in range(3,5):
                right=eval_group_operator(F,*pairs[k],right)
            for word,value in add(left,scale(right,-1)).items():
                out[(j,)+word]=value
        return out
    constant=defect(Q(0),Q(0))
    columns=[add(defect(Q(1),Q(0)),scale(constant,-1)),
             add(defect(Q(0),Q(1)),scale(constant,-1))]
    c,d=coordinates(scale(constant,-1),columns)
    assert not defect(c,d)
    hexagon=gt_low(q,a,c)
    assert hexagon["d"]==d
    words=sorted(set(constant).union(*map(set,columns)))
    minor=None
    for i,w in enumerate(words):
        for z in words[i+1:]:
            matrix=[[col.get(t,Q(0)) for col in columns] for t in (w,z)]
            det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
            if det:
                minor=dict(
                    rows=[list(w),list(z)], matrix=matrix,
                    right_hand_side=[-constant.get(w,Q(0)),-constant.get(z,Q(0))],
                    determinant=det,
                    row_format="first entry is the acted-on free generator; remaining entries form the Magnus word")
                break
        if minor:
            break
    assert minor is not None
    hexagon["pentagon_column_rank"]=2
    hexagon["pentagon_nonzero_minor"]=minor
    hexagon["pentagon_all_associative_rows_verified"]=True
    hexagon["PB4_presentation_relations_verified"]=12
    return hexagon


C_free,U_free,V_free=C,U,V


def printable(x):
    if isinstance(x,Q):
        return str(x)
    if isinstance(x,dict):
        return {str(k):printable(v) for k,v in x.items()}
    if isinstance(x,list):
        return [printable(v) for v in x]
    return x


def mod5(x):
    x=Q(x)
    assert x.denominator%5
    return x.numerator*pow(x.denominator,-1,5)%5


def low_action(q,a=Q(0)):
    # Coefficients independently forced by the full PB4 pentagon below.
    c,d={2:(Q(-1,96),Q(-1,128)),
         3:(Q(-1,18),Q(-1,36))}[q]
    row=gt_low(q,a,c)
    assert row["d"]==d
    x,y=add(ONE,X),add(ONE,Y)
    f=subst(row["F"],log(x),log(y))
    theta=Auto([add(power(x,q),scale(ONE,-1)),
                add(prod(power(f,-1),power(y,q),f),scale(ONE,-1))])
    return theta


def normalize_soule(q,a=Q(1)):
    x,y=add(ONE,X),add(ONE,Y)
    s=-a/Q(q**3-1)
    k=subst(exp(scale(add(U_free,V_free),s)),log(x),log(y))
    eta=Auto([X,add(prod(power(k,-1),y,k),scale(ONE,-1))])
    assert all(t.denominator%5 for p in eta.images for t in p.values())
    changed=amul(eta,low_action(q,a),eta.inverse())
    assert changed.images==low_action(q,Q(0)).images
    return dict(q=q,input_Soule_coefficient=a,coordinate_change_coefficient=s,
                exact_action_equality_through_class5=True)


def local_obstruction(q,a,b):
    x,y=add(ONE,X),add(ONE,Y)
    c=comm(x,y)
    u,v=comm(x,c),comm(y,c)
    e=[comm(x,u),comm(y,u),comm(y,v)]
    groups={2:[c],3:[u,v],4:e}
    lies={2:[C_free],3:[U_free,V_free],4:E}
    theta=low_action(q)
    inertia=mul(power(x,a),power(y,b))
    inertia_coordinates=[Q(a),Q(b)]
    for weight in (2,3,4):
        defect=add(mul(theta.apply(inertia),power(inertia,-q)),scale(ONE,-1))
        assert not truncate(defect,weight-1)
        correction=[-t/Q(q**weight-q)
                    for t in coordinates(hom(defect,weight),lies[weight])]
        assert all(t.denominator%5 for t in correction)
        inertia=prod(inertia,*(power(g,t) for g,t in zip(groups[weight],correction)))
        inertia_coordinates+=correction
    defect=add(mul(theta.apply(inertia),power(inertia,-q)),scale(ONE,-1))
    assert not truncate(defect,4)
    d=coordinates(defect,L5)
    d5=[mod5(t) for t in d]
    tangent=add(scale(X,a),scale(Y,b))
    matrix=[[mod5(t) for t in coordinates(scale(bracket(e,tangent),q),L5)]
            for e in E]
    good=[]
    good_met=[]
    for w in product(range(5),repeat=3):
        if not any((d5[j]+sum(w[k]*matrix[k][j] for k in range(3)))%5
                   for j in range(6)):
            good.append(list(w))
        if not any((d5[j]+sum(w[k]*matrix[k][j] for k in range(3)))%5
                   for j in range(4)):
            good_met.append(list(w))
    assert good_met==good
    tq=(q**4-1)//5
    normalized=[mod5(t/Q(q*tq)) for t in d]
    expected=[a**4*b,3*b-a**3*b*b,2*b+a*a*b**3,
              3*b-a*b**4,a**3*b*b,2*a*a*b**3]
    assert normalized==[x%5 for x in expected]
    normalized_good=[[mod5(Q(wi,tq)) for wi in w] for w in good]
    if not a and not b:
        assert len(good)==125
    elif not b:
        assert normalized_good==[[0,0,0]]
    elif not a:
        assert normalized_good==[[3,2,3]]
    elif a==b:
        assert normalized_good==[[1,1,2]]
    else:
        assert not good
    return dict(q=q,abelian=[a,b],Hall_inertia_coordinates=inertia_coordinates,
                obstruction_exact=d,obstruction_mod5=d5,
                normalized_obstruction_mod5=normalized,
                torsion_parameter_columns=matrix,
                admissible_Frobenius_parameters=good,
                normalized_admissible_Frobenius_parameters=normalized_good,
                full_and_metabelian_loci_identical=True)


def zero_abelian_module():
    x,y=exp(X),exp(Y)
    c=comm(x,y)
    u,v=comm(x,c),comm(y,c)
    e=[comm(x,u),comm(y,u),comm(y,v)]
    b=[comm(x,e[0]),comm(y,e[0]),comm(y,e[1]),comm(y,e[2]),
       comm(c,u),comm(c,v)]
    homogeneous=[U_free,V_free]+E+L5
    group_basis=[u,v]+e+b
    transition=[]
    for g in group_basis:
        row=coordinates(log(g),homogeneous)
        assert all(t.denominator%5 for t in row)
        transition.append(row)
    assert all(transition[i][i]==1 for i in range(11))
    assert all(not transition[i][j] for i in range(11) for j in range(i))
    def D(p):
        out={}
        for word,c0 in p.items():
            for j,letter in enumerate(word):
                if letter==1:
                    for w,c1 in V_free.items():
                        out[word[:j]+w+word[j+1:]]=out.get(
                            word[:j]+w+word[j+1:],Q(0))+c0*c1
        return {w:c for w,c in out.items() if c}
    du,dv=D(U_free),D(V_free)
    du_coord,dv_coord=coordinates(du,L5),coordinates(dv,L5)
    assert du_coord==[0,1,0,0,1,0]
    assert dv_coord==[0,0,1,0,0,-1]
    adjusted=[add(U_free,scale(du,Q(-1,24))),
              add(V_free,scale(dv,Q(-1,24)))]
    for q in (2,3,6):
        r=Q(q*q-1,24)
        F=add(scale(C_free,r),scale(add(U_free,V_free),7),
              scale(E[0],11),scale(E[1],13),scale(E[2],17))
        phi_x=scale(X,q)
        phi_y=log(prod(exp(scale(F,-1)),exp(scale(Y,q)),exp(F)))
        for v0 in adjusted:
            assert subst(v0,phi_x,phi_y)==scale(v0,q**3)
        for weight,basis in ((4,E),(5,L5)):
            for v0 in basis:
                assert subst(v0,phi_x,phi_y)==scale(v0,q**weight)
    return dict(
        homogeneous_basis_order=["U","V","E1","E2","E3",
                                 "B1","B2","B3","B4","B5","B6"],
        group_Hall_log_transition=transition,
        transition_unipotent_over_Z5=True,
        D2_on_U=du_coord,D2_on_V=dv_coord,
        diagonalized_weight3_basis=["U-(B2+B5)/24","V-(B3-B6)/24"],
        action_checks=[2,3,6],
        arbitrary_higher_f_coefficients_used=[7,11,13,17],
        actual_action_diagonal_after_integral_change=True,
        integral_H1_full="Z5^8 plus (Z/5)^3",
        integral_H1_metabelian="Z5^6 plus (Z/5)^3")


def cyclotomic_units():
    def cmul(a,b):
        p=[0]*7
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                p[i+j]+=x*y
        for k in range(6,3,-1):
            t=p[k]
            for j in range(4):
                p[k-4+j]-=t
        return p[:4]
    def cpow(a,n):
        result=[1,0,0,0]
        while n:
            if n&1:
                result=cmul(result,a)
            a=cmul(a,a)
            n//=2
        return result
    zeta=[0,1,0,0]
    one=[1,0,0,0]
    factors=[]
    for a in range(1,5):
        za=cpow(zeta,a)
        factors.append([x-y for x,y in zip(one,za)])
    phi=[0,0,-1,-1]
    sqrt5=[-1,0,-2,-2]
    epsilon={}
    for m in (3,5):
        e=one
        for a,fa in enumerate(factors,1):
            e=cmul(e,cpow(fa,a**(m-1)))
        epsilon[m]=e
    k3=cmul(sqrt5,cmul(factors[2],cpow(factors[3],3)))
    assert epsilon[3]==cmul(cpow(k3,5),cpow(phi,3))
    k5=cmul(cpow(factors[1],3),
            cmul(cpow(factors[2],16),cpow(factors[3],51)))
    assert epsilon[5]==[5*x for x in cpow(k5,5)]
    return dict(
        field_polynomial=[1,1,1,1,1],
        phi=phi,sqrt5=sqrt5,
        epsilon3=epsilon[3],epsilon5=epsilon[5],
        fifth_power_factor3=k3,fifth_power_factor5=k5,
        exact_identity3="epsilon3=k3^5*phi^3",
        exact_identity5="epsilon5=k5^5*5",
        non_fifth_power_and_noncyclotomic_arguments="Proved in source by the fundamental real unit and complex conjugation; not inferred from numeric values")


if __name__ == "__main__":
    result=dict(
        statement="F.23",
        status="Proved for the specified local congruence calculation and zero-abelian fibre",
        scope="Actual arithmetic action; all affine local coordinates retained",
        full_global_class3_frame_difference="Retained explicitly as v3(c)-v2(c); not set to zero or identified with a graded substitute")
    pentagons=[]
    for q in (2,3):
        row=pentagon_low(q)
        print(q, {k:str(v) for k,v in row.items()
                  if k in ("m","r","a","c","d")},flush=True)
        other=pentagon_low(q,Q(1))
        assert row["c"]==other["c"] and row["d"]==other["d"]
        pentagons.append({k:v for k,v in row.items() if k!="F"})
    result["pentagon_coefficients"]=pentagons
    result["local_Soule_normalizations"]=[normalize_soule(q) for q in (2,3)]
    result["zero_abelian_module"]=zero_abelian_module()
    result["primitive_Soule_Kummer_units"]=cyclotomic_units()
    local=[]
    for q in (2,3):
        rows=[local_obstruction(q,a,b) for a,b in product(range(5),repeat=2)]
        print("q",q,"admissible abelian pairs",
              [r["abelian"] for r in rows if r["admissible_Frobenius_parameters"]],
              "total local parameters",sum(len(r["admissible_Frobenius_parameters"])
                                           for r in rows),flush=True)
        local+=rows
    result["local_rows"]=local
    result["normalized_polynomial"]=[
        "a^4*b","3*b-a^3*b^2","2*b+a^2*b^3","3*b-a*b^4",
        "a^3*b^2","2*a^2*b^3"]
    result["normalized_linear_side"]=[
        "a*v1","b*v1+a*v2","b*v2+a*v3","b*v3","a*v2","a*v3"]
    result["central_cohomology"]=dict(
        H1_weight5="Z5",H2_weight5="C5^2",
        localization="isomorphism onto H2(Q2,Z5(5)) plus H2(Q3,Z5(5))",
        class5_full_nonempty_fibre="Z5^6 torsor",
        class5_metabelian_nonempty_fibre="Z5^4 torsor")
    result["counterexample"]=dict(
        abelian_pair=["kappa(2)","2*kappa(2)"],
        class4_lifts_exist=True,class5_lifts_exist=False,
        reason="At2, the residue pair(1,2) lies on none of the three permitted lines")
    Path(__file__).with_suffix(".json").write_text(
        json.dumps(printable(result),indent=2)+"\n")
