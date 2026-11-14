#!/usr/bin/env python3
"""Full A6 Ferrari model, with all inner, outer and free coordinates.

The exact 53 epikernels give A6^53.  Aut(A6) acts faithfully on its ten
Sylow-3 subgroups.  The holomorph embeds as
    (k,alpha) -> (Inn(k) alpha, alpha) in Aut(A6) x Aut(A6),
so two ten-point blocks per factor retain all information.  The stored
coordinates are the factor permutation and these two actual automorphisms.
"""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from sympy import factorint
from de_ferrari_two_model import FerrariTwo

HERE=Path(__file__).resolve().parent

def build_small_action():
    data=np.load(HERE/'de_ferrari_a6_kernels.npz')
    multiplication=data['A6_multiplication'];inverse=data['A6_inverse']
    maps=data['Aut_maps'];am=data['Aut_multiplication'];pairs=data['Aut_generator_pairs']
    autone=int(data['Aut_one']);ga,gb=map(int,pairs[autone])
    one=int(multiplication[0,inverse[0]])
    # In this actual A6 each nonidentity order-three element has a
    # centralizer of order nine.  The ten resulting subgroups are all
    # the Sylow-3 subgroups, by their order and Sylow conjugacy.
    sylow={}
    for g in np.flatnonzero(data['A6_orders']==3):
        c=tuple(map(int,np.flatnonzero(multiplication[g]==multiplication[:,g])))
        assert len(c)==9 and all(data['A6_orders'][h] in (1,3) for h in c)
        assert all(int(multiplication[a,b]) in c for a in c for b in c)
        sylow[c]=None
    sylows=sorted(sylow);assert len(sylows)==10
    index={q:i for i,q in enumerate(sylows)}
    action=np.array([[index[tuple(sorted(map(int,row[list(q)])))] for q in sylows]
                     for row in maps],dtype=np.int64)
    assert len({tuple(row) for row in action})==1440
    assert all(np.array_equal(np.sort(row),np.arange(10)) for row in action)
    for i in range(1440):assert np.array_equal(action[am[i]],action[i,action])
    adict={tuple(pair):i for i,pair in enumerate(pairs)}
    inner=np.array([adict[(int(multiplication[multiplication[g,ga],inverse[g]]),
                          int(multiplication[multiplication[g,gb],inverse[g]]))]
                    for g in range(360)],dtype=np.int64)
    assert len(set(map(int,inner)))==360
    assert np.array_equal(am[inner[:,None],inner[None,:]],inner[multiplication])
    assert not np.any(data['Aut_outer_coordinates'][inner])
    # Direct finite simplicity certificate, without a classification
    # identification: every nonidentity conjugacy class normally generates.
    unseen=set(range(360))-{one};normal_orders=[]
    while unseen:
        g=min(unseen)
        conjugates=set(map(int,multiplication[multiplication[:,g],inverse]))
        unseen-=conjugates;found={one};queue=[one]
        for h in queue:
            for k in conjugates:
                v=int(multiplication[h,k])
                if v not in found:found.add(v);queue.append(v)
        assert len(found)==360;normal_orders.append(len(found))
    assert len(normal_orders)==6
    cert={'ten_Sylow3_subgroups':[list(q) for q in sylows],
          'all_1440_automorphisms_act_faithfully':True,
          'all_1440_squared_composition_checks':True,
          'nonidentity_class_normal_closure_orders':normal_orders}
    return action,inner,cert

