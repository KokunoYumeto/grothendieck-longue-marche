#!/usr/bin/env python3
"""Complete top-layer kernels over the exact degree-four Ferrari core.

The normal presentation uses all original generators, all selected
basis cubes/commutators, and every N-conjugation relation.  It computes
the full kernel and its F-prime intersection, including all power data.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np
from de_ferrari_degree4_lift import Combined as OldCombined,InducedCombined as OldInduced
from de_ferrari_mod9_lift import Jacobi,Span,free_abelianization
from de_ferrari_truncated_model import FerrariTruncated

here=Path(__file__).resolve().parent

class CombinedFive(OldCombined):
    def __init__(self):
        self.H9=Jacobi(9);self.H3=FerrariTruncated(5)
        self.one=np.r_[self.H9.one,self.H3.one]
        self.a=np.r_[self.H9.a,self.H3.a];self.b=np.r_[self.H9.b,self.H3.b];self.c=np.r_[self.H9.c,self.H3.c]
        self.x=np.column_stack((self.H9.x,self.H3.x));self.y=np.column_stack((self.H9.y,self.H3.y))
        self.pairs=tuple(zip(self.x,self.y));self.check_braids((self.a,self.b,self.c))
    def kernel_vector(self,x):
        assert np.array_equal(x[...,:7],np.broadcast_to(self.H9.one,x.shape[:-1]+(7,)))
        return self.H3.top_kernel_vector(x[...,7:])
    def kernel_element(self,v):
        return np.concatenate((np.broadcast_to(self.H9.one,v.shape[:-1]+(7,)),self.H3.top_kernel_element(v)),axis=-1)
    def to_old(self,x,old):
        images=self.H3.aut.images[x[...,-1],:,:30]
        indices=[old.H3.aut.register(im) for im in images.reshape(-1,2,30)]
        auto=np.array(indices,dtype=np.int64).reshape(x.shape[:-1])
        return np.concatenate((x[...,:7],x[...,7:37],auto[...,None]),axis=-1)
    def raw_kernel_vector(self,x):
        diff=(x[...,:7]-self.H9.one)%9;assert not np.any(diff%3)
        y=x[...,7:];assert not np.any(y[...,:6])
        images=self.H3.aut.images[y[...,-1]]
        expected=np.zeros(images.shape[:-1]+(6,),dtype=np.int16)
        expected[...,0,0]=expected[...,1,1]=1
        assert np.array_equal(images[...,:6],expected)
        return np.concatenate((diff//3,y[...,6:62],images[...,6:].reshape(x.shape[:-1]+(112,))),axis=-1)
    def raw_kernel_element(self,v):
        shape=v.shape[:-1];y=np.zeros(shape+(63,),dtype=np.int64);y[...,6:62]=v[...,7:63]%3
        indices=[]
        for delta in v[...,63:].reshape(-1,2,56)%3:
            images=np.zeros((2,62),dtype=np.int16);images[0,0]=images[1,1]=1;images[:,6:]=delta
            indices.append(self.H3.aut.register(images))
        y[...,-1]=np.array(indices,dtype=np.int64).reshape(shape)
        return np.concatenate(((self.H9.one+3*v[...,:7])%9,y),axis=-1)
    def log_kernel(self,x):
        v=self.raw_kernel_vector(x);cross=(self.raw_kernel_vector(self.mul(x,x))-2*v)%3
        return (v-2*cross)%3
    def exp_kernel(self,v):
        x=self.raw_kernel_element(v);cross=(self.raw_kernel_vector(self.mul(x,x))-2*v)%3
        return self.raw_kernel_element((v+2*cross)%3)
    def encode(self,x):
        assert x.ndim==1
        return {'mod9':x[:7].tolist(),'Magnus_unit':x[7:-1].tolist(),
                'automorphism_generator_images':self.H3.aut.images[int(x[-1])].tolist()}
    def decode(self,x):
        a=self.H3.aut.register(np.array(x['automorphism_generator_images'],dtype=np.int16))
        return np.r_[x['mod9'],x['Magnus_unit'],a].astype(np.int64)

class InducedFive(OldInduced):
    def __init__(self,H,d):
        self.chunks=None
        super().__init__(H,d)
    def vector(self,x):
        assert np.array_equal(x[0],self.id)
        return self.H.kernel_vector(x[1]).ravel()
    def element(self,v):return self.id,self.H.kernel_element(v.reshape(6,6,96))
    def word(self,w):
        if self.chunks is None:return super().word(w)
        out=self.one;i=0
        while i<len(w):
            node=self.chunks;j=i;best=None;stop=i
            while j<len(w) and w[j] in node:
                node=node[w[j]];j+=1
                if 'value' in node:best=node['value'];stop=j
            if best is None:best=self.letters[w[i]];stop=i+1
            out=self.mul(out,best);i=stop
        return out
    def install_chunks(self,chunks):
        self.chunks={}
        for word,value in chunks:
            node=self.chunks
            for letter in word:node=node.setdefault(letter,{})
            node['value']=value
    def log(self,x):
        assert np.array_equal(x[0],self.id)
        return self.H.log_kernel(x[1]).ravel()
    def exp(self,v):return self.id,self.H.exp_kernel(v.reshape(6,6,175))

def old_span(matrix,words):
    S=Span(matrix.shape[0])
    for v,w in zip(matrix.T,words):assert S.add(v,w)
    return S

def kernel_image(H,W,oldH,oldW,d,N,selected_words,old_matrix,prime):
    start=time.time();old=old_span(old_matrix,selected_words)
    selected=[W.word(w) for w in selected_words];r=len(selected)
    negative=[[W.power(g,-a) for a in range(3)] for g in selected]
    power6=[W.power(n,6) for n in N]
    S=Span(36*96);coordinate_cache={};counts={'original_generator_relations':0,
         'basis_cube_relations':0,'basis_commutator_relations':0,'conjugation_relations':0}
    def old_coordinates(element):
        old_element=(element[0],H.to_old(element[1],oldH))
        vector=oldW.vector(old_element);key=bytes(vector.astype(np.uint8))
        if key not in coordinate_cache:coordinate_cache[key]=old.coordinates(vector)
        return coordinate_cache[key]
    def relation(element,word_factory):
        coefficients=old_coordinates(element);residual=element
        for i,a in enumerate(coefficients):
            if a:residual=W.mul(residual,negative[i][int(a)])
        vector=W.vector(residual)
        if np.any(S.reduce(vector)[0]):
            word=list(word_factory())
            for i,a in enumerate(coefficients):
                if a:word+=d['bpower'](selected_words[i],-int(a))
            S.add(vector,word)
    for i in range(97):
        for j in range(i+1,97):
            relation(W.comm(N[i],N[j]),lambda i=i,j=j:
                     d['Nwords'][i]+d['Nwords'][j]+d['binv'](d['Nwords'][i])+d['binv'](d['Nwords'][j]))
            counts['original_generator_relations']+=1
    if prime:
        integer_kernel=np.load(here/'de_ferrari_mod9_module.npz')['integral_abelianization_kernel']
        for coeff in integer_kernel.T:
            element=W.one
            for i,a in enumerate(coeff):
                if a:element=W.mul(element,W.power(power6[i],int(a)))
            def source_word(coeff=coeff):
                ans=[]
                for i,a in enumerate(coeff):
                    if a:ans+=d['bpower'](d['Nwords'][i],6*int(a))
                return ans
            relation(element,source_word);counts['original_generator_relations']+=1
    else:
        for i,element in enumerate(power6):
            relation(element,lambda i=i:d['bpower'](d['Nwords'][i],6))
            counts['original_generator_relations']+=1
    for i in range(r):
        vector=W.vector(W.power(selected[i],3))
        S.add(vector,selected_words[i]*3);counts['basis_cube_relations']+=1
        for j in range(i+1,r):
            vector=W.vector(W.comm(selected[i],selected[j]))
            S.add(vector,selected_words[i]+selected_words[j]+d['binv'](selected_words[i])+d['binv'](selected_words[j]))
            counts['basis_commutator_relations']+=1
        for j,n in enumerate(N):
            relation(W.conj(n,selected[i]),lambda i=i,j=j:
                     d['Nwords'][j]+selected_words[i]+d['binv'](d['Nwords'][j]))
            counts['conjugation_relations']+=1
    at=0
    while at<len(S.basis):
        element=W.element(S.basis[at]);word=S.words[at]
        for j,n in enumerate(N):
            vector=W.vector(W.conj(n,element))
            if np.any(S.reduce(vector)[0]):S.add(vector,d['Nwords'][j]+word+d['binv'](d['Nwords'][j]))
        at+=1
    print(json.dumps({'prime':prime,'top_kernel_image_dimension':len(S.basis),
                      'normal_relator_counts':counts,'basis_word_lengths':[len(w) for w in S.words]}),flush=True)
    for i,(v,w) in enumerate(zip(S.basis,S.words)):
        assert np.array_equal(W.vector(W.word(w)),v)
        if prime:assert not np.any(free_abelianization(d['fword'](w)))
        for t in (0,1):S.coordinates(W.vector(W.conj(W.letters[t],W.element(v))))
    metadata={'prime':prime,'image_dimension':len(S.basis),'old_image_dimension':r,
              'normal_relator_counts':counts,'literal_basis_words_verified':True,
              's_and_r_stability_verified':True,'elapsed_seconds':round(time.time()-start,3)}
    print(json.dumps(metadata),flush=True)
    return S,metadata

def construct():
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    H=CombinedFive();W=InducedFive(H,d);oldH=OldCombined();oldW=OldInduced(oldH,d)
    N=[W.word(w) for w in d['Nwords']]
    chunks=[]
    for w,n in zip(d['Nwords'],N):chunks.extend(((w,n),(d['binv'](w),W.inv(n))))
    W.install_chunks(chunks)
    olddata=json.loads(here.joinpath('de_ferrari_degree4_module.json').read_text())
    oldcertificate=np.load(here/'de_ferrari_degree4_module.npz')
    prime,pmeta=kernel_image(H,W,oldH,oldW,d,N,
        olddata['literal_B_words_for_F_prime_basis'],oldcertificate['F_prime_correction_image_basis'],True)
    full,fmeta=kernel_image(H,W,oldH,oldW,d,N,
        olddata['full_kernel_basis_words'],oldcertificate['full_G6_kernel_image_basis'],False)
    for v in prime.basis:full.coordinates(v)
    output={'stage':'joint degree5 characteristic3 Ferrari / mod9 core above exact degree4 core',
            'F_prime_top_kernel':pmeta,'full_top_kernel':fmeta,
            'F_prime_basis_words':prime.words,'full_basis_words':full.words,
            'registered_exact_automorphisms':H.H3.aut.count,
            'complete_normal_presentation':True}
    here.joinpath('de_ferrari_degree5_kernel.json').write_text(json.dumps(output,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_degree5_kernel_certificate.npz',
                        F_prime_top_kernel_basis=prime.matrix(),full_top_kernel_basis=full.matrix())
    return d,H,W,oldH,oldW,prime,full,output

if __name__=='__main__':
    *_,output=construct()
    print(json.dumps({k:v for k,v in output.items() if 'basis_words' not in k},indent=2),flush=True)
