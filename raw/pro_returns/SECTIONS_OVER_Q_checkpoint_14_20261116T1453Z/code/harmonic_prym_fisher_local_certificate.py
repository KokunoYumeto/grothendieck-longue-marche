"""Exact local evaluation of the retained Fisher three-cover formula.

K = Q(sqrt(2)); all field arithmetic and local witnesses use fractions.
Sympy is used only to parse retained Magma expressions and factor rational
norms; the factors are multiplied back and their primality is checked here.
The full 2-Selmer upper bound is supplied independently by the six-class
isogeny-pairing certificate; no software Selmer-group order is used here.
"""
from fractions import Fraction as F
from pathlib import Path
import itertools, json, math, re
import sympy as sp

BASE=Path(__file__).resolve().parent
ZERO=(F(0),F(0)); ONE=(F(1),F(0)); T=(F(0),F(1))
def k(x): return x if isinstance(x,tuple) else (F(x),F(0))
def add(x,y): x,y=k(x),k(y); return (x[0]+y[0],x[1]+y[1])
def neg(x): x=k(x); return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    x,y=k(x),k(y)
    return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def norm(x): x=k(x); return x[0]*x[0]-2*x[1]*x[1]
def inv(x): x=k(x); n=norm(x); assert n; return (x[0]/n,-x[1]/n)
def div(x,y): return mul(x,inv(y))
def power(x,n):
    if n<0:return power(inv(x),-n)
    z=ONE
    while n:
        if n&1:z=mul(z,x)
        x=mul(x,x);n//=2
    return z
def integral(x): return all(a.denominator==1 for a in x)
def ser(x): return [str(a) for a in x]
def sign(x,embedding=1):
    a,b=x; b*=embedding
    if not b:return (a>0)-(a<0)
    if a>=0 and b>=0:return 1
    if a<=0 and b<=0:return -1
    s=(a*a>2*b*b)-(a*a<2*b*b)
    return s if a>0 else -s
def polyval(cs,x):
    r=ZERO
    for a in reversed(cs):r=add(mul(r,x),a)
    return r

raw=(BASE/'harmonic_prym_fisher_small_magma_output.txt').read_text()
raw=re.sub(r'\\\s*\n\s*','',raw)
symt=sp.Symbol('t')
def parse_expr(text):
    e=sp.expand(sp.sympify(text)); a=e.coeff(symt,0);b=e.coeff(symt,1)
    assert sp.expand(e-a-b*symt)==0
    return (F(str(a)),F(str(b)))
def block(label,end,listmode=True):
    s=re.search(re.escape(label)+r' (.*?)\n'+re.escape(end),raw,re.S).group(1).strip()
    if listmode:
        assert s[0]=='[' and s[-1]==']'
        return [parse_expr(v) for v in s[1:-1].split(',')]
    return parse_expr(s)
gamma=block('SMALL COORDINATE GAMMA','HILBERT CHARACTER')
binary_gamma=block('BINARY GAMMA','SMALL COORDINATE GAMMA')
char=block('HILBERT CHARACTER','TRIPLE SQUARE ROOT',False)
mroot=block('TRIPLE SQUARE ROOT','SECOND QUARTIC')
g2=block('SECOND QUARTIC','THIRD QUARTIC')
g3=block('THIRD QUARTIC','SECOND SCALE')
M=7*13*23*139*1119169; r=1119169
b=mul(1146*M*M,power(add(1,T),2)); I=mul(-48,b)
small=[k(r),ZERO,ZERO,ZERO,div(mul(-4,b),r)]
g1=[k(r),k(4*r),k(6*r),k(4*r),sub(r,div(mul(4,b),r))]
def invariants(g):
    e,d,c,bb,a=g
    ii=add(sub(mul(12,mul(a,e)),mul(3,mul(bb,d))),mul(c,c))
    jj=sub(add(add(mul(72,mul(mul(a,c),e)),mul(9,mul(mul(bb,c),d))),mul(-2,power(c,3))),add(mul(27,mul(a,power(d,2))),mul(27,mul(power(bb,2),e))))
    return ii,jj
