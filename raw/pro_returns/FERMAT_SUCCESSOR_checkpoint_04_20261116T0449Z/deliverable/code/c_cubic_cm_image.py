from itertools import product

def mul(x,y,m):
    a,b=x;c,d=y
    return ((a*c-b*d)%m,(a*d+b*c-b*d)%m)
def conj(x,m):a,b=x;return ((a-b)%m,(-b)%m)
def norm(x,m):a,b=x;return (a*a-a*b+b*b)%m

gens=[(-1,2),(-3,-2),(3,4),(-1,-4)]
mod=8
H={(1,0)}
while True:
    K=H|{mul(x,g,mod) for x in H for g in gens}
    if K==H:break
    H=K
U={(a,b) for a,b in product(range(mod),repeat=2) if a%2==1 and b%2==0}
assert H==U and len(H)==16
print('Frobenius scalars generate all',len(H),'elements of (1+2O)/(1+8O).')
for p in [7,13]:
    count=1+sum(1 for x,y in product(range(p),repeat=2) if (y*y-x*x*x-1)%p==0)
    print('p=',p,'point count=',count,'trace=',p+1-count)
    roots=gens[:2] if p==7 else gens[2:]
    for a,b in roots:
        assert a*a-a*b+b*b==p
        assert 2*a-b==p+1-count

# a=1-2*zeta^2=3+2*zeta, eta=a/conj(a)=(-3-8*zeta^2)/7=(5+8*zeta)/7
for m in [4,16,256]:
    eta=(5*pow(7,-1,m)%m,8*pow(7,-1,m)%m)
    assert norm(eta,m)==1
    print('eta mod',m,'=',eta,'norm=',norm(eta,m))
assert ((5*pow(7,-1,4))%4,(8*pow(7,-1,4))%4)==(3,0)
print('eta mod 4 = -1; all exact checks passed.')
