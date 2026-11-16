"""Literal F3 local coboundary equations in the norm-torus dual module.

J_N^D = F3[X]/((X-1)^(N-1)), N=3^n.  The terminal line
(X-1)^(N-2) is the cyclotomic character.  Test i*kappa(649).
"""
from math import comb

def mul(a,b,L):
    c=[0]*L
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:L-i]):
                c[i+j]=(c[i+j]+x*y)%3
    return c

def matrix(q,L):
    z=[comb(q,i)%3 if 1<=i<=q else 0 for i in range(L)]
    columns=[]
    v=[1]+[0]*(L-1)
    for j in range(L):
        columns.append(v)
        v=mul(v,z,L)
    return [list(row) for row in zip(*columns)]

def solve(A,b):
    R=[[(x%3) for x in a]+[v%3] for a,v in zip(A,b)]
    n=len(A[0]); k=0; piv=[]
    for j in range(n):
        t=next((i for i in range(k,len(R)) if R[i][j]),None)
        if t is None: continue
        R[k],R[t]=R[t],R[k]
        u=pow(R[k][j],-1,3);R[k]=[(x*u)%3 for x in R[k]]
        for i in range(len(R)):
            if i!=k and R[i][j]:
                u=R[i][j];R[i]=[(x-u*y)%3 for x,y in zip(R[i],R[k])]
        piv.append(j);k+=1
    if any(not any(r[:n]) and r[n] for r in R):return None
    x=[0]*n
    for i,j in enumerate(piv):x[j]=R[i][n]
    return x

checks=0
for n in range(1,6):
    N=3**n;L=N-1
    for q in (11,59):
        a=[comb(24,i)%3 if i<=24 else 0 for i in range(L)]
        T=[[a[i-j] if i>=j else 0 for j in range(L)] for i in range(L)]
        S=matrix(q,L)
        for i in range(L):T[i][i]=(T[i][i]-1)%3;S[i][i]=(S[i][i]-1)%3
        e=[0]*L;e[N-2]=1
        w=solve(T+S,e+[0]*L)
        assert w is None
        assert pow(q,2*3**(n-1),N)==1
        assert pow(q,3**(n-1),N)!=1
        if n>1:
            assert pow(q,2*3**(n-2),N)!=1
        # In the X-basis the terminal line is -i modulo constants.
        coeff=[((-1)**(N-2-i)*comb(N-2,i))%3 if i<=N-2 else 0
               for i in range(N)]
        assert len({(coeff[i]+i)%3 for i in range(N)})==1
        checks+=1
        print(f'n={n}, q={q}: local coboundary={w is not None}',
              'w='+str({i:x for i,x in enumerate(w or []) if x}))
        if w is not None:
            assert all(sum(a*x for a,x in zip(row,w))%3==v
                       for row,v in zip(T+S,e+[0]*L))
print(f'PASS: {checks} literal local coboundary systems have no solution;'
      ' terminal-line and primitive-Frobenius identities checked')
