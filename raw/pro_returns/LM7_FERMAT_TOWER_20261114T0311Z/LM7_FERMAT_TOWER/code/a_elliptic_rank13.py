#!/usr/bin/env python3
"""Exact rank-eleven ring and rank-thirteen metabelian quotient certificate."""
from fractions import Fraction as Q
from pathlib import Path
import json, importlib.util, contextlib, io
import sympy as sp

spec=importlib.util.spec_from_file_location('small',Path(__file__).with_name('a_elliptic_frobenius.py'))
sm=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(sm)

DIM=11
def basis(i):return tuple(Q(int(j==i)) for j in range(DIM))
zero=basis(0);zero=tuple(Q(0) for _ in range(DIM))
one=basis(0);X=basis(3);Y=basis(1);U=basis(9);V=basis(10)
def add(*ps):return tuple(sum((p[i] for p in ps),Q(0)) for i in range(DIM))
def scale(p,a):return tuple(Q(a)*v for v in p)
def aug(p):return sum(p[:9],Q(0))
def mul(p,q):
    out=[Q(0)]*DIM
    for i,a in enumerate(p):
        if not a:continue
        for j,b in enumerate(q):
            if not b:continue
            if i>=9 and j>=9:continue
            if i>=9:out[i]+=a*b;continue
            if j>=9:out[j]+=a*b;continue
            i1,i2=divmod(i,3);j1,j2=divmod(j,3)
            k1,k2=i1+j1,i2+j2
            out[3*(k1%3)+k2%3]+=a*b
            out[9]+=a*b*(k1//3);out[10]+=a*b*(k2//3)
    return tuple(out)
def prod(*ps):
    out=one
    for p in ps:out=mul(out,p)
    return out
def residue(a):
    a=Q(a);assert a.denominator%3
    return a.numerator*pow(a.denominator,-1,3)%3
def mono(a,b):
    a,b=Q(a),Q(b);r,s=residue(a),residue(b)
    return add(basis(3*r+s),scale(U,(a-r)/3),scale(V,(b-s)/3))
def S(a,which):
    a=Q(a);r=residue(a);q=(a-r)/3
    def pp(i):return mono(i,0) if which==0 else mono(0,i)
    sr=add(*(pp(i) for i in range(r))) if r else zero
    s3=add(*(pp(i) for i in range(3)))
    return add(sr,scale(s3,q),scale(U if which==0 else V,q*r+3*q*(q-1)/2))
def ring_inverse(p):
    m=sp.Matrix.hstack(*(sp.Matrix(mul(p,basis(i))) for i in range(DIM)))
    ans=tuple(Q(v) for v in m.inv()*sp.Matrix(one))
    assert mul(p,ans)==one
    return ans

ring_checks=0
for i in range(DIM):
    for j in range(DIM):
        assert mul(basis(i),basis(j))==mul(basis(j),basis(i))
        for k in range(DIM):
            assert mul(mul(basis(i),basis(j)),basis(k))==mul(basis(i),mul(basis(j),basis(k)))
            ring_checks+=1
assert prod(X,X,X)==add(one,U) and prod(Y,Y,Y)==add(one,V)
for w in [U,V]:
    for t in [add(X,scale(one,-1)),add(Y,scale(one,-1))]:assert mul(w,t)==zero
for a in [Q(-7),Q(-2),Q(-1,2),Q(1,2),Q(1),Q(4),Q(7,2)]:
    for w,t in [(0,X),(1,Y)]:
        assert mul(add(t,scale(one,-1)),S(a,w))==add(mono(a,0) if w==0 else mono(0,a),scale(one,-1))

# Normal group coordinates x^a y^b c^H, retaining the module even when
# multiplication by X-1 and Y-1 annihilates its central U,V directions.
identity=(Q(0),Q(0),zero)
gx=(Q(1),Q(0),zero);gy=(Q(0),Q(1),zero);gc=(Q(0),Q(0),one)
def gm(g,h):
    a,b,H=g;A,B,K=h
    correction=prod(mono(-A,-b-B),S(A,0),S(b,1))
    return a+A,b+B,add(mul(mono(-A,-B),H),K,scale(correction,-1))
def gp(*gs):
    out=identity
    for g in gs:out=gm(out,g)
    return out
def gi(g):
    a,b,H=g
    # Solve the right inverse using the exact multiplication formula.
    corr=prod(mono(a,0),S(-a,0),S(b,1))
    out=(-a,-b,add(scale(mul(mono(a,b),H),-1),corr))
    assert gm(g,out)==identity and gm(out,g)==identity
    return out
def gcom(g,h):return gp(g,h,gi(g),gi(h))
assert gcom(gx,gy)==gc
def binom(a,n):
    out=Q(1)
    for i in range(n):out*=Q(a-i,i+1)
    return out
def powerN(g,a):
    assert residue(g[0])==residue(g[1])==0
    vals=[identity]
    for i in range(3):vals.append(gm(vals[-1],g))
    dif=[v[2] for v in vals];co=[]
    for i in range(4):
        co.append(dif[0]);dif=[add(dif[j+1],scale(dif[j],-1)) for j in range(len(dif)-1)]
    return Q(a)*g[0],Q(a)*g[1],add(*(scale(co[i],binom(Q(a),i)) for i in range(4)))
def power(g,a):
    a=Q(a);r=residue(a);q=(a-r)/3
    small=identity
    for i in range(r):small=gm(small,g)
    cube=gp(g,g,g)
    return gm(small,powerN(cube,q))
def ring_map(H,A):
    a,b,c,d=A
    out=zero
    for i,v in enumerate(H[:9]):
        r,s=divmod(i,3);out=add(out,scale(mono(a*r+c*s,b*r+d*s),v))
    return add(out,scale(add(scale(U,a),scale(V,b)),H[9]),
               scale(add(scale(U,c),scale(V,d)),H[10]))
def action(Xg,Yg):
    A=(Xg[0],Xg[1],Yg[0],Yg[1]);det=A[0]*A[3]-A[1]*A[2]
    assert gcom(Xg,Yg)==(0,0,scale(one,det))
    return Xg,Yg,A,det
def apply(g,f):
    Xg,Yg,A,det=f
    return gp(power(Xg,g[0]),power(Yg,g[1]),(0,0,scale(ring_map(g[2],A),det)))
def compose(f,g):return action(apply(g[0],f),apply(g[1],f))
idaction=action(gx,gy)
def actword(fs):
    f=idaction
    for g in fs:f=compose(f,g)
    return f
def T1(a):return action(gp(gx,power(gy,-Q(a))),gy)
def T2(a):return action(gx,gp(gy,power(gx,Q(a))))
def inner(k):
    q=(0,0,scale(one,k))
    return action(gp(q,gx,gi(q)),gp(q,gy,gi(q)))

h=mul(add(prod(Y,Y),scale(Y,2),scale(one,3)),
      ring_inverse(mul(add(Y,one),add(prod(Y,Y),one))))
canonical=action(gp((0,0,h),gx),power(gy,4))
diag=actword([T2(-2),T1(Q(-1,2)),T2(-3),T1(-1),T2(-1)])
base=compose(diag,canonical)
principal=compose(inner(Q(-1,2)),base)
local=compose(inner(Q(-5,8)),base)
path_test=actword([T1(Q(1,2)),local,T1(Q(-1,2))])
# The reference full-F lift agrees with the genuine action on N/Jm.
# Equality is asserted on that exact subgroup, not on the ambient x,y.
assert principal==compose(inner(Q(1,8)),local)

def ambient(g):
    a,b,H=g
    n=aug(H)
    r=sum(Q(i//3)*H[i] for i in range(9))+3*H[9]
    s=sum(Q(i%3)*H[i] for i in range(9))+3*H[10]
    return sm.normal(a,b,n,r,s)
for f,small in [(principal,sm.principal),(local,sm.local),(canonical,sm.tate(4))]:
    assert ambient(f[0])==small[0] and ambient(f[1])==small[1]

samples=[]
for i in range(12):
    H=tuple(Q((i*(j+2)+j)%7-3,2**(j%2)) for j in range(DIM))
    samples.append((Q(3*(i-5),2),Q(3*(i%4-2)),H))
power_checks=0;group_checks=0
for g in samples:
    for n in range(-4,9):
        direct=identity
        f=g if n>=0 else gi(g)
        for _ in range(abs(n)):direct=gm(direct,f)
        assert power(g,n)==direct;power_checks+=1
    for h0 in samples:
        assert ambient(gm(g,h0))==sm.mul(ambient(g),ambient(h0))
        assert apply(gm(g,h0),principal)==gm(apply(g,principal),apply(h0,principal))
        group_checks+=1

names=['xi=x^3','eta=y^3']+[f'c^X^{i}Y^{j}' for i in range(3) for j in range(3)]+['c^U','c^V']
gens=[power(gx,3),power(gy,3)]+[(0,0,basis(i)) for i in range(DIM)]
assert all(apply(g,principal)==apply(g,path_test) for g in gens)
images={name:{'a':str(apply(g,principal)[0]/3),
              'b':str(apply(g,principal)[1]/3),
              'module':[str(v) for v in apply(g,principal)[2]]}
        for name,g in zip(names,gens)}
P=prod(add(one,X,prod(X,X)),add(one,Y,prod(Y,Y)))
assert gcom(gens[0],gens[1])==(0,0,P)
assert gcom(gens[0],gc)==(0,0,U) and gcom(gens[1],gc)==(0,0,V)
assert gcom(gens[0],(0,0,P))==(0,0,scale(U,9))
assert gcom(gens[1],(0,0,P))==(0,0,scale(V,9))
assert all(v.denominator%3 for rec in images.values() for v in map(Q,rec['module']))

projection=sp.Matrix([[int(i<9) for i in range(DIM)],
    [i//3 if i<9 else (3 if i==9 else 0) for i in range(DIM)],
    [i%3 if i<9 else (3 if i==10 else 0) for i in range(DIM)]])
right=sp.zeros(DIM,3);right[0,0]=1;right[3,1]=1;right[0,1]=-1;right[1,2]=1;right[0,2]=-1
assert projection*right==sp.eye(3)

out={'status':'PASS','statement':'E.58','ring_basis':[f'X^{i}Y^{j}' for i in range(3) for j in range(3)]+['U','V'],
     'ring_associativity_checks':ring_checks,'group_and_action_checks':group_checks,
     'integer_power_checks':power_checks,'canonical_Tate4_h':[str(q) for q in h],
     'Frobenius_principal_images':images,'ambient_projection':projection.tolist(),
     'projection_integer_right_inverse':right.tolist(),
     'lower_central':{'gamma2_generators':['P c','U c','V c'],
        'gamma3_generators':['9U c','9V c'],'gamma2_mod_gamma3':'Z3 + (Z/9)^2',
        'abelianization_rank':10,'underlying_Z3_coordinate_rank':13},
     'based_root_transport':'T1(1/2) local T1(-1/2) = principal = Ad(c^(1/8)) local'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print('PASS:',ring_checks,'rank-eleven ring associativity checks;',group_checks,'group/action comparisons;',power_checks,'power checks.')
print('PASS: actual rank-thirteen Frobenius, both discriminant-root transports, and ambient rank-five projection.')
print('xi and eta images:',images[names[0]],images[names[1]])
