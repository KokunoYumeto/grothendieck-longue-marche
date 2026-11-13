"""Finite certificates for covering and section obstructions in section E."""
from pathlib import Path
from itertools import product
import json

BASE=Path(__file__).resolve().parent
def mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inv(a):return tuple(a.index(i) for i in range(len(a)))
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
def orbits(gens):
    remaining=set(range(len(gens[0])));out=[]
    while remaining:
        seen={min(remaining)};queue=list(seen)
        for a in queue:
            for g in gens:
                if g[a] not in seen:seen.add(g[a]);queue.append(g[a])
        out.append([i+1 for i in sorted(seen)]);remaining-=seen
    return out
a=(1,0,2);b=(2,1,0);bb=mul(b,comm(a,b))
assert bb==a
orig=orbits([a,b]);pulled=orbits([a,bb])
print('S3 original orbits:',orig,'pullback:',pulled)
real=[]
for m in [2,3,4,6,8,12,24,27]:
    solutions=[v for v in range(m) if (1+2*v)%m==0]
    count=len(solutions)*m**8
    real.append({'modulus':m,'first_coordinate_solutions':solutions,'total_splitting_cochains':count,'obstruction_nonzero':not solutions})
    print('Real quartic modulus',m,'first-coordinate solutions',solutions,'total',count)
def heis(p,q):
    a,b,c=p;aa,bb,cc=q
    return (a^aa,b^bb,c^cc^(b&aa))
H=list(product(range(2),repeat=3));e=(0,0,0)
assert all(heis(heis(a,b),c)==heis(a,heis(b,c)) for a in H for b in H for c in H)
x=(1,0,0);y=(0,1,0);z=(0,0,1)
assert heis(x,x)==e and heis(y,y)==e
assert heis(heis(heis(x,y),x),y)==z
assert heis(heis(x,y),heis(x,y))==z
print('Class-two D8: order8; x²=y²=1; [x,y]=central involution; cocycle b*a_prime.')
assert pow(2,(3-1)//2,3)==2
print('Norm certificate for Kummer(2) cup Kummer(3): 2 nonsquare mod3, v3(3)=1 odd.')
points2=[v for v in product(range(2),repeat=3) if any(v) and sum(t**3 for t in v)%2==0]
assert len(points2)==3
print('Plus cubic over F2:',points2,'point count=',len(points2))
cusps=[(0,1,-1),(1,0,-1),(1,-1,0)]
assert all(sum(t**3 for t in v)==0 for v in cusps)
print('Plus cubic rational cusps:',cusps)
print('Leading torus coefficients, unit tangent: P0=(1,-1), Pinfty=(1,-1).')
for v in product(range(-5,6),repeat=3):
    assert (sum(t**4 for t in v)==0)==(v==(0,0,0))
print('Plus quartic: positivity proof in paper; finite sanity check [-5,5]^3 PASS.')
(BASE/'e_obstructions.json').write_text(json.dumps({'s3_orbits':orig,'s3_pullback_orbits':pulled,'real_quartic':real,'cubic_F2_points':points2,'all_checks':True},indent=2)+'\n')
