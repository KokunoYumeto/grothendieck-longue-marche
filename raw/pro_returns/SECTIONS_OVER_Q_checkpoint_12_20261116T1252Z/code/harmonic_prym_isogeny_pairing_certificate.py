"""Exact tangent-symbol pairing on the six A150 isogeny-Selmer classes.

The six conic points were found by Magma, but this program verifies them
literally. No Selmer-group or class-group output is used by this program.
All local points are exact Hensel witnesses; the proof text accounts for
every other place using primitive tangent forms and smooth reduction.
"""
from fractions import Fraction as F
from pathlib import Path
import itertools, json, math
import sympy as sp

BASE=Path(__file__).resolve().parent
ZERO=(F(0),F(0)); ONE=(F(1),F(0)); T=(F(0),F(1))
def k(x):return x if isinstance(x,tuple) else (F(x),F(0))
def add(x,y):
    x,y=k(x),k(y);return (x[0]+y[0],x[1]+y[1])
def neg(x):x=k(x);return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    x,y=k(x),k(y);return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def norm(x):x=k(x);return x[0]**2-2*x[1]**2
def inv(x):x=k(x);n=norm(x);assert n;return (x[0]/n,-x[1]/n)
def div(x,y):return mul(x,inv(y))
def power(x,n):
    x=k(x)
    if n<0:return power(inv(x),-n)
    z=ONE
    while n:
        if n&1:z=mul(z,x)
        x=mul(x,x);n//=2
    return z
def ser(x):return [str(a) for a in x]
def vp(n,p):
    if not n:return 10**9
    if isinstance(n,F):return vp(n.numerator,p)-vp(n.denominator,p)
    v=0
    while n%p==0:n//=p;v+=1
    return v
def modq(x,q):return x.numerator*pow(x.denominator,-1,q)%q
def nearest(q):return (2*q.numerator+q.denominator)//(2*q.denominator)
def egcd(x,y):
    oldr,rr=x,y;olds,ss=ONE,ZERO;oldt,tt=ZERO,ONE
    while rr!=ZERO:
        z=div(oldr,rr);q=(F(nearest(z[0])),F(nearest(z[1])))
        nr=sub(oldr,mul(q,rr));assert abs(norm(nr))<abs(norm(rr))
        oldr,rr=rr,nr;olds,ss=ss,sub(olds,mul(q,ss));oldt,tt=tt,sub(oldt,mul(q,tt))
    return oldr,olds,oldt
def primitive(xs):
    den=math.lcm(*(a.denominator for x in xs for a in x))
    ys=[mul(den,x) for x in xs];g=ZERO;bez=[ZERO]*len(xs)
    for i,y in enumerate(ys):
        ng,s,t=egcd(g,y);bez=[mul(s,z) for z in bez];bez[i]=add(bez[i],t);g=ng
    out=[div(y,g) for y in ys]
    assert all(a.denominator==1 for x in out for a in x)
    v=ZERO
    for z,c in zip(bez,out):v=add(v,mul(z,c))
    assert v==ONE
    return out,bez,div(g,den)

M=325596479663;b=mul(1146*M*M,power(add(1,T),2))
ds=[k(3),k(191),k(23),mul(139,(F(99),F(52))),
    mul(7,(F(1059),F(34))),mul(7,(F(1059),F(-34)))]
conics=[
    [(-16279823983150,-8465508471238),(-5860736633934,-5535140154271),(1,0)],
    [(-1209358353034,-1209358353034),(93027565618,46513782809),(1,0)],
    [(4186240452810,1721009963933),(-529852656346,-157742393874),(1,0)],
    [(F(8465508471238,3),F(-7581746597867,3)),(51387763804,F(-119041529854,3)),(1,0)],
    [(F(-15303034544161,17),F(-9442297910227,17)),(F(170332064643,17),F(106006317820,17)),(1,0)],
    [(F(2017395787991948,3361),F(1550164839675543,3361)),(F(24289382932178,3361),F(17063166874858,3361)),(1,0)]
]
conics=[[tuple(map(F,x)) for x in row] for row in conics]
forms=[];bezouts=[];contents=[]
for d,(n0,z0,v0) in zip(ds,conics):
    B=div(b,d);assert all(a.denominator==1 for a in B)
    assert power(n0,2)==add(mul(d,power(z0,2)),mul(B,power(v0,2)))
    fs,bez,c=primitive([n0,neg(mul(d,z0)),neg(mul(B,v0))])
    forms.append(fs);bezouts.append(bez);contents.append(c)

# Local squareclasses at the unique dyadic place. Unit squares modulo pi^5
# are exactly 1 and 3+2pi, and all 1+pi^5 units lift by one-variable Hensel.
units=[(1,0),(1,1),(1,2),(1,3),(3,1),(3,3),(5,0),(5,2)]
def unitcanon(a,c):return min((a%8,c%4),((3*a+4*c)%8,(2*a+3*c)%4))
unitmap={unitcanon(*u):i for i,u in enumerate(units)}
def v2k(x):return min(2*vp(x[0],2),2*vp(x[1],2)+1)
def local2(x):
    assert x!=ZERO;v=v2k(x);u=div(x,power(T,v))
    assert vp(u[0],2)==0 and vp(u[1],2)>=0
    return 8*(v%2)+unitmap[unitcanon(modq(u[0],8),modq(u[1],4))]
