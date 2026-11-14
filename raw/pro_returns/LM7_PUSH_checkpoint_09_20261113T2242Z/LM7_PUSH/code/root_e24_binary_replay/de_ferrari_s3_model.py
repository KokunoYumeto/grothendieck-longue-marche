#!/usr/bin/env python3
"""Exact Ferrari quotient from all ordered generating pairs of S3.

No nilpotent completion or truncated expansion is used.  The free kernel
is its simultaneous evaluation image in S3^18.  The two actual Nielsen
automorphisms permute these eighteen homomorphisms, giving a finite
semidirect product and the six literal pentagon/conjugator evaluations.
"""
from pathlib import Path
from itertools import permutations
import json,time
import numpy as np
from de_ferrari_two_model import FerrariTwo

class FerrariS3(FerrariTwo):
    def __init__(self):
        self.permutations=list(permutations(range(3)))
        pd={p:i for i,p in enumerate(self.permutations)}
        self.sm=np.array([[pd[tuple(p[k] for k in q)] for q in self.permutations]
                         for p in self.permutations],dtype=np.int64)
        self.si=np.array([next(j for j in range(6) if self.sm[i,j]==0) for i in range(6)])
        def closure(gs):
            seen={0};todo=[0]
            for z in todo:
                for g in gs:
                    w=int(self.sm[z,g])
                    if w not in seen:seen.add(w);todo.append(w)
            return seen
        self.generating_pairs=[(g,h) for g in range(6) for h in range(6)
                               if len(closure((g,h)))==6]
        assert len(self.generating_pairs)==18
        xx=np.array([g for g,h in self.generating_pairs]);yy=np.array([h for g,h in self.generating_pairs])
        self.K=[np.zeros(18,dtype=np.int64)];self.Kwords=[[]];kd={tuple(self.K[0]):0}
        for i,v in enumerate(self.K):
            for j,g in enumerate((xx,yy),1):
                w=self.sm[v,g];key=tuple(w)
                if key not in kd:kd[key]=len(self.K);self.K.append(w);self.Kwords.append(self.Kwords[i]+[j])
        self.K=np.array(self.K);self.kd=kd
        self.km=np.array([[kd[tuple(self.sm[u,v])] for v in self.K] for u in self.K],dtype=np.int64)
        self.ki=np.array([kd[tuple(self.si[u])] for u in self.K],dtype=np.int64)
        ix,iy=kd[tuple(xx)],kd[tuple(yy)]
        pairs={p:i for i,p in enumerate(self.generating_pairs)}
        pa=np.array([pairs[(g,int(self.sm[h,g]))] for g,h in self.generating_pairs])
        pb=np.array([pairs[(int(self.sm[g,self.si[h]]),h)] for g,h in self.generating_pairs])
        self.A=[np.arange(18,dtype=np.int64)];self.Awords=[[]];ad={tuple(self.A[0]):0}
        for i,p in enumerate(self.A):
            for j,g in enumerate((pa,pb),1):
                q=g[p];key=tuple(q)
                if key not in ad:ad[key]=len(self.A);self.A.append(q);self.Awords.append(self.Awords[i]+[j])
        self.A=np.array(self.A);self.ad=ad
        # alpha_i alpha_j evaluates k at p_j[p_i].
        self.am=np.array([[ad[tuple(q[p])] for q in self.A] for p in self.A],dtype=np.int64)
        self.ai=np.array([ad[tuple(np.argsort(p))] for p in self.A],dtype=np.int64)
        self.action=np.array([[kd[tuple(k[p])] for k in self.K] for p in self.A],dtype=np.int64)
        ia,ib=ad[tuple(pa)],ad[tuple(pb)]
        assert self.action[ia,ix]==ix and self.action[ia,iy]==self.km[iy,ix]
        assert self.action[ib,ix]==self.km[ix,self.ki[iy]] and self.action[ib,iy]==iy
        # Every permutation is distinguished by the two generating arrays;
        # hence the action used for this semidirect product is faithful.
        assert len({tuple(np.r_[self.K[self.action[i,ix]],self.K[self.action[i,iy]]]) for i in range(len(self.A))})==len(self.A)
        for i in range(len(self.A)):
            assert np.array_equal(self.action[i,self.km],self.km[self.action[i,:,None],self.action[i,None,:]])
        self.one=np.array([0,0],dtype=np.int64)
        self.a=np.array([0,ia]);self.b=np.array([0,ib]);self.c=np.array([ix,ia])
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
        assert np.array_equal(self.xi1,[ix,0]) and np.array_equal(self.xi2,[iy,0])
        assert np.array_equal(self.conj(self.a,self.xi1),self.xi1)
        assert np.array_equal(self.conj(self.a,self.xi2),self.mul(self.xi2,self.xi1))
        assert np.array_equal(self.conj(self.b,self.xi1),self.mul(self.xi1,self.inv(self.xi2)))
        assert np.array_equal(self.conj(self.b,self.xi2),self.xi2)
    def mul(self,x,y):
        return np.stack((self.km[x[...,0],self.action[x[...,1],y[...,0]]],self.am[x[...,1],y[...,1]]),axis=-1)
    def inv(self,x):
        a=self.ai[x[...,1]]
        return np.stack((self.action[a,self.ki[x[...,0]]],a),axis=-1)
    def encode(self,x):
        return {'free_kernel_evaluations':self.K[int(x[0])].tolist(),
                'Nielsen_permutation':self.A[int(x[1])].tolist()}
    def decode(self,x):
        return np.array([self.kd[tuple(x['free_kernel_evaluations'])],self.ad[tuple(x['Nielsen_permutation'])]],dtype=np.int64)
    def subgroup(self,generators):
        generators=[np.array(g,dtype=np.int64) for g in generators]
        index={(0,0):0};elements=[self.one];words=[[]]
        for i,h in enumerate(elements):
            for j,g in enumerate(generators,1):
                k=self.mul(h,g);key=tuple(k)
                if key not in index:index[key]=len(elements);elements.append(k);words.append(words[i]+[j])
        return np.array(elements),words,index
    def order(self,x):
        h=self.one.copy()
        for i in range(1,len(self.K)*len(self.A)+1):
            h=self.mul(h,x)
            if np.array_equal(h,self.one):return i
        raise AssertionError('Lagrange bound exceeded')

