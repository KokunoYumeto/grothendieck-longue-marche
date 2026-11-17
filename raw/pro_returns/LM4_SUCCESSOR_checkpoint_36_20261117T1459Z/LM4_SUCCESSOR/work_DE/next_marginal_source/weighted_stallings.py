"""Stallings folding with explicit inverse words in the supplied generators.

The edge weights give a homotopy inverse when folds do not lower rank.  With
allow_relations=True they give a right inverse after every rank-lowering
fold; every discarded relation is checked in the original free group.  All
words returned by this module are independently checked by substitution.
"""
from collections import deque

def reduce_word(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inverse(w):return tuple(-x for x in reversed(w))
def multiply(*ws):return reduce_word(x for w in ws for x in w)
def substitute(w,images):return multiply(*(images[x] if x>0 else inverse(images[-x]) for x in w))

class WeightedFold:
    def __init__(self,words,allow_relations=False):
        self.words={i+1:tuple(w) for i,w in enumerate(words)}
        self.allow_relations=allow_relations;self.discarded_relations=[]
        self.parent=[0];self.potential=[()];self.adj=[{}];self.edges=[]
        for i,w in self.words.items():
            at=0
            for j,c in enumerate(w):
                end=0 if j==len(w)-1 else self.new()
                weight=(i,) if j==len(w)-1 else ()
                self.edges.append((at,c,end,weight))
                self.edges.append((end,-c,at,inverse(weight)))
                at=end
        for e in range(len(self.edges)):
            u,c,_,_=self.edges[e];root,_=self.find(u)
            if c in self.adj[root]:self.merge_edges(self.adj[root][c],e)
            else:self.adj[root][c]=e

    def new(self):
        i=len(self.parent);self.parent.append(i);self.potential.append(());self.adj.append({});return i

    def find(self,v):
        # Potential multiplies on the right along the chain.
        path=[];at=v
        while self.parent[at]!=at:path.append(at);at=self.parent[at]
        result=()
        for u in reversed(path):
            result=multiply(self.potential[u],result)
            self.parent[u]=at;self.potential[u]=result
        return at,self.potential[v] if v!=at else ()

    def edge_weight(self,e):
        u,c,v,t=self.edges[e];ru,pu=self.find(u);rv,pv=self.find(v)
        return ru,c,rv,multiply(inverse(pu),t,pv)

    def merge_edges(self,e,f):
        todo=[(e,f)]
        while todo:
            e,f=todo.pop();u,c,a,A=self.edge_weight(e);v,d,b,B=self.edge_weight(f)
            assert u==v and c==d
            if a==b:
                if A!=B:
                    relation=multiply(A,inverse(B))
                    assert self.allow_relations,('rank lowering fold',e,f,A,B)
                    assert not substitute(relation,self.words)
                    self.discarded_relations.append(relation)
                continue
            if b==0 or (a!=0 and len(self.adj[b])>len(self.adj[a])):
                a,b=b,a;A,B=B,A
            self.parent[b]=a;self.potential[b]=multiply(inverse(B),A)
            for label,g in self.adj[b].items():
                if label in self.adj[a]:todo.append((self.adj[a][label],g))
                else:self.adj[a][label]=g
            self.adj[b]={}

    def rewrite(self,w):
        at,_=self.find(0);ans=()
        for c in w:
            if c not in self.adj[at]:return None
            u,_,at,t=self.edge_weight(self.adj[at][c]);ans=multiply(ans,t)
        if at!=self.find(0)[0]:return None
        assert substitute(ans,self.words)==reduce_word(w)
        return ans

if __name__=='__main__':
    f=WeightedFold([(1,),(2,1,-2)])
    assert f.rewrite((2,1,-2))==(2,)
    assert f.rewrite((1,2,1,-2,-1))==(1,2,-1)
    assert f.rewrite((2,)) is None
    g=WeightedFold([(1,2),(2,)])
    assert g.rewrite((1,))==(1,-2)
    h=WeightedFold([(1,1),(1,1,1)],allow_relations=True)
    assert h.rewrite((1,)) is not None
    print('PASS: exact inverse folding and independent free substitution.')

