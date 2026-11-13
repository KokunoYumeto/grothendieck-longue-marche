#!/usr/bin/env python3
"""Actual Ferrari-kernel quotient in truncated F3 Magnus degree three.

All cubic-power terms are retained.  The B3 action is the literal
action on the two free Ferrari generators; its finite image is
computed, rather than replaced by its SL2 homology image.
"""
from pathlib import Path
from collections import deque
import json,time
import numpy as np

def kmul(x,y):
    a=x[...,:2];b=x[...,2:6].reshape(x.shape[:-1]+(2,2));c=x[...,6:].reshape(x.shape[:-1]+(2,2,2))
    A=y[...,:2];B=y[...,2:6].reshape(y.shape[:-1]+(2,2));C=y[...,6:].reshape(y.shape[:-1]+(2,2,2))
    v=a+A
    q=b+B+np.einsum('...i,...j->...ij',a,A)
    t=c+C+np.einsum('...i,...jk->...ijk',a,B)+np.einsum('...ij,...k->...ijk',b,A)
    return np.concatenate((v,q.reshape(q.shape[:-2]+(4,)),t.reshape(t.shape[:-3]+(8,))),axis=-1)%3

def kinv(x):
    a=x[...,:2];b=x[...,2:6].reshape(x.shape[:-1]+(2,2));c=x[...,6:].reshape(x.shape[:-1]+(2,2,2))
    q=np.einsum('...i,...j->...ij',a,a)-b
    t=-c+np.einsum('...i,...jk->...ijk',a,b)+np.einsum('...ij,...k->...ijk',b,a)-np.einsum('...i,...j,...k->...ijk',a,a,a)
    return np.concatenate((-a,q.reshape(q.shape[:-2]+(4,)),t.reshape(t.shape[:-3]+(8,))),axis=-1)%3

def augmul(x,y):
    return (kmul(x,y)-x-y)%3

def auto_matrix(images):
    columns=[images[0],images[1]]
    for i in range(2):
        for j in range(2):columns.append(augmul(images[i],images[j]))
    for i in range(2):
        for j in range(2):
            for k in range(2):columns.append(augmul(augmul(images[i],images[j]),images[k]))
    return np.array(columns,dtype=np.int64).T

def inverse_matrix(A):
    n=A.shape[0];R=np.column_stack((A,np.eye(n,dtype=np.int64)))%3
    for j in range(n):
        k=j+int(np.flatnonzero(R[j:,j])[0]);R[[j,k]]=R[[k,j]]
        R[j]=R[j]*int(R[j,j])%3
        for k in range(n):
            if k!=j and R[k,j]:R[k]=(R[k]-R[k,j]*R[j])%3
    assert np.array_equal(R[:,:n],np.eye(n,dtype=np.int64))
    return R[:,n:]

