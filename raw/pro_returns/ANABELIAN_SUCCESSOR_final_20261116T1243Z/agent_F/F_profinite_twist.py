"""Finite projections of an explicitly nonintegral profinite integer.
Infinite nonintegrality is proved in the accompanying text, not inferred here.
"""
from math import gcd,lcm

def zmod(n):
    two=1
    odd=n
    while odd%2==0:
        two*=2
        odd//=2
    if odd==1:return 0
    return (two*pow(two,-1,odd))%n

for n in range(1,121):
    z=zmod(n)
    two=n & -n
    odd=n//two
    assert z%two==0
    assert odd==1 or z%odd==1
    for d in range(1,n+1):
        if n%d==0:assert z%d==zmod(d)
print('Compatibility checked for every divisor pair d|n with 1<=n<=120.')
for n in [2,3,4,5,6,8,12,24,30,60,120,720,5040]:
    print('n=%d, z mod n=%d'%(n,zmod(n)))
print('Infinite proof: z_2=0, z_l=1 for every odd prime l.')
print('If z were an integer, z_2=0 would force z=0; z_3=1 excludes this.')
print('Finite checks alone do not prove any topos nonalgebraicity statement.')
