#!/usr/bin/env python3
"""Literal Ferrari quotient from the A5 epimorphisms of a free group.

There are 19 kernels modulo Aut(A5)=S5.  The free evaluation image is
A5^19.  Nielsen substitutions permute the factors and conjugate them
by recorded S5 elements.  A faithful degree-190 permutation model of
the resulting semidirect product uses (k c,c) on two five-point blocks
per factor.  All operations below are exact finite-group operations.
"""
from pathlib import Path
from itertools import permutations
import json,time
import numpy as np
from de_ferrari_two_model import FerrariTwo

class FerrariA5(FerrariTwo):
    def __init__(self,orbit=None):
        self.permutations=list(permutations(range(5)))
        pd={p:i for i,p in enumerate(self.permutations)}
        self.sm=np.array([[pd[tuple(p[k] for k in q)] for q in self.permutations]
                         for p in self.permutations],dtype=np.int64)
        self.si=np.array([next(j for j in range(120) if self.sm[i,j]==0) for i in range(120)],dtype=np.int64)
        self.even=[i for i,p in enumerate(self.permutations) if sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2==0]
        self.sign=np.array([0 if i in self.even else 1 for i in range(120)],dtype=np.int64)
        def generates(g,h):
            seen={0};todo=[0]
            for z in todo:
                for a in (g,h):
                    w=int(self.sm[z,a])
                    if w not in seen:seen.add(w);todo.append(w)
            return len(seen)==60
        pairs=[(g,h) for g in self.even for h in self.even if generates(g,h)]
        assert len(pairs)==2280
        self.all_pairs=pairs;classes=[];pair_coordinate={}
        for g,h in pairs:
            if (g,h) in pair_coordinate:continue
            j=len(classes);classes.append((g,h))
            for c in range(120):
                pair=tuple(int(self.sm[self.sm[c,z],self.si[c]]) for z in (g,h))
                assert pair not in pair_coordinate
                pair_coordinate[pair]=(j,c)
        assert len(classes)==19 and len(pair_coordinate)==2280
        pa=[];ca=[];pb=[];cb=[]
        for g,h in classes:
            p,c=pair_coordinate[(g,int(self.sm[h,g]))];pa.append(p);ca.append(c)
            p,c=pair_coordinate[(int(self.sm[g,self.si[h]]),h)];pb.append(p);cb.append(c)
        orbits=[];seen=set()
        for j in range(19):
            if j in seen:continue
            todo=[j];seen.add(j)
            for z in todo:
                for p in (pa,pb):
                    if p[z] not in seen:seen.add(p[z]);todo.append(p[z])
            orbits.append(sorted(todo))
        self.kernel_classes=classes;self.kernel_class_orbits=orbits
        chosen=list(range(19)) if orbit is None else orbits[orbit]
        self.chosen=chosen;self.n=len(chosen);renumber={j:i for i,j in enumerate(chosen)}
        self.generating_pairs=[classes[j] for j in chosen]
        self.one=np.r_[np.arange(self.n),np.zeros(2*self.n,dtype=np.int64)]
        self.a=np.array([renumber[pa[j]] for j in chosen]+[ca[j] for j in chosen]*2,dtype=np.int64)
        self.b=np.array([renumber[pb[j]] for j in chosen]+[cb[j] for j in chosen]*2,dtype=np.int64)
        self.c=self.a.copy()
        self.c[self.n:2*self.n]=self.sm[[g for g,h in self.generating_pairs],self.a[self.n:2*self.n]]
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
        expected=self.one.copy();expected[self.n:2*self.n]=[g for g,h in self.generating_pairs]
        assert np.array_equal(self.xi1,expected)
        expected=self.one.copy();expected[self.n:2*self.n]=[h for g,h in self.generating_pairs]
        assert np.array_equal(self.xi2,expected)
        assert np.array_equal(self.conj(self.a,self.xi1),self.xi1)
        assert np.array_equal(self.conj(self.a,self.xi2),self.mul(self.xi2,self.xi1))
        assert np.array_equal(self.conj(self.b,self.xi1),self.mul(self.xi1,self.inv(self.xi2)))
        assert np.array_equal(self.conj(self.b,self.xi2),self.xi2)
    def mul(self,x,y):
        x,y=np.broadcast_arrays(x,y);p=x[...,:self.n]
        qp=np.take_along_axis(y[...,:self.n],p,axis=-1)
        L=self.sm[x[...,self.n:2*self.n],np.take_along_axis(y[...,self.n:2*self.n],p,axis=-1)]
        R=self.sm[x[...,2*self.n:],np.take_along_axis(y[...,2*self.n:],p,axis=-1)]
        return np.concatenate((qp,L,R),axis=-1)
    def inv(self,x):
        q=np.argsort(x[...,:self.n],axis=-1)
        L=self.si[np.take_along_axis(x[...,self.n:2*self.n],q,axis=-1)]
        R=self.si[np.take_along_axis(x[...,2*self.n:],q,axis=-1)]
        return np.concatenate((q,L,R),axis=-1)
    def permutation(self,x,action_only=False):
        from sympy.combinatorics import Permutation
        assert x.ndim==1
        arrays=[x[self.n:2*self.n]] if action_only else [x[self.n:2*self.n],x[2*self.n:]]
        width=len(arrays)*5;p=x[:self.n]
        out=[]
        for j in range(self.n):
            for k,a in enumerate(arrays):
                out.extend((width*int(p[j])+5*k+np.array(self.permutations[self.si[a[j]]])).tolist())
        return Permutation(out)
    def encode(self,x):
        return {'factor_permutation':x[:self.n].tolist(),'left_S5_indices':x[self.n:2*self.n].tolist(),
                'right_S5_indices':x[2*self.n:].tolist()}

def main():
    from sympy.combinatorics import PermutationGroup
    start=time.time();H=FerrariA5()
    print('19 kernel classes, Nielsen orbit sizes',list(map(len,H.kernel_class_orbits)),flush=True)
    # The faithful paired-block model has the same multiplication as the
    # explicitly stored twisted permutations; test all generator products.
    gs=(H.a,H.b,H.c,H.inv(H.a),H.inv(H.b),H.inv(H.c))
    for x in gs:
        for y in gs:assert H.permutation(H.mul(x,y))==H.permutation(x)*H.permutation(y)
    A=PermutationGroup([H.permutation(H.a,True),H.permutation(H.b,True)])
    aorder=int(A.order());print('Nielsen image order',aorder,flush=True)
    T=PermutationGroup([H.permutation(H.a),H.permutation(H.b),H.permutation(H.c)])
    torder=int(T.order());assert torder==60**19*aorder
    print('Full target order',torder,flush=True)
    out={'ordered_generating_pairs':len(H.all_pairs),'distinct_epimorphism_kernels':19,
         'kernel_class_representatives':H.kernel_classes,'Nielsen_kernel_orbits':H.kernel_class_orbits,
         'free_kernel_order':60**19,'Nielsen_image_order':aorder,'four_strand_image_order':torder,
         'faithful_permutation_degree':190,'six_pure_pairs_commute':[bool(np.array_equal(H.comm(x,y),H.one)) for x,y in H.pairs],
         'braid_generator_orders':[int(H.permutation(g).order()) for g in (H.a,H.b,H.c)],
         'literal_actions_and_braid_relations_verified':True,'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(Path(__file__).with_suffix('.npz'),a=H.a,b=H.b,c=H.c,x=H.x,y=H.y,
                        S5_permutations=np.array(H.permutations),S5_multiplication=H.sm)
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
