"""Literal F_53[zeta] residues of the certified first positional units."""
import json
from pathlib import Path
P=53
def add(a,b):return ((a[0]+b[0])%P,(a[1]+b[1])%P)
def mul(a,b):
    return ((a[0]*b[0]-a[1]*b[1])%P,(a[0]*b[1]+a[1]*b[0]-a[1]*b[1])%P)
def power(a,n):
    r=(1,0)
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n//=2
    return r
z=(0,1)
r=(-7%P,-32%P)
c=power(r,(P*P-1)//3)
assert c in [(1,0),z,power(z,2)]
res={"field":"F53[z]/(z^2+z+1)","unit_residue":r,"cubic_character":[(1,0),z,power(z,2)].index(c),"ninth_power":power(r,(P*P-1)//9),"twenty_seventh_power":power(r,(P*P-1)//27),"status":"PASS"}
print(json.dumps(res,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n')
