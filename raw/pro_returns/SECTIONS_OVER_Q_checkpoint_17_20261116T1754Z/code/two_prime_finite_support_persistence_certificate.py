"""Exact cyclotomic residue-degree checks for A153."""
def primes(bound):
    flags=[True]*(bound+1)
    flags[:2]=[False,False]
    for p in range(2,bound+1):
        if flags[p]:
            yield p
            for k in range(p*p,bound+1,p):flags[k]=False

def v3(a):
    v=0
    while a%3==0:a//=3;v+=1
    return v

checks=0
for p in primes(2000):
    if p==3:continue
    s=v3(p*p-1)
    f0=1 if p%3==1 else 2
    for n in range(1,s+6):
        expected=f0*3**max(0,n-s)
        mod=3**n
        assert pow(p,expected,mod)==1
        for ell in (2,3):
            if expected%ell==0:
                assert pow(p,expected//ell,mod)!=1
        if n>s:assert (expected//f0)%3==0
        checks+=1
print(f'PASS: {checks} exact residue orders at 302 primes other than three')
print('For n>v3(p^2-1), the relative residue degree over Q(mu3) is divisible by three.')
print('No numerical class-group or target-obstruction assertion is made.')
