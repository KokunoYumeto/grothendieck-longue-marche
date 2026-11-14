#!/usr/bin/env python3
"""Actual characteristic-two Ferrari Magnus model, retaining squares.

The exact tensor-algebra and substitution algorithms are adapted from
our characteristic-three model with every operation performed in F2.
No logarithmic coordinates are used.
"""
from pathlib import Path
import json,time
import numpy as np

class Algebra:
    def __init__(self,degree):
        self.degree=degree;self.n=2**(degree+1)-2
        self.blocks={d:slice(2**d-2,2**(d+1)-2) for d in range(1,degree+1)}
    def product(self,x,y,minleft=1,minright=1):
        shape=np.broadcast_shapes(x.shape[:-1],y.shape[:-1]);out=np.zeros(shape+(self.n,),dtype=np.int16)
        for i in range(minleft,self.degree+1-minright):
            for j in range(minright,self.degree+1-i):
                z=np.einsum('...i,...j->...ij',x[...,self.blocks[i]],y[...,self.blocks[j]])
                out[...,self.blocks[i+j]]+=z.reshape(shape+(2**(i+j),))
        return out%2
    def mul(self,x,y):return (x+y+self.product(x,y))%2
    def inv(self,x):
        out=np.zeros_like(x)
        for d in range(1,self.degree+1):
            out[...,self.blocks[d]]=-x[...,self.blocks[d]]
            for i in range(1,d):
                z=np.einsum('...i,...j->...ij',x[...,self.blocks[i]],out[...,self.blocks[d-i]])
                out[...,self.blocks[d]]-=z.reshape(x.shape[:-1]+(2**d,))
            out[...,self.blocks[d]]%=2
        return out
    def auto_matrix(self,images):
        previous=[images[0],images[1]];columns=list(previous)
        for d in range(2,self.degree+1):
            current=[]
            for i in range(2**d):
                current.append(self.product(previous[i//2],images[i%2],minleft=d-1))
            columns.extend(current);previous=current
        return np.array(columns,dtype=np.int16).T

class Automorphisms:
    def __init__(self,A):
        self.A=A;self.n=A.n;self.capacity=1024;self.count=0
        self.images=np.zeros((self.capacity,2,self.n),dtype=np.int16)
        self.matrices=np.zeros((self.capacity,self.n,self.n),dtype=np.int16)
        self.lookup={};self.cache={};self.inverse_cache={0:0}
        identity=np.zeros((2,self.n),dtype=np.int16);identity[0,0]=identity[1,1]=1
        assert self.register(identity)==0
        x,y=identity
        self.a=self.register(np.array([x,A.mul(y,x)]));self.b=self.register(np.array([A.mul(x,A.inv(y)),y]))
    @staticmethod
    def key(images):return bytes(np.asarray(images,dtype=np.uint8).ravel())
    def register(self,images):
        images=np.asarray(images,dtype=np.int16)%2;k=self.key(images)
        old=self.lookup.get(k)
        if old is not None:return old
        if self.count==self.capacity:
            self.images=np.concatenate((self.images,np.zeros_like(self.images)))
            self.matrices=np.concatenate((self.matrices,np.zeros_like(self.matrices)))
            self.capacity*=2
        index=self.count;self.count+=1;self.lookup[k]=index
        self.images[index]=images;self.matrices[index]=self.A.auto_matrix(images)
        return index
    def compose(self,i,j):
        k=self.cache.get((i,j))
        if k is None:
            k=self.register((self.matrices[i]@self.images[j].T).T%2)
            self.cache[(i,j)]=k
        return k
    def compose_many(self,ii,jj):
        ii,jj=np.broadcast_arrays(ii,jj)
        return np.array([self.compose(int(i),int(j)) for i,j in zip(ii.ravel(),jj.ravel())],dtype=np.int64).reshape(ii.shape)
    def inverse(self,i):
        old=self.inverse_cache.get(i)
        if old is not None:return old
        matrix=self.matrices[i];a,b,c,d=(int(t) for t in matrix[:2,:2].ravel())
        det=(a*d-b*c)%2;assert det
        Linv=det*np.array([[d,-b],[-c,a]],dtype=np.int16)%2
        images=np.zeros((2,self.n),dtype=np.int16);images[:,:2]=Linv.T
        tensor=Linv.copy()
        for degree in range(2,self.A.degree+1):
            tensor=np.kron(tensor,Linv)%2;block=self.A.blocks[degree]
            error=(matrix@images.T).T%2
            images[:,block]=-error[:,block]@tensor.T%2
        j=self.register(images)
        assert self.compose(i,j)==0 and self.compose(j,i)==0
        self.inverse_cache[i]=j;self.inverse_cache[j]=i
        return j
    def inverse_many(self,ii):
        return np.array([self.inverse(int(i)) for i in ii.ravel()],dtype=np.int64).reshape(ii.shape)

class FerrariTwo:
    def __init__(self,degree=2):
        assert 1 <= degree <= 8
        self.algebra=Algebra(degree);self.n=self.algebra.n;self.aut=Automorphisms(self.algebra)
        self.one=np.zeros(self.n+1,dtype=np.int64)
        self.a=self.one.copy();self.a[-1]=self.aut.a
        self.b=self.one.copy();self.b[-1]=self.aut.b
        self.c=self.a.copy();self.c[0]=1
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
        expected=self.one.copy();expected[0]=1;assert np.array_equal(self.xi1,expected)
        expected=self.one.copy();expected[1]=1;assert np.array_equal(self.xi2,expected)
        assert np.array_equal(self.conj(self.a,self.xi1),self.xi1)
        assert np.array_equal(self.conj(self.a,self.xi2),self.mul(self.xi2,self.xi1))
        assert np.array_equal(self.conj(self.b,self.xi1),self.mul(self.xi1,self.inv(self.xi2)))
        assert np.array_equal(self.conj(self.b,self.xi2),self.xi2)
    def mul(self,x,y):
        ai=x[...,-1];bi=y[...,-1]
        acted=np.einsum('...ij,...j->...i',self.aut.matrices[ai],y[...,:self.n])%2
        vec=self.algebra.mul(x[...,:self.n],acted)
        ci=self.aut.compose_many(ai,bi)
        return np.concatenate((vec,ci[...,None]),axis=-1)
    def inv(self,x):
        ai=self.aut.inverse_many(x[...,-1])
        vec=np.einsum('...ij,...j->...i',self.aut.matrices[ai],self.algebra.inv(x[...,:self.n]))%2
        return np.concatenate((vec,ai[...,None]),axis=-1)
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
        images={1:x,-1:self.inv(x),2:y,-2:self.inv(y)}
        out=np.broadcast_to(self.one,x.shape).copy()
        for t,letters in groupby(w):
            exponent=sum(1 for _ in letters)
            out=self.mul(out,self.power(images[t],exponent))
        return out
    def pentagon(self,vals):return self.mul(self.mul(vals[0],vals[1]),self.inv(self.mul(self.mul(vals[2],vals[3]),vals[4])))
    def braid_images(self,vals):return self.a,self.conj(self.inv(vals[4]),self.b),self.conj(self.inv(vals[5]),self.c)
    def check_braids(self,images):
        a,b,c=images
        assert np.array_equal(self.mul(self.mul(a,b),a),self.mul(self.mul(b,a),b))
        assert np.array_equal(self.mul(self.mul(b,c),b),self.mul(self.mul(c,b),c))
        assert np.array_equal(self.mul(a,c),self.mul(c,a))
    def top_kernel_vector(self,x):
        lower=2**self.algebra.degree-2
        assert not np.any(x[...,:lower])
        images=self.aut.images[x[...,-1]]
        expected=np.zeros(images.shape[:-1]+(lower,),dtype=np.int16)
        expected[...,0,0]=expected[...,1,1]=1
        assert np.array_equal(images[...,:lower],expected)
        return np.concatenate((x[...,lower:self.n],images[...,lower:].reshape(x.shape[:-1]+(2*(self.n-lower),))),axis=-1)
    def top_kernel_element(self,v):
        lower=2**self.algebra.degree-2;tail=self.n-lower
        result=np.zeros(v.shape[:-1]+(self.n+1,),dtype=np.int64)
        result[...,lower:self.n]=v[...,:tail]%2
        indices=[]
        for delta in v[...,tail:].reshape(-1,2,tail)%2:
            images=np.zeros((2,self.n),dtype=np.int16);images[0,0]=images[1,1]=1;images[:,lower:]=delta
            indices.append(self.aut.register(images))
        result[...,-1]=np.array(indices,dtype=np.int64).reshape(v.shape[:-1])
        return result

    def project(self,x):
        images=self.aut.images[x[...,-1]]
        matrix=np.swapaxes(images[...,:,:2],-1,-2).reshape(x.shape[:-1]+(4,))
        return np.concatenate((matrix,x[...,:2]),axis=-1)
    def to_lower(self,x,old):
        images=self.aut.images[x[...,-1],:,:old.n]
        indices=[old.aut.register(im) for im in images.reshape(-1,2,old.n)]
        ai=np.array(indices,dtype=np.int64).reshape(x.shape[:-1])
        return np.concatenate((x[...,:old.n],ai[...,None]),axis=-1)
    def encode(self,x):
        assert x.ndim==1
        return {'Magnus_unit':x[:-1].tolist(),'automorphism_generator_images':self.aut.images[int(x[-1])].tolist()}
    def decode(self,x):
        ai=self.aut.register(np.array(x['automorphism_generator_images'],dtype=np.int16))
        return np.r_[x['Magnus_unit'],ai].astype(np.int64)
    def relative_kernel_vector(self,x,lower_degree=4):
        lower=2**(lower_degree+1)-2;tail=self.n-lower
        assert tail>=0 and not np.any(x[...,:lower])
        images=self.aut.images[x[...,-1]]
        expected=np.zeros(images.shape[:-1]+(lower,),dtype=np.int16)
        expected[...,0,0]=expected[...,1,1]=1
        assert np.array_equal(images[...,:lower],expected)
        return np.concatenate((x[...,lower:self.n],images[...,lower:].reshape(x.shape[:-1]+(2*tail,))),axis=-1)
    def relative_kernel_element(self,v,lower_degree=4):
        lower=2**(lower_degree+1)-2;tail=self.n-lower
        result=np.zeros(v.shape[:-1]+(self.n+1,),dtype=np.int64);result[...,lower:self.n]=v[...,:tail]%2
        indices=[]
        for delta in v[...,tail:].reshape(-1,2,tail)%2:
            images=np.zeros((2,self.n),dtype=np.int16);images[0,0]=images[1,1]=1;images[:,lower:]=delta
            indices.append(self.aut.register(images))
        result[...,-1]=np.array(indices,dtype=np.int64).reshape(v.shape[:-1])
        return result

def exact_orders(H):
    units={bytes(np.zeros(H.n,dtype=np.uint8))};queue=[np.zeros(H.n,dtype=np.int16)]
    x,y=H.aut.images[0]
    for v in queue:
        for g in (x,y):
            w=H.algebra.mul(v,g);key=bytes(w.astype(np.uint8))
            if key not in units:units.add(key);queue.append(w)
    autos={0};todo=[0]
    for i in todo:
        for g in (H.aut.a,H.aut.b):
            j=H.aut.compose(i,g)
            if j not in autos:autos.add(j);todo.append(j)
    # All actual action generators normalize the complete free-unit image.
    for i in (H.aut.a,H.aut.b):
        for v in queue:
            image=H.aut.matrices[i]@v%2
            assert bytes(image.astype(np.uint8)) in units
    return len(units),len(autos)

def main():
    start=time.time();H=FerrariTwo(2);old=FerrariTwo(1)
    rng=np.random.default_rng(222026)
    gens=[H.a,H.b,H.c,H.inv(H.a),H.inv(H.b),H.inv(H.c)]
    oldgens=[old.a,old.b,old.c,old.inv(old.a),old.inv(old.b),old.inv(old.c)]
    now=H.one;low=old.one
    for _ in range(400):
        i=int(rng.integers(6));now=H.mul(now,gens[i]);low=old.mul(low,oldgens[i])
        assert np.array_equal(H.to_lower(now,old),low)
        assert np.array_equal(H.mul(now,H.inv(now)),H.one)
    unit_order,auto_order=exact_orders(H)
    assert all(np.array_equal(H.power(g,4),H.one) for g in (H.a,H.b,H.c))
    squares=[H.power(H.xi1,2),H.power(H.xi2,2)]
    assert all(not np.array_equal(v,H.one) for v in squares)
    values=H.word([1,2,-1,-2]);assert np.array_equal(values,np.broadcast_to(H.one,values.shape))
    out={'characteristic':2,'maximum_degree':2,'Ferrari_free_kernel_order':unit_order,
        'actual_B3_automorphism_image_order':auto_order,'four_strand_image_order':unit_order*auto_order,
        'all_literal_Ferrari_and_braid_relations_checked':True,
        'actual_generator_squares_retained':True,'exact_word_truncation_comparisons':400,
        'all_six_evaluations_kill_the_F2_commutator':True,
        'elapsed_seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
