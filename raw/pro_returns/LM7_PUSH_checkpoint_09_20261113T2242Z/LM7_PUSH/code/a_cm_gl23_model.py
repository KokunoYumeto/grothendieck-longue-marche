#!/usr/bin/env python3
"""Actual universal Ferrari target for all literal GL2(F3) epikernels.

Its finite permutation representation is the faithful holomorph action
on the 18 matrix-group coordinates.  Every Nielsen transporter is retained.
No product decomposition of the free image is assumed.
"""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup
from a_cm_gl23_group import MatrixGL23
from de_ferrari_two_model import FerrariTwo

HERE=Path(__file__).resolve().parent


class FerrariGL23(FerrariTwo):
    def __init__(self):
        G=MatrixGL23(); self.group=G
        self.elements=G.elements;self.uid=G.uid;self.sm=G.mul;self.si=G.inv
        self.auto=G.auto;self.am=G.am;self.ai=G.ai;self.autone=G.autone
        self.generating_pairs=G.generating_pairs
        self.kernel_representatives=G.kernel_representatives
        self.coordinate=G.coordinate
        self.n=len(self.kernel_representatives);n=self.n
        self.width=3*n
        self.ps=slice(0,n);self.as_=slice(n,2*n);self.ks=slice(2*n,3*n)
        self.one=np.r_[np.arange(n),np.full(n,self.autone),np.full(n,self.uid)]
        pa=[];ca=[];pb=[];cb=[]
        for g,h in self.kernel_representatives:
            p,a=self.coordinate[(g,int(self.sm[h,g]))];pa.append(p);ca.append(a)
            p,a=self.coordinate[(int(self.sm[g,self.si[h]]),h)];pb.append(p);cb.append(a)
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
        literal=self.mul(self.mul(self.mul(self.mul(self.mul(self.a,self.b),self.a),
                    self.inv(self.c)),self.inv(self.b)),self.inv(self.a))
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

    def mul(self,x,y):
        x,y=np.broadcast_arrays(x,y);p=x[...,self.ps]
        q=np.take_along_axis(y[...,self.ps],p,axis=-1)
        a=x[...,self.as_];b=np.take_along_axis(y[...,self.as_],p,axis=-1)
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
            out.extend((48*p+self.auto[self.ai[a],self.sm[self.si[k],np.arange(48)]]).tolist())
        return Permutation(out)

    def encode(self,x):
        return {'exact_coordinates':np.asarray(x).tolist()}


def main():
    started=time.time();H=FerrariGL23()
    print('GL2(F3) complete target:',len(H.generating_pairs),'generating pairs;',
          H.n,'epikernels; degree',48*H.n,flush=True)
    gens=(H.a,H.b,H.c,H.inv(H.a),H.inv(H.b),H.inv(H.c))
    for x in gens:
        assert np.array_equal(H.mul(x,H.inv(x)),H.one)
        for y in gens:
            assert H.permutation(H.mul(x,y))==H.permutation(x)*H.permutation(y)
    groups={'free':(H.xi1,H.xi2),'Nielsen':(H.a,H.b),'target':(H.a,H.b,H.c)}
    orders={}
    for name,gs in groups.items():
        ps=[H.permutation(g) for g in gs]
        with (HERE/f'a_cm_gl23_{name}.input').open('w') as f:
            f.write(f'{48*H.n} {len(ps)}\n')
            for p in ps:f.write(' '.join(map(str,p.array_form))+'\n')
        orders[name]=int(PermutationGroup(ps).order())
        print(name,orders[name],flush=True)
    assert orders['target']==orders['free']*orders['Nielsen']
    pure=[]
    for x,y in H.pairs:
        G=PermutationGroup([H.permutation(x),H.permutation(y)])
        pure.append({'order':int(G.order()),'commute':bool(np.array_equal(H.comm(x,y),H.one)),
                     'x_order':int(H.permutation(x).order()),'y_order':int(H.permutation(y).order())})
    # All determinant characters are retained on the universal free image.
    det=np.array([H.group.det[[g,h]] for g,h in H.kernel_representatives])
    for a in H.auto:assert np.array_equal(H.group.det[a],H.group.det)
    out={'status':'PASS_EXACT_UNIVERSAL_GL23_FERRARI_MODEL',
         'literal_matrix_group_order':48,'complete_automorphism_count':len(H.auto),
         'ordered_generating_pairs':len(H.generating_pairs),
         'exact_epimorphism_kernel_count':H.n,'kernel_representatives':H.kernel_representatives,
         'faithful_permutation_degree':48*H.n,
         'actual_free_image_order':orders['free'],'actual_Nielsen_image_order':orders['Nielsen'],
         'actual_B4_target_order':orders['target'],'six_actual_pure_pair_images':pure,
         'braid_generator_orders':[int(H.permutation(g).order()) for g in (H.a,H.b,H.c)],
         'all_36_generator_product_permutation_comparisons':True,
         'all_determinant_profiles':det.tolist(),
         'Nielsen_kernel_orbits':list(map(list,PermutationGroup([Permutation(H.a[H.ps]),
                                      Permutation(H.b[H.ps])]).orbits())),
         'actual_source_and_whole_fibres_not_yet_claimed':True,
         'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'a_cm_gl23_model.npz',a=H.a,b=H.b,c=H.c,x=H.x,y=H.y,
        xi1=H.xi1,xi2=H.xi2,GL2_elements=np.array(H.elements),GL2_multiplication=H.sm,
        GL2_inverse=H.si,GL2_one=np.array(H.uid),Aut_maps=H.auto,Aut_multiplication=H.am,
        Aut_inverse=H.ai,kernel_representatives=np.array(H.kernel_representatives),determinant_profiles=det)
    (HERE/'a_cm_gl23_model.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
