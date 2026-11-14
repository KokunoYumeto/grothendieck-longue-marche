#!/usr/bin/env python3
"""Exact universal Ferrari target from every SL2(F3) epimorphism kernel.

The actual matrix quotient and all Aut(SL2(F3))-orbits are retained.
No direct-product assertion about the free image is used: its order is
computed in a faithful holomorph permutation action.  All files are new.
"""
from pathlib import Path
from itertools import product
from hashlib import sha256
import json
import time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup
from de_ferrari_two_model import FerrariTwo

HERE = Path(__file__).resolve().parent


class FerrariSL23(FerrariTwo):
    def __init__(self):
        gl = [t for t in product(range(3), repeat=4)
              if (t[0]*t[3]-t[1]*t[2]) % 3]
        self.elements = [t for t in gl if (t[0]*t[3]-t[1]*t[2]) % 3 == 1]
        sd = {t:i for i,t in enumerate(self.elements)}
        def mm(a,b):
            return tuple(v % 3 for v in (a[0]*b[0]+a[1]*b[2],
                        a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],
                        a[2]*b[1]+a[3]*b[3]))
        def mi(a):
            d = pow((a[0]*a[3]-a[1]*a[2]) % 3, -1, 3)
            return tuple(d*v % 3 for v in (a[3],-a[1],-a[2],a[0]))
        self.uid = sd[(1,0,0,1)]
        self.sm = np.array([[sd[mm(a,b)] for b in self.elements]
                           for a in self.elements], dtype=np.int64)
        self.si = np.array([sd[mi(a)] for a in self.elements],dtype=np.int64)
        automorphisms = []
        for a in gl:
            image = tuple(sd[mm(mm(a,b),mi(a))] for b in self.elements)
            if image not in automorphisms:
                automorphisms.append(image)
        self.auto = np.array(automorphisms,dtype=np.int64)
        ad = {tuple(a):i for i,a in enumerate(self.auto)}
        self.autone = ad[tuple(range(24))]
        self.am = np.array([[ad[tuple(a[b])] for b in self.auto]
                           for a in self.auto],dtype=np.int64)
        self.ai = np.array([ad[tuple(np.argsort(a))] for a in self.auto],dtype=np.int64)
        assert len(gl)==48 and len(self.elements)==24 and len(self.auto)==24
        for a in self.auto:
            assert np.array_equal(a[self.sm], self.sm[a[:,None],a[None,:]])
        def subgroup(gens):
            seen={self.uid}; todo=[self.uid]
            for z in todo:
                for g in gens:
                    w=int(self.sm[z,g])
                    if w not in seen:
                        seen.add(w);todo.append(w)
            return todo
        self.generating_pairs = [(g,h) for g in range(24) for h in range(24)
                                 if len(subgroup((g,h)))==24]
        self.kernel_representatives=[]; coordinate={}
        for pair in self.generating_pairs:
            if pair in coordinate:
                continue
            j=len(self.kernel_representatives)
            self.kernel_representatives.append(pair)
            for a,mp in enumerate(self.auto):
                key=tuple(map(int,mp[list(pair)]))
                assert key not in coordinate
                coordinate[key]=(j,a)
        assert len(coordinate)==len(self.generating_pairs)
        # A generating pair determines any automorphism. Every generating
        # pair satisfying the complete source Cayley relations is tested,
        # so the retained GL-conjugations are proved to be all automorphisms.
        base=self.kernel_representatives[0]
        parent={self.uid:None}; words={self.uid:[]}; order=[self.uid]
        for z in order:
            for j,g in enumerate(base):
                w=int(self.sm[z,g])
                if w not in parent:
                    parent[w]=(z,j);words[w]=words[z]+[j];order.append(w)
        assert len(order)==24
        all_maps=[]
        for pair in self.generating_pairs:
            image=np.full(24,-1,dtype=np.int64);image[self.uid]=self.uid
            for v in order[1:]:
                z,j=parent[v];image[v]=self.sm[image[z],pair[j]]
            if all(np.array_equal(image[self.sm[:,g]],self.sm[image,image[g]]) for g in base):
                all_maps.append(tuple(image))
        assert set(all_maps)==set(map(tuple,self.auto))
        self.n=len(self.kernel_representatives); n=self.n
        self.width=3*n
        self.ps=slice(0,n); self.as_=slice(n,2*n); self.ks=slice(2*n,3*n)
        self.one=np.r_[np.arange(n),np.full(n,self.autone),np.full(n,self.uid)]
        pa=[];ca=[];pb=[];cb=[]
        for g,h in self.kernel_representatives:
            p,a=coordinate[(g,int(self.sm[h,g]))];pa.append(p);ca.append(a)
            p,a=coordinate[(int(self.sm[g,self.si[h]]),h)];pb.append(p);cb.append(a)
        self.a=np.r_[pa,ca,np.full(n,self.uid)]
        self.b=np.r_[pb,cb,np.full(n,self.uid)]
        self.xi1=self.one.copy();self.xi1[self.ks]=[g for g,h in self.kernel_representatives]
        self.xi2=self.one.copy();self.xi2[self.ks]=[h for g,h in self.kernel_representatives]
        self.c=self.mul(self.xi1,self.a)
        self.check_braids((self.a,self.b,self.c))
        assert np.array_equal(self.conj(self.a,self.xi1),self.xi1)
        assert np.array_equal(self.conj(self.a,self.xi2),self.mul(self.xi2,self.xi1))
        assert np.array_equal(self.conj(self.b,self.xi1),self.mul(self.xi1,self.inv(self.xi2)))
        assert np.array_equal(self.conj(self.b,self.xi2),self.xi2)
        assert np.array_equal(self.mul(self.c,self.inv(self.a)),self.xi1)
        literal=self.mul(self.mul(self.mul(self.mul(self.mul(self.a,self.b),self.a),self.inv(self.c)),self.inv(self.b)),self.inv(self.a))
        assert np.array_equal(literal,self.xi2)
        sig={1:self.a,2:self.b,3:self.c}
        def pure(i,j):
            h=self.one.copy()
            for k in range(j-1,i,-1):h=self.mul(h,sig[k])
            return self.conj(h,self.power(sig[i],2))
        A12,A13,A23,A24,A34=(pure(i,j) for i,j in ((1,2),(1,3),(2,3),(2,4),(3,4)))
        omega=self.power(self.mul(self.a,self.b),3)
        self.pairs=((A12,self.mul(A23,A24)),(self.mul(A13,A23),A34),
                    (A23,A34),(self.mul(A12,A13),self.mul(A24,A34)),
                    (A12,A23),(omega,A34))
        self.x=np.array([x for x,y in self.pairs]);self.y=np.array([y for x,y in self.pairs])
        self.coordinate=coordinate

    def mul(self,x,y):
        x,y=np.broadcast_arrays(x,y);p=x[...,self.ps]
        q=np.take_along_axis(y[...,self.ps],p,axis=-1)
        a=x[...,self.as_]; b=np.take_along_axis(y[...,self.as_],p,axis=-1)
        k=self.sm[x[...,self.ks],self.auto[a,np.take_along_axis(y[...,self.ks],p,axis=-1)]]
        return np.concatenate((q,self.am[a,b],k),axis=-1)

    def inv(self,x):
        q=np.argsort(x[...,self.ps],axis=-1)
        a=self.ai[np.take_along_axis(x[...,self.as_],q,axis=-1)]
        k=self.auto[a,self.si[np.take_along_axis(x[...,self.ks],q,axis=-1)]]
        return np.concatenate((q,a,k),axis=-1)

    def permutation(self,x,action_only=False):
        assert x.ndim==1
        out=[]
        for j in range(self.n):
            p=int(x[j]);a=int(x[self.n+j]);k=self.uid if action_only else int(x[2*self.n+j])
            out.extend((24*p+self.auto[self.ai[a],self.sm[self.si[k],np.arange(24)]]).tolist())
        return Permutation(out)

    def encode(self,x):
        return {'exact_coordinates':np.asarray(x).tolist()}


