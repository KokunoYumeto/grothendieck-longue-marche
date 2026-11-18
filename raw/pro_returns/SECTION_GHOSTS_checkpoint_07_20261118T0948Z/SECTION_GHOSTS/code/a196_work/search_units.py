from itertools import product

def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def powr(a,n):
 r=(1,0)
 for _ in range(n):r=mul(r,a)
 return r
def scale(a,n):return a[0]*n,a[1]*n
D=(1,2)
U=[]
for v in product(range(-2,3),repeat=6):
 a,b,c=v[:2],v[2:4],v[4:]
 n=add(add(powr(a,3),mul(powr(b,3),D)),mul(powr(c,3),mul(D,D)))
 n=add(n,scale(mul(mul(mul(a,b),c),D),-3))
 if n[0]**2-n[0]*n[1]+n[1]**2==1:
  if any(v[2:]):U.append((sum(abs(i) for i in v),v,n))
U.sort()
for r in U[:80]:print(r)
print('total',len(U))
