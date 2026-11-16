"""All 495 labelled cross-ratio pairs for the tetrahedral and C5 curves.

Coefficients and the common icosahedral basepoint are checked exactly in
Q(q)/(Phi_20(q)), q=exp(pi*i/10).  No numerical equality is used.
The output is data for necessary tests, not a claim that their joint
fundamental-group representation is faithful.
"""
from pathlib import Path
from functools import lru_cache
from itertools import combinations
import csv
import sympy as S

q,u,t,w=S.symbols('q u t w')
mod=S.Poly(S.cyclotomic_poly(20,q),q,domain=S.QQ)

def norm(a):
    p=S.Poly(a,q,domain=S.QQ).rem(mod)
    return tuple(p.nth(i) for i in range(8))
ZERO=norm(0);ONE=norm(1)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
@lru_cache(None)
def mul(a,b):
    c=[S.Rational(0)]*15
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    # q^8=q^6-q^4+q^2-1.
    for k in range(14,7,-1):
        v=c[k]
        for d,f in [(2,1),(4,-1),(6,1),(8,-1)]:c[k-d]+=f*v
    return tuple(c[:8])
@lru_cache(None)
def inv(a):
    assert a!=ZERO
    p=S.Poly(sum(c*q**i for i,c in enumerate(a)),q,domain=S.QQ)
    return norm(S.invert(p,mod).as_expr())
def div(a,b):return mul(a,inv(b))
def powf(a,k):
    if k<0:return powf(inv(a),-k)
    r=ONE
    while k:
        if k&1:r=mul(r,a)
        a=mul(a,a);k//=2
    return r
def expr(a):return S.expand(sum(c*q**i for i,c in enumerate(a)))
Q=norm(q);I=powf(Q,5);OMEGA=powf(Q,4)
def gaussian(a):
    re,im=S.expand_complex(a).as_real_imag()
    return add(norm(re),mul(norm(im),I))
def conjugate(a):
    return tuple(sum(a[j]*powf(Q,-j)[i] for j in range(8)) for i in range(8))

def matnorm(M):
    flat=list(M)
    lead=next(x for x in flat if x!=0)
    return tuple(S.simplify(x/lead) for x in flat)
def mm(A,B):return matnorm(S.Matrix(2,2,A)*S.Matrix(2,2,B))
def tetra_group():
    E=(S.Integer(1),S.Integer(0),S.Integer(0),S.Integer(1))
    gens=[matnorm(S.Matrix([[-1,0],[0,1]])),
          matnorm(S.Matrix([[0,1],[1,0]])),
          matnorm(S.Matrix([[1,S.I],[1,-S.I]]))]
    elements=[E];todo=[E]
    while todo:
        a=todo.pop(0)
        for b in gens:
            c=mm(a,b)
            if c not in elements:elements.append(c);todo.append(c)
    assert len(elements)==12
    assert all(mm(a,b) in elements for a in elements for b in elements)
    return elements

def det(P,Q):return P[0]*Q[1]-P[1]*Q[0]
def cr(points,inds):
    i,j,k,l=[points[i] for i in inds]
    return S.cancel(det(i,k)*det(j,l)/(det(i,l)*det(j,k)))
def fdet(P,Q):return sub(mul(P[0],Q[1]),mul(P[1],Q[0]))
def fcr(points,inds):
    i,j,k,l=[points[i] for i in inds]
    return div(mul(fdet(i,k),fdet(j,l)),mul(fdet(i,l),fdet(j,k)))

