"""Coefficient tau(13) from the product on scan 45, using integer arithmetic."""
N=12
sigma1=[0]*(N+1)
for d in range(1,N+1):
    for k in range(d,N+1,d):sigma1[k]+=d
f24=[1]+[0]*N
for n in range(1,N+1):
    numerator=-24*sum(sigma1[k]*f24[n-k] for k in range(1,n+1))
    assert numerator%n==0
    f24[n]=numerator//n
print({'tau(13)':f24[12],'tau(13)_mod13':f24[12]%13})
