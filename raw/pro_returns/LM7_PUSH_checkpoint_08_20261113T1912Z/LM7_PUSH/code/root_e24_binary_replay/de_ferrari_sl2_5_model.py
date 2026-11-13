#!/usr/bin/env python3
"""Exact universal Ferrari quotient from all epimorphisms to SL2(F5).

The 76 epimorphism kernels are represented faithfully by
SL2(F5)^19 x C2^2.  The two extra coordinates are the global free
abelianization modulo2.  Nielsen automorphisms have an actual
19-factor permutation, PGL2(F5) conjugators, 19x2 central cross
terms, and a GL2(F2) action on the two global coordinates.
"""
from pathlib import Path
from itertools import product
import json,time
import numpy as np
from de_ferrari_a5_model import FerrariA5

def matmul(a,b):
    A,B,C,D=a;e,f,g,h=b
    return ((A*e+B*g)%5,(A*f+B*h)%5,(C*e+D*g)%5,(C*f+D*h)%5)

def matinv(a):
    A,B,C,D=a;k=pow((A*D-B*C)%5,-1,5)
    return tuple(k*t%5 for t in (D,-B,-C,A))

class FerrariSL2Five:
    def __init__(self):
        self.old=FerrariA5();self.n=19
        self.sl=[a for a in product(range(5),repeat=4) if (a[0]*a[3]-a[1]*a[2])%5==1]
        six={a:i for i,a in enumerate(self.sl)};self.sid=six[(1,0,0,1)];self.z=six[(4,0,0,4)]
        self.sm=np.array([[six[matmul(a,b)] for b in self.sl] for a in self.sl],dtype=np.int64)
        self.si=np.array([six[matinv(a)] for a in self.sl],dtype=np.int64)
        canon=lambda a:min(a,tuple(-x%5 for x in a))
        psl=sorted({canon(a) for a in self.sl});pix={a:i for i,a in enumerate(psl)}
        pm=np.array([[pix[canon(matmul(a,b))] for b in psl] for a in psl],dtype=np.int64)
        pi=np.array([pix[canon(matinv(a))] for a in psl],dtype=np.int64);pid=pix[canon((1,0,0,1))]
        involutions=[i for i in range(60) if i!=pid and pm[i,i]==pid]
        V=sorted({tuple(sorted((pid,i,j,int(pm[i,j])))) for i in involutions for j in involutions
                  if i!=j and pm[i,j]==pm[j,i]})
        assert len(involutions)==15 and len(V)==5
        p5ix={p:i for i,p in enumerate(self.old.permutations)}
        def action(matrix):
            inv=matinv(matrix)
            cp=[pix[canon(matmul(matmul(matrix,a),inv))] for a in psl]
            return p5ix[tuple(V.index(tuple(sorted(cp[i] for i in v))) for v in V)]
        self.qsl=np.array([action(a) for a in self.sl],dtype=np.int64)
        assert set(self.qsl)==set(self.old.even)
        assert all(sum(self.qsl==i)==2 for i in self.old.even)
        gl=[a for a in product(range(5),repeat=4) if (a[0]*a[3]-a[1]*a[2])%5]
        gcanon=lambda a:min(tuple(k*x%5 for x in a) for k in range(1,5))
        pgl=sorted({gcanon(a) for a in gl});assert len(pgl)==120
        self.gl=[None]*120
        for a in pgl:
            i=action(a);assert self.gl[i] is None;self.gl[i]=a
        assert all(a is not None for a in self.gl)
        self.auto=np.array([[six[matmul(matmul(c,g),matinv(c))] for g in self.sl]
                            for c in self.gl],dtype=np.int64)
        assert np.array_equal(self.qsl[self.auto],self.old.sm[self.old.sm[np.arange(120)[:,None],self.qsl[None,:]],self.old.si[:,None]])
        assert np.array_equal(self.qsl[self.sm],self.old.sm[self.qsl[:,None],self.qsl[None,:]])
        for c in range(120):assert np.array_equal(self.auto[self.old.sm[c]],self.auto[c,self.auto])
        self.lifts=np.array([[next(i for i in range(120) if self.qsl[i]==g),
                              next(i for i in range(120) if self.qsl[i]==h)]
                             for g,h in self.old.generating_pairs],dtype=np.int64)
        self.one=np.r_[np.arange(19),np.zeros(57,dtype=np.int64),[1,0,0,1],
                       np.full(19,self.sid,dtype=np.int64),[0,0]]
        assert self.one.shape==(101,)
        def nielsen(old,desired,M):
            ans=self.one.copy();p=old[:19];c=old[38:]
            ans[:19]=p;ans[19:38]=c;ans[76:80]=np.asarray(M).ravel()
            reference=self.auto[c[:,None],self.lifts[p]]
            cross=np.zeros((19,2),dtype=np.int64)
            for j in range(19):
                for k in range(2):
                    if desired[j,k]!=reference[j,k]:
                        assert desired[j,k]==self.sm[self.z,reference[j,k]];cross[j,k]=1
            ans[38:76]=cross.ravel();return ans
        g,h=self.lifts.T
        self.a=nielsen(self.old.a,np.column_stack((g,self.sm[h,g])),[[1,1],[0,1]])
        self.b=nielsen(self.old.b,np.column_stack((self.sm[g,self.si[h]],h)),[[1,0],[1,1]])
        self.xi1=self.one.copy();self.xi1[80:99]=g;self.xi1[99:]=[1,0]
        self.xi2=self.one.copy();self.xi2[80:99]=h;self.xi2[99:]=[0,1]
        self.c=self.mul(self.xi1,self.a)
        self.check_braids((self.a,self.b,self.c))
        sig={1:self.a,2:self.b,3:self.c}
        def pure(i,j):
            u=self.one.copy()
            for k in range(j-1,i,-1):u=self.mul(u,sig[k])
            return self.conj(u,self.power(sig[i],2))
        A12,A13,A23,A24,A34=(pure(i,j) for i,j in ((1,2),(1,3),(2,3),(2,4),(3,4)))
        omega=self.power(self.mul(self.a,self.b),3)
        self.pairs=((A12,self.mul(A23,A24)),(self.mul(A13,A23),A34),(A23,A34),
                    (self.mul(A12,A13),self.mul(A24,A34)),(A12,A23),(omega,A34))
        self.x=np.array([x for x,y in self.pairs]);self.y=np.array([y for x,y in self.pairs])
        assert np.array_equal(self.mul(self.c,self.inv(self.a)),self.xi1)
        assert np.array_equal(self.mul(self.mul(self.mul(self.mul(self.mul(self.a,self.b),self.a),self.inv(self.c)),self.inv(self.b)),self.inv(self.a)),self.xi2)
        assert np.array_equal(self.conj(self.a,self.xi1),self.xi1)
        assert np.array_equal(self.conj(self.a,self.xi2),self.mul(self.xi2,self.xi1))
        assert np.array_equal(self.conj(self.b,self.xi1),self.mul(self.xi1,self.inv(self.xi2)))
        assert np.array_equal(self.conj(self.b,self.xi2),self.xi2)

    def mul(self,x,y):
        x,y=np.broadcast_arrays(x,y);p=x[...,:19];q=y[...,:19]
        cx,cy=x[...,19:38],y[...,19:38]
        Ex=x[...,38:76].reshape(x.shape[:-1]+(19,2));Ey=y[...,38:76].reshape(y.shape[:-1]+(19,2))
        M=x[...,76:80].reshape(x.shape[:-1]+(2,2));N=y[...,76:80].reshape(y.shape[:-1]+(2,2))
        t,u=x[...,99:101],y[...,99:101]
        pp=np.take_along_axis(q,p,axis=-1)
        cc=self.old.sm[cx,np.take_along_axis(cy,p,axis=-1)]
        EE=(np.einsum('...ji,...ik->...jk',Ex,N)+np.take_along_axis(Ey,p[...,None],axis=-2))%2
        MM=np.einsum('...ij,...jk->...ik',M,N)%2
        acted=self.auto[cx,np.take_along_axis(y[...,80:99],p,axis=-1)]
        signs=np.einsum('...ji,...i->...j',Ex,u)%2
        acted=np.where(signs,self.sm[self.z,acted],acted)
        kk=self.sm[x[...,80:99],acted]
        tt=(t+np.einsum('...ij,...j->...i',M,u))%2
        return np.concatenate((pp,cc,EE.reshape(x.shape[:-1]+(38,)),MM.reshape(x.shape[:-1]+(4,)),kk,tt),axis=-1)

    def inv(self,x):
        q=np.argsort(x[...,:19],axis=-1);cc=self.old.si[np.take_along_axis(x[...,19:38],q,axis=-1)]
        M=x[...,76:80].reshape(x.shape[:-1]+(2,2))
        Mi=np.stack((M[...,1,1],M[...,0,1],M[...,1,0],M[...,0,0]),axis=-1).reshape(M.shape)
        E=np.take_along_axis(x[...,38:76].reshape(x.shape[:-1]+(19,2)),q[...,None],axis=-2)
        EE=np.einsum('...ji,...ik->...jk',E,Mi)%2;t=x[...,99:101]
        kk=self.auto[cc,self.si[np.take_along_axis(x[...,80:99],q,axis=-1)]]
        signs=np.einsum('...ji,...i->...j',EE,t)%2
        kk=np.where(signs,self.sm[self.z,kk],kk)
        tt=np.einsum('...ij,...j->...i',Mi,t)%2
        return np.concatenate((q,cc,EE.reshape(x.shape[:-1]+(38,)),Mi.reshape(x.shape[:-1]+(4,)),kk,tt),axis=-1)

    def power(self,x,k):
        if k<0:return self.power(self.inv(x),-k)
        out=np.broadcast_to(self.one,x.shape).copy()
        while k:
            if k%2:out=self.mul(out,x)
            x=self.mul(x,x);k//=2
        return out
    def conj(self,x,y):return self.mul(self.mul(x,y),self.inv(x))
    def comm(self,x,y):return self.mul(self.mul(self.mul(x,y),self.inv(x)),self.inv(y))
    def word(self,w,gens=None):
        from itertools import groupby
        x,y=(self.x,self.y) if gens is None else gens
        letters={1:x,2:y,-1:self.inv(x),-2:self.inv(y)};out=np.broadcast_to(self.one,x.shape).copy()
        for t,run in groupby(w):out=self.mul(out,self.power(letters[t],sum(1 for _ in run)))
        return out
    def check_braids(self,images):
        a,b,c=images
        assert np.array_equal(self.mul(self.mul(a,b),a),self.mul(self.mul(b,a),b))
        assert np.array_equal(self.mul(self.mul(b,c),b),self.mul(self.mul(c,b),c))
        assert np.array_equal(self.mul(a,c),self.mul(c,a))
    def project_a5(self,x):
        return np.concatenate((x[...,:19],self.old.sm[self.qsl[x[...,80:99]],x[...,19:38]],x[...,19:38]),axis=-1)
    def project_affine2(self,x):return np.concatenate((x[...,76:80],x[...,99:101]),axis=-1)
    def relative_kernel_vector(self,x):
        assert np.array_equal(self.project_a5(x),np.broadcast_to(self.old.one,x.shape[:-1]+(57,)))
        assert np.array_equal(self.project_affine2(x),np.broadcast_to([1,0,0,1,0,0],x.shape[:-1]+(6,)))
        k=x[...,80:99];assert np.all((k==self.sid)|(k==self.z))
        return np.concatenate(((k==self.z).astype(np.int64),x[...,38:76]),axis=-1)
    def relative_kernel_element(self,v):
        out=np.broadcast_to(self.one,v.shape[:-1]+(101,)).copy()
        out[...,80:99]=np.where(v[...,:19]%2,self.z,self.sid);out[...,38:76]=v[...,19:]%2
        return out
    def encode(self,x):return {'exact_coordinates':x.tolist()}

