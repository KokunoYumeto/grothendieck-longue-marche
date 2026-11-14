#!/usr/bin/env python3
"""Actual Ferrari model from all epimorphisms to the hyperoval A6 cover.

The free image is U^53 x C3^2, where |U|=1080 is the proved perfect
central-three cover.  All nine lifts of each A6 epikernel are recovered
by the two global C3 characters.  The actual exceptional outer action
on the centre is retained in every composition and inverse.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json,time
import numpy as np
from de_ferrari_a6_model import FerrariA6
from de_ferrari_two_model import FerrariTwo
from de_ferrari_mod9_lift import Jacobi

HERE=Path(__file__).resolve().parent
STEM='de_a6_triple_model'


class FerrariA6Triple(FerrariTwo):
    def __init__(self):
        raw=np.load(HERE/'de_a6_triple_cover.npz')
        old=np.load(HERE/'de_ferrari_a6_kernels.npz')
        self.old=FerrariA6();self.n=53
        self.um=raw['cover_multiplication'];self.ui=raw['cover_inverse']
        self.uid=int(raw['cover_one']);self.z=int(raw['cover_central_generator'])
        self.zpowers=np.array([self.uid,self.z,self.um[self.z,self.z]],dtype=np.int64)
        self.zlog=np.full(1080,-1,dtype=np.int64);self.zlog[self.zpowers]=np.arange(3)
        self.quotient=raw['A6_quotient'];self.section=raw['A6_section']
        self.auto=raw['all_lifted_automorphisms']
        self.character=raw['automorphism_central_character'].astype(np.int64)
        self.am=old['Aut_multiplication'];self.ai=old['Aut_inverse']
        self.autone=int(old['Aut_one'])
        self.lifts=self.section[old['kernel_representatives']]
        n=self.n;self.ps=slice(0,n);self.cs=slice(n,2*n)
        self.es=slice(2*n,4*n);self.ms=slice(4*n,4*n+4)
        self.ks=slice(4*n+4,5*n+4);self.ts=slice(5*n+4,5*n+6)
        self.width=5*n+6
        self.one=np.r_[np.arange(n),np.full(n,self.autone),np.zeros(2*n,dtype=np.int64),
                       [1,0,0,1],np.full(n,self.uid),[0,0]].astype(np.int64)
        assert self.one.shape==(271,)
        def nielsen(p,alpha,desired,M):
            out=self.one.copy();out[self.ps]=p;out[self.cs]=alpha
            out[self.ms]=np.asarray(M).ravel()
            reference=self.auto[alpha[:,None],self.lifts[p]]
            difference=self.um[desired,self.ui[reference]]
            cross=self.zlog[difference];assert np.all(cross>=0)
            out[self.es]=cross.ravel();return out
        g,h=self.lifts.T
        self.a=nielsen(old['a_permutation'],old['a_automorphisms'],
                       np.column_stack((g,self.um[h,g])),[[1,1],[0,1]])
        self.b=nielsen(old['b_permutation'],old['b_automorphisms'],
                       np.column_stack((self.um[g,self.ui[h]],h)),[[1,0],[2,1]])
        self.xi1=self.one.copy();self.xi1[self.ks]=g;self.xi1[self.ts]=[1,0]
        self.xi2=self.one.copy();self.xi2[self.ks]=h;self.xi2[self.ts]=[0,1]
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
        x,y=np.broadcast_arrays(x,y);n=self.n;p=x[...,self.ps];q=y[...,self.ps]
        alpha=x[...,self.cs];beta=y[...,self.cs]
        E=x[...,self.es].reshape(x.shape[:-1]+(n,2))
        D=y[...,self.es].reshape(y.shape[:-1]+(n,2))
        M=x[...,self.ms].reshape(x.shape[:-1]+(2,2))
        N=y[...,self.ms].reshape(y.shape[:-1]+(2,2))
        pp=np.take_along_axis(q,p,axis=-1)
        cc=self.am[alpha,np.take_along_axis(beta,p,axis=-1)]
        EE=(np.einsum('...ji,...ik->...jk',E,N)
            +self.character[alpha][...,None]*np.take_along_axis(D,p[...,None],axis=-2))%3
        MM=np.einsum('...ij,...jk->...ik',M,N)%3
        acted=self.auto[alpha,np.take_along_axis(y[...,self.ks],p,axis=-1)]
        shift=np.einsum('...ji,...i->...j',E,y[...,self.ts])%3
        kk=self.um[x[...,self.ks],self.um[self.zpowers[shift],acted]]
        tt=(x[...,self.ts]+np.einsum('...ij,...j->...i',M,y[...,self.ts]))%3
        return np.concatenate((pp,cc,EE.reshape(x.shape[:-1]+(2*n,)),
                               MM.reshape(x.shape[:-1]+(4,)),kk,tt),axis=-1)

    def inv(self,x):
        n=self.n;q=np.argsort(x[...,self.ps],axis=-1)
        beta=self.ai[np.take_along_axis(x[...,self.cs],q,axis=-1)]
        M=x[...,self.ms].reshape(x.shape[:-1]+(2,2))
        det=(M[...,0,0]*M[...,1,1]-M[...,0,1]*M[...,1,0])%3
        assert np.all(det)
        Mi=(np.stack((M[...,1,1],-M[...,0,1],-M[...,1,0],M[...,0,0]),axis=-1)
            .reshape(M.shape)*det[...,None,None])%3
        E=np.take_along_axis(x[...,self.es].reshape(x.shape[:-1]+(n,2)),q[...,None],axis=-2)
        EE=(-self.character[beta][...,None]*np.einsum('...ji,...ik->...jk',E,Mi))%3
        t=x[...,self.ts]
        kk=self.auto[beta,self.ui[np.take_along_axis(x[...,self.ks],q,axis=-1)]]
        shift=-np.einsum('...ji,...i->...j',EE,t)%3
        kk=self.um[self.zpowers[shift],kk]
        tt=-np.einsum('...ij,...j->...i',Mi,t)%3
        return np.concatenate((q,beta,EE.reshape(x.shape[:-1]+(2*n,)),
                               Mi.reshape(x.shape[:-1]+(4,)),kk,tt),axis=-1)

    def project_a6(self,x):
        alpha=x[...,self.cs]
        left=self.am[self.old.inner[self.quotient[x[...,self.ks]]],alpha]
        return np.concatenate((x[...,self.ps],left,alpha),axis=-1)

    def project_affine3(self,x):
        return np.concatenate((x[...,self.ms],x[...,self.ts]),axis=-1)

    def relative_kernel_vector(self,x):
        assert np.array_equal(self.project_a6(x),np.broadcast_to(self.old.one,x.shape[:-1]+(3*self.n,)))
        assert np.array_equal(self.project_affine3(x),np.broadcast_to([1,0,0,1,0,0],x.shape[:-1]+(6,)))
        central=self.zlog[x[...,self.ks]];assert np.all(central>=0)
        return np.concatenate((central,x[...,self.es]),axis=-1)

    def relative_kernel_element(self,v):
        out=np.broadcast_to(self.one,v.shape[:-1]+(self.width,)).copy()
        out[...,self.ks]=self.zpowers[v[...,:self.n]%3]
        out[...,self.es]=v[...,self.n:]%3
        return out

    def encode(self,x):return {'exact_coordinates':x.tolist()}


def main():
    started=time.time()
    deps=['de_a6_triple_cover.npz','de_ferrari_a6_kernels.npz','de_ferrari_a6_model.npz']
    hashes={p:sha256((HERE/p).read_bytes()).hexdigest() for p in deps}
    H=FerrariA6Triple();J=Jacobi(3);rng=np.random.default_rng(13861113)
    def generated(gens):
        seen={H.uid};todo=[H.uid]
        for v in todo:
            for g in gens:
                w=int(H.um[v,g])
                if w not in seen:seen.add(w);todo.append(w)
        return len(todo)
    assert all(generated(pair)==1080 for pair in H.lifts)
    gs=[H.a,H.b,H.c,H.inv(H.a),H.inv(H.b),H.inv(H.c)]
    olds=[H.old.a,H.old.b,H.old.c,H.old.inv(H.old.a),H.old.inv(H.old.b),H.old.inv(H.old.c)]
    affs=[J.a,J.b,J.c,J.inv(J.a),J.inv(J.b),J.inv(J.c)]
    for g,old,aff in zip(gs,olds,affs):
        assert np.array_equal(H.project_a6(g),old)
        assert np.array_equal(H.project_affine3(g),aff[:6])
        assert np.array_equal(H.mul(g,H.inv(g)),H.one)
        for h in gs:
            assert np.array_equal(H.project_a6(H.mul(g,h)),H.old.mul(H.project_a6(g),H.project_a6(h)))
    q=H.one.copy();oq=H.old.one.copy();aq=J.one.copy()
    for _ in range(1000):
        i=int(rng.integers(6));q=H.mul(q,gs[i]);oq=H.old.mul(oq,olds[i]);aq=J.mul(aq,affs[i])
        assert np.array_equal(H.project_a6(q),oq)
        assert np.array_equal(H.project_affine3(q),aq[:6])
        assert np.array_equal(H.mul(q,H.inv(q)),H.one)
    # Check the entire ambient coordinate law on independent arbitrary
    # factors, including outer automorphisms acting nontrivially on C3.
    GL=np.array([np.array(v).reshape(2,2) for v in product(range(3),repeat=4)
                 if (v[0]*v[3]-v[1]*v[2])%3],dtype=np.int64)
    assert len(GL)==48
    def random_element():
        u=H.one.copy();u[H.ps]=rng.permutation(H.n);u[H.cs]=rng.integers(1440,size=H.n)
        u[H.es]=rng.integers(3,size=2*H.n);u[H.ms]=GL[int(rng.integers(48))].ravel()
        u[H.ks]=rng.integers(1080,size=H.n);u[H.ts]=rng.integers(3,size=2)
        return u
    for _ in range(100):
        u,v,w=(random_element() for _ in range(3))
        assert np.array_equal(H.mul(H.mul(u,v),w),H.mul(u,H.mul(v,w)))
        assert np.array_equal(H.mul(u,H.inv(u)),H.one)
        assert np.array_equal(H.mul(H.inv(u),u),H.one)
    I=np.eye(159,dtype=np.int64);kernel=H.relative_kernel_element(I)
    for i,k in enumerate(kernel):
        assert np.array_equal(H.power(k,3),H.one)
        assert np.array_equal(H.relative_kernel_vector(H.mul(k,kernel)),(I[i]+I)%3)
    actions=np.array([H.relative_kernel_vector(H.conj(g,kernel)) for g in gs])
    for i,g in enumerate(gs):
        for j,h in enumerate(gs):
            actual=H.relative_kernel_vector(H.conj(H.mul(g,h),kernel))
            assert np.array_equal(actual,actions[j]@actions[i]%3)
    # Every one of the 477 epikernels is explicitly recovered by the
    # corresponding global central character on actual free words.
    for _ in range(50):
        word=[int(v) for v in rng.choice([1,2,-1,-2],size=31)]
        value=H.word(word,(H.xi1,H.xi2));chars=value[H.ts]
        for j,(g,h) in enumerate(H.lifts):
            for e1,e2 in product(range(3),repeat=2):
                pair=[H.um[H.zpowers[e1],g],H.um[H.zpowers[e2],h]];v=H.uid
                for letter in word:
                    v=int(H.um[v,pair[letter-1] if letter>0 else H.ui[pair[-letter-1]]])
                expected=H.um[H.zpowers[(e1*chars[0]+e2*chars[1])%3],value[H.ks][j]]
                assert v==expected
    braid_orders=[]
    for g in gs[:3]:
        q=H.one.copy()
        for k in range(1,181):
            q=H.mul(q,g)
            if np.array_equal(q,H.one):braid_orders.append(k);break
        else:raise AssertionError('Order does not divide the exact 180 bound')
    assert np.array_equal(H.project_a6(H.x),H.old.x)
    assert np.array_equal(H.project_a6(H.y),H.old.y)
    assert np.array_equal(H.project_affine3(H.x),J.x[:,:6])
    assert np.array_equal(H.project_affine3(H.y),J.y[:,:6])
    out={'status':'PASS_EXACT_CENTRAL_THREE_FERRARI_MODEL',
         'cover_order':1080,'chosen_A6_epikernels':53,'lifts_per_epikernel':9,
         'all_cover_epimorphism_kernel_count':477,
         'free_image_order_from_proved_central_perfect_comparison':9*1080**53,
         'global_abelian_character_rank':2,'central_cross_term_rank_ambient':106,
         'relative_kernel_over_A6_and_affine3_ambient_dimension':159,
         'actual_outer_centre_character_retained':True,
         'all_53_chosen_lift_pairs_generate_cover':True,
         'all_literal_Ferrari_and_braid_relations_checked':True,
         'all_six_pure_evaluation_projection_pairs_checked':True,
         'successive_braid_word_projection_checks':1000,
         'independent_ambient_associativity_and_inverse_checks':100,
         'all_159_squared_kernel_basis_products_and_conjugation_laws_checked':True,
         'all_477_evaluations_on_literal_free_words_checked':50,
         'braid_generator_orders':braid_orders,'source_sha256':hashes,
         'no_source_fibre_lifting_claim_in_this_model':True,
         'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/(STEM+'.npz'),a=H.a,b=H.b,c=H.c,x=H.x,y=H.y,
                        xi1=H.xi1,xi2=H.xi2,chosen_lift_pairs=H.lifts,
                        relative_kernel_conjugation=actions)
    (HERE/(STEM+'.json')).write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/p).read_bytes()).hexdigest()==v for p,v in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
