#!/usr/bin/env python3
"""Exact ell-p-ell return cover and its six-coset modular source.

All groups are evaluated from literal B=C2*C3 words.  The new kernel is
represented as a vector space, not inferred from a proposed automorphism.
"""
from collections import deque
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import argparse
import json
import time
import numpy as np
import sympy as sp
from de_ferrari_a6_source_data import load_data

HERE = Path(__file__).resolve().parent


def rank_mod(a, p):
    a = np.asarray(a, dtype=np.int64).copy() % p
    r = 0
    for c in range(a.shape[1]):
        nz = np.flatnonzero(a[r:,c])
        if not len(nz):
            continue
        j = r+int(nz[0])
        a[[r,j]] = a[[j,r]]
        a[r] = a[r]*pow(int(a[r,c]),-1,p) % p
        ids = np.flatnonzero(a[:,c])
        ids = ids[ids != r]
        if len(ids):
            a[ids] = (a[ids]-a[ids,c,None]*a[r]) % p
        r += 1
        if r == min(a.shape):
            break
    return r


def matrix_power_mod(a, n, p):
    ans = np.eye(len(a),dtype=np.int64)
    while n:
        if n&1:
            ans = ans@a%p
        a = a@a%p
        n >>= 1
    return ans


class Span:
    def __init__(self, d, p):
        self.d, self.p = d,p
        self.rows = {}
        self.originals = []
        self.labels = []

    def add(self, v, label=None):
        v = np.asarray(v,dtype=np.int64).reshape(self.d).copy() % self.p
        original = v.copy()
        for c,row in sorted(self.rows.items()):
            if v[c]:
                v = (v-int(v[c])*row) % self.p
        nz = np.flatnonzero(v)
        if not len(nz):
            return False
        c = int(nz[0])
        v = v*pow(int(v[c]),-1,self.p) % self.p
        self.rows[c] = v
        self.originals.append(original)
        self.labels.append(label)
        return True

    def __len__(self):
        return len(self.rows)


@dataclass
class Element:
    perm: np.ndarray
    c: np.ndarray
    n: np.ndarray
    v: np.ndarray


