from pathlib import Path
import json,math

ROOT=Path('/workspace/scratch/f28c4f52d3ec'); PAGE='148_scan072'; OUT=ROOT/'proposed'
model=json.loads((OUT/f'{PAGE}_parts.json').read_text())
points=model['left_vertices']; edges=model['left_edges']
adj={p:[] for p in points}
for edge in edges:
    a,b=edge['a'],edge['b']; adj[a].append(b); adj[b].append(a)
for a in adj:
    x,y=points[a]; adj[a].sort(key=lambda b:math.atan2(points[b][1]-y,points[b][0]-x))
seen=set(); faces=[]
for start in [(a,b) for a in adj for b in adj[a]]:
    if start in seen: continue
    a,b=start; face=[]
    while (a,b) not in seen:
        seen.add((a,b)); face.append(a); order=adj[b]
        a,b=b,order[(order.index(a)-1)%len(order)]
    assert (a,b)==start
    faces.append(face)
outer=max(faces,key=len); inner=[f for f in faces if f is not outer]
assert len(seen)==46 and len(outer)==7 and len(inner)==13
assert all(len(f)==3 for f in inner)
assert len(points)-len(edges)+len(faces)==2
left=dict(vertices=11,distinct_finite_endpoint_joins=23,physical_additional_trace='c--f',
    rays=len(model['left_rays']),outer_face=outer,bounded_faces=inner,bounded_face_count=13,
    euler_V_minus_E_plus_F=2,
    scope='The simple endpoint-incidence model counts the two visible c--f pencil traces as one distinct join. Both physical traces are nevertheless drawn; the computation does not identify the uncertain isolated numeral.')

rpoints=model['right_vertices']; redges=model['right_edges']
degree={v:0 for v in rpoints}; neighbours={v:set() for v in rpoints}
for edge in redges:
    a,b=edge['a'],edge['b']; degree[a]+=1; degree[b]+=1
    neighbours[a].add(b); neighbours[b].add(a)
degree['h']+=2
for ray in model['right_rays']: degree[ray['a']]+=1
visited={'a'}; pending=['a']
while pending:
    a=pending.pop()
    for b in neighbours[a]-visited: visited.add(b); pending.append(b)
assert len(visited)==8 and all(x==3 for x in degree.values())
assert len(redges)+1==9 and len(model['right_rays'])==6
right=dict(vertices=8,finite_edges_including_loop=9,rays=6,total_incidence_degrees=degree,
    connected_finite_core=True,finite_core_first_betti_number=9-8+1,
    visible_numeric_annotations=len(model['right_labels']),
    scope='Counts the one loop twice in degree and each exterior ray once. Checks the visible graph only; no compatibility rule for the written numbers is assumed.')
result=dict(page=PAGE,left=left,right=right,tex_compiled=False)
(OUT/f'{PAGE}_incidence_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
