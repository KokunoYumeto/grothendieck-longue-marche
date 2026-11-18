"""Independent finite checks, written before opening checkpoint program sources.

Inputs transcribed from mathematical statements/proofs A.CF6, A.CF11,
A.CR14 and A.R6. Standard library only. Integer words: 1=a,2=b,etc.
The graph-chain implementation does not import a checkpoint module.
"""
import json, time
from collections import deque
from pathlib import Path

OUT=Path(__file__).resolve().parent

def mul2(a,b,poly):
    d=poly.bit_length()-1; z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a>>d:a^=poly
    return z
def power2(a,n,poly):
    z=1
    while n:
        if n&1:z=mul2(z,a,poly)
        a=mul2(a,a,poly);n>>=1
    return z
def order2(a,poly):
    x=1
    for n in range(1,1<<(poly.bit_length()-1)):
        x=mul2(x,a,poly)
        if x==1:return n
    return None
def field_checks(poly):
    q=1<<(poly.bit_length()-1)
    assert all(power2(a,q-1,poly)==1 for a in range(1,q))
    return q

def cr14():
    poly=(1<<7)|(1<<1)|1;q=field_checks(poly)
    points=[(x,y) for x in range(q) for y in range(q)
            if mul2(y,y,poly)^y==power2(x,5,poly)]
    P=(2,1<<6);Q=(1<<2,(1<<6)|(1<<5))
    orbit=[];R=P
    while R not in orbit:
        orbit.append(R);R=tuple(mul2(a,a,poly) for a in R)
    assert len(orbit)==7 and orbit[1]==Q and P in points and Q in points
    n7=sum(any(mul2(a,a,poly)!=a for a in R) for R in points)
    gl=1
    for i in range(4):gl*=3**4-3**i
    assert gl==24261120 and gl%7 and len(points)+1==129 and n7==126
    return dict(modulus=poly,points=points,orbit=orbit,total_points=len(points)+1,
                degree_seven_points=n7,degree_seven_closed_points=n7//7,GL4_3=gl)

def r6():
    poly=(1<<6)|(1<<1)|1;q=field_checks(poly)
    zeta=power2(2,7,poly);lam=power2(2,9,poly)
    assert order2(zeta,poly)==9 and order2(lam,poly)==7
    zpow=[power2(zeta,i,poly) for i in range(9)]
    def mul(x,y):return (x[0]^mul2(zpow[x[1]],y[0],poly),(x[1]+y[1])%9)
    def alpha(x):return (mul2(lam,x[0],poly),x[1])
    elems=[(a,i) for a in range(q) for i in range(9)]
    for x in elems:
        for y in elems:assert alpha(mul(x,y))==mul(alpha(x),alpha(y))
    gens=[(1,0),(0,1)];seen={(0,0)};todo=deque(seen)
    while todo:
        x=todo.popleft()
        for g in gens:
            y=mul(x,g)
            if y not in seen:seen.add(y);todo.append(y)
    comm={a^mul2(zeta,a,poly) for a in range(q)}
    core=[i for i in range(9) if all(mul2(zpow[i],a,poly)==a for a in range(q))]
    assert len(seen)==576 and len(comm)==64 and core==[0]
    return dict(modulus=poly,zeta=zeta,lambda_value=lam,zeta_order=9,lambda_order=7,
                generated_order=len(seen),checked_products=576**2,commutator_image_size=len(comm),
                complement_core=core,abelianization_order=9,Frattini_order=1)

def red(w):
    s=[]
    for a in w:
        if s and s[-1]==-a:s.pop()
        else:s.append(a)
    return tuple(s)
def inv(w):return tuple(-a for a in reversed(w))
def cat(*ws):return red(a for w in ws for a in w)
def comm(a,b):return cat(a,b,inv(a),inv(b))
def subst(w,images):return cat(*(images[a-1] if a>0 else inv(images[-a-1]) for a in w))
def compose(u,v):return tuple(subst(w,u) for w in v)
def autpow(a,n):
    x=tuple((i+1,) for i in range(len(a)))
    for _ in range(n):x=compose(a,x)
    return x

def cf6():
    p=3;d=4;one=(0,0,0)
    def gm(a,b):return ((a[0]+b[0])%p,(a[1]+b[1])%p,(a[2]+b[2]+a[0]*b[1])%p)
    def gi(a):return ((-a[0])%p,(-a[1])%p,(-a[2]+a[0]*a[1])%p)
    gens=[(1,0,0),(0,1,0),one,one]
    def evalw(w):
        a=one
        for x in w:a=gm(a,gens[x-1] if x>0 else gi(gens[-x-1]))
        return a
    reps={one:()};q=deque([one]);tree=set()
    while q:
        a=q.popleft()
        for j in range(d):
            b=gm(a,gens[j])
            if b not in reps:reps[b]=reps[a]+(j+1,);tree.add((a,j));q.append(b)
    vertices=list(reps);edges=[(a,j) for a in vertices for j in range(d) if (a,j) not in tree]
    idx={e:i for i,e in enumerate(edges)}
    basis=[cat(reps[a],(j+1,),inv(reps[gm(a,gens[j])])) for a,j in edges]
    assert len(basis)==82
    def chain(w):
        a=one;v=[0]*len(edges)
        for x in w:
            if x>0:e=(a,x-1);sgn=1;b=gm(a,gens[x-1])
            else:
                b=gm(a,gi(gens[-x-1]));e=(b,-x-1);sgn=-1
            if e in idx:v[idx[e]]+=sgn
            a=b
        assert a==one
        return v
    for j,w in enumerate(basis):assert chain(w)==[int(i==j) for i in range(82)]
    a,b,c,e=[(i,) for i in range(1,5)]
    t=cat(comm(a,inv(b)),comm(c,inv(e)))
    C=(a,b,cat(t,c,inv(t)),cat(t,e,inv(t),t,inv(c),t,c,inv(t)))
    D=(a,b,cat(c,inv(t)),cat(t,e,inv(t)))
    C3=autpow(C,3);D3=autpow(D,3)
    assert all(evalw(C3[j])==gens[j] and evalw(D3[j])==gens[j] for j in range(4))
    MC=[chain(subst(w,C3)) for w in basis];MD=[chain(subst(w,D3)) for w in basis]
    # Columns stored as rows of this JSON, deliberately named column arrays.
    z=evalw(comm(a,b))
    def cycle(j,s):return cat(reps[s],(j,),inv(reps[s]))
    x=[u-v for u,v in zip(chain(cycle(3,one)),chain(cycle(3,z)))]
    y=[u-v for u,v in zip(chain(cycle(4,one)),chain(cycle(4,z)))]
    def apply(cols,v):return [sum(v[j]*cols[j][i] for j in range(82)) for i in range(82)]
    assert apply(MC,x)==x and apply(MC,y)==[3*u+v for u,v in zip(x,y)]
    assert apply(MD,x)==[u-3*v for u,v in zip(x,y)] and apply(MD,y)==y
    w=[u-v for u,v in zip(x,y)];Mw=apply(MC,apply(MD,w))
    assert any(a%5 for a in w) and all((a+b)%5==0 for a,b in zip(w,Mw))
    return dict(group_order=27,fibre_quotient_order=str(27*5**82),rank=82,
                C_images=C,D_images=D,C_cube=C3,D_cube=D3,vertices=vertices,
                basis=basis,MC_columns=MC,MD_columns=MD,x=x,y=y,
                restricted_C=[[1,3],[0,1]],restricted_D=[[1,0],[-3,1]],
                eigenvector=w,eigenvalue_mod5=4)

def cf11():
    p=3;n=4;I=tuple(int(i==j) for i in range(n) for j in range(n))
    J=(0,1,0,0,-1,0,0,0,0,0,0,1,0,0,-1,0)
    def mm(a,b):return tuple(sum(a[4*i+k]*b[4*k+j] for k in range(4))%3 for i in range(4) for j in range(4))
    def trans(v):
        vJ=[sum(v[k]*J[4*k+j] for k in range(4)) for j in range(4)]
        return tuple((int(i==j)+2*v[i]*vJ[j])%3 for i in range(4) for j in range(4))
    vs=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,0,1,0)]
    gs=list(map(trans,vs));seen={I};q=deque([I])
    while q:
        a=q.popleft()
        for g in gs:
            b=mm(a,g)
            if b not in seen:seen.add(b);q.append(b)
    w=I
    for j in [4,3,1,1,0]:w=mm(w,gs[j])
    powers=[I]
    for _ in range(5):powers.append(mm(powers[-1],w))
    assert len(seen)==51840 and powers[5]==I and all(x!=I for x in powers[1:5])
    return dict(generating_directions=vs,generators=gs,generated_order=len(seen),
                order_five_word=[4,3,1,1,0],order_five_matrix=w,order_five_powers=powers,
                Schreier_rank=41,fibre_quotient_order=str(8*3**41))

def main():
    ans={};t=time.time()
    for name,f in [('A.CR14',cr14),('A.R6',r6),('A.CF6',cf6),('A.CF11',cf11)]:
        t0=time.time();r=f();ans[name]=r
        (OUT/(name.replace('.','_')+'_independent.json')).write_text(json.dumps(r,indent=2)+'\n')
        print(name,'PASS','elapsed',round(time.time()-t0,3),flush=True)
    summary={'claims':list(ans),'seconds':round(time.time()-t,3),'all_passed':True,
             'protocol':'Written and run before checkpoint program source inspection; mathematical source statements/proofs read.'}
    (OUT/'independent_s6_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary),flush=True)
if __name__=='__main__':main()
