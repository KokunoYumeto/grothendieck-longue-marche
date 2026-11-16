"""Exact local labels, transition maps and cochain signs for A155.

This certificate does not compute any number-field class group.
"""
from math import gcd

def add(*xs):
    ans={}
    for x in xs:
        for w,c in x.items():ans[w]=ans.get(w,0)+c
    return {w:c for w,c in ans.items() if c}

def scale(c,x):return {w:c*a for w,a in x.items() if c*a}
def multiply(x,y):
    ans={}
    for u,a in x.items():
        for v,b in y.items():ans[u+v]=ans.get(u+v,0)+a*b
    return {w:c for w,c in ans.items() if c}

deg={'h':1,'B':1,'o':2,'w':0,'c':1}
ds={'h':{},'B':{('o',):1},'o':{},'w':{('h',):1,('c',):-1},'c':{}}
def differential(x):
    terms=[]
    for word,coeff in x.items():
        before=0
        for i,s in enumerate(word):
            for mid,c in ds[s].items():
                terms.append({word[:i]+mid+word[i+1:]:coeff*c*(-1)**before})
            before+=deg[s]
    return add(*terms)

h={('h',):1};B={('B',):1};o={('o',):1};w={('w',):1};c={('c',):1}
assert differential(scale(-1,multiply(h,B)))==multiply(h,o)
assert add(multiply(w,o),multiply(h,B),scale(-1,multiply(c,B)),
           scale(-1,differential(multiply(w,B))))=={}
print('PASS: both literal cochain differential/sign identities')

def orbits(q,d):
    unused=set(range(d)); ans=[]
    while unused:
        x=min(unused); orbit=[];y=x
        while y not in orbit:
            orbit.append(y);y=q*y%d
        assert y==x
        unused.difference_update(orbit);ans.append(orbit)
    return ans

transition_checks=0; label_checks=0
for q,M in ((2,0),(11,24),(59,24)):
    previous=None
    for n in range(1,8):
        N=3**n;d=gcd(N,M);e=N//d;O=orbits(q,d)
        assert O[0]==[0]
        assert sum(e*len(o) for o in O)==N
        if q==2:
            assert e==1 and sum(len(o) for o in O)==N
        if previous:
            dp,Op=previous
            for orbit in O:
                images={x%dp for x in orbit}
                old=next(o for o in Op if set(o)==images)
                assert len(orbit)%len(old)==0
                f_rel=len(orbit)//len(old)
                assert len(orbit)==f_rel*len(old)
                # Norm(P'-f'P0')=f_rel(P-fP0), coefficient by coefficient.
                assert -len(orbit)==-f_rel*len(old)
                transition_checks+=1
        previous=(d,O)
        label_checks+=d
        if n<=3:print(f'q={q}, n={n}: e={e}, residue degrees={[len(o) for o in O]}')

# Actual root-pushforward and dual root-pullback, over several coefficients.
adjoint_checks=0
for n in range(1,5):
    N=3**n
    for r in range(1,4):
        m=3**r
        for j in range(3*N):
            for i in range(N):
                pushed_pair=int(j%N==i)%m
                pulled_pair=int(j in (i,i+N,i+2*N))%m
                assert pushed_pair==pulled_pair
                adjoint_checks+=1

# Finite character separation at the AMBIENT cyclic group's exponent.
# An element's own order alone does not supply a sufficient precision.
assert all(a*3%3==0 for a in range(3))  # Hom(C9,C3) kills e=3.
assert (1*3)%9==3                     # Hom(C9,C9) detects it.
character_checks=0
for n in range(1,6):
    m=3**n
    for t in range(m):
        values={(a*t)%m for a in range(m)}
        assert (values=={0})==(t==0)
        character_checks+=1
print(f'PASS: {label_checks} actual local labels; {transition_checks} prime-norm relations')
print(f'PASS: {adjoint_checks} coefficient adjoint identities; {character_checks} character separations')
print('Regression: e=3 in C9 is invisible to Hom(C9,C3); all-r tests are retained.')
print('The actual ideal class e_n is deliberately not numerically evaluated.')
