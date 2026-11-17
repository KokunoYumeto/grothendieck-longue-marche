"""Exact source A4 word distinguishing the universal six-coordinate kernel."""
import itertools,json
from pathlib import Path
I=(0,1,2,3)
def mul(p,q):return tuple(p[q[i]] for i in range(4))
def inv(p):return tuple(p.index(i) for i in range(4))
def poww(p,n):
    if n<0:return poww(inv(p),-n)
    a=I
    for _ in range(n):a=mul(a,p)
    return a
def comm(a,b):return mul(mul(mul(inv(a),inv(b)),a),b)
s=(1,0,3,2);r=(1,2,0,3)
group={I};front=[I]
while front:
    a=front.pop()
    for b in (s,r):
        c=mul(a,b)
        if c not in group:group.add(c);front.append(c)
assert len(group)==12
x=poww(mul(s,r),-2);y=mul(mul(s,x),s);z=inv(mul(x,y))
w=comm(comm(poww(x,2),poww(y,2)),poww(z,2))
assert w==s
V={I,s,mul(mul(r,s),inv(r)),mul(mul(poww(r,2),s),inv(poww(r,2)))}
assert len(V)==4 and all(poww(v,2)==I for v in V)
rows=[]
for a in sorted(V):
    xx=poww(mul(a,r),-2);yy=mul(mul(a,xx),a);zz=inv(mul(xx,yy))
    ww=comm(comm(poww(xx,2),poww(yy,2)),poww(zz,2))
    assert (ww==I)==(a==I)
    rows.append({'normalized_cocycle_s':list(a),'word_value':list(ww)})
out={'A4_order':len(group),'s':list(s),'r':list(r),'x':list(x),'y':list(y),'z':list(z),'w':list(w),'normalized_cocycle_rows':rows}
root=Path(__file__).resolve().parent
(root/'check_source_affine_brunnian.json').write_text(json.dumps(out,indent=2)+'\n')
print('SOURCE A4 BRUNNIAN CHECK: order12; all four normalized source cocycles checked; w=s; all three nonzero cocycles detect w.')
print(json.dumps(out,indent=2))

# Literal quaternion central extension and the marked-source Ext correction.
MI=(1,0,0,1); MS=(0,2,1,0); MR=(0,2,1,2)
def mm(a,b):return ((a[0]*b[0]+a[1]*b[2])%3,(a[0]*b[1]+a[1]*b[3])%3,(a[2]*b[0]+a[3]*b[2])%3,(a[2]*b[1]+a[3]*b[3])%3)
def mp(a,n):
    z=MI
    for _ in range(n):z=mm(z,a)
    return z
Mneg=mp(MS,2)
assert Mneg==(2,0,0,2) and mp(MS,4)==MI and mp(MR,3)==MI
SL={MI};front=[MI]
while front:
    a=front.pop()
    for b in (MS,MR):
        c=mm(a,b)
        if c not in SL:SL.add(c);front.append(c)
assert len(SL)==24
points=[0,1,2,None]
def mob(a,z):
    num=a[0] if z is None else (a[0]*z+a[1])%3
    den=a[2] if z is None else (a[2]*z+a[3])%3
    return None if den==0 else num*pow(den,-1,3)%3
def permM(a):return tuple(points.index(mob(a,z)) for z in points)
relabel=next(h for h in itertools.permutations(range(4)) if mul(mul(h,permM(MS)),inv(h))==s and mul(mul(h,permM(MR)),inv(h))==r)
def QM(a):return mul(mul(relabel,permM(a)),inv(relabel))
assert all(QM(mm(a,b))==mul(QM(a),QM(b)) for a in SL for b in SL)
Q8={a for a in SL if QM(a) in V}
assert len(Q8)==8 and all(mp(a,2)==Mneg for a in Q8 if a not in (MI,Mneg))
MQJ=mm(mm(MR,MS),mp(MR,2))
commM=mm(mm(mm(mp(MS,3),mp(MQJ,3)),MS),MQJ)
assert commM==Mneg
# In SL2(F3) x C4 modulo <(-I,2)>, (S,1) has order two;
# (S,0), the lift of b, commutes with it.
assert (mp(MS,2),2)==(Mneg,2)
print('QUATERNION SOURCE CHECK: |SL2(F3)|=24; kernel={+I,-I}; V4 preimage Q8; independent lifts have commutator -I; marked source correction (S,1)^2=(-I,2); the b lift (S,0) commutes with corrected source S.')
out['quaternion_check']={'SL2_order':24,'Q8_order':8,'S':list(MS),'R':list(MR),'minus_I':list(Mneg),'P1_relabel':list(relabel),'commutator':list(commM),'corrected_source_square':[list(Mneg),2]}
(root/'check_source_affine_brunnian.json').write_text(json.dumps(out,indent=2)+'\n')
