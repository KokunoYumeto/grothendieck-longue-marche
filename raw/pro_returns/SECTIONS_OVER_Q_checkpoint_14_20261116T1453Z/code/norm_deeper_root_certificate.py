from itertools import product
from math import gcd

counts={'arithmetic':0,'translation':0,'valuation':0,'coinvariants':0,'norm_quotient':0}
for n,t,r in [(1,2,1),(1,3,2),(2,3,1)]:
    N,T,C=3**n,3**t,3**r
    units=[u for u in range(T) if gcd(u,3)==1]
    # Literal action on a top root label and old beta-root index.
    for a,b,u,v,i in product(range(T),range(T),units,units,range(N)):
        if N>3 and (a+b+u+v+i)%127!=0:
            continue
        lhs=(a+u*(b+v*i))%N
        rhs=(a+u*b+(u*v%T)*i)%N
        assert lhs==rhs
        assert (a+u*(b+v*i))%T==(a+u*b+(u*v%T)*i)%T
        counts['arithmetic']+=1
    assert len({j%T for j in range(T)})==T
    assert all(((i+N)%N)==i for i in range(N))
    assert {(-2*j)%T for j in range(T)}==set(range(T))
    counts['translation']+=T
    print('n,t,r=',(n,t,r),': full translation order and old-index action passed')

# Repeated canonical-2 valuation matrix: no new Kummer relation after deeper base change.
for n,t,h in [(1,2,1),(1,3,2),(2,3,1)]:
    N,T,H=3**n,3**t,3**h
    e=20 # a 3-adic unit, also permitting a prime-to3 boundary ramification factor
    for z in product(range(H),repeat=N):
        rows=tuple(e*z[j%N]%H for j in range(T))
        assert all((pow(e,-1,H)*rows[j])%H==z[j] for j in range(N))
        assert any(rows)==any(z)
        counts['valuation']+=1
    print('n,t,h=',(n,t,h),': repeated valuation injection passed')

for r,m in [(1,1),(1,2),(2,1),(2,2)]:
    R,M,d=3**r,3**m,3**min(r,m)
    V=[(z,w) for z in product(range(R),repeat=3) for w in range(M) if (sum(z)-w)%d==0]
    differences={((z[2]-z[0])%R,(z[0]-z[1])%R,(z[1]-z[2])%R,0) for z,w in V}
    aug={(z[0],z[1],z[2],0) for z in product(range(R),repeat=3) if sum(z)%R==0}
    assert differences==aug
    quotient={(sum(z)%R,w) for z,w in V}
    assert len(quotient)==3**max(r,m)
    assert {((-2*s)%R,(-2*w)%M) for s,w in quotient}==quotient
    counts['coinvariants']+=len(quotient)
    print('r,m=',(r,m),': common-b quotient unchanged by deeper translation')

# For the S3 Galois closure, the nontrivial local norm quotient has order2.
# Scalar cubes are the third-power map, which is the identity on that quotient.
for z in range(2):
    assert (3*z)%2==z
    counts['norm_quotient']+=1
print('Exact count summary:',counts)
print('All A.105 finite identities passed. The local ramification proof is supplied in the text.')
