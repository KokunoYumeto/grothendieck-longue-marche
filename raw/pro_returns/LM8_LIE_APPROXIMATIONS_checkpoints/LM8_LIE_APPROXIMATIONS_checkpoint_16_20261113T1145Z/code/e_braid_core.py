"""Exact finite regular-action tables for the braid audits."""
import hashlib
import numpy as np

def signature(p,q,order):
    """Canonicalize a regular right action using positive-generator BFS."""
    todo=[0];seen={0}
    for v in todo:
        for g in (p,q):
            w=int(g[v])
            if w not in seen:seen.add(w);todo.append(w)
    assert len(todo)==order
    relabel=np.empty(order,dtype=np.uint16)
    relabel[todo]=np.arange(order,dtype=np.uint16)
    canon=np.concatenate((relabel[p[todo]],relabel[q[todo]]))
    return hashlib.sha256(canon.astype('<u2',copy=False).tobytes()).hexdigest(),canon

class Table:
    kernel_sigs={}
    kernel_canons={}
    def __init__(self,row):
        self.n=n=row['index']
        self.a_perm=pa=np.array(row['a_permutation'],dtype=np.uint16)-1
        self.b_perm=pb=np.array(row['b_permutation'],dtype=np.uint16)-1
        self.a=int(pa[0]);self.b=int(pb[0])
        M=np.zeros((n,n),dtype=np.uint16);M[:,0]=np.arange(n,dtype=np.uint16)
        todo=[0];seen={0};self.tree=[]
        for v in todo:
            for k,p in enumerate((pa,pb)):
                w=int(p[v])
                if w not in seen:
                    seen.add(w);todo.append(w);self.tree.append((v,k,w))
                    M[:,w]=p[M[:,v]]
        assert len(todo)==n
        self.M=M
        self.inv=np.argmax(M==0,axis=1).astype(np.uint16)
        assert np.all(M[np.arange(n),self.inv]==0)
        assert np.all(M[self.inv,np.arange(n)]==0)
        assert np.array_equal(M[:,self.a],pa) and np.array_equal(M[:,self.b],pb)
    def mul(self,*xs):
        v=0
        for x in xs:v=int(self.M[v,x])
        return v
    def pow(self,x,k):
        if k<0:x=int(self.inv[x]);k=-k
        y=0
        while k:
            if k&1:y=int(self.M[y,x])
            x=int(self.M[x,x]);k//=2
        return y
    def order(self,x):
        v=x;k=1
        while v:
            v=int(self.M[v,x]);k+=1
            assert k<=self.n
        return k
    def closure(self,gens):
        todo=[0];seen={0}
        gens=tuple(map(int,gens))
        for v in todo:
            for g in gens:
                w=int(self.M[v,g])
                if w not in seen:seen.add(w);todo.append(w)
        return todo
    def source(self,ap,bp):
        sig,canon=signature(self.M[:,ap],self.M[:,bp],self.n)
        assert sig in self.kernel_sigs,'LINS enumeration omitted a constructed kernel'
        assert np.array_equal(canon,self.kernel_canons[sig]) # exact, not a hash-only certificate
        return self.kernel_sigs[sig]
    def self_descent(self,ap,bp):
        imgs=np.zeros(self.n,dtype=np.uint16);gs=(ap,bp)
        for v,k,w in self.tree:imgs[w]=self.M[imgs[v],gs[k]]
        return len(np.unique(imgs))==self.n and all(np.array_equal(imgs[p],self.M[imgs,g]) for p,g in ((self.a_perm,ap),(self.b_perm,bp)))