reps=[mul(power(T,e),tuple(map(F,u))) for e in [0,1] for u in units]
assert [local2(x) for x in reps]==list(range(16))
# Basis (-1,5,epsilon,pi). These Hilbert entries follow from norm
# corestriction to Q2 and the Steinberg identity (epsilon,-pi)=1.
hb=[k(-1),k(5),add(1,T),T]
HM=[[0,0,1,1],[0,0,0,1],[1,0,1,1],[1,1,1,1]]
bits={}
for mask in range(16):
    z=ONE
    for i in range(4):
        if mask>>i&1:z=mul(z,hb[i])
    bits[local2(z)]=mask
assert len(bits)==16
def hilbert2(x,y):
    a,c=bits[local2(x)],bits[local2(y)]
    parity=sum(HM[i][j] for i in range(4) for j in range(4) if (a>>i&1) and (c>>j&1))%2
    return -1 if parity else 1
def modpi(x,L):
    assert all(vp(a,2)>=0 for a in x)
    return (F(modq(x[0],2**((L+1)//2))),F(modq(x[1],2**(L//2))))
def sqrt2k(x,L=64):
    assert local2(x)==0;v=v2k(x);assert v%2==0
    u=div(x,power(T,v))
    z=next(tuple(map(F,(a,c))) for a in range(1,8,2) for c in range(4)
           if v2k(sub(power((F(a),F(c)),2),u))>=5)
    for _ in range(9):
        z=modpi(sub(z,div(sub(power(z,2),u),mul(2,z))),L)
    assert v2k(sub(power(z,2),u))>=L
    return mul(power(T,v//2),z),L+v//2-2

def leg(x,p):
    a=pow(int(x)%p,(p-1)//2,p);return 0 if a==0 else (1 if a==1 else -1)
def roots2(p):return [int(x) for x in sp.sqrt_mod(2,p,all_roots=True)]
def root_lift(rt,p,L):
    mod=p
    for _ in range(1,L):rt+=((2-rt*rt)//mod*pow(2*rt,-1,p)%p)*mod;mod*=p
    assert (rt*rt-2)%mod==0;return rt
def odd_data(x,p,root):
    assert x!=ZERO
    D=math.lcm(x[0].denominator,x[1].denominator);A=int(x[0]*D);C=int(x[1]*D);vD=vp(D,p)
    if root is None:
        v=min(vp(A,p),vp(C,p));aa=A//p**v;cc=C//p**v;den=D//p**vD
        return v-vD,leg((aa*aa-2*cc*cc)*pow(den,-2,p),p)
    L=vp(A*A-2*C*C,p)+1;rt=root_lift(root,p,L);mod=p**L
    n=(A+C*rt)%mod;v=vp(n,p);assert v<L
    return v-vD,leg((n//p**v)*pow(D//p**vD,-1,p),p)
def squareodd(x,p,root):
    if x==ZERO:return True
    v,s=odd_data(x,p,root);return v%2==0 and s==1
def hilbertodd(x,y,p,root):
    a,aa=odd_data(x,p,root);c,cc=odd_data(y,p,root)
    s=-1 if root is not None and p%4==3 and a*c%2 else 1
    return s*(aa if c%2 else 1)*(cc if a%2 else 1)
def redpair(x,mod):return (modq(x[0],mod),modq(x[1],mod))
def redsplit(x,p,root,L):
    D=math.lcm(x[0].denominator,x[1].denominator);vd=vp(D,p)
    rt=root_lift(root,p,L+vd);mod=p**(L+vd)
    num=(int(D*x[0])+int(D*x[1])*rt)%mod
    assert num%p**vd==0
    return (num//p**vd)*pow(D//p**vd,-1,p**L)%p**L
def sqrtodd(x,p,root,L=12):
    v,ss=odd_data(x,p,root);assert v%2==0 and ss==1;u=div(x,F(p)**v);mod=p**L
    if root is not None:
        a=redsplit(u,p,root,L)
        z=int(sp.sqrt_mod(a%p,p));pm=p
        for _ in range(1,L):z+=((a-z*z)//pm*pow(2*z,-1,p)%p)*pm;pm*=p
        assert (z*z-a)%mod==0
        ans=mul(F(p)**(v//2),z)
    else:
        up=redpair(u,p)
        z=next((F(a),F(c)) for a in range(p) for c in range(p)
               if redpair(power((F(a),F(c)),2),p)==up)
        for _ in range(6):
            z=sub(z,div(sub(power(z,2),u),mul(2,z)));z=tuple(F(modq(a,mod)) for a in z)
        assert min(vp(a,p) for a in sub(power(z,2),u))>=L
        ans=mul(F(p)**(v//2),z)
    assert odd_data(sub(power(ans,2),x),p,root)[0]>=L+v if sub(power(ans,2),x)!=ZERO else True
    return ans,L+v//2
def fourthunitodd(x,p,root,L=12):
    assert odd_data(x,p,root)[0]==0;mod=p**L
    if root is not None:
        a=redsplit(x,p,root,L)
        z=int(sp.nthroot_mod(a%p,4,p))
        pm=p
        for _ in range(1,L):z+=((a-z**4)//pm*pow(4*z**3,-1,p)%p)*pm;pm*=p
        ans=k(z)
    else:
        up=redpair(x,p)
        z=next((F(a),F(c)) for a in range(p) for c in range(p)
               if redpair(power((F(a),F(c)),4),p)==up)
        for _ in range(6):
            z=sub(z,div(sub(power(z,4),x),mul(4,power(z,3))));z=tuple(F(modq(a,mod)) for a in z)
        ans=z
    error=sub(power(ans,4),x)
    assert error==ZERO or odd_data(error,p,root)[0]>=L
    return ans,L

def fval(form,U,V,N):return add(add(mul(form[0],N),mul(form[1],power(U,2))),mul(form[2],power(V,2)))
rows=[];products=[[1]*6 for _ in range(6)]
bad=[2,3,5,7,13,23,139,191,1119169]
for i,(d,form) in enumerate(zip(ds,forms)):
    B=div(b,d)
    for p in bad:
        for root in ([None] if p==2 else (roots2(p) or [None])):
            found=None
            kind='square-root'
            if p!=2 and odd_data(d,p,root)[0]%2 and odd_data(B,p,root)[0]%2:
                U,precision=fourthunitodd(neg(div(B,d)),p,root)
                V=ONE;N=ZERO;fv=fval(form,U,V,N)
                assert fv!=ZERO
                vf=odd_data(fv,p,root)[0]
                assert precision+odd_data(form[1],p,root)[0]-vf>=1
                found=(U,V,N,fv,precision,vf);kind='fourth-root'
            # Both weighted affine charts; rational integer values usually
            # suffice. Nonrational residue candidates handle inert places.
            candidates=[ZERO,ONE]+[(F(a),F(c)) for a in range(32) for c in range(8)]
            for coord in candidates:
                if found:break
                for U,V in [(coord,ONE),(ONE,coord)]:
                    fx=add(mul(d,power(U,4)),mul(B,power(V,4)))
                    if fx==ZERO:continue
                    ok=(local2(fx)==0) if p==2 else squareodd(fx,p,root)
                    if not ok:continue
                    N,precision=sqrt2k(fx) if p==2 else sqrtodd(fx,p,root)
                    for N in [N,neg(N)]:
                        fv=fval(form,U,V,N)
                        if fv==ZERO:continue
                        vf=v2k(fv) if p==2 else odd_data(fv,p,root)[0]
                        a0v=v2k(form[0]) if p==2 else odd_data(form[0],p,root)[0]
                        # The actual square root differs from N to this
                        # precision; its tangent value has the same class.
                        if precision+a0v-vf < (5 if p==2 else 1):continue
                        found=(U,V,N,fv,precision,vf);break
                    if found:break
                if found:break
            assert found is not None,(i,p,root)
            U,V,N,fv,precision,vf=found
            hs=[hilbert2(e,fv) if p==2 else hilbertodd(e,fv,p,root) for e in ds]
            for j,h in enumerate(hs):products[i][j]*=h
            row={'i':i,'p':p,'root':root,'U':ser(U),'V':ser(V),'N_approx':ser(N),
                 'root_precision':precision,'root_kind':kind,'fvaluation':vf,'tangent':ser(fv),'symbols':hs}
            rows.append(row)
            print('LOCAL',i+1,p,root,hs,flush=True)
    # Every second entry is totally positive, so both real Hilbert symbols
    # are one, independently of the chosen local point/tangent value.

matrix=[[int(h==-1) for h in row] for row in products]
print('PAIRING MATRIX',matrix)
assert all(matrix[i][i]==0 for i in range(6))
assert all(matrix[i][j]==matrix[j][i] for i in range(6) for j in range(6))
vectors=[sum(bit<<j for j,bit in enumerate(row)) for row in matrix]
pivots={}
for v in vectors:
    while v:
        j=v.bit_length()-1
        if j in pivots:v^=pivots[j]
        else:pivots[j]=v;break
rank=len(pivots);print('EXACT F2 RANK',rank)
radical=[v for v in range(64) if all((v&r).bit_count()%2==0 for r in vectors)]
assert radical==[0,3,52,55]
assert mul(ds[0],ds[1])==k(573)
assert mul(mul(ds[2],ds[4]),ds[5])==k(23*49*1119169)
print('EXACT RADICAL masks',radical,'; squareclass basis 573 and 23*1119169.')
data={'basis':[ser(d) for d in ds],'conics':[[ser(x) for x in row] for row in conics],
      'primitive_forms':[[ser(x) for x in row] for row in forms],
      'bezout':[[ser(x) for x in row] for row in bezouts],
      'contents':[ser(x) for x in contents],'local_rows':rows,'matrix':matrix,'rank':rank,'radical':radical}
(BASE/'harmonic_prym_isogeny_pairing_certificate_data.json').write_text(json.dumps(data,indent=2)+'\n')
