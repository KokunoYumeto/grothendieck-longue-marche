"""Finite exact coefficients from the formula on scan 43; no external tables."""
import json,sys

def convolution(a,b,N):
    out=[0]*(N+1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:N+1-i]):
                out[i+j]+=x*y
    return out

def coefficients(max_index):
    N=max_index+1
    sigma1=[0]*(N+1);sigma3=[0]*(N+1)
    for d in range(1,N+1):
        for n in range(d,N+1,d):
            sigma1[n]+=d;sigma3[n]+=d**3
    # Logarithmic derivative of product (1-x^k)^(-24).
    reciprocal=[0]*(N+1);reciprocal[0]=1
    for n in range(1,N+1):
        numerator=24*sum(sigma1[k]*reciprocal[n-k] for k in range(1,n+1))
        assert numerator%n==0
        reciprocal[n]=numerator//n
    e4=[1]+[240*sigma3[n] for n in range(1,N+1)]
    numerator=convolution(convolution(e4,e4,N),e4,N)
    quotient=convolution(numerator,reciprocal,N)
    c={n:quotient[n+1] for n in range(-1,max_index+1)}
    c[0]-=744
    return c

if __name__=='__main__':
    indexes=[int(s) for s in sys.argv[1:]] or [0,13,91]
    c=coefficients(max(indexes))
    print(json.dumps({n:{'value':c[n],'mod13':c[n]%13} for n in indexes},indent=2))