def main():
    start=time.time();H=FerrariS3()
    target,words,index=H.subgroup((H.a,H.b,H.c))
    assert len(target)==len(H.K)*len(H.A)==17496
    # Derived and lower-central subgroups are computed from their complete
    # normal generating sets inside the explicitly enumerated free image.
    C,_,_=H.subgroup([H.comm(np.array([i,0]),np.array([j,0])) for i in range(len(H.K)) for j in range(len(H.K))])
    lower,_,_=H.subgroup([H.comm(z,np.array([j,0])) for z in C for j in range(len(H.K))])
    assert {tuple(z) for z in C}=={tuple(z) for z in lower} and len(C)>1
    assert all(H.order(z) in (1,3) for z in C)
    assert all(np.array_equal(H.comm(z,w),H.one) for z in C for w in C)
    out={'symmetric_group_permutations':H.permutations,'ordered_generating_pairs':H.generating_pairs,
         'free_kernel_order':len(H.K),'Nielsen_image_order':len(H.A),'full_four_strand_image_order':len(target),
         'free_derived_order':len(C),'free_third_lower_central_order':len(lower),
         'free_derived_is_elementary_abelian_3':True,'free_lower_central_series_stabilizes_nontrivially':True,
         'braid_generator_orders':[H.order(g) for g in (H.a,H.b,H.c)],
         'pure_evaluation_generator_orders':[[H.order(x),H.order(y)] for x,y in H.pairs],
         'full_twist_orders':[H.order(H.power(H.mul(H.a,H.b),3)),H.order(H.power(H.mul(H.mul(H.a,H.b),H.c),4))],
         'literal_Ferrari_action_verified':True,'exact_full_target_enumerated':True,
         'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(Path(__file__).with_suffix('.npz'),free_kernel=H.K,nielsen_permutations=H.A,
                        free_multiplication=H.km,nielsen_multiplication=H.am,action=H.action,
                        four_strand_elements=target,free_derived=C,free_gamma3=lower)
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
