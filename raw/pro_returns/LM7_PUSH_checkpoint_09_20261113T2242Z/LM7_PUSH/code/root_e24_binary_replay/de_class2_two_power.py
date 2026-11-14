#!/usr/bin/env python3
"""Faithful free class-two 2-power-exponent collector on the 97 N-generators.

The abelian modulus is 2**power and the commutator modulus is 2**(power-1).
Mixed words may contain literal B letters or ordered N normal-form blocks.
The short-word versus spanning-tree section comparison is retained exactly.
"""
from functools import cache
import numpy as np


class TwoPowerCollector:
    def __init__(self, power, context):
        assert power >= 2
        self.power = power
        self.mod = 2**power
        self.cmod = self.mod//2
        self.e = context
        self.base = context['base']
        self.d = context['d']
        self.v = context['v']
        self.n = 97
        self.up = np.triu_indices(self.n, 1)
        self.offset = [i*(2*self.n-i-1)//2 for i in range(self.n)]
        self.ci = {self.v['Q'][e]: j for j,e in enumerate(self.v['chords'])}
        self.one = self.v['unit']
        self.ss, self.rr = self.v['ss'], self.v['rr']
        self.rri = self.v['inverse'](self.rr)

    def zero(self):
        return np.zeros(self.n, dtype=np.int64), np.zeros(len(self.up[0]), dtype=np.int64)

    def multiply(self, x, y):
        a,z=x; b,w=y
        return (a+b)%self.mod, (z+w-np.outer(b,a)[self.up])%self.cmod

    def inverse(self, x):
        a,z=x
        return -a%self.mod, (-z-np.outer(a,a)[self.up])%self.cmod

    def ncollect(self, word):
        a,z=self.zero()
        for letter in self.d['nword'](word):
            i=abs(letter)-1; s=1 if letter>0 else -1
            block=slice(self.offset[i],self.offset[i]+self.n-i-1)
            z[block]=(z[block]-s*a[i+1:])%self.cmod
            a[i]=(a[i]+s)%self.mod
        return a,z

    @cache
    def action(self,q):
        A=self.v['act'](q,self.v['C'])[self.v['chords']].astype(np.int64)
        w=self.base['Bpaths'][q]; wi=self.base['binv'](w); tau=[]
        for i,t in enumerate(self.base['Nwords']):
            a,z=self.ncollect(w+t+wi)
            assert np.array_equal(a,A[:,i]%self.mod)
            tau.append(z)
        tau=np.stack(tau,axis=1)
        c=self.v['P'][q][self.v['chords']]
        tau=(tau-c[self.up[0],None]*A[self.up[1]]+
             c[self.up[1],None]*A[self.up[0]])%self.cmod
        return A,tau

    def acted(self,q,a,z):
        A,tau=self.action(q)
        Z=np.zeros((self.n,self.n),dtype=np.int64)
        Z[self.up]=z; Z=Z-Z.T
        Z-=np.diag(a*(a-1)//2)+np.tril(np.outer(a,a),-1)
        return A@a%self.mod, (tau@a+(A@Z@A.T)[self.up])%self.cmod

    def collect(self,word):
        q=self.one; a,z=self.zero()
        for token in word:
            if isinstance(token,tuple):
                b,c=self.acted(q,*token)
                a,z=self.multiply((a,z),(b,c))
                continue
            qn=self.v['times'](q,self.ss if token==0 else self.rr if token==1 else self.rri)
            gen=[]
            if token:
                if q in self.ci:gen.append(self.ci[q]+1)
                if qn in self.ci:gen.append(-self.ci[qn]-1)
            for letter in gen:
                i=abs(letter)-1; s=1 if letter>0 else -1
                block=slice(self.offset[i],self.offset[i]+self.n-i-1)
                z[block]=(z[block]-s*a[i+1:])%self.cmod
                a[i]=(a[i]+s)%self.mod
            q=qn
        assert q==self.one
        return a,z

    def next_kernel(self,word):
        a,z=self.collect(word)
        assert not np.any(a%(self.mod//2)) and not np.any(z%(self.cmod//2))
        return np.concatenate((a//(self.mod//2),z//(self.cmod//2)))%2

    def invword(self,word):
        return [self.inverse(t) if isinstance(t,tuple) else -t for t in reversed(word)]

    def bpower(self,word,k):
        return word*k if k>=0 else self.invword(word)*(-k)

    def literal_checks(self):
        rng=np.random.default_rng(182026+self.power)
        non_tree=max(self.v['Q'],key=lambda q:int(np.abs(self.v['P'][q][self.v['chords']]).sum()))
        assert np.any(self.v['P'][non_tree][self.v['chords']])
        count=0
        for q in (self.ss,self.rr,non_tree):
            for trial in range(4):
                a,z=self.zero();w=[]
                active=sorted(rng.choice(self.n,size=3,replace=False).tolist())
                for i in active:
                    a[i]=int(rng.choice((-3,-2,-1,1,2,3)))
                    w+=self.bpower(self.base['Nwords'][i],int(a[i]))
                i,j=active[:2]
                pos=np.flatnonzero((self.up[0]==i)&(self.up[1]==j))[0]
                z[pos]=int(rng.choice((-3,-2,-1,1,2,3)))
                comm=self.base['Nwords'][i]+self.base['Nwords'][j]+self.base['binv'](self.base['Nwords'][i])+self.base['binv'](self.base['Nwords'][j])
                w+=self.bpower(comm,int(z[pos]));path=self.base['Bpaths'][q]
                direct=self.ncollect(path+w+self.base['binv'](path))
                formula=self.collect(path+[(a,z)]+self.base['binv'](path))
                assert all(np.array_equal(c,d) for c,d in zip(direct,formula))
                count+=1
        return count