assert all(invariants(g)==(I,ZERO) for g in [g1,g2,g3])
# Cubic algebra K[phi]/(phi^3-3I phi), with an actual printed modulus.
def cmul(x,y):
    cs=[ZERO]*5
    for i,a in enumerate(x):
        for j,bb in enumerate(y):cs[i+j]=add(cs[i+j],mul(a,bb))
    cs[2]=add(cs[2],mul(mul(3,I),cs[4]))
    cs[1]=add(cs[1],mul(mul(3,I),cs[3]))
    return cs[:3]
def cadd(x,y):return [add(a,bb) for a,bb in zip(x,y)]
def cscale(c,x):return [mul(c,a) for a in x]
def cinv(x):
    cols=[cmul(x,[ONE if j==i else ZERO for j in range(3)]) for i in range(3)]
    mat=[[cols[j][i] for j in range(3)]+[ONE if i==0 else ZERO] for i in range(3)]
    for j in range(3):
        piv=next(i for i in range(j,3) if mat[i][j]!=ZERO)
        mat[j],mat[piv]=mat[piv],mat[j]
        u=inv(mat[j][j]);mat[j]=[mul(u,z) for z in mat[j]]
        for i in range(3):
            if i==j:continue
            q=mat[i][j];mat[i]=[sub(z,mul(q,w)) for z,w in zip(mat[i],mat[j])]
    return [mat[i][3] for i in range(3)]
def zinv(g):
    e,d,c,bb,a=g
    return [div(sub(mul(3,power(bb,2)),mul(8,mul(a,c))),3),div(mul(4,a),3),ZERO]
zs=[zinv(g) for g in [g1,g2,g3]]
assert cmul(mroot,mroot)==cmul(cmul(zs[0],zs[1]),zs[2])
e,d,c,bb,a=g1
G1=[div(mul(4,sub(mul(bb,c),mul(6,mul(a,d)))),3),div(mul(4,bb),3),ZERO]
G2=[div(mul(2,sub(sub(mul(2,power(c,2)),mul(24,mul(a,e))),mul(3,mul(bb,d)))),3),div(mul(4,c),3),ZERO]
Hs=[zs[0],cscale(F(1,2),G1),cadd(cscale(F(1,6),G2),[mul(F(2,9),I),ZERO,k(F(-2,9))])]
fact=cmul(cmul(zs[1],zs[2]),cinv(mroot))
assert binary_gamma==[cmul(fact,h)[2] for h in Hs]
assert gamma==[binary_gamma[2],sub(binary_gamma[1],mul(2,binary_gamma[2])),add(sub(binary_gamma[0],binary_gamma[1]),binary_gamma[2])]
assert char==g2[4]

# Primitive integral quadratic: exact Bezout coefficients show that no
# finite prime divides all its coefficients.  The removed factor is global,
# so global Hilbert reciprocity leaves the product of local symbols unchanged.
def nearest(q):return (q.numerator*2+q.denominator)//(2*q.denominator)
def egcd(x,y):
    oldr,rr=x,y; olds,ss=ONE,ZERO; oldt,tt=ZERO,ONE
    while rr!=ZERO:
        q=div(oldr,rr); q=(F(nearest(q[0])),F(nearest(q[1])))
        nr=sub(oldr,mul(q,rr))
        assert abs(norm(nr))<abs(norm(rr))
        oldr,rr=rr,nr;olds,ss=ss,sub(olds,mul(q,ss));oldt,tt=tt,sub(oldt,mul(q,tt))
    return oldr,olds,oldt
D=math.lcm(*(v.denominator for z in gamma for v in z))
ints=[mul(D,z) for z in gamma]; assert all(integral(z) for z in ints)
gg=ZERO;bez=[ZERO]*3
for i,a in enumerate(ints):
    ng,s,t=egcd(gg,a);bez=[mul(s,z) for z in bez];bez[i]=add(bez[i],t);gg=ng
prim=[div(z,gg) for z in ints];assert all(integral(z) for z in prim)
assert all(integral(z) for z in bez)
v=ZERO
for z,c in zip(bez,prim):v=add(v,mul(z,c))
assert v==ONE
print('Exact Fisher invariant, square-root, quadratic and coordinate identities: PASS.')
print('Primitive quadratic coefficients:',[ser(z) for z in prim],flush=True)

