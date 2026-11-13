#!/usr/bin/env python3
"""Ferrari model in the actual truncated noncommutative F3 algebra.

Degree four is used without a class<p simplification.  Automorphisms
are represented by their exact two generator images, with lazy exact
composition; their full finite image is not guessed from homology.
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
        return out%3
    def mul(self,x,y):return (x+y+self.product(x,y))%3
    def inv(self,x):
        out=np.zeros_like(x)
        for d in range(1,self.degree+1):
            out[...,self.blocks[d]]=-x[...,self.blocks[d]]
            for i in range(1,d):
                z=np.einsum('...i,...j->...ij',x[...,self.blocks[i]],out[...,self.blocks[d-i]])
                out[...,self.blocks[d]]-=z.reshape(x.shape[:-1]+(2**d,))
            out[...,self.blocks[d]]%=3
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
        self.A=A;self.n=A.n;self.capacity=4096;self.count=0
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
        images=np.asarray(images,dtype=np.int16)%3;k=self.key(images)
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
            k=self.register((self.matrices[i]@self.images[j].T).T%3)
            self.cache[(i,j)]=k
        return k
    def compose_many(self,ii,jj):
        ii,jj=np.broadcast_arrays(ii,jj)
        return np.array([self.compose(int(i),int(j)) for i,j in zip(ii.ravel(),jj.ravel())],dtype=np.int64).reshape(ii.shape)
    def inverse(self,i):
        old=self.inverse_cache.get(i)
        if old is not None:return old
        matrix=self.matrices[i];a,b,c,d=(int(t) for t in matrix[:2,:2].ravel())
        det=(a*d-b*c)%3;assert det
        Linv=det*np.array([[d,-b],[-c,a]],dtype=np.int16)%3
        images=np.zeros((2,self.n),dtype=np.int16);images[:,:2]=Linv.T
        tensor=Linv.copy()
        for degree in range(2,self.A.degree+1):
            tensor=np.kron(tensor,Linv)%3;block=self.A.blocks[degree]
            error=(matrix@images.T).T%3
            images[:,block]=-error[:,block]@tensor.T%3
        j=self.register(images)
        assert self.compose(i,j)==0 and self.compose(j,i)==0
        self.inverse_cache[i]=j;self.inverse_cache[j]=i
        return j
    def inverse_many(self,ii):
        return np.array([self.inverse(int(i)) for i in ii.ravel()],dtype=np.int64).reshape(ii.shape)

class FerrariTruncated:
    def __init__(self,degree=4):
        assert degree in (3,4,5,6)
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
        acted=np.einsum('...ij,...j->...i',self.aut.matrices[ai],y[...,:self.n])%3
        vec=self.algebra.mul(x[...,:self.n],acted)
        ci=self.aut.compose_many(ai,bi)
        return np.concatenate((vec,ci[...,None]),axis=-1)
    def inv(self,x):
        ai=self.aut.inverse_many(x[...,-1])
        vec=np.einsum('...ij,...j->...i',self.aut.matrices[ai],self.algebra.inv(x[...,:self.n]))%3
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
    def project(self,x):
        images=self.aut.images[x[...,-1]]
        matrix=np.swapaxes(images[...,:,:2],-1,-2).reshape(x.shape[:-1]+(4,))
        u=x[...,0];v=x[...,1];z=(x[...,3]-2*u*v-u-2*v)%3
        return np.concatenate((matrix,np.stack((u,v,z),axis=-1)),axis=-1)
    def kernel_vector(self,x):
        assert self.algebra.degree<=4,'The kernel over degree2 is no longer abelian at degree5.'
        projection=self.project(x)
        assert np.array_equal(projection,np.broadcast_to(np.array([1,0,0,1,0,0,0]),projection.shape))
        assert not np.any(x[...,:6])
        images=self.aut.images[x[...,-1]];assert not np.any(images[...,2:6])
        return np.concatenate((x[...,6:self.n],images[...,6:].reshape(x.shape[:-1]+(2*(self.n-6),))),axis=-1)
    def kernel_element(self,v):
        assert self.algebra.degree<=4,'Use the top-degree kernel at degree5.'
        tail=self.n-6;result=np.zeros(v.shape[:-1]+(self.n+1,),dtype=np.int64)
        result[...,6:self.n]=v[...,:tail]%3
        images=v[...,tail:].reshape((-1,2,tail))%3
        indices=[]
        for im in images:
            image=np.zeros((2,self.n),dtype=np.int16);image[0,0]=image[1,1]=1;image[:,6:]=im
            indices.append(self.aut.register(image))
        result[...,-1]=np.array(indices,dtype=np.int64).reshape(v.shape[:-1])
        return result
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
        result[...,lower:self.n]=v[...,:tail]%3
        indices=[]
        for delta in v[...,tail:].reshape(-1,2,tail)%3:
            images=np.zeros((2,self.n),dtype=np.int16);images[0,0]=images[1,1]=1;images[:,lower:]=delta
            indices.append(self.aut.register(images))
        result[...,-1]=np.array(indices,dtype=np.int64).reshape(v.shape[:-1])
        return result

def main():
    from de_ferrari_degree3_model import FerrariDegreeThree
    start=time.time();H=FerrariTruncated(4);old=FerrariDegreeThree()
    rng=np.random.default_rng(214026)
    generators=[H.a,H.b,H.c,H.inv(H.a),H.inv(H.b),H.inv(H.c)]
    oldgenerators=[old.a,old.b,old.c,old.inv(old.a),old.inv(old.b),old.inv(old.c)]
    current=H.one;oldcurrent=old.one
    for _ in range(1000):
        k=int(rng.integers(6));current=H.mul(current,generators[k]);oldcurrent=old.mul(oldcurrent,oldgenerators[k])
        assert np.array_equal(current[:14],oldcurrent[:14])
        image=H.aut.images[int(current[-1]),:,:14]
        assert np.array_equal(image,old.aut.images[int(oldcurrent[-1])])
        assert np.array_equal(H.project(current),old.project(oldcurrent))
        assert np.array_equal(H.mul(current,H.inv(current)),H.one)
    c=H.comm(H.xi1,H.xi2)
    kernels=[H.power(H.xi1,3),H.power(H.xi2,3),H.comm(H.xi1,c),H.comm(H.xi2,c),
             H.power(H.a,3),H.power(H.b,3),H.power(H.mul(H.a,H.b),6)]
    for k in list(kernels):
        for gen in (H.a,H.b,H.xi1,H.xi2):kernels.append(H.conj(gen,k))
    for a in kernels:
        for b in kernels:
            assert np.array_equal(H.kernel_vector(H.mul(a,b)),(H.kernel_vector(a)+H.kernel_vector(b))%3)
    output={'coefficient_field':3,'maximum_Magnus_degree':4,
            'truncated_augmentation_algebra_dimension':H.n,
            'ambient_additive_kernel_coordinate_count':3*(H.n-6),
            'all_literal_Ferrari_and_braid_actions_verified':True,
            'successive_1000_actual_word_reductions_agree_with_degree3_model':True,
            'abelian_kernel_pair_checks':len(kernels)**2,
            'registered_actual_automorphisms_during_audit':H.aut.count,
            'elapsed_seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
