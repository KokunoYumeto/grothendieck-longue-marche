"""Independent exact arithmetic audit of the retained Fisher local data.

Uses only the JSON numbers, not the evaluated code's functions.  This
does not audit the geometric Fisher formula or the Selmer upper bound.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import gcd,isqrt,lcm,prod
import json

base=Path(__file__).resolve().parent
d=json.loads((base/'harmonic_prym_fisher_local_certificate_data.json').read_text())
def read(z):return tuple(Q(x) for x in z)
def plus(x,y):return x[0]+y[0],x[1]+y[1]
def times(x,y):return x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def N(x):return x[0]*x[0]-2*x[1]*x[1]
def inv(x):return x[0]/N(x),-x[1]/N(x)
def pw(x,n):
    if n<0:return pw(inv(x),-n)
    ans=(Q(1),Q(0))
    while n:
        if n&1:ans=times(ans,x)
        x=times(x,x);n//=2
    return ans
def val(x,p):
    x=Q(x)
    if not x:return 10**9
    def f(n):
        c=0
        while n%p==0:n//=p;c+=1
        return c
    return f(x.numerator)-f(x.denominator)
def mod(x,m):return x.numerator*pow(x.denominator,-1,m)%m
def prime(p):return p>=2 and all(p%i for i in range(2,isqrt(p)+1))
def poly(cs,x):
    ans=(Q(0),Q(0))
    for c in reversed(cs):ans=plus(times(ans,x),c)
    return ans

primitive=list(map(read,d['gamma_primitive']))
original=list(map(read,d['gamma_original']))
content=read(d['content']);bez=list(map(read,d['bezout']))
assert original==[times(content,z) for z in primitive]
assert all(x.denominator==1 for z in primitive+bez for x in z)
total=(Q(0),Q(0))
for c,z in zip(bez,primitive):total=plus(total,times(c,z))
assert total==(1,0)
print('PASS: independent primitive-content multiplication and integral Bezout identity')

character=read(d['character'])
nc=N(character)
for key,target in [('norm_factor_numerator',abs(nc.numerator)),
                   ('norm_factor_denominator',nc.denominator),
                   ('character_component_denominator',lcm(*(x.denominator for x in character)))]:
    factors={int(p):e for p,e in d[key].items()}
    assert prod(p**e for p,e in factors.items())==target
    assert all(prime(p) for p in factors)

r=1119169
M=7*13*23*139*r
b=times((Q(1146*M*M),Q(0)),pw((Q(1),Q(1)),2))
small=[(Q(r),Q(0)),(Q(0),Q(0)),(Q(0),Q(0)),(Q(0),Q(0)),
       times((Q(-4,r),Q(0)),b)]
needed={2,3,7,13,23,139,191,r}
for key in ['norm_factor_numerator','norm_factor_denominator','character_component_denominator']:
    needed.update(map(int,d[key]))
listed={row['p'] for row in d['local_rows'] if 'p' in row}
assert needed<=listed
assert all(prime(p) for p in listed)
# Disc(r-4b/r X^4)=-2^14 b^3; all its primes and denominators are listed.
nb=N(b)
for p in (2,3,7,13,23,139,191,r):
    while nb.numerator%p==0:nb/=p
assert abs(nb)==1
# A genuinely omitted finite residue field has at least 17 elements:
# 2,3,5,7,13 are listed; 11 is inert and has residue field of size 121.
assert {2,3,5,7,13}<=listed
assert pow(2,5,11)==10
assert 17+1-2*isqrt(17)-2>6  # The exact weaker lower bound q+1-2(sqrt(q)+1).
print('PASS: complete finite denominator/discriminant support; omitted-field Hasse bound exceeds six')

def quadratic_character(a,b,p):
    # Exponentiate in F_(p^2), independently of the norm-Legendre shortcut.
    def mm(x,y):return ((x[0]*y[0]+2*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    z=(1,0);x=(a%p,b%p);e=(p*p-1)//2
    while e:
        if e&1:z=mm(z,x)
        x=mm(x,x);e//=2
    assert z in ((1,0),(p-1,0))
    return 1 if z==(1,0) else -1

def odd(x,p,root):
    den=lcm(*(a.denominator for a in x))
    aa,bb=(int(a*den) for a in x)
    vd=val(den,p)
    denunit=den//p**vd
    if root is None:
        vn=min(val(aa,p),val(bb,p));aa//=p**vn;bb//=p**vn
        aa=aa*pow(denunit,-1,p)%p;bb=bb*pow(denunit,-1,p)%p
        return vn-vd,quadratic_character(aa,bb,p)
    # Lift a square root independently to precision exceeding both conjugate valuations.
    depth=val(aa*aa-2*bb*bb,p)+3
    rt=root;modulus=p
    for _ in range(1,depth):
        rt+=((-((rt*rt-2)//modulus)*pow(2*rt,-1,p))%p)*modulus
        modulus*=p
    assert (rt*rt-2)%modulus==0
    zz=(aa+bb*rt)%modulus;vn=val(zz,p);assert vn<depth
    un=zz//p**vn*pow(denunit,-1,p)%p
    le=pow(un,(p-1)//2,p);assert le in (1,p-1)
    return vn-vd,(1 if le==1 else -1)

def dyadic_square(x):
    v=min(2*val(x[0],2),2*val(x[1],2)+1)
    assert v%2==0
    u=times(x,pw((Q(0),Q(1)),-v))
    assert val(u[0],2)==0 and val(u[1],2)>=0
    residues=(mod(u[0],8),mod(u[1],4))
    assert residues in ((1,0),(3,2))
    return v,residues

negative=[];finite_count=0
for row in d['local_rows']:
    if 'p' not in row:continue
    p=row['p'];root=row['root'];x=read(row['x'])
    fx=poly(small,x);gx=poly(primitive,x)
    if p==2:
        info=[dyadic_square(v) for v in (fx,character,gx)]
        assert row['hilbert']==1
        print('PASS: dyadic f, character and primitive value are squares:',info)
        finite_count+=1;continue
    vf,lf=odd(fx,p,root);va,la=odd(character,p,root);vg,lg=odd(gx,p,root)
    assert vf%2==0 and lf==1
    assert (vf,lf)==tuple(row['f_local_data'])
    assert (va,la)==tuple(row['a_local_data'])
    assert (vg,lg)==tuple(row['g_local_data'])
    residue_size=p if root is not None else p*p
    hs=(-1 if ((residue_size-1)//2*va*vg)%2 else 1)
    hs*=la**(vg%2)*lg**(va%2)
    assert hs==row['hilbert']
    if hs<0:negative.append((p,root))
    finite_count+=1
assert negative==[(41,17),(139,None),(38709401,15703973)]

def real_sign(x,s):
    a,b=x;b*=s
    if not b:return (a>0)-(a<0)
    if a>=0 and b>=0:return 1
    if a<=0 and b<=0:return -1
    cmp=(a*a>2*b*b)-(a*a<2*b*b)
    return cmp if a>0 else -cmp
for s in (1,-1):
    assert real_sign(small[0],s)==1
    assert real_sign(character,s)==-1
    assert real_sign(primitive[0],s)==1
assert (-1)**len(negative)==d['product']==-1
print(f'PASS: all {finite_count} finite local points and Hilbert symbols independently recomputed')
print('Negative local factors exactly:',negative)
print('PASS: both real places; full retained product = -1')