def vp(n,p):
    if not n:return 10**9
    if isinstance(n,F):return vp(n.numerator,p)-vp(n.denominator,p)
    v=0
    while n%p==0:n//=p;v+=1
    return v
def modq(x,q):return x.numerator*pow(x.denominator,-1,q)%q
units=[(1,0),(1,1),(1,2),(1,3),(3,1),(3,3),(5,0),(5,2)]
reps=[mul(power(T,e),(F(a),F(bb))) for e in [0,1] for a,bb in units]
def unitcanon(a,bb):
    x=(a%8,bb%4);y=((3*a+4*bb)%8,(2*a+3*bb)%4)
    return min(x,y)
unitmap={unitcanon(*u):i for i,u in enumerate(units)}
def local2(x):
    assert x!=ZERO
    v=min(2*vp(x[0],2),2*vp(x[1],2)+1)
    u=div(x,power(T,v))
    assert vp(u[0],2)==0 and vp(u[1],2)>=0
    return 8*(v%2)+unitmap[unitcanon(modq(u[0],8),modq(u[1],4))]
assert [local2(z) for z in reps]==list(range(16))
table=[[local2(mul(x,y)) for y in reps] for x in reps]
def norm_pair(alpha,X,Y):return sub(power(X,2),mul(alpha,power(Y,2)))
normwitnesses={}
for ai,alpha in enumerate(reps):
    if ai==0:continue
    found={0:(ONE,ZERO)}
    candidates=[(F(a),F(bb)) for a in range(8) for bb in range(4)]
    for z in candidates:
        for X,Y in [(ONE,z),(z,ONE)]:
            N=norm_pair(alpha,X,Y)
            if N==ZERO:continue
            ci=local2(N)
            if ci not in found:
                before=list(found.items())
                for ki,(U,V) in before:
                    W=add(mul(X,U),mul(alpha,mul(Y,V)));Z=add(mul(X,V),mul(Y,U))
                    idx=table[ci][ki]
                    assert local2(norm_pair(alpha,W,Z))==idx
                    found[idx]=(W,Z)
            if len(found)==8:break
        if len(found)==8:break
    assert len(found)==8,(ai,len(found))
    normwitnesses[ai]=found
def hilbert2(a,bb):
    ai,bi=local2(a),local2(bb)
    return 1 if ai==0 or bi in normwitnesses[ai] else -1
assert all(hilbert2(x,y)==hilbert2(y,x) for x in reps for y in reps)
assert all(hilbert2(x,neg(x))==1 for x in reps)

def prime(n):
    if n<2:return False
    if n%2==0:return n==2
    return all(n%d for d in range(3,math.isqrt(n)+1,2))
