#!/usr/bin/env python3
"""Exact A6 epikernels and their Nielsen permutation/outer actions.

The 1440 actual Aut(A6) maps come from the independently certified D31
model.  Every map is checked on both generator edges of the entire
A6 Cayley graph.  All ordered pair orbits are partitioned, so testing
generation once per orbit exhausts all pairs.  The actual automorphism
transporters, including both exceptional outer bits, are retained.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time
import numpy as np
from de_ferrari_two_model import FerrariTwo

here=Path(__file__).resolve().parent

def build():
    start=time.time();raw=json.loads((here/'a_peripheral_a6_outer.json').read_text())
    elements=np.array(raw['A6_elements'],dtype=np.int64)
    index={tuple(g):i for i,g in enumerate(elements)}
    one=index[tuple(range(6))];assert len(elements)==360
    multiplication=np.array([[index[tuple(a[b])] for b in elements] for a in elements],dtype=np.int64)
    inverse=np.array([int(np.flatnonzero(row==one)[0]) for row in multiplication],dtype=np.int64)
    maps=np.array(raw['automorphism_maps'],dtype=np.int64)
    pairs=np.array(raw['automorphism_generator_pairs'],dtype=np.int64)
    ga,gb=raw['A6_generators'];assert maps.shape==(1440,360)
    assert np.array_equal(maps[:,[ga,gb]],pairs)
    assert all(np.array_equal(np.sort(row),np.arange(360)) for row in maps)
    for g in (ga,gb):
        assert np.array_equal(maps[:,multiplication[:,g]],
                              multiplication[maps,maps[:,g,None]])
    adict=np.full((360,360),-1,dtype=np.int64)
    adict[pairs[:,0],pairs[:,1]]=np.arange(1440)
    autoone=int(adict[ga,gb]);assert np.array_equal(maps[autoone],np.arange(360))
    automul=adict[maps[:,pairs[:,0]],maps[:,pairs[:,1]]]
    assert np.all(automul>=0)
    autoinv=np.array([int(np.flatnonzero(row==autoone)[0]) for row in automul],dtype=np.int64)
    outer=np.array(raw['outer_coordinates'],dtype=np.int64)
    assert np.array_equal(outer[automul],outer[:,None]^outer[None,:])
    assert set(np.flatnonzero(outer==0))==set(raw['inner_indices'])
    orders=[]
    for g in range(360):
        v=one;n=0
        while n==0 or v!=one:v=int(multiplication[v,g]);n+=1
        orders.append(n)
    def generated(a,b):
        found={one};queue=[one]
        for g in queue:
            for h in (a,b):
                v=int(multiplication[g,h])
                if v not in found:found.add(v);queue.append(v)
        return len(found)
    seen=np.zeros(360*360,dtype=bool)
    pair_kernel=np.full(360*360,-1,dtype=np.int64)
    pair_transporter=np.full(360*360,-1,dtype=np.int64)
    reps=[];orbit_data=[];genpairs=0
    for code in range(360*360):
        if seen[code]:continue
        a,b=divmod(code,360)
        orbit=maps[:,a]*360+maps[:,b];unique=np.unique(orbit)
        assert not np.any(seen[unique]);seen[unique]=True
        size=generated(a,b)
        orbit_data.append({'representative':[a,b],'orbit_size':len(unique),'generated_order':size})
        if size==360:
            assert len(unique)==1440
            j=len(reps);reps.append((a,b));genpairs+=1440
            pair_kernel[orbit]=j;pair_transporter[orbit]=np.arange(1440)
    assert np.all(seen) and genpairs==np.count_nonzero(pair_kernel>=0)
    reps=np.array(reps,dtype=np.int64);n=len(reps)
    pa=[];ca=[];pb=[];cb=[]
    for a,b in reps:
        acode=int(a)*360+int(multiplication[b,a])
        bcode=int(multiplication[a,inverse[b]])*360+int(b)
        pa.append(int(pair_kernel[acode]));ca.append(int(pair_transporter[acode]))
        pb.append(int(pair_kernel[bcode]));cb.append(int(pair_transporter[bcode]))
    pa,ca,pb,cb=map(lambda a:np.array(a,dtype=np.int64),(pa,ca,pb,cb))
    assert np.array_equal(np.sort(pa),np.arange(n)) and np.array_equal(np.sort(pb),np.arange(n))
    # Check the complete actual automorphism action before forgetting any
    # inner or free information in the two smaller targets.
    def auto_product(u,v):
        p,c=u;q,d=v
        return q[p],automul[c,d[p]]
    aa=(pa,ca);bb=(pb,cb)
    lhs=auto_product(auto_product(aa,bb),aa)
    rhs=auto_product(auto_product(bb,aa),bb)
    assert all(np.array_equal(a,b) for a,b in zip(lhs,rhs))
    for j,(a,b) in enumerate(reps):
        assert maps[ca[j],reps[pa[j],0]]==a
        assert maps[ca[j],reps[pa[j],1]]==multiplication[b,a]
        assert maps[cb[j],reps[pb[j],0]]==multiplication[a,inverse[b]]
        assert maps[cb[j],reps[pb[j],1]]==b
    nielsen_orbits=[];visited=set()
    for j in range(n):
        if j in visited:continue
        queue=[j];visited.add(j)
        for q in queue:
            for p in (pa,pb):
                v=int(p[q])
                if v not in visited:visited.add(v);queue.append(v)
        nielsen_orbits.append(sorted(queue))
    commorders=[]
    for a,b in reps:
        v=multiplication[multiplication[multiplication[a,b],inverse[a]],inverse[b]]
        commorders.append(orders[int(v)])
    out={'actual_A6_order':360,'actual_Aut_A6_order':1440,
         'all_automorphisms_checked_on_all_Cayley_generator_edges':True,
         'ordered_pairs_partitioned':360*360,'all_pair_orbit_count':len(orbit_data),
         'ordered_generating_pairs':genpairs,'epimorphism_kernel_count':n,
         'kernel_representatives':reps.tolist(),'all_pair_orbits':orbit_data,
         'Nielsen_kernel_orbits':nielsen_orbits,
         'Nielsen_kernel_orbit_sizes':list(map(len,nielsen_orbits)),
         'commutator_orders_by_kernel':commorders,
         'actual_Nielsen_a_outer_counts':dict(Counter(map(int,outer[ca]))),
         'actual_Nielsen_b_outer_counts':dict(Counter(map(int,outer[cb]))),
         'actual_automorphism_transporter_braid_relation_verified':True,
         'seconds':round(time.time()-start,3)}
    np.savez_compressed(here/'de_ferrari_a6_kernels.npz',A6_elements=elements,
        A6_multiplication=multiplication,A6_inverse=inverse,A6_orders=np.array(orders),
        Aut_maps=maps,Aut_generator_pairs=pairs,Aut_multiplication=automul,
        Aut_inverse=autoinv,Aut_one=np.array(autoone),Aut_outer_coordinates=outer,
        kernel_representatives=reps,pair_kernel=pair_kernel,pair_transporter=pair_transporter,
        a_permutation=pa,b_permutation=pb,a_automorphisms=ca,b_automorphisms=cb)
    (here/'de_ferrari_a6_kernels.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in
        ('kernel_representatives','all_pair_orbits','Nielsen_kernel_orbits','commutator_orders_by_kernel')},indent=2),flush=True)
    return out

class FerrariA6Kernel(FerrariTwo):
    def __init__(self,outer=False):
        cert=np.load(here/'de_ferrari_a6_kernels.npz')
        self.n=len(cert['kernel_representatives']);self.outer=outer
        self.one=np.arange(self.n,dtype=np.int64)
        self.a=cert['a_permutation'].copy();self.b=cert['b_permutation'].copy()
        if outer:
            coordinates=cert['Aut_outer_coordinates']
            self.one=np.r_[self.one,np.zeros(self.n,dtype=np.int64)]
            self.a=np.r_[self.a,coordinates[cert['a_automorphisms']]]
            self.b=np.r_[self.b,coordinates[cert['b_automorphisms']]]
        self.c=self.a.copy()
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
        assert np.array_equal(self.xi1,self.one) and np.array_equal(self.xi2,self.one)
    def mul(self,x,y):
        x,y=np.broadcast_arrays(x,y);p=x[...,:self.n]
        q=np.take_along_axis(y[...,:self.n],p,axis=-1)
        if not self.outer:return q
        e=x[...,self.n:]^np.take_along_axis(y[...,self.n:],p,axis=-1)
        return np.concatenate((q,e),axis=-1)
    def inv(self,x):
        q=np.argsort(x[...,:self.n],axis=-1)
        if not self.outer:return q
        return np.concatenate((q,np.take_along_axis(x[...,self.n:],q,axis=-1)),axis=-1)
    def permutation(self,x):
        from sympy.combinatorics import Permutation
        assert x.ndim==1
        if not self.outer:return Permutation(x.tolist())
        return Permutation([4*int(x[j])+(z^int(x[self.n+j]))
                            for j in range(self.n) for z in range(4)])
    def encode(self,x):
        out={'kernel_permutation':x[:self.n].tolist()}
        if self.outer:out['exceptional_outer_coordinates']=x[self.n:].tolist()
        return out

def main():
    start=time.time();info=build()
    from sympy.combinatorics import PermutationGroup
    targets=[]
    for outer in (False,True):
        H=FerrariA6Kernel(outer)
        gs=[H.a,H.b,H.c,H.inv(H.a),H.inv(H.b),H.inv(H.c)]
        for a in gs:
            for b in gs:assert H.permutation(H.mul(a,b))==H.permutation(a)*H.permutation(b)
        T=PermutationGroup([H.permutation(H.a),H.permutation(H.b)])
        order=int(T.order())
        row={'mode':'permutation_and_outer_V4' if outer else 'kernel_permutation_only',
            'faithful_permutation_degree':H.permutation(H.one).size,
            'target_order':order,'braid_generator_orders':[int(H.permutation(g).order()) for g in (H.a,H.b,H.c)],
            'six_pure_pairs_commute':[bool(np.array_equal(H.comm(x,y),H.one)) for x,y in H.pairs]}
        targets.append(row);print(json.dumps(row),flush=True)
    out={'kernel_data_file':'de_ferrari_a6_kernels.json','targets':targets,
         'outer_kernel_order_over_permutation_target':targets[1]['target_order']//targets[0]['target_order'],
         'all_braid_and_projection_operations_verified':True,'seconds':round(time.time()-start,3)}
    (here/'de_ferrari_a6_kernel_targets.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