class FerrariA6(FerrariTwo):
    def __init__(self):
        data=np.load(HERE/'de_ferrari_a6_kernels.npz')
        self.n=len(data['kernel_representatives']);self.am=data['Aut_multiplication']
        self.ai=data['Aut_inverse'];self.autone=int(data['Aut_one'])
        self.outer=data['Aut_outer_coordinates'];self.genpairs=data['kernel_representatives']
        self.small,self.inner,self.small_certificate=build_small_action()
        self.one=np.r_[np.arange(self.n),np.full(2*self.n,self.autone,dtype=np.int64)]
        ca=data['a_automorphisms'];cb=data['b_automorphisms']
        self.a=np.r_[data['a_permutation'],ca,ca]
        self.b=np.r_[data['b_permutation'],cb,cb]
        self.c=self.a.copy()
        self.c[self.n:2*self.n]=self.am[self.inner[self.genpairs[:,0]],ca]
        self.check_braids((self.a,self.b,self.c))
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
        self.xi1=self.mul(self.c,self.inv(self.a))
        self.xi2=self.mul(self.mul(self.mul(self.mul(self.mul(self.a,self.b),self.a),self.inv(self.c)),self.inv(self.b)),self.inv(self.a))
        for xi,j in ((self.xi1,0),(self.xi2,1)):
            expected=self.one.copy();expected[self.n:2*self.n]=self.inner[self.genpairs[:,j]]
            assert np.array_equal(xi,expected)
        assert np.array_equal(self.conj(self.a,self.xi1),self.xi1)
        assert np.array_equal(self.conj(self.a,self.xi2),self.mul(self.xi2,self.xi1))
        assert np.array_equal(self.conj(self.b,self.xi1),self.mul(self.xi1,self.inv(self.xi2)))
        assert np.array_equal(self.conj(self.b,self.xi2),self.xi2)
    def mul(self,x,y):
        x,y=np.broadcast_arrays(x,y);p=x[...,:self.n]
        q=np.take_along_axis(y[...,:self.n],p,axis=-1)
        left=self.am[x[...,self.n:2*self.n],np.take_along_axis(y[...,self.n:2*self.n],p,axis=-1)]
        right=self.am[x[...,2*self.n:],np.take_along_axis(y[...,2*self.n:],p,axis=-1)]
        return np.concatenate((q,left,right),axis=-1)
    def inv(self,x):
        q=np.argsort(x[...,:self.n],axis=-1)
        left=self.ai[np.take_along_axis(x[...,self.n:2*self.n],q,axis=-1)]
        right=self.ai[np.take_along_axis(x[...,2*self.n:],q,axis=-1)]
        return np.concatenate((q,left,right),axis=-1)
    def permutation(self,x,action_only=False):
        assert x.ndim==1
        arrays=[x[2*self.n:]] if action_only else [x[self.n:2*self.n],x[2*self.n:]]
        width=10*len(arrays);out=[]
        for j in range(self.n):
            for k,a in enumerate(arrays):
                out.extend((width*int(x[j])+10*k+self.small[self.ai[a[j]]]).tolist())
        return Permutation(out)
    def project_outer(self,x):
        assert np.array_equal(self.outer[x[...,self.n:2*self.n]],self.outer[x[...,2*self.n:]])
        return np.concatenate((x[...,:self.n],self.outer[x[...,2*self.n:]]),axis=-1)
    def encode(self,x):
        return {'factor_permutation':x[:self.n].tolist(),
                'left_actual_Aut_A6_indices':x[self.n:2*self.n].tolist(),
                'right_actual_Aut_A6_indices':x[2*self.n:].tolist()}

def main():
    start=time.time();H=FerrariA6()
    from de_ferrari_a6_kernels import FerrariA6Kernel
    small=FerrariA6Kernel(outer=True)
    for a,b in ((H.a,small.a),(H.b,small.b),(H.c,small.c)):
        assert np.array_equal(H.project_outer(a),b)
    gs=(H.a,H.b,H.c,H.inv(H.a),H.inv(H.b),H.inv(H.c))
    for x in gs:
        for y in gs:
            assert H.permutation(H.mul(x,y))==H.permutation(x)*H.permutation(y)
            assert np.array_equal(H.project_outer(H.mul(x,y)),small.mul(H.project_outer(x),H.project_outer(y)))
    print('exact full model and all generator multiplication/projection checks PASS',flush=True)
    A=PermutationGroup([H.permutation(H.a,True),H.permutation(H.b,True)])
    aorder=int(A.order());print('full Nielsen order',aorder,flush=True)
    # The complete epikernel enumeration and the direct simplicity checks
    # prove the free image is A6^53 by the subdirect-product lemma.  This
    # determines the target order without a second enormous BSGS run.
    torder=360**53*aorder
    outer_order=json.loads((HERE/'de_ferrari_a6_kernel_targets.json').read_text())['targets'][1]['target_order']
    out={**H.small_certificate,'epimorphism_kernel_count':53,'free_kernel_order':360**53,
         'Nielsen_image_order':aorder,'four_strand_target_order':torder,
         'Nielsen_image_factorization':factorint(aorder),'four_strand_target_factorization':factorint(torder),
         'target_order_from_exact_free_image_and_Nielsen_image':True,
         'outer_quotient_order':outer_order,'kernel_over_outer_order':torder//outer_order,
         'faithful_permutation_degree':20*H.n,
         'six_pure_pairs_commute':[bool(np.array_equal(H.comm(x,y),H.one)) for x,y in H.pairs],
         'braid_generator_orders':[int(H.permutation(g).order()) for g in (H.a,H.b,H.c)],
         'literal_Ferrari_actions_and_all_braid_relations_checked':True,
         'exact_projection_to_saved_outer_target':True,'seconds':round(time.time()-start,3)}
    np.savez_compressed(HERE/'de_ferrari_a6_model.npz',a=H.a,b=H.b,c=H.c,x=H.x,y=H.y,
                        Aut_Sylow3_action=H.small,inner_A6_automorphisms=H.inner)
    (HERE/'de_ferrari_a6_model.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
