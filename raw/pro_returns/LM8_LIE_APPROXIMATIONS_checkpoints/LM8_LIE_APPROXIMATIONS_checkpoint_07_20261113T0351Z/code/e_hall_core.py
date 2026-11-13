"""Integral Magnus series for standard Lyndon group commutators."""
from functools import cache
from itertools import product

def plus(a,b,k=1):
    c=dict(a)
    for w,v in b.items():
        c[w]=c.get(w,0)+k*v
        if not c[w]:del c[w]
    return c

def mul(a,b,n):
    c={}
    for u,x in a.items():
        for v,y in b.items():
            if len(u)+len(v)<=n:
                w=u+v;c[w]=c.get(w,0)+x*y
    return {w:v for w,v in c.items() if v}

def invdev(a,n):
    ans={():1};t={():1}
    for _ in range(n+1):
        t=mul(t,a,n)
        if not t:break
        t={w:-v for w,v in t.items()};ans=plus(ans,t)
    return ans

@cache
def islyndon(w):return all(w<w[j:] for j in range(1,len(w)))

@cache
def lyndon(n):return tuple(w for w in product((0,1),repeat=n) if islyndon(w))

@cache
def ev(w,mode,n):
    if len(w)>n:return {}
    if len(w)==1:
        letter=((0,1),(1,0),(2,0),(1,2))[mode][w[0]]
        if letter<2:return {(letter,):1}
        return {(1,)*i+(0,)*j:(-1)**(i+j)
                for i in range(n+1) for j in range(n+1-i) if i+j}
    k=next(k for k in range(1,len(w)) if islyndon(w[k:]))
    u,v=w[:k],w[k:]
    a=ev(u,mode,n-len(v));b=ev(v,mode,n-len(u))
    d=plus(mul(a,b,n),mul(b,a,n),-1)
    q=n-len(w)
    return mul(mul(d,invdev(a,q),n),invdev(b,q),n)

def defects(w,n):
    v=ev(w,0,n)
    return plus(v,ev(w,1,n)),plus(plus(v,ev(w,2,n)),ev(w,3,n))

def label(w):return ''.join('x' if i==0 else 'y' for i in w)
def word(s):return tuple(0 if i=='x' else 1 for i in s)
Q={word(w):v for w,v in {
    'xxxyxyy':3,'xxxyyxy':3,'xxyxyxy':1,
    'xxyxyyy':-3,'xxyyxyy':-3,'xxyyyxy':-3,'xyxyxyy':-1}.items()}