Nchar=norm(char)
fn=sp.factorint(abs(Nchar.numerator));fd=sp.factorint(Nchar.denominator)
fden=sp.factorint(math.lcm(*(v.denominator for v in char)))
assert math.prod(int(p)**int(e) for p,e in fn.items())==abs(Nchar.numerator)
assert math.prod(int(p)**int(e) for p,e in fd.items())==Nchar.denominator
bad={2,3,5,7,13,23,139,191,r}|{int(p) for p in fn}|{int(p) for p in fd}|{int(p) for p in fden}
assert all(prime(p) for p in bad)
def leg(x,p):
    z=pow(x%p,(p-1)//2,p);return 0 if z==0 else (1 if z==1 else -1)
def sqrtmod(n,p):
    rr=sp.sqrt_mod(n,p,all_roots=True);return sorted(int(x) for x in rr)
def root_lift(root,p,N):
    rt=root;mod=p
    for _ in range(1,N):
        e=((2-rt*rt)//mod*pow(2*rt,-1,p))%p
        rt+=e*mod;mod*=p
    assert (rt*rt-2)%mod==0
    return rt
def odd_data(x,p,root):
    D=math.lcm(x[0].denominator,x[1].denominator)
    A=int(x[0]*D);B=int(x[1]*D);vD=vp(D,p)
    if root is None:
        v=min(vp(A,p),vp(B,p))
        aa=A//p**v;bb=B//p**v
        den=D//p**vD;di=pow(den,-1,p)
        aa=aa*di%p;bb=bb*di%p
        return v-vD,leg(aa*aa-2*bb*bb,p)
    N=vp(A*A-2*B*B,p)+1
    rt=root_lift(root,p,N);mod=p**N
    vv=(A+B*rt)%mod;v=vp(vv,p);assert v<N
    unit=(vv//p**v)*pow(D//p**vD,-1,p)%p
    return v-vD,leg(unit,p)
def square_odd(x,p,root):
    if x==ZERO:return True
    v,l=odd_data(x,p,root);return v%2==0 and l==1
def hilbert_odd(a,bb,p,root):
    va,la=odd_data(a,p,root);vb,lb=odd_data(bb,p,root)
    sign0=-1 if root is not None and p%4==3 and va*vb%2 else 1
    return sign0*(la if vb%2 else 1)*(lb if va%2 else 1)

rows=[]
for p in sorted(bad):
    if p==2:
        x=ZERO;fx=polyval(small,x);gx=polyval(prim,x)
        assert local2(fx)==0
        h=hilbert2(char,gx)
        rows.append({'p':2,'root':None,'x':ser(x),'fclass':local2(fx),'gclass':local2(gx),'achar':local2(char),'hilbert':h})
        continue
    roots=sqrtmod(2,p)
    if not roots:roots=[None]
    for root in roots:
        if p==r:
            assert root is not None
            C=div(mul(4,b),r*r)
            def red(x,rt,mod):return (modq(x[0],mod)+modq(x[1],mod)*rt)%mod
            Cp=red(C,root,p)
            xs=sp.nthroot_mod(pow(Cp,-1,p),4,p,all_roots=True)
            assert xs
            x0=min(int(z) for z in xs);mod=p*p;rt=root_lift(root,p,2)
            Cmod=red(C,rt,mod)
            g0=(1-Cmod*pow(x0,4,mod))%mod
            deriv=(-4*Cp*pow(x0,3,p))%p
            e=((p-g0)//p*pow(deriv,-1,p))%p
            x=k(x0+p*e)
        else:
            x=None
            for n in range(1000):
                xx=k(n);fx=polyval(small,xx)
                if fx!=ZERO and square_odd(fx,p,root) and polyval(prim,xx)!=ZERO:
                    x=xx;break
            assert x is not None,(p,root)
        fx=polyval(small,x);gx=polyval(prim,x)
        assert fx!=ZERO and gx!=ZERO and square_odd(fx,p,root)
        h=hilbert_odd(char,gx,p,root)
        rows.append({'p':p,'root':root,'x':ser(x),'f_local_data':odd_data(fx,p,root),'g_local_data':odd_data(gx,p,root),'a_local_data':odd_data(char,p,root),'hilbert':h})
for embedding in [1,-1]:
    assert sign(small[0],embedding)==1
    sa=sign(char,embedding);sg=sign(prim[0],embedding)
    rows.append({'real_embedding':embedding,'a_sign':sa,'g_sign':sg,'x':ser(ZERO),'hilbert':-1 if sa==sg==-1 else 1})
answer=math.prod(z['hilbert'] for z in rows)
print('Dyadic norm subgroups: fifteen complete eight-class sets with literal norm witnesses.')
print('Rational finite support:',sorted(bad))
for row in rows:print(row)
print('Fisher Cassels--Tate product:',answer)
data={'gamma_original':[ser(z) for z in gamma],'gamma_primitive':[ser(z) for z in prim],
      'content':ser(div(gg,D)),'bezout':[ser(z) for z in bez],'character':ser(char),
      'norm_factor_numerator':{str(p):int(e) for p,e in fn.items()},'norm_factor_denominator':{str(p):int(e) for p,e in fd.items()},
      'character_component_denominator':{str(p):int(e) for p,e in fden.items()},
      'dyadic_norm_witnesses':{str(ai):{str(ci):[ser(X),ser(Y)] for ci,(X,Y) in fs.items()} for ai,fs in normwitnesses.items()},
      'local_rows':rows,'product':answer}
(BASE/'harmonic_prym_fisher_local_certificate_data.json').write_text(json.dumps(data,indent=2)+'\n')