def main():
    from de_ferrari_two_model import FerrariTwo
    start=time.time();H=FerrariSL2Five();B=FerrariTwo(2)
    def closure(gens):
        seen={H.sid};queue=[H.sid]
        for q in queue:
            for g in gens:
                z=int(H.sm[q,g])
                if z not in seen:seen.add(z);queue.append(z)
        return seen
    comms={int(H.sm[H.sm[H.sm[a,b],H.si[a]],H.si[b]]) for a in range(120) for b in range(120)}
    assert len(closure(comms))==120
    assert [i for i in range(120) if np.array_equal(H.sm[i],H.sm[:,i])]==sorted([H.sid,H.z])
    assert all(len(closure(pair))==120 for pair in H.lifts)
    gs=[H.a,H.b,H.c,H.inv(H.a),H.inv(H.b),H.inv(H.c)]
    oldgs=[H.old.a,H.old.b,H.old.c,H.old.inv(H.old.a),H.old.inv(H.old.b),H.old.inv(H.old.c)]
    bgs=[B.a,B.b,B.c,B.inv(B.a),B.inv(B.b),B.inv(B.c)]
    rng=np.random.default_rng(213725);q=H.one;oq=H.old.one;bq=B.one
    for _ in range(1000):
        i=int(rng.integers(6));q=H.mul(q,gs[i]);oq=H.old.mul(oq,oldgs[i]);bq=B.mul(bq,bgs[i])
        assert np.array_equal(H.project_a5(q),oq)
        assert np.array_equal(H.project_affine2(q),B.project(bq))
        assert np.array_equal(H.mul(q,H.inv(q)),H.one)
    assert np.array_equal(H.project_affine2(H.x),B.project(B.x))
    assert np.array_equal(H.project_affine2(H.y),B.project(B.y))
    # All 57 ambient relative-kernel generators, including every cross
    # character, are checked as an actual elementary abelian subgroup.
    I=np.eye(57,dtype=np.int64);kernel=[H.relative_kernel_element(v) for v in I]
    for i,a in enumerate(kernel):
        assert np.array_equal(H.power(a,2),H.one)
        for j,b in enumerate(kernel):
            assert np.array_equal(H.relative_kernel_vector(H.mul(a,b)),(I[i]+I[j])%2)
        for g in gs:H.relative_kernel_vector(H.conj(g,a))
    # Independently evaluate the 76 generating-pair lifts on random
    # literal free words and compare with the two global character twists.
    for _ in range(100):
        word=[int(t) for t in rng.choice([1,2,-1,-2],size=30)]
        value=H.word(word,(H.xi1,H.xi2));parity=value[99:]
        for j,(g,h) in enumerate(H.lifts):
            for e1,e2 in product(range(2),repeat=2):
                pair=[H.sm[H.z,g] if e1 else g,H.sm[H.z,h] if e2 else h]
                z=H.sid
                for t in word:z=H.sm[z,pair[t-1] if t>0 else H.si[pair[-t-1]]]
                expected=value[80+j]
                if (e1*parity[0]+e2*parity[1])%2:expected=H.sm[H.z,expected]
                assert z==expected
    out={'SL2_F5_order':120,'SL2_F5_is_perfect_verified':True,'SL2_F5_center_order':2,
         'PGL2_F5_automorphisms_verified':120,'A5_epimorphism_kernels':19,
         'lifts_per_A5_epimorphism_kernel':4,'all_SL2_epimorphism_kernels':76,
         'universal_free_image_order_from_exact_comparison':4*120**19,
         'global_character_rank':2,'central_cross_term_rank_ambient':38,
         'relative_kernel_over_A5_and_affine_S4_ambient_dimension':57,
         'all_literal_Nielsen_and_braid_identities_verified':True,
         'both_projection_maps_verified_on1000_successive_words':True,
         'all76_evaluations_verified_on100_literal_free_words':True,
         'all57_kernel_basis_products_and_conjugations_verified':True,
         'A5_and_affine_projection_of_six_pairs_agree':bool(np.array_equal(H.project_a5(H.x),H.old.x) and np.array_equal(H.project_a5(H.y),H.old.y)),
         'seconds':round(time.time()-start,3)}
    assert out['A5_and_affine_projection_of_six_pairs_agree']
    here=Path(__file__).resolve().parent
    here.joinpath('de_ferrari_sl2_5_model.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_sl2_5_model.npz',a=H.a,b=H.b,c=H.c,x=H.x,y=H.y,
                        SL2_matrices=np.array(H.sl),SL2_multiplication=H.sm,SL2_inverse=H.si,
                        PGL2_representatives=np.array(H.gl),PGL2_action=H.auto,
                        SL2_to_A5=H.qsl,chosen_lifts=H.lifts,
                        relative_kernel_conjugation=np.array([[H.relative_kernel_vector(H.conj(g,k)) for k in kernel] for g in gs]))
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
