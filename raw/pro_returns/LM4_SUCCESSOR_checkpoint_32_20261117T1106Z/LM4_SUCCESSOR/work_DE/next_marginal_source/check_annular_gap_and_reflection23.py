#!/usr/bin/env python3
"""Independent exact cut replay and an explicitly marked disk reflection."""
from pathlib import Path
from fractions import Fraction as Q
import json, hashlib
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes/annular_gap_cone23.json'
D=json.loads(P.read_text())
def inv(w):return tuple(-x for x in reversed(w))
def red(w,cone=0):
    s=[]
    for v in w:
        if abs(v)==cone:v=cone
        if s and (s[-1]==-v or cone and s[-1]==v==cone):s.pop()
        else:s.append(v)
    return tuple(s)
def sub(w,A,cone=0):return red((z for x in w for z in (A[abs(x)] if x>0 else inv(A[-x]))),cone)
def read(poly,points):
    letters=[];cert=[]
    for a,b in zip(poly,poly[1:]):
        dx,dy=b[0]-a[0],b[1]-a[1]; hits=[]
        for j,z in enumerate(points,1):
            for end in (a,b):
                assert end[0]!=z[0] or end[1]>z[1],('cut endpoint',j,end)
            if dx==0:
                assert a[0]!=z[0] or not min(a[1],b[1])<=z[1]<=max(a[1],b[1])
                continue
            u=(z[0]-a[0])/dx
            if 0<=u<=1:
                y=a[1]+u*dy
                assert y!=z[1],('puncture hit',j)
                if 0<u<1 and y<z[1]:hits.append((u,j if dx>0 else -j))
        hits.sort();letters.extend(j for _,j in hits)
        cert.append([j for _,j in hits])
    return red(letters),cert
pts=[tuple(map(Q,z)) for z in D['rational_projected_punctures']]
path=[tuple(map(Q,z)) for z in D['path']]
word,events=read(path,pts)
M=(-6,-5,-4,-3)
assert word==M+(2,)+inv(M)==tuple(D['positive_cone_word'])
assert all(p[1]>Q(1,4) for j,p in enumerate(pts) if j!=1)
assert all(pts[j+1][0]-pts[j][0]>Q(1,100) for j in range(5))
# This dictionary is typed from B112's displayed table, not imported from
# the cone producer or its substitution helper.
A={1:(1,3,2,3,-1),2:(1,3,-2,3,2,3,-1),3:(1,),
   4:(4,5,6,-5,-4),5:(5,),6:(-5,4,5)}
MY=sub(M,A,3);assert MY==(-6,-5,-4,-1)
Pold=(1,3,-2,3);L=red(MY+Pold,3)
assert L==(-6,-5,-4,3,-2,3)
assert sub(word,A,3)==red(L+(3,)+inv(L),3)
# Unrotated lower corridor: Im(w/ROT) has sign Im(w)-.371 Re(w).
for w in [(Q(10),Q(0)),(Q(10),Q(-2)),(Q(-1,1000),Q(-2))]:
    assert w[1]-Q(371,1000)*w[0]<0
# Exact independent reflection calibration in a newly SPECIFIED disk comb.
# The real punctures are 1,...,5, common base (6,0); upper comb, positive
# circles. This is not silently identified with the transported old x basis.
points=[(Q(j),Q(0)) for j in range(1,6)];base=(Q(6),Q(0));eps=Q(1,10)
reflection={};polygons=[]
for j in range(1,6):
    e=(Q(j)-eps,Q(0))
    arc=[base,(Q(6),Q(1)),(Q(j)-eps,Q(1)),e]
    circle=[e,(Q(j)-eps,-eps),(Q(j)+eps,-eps),(Q(j)+eps,eps),(Q(j)-eps,eps),e]
    loop=arc+circle[1:]+list(reversed(arc))[1:]
    assert read(loop,points)[0]==(j,)
    mirrored=[(x,-y) for x,y in loop]
    image=read(mirrored,points)[0]
    suffix=tuple(range(j+1,6));expected=inv(suffix)+(-j,)+suffix
    assert image==expected
    reflection[j]=image
    polygons.append({'j':j,'loop':[[str(v) for v in z] for z in loop],'mirror_word':list(image)})
assert all(sub(reflection[j],reflection)==(j,) for j in range(1,6))
assert sub((1,2,3,4,5),reflection)==(-5,-4,-3,-2,-1)
out={'status':'PASS','input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
 'gap_word':word,'events':events,'M_in_Y':MY,'L_in_Y':L,
 'reflection_basis':'New explicit upper comb at real points1..5, right real basepoint; not asserted equal to old transported x basis.',
 'reflection_images':reflection,'reflection_polygons':polygons,
 'scope':'Actual gap-cone cut replay and exact generic reflection calibration. The actual common K automorphism eta remains geometric/symbolic until a based comparison with this comb is made.'}
Path(__file__).with_name('annular_gap_and_reflection23.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all actual gap polygon segments and literal cone word; independent displayed-table substitution')
print('PASS lower unrotated corridor and exact L=e^-1 d^-1 f^-1 (bar b)^-1')
print('PASS explicit five-puncture reflection, both involution identities and inverse boundary product')
print('SCOPE actual eta retained symbolically; no unstated old-comb basis identification')