class AutomorphismImage:
    def __init__(self):
        identity=np.zeros((2,14),dtype=np.int64);identity[0,0]=identity[1,1]=1
        x,y=identity
        ga=np.array([x,kmul(y,x)]);gb=np.array([kmul(x,kinv(y)),y])
        self.generating_images=[ga,gb]
        key=lambda z:bytes(np.asarray(z,dtype=np.uint8).ravel())
        self.key=key
        self.images=[identity];self.matrices=[np.eye(14,dtype=np.int64)]
        self.lookup={key(identity):0};self.parents=[None];self.cache={}
        at=0;right=[]
        while at<len(self.images):
            nexts=[]
            for letter,g in enumerate((ga,gb)):
                images=(self.matrices[at]@g.T).T%3;k=key(images)
                if k not in self.lookup:
                    self.lookup[k]=len(self.images);self.images.append(images)
                    self.matrices.append(auto_matrix(images));self.parents.append((at,letter))
                nxt=self.lookup[k];nexts.append(nxt);self.cache[(at,self.lookup[key(g)])]=nxt
            right.append(nexts);at+=1
            assert at<=100000,'Unexpectedly large finite automorphism image'
        self.images=np.array(self.images,dtype=np.int64)
        self.matrices=np.array(self.matrices,dtype=np.int64)
        self.right_generators=np.array(right,dtype=np.int64)
        self.a=self.lookup[key(ga)];self.b=self.lookup[key(gb)]
        inverse_generators=[]
        for gi in (self.a,self.b):
            Minv=inverse_matrix(self.matrices[gi]);inverse_generators.append(self.lookup[key(Minv[:,:2].T)])
        self.inverses=np.zeros(len(self.images),dtype=np.int64)
        for k,parent in enumerate(self.parents[1:],1):
            i,letter=parent;self.inverses[k]=self.compose(inverse_generators[letter],int(self.inverses[i]))
        for k in range(len(self.images)):
            assert self.compose(k,int(self.inverses[k]))==0
        assert self.compose(self.compose(self.a,self.b),self.a)==self.compose(self.compose(self.b,self.a),self.b)

    def compose(self,i,j):
        k=self.cache.get((i,j))
        if k is None:
            images=(self.matrices[i]@self.images[j].T).T%3
            k=self.lookup[self.key(images)];self.cache[(i,j)]=k
        return k

    def compose_many(self,ii,jj):
        ii,jj=np.broadcast_arrays(ii,jj)
        return np.array([self.compose(int(i),int(j)) for i,j in zip(ii.ravel(),jj.ravel())],dtype=np.int64).reshape(ii.shape)

class FerrariDegreeThree:
    def __init__(self):
        self.aut=AutomorphismImage()
        self.one=np.zeros(15,dtype=np.int64)
        self.a=self.one.copy();self.a[14]=self.aut.a
        self.b=self.one.copy();self.b[14]=self.aut.b
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
        expected=self.one.copy();expected[0]=1
        assert np.array_equal(self.xi1,expected)
        expected=self.one.copy();expected[1]=1
        assert np.array_equal(self.xi2,expected)
        assert np.array_equal(self.conj(self.a,self.xi1),self.xi1)
        assert np.array_equal(self.conj(self.a,self.xi2),self.mul(self.xi2,self.xi1))
        assert np.array_equal(self.conj(self.b,self.xi1),self.mul(self.xi1,self.inv(self.xi2)))
        assert np.array_equal(self.conj(self.b,self.xi2),self.xi2)
        self.kernel_aut_vectors={}
        identity=self.aut.images[0]
        for i,images in enumerate(self.aut.images):
            if np.array_equal(images[:,:2],identity[:,:2]):
                assert not np.any(images[:,2:6])
                self.kernel_aut_vectors[bytes(images[:,6:].astype(np.uint8).ravel())]=i

    def mul(self,x,y):
        ai=x[...,14];bi=y[...,14]
        acted=np.einsum('...ij,...j->...i',self.aut.matrices[ai],y[...,:14])%3
        vec=kmul(x[...,:14],acted)
        ci=self.aut.compose_many(ai,bi)
        return np.concatenate((vec,ci[...,None]),axis=-1)
    def inv(self,x):
        ai=self.aut.inverses[x[...,14]]
        vec=np.einsum('...ij,...j->...i',self.aut.matrices[ai],kinv(x[...,:14]))%3
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
        x,y=(self.x,self.y) if gens is None else gens
        images={1:x,-1:self.inv(x),2:y,-2:self.inv(y)}
        out=np.broadcast_to(self.one,x.shape).copy()
        for t in w:out=self.mul(out,images[t])
        return out
    def pentagon(self,vals):
        return self.mul(self.mul(vals[0],vals[1]),self.inv(self.mul(self.mul(vals[2],vals[3]),vals[4])))
    def braid_images(self,vals):
        return self.a,self.conj(self.inv(vals[4]),self.b),self.conj(self.inv(vals[5]),self.c)
    def check_braids(self,images):
        a,b,c=images
        assert np.array_equal(self.mul(self.mul(a,b),a),self.mul(self.mul(b,a),b))
        assert np.array_equal(self.mul(self.mul(b,c),b),self.mul(self.mul(c,b),c))
        assert np.array_equal(self.mul(a,c),self.mul(c,a))
    def project(self,x):
        images=self.aut.images[x[...,14]]
        matrix=np.swapaxes(images[...,:,:2],-1,-2).reshape(x.shape[:-1]+(4,))
        u=x[...,0];v=x[...,1];z=(x[...,3]-2*u*v-u-2*v)%3
        return np.concatenate((matrix,np.stack((u,v,z),axis=-1)),axis=-1)
    def kernel_vector(self,x):
        projected=self.project(x)
        assert np.array_equal(projected,np.broadcast_to(np.array([1,0,0,1,0,0,0]),projected.shape))
        assert not np.any(x[...,:6])
        images=self.aut.images[x[...,14]]
        assert not np.any(images[...,2:6])
        return np.concatenate((x[...,6:14],images[...,6:].reshape(x.shape[:-1]+(16,))),axis=-1)
    def kernel_element(self,v):
        result=np.zeros(v.shape[:-1]+(15,),dtype=np.int64);result[...,6:14]=v[...,:8]%3
        flats=v[...,8:].reshape(-1,16)%3
        indices=[self.kernel_aut_vectors[bytes(row.astype(np.uint8))] for row in flats]
        result[...,14]=np.array(indices,dtype=np.int64).reshape(v.shape[:-1])
        return result

