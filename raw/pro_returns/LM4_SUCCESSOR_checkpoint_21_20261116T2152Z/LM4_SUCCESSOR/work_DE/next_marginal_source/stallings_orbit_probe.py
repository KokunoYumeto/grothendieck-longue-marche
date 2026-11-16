"""Exact bounded Stallings probes of the actual marginal orbit subgroup.

Only membership in the explicitly finite generated subgroups is decided.
No stabilization or equality with the full infinite orbit subgroup is inferred.
"""
from pathlib import Path
import json,itertools,time
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'positive_fiber_data.json').read_text())
F={int(k):tuple(v) for k,v in D['new_fiber_words'].items()}
acts={int(k)+1:{int(i):tuple(w) for i,w in v.items()} for k,v in D['old_actions'].items()}
acts.update({-int(k)-1:{int(i):tuple(w) for i,w in v.items()} for k,v in D['old_inverse_actions'].items()})
def red(w):
    r=[]
    for x in w:
        if r and r[-1]==-x:r.pop()
        else:r.append(x)
    return tuple(r)
def inv(w):return tuple(-x for x in w[::-1])
def mul(*ww):return red(itertools.chain.from_iterable(ww))
def sub(w,A):return mul(*(A[x] if x>0 else inv(A[-x]) for x in w))

class Folded:
    def __init__(self):self.parent=[0];self.adj=[{}]
    def find(self,a):
        p=self.parent
        while p[a]!=a:p[a]=p[p[a]];a=p[a]
        return a
    def union(self,a,b):
        todo=[(a,b)]
        while todo:
            a,b=map(self.find,todo.pop())
            if a==b:continue
            if b==0 or (a!=0 and len(self.adj[b])>len(self.adj[a])):a,b=b,a
            self.parent[b]=a
            for c,v in self.adj[b].items():
                if c in self.adj[a]:todo.append((v,self.adj[a][c]))
                else:self.adj[a][c]=v
            self.adj[b]={}
    def new(self):
        k=len(self.parent);self.parent.append(k);self.adj.append({});return k
    def connect(self,a,c,b):
        a,b=self.find(a),self.find(b)
        if c in self.adj[a]:self.union(self.adj[a][c],b)
        a,b=self.find(a),self.find(b)
        if -c in self.adj[b]:self.union(self.adj[b][-c],a)
        a,b=self.find(a),self.find(b)
        self.adj[a][c]=b;self.adj[b][-c]=a
    def add(self,w):
        at=0
        for c in w:
            at=self.find(at)
            if c in self.adj[at]:at=self.find(self.adj[at][c])
            else:
                b=self.new();self.connect(at,c,b);at=b
        self.union(at,0)
    def member(self,w):
        at=0
        for c in w:
            at=self.find(at)
            if c not in self.adj[at]:return False
            at=self.find(self.adj[at][c])
        return self.find(at)==0
    def compact(self):
        roots=[i for i,p in enumerate(self.parent) if i==p]
        table={a:i for i,a in enumerate(roots)}
        edges={table[a]:{str(c):table[self.find(b)] for c,b in self.adj[a].items()} for a in roots}
        for a,aa in edges.items():
            for c,b in aa.items():assert edges[b][str(-int(c))]==a
        self.parent=list(range(len(roots)))
        self.adj=[{int(c):b for c,b in edges[a].items()} for a in range(len(roots))]
        return edges
    def summary(self):
        E=self.compact();nv=len(E);ne=sum(map(len,E.values()))//2
        loops=sum(a==b for a,aa in E.items() for c,b in aa.items())//2
        assert ne-loops==nv-1 # peripheral-generated core is a tree with loops
        return {'vertices':nv,'edges':ne,'rank':ne-nv+1,'self_loops':loops}

# Independent elementary examples catch the direction and folding conventions.
g=Folded();g.add((1,));g.add((-2,-1,2,1,2))
assert g.member((1,)) and g.member((-2,-1,2,1,2)) and not g.member((2,))
g.add((2,));assert g.member((1,2,-1,-2)) and g.summary()['vertices']==1

keep=D['retained_basis'];killed=D['killed_basis']
Q=[()]
for n in range(1,3):
    Q += [w for w in itertools.product([x for i in keep for x in (i,-i)],repeat=n) if all(w[i]!=-w[i+1] for i in range(n-1))]
tests={(q,j):mul(q,(j,),inv(q)) for q in Q for j in killed}
def status(G):
    yes=[{'q':q,'j':j} for (q,j),w in tests.items() if G.member(w)]
    return {'summary':G.summary(),'canonical_R_basis_tests':len(tests),'present':yes,
            'four_named_generators':{j:G.member((j,)) for j in killed}}

G=Folded()
for w in F.values():G.add(w)
steps=[{'stage':'eight actual fiber words',**status(G)}]
print('H0',steps[-1],flush=True)
records=[];started=time.time()
for a,A in sorted(acts.items()):
    new=0;total=0
    for k,w in F.items():
        v=sub(w,A);total+=len(v)
        if not G.member(v):
            G.add(v);new+=1
            records.append({'old_source_conjugator':[a],'new_source_index':k,'word':v})
    ss=status(G)
    print('Action',a,'new_generators',new,'input_length',total,
          'rank',ss['summary']['rank'],'vertices',ss['summary']['vertices'],
          'named',ss['four_named_generators'],'tests_present',len(ss['present']),
          'elapsed',round(time.time()-started,2),flush=True)
steps.append({'stage':'all one-letter old-source conjugators',**status(G)})
assert all(G.member(w) for w in F.values())
for A in acts.values():assert all(G.member(sub(w,A)) for w in F.values())
out={'description':__doc__,'steps':steps,'added_words':records,'final_graph':G.compact(),
     'scope':'Finite source-conjugator radius1 only. No inference of full marginal equality.'}
(HERE/'stallings_orbit_radius1.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('FINAL radius1',steps[-1],flush=True)
