#!/usr/bin/env python3
"""Exact metabelian pure quotient F/image-kernel(F'').

Elements are x^a y^b e_v, with a,b modulo120 and v in F3^9.
The conjugation matrices and the commutator come from actual permutation
sifts in de_a6_module.cpp.  This file verifies the normal-form law,
the full cyclic module, all saved original derived words, and the
complete multiplier-one gentle fibre in this particular quotient.
"""
from pathlib import Path
from itertools import product
import json,time
import numpy as np
from de_a6_schreier_certificate import read_certificate,verify_words
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent

def rref(A):
    A=np.array(A,dtype=np.int64,copy=True)%3;pivots=[];r=0
    for c in range(A.shape[1]):
        nz=np.flatnonzero(A[r:,c])
        if not len(nz):continue
        k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*pow(int(A[r,c]),-1,3)%3
        for i in range(A.shape[0]):
            if i!=r:A[i]=(A[i]-A[i,c]*A[r])%3
        pivots.append(c);r+=1
        if r==len(A):break
    return A,pivots

def rank(A):return len(rref(A)[1])
def nullspace(A):
    R,p=rref(A);free=[j for j in range(R.shape[1]) if j not in p];N=np.zeros((R.shape[1],len(free)),dtype=np.int64)
    for k,j in enumerate(free):
        N[j,k]=1
        for i,c in enumerate(p):N[c,k]=-R[i,j]%3
    return N

def inverse(A):
    n=len(A);R,p=rref(np.c_[A,np.eye(n,dtype=np.int64)])
    assert p[:n]==list(range(n)) and np.array_equal(R[:,:n],np.eye(n,dtype=np.int64))
    return R[:,n:]

class Metabelian:
    def __init__(self):
        self.raw=json.loads((HERE/'de_a6_module.json').read_text());assert self.raw['status']=='PASS'
        self.S,self.R,self.X,self.Y=np.array(self.raw['conjugation_matrices'],dtype=np.int64)
        self.c=np.array(self.raw['commutator_x_y'],dtype=np.int64);self.I=np.eye(9,dtype=np.int64)
        self.xi=inverse(self.X);self.yi=inverse(self.Y)
        assert not np.any((self.X@self.Y-self.Y@self.X)%3)
        assert np.array_equal(self.S@self.S%3,self.I)
        assert np.array_equal(self.R@self.R@self.R%3,self.I)
        self.Xpow=[self.I];self.Ypow=[self.I];self.Xinv=[self.I];self.Yinv=[self.I]
        self.Xsum=[np.zeros((9,9),dtype=np.int64)];self.db=[np.zeros(9,dtype=np.int64)]
        for i in range(120):
            self.Xpow.append(self.Xpow[-1]@self.X%3);self.Ypow.append(self.Ypow[-1]@self.Y%3)
            self.Xinv.append(self.Xinv[-1]@self.xi%3);self.Yinv.append(self.Yinv[-1]@self.yi%3)
            self.Xsum.append((self.Xsum[-1]+self.Xinv[-2])%3)
            self.db.append((self.db[-1]-self.xi@self.Yinv[-1]@self.c)%3)
        for A in (self.Xpow,self.Ypow,self.Xinv,self.Yinv):assert np.array_equal(A[120],self.I)
        assert not np.any(self.db[120])
        assert not np.any(self.Xsum[120])
        self.one=np.zeros(11,dtype=np.int64);self.x=self.one.copy();self.x[0]=1
        self.y=self.one.copy();self.y[1]=1
        self.letters={1:self.x,2:self.y,-1:self.inv(self.x),-2:self.inv(self.y)}
        assert np.array_equal(self.comm(self.x,self.y),np.r_[0,0,self.c])
        monomials=[];columns=[]
        for total in range(9):
            for i in range(total+1):
                j=total-i;v=self.Xpow[i]@self.Ypow[j]@self.c%3
                if rank(np.column_stack(columns+[v]))>len(columns):columns.append(v);monomials.append((i,j))
            if len(columns)==9:break
        assert len(columns)==9
        self.cyclic_monomials=monomials;self.cyclic_basis=np.column_stack(columns);self.cyclic_inverse=inverse(self.cyclic_basis)
    def mul(self,g,h):
        a,b=map(int,g[:2]);c,d=map(int,h[:2])
        v=(self.Yinv[d]@(self.Xinv[c]@g[2:]+self.Xsum[c]@self.db[b])+h[2:])%3
        return np.r_[(a+c)%120,(b+d)%120,v]
    def inv(self,g):
        a,b=map(int,g[:2]);c,d=(-a)%120,(-b)%120
        v=-self.Yinv[d]@(self.Xinv[c]@g[2:]+self.Xsum[c]@self.db[b])%3
        h=np.r_[c,d,v]
        assert np.array_equal(self.mul(g,h),self.one) and np.array_equal(self.mul(h,g),self.one)
        return h
    def power(self,g,n):
        if n<0:return self.power(self.inv(g),-n)
        out=self.one.copy()
        while n:
            if n&1:out=self.mul(out,g)
            g=self.mul(g,g);n//=2
        return out
    def conj(self,g,h):return self.mul(self.mul(g,h),self.inv(g))
    def comm(self,g,h):return self.mul(self.conj(g,h),self.inv(h))
    def word(self,w):
        a=b=0;v=np.zeros(9,dtype=np.int64)
        for letter in w:
            if letter==1:v=(self.xi@v+self.db[b])%3;a=(a+1)%120
            elif letter==-1:v=self.X@(v-self.db[b])%3;a=(a-1)%120
            elif letter==2:v=self.yi@v%3;b=(b+1)%120
            elif letter==-2:v=self.Y@v%3;b=(b-1)%120
            else:raise ValueError('F letter')
        return np.r_[a,b,v]
    def source_dag(self,d):
        assert len(d['original'])==2
        values=[]
        for op,a,b in d['nodes']:
            if op==0:v=self.one.copy()
            elif op==1:v=(self.x if a==0 else self.y).copy()
            elif op==2:v=self.mul(values[a],values[b])
            elif op==3:v=self.inv(values[a])
            elif op==4:v=self.comm(values[a],values[b])
            elif op==5:v=self.conj(values[a],values[b])
            else:raise AssertionError('word operation')
            values.append(v)
        return np.array([values[j] for j in d['words']])
    def normalized_action(self,v):
        cprime=(self.c+(self.X-self.I)@(self.Y-self.I)@v)%3
        columns=[self.Xpow[i]@self.Ypow[j]@cprime%3 for i,j in self.cyclic_monomials]
        return np.column_stack(columns)@self.cyclic_inverse%3