def main():
    start=time.time();H=FerrariDegreeThree()
    import de_ferrari_class2_model as old
    for i,x in enumerate((H.a,H.b,H.c)):
        assert H.project(x).tolist()==list((old.a,old.b,old.c)[i])
    for pair,oldpair in zip(H.pairs,old.pairs):
        for a,b in zip(pair,oldpair):assert H.project(a).tolist()==list(b)
    # Enumerate the actual subgroup of truncated Magnus units, not the
    # whole ambient 14-dimensional associative algebra.
    x=H.xi1[:14];y=H.xi2[:14];zero=np.zeros(14,dtype=np.int64)
    seen={bytes(zero.astype(np.uint8))};queue=[zero]
    for element in queue:
        for gen in (x,y):
            value=kmul(element,gen);key=bytes(value.astype(np.uint8))
            if key not in seen:seen.add(key);queue.append(value)
    assert len(seen)==2187
    vectors=[]
    for element in queue:
        el=np.r_[element,0]
        assert np.array_equal(H.mul(el,H.inv(el)),H.one)
        if not np.any(element[:6]):vectors.append(element[6:])
    assert len(vectors)==81
    for i in H.kernel_aut_vectors.values():
        for j in H.kernel_aut_vectors.values():
            a=H.one.copy();a[14]=i;b=H.one.copy();b[14]=j
            assert np.array_equal(H.kernel_vector(H.mul(a,b)),(H.kernel_vector(a)+H.kernel_vector(b))%3)
    assert len(H.aut.images)%24==0
    kernel_order=len(H.kernel_aut_vectors)
    assert len(H.aut.images)==24*kernel_order
    output={'Ferrari_kernel_order':2187,
            'degree_three_Ferrari_kernel_order':81,
            'B3_automorphism_image_order':len(H.aut.images),
            'B3_automorphism_kernel_over_SL2_F3_order':kernel_order,
            'four_strand_target_order':2187*len(H.aut.images),
            'kernel_over_E18_order':81*kernel_order,
            'x_cubed_Magnus_coordinates':H.power(H.xi1,3)[:14].tolist(),
            'y_cubed_Magnus_coordinates':H.power(H.xi2,3)[:14].tolist(),
            'actual_Ferrari_action_and_braid_relations_verified':True,
            'reduction_equals_E18_on_all_evaluation_pairs':True,
            'elapsed_seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
    np.savez_compressed(Path(__file__).with_name('de_ferrari_degree3_model_certificate.npz'),
                         automorphism_images=H.aut.images,
                         automorphism_matrices=H.aut.matrices,
                         right_generator_permutations=H.aut.right_generators,
                         inverse_permutation=H.aut.inverses,
                         degree3_Ferrari_kernel_elements=np.array(vectors,dtype=np.int64))
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
