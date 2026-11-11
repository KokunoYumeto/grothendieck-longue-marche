"""Exact finite group primitives; no computer algebra package required.

Products of permutations act from right to left.  Matrix entries are residues.
All finite objects are exhaustively enumerated, not randomly sampled.
"""
from itertools import permutations, product
from collections import deque
from math import gcd, lcm


class Group:
    def __init__(self, elements, multiply, identity, name):
        self.elements = list(elements)
        self.index = {a:i for i,a in enumerate(self.elements)}
        self.name = name
        self.e = self.index[identity]
        self.n = len(self.elements)
        self.table = [[self.index[multiply(a,b)] for b in self.elements]
                      for a in self.elements]
        self.inv = [next(j for j in range(self.n) if self.table[i][j]==self.e)
                    for i in range(self.n)]
        self.orders = [self.order(i) for i in range(self.n)]
        self.exponent = lcm(*self.orders)
        self.conj = [[self.mul(self.mul(self.inv[h], a),h)
                      for a in range(self.n)] for h in range(self.n)]
        self.classes = [min(c[a] for c in self.conj) for a in range(self.n)]

    def mul(self,a,b):
        return self.table[a][b]

    def power(self,a,k):
        if k<0:
            return self.power(self.inv[a],-k)
        r=self.e
        while k:
            if k&1:r=self.mul(r,a)
            a=self.mul(a,a);k//=2
        return r

    def order(self,a):
        v=a;k=1
        while v!=self.e:v=self.mul(v,a);k+=1
        return k

    def generated(self,gens):
        seen={self.e};todo=[self.e]
        for a in todo:
            for g in gens:
                b=self.mul(a,g)
                if b not in seen:seen.add(b);todo.append(b)
        return seen

    def map_from_generators(self,x,y,a,b):
        """Return the actual homomorphism, or None when any relation fails."""
        values={self.e:self.e};todo=[self.e]
        for p in todo:
            for g,t in [(x,a),(y,b)]:
                q=self.mul(p,g);v=self.mul(values[p],t)
                if q in values:
                    if values[q]!=v:return None
                else:values[q]=v;todo.append(q)
        assert len(values)==self.n
        return tuple(values[i] for i in range(self.n))

    def generating_pairs(self):
        return [(x,y) for x in range(self.n) for y in range(self.n)
                if len(self.generated([x,y]))==self.n]


def permutation_group(n,even=False):
    es=list(permutations(range(n)))
    if even:
        es=[p for p in es if sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))%2==0]
    return Group(es,lambda a,b:tuple(a[b[i]] for i in range(n)),tuple(range(n)),
                 ('A' if even else 'S')+str(n))


def matmul(a,b,n):
    return ((a[0]*b[0]+a[1]*b[2])%n,(a[0]*b[1]+a[1]*b[3])%n,
            (a[2]*b[0]+a[3]*b[2])%n,(a[2]*b[1]+a[3]*b[3])%n)


def sl_elements(n):
    return [a for a in product(range(n),repeat=4) if (a[0]*a[3]-a[1]*a[2])%n==1%n]


def matrix_group(n,projective=False):
    def canon(a):return min(a,tuple((-x)%n for x in a)) if projective else a
    es=sorted(set(canon(a) for a in sl_elements(n)))
    return Group(es,lambda a,b:canon(matmul(a,b,n)),canon((1%n,0,0,1%n)),
                 ('PSL2' if projective else 'SL2')+'(Z/'+str(n)+')')


def orbit_pair_classes(G):
    """Generating pairs modulo simultaneous inner conjugacy."""
    unseen=set(G.generating_pairs());reps=[];which={}
    while unseen:
        x,y=min(unseen);i=len(reps);reps.append((x,y))
        orb={(c[x],c[y]) for c in G.conj}
        for p in orb:which[p]=i
        unseen-=orb
    return reps,which


def universal_envelope(G,outer_automorphisms=()):
    reps,which=orbit_pair_classes(G)
    unseen=set(range(len(reps)));chosen=[]
    while unseen:
        i=min(unseen);orb={i};todo=[i]
        for j in todo:
            x,y=reps[j]
            for a in outer_automorphisms:
                q=which[(a[x],a[y])]
                if q not in orb:orb.add(q);todo.append(q)
        chosen.append(reps[i]);unseen-=orb
    x=tuple(a for a,b in chosen);y=tuple(b for a,b in chosen)
    e=(G.e,)*len(chosen)
    def mul(a,b):return tuple(G.mul(s,t) for s,t in zip(a,b))
    seen={e};es=[e]
    for a in es:
        for g in [x,y]:
            b=mul(a,g)
            if b not in seen:seen.add(b);es.append(b)
    H=Group(es,mul,e,'envelope('+G.name+')')
    return H,H.index[x],H.index[y],chosen
