#!/usr/bin/env python3
"""Exact genuine class-three arithmetic operators and wild defects, E78."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json
import sympy as s

OUT = Path(__file__).resolve().parent
A, B, n, U, V, N, k, r, z = s.symbols("A B n U V N k r z")
zero = (s.Integer(0),)*5


def mul(g, h):
    x,y,c,d,e = map(s.sympify,g)
    X,Y,C,D,E = map(s.sympify,h)
    return tuple(s.expand(v) for v in (
        x+X, y+Y, c+C-X*y,
        d+D+y*X*(X+1)/2-X*c,
        e+E+X*y*(y+1)/2-Y*c+X*y*Y))


def inv(g):
    x,y,c,d,e = map(s.sympify,g)
    return tuple(s.expand(v) for v in (
        -x, -y, -c-x*y,
        -d-x*c-x*y*(x-1)/2,
        -e-y*c+x*y*(1-y)/2))


def power(g, m):
    if m < 0:
        return power(inv(g), -m)
    out = zero
    while m:
        if m & 1:
            out = mul(out, g)
        g = mul(g, g)
        m //= 2
    return out


def alpha(g, kk):
    x,y,c,d,e = map(s.sympify,g)
    kk = s.sympify(kk)
    return tuple(s.expand(v) for v in (
        7*x, 7*y, 7*kk*y+49*c,
        7*kk*(kk-1)*y/2+(147+49*kk)*c+343*d,
        (14-28*kk)*y-49*kk*y*(y-1)/2+147*c+343*e))


def f(u, a, kk):
    return mul(mul(mul(u, alpha(a, kk)), inv(u)), inv(power(a, 7)))


L = 3*A*B - A*V + B*U + B*k + 6*n
R = s.Rational(7,2)*(
    29*A*A*B - 7*A*A*V + 14*A*B*U + 14*A*B*k - 3*A*B
    - 2*A*N - 2*A*U*V + A*V + 90*A*n + B*U*U
    + 2*B*U*k - B*U + B*k*k - B*k
    + 14*U*n + 14*k*n + 42*n)
S = s.Rational(7,2)*(
    13*A*B*B - 3*A*B - A*V*V + A*V
    + 7*B*B*U + 7*B*B*k - 2*B*N - B*U
    + 2*B*V*k - B*k + 90*B*n + 4*B + 14*V*n + 42*n)

aa = (A,B,n,s.Integer(0),s.Integer(0))
uu = (U,V,N,s.Integer(0),s.Integer(0))
actual = f(uu, aa, k)
expected = (0,0,7*L,R,S)
assert all(s.expand(a-b) == 0 for a,b in zip(actual, expected))
changed = f(uu, (A,B,n,r,z), k)
assert all(s.expand(a-b) == 0 for a,b in
           zip(changed, (0,0,7*L,R+336*r,S+336*z)))
assert mul(aa, inv(aa)) == mul(inv(aa), aa) == zero
assert mul(uu, inv(uu)) == mul(inv(uu), uu) == zero

# Exact independent associative Magnus model.
DEG = 3


def madd(*ps):
    out = {}
    for p in ps:
        for w,a in p.items():
            out[w] = out.get(w,Q(0))+a
    return {w:a for w,a in out.items() if a}


def mscale(p, a):
    return {w:a*b for w,b in p.items() if a*b}


def mmul(p, q):
    out = {}
    for w,a in p.items():
        for v,b in q.items():
            if len(w+v) <= DEG:
                out[w+v] = out.get(w+v,Q(0))+a*b
    return {w:a for w,a in out.items() if a}


one = {(): Q(1)}
x = {(): Q(1), (0,): Q(1)}
y = {(): Q(1), (1,): Q(1)}


def mpow(p, a):
    a = Q(a)
    v = madd(p, mscale(one,-1))
    term = one
    out = one
    coef = Q(1)
    for j in range(1, DEG+1):
        term = mmul(term,v)
        coef *= (a-j+1)/j
        out = madd(out,mscale(term,coef))
    return out


def mprod(*ps):
    out = one
    for p in ps:
        out = mmul(out,p)
    return out


def mcomm(p,q):
    return mprod(p,q,mpow(p,-1),mpow(q,-1))


cc = mcomm(x,y)
dd = mcomm(x,cc)
ee = mcomm(y,cc)


def normal(g):
    return mprod(*(mpow(v,Q(a)) for v,a in zip((x,y,cc,dd,ee),g)))


def evaluate(poly,X,Y):
    vx,vy = madd(X,mscale(one,-1)),madd(Y,mscale(one,-1))
    out = {}
    for w,a in poly.items():
        term = one
        for letter in w:
            term = mmul(term,vx if letter == 0 else vy)
        out = madd(out,mscale(term,a))
    return out


def maction(kk):
    return mpow(x,7), mprod(mpow(x,kk),mpow(cc,-2),
                            mpow(y,7),mpow(cc,2),mpow(x,-kk))


images = {}
for label, kk in [("tau",Q(-5,2)),("tau_prime",Q(1,2))]:
    X,Y = maction(kk)
    im = [alpha(g,s.Rational(kk.numerator,kk.denominator))
          for g in [(1,0,0,0,0),(0,1,0,0,0),(0,0,1,0,0),
                    (0,0,0,1,0),(0,0,0,0,1)]]
    for g, actual_image in zip((x,y,cc,dd,ee),im):
        assert evaluate(g,X,Y) == normal(actual_image)
    images[label] = [[str(v) for v in a] for a in im]

magnus_checks = 0
for i in range(160):
    kk = Q(-5,2) if i % 2 == 0 else Q(1,2)
    g = tuple(Q((i*(j+2)+j*j)%17-8,2 if (i+j)%3 == 0 else 1)
              for j in range(5))
    h = tuple(Q((i*(j+5)+3*j)%19-9,2 if (i+j)%4 == 0 else 1)
              for j in range(5))
    X,Y = maction(kk)
    assert normal(mul(g,h)) == mmul(normal(g),normal(h))
    assert normal(inv(g)) == mpow(normal(g),-1)
    assert normal(alpha(g,kk)) == evaluate(normal(g),X,Y)
    assert normal(f(h,g,kk)) == mprod(
        normal(h),evaluate(normal(g),X,Y),
        mpow(normal(h),-1),mpow(normal(g),-7))
    magnus_checks += 4

# Actual affine root/source transport, retaining the arbitrary original
# Kummer t before the evaluated E49 normalization.
transport = []
for tt in [Q(1),Q(4),Q(7),Q(10),Q(-2),Q(1,4),Q(4,7),Q(10,13)]:
    assert (tt-1).numerator % 3 == 0 and tt.denominator % 3
    h_exponent = (1/tt-1)/12
    k3h = -2*tt*h_exponent
    assert tt-6*k3h == 1
    kah = -Q(3,2)*k3h
    old = -1-Q(3,2)*tt
    old_prime = -1+Q(3,2)*tt
    assert old-6*kah == Q(-5,2)
    assert old_prime+6*kah == Q(1,2)
    Xold,Yold = maction(old)
    H = mpow(x,kah)
    Hi = mpow(x,-kah)
    # alpha_h alpha_tau alpha_h^-1 is the actual conjugated Frobenius.
    conjugated = []
    for v in (x,y):
        inside = mprod(Hi,v,H)
        conjugated.append(mprod(H,evaluate(inside,Xold,Yold),Hi))
    assert tuple(conjugated) == maction(Q(-5,2))
    transport.append([str(tt),str(h_exponent),str(k3h),str(kah)])

# The exhibited class-two family and its complete degree-three defect.
family = f((s.Rational(5,2),0,N,0,0),(0,1,0,0,0),s.Rational(-5,2))
assert tuple(s.expand(v) for v in family) == (0,0,0,0,7*(2-N))
family_lift = f((s.Rational(5,2),0,N,0,0),
                (0,1,0,0,(N-2)/48),s.Rational(-5,2))
assert tuple(s.expand(v) for v in family_lift) == zero

# The exact cusp-conjugator transport used to construct an intrinsic
# preimage of every class-two family member.  Its unknown central
# coordinates are retained symbolically; no path value is guessed.
path_conjugator = (s.Rational(5,2),V,2-s.Rational(5,2)*V,r,z)
assert tuple(s.expand(v) for v in
             f(path_conjugator,(0,1,0,0,0),s.Rational(-5,2))) == zero
normalized_path = mul((0,-V,0,0,0),path_conjugator)
assert tuple(s.expand(v) for v in normalized_path[:3]) == (
    s.Rational(5,2),0,2)
assert tuple(s.expand(v) for v in
             f(normalized_path,(0,1,0,0,0),s.Rational(-5,2))) == zero
intrinsic_changed = mul(normalized_path,(0,0,N-2,0,0))
assert tuple(s.expand(v) for v in
             f(intrinsic_changed,(0,1,0,0,0),s.Rational(-5,2))) == (
                 0,0,0,0,7*(2-N))


def mod3q(a, modulus=3):
    a = Q(a)
    assert a.denominator % 3
    return a.numerator * pow(a.denominator,-1,modulus) % modulus


def expr(poly, data, kk):
    return Q(poly.subs(dict(zip((A,B,n,U,V,N,k),list(data)+[kk]))))


# Two successive complete central-fibre coordinate maps and inverses.
# Each lower tuple is kept literal.  We verify the actual correction
# and the effect of every retained normalizing conjugator.
class2_lifts = class3_lifts = framed_checks = 0
class2_fibre_checks = abelian_fibre_checks = 0
for i in range(180):
    u = (Q(i%7-3),Q((3*i)%11-5),Q(0),Q(0),Q(0))
    up = (Q((5*i)%13-6),Q((7*i)%17-8),Q(0),Q(0),Q(0))
    a = (Q((2*i)%5-2),Q((4*i)%7-3),Q(0),Q(0),Q(0))
    ap = (Q((3*i)%11-5),Q((6*i)%13-6),Q(0),Q(0),Q(0))
    eps = tuple(mod3q(v) for v in up[:2])
    abw = tuple((up[j]-eps[j])/6 for j in range(2))
    aword = (abw[0],abw[1],Q(0),Q(0),Q(0))
    anorm = mul(mul(aword,u),inv(alpha(aword,Q(-5,2))))
    apnorm = mul(mul(aword,up),inv(alpha(aword,Q(1,2))))
    assert tuple(apnorm[:2]) == eps
    assert tuple(anorm[j]-apnorm[j] for j in range(2)) == tuple(
        u[j]-up[j] for j in range(2))
    assert tuple(mul(mul(aword,a),inv(aword))[:2]) == tuple(a[:2])
    assert tuple(mul(mul(aword,ap),inv(aword))[:2]) == tuple(ap[:2])
    abelian_fibre_checks += 1
    D = Q(f(u,a,Q(-5,2))[2]-f(up,ap,Q(1,2))[2])/7
    if mod3q(D):
        continue
    a = (a[0],a[1],-D/6,a[3],a[4])
    assert f(u,a,Q(-5,2))[2] == f(up,ap,Q(1,2))[2]
    class2_lifts += 1
    for j in range(3):
        common = Q(3*j-4)
        bu,bup = Q(5*j-8),Q(11*j+7)
        aa2 = (a[0],a[1],a[2]+common,Q(0),Q(0))
        aap2 = (ap[0],ap[1],ap[2]+common,Q(0),Q(0))
        uu2 = (u[0],u[1],bu,Q(0),Q(0))
        uup2 = (up[0],up[1],bup,Q(0),Q(0))
        assert f(uu2,aa2,Q(-5,2))[:3] == f(uup2,aap2,Q(1,2))[:3]
        residue = mod3q(bup)
        ww = (bup-residue)/48
        assert ww.denominator % 3
        conjugator = (Q(0),Q(0),ww,Q(0),Q(0))
        nu2 = mul(mul(conjugator,uu2),
                  inv(alpha(conjugator,Q(-5,2))))
        nup2 = mul(mul(conjugator,uup2),
                   inv(alpha(conjugator,Q(1,2))))
        assert nup2[2] == residue and nu2[2]-nup2[2] == bu-bup
        assert mul(mul(conjugator,aa2),inv(conjugator))[:3] == aa2[:3]
        assert mul(mul(conjugator,aap2),inv(conjugator))[:3] == aap2[:3]
        class2_fibre_checks += 1
    difference = tuple(s.expand(v-w) for v,w in
                       zip(f(u,a,Q(-5,2)),f(up,ap,Q(1,2))))
    assert difference[:3] == (0,0,0)
    rr,ss = map(Q,difference[3:])
    if mod3q(rr) or mod3q(ss):
        continue
    alift = (a[0],a[1],a[2],-rr/336,-ss/336)
    assert f(u,alift,Q(-5,2)) == f(up,ap,Q(1,2))
    class3_lifts += 1
    for j in range(5):
        common = (Q(j-2),Q(2*j+1))
        bu = (Q(3*j+2),Q(5*j-7))
        bup = (Q(17*j-11),Q(19*j+3))
        aa = (alift[0],alift[1],alift[2],
              alift[3]+common[0],alift[4]+common[1])
        aap = (ap[0],ap[1],ap[2],common[0],common[1])
        uu = (u[0],u[1],u[2],bu[0],bu[1])
        uup = (up[0],up[1],up[2],bup[0],bup[1])
        assert f(uu,aa,Q(-5,2)) == f(uup,aap,Q(1,2))
        residues = tuple(mod3q(v,9) for v in bup)
        w = tuple((bup[l]-residues[l])/342 for l in range(2))
        assert all(Q(v).denominator % 3 for v in w)
        conj = (0,0,0,w[0],w[1])
        uu2 = mul(mul(conj,uu),inv(alpha(conj,Q(-5,2))))
        uup2 = mul(mul(conj,uup),inv(alpha(conj,Q(1,2))))
        assert tuple(uup2[3:]) == residues
        assert tuple(s.expand(uu2[3+l]-uup2[3+l]) for l in range(2)) == tuple(
            bu[l]-bup[l] for l in range(2))
        assert mul(mul(conj,aa),inv(conj)) == aa
        assert mul(mul(conj,aap),inv(conj)) == aap
        framed_checks += 1

assert class2_lifts > 0 and class3_lifts > 0 and framed_checks > 0
answer = {
    "statement":"E.78","status":"PASS",
    "actual_arithmetic_Hall_images":images,
    "root_and_source_transport_records":transport,
    "polynomials":{"L":str(s.expand(L)),"R":str(s.expand(R)),"S":str(s.expand(S))},
    "full_symbolic_defect_verified":True,
    "central_changes_exactly_336":True,
    "independent_Hall_Magnus_checks":magnus_checks,
    "initial_class_two_lift_examples":class2_lifts,
    "abelian_fibre_coordinate_checks":abelian_fibre_checks,
    "class_two_fibre_coordinate_checks":class2_fibre_checks,
    "class_three_lift_examples":class3_lifts,
    "complete_central_fibre_coordinate_checks":framed_checks,
    "explicit_family_defect":"e^(7*(2-N))",
    "explicit_family_lift":"r maps to y*e^((N-2)/48), defined for N=2 modulo3",
    "intrinsic_cusp_conjugator_normalization_verified":True,
    "intrinsic_preimage_family":"An actual full cusp-conjugator section at N=2; central t-value changes w^(N-2) in N/gamma3 give every N. N=0 has no intrinsic class-three lift.",
    "class_two_fibre":"Z3^2 x C3",
    "class_three_fibre":"Z3^4 x C9^2",
    "scope":"Actual h quotient over Q3(zeta3), with the explicitly transported E49 source marking. The displayed intrinsic preimages are constructed from an actual peripheral conjugator and central changes; they are not inferred from geometric surjectivity alone."
}
(OUT/"a_wild_class3.json").write_text(json.dumps(answer,indent=2)+"\n")
print("PASS full symbolic actual operators and all three defect polynomials")
print("PASS",magnus_checks,"independent Hall/Magnus identities")
print("PASS",len(transport),"exact root/source conjugation transports")
print("PASS",class2_lifts,"class-two and",class3_lifts,"class-three lifting cases")
print("PASS",abelian_fibre_checks,"abelian and",class2_fibre_checks,"class-two fibre inverses")
print("PASS",framed_checks,"full central-fibre coordinate and inverse checks")
print("PASS exact symbolic cusp-conjugator transport and intrinsic-family defect")
print("ALL PASS")
