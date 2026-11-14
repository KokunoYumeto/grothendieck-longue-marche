#!/usr/bin/env python3
"""Exact ordinary-abelian source quotients and the retained S24 map.

This supplies literal multiplication for S_m=B/(F' F^m).  It connects
the actual full A6 source abelian quotient to S120, and the saved full
binary K6 correction image to the exponent map modulo24.  The latter
map proves that the entire retained D23 source maps onto S24; no
perfectness or maximal-solvable claim is made by this program.
"""
from pathlib import Path
from collections import deque
import json,time
import numpy as np
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent

def inverse2(A):
    n=A.shape[0];a=np.c_[A%2,np.eye(n,dtype=np.int64)]
    for j in range(n):
        k=next(k for k in range(j,n) if a[k,j]);a[[j,k]]=a[[k,j]]
        for k in range(n):
            if k!=j and a[k,j]:a[k]^=a[j]
    assert np.array_equal(a[:,:n],np.eye(n,dtype=np.int64))
    return a[:,n:]

def independent_rows(A):
    found=[];basis={}
    for i,row in enumerate(A%2):
        v=row.copy()
        for pivot,u in sorted(basis.items()):
            if v[pivot]:v^=u
        nz=np.flatnonzero(v)
        if len(nz):basis[int(nz[0])]=v;found.append(i)
    return found

class AbelianSource:
    def __init__(self,d,modulus):
        self.d=d;self.m=modulus;self.Q=d['Q2'];self.qindex={q:i for i,q in enumerate(self.Q)}
        self.e=self.qindex[d['unit']]
        paths={d['unit']:[]};queue=deque([d['unit']])
        while queue:
            q=queue.popleft()
            for letter,g in ((0,d['s2']),(1,d['r2'])):
                z=d['mul2'](q,g)
                if z not in paths:paths[z]=paths[q]+[letter];queue.append(z)
        self.paths=[paths[q] for q in self.Q]
        self.table=np.array([[self.qindex[d['mul2'](q,r)] for r in self.Q] for q in self.Q])
        self.action=np.empty((6,2,2),dtype=np.int64);self.cocycle=np.empty((6,6,2),dtype=np.int64)
        for i,p in enumerate(self.paths):
            self.action[i]=np.column_stack([self.fab(p+w+d['binv'](p)) for w in (d['xword'],d['yword'])])
            for j,r in enumerate(self.paths):
                self.cocycle[i,j]=self.fab(p+r+d['binv'](self.paths[self.table[i,j]]))
        for i in range(6):
            for j in range(6):
                ij=self.table[i,j]
                assert np.array_equal(self.action[i]@self.action[j],self.action[ij])
                for k in range(6):
                    assert np.array_equal(self.cocycle[i,j]+self.cocycle[ij,k],
                        self.action[i]@self.cocycle[j,k]+self.cocycle[i,self.table[j,k]])
        self.one=(self.e,0,0)
        self.s=self.literal([0]);self.r=self.literal([1]);self.ri=self.literal([-1])
        assert self.mul(self.s,self.s)==self.one
        assert self.mul(self.mul(self.r,self.r),self.r)==self.one
        assert self.word(d['xword'])==(self.e,1,0) and self.word(d['yword'])==(self.e,0,1)
    def fab(self,w):
        v=self.d['fword'](w)
        return np.array([sum(1 if a==j else -1 if a==-j else 0 for a in v) for j in (1,2)],dtype=np.int64)
    def mul(self,g,h):
        q,u,v=g;r,a,b=h
        z=(np.array([u,v])+self.action[q]@np.array([a,b])+self.cocycle[q,r])%self.m
        return int(self.table[q,r]),int(z[0]),int(z[1])
    def literal(self,w):
        q=self.d['unit']
        for a in w:q=self.d['mul2'](q,self.d['s2'] if a==0 else self.d['r2'] if a==1 else self.d['r22'])
        j=self.qindex[q];v=self.fab(w+self.d['binv'](self.paths[j]))%self.m
        return j,int(v[0]),int(v[1])
    def word(self,w):
        g=self.one
        for a in w:g=self.mul(g,self.s if a==0 else self.r if a==1 else self.ri)
        return g

