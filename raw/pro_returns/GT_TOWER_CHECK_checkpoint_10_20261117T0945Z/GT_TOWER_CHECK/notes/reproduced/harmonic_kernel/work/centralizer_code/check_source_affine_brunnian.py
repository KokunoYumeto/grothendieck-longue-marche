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
