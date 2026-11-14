#!/usr/bin/env python3
"""Exact exploratory surface point-pushing action from Bardakov--Bellingeri
arXiv:0705.4201, Proposition 4 (printed p.5), genus two, n=2.
Commutator convention is [u,v]=u^{-1}v^{-1}uv.  The proof input is
that proposition, not the uncorrected ER formulas in Bellingeri2003.
"""
import itertools, json, random, math
from pathlib import Path

def red(w):
    a=[]
    for t in w:
        if a and a[-1]==-t: a.pop()
        else: a.append(t)
    return tuple(a)
def mul(*w): return red(t for a in w for t in a)
def inv(w): return tuple(-t for t in reversed(w))
def comm(a,b): return mul(inv(a),inv(b),a,b)
def conj(a,b): return mul(a,b,inv(a))
def subst(w,f): return mul(*(f[t-1] if t>0 else inv(f[-t-1]) for t in w))

def words(genus=2):
    x=[(i+1,) for i in range(2*genus)]
    c=inv(mul(*(comm(inv(x[2*k]),x[2*k+1]) for k in range(genus))))
    maps=[]
    for k in range(genus):
        a,b=x[2*k:2*k+2]
        for kind in (0,1):
            v=a if kind==0 else b
            z=comm(c,v)
            f=x.copy()
            if kind==0:
                f[2*k]=conj(inv(c),a)
                f[2*k+1]=mul(inv(c),b,comm(a,c))
            else:
                f[2*k]=mul(a,c)
                f[2*k+1]=conj(inv(c),b)
            for j in range(2*k+2,2*genus): f[j]=conj(z,x[j])
            assert subst(c,f)==mul(z,c),(k,kind,subst(c,f),mul(z,c))
            maps.append(f)
    return c,maps

class SemiDirect:
    def __init__(self,q=7,r=3,z=2):
        self.q,self.r,self.z=q,r,z
        self.n=q*r
        self.pairs=list(itertools.product(range(q),range(r)))
        self.mul=[[0]*self.n for _ in range(self.n)]
        for i,(a,b) in enumerate(self.pairs):
            for j,(c,d) in enumerate(self.pairs):
                self.mul[i][j]=((a+pow(z,b,q)*c)%q)*r+(b+d)%r
        self.inv=[next(j for j in range(self.n) if self.mul[i][j]==0 and self.mul[j][i]==0) for i in range(self.n)]
        self.conj=[[self.mul[self.mul[g][a]][self.inv[g]] for a in range(self.n)] for g in range(self.n)]
    def eval(self,w,t):
        out=0
        for a in w: out=self.mul[out][t[a-1] if a>0 else self.inv[t[-a-1]]]
        return out
    def canonical(self,t): return min(tuple(row[a] for a in t) for row in self.conj)

class PermGroup:
    def __init__(self,d,even=False):
        perms=list(itertools.permutations(range(d)))
        if even:
            perms=[t for t in perms if sum(t[i]>t[j] for i in range(d) for j in range(i+1,d))%2==0]
        self.perms=perms; self.n=len(perms)
        ix={v:i for i,v in enumerate(perms)}
        self.mul=[[ix[tuple(a[b[j]] for j in range(d))] for b in perms] for a in perms]
        self.inv=[next(j for j in range(self.n) if self.mul[i][j]==0 and self.mul[j][i]==0) for i in range(self.n)]
        self.conj=[[self.mul[self.mul[g][a]][self.inv[g]] for a in range(self.n)] for g in range(self.n)]
    eval=SemiDirect.eval
    canonical=SemiDirect.canonical

def fast_action(G,t,k,kind):
    M,I=G.mul,G.inv
    c=0
    for h in range(len(t)//2):
        a,b=t[2*h:2*h+2]
        c=M[c][M[M[M[a][I[b]]][I[a]]][b]]
    c=I[c]
    a,b=t[2*k:2*k+2]
    v=a if kind==0 else b
    z=M[M[M[I[c]][I[v]]][c]][v]
    tt=list(t)
    if kind==0:
        tt[2*k]=M[M[I[c]][a]][c]
        tt[2*k+1]=M[M[I[c]][b]][M[M[M[I[a]][I[c]]][a]][c]]
    else:
        tt[2*k]=M[a][c]
        tt[2*k+1]=M[M[I[c]][b]][c]
    for j in range(2*k+2,len(t)):
        tt[j]=M[M[z][t[j]]][I[z]]
    return tuple(tt)

def orbit(G,t,cap=200000):
    t=G.canonical(t)
    reps=[t]; ix={t:0}; ps=[[],[],[],[]]
    for cur in reps:
        for i in range(4):
            nxt=G.canonical(fast_action(G,cur,i//2,i%2))
            if nxt not in ix:
                ix[nxt]=len(reps);reps.append(nxt)
                if len(reps)>cap: return None
            ps[i].append(ix[nxt])
    for pp in ps: assert sorted(pp)==list(range(len(reps)))
    return reps,ps

if __name__=='__main__':
    c,fs=words()
    print('Exact free-word boundary checks passed for all four point-pushing generators.',flush=True)
    G=SemiDirect()
    random.seed(149)
    # Work in one fixed nonzero C3-valued character, which point pushing fixes.
    for chi in [(1,0,0,0),(1,1,1,1),(1,2,0,1)]:
        reps=sorted({G.canonical(tuple(3*a+b for a,b in zip(v,chi))) for v in itertools.product(range(7),repeat=4) if G.eval(c,tuple(3*a+b for a,b in zip(v,chi)))!=0})
        ix={t:i for i,t in enumerate(reps)}
        ps=[]
        for f in fs:
            perm=[ix[G.canonical(tuple(G.eval(w,t) for w in f))] for t in reps]
            assert sorted(perm)==list(range(len(reps)))
            ps.append(perm)
        from sympy.combinatorics import Permutation,PermutationGroup
        S=PermutationGroup([Permutation(p) for p in ps])
        print('chi',chi,'representations',len(reps),'permutation image order',S.order(),'orbit sizes',[len(o) for o in S.orbits()],flush=True)

    for d,even in [(4,False),(5,True)]:
        G=PermGroup(d,even)
        print('Group',d,even,'size',G.n,flush=True)
        for j in range(5):
            t=tuple(random.randrange(G.n) for _ in range(4))
            assert all(fast_action(G,t,i//2,i%2)==tuple(G.eval(w,t) for w in fs[i]) for i in range(4))
            oo=orbit(G,t)
            if oo is None:
                print('Orbit exceeds cap',t,flush=True);continue
            reps,ps=oo
            print('seed',t,'orbit size',len(reps),'factorization',__import__('sympy').factorint(len(reps)),flush=True)
            if any(G.n%p for p in __import__('sympy').factorint(len(reps))):
                data={'group':{'d':d,'even':even,'order':G.n,'permutations':G.perms},'seed':t,'orbit_size':len(reps),'representatives':reps,'monodromy_generators':ps,'source':'Bardakov--Bellingeri, arXiv:0705.4201, Proposition 4'}
                Path(__file__).with_name('A_point_pushing_obstruction.json').write_text(json.dumps(data,indent=2))
                print('NEW PRIME IN MONODROMY; saved exact finite certificate',flush=True)
                break