def main():
    start=time.time();d=load_data();S=AbelianSource(d,120)
    Nfab=np.column_stack([S.fab(w) for w in d['Nwords']])
    L=hermite_normal_form(Matrix(Nfab.tolist()));assert abs(int(L.det()))==12
    Li=L.inv();primitive=Li*Matrix(Nfab.tolist());assert all(v.q==1 for v in primitive)
    primitive=np.array(primitive,dtype=np.int64)
    assert not np.any(Nfab%2)
    for w in d['Nwords']+[d['xword'],d['yword']]:assert S.word(w)==S.literal(w)
    # The entire K6 image in the binary source is an elementary abelian
    # group of dimension9; its actual F-prime part has dimension7.
    binary=np.load(HERE/'de_ferrari_two_degree6_module.npz')
    B=binary['full_kernel_basis'].astype(np.int64)%2
    C=binary['F_prime_basis'].astype(np.int64)%2
    powers=binary['N_sixth_power_vectors'].astype(np.int64)%2
    rows=independent_rows(B);assert len(rows)==9
    inverse=inverse2(B[rows]);Ccoords=inverse@C[rows]%2;Pcoords=inverse@powers[rows]%2
    assert np.array_equal(B@Ccoords%2,C) and np.array_equal(B@Pcoords%2,powers)
    assert len(independent_rows(Ccoords.T))==7
    raw=json.loads((HERE/'de_ferrari_two_degree6_module.json').read_text())
    cols=[]
    for w in raw['full_basis_words']:
        v=Li*Matrix(S.fab(w).tolist())/6
        assert all(a.q==1 for a in v)
        cols.append([int(a)%2 for a in v])
    quotient=np.array(cols,dtype=np.int64).T
    assert quotient.shape==(2,9) and len(independent_rows(quotient.T))==2
    assert not np.any(quotient@Ccoords%2)
    assert np.array_equal(quotient@Pcoords%2,primitive%2)
    # This is the literal quotient K6 -> (6L)/(12L).  Its kernel is
    # exactly the saved prime correction image, by the ranks9,7,2.
    # A word killed by D23 lies in K6 and has binary image zero,
    # so its ordinary abelianization lies in12L subset24 Z^2.
    assert not np.any(np.array(12*L,dtype=np.int64)%24)
    G=int(json.loads((HERE/'de_a6_schreier_full_ordered.out').read_text().splitlines()[-1])['order'])
    E=int(json.loads((HERE/'de_a6_schreier_Fprime.out').read_text().splitlines()[-1])['order'])
    assert G//E==6*120**2 and G%(6*E)==0
    orders=json.loads((HERE/'de_a6_schreier_N_input.json').read_text())
    # The literal x,y order120 plus |F/F'|=120^2 identifies the map,
    # with the ordinary ordered exponent coordinates, not only its order.
    assert orders['F_image_orders']==[120,120]
    T=AbelianSource(d,24)
    for g in (S.one,S.s,S.r,S.ri,(S.e,1,0),(S.e,0,1)):
        for h in (S.one,S.s,S.r,S.ri,(S.e,1,0),(S.e,0,1)):
            k=S.mul(g,h)
            assert T.mul((g[0],g[1]%24,g[2]%24),(h[0],h[1]%24,h[2]%24))==(k[0],k[1]%24,k[2]%24)
    out={'status':'PASS','actual_full_A6_abelian_F_quotient_order':6*120**2,
         'actual_pure_abelian_quotient':'(Z/120)^2, ordinary x,y exponent coordinates',
         'explicit_quotient':'S120 = B/(F-prime F^120)',
         'retained_source_quotient':'D23 -> S24 = B/(F-prime F^24)',
         'retained_quotient_order':6*24**2,
         'N_exponent_lattice_Hermite_basis':np.array(L,dtype=np.int64).tolist(),
         'binary_full_prime_quotient_ranks':[9,7,2],
         'actual_binary_to_scaled_exponent_quotient':quotient.tolist(),
         'all_97_sixth_power_columns_compared':True,
         'retained_kernel_exponent_lattice_contained_in_24Z2':True,
         'H_image_in_S120':'(Z/40)^2, the subgroup3(Z/120)^2',
         'boundary_factorization':'B/([H,H] H^40) -> S120, induced by the actual B words',
         'no_perfectness_or_maximal_solvable_inference':True,
         'seconds':round(time.time()-start,3)}
    np.savez_compressed(HERE/'de_ferrari_a6_abelian_compare.npz',Q2_table=S.table,Q2_action=S.action,
                        integral_cocycle=S.cocycle,N_lattice_basis=np.array(L,dtype=np.int64),
                        N_F_abelianization=Nfab,N_primitive_abelianization=primitive,
                        binary_full_basis_to_exponent_quotient=quotient,
                        binary_prime_coordinates=Ccoords,binary_power_coordinates=Pcoords)
    (HERE/'de_ferrari_a6_abelian_compare.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
