from pathlib import Path
import json, math

root=Path('/workspace/scratch/f28c4f52d3ec')
page='148_scan069'
model=json.loads((root/'proposed'/f'{page}_parts.json').read_text())
points=model['vertices']
edges=[tuple(sorted((edge['a'],edge['b']))) for edge in model['edges']]
adj={v:[] for v in points}
for a,b in edges:
    adj[a].append(b); adj[b].append(a)
for a in adj:
    x,y=points[a]
    adj[a].sort(key=lambda b:math.atan2(points[b][1]-y,points[b][0]-x))

# Face walk in the rotation system induced by the manually checked embedding.
seen=set(); faces=[]
for a,b in [(a,b) for a in adj for b in adj[a]]:
    if (a,b) in seen: continue
    start=(a,b); face=[]
    while (a,b) not in seen:
        seen.add((a,b)); face.append(a)
        order=adj[b]
        a,b=b,order[(order.index(a)-1)%len(order)]
    assert (a,b)==start
    faces.append(face)
assert len(seen)==2*len(edges)
boundary=max(faces,key=len)
inner=[face for face in faces if face is not boundary]
assert len(boundary)==10
assert all(len(face)==3 for face in inner)
assert len(inner)==20
assert len(points)-len(edges)+len(faces)==2
assert len(edges)==3*len(points)-len(boundary)-3

# The same face walk without the observed g--h edge leaves one quadrilateral.
without=[face for face in inner if set(face) in [set('egh'),set('ghi')]]
assert len(without)==2
result={
 'page':page,'type':'computation or formal certificate',
 'scope':'Combinatorics of the manually transcribed finite graph; no assertion about uncertain labels or red-curve topology.',
 'vertices':len(points),'finite_edges':len(edges),'exterior_rays':len(model['rays']),
 'vertex_degrees':{a:len(v) for a,v in adj.items()},
 'outer_face':boundary,'bounded_faces':inner,'bounded_face_count':len(inner),
 'every_bounded_face_is_triangular':True,'euler_V_minus_E_plus_F':len(points)-len(edges)+len(faces),
 'disk_edge_formula':f"35 = 3*16 - 10 - 3",
 'added_edge':['g','h'],'adjacent_faces_of_added_edge':without,
 'conclusion':'The observed g--h edge gives 20 bounded triangular faces. Removing it merges e--g--h and g--i--h into the quadrilateral e--g--i--h. The check is consistent with, and did not determine, the source reading.'
}
(root/'proposed'/f'{page}_incidence_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
