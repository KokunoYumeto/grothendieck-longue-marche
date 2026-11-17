"""Exact S4 certificate for C.34; rightmost permutation acts first."""
from collections import deque

def cycle(*c):
    a=list(range(1,5))
    for x,y in zip(c,c[1:]+c[:1]):a[x-1]=y
    return tuple(a)
def mul(a,b):return tuple(a[v-1] for v in b)
def power(a,n):
    z=(1,2,3,4)
    for _ in range(n):z=mul(z,a)
    return z

def order(a):
    for n in range(1,25):
        if power(a,n)==(1,2,3,4):return n
    raise AssertionError

x=cycle(2,3,4);y=cycle(1,2,3,4);xy=mul(x,y);z=power(xy,3)
assert (order(x),order(y),order(xy))==(3,4,4)
# mu_2=-1, mu_odd=1 implies mu=7 mod24, m=3 mod12.
mu=7;m=3
hexagon=mul(mul(power(x,m),power(z,m)),power(y,m))
assert hexagon==x and hexagon!=(1,2,3,4)
left=mul(power(x,mu),power(y,mu));right=power(xy,mu)
assert (order(left),order(right))==(2,4)
seen={(1,2,3,4)};queue=deque(seen)
while queue:
    a=queue.popleft()
    for g in [x,y]:
        b=mul(a,g)
        if b not in seen:seen.add(b);queue.append(b)
assert len(seen)==24
print('Convention: rightmost permutation acts first; tuples are one-line images.')
print('x=',x,'y=',y,'xy=',xy)
print('Orders x,y,xy:',order(x),order(y),order(xy))
print('Generated subgroup order:',len(seen))
print('Mixed root mu=7 mod24; m=3 mod12.')
print('Full hexagon image x^m z^m y^m =',hexagon,'= x != identity.')
print('Peripheral comparison orders:',order(left),order(right),'(therefore not conjugate).')
print('Scope: refutes the specified mixed root only; global roots +1 and -1 work for f=1.')