def main():
    started=time.time(); H=FerrariSL23()
    print('SL2(F3) ordered generating pairs',len(H.generating_pairs),
          'Aut-orbits',H.n,'permutation degree',24*H.n,flush=True)
    gens=(H.a,H.b,H.c,H.inv(H.a),H.inv(H.b),H.inv(H.c))
    for x in gens:
        assert np.array_equal(H.mul(x,H.inv(x)),H.one)
        for y in gens:
            assert H.permutation(H.mul(x,y))==H.permutation(x)*H.permutation(y)
    K=PermutationGroup([H.permutation(H.xi1),H.permutation(H.xi2)])
    A=PermutationGroup([H.permutation(H.a),H.permutation(H.b)])
    T=PermutationGroup([H.permutation(H.a),H.permutation(H.b),H.permutation(H.c)])
    ko,ao,to=map(lambda g:int(g.order()),(K,A,T))
    assert to==ko*ao
    print('Exact free/Nielsen/target orders',ko,ao,to,flush=True)
    derived=K.derived_subgroup(); do=int(derived.order())
    second=derived.derived_subgroup(); ddo=int(second.order())
    quotients=[]
    for x,y in H.pairs:
        G=PermutationGroup([H.permutation(x),H.permutation(y)])
        quotients.append({'order':int(G.order()),'commute':bool(np.array_equal(H.comm(x,y),H.one)),
                          'x_order':int(H.permutation(x).order()),'y_order':int(H.permutation(y).order())})
    out={'status':'PASS_EXACT_UNIVERSAL_SL23_FERRARI_MODEL',
         'SL2_F3_order':24,'all_Aut_maps':24,'ordered_generating_pairs':len(H.generating_pairs),
         'exact_epimorphism_kernel_count':H.n,'kernel_representatives':H.kernel_representatives,
         'faithful_permutation_degree':24*H.n,
         'actual_free_image_order':ko,'actual_Nielsen_image_order':ao,'actual_B4_target_order':to,
         'actual_free_derived_order':do,'actual_free_second_derived_order':ddo,
         'six_actual_pure_pair_images':quotients,
         'braid_generator_orders':[int(H.permutation(g).order()) for g in (H.a,H.b,H.c)],
         'all_36_generator_product_permutation_comparisons':True,
         'all_complete_matrix_group_automorphisms_checked':True,
         'exact_source_fibre_comparison_not_yet_claimed':True,
         'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'a_cm_sl23_model.npz',a=H.a,b=H.b,c=H.c,x=H.x,y=H.y,
                        xi1=H.xi1,xi2=H.xi2,SL2_elements=np.array(H.elements),
                        SL2_multiplication=H.sm,SL2_inverse=H.si,SL2_one=np.array(H.uid),
                        Aut_maps=H.auto,Aut_multiplication=H.am,Aut_inverse=H.ai,
                        kernel_representatives=np.array(H.kernel_representatives))
    (HERE/'a_cm_sl23_model.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