def main():
    start=time.time();M=Metabelian();d=load_data()
    certificate=read_certificate(HERE/'de_a6_schreier_Fprime.bin');verify_words(certificate)
    values=M.source_dag(certificate);assert not np.any(values[:,:2])
    prep=json.loads((HERE/'de_a6_schreier_Fprimecompact_input.json').read_text())
    expected=np.array(M.raw['all_original_E_generator_coordinates'])
    assert np.array_equal(values[prep['source_indices'],2:],expected)
    for g in (M.x,M.y,M.inv(M.x),M.inv(M.y),np.r_[0,0,M.c]):
        for h in (M.x,M.y,np.r_[0,0,M.c]):
            for k in (M.x,M.y,np.r_[0,0,M.c]):
                assert np.array_equal(M.mul(M.mul(g,h),k),M.mul(g,M.mul(h,k)))
    assert np.array_equal(M.power(M.x,120),M.one) and np.array_equal(M.power(M.y,120),M.one)
    norm=np.vstack((M.I+M.S,M.I+M.R+M.R@M.R))%3;kernel=nullspace(norm);rows=[]
    for z in product(range(3),repeat=kernel.shape[1]):
        v=kernel@np.array(z,dtype=np.int64)%3;action=M.normalized_action(v)
        rows.append({'parameter':list(z),'f_module_value':v.tolist(),'derived_action_rank':rank(action),
                     'surjective':rank(action)==9})
    Hstable=np.c_[M.Xpow[3]-M.I,M.Ypow[3]-M.I]%3
    Nstable=np.c_[M.Xpow[6]-M.I,M.Xpow[4]@M.Ypow[2]-M.I]%3
    orders=[]
    for A in (M.Xpow,M.Ypow):orders.append(next(i for i in range(1,121) if np.array_equal(A[i],M.I)))
    out={'status':'PASS','pure_quotient_order':120**2*3**9,
         'pure_abelianization':'(Z/120)^2','derived_module':'(F3)^9',
         'ordinary_x_y_action_orders':orders,'cyclic_module_monomials':[list(x) for x in M.cyclic_monomials],
         'all276_original_derived_generator_values_independently_replayed':True,
         'multiplier_one_norm_rank':rank(norm),'complete_norm_solution_count':len(rows),
         'surjective_multplier_one_count':sum(r['surjective'] for r in rows),
         'H_module_commutator_rank':rank(Hstable),'N_module_commutator_rank':rank(Nstable),
         'complete_gentle_module_points':rows,
         'scope':'Exact actual metabelian source quotient. No full A6 lift, Galois-image, or profinite conclusion.',
         'seconds':round(time.time()-start,3)}
    np.savez_compressed(HERE/'de_ferrari_a6_metabelian.npz',norm_matrix=norm,norm_kernel=kernel,
                        cyclic_module_basis=M.cyclic_basis,cyclic_module_inverse=M.cyclic_inverse,
                        H_commutator_image=Hstable,N_commutator_image=Nstable)
    (HERE/'de_ferrari_a6_metabelian.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='complete_gentle_module_points'},indent=2),flush=True)

if __name__=='__main__':main()