class ReturnModel:
    def __init__(self, ell, p):
        self.ell,self.p = ell,p
        assert ell != p and ell >= 5 and p >= 5 and sp.isprime(ell) and sp.isprime(p)
        self.data = load_data()
        x = sp.Symbol('u')
        factors = sp.factor_list(sp.cyclotomic_poly(p,x),modulus=ell)[1]
        polys = [sp.Poly(g,x,modulus=ell) for g,e in factors]
        self.poly = min(polys,key=lambda q:tuple(int(a)%ell for a in q.all_coeffs()))
        self.f = self.poly.degree()
        assert self.f == sp.n_order(ell,p)
        coeff = [int(self.poly.nth(i))%ell for i in range(self.f)]
        z = np.zeros((self.f,self.f),dtype=np.int64)
        for j in range(self.f-1):
            z[j+1,j] = 1
        z[:,-1] = -np.array(coeff)%ell
        self.zeta = z
        self.zpowers = [np.eye(self.f,dtype=np.int64)]
        for _ in range(p):
            self.zpowers.append(self.zpowers[-1]@z%ell)
        assert np.array_equal(self.zpowers[-1],self.zpowers[0])
        assert not np.array_equal(z,self.zpowers[0])
        self.dim = 6*ell*self.f
        self.local_dim = ell*self.f
        self.cosets = sorted(self.data['Q2'])
        self.pos = {q:i for i,q in enumerate(self.cosets)}
        self.root = self.pos[self.data['unit']]
        section = {self.data['unit']:[]}
        todo = deque(section)
        while todo:
            q = todo.popleft()
            for b,t in ((0,self.data['s2']),(1,self.data['r2'])):
                qn = self.data['mul2'](q,t)
                if qn not in section:
                    section[qn] = section[q]+[b]
                    todo.append(qn)
        self.section = [section[q] for q in self.cosets]
        self.one = self.identity()
        self.local_x = self.local_identity()
        self.local_x[0][0,0] = 1
        self.local_x[2][0] = 1
        self.local_y = self.local_identity()
        self.local_y[1][0] = 1
        self.local_letters = {1:self.local_x,2:self.local_y,
                              -1:self.local_inv(self.local_x),-2:self.local_inv(self.local_y)}
        self.letters = {}
        self.schreier_rows = {}
        for b,t in ((0,self.data['s2']),(1,self.data['r2'])):
            perm,c,n,v,rows = [],[],[],[],[]
            for q,rep in zip(self.cosets,self.section):
                qn = self.data['mul2'](q,t)
                j = self.pos[qn]
                bw = rep+[b]+self.data['binv'](self.section[j])
                fw = self.data['fword'](bw)
                h = self.local_word(tuple(fw))
                perm.append(j); v.append(h[0]); n.append(h[1]); c.append(int(h[2][0]))
                rows.append({'B_word':bw,'F_word':list(fw)})
            self.letters[b] = Element(np.array(perm),np.array(c),np.array(n),np.array(v))
            self.schreier_rows[str(b)] = rows
        self.letters[-1] = self.inverse(self.letters[1])
        assert self.equal(self.power(self.letters[0],2),self.one)
        assert self.equal(self.power(self.letters[1],3),self.one)
        self.S,self.R = self.action(self.letters[0]),self.action(self.letters[1])
        self.T = self.S@self.R%ell

    def local_identity(self):
        return (np.zeros((self.ell,self.f),dtype=np.int64),
                np.zeros(self.ell,dtype=np.int64),np.zeros(1,dtype=np.int64))

    def local_act(self,n,c,v):
        v = np.roll(v,int(c),axis=0)
        return np.array([self.zpowers[int(a)]@b%self.ell for a,b in zip(n,v)])

    def local_mul(self,a,b):
        av,an,ac = a; bv,bn,bc = b
        return ((av+self.local_act(an,ac[0],bv))%self.ell,
                (an+np.roll(bn,int(ac[0])))%self.p,(ac+bc)%self.ell)

    def local_inv(self,a):
        v,n,c = a
        ci = -int(c[0])%self.ell
        ni = -np.roll(n,ci)%self.p
        vi = -self.local_act(ni,ci,v)%self.ell
        return vi,ni,np.array([ci])

    @lru_cache(None)
    def local_word(self,w):
        if not w:
            return self.local_identity()
        return self.local_mul(self.local_word(w[:-1]),self.local_letters[w[-1]])

    def identity(self):
        return Element(np.arange(6),np.zeros(6,dtype=np.int64),
                       np.zeros((6,self.ell),dtype=np.int64),
                       np.zeros((6,self.ell,self.f),dtype=np.int64))

    def mul(self,a,b):
        perm = b.perm[a.perm]
        c = (a.c+b.c[a.perm])%self.ell
        n = (a.n+np.array([np.roll(b.n[j],int(ci)) for j,ci in zip(a.perm,a.c)]))%self.p
        v = (a.v+np.array([self.local_act(ni,ci,b.v[j]) for j,ni,ci in zip(a.perm,a.n,a.c)]))%self.ell
        return Element(perm,c,n,v)

    def inverse(self,a):
        perm = np.argsort(a.perm)
        c = -a.c[perm]%self.ell
        n = np.array([-np.roll(a.n[j],int(ci))%self.p for j,ci in zip(perm,c)])
        v = np.array([-self.local_act(ni,ci,a.v[j])%self.ell for j,ni,ci in zip(perm,n,c)])
        return Element(perm,c,n,v)

    def power(self,a,n):
        if n < 0:
            return self.power(self.inverse(a),-n)
        ans = self.one
        while n:
            if n&1:
                ans = self.mul(ans,a)
            a = self.mul(a,a); n >>= 1
        return ans

    def word(self,w):
        ans = self.one
        for b in w:
            ans = self.mul(ans,self.letters[b])
        return ans

    def equal(self,a,b):
        return all(np.array_equal(getattr(a,k),getattr(b,k)) for k in ('perm','c','n','v'))

    def in_kernel(self,a):
        return np.array_equal(a.perm,np.arange(6)) and not a.c.any() and not a.n.any()

    def action(self,a):
        m = np.zeros((self.dim,self.dim),dtype=np.int64)
        for i,j in enumerate(a.perm):
            for h in range(self.ell):
                dest = h
                src = (h-int(a.c[i]))%self.ell
                rr = (i*self.ell+dest)*self.f
                cc = (int(j)*self.ell+src)*self.f
                m[rr:rr+self.f,cc:cc+self.f] = self.zpowers[int(a.n[i,h])]
        return m


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ell',type=int,default=5)
    parser.add_argument('--prime',type=int,default=7)
    args = parser.parse_args()
    start = time.time()
    m = ReturnModel(args.ell,args.prime)
    ell,p,f,d = m.ell,m.p,m.f,m.dim
    stem = f'bc_return_prime_l{ell}_p{p}'
    xw,yw = m.data['to_B']((1,)),m.data['to_B']((2,))
    zw = m.data['to_B']((-2,-1))
    X,Y,Z = [m.word(w) for w in (xw,yw,zw)]
    assert m.equal(m.mul(m.mul(X,Y),Z),m.one)
    tau = m.mul(m.letters[0],m.letters[1])
    assert m.equal(m.power(tau,2),m.inverse(X))
    assert m.equal(m.power(tau,2*ell*ell*p),m.one)
    assert not m.equal(m.power(tau,2*ell*p),m.one)
    assert m.in_kernel(m.power(tau,2*ell*p))
    # Complete actual kernel generated by literal cusp powers and conjugates.
    span = Span(d,ell)
    pending = deque()
    for w in (xw,yw,zw):
        bw = w*(ell*p)
        h = m.word(bw)
        assert m.in_kernel(h)
        v = h.v.reshape(d)
        if span.add(v,bw):
            pending.append(len(span.originals)-1)
    while pending:
        j = pending.popleft()
        v,w = span.originals[j],span.labels[j]
        for b,a in ((0,m.S),(1,m.R)):
            ww = [b]+w+([0] if b == 0 else [-1])
            vv = a@v%ell
            if span.add(vv,ww):
                pending.append(len(span.originals)-1)
    assert len(span) == d
    for v,w in zip(span.originals,span.labels):
        h = m.word(w)
        assert m.in_kernel(h) and np.array_equal(h.v.reshape(d),v)
    eye = np.eye(d,dtype=np.int64)
    actions = [m.action(g) for g in (X,Y,Z)]
    profiles = []
    for i in range(6):
        a,b = i*m.local_dim,(i+1)*m.local_dim
        profiles.append([m.local_dim-rank_mod(t[a:b,a:b]-np.eye(m.local_dim,dtype=np.int64),ell)
                         for t in actions])
    assert sorted(profiles) == sorted([[f,(ell-1)*f,0],[f,0,(ell-1)*f],
                                       [(ell-1)*f,f,0],[(ell-1)*f,0,f],
                                       [0,f,(ell-1)*f],[0,(ell-1)*f,f]])
    invariants = [d-rank_mod(a-eye,ell) for a in (m.S,m.R,m.T)]
    assert invariants == [d//2,d//3,d//6]
    assert rank_mod(np.vstack([m.S-eye,m.R-eye]),ell) == d
    assert rank_mod(np.hstack([actions[0]-eye,actions[1]-eye]),ell) == d
    ci = matrix_power_mod(m.T,2*ell*p-1,ell)
    assert np.array_equal(m.T@ci%ell,eye)
    norm = np.hstack([eye-m.S,m.S@(eye-m.R)%ell,(m.S@m.R)@(eye-ci)%ell])%ell
    assert rank_mod(norm,ell) == d
    # Every inner correction gives a product-one peripheral triple; all
    # dimensions are compared in the space of actual conjugated elements.
    inner = np.vstack([eye-m.S,eye-m.R,eye-ci])%ell
    assert rank_mod(inner,ell) == d
    assert np.array_equal(norm@np.vstack([eye,eye,eye])%ell,np.zeros((d,d),dtype=np.int64))
    result = {'status':'PASS_LITERAL_RETURN_PRIME_KERNEL_AND_FIBRE',
              'ell':ell,'prime':p,'field_degree':f,
              'field_polynomial':str(m.poly.as_expr()),
              'zeta_matrix':m.zeta.tolist(),
              'B_cosets':[list(q) for q in m.cosets],
              'B_coset_section':m.section,'literal_B_schreier_rows':m.schreier_rows,
              'local_kernel_dimension':m.local_dim,'induced_kernel_dimension':d,
              'actual_kernel_word_rank':len(span),
              'kernel_basis_B_words':span.labels,
              'six_local_fixed_space_profiles':profiles,
              's_r_tau_fixed_dimensions':invariants,
              'peripheral_product_map_rank':d,
              'fixed_base_conjugator_literal_fibre_count':str(ell**d),
              'fixed_base_conjugator_kernel_orbit_count':1,
              'tau_normalized_literal_fibre_count':str(ell**(d//6)),
              'base_tau_order':2*ell*p,'upper_tau_order':2*ell*ell*p,
              'all_kernel_words_replayed':True,
              'input_sha256':{'de_ferrari_a6_source_data.py':sha256((HERE/'de_ferrari_a6_source_data.py').read_bytes()).hexdigest()},
              'scope':'Exact finite return-prime module and fixed-base-conjugator fibre; source-kernel and full-centralizer proofs are in D46.',
              'seconds':round(time.time()-start,3)}
    np.savez_compressed(HERE/(stem+'.npz'),S=m.S,R=m.R,T=m.T,
                        X=actions[0],Y=actions[1],Z=actions[2],
                        kernel_word_vectors=np.array(span.originals),
                        peripheral_norm=norm,inner_corrections=inner)
    (HERE/(stem+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('kernel_basis_B_words','literal_B_schreier_rows')},indent=2))


if __name__ == '__main__':
    main()