def main():
    out=Path(__file__).resolve().parents[1]/'data'
    out.mkdir(exist_ok=True)
    group=tetra_group()
    # phi=2cos(pi/5), R=2cos(pi/10), u0=i*(R+phi).
    phi=add(powf(Q,2),powf(Q,-2))
    R=add(Q,inv(Q))
    u0=mul(I,add(R,phi))
    points=[(S.expand(a*u+b),S.expand(c*u+d)) for a,b,c,d in group]
    exact=[]
    for a,b,c,d in group:
        exact.append((add(mul(gaussian(a),u0),gaussian(b)),
                      add(mul(gaussian(c),u0),gaussian(d))))
    vals=[div(a,b) for a,b in exact]
    assert len(set(vals))==12
    antipode=neg(inv(conjugate(u0)))
    pole=vals.index(antipode)
    north=0
    anchor=next(i for i in range(12) if i not in (north,pole))
    # Common projective normalization sends north to0,pole to infinity,anchor to1.
    factor=div(sub(vals[anchor],antipode),sub(vals[anchor],u0))
    normal=[]
    for v in vals:
        normal.append((mul(sub(v,u0),factor),sub(v,antipode)))
    nv={i:div(a,b) for i,(a,b) in enumerate(normal) if b!=ZERO}
    labels={north:('zero',0),pole:('infinity',0)}
    for k in range(5):
        value=powf(OMEGA,k)
        inds=[j for j in nv if nv[j]==value]
        assert len(inds)==1
        labels[inds[0]]=('first',k)
    second=next(i for i in range(12) if i not in labels)
    t0=nv[second]
    for k in range(5):
        value=mul(t0,powf(OMEGA,k))
        inds=[j for j in nv if nv[j]==value]
        assert len(inds)==1
        labels[inds[0]]=('second',k)
    assert len(labels)==12
    cyclic=[];cyclic_exact=[]
    for j in range(12):
        kind,k=labels[j]
        if kind=='zero':P=(S.Integer(0),S.Integer(1));F=(ZERO,ONE)
        elif kind=='infinity':P=(S.Integer(1),S.Integer(0));F=(ONE,ZERO)
        elif kind=='first':P=(w**k,S.Integer(1));F=(powf(OMEGA,k),ONE)
        else:P=(t*w**k,S.Integer(1));F=(mul(t0,powf(OMEGA,k)),ONE)
        cyclic.append(P);cyclic_exact.append(F)
    rows=[];degrees={};constants=0
    for inds in combinations(range(12),4):
        a=cr(points,inds);b=cr(cyclic,inds)
        n,d=S.fraction(a)
        degree=max(S.degree(n,u),S.degree(d,u))
        assert degree<=4
        degrees[int(degree)]=degrees.get(int(degree),0)+1
        if degree==0:constants+=1
        assert fcr(exact,inds)==fcr(cyclic_exact,inds)
        rows.append([','.join(str(i+1) for i in inds),S.sstr(a),S.sstr(b),degree])
    assert len(rows)==495
    with (out/'crossratio_495.csv').open('w',newline='') as f:
        wr=csv.writer(f);wr.writerow(['labels','psi_A4_u','phi_C5_t','degree_psi']);wr.writerows(rows)
    with (out/'crossratio_labels.csv').open('w',newline='') as f:
        wr=csv.writer(f);wr.writerow(['label','tetrahedral_homogeneous_point','cyclic_homogeneous_point'])
        for i,(a,b) in enumerate(points):
            wr.writerow([i+1,f'({S.sstr(a)} : {S.sstr(b)})',
                         f'({S.sstr(cyclic[i][0])} : {S.sstr(cyclic[i][1])})'])
    print('Tetrahedral projective group order:',len(group))
    print('Exact coefficient field: Q[q]/(q^8-q^6+q^4-q^2+1), q=exp(pi*i/10)')
    print('u0 =',expr(u0));print('t0 =',expr(t0))
    print('C5 root w=q^4; north,pole,anchor labels =',north+1,pole+1,anchor+1)
    print('All 495 basepoint cross-ratio equalities: PASS (exact field arithmetic)')
    print('Degree distribution of psi:',degrees)
    print('Constant psi maps:',constants)
    print('Domain exceptional set: {infinity} plus zeros of u*(u^4-1)*(u^8+14*u^4+1)')
    print('Every nonconstant psi has at most12 points over0,1,infinity; domain has14 punctures.')
    print('Each psi_* therefore kills at least two puncture meridians before further quotient.')
    print('Files: data/crossratio_495.csv; data/crossratio_labels.csv')

if __name__=='__main__':main()
