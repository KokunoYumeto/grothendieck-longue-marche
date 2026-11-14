#!/usr/bin/env python3
"""Actual B=C2*C3 source of all eight five-point evaluations.

The eight F2 maps comprise the five pentagon substitutions in strands
1..4 and all three literal NS braid-action substitutions in B5.
Induction retains all six B/F2 cosets. Faithful compression is certified
by explicit B-set intertwiners, not by merely matching group orders.
"""
from pathlib import Path
from collections import deque
import argparse,json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from sympy import factorint
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_kernel_source import compress
from de_ferrari_mod9_lift import Induced

HERE=Path(__file__).resolve().parent

class Evaluations:
    def __init__(self):
        a=np.load(HERE/'e_hurwitz_five_a5_model_root.npz')
        self.sigma=a['sigma'];self.x=a['x'];self.y=a['y']
        self.degree=self.sigma.shape[1];self.count=len(self.x)
        self.one=np.arange(self.degree,dtype=np.int64)
    def mul(self,x,y):
        x,y=np.broadcast_arrays(x,y)
        return np.take_along_axis(y,x,axis=-1)
    def inv(self,x):return np.argsort(x,axis=-1)
    def power(self,x,n):
        if n<0:return self.power(self.inv(x),-n)
        out=np.broadcast_to(self.one,x.shape).copy()
        while n:
            if n&1:out=self.mul(out,x)
            x=self.mul(x,x);n//=2
        return out
    def word(self,w):
        letters={1:self.x,2:self.y,-1:self.inv(self.x),-2:self.inv(self.y)}
        out=np.broadcast_to(self.one,self.x.shape).copy()
        for t in w:out=self.mul(out,letters[t])
        return out

class Source(Induced):
    def __init__(self,H,d):
        self.H=H;self.d=d;self.Q=sorted(d['Q2']);self.ix={q:i for i,q in enumerate(self.Q)}
        self.root=self.ix[d['unit']];self.id=np.arange(6,dtype=np.int64)
        self.one=(self.id,np.broadcast_to(H.one,(6,H.count,H.degree)).copy())
        sect={d['unit']:[]};todo=deque(sect)
        while todo:
            q=todo.popleft()
            for t,g in ((0,d['s2']),(1,d['r2'])):
                qn=d['mul2'](q,g)
                if qn not in sect:sect[qn]=sect[q]+[t];todo.append(qn)
        self.section=sect;self.letters={}
        for t,g in ((0,d['s2']),(1,d['r2']),(-1,d['r22'])):
            perm=[];values=[]
            for q in self.Q:
                qn=d['mul2'](q,g);perm.append(self.ix[qn])
                values.append(H.word(d['fword'](sect[q]+[t]+d['binv'](sect[qn]))))
            self.letters[t]=(np.array(perm),np.array(values))
        assert self.equal(self.power(self.letters[0],2),self.one)
        assert self.equal(self.power(self.letters[1],3),self.one)
        assert self.equal(self.inv(self.letters[1]),self.letters[-1])
        for fw,bw in (((1,),d['xword']),((2,),d['yword'])):
            el=self.word(bw);assert np.array_equal(el[0],self.id)
            assert np.array_equal(el[1][self.root],H.word(fw))
    def permutation(self,e):
        out=[]
        for q in range(6):
            for i in range(self.H.count):
                out.extend((self.H.degree*(self.H.count*int(e[0][q])+i)+e[1][q,i]).tolist())
        return np.array(out,dtype=np.int64)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--arrays-only',action='store_true')
    args=parser.parse_args();start=time.time();H=Evaluations();d=load_data();W=Source(H,d)
    s,r=W.permutation(W.letters[0]),W.permutation(W.letters[1])
    assert np.array_equal(s[s],np.arange(len(s)))
    assert np.array_equal(r[r[r]],np.arange(len(r)))
    for a in W.letters.values():
        for b in W.letters.values():
            assert np.array_equal(W.permutation(W.mul(a,b)),W.permutation(b)[W.permutation(a)])
    np.savez_compressed(HERE/'e_hurwitz_five_source_root_generators.npz',s=s,r=r)
    new,metadata=compress(s,r)
    np.savez_compressed(HERE/'e_hurwitz_five_source_root_compressed.npz',s=new[0],r=new[1])
    out={**metadata,'evaluation_count':H.count,'coset_count':6,
         'all_evaluation_and_coset_coordinates_retained':True,
         'source_C2_C3_relations_verified':True,'source_multiplication_verified':True,
         'group_order_computed':False,'seconds':round(time.time()-start,3)}
    path=HERE/'e_hurwitz_five_source_root.json'
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in
        ('retained_original_canonical_orders','orbit_correspondences')},indent=2),flush=True)
    if args.arrays_only:return
    G=PermutationGroup([Permutation(p.tolist()) for p in new]);order=int(G.order())
    out.update({'source_image_order':order,'factorization':factorint(order),
                'group_order_computed':True,'seconds':round(time.time()-start,3)})
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('Exact source order',order,'factorization',factorint(order),flush=True)
    print('PASS: faithful complete induced source',flush=True)

if __name__=='__main__':main()
