"""Exact integer check for the angle-convention qualification on scan 015."""
from pathlib import Path
import json

root=Path(__file__).resolve().parents[1]
v=[(0,1),(1,1),(1,0),(2,0),(2,1),(3,1),(3,2),(2,2),(2,3),(1,3),(1,2),(0,2)]
n=len(v)
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def orient(a,b,c):return cross(sub(b,a),sub(c,a))
def between(a,b,c):return orient(a,b,c)==0 and all(min(a[k],b[k])<=c[k]<=max(a[k],b[k]) for k in (0,1))
def meet(a,b,c,d):
    u,w,x,y=orient(a,b,c),orient(a,b,d),orient(c,d,a),orient(c,d,b)
    if u*w<0 and x*y<0:return True
    return (u==0 and between(a,b,c)) or (w==0 and between(a,b,d)) or (x==0 and between(c,d,a)) or (y==0 and between(c,d,b))
e=[sub(v[(j+1)%n],v[j]) for j in range(n)]
lengths=[dot(x,x) for x in e]
dots=[dot(e[j],e[(j+1)%n]) for j in range(n)]
turns=[cross(e[j],e[(j+1)%n]) for j in range(n)]
pairs=[(i,j) for i in range(n) for j in range(i+1,n) if j!=i+1 and (i,j)!=(0,n-1)]
intersections=[(i,j) for i,j in pairs if meet(v[i],v[(i+1)%n],v[j],v[(j+1)%n])]
area2=sum(cross(v[j],v[(j+1)%n]) for j in range(n))
assert len(set(v))==12 and lengths==[1]*12 and dots==[0]*12
assert not intersections and len(pairs)==54
assert sorted(turns)==[-1]*4+[1]*8 and area2==10
result=dict(statement='A simple 12-gon with equal sides and equal smaller angles, but unequal interior angles',vertices=v,edge_vectors=e,squared_edge_lengths=lengths,consecutive_edge_dots=dots,turn_determinants=turns,checked_nonadjacent_edge_pairs=pairs,intersections=intersections,twice_signed_area=area2,qualification='All smaller incident angles are pi/2; interior angles include pi/2 and 3pi/2. This is excluded when the manuscript uses ordinary polygon interior angles. It is not a star polygon or a counterexample under that usual convention.')
(root/'decisions/scan015_finite_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'vertices':12,'unit_edges':12,'right_smaller_angles':12,'nonadjacent_pairs_checked':54,'intersections':0,'area':5}))
