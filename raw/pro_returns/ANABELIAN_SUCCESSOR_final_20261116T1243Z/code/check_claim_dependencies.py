"""Report cycles in the internal claim references for an editorial dependency audit."""
import csv,json
from pathlib import Path
W=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((W/'ANABELIAN_SUCCESSOR_results.csv').open()))
ids={r['id'] for r in rows}
graph={r['id']:[x.strip() for x in r['depends_on'].split(';') if x.strip() in ids] for r in rows}
index={};low={};stack=[];active=set();components=[]
def visit(v):
    index[v]=low[v]=len(index);stack.append(v);active.add(v)
    for w in graph[v]:
        if w not in index:visit(w);low[v]=min(low[v],low[w])
        elif w in active:low[v]=min(low[v],index[w])
    if low[v]==index[v]:
        component=[]
        while True:
            w=stack.pop();active.remove(w);component.append(w)
            if w==v:break
        if len(component)>1:components.append(sorted(component))
for v in graph:
    if v not in index:visit(v)
owner_deps={}
for file in ['agent_criteria/criteria_results.csv','agent_F/F_results.csv']:
    for row in csv.DictReader((W/file).open()):
        owner_deps[row['id']]=row['depends_on']
print(json.dumps({'cycles':components,'cycle_edges':{x:graph[x] for c in components for x in c},'owner_dependencies':owner_deps},indent=2))
